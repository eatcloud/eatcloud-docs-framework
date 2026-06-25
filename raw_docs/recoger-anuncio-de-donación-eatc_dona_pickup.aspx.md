# recoger-anuncio-de-donación-eatc_dona_pickup.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Consulta de datos del anuncio ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 El sistema debe presentar la siguiente informacin contenida en el anuncio de donacin (eatc_dona_headers) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;valor&#125;&#125; 
&#160; 
 Nombre de quien recoge&#58; 
 Muestra la informacin del campo &quot;eatc-picker_name&quot;. 
&#160; 
 Documento de identidad de quien recoge (OJO que no est en el diseo adjunto)&#58; 
 Muestra la informacin del campo &quot;eatc-picker_doc_id&quot;. 
&#160; 
 Placa del vehculo&#58; 
 Muestra la informacin del campo &quot;eatc-picker_license_plate&quot;. 
&#160; 
 Fecha y hora de recogida programada (OJO que no est en el diseo adjunto)&#58; 
 Muestra la informacin del campo &quot;eatc-programed_picking_datetime&quot;. 
&#160; 
 Faltan ##hrs ##min&#58; (OJO que no est en el diseo adjunto)&#58; 
 Tomando el dato de &quot; eatc-programed_picking_datetime &quot;, se coloca lo que falta para llegar a dicha fecha programada con respecto del tiempo actual 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , se muestra la siguiente informacin (siendo el&#58; 2019-09-17 01&#58;37&#58;54 ) 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717 

 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717&amp;_compress &#160; 
&#160; 
 Nombre de quien recoge&#58; Juan Prez 
 Documento de identidad de quien recoge &#58; 77777777 
 Placa del vehculo&#58; HHH777 
 Fecha y hora de recogida programada&#58; 2019-09-19 01&#58;37&#58;54 
 Faltan&#58; 2 horas y 0 minutos 

&#160; 
 Botn &quot;Confirmar recogida&quot; 
 Actualizacin de informacin de encabezado de anuncio de donacin (eatc_dona_headers) 
 Cuando se confirma la programacin, se debe tomar la fecha y hora en que se oprime el botn y las coordenadas del dispositivo y guardarlas en los campos . 
&#160; 
 eatc-picker_start_datetime&#58; 
 eatc-picker_lat&#58;&#160; 
 eatc-picker_lon&#58;&#160; 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-picker_start_datetime =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_lat =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_lon =&#123;&#123;valor&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;valor&#125;&#125; 

&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , el usuario de la app presion el botn &quot; Confirmar recogida &quot; el 2019-09-19 01&#58;00&#58;00 en una ubicacin cuya latitud es&#58; 6.2526506 y longitud es&#58; -75.5968567 (segn el dispositivo) 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-picker_start_datetime = 2019-09-19%2001&#58;00&#58;00 &amp; eatc-picker_lat = 6.2526506 &amp; eatc-picker_lon = -75.5968567 &amp;WHEREeatc-code= 40717 &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria.&#160; El registro actualizado puede consultarse aqu&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717 

&#160; 
 Mensaje si quien recoge no es quien registra&#58; 
 Si el usuario escoge la opcin de que no es quien recoge, el sistema le debe entregar un mensaje con lo siguiente&#58; 
&#160; 
Recuerde entegarle a la persona quien recoge (&#123;eatc_dona_headers. eatc-picker_name&#125; identificado con documento de identidad &#123;eatc_dona_headers. eatc-picker_doc_id&#125; ) la siguiente informacin&#58; 
&#160; 
Cdigo de recogida&#58; &#123;eatc_dona_headers. eatc-verification_code&#125; 
Cdigo del anuncio de donacin&#58; &#123;eatc_dona_headers. eatc-code&#125; 
Fecha y hora programada de recogida&#58; &#123;eatc_dona_headers. eatc-programed_picking_datetime&#125; 
&#160; 
 Ideal que esto tenga una funcionalidad de copiar la informacin al portapapeles para enviarla por ejemplo al WhatsApp. 

&#160; 
 Registro en el histrico de coordenadas (eatc_dona_header_geo_history) 
 Cada vez que se registra una coordenada, la misma debe ser llevada al registro histrico de coordenadas con la respectiva API. Tomando en cuenta el ejemplo anterior con los siguientes datos&#58; 
&#160; 
 eatc-date_time= 2019-09-19 01&#58;00&#58;00 , que corresponde a eatc_dona_headers . eatc-picker_start_datetime (dado que es la primera vez que se registra.&#160; Para las subsiguientes veces ser la fecha y hora actual del dispositivo cuando se toma la coordenada) 
 eatc-dona_header_code= 40717 , que corresponde a eatc_dona_headers .eatc-code 
 eatc-lat= 6.2526506 , &#160; que corresponde a eatc_dona_headers . eatc-picker_lat&#58;&#160; 
 eatc-lon= -75.5968567 , que corresponde a eatc_dona_headers . eatc-picker_lon&#58;&#160; 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla= eatc_dona_header_geo_history &amp;_operacion=insert&amp; eatc-date_time=&#123;&#123;DATETIME&#125;&#125; &amp; eatc-dona_header_code= &#123;&#123;VALOR&#125;&#125;&amp; eatc-lat= &#123;&#123;VALOR&#125;&#125;&amp; eatc-lon= &#123;&#123;VALOR&#125;&#125; 

&#160; 
 Para el ejemplo anterior ( _DOM. cua_master=abaco)&#58; https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_geo_history &amp;_operacion=insert&amp; eatc-date_time= 2019-09-19%2001&#58;00&#58;00&amp; eatc-dona_header_code= 40717&amp; eatc-lat= 6.2526506&amp; eatc-lon= -75.5968567 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190930183903&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;2&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria.&#160; El registro actualizado puede consultarse aqu&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?_id=2 

&#160; 
 Actualizacin de informacin de coordenadas (eatc-picker_lat y eatc-picker_lon) 
 El sistema debe seguir tomando las coordenadas del dispositivo, y cada 30 segundos actualizando el registro de eatc-picker_lat y eatc-picker_lon realizando la siguiente escritura&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-picker_lat = &#123;&#123;valor&#125;&#125; &amp; eatc-picker_lon = &#123;&#123;valor&#125;&#125; &amp;WHEREeatc-code= &#123;&#123;valor&#125;&#125; 

&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente productivo&#58; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , el usuario de la app presion el botn &quot; Confirmar recogida &quot; el dispositivo muestra que 30 segundos despus de haber presionado el botn su latitud es&#58; 6.2544444 y longitud es&#58; -75.5967777 (segn el dispositivo). 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-picker_lat = 6.2544444 &amp; eatc-picker_lon = -75.5967777 &amp;WHEREeatc-code= 40717 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria.&#160; El registro actualizado puede consultarse aqu&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717 .&#160; Posterior a este registro se debe tomar la fecha y hora actual del dispositivo y proceder a realizar el registro en el histrico de coordenadas (eatc_dona_header_geo_history) . 
 Este registro de coordenadas solo para cuando se efecta la funcionalidad &quot; Validacin detallada del anuncio de donacin &quot; y con ella el anuncio pasa a un estado &quot;recibido (received)&quot; 

&#160; 
 Vnculo &quot;Cancelar&quot; 
 Retorna a la vista anterior sin efectuar ninguna operacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Frecoger-anuncio-de-donaci%C3%B3n-eatc_dona_pickup%2F2220540819-12-recoger-donaciones--eatc_dona_pickup-.png&ow=750&oh=1326, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Frecoger-anuncio-de-donaci%C3%B3n-eatc_dona_pickup%2F2220540819-12-recoger-donaciones--eatc_dona_pickup-.png&ow=750&oh=1326 

 550.000000000000 

 RECOGER ANUNCIO DE DONACIN (EATC_DONA_PICKUP)