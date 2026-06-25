# dashboard-sale-mapa-nube-de-alimentos-eatcloud.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Con grandes similitudes a la funcionalidad &quot; Bienvenida&#58; Puntos de Donacin Cercanos (eatc_alim_bienv4) 
&#160; 
 Diseo&#58; https&#58;//zeroheight.com/6217d62d5/p/27eb58-dashboard-app-eatcloud-sale-ec/b/09cbdc &#160; 

 CONSULTA DE PUNTOS DE VENTA CERCANOS 

 (Corresponde a un smil de la Opcin 1 que se haba definido para la Alimentatn pero teniendo en cuenta solo los ). Tomando las coordenadas del dispositivo ( actual_lat y actual_lon que se obtiene en el proceso de consulta respectivo ), y teniendo en cuenta el radio de consulta ( actual_sale_radius_km )&#160; determinado por el proceso de consulta respectivo . 
&#160; 
 Consulta de ofertas cercanas 
 La plataforma cuenta con el siguiente servicio&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? 
&#160; 
 Para mayor informacin consultar&#58; 
&#160; 
 Documentacin general 
 Documentacin especfica 
&#160; 
 Al cual se le envan los siguientes parmetros para realizar una consulta de las ofertas cercanas a la ubicacin del dispositivo&#58; 
&#160; 
 table&#58; en este parmetro se enva el nombre del object store (que contiene informacin georeferenciada) sobre el cual se va a realizar la consulta.&#160; Para efectos de esta consulta ser eatc_sale. 
&#160; 
 fieldname&#58; en este parmetro se envan el nombre del campo en donde se aloja el dato de latitud y longitud para el object store particular.&#160; En este caso el valor ser&#58; eatc-pod_lat,eatc-pod_lon. 
&#160; 
 fieldvalue&#58; en este parmetro se envan las coordenadas decimales, separadas por una coma, a partir de las cuales se realizar la consulta.&#160; 
 Para el caso particular sern las que correspondan a la posicin actual del dispositivo&#58; &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; . 
&#160; 
 showfield&#58; corresponde a los campos que queremos traer en la consulta desde el object store definido.&#160; Para obtener la informacin necesaria para esta vista se ha definido que la informacin que se necesita es&#58; eatc-code,eatc-pod_id,eatc-pod_name,eatc-odd_description,eatc-pod_address,eatc-pod_lat,eatc-pod_lon,eatc-odd_name,eatc-odd_unit_price,eatc-odd_min_sale_unit_price,eatc-odd_max_discount,eatc-odd_image,eatc-odd_state,eatc_cua_origin &#160; 

 km&#58; corresponde al radio de consulta en kilmetros, contados a partir de la coordenada que se enva en el parmetro fieldvalue. Se colocar en este campo el dato actual_sale_radius_km que se obtiene en el proceso de consulta respecivo . 
&#160; 
 filterfield_1&#58; corresponde al campo por el cual se quiere filtrar la informacin del object store particular. En este caso se desean traer solo las ofertas cuyo estado sea &quot;ofertadas&quot; o &quot;parcialmente ordenadas&quot;, por lo tanto el valor ser eatc-odd_state 
&#160; 
 filtervalue_1&#58; como solo se quieren ver las ofertas cuyo estado sea &quot;ofertadas&quot; o &quot;parcialmente ordenadas&quot;, en este parmetro se enva sale,partially_ordered 
&#160; 
 En ese orden de ideas se debe utilizar la siguiente consulta para traer las ofertas cercanas a la coordenada del dispositivo dispositivo&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; &amp; showfield = eatc-code,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_lat,eatc-pod_lon,eatc-odd_name,eatc-odd_description,eatc-odd_unit_price,eatc-odd_min_sale_unit_price,eatc-odd_max_discount,eatc-odd_image,eatc-odd_state,eatc_cua_origin &amp; km = &#123;&#123;actual_sale_radius_km&#125;&#125; &amp;filterfield_1= eatc-odd_state &amp;filtervalue_1= sale,partially_ordered &#160; 
