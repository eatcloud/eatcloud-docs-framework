# ahorro-tablero-resultados-por-referencia-de-producto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin:  
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Se puede basar en la implementacin:  
 Eficiencia > Tablero > Resultados por referencia de producto 

 Mockup: 

 Ahorro  > Tableros > Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

 Label Ttulo de la Vista: Ahorros por referencia de producto 
 class=" lbl_ahorros_por_ref_producto " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_por_ref_producto ) 

 Nota importante para el desarrollo:  
 Adelante se muestran consultas e indicaciones sin tener en cuenta los estados.  Por lo tanto se deber realizar el desarrollo correspondiente para bien sea, con una consulta previa se pueda determinar los anuncios cuyo estado sea "recibido", "pre-certificado" y "certificado", para posteriormente consultar sus respectivos detalles y mostrar la informacin, o para incorporarle de manera peridica el dato del eatc-state (tal cmo se maneja en el encabezado) al correspondiente detalle, con el nimo de poder realizar una consulta filtrada por estado directamente desde eatc_dona .  El desarrollador deber determinar que mtodo es el ms adecuado y el que le entregue mejor performance a la plataforma 

 Tabla de resultados por producto  => debe mostrar informacin de anuncios con estados  "recibido", "pre-certificado" y "certificado" (las consultas indicativas y ejemplos abajo definidos no tienen en cuenta lo anterior y hay que incorporarlo) 
 Se presentar una tabla de resultados por referencia de producto (los valores de la tabla se agruparn por cdigo de producto), en donde se muestra la siguiente informacin 

 Cdigo del producto (en el diseo est en segundo orden pero debe estar de primero)  
 class=" lbl_codigo_producto " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_codigo_producto ) 

 Corresponde al distinct sobre el campo " eatc-odd_id " de la tabla " eatc_dona " para el periodo en cuestin. 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona??eatc-date_time_2[0]={{fecha_inicial}}&eatc-date_time_2[1]=2{{fecha_final}}&eatc_donor={{_DOM. cua_user }}&_distinct= eatc -odd_id  

 Ejemplo: entorno de pruebas, exito, 7 y 8 de junio de 2021 
 https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&eatc-date_time_2[1]=2021-06-08&eatc_donor=exito&_distinct=eatc-odd_id   

 Nombre del producto (en el diseo est en primer orden pero debe estar de segundo)  
 class=" lbl_nombre_producto " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_nombre_producto ) 

 Corresponde al nombre asignado a cada uno de los cdigos anteriormente definidos (puede asimilarse al distinct sobre el campo " eatc-odd_name " de la tabla " eatc_dona " para el periodo en cuestin). 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona??eatc-date_time_2[0]={{fecha_inicial}}&eatc-date_time_2[1]=2{{fecha_final}}&eatc_donor={{_DOM. cua_user }}&_distinct= eatc-odd_name 

 Ejemplo: entorno de pruebas, exito, 7 y 8 de junio de 2021 
 https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&eatc-date_time_2[1]=2021-06-08&eatc_donor=exito&_distinct= eatc-odd_name 

 Ciudad = > NO VA 
 Cantidad = > NO VA 
 Costo unitario = > NO VA 

 Kilogramos entregados 
 class=" lbl_kg_entregados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_kg_entregados ) 

 class=" lbl_pct_kilogramos_entregados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_kg_entregados_desc ) 

 Corresponde a la sumatoria de los Kilogramos Totales ( eatc_dona. eatc-odd_total_weight_kg : que corresponden a los KG efectivamente recibidos por los beneficiarios)  de los anuncios con estados, "received", "pre-certified", "certified", para el artculo en cuestin en el periodo de tiempo seleccionado. 

 Nota para el clculo: Se hace la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona??eatc-date_time_2[0]={{fecha_inicial}}&eatc-date_time_2[1]=2{{fecha_final}}&eatc_donor={{_DOM. cua_user }}& eatc -odd_id={{eatc_dona. eatc -odd_id}} 

 Y se realiza la sumatoria del parmetro eatc_dona. eatc-odd_total_weight_kg 

 Costo total de la mercanca donada 
 class=" lbl_costo_total_donaciones " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_costo_total_donaciones ) 

 class=" lbl_costo_total_donaciones_desc " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_costo_total_donaciones_desc ) 

 Corresponde a la sumatoria de los Costos Totales ( eatc_dona. eatc-odd_total_cost : que corresponden al valor al costo de la mercanca efectivamente recibida por los beneficiarios)  de los anuncios con estados, "received", "pre-certified", "certified", para el artculo en cuestin en el periodo de tiempo seleccionado. 

 Nota para el clculo: Se hace la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona??eatc-date_time_2[0]={{fecha_inicial}}&eatc-date_time_2[1]=2{{fecha_final}}&eatc_donor={{_DOM. cua_user }}& eatc -odd_id={{eatc_dona. eatc -odd_id}} 
 Y se realiza la sumatoria del parmetro eatc_dona. eatc-odd_total_cost 

 Ahorros Impuesto Renta 
 class=" lbl_ahorros_impo_renta " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta ) 

 class=" lbl_ahorros_impo_renta_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta_desc ) 

 Nota para el clculo: Se deber aplicar la frmula de clculo del KPI " income_tax_savings ", sobre el " Costo total de la mercanca donada " (arriba calculado) (se reemplaza en la frmula " eatc_dona_header.eatc-total_cost " con el " Costo total de la mercanca donada " arriba calculado. 

 Ahorros IVA 
 class=" lbl_ahorros_iva " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva ) 

 class=" lbl_ahorros_iva_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva_desc ) 

 Nota para el clculo: Se deber aplicar la frmula de clculo del KPI " vat_savings ", sobre el " Costo total de la mercanca donada " (arriba calculado) (se reemplaza en la frmula " eatc_dona_header.eatc-total_cost " con el " Costo total de la mercanca donada " arriba calculado. 

 Ahorros en almacenamiento ($) => Se puede basar en la i mplementacin de BO   
 class=" lbl_ahorros_almacenamiento " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_almacenamiento ) 

 class=" lbl_ahorros_almacenamiento_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_almacenamiento_desc ) 

 Nota para el clculo: Se deber aplicar la frmula de clculo del KPI " storage_cost_savings ", sobre los " Kilogramos entregados " (arriba calculados) (se reemplaza en la frmula " eatc_dona_header. eatc-total_weight_kg " con los " Kilogramos entregados " arriba calculados. 

 Ahorros en costos de transporte ($)=> Se puede basar en la implementacin de BO 
 class=" lbl_ahorros_transporte " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_transporte ) 

 class=" lbl_ahorros_transporte_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_transporte_desc ) 

 Nota para el clculo: Se deber aplicar la frmula de clculo del KPI " transport_cost_savings ", sobre los " Kilogramos entregados " (arriba calculados) (se reemplaza en la frmula " eatc_dona_header. eatc-total_weight_kg " con los " Kilogramos entregados " arriba calculados. 

 Ahorros en gestin de residuos ($)=>  Se puede basar en la implementacin de BO 
 class=" lbl_ahorros_gestion_residuos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos ) 

 class=" lbl_ahorros_gestion_residuos_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos_desc ) 

 Nota para el clculo: Se deber aplicar la frmula de clculo del KPI " waste_management_savings ", sobre los " Kilogramos entregados " (arriba calculados) (se reemplaza en la frmula " eatc_dona_header .eatc-total_weight_kg " con los " Kilogramos entregados " arriba calculados. 

 Tabla de resultados por producto: ordenamiento 
 La tabla debe permitir ordenar ascendente y descendentemente por todas sus columnas. 

 Tabla de resultados por producto: paginacin 
 La tabla debe mostrarse de manera paginada (de 7 en 7 resultados) 

 Tabla de resultados por producto: Resultados 
 Al final de la tabla se debe presentar la sumatoria de los diferentes ahorros arriba calculados. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 TABLERO > RESULTADOS POR REFERENCIA DE PRODUCTO","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"Cuentas datagov","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":211}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-por-referencia-de-producto%2F1011416935-ahorro_tablero_resultados_por_referencia.jpg&ow=1280&oh=413, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-por-referencia-de-producto%2F1011416935-ahorro_tablero_resultados_por_referencia.jpg&ow=1280&oh=413 
 Cuentas datagov 

 430.000000000000 

 DATA ANALYTICS: AHORRO > TABLERO > RESULTADOS POR REFERENCIA DE PRODUCTO