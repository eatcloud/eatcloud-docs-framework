# ahorro-tablero-resultados-generales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin:  
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Se puede basar en la implementacin:  
 Eficiencia > Tablero > Resultados generales 

 Mockup: 

 Ahorro  > Tableros > Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

 Label Ttulo de la Vista: Resultados generales 
 class=" lbl_resultados_generales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_resultados_generales ) 

 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario: grfico de tendencia) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto . El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer: en este caso no se genera grfico).  

 Ahorros totales ($) => Se puede basar en la implementacin de BO - KPI por defecto 

 class=" lbl_ahorros_totales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales ) 

 class=" lbl_ahorros_totales_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_desc ) 

 Corresponde a totalidad de ahorros generados por tu decisin de donar en vez de botar en el periodo seleccionado (se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado"). 

 Kilogramos entregados => nos podemos basar en la implementacin de " Eficiencia > Tablero > Resultados generales > KPIs Principales > Kilogramos entregados " 

 class=" lbl_kg_entregados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_kg_entregados ) 

 class=" lbl_kg_entregados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_kg_entregados_desc ) 

 Nmero de anuncios entregados => nos podemos basar en la implementacin de " Sostenibilidad > Tablero > Impacto ambiental > KPIs Principales > Nmero de anuncios entregados " 

 class=" lbl_numero_anuncios_entregados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_numero_anuncios_entregados ) 

 class=" lbl_numero_anuncios_entregados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_numero_anuncios_entregados_desc ) 

 KPIs secundarios 
 Con base en los KPIs calculados anteriormente se saca un promedio diario para el periodo consultado y tambin se realizan otros clculos para presentar informacin estadstica 

 Ahorros totales ($) por donacin entregada (en el diseo: Ahorros totales / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 

 class=" lbl_ahorros_totales_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_donacion ) 

 class=" lbl_ahorros_totales_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros totales obtenidos sobre el nmero de donaciones efectivamente recibidas por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Ahorros totales ($) por KG entregado (en el diseo: Ahorros totales / Kg entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_totales_por_kg " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? 
 plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_kg ) 

 class=" lbl_ahorros_totales_por_kg_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_kg_desc ) 

 Corresponde a la divisin del valor de los ahorros totales obtenidos sobre la sumatoria del total de kilogramos de los anuncios efectivamente recibidos por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 TABLERO > RESULTADOS GENERALES (INFORME POR DEFECTO)","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"CUENTAS DATAGOV","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":211}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-generales%2F2291805563-ahorro_tablero_resultados_generales.jpg&ow=852&oh=680, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-generales%2F2291805563-ahorro_tablero_resultados_generales.jpg&ow=852&oh=680 
 CUENTAS DATAGOV 

 412.000000000000 

 DATA ANALYTICS: AHORRO > TABLERO > RESULTADOS GENERALES (INFORME POR DEFECTO)