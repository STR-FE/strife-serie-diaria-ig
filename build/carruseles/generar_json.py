# Escribe build/carruseles/dia-XX.json a partir de las tablas de abajo (una por post).
# Paso: (captura, título, subtítulo, b) — b = desde qué píxel de la captura empieza el zoom (diseño B), o 'E' para el
# móvil entero. Las capturas viven en strife-marketing/serie-v3/capturas/dia-XX/ (las _t llevan los datos tapados);
# las que empiezan por serie-v2/ o reel/ son rutas de strife-marketing tal cual.
#   python3 build/carruseles/generar_json.py
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
ALUMNO = 'Gratis para quien entrena: descarga STRIFE y busca tu gimnasio.'
CENTRO = '30 días gratis para tu centro y luego 14,99 €/mes. Sin comisiones.'

C = {}

C['dia-02'] = ('PASO A PASO · TU HORARIO', ['LA SEMANA,', 'MONTADA.'],
  'Días, hora, aforo y coach: lo pones una vez y el mes entero se rellena solo.', [
  ('d02_01_catalogo', 'TUS CLASES', 'Clases › Catálogo: cada clase con su icono, su edad y su duración.', 'E'),
  ('d02_02_nueva', 'NUEVA CLASE', 'Con el «+»: disciplina, nombre y una línea para quien se apunta.', 63),
  ('d02_03_icono', 'SU ICONO, SU COLOR', 'Y la abreviatura con la que sale en el calendario.', 63),
  ('d02_04_horario', 'PON EL HORARIO', 'Clases › Horario › «+»: la clase, desde cuándo y hasta cuándo.', 63),
  ('d02_05_dias', 'DÍAS, HORA Y CUPO', 'Lunes y miércoles a las 19:00, una hora, 16 plazas y su coach.', 63),
  ('d02_06_mes', 'EL MES, SOLO', 'Antes de guardar ya ves el mes entero, con todas las clases del centro.', 'E'),
  ('d02_07_guardado', 'GUARDADO', 'Cada clase con sus días, su hora, su cupo y su coach.', 63),
  ('d02_08_exportar', 'A TU CALENDARIO', 'Las próximas cuatro semanas, al calendario del móvil en un toque.', 1188)],
  ['UNA VEZ,', 'Y LISTO.'], 'Quien entrena lo ve al momento y reserva desde su móvil. ' + CENTRO)

C['dia-03'] = ('PASO A PASO · FICHAR CON QR', ['LLEGAS,', 'Y FICHAS.'],
  'Escaneas el QR de la clase y quedas presente. Sin libreta en la puerta.', [
  ('d03_01_hoy', 'TU CLASE, YA', 'En Hoy: tu clase de esta tarde, reservada.', 63),
  ('d03_02_ficha', 'EL BOTÓN', 'Se abre 15 minutos antes y se cierra al terminar la clase.', 1188),
  ('d03_03_qr', 'EL QR DE LA PUERTA', 'Tu coach lo proyecta en la tele. Cambia cada 30 segundos.', 'E'),
  ('d03_04_visor', 'APÚNTALE', 'Apunta al QR de tu coach o al de la puerta.', 'E'),
  ('d03_05_presente', '¡PRESENTE!', 'Marcado con tu hora. +10 puntos cuando termine la clase.', 1100),
  ('d03_06_tarde', '¿LLEGAS TARDE?', '«Presente · con retraso»: +6, y tu coach puede perdonártelo.', 1100),
  ('d03_07_codigo', 'SIN CÁMARA, CÓDIGO', 'Las seis letras que salen debajo del QR.', 600),
  ('d03_08_lista', 'Y EN SU LISTA', 'Tu coach te ve dentro, «vía QR», con tu hora.', 63)],
  ['SIN LIBRETA', 'EN LA PUERTA.'], ALUMNO)

C['dia-04'] = ('PASO A PASO · PASAR LISTA', ['LISTA EN', '30 SEGUNDOS.'],
  'Presente, ausente o retraso. Y el QR hace la mitad.', [
  ('d04_01_hoy', 'CLASES DE HOY', 'La que está en curso, con su aforo y quién va.', 63),
  ('d04_02_sesion', 'LA SESIÓN', 'El plan de hoy y quién va, cada uno con su cara.', 63),
  ('d04_03_gestionar', 'GESTIONAR', 'Pasar lista, plan, aforo, sustituto u horario.', 1188),
  ('d04_04_lista', 'PASAR LISTA', 'Proyectar el QR, lista con foto o marcar el resto.', 63),
  ('d04_05_qr', 'PROYECTA EL QR', 'En la tele: cambia solo y cuenta quién va entrando.', 'E'),
  ('d04_05b_pizarra', 'O EN LA PIZARRA', 'Modo pizarra, en claro, para la pared del tatami.', 'E'),
  ('d04_07_mano', 'EL RESTO, A MANO', 'P, A o R por fila. Quien fichó con el QR ya está dentro.', 63),
  ('d04_08_resto', 'MARCAR RESTO', 'Un toque y la lista entera marcada.', 63)],
  ['LA PUERTA,', 'SIN LIBRETA.'], CENTRO)

