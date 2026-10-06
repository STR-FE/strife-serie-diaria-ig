#!/usr/bin/env python3
"""Publica en Instagram el post de hoy, segun calendario.json, en cuanto llega su hora.

El workflow lo ejecuta cada 15 minutos: si hoy hay post, ya es su hora (Europe/Madrid) y no
consta en el registro, lo publica. Un dia que se paso sin publicar no se recupera al dia siguiente.

Imagen suelta: contenedor de medios y publicar. Carrusel: un contenedor por foto
(is_carousel_item), un contenedor CAROUSEL con los hijos, y publicar.
Lleva un registro para no publicar dos veces el mismo dia.

Usa "Instagram API con Instagram Login": host graph.instagram.com, no requiere
pagina de Facebook. Permisos: instagram_business_basic + instagram_business_content_publish.

Variables de entorno necesarias:
  IG_ACCESS_TOKEN   token de larga duracion (60 dias) del panel de la app
  IMAGE_BASE_URL    URL publica HTTPS donde estan las imagenes, sin barra final
  IG_USER_ID        opcional; por defecto "me", que el token ya identifica
  GRAPH_VERSION     opcional, por defecto v25.0
  GRAPH_HOST        opcional, por defecto graph.instagram.com
"""
import argparse, json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CALENDARIO = AQUI / "calendario.json"
REGISTRO = AQUI / "registro.json"
MADRID = ZoneInfo("Europe/Madrid")


def api(metodo, ruta, datos=None):
    host = os.environ.get("GRAPH_HOST", "graph.instagram.com")
    version = os.environ.get("GRAPH_VERSION", "v25.0")
    url = f"https://{host}/{version}/{ruta}"
    cuerpo = None
    if metodo == "POST":
        cuerpo = urllib.parse.urlencode(datos).encode()
    else:
        url += "?" + urllib.parse.urlencode(datos)
    peticion = urllib.request.Request(url, data=cuerpo, method=metodo)
    try:
        with urllib.request.urlopen(peticion, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", "replace")
        raise SystemExit(f"error de la Graph API ({e.code}) en {metodo} {ruta}:\n{detalle}")


def cargar_registro():
    return json.loads(REGISTRO.read_text()) if REGISTRO.exists() else {}


def guardar_registro(registro):
    REGISTRO.write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def esperar(contenedor, token, etiqueta="contenedor"):
    for _ in range(20):
        estado = api("GET", contenedor, {"fields": "status_code,status", "access_token": token})
        codigo = estado.get("status_code")
        if codigo == "FINISHED":
            return
        if codigo == "ERROR":
            raise SystemExit(f"  Instagram no pudo procesar el {etiqueta}: {estado.get('status')}")
        print(f"  esperando {etiqueta} ({codigo}) ...")
        time.sleep(5)
    raise SystemExit(f"  el {etiqueta} no llego a FINISHED en 100 segundos")


def publicar(post, ensayo):
    ig_user = os.environ.get("IG_USER_ID") or "me"
    token = os.environ.get("IG_ACCESS_TOKEN")
    base = (os.environ.get("IMAGE_BASE_URL") or "").rstrip("/")
    faltan = [n for n, v in [("IG_ACCESS_TOKEN", token), ("IMAGE_BASE_URL", base)] if not v]
    if faltan and not ensayo:
        raise SystemExit("faltan variables de entorno: " + ", ".join(faltan))

    archivos = post.get("archivos") or [post["archivo"]]
    urls = [f"{base}/{urllib.parse.quote(a)}" for a in archivos]
    tipo = post.get("tipo", "imagen")
    print(f"{post['id']} · {post['fecha']} {post['hora']} ({post['dia_semana']}) · {post['audiencia']} · {tipo}")
    for u in urls:
        print(f"  imagen : {u}")
    print(f"  caption: {post['caption'][:80]}{'...' if len(post['caption']) > 80 else ''}")

    if ensayo:
        print("  [ensayo] no se publica nada")
        return None

    if tipo == "carrusel":
        hijos = []
        for u in urls:
            hijo = api("POST", f"{ig_user}/media", {
                "image_url": u, "is_carousel_item": "true", "access_token": token,
            })["id"]
            esperar(hijo, token, "hijo del carrusel")
            hijos.append(hijo)
            print(f"  hijo listo: {hijo}")
        contenedor = api("POST", f"{ig_user}/media", {
            "media_type": "CAROUSEL", "children": ",".join(hijos),
            "caption": post["caption"], "access_token": token,
        })["id"]
    else:
        contenedor = api("POST", f"{ig_user}/media", {
            "image_url": urls[0], "caption": post["caption"], "access_token": token,
        })["id"]
    print(f"  contenedor creado: {contenedor}")
    esperar(contenedor, token)

    publicado = api("POST", f"{ig_user}/media_publish", {
        "creation_id": contenedor, "access_token": token,
    })["id"]
    print(f"  PUBLICADO. id del post: {publicado}")
    return publicado


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fecha", help="AAAA-MM-DD; por defecto hoy en Europe/Madrid")
    p.add_argument("--orden", type=int, help="publicar la publicacion n de la serie (1-49), sin mirar la hora")
    p.add_argument("--id", dest="post_id", help="publicar por id (p. ej. guia-clases, dia-07), sin mirar la hora")
    p.add_argument("--dry-run", action="store_true", help="ensayo: muestra que haria sin publicar")
    p.add_argument("--force", action="store_true", help="publicar aunque ya conste en el registro")
    args = p.parse_args()

    posts = json.loads(CALENDARIO.read_text(encoding="utf-8"))
    if args.post_id:
        elegidos = [x for x in posts if x["id"] == args.post_id]
        if not elegidos:
            raise SystemExit(f"no existe el id {args.post_id}")
    elif args.orden:
        elegidos = [x for x in posts if x["orden"] == args.orden]
    else:
        ahora = datetime.now(MADRID)
        fecha = args.fecha or ahora.date().isoformat()
        elegidos = [x for x in posts if x["fecha"] == fecha]
        if not elegidos:
            print(f"{fecha}: no hay post programado para hoy. Nada que hacer.")
            return 0
        if not args.fecha and ahora.strftime("%H:%M") < elegidos[0]["hora"] and not args.dry_run:
            print(f"{fecha}: {elegidos[0]['id']} sale a las {elegidos[0]['hora']} (ahora {ahora:%H:%M}). Todavia no.")
            return 0

    post = elegidos[0]
    registro = cargar_registro()
    clave = post["id"]
    if clave in registro and not args.force:
        print(f"{post['id']} ya se publico el {registro[clave]['publicado_en']} "
              f"(id {registro[clave]['post_id']}). Nada que hacer.")
        return 0

    post_id = publicar(post, args.dry_run)
    if post_id:
        registro[clave] = {
            "fecha_programada": post["fecha"],
            "archivos": post.get("archivos") or [post["archivo"]],
            "post_id": post_id,
            "publicado_en": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        guardar_registro(registro)
    return 0


if __name__ == "__main__":
    sys.exit(main())
