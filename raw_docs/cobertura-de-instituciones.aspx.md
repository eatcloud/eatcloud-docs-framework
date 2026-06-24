# cobertura-de-instituciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cobertura de instituciones 

 Ttulo del informe 
 Label: class=" lbl_cober_inst " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cober_inst )  

 Filtro principal del informe 
 El informe de deber filtrar por los diferentes parmetros de la tabla (datatable). 

 Departamento 
 Label: class=" lbl_departamento_provincia_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_departamento_provincia_estado ) 

 Se obtienen los departamentos con cobertura en el periodo, utilizando siguiente llamado (el resto de los departamentos tendrn cobertura igual a cero): 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&_distinct=eatc-province 

 Por cada departamento encontrado {{ DEPARTAMENTO }}, se debe establecer las respectivas ciudades que debern aparecer pareadas en la siguiente columna. 

 Ciudad 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Por cada departamento encontrado {{ DEPARTAMENTO }}, el sistema debe realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&_distinct= eatc-city 

 Cada ciudad encontrada y pareada con su respectivo departamento se deber guardar en la variable  {{ CIUDAD }}para las dems consultas. 

 Donantes 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Por cada dupla de {{ DEPARTAMENTO }}, {{ CIUDAD }} el sistema debe realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&_distinct= eatc-donor 

 Se toma el " cont " de la respuesta para cada departamento - ciudad en la variable {{ donantes_por_depto_ciudad }} 

 # Donaciones 
 Label: class=" lbl_numero_donaciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_numero_donaciones )  

 Por cada dupla de {{ DEPARTAMENTO }}, {{ CIUDAD }} el sistema debe realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&_cont 

 Se toma el " count " de la respuesta para cada departamento - ciudad en la variable {{ donaciones_por_depto_ciudad }} 

 Instituciones 
 Label: class=" lbl_instituciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_instituciones )   

 Por cada dupla de {{ DEPARTAMENTO }}, {{ CIUDAD }} el sistema debe realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}& eatc-donation_manager_code= _novacio &_distinct= eatc-donation_manager_code 

 Se toma el " count " de la respuesta para cada departamento- ciudad (descartando los datos vacos, o nulos) en la variable {{ instituciones_por_depto_ciudad }} 

 % Cobertura instituciones 
 Label: class=" lbl_pct_cobertura_instituciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_pct_cobertura_instituciones )   

 Por cada dupla de {{ DEPARTAMENTO }}, {{ CIUDAD }} el sistema debe realizar el siguiente clculo: 

 pct_cobertura_instituciones = ( {{ instituciones_por_depto_ciudad }} / {{ donantes_por_depto_ciudad }})*100 

 C OBERTURA ESPECFICA DE INSTITUCIONES 
 Label: class=" lbl_cober_espc_inst " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cober_espc_inst )  

 Listado filtrable, ordenable por columna y con facilidad de bsqueda (datatable) 

 Consultas para la creacin del informe: 
 Se determinan los departamentos 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&_distinct=eatc-province 

 Por cada departamento encontrado {{ DEPARTAMENTO }}, se debe establecer las respectivas ciudades. 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&_distinct= eatc-city 

 Cada ciudad encontrada y pareada con su respectivo departamento se deber guardar en la variable  {{ CIUDAD }} y con ella se deben establecer las diversas instituciones 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&_distinct=eatc-donation_manager_code 

 Para cada institucin encontrada se realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_cmp=eatc-province,eatc-city,eatc-donation_manager_code,eatc-donation_manager_name 

 NIT   
 class=" lbl_identificacion_tributaria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_identificacion_tributaria     

 Corresponde a  
 eatc_dona_headers. eatc-donation_manager_code 

 Institucin beneficiaria   
 class=" lbl_institucion_beneficiaria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_institucion_beneficiaria     

 Corresponde a  
 eatc_dona_headers. eatc-donation_manager_name 

 Departamento 
 Label: class=" lbl_departamento_provincia_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_departamento_provincia_estado ) 

 Corresponde a  
 eatc_dona_headers. eatc-province 

 Ciudad 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Corresponde a  
 eatc_dona_headers. eatc-province 

 Donantes 
 class=" lbl_donantes ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donantes        

 Para cada tripleta de informacin  {{ DEPARTAMENTO }}-{{ CIUDAD }}-{{eatc_dona_headers. eatc-donation_manager_code }} el sistema  realiza la siguiente consulta: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_distinct= eatc-donor_fiscal_name 

 Se toma el " cont " de la respuesta obtenida en la variable {{donantes}} 

 # Donaciones 
 Label: class=" lbl_numero_donaciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_numero_donaciones )  

 Para cada tripleta de informacin  {{ DEPARTAMENTO }}-{{ CIUDAD }}-{{eatc_dona_headers. eatc-donation_manager_code }} el sistema  realiza la siguiente consulta: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_cont 

 Se toma el " count " de la respuesta para cada departamento - ciudad - institucin en la variable {{ donaciones_por_depto_ciudad_institucion }} 

 % Cobertura instituciones 
 Label: class=" lbl_pct_cobertura_instituciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_pct_cobertura_instituciones )   

 # donaciones con match a una institucin especfica del periodo (se documenta con el API aunque para el caso particular no funciona): 

 {{ URL_entorno_beneficiarios }}/api/abaco/eatc_match_registry?fecha_corta[0]={{ fecha_inicial_periodo }}&fecha_corta[1]={{ fecha_final_periodo }}&departamento={{ DEPARTAMENTO }}&municipio={{ CIUDAD }}& donor= &eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_cont 

 # Total de donaciones anunciadas en ese periodo de tiempo y ciudad: 
 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&_cont 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-de-instituciones%2F174712385-cobertura_instituciones2.jpg&ow=492&oh=527, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-de-instituciones%2F174712385-cobertura_instituciones2.jpg&ow=492&oh=527 
 Nuevo BO CUA MASTER Beneficiarios 

 709.000000000000 

 COBERTURA DE INSTITUCIONES