C['dia-05'] = ('PASO A PASO · EL RANKING', ['MES NUEVO,', 'PODIO NUEVO.'],
  'Cada clase a la que vas suma. Podio por disciplina y por clase.', [
  ('d05_01_inicio', 'EN INICIO', 'Tu gente y el ranking del mes, a un toque.', 'E'),
  ('d05_02_podio', 'EL PODIO', 'Los tres de arriba, con sus puntos y cuánto queda para el cierre.', 'E'),
  ('d05_03_boxeo', 'POR DISCIPLINA', 'Boxeo, Muay Thai, MMA o jiu-jitsu: cada una con su podio.', 'E'),
  ('d05_04_nogi', 'Y POR CLASE', 'Solo NO-GI, solo Open Mat… Tú eliges.', 'E'),
  ('d05_05_reglas', 'CÓMO SE SUMA', 'Presente +10, retraso +6 y +5 por cada semana de racha.', 63),
  ('d05_06_desglose', 'CLASE A CLASE', 'Toca a cualquiera y ves de dónde sale cada punto.', 700),
  ('d05_07_racha', 'TU RACHA', 'Las semanas seguidas que llevas, y el club de la constancia.', 'E'),
  ('d05_08_cero', 'EL DÍA 1, A CERO', 'Mes nuevo, marcador en blanco: todos empiezan igual.', 'E')],
  ['CADA CLASE', 'SUMA.'], ALUMNO)

C['dia-06'] = ('PASO A PASO · LA CAJA', ['EL MES,', 'CUADRADO.'],
  'Lo cobrado y quién falta por pagar. Sin hoja de cálculo.', [
  ('d06_01_caja', 'LA CAJA', 'En Inicio: quién está vencido y su cobro, a un toque.', 'E'),
  ('d06_02_cuotas', 'LAS CUOTAS', 'Cobrado este mes, al día, vencen pronto y vencidos.', 63),
  ('d06_03_historial', 'SU FICHA DE PAGOS', 'Su tarifa y cada ciclo de cuota que ha pagado.', 1188),
  ('d06_04_registrar', 'REGISTRAR PAGO', 'El importe ya viene puesto. Efectivo, Bizum o transferencia.', 1000),
  ('d06_05_aldia', 'AL DÍA', 'Cuadra al momento: un vencido menos.', 63),
  ('d06_06_bonos', 'BONOS', 'Packs de clases que se descuentan solos al pasar lista.', 650),
  ('d06_07_tarifa', 'TARIFAS', 'Nombre, precio y las disciplinas que incluye.', 1188),
  ('d06_08b_recordar', 'LA APP LO RECUERDA', 'Avisa al alumno antes de que venza su cuota.', 700)],
  ['TÚ COBRAS,', 'LA APP CUENTA.'], 'La app lleva las cuentas, no el dinero. ' + CENTRO)

C['dia-08'] = ('PASO A PASO · EL PARTE', ['CADA ROLL,', 'APUNTADO.'],
  'El parte del día en 30 segundos: con quién, cómo acabó y con qué.', [
  ('d08_01_alacabar', 'AL ACABAR', 'En Hoy: «El parte de NO-GI está sin registrar».', 'E'),
  ('d08_02_sesion', '¿DE QUÉ CLASE?', 'Solo las clases a las que fuiste.', 63),
  ('d08_03_corro', 'EL CORRO', '¿Con quién rodaste? Solo salen los que estaban.', 63),
  ('d08_04_como', '¿CÓMO ACABÓ?', 'Sometí, tablas o me sometieron.', 780),
  ('d08_05_conque', '¿CON QUÉ?', 'Opcional: mataleón, kimura, triángulo…', 63),
  ('d08_06_tres', 'TRES ROLLS', 'Uno ganado, uno empatado, uno perdido. Guardar.', 63),
  ('d08_06b_guardado', 'APUNTADO', 'Tu marcador del mes, al día.', 'E'),
  ('d08_07_diario', 'TU DIARIO', 'Doce meses de rolls, sesión a sesión.', 63)],
  ['CADA ROLL', 'CUENTA.'], ALUMNO)

C['dia-09'] = ('PASO A PASO · EL TABLÓN', ['DICHO', 'UNA VEZ.'],
  'Se publica una vez en el tablón y lo ve todo el centro. Entra y sale solo.', [
  ('d09_01_tablon', 'EL TABLÓN', 'Arriba en Inicio, con su foto, rotando.', 'E'),
  ('d09_02_anuncios', 'TUS ANUNCIOS', 'Activos, programados y caducados.', 63),
  ('d09_03_nuevo', 'NUEVO ANUNCIO', 'Título, texto e imagen.', 63),
  ('d09_05_urgente', 'URGENTE O NO', 'En ámbar y el primero de la rotación, si quieres.', 63),
  ('d09_06_vigencia', 'ENTRA Y SALE SOLO', 'Cuándo termina, franja horaria o atado a una clase.', 63),
  ('d09_07_resumen', 'EL RESUMEN', 'Antes de publicar, todo en una línea.', 63),
  ('d09_02b_programados', 'PROGRAMADO', 'No ocupa sitio hasta que llega su momento.', 63),
  ('d09_08_loven', 'LO VE TODO EL CENTRO', 'Quién lo publicó y hasta cuándo está.', 'E')],
  ['UNA VEZ,', 'PARA TODOS.'], 'Sin grupos de WhatsApp. ' + CENTRO)

C['dia-10'] = ('PASO A PASO · DAR EL PESO', ['PESAJE EN', '12 DÍAS.'],
  'Anota tu peso, dile tu división y mira cuánto te falta para el pesaje.', [
  ('d10_01_aviso', '¿PESO DE HOY?', 'Si llevas más de una semana sin anotar, Hoy te lo pregunta.', 63),
  ('d10_02_hoja', 'UN NÚMERO', 'Y su contexto: en ayunas, tras entreno o con gi. La lesión se cruza sola.', 'E'),
  ('d10_04_torneo', 'TU TORNEO', 'Tu próxima inscripción de Smoothcomp y los días hasta el pesaje.', 270),
  ('d10_05_inscripcion', 'TU DIVISIÓN', 'Si no viene, la dices tú: división, límite y día del pesaje.', 'E'),
  ('d10_06_bascula', 'A RAYA', '0,3 kg por encima, tu ritmo y el que necesitas para llegar.', 290),
  ('d10_07_cuerpo', 'LA LÍNEA', 'Tu peso por quincenas, con tu límite y cada lesión encima.', 640),
  ('d10_08_objetivo', 'TU OBJETIVO', 'El límite de una de tus divisiones, o el número que quieras.', 1188),
  ('d10_10_privacidad', 'SOLO TÚ', 'Tu peso es privado de entrada. Tú decides si lo ven tus compañeros.', 63)],
  ['A DAR', 'EL PESO.'], 'Tu peso y tus lesiones solo los ves tú. ' + ALUMNO)

