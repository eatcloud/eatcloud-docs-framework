# match-de-anuncios-de-donacion-con-gestores-de-donacion.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Proceso mediante el cual el sistema define si un anuncio de donacin en particular ( eatc_dona_headers )&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?_id=_* 
&#160; 
 es asignable a un gestor de donaciones&#58; ( eatc_donation_managers )&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_donanation_managers?_id=_* 
&#160; 
 por criterios de cercana, afinidad, capacidad de recogida, capacidad de gestin y disponibilidad.&#160; El sistema ha dispuesto una estructura muy simple para registrar este match . 

 ***NUEVO*** Match dinmico para diferentes cuentas maestras&#58; 
 El proceso de match debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 
&#160; 
 Este ajuste aplica tanto para los procesos de match activados por tareas programadas como los que son activados mediante servicios web 

 ***NUEVO*** Exclusin del match a gestores de donacin bloqueados&#58; 
 Para cada cuenta maestra &#123;&#123;_DOM. cua_master &#125;&#125; y donante &#123;&#123;_DOM. cua_user &#125;&#125; , se deber establecer que gestores de donacin estn bloqueados, haciendo la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_blocked_doma?eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_donor= &#123;&#123;_DOM. cua_user &#125;&#125; &amp;eatc_validity_block= activo &#160; 
&#160; 
 Las organizaciones que tengan uno o varios registros activos en esta tabla, no se les debe generar el match con el respectivo donante. 

&#160; 
 Ejemplo&#58; ambiente de produccin , donante&#58; makro y cuenta maestra abaco 
 Se debe proceder a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_blocked_doma?eatc_cua_master=abaco&amp;eatc_donor=makro&amp;eatc_validity_block=activo &#160; 
&#160; 
 Dado que la organizacin identificada con &quot; eatc_doma_id &#58; &quot;9012728627&quot; &#160; aparece en la bsqueda, a esta organizacin se le debe excluir del match con la donaciones producidas por makro . Para los dems donantes el match se debe realizar sin inconvenientes. 

 Match por capacidad de recogida ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
 Para cada anuncio de donacin, se debe comparar su peso total ( eatc_dona_headers .eatc-total_weight_kg) con el valor capacidad de recogida ( eatc_donation_managers .capacidad_recogida).&#160;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_donanation_managers?capacidad_recogida &gt;=&#123;&#123; eatc_dona_headers .eatc-total_weight_kg&#125;&#125; 
&#160; 
 Si el gestor de donaciones tiene una capacidad igual o mayor al peso total del anuncio de donacin se debe guardar en una variable para probar los dems criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 ( que debe estar en estado eatc_state=announced) de la cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 
