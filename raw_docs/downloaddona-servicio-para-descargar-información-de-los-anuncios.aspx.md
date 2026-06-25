# downloaddona-servicio-para-descargar-información-de-los-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
 El presente servicio se especifica para crear interfaces de descarga de datos que sirvan como integracin con otros sistemas.&#160; Inicialmente se disea como una solicitud de BAMX para integrar los datos de EatCloud con su ERP 

 LOG DEL SERVICIO 
 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 
&#160; 
 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;op&#58;false 

 1. VALIDACIN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de Parmetros del body de la peticin &#160; de la especificacin del API pblica . Si lo son, seguir adelante con el prximo paso.&#160; Si no lo son deber entregar una respuesta de error&#58; 
 incomplete_data 

 2. CONSULTA DE LOS DATOS DE LA ESTRUCTURA DE DESCARGA 
&#160; 
 Con los datos que llega en los parmetros&#58; 
&#160; 
 eatc_cua &#160; 
 cua_master 
 eatc_download_platform &#160; 
 eatc_download_structure &#160; 
 eatc_download_format &#160; 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
&#160; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_data_download_map?eatc_cua=&#123;&#123; eatc_cua &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_download_platform=&#123;&#123; eatc_download_platform &#125;&#125;&amp;eatc_download_structure=&#123;&#123; eatc_download_structure &#125;&#125;&amp;eatc_download_format=&#123;&#123; eatc_download_format &#125;&#125;&amp;_cmp= eatc_objectstore , eatc_parameter_1 , eatc_parameter_2,eatc_data_type , download_target_parameter , eatc_descripcion , eatc_variable_query , eatc_variable_formula,eatc_order , eatc_level 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail_not_defined_data_donwload_structure 
&#160; 
 Si la consulta arroja respuesta una respuesta vlida el sistema guarda los datos que se recibieron en , eatc_parameter_1 , eatc_parameter_2 y haciendo un distintc por cada uno de los eatc_objetstore los guarda en la variable &#123;&#123;parametros_a_consultar&#125;&#125; para posteriormente realizar consultas y&#160; prosigue con la siguiente consulta&#58; 
&#160; 
 Ejemplo&#58; para ambiente de pruebas, cua_master&#58; mexico, eatc_cua=_*, eatc_download_platform=pbapi, eatc_download_structure=mx_dona, eatc_download_format=json 
&#160; 
 El sistema realiza la siguiente consulta&#58; https&#58;//devdatagov.eatcloud.info/api/eatcloud/eatc_data_download_map?eatc_cua=_*&amp;eatc_cua_master=mexico&amp;eatc_download_platform=pbapi&amp;eatc_download_structure=mx_dona&amp;eatc_download_format=json&amp;_cmp=eatc_objectstore,eatc_parameter_1,eatc_parameter_2,eatc_data_type,download_target_parameter,eatc_descripcion,eatc_variable_query,eatc_variable_formula,eatc_order,eatc_level y por lo tanto obtiene por cada uno de los objectstore los siguientes &#123;&#123;parametros_a_consultar&#125;&#125; &#160; 
&#160; 
 eatc_dona_headers&#58; &#123;&#123;parametros_a_consultar&#125;&#125; = eatc-dona_header_code,eatc-publication_datetime,eatc-donor,eatc_donor_code,eatc_donor_fiscal_name,eatc-pod_id,eatc-pod_name,eatc-donation_manager_code,eatc-picking_checkout_datetime,eatc-receipt_datetime,eatc-warning 
&#160; 
 eatc_dona&#58; &#123;&#123;parametros_a_consultar&#125;&#125; = eatc-odd_original_quantity,eatc-odd_unit_weight_kg,eatc-odd_quantity,eatc-odd_id,eatc-odd_name,origin_odds_typology_a 

 3. CONSULTA DE LOS ENCABEZADOS DE LOS ANUNCIOS DE DONACIN A DESCARGAR 
&#160; 
 ***NUEVO &#58; Consulta de puntos de donacin a los cuales no se les puede realizar descarga de datos 
&#160; 
 Con los datos que llega en los parmetros&#58; 
 eatc_cua &#160; 
 cua_master 