C['dia-11'] = ('PASO A PASO · LA TIENDA', ['LA TIENDA,', 'SIN MOSTRADOR.'],
  'Ellos apartan en la app y tú cobras al entregar.', [
  ('d11_02_nuevo', 'NUEVO ARTÍCULO', 'Foto, nombre, precio y si se publica ya.', 'E'),
  ('d11_03_tallas', 'TALLAS Y STOCK', 'Cada combinación con sus unidades. El color, sacado de la foto.', 63),
  ('d11_05b_inicio', 'EN INICIO', 'El escaparate, con foto y precio, a la vista de todos.', 'E'),
  ('d11_06_pedidos', 'TE LO APARTAN', 'Álex reserva unos guantes desde la app. Por entregar.', 63),
  ('d11_07b_menos', 'ENTREGAR Y COBRAR', '¿Falta algo? Que te lo deba o perdónaselo.', 450),
  ('d11_07d_hecho', 'QUEDA APUNTADO', 'Entregado, cobrado y lo que queda por cobrar.', 63),
  ('d11_08_vender', 'VENDER AHORA', 'En el mostrador: a quién, qué y cobrar.', 63),
  ('d11_08c_cobrar', 'EN TRES TOQUES', 'Dos vendas rojas, 16 €, por Bizum.', 63)],
  ['SIN COMISIONES,', 'SIN LIBRETA.'], 'La app lleva las cuentas, no el dinero. ' + CENTRO)

C['dia-12'] = ('PASO A PASO · TUS LOGROS', ['TU VITRINA,', 'CONTIGO.'],
  'Parches por asistencia, rachas y sparring, con su fecha.', [
  ('d12_01_perfil', 'EN TU PERFIL', 'Tus parches y los seis que ve el centro primero.', 'E'),
  ('d12_02_logros', 'TUS PARCHES', 'Por familias, y el nivel de tu vitrina.', 63),
  ('d12_03_fecha', 'CON SU FECHA', 'Cuándo lo ganaste y cuántos lo tienen en el centro.', 750),
  ('d12_04_falta', 'EL QUE TE FALTA', 'Cuánto te queda. Eso solo lo ves tú.', 750),
  ('d12_05_vitrina', 'TU VITRINA', 'Elige seis: es lo primero que ven de ti.', 1188),
  ('d12_06_sala', 'LA SALA DE TROFEOS', 'Todo el centro, con sus parches y sus puntos.', 'E'),
  ('d12_07_compara', 'COMPÁRATE', 'Lo que tiene él y lo que tienes tú.', 63),
  ('d12_08_privacidad', 'QUIÉN LOS VE', 'Todos, solo la vitrina o nadie.', 63)],
  ['CADA PARCHE,', 'CON FECHA.'], ALUMNO)

C['dia-13'] = ('PASO A PASO · LA FICHA', ['CADA ALUMNO,', 'SU FICHA.'],
  'Cuota, cinturón, asistencia y contacto en un solo sitio.', [
  ('d13_01_miembros', 'TU GENTE', 'Todos tus alumnos, con su cinturón.', 'E'),
  ('d13_02_samuel', 'LE TOCA', 'Samuel lleva más tiempo con su grado que la media del centro.', 700),
  ('d13_03_oscar', 'EL DINERO', 'Óscar: cuota vencida y un bono con tres clases.', 63),
  ('d13_04_nerea', 'FUERA DEL TATAMI', 'Nerea lo comparte: entrena a medias hasta fin de mes.', 520),
  ('d13_05_dentro_t', 'DENTRO DEL CENTRO', 'Ranking, clases, con quién rueda y quién le graduó.', 'E'),
  ('d13_06_contacto_t', 'CONTACTO', 'El teléfono solo lo ve quien gestiona miembros.', 'E'),
  ('d13_07_actividad', 'ACTIVIDAD', 'Doce semanas: cuándo viene, cancelaciones y faltas.', 63),
  ('d13_08a_cinturon', 'PROMOCIONA', 'Cinturón y grado, con fecha, desde su ficha.', 'E')],
  ['EL CENTRO,', 'EN ORDEN.'], CENTRO)

C['dia-15'] = ('PASO A PASO · COMPETICIÓN', ['COMPITES,', 'APARECE.'],
  'Vincula tu Smoothcomp y tu palmarés entra en tu ficha.', [
  ('d15_05_competicion', 'TU COMPETICIÓN', 'Victorias, por puntos o por sumisión, y eventos.', 'E'),
  ('d15_05b_desplegado', 'CADA COMBATE', 'Contra quién, cómo acabó y la medalla.', 63),
  ('d15_06_palmares', 'EL PALMARÉS', 'Año a año, evento a evento.', 63),
  ('d15_08_derrotas', 'TUS DERROTAS, TUYAS', 'El centro ve tus victorias. Las derrotas, si quieres.', 'E')],
  ['TU PALMARÉS,', 'EN TU FICHA.'], ALUMNO)

