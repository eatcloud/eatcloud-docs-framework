# getpuntos-consulta-de-información-geolocalizada.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 SERVICIO &quot;GETPUNTOS&quot;&#58; 
 Parmetros de consulta 
 Se ha dispuesto un servicio para consultar los puntos geogrficos (determinados por una latitud y una longitud) que estn dentro de un radio establecio a partir de una coordenada dada, con el nimo de tener posibilidad de filtrar por cercana, la informacin que cuenta en nuestros repositorios con latitud y longitud a travs de un servicio.&#160; La URL genrica del servicio es 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/&#123;&#123;CUA&#125;&#125;/getpuntos?&#123;&#123;parametros_de_consulta&#125;&#125; 
&#160; 
 Los parmetros que se envan para realizar una consulta georeferenciada son los siguientes 
&#160; 
 table 
 Obligatorio. En este parmetro se enva el nombre del object store (que contiene informacin georeferenciada, es decir, datos de latitud y longitud en coordenadas decimales) sobre el cual se va a realizar la consulta. 
&#160; 
 fieldname 
 Obligatorio. En este parmetro se envan el nombre o los nombres de los campos en donde se alojan los datos de latitud y longitud para el object store (o table ) particular. 
&#160; 
 fieldvalue 
 Obligatorio. En este parmetro se envan las coordenadas decimales, separadas por una coma, a partir de las cuales se realizar la consulta y que se constituyen en el centro de la circunferencia que contendr los puntos que trae la consulta y cuyo radio ser el dato enviado en el parmetro km . 
&#160; 
 showfield 
 Obligatorio. Corresponde a los campos (separados por comas) que queremos traer en la consulta desde el object store (o table ) definido. Son campos propios del object store o tabla consultada. 
&#160; 
 km 
 Obligatorio. Corresponde al radio de consulta en kilmetros, y que forma una circunferencia cuyo centro geogrfico es el punto definido en el parmetro fieldvalue . 
&#160; 
 filterfield_1,filterfield_2,filterfield_3 
 Opcional. Corresponden al campo o los campos por los cuales se quiere filtrar la informacin que se trae del object store (o table ) en particular (y que se aplican adems del filtro geogrfico). En este caso se desean traer solo las ofertas cuyo estado sea &quot;ofertadas&quot; o &quot;parcialmente ordenadas&quot;, por lo tanto el valor ser eatc-odd_state 
&#160; 
 filtervalue_1,filtervalue_2,filtervalue_3 
 Opcional. Corresponde al valor, o los valores que deben tomar los campos o parmetros definidos en el respectivo filterfied_ y que obrarn como filtro de la informacin que traer la consulta. Tienen un funcionamiento similar a los valores que se le dan a los parmetros de consulta de la API EatCloud . 
&#160; 
 A continuacin se muestra de manera genrica cmo se enva la conusulta al servicio 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/get/&#123;&#123;CUA&#125;&#125;/getpuntos? table = &#123;&#123;objec_store_con_info_georeferenciada&#125;&#125; &amp; fieldname = &#123;&#123;nombres_campos_latitud_longitud_separados_por_coma&#125;&#125; &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Parmetros de respuesta del servicio 
 El servicio trae una respuesta que obtiene los datos solicitado a travs de la definicin showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; ms el siguiente parmetro&#58; 
&#160; 
 eatc-lat 
 Se muestra la latitud en coordenadas decimales del respectivo registro. 
&#160; 
 eatc-lon 
 Se muestra la longitud en coordenadas decimales del respectivo registro. 
&#160; 
 km 
 Corresponde a la distancia en kilmetros desde el centro definido para la bsqueda en el parmetro fieldvalue hasta el punto (latitud y longitud) del registro particular que muestra la respuesta. 

&#160; 
 ENTORNOS, CUENTAS Y TABLAS 
 A continuacin se documenta las tablas de las respectivas cuentas y entornos, sobre las cuales se puede realizar la consulta para traer los puntos, dado que contienen informacin de georeferenciacin. 
&#160; 
 Donantes&#58; 
 A continuacin se presentan las cuentas y los object stores (o table ) a los cuales se les puede realizar una consulta georeferenciada en esta familia de entornos. 