&#160; 
 El sistema deber consultar los puntos de donacin a los cuales no se les puede realizar descarga de datos, con la siguiente&#160; manera&#58; 
&#160; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_pods_not_downloaddona?eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123; eatc_cua &#125;&#125;&amp;eatc_not_downloaddona= y &amp;_cmp=eatc_pod_id 
&#160; 
 Si el sistema arroja resultados, con los IDs trados se debe armar un &#123;&#123;array_pod_id_not_donwloaddona&#125;&#125; que servir para la prxima consulta 
&#160; 
 Ejemplo&#58; cua_master=mexico, eatc_cua=nestle (ambiente de pruebas) 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_pods_not_downloaddona ?eatc_cua_master=mexico&amp;eatc_cua=nestle&amp;eatc_not_downloaddona=y&amp;_cmp=eatc_pod_id &#160; 
&#160; 
 Dada la respuesta del servicio&#58; 0001 entonces con esta informacin se arma el &#123;&#123; array_pod_id_not_donwloaddona &#125;&#125; 
 *** 
&#160; 
 Con los datos que llega en los parmetros&#58; 
 eatc_cua &#160; 
 cua_master 
 eatc_dona_states 
 eatc_initial_date 
 eatc_end_date 
&#160; 
 El array de parmetros a consultar (que se obtuvo anteriormente) ***NUEVO &#58; y el array de puntos de donacin a los cuales no se les realiza esta consulta *** 
&#160; 
 El sistema deber realizar la siguiente consulta de anuncios de donacin&#58; 
&#160; 
 &#123;&#123; URL_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc_donor=&#123;&#123; eatc_cua &#125;&#125;&amp; eatc-publication_date[0]=&#123;&#123; eatc_initial_date &#125;&#125; &amp; eatc-publication_date[1]=&#123;&#123; eatc_end_date &#125;&#125; &amp;eatc-state=&#123;&#123; eatc_dona_states &#125;&#125; &amp;eatc-pod_id=_nin_ &#123;&#123; array_pod_id_not_donwloaddona &#125;&#125; &amp;_cmp= &#123;&#123;parametros_a_consultar&#125;&#125; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail_no_data_found_for_the_query 
&#160; 
 Si la consulta arroja respuesta una respuesta el sistema obtiene la informacin y posteriormente realiza un array de los cdigos de donacin obtenidos &#123;&#123;array_dona_headers_codes&#125;&#125; para realizar la consulta de los datos de los detalles de anuncios de donacin 

 4. CONSULTA DE LOS DETALLES DE LOS ANUNCIOS DE DONACIN A DESCARGAR 
&#160; 
 Con los datos d el array de codigos de cdigos de encabezados de donacin y del array de parmetros a consultar (que se obtuvieron anteriormente) 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
 &#123;&#123; URL_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code = &#123;&#123;array_dona_headers_codes&#125;&#125; &amp;_cmp= &#123;&#123;parametros_a_consultar&#125;&#125; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail_no_data_found_for_the_query 
&#160; 
 Si la consulta arroja respuesta una respuesta el sistema obtiene la informacin y posteriormente para posteriormente realizar las transformaciones necesarias para armar la respuesta de los datos a descargar 

 5. CONFIGURACIN DE LA RESPUESTA PARA LA DESCARGA 
 A partir de los datos que se obtienen en el punto 2 el sistema deber armar una respuesta de la descarga, por cada uno de los anuncios encontrados, interpretando la informacin de la siguiente manera&#58; 
&#160; 
 eatc_parameter_1&#58; contiene informacin del dato que se entregar en la respectiva descarga.&#160; Tambin puede contener informacin para realizar una consulta o una operacin y as obtener el respectivo dato, 
 eatc_parameter_2&#58; contiene informacin para realizar una consulta o una operacin y as obtener el respectivo dato, 
 eatc_data_type&#58; Establece el tipo de dato que se entregar. 
 download_target_parameter &#58; Presenta el nombre del parmetro o la declaracin del campo que se entregar en la descarga 
 eatc_descripcion &#58; entrega una descripcin del dato que se entrega en la descarga. 
 eatc_variable_query &#58; indica una consulta que se debe realizar con los parmetros 1 y/o 2 para obtener el dato que se entrega en la descarga 
 eatc_variable_formula &#58; indica una operacin que se debe realizar con los parmetros 1 y/o 2 para obtener el dato que se entrega en la descarga 
 eatc_order &#58; indica el orden en el cual se entrega la informacin en la estructura respectiva 
 eatc_level &#58; indica el nivel en el cual se entrega la informacin en la estructura respectiva.&#160; Cuando se trata de un JSON, indica un objeto que se anida para entregar informacin de detalle (en el caso de estar definido como 

