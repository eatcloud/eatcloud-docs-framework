# cancelaciones-generalidades.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Generalidades (en el diseo: " Cancelaciones ") 

 Ttulo del informe 
 Label: class=" lbl_generalidades " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_generalidades )  

 KPIS PRINCIPALES 

 Anuncios cancelados 
 class=" lbl_anuncios_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados 

 Tooltip: 
 class=" lbl_anuncios_cancelados_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados_desc      

 " Cantidad de anuncios cancelados en el periodo seleccionado " 

 Llamado para el clculo: 
 El sistema debe realizar el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled &_cont 

 Se toma el valor que la respuesta da en " count ".  La respuesta se lleva a la variable {{ anuncios_cancelados }} para posteriores clculos. 

 Ejemplo: entorno productivo , abaco : 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-02-28&eatc-publication_date[1]=2022-03-28&eatc-state= cancelled &_cont   

 Anuncios cancelados por da 
 class=" lbl_anuncios_cancelados_por_dia ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados_por_dia    

 Tooltip: 
 class=" lbl_anuncios_cancelados_por_dia_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados_por_dia_desc     

 " Promedio diario de los anuncios cancelados en el periodo seleccionado " 

 Llamado para el clculo: 
 El sistema calcula el nmero de das que se tiene en el periodo seleccionado y realiza la siguiente operacin 
{{ anuncios_cancelados_por_dia }} = {{ anuncios_cancelados }} / {{ dias_en_el_periodo }} 

 % de anuncios cancelados 
 class=" lbl_pct_anuncios_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_anuncios_cancelados   

 Tooltip: 
 class=" lbl_pct_anuncios_cancelados_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_anuncios_cancelados_desc   

 " Corresponde a la divisin del nmero de anuncios efectivamente cancelados (es decir, con estado "cancelado") sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. " 

 Llamado para el clculo: 
 El sistema debe realizar el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= _* &_cont 

 Se toma el valor que la respuesta da en " count " como {{ anuncios_del_periodo }} .   

 Ejemplo: entorno productivo , abaco : 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-02-28&eatc-publication_date[1]=2022-03-28&eatc-state= _* &_cont    

 Con este valor y los anteriormente calculados se realiza la siguiente operacin 

{{ porcentaje_anuncios_cancelados }}=({{ anuncios_cancelados }}/{ anuncios_del_periodo }})*100 

 ***NUEVO: NUEVO: ESTADSTICAS EN KG *** 
 Debajo de la actual franja de estadsticas en nmero de donaciones, se agregar la misma estadstica pero en KG, de la siguiente maneta 

 KG cancelados 
 class=" lbl_kg_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados   

 Tooltip: 
 class=" lbl_kg_cancelados_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados_desc      

 "Sumatoria de los KG de lo anuncios que han sido cancelados por el sistema (por superar el tiempo de vida til del anuncio) " => LABEL CREADO PERO NO EN LA PLATAFORMA BENEFICIARIOS: HACER LA CREACIN 

 Llamado para el clculo: 
 El sistema debe realizar el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled &_cmp= eatc-original_weight_kg  

 El sistema realiza la sumatoria de los KG obtenidos.  La respuesta se lleva a la variable {{ kg_cancelados }} para posteriores clculos. 

 Ejemplo: entorno productivo , abaco : 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-02-28&eatc-publication_date[1]=2022-03-28&eatc-state= cancelled &_cmp= eatc-original_weight_kg   

 KG cancelados por da 
 class=" lbl_kg_cancelados_por_dia ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados_por_dia     

 Tooltip: 
 class=" lbl_kg_cancelados_por_dia_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados_por_dia_desc      

 " Promedio diario de KG de los anuncios cancelados en el periodo seleccionado " 

 Llamado para el clculo: 

 El sistema calcula el nmero de das que se tiene en el periodo seleccionado y realiza la siguiente operacin 

{{ kg_cancelados_por_dia }} = {{ kg_cancelados }} / {{ dias_en_el_periodo }} 

 % de KG cancelados 
 class=" lbl_pct_kg_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_kg_cancelados => LABEL CREADO PERO NO EN LA PLATAFORMA BENEFICIARIOS: HACER LA CREACIN 

 Tooltip: 
 class=" lbl_pct_kg_cancelados_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_kg_cancelados_desc   

 " Corresponde a la divisin el peso en KG de los anuncios efectivamente cancelados (es decir, con estado "cancelado") sobre el peso total de anuncios (todos los anuncios) generados en el periodo. " => LABEL CREADO PERO NO EN LA PLATAFORMA BENEFICIARIOS: HACER LA CREACIN 

 Llamado para el clculo: 
 El sistema debe realizar el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= _* &_cmp= eatc-total_weight_kg  

 Se toma el valor que la respuesta da en " count " como {{ kg_del_periodo }} .   

 Ejemplo: entorno productivo , abaco : 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-02-28&eatc-publication_date[1]=2022-03-28&eatc-state= _* &_cmp= eatc-total_weight_kg   

 Con este valor y los anteriormente calculados se realiza la siguiente operacin 

{{ porcentaje_kg_cancelados }}=({{ kg_cancelados }}/{ kg_del_periodo }})*100 

 G RFICA DE TENDENCIA DE KPIS PRINCIPALES 

 Tal cmo se implement en Datagov Cuentas > Analytics, el sistema deber presentar un grfico de tendencia del KPI seleccionado (siendo la seleccin por defecto " Anuncios Cancelados "), para mostrar la progresin semanal del mismo.  Se pueden utilizar el mismo tipo de grficas utilizados en Analytics, con el nimo de reciclar cdigo y agilizar la implementacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 GENERALIDADES","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"Nuevo BO CUA MASTER Beneficiarios","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":171}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaciones-generalidades%2F527994691-cancelaciones_1--1-.jpg&ow=778&oh=654, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaciones-generalidades%2F527994691-cancelaciones_1--1-.jpg&ow=778&oh=654 
 Nuevo BO CUA MASTER Beneficiarios 

 687.000000000000 

 CANCELACIONES > GENERALIDADES