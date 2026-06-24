# agregar-al-carrito-de-compras.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 DESCRIPCIN GENERAL 
 El principal objetivo de esta funcionalidad es definir cantidades_a_agregar_a_la_orden ( eatc_sale_order ) para un producto ofertado especfico ( eatc_sale ), sin que las mismas sobrepasen el inventario disponible de la oferta, que es el dato que se guarda en el parmetro eatc_sale. eatc-odd_quantity .  Con el proceso se separar el inventario, por lo tanto se deber actualizar el dato eatc_sale. eatc-odd_quantity a medida que se van adicionando o restando unidades de producto. Como la idea es tener un comportamiento en tiempo real, el control de esta funcionalidad debe censar en tiempo muy corto estas cantidades disponibles para poder realizar sus acciones y debe funcionar en primera medida como un controlador en tiempo real de inventario. 

 CONSULTA PREVIA DE CANTIDADES AGREGADAS A UNA ORDEN ABIERTA 
 El sistema deber consultar al ingresar a la vista " detalle de producto " en donde se encuentra esta funcionalidad, si existe una orden abierta para esta oferta en particular y su respectivo usuario .  Si no se pasa a Agregar al carrito. Si existe el dato cantidades_agregadas_a_la_orden se pasa al botn que muestra las cantidades a agregar y la cantidad mostrada deber corresponder inicialmente al dato  " cantidades_agregadas_a_la_orden " obtenidas en la consulta de datos de orden abierta 

 BOTN "AGREGAR AL CARRITO" 
 Al presionar el botn " Agregar al carrito " el sistema debe hacer la consulta al Item respectivo  con el respectivo llamado al API para obtener las unidades disponibles del mismo ( eatc-odd_quantity ): 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale? eatc-code={{eatc-code}} 

 Ejemplo 

 en ambiente de pruebas se seleccion un registro cuyo " eatc-code" es "65", por lo tanto la consulta respectiva ser: 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale? eatc-code=64 

 El sistema deber revisar el dato que se est registrado en " eatc-odd_quantity " y actuar de la siguiente manera: 

 BOTN INACTIVO CON LA LEYENDA "AGOTADO" 
 eatc_sale.eatc-odd_quantity es igual a cero: 
 Entonces en el botn deber aparecer la leyenda " Agotado " y permanecer deshabilitado: 

 BOTN CON CANTIDADES A AGREGAR A LA ORDEN Y BOTONES PARA DISMINUIR O AGREGAR CANTIDADES. 

 Este botn, si existe un dato de  " cantidades_agregadas_a_la_orden " obtenidas en la consulta de datos de orden abierta , deber mostrar dichas unidades y tener un comportamiento similar en cuanto al funcionamiento de los botones de agregar y disminuir cantidades, a como se explica a continuacin, para el caso en donde no existen cantidades_agregadas_a_la_orden 

 eatc_sale.eatc-odd_quantity es igual a uno o a una cifra superior 

 El botn aparecer activo, mostrando la unidad  ( 1 ) agregada ( cantidades_a_agregar_a_la_orden ) y dos botones: un menos ( - ) y un ms ( + ) ( el botn + solo aparecer si eatc-odd_quantity (antes del update ) es diferente a "1") a lado y lado de la cifra.  Igualmente y de manera instantnea deber realizar un update a eatc_sale , para restar esa unidad de la cifra eatc-odd_quantity y tambin para actualizar el estado ( eatc-odd_state ) segn sea el caso de la siguiente manera: 

 cantidades_a_agregar_a_la_orden = 1 (que se muestran al centro del botn) 
 Si  eatc-odd_quantity (antes del update ) es mayor que " 1 " se debe registrar el estado: " partially_ordered " 
 Si  eatc-odd_quantity (antes del update ) es igual a "1" se debe registrar el estado: " ordered ". 

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla=eatc_sale&_operacion=update& eatc-odd_quantity={{eatc-odd_quantity_anterior - 1)&eatc-odd_state={{new_state}}&WHEREeatc-code={{eatc-code}} 

 Ejemplo 

 En ambiente de pruebas est en el detalle de producto para la oferta " eatc-code" es "65", por lo tanto la consulta respectiva ser cuando se oprima "Aadir a tu carrito": 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale? eatc-code=64 

 Como el dato eatc-odd_quantity tiene valor " 8 " (2020-08-14) el botn mostrar la unidad adicionada antecedida por el botn - y seguida del botn +. 

 Dado que eatc-odd_quantity es mayor que "1", eatc-odd_state ser "partially_ordered" 
 eatc-odd_quantity_anterior - 1 = 8-1 = 7 

 Por lo tanto la llamada al API deber ser: 

 https://devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&_operacion=update& eatc-odd_quantity= 7 &eatc-odd_state= partially_ordered &WHEREeatc-code=65   

 NOTA IMPORTANTE: 
 Se debe pensar un mecanismo anti-colisiones de actualizacin, de tal manera que si dos dispositivos al mismo tiempo estn actualizando la informacin, hacer que el primero que lo haga de alguna manera bloquee al segundo que lo haga (en cuestin de milisegundos) y as evitar que un registro de descuento de inventario se pierda por la simultaneidad. 

 Botn "+": 
 Funciona de manera similar al botn " Agregar al carrito " (con las mismas validaciones previas) con la diferencia que aadir una unidad ms al dato cantidades_a_agregar_a_la_orden . Este botn no debe hacer ninguna accin y no se debe mostrar si en dichas validaciones previas se encuentra que eatc-odd_quantity es igual a cero (0). 

 Botn "-": 
 A diferencia del botn anterior este resta unidades "separadas" para la venta, por lo tanto deber reversar el registro de eatc-odd_quantity en eatc_sale y tambin cambiar el estado del respectivo item ( eatc-odd_state ) de la siguiente manera: 

 cantidades_a_agregar_a_la_orden = cantidad_a_agregar_a_la_orden_anterior - 1 
 Si  eatc-odd_original_quantity   menos eatc-odd_quantity es mayor que " 1 "se debe registrar el estado: " partially_ordered " 
 Si  eatc-odd_original_quantity   menos eatc-odd_quantity   es igual a " 1 " se debe registrar el estado: " sale " 

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla=eatc_sale&_operacion=update& eatc-odd_quantity={{eatc-odd_quantity_anterior + 1)&eatc-odd_state={{new_state}}&WHEREeatc-code={{eatc-code}} 

 Ejemplo 

 Siguiendo el ejemplo anterior ( https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale? eatc-code=64 

 Como el dato eatc-odd_quantity tiene valor "7" despus de haberle restado una unidad por la anterior compra (en el anterior ejemplo): 

 cantidades_a_agregar_a_la_orden = cantidad_a_agregar_a_la_orden_anterior - 1 = 1-1 = 0 

 Dado que eatc-odd_original_quantity  menos eatc-odd_quantity es 1 (8-7), eatc-odd_state ser "sale" y  
 eatc-odd_quantity_anterior + 1 = 7+1 = 8 

 Por lo tanto la llamada al API deber ser: 

 https://devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&_operacion=update& eatc-odd_quantity= 8 &eatc-odd_state= sale &WHEREeatc-code=65  

 NOTA IMPORTANTE: 
 Se debe pensar un mecanismo anti-colisiones de actualizacin, de tal manera que si dos dispositivos al mismo tiempo estn actualizando la informacin, hacer que el primero que lo haga de alguna manera bloquee al segundo que lo haga (en cuestin de milisegundos) y as evitar que un registro de descuento de inventario se pierda por la simultaneidad. 

 Como el valor que se mostrara en el nmero entre los dos botones (-) y (+) en este caso sera "0", el botn debe volver a su estado original en donde tiene el letrero "Agregar al carrito" 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagregar-al-carrito-de-compras%2F968178900-EmbeddedImage---2024-07-29T233623.065.jpg&ow=754&oh=358, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagregar-al-carrito-de-compras%2F968178900-EmbeddedImage---2024-07-29T233623.065.jpg&ow=754&oh=358 
 App usuario final - Sale 

 817.000000000000 

 AGREGAR AL CARRITO DE COMPRAS