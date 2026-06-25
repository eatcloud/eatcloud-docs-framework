# matchexp-servicio-para-ampliación-del-match.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general del servicio 
 El presente servicio se especifica como parte del proyecto que est encaminado a mejorar y permitir auditar el match que se genera.&#160; Como parte del anlisis se determin partir el proceso del match (que anteriormente se realizaba mediante diversos procesos que no estaban claramente estructurados y por lo tanto representaban dificultades para el anlisis y la auditora) en tres procesos independientes&#58; 
&#160; 
 &#160;Clasificacin de las donaciones con respecto al match 
 Realizacin del registro del match de acuerdo a la clasificacin dada a la donacin&#160; 
 Ampliacin del match (el presente servicio) 
&#160; 
 En ese orden de ideas se debe implementar como un servicio privado (inicialmente invocado directamente desde la plataforma, pero puede darse el caso que a futuro se libere como un servicio pblico), cuyos endpoints, parmetros de invocacin y respuestas, se detallan en el siguiente documento (para tener en cuenta en la implementacin, las cualidades de autenticacin para acceder al servicio, podran obviarse en una primera implementacin, pero deben ser consideradas a futuro)&#58;&#160; 
&#160; 
 Documentacin servicio privado para ampliacin del match 
&#160; 
 Para evitar duplicidad en la documentacin, la implementacin del servicio deber basarse en dicha documentacin (si se deben hacer cambios se debe intervenir dicha documentacin), y a continuacin se explica lo que el servicio debe realizar con la informacin recibida. 

 LOG DEL SERVICIO 
&#160; 
 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros ) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 
&#160; 
 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;op&#58;false 

 1. VALIDACIN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de Parmetros del body de la peticin &#160; de la especificacin del servicio privado . Si lo son, seguir adelante con el prximo paso.&#160; Si no lo son deber entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIN DEL ESTADO DEL ANUNCIO (EL MATCH SOLO DEBE GENERARSE PARA ANUNCIOS EN ESTADO ANNOUNCED) 
 Con el dato que llega en los parmetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc-state= announced &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta ( validacin de datos de la donacin )&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta vlida el sistema sigue con la siguiente validacin&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; 00002203030033 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =00002203030033&amp; eatc-state= announced&amp;_cmp=_id &#160; &#160; 
&#160; 
 Dada la respuesta vlida que trae el servicio entonces el sistema permite seguir adelante. 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; exito72820220324122850387 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =exito72820220324122850387&amp; eatc-state= announced&amp;_cmp=_id &#160;&#160; &#160; 
&#160; 
&#160; 
 Dado que no se obtiene una respuesta vlida por parte del sistema entonces el sistema despliega la respuesta &quot; fail &quot;&#58; 

 3. CONSULTA DE LA REGLA DE AMPLIACIN DEL MATCH APLICABLES AL ANUNCIO 
 Con el dato que llega en el parmetro&#58; 
 eatc_match_asignation_rule 
&#160; 
 El sistema deber consultar las reglas de asignacin del match que le aplican al respectivo anuncio, segn su clasificacin previa, de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule=&#123;&#123; eatc_match_asignation_rule &#125;&#125; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Y deber generar una alerta a un grupo de Telegram en donde se exprese que esta regla de ampliacin del match no tiene registros. 
&#160; 
 Si la consulta arroja una respuesta vlida, a partir de los datos obtenidos y de los otros datos con que se realiza el llamado al servicio, se realizarn las consultas necesarias para escribir en el respectivo eatc_match_registry , como se establece ms adelante. 
&#160; 
 Ejemplo ambiente de pruebas, regla de asignacin&#58; eatc_match_asignation_rule&#58; &quot;abaco_exito_more_100_kg &quot; &#58; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule= abaco_exito_more_100_kg &#160; &#160; &#160; 
