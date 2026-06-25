# mensajería-anuncios-no-adjudicados.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mensajería para diferentes cuentas maestras&#58; 
 El proceso de generación de estos mensajes push debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 
&#160; 
 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 
&#160; 
 El sistema generará una alerta para avisar sobre los anuncios que no han sido adjudicados después de un tiempo prudencial según lo definido en eatc_timeout_rules 
 El sistema debe periódicamente (cada 30 minutos), correr un proceso que compare, para los anuncios cuyo estado (eatc-state) sea &quot; announced &quot;, la hora actual con la hora de publicación ( eatc-picking_checkout_datetime) y si determina que el tiempo transcurrido es mayor al definido en la regla de timeout respectiva&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=non_award_alert&amp;cua=&#123;&#123;cua_user&#125;&#125;&#160;&#160;&#160; 
&#160; 
 Se debe generar un mensaje que llegue a un grupo de Telegram de Operaciones (PENDIENTE DE INVESTIGACIÓN&#58; aquí un recurso en donde se puede ver cómo efectuar esta operación&#58; https&#58;//www.youtube.com/watch?v=7wOtnnbpmNA ) 
&#160; 
 Ejemplo , eatc_cua_master. eatc_cua, cuenta &quot;exito&quot; ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=non_award_alert&amp; cua=exito &#160; &#160;&#160;&#160; 
&#160; 
 Dado que la respuesta (a 29 de octubre de 2020) es&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;6&quot;, 
 eatc-code &#58; &quot;6&quot;, 
 cua &#58; &quot;exito&quot;, 
 eatc-timeout_name &#58; &quot;non_award_alert&quot;, 
 eatc-timeout_description &#58; &quot;Alerta cuando un anuncio no ha sido adjudicado después de un tiempo prudente&quot;, 
 eatc-timeout_in_minutes &#58; &quot;180&quot;, 
 eatc-timeout_in_hours &#58; &quot;3&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot; 
 &#125; 
&#160; 
 Si el estado del anuncio (eatc_dona_headers. eatc-state) es igual a &quot;announced&quot;, el sistema debe comparar la hora actual con ( eatc-timeout_from ) &quot;eatc-publication_datetime&quot; y si han pasado ( eatc-timeout_in_minutes ) 180 minutos o ( eatc-timeout_in_hours ) 3 horas, se debe generar el mensaje al grupo de Telegram &quot;EATCLOUD Operaciones ( https&#58;//web.telegram.org/#/im?p=g477365321 ) en donde se entreguen los datos principales del anuncio 
&#160; 
 El mensaje al grupo de Telegram debe tener la siguiente leyenda la siguiente leyenda&#58;&#160; 
 Han pasado más de &#123;&#123;eatc_timeout_rules. eatc-timeout_in_minutes &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=non_award_alert&amp;cua=&#123;&#123;cua_user&#125;&#125; &#125;&#125; minutos desde la publicación del del anuncio de donación &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; de &#123;&#123;eatc_dona_headers. eatc-pod &#125;&#125; de la ciudad de &#123;&#123;eatc_dona_headers. eatc-city &#125;&#125; que consta de &#123;&#123;eatc_dona_headers. eatc_references &#125;&#125; referencias y un peso aproximado de &#123;&#123;eatc_dona_headers. eatc-total_weight_kg &#125;&#125; KG y el mismo no ha sido adjudicado. Te agradecemos lo verifiques para completar el proceso y su estado pueda quedar como &quot;recibido&quot;. 
&#160; 
&#160; 

&#160; 
 ***NUEVO &#58; envío de correo electrónico con alerta *** 
 El sistema deberá consultar si existen datos en el campo “”, con el ánimo de establecer si se genera un correo de alerta (redundante al mensaje de Telegram) con la misma información implementada originalmente en el mensaje. &#160;Para hacerlo debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud/ eatc_cua?name= &#123;&#123;cua_user&#125; &#125;&amp;_cmp= eatc_non_award_alert_email 
Si la respuesta no arroja datos, arroja una respuesta nula, vacía, en cero o no válida, o incorrecta, entonces el sistema no genera ningún correo electrónico. &#160;Si se recibe una respuesta válida (es decir uno o varios correos electrónicos), entonces el sistema genera un correo electrónico de la siguiente manera
&#160; 
 Asunto&#58; Donación de &#123;&#123;cua_user&#125;&#125; sin ser adjudicada 
 Remitente&#58; noreply@eatcloud.com 
 Destinatario(s)&#58; &#160; &#123;&#123; eatc_cua. eatc_non_award_alert_email &#125;&#125; 
&#160; 
 Cuerpo&#58; &#160; &#123;&#123;el mismo utilizado para la alerta de Telegram&#125;&#125; 
 Ejemplo 1 , cua_user &quot;exito&quot; ambiente de productivo&#58; 
El sistema realiza la siguiente consulta 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;_cmp=eatc_non_award_alert_email&#160; 
&#160; 
 Dado que la respuesta (a 24 de febrero de 2025) es&#58; 
&#160; 
&#123; 
 ts &#58; &quot;250224162317&quot;, 
 op &#58; false, 
 err_msg &#58; &quot;Unknown column 'eatc_non_award_alert_email' in 'field list'&quot;, 
 err_num &#58; 1054, 
 mem &#58; 0.41, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
&#125; 
(Incorrecta) entonces no se genera ningún correo electrónico. 
&#160; 
 Ejemplo 2 , cua_user &quot;aco&quot; ambiente de pruebas&#58; 
El sistema realiza la siguiente consulta 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=aco&amp;_cmp=eatc_non_award_alert_email&#160; 
&#160; 
 Dado que la respuesta (a 24 de febrero de 2025) es&#58; 
&#160; 
 &#123; 
 eatc_non_award_alert_email&#58; &quot; marcela.rodriguez@eatcloud.com &quot; 
 &#125; 
Entonces se genera un correo de la siguiente manera 
&#160; 
 Asunto&#58; Donación de aco sin ser adjudicada 
 Remitente&#58; noreply@eatcloud.com 
 Destinatario(s)&#58; &#160; marcela.rodriguez@eatcloud.com &#160; 
&#160; 
 Cuerpo&#58; &#160; &#123;&#123;el mismo utilizado para la alerta de Telegram&#125;&#125; 
&#160; 
&#160; 
 Consulta de anuncios&#58;&#160; 
&#160; 
 El sistema debe consultar aquellos anuncios con estado ( eatc-state ) &quot;announced&quot; (anunciados), para efectuar la verificación. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-state=announced&#160; 

&#160; 
 Ejemplo , eatc_cua_master. eatc_cua, ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=delivered &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=announced&amp;_compress &#160;&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"On"}] 
 026419da-2312-4e68-a653-00e3c03bc1bd 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 18206db0-393e-4acb-84a2-795276662991 
 2025-08-09T00:46:12.7539830Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"bf83f402-2c49-49c8-aab9-a097eac3cac2","SequenceId":126,"FluidContainerCustomId":"3b84bf2e-109d-464c-8271-cc8a33971c3d","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 MENSAJERÍA DE ALERTA PARA ANUNCIOS NO ADJUDICADOS