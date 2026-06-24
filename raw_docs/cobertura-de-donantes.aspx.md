# cobertura-de-donantes.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cobertura de donantes 

 Ttulo del informe 
 Label: class=" lbl_cober_donan " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_cober_donan ) 

 T ABLA DE RESULTADOS POR CIUDAD / DEPARTAMENTO 
 Se deber implementar una tabla paginada, que permita ordenar por los diferentes campos, que tenga filtros (datatable), que se pueda descargar y que contenga la siguiente informacin por la dupla "departamento - ciudad" 

 Consultas para la creacin del informe: 
 Se determinan los departamentos 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&_distinct=eatc-province 

 Por cada departamento encontrado {{ DEPARTAMENTO }}, se debe establecer las respectivas ciudades. 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&_distinct= eatc-city 

 Cada ciudad encontrada y pareada con su respectivo departamento se deber guardar en la variable  {{ CIUDAD }} y con ella se deben establecer los diversos donantes 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&_distinct= eatc-donor 

 Cada donante encontrado y pareada con su respectivo departamento y ciudad se deber guardar en la variable  {{ DONANTE }} y con ella se deben establecer los diversos donantes 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}& eatc-donor= {{ DONANTE }} & _distinct= eatc-donation_manager_code 

 Para cada dupla de donante y beneficiario se realiza la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}& eatc-donor ={{ DONANTE }}& eatc-donation_manager_code= {{eatc_dona_headers. eatc-donation_manager_code }}&_cmp= eatc-donor , eatc-donor_fiscal_name, eatc-province,eatc-city, eatc-donation_manager_code,eatc-donation_manager_name 

 Donante 
 class=" lbl_donante ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donante         

 Corresponde a : 
 eatc_dona_headers. eatc-donor 
 eatc_dona_headers. eatc-donor_fiscal_name 

 Se toma el " cont " de la respuesta obtenida en la variable {{donantes}} 

 Departamento 
 Label: class=" lbl_departamento_provincia_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_departamento_provincia_estado ) 

 Corresponde a  
 eatc_dona_headers. eatc-province 

 Ciudad 
 Label: class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_ciudad ) 

 Corresponde a  
 eatc_dona_headers. eatc-province 

 Institucin beneficiaria ( en el diseo est como "Instituciones beneficiarias", en plural y debe ir en singular) 
 class=" lbl_institucion_beneficiaria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_institucion_beneficiaria   

 Corresponde a  
 eatc_dona_headers. eatc-donation_manager_name 

 # Donaciones 
 Label: class=" lbl_numero_donaciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_numero_donaciones )  

 Para cada cuarteta de informacin  {{ DEPARTAMENTO }}-{{ CIUDAD }}-{{ DONANTE }}-{{eatc_dona_headers. eatc-donation_manager_code }} el sistema  realiza la siguiente consulta: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}& eatc-donor ={{ DONANTE }}&eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_cont 

 Se toma el " count " de la respuesta para cada departamento - ciudad - institucin en la variable {{ donaciones_por_depto_ciudad_donante_institucion }} 

 % Cobertura donante - beneficiario ( en el diseo: % Cobertura donante) 
 Label: class=" lbl_pct_cobertura_donante_beneficiario " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_pct_cobertura_donante_beneficiario )    

 # donaciones con match de una institucin especfica en un periodo de tiempo dado: 

 {{ URL_entorno_beneficiarios }}/api/abaco/eatc_match_registry?fecha_corta[0]={{ fecha_inicial_periodo }}&fecha_corta[1]={{ fecha_final_periodo }}&departamento={{ DEPARTAMENTO }}&municipio={{ CIUDAD }}& donor ={{eatc_dona_headers. eatc-donor }}&eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&_distinct= eatc-dona_header_code 

 # Total de donaciones anunciadas en ese periodo de tiempo, ciudad y donante: 
 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial_periodo }}&eatc-publication_date[1]={{ fecha_final_periodo }}&eatc-province={{ DEPARTAMENTO }}&eatc-city={{ CIUDAD }}&eatc-donor={{ DONANTE }}&_cont 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-de-donantes%2F86376306-cobertura_donantes2.jpg&ow=487&oh=482, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcobertura-de-donantes%2F86376306-cobertura_donantes2.jpg&ow=487&oh=482 
 Nuevo BO CUA MASTER Beneficiarios 

 701.000000000000 

 COBERTURA DE DONANTES