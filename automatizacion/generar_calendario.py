#!/usr/bin/env python3
"""Convierte pies-de-foto.txt en calendario.json siguiendo ORDEN.

Serie: 29 posts de imagen y 20 carruseles-guía, uno al día desde la fecha de inicio,
en el orden de ORDEN y a la hora que toca según el público y el día de la semana.

  python3 generar_calendario.py 2026-10-06        (o FECHA_INICIO=2026-10-06)
"""
import json, os, re, sys
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "pies-de-foto.txt"
DESTINO = Path(__file__).resolve().parent / "calendario.json"
DIAS_ES = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Horas (Europe/Madrid) por público y día. Sin datos de la cuenta todavía: son estimaciones
# para España. Quien entrena mira Instagram al salir de la clase de la tarde (21:30), el
# sábado tras el open mat (13:00) y el domingo por la tarde (20:30). Quien dirige un gimnasio
# da clase por la tarde: entre semana se le pilla a mediodía (14:00), el sábado a media mañana.
# Cuando la cuenta pase de 100 seguidores, medir_audiencia.py da las horas reales.
HORAS = {
    "alumno": ["21:30", "21:30", "21:30", "21:30", "21:30", "13:00", "20:30"],
    "centro": ["14:00", "14:00", "14:00", "14:00", "14:00", "10:30", "20:30"],
    "marca":  ["21:30", "21:30", "21:30", "21:30", "21:30", "13:00", "20:30"],
}

# El orden: primero qué es y cómo se entra; luego el día a día (clases y asistencia), el
# dinero, el atleta (sparring, cuerpo, ranking, perfil), el coach (parte y seguimiento) y la
# gestión fina (miembros, permisos, ajustes). Un post suelto presenta una idea y la guía de
# al lado la enseña paso a paso. Los cierres de marca caen en domingo; el primero abre la serie.
ORDEN = [
    ("dia-07", "marca"),
    ("dia-22", "alumno"), ("guia-alumno", "alumno"),
    ("dia-23", "centro"), ("guia-club", "centro"),
    ("dia-14", "marca"),
    ("dia-02", "centro"), ("dia-01", "alumno"), ("guia-clases", "alumno"),
    ("dia-04", "centro"), ("guia-asistencia", "centro"),
    ("dia-03", "alumno"), ("guia-hoy", "alumno"),
    ("dia-06", "centro"), ("dia-24", "alumno"), ("guia-cobrar", "centro"),
    ("dia-11", "centro"), ("guia-tienda", "alumno"),
    ("dia-26", "alumno"), ("dia-21", "marca"),
    ("dia-08", "alumno"), ("guia-juego", "alumno"), ("dia-29", "alumno"),
    ("dia-10", "alumno"), ("guia-lesion", "alumno"), ("guia-peso", "alumno"),
    ("dia-05", "alumno"),
    ("dia-16", "centro"), ("guia-parte", "centro"), ("guia-seguimiento", "centro"),
    ("dia-17", "alumno"), ("dia-12", "alumno"), ("dia-15", "alumno"), ("guia-perfil", "alumno"),
    ("dia-13", "centro"), ("guia-miembros", "centro"),
    ("dia-20", "centro"), ("dia-25", "centro"), ("guia-invitar", "centro"),
    ("dia-18", "centro"), ("guia-chat", "alumno"),
    ("guia-permisos", "centro"), ("dia-19", "alumno"), ("dia-09", "centro"),
    ("dia-27", "centro"), ("guia-centro", "centro"), ("guia-ajustes-alumno", "alumno"),
    ("dia-28", "marca"),
    ("guia-ajustes-centro", "centro"),
]


def campo(cuerpo, nombre):
    m = re.search(rf"^{nombre}:\s*(.+)$", cuerpo, re.MULTILINE)
    return m.group(1).strip() if m else None


def leer_inicio():
    crudo = (sys.argv[1] if len(sys.argv) > 1 else "") or os.environ.get("FECHA_INICIO", "")
    if not crudo:
        raise SystemExit("indica la fecha de inicio: python3 generar_calendario.py AAAA-MM-DD")
    try:
        return date.fromisoformat(crudo.strip())
    except ValueError:
        raise SystemExit(f"fecha no valida: {crudo!r} — usa el formato AAAA-MM-DD")


