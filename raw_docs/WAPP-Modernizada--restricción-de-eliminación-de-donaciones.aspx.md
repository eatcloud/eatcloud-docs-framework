# WAPP-Modernizada--restricción-de-eliminación-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “eliminar una donación”.  Uno de nuestros clientes (exito) solicitó bloquear dicha funcionalidad, es decir, que no se puedan eliminar donaciones por parte de los usuarios de la WAPP modernizada.  Por eso se debe crear un nuevo parámetro de configuración por usuario ( tabla : cua_users ) : " delete_donation " que cuando esté marcado como “n” o “FALSE” (según como sea el estándar de implementación en modernización), no permitirá el despliegue de la funcionalidad que permite borrar donaciones.  Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “y” o “TRUE” según como sea el estándar de implementación en modernización) y solamente marcar como “n” o “FALSE” el correspondiente a la cuenta usuario “ exito ” 
 Validación del parámetro de configuración para restringir la funcionalidad 
 Antes de desplegar el botón o los botones que permiten “eliminar una donación” a lo largo de la WAPP modernizada, el sistema deberá validar el parámetro " delete_donation ".  Si el mismo para la respectiva cuenta usuario se encuentra en “n” o “FALSE”, entonces la WAPP no le desplegará el botón que permite borrar la donación.  Por el contrario si el valor del parámetro se encuentra en “s” o “TRUE” entonces la WAPP permitirá el despliegue del botón y la funcionalidad. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 f345de14-1430-4232-965d-4847a3dec700 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 999a6458-33a3-4168-a427-f8dd41b49987 
 2025-05-16T22:22:37.0036707Z 

 {"SessionId":"71f673a5-3d71-4381-a5ca-5e89cf3c142d","SequenceId":100,"FluidContainerCustomId":"8c9cf9b6-ba52-44d2-b48e-916eff6c2860","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 

 WAPP Modernizada: restricción de eliminación de donaciones