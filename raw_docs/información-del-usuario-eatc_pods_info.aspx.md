# información-del-usuario-eatc_pods_info.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 Pop up, o pgina que muestra la informacin bsica del usuario (en este caso&#58; el punto de donacin), para su consulta. ESTA VISTA NO TIENE AUN DISEO, ES DECIR QUE NO SE ENTREG MOCKUP 

 Ingreso a la vista&#58; 
 Se ingresa desde el botn usuario (que aparece en la parte superior derecha en el dashboard de escritorio) 

 Informacin a mostrar 
 La vista debe mostrar la siguiente informacin por punto de donacin&#58; 
 eatc-id &#58;&#160; 
 eatc-name &#58;&#160; 
 eatc-phone &#58;&#160; 
 eatc-adress &#58;&#160; 
 eatc-city &#58;&#160; 
 eatc-country &#58;&#160; 
 eatc-lat &#58;&#160; 
 eatc-lon &#58; 
 eatc-responsable &#58; 
 eatc-typology_a &#58;&#160; 
 eatc-dona_packing &#58;&#160; 
 eatc-typology_b &#58; 
 eatc-typology_c &#58;&#160; 

&#160; 
 Ejemplo&#58; 
&#160; 
 Para el punto de donacin &quot;xito de Colombia&quot; debe mostrar la siguiente informacin&#58; 
 &#160; 
 https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31 
&#160; 
 eatc-id &#58; &quot;31&quot;, 
 eatc-name &#58; &quot;EXiTO COLOMBiA&quot;, 
 eatc-phone &#58; &quot;(4) 6050307&quot;, 
 eatc-adress &#58; &quot;&quot;Transversal 39B, Medellin, Antioquia&quot;&quot;, 
 eatc-city &#58; &quot;Medellin&quot;, 
 eatc-country &#58; &quot;co&quot;, 
 eatc-lat &#58; &quot;6.25512&quot;, 
 eatc-lon &#58; &quot;-75.58275&quot;, 
 eatc-responsable &#58; &quot;Juan Camilo Morales&quot;, 
 eatc-typology_a &#58; &quot;EXiTO&quot;, 
 eatc-dona_packing &#58; &quot;&quot;canastillas,cajas&quot;&quot;, 
 eatc-typology_b &#58; &quot;&quot;, 
 eatc-typology_c &#58; &quot;&quot; , 
&#160; 
 Manejo de las &quot;etiquetas&quot; o &quot;labels&quot; 
 EatCloud va a implementar un mecanismo para personalizar las etiquetas de informacin que preseden la misma, en especfico estas 
 eatc-id &#58;&#160; 
 eatc-name &#58;&#160; 
 eatc-phone &#58;&#160; 
 eatc-adress &#58;&#160; 
 eatc-city &#58;&#160; 
 eatc-country &#58;&#160; 
 eatc-lat &#58;&#160; 
 eatc-lon &#58; 
 eatc-responsable &#58; 
 eatc-typology_a &#58;&#160; 
 eatc-dona_packing &#58;&#160; 
 eatc-typology_b &#58; 
 eatc-typology_c &#58;&#160; 

&#160; 
 PENDIENTE&#58; Consulta de idioma y de abreviatura del cliente&#160; 

&#160; 
 Consulta de equivalentes para las etiquetas 
 Para mostrar la informacin se debe realizar la siguiente consulta (dadas las caractersticas de cada dato) y extrayendo el dato &quot; equivalence &quot;.&#160; Dado que hay dos tipos de equivalencias&#58; una que corresponde a solamente la internacionalizacin, en donde una &quot;etiqueta&quot; solo se traduce y con esta traduccin sirve para todos los clientes de EatCloud y otra que comprende la &quot;personalizacin&quot; en donde el nombre depende de cada cliente (como por ejemplo en los datos que tienen que ver con tipologas), se dan estos dos tipos de equivalencias&#58; 
&#160; 
 Etiquetas personalizadas 
 eatc-id &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-id&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=EXTO 
 eatc-name &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-name&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=EXTO 
 eatc-typology_a &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-typology_a&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=EXTO 
 eatc-typology_b &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-typology_b&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=EXTO 

 eatc-typology_c &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-typology_c&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=EXTO &#160; 
&#160; 
 Etiquetas internacionalizadas 
 eatc-phone &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-phone&amp;language__idiomas__codigo=es&amp;customer__eatc_clientes__code=_todos &#160; 
 eatc-adress &#58;&#160; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-adress&amp;language__idiomas__codigo=es 
 eatc-city &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-city&amp;language__idiomas__codigo=es &#160; 
 eatc-country &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-country&amp;language__idiomas__codigo=es &#160; 
 eatc-lat &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-lat&amp;language__idiomas__codigo=es &#160; 
 eatc-lon &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-lon&amp;language__idiomas__codigo=es &#160; 
 eatc-responsable &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc-responsable&amp;language__idiomas__codigo=es &#160;&#160;&#160; 
 eatc-dona_packing &#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_int_cust_labels&amp;label=eatc- dona_packing &amp;language__idiomas__codigo=es &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Donantes 

 INFORMACIN DEL USUARIO: EATC_PODS_INFO