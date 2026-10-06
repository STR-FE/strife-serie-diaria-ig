# Serie diaria v2 · resumen (5–6 de octubre de 2026)

## Qué se ha hecho

**1. La serie original, al día.** Los 29 posts de agosto estaban desfasados: decían «beta cerrada · verano
2026», la mitad eran pantallas dibujadas y las capturas reales eran de un gimnasio con alumnos reales. Ahora:

- Todos llevan capturas reales de la app 1.4.1 en el centro de pruebas Villalba Fighting Co., con alumnos ficticios.
- Los textos y pies de foto cuadran con la app y con la web (`getstrife.com`): «ya en Google Play», gratis para
  quien entrena, 30 días de prueba para el centro y 14,99 €/mes.
- Los cuatro cierres de marca se rehicieron con las liebres y el flamenco del reel.
- Las imágenes no llevan contador «NN / 29», porque ya no salen en ese orden.

**2. Veinte guías en carrusel**, una por caso de uso, en el diseño B: el móvil a todo el ancho, legible en el
teléfono.

| Para quien entrena | Para quien dirige |
|---|---|
| Tu primer día · La tab Clases · Hoy · Mi juego (tres rolls) · Una lesión con el 3D · Peso y episodios · Tu perfil · La tienda · El chat · Ajustes del alumno | Abre tu centro · Pasar lista · Cobrar la cuota · El parte de clase · Seguimiento · Miembros · Permisos · Invitar · Tu centro en Inicio · Ajustes del centro |

Avatares, banners, iconos de clase, anuncios y productos llevan ilustraciones de marca. Los alumnos son ficticios.
Las únicas personas reales son las fotos del centro, con consentimiento, y el perfil del dueño.

**3. La publicación, automática y a la hora de cada público.**

- 49 publicaciones, una al día, del 6 de octubre al 23 de noviembre: los 29 posts y las 20 guías.
- Orden: qué es y cómo se entra → clases y asistencia → el dinero → el atleta → el coach → la gestión fina.
  Cada post suelto va seguido de su guía.
- Horas: quien entrena, entre semana a las 21:30; quien dirige, a las 14:00; los fines de semana aparte.
  Se calculan en hora de Madrid, así que el cambio de hora no las mueve.
- GitHub Actions comprueba cada 15 minutos si toca publicar. No hace falta ninguna máquina encendida.

**4. Lanzamiento.** El 6 de octubre se publicó a mano el primer post («STRIFE · Ya en Google Play») para
comprobar que funcionaba. Salió bien.

**5. Token de Instagram renovado** hasta el 5 de diciembre de 2026. Se renovó desde un workflow y se guardó en
el secreto cifrado de punta a punta: nunca apareció en claro. Cómo repetirlo: `MANUAL.md` §5.

## Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Lo que se publica (JPEG), el calendario y la automatización | este repo, `main` |
| Cómo funciona y cómo cambiarlo | `MANUAL.md` |
| Capturas originales, JSON de las guías, ilustraciones y scripts de datos de prueba | repo privado `strife-marketing`, rama `serie-v2-capturas` |

## Fallos encontrados y corregidos

- La primera publicación no quedó en el registro: el fichero aún no existía y el workflow solo miraba ficheros
  ya conocidos. El post de las 21:30 se habría repetido. Corregido y comprobado.
- Algunas capturas traían un borde verde de 2 px (un aviso de Android). Tapado.

## Pendiente

- **Datos de prueba en producción.** Los datos que se sembraron en el centro de pruebas para las capturas siguen
  ahí. Se borran con los scripts de limpieza de `strife-marketing/serie-v2/` (`serie_v2_clean.sql` y luego
  `reel/mi-5/mi5_clean.sql`). No afecta a la serie: las imágenes ya están aquí.
- **Horas reales.** Cuando la cuenta pase de ~100 seguidores, medirlas con `medir_audiencia.py` y ajustar `HORAS`.
- **Token.** Volver a renovarlo antes del 5 de diciembre si la serie sigue.
- **Rama `serie-v2-capturas` de `strife-marketing`.** Sin mergear.