&#160; 
 &#123;&#123;todas_las_cuentas&#125;&#125;&#58; eatc_pods 
 fieldname = eatc-lat,eatc-lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;CUA&#125;&#125;/ eatc_pods?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/&#123;&#123;CUA&#125;&#125;/getpuntos? table = eatc_pods &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 En ambiente de pruebas se realizar una consulta para determinar cuales puntos (del repositorio de todoslos puntos) y que pertenecen a la cuenta exito , se encuentran en un radio de 10 KM. 
&#160; 
 Ambiente&#58; pruebas https&#58;//devdonantes.eatcloud.info 
 CUA&#58; allpods 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devdonantes.eatcloud.info /api/allpods/ eatc_pods?_campos (eatc-adress,eatc-name,eatc-cua ) 
 km&#58; 10 
 filterfield_1&#58; eatc-cua 
 filtervalue_1&#58; exito 
&#160; 
 https&#58;//devdonantes.eatcloud.info /get/ allpods /getpuntos? table = eatc_pods &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = eatc-adress,eatc-name,eatc-cua &amp;km= 10 &amp;filterfield_1= eatc-cua &amp;filtervalue_1= exito &#160;&#160;&#160;&#160; 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 En ambiente de productivo se realizar una consulta para determinar cuales puntos de la cuenta exito , se encuentran en un radio de 10 KM y pertenecen a la marca EXITO EXPRESS. 
&#160; 
 Ambiente&#58; productivo https&#58;//donantes.eatcloud.info 
 CUA&#58; exito 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//donantes.eatcloud.info /api/exito/ eatc_pods?_campos (eatc-adress,eatc-name ) 
 km&#58; 10 
 filterfield_1&#58; eatc-typology_a 
 filtervalue_1&#58; EXITO%20EXPRESS 
&#160; 
 https&#58;//donantes.eatcloud.info /get/ exito /getpuntos? table = eatc_pods &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = eatc-adress,eatc-name &amp;km= 10 &amp;filterfield_1= eatc-typology_a &amp;filtervalue_1= EXITO%20EXPRESS 

&#160; 
 eatcloud&#58; eatc_sale 
 fieldname = eatc-pod_lat,eatc-pod_lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_sale?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 En ambiente de pruebas se realizar una consulta para determinar cuales ofertas de ltimo minuto de donacin de la cuenta colombia , se encuentran en un radio de 7 KM de un punto especfico. 
&#160; 
 Ambiente&#58; pruebas https&#58;//devdonantes.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devdonantes.eatcloud.info /api/eatcloud/ eatc_sale?_campos ( eatc-pod_name,eatc-pod_address,eatc-odd_name,eatc-odd_description) 
 km&#58; 7 
 filterfield_1&#58; eatc_cua_origin 
 filtervalue_1&#58; colombia 
&#160; 
 https&#58;//devdonantes.eatcloud.info /get/ eatcloud /getpuntos? table = eatc_sale &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield =eatc-pod_name,eatc-pod_address,eatc-odd_name,eatc-odd_description &amp;km= 7 &amp;filterfield_1= eatc_cua_origin &amp;filtervalue_1= colombia &#160; &#160;&#160;&#160;&#160; 
&#160; 
 abaco&#58; eatc_dona_headers 
 fieldname = eatc-lat,eatc-lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_donantes&#125;&#125;/api/abaco/ eatc_dona_headers?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/abaco/getpuntos? table = eatc_dona_headers &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 En ambiente de pruebas se realizar una consulta para determinar cuales anuncios de donacin de la cuenta exito , se encuentran en un radio de 7 KM de un punto especfico. 
&#160; 
 Ambiente&#58; pruebas https&#58;//devdonantes.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devdonantes.eatcloud.info /api/abaco/ eatc_dona_headers?_campos ( eatc-code,eatc-pod_name,eatc-publication_datetime,eatc-donation_manager_name) 
 km&#58; 7 
 filterfield_1&#58; eatc_cua_origin 
 filtervalue_1&#58; exito 
