import os, shutil, subprocess, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
MKT = os.path.expanduser('~/StudioProjects/strife-marketing')
CAPS = os.path.join(MKT, 'serie-v2', 'capturas')
ART = os.path.join(MKT, 'reel', 'public')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SHOT_TOP, SHOT_BOTTOM = 63, 2223

HEAD = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  @font-face { font-family:'Anton'; src:url('fonts/anton.woff2') format('woff2'); }
  @font-face { font-family:'JetBrains Mono'; font-weight:700; src:url('fonts/jbmono-bold.woff2') format('woff2'); }
  @font-face { font-family:'Inter'; src:url('fonts/inter-regular.woff2') format('woff2'); }
  * { margin:0; padding:0; box-sizing:border-box; }
  html,body { width:1080px; height:%(h)dpx; overflow:hidden; }
  body {
    position:relative; font-family:'Inter',sans-serif;
    background: radial-gradient(ellipse 900px 500px at 15%% 100%%, rgba(120,45,15,0.35), transparent 60%%), #0b0c0e;
  }
  .header { position:absolute; top:70px; left:72px; right:72px; display:flex; justify-content:space-between; }
  .label { font-family:'JetBrains Mono',monospace; font-weight:700; font-size:28px; letter-spacing:0.18em; color:#e2571e; }
  .counter { font-family:'JetBrains Mono',monospace; font-weight:700; font-size:26px; letter-spacing:0.1em; color:#5f6064; }
  .title-row { position:absolute; top:158px; left:68px; right:68px; display:flex; align-items:flex-end; gap:14px; }
  .num { font-family:'Anton',sans-serif; font-size:132px; line-height:0.78; color:#e2571e; }
  .txt { font-family:'Anton',sans-serif; font-size:58px; line-height:0.95; color:#fff; text-transform:uppercase; padding-bottom:10px; }
  .subtitle { position:absolute; top:300px; left:72px; width:940px; font-size:29px; line-height:1.35; color:#a2a2a3; }
  .phone { position:absolute; left:320px; top:386px; width:440px; height:946px; border-radius:60px; overflow:hidden; background:#000; }
  .phone .bar { height:66px; background:#000; position:relative; }
  .phone .bar .time { position:absolute; left:26px; top:16px; font-weight:700; font-size:26px; color:#fff; }
  .phone .bar .icons { position:absolute; right:24px; top:20px; display:flex; gap:8px; }
  .phone img { width:100%%; height:calc(100%% - 66px); object-fit:cover; object-position:top center; display:block; }
  .logo { position:absolute; left:72px; bottom:56px; font-family:'Anton',sans-serif; font-size:38px; color:#fff; }
  .logo span, .o { color:#e2571e; }
  .big { position:absolute; left:68px; top:%(big_top)dpx; font-family:'Anton',sans-serif; font-size:150px; line-height:0.93; color:#fff; text-transform:uppercase; }
  .lead { position:absolute; left:72px; top:%(lead_top)dpx; width:880px; font-size:32px; line-height:1.4; color:#a2a2a3; }
  .mono { position:absolute; left:72px; font-family:'JetBrains Mono',monospace; font-weight:700; font-size:24px; letter-spacing:0.14em; color:#e2571e; }
  .art { position:absolute; opacity:0.30; }
  .wordmark { position:absolute; left:0; right:0; text-align:center; font-family:'Anton',sans-serif; font-size:190px; line-height:1; color:#fff; letter-spacing:0.01em; }
  .tagline { position:absolute; left:0; right:0; text-align:center; font-family:'JetBrains Mono',monospace; font-weight:700; font-size:30px; letter-spacing:0.2em; color:#e8e8e8; }
  .sub2 { position:absolute; left:0; right:0; text-align:center; font-size:30px; color:#a2a2a3; }
</style>
</head>
<body>
"""

ICONS = """<div class="icons">
<svg width="30" height="20" viewBox="0 0 30 20"><rect x="0" y="12" width="5" height="8" rx="1" fill="white"/><rect x="7" y="9" width="5" height="11" rx="1" fill="white"/><rect x="14" y="5" width="5" height="15" rx="1" fill="white"/><rect x="21" y="1" width="5" height="19" rx="1" fill="white"/></svg>
<svg width="24" height="18" viewBox="0 0 24 18"><path d="M12 16.5C13 16.5 13.8 15.7 13.8 14.7C13.8 13.7 13 12.9 12 12.9C11 12.9 10.2 13.7 10.2 14.7C10.2 15.7 11 16.5 12 16.5Z" fill="white"/><path d="M12 9C14.5 9 16.8 10 18.5 11.6L16.6 13.6C15.4 12.5 13.8 11.8 12 11.8C10.2 11.8 8.6 12.5 7.4 13.6L5.5 11.6C7.2 10 9.5 9 12 9Z" fill="white"/><path d="M12 2C16.7 2 21 3.9 24 7L22.1 9C19.5 6.5 15.9 5 12 5C8.1 5 4.5 6.5 1.9 9L0 7C3 3.9 7.3 2 12 2Z" fill="white"/></svg>
<svg width="42" height="20" viewBox="0 0 42 20" fill="none"><rect x="1" y="1" width="34" height="18" rx="4" stroke="white" stroke-width="1.5"/><rect x="3.5" y="3.5" width="29" height="13" rx="2" fill="white"/><rect x="37" y="7" width="3" height="6" rx="1.5" fill="white"/></svg>
</div>"""

FOOTER = 'YA EN GOOGLE PLAY'

GUIAS = {
    'guia-alumno': dict(label='GUÍA · TU PRIMER DÍA', slides=[
        dict(name='01-portada', cover=('TU PRIMER', 'DÍA.'),
             lead='Cuenta, perfil, rol y plaza pedida en tu gimnasio. Desliza: cada foto es un paso.'),
        dict(name='02-paso-1-crea-tu-cuenta', num='01', title='CREA TU CUENTA', cap='22_03_crear_cuenta',
             sub='Con Google o con email. Entrar no cuesta nada: para quien entrena, STRIFE es gratis.'),
        dict(name='03-paso-2-completa-tu-perfil', num='02', title='COMPLETA TU PERFIL', cap='22_04_perfil',
             sub='Nombre y @usuario, para que tus compañeros te reconozcan en el tatami.'),
        dict(name='04-paso-3-di-quien-eres', num='03', title='DI QUIÉN ERES', cap='22_05_rol_atleta',
             sub='Atleta si entrenas. Si además das clase o llevas un gimnasio, se añade luego.'),
        dict(name='05-paso-4-busca-tu-gimnasio', num='04', title='BUSCA TU GIMNASIO', cap='22_09_centro_en_mapa',
             sub='Por nombre o en el mapa. Y si tu centro te invitó, la invitación ya te espera.'),
        dict(name='06-paso-5-pide-plaza', num='05', title='PIDE PLAZA', cap='22_12_sin_centro_esperando',
             sub='Tu centro aprueba la solicitud. Mientras, la app ya es tuya.'),
        dict(name='07-paso-6-ya-estas-dentro', num='06', title='YA ESTÁS DENTRO', cap='22_13_te_han_aceptado',
             sub='Te avisa en cuanto te aceptan: horario, reservas y el chat de tu centro.'),
        dict(name='08-cierre', close=('NOS VEMOS', 'EN EL TATAMI.'),
             lead='Reserva tu primera clase y ficha con el QR al entrar. Gratis para quien entrena.'),
    ]),
    'guia-club': dict(label='GUÍA · ABRE TU CENTRO', slides=[
        dict(name='01-portada', cover=('ABRE TU', 'CENTRO.'),
             lead='Cuenta, rol, centro, disciplinas y solicitud enviada. Desliza: cada foto es un paso.'),
        dict(name='02-paso-1-crea-tu-cuenta', num='01', title='CREA TU CUENTA', cap='22_03_crear_cuenta',
             sub='La misma cuenta sirve para entrenar y para dirigir.'),
        dict(name='03-paso-2-di-quien-eres', num='02', title='DI QUIÉN ERES', cap='23_01_rol_admin',
             sub='Administrador para llevar el centro. Entrenador también, si das clase.'),
        dict(name='04-paso-3-datos-del-centro', num='03', title='DATOS DEL CENTRO', cap='23_02_crea_tu_centro',
             sub='Nombre, emblema y dirección en el mapa. Una pantalla.'),
        dict(name='05-paso-4-tus-disciplinas', num='04', title='TUS DISCIPLINAS', cap='23_03_disciplinas',
             sub='Boxeo, muay thai, MMA, karate… Marca lo que se entrena y cuáles llevan cinturón.'),
        dict(name='06-paso-5-quien-entra', num='05', title='QUIÉN ENTRA', cap='23_04_politica_admision',
             sub='Abierto, bajo solicitud, solo con invitación o secreto. Tú decides la puerta.'),
        dict(name='07-paso-6-pide-el-alta', num='06', title='PIDE EL ALTA', cap='23_05_pide_el_alta',
             sub='Tres datos para el revisor: tu papel, desde cuándo abres y cuántos sois.'),
        dict(name='08-paso-7-revisa-y-envia', num='07', title='REVISA Y ENVÍA', cap='23_06_revisar_y_enviar',
             sub='Un vistazo final y listo. Un revisor lo aprueba en minutos.'),
        dict(name='09-paso-8-tu-centro-ya-existe', num='08', title='TU CENTRO YA EXISTE', cap='23_07_tu_centro_ya_existe',
             sub='Eres su admin desde ya, con 30 días de prueba gratis.'),
        dict(name='10-cierre', close=('TU CENTRO,', 'EN MARCHA.'),
             lead='Monta el horario e invita a tu gente. Después, 14,99 €/mes con todo dentro.'),
    ]),
}

CIERRES = [
    dict(n=7, slug='cierre-semana-1', art='hares', tagline='YA EN GOOGLE PLAY', sub='La app de tu gimnasio de deportes de contacto.'),
    dict(n=14, slug='cierre-semana-2', art='flamingo', tagline='GRATIS PARA QUIEN ENTRENA', sub='Descárgala y busca tu gimnasio.'),
    dict(n=21, slug='cierre-semana-3', art='hares', flip=True, tagline='30 DÍAS GRATIS PARA TU CENTRO', sub='Horario, QR, cuotas, tienda y seguimiento.'),
    dict(n=28, slug='cierre-semana-4', art='flamingo', flip=True, tagline='14,99 € / MES · TODO DENTRO', sub='Atletas y coaches, gratis siempre. Ya en Google Play.'),
]


def render(page, out, h):
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
           f'--window-size=1080,{h}', f'--screenshot={out}', 'file://' + page]
    for intento in range(3):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=60)
            return
        except subprocess.TimeoutExpired:
            subprocess.run(['pkill', '-f', page])
    raise SystemExit(f'Chrome no termina con {page}')


def shot(cap):
    os.makedirs(os.path.join(REPO, 'capturas-app', 'v2'), exist_ok=True)
    dst = os.path.join(REPO, 'capturas-app', 'v2', cap + '.png')
    Image.open(os.path.join(CAPS, cap + '.png')).convert('RGB').crop((0, SHOT_TOP, 1080, SHOT_BOTTOM)).save(dst)
    return f'../capturas-app/v2/{cap}.png'


def guia_slide(label, i, total, s):
    head = HEAD % dict(h=1350, big_top=470, lead_top=820)
    counter = f'{i:02d} / {total:02d}'
    top = f'<div class="header"><div class="label">{label}</div><div class="counter">{counter}</div></div>'
    if 'cover' in s or 'close' in s:
        l1, l2 = s.get('cover') or s.get('close')
        body = top + f'<div class="big">{l1}<br><span class="o">{l2}</span></div><div class="lead">{s["lead"]}</div>'
        body += '<div class="mono" style="top:1130px">' + ('DESLIZA →' if 'cover' in s else FOOTER) + '</div>'
    else:
        body = top + f'<div class="title-row"><div class="num">{s["num"]}</div><div class="txt">{s["title"]}</div></div>'
        body += f'<div class="subtitle">{s["sub"]}</div>'
        body += f'<div class="phone"><div class="bar"><div class="time">9:41</div>{ICONS}</div><img src="{shot(s["cap"])}"></div>'
    return head + body + '<div class="logo">STR<span>/</span>FE</div>\n</body>\n</html>\n'


def cierre(c):
    head = HEAD % dict(h=1080, big_top=0, lead_top=0)
    if c['art'] == 'hares':
        art = f'<img class="art" src="{ART}/hares_transparent_bg.png" style="left:28px; top:-10px; width:1024px; opacity:0.42">'
    else:
        art = f'<img class="art" src="{ART}/flamingo_snake_transparent_bg.png" style="left:250px; top:-150px; width:580px; opacity:0.42">'
    if c.get('flip'):
        art = art.replace('style="', 'style="transform:scaleX(-1); ')
    body = art + '<div class="header"><div class="label">LA APP</div>'
    body += '<div class="counter"></div></div>'
    body += '<div class="wordmark" style="top:600px">STR<span class="o">/</span>FE</div>'
    body += f'<div class="tagline" style="top:830px">{c["tagline"]}</div>'
    body += f'<div class="sub2" style="top:895px">{c["sub"]}</div>'
    return head + body + '\n</body>\n</html>\n'


def main(what):
    if 'guias' in what:
        for gid, g in GUIAS.items():
            png_dir, jpg_dir = os.path.join(REPO, gid), os.path.join(REPO, 'jpg', gid)
            for d in (png_dir, jpg_dir):
                shutil.rmtree(d, ignore_errors=True)
                os.makedirs(d)
            total = len(g['slides'])
            for i, s in enumerate(g['slides'], 1):
                page = os.path.join(BASE, f'{gid}-{i:02d}.html')
                open(page, 'w').write(guia_slide(g['label'], i, total, s))
                out = os.path.join(BASE, 'out', f'{gid}-{i:02d}.png')
                render(page, out, 1350)
                im = Image.open(out).convert('RGB')
                im.save(os.path.join(png_dir, s['name'] + '.png'))
                im.save(os.path.join(jpg_dir, s['name'] + '.jpg'), quality=92)
            print('ok', gid, total)
    if 'cierres' in what:
        for c in CIERRES:
            key = f"dia-{c['n']:02d}"
            page = os.path.join(BASE, key + '.html')
            open(page, 'w').write(cierre(c))
            out = os.path.join(BASE, 'out', key + '.png')
            render(page, out, 1080)
            im = Image.open(out).convert('RGB')
            im.save(os.path.join(REPO, f"{key}-{c['slug']}.png"))
            im.save(os.path.join(REPO, 'jpg', f"{key}-{c['slug']}.jpg"), quality=92)
            print('ok', key)


main(sys.argv[1:] or ['guias', 'cierres'])
