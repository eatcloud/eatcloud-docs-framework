# Logica-a.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

 Introducción a la lógica base 
&#160; 
Para entender la lógica de multiples nubes primero debemos establecer la lógica base, existe un sistema tipo “jerargico” donde varios usuarios pueden pertenecer a un solo punto de donación, varios puntos de donación pertenecen a un donante (cua_user) y varios donantes pertenecen a una nube (cua_master). 
 Solucion 
Se adiciona un campo a la tabla “cua_users” llamado multiple_clouds, de tipo boolean, el cuál al estár en 1 o true hace referencia a que dicho donante tiene más de una nube diferente de la nube usada para la creación de donaciones. 
Al tener dicho campo como true o 1, se debe hacer una consulta a la tabla “multiple_cua_masters” con el parametro de busqueda code_cua_user=&#123;&#123;cua_user&#125;&#125;, para asi hallar las nubes a las que pertenece dicho donante. 
&#160; 
Para hacer tales consultas se puede seguir la lógica de consultas privadas . 
&#160; 

 [{"UserId":17,"DisplayName":"Carlos Villa","LoginName":"carlos.villa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 
 70bc01bc-300f-4295-a0ad-c5ad862cde25 
 1!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 3d45d67c-2979-409c-bc55-70d2a8e1395a 
 2025-07-22T15:29:29.1141566Z 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%287%29%2F96376-110e0a51-ce97-4c82-a0a8-c2aa468a73b1.jpg, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%287%29%2F96376-110e0a51-ce97-4c82-a0a8-c2aa468a73b1.jpg 

 {"SessionId":"3b173c5d-661a-4fb1-92e1-6719469e37b9","SequenceId":1735,"FluidContainerCustomId":"a4e854ad-99fe-4d23-83db-6c91faa81252","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 17;#i:0#.f|membership|carlos.villa@eatcloud.com 
 Carlos Villa 
 1023.00000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 Logica de multiples nubes