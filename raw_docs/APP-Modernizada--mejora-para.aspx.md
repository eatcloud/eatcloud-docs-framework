# APP-Modernizada--mejora-para.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
Por procesos contables de uno de nuestros clientes “ara” se nos solicita implementar un mecanismo que no permita que queden donaciones abiertas de este donante realizadas en un mes en particular, es decir, el último día del mes, la APP móvil deberá contar con un mecanismo que “fuerce” a los beneficiarios a cerrar todas las donaciones de “ARA” es decir, a realizarles la verificación detallada de la donación para que las mismas sean “certificables”. 

Por lo tanto la APP, a partir de la lectura de un parámetro de configuración en la “ cua_user ” “ mandatory_dona_closing ” (que por el momento solamente para la cuenta “ ara ” debe estar en “ TRUE ”), debe leer las donaciones que cada usuario de la APP tenga en estado “delivered” y “sin fecha válida de recepción” (que es el dato que se registra cuando se realiza la verificación detallada de una donación") y no permitir el ingreso a la nube de donaciones, hasta que no se “cierren” es decir “se verifiquen detalladamente” estas donaciones (en principio del donante “ara” solamente). 

Esta funcionalidad deberá estar operativa los dos últimos días del mes. 

Por otro lado,  también en los últimos días del mes, para el donante cuyo parámetro mandatory_dona_closing esté en “ TRUE ”, no se permitirá realizar programaciones de recogida posteriores al cierre del horario laboral del último día del mes, esto con el ánimo de que todas las donaciones del mes, queden gestionadas dentro del mismo (y no pasen al siguiente) 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 d62d2a00-67fa-4f6b-9551-5daf633845f8 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 2e171ec5-4a01-478b-9fcd-6294653cebf9 
 2025-07-30T05:45:31.7637181Z 

 {"SessionId":"f308437a-36fa-41cb-a9c5-6b56b81915b1","SequenceId":1949,"FluidContainerCustomId":"f6532504-0f9d-41c2-9745-364c42453168","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 APP Modernizada: mejora para agilizar cierre de donaciones al fin de mes para cua_user específicas