# consulta-de-datos-de-orden-abierta.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Con esta consulta se establece el dato de las cantidades_agregadas_a_la_orden para una orden abierta (que es aquella que no posee an registro de cdigo de cabecera: eatc-sale_order_header_code ) , recuperando este dato para mostrarlo en el botn de "agregar al carrito de compras" como dato inicial.  Tambin se validan los casos principales de operacin para la creacin de registro de orden . 

 Para hacer esta consulta el sistema debe tomar el cdigo del item ofertado ( eatc_sale.eatc-code ) y con l realizar un llamado al API eatc_sale_order , para el cdigo del usuario respectivo ( eatc_sale_users.eatc-code que se toma del proceso de obtencin de cdigo de usuario ) de la siguiente manera: 

 {{URL_entorno_beneficiarios}}/api/eatcloud/eatc_sale_order? eatc-sale_code = {{eatc_sale.eatc-code}}& eatc-user_code ={{ eatc_sale_users.eatc-code }} 

 Con la consulta se pueden presentar los siguientes casos, que deben ser manejados como se explica a continuacin, tanto para obtener el dato de cantidades_agregadas_a_la_orden , como para definir que accin de debe realizar para crear el registro en la respectiva eatc_sale_order ( insert o update ) 

 Ejemplo caso 1: existe por lo menos un registro de orden que est en proceso 
 En ambiente de pruebas, el usuario cuyo eatc-user_code es 7777 , est agregando a partir de un tem ofertado cuyo eatc-code es 28 , por lo tanto la consulta a realizar es la siguiente: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order? eatc-sale_code = 28& eatc-user_code =7777    

 El sistema (a 2020-08-14) arroja dos registros, 

 { 
 _id : "5", 
 eatc-sale_order_header_code : "", 
 ... 
 eatc-odd_quantity : "10", 
 ... 
 } 

 Como el registro cuyo _id es "5", no posee an registro de cabecera, el sistema debe: 

 Tomar como dato de " cantidades_agregadas_a_la_orden " a "10" 

 Cuando se realice la creacin de registro de orden , se debe realizar un update de dicho registro para que incorpore las cantidades_a_agregar_a_la_orden 

 Ejemplo caso 2: existen varios registros pero por lo menos uno est en proceso 
 En ambiente de pruebas, el usuario cuyo eatc-user_code es 7777 , est agregando a partir de un tem ofertado cuyo eatc-code es 7 , por lo tanto la consulta a realizar es la siguiente: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order? eatc-sale_code = 7& eatc-user_code =7777   

 El sistema (a 2020-08-14) arroja dos registros, 

 { 
 _id : "2", 
 eatc-sale_order_header_code : "1", 
 ... 
 eatc-odd_quantity : "1", 
 ... 
 } 
 { 
 _id : "3", 
 eatc-sale_order_header_code : "", 
 ... 
 eatc-odd_quantity : "2", 
 ... 
 } 

 Como el registro cuyo _id es "3", no posee an registro de cabecera, el sistema debe: 

 Tomar como dato de " cantidades_agregadas_a_la_orden " a "2" 

 Cuando se realice la creacin de registro de orden , se debe realizar un update de dicho registro para que incorpore las cantidades_a_agregar_a_la_orden 

 Ejemplo caso 3: no existen registros de orden creados 
 En ambiente de pruebas, el usuario cuyo eatc-user_code es 7777 , est agregando a partir de un tem ofertado cuyo eatc-code es 14 , por lo tanto la consulta a realizar es la siguiente: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order? eatc-sale_code = 14& eatc-user_code =7777     

 El sistema (a 2020-08-14) no arroja respuesta, 

 { 
 ts : "200818103254", 
 op : true, 
 cont : 0, 
 err_msg : "No se produjeron resultados", 
 err_num : "", 
 mem : 0.41, 
 time : "00:00:00" 
 } 

 Por lo tanto: 

 No se genera el dato de  " cantidades_agregadas_a_la_orden " 

 Cuando se realice la creacin de registro de orden , se debe realizar un insert 

 Ejemplo caso 4:  existen registros pero de rdenes ya creadas (es decir que no estn en proceso) 
 En ambiente de pruebas, el usuario cuyo eatc-user_code es 7777 , est agregando a partir de un tem ofertado cuyo eatc-code es 21 , por lo tanto la consulta a realizar es la siguiente: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order? eatc-sale_code = 21& eatc-user_code =7777    

 El sistema (a 2020-08-14) arroja un registro, 

 { 
 _id : "4", 
 eatc-sale_order_header_code : "1", 
 ... 
 eatc-odd_quantity : "1", 
 ... 
 } 

 Como el registro cuyo _id es "4",  posee registro de cabecera, el sistema debe: 

 No se genera el dato de  " cantidades_agregadas_a_la_orden " 

 Cuando se realice la creacin de registro de orden , se debe realizar un insert 

 Los datos obtenidos en este proceso se utilizan en las funcionalidades y procesos 

 Detalle de producto ( agregar al carrito de compras ) 

 Creacin del registro en eatc_sale_order 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 App usuario final - Sale 

 CONSULTA DE DATOS DE ORDEN (PEDIDO) ABIERTA