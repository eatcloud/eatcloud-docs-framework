# proceso-envío-de-notificación-dona-no-adjudicadas.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para enviar una notificación diferentes correos de ABACO e EatCloud, ante una donación de más de 500 KG, que no hallan sido adjudicadas después de dos horas de ser creadas. 
&#160; 
 Por lo tanto el sistema deberá invocar el servicio mediante un cronjob que corra cada 30 minutos, evaluando datos de la fecha y hora de publicación y comparándola con la fecha y hora actual.&#160; Si el lapso de tiempo ha sido superior a 2 horas, es decir que la donación de más de 500 KG, no ha sido adjudicada, entonces se generará un correo electrónico avisando de esta condición. 
&#160; 
 MENSAJE PARA ANUNCIAR LA NO ADJUDICACIÓN DE UNA DONACIÓN DE MÁS DE 500 KG DESPUÉS DE DOS HORAS DE SER PUBLICADA 
&#160; 
 Se implementará una mejora, que generará un mensaje por correo electrónico donaciones de más de 500 KG no han sido adjudicadas en un periodo de dos (2) horas contadas a partir de la fecha y hora de publicación de la donación.&#160; Inicialmente se activará el servicio para la cua_master ABACO, con posibilidad de activarlo luego para mexico, después de socializa 
&#160; 
 Consulta de los datos del encabezado del anuncio de donación&#58; 
&#160; 
 El sistema realizará la siguiente consulta (cada vez que corra el cronjob) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date&#123;0]=&#123;&#123;fecha_actual&#125;&#125;&amp;eatc-publication_date&#123;1]=&#123;&#123;fecha_actual&#125;&#125;&amp;eatc-state= announced &amp; eatc-total_weight_kg=_&gt;_500&amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-total_cost,eatc_closer_expiration_date&#160; 
&#160; 
 Si la anterior consulta no arroja resultados el sistema no genera ningún mensaje. 
&#160; 
 Con los resultados obtenidos, el sistema evalúa,&#160; con respecto a la fecha y hora actual el dato recibido en &quot; eatc_dona_headers.eatc-publication_datetime &quot;.&#160; Para cada uno de los anuncios cuyas fechas de publicación tienen más de dos horas de antiguedad, con respecto a la actual, el sistema realiza las siguientes consultas. 
&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; &amp; eatc_doma_id = not_adjudication_email 
&#160; 
 Si existen registros en esta tabla, para dichos anuncios no se prosigue con el proceso. 
&#160; 
 Para aquellos anuncios que no poseean registros en la anterior tabla, el sistema sigue adelante con las demás consultas&#58; 
&#160; 
 Consulta de los datos del detalle del anuncio de donación&#58; 
&#160; 
 A partir de los datos consultados y para cada uno de los anuncios cuya fecha de publicación tiene más de dos horas de antiguedad, el sistema realizará la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers&#125;&#125;&amp;_cmp= eatc-odd_id ,eatc-odd_name,eatc-odd_quantity,eatc-odd_total_weight_kg ,eatc-odd_total_cost&#160; 
&#160; 
 Con los datos obtenidos, se construirá el mensaje más adelante. 
&#160; 
 Para cada anuncio de uno de anuncios encontrados, se determina uno de los correos al cuál se debe enviar el mensaje&#58; 
&#160; 
 A partir del dato de cada uno de los anuncios de más de 500 KG cuya publicación ha sido hace más de dos horas de la fecha y hora actual&#58; 
 eatc_dona_headers. eatc-donor 
&#160; 
 Que llega de una consultaa anterior, el sistema realizará la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua&amp;fieldvalue=&#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125;&amp;fielddecrypt= eatc_customer_fiscal_id 
&#160; 
 Con el dato desencriptado eatc_customers_cua. eatc_customer_fiscal_id obtenido, el sistema realiza la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers&amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123; eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125;&amp;fielddecrypt= eatc_email &#160; 
