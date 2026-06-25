# Servicio-para-enviar-mensaje-push-a-una-organización-en-específico.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Generalidades 
 Se deberá crear un servicio, que al ser invocado, se le pueda enviar un mensaje push a una organización en particular. &#160;El servicio podría ser invocado utilizando el &#160; code_cua_master y el code que se encuentran en el maestro &quot; donation_managers &quot; &#160;modernizado. Si se requiere título y cuerpo del mensaje, y existen restricciones de tamaño para el mismo, se deben informar cuales son los tamaños (en número de caracteres) permitidos y validar el envío de esta información. &#160;Si existe una notación especial para que el vínculo del mensaje entre directamente a una donación específica, o dicho vínculo se puede crear a partir del código de la donación, se debe informar cómo hacer dicha vinculación. &#160;Se solicta que al crear el servicio, se utilice esta página para documentar los parámetros y restricciones definidos con el ánimo que sea guía para implementación de mensajería a partir de interacciones con la APP o con la WAPP. 
También se debe pensar la manera de colocarle botones de confirmación al mensaje y su respectivo llamado a API, de tal manera que por ejemplo (en uno de los primeros casos funcionales), se pueda preguntarle mediante el mensaje (o una funcionalidad en la APP vinculada desde el mensaje) si una donación fue efectivamente adjudicada a una organización o no. &#160;En caso afirmativo se deberá generar un proceso de adjudicación, en caso negativo, se deberá marcar la donación como no entregada. &#160;Por lo tanto esta mensajería deberá poder invocar funcionalidades especificas dentro de la APP o por el contrario, llamados a API específicos a partir de interacción con botones, por ejemplo. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 e76721c5-ff71-46b3-85b6-5ed28213ed1b 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 db639a4b-00ea-47d0-8f9a-9d1bbfc0b8e6 
 2025-10-08T06:15:53.4330659Z 

 {"SessionId":"d7bbb8fe-af91-4528-8ee7-5350dda5086d","SequenceId":1543,"FluidContainerCustomId":"2d88094f-66f4-4846-a27f-91da0f2030e7","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 Servicio para enviar mensaje push a una organización en específico