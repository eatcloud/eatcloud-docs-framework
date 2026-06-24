# dashboard-principal.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El dashboard principal presentar estadsticas bsicas de la gestin en un territorio.  A continuacin se presentan las imgenes del diseo inicial del informe, que debern servir de gua para la construccin del BO. 

Filtro de fechas 
Fecha inicial 
 id=" lbl_fecha_inicial " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_fecha_inicial) 

 Valor por defecto: el mismo da del mes, tres meses ms atrs. 
 Valor ms antiguo permitido (inicialmente): fecha actual del ao anterior (o fecha un ao atrs contada a partir de la fecha final seleccionada). 

 El valor seleccionado se llevar a la variable {{fecha_inicial}} 

Fecha final 
 id=" lbl_fecha_final " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_fecha_final ) 

 Valor por defecto: da actual. 

 El valor seleccionado se llevar a la variable {{fecha_final}} 

Cargar nueva Info => Consultar => SE DEBE EVALUAR SI ESTO ES NECESARIO O SE PUEDE OBVIAR (que simplemente cuando se terminen de seleccionar las fechas se lance el prximo selector) 

 clase=" lbl_consultar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_consultar ) 

La informacin que se visualiza corresponde a los datos en el rango de fechas seleccionado arriba 
 clase=" lbl_info_rango_fechas " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_info_rango_fechas ) 

 Indicadores ambientales y sociales 
 class=" lbl_ind_amb_soc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_ind_amb_soc )  

Kilogramos Rescatados 
 class=" lbl_kg_rescatados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_rescatados )  

 Tooltip: class=" lbl_kg_rescatados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_rescatados_desc )  
KG que fueron efectivamente despachados (cuyo estado es  "despachado", "recibido", "pre-certificado" y "certificado") en el periodo en cuestin. 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city= {{eatc_city}} &eatc-province= {{eatc_province}} &eatc-state= delivered , received,pre-certified,certified &_sum=eatc-total_weight_kg  

Nmero de organizaciones beneficiadas (en el diseo: Instituciones beneficiadas) 
 class=" lbl_organizaciones_beneficiadas " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_organizaciones_beneficiadas ) 

 Tooltip: class=" lbl_organizaciones_beneficiadas_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_organizaciones_beneficiadas_desc ) 
Corresponde a la cantidad de organizaciones sociales que se le han despachado por lo menos una donacin en el periodo en cuestin 

Llamado para el clculo del indicador 
 cont de {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city={{eatc_city}}&eatc-province={{eatc_province}}&eatc-state= delivered , received,pre-certified,certified &_distinct=eatc-donation_manager_code 

Unidades despachadas (en el diseo: productos recibidos) 
 class=" lbl_und_despachadas " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_und_despachadas )  

 Tooltip: class=" lbl_und_despachadas_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_und_despachadas_desc )  
Total de unidades de producto despachadas a los beneficiarios en el periodo. 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city= {{eatc_city}} &eatc-province= {{eatc_province}} &eatc-state= delivered , received,pre-certified,certified &_sum=eatc_dona_units  

KG Cancelados (en el diseo: Kilogramos Cancelados) 
 clase=" lbl_kg_cancelados ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_cancelados )  

 Tooltip: clase=" lbl_kg_cancelados_desc 2 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_cancelados_desc2 )   
Peso expresado en KG de los anuncios que fueron cancelados por la plataforma (por haber finalizado su periodo de vigencia) en las fechas seleccionadas. 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city={{eatc_city}}&eatc-province={{eatc_province}}&eatc-state= cancelled &_sum=eatc-original_weight_kg  

KG pendientes por verificar (no est en el diseo) 
 class=" lbl_kg_pend_verf " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_pend_verf )  

 Tooltip: class=" lbl_kg_pend_verf_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_pend_verf_desc )   
Kilogramos que aun estn en proceso de verificacin por los miembros del ecosistema. 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city= {{eatc_city}} &eatc-province= {{eatc_province}} &eatc-state= delivered &_sum=eatc-total_weight_kg  

Platos servidos (en el diseo: Platos de alimentos) 
 class=" lbl_platos_servidos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_platos_servidos ) 

 Tooltip: class=" lbl_platos_servidos_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_platos_servidos_desc ) 