&#160; 
 Con el dato del correo desencriptado ( eatc_customers. eatc_email ) , los datos anteriormente consultados y los datos de invocación del servicio&#58; 
 eatc_user &#160; 
 eatc_doma &#160; 
&#160; 
Se toman los correos adicionales a eatc_customers.eatc_mail del parámetro &#123;&#123;array_destinatarios_internos&#125;&#125; de la cuenta maestra 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123;eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
&#160; 
 se genera el siguiente correo electrónico&#58; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; ,&#123;&#123;eatc_customers. eatc_email &#125;&#125; 
&#160; 
 Deprecado (anteriormente)&#58; 
 From&#58; noreply@eatcloud.com 
 to&#58; soporte@eatcloud.com ,donaciones@abaco.org.co,ingridbrawn@abaco.org.co,&#123;&#123;eatc_customers. eatc_email &#125;&#125; 
&#160; 
&#160; 
 Asunto&#58; Anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; no ha sido adjudicado 
&#160; 
 Cuerpo&#58; 
 El anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; no ha sido adjudicado después de más de 2 horas de publicación.&#160; El anuncio fue publicado para el punto de donación &#123;&#123; eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123; eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123; eatc_dona_headers. eatc-total_weight_kg &#125;&#125;, un costo de &#123;&#123; eatc_dona_headers. eatc-total_cost &#125;&#125;, una fecha más próxima de vencimiento &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; y contenía los siguientes productos&#58; 
&#160; 
 ***Con los datos de cada uno de los detalles de donación (eatc_dona) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Nombre&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Cantidad&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Costo total 
 | &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; “Cada Kilo Cuenta” 
&#160; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados de la donación no entregada que fue informada mediante email. ***Nuevo &#58; se escriben los correos de acuerdo a la consulta del &#123;&#123;array_destinatarios_internos&#125;&#125; en el paso anterior *** 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; * 
 eatc-state = announced&#160; ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;*** 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; *** Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 
 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;array_destinatarios_internos&#125;&#125;, &#123;&#123;eatc_customers. eatc_email &#125;&#125;, informando que el anuncio de donación de más de 500 KG no ha sido adjudicado después de 2 horas de ser publicado 
 eatc_doma_id = not_adjudication_email&#160; ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; &#160; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
&#160; 
 ***NUEVO&#58; MENSAJE PARA ANUNCIAR LA NO ADJUDICACIÓN DE UNA DONACIÓN. &#160;Un día posterior a ser anunciada *** 
&#160; 
 Se implementará una mejora, que generará un mensaje por correo electrónico donaciones no adjudicadas. ABACO Solicita que el mensaje de alerta se genere de lunes a viernes, y que se de 1 dia posterior a ser anunciado. 
 Consulta de los datos del encabezado del anuncio de donación&#58; 
Determinación de la fecha de publicación (un día anterior a la actual) 
El sistema debe determinar la fecha de publicación con la cual se consultarán los anuncios, siendo igual a la fecha actual menos un día&#58; 
 &#123;&#123;fecha_publicacion_consulta&#125;&#125; = &#123;&#123;fecha_actual&#125;&#125; - 1 día 
Determinación de la fecha de publicación (un día anterior a la actual) 
&#160; 
Programación cronjob para la corrida del proceso 
Se deberá programar un cronjob que corra cada dos horas, en horario de 7 am a 6 pm de lunes a viernes. 
&#160; 
Consulta de anuncios no adjudicados 
 El sistema realizará la siguiente consulta (cada vez que corra el cronjob) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date=&#123; &#123;&#123;fecha_publicacion_consulta&#125;&#125; &amp;eatc-state= announced &amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-total_cost,eatc_closer_expiration_date&#160; 
&#160; 
 Si la anterior consulta no arroja resultados el sistema no genera ningún mensaje. 