&#160; 
 Ejemplo&#58; para ambiente de pruebas, cua_master&#58; mexico, eatc_cua=_*, eatc_download_platform=pbapi, eatc_download_structure=mx_dona, eatc_download_format=json 
&#160; 
 El sistema realiza la siguiente consulta&#58; https&#58;//devdatagov.eatcloud.info/api/eatcloud/eatc_data_download_map?eatc_cua=_*&amp;eatc_cua_master=mexico&amp;eatc_download_platform=pbapi&amp;eatc_download_structure=mx_dona&amp;eatc_download_format=json&amp;_cmp=eatc_objectstore,eatc_parameter_1,eatc_parameter_2,eatc_data_type,download_target_parameter,eatc_descripcion,eatc_variable_query,eatc_variable_formula,eatc_order,eatc_level y por lo tanto el JSON que debe ser entregado como respuesta por cada uno de los anuncios de donacin deber ser as&#58; 
&#160; 
 &#123; 
 id_referencia_donacion &#58; &#123;&#123;eatc_dona_headers.eatc-dona_header_code&#125;&#125;, 
 fecha_de_anuncio &#58; &#123;&#123;eatc_dona_headers.eatc-publication_datetime&#125;&#125;, 
 id_donador &#58; &#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;, 
 id_division &#58; &#123;&#123;eatc_dona_headers.eatc_donor_code&#125;&#125;, 
 division &#58; &#123;&#123;eatc_dona_headers.eatc_donor_fiscal_name&#125;&#125;, 
 id_cedis &#58; &#123;&#123;eatc_dona_headers.eatc_donor_code&#125;&#125; concat &#123;&#123;eatc_dona_headers.eatc-pod_id&#125;&#125; , 
 cedis &#58; &#123;&#123;eatc_dona_headers.eatc-pod_name&#125;&#125;, 
 id_banco &#58; &quot;&#123;&#123;url_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_dona_headers.eatc-donation_manager_code))&amp;_cmp=organizacion_vinculada&quot;, 
 banco &#58; &quot;&#123;&#123;url_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;id_banco))&amp;_cmp=organizacin&quot;, 
 &#123; 
 kg_origen &#58; &quot;&#123;&#123;eatc_dona.eatc-odd_original_quantity&#125;&#125; *&#123;&#123;eatc_dona.eatc-odd_unit_weight_kg&#125;&#125;&quot;, 
 kg_destino &#58; &quot;&#123;&#123;eatc_dona.eatc-eatc-odd_quantity&#125;&#125; *&#123;&#123;eatc_dona.eatc-odd_unit_weight_kg&#125;&#125;&quot;, 
 id_producto &#58; &#123;&#123;eatc_dona.eatc-odd_id&#125;&#125;, 
 nombre_producto &#58; &#123;&#123;eatc_dona.eatc-odd_name&#125;&#125;, 
 id_categoria &#58; &#123;&#123;eatc_dona.origin_odds_typology_a&#125;&#125;, 
 &#125;, 
 &#123;...&#125;, 

&#160; 
 fecha_de_acopio &#58; &quot;extract from datetime &#123;&#123;eatc_dona_headerseatc-picking_checkout_datetime&#125;&#125; date&quot;, 
 fecha_de_recepcion &#58; &quot;extract from datetime &#123;&#123;eatc_dona_headers.eatc-receipt_datetime&#125;&#125; date&quot;, 
 observaciones &#58; &#123;&#123;eatc_dona_headers.eatc-warning&#125;&#125;, 
 &#125; 

 6. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 El servicio responder con el JSON respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 DOWNLOADDONA: SERVICIO PARA DESCARGAR INFORMACIN DE LOS ANUNCIOS DE DONACIN