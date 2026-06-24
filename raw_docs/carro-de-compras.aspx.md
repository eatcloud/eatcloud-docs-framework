# carro-de-compras.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo: 

 Esta funcionalidad muestra la informacin que se encuentra registrada en eatc_sale_order (y que fue registrada por el proceso respectivo ). Por principio general la App solo manejar una orden abierta.  Esta orden abierta solo podr  pertenecer a un punto de venta ( eatc_pod ).  Por el momento no se contempla manejar ms de una orden abierta, de diferentes puntos de despacho. 

 La consulta para traer los datos  para esta vista, es similar a la que se realiza en el componente de Consulta de datos de Orden Abierta . Si no se encuentra una orden abierta, se presentar el carro de compras vaco, que despliega un botn de comienza a comprar , que debe direccionar a la vista anterior desde la cual se ingres al carro de compras vaco ( Dasboard sale , Dashboard de punto de venta o Detalle de producto ).  Si existen registro de orden abierta, se muestra el carro de compras con dichos registros. 

 CARRO DE COMPRAS 

 X (parte superior izquierda) 
 Devuelve a la vista anterior desde la cual se ingres al carro de compras vaco ( Dasboard sale , Dashboard de punto de venta o Detalle de producto ) 

 Informacin del punto de venta / despacho (aun no est en el wireframe): 

 Con la informacin de cualquiera de los registros que se obtiene en la consulta respectiva se pinta la informacin de la siguiente manera: 

 Nombre del punto de venta (pod): corresponde a la informacin que se  recibe en el parmetro eatc_sale_order.eatc-pod_name . (Dado que esta informacin se extrae de varios detalles, el sistema debe verificar que al hacerle un distinct a dichos detalles, la misma sea nica) 
 Direccin : corresponde a la informacin que se recibe en el parmetro eatc_sale_order.eatc-pod_address . (Dado que esta informacin se extrae de varios detalles, el sistema debe verificar que al hacerle un distinct a dichos detalles, la misma sea nica) 
 Botn "Cmo llegar": c on la informacin que se obtiene en los parmetros: eatc_sale_order. eatc-pod_lat y eatc_sale_order. eatc-pod_lon de la consulta respectiva , se envan dichos datos a una app de navegacin y mapas para mostrar cmo llegar (funcionalidad similar a la implementada para la Alimentatn, por lo tanto se puede reciclar cdigo) . (Dado que esta informacin se extrae de varios detalles, el sistema debe verificar que al hacerle un distinct a dichos detalles, la misma sea nica) 

 Horario de atencin : con el dato que se recibe en el parmetro eatc_sale_order.eatc-pod_id y el que se recibe en eatc_sale_order.eatc_cua_origin, se realiza la siguiente consulta para traer la informacin, del da actual, y del da siguiente al actual (en la imagen se coloca un solo horario, pero la idea es que se muestre el da actual (por ejemplo: LU) y el da siguiente (por ejemplo: MA)) 

 {{URL_entorno}}/api/{{ eatc_cua_origin}} /eatc_sale_schedule?eatc-pod_id= eatc-pod_id   

 Card de producto ordenado 
 En esta tarjeta se muestra informacin bsica del producto ordenado de la siguiente manera 

 Tumbnail : corresponde a la informacin que se recibe en el parmetro eatc_sale_order. eatc-odd_image 
 -X% (porcentaje de descuento: no est en el wireframe) : crculo en la parte superior derecha del tumbnail, que muestra  la informacin que se recibe en el parmetro eatc_sale_order. eatc-odd_max_discount 
 Nombre del producto: corresponde a la informacin que se  recibe en el parmetro eatc_sale_order. eatc-odd_name 
 Precio total: corresponde a la informacin que se  recibe en el parmetro eatc_sale_order. eatc-odd_total_price .  

 Cantidad ordenada: corresponde a la informacin que se  recibe en el parmetro eatc_sale_order. eatc-odd_quantity 

 Botn menos 
 Este botn debe realizar dos acciones principales al restar una unidad a la orden: 

 Actualizar inventario en eatc_sale (volviendo a poner disponible la unidad restada a la orden) :  tal cual como funciona el proceso respectivo . 
 Actualizar los datos de la orden e atc_sale_order : restando la unidad ordenada y haciendo el update respectivo 

 Botn ms 
 Este botn debe realizar dos acciones principales al restar una unidad a la orden: 

 Actualizar inventario en eatc_sale (restando la nueva cantidad al inventario) :  tal cual como funciona el proceso respectivo . 
 Actualizar los datos de la orden e atc_sale_order : restando la unidad ordenada y haciendo el update respectivo 

 Tipo de recogida: 
 En esta card se muestra el dato " eatc_sale_order_header. eatc-delivery_method " que se obtiene del  proceso de check-out   

 Mtodo de pago: 
 En esta card se muestra el dato del medio de pago seleccionado que se obtiene del  proceso de check-out   

 Total: 

 El sistema debe mostrar el total de la transaccin, que se constituye en la sumatoria de los valores eatc_sale_order. eatc-odd_total_price . de los distintos de detalles relacionados en la vista (Estos items solo pueden pertenecer a un solo una ubiacin geogrfica eatc_pod es decir eatc-pod_lat y eatc-pod_lon deben ser igual), . Este valor se guarda en el parmetro: eatc_sale_order_header. eatc-odd_total_price 

 BOTN DE ACCIN PARA PAGO 
 Este botn debe tener dos estados diferentes, de acuerdo a si se ha realizado o no el proceso de Check-out, de la siguiente manera: 

 No se ha realizado el proceso de check-out: "Ingresar datos pago" 
 Cuando se oprime este botn el sistema deber realizar lo siguiente: 

 Validar si el usuario tiene sus datos bsicos registrados 
 Si el usuario es un usuario annimo (es decir, que solo tiene el token generado para su identificacin ), entonces se deber proceder con el proceso de Registro de Usuario para poder proseguir con el pago. 

 Generacin de cdigo nico de transaccin (que se utilizar posteriormente como eatc_sale_order_header.eatc-code) 
 El sistema debe generar un cdigo nico para la transaccin y guardarlo en una variable.  Si el proceso de check-out es exitoso, este cdigo se utilizar para generar el eatc_sale_order_header.eatc-code que se incorporar en cada detalle y en encabezado respectivo. 

 Direccionamiento al proceso de check-out 
 La App se redirecciona al proceso de check-out 

 Ya se realiz el proceso de check-out: "Pagar" 
 Al oprimir este botn, se toman los datos necesarios para realizar el pago y se envan al proceso " Pagar: integracin con la pasarela de pago, confirmacin y creacin del encabezado de orden de pedido " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcarro-de-compras%2F1446437520-EmbeddedImage---2024-07-29T235723.342.jpg&ow=616&oh=606, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcarro-de-compras%2F1446437520-EmbeddedImage---2024-07-29T235723.342.jpg&ow=616&oh=606 
 App usuario final - Sale 

 822.000000000000 

 CARRO DE COMPRAS