C['dia-16'] = ('PASO A PASO · SEGUIMIENTO', ['NADIE SE', 'DESCUELGA.'],
  'El termómetro te dice quién se está enfriando antes de que se vaya. Y le escribes tú.', [
  ('d16_01_aviso', 'EL AVISO', '«Óscar Lozano se está yendo.» Te enteras antes de que deje de venir.', 63),
  ('d16_02_oscar', 'SU FICHA', '54 sobre 100, y de qué está hecho: de 2,5 clases a la semana a 0,3.', 'E'),
  ('d16_04_cuentas', 'LAS CUENTAS', 'Cinco sumas, y cada una sale de algo que pasó, con su fecha.', 63),
  ('d16_03_hoy', 'CADA DÍA, EN HOY', 'Cuántos se enfrían y cuántos se van, a un toque.', 430),
  ('d16_05_tablero', 'EL TABLERO', 'Ordenados por lo que puedes hacer hoy, no por puntuación.', 'E'),
  ('d16_06_escribir', 'ESCRÍBELE TÚ', 'Tres arranques con sus datos dentro, y lo firmas tú.', 600),
  ('d16_10_aplazar', '¿DE VIAJE? APLÁZALO', 'Lo silencias hasta una fecha, con el motivo escrito para el resto del staff.', 63),
  ('d16_08_volvieron', 'VOLVIERON', 'Estaba frío y ha vuelto a entrenar. La lista que importa.', 380)],
  ['LO NOTAS', 'A TIEMPO.'], 'Lo escribe una persona, nunca la app. Incluido en tu centro. ' + CENTRO)

C['dia-17'] = ('PASO A PASO · CARA A CARA', ['CARA', 'A CARA.'],
  'Elige rival en el ranking y compárate: puntos, rachas y asistencia.', [
  ('d17_01_rival', 'ELIGE RIVAL', 'El que va justo delante. Toca «VS».', 'E'),
  ('d17_03_caraacara', 'EL COMBATE', 'El que defiende contra el aspirante, asalto a asalto.', 'E'),
  ('d17_06_remontada', 'LA REMONTADA', 'Octubre, día a día, y cuánto te separa.', 'E'),
  ('d17_08_espejo', 'EL ESPEJO', 'Así entrena cada uno, y dónde os cruzáis.', 'E')],
  ['TRES CLASES', 'Y ES TUYO.'], ALUMNO)

C['dia-18'] = ('PASO A PASO · EL CHAT', ['EL GRUPO,', 'SIN RUIDO.'],
  'El chat del centro, dentro de la app: con normas, denuncias y bloqueo.', [
  ('d18_01b_conversacion', 'EL CHAT DEL CENTRO', 'Un solo grupo para todo el centro.', 420),
  ('d18_03_pulsado', 'MANTÉN PULSADO', 'Responder, copiar, denunciar o bloquear.', 1188),
  ('d18_04_motivo', '¿QUÉ PASA?', 'Spam o publicidad. No sabrá quién le ha denunciado.', 63),
  ('d18_05_registrada', 'REGISTRADA', 'Quién la ve y qué puede pasar.', 1000),
  ('d18_06_bloquear', 'BLOQUEAR', 'Dejáis de veros en el chat. Sigue en el centro.', 650),
  ('d18_07_bandeja', 'LA BANDEJA', 'Las denuncias, solo para el admin y los coaches.', 63),
  ('d18_08_resuelve', 'RESUELVE', 'Borrar, avisar al autor o desestimar.', 63),
  ('d18_08c_retirado', 'RETIRADO', '«Mensaje retirado por incumplir las normas».', 1000)],
  ['CON NORMAS', 'DE VERDAD.'], CENTRO)

C['dia-19'] = ('PASO A PASO · TU CINTURÓN', ['TU CINTURÓN', 'TIENE HISTORIA.'],
  'Cada grado con su fecha y quién te lo dio.', [
  ('d19_01_ficha', 'LE TOCA', 'Tu coach ve cuánto llevas con tu grado.', 'E'),
  ('d19_02_promocionar', 'PROMOCIONAR', 'Disciplina, cinturón y grados.', 950),
  ('d19_04_promocionado', 'TE HAN PROMOCIONADO', '«¡Enhorabuena! Sigue así.»', 63),
  ('d19_05_perfil', 'EN TU PERFIL', 'Tu cinturón nuevo, a la vista.', 63),
  ('d19_06_ficha_desplegada_t', 'TÚ DECIDES', 'Qué ve tu centro de ti y qué no.', 600),
  ('d19_07_linaje_t', 'EL LINAJE', 'Quién te graduó, y quién le graduó a él.', 950)],
  ['CADA GRADO,', 'CON FIRMA.'], ALUMNO)

C['dia-20'] = ('PASO A PASO · ADMISIONES', ['LA PUERTA,', 'CON CRITERIO.'],
  'Tú decides cómo se entra en tu centro.', [
  ('d20_01_politica', 'CÓMO SE ENTRA', 'Abierto, bajo solicitud, solo invitación o secreto.', 63),
  ('d20_02_pide', 'LA PIDE', 'Hugo encuentra el centro en el mapa y pide plaza.', 'E'),
  ('d20_03_aviso', 'TE AVISA', 'Solicitudes pendientes, en Inicio.', 'E'),
  ('d20_05_pendientes', 'PENDIENTES', '«Solicita entrar como alumno». Aceptar o rechazar.', 63),
  ('d20_06_historial', 'HISTORIAL', 'Cada solicitud: quién, por quién y cuándo.', 63),
  ('d20_07_lellega', 'LE LLEGA', '«Te han aceptado en Villalba Fighting Co.»', 63),
  ('d20_08_miembros', 'YA ES DE LOS TUYOS', 'Hugo, en Alumnos, desde hoy.', 'E')],
  ['TU GENTE,', 'DENTRO.'], CENTRO)

