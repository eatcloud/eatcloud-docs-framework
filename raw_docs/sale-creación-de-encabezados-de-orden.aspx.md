# sale-creación-de-encabezados-de-orden.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Dado una orden de oferta de ltimo minuto ( eatc_sale_order ) la plataforma debe crear un encabezado (eatc_sale_order_headers) en donde se debern realizar algunas operaciones de totalizacin de informacin, y se adicionar informacin para facilitar las bsquedas y consolidaciones en la plataforma.&#160; 
&#160; 
 Dicho encabezado se crear en la cuenta de el entorno beneficiarios, eatcloud 
&#160; 
 &#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_headers&amp;_operacion=insert&amp; &#123;&#123;Parmetros creacin eatc_sale_order_headers &#125;&#125; 

&#160; 
 _crear_sale_order_headers.php 

 &#123;&#123;PARMETROS CREACIN EATC_SALE_ORDER_HEADERS&#125;&#125; 

 Parmetros para la creacin del registro 
 Los siguientes parmetros los debe recibir el servicio de creacin del encabezado de la orden para poder operar, y a partir de ellos realizar los registros de informacin correspondientes. 

 eatc-code &#160; 
&#160; 
 Cdigo de la cabecera del encabezado de la orden que corresponde al parmetro que se utiliza para invocar el proceso y con l se identifican los registros de detalle que se&#160; 
&#160; 
 eatc_sale_order. eatc-sale_order_header_code 

 eatc-delivery_method &#160; 
&#160; 
 Mtodo de entrega de la oferta, que se obtiene en el proceso de check-out 
 eatc_sale_order_header. eatc-delivery_method 

 Identificador nico de transaccin 

 eatc-id &#160; 
&#160; 
 identificador nico del registro en la base de datos. puede ser similar al tradicional _id 

 Constantes 

 eatc-state &#160; 
&#160; 
 Dado que el encabezado se crea despus de haberse recibido confirmacin del pago , en esta creacin su estado debe ser &quot; paid_out &quot; 
 eatc-state = paid_out //El estado al crearse el encabezado debe ser &quot; paid_out &quot;&#160; 

 Time stamps 

 eatc-date &#160; 
&#160; 
 Fecha de creacin de la orden&#160; (en formato AAAA-MM-DD) 

 eatc-datetime &#160; 