&#160; 
 NOTA IMPORTANTE &#58; en el parmetro showfield se pueden enviar los parmetros que se quieren visualizar en los datos que trae la consulta, en el anterior caso solo se visualiza el eatc-pod_id, pero si se necesitan visualizar ms campos, se podr colocar cualquiera de los disponibles para el object store particular ( eatc_sale&#58; https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale?_campos ) y la respuesta los traer. 
&#160; 
 Ejemplo&#58; 
 Para un usuario (en ambiente de pruebas) que se encuentra en la coordenada&#58;&#160; 
 actual_lat= 6.25177777 
 actual_lon= -75.59877777 
 actual_sale_radius_km =5 (aplica lo establecido aqu ) 
&#160; 
 El sistema realiza la siguiente consulta 
&#160; 
 https&#58;//devdonantes.eatcloud.info//get/eatcloud/getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue =6.25177777,-75.59877777&amp; showfield = eatc-code,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_lat,eatc-pod_lon,eatc-odd_name,eatc-odd_description,eatc-odd_unit_price,eatc-odd_min_sale_unit_price,eatc-odd_max_discount,eatc-odd_image,eatc-odd_state,eatc_cua_origin &amp; km = 5 &amp;filterfield_1= eatc-odd_state &amp;filtervalue_1= sale,partially_ordered &#160;&#160; 
 &#160; 
 Con la informacin que se trae se tendrn los datos necesarios para pintar la informacin que se muestra en la presente vista 
&#160; 
 NOTA IMPORTANTE &#58; Vale la pena resaltar que la respuesta a la anterior consulta trae el parmetro km que muestra la distancia desde el punto que trae la consulta, hasta el punto cuya latitud y longitud se est entregando en el dispositivo, y servir luego para ordenar en la &quot; Marquesina de puntos de despacho &quot; por cercana (esta marquesina debe mostrar primero el ms cercano y a medida que se avance en la misma se debe ir avanzando hasta el ms lejano) 

 BUSCADOR Y ACCESO AL CARRO DE COMPRAS 

 En la parte superior se dispone un buscador, que permitir buscar ofertas. El sistema filtrar las ofertas (obtenidas en la &quot; consulta de ofertas cercanas &quot;) que contengan dicho criterio de bsqueda en los campos&#58;&#160; 
&#160; 
 eatc-odd_name 
 eatc-odd_description 
 eatc-pod_name 
&#160; 
 Los resultados de bsqueda se dispondrn en la vista Listado de productos . 
&#160; 
 cono Carro de Compras 
 Al presionar este cono se da acceso a la funcionalidad &quot; Carro de Compras &quot; 

 MAPA (CON MARQUESINA DE PUNTOS DE DESPACHO CERCANOS)&#58; 
 El punto rojo que se muestra en el mapa es el que corresponde a las coordenadas del dispositivo.&#160; se deben pintar en el mapa los puntos ( eatc-pod_lat y eatc-pod_lon ) que arroja la consulta arriba descrita. Si se seleciona uno de los puntos pintados en el mapa, se debe mostrar la siguiente tarjeta de informacin correspondiente en la marquesina de puntos de venta cercanos (que se detalla a continuacin). 

 MARQUESINA DE PUNTOS DE DESPACHO CERCANOS&#58; 
 Se constituye en la presentacin de los puntos de venta cercanos, que son trados por la &quot; consulta de ofertas cercanas &quot; y que se pueden desplegar si se le hace clic al punto correspondiente en el mapa, o al navegar de manera horizontal (swipe horizontal), presentando en primer lugar el punto ms cercano y continuando de manera ascendente segn dicha cercana (parmetro km de la consulta de ofertas cercanas ). Es una funcionalidad&#160; muy similar a la implementada en su momento para la App de la Alimentaton&#58; &quot; Carrusel de puntos de donacin cercanos &quot; y por lo tanto se puede reciclar cdigo de ella para su implementacin. 
&#160; 
 Tarjeta de informacin de punto (navegado horizontalmente en la marquesina o seleccionado en el mapa) 
 Diseo &#58; https&#58;//zeroheight.com/6217d62d5/p/30e9f2-cardsec/b/41765d/t/18db0a &#160; 
