# Envío-de-notificación-(e-mail)-comida-preparada.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para enviar una notificación diferentes correos de ABACO e EatCloud, ante una donación de halla sido marcada como de “comida preparada” ( eatc_dona_headers. eatc_prepared_food= y ). 
&#160; 
 Por lo tanto el sistema deberá invocar el servicio mediante un cronjob que corra cada 15 minutos, evaluando donaciones que hallan sido creadas en el lapso de tiempo entre la corrida anterior y la actual del proceso, y que tengan esta connotación, con el ánimo de enviar un correo, anunciando la generación de este tipo de anuncios. 
&#160; 
 ***NUEVO&#58; MENSAJE PARA ANUNCIAR LA CREACIÓN DE UNA DONACIÓN DE COMIDA PREPARADA *** 
&#160; 
 Se implementará una mejora, que generará un mensaje por correo electrónico donaciones marcadas como “comida preparada” ( eatc_dona_headers. eatc_prepared_food= y&#58; campo pendiente por ser creado ).&#160; Se deberá activar para las cuentas maestras de ABACO y MEXICO 
&#160; 
 Consulta de los datos del encabezado del anuncio de donación&#58; 
&#160; 
 El sistema realizará la siguiente consulta (cada vez que corra el cronjob) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; cua_master &#125;&#125; / eatc_dona_headers? eatc-publication_date&#123;0]= &#123;&#123;fecha_actual&#125;&#125; &amp;eatc-publication_date&#123;1]= &#123;&#123;fecha_actual&#125;&#125; &amp;eatc-state= announced&amp; eatc_prepared_food= y &amp; _cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-total_cost,eatc_closer_expiration_date&#160; 
&#160; 
 Si la anterior consulta no arroja resultados, o arroja una respuesta incorrecta, el sistema no genera ningún mensaje. 
&#160; 
 Si el sistema obtiene una respuesta válida, entonces realiza las siguientes operaciones&#58; 
&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; cua_master &#125;&#125; / eatc_dona_header_state_history ? eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; &amp; eatc_doma_id = prepared_food_email 
&#160; 
 Si existen registros en esta tabla, para dichos anuncios no se prosigue con el proceso. 
&#160; 
 Para aquellos anuncios que no posean registros en la anterior tabla, el sistema sigue adelante con las demás consultas&#58; 
&#160; 
 Consulta de los datos del detalle del anuncio de donación&#58; 
&#160; 
 A partir de los datos consultados y para cada uno de los anuncios marcados como “comida preparada” y que no hayan sido previamente informados por correo electrónico, el sistema realiza la siguiente consulta, para traer sus detalles&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; cua_master &#125;&#125; /eatc_dona? eatc-dona_header_code=&#123;&#123;eatc_dona_headers&#125;&#125; &amp;_cmp= eatc-odd_id ,eatc-odd_name,eatc-odd_quantity,eatc-odd_total_weight_kg ,eatc-odd_total_cost&#160; 
&#160; 
 Con los datos obtenidos, se construirá el mensaje más adelante. 
&#160; 
&#160; 
Se toman los correos a los cuales enviarle los correos electrónicos ( &#123;&#123;array_destinatarios_internos&#125;&#125; ) del campo eatc_cua_master. eatc_prepared_food_notification_emails de la cuenta maestra 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_prepared_food_notification_emails 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123; eatc_cua_master. eatc_prepared_food_notification_emails &#125;&#125; 
&#160; 
 se genera el siguiente correo electrónico&#58; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; 
&#160; 
&#160; 
 Asunto&#58; Anuncio de donación de comida preparada &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; *** en ambiente de prueba incorporar el prefijo [PRUEBA] *** 
&#160; 
 Cuerpo&#58; 
 El anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; fue &#160;marcado como “comida preparada”.&#160; El anuncio fue publicado para el punto de donación &#123;&#123; eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123; eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123; eatc_dona_headers. eatc-total_weight_kg &#125;&#125;, un costo de &#123;&#123; eatc_dona_headers. eatc-total_cost &#125;&#125;, una fecha más próxima de vencimiento &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; y contiene los siguientes productos&#58; 
&#160; 
 ***Con los datos de cada uno de los detalles de donación (eatc_dona) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Nombre&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Cantidad&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Costo total 
 | &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; 
&#160; 
&#160; 
 Equipo EatCloud&#58; &quot;Cada Kilo Cuenta&quot; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados de la donación marcada como “comida preparada” que fue informada mediante email. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; * 
 eatc-state = announced&#160; ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;*** 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; *** Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 
 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;array_destinatarios_internos&#125;&#125;, &#123;&#123;eatc_customers. eatc_email &#125;&#125;, informando que el anuncio es de comida preparada 
 eatc_doma_id = prepared_food_email &#160; ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; &#160; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 d0be05dd-10ab-4d2c-a95f-17466860b419 
 1!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 c842e1d6-43c0-4295-a20a-f10d81bcc358 
 2025-04-17T05:46:00.2589989Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"46a9dd80-8a2f-4251-831a-0abf0f801057","SequenceId":41,"FluidContainerCustomId":"5d424067-6be8-446c-821d-988979429c8d","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Envío de notificación (e-mail) comida preparada