&#160; 
 Fecha y hora de creacin de la orden (en formato AAAA-MM-DD HH&#58;MM&#58;SS) 

 Transformaciones internas 

 eatc-pod_id &#160; 
 Identificador nico del punto de venta, que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-pod_id 

 eatc-donor_code &#160; 
 Identificador nico del vendedor, que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-donor_code 

 eatc-donor &#160; 
 Nombre del vendedor, que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-donor 

 eatc-cua_origin &#160; 
 Cuenta desde la cual se crea la oferta, y que se toma del detalle de la orden (eatc_sale_order..eatc-cua_origin)&#58; 
 eatc_sale_order. eatc-cua_origin 

 eatc-pod_name &#160; 
 Nombre del punto de venta (punto de entrega),&#160; que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-pod_name 

 eatc-pod_address &#160; 
 Direccin del punto de venta (punto de entrega), que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-pod_address 

 eatc-pod_phone &#160; 
 Telfono del punto de venta (punto de entrega), que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-pod_phone 

 eatc-pod_lat &#160; 
 Latitud de la ubicacin del punto de venta (punto de entrega) en coordenadas decimales, que se obtiene de la informacin del detalle del pedido&#58; 
 eatc_sale_order. eatc-pod_lat 

 eatc-pod_lon &#160; 
 Latitud de la ubicacin del punto de venta (punto de entrega) en coordenadas decimales, que se obtiene de la informacin del detalle de pedido&#58; 
 eatc_sale_order. eatc-pod_lon 

 eatc-user_code &#160; 
 Cdigo del usuario que realiza el anuncio y que se toma de la informacin de los detalles 
 eatc_sale_order. eatc-user_code 

 Querys 

 ****NUEVO**** eatc_vertical &#160; 
 Este dato corresponde al valor del parmetro vertical , de la cuenta respectiva ( eatc_cua_origin ) 
 eatc_cua. vertical (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc_cua_origin &#125;&#125;) 

&#160; 
 Ejemplo&#58; cuenta &quot;starbucks&quot; 
 Para un anuncio cuyo eatc_cua_origin es &quot; starbucks &quot; este parmetro debe guardar &quot; horeca &quot; dado que en la consulta respectiva ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= starbucks ) este es el dato guardado en el parmetro de la cuenta (CUA) vertical 

 ****NUEVO**** eatc_cua_size &#160; 
 Este dato corresponde al valor del parmetro eatc_cua_size , de la cuenta respectiva ( eatc_cua_origin ) 
 eatc_cua. eatc_cua_size (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc_cua_origin &#125;&#125;) 

&#160; 
 Ejemplo&#58; cuenta &quot;exito&quot; 
 Para un anuncio cuyo eatc_cua_origin es &quot; exito &quot; este parmetro debe guardar &quot; big_retail &quot; dado que en la consulta respectiva ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= exito ) este es el dato guardado en el parmetro de la cuenta (CUA) eatc_cua_size 

 eatc-pod_typology_a &#160; 
 Primera tipologa del punto de venta (punto de entrega)&#160; 
 eatc_pod. eatc-typology_a 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc-cua_origin&#125;&#125; /eatc_pods?eatc-id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente productivo llega informacin de una orden de donacin cuyo &quot;eatc-pod_id&quot; es &quot;39&quot; y cuyo eatc-cua_origin es &quot;exito&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot;eatc-pod_typology_a&quot; el dato &quot; ALMACENES EXITO &quot; (eatc_pod. eatc-typology_a ) 

 eatc-pod_typology_b &#160; 
 Primera tipologa del punto de venta (punto de entrega)&#160; 
 eatc_pod. eatc-typology_b 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc-cua_origin&#125;&#125; /eatc_pods?eatc-id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente productivo llega informacin de una orden de donacin cuyo &quot;eatc-pod_id&quot; es &quot;39&quot; y cuyo eatc-cua_origin es &quot;exito&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot;eatc-pod_typology_a&quot; el dato &quot; MEDELLIN &quot; (eatc_pod. eatc-typology_b ) 

 eatc-pod_typology_c &#160; 
 Primera tipologa del punto de venta (punto de entrega)&#160; 
 eatc_pod. eatc-typology_c 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc-cua_origin&#125;&#125; /eatc_pods?eatc-id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente productivo llega informacin de una orden de donacin cuyo &quot;eatc-pod_id&quot; es &quot;39&quot; y cuyo eatc-cua_origin es &quot;exito&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot;eatc-pod_typology_a&quot; el dato &quot; DISTRITO MEDELLIN B &quot; (eatc_pod. eatc-typology_c ) 

 ***NUEVO&#58; eatc-pod_size **** 
 Primera tipologa del punto de venta (punto de entrega)&#160; 
 eatc_pod. eatc-size 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc-cua_origin&#125;&#125; /eatc_pods?eatc-id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente prueba llega informacin de una orden de donacin cuyo &quot;eatc-pod_id&quot; es &quot;39&quot; y cuyo eatc-cua_origin es &quot;exito&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot;eatc-size&quot; el dato &quot; hipermercado &quot; (eatc_pod. eatc-size ) 

 eatc-user_doc_id &#160; 
 Documento de identidad del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160; Un aspecto a tomar en cuenta es que esta informacin se guardar encriptada en la base de datos y solo se desencriptar en capas de visualizacin de datos con criterios de autorizacin y seguridad. 
 eatc_sale_user. eatc-doc_id 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_doc_id &quot; el dato &quot; 71745712 &quot; (eatc_sale_user. eatc-doc_id ) 

 eatc-user_name &#160; 
 Nombre del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160; Un aspecto a tomar en cuenta es que esta informacin se guardar encriptada en la base de datos y solo se desencriptar en capas de visualizacin de datos con criterios de autorizacin y seguridad. 
 eatc_sale_user. eatc-name 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_name &quot; el dato &quot; Juan David Correa Toro &quot; (eatc_sale_user. eatc-name ) 

 eatc-user_address &#160; 
 Direccin del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160; Un aspecto a tomar en cuenta es que esta informacin se guardar encriptada en la base de datos y solo se desencriptar en capas de visualizacin de datos con criterios de autorizacin y seguridad. 
 eatc_sale_user. eatc-address 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_address &quot; el dato &quot; Calle 6 sur No. 70-215, Apto 806 &quot; (eatc_sale_user. eatc-address ) 

 eatc-user_phone &#160; 
 Telfono del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160; Un aspecto a tomar en cuenta es que esta informacin se guardar encriptada en la base de datos y solo se desencriptar en capas de visualizacin de datos con criterios de autorizacin y seguridad. 
 eatc_sale_user. eatc-phone 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_phone &quot; el dato &quot; 573113581682 &quot; (eatc_sale_user. eatc-phone ) 

 eatc-user_city &#160; 
 Ciudad del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-city 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_city &quot; el dato &quot; MEDELLIN &quot; (eatc_sale_user. eatc-city ) 

 eatc-user_province &#160; 
 Provincia, departamento o estado del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-province 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_province &quot; el dato &quot; ANTIOQUIA &quot; (eatc_sale_user. eatc-province ) 

 eatc-user_country &#160; 
 Pas del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-country 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_country &quot; el dato &quot; CO &quot; (eatc_sale_user. eatc-country ) 

 eatc-user_typology_a &#160; 
 Primera tipologa del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-typology_a 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_typology_a &quot; el dato &quot; CTO &quot; (eatc_sale_user. eatc-typology_a ) 

 eatc-user_typology_b &#160; 
 Primera tipologa del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-typology_a 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_typology_b &quot; el dato &quot; PN &quot; (eatc_sale_user. eatc-typology_b ) 

 eatc-user_typology_c &#160; 
 Primera tipologa del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-typology_a 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_typology_c &quot; el dato &quot; HU &quot; (eatc_sale_user. eatc-typology_c ) 

 eatc-user_typology_c &#160; 
 Primera tipologa del usuario que se obtiene al enviar el eatc-user_code registrado en el encabezado, al parmetro eatc-code &#160; del repositorio de usuarios eatc_sale_user .&#160;&#160; 
 eatc_sale_user. eatc-typology_a 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud / eatc_sale_users ?eatc-code= &#123;&#123;eatc-user_code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas llega informacin de una orden de donacin cuyo &quot; eatc-user_code &quot; es &quot;7777&quot;, entonces la consulta a realizar es&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ api/ eatcloud / eatc_sale_users ?eatc-code=7777 &#160;&#160; 
&#160; 
 Y por lo tanto se debe llevar al registro del encabezado de orden en el parmetro &quot; eatc-user_typology_c &quot; el dato &quot; HU &quot; (eatc_sale_user. eatc-typology_c ) 

 Funciones 

 eatc-original_price &#160;&#160; 
 Precio original&#160; total del pedido, es decir la sumatoria de &quot; eatc_sale_order. eatc-odd_original_total_price &quot;&#160; del pedido respectivo (eatc_sale_order). 
 suma( eatc_sale_order. eatc-odd_original_total_price ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc-original_price &quot; es&#58; &quot; 6 &quot;( eatc_sale_order. eatc-odd_original_total_price ) 

 eatc-total_price &#160;&#160; 
 Precio&#160; total del pedido, es decir la sumatoria de &quot; eatc_sale_order. eatc-odd_total_price &quot;&#160; del pedido respectivo (eatc_sale_order). 
 suma( eatc_sale_order. eatc-odd_total_price ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc-total_price &quot; es&#58; &quot; 6 &quot;( eatc_sale_order. eatc-odd_total_price ) 

 eatc-original_vat &#160;&#160; 
 Valor original total del impuesto a las ventas (sumatoria de todos los impuestos a las ventas aplicables a los detalles del anuncio&#58; eatc_sale_order. eatc-original_vat ) 
 suma( eatc_sale_order. eatc-original_vat ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc-original_vat &quot; es&#58; &quot; 0,957983193277311 &quot;( eatc_sale_order. eatc-original_vat ) 

 eatc-total_vat &#160;&#160; 
 Valor definitivo total del impuesto a las ventas (sumatoria de todos los impuestos a las ventas aplicables a los detalles del pedido&#58; eatc_sale_order. eatc-total_vat ), despus del proceso de verificacin 
 suma( eatc_sale_order. eatc-total_vat ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc-total_vat &quot; es&#58; &quot; 0,957983193277311 &quot;( eatc_sale_order. eatc-total_vat ) 

 eatc-original_total_other_taxes &#160;&#160; 
 Valor original total del impuesto a las ventas (sumatoria de todos los otros impuestos a los detalles del pedido&#58; eatc_sale_order.eatc-original_total_other_taxes ) 
 suma( eatc_sale_order. eatc-original_total_other_taxes ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc- original_total_other_taxes &quot; es&#58; &quot; 0,957983193277311 &quot;( eatc_sale_order. eatc-original_total_other_taxes ) 

 eatc-total_other_taxes &#160;&#160; 
 Valor&#160; total del impuesto a las ventas (sumatoria de todos los otros impuestos a los detalles del pedido&#58; eatc_sale_order.eatc-total_other_taxes ), despus del proceso de verificacin 
 suma( eatc_sale_order. eatc-total_other_taxes ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc- total_other_taxes &quot; es&#58; &quot; 0,957983193277311 &quot;( eatc_sale_order. eatc-total_other_taxes ) 

 eatc-original_total_weight_kg &#160;&#160; 
 Peso original de la orden (antes del proceso de verificacin, que puede ajustar cantidades)&#58; Sumatoria de ( eatc_sale_order. eatc-odd_original_quantity * eatc_sale_order. eatc-odd_unit_weight_kg ) 
 suma(eatc_sale_order. eatc-odd_original_quantity * eatc_sale_order. eatc-odd_unit_weight_kg ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc- original_total_weight_kg &quot; es&#58; &quot; 4 &quot;(eatc_sale_order. eatc-odd_original_quantity * eatc_sale_order. eatc-odd_unit_weight_kg ) 

 eatc-total_weight_kg &#160;&#160; 
 Peso original de la orden (despus del proceso de verificacin, que puede ajustar cantidades)&#58; Sumatoria de ( eatc_sale_order. eatc-odd_total_weight_kg ) 
 suma(eatc_sale_order. eatc-odd_total_weight_kg ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas)&#58; 
&#160; 
 En llega informacin de un anuncio de donacin cuyo &quot; eatc-sale_order_header_code &quot; es &quot;1&quot;, entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale_order? eatc-sale_order_header_code = 1 &#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc- total_weight_kg &quot; es&#58; &quot; 4 &quot;(eatc_sale_order. eatc-odd_total_weight_kg ) 

 eatc-contains_alergens &#160; 
 Si cualquiera&#160; de los detalles de la orden&#160; eatc_sale_order. eatc-contains_alergens respectivo, tiene como valor &quot; si &quot; (o 1 ) en este parmetro del encabezado se colocar &quot; si &quot;. Con solo uno que lo tenga se cumple la regla y por lo tanto el encabezado respectivo debe tener&#160; en el valor eatc_sale_order_headers. eatc-contains_alergens = si 

 eatc-closer_expiration_date &#160; 
 El sistema debe calcular cul es la fecha ms prxima de las guardadas en&#160; eatc_sale_order. eatc-closer_expiration_date y guardarla en este parmetro 

 *****AJUSTE**** eatc-offer_lifetime &#160; 
 El sistema debe colocar el menor de los tiempos de vida til de la oferta registrados en&#160; eatc_sale_order. eatc-offer_lifetime y guardarla en este parmetro.&#160; 
 Si no existe ningn registro en el parmetro se debe colocar 10* 
 Si existe por lo menos un dato con el registro 10 , se debe colocar 10* .&#160; 
 Si no existen&#160; registros con el dato 10 , y por lo menos uno con el dato 24 se debe colocar 24* .&#160; 
 Si no existen&#160; registros con el dato 10 , o&#160; 24 se debe colocar 48* 
&#160; 
 *Los valores pueden variar segn las estipulaciones que se registren en el siguiente maestro 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout 
&#160; 
 por lo tanto se deben tomar como ejemplos y no como fundamentos de la lgica a implementar 

 *****NUEVO **** eatc-offer_lifetime_until &#160; 
 El sistema debe calcular cul es la fecha ms prxima de las guardadas en&#160; eatc_sale_order. eatc-offer_lifetime_until y guardarla en este parmetro 

 eatc-verification_code 
 Cdigo de verificacin (que se utilizar en las funcionalidades &quot;Entrega oferta de ltima hora&quot;. Es un cdigo nico de 6 dgitos (puede corresponder a un hash de alguna informacin del anuncio) que se genera para cada encabezado y que servir para validar quien recoge la oferta. 

 EatCloud 
 Corresponde a informacin que se agrega a partir de la interaccin con la plataforma.&#160; Por este motivo, cuando se crea un encabezado de orden, estos datos no se envan en la creacin, para que queden vacos y sean complementados luego por procesos de las plataformas. 

 eatc-user_score = //Inicialmente se deja vaco 
 eatc-pod_score =//Inicialmente se deja vaco 
 eatc-total_volume_cm3 = //Inicialmente se deja vaco 
 eatc-provider_id = //Inicialmente se deja vaco 
 eatc-scheduling_datetime = //Fecha y hora en la cual se efectu la programacin de la recogida del anuncio de donacin 
 eatc-programed_picking_datetime = //Fecha y hora programada de la recogida del anuncio de donacin 
 eatc-picker_name = //Nombre de la persona quien recoge la donacin 
 eatc-picker_doc_id = //Documento de identidad de la persona quien recoge la donacin 
 eatc-picker_license_plate = //Nombre de la persona quien recoge la donacin 
 eatc-picker_start_datetime = // Fecha y hora en que se activa la funcionalidad de &quot;recoger anuncio de donacin&quot; 
 eatc-picker_lat = // Latitud de quien recoge 
 eatc-picker_lon = // Longitud de quien recoge 
 eatc-picking_checkin_datetime = //Fecha y hora real del ingreso a la recogida del anuncio de donacin 
 eatc_code_verification_datetime = //Fecha y hora 
 eatc-picking_checkout_datetime = //Fecha y hora real de la salida de la recogida del anuncio de donacin 
 eatc-receipt_datetime = //Fecha y hora de la recepcin del anuncio de donacin en las instalaciones del gestor de las donaciones 
 eatc-doc = //Documento soporte de la transaccin (podr ser la factura de la misma) 

 &#123;&#123;PARMETROS ACTUALIZACIN EATC_SALE_ORDER_HEADERS&#125;&#125; 

 Verificacin del anuncio 
 Una vez se realiza la verificacin del anuncio los anteriores pasos (eatc-state=recieved). El sistema ajusta (desde el dispositivo) la siguiente informacin&#58; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE ENCABEZADOS DE ORDEN DE PEDIDO (SALE)