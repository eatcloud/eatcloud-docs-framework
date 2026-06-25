# error-handler-para-incorporación-de-localidad-y-proyecto-especial.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ERROR HANDLER LOCALIDAD 
&#160; 
 Se implementar un proceso que correr cada da, para ir incorporando la informacin que por algn motivo no se pudo incorporar en los procesos de creacin de encabezado . Para ello el sistema realizar una consulta para determinar los cdigos de anuncios de donacin que no poseen el dato eatc_localidad_comuna para el da actual. 
&#160; 
 El sistema por lo tanto deber establecer cul es la fecha actual, para enviarla como parmetro al servicio 
 fecha_actual = &#123;&#123;fecha&#125;&#125; 
&#160; 
 En un horario nocturno (despus de las 11 PM), recibiendo el parmetro de la fecha actual ( &#123;&#123;fecha&#125;&#125; ), se debe correr un proceso que consultar los anuncios que no tienen un registro en el campo &quot;&quot;, lo cual lo podr determinar realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_actual&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_actual&#125;&#125;&amp; eatc_localidad_comuna= _vacio &amp;_cmp= eatc-code , eatc-donor , eatc-pod_id 
&#160; 
 Para cada objeto de respuesta el sistema deber realizar la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-cua=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc-id=&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&amp;_cmp= eatc_comuna_localidad 
&#160; 
 Si se obtienen datos con la consulta , el sistema deber realizar la siguiente actualizacin de datos ( para cada objeto de respuesta inicial ) , para llevar el dato que se acaba de obtener ( &#123;&#123; eatc_pods. eatc_comuna_localidad &#125;&#125; ) al dato que estaba vaco (eatc_dona_headers. eatc_localidad_comuna ) en el respectivo encabezado, es decir, para cada cdigo de donacin determinado en la consulta inicial (&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_localidad_comuna= &#123;&#123; eatc_pods. eatc_comuna_localidad &#125;&#125; &amp;WHEREeatc-code= &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si no se obtienen datos en la consulta no se realiza actualizacin de datos 

&#160; 
 ERROR HANDLER PROYECTO ESPECIAL 
 (Con base en la implementacin anterior) Se implementar un proceso que correr cada da, para ir incorporando la informacin que por algn motivo no se pudo incorporar en los procesos de creacin de encabezado . Para ello el sistema realizar una consulta para determinar los cdigos de anuncios de donacin que no poseen el dato eatc_special_project para el da actual. 
&#160; 
 El sistema por lo tanto deber establecer cul es la fecha actual, para enviarla como parmetro al servicio 
 fecha_actual = &#123;&#123;fecha&#125;&#125; 
&#160; 
 En un horario nocturno (despus de las 11 PM), recibiendo el parmetro de la fecha actual ( &#123;&#123;fecha&#125;&#125; ), se debe correr un proceso que consultar los anuncios que no tienen un registro en el campo &quot;&quot;, lo cual lo podr determinar realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_actual&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_actual&#125;&#125;&amp; eatc_special_project = _vacio &amp;_cmp= eatc-code , eatc-donor , eatc-pod_id 
&#160; 
 Para cada objeto de respuesta el sistema deber realizar la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-cua=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc-id=&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&amp;_cmp= eatc_special_project 
&#160; 
 Si se obtienen datos con la consulta , el sistema deber realizar la siguiente actualizacin de datos ( para cada objeto de respuesta inicial ) , para llevar el dato que se acaba de obtener ( &#123;&#123; eatc_pods. eatc_special_project &#125;&#125; ) al dato que estaba vaco (eatc_dona_headers. eatc_localidad_comuna ) en el respectivo encabezado, es decir, para cada cdigo de donacin determinado en la consulta inicial (&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_special_project = &#123;&#123; eatc_pods. eatc_special_project &#125;&#125; &amp;WHEREeatc-code= &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si no se obtienen datos en la consulta no se realiza actualizacin de datos 

&#160; 
 CARGADOR HISTRICO LOCALIDAD 
&#160; 
 Para las donaciones del presente ao, se debe generar un proceso, que valla recorriendo hacia atrs las fechas (hasta el 1 de enero de 2024), para invocar al error handler previmante desarrollado .&#160; Para ello deber ir envindole fechas anteriores, al inicio de corrida del error handler, para que el mismo opere de manera iterativa y discreta, y valla incorporando la informacin de localidad. 
&#160; 
 El sistema por lo tanto deber ir enviando de manera discreta, fechas anteriores al inicio de corrida del error handler , y&#160; hasta el primero de enero de 2024 
 fecha_anterior_al_inicio_error_handler = &#123;&#123;fecha&#125;&#125; 
&#160; 
 Cargador histrico Proyectos especiales 
 Para las donaciones del presente ao, se debe generar un proceso, que valla recorriendo hacia atrs las fechas (hasta el 1 de enero de 2024), para invocar al error handler previmante desarrollado .&#160; Para ello deber ir envindole fechas anteriores, al inicio de corrida del error handler, para que el mismo opere de manera iterativa y discreta, y valla incorporando la informacin de localidad. 
&#160; 
 El sistema por lo tanto deber ir enviando de manera discreta, fechas anteriores al inicio de corrida del error handler , y&#160; hasta el primero de enero de 2024 
 fecha_anterior_al_inicio_error_handler = &#123;&#123;fecha&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ERROR HANDLER: PARA INCORPORACIN DE INFORMACIN DE LOCALIDAD, PROYECTO ESPECIAL