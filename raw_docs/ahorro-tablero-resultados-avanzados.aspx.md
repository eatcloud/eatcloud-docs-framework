# ahorro-tablero-resultados-avanzados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin:  
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Se puede basar en la implementacin:  
 Eficiencia > Tablero > Resultados avanzados 

 Mockup: 

 Ahorro  > Tableros > Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

 Label Ttulo de la Vista: Resultados avanzados 
 class=" lbl_resutados_avanzados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_resutados_avanzados ) 

 A HORROS SEGN TIPOLOGA A 
 Se mostrarn en una franja horizontal en primer lugar, los resultados por la tipologa a ( class=" lbl_eatc_pods_typolgy_a " ) de los puntos de donacin de la cuenta respectiva 

 A HORROS SEGN TIPOLOGA A DE PUNTOS DE DONACIN 

 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 

 class=" lbl_ahorros_segun " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_segun ) 

 Seguido de  

 class=" lbl_eatc_pods_typolgy_a " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_eatc_pods_typolgy_a ) 
 (valor por defecto: " tipologa a de puntos de donacin ") 

 Selector de KPI 
 La interfaz presentar un selector de KPIs de resultados, que permitir al usuario elegir uno (entre los que a continuacin se relacionan) y poder visualizar el grfico de barras, con los datos del indicador seleccionado para cada una de las tipologas a de puntos de donacin de la cuenta en particular en el periodo seleccionado .  El label del indicador, estar acompaado tambin de un tooltip que desplegar la descripcin del mismo ( _desc ).  

 Existir un KPI por defecto , que ser el que se muestre cuando, se abra el informe y que ms adelante se especifica. Cuando se cambia a otro indicador, el grfico de tendencia variar segn la seleccin.  

 Grfico de barras por tipologa a de puntos de donacin 
 En las barras se podr observar el indicador para cada uno de las tipologas a de los puntos de donacin que la cuenta tiene registradas, para el periodo seleccionado. 

 A continuacin se presentarn los indicadores o KPIs de resultados que se desplegarn en el selector (y por ende, al presionarlo, en las grficas de barras). 

 Indicadores de ahorro 
 Estos indicadores son los mismos que se implementaron en Ahorro > Tablero > Ahorros detallados > KPIs Principales y por lo tanto se podr basar la implementacin en esa implementacin previa. 

 Ahorros tributarios totales => Se puede basar en la implementacin de BO => KPI por defecto 
 class=" lbl_ahorros_triburarios " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_triburarios ) 

 class=" lbl_ahorros_triburarios _desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_triburarios_desc ) 

 Corresponde a los ahorros que por efecto de impuesto a la renta e impuesto al valor agregado que se pueden obtener al tomar la decisin de donar en vez de botar (en el periodo de tiempo seleccionado). 

 Nota para la implementacin: corresponde a la sumatoria de los KPIs income_tax_savings y vat_savings 

 Ahorros logsticos totales ($)   
 class=" lbl_ahorros_logisticos_totales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_logisticos_totales ) 

 class=" lbl_ahorros_logisticos_totales_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_logisticos_totales_desc ) 

 Corresponde al total de ahorros por efecto de costos logsticos (que incluyen los ahorros en costos de almacenamiento, transporte y gestin de residuos) en el periodo de tiempo seleccionado (se calculan sobre los anuncios de donacin con estado "recibido", "pre-certificado" y "certificado"). 

 Nota para la implementacin: corresponde a la sumatoria de los KPI storage_cost_savings , transport_cost_savings y waste_management_savings 

 Ahorros en almacenamiento ($) => Se puede basar en la i mplementacin de BO   
 class=" lbl_ahorros_almacenamiento " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_almacenamiento ) 

 class=" lbl_ahorros_almacenamiento_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_almacenamiento_desc ) 

 Corresponde al clculo de los ahorros que por concepto de almacenamiento est logrando tu organizacin por tu decisin de donar en vez de botar (en el periodo de tiempo seleccionado: se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado"). 

 Nota para la implementacin: corresponde a la sumatoria del KPI storage_cost_savings 

 Ahorros en costos de transporte ($)=> Se puede basar en la implementacin de BO 
 class=" lbl_ahorros_transporte " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_transporte ) 

 class=" lbl_ahorros_transporte_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_transporte_desc ) 

 Corresponde al clculo de los ahorros que por concepto de transporte est logrando tu organizacin por tu decisin de donar en vez de botar (en el periodo de tiempo seleccionado: se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado"). 

 Nota para la implementacin: corresponde a la sumatoria del KPI transport_cost_savings 

 Ahorros en gestin de residuos ($)=>  Se puede basar en la implementacin de BO 
 class=" lbl_ahorros_gestion_residuos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos ) 

 class=" lbl_ahorros_gestion_residuos_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos_desc ) 

 Corresponde al clculo de ahorro en gestin y disposicin final de residuos que ests logrando por tomar la decisin de donar en vez de botar (en el periodo de tiempo seleccionado: se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado") 

 Nota para la implementacin: corresponde a la sumatoria del KPI waste_management_savings 

 A HORROS SEGN TIPOLOGA B 
 Se mostrarn en una franja horizontal en segundo lugar, los resultados por la tipologa b ( class=" lbl_eatc_pods_typolgy_b " ) de los puntos de donacin de la cuenta respectiva 

 La dinmica de presentacin es similar a la de los resultados por tipologa A (arriba descritos) , variando simplemente los ttulos y el criterio de agrupacin de la estadstica de barras (ahora ser la tipologa b de los puntos de donacin.  Los indicadores sern los mismos que los arriba documentados (por lo tanto no se vuelven a relacionar) 

 R ESULTADOS SEGN TIPOLOGA B DE PUNTOS DE DONACIN 

 La implementacin tiene la misma dinmica de la anteriormente documentada (selector de KPIs, Grfico de Barras por Tipologa A), por lo tanto solo haremos referencia la aquello que vara con respecto a la anterior implementacin 
 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
 class=" lbl_ahorros_segun " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_segun ) 
 Seguido de  
 class=" lbl_eatc_pods_typolgy_b " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_eatc_pods_typolgy_b ) 
 (valor por defecto: " tipologa b de puntos de donacin ") 

 A HORROS POR CIUDAD 
 En un grfico de torta (o circular) se debe mostrar el nmero de anuncios por ciudad para la cuenta en cuestin, presentando un listado accesorio, con datos que completen la informacin del grfico (sobre todo para donantes con muchas ciudades y dnde algunas de ellas tienen resultados poco significativos en el total).  

 Aquel grupo de ciudades que pesen en conjunto menos del 7% del total, se debern agrupar en la torta como "otras ciudades, tal como se ejemplifica en el siguiente grfico (para el caso de pases) 

 Ttulo de la seccin: Ahorros por ciudad 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 

 class=" lbl_ahorros_por_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_por_ciudad ) 

 Tabla de informacin por ciudad: 

 La tabla contendr la siguiente informacin. 

 Ciudad 
 class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ciudad ) 
 Muestra la ciudad sobre la cual se presentan estadsticas. 

 Ahorros totales (en el diseo: ahorro total) 
 class=" lbl_ahorros_totales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales ) 

 class=" lbl_ahorros_totales_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_desc ) 

 Corresponde a los ahorros totales para la ciudad en cuestin. 

 Ahorros tributarios (en el diseo: ahorro tributario) 
 class=" lbl_ahorros_tributarios " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_tributarios ) 

 class=" lbl_ahorros_tributarios _desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_triburarios_desc ) 

 Corresponde a los ahorros tributarios para la ciudad en cuestin. 

 Ahorros logsticos (en el diseo: Ahorros en gestin de residuos) 
 class=" lbl_ahorros_logisticos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_logisticos ) 

 class=" lbl_ahorros_gestion_residuos_desc " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos_desc ) 

 Corresponde a los ahorros logsticos para la ciudad en cuestin. 

 Tabla de informacin por ciudad: ordenamiento 
 La tabla debe permitir ordenar ascendente y descendentemente por todas sus columnas. 

 Tabla de informacin por ciudad: paginacin 
 La tabla debe mostrarse de manera paginada (de 7 en 7 resultados) 

 Tabla de informacin por ciudad: Filtros 
 Se proponen los siguientes filtros, los cuales deben irse implementando de manera paulatina 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 TABLERO > RESULTADOS AVANZADOS","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"Cuentas datagov","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":171}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-avanzados%2F2004360470-ahorro_tablero_resultados_avanzados.jpg&ow=1040&oh=811, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-resultados-avanzados%2F2004360470-ahorro_tablero_resultados_avanzados.jpg&ow=1040&oh=811 
 Cuentas datagov 

 420.000000000000 

 DATA ANALYTICS: AHORRO > TABLERO > RESULTADOS AVANZADOS