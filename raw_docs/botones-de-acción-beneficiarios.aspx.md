# botones-de-acción-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Desde el dashboard se podr ingresar a los siguientes botones: 

 Mis donaciones: 
  E l globo de notificacin presenta el nmero de anuncios de donacin ( eatc_dona_headers ) que han sido adjudicados a la fundacin cuyo usuario consulta 

 Mostrar el nmero de las donaciones cuyo estado sea Awarded, Scheduled y Delivered  (***NUEVO***) cuando no tienen una fecha y hora vlida en eatc-receipt_datetime 
 Para mostrar esta informacin el sistema debe realizar el la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donation_manager_code={{valor}}&eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00 &_compress 

 Se toma el " cont " se debe generar el nmero que se presenta en la burbuja. 

 Al oprimir el botn se va a la funcionalidad  " Mis Donaciones " 

 Ejemplo, _DOM. cua_master=abaco, ambiente de pruebas: 

 El usuario Juan Carlos Buitrago, cuya organizacin es: 90326456-1, se realiza la siguiente consulta: 

 Ambiente de prueba: https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=900326456-1&eatc-state=awarded,scheduled,delivered      
 Trama comprimida: https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=900326456-1&eatc-state=awarded,scheduled,delivered&_compress    

 Siendo 2 de diciembre de 2019, el API responde de la siguiente manera: 
 { 
 ts : "191202175148", 
 op : true, 
 cont : 1, 
 res : 
 } 

 Por lo tanto el nmero que se debe pintar en el globo sera " 1 " 

 Nube de donaciones:  
 Slo mostrar en el globo, los anuncios que estn anunciados y que hacen match 
 El globo de notificacin presenta los anuncios de donacin ( eatc_dona_headers ) cuyo estado es "anunciado" y que estn presente en el eatc_match_registry para la organizacin que consulta (es decir, que estn pendientes de ser adjudicados y hacen match), y presenta un vnculo a la funcionalidad " seguimiento de anuncios ".  Para ello se hace la consulta al nuevo servicio matchquery para obtener lo que trae en el parmetro " cont " 

 {{URL_entorno_beneficiarios}}/matchquery/{{_DOM.cua_master}}/{{eatc_donation_managers.identificador_unico_registro}} ?_compress 

 Ejemplo _DOM. cua_master=abaco, ambiente de pruebas : 

 El da 26 de mayo de 2021, la organizacin cuyo identificador_unico_de_registro es 811018073   

 https://devbeneficiarios.eatcloud.info/matchquery/abaco/811018073?_compress 

 Como el API responde de la siguiente manera (siendo 26 de mayo de 2021): 
 { 
 ts : "210526153741" , 
 op : true , 
 cont : 5 , 
 res : .... 
 } 

 Por lo tanto el nmero que se debe pintar en el globo sera " 5 " 

 ANTERIORMENTE:  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_match_registry?fecha_corta={{dia_actual_AAAA-MM-DD}},{{ dia_actual-1_dia_AAAA-MM-DD }},{{ dia_actual-2_dias_AAAA-MM-DD }},{{ dia_actual-3_dias_AAAA-MM-DD }},{{ dia_actual-4_dias_AAAA-MM-DD }}&eatc-donation_manager_code={{eatc_donation_managers. identificador_unico_registro }} 

 Ejemplo _DOM. cua_master=abaco, ambiente de pruebas: 

 #Anuncios de donacin ( eatc_dona_headers ) estado " announced " y que hacen Match 

 El da 16 de abril de 2020, la organizacin cuyo identificador_unico_de_registro es 900082682 (FUNDACIN BANCO ARQUIDIOCESANO DE ALIMENTOS DE MEDELLN) debe realizar la siguiente consulta al match para establecer cuales anuncios han hecho match con su organizacin en los ltimos cinco das: 

 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_match_registry?fecha_corta=2020-04-16,2020-04-15,2020-04-14,2020-04-13,2020-04-11&eatc-donation_manager_code=900082682   

 Tomando esta informacin que trae la anterior consulta se tiene que los anuncios con eatc-dona_header_code : abacoabaco_bog20200414155808931, abacoabaco_bog20200414151341645 y colombiafRfpi7G2m2SYWdRHH4oJH20200416150831278 han hecho match, entonces con esos cdigos se consulta al API de eatc_dona_headers para establecer cuales tienen estado "announced" 

 Trama comprimida: https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=announced&eatc-code=abacoabaco_bog20200414155808931,abacoabaco_bog20200414151341645,colombiafRfpi7G2m2SYWdRHH4oJH20200416150831278&_compress    

 Como el API responde de la siguiente manera (siendo 20 de abril del 2020): 
 { 
 ts : "200420221231", 
 op : true, 
 cont : 3, 
 res : ... 
 } 

 Por lo tanto el nmero que se debe pintar en el globo sera " 3 " 

 NO SE LE PERMITIRN VER NUEVOS ANUNCIOS A LAS ORGANIZACIONES QUE TENGAN ANUNCIOS DE DONACIN PENDIENTES POR VERIFICAR ***NUEVO: SEGN LMITES DEFINIDOS EN EATC_EATCLOUD_RESTRICTIONS *** 
   (anteriormente: exptuando BdeA eatc_doma_typology_b=1 y aplicando timeout) 

 NOTA PARA EL DESARROLLO:  
 Anteriormente, para esta restriccin en particular: No permitir que se consulte la nube, simplemente se estableci que esta condicin no le aplicaba a bancos de alimentos. A partir de la fecha, existe una tabla: eatc_eatcloud_restrictions en donde se establecen lmites para las donaciones pendientes de veficiacin , fijando el nmero de donaciones que se permite " no tener verificadas " antes de impedir la visualizacin de la nube (anteriormente era un parmetro fijo que estableca que no poda tener ninguna donacin pendiente para aplicarle la restriccin y se exclua a los bancos de alimentos). Por lo tanto se establecen las siguientes consultas para definir cuando aplica la restriccin de consulta a la nube de donaciones. 

 ***NUEVO: Consulta para establecer el nmero de donaciones pendientes por verificar que restringe el acceso a la nube de donaciones *** 

 Si la tipologa b de la organizacin no est excluida, entonces el sistema deber realizar las siguientes consultas para establecer el nmero de donaciones pendientes por verificar que restringir el acceso a la nube, de la siguiente manera: 

 Teniendo como base la tipologa B de la organizacin que esta loggeada en la APP ( {{eatc_donation_managers. eatc_doma_typology_b } }), el sistema realizar la siguiente consulta: 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_verification &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = {{eatc_donation_managers. eatc_doma_typology_b }} &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_verification &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_verification &eatc_cua_master = _default & eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 El dato que devuelva cualquiera de las anteriores consultas, corresponder al nmero de donaciones que se le permitir tener sin verificacin, antes de restringirle el acceso a la nube como se explicar ms adelante 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc_donation_managers. eatc_doma_typology_b } } =2 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_verification&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= 2 &_cmp= eatc_restrictive_number_of_dona   

 Como el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_verification&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= _default &_cmp= eatc_restrictive_number_of_dona   

 El valor que se recibe en {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} (que en el ejemplo es 2) se guarda para posteriores comparaciones que definirn si se restringe o no el acceso a la nube de donaciones. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico, {{eatc_donation_managers. eatc_doma_typology_b } } =1 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_verification&eatc_cua_master=mexico&eatc_doma_typ_b_restriction= 1 &_cmp= eatc_restrictive_number_of_dona   
 El valor que se recibe en {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} (que en el ejemplo es 3) se guarda para posteriores comparaciones que definirn si se restringe o no el acceso a la nube de donaciones. 

 ***NUEVO: Establecimiento del nmero de anuncios pendientes por verificar (estado eatc-state=delivered y (prueba lgica "y") cuya eatc-receipt_datetime no sea vlida) *** 

 El sistema realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{eatc-donation_manager_code}}&eatc-state=delivered&eatc-receipt_datetime=0000-00-00%2000:00:00&_cont 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc-donation_manager_code}} =900326456_001 

 El sistema realiza la siguiente consulta: 
 https://devdonantes.eatcloud.info /api/ abaco /eatc_dona_headers?eatc-donation_manager_code= 900326456_001 &eatc-state=delivered&eatc-receipt_datetime=0000-00-00%2000:00:00&_cont   

 Dado que la respuesta del sistema es count= 5 entonces con este nmero se realizarn las siguientes comparaciones 

 Con el valor que llega en la respuesta el sistema realiza las siguientes comparaciones: 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} 

 Esto quiere decir que el nmero de donaciones pendientes de ser verificadas es mayor al nmero que genera la restriccin, razn por la cual, no se le debe permitir ingresar a la nube de donaciones desplegndole al usuario el siguiente mensaje 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_pendiente_verificacion_desc " 
 Hemos encontrado {{cont}} donaciones pendientes de verificacin. Te solicitamos las verifiques para que luego retornes a visualizar los anuncios de donacin que estn disponibles. Muchas gracias. 

 Y deber redireccionar a " Mis Donaciones " 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} >= {{cont}}  

 Esto quiere decir que el nmero de donaciones pendientes no sobrepasa al nmero que genera la restricin, razn por la cual se genera una alerta, pero no se restringe el ingreso a la nube de donaciones: 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_pendiente_verificacion_desc " 

 Hemos encontrado {{cont}} donaciones pendientes de verificacin. Te solicitamos los verifiques para que luego retornes a visualizar los anuncios que estn disponibles. Muchas gracias. 

 [Consultar nube de donaciones]                            [Verificar anuncios] 

 El Botn [Verificar anuncios] debe redireccionar a " Mis Donaciones " 

 El Botn [Consultar nube de donaciones] debe permitir ingresar a la Nube de donaciones . 

 DEPRECADO: 

 DEPRECADO: *** 
 NUEVO: Consulta para establecer las tipologas b de gestores de donaciones a los cuales no les aplica la restriccin:*** 
 El sistema realizar la siguiente consulta: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_verification&eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl 

 El resultado que arroje la consulta, ser el array de tipologas b a los cuales no les aplicar la presente exclusin para la consulta de la nube {{ array_typ_b_exclude }} (anteriormente estaba quemado que eran la tipologa b = 1, ahora ser un dato que se consulta dinmicamente). 

 Si la consulta no arroja resultados querr decir que no existirn exclusiones para la restriccin de consulta de la nube a partir de un nmero de donaciones que no han sido verificadas. 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco El sistema realiza la siguiente consulta: https://dev.datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_verification&eatc_cua_master=abaco&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl   

 Dada que la respuesta es 1, esto quiere decir que para la cuenta maestra abaco, no le aplica la restriccin de visualizacin de la nube por donaciones pendientes de verificacin, a las organizaciones tipologa b =1, es decir, a los bancos de alimentos. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico 

 El sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_verification&eatc_cua_master=mexico&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl   

 Como la consulta no arroja resultados, quiere decir que para la cuenta maestra mexico, no existen organizaciones excluidas de la restriccin de no poder ver la nube de donaciones cuando hay donaciones pendientes de verificar (es decir, la restriccin de no ver la nube tambin le aplica a los bancos de alimentos, que en desarrollo anterior, siempre estaban excluidos). 

 ANTES: se validaba anuncios cuya fecha y hora de checkout (eatc- picking_checkout_datetime ) fuera vlida y no tuvieran fecha y hora de recepcin ( eatc-receipt_datetime ) 

 ANTES: El sistema, antes de mostrar la nube de donaciones, debe verificar, si el usuario tiene anuncios con estado (eatc-state) "delivered" (entregado).  En caso de que exista uno o varios anuncios con ese estado, se debe mostrar el siguiente mensaje: 

 DEPRECADO: Aplicando nuevo timeout para dejar espacio suficiente a la gestin 
 El sistema deber consultar el siguiente timeout 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master.eatc_cua}}/eatc_timeout_rules?eatc-timeout_name=dona_management_timeout&eatc-city={{eatc_donation_managers.municipio}}&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b 
 Si la consulta no arroja resultados se deber realizar la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master.eatc_cua}}/eatc_timeout_rules?eatc-timeout_name=dona_management_timeout&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b 
 Si la consulta no arroja resultados se toma como timeout por defecto: 
 eatc-timeout_in_minutes=1440 
 eatc-timeout_from=eatc-picking_checkout_datetime  

 Ejemplo entorno de pruebas ABACO, cuidad del gestor: Medelln: 
 El sistema realiza la siguiente bsqueda:  
 https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_management_timeout&eatc-city=Medelln&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b    

 Como la consulta no arroja resultados se deber realizar la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_management_timeout&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b   

 El sistema establece entonces que el respectivo timeout (eatc_timeout_rules.eatc-timeout_in_minutes) es de 1440 minutos. 
 El sistema, antes de mostrar la nube de donaciones, debe verificar (para organizaciones cuya eatc_doma_typology_b es diferente a la que arroj la consulta respectiva ), si el usuario tiene anuncios cuyo estado (eatc-state) sea "delivered" y (prueba lgica "y") sin registro vlido de fecha en el parmetro eatc_dona_headers.eatc-receipt_datetime.   

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}//eatc_dona_headers?eatc-donation_manager_typology_b=_nin_{{array_typ_b_exclude}}&eatc-donation_manager_code={{eatc-donation_manager_code}}&eatc-state=delivered&eatc-receipt_datetime=0000-00-00%2000:00:00&_count 
 Para los anuncios que cumplen esta la anterior condicin, el sistema deber evaluar si el dato contenido en: eatc_dona_headers.eatc-picking_checkout_datetime (es decir en eatc_timeout_rules.eatc-timeout_from)ms el timeout en minutos (eatc_timeout_rules.eatc-timeout_in_minutes o su valor por defecto de 1440 minutos) que se consult anteriormente, dan como resultado una fecha y hora mayor a la fecha y actual. 

 Label: class="lbl_bloqueo_nube_verificacion_dona" 
 Hemos encontrado donaciones pendientes de verificacin. Te solicitamos las verifiques para que luego retornes a visualizar los anuncios de donacin que estn disponibles. Muchas gracias. 
 Y deber redireccionar a "Mis Donaciones" 

 El mensaje para todas lo eatc_donations_managers que no les aplique restriccin (anteriormente eran los tipologa b = 1), ser el siguiente: 
 Si existen anuncios pendientes por ser verificados para los bancos de alimentos: 
 {URL_entorno_donantes}}/api/{{_DOM.cua_master}}//eatc_dona_headers?eatc-donation_manager_typology_b={{eatc_donation_managers.eatc_doma_typology_b}}&eatc-donation_manager_code={{eatc-donation_manager_code}}&eatc-state=delivered&eatc-receipt_datetime=0000-00-00%2000:00:00&_compress 
 Entonces se deber desplegar el siguiente mensaje en la APP. 
 Hemos encontrado anuncios de donacin pendientes de verificacin. Te solicitamos los verifiques para que luego retornes a visualizar los anuncios que estn disponibles. Muchas gracias. 

 Consultar nube de donaciones                          Verificar anuncios 
 El Botn "Verificar anuncios" debe redireccionar a " Mis Donaciones " 
 Si los anuncios pendientes por verificar an no cumplen el timeout respectivo (es decir eatc_dona_headers.eatc-picking_checkout_datetime ms el timeout en minutos (eatc_timeout_rules.eatc-timeout_in_minutes o su valor por defecto de 1440 minutos) que se consult anteriormente, dan como resultado una fecha y hora menor a la fecha y actual, entonces el botn consultar tendr el siguiente comportamiento: 
 El Botn "Consultar nube de donaciones" debe permitir ingresar a la nube de donaciones . 

 Si los anuncios pendientes por verificar an no cumplen el timeout respectivo (es decir eatc_dona_headers.eatc-picking_checkout_datetime ms el timeout en minutos (eatc_timeout_rules.eatc-timeout_in_minutes o su valor por defecto de 1440 minutos) que se consult anteriormente, dan como resultado una fecha y hora menor a la fecha y actual, entonces el botn consultar tendr el siguiente comportamiento: 
 El Botn "Consultar nube de donaciones" debe permitir ingresar a la nube de donaciones . 

 Si los anuncios pendientes por verificar an no cumplen el timeout respectivo (es decir eatc_dona_headers. eatc-picking_checkout_datetime ms el timeout en minutos ( eatc_timeout_rules. eatc-timeout_in_minutes o su valor por defecto de 1440 minutos ) que se consult anteriormente, dan como resultado una fecha y hora menor a la fecha y actual, entonces el botn consultar tendr el siguiente comportamiento: 

 NO SE LE PERMITIRN VER NUEVOS ANUNCIOS A LAS ORGANIZACIONES QUE TENGAN ANUNCIOS DE DONACIN PENDIENTES POR RECOGER ***NUEVO: SEGN LMITES DEFINIDOS EN EATC_EATCLOUD_RESTRICTIONS *** 
   (anteriormente: exceptuando los bancos de alimentos eatc_doma_typology_b=1) 

 NOTA PARA EL DESARROLLO:  
 Anteriormente, para esta restriccin en particular: No permitir que se consulte la nube, simplemente se estableci que esta condicin no le aplicaba a bancos de alimentos. A partir de la fecha, existe una tabla: eatc_eatcloud_restrictions en donde se establecen lmites para las donaciones pendientes de realizar checkin en el punto de donacin , fijando el nmero de donaciones que se permite " tener pendientes por recoger " antes de impedir la visualizacin de la nube (anteriormente era un parmetro fijo que estableca que no poda tener ninguna donacin pendiente para aplicarle la restriccin y se exclua a los bancos de alimentos). Por lo tanto se establecen las siguientes consultas para definir cuando aplica la restriccin de consulta a la nube de donaciones. 

 ***NUEVO: Consulta para establecer el nmero de donaciones pendientes por recoger que restringe el acceso a la nube de donaciones *** 

 Teniendo como base la tipologa B de la organizacin que esta loggeada en la APP ( {{eatc_donation_managers. eatc_doma_typology_b } }), el sistema realizar la siguiente consulta: 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_pickup &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = {{eatc_donation_managers. eatc_doma_typology_b }} &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_pickup &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_pickup &eatc_cua_master = _default & eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 El dato que devuelva cualquiera de las anteriores consultas ( {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} ), corresponder al nmero de donaciones que se le permitir tener sin recoger, antes de restringirle el acceso a la nube (que anteriormente estaba fijado como una o ms donaciones) 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc_donation_managers. eatc_doma_typology_b } } =2 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_pickup&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= 2 &_cmp= eatc_restrictive_number_of_dona   

 Como el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_pickup&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= _default &_cmp= eatc_restrictive_number_of_dona   

 El valor que se recibe en {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} (que en el ejemplo es 3) se guarda para posteriores comparaciones que definirn si se restringe o no el acceso a la nube de donaciones. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico, {{eatc_donation_managers. eatc_doma_typology_b } } =1 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_pickup&eatc_cua_master=mexico&eatc_doma_typ_b_restriction= 1 &_cmp= eatc_restrictive_number_of_dona    

 El valor que se recibe en {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} (que en el ejemplo es 3) se guarda para posteriores comparaciones que definirn si se restringe o no el acceso a la nube de donaciones. 

 ***NUEVO: Establecimiento del nmero de anuncios pendientes por recoger (estado eatc-state=scheduled y (prueba lgica "y") cuya eatc-picking_checkin_datetime no sea vlida) *** 

 El sistema realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}//eatc_dona_headers?eatc-donation_manager_code={{eatc-donation_manager_code}}&eatc-state= scheduled & eatc-picking_checkin_datetime =0000-00-00%2000:00:00&_count 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc-donation_manager_code}} =900326456_001 

 El sistema realiza la siguiente consulta: 
 https://devdonantes.eatcloud.info /api/ abaco /eatc_dona_headers?eatc-donation_manager_code= 900326456_001 &eatc-state=scheduled&eatc-picking_checkin_datetime=0000-00-00%2000:00:00&_cont    

 Dado que la respuesta del sistema es count= 5 entonces con este nmero se reaizarn las siguientes comparaciones 

 Con el valor que llega en la respuesta el sistema realiza las siguientes comparaciones: 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} 

 Esto quiere decir que el nmero de donaciones pendientes por recoger es mayor al nmero que genera la restricin, , razn por la cual, no se le debe permitir ingresar a la nube de donaciones desplegndole al usuario el siguiente mensaje 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_pendiente_recogida_des " 

 Hemos encontrado {{cont}} donaciones pendientes de recogida. Te solicitamos los recojas para que luego retornes a visualizar los anuncios que estn disponibles. Muchas gracias. 

 Y deber redireccionar a " Mis Donaciones " 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} >= {{cont}} 

 Esto quiere decir que el nmero de donaciones pendientes no sobrepasa al nmero que genera la restricin, razn por la cual se genera una alerta, pero no se restringe el ingreso a la nube de donaciones: 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_pendiente_recogida_des " 

 Hemos encontrado {{cont}} donaciones pendientes de recogida. Te solicitamos los verifiques para que luego retornes a visualizar los anuncios que estn disponibles. Muchas gracias. 

 [Consultar nube de donaciones]                            [Verificar anuncios] 

 El Botn [Verificar anuncios] debe redireccionar a " Mis Donaciones " 

 El Botn [Consultar nube de donaciones] debe permitir ingresar a la Nube de donaciones . 

 DEPRECADO: 
 ***NUEVO: Consulta para establecer las tipologas b de gestores de donaciones a los cuales no les aplica la restriccin:*** 

 El sistema realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_pickup&eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl 

 El resultado que arroje la consulta, ser el array de tipologas b a los cuales no les aplicar la presente exclusin para la consulta de la nube {{ array_typ_b_exclude }} (anteriormente estaba quemado que eran la tipologa b = 1, ahora ser un dato que se consulta dinmicamente). 

 Si la consulta no arroja resultados querr decir que no existirn exclusiones para la restriccin de consulta de la nube a partir de un nmero de donaciones que no han sido recogidas. 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_pickup&eatc_cua_master=abaco&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl 

 Dada que la respuesta es 1, esto quiere decir que para la cuenta maestra abaco, no le aplica la restriccin de visualizacin de la nube por donaciones pendientes de recogida, a las organizaciones tipologa b =1, es decir, a los bancos de alimentos. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico 

 El sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_pickup&eatc_cua_master=mexico&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl   

 Como la consulta no arroja resultados, quiere decir que para la cuenta maestra mexico, no existen organizaciones excluidas de la restriccin de no poder ver la nube de donaciones cuando hay donaciones pendientes de recoger (es decir, la restriccin de no ver la nube tambin le aplica a los bancos de alimentos, que en desarrollo anterior, siempre estaban excluidos). 

 El sistema, antes de mostrar la nube de donaciones, debe establecer, si el usuario tiene anuncios con estado (eatc-state) "scheduled" (programado) y cuya fecha de programacin de la recogida (eatc-programed_picking_datetime) sumndole el anterior timeout (eatc_timeout_rules.dona_pickup_timeout) sea superior a la fecha y hora actual (es decir, si programaron anuncios y no los han recogido en la fecha y hora que determinaron para ello ms el timeout). En caso de que existan un nmero  mayor o igual al establecido en la consulta anterior que genere restriccin para la consulta de la nube (anteriormente era un valor fijo de 1 o ms), se debe mostrar el siguiente mensaje: 

 Aplicando nuevo timeout para dejar espacio suficiente a la recogida. 
 El sistema deber consultar el siguiente timeout 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master.eatc_cua}}/eatc_timeout_rules?eatc-timeout_name=dona_pickup_timeout&eatc-city={{eatc_donation_managers.municipio}}&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b 
 Si la consulta no arroja resultados se deber realizar la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master.eatc_cua}}/eatc_timeout_rules?eatc-timeout_name=dona_pickup_timeout&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b 
 Si la consulta no arroja resultados se toma como timeout por defecto: 
 eatc_timeout_rules.eatc-timeout_in_minutes=480 

 Ejemplo entorno de pruebas ABACO, cuidad del gestor: Medelln: 
 El sistema realiza la siguiente bsqueda:  
 https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_pickup_timeout&eatc-city=Medelln&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b   

 Como la consulta no arroja resultados se deber realizar la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_pickup_timeout&_cmp=eatc-timeout_in_minutes,eatc-timeout_from,eatc-doma_typolgy_b 

 El sistema establece entonces que el respectivo timeout (eatc_timeout_rules.eatc-timeout_in_minutes) es de 480 minutos. 
 El mensaje para todos los eatc_donations_managers ***NUEVO: cuyo eatc_doma_typology_b est incluido en {{ array_typ_b_exclude }}   ***  (anteriormente: cuyo eatc_doma_typology_b es 1), ser el siguiente: 

 Hemos encontrado {{cont}} anuncios de donacin pendientes de recogida. Te solicitamos los recojas para que luego retornes a visualizar los anuncios que estn disponibles. Muchas gracias. 

 Consultar nube de donaciones                          Recoger anuncios 
 El Botn "Recoger anuncios" debe redireccionar a " Mis Donaciones " 
 El Botn "Consultar nube de donaciones" debe permitir ingresar a la nube de donaciones . 

 NO SE LE PERMITIRN VER NUEVOS ANUNCIOS PENDIENTES DE REGISTRAR HORA DE SALIDA DEL PUNTO DE DONACIN ***NUEVO: SEGN LMITES DEFINIDOS EN EATC_EATCLOUD_RESTRICTIONS *** 

 NOTA PARA EL DESARROLLO:  
 Anteriormente, para esta restriccin en particular: No permitir que se consulte la nube, simplemente se estableci que esta condicin no le aplicaba a bancos de alimentos. A partir de la fecha, existe una tabla: eatc_eatcloud_restrictions en donde se establecen lmites para las donaciones pendientes de realizar checkout en el punto de donacin , fijando el nmero de donaciones que se permite " tener pendientes por registrarle la salida del punto de donacin " antes de impedir la visualizacin de la nube (anteriormente era un parmetro fijo que estableca que no poda tener ninguna donacin pendiente para aplicarle la restriccin y se exclua a los bancos de alimentos). Por lo tanto se establecen las siguientes consultas para definir cuando aplica la restriccin de consulta a la nube de donaciones. 

 Teniendo como base la tipologa B de la organizacin que esta loggeada en la APP ( {{eatc_donation_managers. eatc_doma_typology_b } }), el sistema realizar la siguiente consulta: 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_checkout &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = {{eatc_donation_managers. eatc_doma_typology_b }} &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_checkout &eatc_cua_master = {{eatc_cua_master. eatc_cua }}& eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ? eatc_restriction_type = pending_checkout &eatc_cua_master = _default & eatc_doma_typ_b_restriction = _default &_cmp= eatc_restrictive_number_of_dona 

 El dato que devuelva cualquiera de las anteriores consultas ( {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} ), corresponder al nmero de donaciones que se le permitir tener sin recoger, antes de restringirle el acceso a la nube (que anteriormente estaba fijado como una o ms donaciones) 

 ***NUEVO: Establecimiento del nmero de anuncios pendientes por recoger (estado eatc-state=scheduled,delivered y (prueba lgica "y") cuya eatc-picking_checkout_datetime no sea vlida) *** 
 El sistema realiza la siguiente consulta 
 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}//eatc_dona_headers?eatc-donation_manager_code={{eatc-donation_manager_code}}&eatc-state= scheduled,delivered & eatc-picking_checkout_datetime =0000-00-00%2000:00:00&_count 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc-donation_manager_code}} =900326456_001 

 El sistema realiza la siguiente consulta: 
 https://devdonantes.eatcloud.info /api/ abaco /eatc_dona_headers?eatc-donation_manager_code= 900326456_001 &eatc-state=scheduled,delivered&eatc-picking_checkout_datetime=0000-00-00%2000:00:00&_cont    

 Dado que la respuesta del sistema es count= 5 entonces con este nmero se reaizarn las siguientes comparaciones 

 Con el valor que llega en la respuesta el sistema realiza las siguientes comparaciones: 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} 

 Esto quiere decir que el nmero de donaciones pendientes por recoger es mayor al nmero que genera la restricin, , razn por la cual, no se le debe permitir ingresar a la nube de donaciones desplegndole al usuario el siguiente mensaje 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_bloqueo_nube_fecha_salida " 

 Hemos encontrado {{cont}} pendientes de registro de hora de salida del punto de donacin. Te solicitamos realizar el registro (y posteriormente la verificacin de la donacin) para que luego retornes a visualizar los anuncios de donacin que estn disponibles. Muchas gracias. 
 Y deber redireccionar a " Mis Donaciones " 

 {{eatc_eatcloud_restrictions. eatc_restrictive_number_of_dona }} >= {{cont}} 

 Esto quiere decir que el nmero de donaciones pendientes no sobrepasa al nmero que genera la restricin, razn por la cual se genera una alerta, pero no se restringe el ingreso a la nube de donaciones: 

 Labels : class="lbl_hemos_encontrado" {{cont}} class=" lbl_bloqueo_nube_fecha_salida " 

 Hemos encontrado {{cont}} pendientes de registro de hora de salida del punto de donacin. Te solicitamos realizar el registro (y posteriormente la verificacin de la donacin) para que luego retornes a visualizar los anuncios de donacin que estn disponibles. Muchas gracias. 

 El Botn [Verificar anuncios] debe redireccionar a " Mis Donaciones " 

 El Botn [Consultar nube de donaciones] debe permitir ingresar a la Nube de donaciones . 

 DEPRECADO: 
 ***NUEVO: Consulta para establecer las tipologas b de gestores de donaciones a los cuales no les aplica la restriccin:*** 
 El sistema realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_checkout&eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl 

 El resultado que arroje la consulta, ser el array de tipologas b a los cuales no les aplicar la presente exclusin para la consulta de la nube {{ array_typ_b_exclude }} (anteriormente estaba quemado que eran la tipologa b = 1, ahora ser un dato que se consulta dinmicamente). 

 Si la consulta no arroja resultados querr decir que no existirn exclusiones para la restriccin de consulta de la nube a partir de un nmero de donaciones cuyo checkout no ha sido registrado. 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_checkout&eatc_cua_master=abaco&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl    

 Dada que la respuesta es 1, esto quiere decir que para la cuenta maestra abaco, no le aplica la restriccin de visualizacin de la nube por donaciones pendientes de registro de checkout, a las organizaciones tipologa b =1, es decir, a los bancos de alimentos. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico 

 El sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_eatcloud_restrictions?eatc_restriction_type=pending_checkout&eatc_cua_master=mexico&eatc_doma_typ_b_restriction_excl=_novacio&_cmp=eatc_doma_typ_b_restriction_excl   

 Como la consulta no arroja resultados, quiere decir que para la cuenta maestra mexico, no existen organizaciones excluidas de la restriccin de no poder ver la nube de donaciones cuando hay donaciones pendientes de realizarles el checkout (es decir, la restriccin de no ver la nube tambin le aplica a los bancos de alimentos, que en desarrollo anterior, siempre estaban excluidos). 

 Para organizaciones diferentes ***NUEVO: a las  presentes en el array de tipologas b excluidas {{ array_typ_b_exclude }} *** (anteriormente: cuyo eatc_doma_typology_b=1 (eatc_doma_typology_b=2,3,4,5)) cuando se ha superado el timeout para registrar la salida, se debe bloquear la nube de donaciones 
 El sistema, antes de mostrar la nube de donaciones, debe verificar, si el usuario tiene anuncios con un registro vlido en la fecha y hora de llegada ( eatc_dona_headers.eatc-picking_checkin_datetime ) y (prueba lgica "y") sin registro vlido de fecha y hora de salida eatc_dona_headers.eatc-picking_checkout_datetime siempre y cuando ya se haya superado el timeout respectivo ( y como se establece aqu) .  

 ***NUEVO: definicin del nmero de anuncios necesarios para que se establezca el bloqueo de la nube*** 
 Teniendo como base la tipologa B de la organizacin que esta loggeada en la APP ( {{eatc_donation_managers. eatc_doma_typology_b } }), el sistema realizar la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_checkout&eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_doma_typ_b_restriction= {{eatc_donation_managers. eatc_doma_typology_b }} &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_checkout&eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_doma_typ_b_restriction= _default &_cmp= eatc_restrictive_number_of_dona 

 Si el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_checkout&eatc_cua_master= _default &eatc_doma_typ_b_restriction= _default &_cmp= eatc_restrictive_number_of_dona 

 El dato que devuelva cualquiera de las anteriores consultas, corresponder al nmero de donaciones que se le permitir tener sin registro de checkout, antes de restringirle el acceso a la nube 

 Ejemplo 1: ambiente de pruebas, {{eatc_cua_master. eatc_cua }}= abaco, {{eatc_donation_managers. eatc_doma_typology_b } } =2 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_checkout&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= 2 &_cmp= eatc_restrictive_number_of_dona   

 Como el sistema no arroja resultados, entonces se procede a realizar la siguiente consulta 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_checkout&eatc_cua_master=abaco&eatc_doma_typ_b_restriction= _default &_cmp= eatc_restrictive_number_of_dona    

 Dado que la respuesta es igual a "1", eso quiere decir que el nmero de donaciones sin checkout (que hallan cumplido con el timeout) deben ser menores a 1 para que NO se restrinja el acceso a la nube de donaciones. 

 Ejemplo 2: ambiente productivo, {{eatc_cua_master. eatc_cua }}= mexico, {{eatc_donation_managers. eatc_doma_typology_b } } =1 

 El sistema realiza la siguiente consulta: 
 https://dev. datagov .eatcloud.info/api/eatcloud/ eatc_eatcloud_restrictions ?eatc_restriction_type=pending_verification&eatc_cua_master=mexico&eatc_doma_typ_b_restriction= 1 &_cmp= eatc_restrictive_number_of_dona   

 Dado que la respuesta es igual a "3", eso quiere decir que el nmero de donaciones sin verificar (que hallan cumplido con el timeout) deben ser menores a 3 para que NO se restrinja el acceso a la nube de donaciones. 

 En caso de que existan un nmero que genere restriccin para la consulta de la nube (anteriormente era un valor fijo de 1 o ms), se debe mostrar el siguiente mensaje: 

 Label : class=" lbl_bloqueo_nube_fecha_salida " 
 Hemos encontrado donaciones pendientes de registro de hora de salida del punto de donacin. Te solicitamos realizar el registro (y posteriormente la verificacin de la donacin) para que luego retornes a visualizar los anuncios de donacin que estn disponibles. Muchas gracias. 

 Y deber redireccionar a "Mis Donaciones" 

 Esta restriccin no les aplicarn a las organizaciones cuya tipologa b est presente en el {{ array_typ_b_exclude }} ( anteriormente: eatc_doma_typology_b sea 1) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbotones-de-acci%C3%B3n-beneficiarios%2F3415824716-EmbeddedImage--16-.png&ow=748&oh=288, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbotones-de-acci%C3%B3n-beneficiarios%2F3415824716-EmbeddedImage--16-.png&ow=748&oh=288 
 EatCloud Beneficiarios 

 522.000000000000 

 BOTONES DE ACCIN (EATC_DOMA_BTN)