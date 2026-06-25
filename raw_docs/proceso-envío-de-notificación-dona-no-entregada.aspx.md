# proceso-envío-de-notificación-dona-no-entregada.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para enviar una notificación al correo administrador registrado en la plataforma, ante una no entrega de una donación.&#160; Se debe implementar como un servicio público, cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento&#160;&#160; 
&#160; 
 API pública para envío de correo ante donaciones no entregadas 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 
&#160; 
 ***NUEVO&#58; mensaje para anunciar al donante sobre una donación no entregada *** 
 Se implementará una mejora, que generará un mensaje por correo electrónico cuando una donación es marcada como &quot; No Entegada &quot; (eatc-state= not_delivered ). 
&#160; 
 Consulta de los datos del encabezado del anuncio de donación&#58; 
 A partir de los datos&#58; 
 cua_master 
 eatc_dona_header_code &#160; 
&#160; 
 Que llegan en el llamado del API , el sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-state= not_delivered &amp;_cmp= eatc-code,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-publication_datetime,eatc-total_weight_kg,eatc-total_cost,eatc-state 
&#160; 
 Si la anterior consulta no arroja resultados (lo cual puede indicar que el anuncio no exista o que no tenga el estado not_delivered ), el sistema deberá responder con&#58;&#160; 
 &quot;err_msg&quot; &#58; &quot;fail&#58; donation does not exist or has incorrect state&quot; 
&#160; 
 En caso de conseguir una respuesta válida, el sistema sigue con las siguientes consultas&#58; 
&#160; 
 Consulta de los datos del detalle del anuncio de donación&#58; 
 A partir de los datos&#58; 
 cua_master 
 eatc_dona_header_code &#160; 
&#160; 
 Que llegan en el llamado del API , el sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;_cmp= eatc-odd_id ,eatc-odd_name,eatc-odd_quantity,eatc-odd_total_weight_kg ,eatc-odd_total_cost&#160; 
&#160; 
 Con los datos obtenidos, se construirá el mensaje 

&#160; 
 Consulta del correo al cuál se debe enviar el mensaje&#58; 
 A partir del dato&#58; 
 eatc_dona_headers. eatc-donor 
&#160; 
 Que llega de una consultaa anterior, el sistema realizará la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua&amp;fieldvalue=&#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125;&amp;fielddecrypt= eatc_customer_fiscal_id 
&#160; 
 Con el dato desencriptado eatc_customers_cua. eatc_customer_fiscal_id obtenido, el sistema realiza la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers&amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123; eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125;&amp;fielddecrypt= eatc_email &#160; 
&#160; 
 Con el dato del correo desencriptado ( eatc_customers. eatc_email ) , los datos anteriormente consultados y los datos de invocación del servicio&#58; 
 eatc_user &#160; 
 eatc_doma &#160; 
&#160; 
 ***Nuevo &#58; se toman los correos adicionales a eatc_customers.eatc_mail del parámetro &#123;&#123;array_destinatarios_internos&#125;&#125; de la cuenta maestra *** 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123;eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
&#160; 
 se genera el siguiente correo electrónico&#58; 
&#160; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; ,&#123;&#123;eatc_customers. eatc_email &#125;&#125; 
&#160; 
&#160; 
 Deprecado (anteriormente)&#58; 
 From&#58; noreply@eatcloud.com 
 to&#58; soporte@eatcloud.com ,&#123;&#123;eatc_customers. eatc_email &#125;&#125;,donaciones@abaco.org.co,ingridbrawn@abaco.org.co 
&#160; 
&#160; 
 Asunto&#58; Anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; no fue entregado 
&#160; 
 Cuerpo&#58; 
 Recientemente el usuario &#123;&#123; eatc_user &#125;&#125; del gestor de donaciones &#123;&#123; eatc_doma &#125;&#125; nos ha informado que el anuncio de donación &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; no fue entregado.&#160; El anuncio fue publicado para el punto de donación &#123;&#123; eatc_dona_headers. eatc-pod_name &#125;&#125; en la fecha &#123;&#123; eatc_dona_headers. eatc-publication_datetime &#125;&#125; con un peso de &#123;&#123; eatc_dona_headers. eatc-total_weight_kg &#125;&#125;, un costo de &#123;&#123; eatc_dona_headers. eatc-total_cost &#125;&#125; y contenía los siguientes productos&#58; 
&#160; 
 ***Con los datos de cada uno de los detalles de donación (eatc_dona) el sistema construye la siguiente tabla*** 
 | Código&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Nombre&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Cantidad&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Peso total &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; | Costo total 
 &#160;| &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; | &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; 
&#160; 
 Les solicitamos muy comedidamente revisar con el punto de donación el motivo de esta &quot; no entrega &quot; para evitar inconvenientes en el futuro. 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; &quot;Cada Kilo Cuenta&quot; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
&#160; 
 Escritura en el historial de estados de la donación no entregada que fue informada mediante email. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; ***parámetro de invocación del servicio*** 
 eatc-state = not_delivered&#160; ***constante que debe corresponder al dato que se obtiene en&#160; &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;*** 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; *** Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 
 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;eatc_customers. eatc_email &#125;&#125; informando que el anuncio de donación no fue entregado 
 eatc_doma_id = &#123;&#123; eatc_doma_id &#125;&#125; ***parámetro de invocación del servicio*** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; ***parámetro de invocación del servicio*** 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"Off"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 b6fdc742-6970-4c9f-bf59-7de5001e41e5 
 1!1!3 
 https://eastus1-0.pushfp.svc.ms/fluid 
 ad756c55-7ba7-4819-ad2c-726eec206293 
 2025-04-09T23:01:17.1707143Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"758c56a3-fb3a-4fee-8317-dc71ff222f39","SequenceId":51,"FluidContainerCustomId":"634ede39-2b3e-4e23-ba76-d58871658ef3","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 PROCESO ENVÍO DE NOTIFICACIÓN ANTE DONACIÓN NO ENTREGADA