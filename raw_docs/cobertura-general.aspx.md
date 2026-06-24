# cobertura-general.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cobertura general 

 Ttulo del informe 
 Label: class=" lbl_cober_gnrl " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cober_gnrl )  

 KPIS PRINCIPALES 

 % de cobertura global 
 class=" lbl_pct_cobertura_global ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_cobertura_global   

 Tooltip: 
 class=" lbl_pct_cobertura_global_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pct_cobertura_global_desc      

 "Sumatoria de departamentos con acceso a donaciones en el periodo seleccionado, sobre el total de departamentos en el pas" 

 Llamado para el clculo: 
 Para obtener el numerador del indicador se realiza el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&_distinct=eatc-province 

 Se toma el " cont " de la respuesta obtenida en la variable {{ numero_dptos_cubiertos }} 

 Para obtener el denominador del indicador primero se establece el pas de la cuenta maestra con el siguiente llamado 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua_master?eatc_cua={{_DOM. cua_master }}&_cmp= eatc_country 

 Con el dato {{eatc_cua. eatc_country }} obtenido se procede a realizar la siguiente consulta: 

 {{ URL_entorno_datagov }}/api/{{eatc_cua. eatc_country }}/eatc_municipalities?_id=_*&_distinct= eatc-province 

 Se toma el " cont " de la respuesta obtenida en la variable {{ numero_total_dptos }} 

 El porcentaje corresponder al siguiente clculo: 

 pct_cobertura_global = ({{ numero_dptos_cubiertos }}/{{ numero_total_dptos }})*100 

 % DE COBERTURA POR DEPARTAMENTO 
 Label: class=" lbl_pct_cobertura_por " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_pct_cobertura_por )  

 Concatenado con: 

 Label: class=" lbl_departamento_provincia_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_departamento_provincia_estado ) 

 Tooltip: class=" lbl_pct_cobertura_por_depto_desc " "Ciudades con donaciones en el periodo seleccionado, sobre el total de ciudades" ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_pct_cobertura_por )  

 A diferencia del mockup, debe ser un grfico de barras horizontales, ordenado de mayor a menor (primero los departamentos con mayor porcentaje de cobertura), en donde se muestre el porcentaje de cobertura de cada departamento (en el periodo en cuestin) 

 Llamado para el clculo: 
 Se obtienen los departamentos con cobertura en el periodo, utilizando siguiente llamado (el resto de los departamentos tendrn cobertura igual a cero): 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&_distinct=eatc-province 

 Para cada departamento con cobertura en el periodo se determina el nmero de municipalidades con cobertura: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{eatc_dona_headers. eatc-province }}&_distinct= eatc-city 

 Se toma el " cont " de la respuesta para cada departamento en la variable {{ numero_ciudades_cubiertas_por_depto }} 

 Para obtener el denominador del indicador primero se establece el pas de la cuenta maestra con el siguiente llamado 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua_master?eatc_cua={{_DOM. cua_master }}&_cmp= eatc_country 

 Con el dato {{eatc_cua. eatc_country }} obtenido se procede a realizar la siguiente consulta: 

 {{ URL_entorno_datagov }}/api/{{eatc_cua. eatc_country }}/eatc_municipalities? eatc-province = {{eatc_dona_headers. eatc-province }} &_distinct= eatc-city 

 Se toma el " cont " de la respuesta obtenida en la variable {{ numero_total_ciudades_por_dpto }} 

 El porcentaje corresponder al siguiente clculo: 

 pct_cobertura_por_depto = ({{ numero_ciudades_cubiertas_por_depto }} / {{ numero_total_ciudades_por_dpto }}) * 100 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-general%2F4030714960-cobertura_general.jpg&ow=548&oh=487, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-general%2F4030714960-cobertura_general.jpg&ow=548&oh=487 
 Nuevo BO CUA MASTER Beneficiarios 

 705.000000000000 

 COBERTURA GENERAL