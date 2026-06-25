# mensajería-para-promover-la-verificación-de-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** Mensajera para diferentes cuentas maestras&#58; 
 El proceso de generacin de estos mensajes push debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 
&#160; 
 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 

&#160; 
 El sistema generar un anuncio para recordar la verfificacin de un anuncio segn lo definido en eatc_timeout_rules ***DINAMIZAR para mltiples cuentas maestras*** 
 El sistema debe peridicamente (cada 30 minutos), correr un proceso que compare la hora actual con la hora de salida del beneficiario ( eatc-picking_checkout_datetime) y si determina que el timpo transcurrido es mayor al definido en la regla de timeout respectiva&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=verification_timeout&#160;&#160;&#160;&#160; 
&#160; 
 &#160;se debe genear un mensaje push que llegue al telfono e invite al usuario a verificar los anuncios pendientes 

&#160; 
 Ejemplo, eatc_cua_master. eatc_cua=abaco ambiente de produccin&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=verification_timeout &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Dado que la respuesta (a 29 de octubre de 2019) es&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;5&quot;, 
 eatc-code &#58; &quot;5&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;verification_timeout&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre el check-out y la verificacin (para generacin de alertas)&quot;, 
 eatc-timeout_in_minutes &#58; &quot;120&quot;, 
 eatc-timeout_in_hours &#58; &quot;2,00&quot;, 
 eatc-timeout_from &#58; &quot;eatc-picking_checkout_datetime&quot; 
 &#125; 
&#160; 
 Si no hay un registro vlido en campo eatc-receipt_datetime ( o el mismo es igual a 0000-00-00 00&#58;00&#58;00), el sistema debe comparar la hora actual con ( eatc-timeout_from ) eatc-picking_checkout_datetime y si han pasado ( eatc-timeout_in_minutes ) 2,00 horas o ( eatc-timeout_in_hours ) 120 minutos se debe generar el mensaje push 
&#160; 
 El mensaje push debe tener la siguiente leyenda la siguiente leyenda&#58;&#160; 
&#160; 
 Han pasado ms de &#123;&#123;eatc_timeout_rules. eatc-timeout_in_minutes &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=verification_timeout&#125;&#125; minutos desde la entrega del anuncio de donacin y el mismo no ha sido verificado. Te agradecemos lo verifiques para completar el proceso y su estado pueda quedar como &quot;recibido&quot;. 
&#160; 
 y al hacer click en el anuncio lo debe direccionar idealmente al dashboard del anuncio en cuestin, y si esto no es posible, a Mis Donaciones. 

&#160; 
 Consulta de anuncios ***DINAMIZAR para mltiples cuentas maestras***&#58;&#160; 
 El sistema debe consultar aquellos anuncios con estado ( eatc-state ) &quot;delivered&quot; (entregados), para efectuar la verificacin. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-state=delivered&#160;&#160;&#160;&#160;&#160; 

&#160; 
 Ejemplo, eatc_cua_master. eatc_cua=abaco ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=delivered &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=delivered&amp;_compress &#160;&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MENSAJERA PARA PROMOVER LA VERIFICACIN DE ANUNCIOS