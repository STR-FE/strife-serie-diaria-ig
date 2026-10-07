# Plan: horas de publicación dinámicas (a partir de ~100 seguidores)

Estado a 7 de octubre de 2026: **sin ejecutar**. Se activa cuando la cuenta llegue a ~100 seguidores.

## Por qué esperar

- Instagram solo sirve `online_followers` (a qué hora están conectados los seguidores) con 100+ seguidores.
- Con menos, el alcance por hora de publicación es ruido: una publicación al día no da muestra.
- Hasta entonces se mantienen las `HORAS` fijas de `automatizacion/generar_calendario.py`.

## Qué ya existe

- `automatizacion/medir_audiencia.py`: pide `online_followers` y el alcance, likes, guardados y compartidos de cada post de `registro.json`.
- `generar_calendario.py` produce `calendario.json` con las horas de la tabla `HORAS`.
- `publicar-instagram.yml` comprueba cada 15 minutos qué toca publicar según `calendario.json`; no hay que cambiarlo.

## Pendiente de comprobar (antes de nada)

El token vive solo como secreto de GitHub (`IG_ACCESS_TOKEN`), así que no se puede probar en local. Hay que lanzar `medir_audiencia.py` desde un workflow `workflow_dispatch` y mirar:

1. ¿`online_followers` responde o da error de permisos? Con la vía «Instagram Login» no hay permiso de insights documentado.
2. ¿Responde `/{post_id}/insights` (reach, likes, saved, shares)? Esto funciona sin los 100 seguidores y se puede comprobar ya.

Si `online_followers` falla por permisos, hay que decidir entre: otra vía de login con permiso de insights, o leer las horas a mano en la app (Perfil > Estadísticas) y actualizar `HORAS`.

**Cuidado:** el repo es público y los logs de Actions también. No imprimir el token; la salida de `medir_audiencia.py` solo lleva ids de post y cifras.

## Pasos cuando haya 100 seguidores

1. Workflow semanal (`medir-horas.yml`, también `workflow_dispatch`) que ejecuta `medir_audiencia.py` con el secreto.
2. Sacar las 2–3 mejores franjas por público a partir de `online_followers`. El alcance por hora de publicación queda como segunda señal.
3. Reescribir en `calendario.json` solo las publicaciones futuras (`fecha` posterior a hoy y sin entrada en `registro.json`).
4. Repartir las publicaciones entre las franjas buenas, no todas a la hora pico, para seguir comparando.
5. Commit automático del `calendario.json` nuevo. El workflow que publica lo recoge solo.

## Criterio de hecho

- Con la cuenta por encima de 100 seguidores, el workflow semanal deja un `calendario.json` con horas distintas de las fijas y sin tocar nada ya publicado.
- Las horas salen en Madrid, para que el cambio de hora no las mueva.
