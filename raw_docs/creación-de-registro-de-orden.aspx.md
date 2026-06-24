# creación-de-registro-de-orden.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema debe realizar el proceso de consulta de datos de orden abierta para obtener el dato de  " cantidades_agregadas_a_la_orden ", si este dato es igual cantidades_a_agregar_a_la_orden que pasa el proceso de Agregar al carrito , entonces no se hace ningn registro. 

 Si ambos datos son diferentes entonces se debe proceder, a realizar un update como se establece ms abajo .  Si no hay dato de cantidades_agregadas_a_la_orden se procede a realizar un insert como se detalla a continuacin. 

 Creacin del registro en eatc_sale_order 
 Utilizando la informacin incorporada en eatc_sale y las cantidades compradas (ordenadas: cantidad_comprada ) en la funcionalidad respectiva , se realiza el registro en la estructura eatc_sale_order , de la siguiente manera: 

 {{parmetros de creacin de eatc_sale_order }} 

 eatc-sale_code : cdigo del tem sale del cual se toma la informacin ( eatc_sale.eatc-code ) 
 eatc-user_code : cdigo del usuario que est realizando la orden o pedido ( eatc_sale_users.eatc-code ) 
 eatc-code : identificador nico del presente registro (se debe generar un cdigo nico que evite colisiones, a definicin del desarrollador) 
 eatc-sale_order_header_code : se deja vaco. 
 eatc-doc : se deja vaco. 
 eatc-date_time :  estampe de fecha y hora en formato AAAA-MM-DD HH:MM:SS 
 eatc-date_time_2 : estampe de fecha en formato AAAA-MM-DD 
 eatc-odd_id : Identificador nico del producto o artculo ordenado ( eatc_sale.eatc-odd_id ) 
 eatc-odd_name : nombre el artculo o producto ordenado ( eatc_sale.eatc-odd_name ) 
 eatc-odd_description : descripcin del artculo o producto ordenado ( eatc_sale.eatc-odd_description ) 
 eatc-odd_original_quantity : dato cantidades_a_agregar_a_la_orden que se obtiene del proceso de agregar al carrito de compras 
 eatc-odd_quantity : dato cantidades_a_agregar_a_la_orden que se obtiene del proceso de agregar al carrito de compras 
 eatc_cua_origin : Cuenta desde la cual se gener la oferta ( eatc_sale.eatc_cua_origin ) 
 eatc-pod_id : identificador nico del punto de venta ( eatc_sale.eatc-pod_code ) 
 eatc-pod_name : nombre del punto de venta ( eatc_sale.eatc-pod_name ) 
 eatc-pod_address : direccin del punto de venta ( eatc_sale.eatc-pod_adress ) 
 eatc-pod_lat : latitud del punto de venta en coordenadas decimales ( eatc_sale.eatc-pod_lat ) 
 eatc-pod_lon : longitud del punto de venta en coordenadas decimales ( eatc_sale.eatc-pod_lon ) 
 eatc-pod_city : ciudad del punto de venta ( eatc_sale.eatc-pod_city ) 
 eatc-pod_province : departamento, estado, provincia del punto de venta ( eatc_sale.eatc-pod_province ) 
 eatc-pod_country : pas del punto de donacin ( eatc_sale.eatc-pod_country ) 
 eatc_donor_code : identificador nico del Vendedor (Donante) en el sistema ( eatc_sale.eatc_donor_code ) 
 eatc_donor : nombre del donante ante el sistema. Corresponde tambin al nombre de la cuenta del donante ( eatc_sale.eatc_donor ) 
 eatc-odd_unit_weight_kg : peso unitario del artculo en kilogramos ( eatc_sale.eatc-odd_unit_weight_kg ) 
 eatc-odd_original_total_weight_kg : peso original total del artculo a ser vendido (peso unitario por cantidad original) ( eatc-odd_original_quantity*eatc-odd_unit_weight_kg ) 
 eatc-odd_total_weight_kg : peso total del artculo a ser vendido (peso unitario por cantidad) ( eatc-odd_quantity*eatc-odd_unit_weight_kg ) 
 eatc-odd_unit_full_price : Precio de venta al pblico del artculo a ser vendido (sin descuento de ltimo minuto) ( eatc_sale.eatc-odd_unit_price ). 
 eatc-odd_sale_unit_price : Precio de venta al pblico con descuento (contempla el descuento mximo para el salvamento del producto) ( eatc_sale.eatc-odd_min_sale_unit_price ) 
 eatc-odd_discount : descuento venta de ltimo minuto del producto ( eatc_sale.eatc-odd_max_discount ) 
 eatc-odd_original_total_price : precio original total del o de los productos o artculos vendidos ( eatc-odd_original_quantity * eatc-odd_sale_unit_price ) 
 eatc-odd_total_price : Precio total definitivo del o de los productos o artculos donados ( eatc-odd_quantity * eatc-odd_sale_unit_price ) 
 eatc_vat_percentage : porcentaje del impuesto al valor agregado aplicable al producto ( eatc_sale.eatc_VAT_percentage ) 
 eatc-original_vat_base : base gravable sobre la cual se calcula el impuesto a las ventas original ( (eatc-odd_unit_full_price * eatc-odd_original_quantity)/(1+(eatc_vat_percentage/100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-original_vat : valor original total del impuesto a las ventas ( eatc-original_vat_base*(eatc_vat_percentage/100) )=> Se solicita revisin del clculo por parte del desarrollador 
 eatc-vat_base : base gravable sobre la cual se calcula el impuesto a las ventas definitivo ( (eatc-odd_unit_full_price * eatc-odd_quantity)/(1+(eatc_VAT_percentage/100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-total_vat : valor definitivo total del impuesto a las ventas, despus del proceso de verificacin ( eatc-vat_base*(eatc_VAT_percentage/100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-other_taxes_percentage : porcentaje de otros impuestos aplicables (como por ejemplo impuesto al consumo) ( eatc_sale.eatc-other_taxes_percentage ) 
 eatc-original_other_taxes_base : base gravable sobre la cual se calculan los otros impuestos originales ( (eatc-odd_unit_full_price * eatc-odd_original_quantity)/(1+(eatc-other_taxes_percentage/100)) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-original_total_other_taxes : valor original total de otros impuestos ( eatc-original_other_taxes_base * eatc-other_taxes_percentage ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-other_taxes_base : base gravable sobre la cual se calculan los otros impuestos definitivos ( (eatc-odd_unit_full_price * eatc-odd_quantity)/(1+(eatc-other_taxes_percentage/100)) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-total_other_taxes : "Valor definitivo total otros impuestos ( eatc-other_taxes_base * eatc-other_taxes_percentage ) despus del proceso de verificacin => Se solicita revisin del clculo por parte del desarrollador 
 eatc-odd_state : estado del artculo.  Se coloca " ordered " 
 eatc-odd_rejection_cause : se deja vaco. 
 eatc-odd_rejection_cause_code : se deja vaco. 
 eatc-warning : ( eatc_sale.eatc-warning) 
 eatc-contains_alergens_ : informacin si el detalle de la oferta contiene alrgenos ( eatc_sale.eatc-contains_alergens ) 
 eatc-closer_expiration_date : fecha ms prxima de expiracin o vencimiento de los productos del detalle de la oferta ( eatc_sale.eatc-closer_expiration_date ) 
 eatc-refund_quantity : se deja vaco. 
 eatc-refund_amount : "se deja vaco. 

 *****NUEVOS PARMETROS A ADICIONAR EN eatc_sale_order**** 
 eatc-offer_lifetime : ( eatc_sale. eatc-offer_lifetime ) 
 eatc-offer_lifetime_until : ( eatc_sale. eatc-offer_lifetime_until ) 
 [***] Se guarda la informacin en el object store eatc_sale_order de la cuenta eatcloud: 

 Mtodo POST  

 {URL_entorno_beneficiarios}}/crd/eatcloud/?_tabla=eatc_sale_order&_operacion=insert& {{Parmetros creacin en eatc_sale_order }} 

 Update del registro en eatc_sale_order 
 Teniendo claro el _id del registro abierto en eatc_sale_order consultado en el proceso respectivo , y la informacin incorporada en eatc_sale y cantidades_a_agregar_a_la_orden en la funcionalidad respectiva , se realiza la actualizacin del registro en la estructura eatc_sale_order , de la siguiente manera: 

 {{parmetros de actualizacin de eatc_sale_order }} 

 eatc-odd_original_quantity : dato cantidades_a_agregar_a_la_orden que se obtiene del proceso de agregar al carrito de compras 
 eatc-odd_quantity : dato cantidades_a_agregar_a_la_orden que se obtiene del proceso de agregar al carrito de compras 
 eatc-odd_original_total_weight_kg : peso original total del artculo a ser vendido (peso unitario por cantidad original) ( eatc-odd_original_quantity* ( eatc_sale.eatc-odd_unit_weight_kg )) 
 eatc-odd_total_weight_kg : peso total del artculo a ser vendido (peso unitario por cantidad) ( eatc-odd_quantity* ( eatc_sale.eatc-odd_unit_weight_kg )) 
 eatc-odd_original_total_price : precio original total del o de los productos o artculos vendidos ( eatc-odd_original_quantity * ( eatc_sale.eatc-odd_min_sale_unit_price )) 
 eatc-odd_total_price : Precio total definitivo del o de los productos o artculos donados ( eatc-odd_quantity * ( eatc_sale.eatc-odd_min_sale_unit_price )) 
 eatc_vat_percentage : porcentaje del impuesto al valor agregado aplicable al producto ( eatc_sale.eatc_VAT_percentage ) 
 eatc-original_vat_base : base gravable sobre la cual se calcula el impuesto a las ventas original ( (eatc-odd_unit_full_price * eatc-odd_original_quantity)/(1+(eatc_vat_percentage/100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-original_vat : valor original total del impuesto a las ventas ( eatc-original_vat_base*( ( eatc_sale.eatc_VAT_percentage ) /100) )=> Se solicita revisin del clculo por parte del desarrollador 
 eatc-vat_base : base gravable sobre la cual se calcula el impuesto a las ventas definitivo ( (eatc-odd_unit_full_price * eatc-odd_quantity)/(1+(eatc_VAT_percentage/100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-total_vat : valor definitivo total del impuesto a las ventas, despus del proceso de verificacin ( eatc-vat_base*( ( eatc_sale.eatc_VAT_percentage ) /100) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-other_taxes_percentage : porcentaje de otros impuestos aplicables (como por ejemplo impuesto al consumo) ( eatc_sale.eatc-other_taxes_percentage ) 
 eatc-original_other_taxes_base : base gravable sobre la cual se calculan los otros impuestos originales ( (eatc-odd_unit_full_price * eatc-odd_original_quantity)/(1+(eatc-other_taxes_percentage/100)) ) => Se solicita revisin del clculo por parte del desarrollador eatc-original_total_other_taxes : valor original total de otros impuestos ( eatc-original_other_taxes_base * ( eatc_sale.eatc-other_taxes_percentage )) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-other_taxes_base : base gravable sobre la cual se calculan los otros impuestos definitivos ( (eatc-odd_unit_full_price * eatc-odd_quantity)/(1+(eatc-other_taxes_percentage/100)) ) => Se solicita revisin del clculo por parte del desarrollador 
 eatc-total_other_taxes : "Valor definitivo total otros impuestos ( eatc-other_taxes_base * ( eatc_sale.eatc-other_taxes_percentage )) despus del proceso de verificacin => Se solicita revisin del clculo por parte del desarrollador 

 [***] Se guarda la informacin en el object store eatc_sale_order de la cuenta eatcloud: 

 Mtodo POST  

 {URL_entorno_beneficiarios}}/crd/eatcloud/?_tabla=eatc_sale_order&_operacion=update& {{Parmetros actualizacin en eatc_sale_order }}&WHERE_id={{id_registro_sale_order}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 App usuario final - Sale 

 CREACIN DE REGISTRO DE ORDEN (PEDIDO)