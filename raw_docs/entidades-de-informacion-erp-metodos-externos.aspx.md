# entidades-de-informacion-erp-metodos-externos.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL&#58; 
 Las entidades de información han sido definidas dentro de la plataforma como los &quot;métodos&quot; de la misma. Dichos métodos contienen &quot;parámetros&quot; (o datos) que han sido documentados técnicamente para su manejo estándar. 

 MÉTODOS (ENTIDADES DE INFORMACIÓN)&#58; 
 Para consultar los métodos o entidades de información de nuestra plataforma se ingresa el siguiente recurso&#58; 

Vista tabla 

 https&#58;//config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?maestro=eatc_metodos_erp&amp;lista=si&amp;atrib_filtro_tb=name&amp;val_filtro_tb=_todos 
&#160; 
Vista json 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_metodos_erp&amp;nombre=_todos &#160; 

 Documentación de métodos&#58; 
 Cada método documentado, contiene un nombre (que también sirve de identificador), un tipo, una descripción, una URL, y una URL de parámetros. 

Ejemplo&#58; método &quot;puntos_de_donacion&quot; 
 Vista json&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_metodos_erp&amp;name=puntos_de_donacion &#160; 

 &#123; 
 timestamp &#58; &quot;190816100535&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 res &#58;&#160; 
 [ 
 &#123; 
 character_encoding &#58; &quot;UTF-8&quot;, 
 delete_parameter &#58; &quot;&quot;, 
 description &#58; &quot;Maestro de los puntos de donación de Almacenes Éxtito&quot;, 
 format &#58; &quot;Valores separados por comas&quot;, 
 format__formatos_mensajes_datos__extension &#58; &quot;csv&quot;, 
 id_parameters &#58; &quot;id&quot;, 
 id__ &#58; &quot;EXTOOTRSpuntos_de_donacion&quot;, 
 information_source &#58; &quot;Otras fuentes de información del Grupo Éxito&quot;, 
 information_source__eatc_information_sources__code &#58; &quot;OTRS&quot;, 
 information_source__eatc_information_sources__customer__eatc_clientes__code &#58; &quot;EXTO&quot;, 
 name &#58; &quot;puntos_de_donación&quot;, 
 observations &#58; &quot;Los almacenes serán definidos de manera conjunta con Juan Carlos Buitrago, a fin de garantizar el éxito del piloto. Se definió que el login de la plataforma para el usuario final en bodega, por efectos de su alta rotación, serán los datos del almacén.&quot;, 
 raw_file_type &#58; &quot;Texto separado por caracteres&quot;, 
 separator &#58; &quot;punto y coma&quot;, 
 separator__separadores_archivos_planos__caracter &#58; &quot;;&quot;, 
 several_files &#58; &quot;no&quot;, 
 type &#58; &quot;maestro&quot;, 
 url &#58; &quot;&quot; 
 &#125; 
 ], 
 memoria &#58; 0.31, 
 duracion &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 

 PARÁMETROS (DATOS)&#58; 
 Para consultar los parámetros de los diferentes métodos o entidades de información de nuestra plataforma se ingresa el siguiente recurso&#58; 

Vista tabla 
 https&#58;//config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?maestro=eatc_parametros_erp&amp;lista=si&amp;atrib_filtro_tb=method&amp;val_filtro_tb=_todos &#160; 
Vista json 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros_erp&amp;method=_todos &#160; 

 Documentación de parámetros&#58; 
 Cada parámetro documentado, corresponde a un método en particular &quot;method&quot; (con su respectivo tipo&#58; &quot; method__eatc_metodos_erp__type &quot;, el sistema de información del que proviene &quot; method__eatc_metodos_erp__information_source &quot;, con su código &quot; method__eatc_metodos_erp__information_source__eatc_information_sources__code&quot; , y el cliente &quot; method__eatc_metodos_erp__information_source__eatc_information_sources__customer__eatc_clientes__cod &quot; ), posee un nombre ( &quot;name&quot; ), una descripción ( &quot;description&quot; ), se define si el parámetro es obligatorio o no ( &quot;required&quot; ), la definición se hace parte del ID (si hace parte de una clave compuesta o es una clave única&#58; &quot; is_part_of_the_id &quot; ),&#160; ( &quot;k_formato&quot; ). Algunos de estos atributos son obligatorios y otros no. Con toda esta información se pueden crear a partir de la documentación de la configuración los esquemas de persistencia en los diferentes entornos. 

Ejemplo&#58; método &quot;articulos&quot;, parámetro &quot;categoria_codigo&quot; 
 Vista json&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=mzzaafv_parametros&amp;a_method=articulos&amp;name=categoria_codigo &#160; 

&#160; 
 &#123; 
 description &#58; &quot;Código de la categoría&quot;, 
 id__ &#58; &quot;articulosEXTOCINCcategoria_codigo&quot;, 
 is_part_of_the_id &#58; &quot;no&quot;, 
 method &#58; &quot;articulos&quot;, 
 method__eatc_metodos_erp__information_source &#58; &quot;Sistema Cinco&quot;, 
 method__eatc_metodos_erp__information_source__eatc_information_sources__code &#58; &quot;CINC&quot;, 
 method__eatc_metodos_erp__information_source__eatc_information_sources__customer__eatc_clientes__cod &#58; &quot;EXTO&quot;, 
 method__eatc_metodos_erp__type &#58; &quot;maestro&quot;, 
 name &#58; &quot;categoria_codigo&quot;, 
 required &#58; &quot;si&quot; 
 &#125; 

 Índice de métodos y parámetros&#58; 
 A continuación la relación de los métodos y parámetros definidos para la plataforma&#58; 
&#160; 
 ÉXITO&#58; 
 Puntos de donación 
 Artículos 
 Sublíneas 
 Categorías 
 Subcategorías 

 Anuncio de donación 
&#160; 
 ÁBACO&#58; 
 eatc_pods&#58; puntos de donación 
 eatc_attention_schedule&#58; horarios de atención 
 eatc_odds&#58; objetos de donación 
 eatc_donation_managers&#58; gestores de donaciones 
 eatc_final_beneficiaries&#58; beneficiarios finales 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CARACTERIZACIÓN DE ENTIDADES DE INFORMACIÓN EXTERNAS