# eficiencia-tablero-resultados-por-referencia-de-producto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Mockup&#58; 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Resultados por referencia de producto 
 class=&quot; lbl_resultados_por_ref_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_resultados_por_ref_producto ) 
&#160; 
 Descripcin de la tabla&#58; Resultados por referencia de producto (No est en el diseo) 
 Debajo del ttulo de la vista se debe colocar la siguiente descripcin&#58; 
&#160; 
 class=&quot; lbl_resultados_por_ref_producto_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_resultados_por_ref_producto_desc ) 
&#160; 
 La siguiente tabla muestra datos de los pesos de los productos efectivamente entregados (con cdigo de recogida verificado y verificacin detallada del anuncio por parte del beneficiario), en el periodo en cuestin (anuncios con estado &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;). 
&#160; 
 Nota importante para el desarrollo&#58;&#160; 
 Adelante se muestran consultas e indicaciones sin tener en cuenta los estados.&#160; Por lo tanto se deber realizar el desarrollo correspondiente para bien sea, con una consulta previa se pueda determinar los anuncios cuyo estado sea &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;, para posteriormente consultar sus respectivos detalles y mostrar la informacin, o para incorporarle de manera peridica el dato del eatc-state (tal cmo se maneja en el encabezado) al correspondiente detalle, con el nimo de poder realizar una consulta filtrada por estado directamente desde eatc_dona .&#160; El desarrollador deber determinar que mtodo es el ms adecuado y el que le entregue mejor performance a la plataforma 

 Tabla de resultados por producto =&gt; debe mostrar informacin de anuncios con estados&#160; &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot; (las consultas indicativas y ejemplos abajo definidos no tienen en cuenta lo anterior y hay que incorporarlo) 
 Se presentar una tabla de resultados por referencia de producto (los valores de la tabla se agruparn por cdigo de producto), en donde se muestra la siguiente informacin 

 Cdigo del producto (en el diseo est en segundo orden pero debe estar de primero)&#160; 
 class=&quot; lbl_codigo_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_producto ) 
&#160; 
 Corresponde al distinct sobre el campo &quot; eatc-odd_id &quot; de la tabla &quot; eatc_dona &quot; para el periodo en cuestin. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona??eatc-date_time_2[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-date_time_2[1]=2&#123;&#123;fecha_final&#125;&#125;&amp;eatc_donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc -odd_id&#160; 
&#160; 
 Ejemplo&#58; entorno de pruebas, exito, 7 y 8 de junio de 2021 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&amp;eatc-date_time_2[1]=2021-06-08&amp;eatc_donor=exito&amp;_distinct=eatc-odd_id &#160; 

&#160; 
 Nombre del producto (en el diseo est en primer orden pero debe estar de segundo)&#160; 
 class=&quot; lbl_nombre_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_nombre_producto ) 
&#160; 
 Corresponde al nombre asignado a cada uno de los cdigos anteriormente definidos (puede asimilarse al distinct sobre el campo &quot; eatc-odd_name &quot; de la tabla &quot; eatc_dona &quot; para el periodo en cuestin). 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona??eatc-date_time_2[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-date_time_2[1]=2&#123;&#123;fecha_final&#125;&#125;&amp;eatc_donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc-odd_name 
&#160; 
 Ejemplo&#58; entorno de pruebas, exito, 7 y 8 de junio de 2021 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&amp;eatc-date_time_2[1]=2021-06-08&amp;eatc_donor=exito&amp;_distinct= eatc-odd_name 

&#160; 
 Kilogramos entregados 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_pct_kilogramos_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Corresponde a la sumatoria de los Kilogramos Totales ( eatc-total_weight_kg &#58; que corresponden a los KG efectivamente recibidos por los beneficiarios)&#160; de los anuncios con estados, &quot;received&quot;, &quot;pre-certified&quot;, &quot;certified&quot;. 

&#160; 
 Porcentaje de Kilogramos entregados (No est en el diseo) 
 class=&quot; lbl_pct_kilogramos_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kilogramos_entregados ) 
&#160; 
 class=&quot; lbl_pct_kilogramos_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kilogramos_entregados_desc ) 
&#160; 
 Corresponde a la divisin del total de kilogramos de los anuncios efectivamente recibidos ( eatc-total_weight_kg ) por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;),&#160; sobre el peso original ( original_weight_kg ) de los anuncios (todos los anuncios) generados en el periodo. 
&#160; 
 Nmero de anuncios (frecuencia de donacin de cada referencia) 
 class=&quot; lbl_numero_anuncios_por_referencia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_por_referencia ) 
&#160; 
 class=&quot; lbl_numero_anuncios_por_referencia_desc &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_por_referencia_desc ) 
&#160; 
 Es la cantidad de anuncios en los que se realiz una donacin de la referencia particular en el periodo seleccionado. 
&#160; 
 Corresponde al distinct sobre el campo &quot; eatc-dona_header_code &quot; (de la tabla &quot; eatc_dona &quot; para un&#160; eatc-odd_id en el periodo en cuestin. 
 cont de &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona??eatc-date_time_2[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-date_time_2[1]=2&#123;&#123;fecha_final&#125;&#125;&amp;eatc_donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc-odd_id= &#123;&#123; eatc-odd_id &#125;&#125;&amp;_distinct= eatc-dona_header_code&#160; 
&#160; 
 Ejemplo&#58; entorno de pruebas, exito, 7 y 8 de junio de 2021, para el producto con eatc-odd_id = 1483446 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&amp;eatc-date_time_2[1]=2021-06-08&amp;eatc_donor=exito&amp; eatc-odd_id= 1483446&amp;_distinct= eatc-dona_header_code = 1 

&#160; 
 Tabla de resultados por producto&#58; ordenamiento 
 La tabla debe permitir ordenar ascendente y descendentemente por todas sus columnas. 
&#160; 
 Tabla de resultados por producto&#58; paginacin 
 La tabla debe mostrarse de manera paginada&#160; 
&#160; 
 Tabla de resultados por producto&#58; Filtros 
 Se proponen los siguientes filtros, los cuales deben irse implementando de manera paulatina 

 Tabla de resultados por producto&#58; Resultados 
 Al final de la tabla se debe presentar la sumatoria de los KG donados y los KG aprovechados segn los filtros que se la apliquen a la tabla. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-por-referencia-de-producto%2F648535439-eficiencia_tablero_por_ref_producto.jpg&ow=1071&oh=526, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-por-referencia-de-producto%2F648535439-eficiencia_tablero_por_ref_producto.jpg&ow=1071&oh=526 
 Cuentas datagov 

 384.000000000000 

 DATA ANALYTICS: EFICIENCIA > TABLERO > RESULTADOS POR REFERENCIA DE PRODUCTO