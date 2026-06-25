# WAPP-Modernizada--restricción-de-edición-o-captura-de-documento-soporte.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “adicionar un documento soporte” a la donación. &#160;Uno de nuestros clientes (ara) solicitó bloquear dicha funcionalidad, es decir, que no se pueda cambiar por parte de los usuarios de la WAPP modernizada los documentos soportes (que vienen por integración) y que simplemente los puedan “ver”. &#160;Por eso se debe crear un nuevo parámetro de configuración por cuenta usuario &quot; create_edit_dona_doc_access &quot; que cuando esté marcado como “n” o “FALSE” (según como sea el estándar de implementación en modernización), no permitirá el despliegue de la funcionalidad que permite editar el documento soporte (eatc_dona_headers. eatc-doc ). &#160;Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “y” o “TRUE” según como sea el estándar de implementación en modernización) y solamente marcar como “n” o “FALSE” el correspondiente a la cuenta usuario “ ara ” 
 Validación del parámetro de configuración para restringir la funcionalidad 
 En la funcionalidad de crear una DONA en la WAPP modernizada, el sistema deberá validar el parámetro &quot; create_edit_dona_doc_access &quot;. &#160;Si el mismo para la respectiva cuenta usuario se encuentra en “n” o “FALSE”, entonces la WAPP no le permitirá adicionar o editar el documento soporte, y solo lo podrá leer o consultar. &#160;Por el contrario si el valor del parámetro se encuentra en “s” o “TRUE” entonces la WAPP permitirá (como a todos los usuarios hasta el momento), la creación o edición del documento soporte. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 cb87bb3d-21c3-43fd-98e6-af95d70352e8 
 1!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 71e574d7-17a1-4f88-9025-9e7978d7359c 
 2025-06-27T04:25:31.6401370Z 

 {"SessionId":"5466ef3b-0d70-482a-bc26-4ada20847618","SequenceId":1207,"FluidContainerCustomId":"31fa5ce2-beee-4eab-9689-16c67bdbc2c6","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción de edición o captura de documento soporte