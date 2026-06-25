# sale-chekout-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

&#160; 
 Diseo&#58; 
 Tipo de recogida&#58; https&#58;//drive.google.com/file/d/11sv5XatX0dYN3Vc_VKu4V5LiF5IY0mzH/view?usp=sharing 
 Datos persona&#58; https&#58;//drive.google.com/file/d/1mkuhFCT5tv6WwsIlHc5o-ooCwrAotrsC/view?usp=sharing &#160; 
 Payments methods&#58; https&#58;//drive.google.com/file/d/1iTdBB0HH2TUUAp7zziTweZRoSagEBVHK/view?usp=sharing &#160; 
 Order sumary&#58; https&#58;//drive.google.com/file/d/1BfIRNrOlP4SEbXTAfPWRb4U65PkrgCV4/view?usp=sharing &#160; 
 Thks&#58; https&#58;//drive.google.com/file/d/1YuDFoYLylvuYdIcAAPtKdyC4vGG3DdI0/view?usp=sharing &#160; 

 TIPO (MTODO) DE RECOGIDA (ENTREGA) ***NUEVO&#58; INTERNACIONALIZACIN*** 
 En este apartado del check out, el sistema muestra en una card seleccionable los mtodos de entrega disponibles.&#160; Dichos mtodos se podrn consultar a travs mediante los siguientes procesos&#58; 
&#160; 
 NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los causales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_sale_delivery_methods&amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125; 

 Anteriormente &#58; &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_delivery_methods?_id=_* 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_sale_delivery_methods&amp;eatc_language=en &#160; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en el selector de la siguiente manera&#58; 
&#160; 
 Antes de la tarjeta que muestra la informacin del mtodo de entrega de la oferta, se debe mostrar la siguiente leyenda&#58; 
&#160; 
 Por favor seleccion un mtodo de entrega para la oferta realizada 
&#160; 
 La tarjeta del mtodo de entrega deber contener la siguiente informacin&#58; 
&#160; 
 Nombre &#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_sale_delivery_methods&amp;eatc_int_field= eatc-name &amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125; 
 Descripcin&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_sale_delivery_methods&amp;eatc_int_field= eatc-description &amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125; 
&#160; 
 Despus de las tarjetas se debe mostrar la siguiente leyenda&#58; 
&#160; 
 Al seleccionar el mtodo de entrega te comprometes a aplicar sus especificaciones despus de realizar el pago correspondiente.&#160; 
&#160; 
 Al seleccionar el mtodo de entrega (haciendo clic en la card), el sistema toma el valor consignado en eatc_internationalize_dt. eatc_data_id y con l realiza la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_delivery_methods?_id=&#123;&#123;eatc_internationalize_dt. eatc_data_id &#125;&#125; 
&#160; 
 el sistema guarda el valor eatc_sale_delivery_methods. eatc-code correspondiente en una variable que luego deber (si el check-out es exitoso), guardar en el siguiente parmetro del encabezado de orden&#58; 
&#160; 
 eatc_sale_order_header. eatc-delivery_method 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_header 

 X 
 La X en la parte superior izquierda devuelve a la funcionalidad anterior 
&#160; 
 Ver carrito 
 El botn Ver Carrito direcciona al Carro de Compras 
&#160; 
 Botn de accin inferior derecho 
 Este botn aparecer una vez se seleccione el mtodo de recogida, este botn se desplegar, y segn la seleccin realizada el botn podr tener varias leyendas, de acuerdo a los datos incorporados en la informacin del mtodo de entrega que se obtiene a partir de la siguiente consulta&#58; 
&#160; 
 &#160;&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale_delivery_methods ?_id=_* 
&#160; 
 y que fue seleccionado ms arriba de la siguiente manera&#58; 
&#160; 
 eatc_sale_delivery_methods.eatc-require_delivery_address = si 
 El sistema deber desplegar el botn [Datos de envo] que direcionar a la funcionalidad de su mismo nombre 
