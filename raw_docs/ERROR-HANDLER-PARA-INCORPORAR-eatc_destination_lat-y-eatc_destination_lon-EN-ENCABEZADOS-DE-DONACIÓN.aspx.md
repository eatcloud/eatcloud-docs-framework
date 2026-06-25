# ERROR-HANDLER-PARA-INCORPORAR-eatc_destination_lat-y-eatc_destination_lon-EN-ENCABEZADOS-DE-DONACIÓN.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se implementar un proceso que correr cada da, para ir incorporando la informacin que por algn motivo no se pudo incorporar en el proceso awarddona . Para ello el sistema realizar una consulta para determinar los cdigos de anuncios de donacin que no poseen el dato eatc_destination_lat y eatc_destination_lon para el da actual. 
&#160; 
 El sistema por lo tanto deber establecer cul es la fecha actual, para enviarla como parmetro al servicio&#58; 
&#160; 
 fecha_actual = &#123;&#123;fecha&#125;&#125; 
&#160; 
 En un horario nocturno (despus de las 11 PM), recibiendo el parmetro de la fecha actual ( &#123;&#123;fecha&#125;&#125; ), se debe correr un proceso que consultar los anuncios que no tienen un registro en los campos &quot; eatc_destination_lat y eatc_destination_lon &quot;, lo cual lo podr determinar realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]= &#123;&#123; fecha &#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123; fecha &#125;&#125; &amp;eatc-donation_manager_code= _novacio &amp; eatc_destination_lat = _vacio &amp; eatc_destination_lon = _vacio &amp;_cmp= eatc-code , eatc-donation_manager_code 
&#160; 
 Para cada objeto de respuesta el sistema deber realizar la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;_cmp= latitud , longitud 
&#160; 
 Si se obtienen datos con la consulta , el sistema deber realizar la siguiente actualizacin de datos ( para cada objeto de respuesta inicial ) , con el nimo de llevar los datos que se acaban de obtener ( &#123;&#123; eatc_donation_managers . latitud &#125;&#125; y &#123;&#123; eatc_donation_managers . longitud &#125; ) a los que esta an vacos (eatc_dona_headers. eatc_destination_lat, eatc_dona_headers. eatc_destination_lon ) en el respectivo encabezado, es decir, para cada cdigo de donacin determinado en la consulta inicial (&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;) 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion= update &amp; eatc_destination_lat =&#123;&#123;eatc_donation_managers. latitud &#125;&#125;&amp; eatc_destination_lon =&#123;&#123;eatc_donation_managers. longitud &#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si no se obtienen datos en la consulta no se realiza actualizacin de datos 

&#160; 
 CARGADOR HISTRICO eatc_destination_lat y eatc_destination_lon 
&#160; 
 Para las donaciones del presente ao, se debe generar un proceso, que valla recorriendo hacia atrs las fechas, para invocar al presente error handler.&#160; Para ello deber ir envindole fechas anteriores, al inicio de corrida del error handler, para que el mismo opere de manera iterativa y discreta, y valla incorporando la informacin de localidad. 
&#160; 
El sistema por lo tanto deber ir enviando de manera discreta, fechas anteriores al inicio de corrida del error handler. 
 fecha_anterior_al_inicio_error_handler = &#123;&#123;fecha&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ERROR HANDLER PARA INCORPORAR eatc_destination_lat y eatc_destination_lon EN ENCABEZADOS DE DONACIN