# cancelaciones-detalle-de-anuncios-cancelados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Detalle de anuncios cancelados 

 ***NUEVO : Filtro (a quienes se le muestra el informe y todos sus indicadores): *** 

 A los usuarios tipo  eatc_cua_master 

 Ttulo del informe 
 Label: class=" lbl_det_dona_cancelados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_det_dona_cancelados )  

 F ILTRO PRINCIPAL DEL INFORME 

 El sistema deber presentar un filtro principal, que al seleccionarlo deber desplegar un filtro secundario (cuya opcin por defecto ser "Todas / Todos") que principalmente operar para mostrar o no la grfica (la grfica solo se mostrar en la opcin por defecto "todas / todos") y para filtrar la tabla abajo dispuesta: 

 Cancelados por donante: 

 Label del selector 
 Label: class=" lbl_cancelados_por_donante " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cancelados_por_donante )   

 Men secundario: valor por defecto: Todos: 
 Label: class=" lbl_todos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_todos )   

 Men secundario: otros valores del selector: 
 Partiendo del selector de fechas principal del informe, el sistema realizar la siguiente consulta para determinar los valores a mostrar: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled &_distinct= eatc-donor 

 Cancelados por ciudad: 

 Label del selector 
 Label: class=" lbl_cancelados_por_ciudad " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cancelados_por_ciudad)  

 Men secundario: valor por defecto: Todas: 
 Label: class=" lbl_todas " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_todas )   

 Men secundario: otros valores del selector: 
 Partiendo del selector de fechas principal del informe, el sistema realizar la siguiente consulta para determinar los valores a mostrar: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled &_distinct= eatc-city 

 Al realizar una seleccin el sistema deber obtener el respectivo eatc_dona_headers. eatc-province para realizar posteriores consultas. 

 NO VA: Cancelados por tipo de beneficiario (dadas las caractersticas de los anuncios cancelados no va): 

 Label del selector 
 Label: class=" lbl_cancelados_por_tipo_beneficiario " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cancelados_por_tipo_beneficiario)  

 Men secundario: valor por defecto: Todos: 
 Label: class=" lbl_todos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_todos ) 

 Men secundario: otros valores del selector: 
 El  los selectores del filtro se arman de acuerdo a la tipologa b de las instituciones que se obtiene de la siguiente consulta: 
 {{ URL_entorno_beneficiarios }}/api/{{_DOM. cua_master }}/ eatc_doma_typology_b ?_id=_*&_distinct= eatc_name 

 Al seleccionar una opcin se debe obtener el " eatc_doma_typology_b. eatc_code " respectivo: 
 {{ URL_entorno_beneficiarios }}/api/{{_DOM. cua_master }}/ eatc_doma_typology_b ?eatc_name={{ opcion_seleccionada }}&_distinct= eatc_code 

 Para el caso de la opcin " Todos " el parmetro de consulta ser " _* " 

 GRFICO TOP 10 

 En un grfico de barras horizontales (en el diseo las barras son verticales), se presentarn los 10 primeros resultados para las mtricas " Anuncios Cancelados " y " % anuncios cancelados ".  (Grficas independientes por las diferencias de magnitud), segn la opcin seleccionada en el selector anterior, con la opcin "Todos / todas" como seleccin en el submen (que es su valor por defecto), de la siguiente manera: 

 Por donante 
 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled & eatc-donation_manager_code={{ eatc_dona_headers. eatc-donation_manager_code}}&_cont 

 Por donante 
 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled & eatc-city={{ eatc_dona_headers. eatc-city}} & eatc-province={{ eatc_dona_headers. eatc-province}}&_cont 

 LISTADO CANCELADOS 
 El sistema deber presentar una tabla, paginada, descargable, filtrable y ordenable por columnas (datatable) que contenga la siguiente informacin). 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled & eatc-city={{ eatc_dona_headers. eatc-city}} & eatc-province={{ eatc_dona_headers. eatc-province}}&eatc-donor={{ eatc_dona_headers. eatc-donor}}&_cmp=eatc-city,eatc-province,eatc-donor,eatc-total_weight_kg,eatc-total_cost 

 Ciudad (no est en el diseo ) 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Corresponde a  
 eatc_dona_headers. eatc-city 

 La respectiva ciudad (que corresponde a la dupla {{ciudad}} / {{departamento}} ) se presentar como un vnculo que dar acceso al detalle de cancelados por ciudad , que se documentar ms adelante. 

 Departamento (no est en el diseo propuesto ) 
 Label: class=" lbl_departamento_provincia_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_departamento_provincia_estado ) 

 Corresponde a  
 eatc_dona_headers. eatc-province 

 Donante ( en el diseo est como primera columna) 
 class=" lbl_donante ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donante         

 Corresponde a : 
 eatc_dona_headers. eatc-donor 

 Anuncios cancelados 
 class=" lbl_anuncios_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados   

 Corresponde al 
 count de la consulta respectiva 

 KG cancelados 
 class=" lbl_kg_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados    

 Corresponde a la 
 sumatoria de los datos obtenidos en el parmetro eatc_dona_headers. eatc-total_weight_kg 

 Pesos ($) cancelados 
 class=" lbl_pesos ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pesos   

 concatenado con: 

 class=" lbl_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_cancelados    

 Corresponde a la 
 sumatoria de los datos obtenidos en el parmetro eatc_dona_headers. eatc-total_cost 

 D ETALLE DE CANCELADOS POR CIUDAD 

 Label del informe (en el diseo est diferente) 
 Label: class=" lbl_detalle_cancelados_por_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_detalle_cancelados_por_ciudad )    

 El sistema deber presentar una tabla, paginada, descargable, filtrable y ordenable por columnas (datatable) que contenga la siguiente informacin). 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled & eatc-city= {{ciudad}} & eatc-province= / {{departamento}} &eatc-donor={{ eatc_dona_headers. eatc-donor}}&_distinct=eatc-pod_id 

 Por cada Punto de donacin que traiga la consulta el sistema deber realizar la siguiente consulta para construir los registros de la siguiente tabla 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-state= cancelled & eatc-city= {{ciudad}} & eatc-province= / {{departamento}} &eatc-donor={{ eatc_dona_headers. eatc-donor}}&eatc-pod_id= {{eatc-pod_id}} &_cmp=eatc-pod_id,eatc-pod_name,eatc-total_weight_kg,eatc-total_cost 

 Ciudad ( en el diseo est como segunda columna) 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Corresponde a  
 eatc_dona_headers. eatc-city 

 La respectiva ciudad (que corresponde a la dupla {{ciudad}} / {{departamento}} ) se presentar como un vnculo que dar acceso al detalle de cancelados por ciudad , que se documentar ms adelante. 

 Donante (no est en el diseo propuesto ) 
 class=" lbl_donante ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donante         

 Corresponde a : 
 eatc_dona_headers. eatc-donor 

 POD id 
 class=" lbl_pod_id ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pod_id        

 Corresponde a : 
 eatc_dona_headers. eatc-pod_id 

 POD id 
 class=" lbl_nombre_pod ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_nombre_pod       

 Corresponde a : 
 eatc_dona_headers. eatc-pod_name 
 Anuncios cancelados 
 class=" lbl_anuncios_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_anuncios_cancelados   

 Corresponde al 
 count de la consulta respectiva 

 KG cancelados 
 class=" lbl_kg_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_kg_cancelados    

 Corresponde a la 
 sumatoria de los datos obtenidos en el parmetro eatc_dona_headers. eatc-total_weight_kg 

 Pesos ($) cancelados 
 class=" lbl_pesos ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pesos   

 concatenado con: 
 class=" lbl_cancelados ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_cancelados    

 Corresponde a la 
 sumatoria de los datos obtenidos en el parmetro eatc_dona_headers. eatc-total_cost 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 DETALLE DE ANUNCIOS CANCELADOS","textAlignment":"Center","showPublishDate":false,"authors":[],"showTopicHeader":true,"authorByline":[],"layoutType":"NoImage","topicHeader":"Nuevo BO CUA MASTER Beneficiarios","enableGradientEffect":true,"isDecorative":true},"containsDynamicDataSource":false,"reservedHeight":171}"> 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaciones-detalle-de-anuncios-cancelados%2F1105488461-cancelaciones_detalle.jpg&ow=675&oh=749, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaciones-detalle-de-anuncios-cancelados%2F1105488461-cancelaciones_detalle.jpg&ow=675&oh=749 
 Nuevo BO CUA MASTER Beneficiarios 

 691.000000000000 

 CANCELACIONES > DETALLE DE ANUNCIOS CANCELADOS