# WAPP-Modernizada--Implementar-webhook-para-mensajería.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, no se han implementado mecanismos de comunicación expedita con los puntos de donación. &#160;Se está viendo la necesidad de enviar en primera instancia el código de verificación de entrega desde la APP y la idea es implementar una arquitectura que luego permita generar nuevos flujos de mensajería de manera sincrónica. 
 Como su nombre lo indica, se propone una arquitectura basada en webhooks para esta implementación, pero si el desarrollador encuentra otra arquitectura estándar que soporte comunicación en tiempo real, se autoriza realizar implementación a criterio del desarrollador, preservando el espíritu de poder abrir un canal de comunicación directo con los puntos de donación a través de mensajes que se puedan mostrar en la WAPP modernizada. 
Configurar un webhook de mensajería por punto de donación 
Se deberá generar una URL correspondiente al webhook que fácilmente se pueda construir con el cua_user y el pod_id. &#160; A este webhook se podrán enviar mensajes.&#160; 
Alguna documentación al respecto&#58;&#160; 

 https&#58;//medium.com/@joshuaokechukwu001/leveraging-next-js-api-routes-to-capture-webhook-payloads-for-client-side-access-97f32f9b3df8 &#160; 
&#160; 
 Configurar una ventana de mensajes 
 A partir de la información del webhook, el sistema en una ventana ubicada en la parte superior de la WAPP, deberá poder visualizar información de mensajes entrantes. &#160;En particular se debe buscar la forma que se puedan recibir partes del mensajes que sean “copiables” para luego operar la plataforma. &#160;Por ejemplo, en el primer caso funcional, la APP deberá enviar al POD el código de verificación. &#160;Dicho código deberá poder copiarse desde el mensaje, para luego ir a la funcionalidad de verificación del código (ojalá de la respectiva donación) y completar el proceso copiando y pegando el código entregado. &#160;Este mecanismo se puede reemplazar por un botón que realice un llamado al API respectiva y haga lo que se realiza cuando se ingresa el código de verificación de recogida de manera correcta. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 f6aed838-46a2-4be4-a013-47f5088b4ee2 
 1!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 0bdab4a5-8f63-4751-ae19-d96993a57920 
 2025-04-16T05:04:12.8181423Z 

 {"SessionId":"36cf6a0e-131a-41a7-81b9-fd367c4cfedc","SequenceId":1028,"FluidContainerCustomId":"652582ad-2452-4935-9c63-90d1ec2d4974","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 

 WAPP Modernizada: Implementar webhook para mensajería