&#160; 
 Cuyo peso total es de 1000 kg ( eatc-total_weight_kg &#58; &quot;1000&quot;),si se compara con el gestor de donaciones &quot;abaco&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), cuya capacidad de recogida es de 4500 KG ( capacidad_recogida &#58; &quot;4500&quot;), el proceso debe determinar que existe match por este criterio. 

 Match por capacidad de gestin ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
 Para cada anuncio de donacin, se debe comparar su peso total ( eatc_dona_headers .eatc-total_weight_kg) con el valor capacidad de recogida ( eatc_donation_managers .capacidad_gestion).&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_donanation_managers?capacidad_gestion &gt;=&#123;&#123; eatc_dona_headers .eatc-total_weight_kg&#125;&#125; 
&#160; 
 Si el gestor de donaciones tiene una capacidad igual o mayor al peso total del anuncio de donacin se debe guardar en una variable para probar los dems criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012&#160; ( que debe estar en estado eatc_state=announced) 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 
&#160; 
 Cuyo peso total es de 1000 kg ( eatc-total_weight_kg &#58; &quot;1000&quot;),si se compara con el gestor de donaciones &quot;ABACO&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), cuya capacidad de gestin es de 4500 KG ( capacidad_gestion &#58; &quot;4500&quot;), el proceso debe determinar que existe match por este criterio. 

 Match por disponibilidad ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
 Se debe evaluar si a partir de la fecha y hora de la publicacin del anuncio ( eatc_dona_headers .eatc-publication_datetime) contando 24 horas, el gestor de donacin se encuentra en jornada de atencin a&#160; partir de los datos registrados en el maestro de gestores de donacin correspondientes a sus jornadas de atencin (jornada1, hora_inicio_jornada1, hora_fin_jornada1, jornada2, hora_inicio_jornada2, hora_fin_jornada2) . 
&#160; 
 Si el gestor de donaciones tiene una jornada que abarque cualquier segmento de las 24 horas contadas despus de la publicacin del anuncio, se debe guardar en una variable para probar los dems criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 de la cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 
&#160; 
 Cuya fecha de publicacin ( eatc-publication_datetime) fue&#58; &quot;2019-09-18 15&#58;37&#58;54&quot; (mircoles), si se compara con el gestor de donaciones de la cuenta maestra &quot;abaco&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), que tiene jornada de atencin los das jueves de 08&#58;00&#58;00 a 17&#58;00&#58;00 ( jornada1 &#58; &quot;lu,ma,mi,ju,vi&quot;; hora_inicio_jornada1 &#58; &quot;08&#58;00&#58;0 hora_fin_jornada1 &#58; &quot;17&#58;00&#58;00&quot;),el proceso debe determinar que existe match por este criterio. 

 Match por cercana ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
 El sistema debe calcular si el punto de donacin desde donde se genera el anuncio de donacin ( eatc_dona_headers &#58; eatc-lat, eatc-lon), se encuentra a una distancia determinada despus de cierto tiempo (la idea es que de manera incremental se valla aumentando el radio de match), del gestor de donaciones&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_donanation_managers?_id=_* coordenadas 
&#160; 
 La idea es que las reglas de temporalidad y distancia en kilmetros del match sean paramtricas ( es decir, que se puedan ajustar peridicamente, mediante un parmetro de sistema y que no estn quemadas en los scripts ). Una primera propuesta sera&#58; 

 Match por cercana ***NUEVO*** multipunto&#58; 
 Se estableci una nueva estructura de datos, en donde los&#160; Bancos de Alimentos, podrn definir mltiples puntos desde los cuales podrn realizar donaciones 
&#160; 
 El sistema debe calcular si el punto de donacin desde donde se genera el anuncio de donacin ( eatc_dona_headers &#58; eatc-lat, eatc-lon ), se encuentra a una distancia determinada despus de cierto tiempo (la idea es que de manera incremental se valla aumentando el radio de match), de los mltiples puntos que maneja cada gestor de donaciones. 

&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_doma_multipoint?_id=_* 
&#160; 
 eatc_doma_multipoint. eatc_lat y eatc_doma_multipoint. eatc_lon 
&#160; 
 Cuando se obtenga un match por este mtodo se deber llevar el dato adicional eatc_match_registry . eatc_pick_up_point_name con el dato que se obtiene del parmetro &#160; eatc_doma_multipoint. eatc_pick_up_point_name a partir de la consulta anterior&#58; 

&#160; 
 Escritura con la API&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/ &#123;&#123; _DOM .cua_master&#125;&#125; /?_tabla= eatc_match_registry &amp;_operacion=insert&amp; date_time =&#123;&#123;timestamp&#125;&#125; &amp; eatc-dona_header_code =&#123;&#123;VALOR&#125;&#125;&amp; eatc-donation_manager_code = &#123;&#123; eatc_doma_multipoint. eatc_doma_id &#125;&#125;&amp; eatc-pod_id = &#123;&#123;VALOR&#125;&#125;&amp; eatc-pod_name =&#123;&#123;VALOR&#125;&#125;&amp; eatc-donation_manager_nam e=&#123;&#123; eatc_doma_multipoint. eatc_doma_name &#125;&#125;&amp; eatc_pick_up_point_name =&#123;&#123; eatc_doma_multipoint . eatc_pick_up_point_name&#125;&#125; 

 Los gestores de donacin que vallan cumpliendo la regla de match, se deben guardar en una variable para probar los dems criterios de match antes de registrarlo en la estructura definida para ese fin. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 
&#160; 
 Cuya fecha de publicacin cuya ubicacin corresponde a eatc-lat &#58; &quot;6.25512&quot;, eatc-lon &#58; &quot;-75.558275&quot;, si se compara con el gestor de donaciones de la cuenta maestra &quot;abaco&quot; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1 ), cuya ubicacin es coordenadas &#58; &quot;4.621306, -74.089891&quot;,el proceso debe determinar que en ninguno de los tres intentos con diferentes distancias en KM se obtiene match. 

 Match por afinidad (standby)&#58; 
 Inicialmente no se han definido muy bien los criterios para generar este match.&#160; Debera establecerse una manera (quizs a travs del mapeo de clasificaciones de productos) para establecer si un anuncio de donacin es apto para un grupo poblacional.&#160; Igualmente la informacin inicialmente suministrada de los gestores de donacin no permite realizar bien la prueba (porque se enviaron con afinidad a todos los grupos). Conforme se valla avanzando en el piloto se debe revisar este match 

 Match Escalonado ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
 En la plataforma se han definido reglas de timeout, asociadas a la tipologa b de los gestores de donacin&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b 
&#160; 
 de tal manera que el sistema pueda evaluar un tiempo determinado para realizarle match a un anuncio, a partir de la evaluacin del tipo de gestor de donaciones ( eatc-doma_typolgy_b ).&#160; A esta regla tambin se le puede establecer un peso a partir del cual debe&#160; funcionar ( eatc-since_kg ), para que donaciones por debajo de ese peso no les aplique la regla y se pueda hacer match de manera inmediata. 

&#160; 
 Primer match 
 El sistema lee la cuenta desde la cual se genera el anuncio y con ella lee las reglas de timeout que les corresponde ( eatc_timeout_rules. cua ), si no encuentra registro utilizar el dato _default para leer los datos.&#160; Luego toma aquellos cuyo eatc-timeout_in_minutes sea igual a cero, para luego buscar las la tipologa de de las organizaciones ( eatc_timeout_rules. eatc-doma_typolgy_b ) con las cuales se puede hacer match para realizarlo. 

&#160; 
 Ejemplo 1&#58; cuenta con registro particular 
 Para un anuncio de la cuenta menusolidario el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= menusolidario&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=menusolidario&amp;eatc-timeout_in_minutes=0 &#160; 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=menusolidario&amp;eatc-timeout_in_minutes=0 
&#160; 
 Como la consulta trae datos&#58; 
 &#123; 
 _id &#58; &quot;42&quot;, 
 eatc-code &#58; &quot;13&quot;, 
 cua &#58; &quot;menusolidario&quot;, 
 eatc-timeout_name &#58; &quot;eatc_doma_typolgy_b&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 4 cuando el donante es menusolidario&quot;, 
 eatc-timeout_in_minutes &#58; &quot;0&quot;, 
 eatc-timeout_in_hours &#58; &quot;0&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot;, 
 eatc-doma_typolgy_b &#58; &quot;4&quot;, 
 eatc-since_kg &#58; &quot;0&quot; 
 &#125; 
&#160; 
 Se realiza el primer match con las organizaciones cuya tipologa b ( eatc-doma_typolgy_b ) es igual a 4. 

&#160; 
 Ejemplo 2&#58; cuenta sin registro de timeout 
 Para un anuncio de la cuenta alqueria el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= alqueria&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160;&#160; 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160; 
&#160; 
 Como la consulta no trae datos datos ( err_msg &#58; &quot;No se produjeron resultados&quot;), se procede a realizar la consulta con el parmetro _default 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= _default&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-timeout_in_minutes=0 &#160;&#160;&#160; 
&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-timeout_in_minutes=0 &#160; 
&#160; 
 Dado que la consulta _default, trae datos&#58; 
 &#123; 
 _id &#58; &quot;16&quot;, 
 eatc-code &#58; &quot;9&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;eatc_doma_typolgy_b&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 1&quot;, 
 eatc-timeout_in_minutes &#58; &quot;0&quot;, 
 eatc-timeout_in_hours &#58; &quot;0&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot;, 
 eatc-doma_typolgy_b &#58; &quot;1&quot;, 
 eatc-since_kg &#58; &quot;20&quot; 
 &#125; 
&#160; 
 Se realiza el primer match con las organizaciones cuya tipologa b ( eatc-doma_typolgy_b ) es igual a 1 siempre y cuando el peso sea mayor a 20 KG (para las donaciones de menos de 20 KG se procede a realizar el match por distancia. 

&#160; 
 Match posteriores 
 En procesos de cron, que se disparan peridicamente, el sistema evala la fecha y hora actual y define si se ha cumplido el tiempo en minutos para ir aplicando las dems reglas de match presentes en los respectivos registros de timeout, teniendo en cuenta la lgica anteriormente definida. 

 [NUEVO] Match Escalonado incluyendo reglas por ciudades ***NUEVO*** dinamizar segn diversas cuentas maestras&#58; 
&#160; 
 Implementacin previa&#58; 
 Como primera medida antes de esta implementacin, se implementar el registro de eatc-city en el eatc_dona_headers , a fin de tener datos ms a la mano para realizar los clculos. 
&#160; 
 Adicin del parmetro eatc-city a la estructura del timeout&#58; 
 Se adicion el parmetro eatc-city a la estructura de datos eatc_timeout_rules y principalmente este dato operar para el timeout eatc_doma_typolgy_b &#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b 
&#160; 
 de tal manera que el sistema pueda evaluar un tiempo determinado para realizarle match a un anuncio, a partir de la evaluacin del tipo de gestor de donaciones ( eatc-doma_typolgy_b ), teniendo en cuenta tambin la ciudad del anuncio ( eatc-city ).&#160; A esta regla tambin se le puede establecer un peso a partir del cual debe&#160; funcionar ( eatc-since_kg ), para que donaciones por debajo de ese peso no les aplique la regla y se pueda hacer match de manera inmediata.&#160; Por regla general, siempre habr prelacin para las definiciones de eatc_doma_typolgy_b estipuladas para una cuenta, y luego (de manera subordinada) aplicarn la de ciudad. Por eso siempre se evala primero al cuenta ( cua ) y luego en segunda instancia la ciudad ( eatc-city ) 

&#160; 
 Primer match 
 El sistema lee la cuenta desde la cual se genera el anuncio y con ella lee las reglas de timeout que les corresponde ( eatc_timeout_rules. cua ), si no encuentra registro utilizar el dato _default para leer los datos.&#160; Luego toma aquellos cuyo eatc-timeout_in_minutes sea igual a cero, para luego buscar las la tipologa de de las organizaciones ( eatc_timeout_rules. eatc-doma_typolgy_b ) con las cuales se puede hacer match para realizarlo. 

&#160; 
 Ejemplo 1&#58; cuenta con registro particular de timeout (que debe tener prelacin) 
 Para un anuncio de la cuenta menusolidario el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= menusolidario&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=menusolidario&amp;eatc-timeout_in_minutes=0 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=menusolidario&amp;eatc-timeout_in_minutes=0 &#160; 
&#160; 
 Como la consulta trae datos&#58; 
 &#123; 
 _id &#58; &quot;42&quot;, 
 eatc-code &#58; &quot;13&quot;, 
 cua &#58; &quot;menusolidario&quot;, 
 eatc-timeout_name &#58; &quot;eatc_doma_typolgy_b&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 4 cuando el donante es menusolidario&quot;, 
 eatc-timeout_in_minutes &#58; &quot;0&quot;, 
 eatc-timeout_in_hours &#58; &quot;0&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot;, 
 eatc-doma_typolgy_b &#58; &quot;4&quot;, 
 eatc-since_kg &#58; &quot;0&quot; 
 &#125; 
&#160; 
 Se realiza el primer match con las organizaciones cuya tipologa b ( eatc-doma_typolgy_b ) es igual a 4. 

&#160; 
 Ejemplo 2&#58; cuenta sin registro de timeout y con registro para una ciudad especfica 
&#160; 
 Suponiendo que se realiza un anuncio de la cuenta alqueria en la ciudad de CALI el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= alqueria&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160;&#160; 
&#160; 
 Como la consulta no trae datos datos ( err_msg &#58; &quot;No se produjeron resultados&quot; ), se procede a realizar la consulta con el parmetro _default , y el parmetro eatc-city =CALI 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= _default&amp; eatc-city =CALI&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-city=CALI&amp;eatc-timeout_in_minutes=0 &#160;&#160;&#160;&#160;&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-city=CALI&amp;eatc-timeout_in_minutes=0 &#160;&#160;&#160; 
&#160; 
 Dado que la anterior consulta trae datos&#58; 
 &#123; 
 _id &#58; &quot;44&quot;, 
 eatc-code &#58; &quot;21&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;eatc_doma_typolgy_b&quot;, 
 eatc-timeout_description &#58; &quot;En la ciudad de Cali, el Banco de Alimentos podr ver las donaciones desde 0 KG de manera inmediata y exclusiva por dos horas&quot;, 
 eatc-timeout_in_minutes &#58; &quot;0&quot;, 
 eatc-timeout_in_hours &#58; &quot;0&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot;, 
 eatc-doma_typolgy_b &#58; &quot;1&quot;, 
 eatc-since_kg &#58; &quot;0&quot;, 
 eatc-city &#58; &quot;CALI&quot; 
 &#125; 
&#160; 
 Se realiza el primer match con las organizaciones cuya tipologa b ( eatc-doma_typolgy_b ) es igual a 1 (sin importar el peso de la donacin). 

&#160; 
 Ejemplo 3&#58; cuenta sin registro de timeout y sin registro para una ciudad especfica 
&#160; 
 Para un anuncio de la cuenta alqueria en la ciudad de MEDELLIN el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= alqueria&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160;&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=alqueria&amp;eatc-timeout_in_minutes=0 &#160; 
&#160; 
 Como la consulta no trae datos datos ( err_msg &#58; &quot;No se produjeron resultados&quot;), se procede a realizar la consulta con el parmetro _default , y el parmetro eatc-city =MEDELLIN 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= _default&amp; eatc-city =MEDELLIN&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default &amp; eatc-city =MEDELLIN &amp;eatc-timeout_in_minutes=0 &#160;&#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default &amp; eatc-city =MEDELLIN &amp;eatc-timeout_in_minutes=0 &#160;&#160;&#160;&#160; 
&#160; 
 Dado que esta nueva consulta, tampoco trae datos ( err_msg &#58; &quot;No se produjeron resultados&quot; ), se procede a realizar una tercera consulta ahora sin el parmetro eatc-city =MEDELLIN 
 &#123;&#123;URL_entorno _donantes &#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name= eatc_doma_typolgy_b &amp;cua= _default&amp; eatc-timeout_in_minutes=0 
&#160; 
 Ambiente productivo (CUA_master=abaco) &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-timeout_in_minutes=0 &#160; 
 Ambiente de pruebas (CUA_master=abaco) &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=eatc_doma_typolgy_b&amp;cua=_default&amp;eatc-timeout_in_minutes=0 &#160;&#160;&#160; 
&#160; 
 Dado que la consulta _default, trae datos&#58; 
 &#123; 
 _id &#58; &quot;16&quot;, 
 eatc-code &#58; &quot;9&quot;, 
 cua &#58; &quot;_default&quot;, 
 eatc-timeout_name &#58; &quot;eatc_doma_typolgy_b&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 1&quot;, 
 eatc-timeout_in_minutes &#58; &quot;0&quot;, 
 eatc-timeout_in_hours &#58; &quot;0&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot;, 
 eatc-doma_typolgy_b &#58; &quot;1&quot;, 
 eatc-since_kg &#58; &quot;20&quot; 
 &#125; 
&#160; 
 Se realiza el primer match con las organizaciones cuya tipologa b ( eatc-doma_typolgy_b ) es igual a 1 siempre y cuando el peso sea mayor a 20 KG (para las donaciones de menos de 20 KG se procede a realizar el match por distancia. 

&#160; 
 Match posteriores 
 En procesos de cron, que se disparan peridicamente, el sistema evala la fecha y hora actual y define si se ha cumplido el tiempo en minutos para ir aplicando las dems reglas de match presentes en los respectivos registros de timeout, teniendo en cuenta la lgica anteriormente definida. 

 REGISTRO DEL MATCH ***NUEVO*** DINAMIZAR SEGN DIVERSAS CUENTAS MAESTRAS&#58; 
 Si un gestor de donaciones cumple con todos los criterios de match se registra en la estructura definida para ese fin (eatc_match_registry) .&#160;&#160; 
&#160; 
 SE INCORPORA LA SIGUIENTE INFORMACIN AL MATCH&#58; eatc-pod_id, eatc-pod_name y eatc-donation_manager_name 
 Escritura con la API&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/ &#123;&#123;eatc_cua_master.eatc-cua&#125;&#125; /?_tabla= eatc_match_registry &amp;_operacion=insert&amp; date_time =&#123;&#123;FECHA Y HORA&#125;&#125; &amp; eatc-dona_header_code =&#123;&#123;VALOR&#125;&#125;&amp; eatc-donation_manager_code = &#123;&#123;VALOR&#125;&#125;&amp; eatc-pod_id = &#123;&#123;VALOR&#125;&#125;&amp; eatc-pod_name =&#123;&#123;VALOR&#125;&#125;&amp; eatc-donation_manager_nam e=&#123;&#123;VALOR&#125;&#125; 

&#160; 
 Ejemplo&#58; 
 El para el anuncio eatc-code = 00001911180031 de la cuenta maestra &quot;abaco&quot; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00001911180031 &#160;&#160; 
&#160; 
 El sistema determin en el proceso que corri el 2019-09-18 16&#58;00&#58;00 que existe match completo con &quot;FUNDACIN BANCO ARQUIDIOCESANO DE ALIMENTOS DE MEDELLN ( identificador_unico_registro &#58; &quot;900082682-9&quot;)( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=15 ), el sistema debe realizar el siguiente registro utilizando el API. 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_match_registry &amp;_operacion=insert&amp; date_time =2019-09-18%2016&#58;00&#58;00 &amp; eatc-dona_header_code =2019209714&amp; eatc-donation_manager_code = 900082682-9&amp; eatc-pod_id = 31&amp; eatc-pod_name =xito%20Colombia&amp; eatc-donation_manager_name =FUNDACIN%20BANCO%20ARQUIDIOCESANO%20DE%20ALIMENTOS%20DE%20MEDELLN 
&#160; 
(PRUEBA MATCH CONCURRENCIA&#58; https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_match_registry &amp;_operacion=insert&amp; date_time =2019-11-19%2016&#58;00&#58;00 &amp; eatc-dona_header_code = 00001911170031 &amp; eatc-donation_manager_code = 830045172-1 ) 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190926160803&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;2&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar en&#58;&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/ &#123;&#123;eatc_cua_master.eatc-cua&#125;&#125; /api/ &#123;&#123;eatc_cua_master.eatc-cua&#125;&#125; /eatc_match_registry?_id=_* 
&#160; 
 El sistema antes de realizar un registro debe verificar que el mismo no se halla realizado previamente (de alguna manera se debe guardar el cdigo del anuncio y del donante y cuando se vuelva a correr se debe descartar realizar un registro para dicho par de datos (esto se hace porque la funcionalidad de &quot; Cancelar Anuncio de donacin &quot; puede borrar un registro en el match y por lo tanto el proceso no debe volver a generar dicho match que borr el usuario (SE DEBE ANALIZAR CUAL ES LA MEJOR MANERA DE HACER ESTO). 

 Envo a la plataforma de mensajera PUSH a partir del match ***NUEVO*** dinamizar segn diversas cuentas maestras 
 Cuando la plataforma realiza el match entre un anuncio de donacin y un gestor de donaciones, se debe enviar un registro al API de mensajera PUSH, de la siguiente manera, tomando el cuenta la informacin del anuncio de donacin ( eatc-total_weight_kg, eatc-pod_name , eatc-publication_datetime, eatc-pod_address) y del gestor de donacin con el que se hizo match (identificador_unico_registro). 

&#160; 
 ****NUEVO**** El mensaje push tambin debe contener un resumen de las unidades donadas 
 El mensaje push tambin debe contener un listado (array) que contenga la siguiente informacin del detalle del anuncio (eatc_dona&#58; tantas veces como lneas tenga el anuncio respectivo).&#160; Esto con el nimo de brindar mayor informacin de primera mano al posible beneficiario y que esto aliente su adjudicacin. 
&#160; 
 Contenido del anuncio&#58; 
 &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; (&#123;&#123; eatc_dona. eatc-odd_quantity&#125;&#125; und);&#160; 
&#160; 
 Esto con el nimo de brindar mayor informacin de primera mano al posible beneficiario y que esto aliente su adjudicacin. 
&#160; 
 EJEMPLO&#58; 
 Para el anuncio cuyo eatc-code (eatc_dona.eatc-dona_header_code) es (en ambiente de pruebas) &quot;00001912190388&quot; en la cuenta maestra &quot;abaco&quot; ( https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=00001912190388 ), en el mensaje push se debera mostrar lo siguiente&#58; 
&#160; 
 Contenido del anuncio&#58; PASTA SAN REMO CONCHA 400G (4 und); PASTA SAN REMO SPAGHETTI 400G (2 und); PASTA SAN REMO FIDEO 400G (1 und); PASTA SPAGUETTI (1&#160; und); HARINA BLANCA(2 und); SALSA DE TOMATE (1 und); PASTA CORRIENTE FIDEOS (1 und); SPAGUETTI CLASICO (1 und); PAN BLANCO (1 und); SAL REFINADA (2 und). 
&#160; 
 Formato HTTP plano 
 POST /fcm/send HTTP/1.1 
 Host&#58; fcm.googleapis.com 
 Authorization&#58;&#160; key=AIzaSyCczFDqIVI_XP0qCI5WJ5MfrR3xVJmoFqU 
 Content-Type&#58; application/json 
 cache-control&#58; no-cache 
 &#123; 
 &#160;&#160;&#160;&#160;&quot;notification&quot;&#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;title&quot;&#58; &quot;$ eatc-total_weight_kg KG $ eatc-pod_name &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;body&quot;&#58; &quot;Fecha&#58; $ eatc-publication_datetime ( Faltan ## Horas). Direccin de recogida&#58; $ eatc-pod_address &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;sound&quot;&#58; &quot;default&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;click_action&quot;&#58; &quot;FCM_PLUGIN_ACTIVITY&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;icon&quot;&#58; &quot;fcm_push_icon&quot; 
 &#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&quot;data&quot;&#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;param1&quot;&#58; &quot;value1&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;param2&quot;&#58; &quot;value2&quot; 
 &#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&quot;to&quot;&#58; &quot;/topics/$ identificador_unico_registro &quot;, 
 &#160;&#160;&#160;&#160;&quot;priority&quot;&#58; &quot;high&quot;, 
 &#160;&#160;&#160;&#160;&quot;restricted_package_name&quot;&#58; &quot;co.nzzn.eatcloud.beneficiarios&quot; 
 &#125; 

&#160; 
 Ajax Jquery&#58; 
 var settings = &#123; 
 &#160;&#160;&quot;async&quot;&#58; true, 
 &#160;&#160;&quot;crossDomain&quot;&#58; true, 
 &#160;&#160;&quot;url&quot;&#58; &quot; https&#58;//fcm.googleapis.com/fcm/send 
 &quot;, 
 &#160;&#160;&quot;method&quot;&#58; &quot;POST&quot;, 
 &#160;&#160;&quot;headers&quot;&#58; &#123; 
 &#160;&#160;&#160;&#160;&quot;Authorization&quot;&#58; &quot;key=AIzaSyCczFDqIVI_XP0qCI5WJ5MfrR3xVJmoFqU&quot;, 
 &#160;&#160;&#160;&#160;&quot;Content-Type&quot;&#58; &quot;application/json&quot;, 
 &#160;&#160;&#160;&#160;&quot;cache-control&quot;&#58; &quot;no-cache&quot; 
 &#160;&#160;&#125;, 
 &#160;&#160;&quot;processData&quot;&#58; false, 
 &#160;&#160;&quot;data&quot;&#58; &quot;&#123;
&#160; &#160; \&quot;notification\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;title\&quot;&#58; \&quot;$ eatc-total_weight_kg KG $ eatc-pod_name \&quot;,
&#160; &#160; &#160; &#160; \&quot;body\&quot;&#58; \&quot;Fecha&#58; $ eatc-publication_datetime ( Faltan ## Horas). Direccin de recogida&#58; $ eatc-pod_address \&quot;,
&#160; &#160; &#160; &#160; \&quot;sound\&quot;&#58; \&quot;default\&quot;,
&#160; &#160; &#160; &#160; \&quot;click_action\&quot;&#58; \&quot;FCM_PLUGIN_ACTIVITY\&quot;,
&#160; &#160; &#160; &#160; \&quot;icon\&quot;&#58; \&quot;fcm_push_icon\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;data\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;param1\&quot;&#58; \&quot;value1\&quot;,
&#160; &#160; &#160; &#160; \&quot;param2\&quot;&#58; \&quot;value2\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;to\&quot;&#58; \&quot;/topics/$ identificador_unico_registro &quot;\&quot;,
&#160; &#160; \&quot;priority\&quot;&#58; \&quot;high\&quot;,
&#160; &#160; \&quot;restricted_package_name\&quot;&#58; \&quot;co.nzzn.eatcloud.beneficiarios\&quot;
&#125;&quot; 
 &#125; 
 $.ajax(settings).done(function (response) &#123; 
 &#160;&#160;console.log(response); 
 &#125;); 
&#160; 

&#160; 
 PHP y cURL 
 &lt;?php 
 $curl = curl_init(); 
 curl_setopt_array($curl, array( 
 &#160;&#160;CURLOPT_URL =&gt; &quot; https&#58;//fcm.googleapis.com/fcm/send 
 &quot;, 
 &#160;&#160;CURLOPT_RETURNTRANSFER =&gt; true, 
 &#160;&#160;CURLOPT_ENCODING =&gt; &quot;&quot;, 
 &#160;&#160;CURLOPT_MAXREDIRS =&gt; 10, 
 &#160;&#160;CURLOPT_TIMEOUT =&gt; 30, 
 &#160;&#160;CURLOPT_HTTP_VERSION =&gt; CURL_HTTP_VERSION_1_1, 
 &#160;&#160;CURLOPT_CUSTOMREQUEST =&gt; &quot;POST&quot;, 
 &#160;&#160;CURLOPT_POSTFIELDS =&gt; &quot;&#123;
&#160; &#160; \&quot;notification\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;title\&quot;&#58; \&quot;$ eatc-total_weight_kg KG $ eatc-pod_name \&quot;,
&#160; &#160; &#160; &#160; \&quot;body\&quot;&#58; \&quot;Fecha&#58; $ eatc-publication_datetime ( Faltan ##hrs ##min&#58;). Direccin de recogida&#58; $ eatc-pod_address \&quot;,
&#160; &#160; &#160; &#160; \&quot;sound\&quot;&#58; \&quot;default\&quot;,
&#160; &#160; &#160; &#160; \&quot;click_action\&quot;&#58; \&quot;FCM_PLUGIN_ACTIVITY\&quot;,
&#160; &#160; &#160; &#160; \&quot;icon\&quot;&#58; \&quot;fcm_push_icon\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;data\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;param1\&quot;&#58; \&quot;value1\&quot;,
&#160; &#160; &#160; &#160; \&quot;param2\&quot;&#58; \&quot;value2\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;to\&quot;&#58; \&quot;/$ identificador_unico_registro /testtopic\&quot;,
&#160; &#160; \&quot;priority\&quot;&#58; \&quot;high\&quot;,
&#160; &#160; \&quot;restricted_package_name\&quot;&#58; \&quot;co.nzzn.eatcloud.beneficiarios\&quot;
&#125;&quot;, 
 &#160;&#160;CURLOPT_HTTPHEADER =&gt; array( 
 &#160;&#160;&#160;&#160;&quot;Authorization&#58; key=AIzaSyCczFDqIVI_XP0qCI5WJ5MfrR3xVJmoFqU&quot;, 
 &#160;&#160;&#160;&#160;&quot;Content-Type&#58; application/json&quot;,&#160;&#160;&#160;&#160; 
 &#160;&#160;&#160;&#160;&quot;cache-control&#58; no-cache&quot; 
 &#160;&#160;), 
 )); 
 $response = curl_exec($curl); 
 $err = curl_error($curl); 
 curl_close($curl); 
 if ($err) &#123; 
 &#160;&#160;echo &quot;cURL Error #&#58;&quot; . $err; 
 &#125; else &#123; 
 &#160;&#160;echo $response; 
 &#125; 
 ?&gt; 
&#160; 
 Faltan ##hrs ##min **NUEVO** Dinamizar para mltiples cuentas maestras 
 Tomando el dato de &quot; eatc-publication_datetime &quot;, se le suman 24 horas y la informacin corresponde a la resta de esa hora con respecto a la fecha y hora actual. 
&#160; 
 Ejemplo&#58; 
 El para el anuncio &quot; eatc-id &quot; = 8687012 (eatc-code = 2019209714) de la cuenta maestra &quot;abaco&quot; que tiene la siguiente informacin&#58; 
&#160; 
 eatc-publication_datetime &#58; &quot;2019-09-18 15&#58;37&#58;54 
 eatc-total_weight_kg &#58; &quot;1000&quot;, 
 eatc-pod_name &#58; &quot;EXITO COLOMBIA&quot;, 
 eatc-pod_address &#58; &quot;&quot;Transversal 39B, Medelln, Antioquia&quot;&quot;, 
&#160; 
 Y que hizo match completo con &quot;FUNDACIN BANCO ARQUIDIOCESANO DE ALIMENTOS DE MEDELLN ( identificador_unico_registro &#58; &quot;900082682-9&quot;)( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=15 ), el sistema debe realizar el siguiente registro utilizando el API de Firebase. 

&#160; 
 PHP y cURL 
 &lt;?php 
 $curl = curl_init(); 
 curl_setopt_array($curl, array( 
 &#160;&#160;CURLOPT_URL =&gt; &quot; https&#58;//fcm.googleapis.com/fcm/send 
 &quot;, 
 &#160;&#160;CURLOPT_RETURNTRANSFER =&gt; true, 
 &#160;&#160;CURLOPT_ENCODING =&gt; &quot;&quot;, 
 &#160;&#160;CURLOPT_MAXREDIRS =&gt; 10, 
 &#160;&#160;CURLOPT_TIMEOUT =&gt; 30, 
 &#160;&#160;CURLOPT_HTTP_VERSION =&gt; CURL_HTTP_VERSION_1_1, 
 &#160;&#160;CURLOPT_CUSTOMREQUEST =&gt; &quot;POST&quot;, 
 &#160;&#160;CURLOPT_POSTFIELDS =&gt; &quot;&#123;
&#160; &#160; \&quot;notification\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;title\&quot;&#58; \&quot;1000 KG, EXITO COLOMBIA\&quot;,
&#160; &#160; &#160; &#160; \&quot;body\&quot;&#58; \&quot;Fecha&#58; 2019-09-18 15&#58;37&#58;54 ( Faltan ##hrs ##min&#58;). Direccin de recogida&#58; Transversal 39B, Medelln, Antioquia\&quot;,
&#160; &#160; &#160; &#160; \&quot;sound\&quot;&#58; \&quot;default\&quot;,
&#160; &#160; &#160; &#160; \&quot;click_action\&quot;&#58; \&quot;FCM_PLUGIN_ACTIVITY\&quot;,
&#160; &#160; &#160; &#160; \&quot;icon\&quot;&#58; \&quot;fcm_push_icon\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;data\&quot;&#58; &#123;
&#160; &#160; &#160; &#160; \&quot;param1\&quot;&#58; \&quot;value1\&quot;,
&#160; &#160; &#160; &#160; \&quot;param2\&quot;&#58; \&quot;value2\&quot;
&#160; &#160; &#125;,
&#160; &#160; \&quot;to\&quot;&#58; \&quot;/900082682-9/testtopic\&quot;,
&#160; &#160; \&quot;priority\&quot;&#58; \&quot;high\&quot;,
&#160; &#160; \&quot;restricted_package_name\&quot;&#58; \&quot;co.nzzn.eatcloud.beneficiarios\&quot;
&#125;&quot;, 
 &#160;&#160;CURLOPT_HTTPHEADER =&gt; array( 
 &#160;&#160;&#160;&#160;&quot;Authorization&#58; key=AIzaSyCczFDqIVI_XP0qCI5WJ5MfrR3xVJmoFqU&quot;, 
 &#160;&#160;&#160;&#160;&quot;Content-Type&#58; application/json&quot;,&#160;&#160;&#160;&#160; 
 &#160;&#160;&#160;&#160;&quot;cache-control&#58; no-cache&quot; 
 &#160;&#160;), 
 )); 
 $response = curl_exec($curl); 
 $err = curl_error($curl); 
 curl_close($curl); 
 if ($err) &#123; 
 &#160;&#160;echo &quot;cURL Error #&#58;&quot; . $err; 
 &#125; else &#123; 
 &#160;&#160;echo $response; 
 &#125; 
 ?&gt; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MATCH DE ANUNCIOS DE DONACIN CON GESTORES DE DONACIN