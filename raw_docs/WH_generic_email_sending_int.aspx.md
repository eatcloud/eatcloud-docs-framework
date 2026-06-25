# WH_generic_email_sending_int.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ENVÍO DE INFORMACIÓN COMPLETA 
 Inicialmente se hace una validación muy básica para garantizar que los datos lleguen completos, por lo tanto, desde el envío se deberá garantizar que se envíen los siguientes datos&#58; 
 para &#58; correo electrónico del destinatario ( es obligatorio para la herramienta que se utiliza). 

 asunto &#58; siempre es obligatorio 

 cuerpo_html &#58; siempre obligatorio . 
&#160; 
 NOTA IMPORTANTE&#58; Por el momento no se contempla el envío de “adjuntos” por fuera del cuerpo del mensaje (como URLs) dado que en una primera prueba no funcionó. Por lo tanto los valores adjunto_archivo y adjunto_nombre se envían vacíos. 
&#160; 
&#160; 
 WEBHOOK para envío de correo genérico 
 URL Activepieces (flujo)&#58; 
 http&#58;//20.83.146.184/projects/yx5chJZTyM4OJKCU2WUw3/flows/KxzGA9kOwjk46IvsLeFDm &#160; 
Endpoint (WebHook)&#58; 
 http&#58;//20.83.146.184/api/v1/webhooks/KxzGA9kOwjk46IvsLeFDm/sync &#160; 
&#160; 
Datos en el body para invocar el WH&#58; 
 &#123; 
 &#160; &#160;&#160; &quot;data&quot; &#58; &#123; 
 &#160; &#160; &#160; &#160; &quot;rows&quot; &#58; &#160; [ 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#123; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;para&quot; &#58; &quot; &#123;&#123;email&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;cc&quot; &#58; &quot;&#123;&#123;emails_separados_por_comas&#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;bcc&quot; &#58; &quot;&#123;&#123;emails_separados_por_comas&#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;asunto&quot; &#58; &quot; &#123;&#123;string&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;cuerpo_html&quot; &#58; &quot; &#123;&#123;código_html&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;responder_a&quot; &#58; &quot;&#123;&#123;email&#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;nombre_remitente&quot; &#58; &quot;&#123;&#123;string&#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;email_remitente&quot; &#58; &quot;&#123;&#123;email&#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;adjunto_archivo&quot; &#58; &quot;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;adjunto_nombre&quot; &#58; &quot;&quot; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#125; 
 &#160; &#160; &#160; &#160;&#160; ] 
 &#160; &#160;&#160; &#125; 
 &#125; 
&#160; 
&#160; 
Respuestas endpoint&#58; 
Error&#58; datos incompletos (no se envían los datos mínimos solcitados) 
El sistema responderá de la siguiente manera 
&#123;
&#160;&quot;ok&quot;&#58; false ,
&#160;&quot;data&quot;&#58; &#123;
&#160; &#160;&quot;cc&quot;&#58; &quot; &#123;&#123;emails_separados_por_comas&#125;&#125; &quot;,
&#160; &#160;&quot;bcc&quot;&#58; &quot; &#123;&#123;emails_separados_por_comas&#125;&#125; &quot;,
&#160; &#160;&quot;para&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;asunto&quot;&#58; &quot; &#123;&#123;string&#125;&#125; &quot;,
&#160; &#160;&quot;cuerpo_html&quot;&#58; &quot; &#123;&#123;código_html&#125;&#125; &quot;,
&#160; &#160;&quot;responder_a&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;adjunto_nombre&quot;&#58; &quot;&quot;,
&#160; &#160;&quot;adjunto_archivo&quot;&#58; &quot;&quot;,
&#160; &#160;&quot;email_remitente&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;nombre_remitente&quot;&#58; &quot; &#123;&#123;string&#125;&#125; &quot;
&#160;&#125;,
&#160;&quot;message&quot;&#58; &quot; faltan_datos_para_enviar_email &quot;,
&#160;&quot;management_verification_code&quot;&#58; false 
&#125; 
&#160; 
Éxito&#58; el email fue enviado exitosamente 
El sistema responderá de la siguiente manera 
&#123;
&#160;&quot;ok&quot;&#58; true ,
&#160;&quot;data&quot;&#58; &#123;
&#160; &#160;&quot;cc&quot;&#58; &quot; &#123;&#123;emails_separados_por_comas&#125;&#125; &quot;,
&#160; &#160;&quot;bcc&quot;&#58; &quot; &#123;&#123;emails_separados_por_comas&#125;&#125; &quot;,
&#160; &#160;&quot;para&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;asunto&quot;&#58; &quot; &#123;&#123;string&#125;&#125; &quot;,
&#160; &#160;&quot;cuerpo_html&quot;&#58; &quot; &#123;&#123;código_html&#125;&#125; &quot;,
&#160; &#160;&quot;responder_a&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;adjunto_nombre&quot;&#58; &quot;&quot;,
&#160; &#160;&quot;adjunto_archivo&quot;&#58; &quot;&quot;,
&#160; &#160;&quot;email_remitente&quot;&#58; &quot; &#123;&#123;email&#125;&#125; &quot;,
&#160; &#160;&quot;nombre_remitente&quot;&#58; &quot; &#123;&#123;string&#125;&#125; &quot;
&#160;&#125;,
&#160; &#160;&quot;date&quot;&#58; &quot; &#123;&#123;fecha_envio_correo&#125;&#125; &quot;,
&#160;&quot;message&quot;&#58; &quot; statusText_OK &quot;,
&#160;&quot;management_verification_code&quot;&#58; true 
&#125; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-verificaci%C3%B3n-del-codigo-de-recogida%281%29%281%29%2Fcopy-%282%29-3406938382-captura_obligatoria_eatc_doc.jpg&ow=1233&oh=731, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-verificaci%C3%B3n-del-codigo-de-recogida%281%29%281%29%2Fcopy-%282%29-3406938382-captura_obligatoria_eatc_doc.jpg&ow=1233&oh=731 

 1235.00000000000 
 90bc37b5-1c34-47a4-814a-00eb73b6ed13 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 e9d51143-3c6e-4ba6-9650-9db17e96b986 
 2026-06-10T04:26:26.1410836Z 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-09T20:27:03.2787663Z"}] 
 eatcloud donantes web-app 
 {"SessionId":"e6f101c4-15bd-4229-9e39-5a5a7222c2a3","SequenceId":32,"FluidContainerCustomId":"f1ee98a0-ded0-4819-bd3a-3d5e1bceab14","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 

 WH_generic_email_sending_int