&#160; 
 eatc_sale_delivery_methods.eatc-require_delivery_address = no 
 El sistema deber evaluar el prximo parmetro ( eatc-require_picker_data ) para establecer cmo ser el comportamiento del botn 
&#160; 
 eatc_sale_delivery_methods.eatc-require_picker_data = si 
 El sistema deber desplegar el botn [Datos de quien recoge] que direcionar a funcionalidad &quot; Datos recogida &quot;. 
&#160; 
 eatc_sale_delivery_methods.eatc-require_picker_data = no 
 El sistema deber desplegar el botn [Mtodo de pago] que direcionar a funcionalidad &quot; Medios de pago &quot;, previa recoleccin de &quot; Datos recogida a partir de los datos del usuario (proceso en segundo plano) &quot; 

 DATOS DE ENVO (NO SE IMPLEMENTAR EN LA PRIMERA ETAPA) 

 En esta funcionalidad se solicitan los datos de envo para procesos de entrega de la orden en el domicilio del usuario (no se implementar en la primera etapa) 

 DATOS RECOGIDA 

 Formulario de captura 
 En esta funcionalidad se solicitan los datos de la persona que recoge la oferta. El comportamiento de esta funcionalidad debe ser similar a la implementada para registrar los datos de quien recoge en los anuncios de donacin (se debe preguntar a Ivn Restrepo para que entregue cdigo para su revisin e implementacin, dado que cuando se termina el proceso se debe mostrar el cdigo de verificacin para que pueda ser enviado a quien recoge).&#160; El formulario de captura ser de la siguiente manera&#58; 
&#160; 
 Nombre de quien recoge 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 

Una variable&#58; eatc_sale_order_headers. eatc-picker_name , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 
&#160; 
 Nmero de documento 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Una variable&#58; eatc_sale_order_headers. eatc-picker_doc_id , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 

 Botn &quot;Tipo recogida&quot; 
 Este botn retorna a la funcionalidad del mismo nombre . 

 Botn &quot;Medio de pago&quot; 
 Este botn direcciona a la funcionalidad del mismo nombre . 

 DATOS RECOGIDA A PARTIR DE LOS DATOS DEL USUARIO (PROCESO EN SEGUNDO PLANO) 
&#160; 
 Si es el usuario mismo quien recoge la oferta, los datos de recogida se toman directamente de los datos del usuario ( eatc_sale_users ) de la siguiente manera 
&#160; 
 Nombre de quien recoge 
 Tipo de dato &#58; string 
 La informacin se toma de&#58; eatc_sale_users. eatc-user_name 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Una variable&#58; eatc_sale_order_headers. eatc-picker_name , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 
&#160; 
 Nmero de documento 
 Tipo de dato &#58; string 
 La informacin se toma de&#58; eatc_sale_users. eatc-doc_id 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Una variable&#58; eatc_sale_order_headers. eatc-picker_doc_id , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 

 MEDIO DE PAGO 
&#160; 
 Esta funcionalidad se debe adecuar a las posibilidades brindadas por la pasarela de pagos y que se estipulan aqu&#58; https&#58;//docs.wompi.co/docs/en/metodos-de-pago 
&#160; 
 Botn &quot;Confirmar pedido&quot; (en vez de &quot;Ver pedido&quot;) 
 Retorna a la funcionalidad de &quot; Carro de Compras &quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsale-chekout-sale%2F2520499962-EmbeddedImage---2024-07-30T004650.984.jpg&ow=325&oh=766, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsale-chekout-sale%2F2520499962-EmbeddedImage---2024-07-30T004650.984.jpg&ow=325&oh=766 
 App usuario final - Sale 

 831.000000000000 

 SALE CHECKOUT: OBTENCIN DE DATOS PARA REALIZAR LA TRANSACCIN DE VENTA (EATC_SALE_CHK)