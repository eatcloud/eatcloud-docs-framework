# detalle-de-producto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo de la vista&#58; https&#58;//drive.google.com/file/d/1JTxIpi_1dcVJJvVJUABvRKk1G83VX-oh/view?usp=sharing &#160; 
&#160; 
 En esta vista se presenta el detalle del producto que se obtiene de la consulta respectiva y de una consulta adicional (horarios de recogida). Adems presenta la oportunidad de agregar el producto al &quot;carro de compras&quot;, para seguir adelante con el proceso 

 Muestra informacin de esta vista se presenta de la siguiente manera&#58; 
 Imagen del producto &#58; corresponde a la informacin que se recibe en el parmetro eatc-odd_image . 
 X (parte superior izquierda) &#58; devuelve a la vista desde la cual se ingres al detalle y acciona los procesos propios de la funcionalidad &quot; Aadir al Carro de compras &quot; (esto tambin debe funcionar si se presiona el botn atrs de la barra de navegacin del sistema operativo o del telfono). Ms abajo se puntualiza mejor el funcionamiento de estos botones. 
 cono carro de compras (parte superior derecha)&#58; se detalla su funcionamiento ms abajo . 
 cono compartir (parte inferior derecha)&#58; enva la informacin para compartir a la funcionalidad de compartir informacin de oferta en otras apps del telfono. 

 Nombre del producto&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_name 
 % de descuento &#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_max_discount 

 Contiene alergenos &#58; (SI / NO&#58; difiere de la imagen ilustrativa) corresponde a la informacin que se&#160; recibe en el parmetro eatc-contains_alergens (si este parmetro contiene el valor &quot;0&quot;, nulo o vaco, no se muestra la leyenda &quot;Contiene alergenos&quot; 
 Descripcin del producto&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_description .&#160; 
 Horario de atencin &#58; con el dato que se recibe en el parmetro eatc-pod_id y el que se recibe en eatc_cua_origin, se realiza la siguiente consulta para traer la informacin, del da actual, y del da siguiente al actual (en la imagen se coloca un solo horario, pero la idea es que se muestre el da actual (por ejemplo&#58; LU) y el da siguiente (por ejemplo&#58; MA)) 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123; eatc_cua_origin&#125;&#125; /eatc_sale_schedule?eatc-pod_id= eatc-pod_id &#160; 
 Direccin&#58; corresponde a la informacin que se recibe en el parmetro eatc-pod_address 
 A X KM&#58; con el dato que se recibe en el parmetro km obtenido de la &quot; consulta de ofertas cercanas &quot;&#160; 
 Precio antes de la oferta&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_unit_price. Se debe colocar ms pequeo y tachado ates del precio de la oferta 
 Precio en oferta&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_min_sale_unit_price 

 Aadir al carrito de compras 
 Se desarrolla en profundidad aqu . Con esta accin se determinan las cantidades_a_agregar_a_la_orden 

 Botones que hacen salir de la vista de detalle de producto 
 Existen tres botones que harn que el usuario salga de la presente vista, hacia otras relacionadas.&#160; Al accionar dichos botones se deber proceder a Aadir al carrito de compras (en segundo plano) y a realizar redirecciones y acciones especficas segn sea el caso. 

 Botn &quot;X&quot; parte superior izquierda 
 Este botn siempre deber enviar a la vista de dashboard de punto de venta (sin importar qu otra vista se halla ingresado al respectivo detalle), realizando la consulta respectiva para popular dicha vista.&#160; Este botn tambin realiza en segundo plano la accin de creacin de registro de orden , 

 cono &quot;Carrito de compras&quot; 
 Este botn siempre deber ir mostrando en un globo (en la parte superior derecha del cono), las cantidades que se van adicionando (y que para el caso del primer producto que se adiciona, ser igual a la cantidad presente en el botn &quot; Comprar ahora &quot;.&#160; Para los otros casos, ser igual a sumatoria de las cantidades presentes en los detalles de la respectiva eatc_sale_order ). Al presionar el botn&#160; se realiza en segundo plano la accin de creacin de registro de orden ,&#160; y se redirecciona a la vista de Carro de Compras . 

 Botn &quot;volver&quot; o &quot;atrs&quot; de la barra de navegacin del sistema operativo o del telfono 
 Este botn siempre deber enviar a la vista de dashboard de punto de venta (sin importar qu otra vista se halla ingresado al respectivo detalle), realizando la consulta respectiva para popular dicha vista.&#160; Este botn tambin realiza en segundo plano la accin de creacin de registro de orden . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdetalle-de-producto%2F3024600179-EmbeddedImage---2024-07-29T231933.406.jpg&ow=404&oh=1038, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdetalle-de-producto%2F3024600179-EmbeddedImage---2024-07-29T231933.406.jpg&ow=404&oh=1038 
 App usuario final - Sale 

 808.000000000000 

 DETALLE DE PRODUCTO (EATC_SALE)