&#160; 
 Esta tarjeta debe presentar la siguiente informacin (que se toma de la &quot; consulta de ofertas cercanas &quot; y una consulta adicional para incorporar los horarios de atencin)&#58; 

 Tumbnail &#58; corresponde a la informacin que se recibe en el parmetro eatc-odd_image 
&#160; 

 Nombre restaurante (eatc_pod)&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-pod_name 
&#160; 

 Direccin &#58; corresponde a la informacin que se recibe en el parmetro eatc-pod_address 
&#160; 

 A &#123;&#123;km&#125;&#125; km de tu lugar actual &#58; con el dato que se recibe en el campo km se coloca esta informacin en la card ( no aparece en la imagen ilustrativa de la derecha ). 
&#160; 

 Horario de atencin &#58; con el dato que se recibe en el parmetro eatc-pod_id y el que se recibe en eatc_cua_origin, se realiza la siguiente consulta para traer la informacin, del da actual, y del da siguiente al actual (en la imagen se coloca un solo horario, pero la idea es que se muestre el da actual (por ejemplo&#58; LU) y el da siguiente (por ejemplo&#58; MA)) 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123; eatc_cua_origin&#125;&#125; /eatc_sale_schedule?eatc-pod_id= eatc-pod_id 

 Al hacerle click a la&#160; anterior tarjeta 
 El sistema realiza una consulta de informacin para obtener los datos del punto seleccionado y posteriormente (con esos datos recolectados) debe pasar a la vista &quot; Dashboard de punto de venta &quot;. 
&#160; 
 La consulta es la siguiente&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; &amp; showfield = _id,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_lat,eatc-pod_lon,eatc-odd_name,eatc-odd_description,eatc-odd_unit_price,eatc-odd_min_sale_unit_price,eatc-odd_max_discount,eatc-odd_image,eatc-odd_state,eatc_cua_origin &amp; km = 5 &amp;filterfield_1= eatc-odd_state &amp;filtervalue_1= sale,partially_ordered &amp;filterfield_2= eatc-pod_lat&amp; &amp;filtervalue_2= &#123;&#123;eatc-pod_lat&#125;&#125; &amp;filterfield_3= eatc-pod_lon&amp; &amp;filtervalue_3= &#123;&#123;eatc-pod_lon&#125;&#125; 
&#160; 
&#160; 
 Ejemplo&#58; 
 Un usuario (en ambiente de pruebas) ubicado en esta coordenada&#58; 
 actual_lat= 6.25177777 
 actual_lon= -75.59877777 
&#160; 
 Seleciona el punto ( eatc-pod_name) &quot; DevNodrizza plaza &quot;,&#160; ( eatc-pod_id &#58; &quot;u4bdtz0ie85xBZPKp1gaY), que tiene la siguiente informacin&#58; 
 eatc-pod_lat &#58; &quot;6.251660001544927&quot;, 
 eatc-pod_lon &#58; &quot;-75.59860641136767&quot;, 
&#160; 
 Por lo tanto el sistema debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/get/eatcloud/getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue =6.25177777,-75.59877777&amp; showfield = _id,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_lat,eatc-pod_lon,eatc-odd_name,eatc-odd_description,eatc-odd_unit_price,eatc-odd_min_sale_unit_price,eatc-odd_max_discount,eatc-odd_image,eatc-odd_state,eatc_cua_origin &amp; km = 5 &amp;filterfield_1= eatc-odd_state &amp;filtervalue_1= sale,partially_ordered &amp;filterfield_2= eatc-pod_lat &amp;filtervalue_2= 6.251660001544927 &amp;filterfield_3= eatc-pod_lon&amp; &amp;filtervalue_3= -75.59860641136767 &#160; 
