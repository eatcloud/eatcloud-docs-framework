# creación-de-kpis.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En este apartado se documentarn procesos tcnicos necesarios para el funcionamiento de las tareas, que podrn ser realizados mediante tareas programadas, procedimientos almacenados u otro tipo de tcnica que garantice estabilidad, performance e inmediatez. 

 Esta informacin se llevar a la estructura eatc_dona_kpi que funcionar como una tabla de registro (una especie de detalle adicional por cada encabezado) que podr ser consultada para realizar consolidados que se mostrarn a lo largo de la plataforma. 

 Para registrar los KPIs en esta estructura, se debern realizar transformaciones y funciones a partir de la informacin de cada encabezado de donacin. 

 Otro aspecto a tener en cuenta es que cuando se crea el encabezado, solo se generan las transformaciones al momento de crear el anuncio .  Posteriormente, cuando a travs de la funcionalidad de la plataforma se asigna el anuncio de donacin , se deben realizar las transformaciones al momento de adjudicar . 

 Creacin dinmica de KPIs para diferentes cuentas maestras: 
 El proceso de creacin de KPIs debe correr para todas las cuentas maestras registradas en el respectivo maestro: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 

 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 

 ***NUEVO: No se generan KPIs que tienen que ver con el peso o el costo de una donacin de distribucin (para no generar doble registro) *** 
 El proceso de creacin de KPIs que se calculan a partir del peso o el costo de las donaciones, no podrn calcularse en aquellas donaciones que estn registradas como distribuciones, dado que sus KPIs referentes a peso y costo, se calculan en las donaciones de las cuales proceden estas distribuciones.  Por lo tanto el sistema no podr calcular estos KPIs a aquellas donaciones que tienen el siguiente registro: 
 eatc_dona_headers. eatc_distribution = y 

 Los KPIs que tienen que ver con tiempos, si se podrn calcular. 

 Transformaciones al momento de crear el anuncio de donacin 

 eatc-dona_header_code ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Cdigo del encabezado de donacin. Corresponde eatc-code de eatc_dona_header.  
 eatc_dona_header.eatc-code  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-code) 

 eatc_donor_code ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Cdigo del donante. Corresponde eatc_donor_code de eatc_dona_header.  
 eatc_dona_header.eatc_donor_code  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc_donor_code) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el registro ser "890.900.608-9" (ya que corresponde al campo " eatc_donor_code " de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=2019209714   

 ****NUEVO: eatc_cua_size *** 
 Corresponde al tamao del la cuenta que realiza el anuncio de donacin. . Corresponde eatc_cua_size de eatc_dona_header.  
 eatc_dona_header.eatc_cua_size 
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc_cua_size) 

 PARA REALIZAR EL REGISTRO SE DEBE UTILIZAR LA FUNCIN INSERT con los parmetros arriba descritos 
 {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_kpi&_operacion=insert&{{parametros de creacin}} 

 eatc-pod_id ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Cdigo del punto de donacin al cual pertenece el KPI. Corresponde eatc-pod_id de eatc_dona_header.  
 eatc_dona_header.eatc-pod_id  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-pod_id) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el registro ser " 31 " (ya que corresponde al campo " eatc-pod_id " de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 2019209714   

 eatc-pod_typology_a ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde a la primera tipologa del punto de donacin. . Corresponde eatc-pod_typology_a de eatc_dona_header.  
 eatc_dona_header.eatc-pod_typology_a  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-pod_typology_a) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el registro ser " Exito " (ya que corresponde al campo " eatc-pod_typology_a " de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 2019209714   

 eatc-pod_typology_b ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde a la segunda tipologa del punto de donacin. . Corresponde eatc-pod_typology_b de eatc_dona_header.  
 eatc_dona_header.eatc-pod_typology_b  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-pod_typology_b) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el registro ser " [valor] " (ya que corresponde al campo "eatc-pod_typology_b" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 2019209714   

 eatc-pod_typology_c ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde a la tercera tipologa del punto de donacin. . Corresponde eatc-pod_typology_c de eatc_dona_header.  
 eatc_dona_header.eatc-pod_typology_c  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-pod_typology_c) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el registro ser " [valor] " (ya que corresponde al campo "eatc-pod_typology_c" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 2019209714   

 PARA REALIZAR EL REGISTRO SE DEBE UTILIZAR LA FUNCIN INSERT con los parmetros arriba descritos 
 {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_kpi&_operacion=insert&{{parametros de creacin}} 

 ****NUEVO: eatc-pod_size *** 
 Corresponde al tamao del punto de donacin. . Corresponde eatc-pod_size de eatc_dona_header.  
 eatc_dona_header.eatc-pod_size 
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-pod_size) 

 PARA REALIZAR EL REGISTRO SE DEBE UTILIZAR LA FUNCIN INSERT con los parmetros arriba descritos 
 {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_kpi&_operacion=insert&{{parametros de creacin}} 

 Transformaciones al momento de adjudicar 
 Cuando se crea el anuncio de donacin la siguiente informacin se debe dejar vaca.  Posteriormente, con los procesos de la Plataforma esta informacin se ir enriqueciendo a medida que se opere el mdulo funcional: Aceptacin de anuncio de donacin . 

 eatc-donation_manager_code ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Cdigo del gestor de donaciones al cual se le adjudic la donacin al cual pertenece el KPI. Corresponde eatc-donation_manager_code de eatc_dona_header.  
 eatc_dona_header.eatc-donation_manager_code  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-donation_manager_code) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-code es 40716 , el registro ser " 900326456-1 " (ya que corresponde al campo "eatc-donation_manager_code" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 ) 

 eatc-donation_manager_typology_a   ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Primera tipologa del gestor de donaciones al cual se le adjudic la donacin al cual pertenece el KPI. Corresponde eatc-donation_manager_typology_a de eatc_dona_header.  
 eatc_dona_header.eatc-donation_manager_typology_a  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-donation_manager_typology_a) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-code es 40716 , el registro ser "ABACO" (ya que corresponde al campo "eatc-donation_manager_typology_a" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 ) 

 eatc-donation_manager_typology_b   ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Segunda tipologa del gestor de donaciones al cual se le adjudic la donacin al cual pertenece el KPI. Corresponde eatc-donation_manager_typology_b de eatc_dona_header.  
 eatc_dona_header.eatc-donation_manager_typology_b  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-donation_manager_typology_a) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-code es 40716 , el registro ser "0" (ya que corresponde al campo "eatc-donation_manager_typology_b" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 ) 

 eatc-donation_manager_typology_c   ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Segunda tipologa del gestor de donaciones al cual se le adjudic la donacin al cual pertenece el KPI. Corresponde eatc-donation_manager_typology_c de eatc_dona_header.  
 eatc_dona_header.eatc-donation_manager_typology_c  
 ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_header?eatc-donation_manager_typology_a) 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-code es 40716 , el registro ser "0" (ya que corresponde al campo "eatc-donation_manager_typology_c" de la consulta respectiva https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 )   

 PARA REALIZAR EL REGISTRO SE DEBE UTILIZAR LA FUNCIN UPDATE con los parmetros arriba descritos (para el ejemplo anterior sera) 
 https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_kpi&_operacion=update&eatc-donation_manager_code= 900326456-1 &eatc-donation_manager_typology_a= ABACO &eatc-donation_manager_typology_b= 0 &eatc-donation_manager_typology_b= 0 &WHEREeatc-dona_header_code= 40716 

 Por cada anuncio de donacin, cuando es recibido por el beneficiario   se le deben generar un total de 23 KPIs (al 27 de noviembre de 2019) diferentes (segn lo registrado en la tabla de reglas de KPIs ).  La idea es que el da de maana, cuando se adicionen nuevas reglas para el clculo de KPIs, el sistema est en condiciones de recorrer dichas reglas para generar nuevos clculos de KPIs que a su vez se convertirn en nuevos registros en la tabla respectiva (). 

 Cada KPI calculado, genera un registro, es decir que inicialmente, por cada encabezado de anuncio de donacin , se deben generar 23 registros en esta estructura.  Cada registro contiene la siguiente informacin. 

 Funciones KPI (se calculan cuando el anuncio ha sido recibido: eatc-state = " delivered" (despachado) ) => ***Nuevo: inclusin de parmetros eatc_cua_master y and_eatc_calculate_from_valid_date y consulta con parmetro _default *** 

 El sistema realiza la siguiente consulta, para establecer los KPIs que deben ser construidos cuando el anuncio tiene el estado en cuestin: 

 {{url_entorno_datagov}}/api/eatcloud/eatc_kpi_rules?e atc_cua_master={{_DOM. cua_master }} &eatc_calculate_from_state=delivered& and_eatc_calculate_from_valid_date= _vacio &_cmp=eatc_kpi,type,rule,eatc_calculate_from_state,and_eatc_calculate_from_valid_date   

 Si la consulta no aroja resultados, deber realizarse la siguiente consulta: 

 {{url_entorno_datagov}}/api/eatcloud/eatc_kpi_rules?eatc_cua_master= _default &eatc_calculate_from_state=delivered&and_eatc_calculate_from_valid_date=_vacio&_cmp=eatc_kpi,type,rule,eatc_calculate_from_state,and_eatc_calculate_from_valid_date   

 kpi 
 Nombre del KPI que se est calculando.  Corresponde a al campo eatc_kpi del maestro eatc_kpi_rules .  
 eatc_kpi_rules. eatc_kpi   

 eatc-kpi_type 
 Tipo de KPI (Social impact, Enviromental impact, Economic impact) del KPI que se est calculando 
 eatc_kpi_rules. type 

 value   
 Valor calculado del KPI. Resulta de la aplicacin de la regla de clculo (rule) de cada KPI) 
 eatc_kpi_rules. rule   

 Registro en la estructura de datos correspondiente 
 El sistema deber realizar el siguiente registro: 

 REGISTRO CON EL API: {{ URL_entorno_donantes }}/crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_kpi&_operacion=update&kpi={{eatc_kpi_rules. eatc_kpi }}& eatc-kpi_type ={{eatc_kpi_rules. type }}& value = {{value}} &WHEREeatc-dona_header_code={{eatc-dona_header_code}} 

 Se debe iterar o recorrer dichas respuestas para generar cada uno de los 6 registros de KPIs que generan cada encabezado con estado despachado 

 Funciones KPI (se calculan cuando el anuncio ha sido verificado por el beneficiario: eatc-state = " delivered" y con fecha y hora de recepcin vlida ) => ***Nuevo: inclusin de parmetros eatc_cua_master y and_eatc_calculate_from_valid_date y consulta con parmetro _default *** 

 El sistema realiza la siguiente consulta, para establecer los KPIs que deben ser construidos cuando el anuncio tiene el estado en cuestin: 

 El sistema realiza la siguiente consulta, para establecer los KPIs que deben ser construidos cuando el anuncio tiene el estado en cuestin: 

 {{url_entorno_datagov}}/api/eatcloud/eatc_kpi_rules? eatc_cua_master={{_DOM. cua_master }} & eatc_calculate_from_state= delivered & and_eatc_calculate_from_valid_date= _novacio &_cmp=eatc_kpi,type,rule,eatc_calculate_from_state, and_eatc_calculate_from_valid_date   

 Si la consulta no aroja resultados, deber realizarse la siguiente consulta: 

 {{url_entorno_datagov}}/api/eatcloud/eatc_kpi_rules?eatc_cua_master= _default &eatc_calculate_from_state=delivered&and_eatc_calculate_from_valid_date=_novacio&_cmp=eatc_kpi,type,rule,eatc_calculate_from_state,and_eatc_calculate_from_valid_date   

 Con la informacin recibida se realizan los siguientes clculos y registros: 

 kpi 
 Nombre del KPI que se est calculando.  Corresponde a al campo eatc_kpi del maestro eatc_kpi_rules .  
 eatc_kpi_rules. eatc_kpi 

 DEPRECADO: Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el primer registro en este campo ser " CO2_tons " (ya que corresponde al campo "eatc_ kpi " de la res =0 del la consulta a https://datagov.eatcloud.info/api/eatcloud/eatc_kpi_rules?eatc_calculate_from_state=received&_cmp=eatc_kpi   

 eatc-kpi_type 
 Tipo de KPI (Social impact, Enviromental impact, Economic impact) del KPI que se est calculando 
 eatc_kpi_rules. type   

 DEPRECADO: Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el primer registro en este campo ser " Environmental impact " (ya que corresponde al campo " type (y su respectiva equivalencia)" de la res =0 del la consulta a https://datagov.eatcloud.info/api/eatcloud/eatc_kpi_rules?eatc_calculate_from_state=received&_cmp=type   

 value   
 Valor calculado del KPI. Resulta de la aplicacin de la regla de clculo (rule) de cada KPI) 
 eatc_kpi_rules. rule ( {{url_entorno_datagov}}/api/eatcloud/eatc_kpi_rules?eatc_calculate_from_state=received&_cmp=rule ) 

 DEPRECADO: Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 

 Para el encabezado de anuncio de donacin cuyo eatc-dona_header_code es 2019209714 , el primer registro en este campo ser " 0,023 KG " (ya que corresponde a aplicar la operacin contenida en el campo " rule " ( eatc_dona_header.eatc-total_weight_kg*(0,023/1000 ) de la primera respuesta de la consulta a https://datagov.eatcloud.info/api/eatcloud/eatc_kpi_rules?eatc_calculate_from_state=received&_cmp=rule de la siguiente manera:  
 eatc_dona_header.eatc-total_weight_kg ( https://donantes.eatcloud.info/api/abaco/eatc_dona_header?eatc-code= 2019209714 ) = 1000 
 {{value}} = [1000 * 0,023/1000] = 0,023  

 Registro en la estructura de datos correspondiente 
 El sistema deber realizar el siguiente registro: 

 REGISTRO CON EL API: {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_kpi&_operacion=update&kpi={{eatc_kpi_rules. eatc_kpi }}& eatc-kpi_type ={{eatc_kpi_rules. type }}& value = {{value}} &WHEREeatc-dona_header_code={{eatc-dona_header_code}} 

 Se debe iterar o recorrer dichas respuestas para generar cada uno de los 17 registros de KPIs que generan cada encabezado con estado recibido 

 OTROS KPIS GENERALES (QUE SE PUEDEN CALCULAR EN TIEMPO REAL) 

 Anuncios Generados ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde al total de los anuncios que se han generado en un periodo de tiempo. Se genera consultando el Api de eatc_dona_headers en un momento especfico y revisando la variable " cont " 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?_id=_*&_compress 

 Porcentaje de anuncios entregados ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde al total de anuncios cuyo estado es entregado o posteriores (pre-certificado y certificado)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc-state=delivered,received,pre-certified,certified&_compress sobre el total de anuncios generados  {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?_id=_*&_compress (por cien) 

 OTROS KPIS QUE SE PUEDEN CALCULAR 
 Peso promedio de la donacin entregada ***IMPLEMENTAR dinamismo a partir de eatc_cua_master.eatc_cua*** 
 Corresponde la sumatoria de todos los pesos de los anuncios generados sobre la cantidad de anuncios generados 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?_id=_*&_compress 

 Desviacin estndar de peso 
 Percentiles de peso 
 Determinar el porcentaje de los anuncios que se encuentran entre los siguientes rangos: 

 De 0 a 2 KG 
 De 2.1 a 5 KG 
 De 5.1 a 10 KG 
 De 10,1 a 20 KG 
 De 20,1 a 50 KG 
 De 50,1 a 100 KG 
 De 100,1 a 200 KG 
 De 200,1 a 500 KG 
 De 500,1 a 1000 KG 
 De 1000,1 a 5000 KG  
 De 5000,1 KG en adelante 

 TOTALIZACIONES PARA CONSULTA DE KPIs 

 Se debe generar un mecanismo que sirva para, a partir de la estructura eatc_dona_kpi, generar totalizaciones que permitan consultar fcilmente estadsticas desde la APP, en las funcionalidades: 

 Donantes: dashboard general ( desktop ) 
 Donantes: detalle de KPIs 
 Beneficiarios: dashboard principal 
 Beneficiarios: detalle de KPIs 

 Las totalizaciones seran las siguientes: 

 Totalizaciones por todo el proyecto EatCloud 
 Se debe sacar de todos los KPIs acumulaciones por todo el proyecto, que comprendan: 

 Total acumulado por KPI 
 Sumatoria de todos los valores (value) de cada KPI 

 Acumulado anual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el 1 de enero del ao en curso 

 Acumulado mensual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el primer da del mes en curso 

 Totalizaciones por punto de donacin eatc_pod 
 Puede ser conveniente que esta informacin tambin cuente con las diversas tipologas (a,b y c) del punto de donacin con el fin de poder realizar consultas o clculos por esos criterios (o evaluar la posibilidad de tambin almacenar acumulados por cada una de dichas tipologas) 

 Total acumulado por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde que la plataforma opera 

 Acumulado anual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el 1 de enero del ao en curso 

 Acumulado mensual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el primer da del mes en curso 

 Totalizaciones por gestor de donaciones eatc_donation_manager 
 Puede ser conveniente que esta informacin tambin cuente con las diversas tipologas (a,b y c) de cada gestor de donaciones, con el fin de poder realizar consultas o clculos por esos criterios (o evaluar la posibilidad de tambin almacenar acumulados por cada una de dichas tipologas) 

 Total acumulado por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde que la plataforma opera 

 Acumulado anual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el 1 de enero del ao en curso 

 Acumulado mensual por KPI 
 Sumatoria de todos los valores (value) de cada KPI desde el primer da del mes en curso 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE KPIs