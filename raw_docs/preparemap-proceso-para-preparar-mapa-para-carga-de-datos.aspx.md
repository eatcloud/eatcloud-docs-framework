# preparemap-proceso-para-preparar-mapa-para-carga-de-datos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 INTRODUCCIN&#58; POR QU ES NECESARIO PREPARAR EL MAPA DE INFORMACIN? 
&#160; 
 Dado que cierta informacin es obligatoria de acuerdo a la evaluacin de la configuracin de la cuenta que la solicita, el objetivo de este proceso es consultar las reglas de obligatoriedad definidas en eatc_mandatory_info y as establecer si un campo es mandatorio o no para una cuenta en particular.&#160; De igual manera este proceso sirve para establecer los valores de informacin &quot; constante &quot; para la cuenta en cuestin, cuando se realiza una carga, o de informacin variable cuando se realiza dicho propsito. 
&#160; 
&#160; 
 LLAMADO AL SERVICIO 
 Se implementar un servicio que tenga la siguiente estructura&#58; 

&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; / preparemap / &#123;&#123;_DOM.cua_user&#125;&#125; ?eatc_objectstore= &#123;&#123;objectstore_a_mapear&#125;&#125; &amp;eatc_platform= &#123;&#123;platform&#125;&#125; &amp;tk= &#123;&#123;aut_token&#125;&#125; 
 ota &#58; el parmetro _compress es opcional, si se enva, la respuesta final del servicio se entrega comprimida y si no, se entrega descomprimida. 

&#160; 
 EJEMPLO&#58;&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ preparemap / ara ?eatc_objectstore= eatc_dona &amp;eatc_platform= wapp&#160; 
 https&#58;//beneficiarios.eatcloud.info/ preparemap / ara ?eatc_objectstore= eatc_dona &amp;eatc_platform= wapp&#160; 
&#160; 

&#160; 
 CONSULTAS DE INFORMACIN A REALIZAR 

&#160; 
 Cuando el servicio es invocado, se realizarn las siguientes consultas&#58; 
&#160; 
 Consulta de la informacin mandatoria 
 Al recibir el llamado el sistema debe tomar el objectstore informado y realizar la siguiente consulta de la informacin mandatoria&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_mandatory_info?eatc_objectstore= &#123;&#123;objectstore_a_mapear&#125;&#125; &amp;eatc_platform= &#123;&#123;platform&#125;&#125; 

&#160; 
 EJEMPLO&#58; ambiente de pruebas, eatc_objectstore =eatc_dona, eatc_platform =wapp 
 El llamado a realizar es el siguiente&#58;&#160; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp;eatc_platform =wapp &#160;&#160; 

&#160; 
 Consulta de la configuracin de la cuenta 
 Con el dato &#123;&#123;_DOM.cua_user&#125;&#125; se procede a realizar la sigiente consulta 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name= &#123;&#123;_DOM.cua_user&#125;&#125; 

&#160; 
 EJEMPLO&#58; ambiente de pruebas, eatc_cua=ara 
 El llamado a realizar es el siguiente&#58;&#160; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=ara &#160; 
&#160; 
&#160; 
 PREPARACIN DE INFORMACIN DEL MAPA DE DATOS 
&#160; 
 El sistema toma cada registro obtenido en la consulta a los datos mandatorios, y con los datos recibidos por parmetros y en la respectiva consulta va generando un registro en la estructura eatc_data_map de la siguiente manera&#58; 

&#160; 
 eatc_data_map. eatc_cua 
 Se llena con la informacin que proviene de la invocacin del servicio&#58; &#123;&#123;_DOM.cua_user&#125;&#125; 

&#160; 
 eatc_data_map. eatc_platform 
 Se llena con la informacin que proviene de la invocacin del servicio&#58; &#123;&#123;platform&#125;&#125; (el llamado puede tomar los valores &quot; wapp &quot;, &quot; bo &quot; o &quot; datagov &quot;) 

&#160; 
 eatc_data_map. eatc_objectstore 
 Se llena con la informacin que proviene de la invocacin del servicio&#58; &#123;&#123;objectstore_a_mapear&#125;&#125; 

&#160; 
 eatc_data_map. eatc_parameter 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_parameter 

&#160; 
 eatc_data_map. eatc_parameter_lbl 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_parameter_lbl 

&#160; 
 eatc_data_map. eatc_descripcion 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_descripcion 

&#160; 
 eatc_data_map. eatc_descripcion_lbl 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_descripcion_lbl 

&#160; 
 eatc_data_map. eatc_data_type 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_data_type 

&#160; 
 eatc_data_map. eatc_format 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_format 

&#160; 
&#160; 
 eatc_data_map. eatc_madatory_map 
&#160; 
 Cuando eatc_mandatory_info .eatc_madatory_map=&quot;y&quot; o &quot;n&quot; 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_madatory_map 