C['dia-21'] = ('STRIFE · UN DÍA EN TU CENTRO', ['UN DÍA', 'EN TU CENTRO.'],
  'Villalba Fighting Co., de la mañana a la noche. Todo en la misma app.', [
  ('d06_01_caja', '09:00 · LA CAJA', 'Con el café: quién está vencido y su cobro, a un toque.', 'E'),
  ('d20_05_pendientes', '13:30 · UNA SOLICITUD', 'Hugo pide plaza. Aceptar o rechazar, desde el móvil.', 63),
  ('d03_01_hoy', '18:00 · ¿VAS?', 'Álex tiene su clase de la tarde reservada.', 63),
  ('d04_05_qr', '19:58 · EL QR', 'En la tele de la entrada. Cambia solo y cuenta quién va entrando.', 'E'),
  ('d04_04_lista', '20:00 · LA LISTA', 'Quien fichó con el QR ya está dentro. El resto, de un toque.', 63),
  ('d08_06_tres', '21:30 · LOS ROLLS', 'Álex apunta con quién rodó y cómo acabó.', 63),
  ('d16_05_tablero', '22:00 · EL TERMÓMETRO', 'Quién se está enfriando, antes de que se vaya.', 400)],
  ['TU GIMNASIO,', 'EN UNA APP.'], CENTRO)

C['dia-24'] = ('PASO A PASO · TU CUOTA', ['TU CUOTA,', 'CLARA.'],
  'Cuánto pagas y hasta cuándo está cubierta, en tu perfil.', [
  ('d24_01_aviso', 'EL AVISO', '«Tu cuota vence hoy · se paga en recepción».', 63),
  ('d24_02_micuota', 'MI CUOTA', 'Tu tarifa y hasta cuándo estás cubierto.', 'E'),
  ('d06_04_registrar', 'EN RECEPCIÓN', 'Pagas en el centro y lo registran en dos toques.', 1000),
  ('d24_06_aldia', 'AL DÍA', 'Y en tu perfil, cubierta hasta el mes que viene.', 'E')],
  ['SIN SORPRESAS', 'A FIN DE MES.'], ALUMNO)

C['dia-25'] = ('PASO A PASO · INVITAR', ['INVITA EN', 'UN TOQUE.'],
  'Tenga la app o no.', [
  ('d25_01_invitar', 'INVITAR', 'Email, @usuario o nombre: un solo buscador.', 560),
  ('d25_02_buscalo', 'BÚSCALO', 'Por su nombre.', 560),
  ('d25_03_rol', 'CON QUÉ ROL', 'Alumno, entrenador o administrador.', 300),
  ('d25_05_compartir', '¿NO TIENE LA APP?', 'Mándale el enlace a Google Play por WhatsApp.', 1188),
  ('d25_06_pendiente', 'PENDIENTE', 'La invitación, con su fecha de caducidad.', 1100),
  ('d25_07_lellega', 'LE LLEGA', 'Aceptar o rechazar, desde el aviso.', 63),
  ('d25_08_miembro', 'YA ES MIEMBRO', '«Ya eres miembro de Villalba Fighting Co.»', 'E')],
  ['TU GENTE,', 'DENTRO.'], CENTRO)

C['dia-26'] = ('PASO A PASO · TU CLASE', ['SABES', 'A QUÉ VAS.'],
  'El plan de hoy, el coach y quién va, antes de pisar el tatami.', [
  ('d26_01_hoy', 'LAS DE HOY', 'Despliega: aforo, quién va y reserva.', 'E'),
  ('d26_02_clase', 'LA CLASE', 'Cuándo, cuánto dura, para quién y quién la da.', 63),
  ('d26_03_plan', 'HOY TRABAJAMOS', 'Lo que ha preparado tu coach.', 63),
  ('d26_04_sala', 'QUIÉN VA', 'Van once. Con quién empezar y con quién exigirte.', 63),
  ('d26_06_ruben', '¿CON QUIÉN?', 'Toca a cualquiera: su cinturón, sus parches y su juego.', 'E'),
  ('d26_08_exportar', 'A TU CALENDARIO', 'Las próximas cuatro semanas, en el calendario del móvil.', 1188)],
  ['SABES', 'A QUÉ VAS.'], ALUMNO)

C['dia-27'] = ('PASO A PASO · TU CENTRO', ['TU CENTRO,', 'LO PRIMERO.'],
  'Tu foto, tu emblema y si hoy está abierto.', [
  ('d27_01_portada', 'LA PORTADA', 'Foto, emblema, «Abierto» y disciplinas.', 'E'),
  ('d27_02_ficha', 'LA FICHA', 'Horario de la semana, hoy resaltado, y cómo llegar.', 560),
  ('d27_04_perfil', 'LOGO Y PORTADA', 'Se cambian desde la cabecera.', 63),
  ('d27_05_info', 'DESCRIPCIÓN E INSTAGRAM', 'Lo que eres, en una línea, y tu @.', 63),
  ('d27_05b_horario', 'EL HORARIO', 'Franjas por día. Se guarda solo.', 63),
  ('d27_06_colores', 'TUS COLORES', 'La paleta de tu centro, en toda la app.', 300),
  ('d27_08_asilove', 'ASÍ LO VEN', 'La misma portada, en el móvil de cada alumno.', 'E')],
  ['UNA APP', 'CON TU CARA.'], CENTRO)

