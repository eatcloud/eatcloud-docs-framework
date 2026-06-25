# LIBERACIÓN-automática-de-donaciones-programadas-no-recogidas.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Cronjob para ejecutar el proceso 
Se deberá configurar un cronjob que corra por cuenta maestra &#123;&#123;cua_master&#125;&#125; (puede ser cada dos horas de 7 AM a 7 PM) y que itere las diferentes cuentas usuario &#123;&#123;cua_user&#125;&#125; de cada cuenta maestra, dado que para operar deberá realizar consultas por cua_user, para poder operar. 
&#160; 
Las consultas que se deberán hacer por cada &#123;&#123;cua_user&#125;&#125; para operar el proceso serán las siguientes&#58; 
Consultar las donaciones con estado scheduled 
El sistema deberá determinar cuales donaciones están en el día particular con estado “scheduled” 
&#160; 
 &#123;&#123;URL_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; / eatc_dona_headers ?eatc-donor= &#123;&#123;cua_user&#125;&#125; &amp;eatc-publication_date[0]=&#123;&#123;current_date&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;current_date&#125;&#125;&amp;eatc-state=scheduled&amp;_cmp=eatc-code, eatc-programed_picking_datetime 
Para cada una de las donaciones encontradas el sistema deberá realizar la siguiente evaluación&#58; 
 DONACIÓN Con estado &quot; SCHEDULED &quot;&#58; Determinación si la fecha actual es anterior a la fecha de recogida programada más un TIMEOUT, para invocar el proceso “libdona” 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua= &#123;&#123;cua_user&#125;&#125; &amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
 Si no hay resultados entonces deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
&#160; 
 Ejemplo cuenta maestra abaco en ambiente de pruebas &#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
 res &#58; 
 [ 
 &#123; 
 eatc-timeout_description &#58; &quot;Tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada&quot; , 
 eatc-timeout_in_minutes &#58; &quot;30&quot; , 
 eatc-timeout_in_hours &#58; &quot;0,5&quot; , 
 eatc-timeout_from &#58; &quot;eatc-programed_picking_datetime&quot; 
 &#125; 
 ], 
 Si la consulta no arroja respuesta, se tomará como valor por defecto&#58; 
 eatc-timeout_in_minutes &#58; &quot;30&quot; , 
 eatc-timeout_in_hours &#58; &quot;0,5&quot; , 
&#160; 
 Es decir que este timeout indica un tiempo mínimo que se debe esperar antes de poder liberar la donación contado a partir de la fecha de recogida programada. 
&#160; 
 El sistema deberá determinar, a la hora consultar la donación y que la misma aparezca en el listado de donaciones , ese tiempo mínimo ha transcurrido o no. 
&#160; 
 El tiempo mínimo no ha transcurrido&#58; 
 Esto quiere decir que la fecha y hora actual es anterior (está en el pasado) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &lt; &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Si el tiempo mínimo no ha transcurrido, NO SE invocará el servicio “libdona” &quot; Liberar donación &quot; para liberar automáticamente esta donación. 

&#160; 
 El tiempo mínimo ya se cumplió&#58; 
 Esto quiere decir que la fecha y hora actual es posterior (está en el futuro) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; &lt; &#123;&#123;fecha_hora_actual&#125;&#125; 
&#160; 
 Si el tiempo mínimo ya transcurrió, entonces se deberá invocar el servicio “ libdona ” para liberar la donación. &#160;En la causal que recibe el servicio según su documentación ( eatc_dona_release_cause ) se deberá enviar&#58; “liberación automática por no recogida en hora establecida” 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 20ef30a3-e0a0-4399-be96-b43b885922b4 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 7b464c19-5e8f-40a3-9611-8f139544f43f 
 2025-05-13T23:08:45.1763751Z 

 {"SessionId":"675b299c-03fb-461c-ac97-94dc4d8c5f65","SequenceId":92,"FluidContainerCustomId":"12cc408a-86ef-4880-980f-4407fb632e52","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"Off"}] 

 LIBERACIÓN automática de donaciones programadas no recogidas