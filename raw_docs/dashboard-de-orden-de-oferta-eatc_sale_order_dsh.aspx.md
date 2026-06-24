# dashboard-de-orden-de-oferta-eatc_sale_order_dsh.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 EatCloud Donantes. Basado en Dashboard de anuncio de donacin (eatc_dona_dsh) : se puede utilizar la misma plantilla, quizs cambiando el color de fondo para diferenciarlo de los anuncios visualmente 

 En esta vista se mostrarn los detalles de la orden de oferta, y botones de accin para completar la entrega de la orden 

 Detalle de orden (pedido) de oferta 
 Consulta de anuncios 
 El sistema toma el parmetro " eatc-code " del encabezado de orden de oferta ( eatc_sale_order_headers ) seleccionado  desde el listado donde se invoca esta vista ( seguimiento de rdenes de oferta: botn ver ms )  y con l se invoca el servicio de desencripcin para traer la informacin desencriptada: 

 {{URL_entorno_beneficiarios}}/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &filterfield_1= eatc-code &filtervalue_1= {{eatc-code}} 

 Ejemplo (ambiente de pruebas): 
 El para la orden cuyo " eatc-code " = 7777   

 https://devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &filterfield_1= eatc-code &filtervalue_1 = 7777   

 Con la respuesta del API se toma la siguiente informacin del usuario que adquiri la promocin: 

 Nombre: eatc-user_name 
 Telfono : eatc-user_phone 
 Nombre de quien recoge: eatc-picker_name 
 Documento de identidad de quien recoge: eatc-picker_doc_id 
 Placa de quien recoge: eatc-picker_license_plate 

 Si en alguno de estos parmetros no hay datos, no se muestra en la interfaz de usuario 

 Mensaje de ALERTA 
 En un lugar muy visible (y en un fondo que lo haga an ms visible, puede ser Rojo) del dashboard de donacin, se debe colocar un mensaje "ALERTA", si y solo si en el campo eatc-warning posee informacin, diferente a 0 o vaca (y no es nulo) y que muestre el contenido del campo eatc-warning del anuncio respectivo. 

 Botn "Registrar factura" 
 Se despliega si en el dato eatc_sale_order_headers. eatc-doc no existe un registro vlido 

 Este botn deber contener un tooltip que informe: 
 Por favor ingrese el nmero de factura o equivalente que genera su sistema POS o de facturacin para la oferta que se entregar. 

 Este apartado solo se habilita para ordenes de oferta cuyo estado ( eatc_sale_order_states ), es paid_out 

 No permitir salir del dashboard hasta no haber registrado una factura o documento equivalente 
 Este botn dar ingreso a la funcionalidad: Registrar Factura , para realizar la entrega ser un dato obligatorio por lo tanto, si el dato correspondiente a este documento ( eatc_sale_order_header.eatc-doc ) no se encuentra populado al salir del dashboard y el usuario desea salir del dashboard, se debe preguntar: 
 Desea hacer entrega de esta orden (pedido) de oferta?  

 Si  No 

 Opcin SI: 
 Dar ingreso a la funcionalidad: Registrar Factura 

 Opcin NO: 
 Permitir salir de la vista de dashboard de orden de oferta. 

 Contenido de la orden 
 Este apartado muestra el detalle de orden de oferta (eatc_sale_order) mediante una consulta al API se debe traer informacin de los productos adquiridos por el usuario y listarlos dentro de un colapsible de la siguiente manera: 

 Consulta de detalles de orden de oferta (eatc_sale_order) 
 El sistema toma el parmetro " eatc-code " del encabezado de orden - pedido de oferta ( eatc_sale_order_headers )   y con l se invoca el API de detalles de orden de oferta ( eatc_sale_order ) , enviando ese valor en el parmetro eatc-sale_order_header_code 
 {{URL_entorno_beneficiarios}}/api/eatcloud/eatc_sale_order? eatc-sale_order_header_code ={{eatc_sale_order_headers . eatc-code }} 

 Ejemplo en ambiente de pruebas: 
 El para la orden de oferta cuyo " eatc-code " = 7777  

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order? eatc-sale_order_header_code =7777   

 Con la respuesta del API se pinta en la interfaz de usuario la siguiente informacin de cada uno de los productos que conforman la orden de oferta: 
 Item: eatc-odd_name 
 Fecha y hora : eatc-date_time 
 Descripcin : eatc-odd_description 
 Cantidad :  eatc-odd_quantity 
 Porcentaje de Descuento : eatc-odd_discount 
 Precio total con descuentos e impuestos :  eatc-odd_total_price 
 Valor IVA: eatc-total_vat 
 Valor otros impuestos: eatc-total_other_taxes 

 Mapa de la orden de oferta: en primera instancia ***no va*** 

 Visualizacin de horarios de venta registrados en el dashboard de la orden de oferta 
 Se deben visualizar los horarios de venta registrados para el el punto de despacho respectivo  en el dashboard del orden de oferta (debe ser una visualizacin muy similar a la que se implement en la funcionalidad configuracin horarios de venta , que sea meramente informativa y que no ocupe tanto espacio de pantalla.  Puede ser conveniente incluir un botn para ir a la funcionalidad de edicin de dichos horarios desde esa visualizacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-orden-de-oferta-eatc_sale_order_dsh%2F3198578717-7.2-detalle-anuncio--eatc_dona_dsh---1-.png&ow=375&oh=1636, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-orden-de-oferta-eatc_sale_order_dsh%2F3198578717-7.2-detalle-anuncio--eatc_dona_dsh---1-.png&ow=375&oh=1636 

 148.000000000000 

 DASHBOARD DE ORDEN DE OFERTA (EATC_SALE_ORDER_DSH)