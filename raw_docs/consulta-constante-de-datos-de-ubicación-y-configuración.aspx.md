# consulta-constante-de-datos-de-ubicación-y-configuración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Dado que la presente aplicacin desplegar informacin georeferenciada de ofertas y de mensajes en el Mapa de la Nube de Alimentos , y la configuracin de la manera que se despliegue esta informacin ser paramtrica y configurable de manera remota, la aplicacin tendr que censar constantemente la coordenada en la cual se encuentra este dispositivo y si el cambio de posicin entre la coordenada anterior y la nueva coordenada es mayor de 1000 metros, se debern consultar algunos parmetros de configuracin aplicables. 

 Consulta de coordenadas (actual_lat, actual_lon) 
 El sistema debe ir consultando de manera peridica (en una periodicidad definida por el desarrollador), la latitud y longitud que arroja el dispositivo y la debe ir guardando en variables disponibles para las dems funciones: actual_lat, actual_lon .  Cuando el cambio de una coordenada anterior guardada y una nueva sea mayor a 1000 metros debe disparar la siguiente consulta  (que tambin se debe hacer con la primera coordenada que se obtenga al iniciar una interaccin con la plataforma). 

 Consulta de municipio (actual_city) 
 Con la primera coordenada que se obtenga y subsecuentes (despus de un cambio de coordenadas que implique una distancia mayor a 1000 metros con la anterior coordenada), se debe realizar la siguiente consulta ( documentacin general de la consulta - documentacin consulta particular y ejemplos ). 

 ***Nuevo*** consultas geogrficas apuntando a datagov 

 El sistema deber determinar a partir de la consulta de la posicin del dispositivo, el cdigo de dos dgitos del pas, y con esta informacin realizar la siguiente consulta: 

 https://datagov.eatcloud.info /get/{{ codigo_dos_digitos_pais }}/getpuntos? table = eatc_municipalities & fieldname = eatc-lat,eatc-lon & fieldvalue = {{actual_lat}} , {{actual_lon}} & showfield = eatc-city & km = {{radio_a_partir_de_fieldvalue_para_la_conuslta}}) 

 (Anteriormente: https://beneficiarios.eatcloud.info /get/data/getpuntos? table = eatc_co_municipalities & fieldname = latitud,longitud & fieldvalue = {{actual_lat}} , {{actual_lon}} & showfield = {{campos_del_object_store_a_mostrar}} & km = {{radio_a_partir_de_fieldvalue_para_la_conuslta}}) 

 Ejemplo 1: 
 En ambiente de pruebas un dispositivo cuya primera coordenada tomada al iniciar a utilizar el aplicativo es: 6.2045697,-75.60157, consulta el municipio (eatc-city) para guardarlo y tenerlo disponible para futuras consultas. 

 Ambiente: pruebas (como estos datos se centralizan en datagov, la consulta siempre se hace sobre esa estructura) 
 fieldvalue: 6.2045697,-75.60157 
 showfield: eatc-city 
 km: 2 (se toma 2 KM como una distancia prudente para encontrar un centro poblado, pero habr casos especiales que se necesite un radio mayor y que deben ajustar en la medida de que se vallan detectando casos afectados por esta condicin) 

 https://datagov.eatcloud.info /get/ co /getpuntos? table = eatc_municipalities & fieldname = eatc-lat,eatc-lon & fieldvalue = 6.2045697,-75.60157 & showfield =eatc-city &km= 2     

 Como la respuesta trae dos municipios, ambos se guardan (haciendo un distinct) para realizar consultas a partir de los dos (actual_city=MEDELIN,ITAGUI). 

 Determinacin del radio de consulta para las ofertas cercanas (actual_sale_radius_km) 
 La plataforma cuenta con el siguiente servicio: 

 {{URL_entorno_beneficiarios}}/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale&{{parmetros_de_consulta}} 

 Que permite establecer cul es el radio de consulta para ofertas para  
 El usuario especfico,  
 El usuario segn alguna de sus tipologas (pendiente por definir),  
 La ciudad en dnde se encuentra el dispositivo que est haciendo las consultas 
 El pas en dnde se encuentra el dispositivo que est haciendo las consultas 
 o El radio establecido por defecto para esta consulta 

 De la siguiente manera: 

 Parmetros de consulta: 

 eatc-user_id:  
 Como primer paso se enva el cdigo del usuario (si el usuario ya est identificado por la plataforma, se toma ese ID, si no ha sido identificado aun por la plataforma entonces se pasa al siguiente parmetro y se enva _default en este).  Si la consulta no trae resultados se pasa  a la siguiente consulta (enviando este parmetro como _default ) 

 Ejemplo: en ambiente de pruebas el usuario con eatc-id = 777 debe hacer esta consulta: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale& eatc-user_id=777    

 Como la consulta no trae resultados, pasa al siguiente paso, enviando en el parmetro eatc-user_id el dato _default . Si se hubiera detectado un dato vlido en este punto, el proceso se detiene y no son necesarias las dems consultas. 

 (Prximamente) eatc-user_typology_a, eatc-user_typology_b, eatc-user_typology_c:  
 en implementaciones posteriores se podrn realizar consultas especficas por estos parmetros pero por el momento se obviarn y se pasa directamente al prximo parmetro ( eatc-city ) 

 eatc-city 
 Si las anteriores bsquedas no dieron resultado entonces se enva el dato de la ciudad actual ( actual_city ), para efectuar la bsqueda. 

 Ejemplo 1: en ambiente de pruebas el usuario se encuentra en la siguiente cerca de las ciudades de MEDELLIN e ITAGUI (actual_city): 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale& eatc-user_id=_default&eatc-city=MEDELLIN,ITAGUI 

 Como la consulta trae datos, se toma actual_sale_radius_km= 5 (dato que viene en el parmetro: eatc-radius_km   de la anterior consulta ) . En este punto el proceso se detiene y no son necesarias las posteriores consultas. 

 Ejemplo 2: en ambiente de pruebas el usuario se encuentra en la siguiente ciudad de BUCARAMANGA: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale,eatc_sale_messages& eatc-user_id=_default&eatc-city=BUCARAMANGA    

 Cmo la consulta no trae resultados, pasa a la siguiente, enviando en el parmetro de ciudad ( eatc-city ) el dato _default 

 eatc-country:  

 Se enva el cdigo de dos dgitos del pas.   

 Ejemplo: en ambiente de pruebas el usuario se encuentra en Bucaramanga (Colombia): 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale& eatc-user_id=_default&eatc-city=_default&eatc-country=co       

 Como la consulta no trae resultados, pasa a la siguiente consulta, enviando en el parmetro eatc-country el dato _default . Si se hubiera detectado un dato vlido en este punto, el proceso se detendra no sera necesaria la ltima consulta. 

 consulta _default:  
 Se envan todos los parmetros de consulta anteriormente descritos con el dato _default 

 Ejemplo: en ambiente de pruebas el usuario anterior (que est en Bucaramanga, Colombia) deber enviar la siguiente consulta: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale& eatc-user_id=_default&eatc-city=_default&eatc-country=_default      

 Como la consulta trae datos, se toma actual_sale_radius_km= 5 (dato que el dato viene en el parmetro: eatc-radius_km ) para realizar consultas posteriores. 

 Determinacin del radio de consulta para mensajes (actual_messages_radius_km) 
 La plataforma cuenta con el siguiente servicio: 

 {{URL_entorno_beneficiarios}}/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages&{{parmetros_de_consulta}} 

 Que permite establecer cul es el radio de consulta para ofertas para  
 El usuario especfico,  
 El usuario segn alguna de sus tipologas (pendiente por definir),  
 La ciudad en dnde se encuentra el dispositivo que est haciendo las consultas 
 El pas en dnde se encuentra el dispositivo que est haciendo las consultas 
 o El radio establecido por defecto para esta consulta 

 De la siguiente manera: 

 Parmetros de consulta: 

 eatc-user_id:  
 Como primer paso se enva el cdigo del usuario (si el usuario ya est identificado por la plataforma, se toma ese ID, si no ha sido identificado aun por la plataforma entonces se pasa al siguiente parmetro y se enva _default en este).  Si la consulta no trae resultados se pasa  a la siguiente consulta (enviando este parmetro como _default ) 

 Ejemplo: en ambiente de pruebas el usuario con eatc-id = 777 debe hacer esta consulta: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages& eatc-user_id=777     

 Como la consulta no trae resultados, pasa al siguiente paso, enviando en el parmetro eatc-user_id el dato _default . Si se hubiera detectado un dato vlido en este punto, el proceso se detiene y no son necesarias las dems consultas. 

 (Prximamente) eatc-user_typology_a, eatc-user_typology_b, eatc-user_typology_c:  
 en implementaciones posteriores se podrn realizar consultas especficas por estos parmetros pero por el momento se obviarn y se pasa directamente al prximo parmetro ( eatc-city ) 

 eatc-city 

 Si las anteriores bsquedas no dieron resultado entonces se enva el dato de la ciudad actual ( actual_city ), para efectuar la bsqueda. 

 Ejemplo 1: en ambiente de pruebas el usuario se encuentra en la siguiente cerca de las ciudades de MEDELLIN e ITAGUI (actual_city): 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages& eatc-user_id=_default&eatc-city=MEDELLIN,ITAGUI         

 Como la consulta trae datos, se toma actual_messages_radius_km= 50 (dato que viene en el parmetro: eatc-radius_km ) para realizar consultas posteriores. En este punto el proceso parara y no son necesarias las posteriores consultas. 

 Ejemplo 2: en ambiente de pruebas el usuario se encuentra en la siguiente ciudad de BUCARAMANGA: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages& eatc-user_id=_default&eatc-city=BUCARAMANGA     

 Cmo la consulta no trae resultados, pasa a la siguiente, enviando en el parmetro de ciudad ( eatc-city ) el dato _default 

 eatc-country:  
 Se enva el cdigo de dos dgitos del pas.   

 Ejemplo: en ambiente de pruebas el usuario se encuentra en Bucaramanga (Colombia): 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages& eatc-user_id=_default&eatc-city=_default&eatc-country=co        

 Como la consulta no trae resultados, pasa a la siguiente consulta, enviando en el parmetro eatc-country el dato _default . Si se hubiera detectado un dato vlido en este punto, el proceso se detendra no sera necesaria la ltima consulta. 

 consulta _default:  
 Se envan todos los parmetros de consulta anteriormente descritos con el dato _default 

 Ejemplo: en ambiente de pruebas el usuario anterior (que est en Bucaramanga, Colombia) deber enviar la siguiente consulta: 

 https://devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_query_radius?eatc-query_type=eatc_sale_messages& eatc-user_id=_default&eatc-city=_default&eatc-country=_default       

 Como la consulta trae datos, se toma actual_messages_radius_km=50 (dato que viene en el parmetro: eatc-radius_km ) para realizar consultas posteriores. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 App usuario final - Sale 

 CONSULTA CONSTANTE DE DATOS DE UBICACIN Y CONFIGURACIN DE RADIOS DE CONSULTA