def leer_piezas():
    texto = FUENTE.read_text(encoding="utf-8")
    piezas = {}
    for m in re.finditer(r"^D[ÍI]A\s+(\d+)\s*·\s*(.+?)$([\s\S]*?)(?=^D[ÍI]A\s|^CARRUSEL|\Z)", texto, re.MULTILINE):
        numero, cuerpo = int(m.group(1)), m.group(3)
        archivo = re.sub(r"\s*\(.*\)$", "", campo(cuerpo, "Archivo") or "")
        pie, tags = campo(cuerpo, "Pie"), campo(cuerpo, "Tags") or ""
        if not (archivo and pie):
            raise SystemExit(f"DIA {numero}: falta Archivo o Pie")
        piezas[f"dia-{numero:02d}"] = {"tipo": "imagen", "archivos": [f"jpg/{archivo[:-4]}.jpg"],
                                       "caption": f"{pie}\n\n{tags}".strip()}
    for m in re.finditer(r"^CARRUSEL\s*·\s*(.+?)$([\s\S]*?)(?=^CARRUSEL\s|^D[ÍI]A\s|\Z)", texto, re.MULTILINE):
        cuerpo = m.group(2)
        pid, pie, tags = campo(cuerpo, "Id"), campo(cuerpo, "Pie"), campo(cuerpo, "Tags") or ""
        if not (pid and pie):
            raise SystemExit(f"carrusel sin Id o sin Pie: {m.group(1)}")
        archivos = sorted((RAIZ / "jpg" / pid).glob("*.jpg"))
        piezas[pid] = {"tipo": "carrusel", "archivos": [f"jpg/{pid}/{a.name}" for a in archivos],
                       "caption": f"{pie}\n\n{tags}".strip()}
    return piezas


def construir(inicio, piezas):
    posts = []
    for i, (pid, publico) in enumerate(ORDEN):
        if pid not in piezas:
            raise SystemExit(f"{pid} está en ORDEN pero no en pies-de-foto.txt")
        dia = inicio + timedelta(days=i)
        p = {"id": pid, "orden": i + 1, "fecha": dia.isoformat(), "dia_semana": DIAS_ES[dia.weekday()],
             "hora": HORAS[publico][dia.weekday()], "audiencia": publico, **piezas[pid]}
        if p["tipo"] == "imagen":
            p["archivo"] = p["archivos"][0]
        posts.append(p)
    return posts


def validar(posts, piezas):
    errores = []
    ids = [p["id"] for p in posts]
    if len(set(ids)) != len(ids):
        errores.append("hay ids repetidos en ORDEN")
    for pid in sorted(set(piezas) - set(ids)):
        errores.append(f"{pid} está en pies-de-foto.txt pero no en ORDEN")
    for p in posts:
        if p["tipo"] == "carrusel" and not (2 <= len(p["archivos"]) <= 10):
            errores.append(f"{p['id']}: carrusel con {len(p['archivos'])} fotos (Instagram: 2-10)")
        for a in p["archivos"]:
            if not (RAIZ / a).exists():
                errores.append(f"{p['id']}: no existe {a}")
        if len(p["caption"]) > 2200:
            errores.append(f"{p['id']}: caption de {len(p['caption'])} caracteres (limite 2200)")
    return errores


if __name__ == "__main__":
    inicio = leer_inicio()
    piezas = leer_piezas()
    posts = construir(inicio, piezas)
    errores = validar(posts, piezas)
    DESTINO.write_text(json.dumps(posts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(posts)} publicaciones -> {DESTINO.name}, del {posts[0]['fecha']} al {posts[-1]['fecha']}")
    for p in posts:
        extra = f" · {len(p['archivos'])} fotos" if p["tipo"] == "carrusel" else ""
        print(f"  {p['fecha']} {p['dia_semana']:9s} {p['hora']}  {p['audiencia']:6s} {p['id']}{extra}")
    if errores:
        print("\nAVISOS:")
        for e in errores:
            print(f"  - {e}")
        raise SystemExit(1)
    print("validacion OK")