&#160; 
 La informacin resultante es con la que debe trabajar la vista &quot; Dashboard de punto de venta &quot;, que es a la que debe direccionarse a partir del clic. 

 Mensajes de dashboard&#58; 
 Se constituye en la presentacin mensajes que pueden ser trados por criterios de cercana a la ubicacin del usuario, y que segn un el criterio &quot; actual_messages_radius_km &quot; que se obtiene en el proceso de consulta respectivo , se despliegan a manera de marquesina (rotador de banners) en el lugar de la App establecido para esto. 

 Consulta de los mensajes disponibles para el dashboard&#160; (sale_dashboard) 
 Diseo &#58; https&#58;//zeroheight.com/6217d62d5/p/30e9f2-cardsec/t/62d2cd &#160; 

 La App debe consultar en primera instancia el API para determinar que mensajes estn disponibles en su cercana, utilizando el servicio &quot;getpuntos&quot; (que se describi en detalle ms arriba) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? 
&#160; 
 Para mayor informacin consultar&#58; 
 Documentacin general 
 Documentacin especfica 

 Al cual se le envan los siguientes parmetros para realizar una consulta de las ofertas cercanas a la ubicacin del dispositivo&#58; 
&#160; 
 table&#58; eatc_sale_messages. 
&#160; 
 fieldname&#58; eatc-lat,eatc-lon. 
&#160; 
 fieldvalue&#58; en este parmetro se envan las coordenadas decimales, separadas por una coma, a partir de las cuales se realizar la consulta. Para el caso particular sern las que correspondan a la posicin actual del dispositivo&#58; &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; . 
&#160; 
 showfield&#58; _id,code,date,title,url,url_button_legend,url_button_icon,image_url,order,display_conditions,display_time_sec,published_since,published_until 
&#160; 
 km&#58; corresponde al radio de consulta en kilmetros, contados a partir de la coordenada que se enva en el parmetro fieldvalue. Se colocar en este campo el dato actual_message_radius_km que se obtiene en el proceso de consulta respectivo . 
&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_messages &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; &amp; showfield = _id,code,date,title,url,url_button_legend,url_button_icon,image_url,order,display_conditions,display_time_sec,published_since,published_until &amp; km = &#123;&#123; eatc-messages_radius_km &#125;&#125; 
&#160; 
 Ejemplo 1&#58; 
 Un usuario (ambiente de pruebas) con su dispositivo ubicado en la coordenada&#160; 6.2045697,-75.60157, entra al dashboard. Por lo tanto el sistema hace la siguiente consulta para traer la informacin 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 km&#58; 50 (aplica lo establecido aqu ) 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/eatcloud/getpuntos? table = eatc_sale_messages &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = _id,code,date,title,url,url_button_legend,url_button_icon,image_url,order,display_conditions,display_time_sec,published_since,published_until &amp; km = 50 &#160; 

&#160; 
 El API devuelve una respuesta que contiene los siguientes parmetros (a continuacin se dan lineamientos generales para disponer el mensaje de acuerdo a la informacin que trae el API)&#58; 
&#160; 
 _id, code, date&#58; 
 Son datos informativos que permiten diferenciar el mensaje.&#160; Por el momento no se muestran en la interfaz del usuario. 

&#160; 
 title 
 Sirve para pintar el ttulo del mensaje (se muestra como tal en la App). 

&#160; 
 &#160; message 
 Sirve para pintar el cuerpo del mensaje (se muestra como tal en la App). 