&#160; 
 https&#58;//devdonantes.eatcloud.info /get/ abaco /getpuntos? table = eatc_dona_headers &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield =eatc-code,eatc-pod_name,eatc-publication_datetime,eatc-donation_manager_name &amp;km= 7 &amp;filterfield_1= eatc_cua_origin &amp;filtervalue_1= exito &#160;&#160;&#160;&#160;&#160; 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 En ambiente de productivo se realizar una consulta para determinar cuales anuncios de donacin tienen estado anunciado (announced) y&#160; a 120 KM de un punto particular (la coordenada de la Fundacin Mis Corazones Alegres), con el animo de pintar la card de anuncio que se muestra en la nube de donaciones . 
&#160; 
 Ambiente&#58; productivo https&#58;//donantes.eatcloud.info 
 CUA&#58; abaco 
 fieldvalue&#58; 6.255987,-75.561257 ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=116 campo &quot;coordenadas&quot;) 
 showfield&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?_campos (eatc-publication_datetime,eatc-total_weight_kg,eatc_pod_name,eatc-pod_address,eatc_donor,eatc-code,eatc-pod_id,eatc-id,eatc-state,eatc-city,eatc-adjudication_datetime,eatc-warning) 
 km&#58; 120 
 filterfield_1&#58; eatc-state 
 filtervalue_1&#58; announced 
&#160; 
 https&#58;//donantes.eatcloud.info /get/ abaco /getpuntos? table = eatc_dona_headers &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = eatc-publication_datetime,eatc-total_weight_kg,eatc-pod_name,eatc-pod_address,eatc-donor,eatc-code,eatc-pod_id,eatc-id,eatc-state,eatc-city,eatc-adjudication_datetime &amp;km= 120 &amp;filterfield_1= eatc-state &amp;filtervalue_1= announced &#160;&#160;&#160;&#160;&#160;&#160;&#160; 

&#160; 
 &#123;&#123;todas_las_cuentas&#125;&#125;&#58; eatc_pods_coordinates 
 fieldname = eatc-lat,eatc-lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;CUA&#125;&#125;/ eatc_pods_coordinates?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/&#123;&#123;CUA&#125;&#125;/getpuntos? table = eatc_pods_coordinates &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 .... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devdonantes.eatcloud.info 
 CUA&#58; allpods 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devdonantes.eatcloud.info /api// eatc_pods_coordinates?_campos ( ) 
 km&#58; 10 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info /get//getpuntos? table = eatc_pods_coordinates &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 10 &amp;filterfield_1=&amp;filtervalue_1= &#160;&#160;&#160;&#160; 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 .... 
&#160; 
 Ambiente&#58; productivo https&#58;//donantes.eatcloud.info 
 CUA&#58; exito 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//donantes.eatcloud.info /api// eatc_pods_coordinates?_campos(eatc-adress,eatc-name ) 
 km&#58; 10 
 filterfield_1&#58; eatc-typology_a 
 filtervalue_1&#58; EXITO%20EXPRESS 
&#160; 
 https&#58;//donantes.eatcloud.info /get//getpuntos? table = eatc_pods_coordinates &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 10 &amp;filterfield_1=&amp;filtervalue_1= &#160;&#160;&#160;&#160; 
&#160; 

&#160; 
 &#123;&#123;todas_las_cuentas&#125;&#125;&#58; eatc_dona_header_geo_history 
 fieldname = ... 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;CUA&#125;&#125;/ eatc_dona_header_geo_history?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/get/&#123;&#123;CUA&#125;&#125;/getpuntos? table = eatc_dona_header_geo_history &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 .... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devdonantes.eatcloud.info 
 CUA&#58; allpods 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devdonantes.eatcloud.info /api// eatc_dona_header_geo_history?_campos ( ) 
 km&#58; 10 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info /get//getpuntos? table = eatc_dona_header_geo_history &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 10 &amp;filterfield_1=&amp;filtervalue_1= &#160;&#160;&#160;&#160; 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 .... 
