# Notificación-de-los-productos-no-encontrados.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para enviar una notificación diferentes correos del donante, ABACO / BAMX e EatCloud, ante una donación que presenta faltantes o sobrantes gracias al proceso de verificación detallada de la donación que se realiza mediante la APP. 
&#160; 
 Por lo tanto el sistema deberá invocar el servicio mediante un cronjob que corra cada 30 minutos (por cuenta maestra), evaluando datos de la fecha de la tabla eatc_odds_rejection_registry para enviar correos a los respectivos encargados. 

 ***NUEVO&#58; MENSAJE PARA ANUNCIAR LOS PRODUCTOS NO ENCONTRADOS EN UNA DONACIÓN *** 
&#160; 
 Se implementará una mejora, que generará un mensaje por correo electrónico de los productos no encontrados en una donación y que se direccionará al donante y a los mails de gestión de donaciones. 
&#160; 
 Consulta de productos no encontrados 
&#160; 
 El sistema realizará la siguiente consulta (cada vez que corra el cronjob) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; cua_master &#125;&#125;/ eatc_odds_rejection_registry ? date_time =&#123;&#123;fecha_actual&#125;&#125; _lk &amp;_distinct= eatc-dona_header_code 
&#160; 
 Si la anterior consulta no arroja resultados el sistema no genera ningún mensaje. 
&#160; 
 Con los resultados obtenidos &#123;&#123;array_eatc_dona_headers_code&#125;&#125; , el sistema realiza la siguiente validación. 
&#160; 
 Consulta en el historial de estados para determinar que no se haya enviado previamente este mismo email&#58; 
&#160; 
 El sistema evalúa que no se haya enviado correo electrónico previamente para el mismo anuncio, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc_dona_header_code= &#123;&#123;array_eatc_dona_headers_code&#125;&#125; &amp; eatc_doma_id = product_news_email&amp;_cmp= eatc_dona_header_code 
&#160; 
 Si existen registros en esta tabla, se toman los códigos de encabezados que aparecen en la tabla y se arma un &#160; &#123;&#123;array_dona_header_code_con_correo_previo&#125;&#125; , para dichos anuncios no se prosigue con el proceso. 
&#160; 
 Para aquellos anuncios que no poseean registros en la anterior tabla, se arma un array&#58; &#160; &#123;&#123;array_dona_header_code_SIN_correo_previo&#125;&#125; , el sistema sigue adelante con las demás consultas&#58; 
&#160; 
 Para cada anuncio con novedad y que no ha sido previamente informado por correo se realiza lo siguiente&#58; 
Escritura del dato eatc_donor en eatc_odds_rejection_registry 
Si existen registros que no tienen información en eatc_odds_rejection_registry. eatc_donor &#160; el sistema realiza la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_odds_rejection_registry .eatc-dona_header_code &#125;&#125;&amp;_cmp=eatc-code, eatc-donor 
Con los valores recolectados el sistema realiza la siguiente escritura 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /crd/ &#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_odds_rejection_registry &amp;_operacion=update&amp; eatc_donor =&#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125;&amp;WHERE eatc-dona_header_code = &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
Consulta del correo del donante 
Con el dato 
 eatc_dona_headers. eatc-donor 
 Que llega de una consulta anterior, el sistema realizará la siguiente consulta 
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
 ***Nuevo &#58; se toman los correos adicionales a eatc_customers.eatc_mail del parámetro &#123;&#123;array_destinatarios_internos&#125;&#125; de la cuenta maestra *** 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails,dona_news_instructions 
 Nota &#58; el campo dona_news_instructions no ha sido creado aun. 
&#160; 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123;eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
&#160; 
 Consulta para generar la tabla de información 
&#160; 
 El sistema realizará la siguiente consulta para los anuncios de cada eatc_donor 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; cua_master &#125;&#125;/ eatc_odds_rejection_registry ? eatc_donor = &#123;&#123; eatc_donor &#125;&#125; &amp; eatc-dona_header_code= &#123;&#123;array_dona_header_code_SIN_correo_previo&#125;&#125; &amp;_cmp= eatc-dona_header_code,eatc-pod_id,eatc-odd_id,eatc-odd_rejection_cause,quantity,evidence 
Para cada anuncio realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_headers ? eatc-code = &#123;&#123; eatc_odds_rejection_registry . eatc-dona_header_code&#125;&#125;&amp;_cmp=eatc-pod_name 
y para cada producto traerá su respectivo nombre&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona ? eatc-dona_header_code = &#123;&#123; eatc_odds_rejection_registry . eatc-dona_header_code&#125;&#125;&amp;eatc-odd_id= &#123;&#123; eatc_odds_rejection_registry . eatc-odd_id&#125;&#125;&amp;_cmp=eatc-odd_name 
&#160; 
 se genera el siguiente correo electrónico&#58; 
&#160; 
 From&#58; noreply@eatcloud.com 
 to&#58; &#123;&#123;array_destinatarios_internos&#125;&#125; ,&#123;&#123;eatc_customers. eatc_email &#125;&#125; 
&#160; 
&#160; 
&#160; 
 Asunto&#58; &#123;&#123; eatc_donor &#125;&#125; novedades productos donados 
&#160; 
 Cuerpo&#58; 
 Se han presentado las siguientes novedades con productos donados &#58; 
&#160; 
 ***Con los datos de la consulta anterior el sistema construye la siguiente tabla*** 
 | Donación &#160;| Punto de donación | Código producto | Producto &#160;| Novedad &#160;| &#160;Cantidad &#160;| &#160;Evidencia 
 | &#123;&#123; eatc_odds_rejection_registry . eatc-dona_header_code &#125;&#125; | &#123;&#123; eatc_dona_headers . eatc-pod_name &#125;&#125; | &#123;&#123; eatc_odds_rejection_registry . eatc-odd_id &#125;&#125; | &#123;&#123; eatc_dona . eatc-odd_name &#125;&#125; | &#123;&#123; eatc_odds_rejection_registry . eatc-odd_rejection_cause &#125;&#125; | &#123;&#123; eatc_odds_rejection_registry . quantity &#125;&#125; | &#123;&#123; eatc_odds_rejection_registry . evidence &#125;&#125; 
&#160; 
 &#123;&#123; eatc_cua_master. dona_news_instructions&#125;&#125; 
&#160; 
 De antemano muchas gracias por la atención prestada 
&#160; 
 Equipo EatCloud&#58; &quot;Cada Kilo Cuenta&quot; 
&#160; 
 Una vez enviado el mensaje el sistema realiza el siguiente registro en el historial de estados del anuncio en particular, para guardar un log de la operación realizada&#58; 
&#160; 
 Escritura en el historial de estados de la donación no entregada que fue informada mediante email.&#160; 
 Para cada una de las donaciones informadas en el anterior correo se realiza el siguiente registro&#58; 
&#160; 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
 eatc-state = &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; *** Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 
 eatc-log =Se ha enviado un correo electrónico automático a &#123;&#123;array_destinatarios_internos&#125;&#125;, &#123;&#123;eatc_customers. eatc_email &#125;&#125;, informando las novedades en los productos en esta donación. *** Mensaje&#58; concatenación de constantes y variables*** 
 eatc_doma_id = product_news_email &#160; ***constante *** 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; &#160; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 978.000000000000 

 Notificación de novedades en productos (no encontrados y excedentes)