&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente cada uno de los anuncios que se encontraron en la anterior consulta, iterando por cada código de anuncio (eatc_dona_headers. eatc-code ), la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; &amp; eatc_doma_id = not_adjudication_email &amp;_cmp= eatc_dona_header_code 
Se obtiene entonces un &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; 
&#160; 
Si el &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; es igual al array de &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; de la &#160;primera consulta, entonces el mensaje no se envía.&#160; 
&#160; 
 Si el array es menor, entonces se depura la consulta inicial de la siguiente manera&#58; &#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date=&#123; &#123;&#123;fecha_publicacion_consulta&#125;&#125; &amp;eatc-state= announced&amp; eatc-code= _nin_ &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; &amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg, eatc-state ,eatc_closer_expiration_date&#160; 
Con los datos recibidos y a los correos que se definen en la siguiente consulta, se les envía un correo. 
&#160; 
&#160; 
Consulta de destinatarios del correo &#123;&#123;array_destinatarios_internos&#125;&#125; &#58; dato en el parámetro&#160;eatc_customers. eatc_mail de la cuenta maestra *** 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123;eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
&#160; 
 ***NUEVO&#58; Consulta de e-mail de Bancos de Alimentos a los cuales se les asignó la donación *** &#160; 
El sistema realiza la siguiente consulta para cada donación a la cuál se le envía mensaje&#58; 
&#160; 
&#123;&#123;URL__beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_match_registry?eatc-dona_header_code= &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; &amp;_cmp= eatc-donation_manager_code 
con el dato o los datos obtenidos se realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL__beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro= &#123;&#123; eatc_match_registry. eatc-donation_manager_code &#125;&#125; &amp;_cmp =correo_electronico 
 Las respuestas obtenidas se almacenan en la variable 
&#160; 
 &#123;&#123;array_destinatarios_externos&#125;&#125; = &#123;&#123; eatc_donation_managers. correo_electronico &#125;&#125; 
&#160; 
 se genera el siguiente correo electrónico&#58; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; 
 cc &#58; &#123;&#123;array_destinatarios_externos&#125;&#125; ***NUEVO&#58; se envía correo a los Bancos de Alimentos a los cuales el anuncio les hace match 
&#160; 
&#160; 
&#160; 
 Asunto&#58; Anuncios de donación que no han sido adjudicados después de 1 día de su publicación 
&#160; 
 Cuerpo&#58; 
&#160; 
Se han encontrado los siguientes anuncios de donación pendientes de adjudicación 1 día después de su fecha de publicación. 
&#160; 
 Los sigientes anuncios de donación&#160; no ha sido adjudicados después de más de 2 horas de publicación&#58; 
&#160; 
 ***Con los datos de cada uno de los anuncios donación (eatc_dona_headers) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Fecha y hora de publicación &#160; &#160; &#160; &#160; &#160; &#160;| Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Estado &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;| Fecha próxima de vencimiento 
 | &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-publication_datetime &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-total_weight_kg &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; 
&#160; 
 Recuerda que se envía un solo correo por anuncio. 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; &quot;Cada Kilo Cuenta&quot; 
&#160; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
 Escritura en el historial de estados de la donación no entregada que fue informada mediante email. 
 Para cada uno de los anuncios relacionados en la tabla del correo, se realizará esta escritura en el historial de cambios de estados de las donaciones ( eatc_dona_header_state_history ). 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; * 
 eatc-state = announced ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;*** 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; ***Fecha y hora de envío del correo*** 
 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;array_destinatarios_internos&#125;&#125;, informando que el anuncio de donación no ha sido adjudicado después de un día de ser publicado 
 eatc_doma_id = not_adjudication_email ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
&#160; 
 ***NUEVO&#58; MENSAJE PARA ANUNCIAR LA NO ADJUDICACIÓN DE UNA DONACIÓN&#58; dos horas después de ser anunciada. *** 
&#160; 
 Se implementará una mejora, que generará un mensaje a un grupo de Telegram al cual se debe adicionar el usuario de Ana María Correa. 
 Consulta de los datos del encabezado del anuncio de donación&#58; 
