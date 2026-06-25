# Reprogramación-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

Para la reprogramación de donación se hacen 2 consultas&#58; 

Consulta al historial de donaciones para saber cuantas veces ha sido programada una donación de la siguiente manera&#58;
 $&#123; URL_DONANTES &#125; api/ $&#123; cuaMaster &#125; /eatc_dona_header_state_history?eatc-dona_header_code= $&#123; donationInfo[ &quot;eatc-code&quot; ] &#125; &amp;eatc-state=scheduled&amp;_cont &#160; 

Se hace una consulta a la tabla modernizada reprogramation_attempts la cual aloja el numero de reintentos de programación que tiene permitido un beneficiario, con tipología, &#160;y cua_master. 
&#160; 
La segunda estructura de la tabla reprogramation_attempts se puede observar aqui&#58; 
&#160; 

&#160; 
La segunda consulta lo que hace es primero buscar coincidencia con la columna “ code_donation_manager ” con &quot; cua_master &quot;, de no haberla, busca en la columna “ doma_typology_b ” con “ cua_master ”, y si aun no encuentra coincidencias, busca el registro donde &#160;“ code_donation_manager ” y “ doma_typology_b ” estén vacíos y solo haya coincidencia con el campo “ cua_master ”. 
&#160; 
Una vez que se obtengan ambos valores, se compara el valor de &#123;&#123; reprogramation_attempts &#125;&#125; con el obtenido en la primera consulta y si es mayor, se permite la reprogramación, de lo contrario no. 

 [{"UserId":17,"DisplayName":"Carlos Villa","LoginName":"carlos.villa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 
 b69898ac-34c5-4b26-aab7-741f0154ee77 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 0f504979-5d10-469b-9872-83aed93decbe 
 2025-08-15T08:17:25.5421373Z 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%289%29%2F84477-content.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%289%29%2F84477-content.png 

 {"SessionId":"ddd8f320-cd1a-4956-a4bb-d1726107a5e9","SequenceId":-1,"FluidContainerCustomId":"7a8bcdda-6079-44b6-8600-bc6092723ce6","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1098.00000000000 
 17;#i:0#.f|membership|carlos.villa@eatcloud.com 
 Carlos Villa 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"On"}] 

 Reprogramación de donación