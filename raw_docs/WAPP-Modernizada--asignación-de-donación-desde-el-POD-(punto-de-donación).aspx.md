# WAPP-Modernizada--asignación-de-donación-desde-el-POD-(punto-de-donación).aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, cuando se crea una donación en la WAPP la misma sale en estado “announced” para ser procesada por los servicios que generan la adjudicación / programación directa, el match y su posterior gestión. 

 Se ha aprobado una mejora que implicará que desde el punto de donación (para pods definidos) se puedan asignar las donaciones a beneficiarios determinados y adicional a ello, no opere sobre estas donaciones la liberación de la donación por demora en la programación ( dona_particular_scheduling_timeout ) 
 Puntos a los cuales se le despliega la funcionalidad 
Deberán ser puntos debidamente configurados como poseedores de la funcionalidad (se debe definir un parámetro de configuración para ello). 
En la tabla de pods de modernización existe el campo “direct_awarding”, el cual por defecto tiene el valor “NA” y tiene 3 opciones de configuración: 

NA: Funciona de manera tradicional. 

not_timeout: Tiene acceso a la funcionalidad y al selector de beneficiarios desde la WAPP, pero no es afectado por las reglas de timeout para liberación. 

timeout: Tiene acceso a la funcionalidad y al selector de beneficiaros desde la WAPP, pero si es afectado por las reglas de timeout para liberación. 
 Construcción del selector de gestor de donaciones 
Se debe disponer una estructura de datos en donde se encuentre la dupla Punto de donación - Beneficiario, y con esta información se armará el selector de beneficiarios a los cuales se les puede asignar, en cada punto respectivo, una donación. 
En la tabla “direct_dona” de modernización, la cual almacena la configuración de asignación directa y manual se deben añadir los puntos con su par de beneficiarios, dichos beneficiarios son los que aparecerán en el selector para el punto configurado. 

 Asignación de la donación mediante el proceso de creación de encabezados 
Se le envía al servicio de creación de encabezados un objeto en la propiedad “data_direct_awarding” desde la WAPP, el cual entiende que debe hacer el proceso de adjudicación. El parámetro “timeout” es el que condiciona si la donación es o no afectada por el timeout de liberación. 

 [{"UserId":17,"DisplayName":"Carlos Villa","LoginName":"carlos.villa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 {"SessionId":"eacc4723-64dc-4365-9331-98715b27c0c1","SequenceId":3494,"FluidContainerCustomId":"a6e1a36c-0db5-4705-99a4-c98981c04c01","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 ca7a9bdf-e7c4-4ceb-a824-ac75e3449c64 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 213724f2-3477-4b16-a069-bb0bcbec5905 
 2025-04-16T05:18:27.4187344Z 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 993.000000000000 

 WAPP Modernizada: asignación de donación desde el POD (punto de donación)