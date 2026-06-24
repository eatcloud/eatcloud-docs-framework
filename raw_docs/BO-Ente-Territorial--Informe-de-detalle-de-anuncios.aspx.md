# BO-Ente-Territorial--Informe-de-detalle-de-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Consideraciones iniciales: 
El presente informe se debe considerar como un informe tipo que se desplegar para varios tipos de usuarios a lo largo de la plataforma, en particular este informe lo podrn ver los perfiles de: 
Ente territorial (se empezar con esta implementacin) 
Beneficiario (tanto cuenta maestra, como beneficiario tipo BdeA o Beneficiario tipo Fundacin). 
Datagov_cuentas: usuario tipo cua_user (cliente) 

Por lo tanto en su implementacin se debern implementar los diversos filtros (desde el principio) y se deber utilizar esta implementacin para conceptualizar la migracin de informes de las plataformas originales a la plataforma modernizada. 

Informe tipo a partir del cual se debe implementar 
El informe tipo a partir del cul se debe implementar, ser el implementado para el BO de Beneficiarios: y cuya implementacin se puede encontrar aqui: 
Ambiente de pruebas: https://devbeneficiarios.eatcloud.info/_nbob/#!/bdtlanun   
Ambiente de produccin: https://beneficiarios.eatcloud.info/_nbob/#!/bdtlanun   

Documentacin (incompleta: est muy centrada en la construccin de la tabla de datos: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/b-informe-de-detalle-de-anuncios.aspx   

El desarrollo debe basarse en la medida de las posibilidades en lo ya implementado, tomando por ejemplo labels y diseo de la tabla.  Tambin el desarrollo debe pensarse como un proceso metdico de migracin de informes, de tal manera que se puedan pensar tareas automticas para realizar dicha migracin sistemticamente. 

Llamado a endpoints para construccin del informe 
A continuacin se proponen los filtros particulares que harn parte de los llamados para construir los informes, segn los diversos perfiles contemplados para este informe: 

Filtro de campos:  

 eatc_dona_headers :  

 {{filtro_campos_encabezado}} =_cmp= eatc-code,eatc-publication_date,eatc-publication_datetime,eatc-state, eatc_donor_code, eatc_donor_fiscal_name, eatc_donor, eatc-doc,eatc-pod_id,eatc-pod_name,eatc-pod_address, eatc-pod_phone,eatc_cua_origin,eatc-province, eatc_consolidation_origin,eatc-donation_manager_name, eatc-donation_manager_typology_b, eatc-donation_manager_adress,eatc-donation_manager_phone,eatc-adjudication_datetime,eatc-programed_picking_datetime, eatc-picker_name,eatc-picker_doc_id,eatc-picker_license_plate,eatc-picker_start_datetime, eatc-picking_checkin_datetime, eatc_code_verification_datetime, eatc-p,icking_checkout_datetime,eatc-receipt_datetime,eatc_constancy_datetime,eatc-pre_certification_datetime,eatc-certification_datetime,eatc-warning 

eatc_dona:  

 {{filtro_campos_detalle}} =_cmp=eatc-date_time_2,_id, eatc-odd_id,eatc-odd_name,eatc-odd_typology_a, eatc_closer_expiration_date,eatc-odd_original_quantity, eatc-odd_quantity,eatc-odd_unit_weight_kg,eatc-odd_total_weight_kg, eatc-return_cause_code, eatc-return_cause,eatc-odd_total_cost,eatc-VAT_percentage,eatc-total_VAT, 

Filtros por tipo de usuarios: 
Ente territorial: 

 Encabezados: eatc_dona_headers:   

{{ url_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers ?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_final }}&eatc-donor=_*&eatc-donation_manager_code=_*& eatc-province ={{array_provincias}}& eatc-city ={{array_ciudades}}& {{filtro_campos_encabezado}}  

=> se obtiene con esta consulta el {{array_eatc_code}} =array (eatc_dona_headers.eatc-code) 

 Detalles: eatc_dona:   
{{url_entorno_donantes}}/api/{{cua_master}}/eatc_dona?eatc-dona_header_code= {{array_eatc_code}} & {{filtro_campos_detalle}} 

Beneficiarios  
Cuenta maestra: 

 Encabezados: eatc_dona_headers:   
{{ url_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers ?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_final }}&eatc-donor=_*&eatc-donation_manager_code=_*& eatc-province =_*& eatc-city =_*& {{filtro_campos_encabezado}}  

=> se obtiene con esta consulta el {{array_eatc_code}} =array (eatc_dona_headers.eatc-code) 

 Detalles: eatc_dona:   
{{url_entorno_donantes}}/api/{{cua_master}}/eatc_dona?eatc-dona_header_code= {{array_eatc_code}} & {{filtro_campos_detalle}} 

BdeA 

 Consulta de organizaciones adscritas (envindo el identificador nico del banco: eatc_donation_managers. identificador_unico_registro  al siguiente endpoint):  

 {{array_org_adscritas}} = {{URL_beneficiarios}}api/{{cua_master}}/eatc_donation_managers?organizacion_vinculada={{ eatc_donation_managers. identificador_unico_registro }}&_cmp= identificador_unico_registro 

 Encabezados: eatc_dona_headers:   

{{ url_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers ?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_final }}&eatc-donor=_*&eatc-donation_manager_code= {{array_org_adscritas}} & eatc-province =_*& eatc-city =_*& {{filtro_campos_encabezado}}  

=> se obtiene con esta consulta el {{array_eatc_code}} =array (eatc_dona_headers.eatc-code) 

 Detalles: eatc_dona:   
{{url_entorno_donantes}}/api/{{cua_master}}/eatc_dona?eatc-dona_header_code= {{array_eatc_code}} & {{filtro_campos_detalle}} 

 Tipo fundacin 

 Encabezados: eatc_dona_headers:   

{{ url_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers ?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_final }}&eatc-donor=_*&eatc-donation_manager_code= {{ eatc_donation_managers. identificador_unico_registro }} & eatc-province =_*& eatc-city =_*& {{filtro_campos_encabezado}}  

=> se obtiene con esta consulta el {{array_eatc_code}} =array (eatc_dona_headers.eatc-code) 

 Detalles: eatc_dona:   
{{url_entorno_donantes}}/api/{{cua_master}}/eatc_dona?eatc-dona_header_code= {{array_eatc_code}} & {{filtro_campos_detalle}} 

eatc_cua: 

 Encabezados: eatc_dona_headers:   

{{ url_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers ?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_final }}&eatc-donor={{ eatc_cua }}&eatc-donation_manager_code=_*& eatc-province =_*& eatc-city =_*& {{filtro_campos_encabezado}}  

=> se obtiene con esta consulta el {{array_eatc_code}} =array (eatc_dona_headers.eatc-code) 

 Detalles: eatc_dona:   
{{url_entorno_donantes}}/api/{{cua_master}}/eatc_dona?eatc-dona_header_code= {{array_eatc_code}} & {{filtro_campos_detalle}} 

Beneficiario tipo Fundacin: Datagov_cuentas: usuario tipo cua_user (cliente) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Ente-Territorial--Informe-de-detalle-de-anuncios%2F1992761801-Captura-de-pantalla-2024-08-19-164249.png&ow=1619&oh=772, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Ente-Territorial--Informe-de-detalle-de-anuncios%2F1992761801-Captura-de-pantalla-2024-08-19-164249.png&ow=1619&oh=772 

 967.000000000000 

 BO Ente Territorial: Informe de detalle de anuncios