Determinación de la fecha y hora de consulta desde. 
El sistema debe determinar la fecha y hora de publicación deste la cual se consultarán los anuncios no adjudicados, y corresponderá a la primera hora del día en curso&#58; 
 &#123;&#123;fecha_hora_publicacion_desde&#125;&#125; = &#123;&#123;fecha_actual&#125;&#125; %20 00&#58;00&#58;00 
Determinación de la fecha y hora de consulta hasta. 
El sistema debe determinar la fecha y hora hasta la cual se consultarán los anuncios, siendo igual a la fecha y hora actual menos dos horas&#58; 
 &#123;&#123;fecha_hora_publicacion_hasta&#125;&#125; = &#123;&#123;fecha_hora_actual&#125;&#125; - 2 horas 
&#160; 
&#160; 
Programación cronjob para la corrida del proceso 
Se deberá programar un cronjob que corra cada media hora, en horario de 7&#58;30 am a 12 del medio día, todos los días. 
&#160; 
Consulta de anuncios no adjudicados 
 El sistema realizará la siguiente consulta (cada vez que corra el cronjob) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date= &#123;&#123;fecha_publicacion_consulta&#125;&#125; &amp;eatc-state= announced &amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-total_cost,eatc_closer_expiration_date&#160; 
&#160; 
 Si la anterior consulta no arroja resultados el sistema no genera ningún mensaje. 
&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente cada uno de los anuncios que se encontraron en la anterior consulta, iterando por cada código de anuncio (eatc_dona_headers. eatc-code ), la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; &amp; eatc_doma_id = not_adjudication_telegram &amp;_cmp= eatc_dona_header_code 
Se obtiene entonces un &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; 
&#160; 
Si el &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; es igual al array de &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; de la &#160;primera consulta, entonces el mensaje no se envía.&#160; 
&#160; 
 Si el array es menor, entonces se depura la consulta inicial de la siguiente manera&#58; &#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date=&#123; &#123;&#123;fecha_publicacion_consulta&#125;&#125; &amp;eatc-state= announced&amp; eatc-code= _nin_ &#123;&#123;array_eatc_dona_header_code_con_mensaje_previo&#125;&#125; &amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg, eatc-state ,eatc_closer_expiration_date&#160; 
Con los datos recibidos se envía un mensaje a un grupo de Telegram dispuesto para este fin. 
&#160; 
&#160; 
&#160; 
 Los sigientes anuncios de donación&#160; no ha sido adjudicados después de más de 2 horas de publicación&#58; 
&#160; 
 ***Con los datos de cada uno de los anuncios donación (eatc_dona_headers) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;| Fecha y hora de publicación &#160; &#160; &#160; &#160; &#160; &#160;| Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;| Estado &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;| Fecha próxima de vencimiento 
 | &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-publication_datetime &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-total_weight_kg &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; | &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; 
&#160; 
&#160; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados de los anuncios incluidos en el mensaje, para guardar un log de la operación realizada&#58; 
 Escritura en el historial de estados de la donación no entregada que fue informada mediante email. 
 Para cada uno de los anuncios relacionados en la tabla del correo, se realizará esta escritura en el historial de cambios de estados de las donaciones ( eatc_dona_header_state_history ). 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
 eatc-state = announced ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;*** 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; ***Fecha y hora de envío del mensaje*** 
 eatc-log =Se ha enviado un mensaje al grupo de Telegram destinado para informar los anuncios que no han sido adjudicados, 2 horas después de ser programados. 
 eatc_doma_id = not_adjudication_telegram ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history &#160; con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 94eaefee-4c0e-4680-9859-45df85c7fb70 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 a5c9acd5-fb9f-4e88-90cd-b5309e8a2550 
 2025-05-20T05:34:15.3932734Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"3f143853-a05e-4651-831c-06e4dfb7577b","SequenceId":1133,"FluidContainerCustomId":"fa936a69-b2bb-47bf-9bf3-98365814f101","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 PROCESO ENVÍO DE NOTIFICACIÓN ANTE DONACIÓN NO ADJUDICADA