&#160; 
 url 
 URL que se abrir al presionar el rea del mensaje o el botn respectivo (que se construir de acuerdo a la informacin que se obtiene en los siguientes parmetros.&#160; Si dicha informacin viene vaca, entonces el botn no se debe pintar y solo funcionar el rea del mensaje como punto de entrada a la URL al hacerle clic). 

&#160; 
 url_button_legend &#58; ejemplo&#58; &quot;Ver ms&quot;. 
 Corresponde a la leyenda del botn que abre la URL.&#160; Si por ejemplo en este campo no trae informacin (est vaco) esto querr decir que el mismo mensaje ser el botn para abrir la URL respectiva y no habr un botn adicional (es decir el botn adicional se debe ocultar). 

&#160; 
 url_button_icon &#58; &quot;&quot;, 
 [PROXIMAMENTE&#58; NO ES NECESARIO EN UNA PRIMERA IMPLEMENTACIN] En futuras versiones se podr incorporar un pequeo cono para el botn el cual se podr desplegar desde una URL particular, con el nimo de hacerlo administrable. 

&#160; 
 image_url 
 Se constituye en la imagen de fondo del mensaje (sobre la cual se pintan el ttulo, en mensaje y el botn).&#160; Esta imagen se obtendr de la URL registrada en este campo. 

&#160; 
 order 
 Este campo servir para establecer el orden en que se muestran los mensajes, mostrndose primero el que tenga orden&#58; &quot;1&quot; , y luego los posteriores.&#160; Si hay algn empate en Orden, el criterio de desempate ser el campo km , mostrando primero el mensaje ms cercano. 

&#160; 
 display_conditions &#58; ejemplo&#58; &quot;always&quot; 
 [PROXIMAMENTE&#58; NO ES NECESARIO EN UNA PRIMERA IMPLEMENTACIN] En futuras versiones, se podrn establecer condiciones de visualizacin de los mensajes.&#160; Como en este caso el parmetro indica &quot; always &quot;, esto indica que siempre se visualiza el mensaje en este punto. 

&#160; 
 display_time_sec &#58; ejemplo &quot;7&quot;, 
 El dato recuperado en este parmetro establece el tiempo en segundos de la visualizacin de un mensaje (antes de pasar a otro de manera automtica).&#160; Cuando en este parmetro se indique que el mensaje debe estar fijo (&quot; fix &quot;) querr decir que el mensaje no rotar, ni tendr un tiempo de visualizacin, y que para pasar al prximo mensaje se tendr que hacer un swipe horizontal. 

&#160; 
 published_since, published_until &#58; 
 [PROXIMAMENTE&#58; NO ES NECESARIO EN UNA PRIMERA IMPLEMENTACIN] En futuras versiones, se podr establecer tiempos de inicio y fin de la publicacin para establecer cundo se comienza a mostrar y cundo se termina de mostrar un mensaje. 

&#160; 
 km 
 Este campo servir para establecer el orden en que se muestran los mensajes en caso de que exista empate segn la informacin obtenida en el parmetro &quot; orden &quot; , mostrando primero el mensaje ms cercano. 

&#160; 
 Al hacerle click a la&#160; anterior tarjeta 
 El sistema debe direccionar a la URL que se registra en el campo url 

 SECCIN &quot;ltimo minuto&quot;&#58; 
&#160; 
 Se constituye en la presentacin de los productos ofertados cercanos, que son trados por la &quot; consulta de ofertas cercanas &quot; y cuya informacin particular se podr desplegar si se le hace clic a la tarjeta respectiva (y cuya construccin se detalla aqu , dado que puede ser un componente reutilizable en varias vistas de la App). Es una funcionalidad&#160; muy similar a la implementada en su momento para la App de la Alimentaton&#58; &quot; Carrusel de puntos de donacin cercanos &quot; (pero en este caso presentando productos en oferta de ltimo minuto) y por lo tanto se puede reciclar cdigo de ella para su implementacin. La informacin presenta las tarjetas, ordenada por el campo km (presentando primero las ms cercanas y luego las ms lejanas) y que podr navegarse con un swipe horizontal. 
&#160; 
 El diseo de la tarjeta de informacin de producto , puede consultarse aqu . 

 Vnculo ver todo&#58; 
 Al hacerle clic a este vnculo se debe tomar la informacin obtenida por la &quot; consulta de ofertas cercanas &quot; y pasar a la vista &quot; Listado de productos &quot;. 

 MEN INFERIOR DE NAVEGACIN 
&#160; 
 Se detalla su funcionamiento aqu 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-sale-mapa-nube-de-alimentos-eatcloud%2F310986823-EmbeddedImage--85-.jpg&ow=544&oh=1266, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-sale-mapa-nube-de-alimentos-eatcloud%2F310986823-EmbeddedImage--85-.jpg&ow=544&oh=1266 
 APP Usuario final - Sale 

 785.000000000000 

 DASHBOARD PRINCIPAL: NUBE DE ALIMENTOS: MAPA