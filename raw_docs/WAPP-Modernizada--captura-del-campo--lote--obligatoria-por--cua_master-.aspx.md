# WAPP-Modernizada--captura-del-campo--lote--obligatoria-por--cua_master-.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “captura del lote de producto” al crear la donación, de manera opcional .  Se nos ha solicitado que para la cua_master “ esp ”, esta captura sea obligatoria.  Por eso se debe crear un nuevo parámetro de configuración por cua_master " mandatory_lot_in_dona " que cuando esté marcado como “0” o “FALSE” (según como sea el estándar de implementación en modernización), seguirá funcionando tal cual como funciona hoy  (es decir, que la captura del campo “Lote” será opcional.  Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “0” o “FALSE” y solamente configurar como 1 o “TRUE” para la cua_master “ esp ”, y de esta manera el sistema de captura de donaciones y en específico de los lotes de cada producto, se convertirá en un campo obligatorio a la hora de crear una donación. 
 Validación del parámetro de configuración para hacer obligatoria la captura del lote de cada producto 
 En la funcionalidad de crear una DONA en la WAPP modernizada, el sistema deberá validar el parámetro " mandatory_lot_in_dona ", de cada cua_master.  Si el mismo para la respectiva cuenta maestra se encuentra en “0” o “FALSE”, entonces la WAPP permitirá la captura del lote de manera opcional.  Por el contrario si el valor del parámetro se encuentra en “1” o “TRUE” entonces la WAPP hará obligatoria la captura del lote para cada producto. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 c44b0f9f-6f3e-4c93-a6e5-bf326bb07e8d 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 a202cc93-ce54-4be0-8ee2-aabd773d5d5f 
 2025-09-20T05:05:39.3094913Z 

 {"SessionId":"20060768-c03c-4c76-b028-8c524ff88de7","SequenceId":1901,"FluidContainerCustomId":"64e2d2cc-bf6e-4dfb-b92c-07508facdd35","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: captura del campo "lote" obligatoria por "cua_master"