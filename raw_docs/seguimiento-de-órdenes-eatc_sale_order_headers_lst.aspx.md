# seguimiento-de-órdenes-eatc_sale_order_headers_lst.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 EatCloud Donantes&#58; basado en Seguimiento de anuncios (eatc_dona_lst) &#58; se puede utilizar la misma plantilla de diseo 

 Esta funcionalidad, similar al Seguimiento de anuncio servir para que los oferentes entreguen los pedidos a quienes han efectuado su pago y se disponen a hacerlo. por lo tanto su funcionamiento es muy similar y se podr reciclar mucho cdigo, simplemente que la fuente de informacin ser otra ( eatc_sale_order_headers en vez de eatc_dona_headers ) y el tratamiento de los estados de las rdenes ( eatc-state ) es diferente a como se manejan los estados de los anuncios. 

 Buscador (***NUEVO***) 
 El sistema debe permitir realizar bsqueda de la oferta, por el eatc-verification_code disponiendo de un campo de texto para que el usuario digite el cdigo de verificacin (o cdigo de recogida) . Cmo los datos privados del usuario que recoge se guardan encriptados en eatc_sale_order_headers , debern utilizarse los servicios de desencripcin ( y sus respectivos procesos de autenticacin ) para efectuar la bsqueda (la bsqueda debe operar en primera instancia solo sobre los anuncios cuyo estado es &quot; paid_out &quot;, es decir, que han sido ya pagados por el cliente. 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &amp;filterfield_1= eatc-state &amp;filtervalue_1=paid_out&amp;filterfield_2=eatc-verification_code&amp;filtervalue_2=&#123;&#123;criterio_busqueda&#125;&#125;&amp;filterfield_3=eatc-pod_id&amp;filtervalue_3=&#123;&#123;eatc-pod_id&#125;&#125; 

&#160; 
 Ejemplo (ambiente de pruebas)&#58; 
&#160; 
 En el punto de venta &quot;39&quot; El usuario digita el cdigo de recogida 907490, por lo tanto la bsqueda deber ser la siguiente&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname=eatc-user_doc_id,eatc-user_name,eatc-user_phone&amp;filterfield_1=eatc-state&amp;filtervalue_1=paid_out&amp;filterfield_2=eatc-verification_code&amp;filtervalue_2=907490&amp;filterfield_3=eatc-pod_id&amp;filtervalue_3=39 &#160; 

 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados de la oferta ( eatc_sale_order_states ), en particular&#58; 
paid_out 
delivered 
partially_refund 

refund 
&#160; 
 (los otros estados no se utilizarn por el momento) 
 , teniendo al ingresar a la vista el filtro por defecto que presente ofertas&#160; con estado &quot; paid_out &quot; o &quot;pagadas&quot;, es decir, en la lista se deben mostrar las rdenes que aun estn en el almacn y estn pendientes de ser entregadas. 
&#160; 
 En su vista por defecto se debe ordenar el listado mostrando primero los ms recientes y luego los ms antiguos. 
&#160; 
 Consulta de rdenes de pedido (eatc_sale_order_headers) 
 El sistema toma el parmetro &quot; eatc-id &quot; del punto de despacho ( eatc_pods ) respectivo y utiliza el servicio de desencripcin para poder tener datos del usuario que no estn encriptados de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &amp;filterfield_1= eatc-state &amp;filtervalue_1=paid_out&amp;filterfield_2=eatc-pod_id&amp;filtervalue_2= &#123;&#123;eatc-id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO SAN ANTONIO&quot;, cuyo &quot; eatc-id &quot; = 39 consulta en ambiente de pruebas de la siguiente manera 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &amp;filterfield_1= eatc-state &amp;filtervalue_1=paid_out&amp;filterfield_2=eatc-pod_id&amp;filtervalue_2= 39 para mostrar la informacin por defecto (filtro por defecto) 
&#160; 
 y esta consulta, para mostrar toda la informacin&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname= eatc-user_doc_id,eatc-user_name,eatc-user_phone &amp;filterfield_1=eatc-pod_id&amp;filtervalue_1= 39 &#160; 

 Filtros 
 Los filtros deben realizar llamados al API, para traer ofertas con diferentes estados a los del filtro por defecto (paid_out) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname=eatc-user_doc_id,eatc-user_name,eatc-user_phone&amp;filterfield_1= eatc-state &amp;filtervalue_1= &#123;&#123;valor_filtro&#125;&#125; &amp;filterfield_2=eatc-pod_id&amp;filtervalue_2=&#123;&#123;eatc-id&#125;&#125; 

&#160; 
 Ejemplo (ambiente de pruebas)&#58; 
 El usuario &quot;EXITO SAN ANTONIO&quot;, cuyo &quot; eatc-id &quot;&quot;= 39 ( eatc-pod_id ) , desea consultar los anuncios entregados (eatc-state=delivered)&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname=eatc-user_doc_id,eatc-user_name,eatc-user_phone&amp;filterfield_1= eatc-state &amp;filtervalue_1= delivered &amp;filterfield_2=eatc-pod_id&amp;filtervalue_2=39 &#160; 

 Card de la orden de oferta (eatc_sale_order_header) 

 El informe debe ser construido en tiempo real para mostrar la fotografa de las rdenes o pedidos de ofertas en el momento que se&#160; carga el informe.&#160; Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
 Cada rden de oferta ( eatc_sale_order_headers ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 
&#160; 
 Fecha y hora de la orden o pedido&#58; 
 &#160;eatc_sale_order_headers.eatc-datetime 

 Datos del usuario que compr 
 Nombre&#58; eatc_sale_order_headers.eatc-user_name 
 Telfono&#58; eatc_sale_order_headers.eatc-user_phone 

 Total de kilos que contiene el pedido 
 eatc_sale_order_headers.eatc-total_weight_kg 

 Estado del pedido ( eatc_sale_order_states ) 
 eatc_sale_order_headers.eatc-state 

 Botn &quot;ver ms&quot; (anteriormente botn &quot;+&quot;) 
 Este botn dar la entrada a la funcionalidad &quot; dashboard de orden o pedido de oferta &quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-%C3%B3rdenes-eatc_sale_order_headers_lst%2F816918026-6-seguimiento-anuncios--eatc_dona_lst---2-.png&ow=375&oh=2866, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-%C3%B3rdenes-eatc_sale_order_headers_lst%2F816918026-6-seguimiento-anuncios--eatc_dona_lst---2-.png&ow=375&oh=2866 

 146.000000000000 

 SEGUIMIENTO Y ENTREGA DE RDENES (EATC_SALE_ORDER_HEADERS_LST)