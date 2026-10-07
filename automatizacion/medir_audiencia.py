#!/usr/bin/env python3
"""Mide con datos reales de la cuenta cuando publicar.

1. online_followers: a que hora estan conectados TUS seguidores (histograma
   por hora, ultimos 30 dias). Instagram exige 100+ seguidores para servirlo.
2. rendimiento por publicacion: alcance y likes de cada post ya publicado,
   cruzado con su hora, para ver que franjas funcionan.

Nota: en la via "Instagram Login" no esta documentado un permiso de insights
aparte; si la llamada falla por permisos, el dato de horas no esta disponible en
esta via y habria que medirlo desde la app de Instagram (Perfil > Estadisticas).

Uso:  IG_ACCESS_TOKEN=... python3 medir_audiencia.py
Si las franjas reales contradicen las HORAS de generar_calendario.py,
cambia HORAS y el cron de .github/workflows/publicar-instagram.yml.
"""
import json, os, urllib.parse, urllib.request
from collections import Counter
from pathlib import Path

HOST = os.environ.get("GRAPH_HOST", "graph.instagram.com")
VERSION = os.environ.get("GRAPH_VERSION", "v25.0")


def api(ruta, datos):
    url = f"https://{HOST}/{VERSION}/{ruta}?" + urllib.parse.urlencode(datos)
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"error": json.loads(e.read().decode("utf-8", "replace")).get("error", {})}

COMUNES = ["reach", "views", "likes", "comments", "saved", "shares", "total_interactions"]
EXTRA = {
    "REELS": ["ig_reels_avg_watch_time", "ig_reels_video_view_total_time"],
    "STORY": ["replies", "navigation", "follows", "profile_visits"],
    "FEED": ["follows", "profile_visits"],
}
CUENTA = ["reach", "views", "profile_views", "accounts_engaged", "total_interactions",
          "likes", "comments", "saves", "shares", "replies", "follows_and_unfollows"]


def valor(d):
    """Un insight llega como values[0].value o como total_value.value."""
    if "total_value" in d:
        return d["total_value"].get("value")
    vals = d.get("values") or [{}]
    return vals[0].get("value")


def metricas(objeto, nombres, token, extra=None):
    """Una llamada por metrica: si una no existe para ese tipo de pieza, la API
    rechaza TODA la peticion, asi que se piden sueltas y se anotan los errores."""
    salida, errores = {}, {}
    for m in nombres:
        r = api(f"{objeto}/insights", {"metric": m, "access_token": token, **(extra or {})})
        if "error" in r:
            errores[m] = r["error"].get("message", "error")
        else:
            for d in r.get("data", []):
                salida[d["name"]] = valor(d)
    return salida, errores


def cuenta(ig_user, token):
    print("== Cuenta ==")
    r = api(ig_user, {"fields": "username,followers_count,follows_count,media_count", "access_token": token})
    if "error" in r:
        print(f"  sin datos: {r['error'].get('message')}")
    else:
        print("  " + " · ".join(f"{k} {v}" for k, v in r.items() if k != "id"))
    print("\n== Cuenta: ultimos 30 dias (total) ==")
    datos, errores = metricas(f"{ig_user}", CUENTA, token, {"metric_type": "total_value", "period": "day"})
    for k, v in datos.items():
        print(f"  {k}: {v}")
    for k, m in errores.items():
        print(f"  ({k} no disponible: {m[:90]})")


def piezas(ig_user, token):
    print("\n== Todas las publicaciones de la cuenta ==")
    r = api(f"{ig_user}/media", {"fields": "id,media_type,media_product_type,timestamp,permalink,caption",
                                   "limit": 50, "access_token": token})
    if "error" in r:
        print(f"  sin datos: {r['error'].get('message')}")
        return
    media = r.get("data", [])
    s = api(f"{ig_user}/stories", {"fields": "id,media_type,media_product_type,timestamp,permalink", "access_token": token})
    historias = s.get("data", []) if "error" not in s else []
    print(f"  {len(media)} en el feed/reels · {len(historias)} estados activos (24 h)")
    avisados = set()
    for m in media + historias:
        tipo = m.get("media_product_type", "FEED")
        legible = {"REELS": "reel", "STORY": "estado", "FEED": m.get("media_type", "post").lower()}.get(tipo, tipo)
        titulo = (m.get("caption") or "").replace("\n", " ")[:50]
        print(f"\n  [{legible}] {m.get('timestamp', '')[:16]} {m.get('permalink', '')}")
        if titulo:
            print(f"    «{titulo}»")
        datos, errores = metricas(m["id"], COMUNES + EXTRA.get(tipo, EXTRA["FEED"]), token)
        print("    " + (" · ".join(f"{k} {v}" for k, v in datos.items()) or "sin metricas"))
        for k, msg in errores.items():
            if (tipo, k) not in avisados:
                avisados.add((tipo, k))
                print(f"    ({k} no disponible en {legible}: {msg[:90]})")


def main():
    ig_user = os.environ.get("IG_USER_ID") or "me"
    token = os.environ.get("IG_ACCESS_TOKEN")
    if not token:
        raise SystemExit("exporta IG_ACCESS_TOKEN")

    cuenta(ig_user, token)
    piezas(ig_user, token)

    print("\n== ¿A qué hora están conectados tus seguidores? (UTC) ==")
    r = api(f"{ig_user}/insights", {"metric": "online_followers", "period": "lifetime", "access_token": token})
    if "error" in r:
        print(f"  sin datos todavía: {r['error'].get('message', r['error'])}")
        print("  (Instagram lo sirve a partir de ~100 seguidores)")
    else:
        horas = Counter()
        for serie in r.get("data", []):
            for punto in serie.get("values", []):
                for h, n in (punto.get("value") or {}).items():
                    horas[int(h)] += n
        if horas:
            tope = max(horas.values())
            for h in range(24):
                n = horas.get(h, 0)
                print(f"  {h:02d}h UTC ({(h + 2) % 24:02d}h Madrid) {'█' * int(n / tope * 40):40s} {n}")
            mejores = [f"{(h + 2) % 24:02d}h Madrid" for h, _ in horas.most_common(3)]
            print(f"  mejores franjas: {', '.join(mejores)}")

    print("\n== Rendimiento de lo ya publicado ==")
    registro = Path(__file__).resolve().parent / "registro.json"
    if not registro.exists():
        print("  aún no hay publicaciones registradas")
        return
    for clave, fila in json.loads(registro.read_text()).items():
        m = api(f"{fila['post_id']}/insights", {"metric": "reach,likes,saved,shares", "access_token": token})
        if "error" in m:
            print(f"  {clave}: {m['error'].get('message', 'sin metricas')}")
            continue
        valores = {d["name"]: d["values"][0]["value"] for d in m.get("data", [])}
        print(f"  {clave} ({fila['fecha_programada']}): " + " · ".join(f"{k} {v}" for k, v in valores.items()))


if __name__ == "__main__":
    main()