&#160; 
 Ambiente&#58; productivo https&#58;//donantes.eatcloud.info 
 CUA&#58; exito 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//donantes.eatcloud.info /api// eatc_dona_header_geo_history?_campos(eatc-adress,eatc-name ) 
 km&#58; 10 
 filterfield_1&#58; eatc-typology_a 
 filtervalue_1&#58; EXITO%20EXPRESS 
&#160; 
 https&#58;//donantes.eatcloud.info /get//getpuntos? table = eatc_dona_header_geo_history &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 10 &amp;filterfield_1=&amp;filtervalue_1= &#160;&#160;&#160;&#160; 
&#160; 

&#160; 
 Beneficiarios 
 A continuacin se presentan las cuentas y los object stores (o table ) a los cuales se les puede realizar una consulta georeferenciada en esta familia de entornos. 
&#160; 
 data&#58; eatc_co_municipalities 
 fieldname = latitud,longitud 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta https&#58;//beneficiarios.eatcloud.info /api/data/ eatc_co_municipalities?_campos 
&#160; 
 Consulta genrica&#58; 
 https&#58;//beneficiarios.eatcloud.info /get/data/getpuntos? table = eatc_co_municipalities &amp; fieldname = latitud,longitud &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 Desde una coordenada se desea saber cual es el departamento a la que corresponde 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//beneficiarios.eatcloud.info/ api/data/ eatc_co_municipalities?_campos (codigo_departamento,nombre_departamento ) 
 km&#58; 7 
 &#160; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/get/data/getpuntos?table=eatc_co_municipalities&amp;fieldname=latitud,longitud&amp;fieldvalue=6.2045697,-75.60157&amp;showfield=codigo_departamento,nombre_departamento&amp;km=7 &#160; 
&#160; 
 Se puede observar que todos los datos que trae la consulta corresponden al departamento de ANTIOQUIA 
&#160; 
 Ejemplo 2&#58; 
 Desde una coordenada se desea saber los municipios ms cercanos y que pertenecen al departamento de Antioquia 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//beneficiarios.eatcloud.info/ api/data/ eatc_co_municipalities?_campos (nombre_municipio,codigo_dpto_mpio,nombre_centro_poblado,nombre_tipo_ctro_pbdo ) 
 km&#58; 2 
 filterfield_1&#58; nombre_departamento 
 &amp;filtervalue_1&#58; ANTIOQUIA 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/get/data/getpuntos?table=eatc_co_municipalities&amp; fieldname =latitud,longitud&amp; fieldvalue =6.2045697,-75.60157&amp; showfield =nombre_municipio,codigo_dpto_mpio,nombre_centro_poblado,nombre_tipo_ctro_pbdo&amp; km =2 &amp;filtervalue_1= nombre_departamento &amp;filterfield_2= ANTIOQUIA 

&#160; 
 eatcloud&#58; eatc_sale_order 
 fieldname = eatc-pod_lat,eatc-pod_lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/ eatc_sale_order?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_order &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 ... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devbeneficiarios.eatcloud.info /api/eatcloud/ eatc_sale_order?_campos ( ) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/ eatcloud /getpuntos? table = eatc_sale_order &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1= 

&#160; 
 eatcloud&#58; eatc_sale_order_headers 
 fieldname = eatc-pod_lat,eatc-pod_lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/ eatc_sale_order_headers?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_order_headers &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 ... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devbeneficiarios.eatcloud.info /api/eatcloud/ eatc_sale_order_headers?_campos ( ) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/ eatcloud /getpuntos? table = eatc_sale_order_headers &amp; fieldname = eatc-pod_lat,eatc-pod_lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1= 

&#160; 
 eatcloud&#58; eatc_sale_users_coordinates 
 fieldname = eatc-lat,eatc-lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/ eatc_sale_users_coordinates?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_users_coordinates &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 ... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devbeneficiarios.eatcloud.info /api/eatcloud/ eatc_sale_users_coordinates?_campos ( ) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/ eatcloud /getpuntos? table = eatc_sale_users_coordinates &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1= 

