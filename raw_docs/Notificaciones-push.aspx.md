# Notificaciones-push.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Notificaciones para donaciones creadas o por adjudicar&#58; 
Para notificar a un usuario de la app modernizada sobre una donación nueva o por adjudicar se debe consumir la siguiente API&#58; 
&#123;URL_ENTORNO&#125;/apipub/notipush 
&#160; 
Reemplazando la &#123;URL_ENTORNO&#125; por el entorno en el que queremos trabajar&#58; 
Dev&#58; https&#58;//devservice.eatcloud.info 
 Producción&#58; https&#58;//service.eatcloud.info 
&#160; 
En el body se debe enviar la siguiente 

9 

&#160; 

1 
 &#123; 

2 
 &quot;expotokens&quot; &#58; %5B; &quot;token1&quot; , &quot;token2&quot; , ... %5D;, 

3 
 &quot;notification_type&quot; &#58; &quot;PushNewAnnouncementApp&quot; , 

4 
 &quot;data&quot; &#58; &#123; 

5 
 &#160; &#160; &#160; &#160; &#160; &#160; &quot;eatc_cua_master&quot; &#58; &quot;abaco&quot; , 

6 
 &#160; &#160; &#160; &#160; &#160; &#160; &quot;eatc-cancellation_datetime&quot; &#58; cancellation_date . 

7 
 &#160; &#160; &#160; &#160; &#160; &#160; ... . 

8 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#125; 

9 
 &#125; 

&#123;
 &quot;expotokens&quot;&#58; %5B;&quot;token1&quot;, &quot;token2&quot;, ...%5D;,
 &quot;notification_type&quot;&#58; &quot;PushNewAnnouncementApp&quot;,
 &quot;data&quot;&#58; &#123;
 &quot;eatc_cua_master&quot;&#58; &quot;abaco&quot;,
 &quot;eatc-cancellation_datetime&quot;&#58; cancellation_date.
 ....
 &#125;
&#125; 

En “data” se deben enviar los headers o encabezados de la donación por la cual se quiere enviar la notificación. 
Específicamente los siguientes datos&#58; 

1 

&#160; 

1 
 &#123; &quot;eatc_cua_master&quot; , &quot;eatc-cancellation_datetime&quot; , &quot;eatc-pod_id&quot; , &quot;eatc_cua_origin&quot; , &quot;eatc-warning&quot; , &quot;eatc-code&quot; , &quot;eatc-state&quot; , &quot;eatc-publication_datetime&quot; , &quot;eatc-pod_name&quot; , &quot;eatc-pod_address&quot; , &quot;eatc-total_weight_kg&quot; , &quot;eatc_prepared_food&quot; , &quot;eatc-verification_code&quot; &#125; 

&#123; &quot;eatc_cua_master&quot;, &quot;eatc-cancellation_datetime&quot;, &quot;eatc-pod_id&quot;, &quot;eatc_cua_origin&quot;, &quot;eatc-warning&quot;, &quot;eatc-code&quot;, &quot;eatc-state&quot;, &quot;eatc-publication_datetime&quot;, &quot;eatc-pod_name&quot;, &quot;eatc-pod_address&quot;, &quot;eatc-total_weight_kg&quot;, &quot;eatc_prepared_food&quot;, &quot;eatc-verification_code&quot; &#125; 

En “expotokens” se deben enviar en un array los token de los usuarios que desean ser notificados, dichos tokens se pueden encontrar en la tabla “users” de modernización en la columna “push_token”. Este API está validando si los tokens son validos o no. Por eso es importante notificar soloa los usuarios que se desean que reciban dicha notificación. 

 ***NUEVO&#58; Notificaciones para donaciones cercanas a una previamente programada&#58; *** 
 notification_type&#58; &#160; PushNearAnnouncementApp 
 to &#58; token, 
 title &#58; ´ ¡Anuncio cercano a uno que te haz adjudicado! ´, 
 body &#58; ´ Hay otro anuncio de &#123;&#123;eatc-total_weight_kg&#125;&#125; KG en el punto &#123;&#123;eatc-pod_name&#125;&#125; ´, muy cerca de donde recogerás otro que ya te haz adjudicado. Te invitamos a que también te lo adjudiques y aproveches el viaje. ¡Revisa sus detalles ahora! ´, 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Ente-Territorial--Informe-de-detalle-de-anuncios%281%29%2Fcopy-%281%29-1992761801-Captura-de-pantalla-2024-08-19-164249.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Ente-Territorial--Informe-de-detalle-de-anuncios%281%29%2Fcopy-%281%29-1992761801-Captura-de-pantalla-2024-08-19-164249.png 

 1114.00000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 e3f0623c-99a0-4a8e-8e4e-7528cfd3d9a4 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 2da6be55-7180-4cfd-a9c7-04f5f56a5b58 
 2025-12-24T03:19:57.7731171Z 

 {"SessionId":"63c3cf64-c80e-4755-acf5-b7795f026fbe","SequenceId":1403,"FluidContainerCustomId":"9b4a295b-d896-4bc4-aa60-3145e2856194","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Notificaciones push