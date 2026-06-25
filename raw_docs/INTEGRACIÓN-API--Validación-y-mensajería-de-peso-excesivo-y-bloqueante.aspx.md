# INTEGRACIÓN-API--Validación-y-mensajería-de-peso-excesivo-y-bloqueante.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DE LA IMPLEMENTACIÓN 
 Al crear anuncios por API se deberá validar el peso excesivo y bloqueante, de tal manera que se minimicen errores debidos a pesos mal configurados en las donaciones que fluyen a través de integración. 
&#160; 
El proceso debe funcionar de manera muy similar a como lo hace cuando se ingresan manualmente las donaciones&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/creaci%C3%B3n-de-anuncio-de-donaci%C3%B3n-eatc_dona_upl.aspx#validaci%C3%B3n-de-peso-total-(eatc-odd_total_weight_kg)-cuando-el-resultado-es-un-peso-muy-elevado-mensaje-con-n%C3%BAmeros-vivos-para-pr &#160; 

Correos a los cuales se envía notificación&#58; 
 A partir del dato del donante que realiza la donación, el sistema realizará la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua&amp;fieldvalue=&#123;&#123;eatc_dona_headers.eatc-donor&#125;&#125;&amp;fielddecrypt=eatc_customer_fiscal_id 
&#160; 
&#160; 
 Con el dato desencriptado eatc_customers_cua. eatc_customer_fiscal_id obtenido, el sistema realiza la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers&amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123; eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125;&amp;fielddecrypt= eatc_email 
&#160; 
 El dato del correo desencriptado (eatc_customers. eatc_email ) se utiliza para enviar la notificación 
&#160; 
Correos internos a los cuales se les envía también la notificación &#123;&#123;array_destinatarios_internos&#125;&#125; 
El sistema realiza la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_dona_management_notification_emails 
 La respuesta obtenida se almacena en la variable 
&#160; 
 &#123;&#123;array_destinatarios_internos&#125;&#125; = &#123;&#123;eatc_cua_master. eatc_dona_management_notification_emails &#125;&#125; 
 A este array también se le envía la notificacción 

 Peso excesivo ( referencia para implementación ) 
 El sistema enviará un mensaje, alertando del registro con peso excesivo y sugiriendo al donante que a través de la WAPP del punto de donación en particular, se revise si el peso registrado es correcto o no, haciendo la respectiva edición. 
&#160; 
 En este caso, el sistema permitirá el registro de la donación. 

 Peso bloqueante ( referencia para implementación ) 
 El sistema enviará un mensaje, alertando la imposibilidad de registrar la donación dado que contiene un peso que en nuestro sistema está configurado como no permitido para el punto de donación en particular. &#160;El mensaje debe incluir un vínculo a la mesa de ayuda sugiriendo que se comunique con ella para revisar el incidente y debe contener los datos de la donación que se rechaza por peso bloqueante y el dato del peso bloqueante que aplica para el caso en particular. 
&#160; 
 En este caso, el sistema no permitirá el registro de la donación. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 fb455271-6de0-48e6-92ec-f3698f72908b 
 1!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 5ccdf00f-ee63-4e45-85af-fb6109deecbb 
 2025-04-26T04:49:46.0285988Z 

 {"SessionId":"b7f3f384-5623-4613-b999-e84127516c15","SequenceId":3729,"FluidContainerCustomId":"38ed95c5-c65a-4240-949b-4b7820282a2f","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 INTEGRACIÓN API: Validación y mensajería de peso excesivo y bloqueante