&#160; 
 El sistema obtiene la siguiente respuesta, la cual contendr datos para realizar la escritura del match&#58; 
 res &#58; 
 [ 
 &#123; 
 _id &#58; &quot;11&quot; , 
 eatc_match_expansion_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;_*&quot; , 
 eatc_param_value_desc &#58; &quot;Para esta clasificacin de donaciones se podr ampliar a todo tipo de organizaciones sociales&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;160&quot; , 
 eatc_expansion_lapse_in_minutes &#58; &quot;10&quot; , 
 eatc_expansion_radius &#58; &quot;7&quot; , 
 eatc_max_expansion_radius &#58; &quot;100&quot; 
 &#125; 
 ], 

 4. CONSULTA DE DATOS DE BENEFICIARIOS PARA EL REGISTRO DEL MATCH 
&#160; 
 Con los datos obtenidos en la anterior consulta, en particular&#58; 
&#160; 
 cua_code 
 eatc_match_asignation_rule 
 eatc_doma_param 
 eatc_doma_param_value 
 eatc_expansion_radius 
 eatc_max_expansion_radius 
&#160; 
 &#160;y los datos que llegan en los parmetros del llamado al servicio&#58; 
 cua_master 
 cua_user 
 eatc_dona_header_code 
 eatc_dona_lat 
 eatc_dona_lon 
 eatc_dona_total_weight_kg 
&#160; 
 El sistema deber realizar las siguientes operaciones&#58; 
&#160; 
 4.1. Consulta de beneficiarios bloqueados 
&#160; 
 Con los datos que llegan en los parmetros del llamado al servicio&#58; 
 cua_master 
 cua_user 
&#160; 
 El sistema deber consultar los beneficiarios que han sido bloqueados para la cuenta especfica, haciendo la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_blocked_doma?eatc_cua_master= &#123;&#123; cua_master &#125;&#125; &amp;eatc_donor= &#123;&#123; cua_user &#125;&#125; &amp;eatc_validity_block= activo &amp;_cmp= eatc_doma_id 
&#160; 
 Las organizaciones que tengan uno o varios registros activos en esta tabla, no se les debe generar el match con el respectivo donante y para ello se guardar un &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; &#160; que ser utilizado para realizar futuras consultas 
&#160; 
 Ejemplo&#58; ambiente de produccin , donante&#58; makro y cuenta maestra abaco 
&#160; 
 Se debe proceder a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_blocked_doma?eatc_cua_master=abaco&amp;eatc_donor=makro&amp;eatc_validity_block=activo&amp;_cmp= eatc_doma_id &#160; 
&#160; 
 Dado se obtiene como respuesta los valores &#58; &quot;9012728627&quot; &#160; y &quot; 900958453 &quot;, entonces el sistema almacena&#58; 
&#160; 
 &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; = 9012728627,900958453 

