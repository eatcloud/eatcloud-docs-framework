# WAPP-Modernizada--mejora-al-invocar-el-servicio-para-marcar-como-not_delivered-una-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad existe una implementación de API pública para cancelación / no entrega / borrado de donación que debe ser invocada desde la WAPP para marcar como no entregada una donación.&#160; 
&#160; 
 DEPRECADO&#58; Dada la detección de malos manejos de esta funcionalidad, se incorporan validaciones para que el botón solamente se despliegue para donaciones en estado “ scheduled ” y a partir de 24 horas después a la hora registrada en &#160;“ eatc-programed_picking_datetime ”.&#160; 
&#160; 
Despliegue del botón a partir del timeout “dona_not_delivered_from_scheduled” 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable a la &#123;&#123;cua_user&#125;&#125; respectiva 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_not_delivered_from_scheduled&amp;cua= &#123;&#123;cua_user&#125;&#125; &amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
Si no hay respuesta, entonces se deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_not_delivered_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
 En caso de no tener una respuesta del servicio, entonces dejar como valor por defecto 24 horas (quemado en el código) 
&#160; 
 El tiempo mínimo no ha transcurrido&#58; 
 Esto quiere decir que la fecha y hora actual es anterior (está en el pasado) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &lt; &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Si el tiempo mínimo no ha transcurrido,&#160; NO SE PODRÁ MOSTRAR EL BOTÓN &#160;&quot; Marcar como no entregado &quot; en la WAPP, y por lo tanto el anuncio no se podrá marcar de esa manera. 

&#160; 
 El tiempo mínimo ya se cumplió&#58; 
 Esto quiere decir que la fecha y hora actual es posterior (está en el futuro) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; &lt; &#123;&#123;fecha_hora_actual&#125;&#125; 
&#160; 
 Si el tiempo mínimo ya transcurrió, entonces se deberá Mostrar el botón &quot; Marcar como no entregado &quot; y al accionarse, seguir el proceso. 

&#160; 
 Además se solicita que en el llamado al servicio se incorpore el parámetro con el valor constante indicado (todos los llamados desde la WAPP al API pública deberán ser marcadas como registradas por el POD, como lo indica el valor establecido). 
&#160; 
&#160; 
 eatc-state_2 = not_delivered _ registered _by_pod 
 Anteriormente&#58; eatc_state_2 = not_delivered_by_pod 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 3abc744b-ec2a-4cba-a64d-7e960d7574d6 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 16b7421b-17a8-42ab-9df5-4bbe66af1cc5 
 2026-06-17T23:50:42.6861917Z 

 {"SessionId":"169b09ff-d0ae-4a71-bce2-1afcc90d9fa9","SequenceId":1142,"FluidContainerCustomId":"adfa4ab7-7588-4993-acf9-af7404a91f20","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-17T16:07:39.2681819Z"}] 

 WAPP Modernizada: mejora al invocar el servicio para marcar como not_delivered una donación