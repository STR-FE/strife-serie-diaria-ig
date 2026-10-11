# Plan: cada post suelto, un carrusel paso a paso

Estado a 11 de octubre de 2026, 19:20:

- **dia-02 hecho** (`jpg/dia-02/`), en el calendario como carrusel. Pendiente de que Jaime lo revise antes del push.
- **dia-01 sigue como imagen suelta.** El carrusel del widget (`build/carruseles/dia-01-widget.json`) no se publica de
  momento: puede confundirse con la forma normal de reservar desde la app, y no deja claro que es un widget de la
  pantalla de inicio del teléfono. Si se retoma, tiene que enseñar el móvil entero, con el escritorio.
- **No hay commit ni push hasta tener TODOS los flujos** (Jaime, 11 oct). Mientras tanto, lo programado se publica
  como estaba (imagen suelta).
- Capturas hechas (strife-marketing/serie-v3/capturas): dia-02, 03, 04, 05, 06, 08, 09, 11, 12, 13, 17, 18, 19, 20,
  24, 25, 26, 27 y 29. dia-01 con el widget, apartado. Faltan: dia-10 (a partir del 12 oct), dia-15 (Smoothcomp),
  dia-16 (con la versión de RL-357), dia-05 paso «el día 1, a cero» (1 nov) y los cierres dia-21 y dia-28.
- Fernando Muller Jung (persona real) sale de Villalba por decisión de Jaime (11 oct): `v3_00_fernando_seed.sql`.
- Siembra autorizada para toda la serie, cada paso con su limpieza: `siembra/v3_limpiar.sh` lo deshace todo en orden
  inverso y termina con `v3_check.sql`, en el que todas las filas deben salir `true`.
- dia-10 se captura a partir del 12 oct: el aviso de peso pide más de 7 días desde el último peso (el 4 oct).

Fallos de la app vistos al capturar, para tickets:

- RL-358 (abierto): Mi semana se queda desfasada tras un RSVP del widget.
- En «Mi juego» de Hoy, la lesión sale como «lpaa der.»: `bodyStructureAtflShort` («LPAA») pasado a minúsculas.
- En el perfil de otro alumno, «El juego de Rubén» dice «TU ARMA» y «TU GRIETA».
- En la hoja de rival de Mi juego, «Tú» es siempre un avatar anónimo «?» (`SparAnonAvatar`); en «Comparar trofeos» sí
  sale tu cara. ¿Intencionado?
- Las filas de la Sala de Trofeos no abren el perfil del compañero.
- Proyector del QR: las caritas de «En vivo · N ya en la lista» son iniciales aunque el alumno tenga foto.
- Pasar lista: «Marcar resto» marca presentes al momento, sin confirmar, y también a los alumnos que no habían
  reservado (17 de 17 cuando iban 11).
- Pagos: con 1 vencido pone «1 vencidos».
- Bandeja de avisos del alumno: «Clase cancelada: NO-GI» sale dos veces.
- Ranking › Cara a cara › Remontada: «Tus oportunidades antes del cierre» no filtra por la disciplina del ranking
  (en BJJ propone Muay Thai) (`compare_providers.dart`, `compareOpportunitiesProvider`).
- El parte (sparring) y la hoja de rival: «Tú» sale como un círculo sin foto aunque tengas avatar.
- Diario: «Esguince · LPAA der..» con doble punto.
- Registrar pago de cuota con menos importe no pregunta qué hacer con la diferencia (la tienda sí: «Que me lo deba /
  Se lo perdono»).
- Cambiar la hora de una sesión por SQL avisa a los apuntados («clase reprogramada»). Por eso el clean de la sesión
  borra esos avisos.

Reglas de diseño (Jaime, 11 oct):

- Nunca un usuario en primera plana, ni ficticio: las caras solo dentro de las capturas. Portadas con texto y arte de
  marca.
- Alternar el zoom de arriba (diseño B) con pasos de captura entera (`"modo": "entero"`) cuando ayuda a ubicarse.

## Dónde está cada cosa

- Este repo es público: aquí solo van los JPG publicables y los JSON de cada carrusel (`build/carruseles/`).
- Repo privado `strife-marketing/serie-v3/`:
  - `capturas/dia-XX/`: las capturas originales, de la 1.5.8 compilada en `roll_lab_v158`, en el emulador P1.
  - `siembra/`: SQL de siembra y de limpieza, y la subida de caras a `user-avatars`.
  - `tomas/`: las listas de tomas.
- La foto del banner de Villalba **no se usa** fuera de las capturas: es una captura de una historia de Instagram ajena,
  con camisetas de otro club.
- Tickets abiertos al capturar: RL-357 (Seguimiento sin entrada, en curso en otra sesión) y RL-358 (Mi semana se queda
  desfasada tras un RSVP del widget).

## Qué se pide

- Los 23 posts de una imagen que quedan desde el 12 de octubre pasan a carrusel paso a paso: el flujo entero de
  la funcionalidad, pantalla a pantalla, como las guías.
- dia-14 (hoy, 20:30) se queda como está.
- Con personas: las cuentas ficticias de Villalba llevan cara IA como foto de perfil, así que las capturas ya salen
  con caras. Las caras salen de `strife-marketing/reel/caras-ia` (21). Se pueden repetir caras y nombres.
- **Capturas nuevas de la 1.5.8** en Villalba Fighting Co., todas las que hagan falta. Las de la 1.4.1 no se
  reutilizan.

## Formato

- Portada + hasta 8 pasos + cierre = 10 fotos como máximo (límite de Instagram).
- Diseño B de `build/guia_diseno.py`, con la lupa del C cuando el paso es un detalle pequeño.
- Un JSON por carrusel en `build/carruseles/dia-XX.json`, con el mismo formato que las guías.
- Las fotos van en `jpg/dia-XX/NN.jpg`.
- En `pies-de-foto.txt`, cada `DÍA` pasa a `CARRUSEL` con `Id: dia-XX`. `generar_calendario.py 2026-10-06`
  regenera el calendario sin mover fechas ni horas.