&#160; 
 Cuando eatc_mandatory_info .eatc_madatory_map=&quot;if&quot; 
 El sistema deber realizar la consulta de la informacin que se alberga en&#160; eatc_mandatory_info .eatc_mandatory_map_logical_proof para realizar la prueba lgica propuesta, utilizando los datos recibidos en la consulta de la configuracin de la cuenta y de esta manera establecer si la informacin es mandatoria o no. En trminos generales, en este campo deben quedar registros con valores &quot; y &quot; o &quot; n &quot; y no deben quedar valores &quot; if &quot; 

&#160; 
 Ejemplo 1&#58; Ambiente de pruebas&#58; eatc_cua =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter =eatc-odd_name 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info .eatc_mandatory_map_logical_proof de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter =eatc-odd_name&amp;_distinct=eatc_ mandatory_map_logical_proof &#160;&#160; &#160; &#160; 
&#160; 
 La respuesta obtenida es la siguiente&#58;&#160; 
&#160; 
 eatc_mandatory_map_logical_proof &#58; &quot;IF (&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;eatc_odds_app=eatc_odds&amp;_cont)&#58; count=1 n ELSE y&quot; 
&#160; 
 La anterior prueba plantea lo siguiente&#58; si en la configuracin de obtencin de los datos de los artculos en la wapp ( eatc_cua.eatc_odds_app ), se plantea que dichos datos se obtienen de un maestro de productos ( eatc_odds ) entonces no es requerido que en los datos del archivo plano nos entreguen un &quot;Nombre de producto&quot; porque el mismo se puede recuperar de un maestro de productos a partir del cdigo del producto . 
&#160; 
 Entonces el sistema debe realizar la prueba lgica establecida de acuerdo a los datos recibidos de la siguiente manera&#58; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_cua?name= ara &amp;eatc_odds_app=eatc_odds&amp;_cont &#160; 
&#160; 
 Dado que respuesta obtenida es la siguiente&#58;&#160; 
 count &#58; &quot;1&quot; 
