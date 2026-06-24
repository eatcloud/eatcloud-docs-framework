# dashboard-de-punto-de-venta-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo de la vista: https://drive.google.com/file/d/1GM6YA3iQmfwTG0sV8sJXcntNyvZE5ZrR/view?usp=sharing   

 Dado que el diseo de esta vista es muy similar al de la vista " Listado de productos ", conviene que en su construccin, se pueda aislar fcilmente el componente " Informacin de Punto de Venta ", dado que es la nica diferencia que tendr a nivel de construccin con la otra vista mencionada. 

 Consulta de informacin para ingresar al dashboard de punto de venta 
 Con los datos obtenidos en la consulta respectiva , se pinta la informacin de esta vista, de la siguiente manera: 

 Se obtiene el dato del cdigo del punto de venta: 

eatc_sale. eatc-pod_id del producto seleccionado 

 Con este dato se enva la siguiente consulta: 

 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale? eatc-pod_id ={{eatc_sale. eatc-pod_id }&eatc-odd_state=partially_ordered,sale& _commpress 

 Y con los datos que arroja la consulta se construye la vista (se debe revisar si es necesario paginar la vista si hay muchos registros) 

 X (parte superior izquierda) 
 Devuelve al dashboard principal . 

 Buscador 
 Digitando informacin en el buscador, el sistema filtrar las ofertas que contengan dicho criterio de bsqueda en los campos:  

 eatc-odd_name 
 eatc-odd_description 

 Informacin del punto de venta / despacho: 
 Diseo: https://zeroheight.com/6217d62d5/p/30e9f2-cardsec/t/18db0a   

 Con la informacin de cualquiera de los registros que se obtiene en la consulta respectiva se pinta la informacin de la siguiente manera: 

 Nombre del punto de venta (pod): corresponde a la informacin que se  recibe en el parmetro eatc-pod_name 
 Direccin : corresponde a la informacin que se recibe en el parmetro eatc-pod_address 
 A {{km}} KMl : con el dato que se recibe en el campo km se coloca esta informacin en la card. 
 Botn "Cmo llegar": c on la informacin que se obtiene en los parmetros: eatc-pod_lat y eatc-pod_lon de la consulta respectiva , se envan dichos datos a una app de navegacin y mapas para mostrar cmo llegar (funcionalidad similar a la implementada para la Alimentatn, por lo tanto se puede reciclar cdigo) 
 Horario de atencin : con el dato que se recibe en el parmetro eatc-pod_id y el que se recibe en eatc_cua_origin, se realiza la siguiente consulta para traer la informacin, del da actual, y del da siguiente al actual (en la imagen se coloca un solo horario, pero la idea es que se muestre el da actual (por ejemplo: LU) y el da siguiente (por ejemplo: MA)) 

 {{URL_entorno}}/api/{{ eatc_cua_origin}} /eatc_sale_schedule?eatc-pod_id= eatc-pod_id   

 Informacin de productos 
 La App muestra un listado de productos dispuestos en tarjetas individuales, y que fluirn hacia abajo mediante un scroll vertical. La informacin que despliega la tarjeta se especifica aqu , y por defecto presentar una disposicin horizontal. 

 Tarjeta de producto horizontal (vista por defecto) 
 Diseo: https://zeroheight.com/6217d62d5/p/30e9f2-cardsec/t/18db0a   

 Botones de accin sobre la lista (segunda etapa de implementacin) 

 La aplicacin presenta tres botones para realizar acciones sobre la lista de productos: 

 Botn de visualizacin tipo lista 
 Est seleccionado por defecto y quiere decir que la visualizacin de los productos tendr una disposicin tipo lista, con la card de productos dispuesta en un formato horizontal . 

 Botn de visualizacin tipo grid 
 Quiere decir que la visualizacin de los productos tendr una disposicin tipo grilla de productos, con la card de productos dispuesta en un formato vertical . 

 Ordenar los productos 
 Inicialmente se propondrn dos tipos de ordenamiento: 

 De menor a mayor precio : operar con los datos que trae el campo " eatc-odd_min_sale_unit_price " de la consulta respectiva . 

 De menor a mayor descuento : operar con los datos que trae el campo " eatc-odd_max_discount " de la consulta respectiva . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-punto-de-venta-sale%2F2321010487-EmbeddedImage--95-.jpg&ow=654&oh=1280, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-punto-de-venta-sale%2F2321010487-EmbeddedImage--95-.jpg&ow=654&oh=1280 
 App usuario final - Sale 

 798.000000000000 

 DASHBOARD DE PUNTO DE VENTA