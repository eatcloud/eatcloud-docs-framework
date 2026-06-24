# WAPP-Modernizada--restricción-de-edición-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “editar una donación”.  Uno de nuestros clientes (exito) solicitó bloquear dicha funcionalidad, es decir, que no se puedan editar donaciones por parte de los usuarios de la WAPP modernizada.  Por eso se debe crear un nuevo parámetro de configuración por cuenta usuario " edit_dona_access " que cuando esté marcado como “n” o “FALSE” (según como sea el estándar de implementación en modernización), no permitirá el despliegue de la funcionalidad que permite borrar donaciones.  Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “y” o “TRUE” según como sea el estándar de implementación en modernización) y solamente marcar como “n” o “FALSE” el correspondiente a la cuenta usuario “ exito ” 
 Validación del parámetro de configuración para restringir la funcionalidad 
 Antes de desplegar el botón o los botones que permiten “editar una donación” a lo largo de la WAPP modernizada, el sistema deberá validar el parámetro " edit_dona_access ".  Si el mismo para la respectiva cuenta usuario se encuentra en “n” o “FALSE”, entonces la WAPP no le desplegará el botón que permite editar la donación.  Por el contrario si el valor del parámetro se encuentra en “s” o “TRUE” entonces la WAPP permitirá el despliegue del botón y la funcionalidad. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 c1ce13d2-c172-4ab3-8879-0fc95c83a840 
 1!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 92b605d4-ac83-4b18-bc33-fb6c0bf3d5bc 
 2025-04-28T23:02:26.9475096Z 

 {"SessionId":"58f49a55-cf9b-42bc-9df0-310e52438626","SequenceId":122,"FluidContainerCustomId":"1a43ef5a-b5dd-4a8a-bfd5-0c124595946b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción de edición de donaciones