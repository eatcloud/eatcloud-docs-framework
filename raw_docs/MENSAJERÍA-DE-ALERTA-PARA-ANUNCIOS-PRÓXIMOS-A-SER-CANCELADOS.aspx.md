# MENSAJERÍA-DE-ALERTA-PARA-ANUNCIOS-PRÓXIMOS-A-SER-CANCELADOS.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mensajería para diferentes cuentas maestras&#58; 
 El proceso de generación de estos mensajes push debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 
&#160; 
 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 
&#160; 
 El sistema generará una alerta para avisar sobre los anuncios que no han sido adjudicados dos horas antes de su fecha y hora de cancelación 
 El sistema debe periódicamente (cada 30 minutos), correr un proceso que compare, para los anuncios cuyo estado (eatc-state) sea &quot; announced &quot;, la hora actual con la hora de cancelación ( eatc-cancellation_datetime) y si determina que la fecha y hora de cancelación está a dos horas o menos, de cumplirse, entonces el sistema deberá, establecer los anuncios que cumplen esa condición y para cada uno de ellos, enviar un mensaje de alerta al donante que promoverá el “alargamiento de la vida útil del anuncio” operando la nueva funcionalidad , para ello desarrollada. 

&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &#160;&amp; eatc_doma_id= not_adjudication_pre_cancellation_email 
&#160; 
 Si existen registros en esta tabla, para dichos anuncios no se prosigue con el proceso. 
&#160; 
&#160; 
 Para aquellos anuncios que no posean registros en la anterior tabla, el sistema sigue adelante con las demás consultas&#58; 
 Consulta de los datos del detalle del anuncio de donación&#58; 
&#160; 
 A partir de los datos consultados y para cada uno de los anuncios cuya fecha de publicación tiene más de dos horas de antiguedad, el sistema realizará la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers&#125;&#125;&amp;_cmp=eatc-odd_id ,eatc-odd_name,eatc-odd_quantity,eatc-odd_total_weight_kg ,eatc-odd_total_cost&#160; 
&#160; 
 Con los datos obtenidos, se construirá el mensaje más adelante. 
&#160; 
 Para cada anuncio de uno de anuncios encontrados, se determina el correo y el teléfono celular para enviar los mensajes&#58; 
&#160; 
 A partir del dato de cada uno de los anuncios cuya fecha de cancelación se encuentra dentro de las próximas dos horas se determinan los datos 
 eatc_dona_headers. eatc-donor =&gt; &#123;&#123;cua_user&#125;&#125; 
 eatc_dona_headers. eatc-pod_id =&gt; &#123;&#123;eatc_pod_id&#125;&#125; 
 eatc_dona_headers. eatc-pod_phone 
&#160; 
&#160; 
 Con esos datos el sistema realizará la siguiente consulta (en la estructura POD de modernización, con los respectivos mecanismos de autenticación requeridos) 
 &#123;&#123;DOMINIO_modernizado&#125;&#125; /api/pods? code_cua_user = &#123;&#123;cua_user&#125;&#125; &amp; code_pod = &#123;&#123;eatc_pod_id&#125;&#125; 
&#160; 
El sistema toma el correo electrónico del POD (o del usuario que se loguea en el pod)&#58; &#123;&#123;email_responsable_pod&#125;&#125; 
&#160;y el teléfono móvil del pod (en caso de encontrarlo) y genera (respectivamente) el siguiente correo electrónico&#58; 
 From&#58;&#160; noreply@eatcloud.com 
 to&#58;&#160; &#123;&#123;email_responsable_pod&#125;&#125; 
&#160; 
&#160; 
 Asunto&#58; Anuncio de donación &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; no ha sido adjudicado está próximo a cancelarse 
&#160; 
 Cuerpo&#58; 
 El anuncio de donación &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&#160;no ha sido adjudicado y está a dos horas o menos de ser cancelado.&#160; El anuncio fue publicado para el punto de donación &#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125;, un costo de &#123;&#123;eatc_dona_headers. eatc-total_cost &#125;&#125;, una fecha más próxima de vencimiento &#123;&#123;eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; y contenía los siguientes productos&#58; 
&#160; 
 ***Con los datos de cada uno de los detalles de donación (eatc_dona) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Nombre&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Cantidad&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Costo total 
 | &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; 
&#160; 
Por favor ingresa a &#123;&#123;URL_webapp_modernizada&#125;&#125; y de ser necesario podrás alargarle la vida útil al anuncio, editándolo. 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; “Cada Kilo Cuenta” 
Y el siguiente mensaje de WhatsApp al teléfono del encargado del pod&#58; 
&#160; 
 El anuncio de donación &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&#160;no ha sido adjudicado y está a dos horas o menos de ser cancelado.&#160; El anuncio fue publicado para el punto de donación &#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125;, un costo de &#123;&#123;eatc_dona_headers. eatc-total_cost &#125;&#125;, una fecha más próxima de vencimiento &#123;&#123;eatc_dona_headers. eatc_closer_expiration_date &#125;&#125;. 
&#160; 
Por favor ingresa a &#123;&#123;URL_webapp_modernizada&#125;&#125; y de ser necesario podrás alargarle la vida útil al anuncio, editándolo. 
&#160; 
 Una vez enviado el mensaje (o los mensajes) el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
 Escritura en el historial de estados de la donación anunciada próxima a cancelarse, del envío del mensaje para promover su alargue de vida útil. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 

 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &#160;* 

 eatc-state = announced&#160; &#160;***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;*** 

 eatc-date_time =&#123;&#123;timestamp&#125;&#125; &#160; *** &#160; Fecha y hora en la que se envía el mensaje (es decir la fecha y la hora en que corre el presente proceso)*** 

 eatc-log =Se ha enviado un correo electrónico a&#160; &#123;&#123;email_responsable_pod&#125;&#125; , informando que el anuncio de donación no ha sido adjudicado y está a menos de dos horas se cancelarse, solicitando su gestión para alargarle la vida útil. 

 eatc_doma_id= &#160; not_adjudication_pre_cancellation_email ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 

 cua_master = &#123;&#123; cua_master &#125;&#125; &#160; 
 Inserción en&#160;eatc_dona_header_state_history &#160; con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 e4fefb76-a18e-4f37-a321-99b73f2b898d 
 3!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 06382ed5-4860-4e01-9190-4ec42844efbc 
 2025-09-08T22:55:22.3199831Z 

 {"SessionId":"fa7965df-c51b-4a31-9787-2c7a7aded3cb","SequenceId":3904,"FluidContainerCustomId":"c903a28e-40fa-4ed8-8289-a3ccb7722269","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 MENSAJERÍA DE ALERTA PARA ANUNCIOS PRÓXIMOS A SER CANCELADOS