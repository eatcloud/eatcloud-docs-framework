# MENSAJERÍA-DE-ALERTA-PARA-ANUNCIOS-QUE-NO-HAN-SIDO-PROGRAMADOS.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cronjob&#58; 
&#160; 
 El proceso deberá correr cada 30 minutos de 6 AM a 7 PM 
 Mensajería para diferentes cuentas maestras&#58; 
&#160; 
 El proceso de generación de estos mensajes push debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_*&amp;_cmp=eatc_cua &#160; 
 Determinación de la fecha actual 
 El sistema deberá establecer la fecha actual en la variable &#123;&#123;fecha_actual&#125;&#125; 
 y la fecha y hora actual en la variable &#123;&#123;fecha_hora_actual&#125;&#125; 
&#160; 
&#160; 
 Consulta de cua_user sobre las que operará el proceso&#58; 
&#160; 
 El sistema deberá realizar las siguientes consultas (por cuenta maestra), para establecer las cua_user sobre las cuales aplican las evaluaciones respectivas para el envío de los mensajes&#58; 
&#160; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-adjudication_datetime[0]= &#123;&#123;fecha_actual&#125;&#125; %2000&#58;00&#58;00&amp;eatc-adjudication_datetime[1]= &#123;&#123;fecha_hora_actual&#125;&#125; &amp;eatc-state=awarded&amp;_distinct=eatc-donor 
Consulta del dona_particular_scheduling_timeout aplicable 
El sistema realiza la siguiente consulta para cada uno de los donantes obtenidos en la anterior consulta&#58;&#160; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/ eatc_timeout_rules ?cua=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc-timeout_name=dona_particular_scheduling_timeout&amp;_cmp=eatc-timeout_in_minutes 
Si no se obtienen resultados particulares, entonces se procede a definir el valor por _default 
&#160; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/ eatc_timeout_rules ?cua= _default &amp;eatc-timeout_name=dona_particular_scheduling_timeout&amp;_cmp=eatc-timeout_in_minutes 
&#160; 
El valor obtenido se divide entre 2 para obtener un tiempo que debe haber transcurrido para la generación del mensaje 
 &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; = &#123;&#123; eatc_timeout_rules. eatc-timeout_in_minutes &#125;&#125; / 2 
 ENVÍO DE TRES TIPOS DE MENSAJES 
El sistema enviará tres tipos de mensajes. &#160;Dos de los cuales se deben implementar rápidamente (Mensaje WhatsAPP y correo electrónico) y la mensajería PUSH para la APP se debe implementar de cara al lanzamiento de la App Modernizada. 
 Correo electrónico 
 Consulta de donaciones que ya han generado mensajes&#58; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_header_state_history?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &amp;eatc_doma_id= non_scheduled_dona_email &amp;_cmp= eatc_dona_header_code 
&#160; 
 Con esta consulta se obtiene un array de códigos de cabecera a los cuales ya se les ha enviado e-mail &#123;&#123;eatc_dona_headers_with_email&#125;&#125; 
&#160; 
 Consulta de las donaciones sobre las cuales correrá el proceso&#58; 
&#160; 
 El sistema deberá realizar las siguientes consultas (por cuenta maestra), para establecer las cua_user sobre las cuales aplican las evaluaciones respectivas para el envío de los mensajes. &#160;Para establecer la fecha hasta la cual se consultarán donaciones ( eatc-adjudication_datetime[1] ), a la fecha y hora actual se le resta el dato de &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; obtenido anteriormente &#58; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-code=_nin_ &#123;&#123;eatc_dona_headers_with_email&#125;&#125; &amp;eatc-adjudication_datetime[0]= &#123;&#123;fecha_actual&#125;&#125; %2000&#58;00&#58;00&amp; eatc-adjudication_datetime[1] = &#123;&#123; &#123;&#123;fecha_hora_actual&#125;&#125; - &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; &#125;&#125; &amp;eatc-state=awarded&amp;eatc-donor=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;_cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-state, eatc-donation_manager_name,eatc-donation_manager_code 
Consulta de correo electrónico del beneficiario para enviarle el correo 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_beneficiarios&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/ eatc_donation_managers ?identificador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;_cmp= correo_electronico 
 La respuesta obtenida se almacena en la variable 
 &#123;&#123;destinatario_beneficiario&#125;&#125; = &#123;&#123; eatc_donation_managers . correo_electronico &#125;&#125; 
