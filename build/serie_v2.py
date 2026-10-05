import os, subprocess, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
MKT = os.path.expanduser('~/StudioProjects/strife-marketing')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SHOT_H = 1434
FOOTER = 'YA EN<br>GOOGLE PLAY'
DIRIGE, ENTRENA = 'PARA QUIEN DIRIGE', 'PARA QUIEN ENTRENA'

HTML_SHELL = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  @font-face {{
    font-family: 'Anton'; font-weight: 400; font-style: normal;
    src: url('fonts/anton.woff2') format('woff2');
  }}
  @font-face {{
    font-family: 'JetBrains Mono'; font-weight: 700; font-style: normal;
    src: url('fonts/jbmono-bold.woff2') format('woff2');
  }}
  @font-face {{
    font-family: 'Inter'; font-weight: 400; font-style: normal;
    src: url('fonts/inter-regular.woff2') format('woff2');
  }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html,body {{ width:1080px; height:1350px; background:#0b0b0d; overflow:hidden; }}
  body {{
    position:relative;
    background:
      radial-gradient(ellipse 900px 500px at 15% 100%, rgba(120,45,15,0.35), transparent 60%),
      #0b0c0e;
    font-family:'Inter',sans-serif;
  }}

  .header {{
    position:absolute; top:70px; left:72px; right:72px;
    display:flex; justify-content:space-between; align-items:center;
  }}
  .header .label {{
    font-family:'JetBrains Mono',monospace; font-weight:700; font-size:28px;
    letter-spacing:0.14em; color:#e2571e; text-transform:uppercase;
  }}
  .header .tag {{
    font-family:'JetBrains Mono',monospace; font-weight:700; font-size:26px;
    letter-spacing:0.12em; color:#5f6064; text-transform:uppercase;
  }}

  .headline {{
    position:absolute; top:150px; left:68px; width:960px;
    font-family:'Anton',sans-serif; font-size:110px; line-height:0.93;
    text-transform:uppercase;
  }}
  .headline .l1 {{ color:#ffffff; display:block; }}
  .headline .l2 {{ color:#e2571e; display:block; }}

  .subtitle {{
    position:absolute; top:{subtitle_top}px; left:72px; width:780px;
    font-family:'Inter',sans-serif; font-weight:400; font-size:29px; line-height:1.35;
    color:#a2a2a3;
  }}

  .phone {{
    position:absolute; left:300px; top:575px; width:534px; height:775px;
    border-radius:52px 52px 0 0; overflow:hidden; background:#000;
  }}
  .phone .statusbar {{
    position:relative; height:66px; width:100%; background:#000;
  }}
  .phone .statusbar .time {{
    position:absolute; left:26px; top:16px; font-family:'Inter',sans-serif;
    font-weight:700; font-size:26px; color:#fff;
  }}
  .phone .statusbar .icons {{
    position:absolute; right:24px; top:20px; display:flex; align-items:center; gap:8px;
  }}
  .phone .shot {{
    width:100%; height:calc(100% - 66px); object-fit:cover; object-position:top center; display:block;
  }}

  .footer-logo {{
    position:absolute; left:72px; bottom:150px;
    font-family:'Anton',sans-serif; font-size:38px; color:#fff;
  }}
  .footer-logo span {{ color:#e2571e; }}
  .footer-tag {{
    position:absolute; left:72px; bottom:72px;
    font-family:'JetBrains Mono',monospace; font-weight:700; font-size:22px;
    letter-spacing:0.08em; color:#5f6064; line-height:1.5;
  }}
  .counter {{
    position:absolute; right:72px; bottom:72px;
    font-family:'JetBrains Mono',monospace; font-weight:700; font-size:26px;
    letter-spacing:0.1em; color:#e2571e;
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="label">{label}</div>
    <div class="tag">{tag}</div>
  </div>
  <div class="headline"><span class="l1">{line1}</span><span class="l2">{line2}</span></div>
  <div class="subtitle">{subtitle}</div>
  <div class="phone">
    <div class="statusbar">
      <div class="time">9:41</div>
      <div class="icons">
        <svg width="30" height="20" viewBox="0 0 30 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="0" y="12" width="5" height="8" rx="1" fill="white"/>
          <rect x="7" y="9" width="5" height="11" rx="1" fill="white"/>
          <rect x="14" y="5" width="5" height="15" rx="1" fill="white"/>
          <rect x="21" y="1" width="5" height="19" rx="1" fill="white"/>
        </svg>
        <svg width="24" height="18" viewBox="0 0 24 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 16.5C13 16.5 13.8 15.7 13.8 14.7C13.8 13.7 13 12.9 12 12.9C11 12.9 10.2 13.7 10.2 14.7C10.2 15.7 11 16.5 12 16.5Z" fill="white"/>
          <path d="M12 9C14.5 9 16.8 10 18.5 11.6L16.6 13.6C15.4 12.5 13.8 11.8 12 11.8C10.2 11.8 8.6 12.5 7.4 13.6L5.5 11.6C7.2 10 9.5 9 12 9Z" fill="white"/>
          <path d="M12 2C16.7 2 21 3.9 24 7L22.1 9C19.5 6.5 15.9 5 12 5C8.1 5 4.5 6.5 1.9 9L0 7C3 3.9 7.3 2 12 2Z" fill="white"/>
        </svg>
        <svg width="42" height="20" viewBox="0 0 42 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="1" y="1" width="34" height="18" rx="4" stroke="white" stroke-width="1.5"/>
          <rect x="3.5" y="3.5" width="29" height="13" rx="2" fill="white"/>
          <rect x="37" y="7" width="3" height="6" rx="1.5" fill="white"/>
        </svg>
      </div>
    </div>
    <img class="shot" src="{screenshot}">
  </div>
  <div class="footer-logo">STR<span>/</span>FE</div>
  <div class="footer-tag">{footer}</div>
  <div class="counter">{counter}</div>
</body>
</html>
"""

SLIDES = [
    dict(n=1, slug='voy', src='public/mi5/sesion_3.png', y=63, label='RESERVAS · SESIÓN', tag=ENTRENA,
         line1='VOY.', line2='', subtitle_top=300,
         subtitle='Abre la clase, mira quién va y reserva con un toque. ¿No vas? Avisa y tu hueco lo pilla otro.'),
    dict(n=2, slug='la-semana-montada', src='public/mi4/calendario_mes.png', y=63, label='HORARIO · CALENDARIO', tag=DIRIGE,
         line1='LA SEMANA,', line2='MONTADA.',
         subtitle='Días, hora, aforo y coach: lo pones una vez y el mes entero se rellena solo.'),
    dict(n=3, slug='ficha-al-entrar', src='public/mi5/qr_ok.png', y=300, label='ASISTENCIA · QR', tag=ENTRENA,
         line1='FICHA', line2='AL ENTRAR.',
         subtitle='Escanea el QR de la clase al llegar y quedas presente. Sin libreta en la puerta.'),
    dict(n=4, slug='lista-30-segundos', src='public/mi4/lista_1.png', y=63, label='CLASE · PASAR LISTA', tag=DIRIGE,
         line1='LISTA EN', line2='30 SEGUNDOS.',
         subtitle='Presente, ausente o retraso. Quien ficha con el QR ya entra marcado.'),
    dict(n=5, slug='mes-nuevo-podio-nuevo', src='public/mi5/ranking_1.png', y=250, label='RANKING · ASISTENCIA', tag=ENTRENA,
         line1='MES NUEVO,', line2='PODIO NUEVO.',
         subtitle='Cada clase a la que vas suma. Podio por disciplina y por clase; el día 1, todos a cero.'),
    dict(n=6, slug='el-mes-cuadrado', src='public/mi4/pagos_1.png', y=63, label='PAGOS · CUOTAS', tag=DIRIGE,
         line1='EL MES,', line2='CUADRADO.',
         subtitle='Cobrado, parcial y pendiente: quién debe, a la vista. Sin hoja de cálculo.'),
    dict(n=8, slug='cada-roll-apuntado', src='public/mi5/anotar_2.png', y=63, label='MI JUEGO · EL PARTE', tag=ENTRENA,
         line1='CADA ROLL,', line2='APUNTADO.',
         subtitle='Al salir del tatami: con quién rodaste y cómo acabó. Tu diario de sparring, en 30 segundos.'),
    dict(n=9, slug='dicho-una-vez', src='public/mi4/tablon_1.png', y=63, label='CENTRO · TABLÓN', tag=DIRIGE,
         line1='DICHO', line2='UNA VEZ.',
         subtitle='Avisos urgentes, programados o atados a una clase. Entran y salen solos, sin cadenas de WhatsApp.'),
    dict(n=10, slug='el-peso-a-raya', src='public/mi5/cuerpo_peso.png', y=63, label='CUERPO · PESO', tag=ENTRENA,
         line1='EL PESO,', line2='A RAYA.',
         subtitle='Un número y listo: la curva, tu objetivo y las lesiones que te frenan, en tu perfil.'),
    dict(n=11, slug='la-tienda-sin-mostrador', src='public/mi5/producto_2.png', y=700, label='CENTRO · TIENDA', tag=DIRIGE,
         line1='LA TIENDA,', line2='SIN MOSTRADOR.',
         subtitle='El alumno reserva talla y color en la app; tú entregas y cobras en el mostrador.'),
    dict(n=12, slug='tu-vitrina-contigo', src='public/mi5/logros_1.png', y=63, label='PERFIL · LOGROS', tag=ENTRENA,
         line1='TU VITRINA,', line2='CONTIGO.',
         subtitle='Parches por asistencia, rachas y sparring, con su fecha. Y tus seis favoritos en la vitrina.'),
    dict(n=13, slug='el-club-en-orden', src='mi-4/capturas/ficha_1.png', y=63, label='MIEMBROS · FICHA', tag=DIRIGE,
         line1='EL CENTRO,', line2='EN ORDEN.',
         subtitle='La ficha de cada alumno: cuota, cinturón, asistencia y contacto, en un solo sitio.'),
    dict(n=15, slug='compites-aparece', src='serie-v2/capturas/15_01_perfil_competicion.png', y=812, label='PERFIL · COMPETICIÓN', tag=ENTRENA,
         line1='COMPITES,', line2='APARECE.',
         subtitle='Vincula tu perfil de Smoothcomp: victorias, medallas y cada evento, en tu perfil.'),
    dict(n=16, slug='nadie-se-descuelga', src='public/mi4/seguimiento_1.png', y=63, label='SEGUIMIENTO · TERMÓMETRO', tag=DIRIGE,
         line1='NADIE SE', line2='DESCUELGA.',
         subtitle='El termómetro avisa de quién se está enfriando antes de que se vaya, y a quién escribir hoy.'),
    dict(n=17, slug='cara-a-cara', src='serie-v2/capturas/17_02_combate.png', y=63, label='RANKING · CARA A CARA', tag=ENTRENA,
         line1='CARA', line2='A CARA.',
         subtitle='Elige rival en el ranking: puntos, rachas y asistencia, lado a lado. Y cuánto te falta.'),
    dict(n=18, slug='el-grupo-sin-ruido', src='public/mi5/chat_1.png', y=63, label='CENTRO · CHAT', tag=DIRIGE,
         line1='EL GRUPO,', line2='SIN RUIDO.',
         subtitle='El chat del centro, dentro de la app: con normas, denuncias y bloqueo.'),
    dict(n=19, slug='tu-cinturon-tiene-historia', src='serie-v2/capturas/19_02_promocionar.png', y=700, label='MIEMBROS · CINTURONES', tag=DIRIGE,
         line1='CADA GRADO,', line2='CON FECHA.',
         subtitle='Promocionas desde la ficha: cinturón y grados, con fecha y firma. El linaje del centro, sin romperse.'),
    dict(n=20, slug='la-puerta-con-criterio', src='public/mi4/admisiones_1.png', y=63, label='MIEMBROS · ADMISIONES', tag=DIRIGE,
         line1='LA PUERTA,', line2='CON CRITERIO.',
         subtitle='Cada solicitud llega con su nombre y su rol. Un toque: dentro o fuera.'),
    dict(n=22, slug='empieza-aqui', src='serie-v2/capturas/22_09_centro_en_mapa.png', y=850, label='PRIMER DÍA · TU GIMNASIO', tag=ENTRENA,
         line1='EMPIEZA', line2='AQUÍ.',
         subtitle='Descargas la app, buscas tu gimnasio en el mapa y pides plaza. El primer día empieza antes de llegar.'),
    dict(n=23, slug='abre-tu-club', src='serie-v2/capturas/23_06_revisar_y_enviar.png', y=600, label='ALTA · TU CENTRO', tag=DIRIGE,
         line1='ABRE TU', line2='CENTRO.',
         subtitle='Nombre, disciplinas y quién entra. Un revisor lo aprueba en minutos y empiezas con 30 días gratis.'),
    dict(n=24, slug='tu-cuota-clara', src='public/mi5/cuota_1.png', y=966, label='PERFIL · MI CUOTA', tag=ENTRENA,
         line1='TU CUOTA,', line2='CLARA.',
         subtitle='Cuánto y hasta cuándo está cubierta, en tu perfil. Pagas en recepción; la app lleva las cuentas.'),
    dict(n=25, slug='invita-en-un-toque', src='serie-v2/capturas/25_02_elegir_rol.png', y=520, label='MIEMBROS · INVITAR', tag=DIRIGE,
         line1='INVITA EN', line2='UN TOQUE.',
         subtitle='Nombre, @usuario o email, y el rol con el que entra. La invitación le llega y el alta se hace sola.'),
    dict(n=26, slug='sabes-a-que-vas', src='mi-5/capturas/sesion_1.png', y=63, label='CLASE · SESIÓN', tag=ENTRENA,
         line1='SABES', line2='A QUÉ VAS.',
         subtitle='El plan de hoy, el coach y quién va, antes de pisar el tatami.'),
    dict(n=27, slug='tu-club-tu-casa', src='public/mi4/inicio_1.png', y=63, label='CENTRO · PORTADA', tag=DIRIGE,
         line1='TU CENTRO,', line2='TU CASA.',
         subtitle='Portada, emblema, disciplinas y estado: la cabecera es de tu centro.'),
    dict(n=29, slug='tu-juego-en-datos', src='public/mi5/mijuego_oscuro.png', y=63, label='MI JUEGO · EL MES', tag=ENTRENA,
         line1='TU JUEGO,', line2='EN DATOS.',
         subtitle='Rolls del mes, balance, lo que rematas y lo que te rematan. El sparring, contado.'),
]


def build(s):
    key = f"dia-{s['n']:02d}"
    shot = os.path.join(REPO, 'capturas-app', 'v2', key + '.png')
    os.makedirs(os.path.dirname(shot), exist_ok=True)
    im = Image.open(os.path.join(MKT, s['src'] if s['src'].startswith('serie-v2') else 'reel/' + s['src'])).convert('RGB')
    im.crop((0, s['y'], 1080, s['y'] + SHOT_H)).save(shot)
    html = HTML_SHELL.format(
        label=s['label'], tag=s['tag'], line1=s['line1'], line2=s['line2'], subtitle=s['subtitle'],
        counter=f"{s['n']:02d} / 29", screenshot=f'../capturas-app/v2/{key}.png', footer=FOOTER,
        subtitle_top=s.get('subtitle_top', 452),
    )
    page = os.path.join(BASE, key + '.html')
    open(page, 'w').write(html)
    out = os.path.join(BASE, 'out', key + '.png')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1080,1350', f'--screenshot={out}', 'file://' + page],
                   check=True, capture_output=True)
    final = os.path.join(REPO, f"{key}-{s['slug']}.png")
    Image.open(out).convert('RGB').save(final)
    Image.open(out).convert('RGB').save(os.path.join(REPO, 'jpg', f"{key}-{s['slug']}.jpg"), quality=92)
    print('ok', key)


only = {int(a) for a in sys.argv[1:]}
for s in SLIDES:
    if not only or s['n'] in only:
        build(s)