&#160; 
 Lo que quiere decir que para la cuenta en cuestin existe un maestro de productos, del cual se pueden extractar los nombres de los artculos (que en particular es&#58; https&#58;//devdonantes.eatcloud.info/api/ara/eatc_odds?_id=_* ) . 
&#160; 
 Entonces el resultado de la prueba lgica es &quot; n &quot; y por lo tanto se lleva al registro de eatc_mandatory_info .eatc_madatory_map el valor &quot; n &quot; ( lo cual quiere decir que en mapeo que se realizar (o mejor dicho&#58; se complementar en la WAPP, en la funcionalidad de carga de donaciones a partir de archivos planos) no ser obligatorio que se mapee el campo con el nombre del producto, dado que el mismo se puede recuperar a partir de una consulta al maestro de artculos ( eatc_odds ), a partir del cdigo del producto ). 

&#160; 
 Ejemplo 2&#58; Ambiente de pruebas&#58; eatc_cua =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter =eatc-odd_unit_weight_kg 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info .eatc_mandatory_map_logical_proof de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp&amp; eatc_parameter =eatc-odd_unit_weight_kg&amp; _distinct =eatc_ mandatory_map_logical_proof &#160;&#160; &#160; &#160; 
&#160; 
 La respuesta obtenida es la siguiente&#58;&#160; 
&#160; 
 eatc_mandatory_map_logical_proof &#58; &quot;IF (&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;odds_weight=eatc_odds&amp;_cont)&#58; count=1 n ELSE y&quot; 
&#160; 
 La anterior prueba plantea lo siguiente&#58; si en la configuracin de obtencin de los datos del peso de los artculos en la wapp ( eatc_cua.odds_weight ), se plantea que dichos datos se obtienen de un maestro de productos ( eatc_odds ) entonces no es requerido que en los datos del archivo plano nos entreguen un &quot;el peso del producto&quot; porque el mismo se puede recuperar de un maestro de productos a partir del cdigo del mismo. 
&#160; 
&#160; 
 Entonces el sistema debe realizar la prueba lgica establecida de acuerdo a los datos recibidos de la siguiente manera&#58; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_cua?name= ara &amp;odds_weight=eatc_odds&amp;_cont &#160; 
&#160; 
 Dado que respuesta obtenida es la siguiente&#58;&#160; 
 count &#58; &quot;1&quot; 
&#160; 
 Lo que quiere decir que para la cuenta en cuestin existe un maestro de productos, del cual se pueden extractar los pesos de los artculos (que en particular es&#58; https&#58;//devdonantes.eatcloud.info/api/ara/eatc_odds?_id=_* ). 
&#160; 
 Entonces el resultado de la prueba lgica es &quot; n &quot; y por lo tanto se lleva al registro de eatc_mandatory_info .eatc_madatory_map el valor &quot; n &quot; (lo cual quiere decir que en mapeo que se realizar (o mejor dicho&#58; se complementar en la WAPP, en la funcionalidad de carga de donaciones a partir de archivos planos) no ser obligatorio que se mapee el campo con el con el peso unitario del producto, dado que el mismo se puede recuperar a partir de una consulta al maestro de artculos ( eatc_odds ), a partir del cdigo del producto). 
&#160; 
 eatc_data_map. eatc_requiered 
 Se llena con la informacin que proviene de la consulta de la informacin mandatoria y corresponde a eatc_mandatory_info .eatc_requiered 

&#160; 
 eatc_data_map. eatc_constant_validation 
 Se llena con la informacin que proviene del campo eatc_mandatory_info .eatc_constant_validation reemplazando los valores presentes en el llamado al servicio (preparemap). 
&#160; 
 Cuando eatc_mandatory_info .eatc_constant_validation=&quot;&quot; (vaco) 
 El campo se deja vaco. 
&#160; 
 Ejemplo 1&#58; Ambiente de pruebas&#58; eatc_cua =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter =eatc-odd_name 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_validation de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter =eatc-odd_name&amp;_distinct= eatc_alternative_constant_source &#160; 
&#160; 
 Entonces no se lleva nada al campo eatc_data_map. eatc_constant_value 

&#160; 
 Cuando eatc_mandatory_info .eatc_constant_validation es diferente de vaco 
&#160; 
 Se reemplazan los valores presentes en la validacin y que se obtienen en el llamado al servicio (preparemap) y se lleva la frmula de validacin con los valores reemplazados al registro. 
&#160; 
 Ejemplo 1&#58; Ambiente de pruebas&#58; &#123;&#123;_DOM.cua_user&#125;&#125; =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter = eatc-pod_id 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_validation de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter =eatc-pod_id&amp;_distinct= eatc_constant_validation &#160; &#160; 
&#160; 
 Que es la siguiente&#58; 
 IF (&#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_sub_pods?eatc_sub_pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_cont&#58; count=0) &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_distinct=eatc-id ELSE &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_sub_pods?eatc_sub_pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_distinct=eatc_pod_id 
&#160; 
 Entonces el sistema deber guardar para el caso especfico lo siguiente (reemplazando en donde corresponde los valores recibidos en la consulta del servicio) 
&#160; 
 IF ( https&#58;//devdonantes.eatcloud.info /api/ ara /eatc_sub_pods?eatc_sub_pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_cont&#58; count=0) https&#58;//devdonantes.eatcloud.info /api/ ara /eatc_pods?eatc-id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_distinct=eatc-id ELSE https&#58;//devdonantes.eatcloud.info /api/ ara /eatc_sub_pods?eatc_sub_pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;_distinct=eatc_pod_id 

&#160; 
 eatc_data_map. eatc_constant_formula 
 Se llena con la informacin que proviene del campo eatc_mandatory_info .eatc_constant_formula reemplazando los valores presentes en el llamado al servicio (preparemap). 
&#160; 
 Cuando eatc_mandatory_info .eatc_constant_formula=&quot;&quot; (vaco) 
&#160; 
 El campo se deja vaco. 
&#160; 
 Ejemplo 1&#58; Ambiente de pruebas&#58; eatc_cua =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter =eatc-odd_name 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_formula de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter =eatc-odd_name&amp;_distinct= eatc_constant_formula &#160;&#160; 
&#160; 
 Entonces no se lleva nada al campo eatc_data_map. eatc_constant_formula 

&#160; 
 Cuando eatc_mandatory_info .eatc_constant_formula es diferente de vaco 
 Se reemplazan los valores presentes en la frmula o llamado y que se obtienen en el llamado al servicio (preparemap) y se lleva la frmula con los valores reemplazados al registro. 
 Ejemplo 1&#58; Ambiente de pruebas&#58; &#123;&#123;_DOM.cua_user&#125;&#125; =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter = eatc-dona_header_code 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_formula de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter = eatc-dona_header_code &amp;_distinct= eatc_constant_formula &#160;&#160; &#160; &#160; 
&#160; 
 Que es la siguiente&#58; 
 &#123;&#123; _DOM.cua_user &#125;&#125;+&#123;&#123;eatc-pod_id&#125;&#125;+&#123;&#123;timestamp&#125;&#125; 
&#160; 
 Entonces el sistema deber guardar para el caso especfico lo siguiente (reemplazando en donde corresponde los valores recibidos en la consulta del servicio) 
&#160; 
 ara+&#123;&#123;eatc-pod_id&#125;&#125;+&#123;&#123;timestamp&#125;&#125; 
&#160; 
 eatc_data_map. eatc_constant_value 
 Se llena con la informacin que proviene del campo eatc_mandatory_info .eatc_constant_value &#160; reemplazando los valores presentes en el llamado al servicio (preparemap). 
&#160; 
 Cuando eatc_mandatory_info .eatc_constant_value=&quot;&quot; (vaco) 
 El campo se deja vaco. 
&#160; 
 Cuando eatc_mandatory_info .eatc_constant_value es un valor 
 Se reemplazan los valores presentes en la frmula o llamado y que se obtienen en el llamado al servicio (preparemap) y se lleva el resultado del llamado o frmula al registro. 
 Ejemplo 1&#58; Ambiente de pruebas&#58; &#123;&#123;_DOM.cua_user&#125;&#125; =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter = origen 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_value de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter = origen &amp;_distinct= eatc_constant_value &#160;&#160; &#160; &#160; 
&#160; 
 Que es la siguiente&#58; 
 flat_upload 
&#160; 
 Entonces el sistema deber guardar dicho valor al registro 
&#160; 
 flat_upload 
&#160; 
 Cuando eatc_mandatory_info .eatc_constant_value es una frmula o consulta 
 Se reemplazan los valores presentes en la frmula o llamado y que se obtienen en el llamado al servicio (preparemap) y se lleva el resultado del llamado o frmula al registro. 
 Ejemplo 1&#58; Ambiente de pruebas&#58; &#123;&#123;_DOM.cua_user&#125;&#125; =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter = eatc_cua_origin 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_constant_value de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter = eatc_cua_origin &amp;_distinct= eatc_constant_value &#160;&#160; &#160; &#160; 
&#160; 
 Que es la siguiente&#58; 
 &#123;&#123; _DOM.cua_user &#125;&#125; 
&#160; 
 Entonces el sistema deber guardar para el caso especfico lo siguiente (reemplazando en donde corresponde los valores recibidos en la consulta del servicio) 
&#160; 
 ara 

&#160; 
 eatc_data_map. eatc_variable_validation 
 Se llena con la informacin que proviene del campo eatc_mandatory_info .eatc_variable_validation y reemplazando los valores presentes en el llamado al servicio. 
&#160; 
 Cuando eatc_mandatory_info .eatc_variable_validation=&quot;&quot; (vaco) 
 El campo se deja vaco. 
&#160; 
 Cuando eatc_mandatory_info .eatc_variable_validation es una frmula o consulta 
 Se reemplazan los valores presentes en la frmula o llamado y que se obtienen en el llamado al servicio (preparemap) y se lleva el resultado del llamado o frmula al registro. 
 Este caso no se da presenta aun en los datos de posibles cargas realizadas hasta el momento, pero no se descarta que se presente en un futuro 

&#160; 
 eatc_data_map. eatc_variable_formula 
 Se llena con la informacin que proviene del campo eatc_mandatory_info .eatc_variable_formula y reemplazando los valores presentes en el llamado al servicio (preparemap). 
&#160; 
 Cuando eatc_mandatory_info .eatc_variable_formula=&quot;&quot; (vaco) 
 El campo se deja vaco. 
 Entonces no se lleva nada al campo eatc_data_map. eatc_constant_formula 

&#160; 
 Cuando eatc_mandatory_info .eatc_variable_formula es diferente de vaco 
 Se reemplazan los valores presentes en la frmula o llamado y que se obtienen en el llamado al servicio (preparemap) y se lleva la frmula o llamado con los valores reemplazados al registro. 
 Ejemplo 1&#58; Ambiente de pruebas&#58; eatc_cua =ara eatc_objectstore =eatc_dona eatc_platform =wapp y eatc_parameter =eatc-odd_name 
&#160; 
 El sistema trae la informacin contenida en eatc_mandatory_info . eatc_variable_formula de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore= eatc_dona &amp; eatc_platform =wapp &amp; eatc_parameter =eatc-odd_name&amp;_distinct= eatc_variable_formula &#160;&#160; 
&#160; 
 Que es la siguiente&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123;_DOM.cua_user&#125;&#125; /eatc_odds?eatc-id=&#123;&#123;eatc_dona.eatc-odd_id&#125;&#125;&amp;_distinct=eatc-odd_name 
&#160; 
 Entonces el sistema deber guardar para el caso especfico lo siguiente (reemplazando en donde corresponde los valores recibidos en la consulta del servicio) 
&#160; 
 https&#58;//devdonantes.eatcloud.info /api/ ara /eatc_odds?eatc-id=&#123;&#123;eatc_dona.eatc-odd_id&#125;&#125;&amp;_distinct=eatc-odd_name 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PREPAREMAP: PROCESO PARA PREPARAR MAPA DE DATOS PARA CARGA DE INFORMACIN EN ARCHIVO PLANO