&#160; 
Se toman los correos a los cuales enviarle los correos electrónicos ( &#123;&#123;array_destinatarios_internos&#125;&#125; ) del campo eatc_cua_master . eatc_dona_management_notification_emails de la cuenta maestra 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails 
 La respuesta obtenida se almacena en la variable 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123; eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
&#160; 
 se generan dos correos, uno genérico para los destinatarios interno, y otro particular para el beneficiario&#58; 
&#160; 
 Correo genérico (con tabla con todos los anuncios encontrados) 
Con todos los anuncios encontrados se genera el siguiente correo electrónico&#58;&#160; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; 
&#160; 
&#160; 
&#160; 
 Asunto&#58; Anuncios de donación adjudicados que no han sido programados. *** Si se envía a ambiente de pruebas colocarle como prefijo al asunto “[Prueba]”*** 
&#160; 
 Cuerpo&#58; 
&#160; 
Se han encontrado los siguientes anuncios de donación adjudicados, pendientes de ser programados. 
&#160; 
 ***Con los datos de cada uno de los detalles de donación (eatc_dona) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Fecha y hora de publicación &#160; &#160; &#160; &#160; &#160; | Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Estado &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Beneficiario 
 | &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; | &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125; | &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125; | &#123;&#123;eatc_dona_headers. eatc-state &#125;&#125; | &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125; 
&#160; 
 Recuerda que se envía un solo correo por anuncio. 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; &quot;Cada Kilo Cuenta&quot; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Correo particular (para cada beneficiario con anuncios pendientes de programación) 
Por cada beneficiario con anuncio adjudicado pero no programado se le genera el siguiente mensaje&#58;&#160; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;destinatario_beneficiario&#125;&#125; 
&#160; 
&#160; 
 Asunto&#58; Anuncios de donación adjudicados que no han sido programados. *** Si se envía a ambiente de pruebas colocarle como prefijo al asunto “[Prueba]”*** 
&#160; 
 Cuerpo&#58; 
&#160; 
 El anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &#160;adjudicado a tu organización, no ha sido programado para su recolección.&#160; El anuncio fue publicado para el punto de donación &#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125;. 
&#160; 
 Por favor abre tu &lt;a href=https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios&amp;hl=es_CO&gt; aplicación EatCloud &lt;/a&gt; para programar su recolección&#160; 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; “Cada Kilo Cuenta” 
&#160; 
&#160; 
 Una vez enviados los mensajes, el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados el envío de correo electrónico por donación no programada. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 

 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; 

 eatc-state = awarded ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;*** 

 eatc-date_time =&#123;&#123;timestamp&#125;&#125;***Fecha y hora en la cual se envía el mensaje (es decir la fecha y la hora en que corre el presente proceso)*** 

 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;array_destinatarios_internos&#125;&#125; , &#123;&#123;destinatario_beneficiario&#125;&#125; informando que el anuncio en estado “awarded” que no han sido programado. 

 eatc_doma_id= non_scheduled_dona_email ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 

 cua_master = &#123;&#123; cua_master &#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 Mensaje de WhatsApp 
 Consulta de donaciones que ya han generado mensajes&#58; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_header_state_history?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &amp;eatc_doma_id= non_scheduled_dona_wa &amp;_cmp= eatc_dona_header_code 
&#160; 
 Con esta consulta se obtiene un array de códigos de cabecera a los cuales ya se les ha enviado e-mail &#123;&#123;eatc_dona_headers_with_wam&#125;&#125; 
&#160; 
 Consulta de las donaciones sobre las cuales correrá el proceso&#58; 
&#160; 
 El sistema deberá realizar las siguientes consultas (por cuenta maestra), para establecer las cua_user sobre las cuales aplican las evaluaciones respectivas para el envío de los mensajes. &#160;Para establecer la fecha hasta la cual se consultarán donaciones ( eatc-adjudication_datetime[1] ), a la fecha y hora actual se le resta el dato de &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; obtenido anteriormente &#58; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-code=_nin_ &#123;&#123;eatc_dona_headers_with_wam&#125;&#125; &amp;eatc-adjudication_datetime[0]= &#123;&#123;fecha_actual&#125;&#125; %2000&#58;00&#58;00&amp; eatc-adjudication_datetime[1] = &#123;&#123; &#123;&#123;fecha_hora_actual&#125;&#125; - &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; &#125;&#125; &amp;eatc-state=awarded&amp;eatc-donor=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;_cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-state, eatc-donation_manager_name,eatc-donation_manager_code 
Consulta del teléfono móvil (WhatsApp) al cuál se le envía la notificación 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_beneficiarios&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/ eatc_donation_managers ?identificador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;_cmp= wa_notificaciones 
 Nota importante para el desarrollo&#58;&#160; 
 El campo wa_notificaciones no ha sido creado. Se deben coordinar acciones para crear dicho campo en entorno legacy y modernizado, y se deberán generar tareas para crear un mecanismo de obtención de dicho número habilitado para enviarle mensajes por WA, a través inicialmente de la App Legacy (puede ser un formulario web embebido), y posteriormente por el formulario de Onboarding de Beneficiarios y de la APP modernizada. 
&#160; 
 La respuesta obtenida se almacena en la variable 
 &#123;&#123;destinatario_wa&#125;&#125; = &#123;&#123; eatc_donation_managers . wa_notificaciones &#125;&#125; 
&#160; 
&#160; 
Por cada beneficiario con anuncio adjudicado pero no programado se le genera el siguiente mensaje a WhatsApp al correspondiente número &#123;&#123;destinatario_wa&#125;&#125; &#58;&#160; 
&#160; 
 El anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &#160;adjudicado a tu organización, no ha sido programado para su recolección.&#160; El anuncio fue publicado para el punto de donación &#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125;. 
&#160; 
 Por favor abre tu &lt;a href=https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios&amp;hl=es_CO&gt; aplicación EatCloud &lt;/a&gt; para programar su recolección&#160; 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; “Cada Kilo Cuenta” 
 NOTA con respecto al vínculo para abrir la APP &lt;a href=https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios&amp;hl=es_CO&gt;&#58; &#160;Inicialmente se debe enviar un vínculo genérico para abrir la APP en general, pero con la modernización de la misma se deberá implementar un vínculo que abra la APP en el anuncio particular que se está informando y en su funcionalidad de programar recogida, con el ánimo de que el usuario al hacer clic entre directamente a la programación del anuncio. 
&#160; 
 Una vez enviados los mensajes, el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados el envío del mensaje de WhatsApp por donación no programada. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 

 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; 

 eatc-state = awarded ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;*** 

 eatc-date_time =&#123;&#123;timestamp&#125;&#125;***Fecha y hora en la cual se envía el mensaje (es decir la fecha y la hora en que corre el presente proceso)*** 

 eatc-log =Se ha enviado un mensaje de WhatsApp a &#123;&#123;destinatario_wa&#125;&#125; informando que el anuncio en estado “awarded” que no han sido programado. 

 eatc_doma_id= non_scheduled_dona_wa ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 

 cua_master = &#123;&#123; cua_master &#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
 Mensaje Push APP Modernizada 
 Consulta de donaciones que ya han generado mensajes&#58; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_header_state_history?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &amp;eatc_doma_id= non_scheduled_dona_pm &amp;_cmp= eatc_dona_header_code 
&#160; 
 Con esta consulta se obtiene un array de códigos de cabecera a los cuales ya se les ha enviado e-mail &#123;&#123;eatc_dona_headers_with_pm&#125;&#125; 
&#160; 
 Consulta de las donaciones sobre las cuales correrá el proceso&#58; 
&#160; 
 El sistema deberá realizar las siguientes consultas (por cuenta maestra), para establecer las cua_user sobre las cuales aplican las evaluaciones respectivas para el envío de los mensajes. &#160;Para establecer la fecha hasta la cual se consultarán donaciones ( eatc-adjudication_datetime[1] ), a la fecha y hora actual se le resta el dato de &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; obtenido anteriormente &#58; 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-code=_nin_ &#123;&#123;eatc_dona_headers_with_pm&#125;&#125; &amp;eatc-adjudication_datetime[0]= &#123;&#123;fecha_actual&#125;&#125; %2000&#58;00&#58;00&amp; eatc-adjudication_datetime[1] = &#123;&#123; &#123;&#123;fecha_hora_actual&#125;&#125; - &#123;&#123;tiempo_transcurrido_para_el_mensaje&#125;&#125; &#125;&#125; &amp;eatc-state=awarded&amp;eatc-donor=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;_cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-state, eatc-donation_manager_name,eatc-donation_manager_code 
&#160; 
Por cada beneficiario con anuncio adjudicado pero no programado se le genera el siguiente mensaje mensaje Push&#58;&#160; 
&#160; 
 Anuncio &#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; pendiente de programación. &lt;a href=https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios&amp;hl=es_CO&gt; Programar recolección &lt;/a&gt; &#160; 
 NOTA con respecto al vínculo para abrir la APP &lt;a href=https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios&amp;hl=es_CO&gt;&#58; &#160;Inicialmente se debe enviar un vínculo genérico para abrir la APP en general, pero con la modernización de la misma se deberá implementar un vínculo que abra la APP en el anuncio particular que se está informando y en su funcionalidad de programar recogida, con el ánimo de que el usuario al hacer clic entre directamente a la programación del anuncio. 
&#160; 
 Una vez enviados los mensajes, el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados el envío del mensaje de WhatsApp por donación no programada. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 

 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; 

 eatc-state = awarded ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;*** 

 eatc-date_time =&#123;&#123;timestamp&#125;&#125;***Fecha y hora en la cual se envía el mensaje (es decir la fecha y la hora en que corre el presente proceso)*** 

 eatc-log =Se ha enviado un mensaje de WhatsApp a &#123;&#123;destinatario_wa&#125;&#125; informando que el anuncio en estado “awarded” que no han sido programado. 

 eatc_doma_id= non_scheduled_dona_pm ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 

 cua_master = &#123;&#123; cua_master &#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 e4b23769-a6a0-48ee-ac68-d614b4dd822b 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 cbf309b0-bca8-4aba-b004-a529aeebba8e 
 2025-04-21T23:47:43.7402957Z 

 {"SessionId":"0f8cd502-af5a-435b-9819-da15d3d97916","SequenceId":13644,"FluidContainerCustomId":"3934f5e9-cf8e-4062-9923-1f23449ecb89","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 

 MENSAJERÍA DE ALERTA PARA ANUNCIOS QUE NO HAN SIDO PROGRAMADOS