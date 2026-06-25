# matchreg-servicio-para-registro-del-match.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general del servicio 
 El presente servicio se especifica como parte del proyecto que está encaminado a mejorar y permitir auditar el match que se genera.&#160; Como parte del análisis se determinó partir el proceso del match (que anteriormente se realizaba mediante diversos procesos que no estaban claramente estructurados y por lo tanto representaban dificultades para el análisis y la auditoría) en tres procesos independientes&#58; 
&#160; 
 &#160;Clasificación de las donaciones con respecto al match 
 Realización del registro del match de acuerdo a la clasificación dada a la donación (el presente servicio) 
 Ampliación del match 
&#160; 
 En ese orden de ideas se debe implementar como un servicio privado (inicialmente invocado directamente desde la plataforma, pero puede darse el caso que a futuro se libere como un servicio público), cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento (para tener en cuenta en la implementación, las cualidades de autenticación para acceder al servicio, podrían obviarse en una primera implementación, pero deben ser consideradas a futuro 
&#160; 
 Documentación servicio privado para registro del match 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 

 LOG DEL SERVICIO 
 El sistema deberá guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqué de un llamado no exitoso (datos incompletos, fallo de ejecución, fallos validación entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
&#160; 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;“op”&#58;”false” 

 1. VALIDACIÓN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación del servicio privado . Si lo son, seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIÓN DEL ESTADO DEL ANUNCIO (EL MATCH SOLO DEBE GENERARSE PARA ANUNCIOS EN ESTADO “ANNOUNCED”) 
 Con el dato que llega en los parámetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 El sistema deberá realizar la siguiente validación del punto de donación, antes de desplegarle la funcionalidad de captura de anuncios de donación&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc-state= announced &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta ( validación de datos de la donación )&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; 00002203030033 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =00002203030033&amp; eatc-state= announced&amp;_cmp=_id &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; exito72820220324122850387 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =exito72820220324122850387&amp; eatc-state= announced&amp;_cmp=_id &#160;&#160; &#160; 
&#160; 
&#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta &quot; fail &quot;&#58; 

 3. CONSULTA DE LAS REGLAS DE MATCH APLICABLES AL ANUNCIO 
 Con el dato que llega en el parámetro&#58; 
 eatc_match_asignation_rule 
&#160; 
 El sistema deberá consultar las reglas de asignación del match que le aplican al respectivo anuncio, según su clasificación previa, de la siguiente manera&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_match_asignation_rules?eatc_match_asignation_rule=&#123;&#123; eatc_match_asignation_rule &#125;&#125; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Y deberá generar una alerta a un grupo de Telegram en donde se exprese que esta regla de asignación del match no tiene registros. 
&#160; 
 Si la consulta arroja una respuesta válida, a partir de los datos obtenidos y de los otros datos con que se realiza el llamado al servicio, se realizarán las consultas necesarias para escribir en el respectivo eatc_match_registry, como se establece más adelante. 
&#160; 
 Ejemplo ambiente de pruebas, regla de asignación&#58; eatc_match_asignation_rule&#58; &quot;abaco_exito_more_100_kg &quot; &#58; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_match_asignation_rules?eatc_match_asignation_rule= abaco_exito_more_100_kg &#160; &#160; 
&#160; 
 El sistema obtiene la siguiente respuesta, la cual contendrá datos para realizar la escritura del match&#58; 
&#160; 
 res &#58; 
 [ 
 &#123; 
 _id &#58; &quot;40&quot; , 
 eatc_code &#58; &quot;abaco_exito_more_100_kg_o1&quot; , 
 eatc_match_asignation_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_asignation_order &#58; &quot;1&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;1&quot; , 
 eatc_param_value_desc &#58; &quot;Tiempo entre la generación de un anuncio de la cuenta “exito” de más de 100 KG y el match para organizaciones&#160; eatc_donation_managers&#160; cuyo eatc_typology_b es igual a 1&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;0&quot; , 
 eatc_min_radius &#58; &quot;30&quot; , 
 eatc_exclusive &#58; &quot;n&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;41&quot; , 
 eatc_code &#58; &quot;abaco_exito_more_100_kg_o2&quot; , 
 eatc_match_asignation_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_asignation_order &#58; &quot;2&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;5&quot; , 
 eatc_param_value_desc &#58; &quot;Tiempo entre la generación de un anuncio de la cuenta “exito” de más de 100 KG y el match para organizaciones&#160; eatc_donation_managers&#160; cuyo eatc_typology_b es igual a 5&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;100&quot; , 
 eatc_min_radius &#58; &quot;7&quot; , 
 eatc_exclusive &#58; &quot;n&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;42&quot; , 
 eatc_code &#58; &quot;abaco_exito_more_100_kg_o3&quot; , 
 eatc_match_asignation_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_asignation_order &#58; &quot;3&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;2&quot; , 
 eatc_param_value_desc &#58; &quot;Tiempo entre la generación de un anuncio de la cuenta “exito” de más de 100 KG y el match para organizaciones&#160; eatc_donation_managers&#160; cuyo eatc_typology_b es igual a 2&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;120&quot; , 
 eatc_min_radius &#58; &quot;7&quot; , 
 eatc_exclusive &#58; &quot;n&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;43&quot; , 
 eatc_code &#58; &quot;abaco_exito_more_100_kg_o4&quot; , 
 eatc_match_asignation_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_asignation_order &#58; &quot;4&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;3&quot; , 
 eatc_param_value_desc &#58; &quot;Tiempo entre la generación de un anuncio de la cuenta “exito” de más de 100 KG y el match para organizaciones&#160; eatc_donation_managers&#160; cuyo eatc_typology_b es igual a 3&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;140&quot; , 
 eatc_min_radius &#58; &quot;7&quot; , 
 eatc_exclusive &#58; &quot;n&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;44&quot; , 
 eatc_code &#58; &quot;abaco_exito_more_100_kg_o5&quot; , 
 eatc_match_asignation_rule &#58; &quot;abaco_exito_more_100_kg&quot; , 
 eatc_asignation_order &#58; &quot;5&quot; , 
 eatc_doma_param &#58; &quot;eatc_doma_typology_b&quot; , 
 eatc_doma_param_value &#58; &quot;4&quot; , 
 eatc_param_value_desc &#58; &quot;Tiempo entre la generación de un anuncio de la cuenta “exito” de más de 100 KG y el match para organizaciones&#160; eatc_donation_managers&#160; cuyo eatc_typology_b es igual a 4&quot; , 
 eatc_timeout_from &#58; &quot;eatc-publication_datetime&quot; , 
 eatc_timeout_in_minutes &#58; &quot;140&quot; , 
 eatc_min_radius &#58; &quot;7&quot; , 
 eatc_exclusive &#58; &quot;n&quot; 
 &#125; 
 ] 

 4. CONSULTA DE DATOS DE BENEFICIARIOS PARA EL REGISTRO DEL MATCH 
 Con los datos obtenidos en la anterior consulta, en particular&#58; 
&#160; 
 cua_code 
 eatc_match_asignation_rule 
 eatc_doma_param 
 eatc_doma_param_value 
 eatc_min_radius 
 eatc_exclusive 
&#160; 
 &#160;y los datos que llegan en los parámetros del llamado al servicio&#58; 
&#160; 
 cua_master 
 cua_user 
 eatc_dona_header_code 
 eatc_dona_lat 
 eatc_dona_lon 
 eatc_dona_total_weight_kg 
&#160; 
 El sistema deberá realizar las siguientes operaciones&#58; 
 4.0. ***NUEVO&#58; Consulta de beneficiarios con licencia &quot; suspension_pending &quot; *** 
El sistema deberá establecer aquellos beneficiarios cuya licencia ( eatc_donation_managers. eatc_license ) sea “ suspension_pending ” y a estos usuarios no se les generará match 
&#160; 
&#123;&#123;URL_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_license = suspension_pending &amp;_cmp=identificador_unico_registro 
 4.1. Consulta de beneficiarios bloqueados 
 Con los datos que llegan en los parámetros del llamado al servicio&#58; 
 cua_master 
 cua_user 
&#160; 
 El sistema deberá consultar los beneficiarios que han sido bloqueados para la cuenta específica, haciendo la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_blocked_doma?eatc_cua_master= &#123;&#123; cua_master &#125;&#125; &amp;eatc_donor= &#123;&#123; cua_user &#125;&#125; &amp;eatc_validity_block= activo &amp;_cmp= eatc_doma_id 
&#160; 
 Las organizaciones que tengan uno o varios registros activos en esta tabla, no se les debe generar el match con el respectivo donante y para ello se guardará un &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; &#160; que será utilizado para realizar futuras consultas 
&#160; 
 Ejemplo&#58; ambiente de producción , donante&#58; makro y cuenta maestra abaco 
 Se debe proceder a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_blocked_doma?eatc_cua_master=abaco&amp;eatc_donor=makro&amp;eatc_validity_block=activo&amp;_cmp= eatc_doma_id &#160; 
&#160; 
 Dado se obtiene como respuesta los valores &#58; &quot;9012728627&quot; &#160; y &quot; 900958453 &quot;, entonces el sistema almacena&#58; 
&#160; 
 &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; = 9012728627,900958453 

&#160; 
 4.2. Consulta de beneficiarios que hacen match según reglas de asignación 
 Por cada regla específica (identificada de manera única por el dato&#58; eatc_match_asignation_rules. cua_code ) y tomando los datos; 
&#160; 
 cua_code 
 eatc_match_asignation_rule 
 eatc_doma_param 
 eatc_doma_param_value 
 eatc_min_radius 
 eatc_exclusive 
&#160; 
 y los datos que llegan en los parámetros del llamado al servicio&#58; 
&#160; 
 cua_master 
 eatc_dona_header_code 
 eatc_dona_lat 
 eatc_dona_lon 
 eatc_dona_total_weight_kg 
 eatc_timeout_in_minutes 
&#160; 
 El sistema deberá realizar consultas como la que se expresa a continuación y en el orden que se establece en el campo&#58; eatc_match_asignation_rules. eatc_asignation_order 

&#160; 
 eatc_match_asignation_rules. cua_code _sub_&#58;eatc_asignation_order 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/&#123;&#123; cua_master &#125;&#125;/getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = &#123;&#123; eaatc_dona_lat &#125;&#125; , &#123;&#123; eaatc_dona_lon &#125;&#125; &amp; showfield = identificador_unico_registro &amp; km = &#123;&#123; eatc_min_radius _sub_&#58;eatc_code &#125;&#125; &amp;filterfield_1= &#123;&#123; eatc_doma_param _sub_&#58;eatc_code &#125;&#125; &amp;filtervalue_1= &#123;&#123; eatc_doma_param_value _sub_&#58;eatc_code &#125;&#125; &amp;filterfield_2= capacidad_recogida &amp;filtervalue_2= _&gt;_ eatc_dona_total_weight_kg 
 &amp;filterfield_3= capacidad_gestion &amp;filtervalue_3= _&gt;_ ( eatc_dona_total_weight_kg +sumatoria(peso_total_donaciones_asignadas_en_el_día_a_la_organizacion) ) &amp;filterfield_4= identificador_unico_registro &amp;filtervalue_4= _nin_ &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; 

&#160; 
 4.2.1. ***NUEVO&#58; envío de un parámetro y un valor o un parámetro y una variable en &quot;eatc_min_radius&quot; *** 
 A la fecha en el parámetro eatc_match_asignation_rules. eatc_min_radius se ha recibido un número, que permite operar las consultas georeferenciadas.&#160; Se deberá implementar la posibilidad de guardar en ese campo una dupla de &quot; parámetro=valor &quot; o &quot; parametro=valor1,valor2,..,valor(n) &quot;&#160; o una dupla parámetro=&#123;&#123; variable &#125;&#125; (que se conviene que esta variable estará asociada al anuncio de donación. De acuerdo a la notación, el sistema deberá buscar el valor correspondiente a la variable para el anuncio en cuestión y llevarlo a la consulta del match ) 
&#160; 
 Ejemplos&#58; 
 eatc_min_radius &#58; &quot; eatc_region=occidente,centro &quot; &#160; 
 eatc_min_radius &#58; &quot; eatc_contry_code=mx &quot; &#160; 
 eatc_min_radius &#58; &quot; eatc_region=&#123;&#123;eatc_dona_headers. eatc_region &#125;&#125; &quot;=&gt;PARAMETRO PENDIENTE DE CREAR 
&#160; 
 que al sistema identificar, que lo que llega no es un número, entonces procederá a filtrar directamente de la tabla &quot; eatc_donation_managers &quot; utilizando esta información como un parámetro y sus respectivos valores en la consulta de los gestores de donaciones, de la siguiente manera&#58; 
 eatc_match_asignation_rules. cua_code _sub_&#58;eatc_asignation_order 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_donation_managers ? &#123;&#123; eatc_doma_param _sub_&#58;eatc_code &#125;&#125; = &#123;&#123; eatc_doma_param_value _sub_&#58;eatc_code &#125;&#125;&amp;&#123;&#123; parametro_en&#58; eatc_min_radius_sub_&#58;eatc_code &#125;&#125;=&#123;&#123; valor(es)_en&#58; eatc_min_radius_sub_&#58;eatc_code &#125;&#125;&amp; capacidad_recogida = _&gt;_ eatc_dona_total_weight_kg 
 &amp; capacidad_gestion = _&gt;_ ( eatc_dona_total_weight_kg +sumatoria(peso_total_donaciones_asignadas_en_el_día_a_la_organizacion) )&amp; identificador_unico_registro = _nin_ &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; &amp;_cmp = identificador_unico_registro 
&#160; 
 O cuando lleguen variables&#58; 
&#160; 
 eatc_match_asignation_rules. cua_code _sub_&#58;eatc_asignation_order 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_donation_managers ? &#123;&#123; eatc_doma_param _sub_&#58;eatc_code &#125;&#125; = &#123;&#123; eatc_doma_param_value _sub_&#58;eatc_code &#125;&#125;&amp;&#123;&#123; parametro_en&#58; eatc_min_radius_sub_&#58;eatc_code &#125;&#125;=&#123;&#123; valor_correspondiente_a_la_variable_en &#58; eatc_min_radius_sub_&#58;eatc_code &#125;&#125;&amp; capacidad_recogida = _&gt;_ eatc_dona_total_weight_kg 
 &amp; capacidad_gestion = _&gt;_ ( eatc_dona_total_weight_kg +sumatoria(peso_total_donaciones_asignadas_en_el_día_a_la_organizacion) )&amp; identificador_unico_registro = _nin_ &#123;&#123; aray_beneficiarios_bloqueados &#125;&#125; &amp;_cmp = identificador_unico_registro 

&#160; 
 Por cada identificador único de registro encontrado, se debe realizar la siguiente validación (que por no tener clara una notación al respecto simplemente se expresa verbalmente como se expresó en la documentación original del match), para revisar si se puede incluir en el vector de resultados&#58; 

&#160; 
 Match por disponibilidad&#58; 
 Se debe evaluar si a partir de la fecha y hora de la publicación del anuncio ( eatc_dona_headers .eatc-publication_datetime) contando 24 horas, el gestor de donación se encuentra en jornada de atención a&#160; partir de los datos registrados en el maestro de gestores de donación correspondientes a sus jornadas de atención (jornada1, hora_inicio_jornada1, hora_fin_jornada1, jornada2, hora_inicio_jornada2, hora_fin_jornada2) . 
 Si el gestor de donaciones tiene una jornada que abarque cualquier segmento de las 24 horas contadas después de la publicación del anuncio, se debe guardar en una variable para probar los demás criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 de la cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress 
&#160; 
 Cuya fecha de publicación ( eatc-publication_datetime) fue&#58; &quot;2019-09-18 15&#58;37&#58;54&quot; (miércoles), si se compara con el gestor de donaciones de la cuenta maestra &quot;abaco&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), que tiene jornada de atención los días jueves de 08&#58;00&#58;00 a 17&#58;00&#58;00 ( jornada1 &#58; &quot;lu,ma,mi,ju,vi&quot;; hora_inicio_jornada1 &#58; &quot;08&#58;00&#58;0 hora_fin_jornada1 &#58; &quot;17&#58;00&#58;00&quot;),el proceso debe determinar que existe match por este criterio. 
&#160; 
 Match multipunto&#58; 
 Se estableció una nueva estructura de datos, en donde los&#160; Bancos de Alimentos, podrán definir múltiples puntos desde los cuales podrán realizar donaciones 
&#160; 
 El sistema debe calcular si el punto de donación desde donde se genera el anuncio de donación ( eatc_dona_headers &#58; eatc-lat, eatc-lon ), se encuentra a una distancia determinada después de cierto tiempo (la idea es que de manera incremental se valla aumentando el radio de match), de los múltiples puntos que maneja cada gestor de donaciones. 

&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_doma_multipoint?_id=_* 
&#160; 
 eatc_doma_multipoint. eatc_lat y eatc_doma_multipoint. eatc_lon 
 Cuando se obtenga un match por este método se deberá llevar el dato adicional eatc_match_registry . eatc_pick_up_point_name con el dato que se obtiene del parámetro &#160; eatc_doma_multipoint. eatc_pick_up_point_name a partir de la consulta anterior 

&#160; 
 4.3. Armado de vector de resultados ***NUEVO&#58; ajuste de timeout ante reglas que no hacen match *** 
 Por cada eatc_donation_managers. identificador_unico_registro que van arrojando las consultas realizadas y los filtros aplicados, se debe armar un vector de resultados que contenga la siguiente información&#58; 
&#160; 
 eatc_donation_managers. identificador_unico_registro =&gt; que cumplió con los criterios del match según las reglas 
 eatc_dona_header_code =&gt; a la cual se le está haciendo match (y que es uno de los parámetros de invocación del servicio) 
 eatc_match_asignation_rule =&gt; que le aplicó al anuncio (y que es uno de los parámetros de invocación del servicio) 
 eatc_match_asignation_rules. cua_code =&gt; con el cual se obtuvo el respectivo donante como match. 
 eatc_match_asignation_rules. eatc_asignation_order =&gt; que se obtuvo al consultar las reglas de asignación del match para el caso específico 
 eatc_match_asignation_rules. eatc_timeout_in_minutes =&gt; que se obtuvo al consultar las reglas de asignación del match para el caso específico, Si la regla de asignación del match anterior en el orden a la presente, no obtuvo un resultado (como se explica más adelante), el timeout en minutos lo hereda la siguiente regla, siendo en este caso igual al timeout que tiene registrado la regla específica que no obtuvo resultados y no el de la presente regla 

&#160; 
 Vector de resultados ante una regla de asignación específica sin resultados de match&#58; 
 Si para una regla específica (eatc_match_asignation_rules. cua_code ) no se obtiene resultado, el vector deberá contener la siguiente información&#58; 

&#160; 
 no_match =&gt; indica que no hubo un solo beneficiario que fuera encontrado por la regla específica del match. 
 eatc_dona_header_code =&gt; a la cual se le está haciendo match (y que es uno de los parámetros de invocación del servicio) 
 eatc_match_asignation_rule =&gt; que le aplicó al anuncio (y que es uno de los parámetros de invocación del servicio) 
 eatc_match_asignation_rules. cua_code =&gt; con el cual se obtuvo el respectivo donante como match. 
 eatc_match_asignation_rules. eatc_asignation_order =&gt; que se obtuvo al consultar las reglas de asignación del match para el caso específico 
 eatc_match_asignation_rules. eatc_timeout_from =&gt; que se obtuvo al consultar las reglas de asignación del match para el caso específico 

&#160; 
 Esta información deberá incorporarse en la respuesta del servicio exitosa . 
 Si ninguna de las reglas de match obtuvo resultados, se deberá responder &quot;Registro no exitoso&quot; tal como se especifica en la respectiva documentación , y deberá generar una alerta a un grupo de Telegram. También esto deberá permitir realizar un llamado al servicio de ampliación del match. 

 5. REGISTRO DEL MATCH 

 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
&#160; 
 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 date_time = &#123;&#123;datetime_stamp&#125;&#125; 
 fecha_corta = &#123;&#123;date_stamp&#125;&#125; 
 eatc-dona_header_code= &#123;&#123; eatc_dona_header_code &#125;&#125; =&gt; Que proviene del (de los) vector(es) de resultados. 
 eatc-donation_manager_code= &#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125; =&gt; Que proviene del (de los) vector(es) de resultados. 
 matching_since = &#123;&#123;datetime_stamp&#125;&#125; + &#123;&#123; eatc_match_asignation_rules. eatc_timeout_in_minutes &#125;&#125; =&gt; A la fecha y hora actual se le suma el timeout en minutos que proviene del (de los) vector(es) de resultados. Este planteamiento quiere decir que el registro del match debe hacerse inmediatamente se publique el anuncio. 
 eatc_match_asignation_rule = &#123;&#123; eatc_match_asignation_rule &#125;&#125; que proviene del (de los) vector(es) de resultados. 
 eatc_match_asignation_rule_code = &#123;&#123; eatc_match_asignation_rules. cua_code &#125;&#125; que proviene del (de los) vector(es) de resultados. 

&#160; 
 NOTA PARA EL DESARROLLO&#58; los demás campos presentes en el registro del match, se deberán llenar mediante procesos nocturnos, dado que no son requeridos de primera mano para la operación del sistema, pero si para cuestiones análíticas que pueden correr con posterioridad. 

&#160; 
 Escritura con la API&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla=eatc_match_registry&amp;_operacion=insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 6. LLAMADO AL SERVICIO DE AMPLIACIÓN DEL MATCH 
 Una vez se termina de registrar el match, se realiza el llamado al servicio de ampliación del match . 

 7. RESPUESTA EXISTOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si las actualizaciones de información realizadas por el servicio se realizan de manera adecuada, entonces entregará la respuesta&#58; 
 success 
&#160; 
 Y debe incluir datos de reglas de asignación especificas que no tuvieron resultados del match .&#160; Se debe generar una alerta a un grupo de Telegram con estas reglas específicas que no generen match. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 c58b43d8-c705-4a04-bf5f-527fb6ebf198 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 1e290386-f861-4872-9104-6b813adc344c 
 2025-11-06T05:25:48.4866588Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"5e6e784e-cc9d-4505-bef3-7243c4594450","SequenceId":655,"FluidContainerCustomId":"855888da-8881-4565-b09a-4807daf8e0ea","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 MATCHREG SERVICIO PARA REGISTRO DEL MATCH