# APP--Funcionalidad-para-confirmar-o-rechazar-la-entrega-de-una-donación-reportada-por-otra-organización.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
Como parte de la mejora del proceso de reporte de donaciones no entregadas, se va abrir la posibilidad de informar por mensajería push , una vez se seleccione el causal de que la donación fue entregada a otra organización () y se pueda capturar información de a qué otra organización se entregó , entonces la organización que reporta, estará entregando el código de la organización a la que se dice que le entregaron y en ese punto se podrá enviar un mensaje push a la organización a la cual se dice que le entregaron, con el ánimo de que dicha organización confirme el hecho o lo desmienta.  A continuación se detalla una funcionalidad que debe estar presente en la APP, con el ánimo de “confirmar” o “rechazar” este informe de que una donación fue entregada a otra organización.  Por ese motivo, esta funcionalidad se le despliega a la organización que fue informada (no a la que informa) y deberá contener las siguientes funcionalidades 

Funcionalidad que pueda ser accedida a través de un vínculo de un mensaje push: 
Debe existir una manera de acceder a esta funcionalidad, mediante un vínculo desde un mensaje push, o mediante un vínculo a en la card del listado de “mis elegidas” o en los detalles de la donación en estado “delivered”. 

Funcionalidad que pueda ser accedida a través de un vínculo de en la card de mis elegidas o en el detalle de la donación en estado “delivered”: 
Debe existir una manera de acceder a esta funcionalidad, mediante un vínculo desde un mensaje push, o mediante un vínculo a en la card del listado de “mis elegidas” o en los detalles de la donación en estado “delivered”. 

 Funcionalidad de confirmación: 
El sistema deberá desplegar un cuadro de diálogo en donde informe lo siguiente 
La donación de código {{codigo_donacion}} fue informada como si se le ubiera entregado a su organización. Por favor ayúdenos a confirmar esta información 
 Botones de acción: 
A continuación del mensaje anterior se deberán desplegar dos botones, uno para confirmar que fue entregada a dicha organización y otro para negarlo 

 SI: me entregaron la donación 
Al presionar este botón, el sistema deberá confirmar los datos de “programación” de la donación (que se debieron haber confirmado desde la APP de quién reportó el incidente ) es decir, no hay ninguna escritura adicional en el encabezado de donación.   Adicional a esto, se deberá generar un llamado de atención para la organización con el código “”. Para hacer este llamado se puede utilizar este Webhook: y una muestra de datos como la siguiente 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 3ced71ce-38cc-47ba-aef9-3469014060a7 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 f1ee4289-9885-42c6-b28a-f26836cce561 
 2025-10-08T06:47:34.8132214Z 

 {"SessionId":"b5627f02-d95f-4de6-875c-81cd0591ee32","SequenceId":242,"FluidContainerCustomId":"1945ba4f-c0d9-4f61-89fe-3fdec30c600f","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 APP: Funcionalidad para confirmar o rechazar la entrega de una donación reportada por otra organización