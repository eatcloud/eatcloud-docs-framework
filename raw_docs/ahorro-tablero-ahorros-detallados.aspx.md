# ahorro-tablero-ahorros-detallados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin:  
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Se puede basar en la implementacin:  
 Eficiencia > Tablero > Rendimiento 

 Mockup: 

 Ahorro  > Tableros > Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

 Label Ttulo de la Vista: Ahorros detallados 
 class=" lbl_ahorros_detallados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_ahorros_detallados ) 

 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto . El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer: en este caso no se genera grfico).  

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

 KPIs secundarios  

 Ahorros en impuesto de renta ($)  
 class=" lbl_ahorros_impo_renta " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta ) 

 class=" lbl_ahorros_impo_renta_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta_desc ) 

 Corresponde a los ahorros que por efecto de impuesto a la renta se pueden obtener al tomar la decisin de donar en vez de botar (en el periodo de tiempo seleccionado: se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado"). 

 Ahorros en IVA ($) 
 class=" lbl_ahorros_iva " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva ) 

 class=" lbl_ahorros_iva_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva_desc ) 

 Corresponde a los ahorros que por efecto de impuesto al valor agregado que se pueden obtener al tomar la decisin de donar en vez de botar (en el periodo de tiempo seleccionado: se calculan sobre los anuncios efectivamente entregados a los beneficiarios, es decir con estado "recibido", "pre-certificado" y "certificado"). 

 Ahorros en impuesto de renta ($) por donacin entregada (en el diseo: Ahorros en impuesto de renta ($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_impo_renta_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta_por_donacion ) 

 class=" lbl_ahorros_impo_renta_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_impo_renta_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros por efecto de impuesto a la renta sobre el nmero de anuncios de donacin efectivamente recibidos por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo el Ahorro en impuesto de renta (arriba calculado) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 Ahorros en IVA ($) por donacin entregada (en el diseo: Ahorros en IVA ($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_iva_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva_por_donacion ) 

 class=" lbl_ahorros_iva_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_iva_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros por efecto de impuesto al valor agregado sobre el nmero de anuncios de donaciones efectivamente recibidas por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo los Ahorros en IVA (arriba calculados) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 Ahorros en gestin de residuos ($) por donacin entregada (en el diseo: Ahorros gestion residuos($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_gestion_residuos_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos_por_donacion ) 

 class=" lbl_ahorros_gestion_residuos_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_gestion_residuos_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros por efecto de gestin de residuos sobre el nmero de anuncios de donacin efectivamente recibidas por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo los Ahorros en gestin de residuos (arriba calculados) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 Ahorros en costos de almacenamiento ($) por donacin entregada (en el diseo: Ahorros costos almacenamiento ($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_almacenamiento_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_costos_almacenamiento_por_donacion ) 

 class=" lbl_ahorros_almacenamiento_por_donacion_desc " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_almacenamiento_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros por efecto de costos de almacenamiento sobre el nmero de anuncios efectivamente recibidos por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo los Ahorros en costo de almacenamiento (arriba calculados) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 Ahorros en costos logsticos ($) por donacin entregada (en el diseo: Ahorros costos logsticos ($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_logisticos_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_logisticos_por_donacion ) 

 class=" lbl_ahorros_logisticos_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_logisticos_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros por efecto de costos logsticos (que incluyen los ahorros en costos de almacenamiento, transporte y gestin de residuos) sobre el nmero de anuncios de donacin. efectivamente recibidos por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo los Ahorros en logsticos totales (arriba calculados) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 Ahorros totales ($) por donacin entregada (en el diseo: Ahorros Totales ($) / Anuncios entregados: que es ms bien la frmula para el clculo no el nombre del KPI) 
 class=" lbl_ahorros_totales_por_donacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_donacion ) 

 class=" lbl_ahorros_totales_por_donacion_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_ahorros_totales_por_donacion_desc ) 

 Corresponde a la divisin del valor de los ahorros totales sobre el nmero de anuncios de donacin. efectivamente recibidos por los beneficiarios (es decir con estado "recibido", "pre-certificado" y "certificado") en el periodo de tiempo seleccionado. 

 Nota para la implementacin:   Se puede calcular dividiendo los Ahorros totales (anteriormente calculados) sobre: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{fecha_inicio_periodo}}&eatc-publication_date[1]={{fecha_fin_periodo}}&eatc-donor={{_DOM. cua_user }}&eatc-state= received,pre-certified,certified &_cont 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 TABLERO > AHORROS DETALLADOS","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"Cuentas datagov","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":171}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-ahorros-detallados%2F599196997-ahorro_tablero_ahorros_detallados.jpg&ow=945&oh=768, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fahorro-tablero-ahorros-detallados%2F599196997-ahorro_tablero_ahorros_detallados.jpg&ow=945&oh=768 
 Cuentas datagov 

 416.000000000000 

 DATA ANALYTICS: AHORRO > TABLERO > AHORROS DETALLADOS