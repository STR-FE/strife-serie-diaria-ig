# Manual de la serie diaria

Cómo funciona la publicación automática y qué tocar para cambiar cada cosa.

> **▶ EN MARCHA desde el 6 de octubre de 2026.** 49 publicaciones, una al día, hasta el 23 de noviembre.
> Para pausarla: pestaña **Actions** › *Publicar serie diaria en Instagram* › **Disable workflow**.

## 1. La cadena

| Pieza | Qué hace |
|---|---|
| `pies-de-foto.txt` | **Lo que escribes tú.** El texto de los 29 posts (`DÍA N`) y de los 20 carruseles (`CARRUSEL`, con su `Id:`). |
| `automatizacion/generar_calendario.py` | **El que ordena.** `ORDEN` dice qué sale cada día y para qué público; `HORAS` dice a qué hora según el público y el día de la semana. |
| `automatizacion/calendario.json` | **El plan.** Fecha, hora, imágenes y texto de cada publicación. No se edita a mano: se regenera. |
| `automatizacion/publicar.py` | **El que publica.** Si hoy hay post, ya es su hora y no consta en el registro, lo publica. |
| `automatizacion/registro.json` | **La memoria.** Lo ya publicado, para no repetirlo nunca. Lo escribe el workflow. |
| `.github/workflows/publicar-instagram.yml` | **El despertador.** Corre en GitHub cada 15 minutos; no depende de ningún ordenador. |
| `.github/workflows/renovar-token.yml` | **El token.** Los días 1 y 20 comprueba que el token se puede renovar (ver §5). |

## 2. Las horas

La hora de cada publicación está en `calendario.json` (campo `hora`, Europe/Madrid) y **sí manda**: el workflow
despierta cada 15 minutos y `publicar.py` solo publica cuando llega esa hora. El cambio de hora de octubre y marzo
no la mueve. GitHub puede retrasar el cron unos minutos. Un día que se pasa sin publicar no se recupera al siguiente.

| Público | L-V | Sábado | Domingo |
|---|---|---|---|
| Quien entrena (`alumno`, `marca`) | 21:30 | 13:00 | 20:30 |
| Quien dirige un centro (`centro`) | 14:00 | 10:30 | 20:30 |

Son estimaciones: Instagram no da las horas de actividad hasta ~100 seguidores. Entonces,
`IG_ACCESS_TOKEN=… python3 automatizacion/medir_audiencia.py` las saca y se cambian en `HORAS`.

## 3. El orden

Primero qué es y cómo se entra; luego el día a día (clases y asistencia), el dinero, el atleta (sparring, cuerpo,
ranking, perfil), el coach (parte y seguimiento) y la gestión fina (miembros, permisos, ajustes). Un post suelto
presenta una idea y la guía de al lado la enseña paso a paso. Los cierres de marca caen en domingo.

## 4. Qué puedes cambiar

| Qué | Dónde | Cómo |
|---|---|---|
| Orden o público | `ORDEN` en `generar_calendario.py` | mover filas |
| Horas | `HORAS` en `generar_calendario.py` | una lista de 7 por público |
| Textos y hashtags | `pies-de-foto.txt` | respeta `Pie:`, `Tags:` e `Id:` |
| Fecha de inicio | ningún fichero | `python3 automatizacion/generar_calendario.py 2026-10-06` |

**Regla:** cambies lo que cambies, regenera con la fecha de inicio real (`2026-10-06`) y sube. Quien publica es
GitHub: lo que no está subido no existe. Lo ya publicado no se repite aunque cambie el orden (va por `id`).

## 5. El token

Dura 60 días; el actual caduca el **5 de diciembre de 2026**. Para renovarlo sin que salga en claro:

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out tok.key
gh workflow run renovar-token.yml -R STR-FE/strife-serie-diaria-ig -f clave_publica="$(openssl pkey -in tok.key -pubout | base64 | tr -d '\n')"
# del log, el bloque entre TOKEN_CIFRADO_INICIO y TOKEN_CIFRADO_FIN, en cifrado.b64:
base64 -d -i cifrado.b64 | openssl pkeyutl -decrypt -inkey tok.key -pkeyopt rsa_padding_mode:oaep \
  | gh secret set IG_ACCESS_TOKEN -R STR-FE/strife-serie-diaria-ig
rm tok.key cifrado.b64
```

Generar o renovar un token no invalida el anterior. Para matar uno filtrado hay que revocar el acceso de la app en
[instagram.com/accounts/manage_access](https://instagram.com/accounts/manage_access). Nunca lo pegues en un chat,
un correo o un commit.

## 6. Probar sin publicar

| Quiero… | Dónde |
|---|---|
| ver qué saldría hoy | `cd automatizacion && python3 publicar.py --dry-run` |
| ver un post concreto | `python3 publicar.py --id guia-clases --dry-run` |
| publicar uno a mano, ya | Actions › *Run workflow* › `id` y `dry_run` desmarcado |

## 7. Las imágenes

Todas salen de capturas reales de la app 1.4.1 en **Villalba Fighting Co.** con alumnos ficticios; nada de JGS.
Las capturas originales están en el repo privado `strife-marketing` (`reel/mi-4`, `reel/mi-5` y `serie-v2/`, con
su `capturas.md`). Instagram solo acepta JPEG: lo que se publica está en `jpg/`.

| Qué | Generador | Sale en |
|---|---|---|
| 25 posts con móvil | `build/serie_v2.py` | raíz y `jpg/` |
| 4 cierres y las guías del alumno y del centro | `build/guias_cierres_v2.py` | `guia-alumno/`, `guia-club/` y `jpg/` |
| 18 guías por caso de uso (diseño B) | `build/guia_diseno.py <guia.json> B` | `build/diseno/<guia>/B/`; luego a `jpg/<guia>/` |

Los JSON de las 18 guías están en `strife-marketing/serie-v2/guias/`. Tras cambiar una guía hay que volver a pasar
sus PNG a `jpg/<guia>/` y subir.