&#160; 
 4.2. Consulta de beneficiarios que hacen match segn reglas de ampliacin 
 Por cada regla especfica (identificada de manera nica por el dato&#58; eatc_match_expansion_rules. eatc_match_expansion_rule ) y tomando los datos; 
 eatc_doma_param 
 eatc_doma_param_value 
 eatc_timeout_from 
 eatc_timeout_in_minutes 
 eatc_expansion_lapse_in_minutes 
 eatc_expansion_radius 
 eatc_max_expansion_radius 
&#160; 
 y los datos que llegan en los parmetros del llamado al servicio&#58; 
&#160; 
 cua_master 
 eatc_dona_header_code 
 eatc_dona_lat 
 eatc_dona_lon 
 eatc_dona_total_weight_kg 
&#160; 
 El sistema deber realizar consultas como la que se expresa a continuacin ampliando progresivamente el radio de consulta, hasta llegar al radio mximo de expansin ( eatc_max_expansion_radius ). El nmero de ampliaciones progresiva ser igual el nmero entero ms prximo que corresponda a la divisin del mximo radio de expansin ( eatc_max_expansion_radius ) entre el radio de expansin ( eatc_expansion_radius ) 
&#160; 
 Ejemplo ambiente de pruebas, regla de asignacin&#58; eatc_match_asignation_rule&#58; &quot;abaco_exito_more_100_kg &quot; &#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule= abaco_exito_more_100_kg&amp;_cmp=eatc_max_expansion_radius,eatc_expansion_radius 
&#160; 
 El sistema obtiene la siguiente respuesta, la cual contendr datos para realizar la escritura del match&#58; 
&#160; 
 res &#58; 
 [ 
 &#123; 
 eatc_max_expansion_radius &#58; &quot;100&quot; 
 eatc_expansion_radius &#58; &quot;7&quot; , 

&#160; 
 &#125; 
 ], 
&#160; 
 Entonces el nmero de expansiones suscesivas ser igual a 100/7= 14,28 Siendo el entero ms prximo =14 (iteraciones o ampliaciones) 

&#160; 
 NOTA PARA EL DESARROLLO&#58; no se tiene conocimiento si los ltimos operadores lgicos implementados para el API tambin se implementaron para las consultas geogrficas (getpuntos), por lo tanto la siguiente notacin se expresa en los trminos de las pruebas lgicas implementadas para el API, y por lo tanto sera til extenderlas a las consultas &quot;getpuntos&quot; o reciclar scrpting de las validaciones del match legacy&#58; Exclusin del match a gestores de donacin bloqueados , Match por capacidad de recogida , Match por capacidad de gestin , 
 Se deja en la notacin una anotacin para empezar a visualizar cmo se puede controlar mejor la capacidad de gestin de las instituciones&#58; +sumatoria(peso_total_donaciones_asignadas_en_el_da_a_la_organizacion) 

&#160; 
eatc_match_expansion_rules. eatc_match_expansion_rule _sub_&#58;n 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/&#123;&#123; cua_master &#125;&#125;/getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = &#123;&#123; eaatc_dona_lat &#125;&#125; , &#123;&#123; eaatc_dona_lon &#125;&#125; &amp; showfield = identificador_unico_registro &amp; km = &#123;&#123; eatc_expansion_radius*( n ) &#125;&#125; &amp;filterfield_1= &#123;&#123; eatc_doma_param _sub_&#58;eatc_code &#125;&#125; &amp;filtervalue_1= &#123;&#123; eatc_doma_param_value _sub_&#58;eatc_code &#125;&#125; &amp;filterfield_2= capacidad_recogida &amp;filtervalue_2= _&gt;_ eatc_dona_total_weight_kg 
 &amp;filterfield_3= capacidad_gestion &amp;filtervalue_3= _&gt;_ ( eatc_dona_total_weight_kg +sumatoria(peso_total_donaciones_asignadas_en_el_da_a_la_organizacion) ) &amp;filterfield_4= identificador_unico_registro &amp;filtervalue_4= _nin_ &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; 

&#160; 
 Para calcular el timeout que le aplica a la respectiva expansin, se debe hacer el siguiente clculo 
&#160; 
 eatc_match_expansion_rule. eatc_timeout_in_minutes_sub_&#58;n 
 eatc_timeout_in_minutes+(eatc_expansion_lapse_in_minutes *(n - 1) ) 

&#160; 
 Por cada identificador nico de registro encontrado, se debe realizar la siguiente validacin (que por no tener clara una notacin al respecto simplemente se expresa verbalmente como se expres en la documentacin original del match), para revisar si se puede incluir en el vector de resultados&#58; 

&#160; 
 Match por disponibilidad&#58; 
 Se debe evaluar si a partir de la fecha y hora de la publicacin del anuncio ( eatc_dona_headers .eatc-publication_datetime) contando 24 horas, el gestor de donacin se encuentra en jornada de atencin a&#160; partir de los datos registrados en el maestro de gestores de donacin correspondientes a sus jornadas de atencin (jornada1, hora_inicio_jornada1, hora_fin_jornada1, jornada2, hora_inicio_jornada2, hora_fin_jornada2) . 
 Si el gestor de donaciones tiene una jornada que abarque cualquier segmento de las 24 horas contadas despus de la publicacin del anuncio, se debe guardar en una variable para probar los dems criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 de la cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress 
&#160; 
 Cuya fecha de publicacin ( eatc-publication_datetime) fue&#58; &quot;2019-09-18 15&#58;37&#58;54&quot; (mircoles), si se compara con el gestor de donaciones de la cuenta maestra &quot;abaco&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), que tiene jornada de atencin los das jueves de 08&#58;00&#58;00 a 17&#58;00&#58;00 ( jornada1 &#58; &quot;lu,ma,mi,ju,vi&quot;; hora_inicio_jornada1 &#58; &quot;08&#58;00&#58;0 hora_fin_jornada1 &#58; &quot;17&#58;00&#58;00&quot;),el proceso debe determinar que existe match por este criterio. 
&#160; 
 Match multipunto&#58; 
 Se estableci una nueva estructura de datos, en donde los&#160; Bancos de Alimentos, podrn definir mltiples puntos desde los cuales podrn realizar donaciones 
 El sistema debe calcular si el punto de donacin desde donde se genera el anuncio de donacin ( eatc_dona_headers &#58; eatc-lat, eatc-lon ), se encuentra a una distancia determinada despus de cierto tiempo (la idea es que de manera incremental se valla aumentando el radio de match), de los mltiples puntos que maneja cada gestor de donaciones. 

&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_doma_multipoint?_id=_* 
&#160; 
 eatc_doma_multipoint. eatc_lat y eatc_doma_multipoint. eatc_lon 
 Cuando se obtenga un match por este mtodo se deber llevar el dato adicional eatc_match_registry . eatc_pick_up_point_name con el dato que se obtiene del parmetro &#160; eatc_doma_multipoint. eatc_pick_up_point_name a partir de la consulta anterior 

&#160; 
 4.3. Armado de vector de resultados 
 Por cada eatc_donation_managers. identificador_unico_registro que van arrojando las consultas realizadas y los filtros aplicados, se debe armar un vector de resultados que contenga la siguiente informacin&#58; 
&#160; 
 eatc_donation_managers. identificador_unico_registro =&gt; que cumpli con los criterios del match segn las reglas 
 eatc_dona_header_code =&gt; a la cual se le est haciendo match (y que es uno de los parmetros de invocacin del servicio) 
 eatc_match_expansion_rule =&gt; que le aplic al anuncio (y que es uno de los parmetros de invocacin del servicio) 
 eatc_match_expansion_rule. cua_code =&gt; eatc_match_expansion_rules. eatc_match_expansion_rule _sub_&#58;n es decir a la iteracin de expansin correspondiente. 
 eatc_match_expansion_rule. eatc_asignation_order =&gt; correspondera al n o al nmero de la iteracin de expansin que se realiz 
 eatc_match_expansion_rule. eatc_timeout_in_minutes =&gt; que se obtuvo al consultar las reglas de expansin del match para el caso especfico&#58; eatc_match_expansion_rule. eatc_timeout_in_minutes_sub_&#58;n , Si la regla de asignacin del match anterior en el orden a la presente, no obtuvo un resultado (como se explica ms adelante), el timeout en minutos lo hereda la siguiente regla, siendo en este caso igual al timeout que tiene registrado la regla especfica que no obtuvo resultados y no el de la presente regla 

&#160; 
 Vector de resultados ante una regla de asignacin especfica sin resultados de match&#58; 
 Si para una regla especfica (eatc_match_asignation_rules. cua_code ) no se obtiene resultado, el vector deber contener la siguiente informacin&#58; 

&#160; 
 no_match =&gt; indica que no hubo un solo beneficiario que fuera encontrado por la regla especfica del match. 
 eatc_dona_header_code =&gt; a la cual se le est haciendo match (y que es uno de los parmetros de invocacin del servicio) 
 eatc_match_expansion_rule =&gt; que le aplic al anuncio (y que es uno de los parmetros de invocacin del servicio) 
 eatc_match_expansion_rule. cua_code =&gt; eatc_match_expansion_rules. eatc_match_expansion_rule _sub_&#58;n es decir a la iteracin de expansin correspondiente. 
 eatc_match_asignation_rules. eatc_asignation_order =&gt; n 
 eatc_match_asignation_rules. eatc_timeout_from =&gt; que se obtuvo al consultar las reglas de expansin del match para el caso especfico&#58; eatc_match_expansion_rule. eatc_timeout_in_minutes_sub_&#58;n 

&#160; 
 Esta informacin deber incorporarse en la respuesta del servicio exitosa . 
 Si ninguna de las reglas de match obtuvo resultados, se deber responder &quot;Registro no exitoso&quot; tal como se especifica en la respectiva documentacin , y deber generar una alerta a un grupo de Telegram. Tambin esto deber permitir realizar un llamado al servicio de ampliacin del match. 

 5. REGISTRO DEL MATCH 
&#160; 
 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
&#160; 
 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
&#160; 
 &#123;&#123; parmetros_insert_CRD &#125;&#125; 
 date_time = &#123;&#123;datetime_stamp&#125;&#125; 
 fecha_corta = &#123;&#123;date_stamp&#125;&#125; 
 eatc-dona_header_code= &#123;&#123; eatc_dona_header_code &#125;&#125; =&gt; Que proviene del (de los) vector(es) de resultados. 
 eatc-donation_manager_code= &#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125; =&gt; Que proviene del (de los) vector(es) de resultados. 
 matching_since = &#123;&#123;eatc_dona_headers.( eatc_match_expansion_rules. eatc_timeout_from) &#125;&#125; + &#123;&#123; eatc_match_expansion_rule. eatc_timeout_in_minutes_sub_&#58;n &#125;&#125; =&gt; A la fecha desde que se aplica el timeout del respectivo anuncio, se le suma el timeout en minutos que proviene del (de los) vector(es) de resultados. Este planteamiento quiere decir que el registro del match debe hacerse inmediatamente se publique el anuncio. &#160; **NUEVO CAMPO&#58; Este campo aun no est creado en la tabla de registro de match y se debe crear ** . 
 eatc_match_asignation_rule = &#123;&#123; eatc_match_expansion_rule &#125;&#125; que proviene del (de los) vector(es) de resultados. **NUEVO CAMPO&#58; Este campo aun no est creado en la tabla de registro de match y se debe crear ** . 
 eatc_match_asignation_rule_code = &#123;&#123; eatc_match_expansion_rule. cua_code &#125;&#125; que proviene del (de los) vector(es) de resultados. **NUEVO CAMPO&#58; Este campo aun no est creado en la tabla de registro de match y se debe crear ** . 

&#160; 
 NOTA PARA EL DESARROLLO&#58; los dems campos presentes en el registro del match, se debern llenar mediante procesos nocturnos, dado que no son requeridos de primera mano para la operacin del sistema, pero si para cuestiones anlticas que pueden correr con posterioridad. 

&#160; 
 Escritura con la API&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla=eatc_match_registry&amp;_operacion=insert &amp; &#123;&#123; parmetros_insert_CRD &#125;&#125; 

 7. R ESPUESTA EXISTOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si las actualizaciones de informacin realizadas por el servicio se realizan de manera adecuada, entonces entregar la respuesta&#58; 
 success 
&#160; 
 Y debe incluir datos de reglas de asignacin especificas que no tuvieron resultados en la ampliacin del match .&#160; Se debe generar una alerta a un grupo de Telegram con estas reglas especficas que no generen ampliacin del match. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MATCHEXP: SERVICIO PARA AMPLIACIN DEL MATCH