# mensajería-para-promover-el-registro-de-la-hora-de-salida.aspx

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
 El sistema generar un anuncio para recordar el registro de la salida del beneficiario de un anuncio segn lo definido en eatc_timeout_rules ***DINAMIZAR para mltiples cuentas maestras*** 
&#160; 
 El sistema debe peridicamente (cada 30 minutos), correr un proceso que compare la hora actual con la hora del checkin ( eatc-picking_checkin_datetime) y si determina que el tiempo transcurrido es mayor al definido en la regla de timeout respectiva&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=checkout_timeout&#160;&#160;&#160;&#160;&#160; 
&#160; 
 se debe generar un mensaje push que llegue al telfono e invite al usuario a registrar la salida del beneficiario. 
&#160; 
 Ejemplo, eatc_cua_master. eatc_cua, ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=checkout_timeout &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Dado que la respuesta (a 29 de octubre de 2020) es&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;4&quot;, 
 eatc-code &#58; &quot;4&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;checkout_timeout&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre el check-in y el check-out (para generacin de alertas)&quot;, 
 eatc-timeout_in_minutes &#58; &quot;20&quot;, 
 eatc-timeout_in_hours &#58; &quot;0,33&quot;, 
 eatc-timeout_from &#58; &quot;eatc-picking_checkin_datetime&quot; 
 &#125; 
&#160; 
 Si no existe un registro en eatc-picking_checkout_datetime (o el mismo es igual a 0000-00-00 00&#58;00&#58;00 ) El sistema debe comparar la hora actual con ( eatc-timeout_from ) eatc-picking_checkin_datetime y si han pasado ( eatc-timeout_in_minutes ) 0,33 horas o ( eatc-timeout_in_hours ) 20 minutos se debe generar el mensaje push 
&#160; 
 El mensaje push debe tener la siguiente leyenda&#58;&#160; 
&#160; 
 Han pasado ms de &#123;&#123;eatc_timeout_rules. eatc-timeout_in_minutes &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=checkout_timeout&#125;&#125; minutos desde el registro de la hora de llegada al punto de donacin. Si ya saliste del lugar, por favor registra la hora de salida. 
&#160; 
 y al hacer click en el anuncio lo debe direccionar idealmente al dashboard del anuncio en cuestin, y si esto no es posible, a Mis Donaciones. 
&#160; 
 Consulta de anuncios&#58;&#160; 
 El sistema debe consultar aquellos anuncios que tengan un registro&#160; vlido en eatc-picking_checkin_datetime (diferente a 0000-00-00 00&#58;00&#58;00) para operar este proceso. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MENSAJERA PARA PROMOVER EL REGISTRO DE LA HORA DE SALIDA DEL BENEFICIARIO