## Lista de tomas

Por post: protagonista, pasos (pantalla `.dart`, cómo se llega, cuenta, siembra y caras), solapes y cambios de la
1.5.8.

- Quien entrena (12 posts, ~105 capturas): `strife-marketing/serie-v3/tomas/tomas-alumno.md`
- Quien dirige y marca (13 posts, ~92 capturas): `strife-marketing/serie-v3/tomas/tomas-centro.md`

| Fecha | Post | Público | Flujo |
|---|---|---|---|
| 12 oct | dia-02 | centro | Catálogo → nueva clase → horario → mes → exportar |
| 13 oct | dia-01 | alumno | Widget 1.5.8: aviso → añadir → ✓ «Asistiré» → ficha → quién va → cancelar |
| 15 oct | dia-04 | centro | Hoy → sesión → Gestionar → Pasar lista (QR + Lista con foto) → P/A/R → Marcar resto |
| 18 oct | dia-03 | alumno | El QR desde el alumno: escanear → «¡Presente!» → la ficha |
| 20 oct | dia-06 | centro | Pagos del mes → alumno → registrar pago → recordatorio → bonos |
| 21 oct | dia-24 | alumno | Tu cuota: estado, hasta cuándo, recordatorio, pagado |
| 23 oct | dia-11 | centro | Tienda: producto → stock → pedido → entrega → vender ahora |
| 25 oct | dia-21 | marca | Cierre: «un día en tu centro» |
| 26 oct | dia-26 | alumno | La ficha de la clase antes de ir |
| 27 oct | dia-08 | alumno | Apuntar un roll |
| 29 oct | dia-29 | alumno | Mi juego |
| 30 oct | dia-10 | alumno | Peso, objetivo y lesiones |
| 2 nov | dia-05 | alumno | Ranking y podio |
| 3 nov | dia-16 | centro | Termómetro de seguimiento |
| 6 nov | dia-17 | alumno | Cara a cara |
| 7 nov | dia-12 | alumno | Logros y vitrina |
| 8 nov | dia-15 | alumno | Smoothcomp y palmarés |
| 10 nov | dia-13 | centro | Ficha del alumno |
| 12 nov | dia-20 | centro | Admisiones |
| 13 nov | dia-25 | centro | Invitar, con «Compartir invitación» por WhatsApp |
| 15 nov | dia-18 | centro | Chat: normas, denuncia, bloqueo |
| 18 nov | dia-19 | alumno | Cinturón: promoción y linaje |
| 19 nov | dia-09 | centro | Tablón |
| 20 nov | dia-27 | centro | Portada del centro en Inicio |
| 22 nov | dia-28 | marca | Cierre: «empieza en 5 pasos» |

## Decisiones (11 oct)

- **Plazo:** dia-02 y dia-01 estarán a tiempo. Se va por orden de fecha.
- **Solapes:**
  - El post cuenta el flujo principal y la guía del mismo tema se rehace con el ángulo complementario que proponen
    las listas de tomas: asistencia, miembros, invitar, centro y, en parte, juego.
  - guia-clases pierde catálogo, horario y mes, que ya salen en dia-02.
- **Seguimiento (dia-16):** el tablero no tiene entrada en la UI. Ticket **RL-357** (rolllab.atlassian.net/browse/RL-357).
  dia-16 se captura con la versión que lo
  arregle, antes del 30 de octubre.
- **Widget (dia-01):** en el emulador, con un lanzador limpio.
- **Por defecto, si Jaime no dice otra cosa:**
  - QR: el emulador lo proyecta y el Redmi lo escanea de verdad.
  - Smoothcomp: el perfil de Jaime, con los rivales y el banner pixelados.
  - El mensaje de WhatsApp se captura tal cual sale.
  - Cierres: dia-21 «un día en tu centro» y dia-28 «empieza en 5 pasos».
  - dia-05 se captura el 1 de noviembre.

## Además

- **guia-asistencia (16 oct)** enseña la fila de botones de la 1.4 (sin «Lista con foto») y un avatar de
  iniciales. Hay que rehacer `04.jpg` con la captura del paso 04 de dia-04.
- guia-invitar no enseña la sección nueva de WhatsApp, pero no muestra nada falso.

## Cómo se captura

- Dispositivos:
  - Emulador P1 (1080×2400), con las cuentas de prueba.
  - Redmi (1080×2400, STRIFE 1.5.8 de Google Play), con la cuenta de Jaime.
  - Barra de estado en modo demo, modo oscuro y `adb exec-out screencap`.
- **Siembra en producción** (Villalba Fighting Co.):
  - Caras como avatar.
  - Clases, sesiones y RSVP; asistencia de octubre; sparring.
  - Cuerpo, pagos, tienda, seguimiento, cinturones, chat, tablón, admisión e invitaciones.
  - El detalle está en las dos listas.
  - Todo con su script de limpieza, como `mi5_seed.sql` / `mi5_clean.sql`.
  - **Cada escritura en producción, con el OK explícito de Jaime.**
- Se captura por orden de fecha de publicación. Los primeros, dia-02 y dia-01, salen el 12 y el 13 de octubre.

## Comprobación

- Cada carrusel se revisa en imagen antes de dar el visto bueno.
- `generar_calendario.py` valida que existen las fotos y que cada carrusel tiene entre 2 y 10.
- Diff de `calendario.json`: solo cambian `tipo` y `archivos`.
- Commit y push solo con el OK de Jaime: GitHub Actions publica lo que haya en `main`.
