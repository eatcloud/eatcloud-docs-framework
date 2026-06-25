# d-informe-de-anuncios-prg-dlv.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se basa en esta implementacin del informe de anuncios programados - despachados realizada para el BO Beneficiarios ABACO 
&#160; 
 Esta herramienta sirve para analizar los anuncios despachados (delivered) que no completan el proceso para quedar como recibidos (recieved) y que tambin es importante promover se complete el proceso 

 Consulta general para traer anuncios 
 Se debe configurar un selector de fecha inicial ( class=&quot; lbl_fecha_inicial &quot; )&#160; (cuyo valor por defecto debe ser el primer da del mes actual) y selector de fecha final ( class=&quot; lbl_fecha_final &quot; ) (cuyo valor por defecto debe ser el da actual) que permita seleccionar por fecha de publicacin ( eatc_dona_headers. eatc-publication_date ) los anuncios de donacin del donante respectivo 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc-donor= &#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Selector de tipo de anuncio&#58; 
 El informe deber mostrar un selector para establecer el estado&#58;&#160; 
 Despachados ( delivered )&#58; valor por defecto del selector&#58; 
 class= lbl_despachados &#160; 
&#160; 
 Programados ( scheduled ) 
 class= lbl_programados &#160; 

 Ranking de eatc-pod_name por cantidad de anuncios en este estado 
 Se deber generar una tabla que muestre los Puntos de Donacin con ms cantidad de anuncios en este estado y que muestre la siguiente informacin&#58; 
&#160; 
 Punto de donacin 
 Label&#58; id=&quot;lbl_nombre_punto_donacion&quot; 
 Orden&#58; 1ra columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-pod_name 
&#160; 
 Cdigo punto de donacin 
 Label&#58; id=&quot;lbl_codigo_punto_donacion&quot; 
 Orden&#58; 1.1ra columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-pod_name 
&#160; 
 Nmero de anuncios (se ordena por esta columna el listado mostrando de mayor a menor cantidad de anuncios)***DINAMIZAR a partir de _DOM.cua_master 
 Label&#58; id=&quot;lbl_numero_anuncios&quot; 
 Orden&#58; 2da columna 
 La informacin se toma del&#58; count de las siguientes consultas segn sea el caso 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state= scheduled &amp;eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&amp;_compress 
&#160; 
 &#123;&#123;URL_donantes&#125;&#125;api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state= delivered &amp;eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&amp;_compress 
&#160; 
 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin. 

&#160; 
 (***NUEVO***) &quot;Delivered&quot;&#58; Nmero de anuncios pendientes de validacin del cdigo de recogida (donante) 
 Label&#58; class=&quot;lbl_pendientes_validacion_codigo_recogida&quot; 
 Orden&#58; 2.1 columna 
 La informacin se toma del&#58; count de la siguiente consulta segn sea el caso 
 &#123;&#123;URL_donantes&#125;&#125;api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state= delivered &amp;eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&amp; eatc_code_verification_datetime =0000-00-00%2000&#58;00&#58;00&amp;_compress 
&#160; 
 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin. 

&#160; 
 (***NUEVO***) &quot;Delivered&quot;&#58; Nmero de anuncios pendientes de verificacin del anuncio (beneficiario) 
 Label&#58; class=&quot;lbl_pendientes_verificacion_donacion&quot; 
 Orden&#58; 2.2 columna 
 La informacin se toma del&#58; count de la siguiente consulta segn sea el caso 
 &#123;&#123;URL_donantes&#125;&#125;api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state= delivered &amp;eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&amp; eatc-receipt_datetime =0000-00-00%2000&#58;00&#58;00&amp;_compress 
&#160; 
 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin, 

 Detalle de anuncios en este estado 
 Accedido desde el nmero de anuncios del informe anterior, se debe generar una lista con los anuncios con este estado.&#160; La lista debe contener la siguiente informacin y permitir la siguiente edicin de informacin&#58; 
&#160; 
 Buscador&#58; 
 Esta vista debe tener un buscador que permita ubicar de la manera ms amplia posible un anuncio en el listado. 

&#160; 
 Fecha publicacin 
 Label&#58; class=&quot;lbl_fecha_publicacion&quot; 
 Orden&#58; 1ra columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-publication_date 

&#160; 
 Cdigo 
 Label&#58; class=&quot;lbl_codigo&quot; 
 Orden&#58; 2da columna 
 La informacin se toma del&#58; eatc_dona_headers .eatc-code 

&#160; 
 Fecha de programacin 
 Label&#58; class=&quot;lbl_fecha_programacion&quot; 
 Orden&#58; 3ta columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-scheduling_datetime 

&#160; 
 Fecha de recogida programada 
 Label&#58; class=&quot;lbl_fecha_recogida_programada&quot; 
 Orden&#58; 4ta columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-programed_picking_datetime 

&#160; 
 Fecha de llegada punto de donacin 
 Label&#58; class=&quot;lbl_fecha_llegada_pod&quot; 
 Orden&#58; 5ta columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-picking_checkin_datetime 

&#160; 
 Fecha y hora validacin cdigo recogida 
 Label&#58; class=&quot;lbl_fecha_validacion_codigo&quot; 
 Orden&#58; 6ta columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc_code_verification_datetime 

&#160; 
 Fecha y hora salida punto donacin 
 Label&#58; class=&quot;lbl_fecha_salida_pod&quot; 
 Orden&#58; 6ta columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-picking_checkout_datetime 

&#160; 
 Fecha y hora recepcin anuncio 
 Label&#58; class=&quot;lbl_fecha_recepcin&quot; 
 Orden&#58; 6ta columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-receipt_datetime&quot; 

&#160; 
 KG 
 Label&#58; class=&quot;lbl_kg&quot; 
 Orden&#58; 7ma columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-total_weight_kg 

&#160; 
 Estado 
 Label&#58; class=&quot;lbl_estado&quot; 
 Orden&#58; 5ta columna 
 La informacin se toma de&#58;&#160; eatc_donation_managers.eatc-state 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Donantes 

 INFORME DE ANUNCIOS PROGRAMADOS - DESPACHADOS