C['dia-28'] = ('STRIFE · EN MARCHA', ['EN MARCHA', 'EN 5 PASOS.'],
  'Tu centro en STRIFE, esta semana. Y lo que cuesta, claro.', [
  ('d02_05_dias', 'PON EL HORARIO', 'Una vez, y el mes entero se rellena solo.', 63),
  ('d25_03_rol', 'INVITA A TU GENTE', 'Por @usuario, por correo o por WhatsApp.', 300),
  ('d04_04_lista', 'PASA LISTA', 'Con el QR, con una foto o a mano.', 63),
  ('d06_04_registrar', 'COBRA', 'Cada cuota, con su importe ya puesto. Efectivo, Bizum o transferencia.', 1000),
  ('dia-28/d28_05_suscripcion', 'LO QUE CUESTA', '30 días gratis. Después, 14,99 €/mes con todo dentro.', 63)],
  ['30 DÍAS', 'GRATIS.'], 'Para tu centro, y luego 14,99 €/mes. Atletas y coaches, gratis siempre.')

C['dia-29'] = ('PASO A PASO · MI JUEGO', ['TU JUEGO,', 'EN DATOS.'],
  'Lo que rematas, lo que te rematan y contra quién.', [
  ('d29_01_perfil', 'EN TU PERFIL', 'Tu arma, tu grieta y cuánto acabas.', 'E'),
  ('d29_02_mes', 'EL MES', 'Sometí, tablas, me sometieron, y el balance.', 63),
  ('d29_03_juego', 'TU JUEGO', 'Con qué rematas y con qué te rematan.', 63),
  ('d29_04_escalada', 'LA ESCALADA', 'Doce meses, y el día en que el balance cruzó.', 63),
  ('d29_05_peso', 'EL PESO IMPORTA', 'Cuánto acabas con los más ligeros, los parejos y los pesados.', 63),
  ('d29_06_rivales', 'TUS RIVALES', 'Con quién ruedas más este mes.', 63),
  ('d29_07_ruben', 'TÚ CONTRA RUBÉN', 'Vuestros últimos rolls, del más antiguo al último.', 'E'),
  ('d29_08_privacidad', 'SI QUIERES, QUE LO VEAN', 'Mi juego en tu perfil. Nunca con quién rodaste.', 63)],
  ['CADA ROLL', 'SUMA.'], ALUMNO)

V2 = 'serie-v2/capturas/guias/'
C['guia-clases'] = ('GUÍA · LA TAB CLASES', ['TU HORARIO,', 'EN UNA TAB.'],
  'Por semana, por mes o en lista. Reservas con un toque y ves quién más va.', [
  ('clases/gc_01_semana', 'TU SEMANA', 'Cada clase con su color, día a día. Las canceladas, tachadas.', 'E'),
  ('clases/gc_02_mes', 'O POR MES', 'Todo octubre de un vistazo, hoy resaltado.', 380),
  ('clases/gc_03_lista', 'O EN LISTA', 'Con el coach, el aforo y las caras de quien ya va.', 63),
  ('clases/gc_04_sesion', 'SABES A QUÉ VAS', 'La ficha de la clase: cuándo, cuánto dura y la sala de hoy.', 'E'),
  ('clases/gc_05_voy', 'VOY.', 'Un toque en «Asistiré» y estás en la lista. ¿No vas? Avisa y tu hueco lo pilla otro.', 860),
  ('clases/gc_06_misemana', 'MI SEMANA', 'Tu racha, tu próxima clase y lo que ya pasó esta semana.', 63)],
  ['RESERVA', 'EN UN TOQUE.'], ALUMNO)

C['guia-juego'] = ('GUÍA · MI JUEGO', ['UN ROLL,', 'DOS PARTES.'],
  'Lo apuntas tú y a tu compañero le aparece solo, con el resultado dado la vuelta.', [
  ('juego/gj_01_parte_alex', 'TU PARTE', 'Álex añade dos rolls con Miguel a su parte del domingo.', 880),
  ('juego/gj_02_aviso', 'LE LLEGA', '«Álex Romero ha registrado 2 rolls contigo en NO-GI.»', 63),
  ('juego/gj_03_suparte', 'YA ESTÁ EN SU PARTE', 'La kimura de Álex, en el parte de Miguel como «Sometí». Sin tocar nada.', 200),
  ('juego/gj_04_hoy', 'Y EN SU HOY', 'Su mes al día: 1 · 1 · 0 y todos los partes hechos.', 780),
  ('juego/gj_05_mijuego', 'CUENTA PARA LOS DOS', 'Su arma del mes, su balance y su escalada.', 63),
  ('juego/gj_06_quien', 'QUIÉN MÁS LO VE', 'Solo el rival de cada roll. El coach, agregados anónimos.', 800)],
  ['EL SPARRING,', 'CONTADO.'], 'Si tu compañero lo anota, también sale en tu diario. ' + ALUMNO)

C['guia-centro'] = ('GUÍA · TU CENTRO EN INICIO', ['TU CENTRO,', 'TU CASA.'],
  'La portada, el tablón, tu gente, la tienda y la caja, en la primera pestaña.', [
  ('centro/ce_01_inicio', 'LA PORTADA', 'Tu foto, tu emblema, si hoy está abierto y tus disciplinas.', 'E'),
  ('centro/ce_01_inicio', 'EL TABLÓN', 'Lo que has publicado, pasando solo. Un toque y lo lee entero.', 820),
  ('centro/ce_02_gente', 'TU GENTE', 'Cuántos sois, los cinturones y quién lidera el ranking.', 950),
  ('centro/ce_03_tienda_caja', 'LA TIENDA', 'Lo vendido este mes, lo que queda y quién debe.', 800),
  ('centro/ce_03_tienda_caja', 'LA CAJA', 'Las cuotas del mes: lo cobrado y cuántos están al día.', 1300),
  ('dia-20/d20_03_aviso', 'Y LO QUE ESPERA', 'Una solicitud nueva sale arriba, antes que nada.', 'E')],
  ['UNA APP,', 'TODO EL CENTRO.'], CENTRO)

