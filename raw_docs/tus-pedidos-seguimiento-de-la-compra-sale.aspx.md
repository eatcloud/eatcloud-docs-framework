# tus-pedidos-seguimiento-de-la-compra-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo&#58; https&#58;//zeroheight.com/6217d62d5/p/887515-vista-listado-de-pedidos 

 Esta vista mostrar un listado de los pedidos ( eatc_sale_order_headers ) en curso (en primera prioridad&#58; pedidos cuyo estado eatc_state , es paid_out ), empezando por el ms antiguo (es decir, aquel cuya eatc-datetime sea ms antigua y por lo tanto, el que tiene mayor prioridad de recogida), y tambin los pedidos ya entregados (cuyo estado eatc_state , es delivered,partially_refund,refund ), mostrando en este segundo caso primero los ms actuales. 

 Consulta para traer la informacin de los pedidos 
 Con los datos del usuario de la App&#160; ( eatc_user_code ) se realiza la siguiente consulta para traer los datos de sus pedidos&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers?eatc-user_code=&#123;&#123;eatc_sale_users. eatc-code&#125;&#125; 

 LISTADO DE PEDIDOS 
 En este listado, compuesto por dos secciones principales&#58; 
&#160; 
 EN CURSO&#58; mostrar pedidos cuyo eatc_state , es paid_out . Estos pedidos se ordenarn mostrando primero aquellos cuya fecha ( eatc-datetime ) sea ms antigua (orden descendente de antigedad). 

 ENTREGADOS&#58; mostrar pedidos cuyo eatc_state , es delivered , partially_refund o refund . ,Estos pedidos se ordenarn mostrando primero aquellos cuya fecha ( eatc-datetime ) sea es ms actual (orden ascendente de antigedad). 
&#160; 
 Como se ver ms adelante cada tarjeta tendr un par de botones, pero el resto de su rea ser sensible y llevar a la vista &quot; Detalle de Orden &quot; 

 EN CURSO&#58; 
 En&#160; esta seccin se mostrar una card que contendr la siguiente informacin&#58; 
&#160; 
 Informacin&#58; 
 Cdigo de entrega&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-verification_code ( en la App debe mostrarse claramente es el cdigo de entrega) 
 Nombre punto de venta&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-pod_name 
 Direccin (del punto de despacho)&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-pod_address 
 A x KM&#58; para obtener este dato se debe tomar el cdigo del encabezado de pedido ( eatc_sale_order_headers. eatc-code ) y con esta informacin se realiza una consulta, para mostrar el parmetro km que se obtiene de la consulta, de la siguiente manera&#58; 

 &#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_order_headers &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;actual_lat&#125;&#125; , &#123;&#123;actual_lon&#125;&#125; &amp; showfield = eatc-code &amp; km = &#123;&#123;actual_sale_radius_km&#125;&#125; &amp;filterfield_1= eatc-code &amp;filtervalue_1= &#123;&#123; (eatc_sale_order_headers. eatc-code&#125;&#125; 
&#160; 
 Fecha y hora del pedido&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-datetime 

 Horario de atencin &#58; con el dato que se recibe en el parmetro eatc_sale_order_headers. eatc-pod_id y el que se recibe en eatc_sale_order_headers. eatc_cua_origin , se realiza la siguiente consulta para traer la informacin, del da actual, y del da siguiente al actual (en la imagen se coloca un solo horario, pero la idea es que se muestre el da actual (por ejemplo&#58; LU) y el da siguiente (por ejemplo&#58; MA 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123; eatc_cua_origin&#125;&#125; /eatc_sale_schedule?eatc-pod_id= eatc-pod_id &#160; 
&#160; 
 Valor del pedido&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-total_price 
&#160; 
 Botones&#58; 
 Cmo llegar&#58; con los datos eatc-pod_lat,eatc-pod_lon del respectivo encabezado ( eatc_sale_order_headers ), se genera un vnculo que se pueda abrir en una app de mapas y navegacin (como por ejemplo Waze). 
 Ayuda&#58; conectar a la seccin &quot; Centro de ayuda para pedidos &quot;. 
&#160; 
 Botn de Aviso de Alerta&#58; 
 En este botn mostrar un aviso segn el mtodo de recogida ( eatc_sale_order_headers. eatc-delivery_method ) &#58; 
&#160; 
 Mtodo&#58; user_pickup 
 Si el mtodo registrado es&#58; user_pickup se despliega el siguiente mensaje &quot;Llegu a recoger&#58; consulta el cdigo de recogida&quot; + &quot; Alerta de recogida &quot; que se describe ms abajo. 
 Al oprimir el botn el sistema debe realizar dos cosas&#58; 
 Mostrar el siguiente mensaje 
&#160; 
 Tu cdigo de recogida es&#58; &#123;&#123;eatc_sale_order_headers. eatc-verification_code &#125;&#125;. Presntalo al llegar al punto de despacho, para&#160; 
 Realizar el registro de la fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS en el campo eatc_sale_order_headers. eatc-picking_checkin_datetime 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_headers&amp;_operacin=update&amp; eatc-picking_checkin_datetime =&#123;&#123;timestamp&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_sale_order_header.eatc-code&#125;&#125; 
&#160; 
 Mtodo&#58; third_person_pickup 
 Si el mtodo registrado es&#58; third_person_pickup se despliega el siguiente mensaje &quot;Entrega el cdigo de recogida a quien recoge&quot; + &quot; Alerta de recogida &quot; que se describe ms abajo. 
 Al oprimir el botn el sistema debe mostrar el siguiente mensaje&#58; 
&#160; 
 Tu cdigo de recogida es&#58; &#123;&#123;eatc_sale_order_headers. eatc-verification_code &#125;&#125;. Envalo a la persona que recoger tu pedido indicndole que lo presente al recogerlo. 
&#160; 
 Ideal poder poner un botn de compartir del sistema operativo para que el usuario pueda enviar por cualquier mtodo disponible en su telfono, la siguiente informacin&#58; 
&#160; 
 El de recogida del pedido realizado por &#123;&#123;eatc_sale_order_headers. eatc-user_name &#125;&#125; es &#123;&#123;eatc_sale_order_headers. eatc-verification_code &#125;&#125;. Al recoger el pedido en &#123;&#123;eatc_sale_order_headers. eatc-pod_address &#125;&#125; *** presntalo para que te lo enteguen. 
&#160; 
 *** 
 Sera ideal que este la informacin &#123;&#123;eatc_sale_order_headers. eatc-pod_address &#125;&#125; contenga un geovnculo que pueda ser abierto en una App de navegacin y mapas y que contenga las coordenadas&#58; &#123;&#123;eatc_sale_order_headers. eatc-pod_lat &#125;&#125; y &#123;&#123;eatc_sale_order_headers. eatc-pod_lon &#125;&#125; 

&#160; 
 Alerta de recogida [Pendiente de implementacin de tareas para implementar el parmetro eatc-offer_lifetime_until ] 
 Para el despliegue de esta alerta el sistema debe evaluar el dato consignado en eatc_sale_order_headers. eatc-offer_lifetime_until y compararlo con la fecha y hora actual para desplegar informacin de la siguiente manera 
&#160; 
 Si la fecha y hora actual es anterior a la fecha y hora consiganda en eatc_sale_order_headers. eatc-offer_lifetime_until el sistema debe calcular las horas y minutos&#160; que faltan hasta la hora consignada en eatc_sale_order_headers. eatc-offer_lifetime_until 
 Si la fecha y hora actual es posterior a la fecha y hora consiganda en eatc_sale_order_headers. eatc-offer_lifetime_until &#160; se debe desplegar un mensaje vistoso que diga &quot;recoge de inmediato&quot; 
&#160; 
 De manera ideal cuando se cumpla condicin que genera el mensaje &quot;recoge de inmediato&quot; en las dems vistas de la App, que indique que tiene un pedido que debe recoger de inmediato y que lleve a esta vista 

 ENTREGADOS 
 En&#160; esta seccin se mostrar una card que contendr la siguiente informacin&#58; 
&#160; 
 Informacin&#58; 
 Cdigo del pedido&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-code 
 Nombre punto de venta&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-pod_name 
 Fecha y hora de entrega&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-receipt_datetime 

 Card pedidos entregados 

 Valor del pedido&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-total_price 
 Estado&#58; corresponde a la informacin registra en eatc_sale_order_headers. eatc-state 
&#160; 
 Botn&#58; 
 Ayuda&#58; conectar a la seccin &quot; Centro de ayuda para pedidos &quot;. 

 DETALLE DE ORDEN 
&#160; 
 Cuando se hace click en el rea sensible de la card de la vista anterior, se llevar a una vista en dnde se detalla la informacin del pedido, en cuanto a sus horas y detalles de producto. 
&#160; 
 Para construir la informacin de esta pantalla, se debe obtener, a partir del cdigo de la orden ( eatc-code ) la informacin del encabezado de la orden seleccionada y tambin informacin del detalle de los productos ordenados que se obtienen con las siguientes consultas&#58; 
&#160; 
 Encabezado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers? eatc-code=&#123;&#123;eatc-code&#125;&#125; 
&#160; 
 Detalle&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order? eatc-sale_order_header_code=&#123;&#123;eatc-code&#125;&#125; 

 Pago exitoso confirmado el &#123;&#123;datetime&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order_headers. eatc-date_time &#160; 
&#160; 
 &#123;&#123;Nombre del restaurante&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order_headers. eatc-pod_name &#160; 
&#160; 
 &#123;&#123;Direccin del restaurante&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order_headers. eatc-pod_address &#160; 
&#160; 
 Botn [Cmo llegar] 
 Con los datos eatc-pod_lat,eatc-pod_lon del respectivo encabezado ( eatc_sale_order_headers ), se genera un vnculo que se pueda abrir en una app de mapas y navegacin (como por ejemplo Waze). 
&#160; 
 Resumen productos 
 En esta seccin se muestra la siguiente informacin obtenida de los detalles de la orden&#58; 
&#160; 
 &#123;&#123;tumbnail&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order. eatc-odd_image &#160; 
&#160; 
 &#123;&#123;Nombre del plato&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order. eatc-odd_name &#160; 
&#160; 
 &#123;&#123;unidades&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order. eatc-odd_quantity &#160; 
&#160; 
 &#123;&#123;precio&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order. eatc-odd_total_price &#160; 

 Lnea de tiempo&#58; 
 Se muestra una lnea de tiempo con las fechas y horas que van siendo agregadas a medida que se va procesando el pedido.&#160; Cuando una nueva fecha y hora se registra, la lnea de tiempo se &quot;ilumina&quot; (es decir que pasa de estar en gris, a tener color).&#160; Si hay un dato de esta lnea de tiempo que no se registra en el respectivo encabezado ( eatc_sale_order_headers ) pero una fecha y hora posterior de la siguiente secuencia se registra, la lnea de tiempo intermedia se ilumina pero no muestra el dato de la fecha y hora correspondiente. 

 Seleccin de productos (en vez de por pagar)&#58; se debe colocar la fecha y hora ms antigua entre las fechas de los detalles&#58; eatc_sale_order. eatc-date_time 
 Pagado&#58; se coloca el dato que viene en el encabezado en el siguiente parmetro eatc_sale_order_headers. eatc-date_time 
 Llegada al punto de venta&#58; se coloca el dato que viene en el encabezado en el siguiente parmetro eatc_sale_order_headers. eatc-picking_checkin_datetime 
 Salida del&#160; punto de venta&#58; se coloca el dato que viene en el encabezado en el siguiente parmetro eatc_sale_order_headers. eatc-picking_checkout_datetime 
 Entrega del pedido&#58; se coloca el dato que viene en el encabezado en el siguiente parmetro eatc_sale_order_headers. eatc-receipt_datetime 

 Detalle de tu cobro 
 En una primera instancia no se colocar esta informacin 

 Detalle transacciones 
 En este punto se colocar inicialmente la siguiente informacin&#58; 
&#160; 
 &#123;&#123;Fecha y hora de pago&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order_headers. eatc-date_time &#160; 
&#160; 
 &#123;&#123;Valor total pagado&#125;&#125; 
 Se debe colocar la informacin que se obtiene en el siguiente parmetro eatc_sale_order_headers. eatc-total_price 

 Botn [Necesito ayuda] 
 Conectar a la seccin &quot; Centro de ayuda para pedidos &quot;. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftus-pedidos-seguimiento-de-la-compra-sale%2F3684111314-EmbeddedImage---2024-07-30T011128.867.jpg&ow=1280&oh=975, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftus-pedidos-seguimiento-de-la-compra-sale%2F3684111314-EmbeddedImage---2024-07-30T011128.867.jpg&ow=1280&oh=975 
 APP Usuario final - Sale 

 838.000000000000 

 TUS PEDIDOS: SEGUIMIENTO DE LA COMPRA (EATC_SALE_ORDER_LST)