&#160; 
 eatcloud&#58; eatc_sale_messages 
 fieldname = eatc-lat,eatc-lon 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/ eatc_sale_messages?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/eatcloud/getpuntos? table = eatc_sale_messages &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 ... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devbeneficiarios.eatcloud.info /api/eatcloud/ eatc_sale_messages?_campos ( ) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/ eatcloud /getpuntos? table = eatc_sale_messages &amp; fieldname = eatc-lat,eatc-lon &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1= 

&#160; 
 abaco&#58; eatc_donation_managers 
 fieldname = coordenadas 
 showfield= se pueden incorporar en este parmetro cualquier subconjunto de campos que se obtienen de la siguiente consulta &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/abaco/ eatc_donation_managers?_campos 
&#160; 
 Consulta genrica&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/abaco/getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; &amp; showfield = &#123;&#123;campos_del_object_store_a_mostrar&#125;&#125; &amp; km = &#123;&#123;radio_a_partir_de_fieldvalue_para_la_conuslta&#125;&#125; &amp;filterfield_1= &#123;&#123;campo_para_primer_filtro&#125;&#125; &amp;filtervalue_1= &#123;&#123;valores_del_campo_para_el_primer_filtro&#125;&#125; &amp;filterfield_2= &#123;&#123;campo_para_segundo_filtro&#125;&#125; &amp;filtervalue_2= &#123;&#123;valores_del_campo_para_el_segundo_filtro&#125;&#125; &amp;filterfield_3= &#123;&#123;campo_para_tercer_filtro&#125;&#125; &amp;filtervalue_3= &#123;&#123;valores_del_campo_para_el_tercer_filtro&#125;&#125; &#160; 
&#160; 
 Ejemplo 1&#58; 
 ... 
&#160; 
 Ambiente&#58; pruebas https&#58;//devbeneficiarios.eatcloud.info 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//devbeneficiarios.eatcloud.info /api/abaco/ eatc_donation_managers?_campos ( eatc-code,eatc-pod_name,eatc-publication_datetime,eatc-donation_manager_name) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info /get/ abaco /getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1= &#160;&#160;&#160;&#160;&#160; 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 En ambiente de productivo se realizar una consulta para determinar cuales anuncios de donacin tienen estado recibidos y&#160; a 7 KM de un punto particular y fueron recibidos por la fundacin Mis corazones alegres. 
&#160; 
 Ambiente&#58; productivo https&#58;//beneficiarios.eatcloud.info 
 CUA&#58; exito 
 fieldvalue&#58; 6.2045697,-75.60157 
 showfield&#58; https&#58;//beneficiarios.eatcloud.info /api/allpods/ eatc_donation_managers?_campos ( ) 
 km&#58; 7 
 filterfield_1&#58; &#160; 
 filtervalue_1&#58; &#160; 
 filterfield_2&#58; &#160; 
 filtervalue_2&#58; &#160; 
&#160; 
 ***REVISAR*** 
 https&#58;//beneficiarios.eatcloud.info /get/ abaco /getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = 6.2045697,-75.60157 &amp; showfield = &amp;km= 7 &amp;filterfield_1=&amp;filtervalue_1=&amp;filterfield_2=&amp;filtervalue_2= 

&#160; 
 OTRAS MEJORAS 
&#160; 
 Otra mejora importante sera colocar un parmetro adicional para indicar un campo para hacer un select distinct, y solo traer los registros que sean diferentes en ese parmetro (tambin sera opcional) 

&#160; 
 distinctfield &#58; el nombre del campo por el cual se realizara el select distinct, por ejemplo para el caso anterior si se desea traer solo los puntos cuyo cdigo sea diferente entonces en este parmetro se pondra el valor eatc-pod_id en este parmetro 

 https&#58;//devdonantes.eatcloud.info/get/eatcloud/getpuntos?table=eatc_sale&amp;fieldname=eatc-pod_lat,eatc-pod_lon&amp;fieldvalue=6.204509267708382,-75.59945952147247&amp;showfield=eaetc-pod_id&amp;km=5&amp; filterfield= eatc-odd_state &amp; filterfieldvalue= sale , partially_ordered&amp; distinctfield= eatc-pod_id 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 GETPUNTOS: CONSULTA DE INFORMACIN GEOLOCALIZADA