C['guia-asistencia'] = ('GUÍA · PASAR LISTA', ['LA LISTA,', 'DESPUÉS.'],
  'Cerraste la puerta y quedan huecos. La lista del domingo se arregla el lunes.', [
  ('asistencia/ga_01_lista', 'SIGUE ABIERTA', 'La del domingo: 8 de 17 marcados y 9 sin marcar.', 63),
  ('asistencia/ga_02_marcas', 'QUIEN NO VINO', 'Dani reservó y no apareció: ausente. Diego llegó tarde: retraso.', 'E'),
  ('asistencia/ga_03_buscar', 'SE TE PASÓ ALGUIEN', 'Nerea vino sin reservar. La buscas por su nombre y la marcas.', 400),
  ('asistencia/ga_04_antes', '¿TARDE?', 'Diego, con su retraso: +6 en vez de +10.', 700),
  ('asistencia/ga_04_perdon', '¿LO VES JUSTO?', 'Un toque en P y el retraso pasa a presente.', 700),
  ('asistencia/ga_05_final', 'CUADRADA', '11 de 17: 10 presentes y 1 ausente. Y el ranking, al día.', 63)],
  ['LA PUERTA,', 'SIN LIBRETA.'], 'Pasar lista, también al día siguiente. ' + CENTRO)

C['guia-miembros'] = ('GUÍA · MIEMBROS', ['CADA ALUMNO,', 'UNA FICHA.'],
  'Cómo viene, cuándo viene, si se está enfriando y qué puede hacer en tu centro.', [
  ('miembros/gm_01_miembros', 'TU GENTE', 'Staff y alumnos, con su cinturón. Y el termómetro, arriba.', 'E'),
  ('miembros/gm_02_ficha', 'CÓMO VIENE', 'Rubén: 5,7 clases por semana, su media son 2,9. En racha.', 63),
  ('miembros/gm_03_actividad', 'CUÁNDO VIENE', 'Doce semanas, sus clases fijas y si cancela o falta.', 63),
  ('miembros/gm_04_seguimiento', 'SU TERMÓMETRO', 'De qué está hecha su puntuación, señal a señal.', 640),
  ('miembros/gm_06_acceso', 'ANTES DE TOCAR', 'Lo que hace cada rol se decide en Ajustes. Aquí, solo excepciones.', 63),
  ('miembros/gm_07_permisos', 'SU ROL', 'Alumno, entrenador o administrador. Y cada permiso, a mano si hace falta.', 600)],
  ['EL CENTRO,', 'EN ORDEN.'], CENTRO)

C['guia-invitar'] = ('GUÍA · INVITAR', ['AÚN NO TIENE', 'CUENTA.'],
  'Invítale con su correo y la invitación le espera hasta que se registre.', [
  ('invitar/gi_02_nadie', 'NO ESTÁ', '«Nadie se llama así en STRIFE.» ¿Tienes su correo?', 300),
  ('invitar/gi_03_correo', 'SU CORREO', '«Aún no hay cuenta con ese correo: la invitación quedará esperando.»', 300),
  ('invitar/gi_03_correo', 'CON QUÉ ROL', 'Alumno, entrenador o administrador.', 900),
  ('invitar/gi_04_creada', 'CREADA', 'La verá al registrarse con ese correo. Caduca en un mes.', 1300)],
  ['TU GENTE,', 'DENTRO.'], CENTRO)

C['guia-lesion'] = ('GUÍA · TU CUERPO EN 3D', ['HASTA EL', 'LIGAMENTO.'],
  'Apunta una lesión en la silueta, concrétala en 3D y mira cuánto te cuesta.', [
  ('lesion/l03_queha', '¿QUÉ HA PASADO?', 'Lesión, enfermedad o piel. Y el tipo: esguince, rotura, luxación…', 63),
  ('lesion/l04_zona', 'MARCA DÓNDE', 'Toca la zona en la silueta, por delante o por detrás.', 'E'),
  ('lesion/l05_3d', 'CONCRÉTALO EN 3D', 'El hombro en 3D: por fuera, de frente, por dentro y por detrás.', 63),
  ('lesion/l06c_interna', 'SIN MÚSCULOS', 'Filtra por articulaciones y los músculos se vuelven transparentes.', 63),
  ('lesion/l06_ahiesta', 'AHÍ ESTÁ', 'Ligamento glenohumeral inferior: se ilumina en el modelo.', 63),
  ('lesion/l07_cuanto', 'CUÁNTO TE FRENA', 'Desde cuándo y cuánto: normal, a medias o fuera del tatami.', 'E'),
  ('lesion/l11_episodio', 'TU EPISODIO', 'Dónde, qué, desde cuándo y tu peso durante la lesión.', 1100),
  ('lesion/l12_compartir', '¿SE LO DICES?', 'Solo que estás fuera, y si quieres hasta cuándo. Ni el qué ni dónde.', 900)],
  ['TUS DATOS', 'SON TUYOS.'], ALUMNO)

