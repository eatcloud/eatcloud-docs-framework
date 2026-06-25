# mensajería-anuncios-no-recogidos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** Mensajera para diferentes cuentas maestras&#58; 
&#160; 
 El proceso de generacin de estos mensajes push debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 
&#160; 
 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 
&#160; 
 El sistema generar una alerta para avisar sobre los anuncios que no han sido adjudicados despus de un tiempo prudencial segn lo definido en eatc_timeout_rules ***DINAMIZAR para mltiples cuentas maestras*** 
 El sistema debe peridicamente (cada 30 minutos), correr un proceso que compare, para los anuncios cuyo estado (eatc-state) sea &quot; scheduled &quot; y no tengan un registro vlido en el campo &quot; eatc-picking_checkin_datetime &quot; (es decir que sea diferente a 0000-00-00 00&#58;00&#58;00, la hora actual con la hora programada de recogida ( eatc-programed_picking_datetime ) y si determina que el tiempo transcurrido es mayor al definido en la regla de timeout respectiva 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=non_picking_alert 
&#160; 
 se debe generar un mensaje que llegue a un grupo de Telegram de Operaciones (PENDIENTE DE INVESTIGACIN&#58; aqu un recurso en donde se puede ver cmo efectuar esta operacin&#58; https&#58;//www.youtube.com/watch?v=7wOtnnbpmNA ) 
&#160; 
 Ejemplo , eatc_cua_master. eatc_cua, cuenta &quot;exito&quot; ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=non_picking_alert &#160;&#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Dado que la respuesta (a 29 de octubre de 2020) es&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;6&quot;, 
 eatc-code &#58; &quot;7&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;non_picking_alert&quot;, 
 eatc-timeout_description &#58; &quot;Alerta cuando un anuncio no ha sido recogido despus de un tiempo prudente posterior a la hora programada&quot;, 
 eatc-timeout_in_minutes &#58; &quot;60&quot;, 
 eatc-timeout_in_hours &#58; &quot;1&quot;, 
 eatc-timeout_from &#58; &quot;eatc-programed_picking_datetime&quot; 
 &#125; 
&#160; 
 Si el estado del anuncio (eatc_dona_headers. eatc-state) es igual a &quot; scheduled &quot;, el sistema no debe comparar la hora actual con ( eatc-timeout_from ) &quot;eatc-programed_picking_datetime&quot; y si han pasado ( eatc-timeout_in_minutes ) 60 minutos o ( eatc-timeout_in_hours ) 1 hora, se debe generar el mensaje al grupo de Telegram &quot;EATCLOUD Operaciones ( https&#58;//web.telegram.org/#/im?p=g477365321 ) en donde se entreguen los datos principales del anuncio 
&#160; 
 El mensaje al grupo de Telegram debe tener la siguiente leyenda la siguiente leyenda&#58;&#160; 
&#160; 
 El siguiente anuncio de donacin no ha sido recogido segn su establecido en su programacin (lleva un retraso de ms de una hora) 
&#160; 
 Cdigo&#58; eatc-code 
 Donante&#58; eatc-donor 
 Nombre del punto de donacin&#58; eatc-pod_name 
 Direccin&#58; eatc-pod_address 
 Telfono&#58; eatc-pod_phone 
 Fecha y hora de publicacin&#58; eatc-publication_datetime 
 Estado&#58; eatc-state 
 Fecha y hora de adjudicacin&#58; eatc-adjudication_datetime 
 Cdigo beneficiario&#58; eatc-donation_manager_code 
 Nombre beneficiario&#58; eatc-donation_manager_name 
 Direccin&#58; eatc-donation_manager_address 
 Telfono&#58; eatc-donation_manager_phone 
 Fecha y hora programada de recogida&#58; eatc-programed_picking_datetime 
 Nombre de quin recoge&#58; eatc-picker_name 
 Fecha y hora de salida&#58; eatc-picker_start_datetime 
 Cdigo&#58; eatc-picking_checkin_datetime 
&#160; 

&#160; 
 Consulta de anuncios ***DINAMIZAR para que opere con mtiples cuentas maestras***&#58;&#160; 
 El sistema debe consultar aquellos anuncios con estado ( eatc-state ) &quot;scheduled&quot; (entregados), para efectuar la verificacin. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-state=scheduled 

&#160; 
 Ejemplo , eatc_cua_master. eatc_cua, ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=scheduled &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=scheduled&amp;_compress &#160; &#160;&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MENSAJERA DE ALERTA PARA ANUNCIOS QUE NO HAN SIDO RECOGIDOS