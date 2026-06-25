# Logica-super-puntos---puntos-gestion.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

La lógica de super puntos o puntos gestión establece que un punto de donación (padre) puede hacer donaciones a nombre de otro punto (hijo) de su mismo donante, para eso hay dos tipos de configuraciones&#58; 

 Super punto&#58; Haciendo referencia al punto padre que puede crear donaciones de todos los puntos de su donante, sin excepción. 

 Super punto parcial &#58; Haciendo referencia a un punto padre que puede crear donaciones solo a nombre de unos cuantos puntos seleccionados. 
&#160; 
En la tabla de pods de modernización hay un campo llamado super_pod, este campo tiene por defecto el valor “ NA ”, pero puede tener valor “ super ” o “ partial ”. 
&#160; 
-Si un punto tiene el campo super_pod con un valor de “ super” , se entiende que este punto tendrá acceso a todos los puntos de su donante. 
-Si un punto tiene el campo super_pod con un valor de “ partial ” se hace una consulta a la tabla super_partial_users_pods de modernización donde tendremos una estructura como la siguiente&#58; 
&#160; 

Donde la columna code_pod hace referencia a ese punto padre que podrá crear donaciones a nombre de sus puntos hijos, almacenados en la columna code_pod_child. 
&#160; 
En ambos escenarios el punto de donación tendrá acceso en la webapp a un buscador de puntos de donación que por defecto tendrá el nombre del punto de donación con el que se inició sesión&#58; 
&#160; 

&#160; 
Para llevar a cabo el proceso de edición por API vease más en Consultas CRD (Crud). 
&#160; 

 [{"UserId":17,"DisplayName":"Carlos Villa","LoginName":"carlos.villa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 
 3640c787-e484-411f-8bcc-aa212628d29f 
 1!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 e72ab26c-e72a-4f88-921c-09ee2de65b53 
 2025-08-15T00:12:39.3960263Z 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2F__rectSitelogo__Avatar-EatCloud.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2F__rectSitelogo__Avatar-EatCloud.png 

 {"SessionId":"50d0a3d6-64d5-41d8-a9da-9c4d80d4afb8","SequenceId":11,"FluidContainerCustomId":"5aa3bf6d-dfda-48d6-a6e2-bf9698eb152b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 17;#i:0#.f|membership|carlos.villa@eatcloud.com 
 Carlos Villa 
 1092.00000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"On"}] 

 Logica super puntos | puntos gestion