Corresponde a la sumatoria del total de porciones servidas a partir de las donaciones entregadas (con verificacin del cdigo de recogida y verificacin detallada de la donacin por por parte de los beneficiarios), en el periodo seleccionado.  

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_kpi?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]= {{fecha_final}} &eatc-city={{eatc_city}}&eatc-province={{eatc_province}}&kpi=total_portions&_sum=value 

KG de CO2 ahorrados (en el diseo: KG de CO2 Mitigados) 
 class=" lbl_kg_CO2_ahorrados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_CO2_ahorrados ) 

 Tooltip: class=" lbl_kg_CO2_ahorrados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_CO2_ahorrados_desc ) 
Corresponde a la cantidad de KG de CO2 que le ests ahorrando al planeta por tu decisin de donar en vez de botar, en el periodo establecido (para anuncios cuyo estado es "recibido", "pre-certificado" y "certificado").  

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_kpi?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]= {{fecha_final}} &eatc-city={{eatc_city}}&eatc-province={{eatc_province}}&kpi=CO2_tons&_sum=value 
El resultado se multiplica por 1000 (para convertir toneladas en KG)

% de aprovechamiento en KG  (en el diseo: % Aprovechamiento) 
 class=" lbl_pct_aprovechamiento_kg " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_pct_aprovechamiento_kg )  

 Tooltip: class=" lbl_pct_aprovechamiento_kg_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_pct_aprovechamiento_kg_desc )   
Sumatoria de los kilogramos efectivamente recibidos por el beneficiario sobre la sumatoria de  KG originalmente reportados en los anuncios como donaciones (para anuncios  de donacin con estado "recibido". "pre-certificado" y "certificado"), multiplicada por 100. 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city={{eatc_city}}&eatc-province={{eatc_province}}&eatc-state= received,pre-certified,certified &_sum=eatc-total_weight_kg,eatc-original_weight_kg  

{{KG_efectivamente_recibidos}} = {{eatc_dona_headers. eatc-total_weight_kg }}  
{{KG_originales}} = {{eatc_dona_headers. eatc-original_weight_kg }}  

 INDICADOR A MOSTRAR: {{KG_efectivamente_recibidos}} / {{KG_originales}} *100 

 Impacto de las alianzas 
 class=" lbl_impacto_alianzas " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_impacto_alianzas )  

Con los datos que llegan en el perfil ( {{eatc_city}}, {{eatc_province}} , {{cua_master}} ) el sistema realiza la siguiente consulta: 
{{URL_datagov}}/api/eatcloud/eatc_special_projects?eatc_cua_master= {{cua_master}} &eatc_province= {{eatc_province}} &eatc-city= {{eatc_city}} &_cmp=eatc_name,eatc_initial_date,eatc_code 

KG Rescatados Adicionales 
 class=" lbl_kg_rescatados_adicionales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_rescatados_adicionales )  

 Tooltip: class=" lbl_kg_rescatados_adicionales_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_kg_rescatados_adicionales_desc )  
KG rescatados gracias al ingreso de nuevos aliados 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city= {{eatc_city}} &eatc-province= {{eatc_province}} &eatc-state= delivered , received,pre-certified,certified &eatc_special_project={{eatc_special_projects. eatc_code }}&_sum=eatc-total_weight_kg  

Donaciones despachadas adicionales 
 class=" lbl_dona_desp_adicionales " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_dona_desp_adicionales )  

 Tooltip: class=" lbl_dona_adicionales_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_dona_desp_adicionales_desc )  
Donaciones despachadas gracias al ingreso de nuevos aliados 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]= {{fecha_inicial}} &eatc-publication_date[1]={ {{fecha_final}} &eatc-city= {{eatc_city}} &eatc-province= {{eatc_province}} &eatc-state= delivered , received,pre-certified,certified &eatc_special_project={{eatc_special_projects. eatc_code }}&_count 

Puntos de donacin dados de alta 
 class=" lbl_pods_dados_de_alta " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_pods_dados_de_alta )  

 Tooltip: class=" lbl_pods_dados_de_alta_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_pods_dados_de_alta_desc )  
Nuevos puntos de donacin incorporados a la plataforma gracias a las alianzas 

Llamado para el clculo del indicador 
{{URL_entorno_donantes}}/api/allpods/eatc_pods?eatc_special_projecteatc_special_project={{eatc_special_projects. eatc_code }}&_count 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal%2F1643144772-KPIs1.jpg&ow=1216&oh=694, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal%2F1643144772-KPIs1.jpg&ow=1216&oh=694 

 901.000000000000 

 DASHBOARD PRINCIPAL