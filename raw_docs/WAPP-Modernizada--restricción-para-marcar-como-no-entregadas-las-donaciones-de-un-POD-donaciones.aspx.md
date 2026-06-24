# WAPP-Modernizada--restricción-para-marcar-como-no-entregadas-las-donaciones-de-un-POD-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “marcar como no entregada”.  Uno de nuestros clientes (exito) solicitó bloquear dicha funcionalidad, es decir, que no se puedan eliminar donaciones por parte de algunos PODs o usuarios de la WAPP modernizada.  Por eso se debe crear un nuevo parámetro de configuración por usuario ( tabla : cua_users ) : " not_deliver_donation " que cuando esté marcado como “n” o “FALSE” (según como sea el estándar de implementación en modernización), no permitirá el despliegue de la funcionalidad que permite marcar como no entregadas las donaciones.  Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “y” o “TRUE” según como sea el estándar de implementación en modernización) y solamente marcar como “n” o “FALSE” el correspondiente a la cuenta usuario “ exito ” 
 Validación del parámetro de configuración para restringir la funcionalidad 
 Antes de desplegar el botón o los botones que permiten “marcar como no entregada una donación” a lo largo de la WAPP modernizada, el sistema deberá validar el parámetro " not_deliver_donation ".  Si el mismo para la respectiva cuenta usuario se encuentra en “n” o “FALSE”, entonces la WAPP no le desplegará el botón que permite borrar la donación.  Por el contrario si el valor del parámetro se encuentra en “s” o “TRUE” entonces la WAPP permitirá el despliegue del botón y la funcionalidad. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 3a3eca02-e65b-419d-8871-155deeeb2289 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 4cb99e41-0dea-438c-897d-230348d2fc79 
 2025-05-28T06:38:00.5511599Z 

 {"SessionId":"9fc1cf3f-cc87-4c97-9471-17b6d7eb3d76","SequenceId":459,"FluidContainerCustomId":"e81522d5-0caf-499a-b5ce-4e700c0eba7b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción para marcar como no entregadas las donaciones de un POD donaciones