C['guia-lesion-juego'] = ('GUÍA · LA LESIÓN EN TU JUEGO', ['TOCADO,', 'PERO CONTADO.'],
  'Lo que te frena una lesión, en tu sparring, en tu diario y en tu centro.', [
  ('lesion/l08_guardado', 'TOCADO', 'Tu estado, arriba en Cuerpo. Y la lesión sobre tu curva de peso.', 63),
  ('lesion/j01_hoy', 'CADA PARTE, CON LO SUYO', 'Tus partes de sparring llevan la lesión que tenías ese día.', 900),
  ('lesion/j02_parte', 'RODASTE CON…', '«Rodaste con luxación, fuera del tatami.» Y aun así, tres rolls.', 63),
  ('lesion/j03_diario', 'EL DIARIO LO MARCA', 'Desde que te lesionaste, cuántos rolls haces y cuánto acabas.', 400),
  ('lesion/j03b_diario', 'SESIÓN A SESIÓN', 'Cada clase con el episodio que tenías entonces.', 63),
  ('lesion/l13_coach', 'LO QUE VE TU COACH', 'Solo «fuera del tatami». Nadie pregunta, y nadie te escribe por faltar.', 520),
  ('lesion/l10_cerrar', 'YA ESTOY BIEN', 'Un toque y se cierra. Tu curva y tu juego vuelven a lo normal.', 'E')],
  ['VUELVES', 'CUANDO TOCA.'], ALUMNO)

C['guia-peso'] = ('GUÍA · TU PESO', ['EL PESO,', 'A RAYA.'],
  'Un año de registros, cada lesión encima de la curva y el margen hasta tu categoría.', [
  ('peso/p01_cuerpo', 'TU CUERPO', 'Peso, estado y lo que llevas este año, en una pantalla.', 'E'),
  ('peso/l02_anotar', 'ANOTA', 'Un número y su contexto. La lesión abierta se cruza sola.', 63),
  ('peso/p03_meses', 'UN AÑO ENTERO', 'Media y rango por meses, con cada lesión encima.', 700),
  ('peso/p02b_sinepisodios', 'O SIN EPISODIOS', 'Apágalos y queda la curva limpia.', 700),
  ('peso/p04_registros', 'CADA REGISTRO', 'Los últimos 90 días, registro a registro.', 63),
  ('peso/p05_diario', 'EL CRUCE', 'Cuánto te mueven las lesiones y los días que te dejaron fuera.', 1188),
  ('peso/pe03_objetivo', 'TU OBJETIVO', 'Los límites de tus categorías, o el número que quieras.', 1188),
  ('peso/pe01_bascula', 'TU CATEGORÍA', 'Con gi y sin gi: tu límite y el margen que te queda.', 900)],
  ['TU PESO,', 'TUYO.'], 'Peso y lesiones solo los ves tú. ' + ALUMNO)

C['guia-aparte'] = ('GUÍA · EL APARTE', ['SOLO TÚ', 'Y TU CENTRO.'],
  'Un hilo privado con tu centro. Lo que no dirías en el chat de todos.', [
  ('aparte/ap01_hoy', 'EN HOY', 'El aparte, con el último mensaje de tu centro.', 'E'),
  ('aparte/ap02_hilo', 'EL HILO', 'Solo entre tú y el centro. Nadie más del grupo lo ve.', 'E'),
  ('aparte/ap04_enviado', 'CONTESTA', 'Cuando quieras y como quieras.', 1000),
  ('lesion/l13_coach', 'LO QUE VE TU CENTRO', 'Tu ritmo, no tus datos. Si estás lesionado, solo «fuera del tatami».', 520),
  ('aparte/ap06_coach', 'LO ESCRIBE UNA PERSONA', 'Tu coach elige cómo decírtelo y lo firma con su nombre.', 1000),
  ('aparte/ap08_lellega', 'TE LLEGA', 'Como mensaje de tu centro, nunca como aviso automático.', 1000)],
  ['HABLA', 'CON TU CENTRO.'], ALUMNO)

C['guia-avisos'] = ('GUÍA · LOS AVISOS', ['SOLO LO', 'QUE IMPORTA.'],
  'Tu cuota, tus clases, tus ascensos y tus rolls. Y tú eliges cuáles.', [
  ('avisos/av01_campana', 'LA CAMPANA', 'Cuota, pedidos, ascensos y clases canceladas, en un sitio.', 'E'),
  ('avisos/av02_abre_t', 'UN TOQUE Y VAS', 'Cada aviso te lleva a lo suyo: un ascenso, a tu cinturón.', 63),
  ('avisos/av04_tramo1', 'TÚ ELIGES', 'Ajustes › Notificaciones: cinturones, clases y sparring.', 600),
  ('avisos/av04_tramo2', 'Y TU TIENDA', 'Tu pedido te espera, pedido actualizado o anulado.', 1100)],
  ['ENTÉRATE', 'A TIEMPO.'], ALUMNO)


for pid, (label, cover, lead, pasos, cierre, lead_cierre) in C.items():
    slides = [{'cover': cover, 'lead': lead}]
    for k, (cap, title, sub, b) in enumerate(pasos, 1):
        if cap.startswith(('serie-v2/', 'reel/')):
            ruta = None
        elif '/' in cap:
            ruta = cap
        else:
            carpeta = 'dia-24' if cap.startswith('d24') else ('dia-06' if cap.startswith('d06') else 'dia-' + cap[1:3])
            ruta = f'{carpeta}/{cap}'
        s = {'num': f'{k:02d}', 'title': title, 'cap': cap if ruta is None else f'serie-v3/capturas/{ruta}', 'sub': sub}
        if b == 'E':
            s['modo'] = 'entero'
        else:
            s['b'] = b
        slides.append(s)
    slides.append({'cover': cierre, 'lead': lead_cierre, 'tag': 'YA EN GOOGLE PLAY'})
    json.dump({'id': pid, 'label': label, 'slides': slides}, open(os.path.join(AQUI, pid + '.json'), 'w'),
              ensure_ascii=False, indent=1)
    print(pid, len(slides))
