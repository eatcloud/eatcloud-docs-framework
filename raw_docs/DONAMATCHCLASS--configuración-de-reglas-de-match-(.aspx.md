# DONAMATCHCLASS--configuración-de-reglas-de-match-(.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nueva estructura para establecer las reglas de clasificación con herramienta para llenar dicho campo 
 Se ha definido que en adelante, las reglas de clasificación para el match, recidirán en el campo eatc_conditions de la estructura 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/dona_match_classification_querys?_campos 
 La definición de estas clasificaciones se generarán con esta herramienta que es un &#160;genrador de json que se lleva a dicho campo&#58; 
 https&#58;//jdreatcloud.github.io/generador-reglas/ &#160; 
&#160; 
 El principal avance de esta metodología es que se podrán generar reglas por cualquiera de los campos de la donación, con una gama completa de operadores para evaluar dichos campo 

Y pudiendo agregar múltiples reglas que se deben cumplir todas para que el anuncio quede clasificado como se establece en el campo “eatc_result”. &#160;Adicional a esto, se establece un campo “ eatc_priority ” que sirve para “desempatar” reglas que ya se pueden generar en un número plural para cada anuncio. &#160;Por eso, es importante al generar reglas que varias le apliquen a un mismo anuncio, se deberá establecer cuál será la más prioritaria (de número de prioridad más bajo) para que sea esta la que le aplique al anuncio. &#160;Como estipulación general, se puede establecer que en la mayoría de los casos, la regla más específica, es la que aplica con prioridad, sobre reglas menos específicas o más generales. 
&#160; 
También en términos generales, los campos que deberán llenarse para configurar una regla de match, serán&#58; 
 eatc_cua_master 
 eatc-donor (cua_user) 
 eatc_result 
&#160; 
 Se ha generado una colección POSTMAN “CRUD query clasification CUA” para esta configuración&#58; https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/folder/11174160-c9f7ca25-85c1-447f-8a97-c33b7ce3b197?action=share&amp;creator=11174160&amp;active-environment=11174160-866b076d-41f4-4102-aade-7f4da0d32617 &#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FDONAMATCHCLASS--configuraci%C3%B3n-de-reglas-de-match-%28%2F1766522845456image.png&ow=665&oh=278, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FDONAMATCHCLASS--configuraci%C3%B3n-de-reglas-de-match-%28%2F1766522845456image.png&ow=665&oh=278 

 d11d2d29-cd64-4e0a-a453-4addf7fb0df4 
 3!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 296693b2-89ae-4906-9dfd-65d10cf0145c 
 2025-12-24T04:41:55.2704965Z 

 {"SessionId":"9b1f726c-c0e9-4a0b-b422-941562f09157","SequenceId":3510,"FluidContainerCustomId":"cf9ef1f4-6a3a-4188-ab8b-de145e4ba778","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1179.00000000000 

 dona_match_classification_querys: configuración de reglas de match