# cálculo-de-información-estadística.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CREACIÓN DE INFORMACIÓN ESTADÍSTICA PARA CIERRE AUTOMÁTICO DE ANUNCIOS 

 En un proceso que puede correr de manera diferenciada (con un script y un cronjob a parte) del proceso de cierre automático de anuncios.  En este proceso el sistema consulta información y realiza cálculos para generar información estadística. 

 Consulta del periodo para generación de estadísticas de tipo dona_time_lapse 

 Para determinar el periodo de tiempo con el cuál se realizan las consultas y por ende los cálculos estadísticos de lapso de tiempo para el cierre automático de donaciones, el sistema realiza el siguiente llamado 

 {{URL_datagov}}/ api/eatcloud/eatc_statistical_information_periods?eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_stadistic= dona_time_lapse &_cmp=eatc_period_in_day  

 El valor que trae la consulta (número entero), será utilizado para calcular la fecha inicial para la realización de la próxima consulta: 

 {{ fecha_inicial }} = {{ fecha_actual }} - {{eatc_statistical_information_periods. eatc_period_in_day }} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024: 

 El sistema realiza la siguiente consulta 
 https://dev.datagov.eatcloud.info/ api/eatcloud/eatc_statistical_information_periods?eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_stadistic= dona_time_lapse &_cmp=eatc_period_in_day   

 Dado que  {{eatc_statistical_information_periods. eatc_period_in_day }} = 7  entonces 
 {{ fecha_inicial }} = 2024-05-2 - 7 (días) = 2024-04-25 

 Consulta de información para el cálculo de estadísticas 

 Teniendo en cuenta la consulta anterior, el sistema realiza el siguiente llamado al API para obtener la información necesaria para realizar el cálculo de las estadíticas 

 {{URL_donantes}} /api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_actual }}&eatc-state=received,pre-certificated,certificated&_cmp=eatc-programed_picking_datetime,eatc-picking_checkin_datetime,eatc-picking_checkout_datetime,eatc-receipt_datetime,eatc-state  

 Con los datos recibidos realiza el cálculo de las siguientes estadísticas 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024: 

 El sistema realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-04-25&eatc-publication_date[1]=2024-05-02&eatc-state=received,pre-certificated,certificated&_cmp=eatc-programed_picking_datetime,eatc-picking_checkin_datetime,eatc-picking_checkout_datetime,eatc-receipt_datetime,eatc-state    

 Lapso de tiempo promedio para el checkin a partir de la fecha y hora programada de recogida ( checkin_time_lapse) 

 El sistema para cada registro obtenido en la consulta, realiza la siguiente operación: 
 {{ individual_checkin_time_lapse }}={{eatc_dona_headers. eatc-picking_checkin_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el número de registros obtenidos: 
 {{ checkin_time_lapse }}= SUMATORIA ({{ individual_checkin_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024: 

 {{ individual_checkin_time_lapse_1 }}= 2024-04-30 15:05:00 - 2024-04-30 15:00:00 = 5 minutos 
 {{ individual_checkin_time_lapse_2 }}= 2024-05-03 15:10:00 - 2024-05-03 15:00:00 = 10 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (5 minutos + 10 minutos) / 2 = 15 minutos / 2 = 7.5 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los cálculos en minutos, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 Con la información obtenida el sistema realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha  y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= checkin_time_lapse 
 eatc_period_in_day= {{eatc_statistical_information_periods. eatc_period_in_day }} 
 eatc_cua_master= {{eatc_cua_master. eatc_cua }} 
 eatc_stadistic_desc= lbl_checkin_time_lapse_desc 
 eatc_stadistic_value={{ checkin_time_lapse }} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert& {{parametros_para_el_registro}} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=checkin_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_checkin_time_lapse_desc&eatc_stadistic_value=7.5  

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los cálculos en minutos, así se registran, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 Lapso de tiempo promedio para el checkout a partir de la fecha y hora programada de recogida ( checkout_time_lapse) 

 El sistema para cada registro obtenido en la consulta, realiza la siguiente operación: 
 {{ individual_checkout_time_lapse }}={{eatc_dona_headers. eatc-picking_checkout_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el número de registros obtenidos: 
 {{ checkout_time_lapse }}= SUMATORIA ({{ individual_checkout_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024: 

 {{ individual_checkout_time_lapse_1 }}= 2024-04-30 15:10:00 - 2024-04-30 15:00:00 = 10 minutos 
 {{ individual_checkout_time_lapse_2 }}= 2024-05-03 15:20:00 - 2024-05-03 15:00:00 = 20 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (10 minutos + 20 minutos) / 2 = 30 minutos / 2 = 15 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los cálculos en minutos, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 Con la información obtenida el sistema realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha  y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= checkout_time_lapse 
 eatc_period_in_day= {{eatc_statistical_information_periods. eatc_period_in_day }} 
 eatc_cua_master= {{eatc_cua_master. eatc_cua }} 
 eatc_stadistic_desc= lbl_checkout_time_lapse_desc 
 eatc_stadistic_value={{ checkout_time_lapse }} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert& {{parametros_para_el_registro}} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=checkout_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_checkout_time_lapse_desc&eatc_stadistic_value=15 

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los cálculos en minutos, así se registran, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 Lapso de tiempo promedio para la recepción a partir de la fecha y hora programada de recogida ( receipt_time_lapse) 

 El sistema para cada registro obtenido en la consulta, realiza la siguiente operación: 
 {{ individual_receipt_time_lapse }}={{eatc_dona_headers. eatc-receipt_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el número de registros obtenidos: 
 {{ receipt_time_lapse }}= SUMATORIA ({{ individual_receipt_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024: 

 {{ individual_receipt_time_lapse_1 }}= 2024-04-30 16:00:00 - 2024-04-30 15:00:00 = 60 minutos 
 {{ individual_receipt_time_lapse_2 }}= 2024-05-03 17:00:00 - 2024-05-03 15:00:00 = 120 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (60 minutos + 120 minutos) / 2 = 180 minutos / 2 = 90 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los cálculos en minutos, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 Con la información obtenida el sistema realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date = {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime = {{Fecha  y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic = receipt _time_lapse 
 eatc_period_in_day = {{eatc_statistical_information_periods. eatc_period_in_day }} 
 eatc_cua_master = {{eatc_cua_master. eatc_cua }} 
 eatc_stadistic_desc = lbl_ receipt _time_lapse_desc 
 eatc_stadistic_value ={{ checkin_time_lapse }} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert& {{parametros_para_el_registro}} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, día actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=receipt_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_receipt_time_lapse_desc&eatc_stadistic_value=90 

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los cálculos en minutos, así se registran, pero el desarrollador deberá definir la unidad de medida que más le facilite sumarle a fechas y horas y  obtener los resultados que se calcularán con estas estadísticas. 

 ***NUEVO: CREACIÓN DE INFORMACIÓN ESTADÍSTICA PARA INFORME AVANZADO DE CANCELADOS *** 

 En un proceso que puede correr el primer día de cada mes en la madrugada, dado que se diseña para calcular información mensual por punto de donación. 

 Se recomienda hacer un proceso a parte de los ya desarrollados para información estadística, que pueda correr de manera discreta, durante la madrugada el primer día hábil de cada mes, para sacer las estadísticas del mes anterior. 

 Tambien se debe realizar un proceso discreto que calcule las estadísticas de meses anteriores, y que corra de manera nocturna, hasta que cubra un periodo de cálculo de hasta dos años más un mes atrás, haciendo cálculos mensuales (las presentes estadísticas se calculan por mes). 

 Consulta de los puntos de donación a los cuales se les calculará la información estadística de cancelados 

 Para determinar los puntos  de donación a los culaes se les calculará la información estadística de cancelados, el sistema determinará cuales puntos de donación tuvieron cancelados en el mes anterior con la siguiente consulta (se deberá realizar una consulta por cuenta maestra) 

 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled &_distinct= eatc-pod_id 

 Ejemplo: Ambiente de pruebas, proceso que corrió el primero de febrero de 2024 
Dado que el mes anterior es enero de 2024, el sistema los siguientes llamados (uno por cuenta maestra activa): 

 https://devdonantes.eatcloud.info/ api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=cancelled&_distinct=eatc-pod_id   

 https://devdonantes.eatcloud.info/api/mexico/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=cancelled&_distinct=eatc-pod_id   

 Para cada punto de donación que se encuentre con la anterior consulta se deberá consultar información estadística de cancelados (cantidad, sumatoria de kilogramos, sumatoria de valores, sumatoria de referencias y sumatoria de unidades) e información para realizar filtros y agrupaciones de información (principalmente datos de ubicación como cuenta, país, provincia y ciudad. 

 Consulta de información para el cálculo de estadísticas 
 Para cada punto del array de puntos con donaciones canceladas, el sistema deberá realizar las siguientes consultas 

Consulta de datos para filtro y agrupaciones: 
El sistema deberá guardar los datos de ubicación de cada punto del array haciendo la siguiente consulta: 

 {{ URL_donantes }}/api/ allpods / eatc_pods ?eatc-id={{eatc_dona_headers. eatc-pod_id }}&_cmp=eatc-id,eatc-cua,eatc-cua_master,eatc-province,eatc-city,eatc_comuna_localidad 

 Cada dato del punto obtenido (allpods/eatc_pods. {{parametro_en_cmp}} ) se guarda para realizar consultas y para registrar la respectiva estadística: 

 eatc_pods .eatc-id 
 eatc_pods .eatc-cua 
 eatc_pods .eatc-cua_master 
 eatc_pods .eatc-province 
 eatc_pods .eatc-city 
 eatc_pods .eatc_comuna_localidad 

En algunos casos esta consulta puede traer doble registro, entonces el sistema deberá guardar ambos conjuntos de valores, dado que más adelante las consultas se realizan con la dupa código del punto (eatc-id) y cuenta de usuario (eatc-cua)

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=mexico, eatc_dona_headers. eatc-pod_id=RdP40wnLssgOrTnEghpEc: 

 El sistema realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc-id=RdP40wnLssgOrTnEghpEc&_cmp=eatc-id,eatc-cua,eatc-cua_master,eatc-province,eatc-city,eatc_comuna_localidad   

El sistema guarda la respuesta para próximas consultas e inserciones de datos 

 Consulta y registro de datos estadísticos: 
El sistema realizará las siguientes consultas de datos estadísticos, para en algunos casos realizar registros directos y en otros casos realizar razones simples, para calcular porcentajes con las respuestas obtenidas. 

 Cantidad de anuncios cancelados (lbl_anuncios_cancelados) 
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_cont 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_anuncios_cancelados   ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_anuncios_cancelados_desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _cont }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema previamente había hecho esta consulta: 

 https://devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc-id=42&_cmp=eatc-id,eatc-cua,eatc-cua_master,eatc-province,eatc-city,eatc_comuna_localidad   

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=cancelled&eatc-pod_id=42 & eatc_cua_origin =exito&_cont   

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_anuncios_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_anuncios_cancelados_desc 
eatc_stadistic_value= 6 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_anuncios_cancelados& eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_anuncios_cancelados_desc& eatc_stadistic_value= 6 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01  

 Cantidad de anuncios (lbl_anuncios_de_donacion) 
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= _* & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_cont 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_anuncios_de_donacion ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_anuncios_de_donacion_desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ _cont }}   ***Sacado de la anterior consulta*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 
 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert& {{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=_*&eatc-pod_id=42 & eatc_cua_origin =exito&_cont   

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_anuncios_de_donacion 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_anuncios_de_donacion_desc 
eatc_stadistic_value= 6 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_anuncios_de_donacion& eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_anuncios_de_donacion_desc& eatc_stadistic_value= 6 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 Porcentaje de anuncios cancelados ( lbl_pct_anuncios_cancelados ) 

 El sistema a partir de los cálculos anteriores determina que: 

 lbl_pct_anuncios_cancelados = ( lbl_anuncios_cancelados / lbl_anuncios_de_donacion) * 100 

 Con la información obtenida en esta operación y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_pct_anuncios_cancelados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= l bl_pct_anuncios_cancelados_desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ lbl_pct_anuncios_cancelados }}   ***Sacado del cálculo anterior*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 

 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 Dadas las anteriores estadísticas el sistema determina que 

 lbl_pct_anuncios_cancelados = ( 6 / 6) * 100 =100 

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_pct_anuncios_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_pct_anuncios_cancelados_desc 
eatc_stadistic_value= 100 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_pct_anuncios_cancelados & eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_pct_anuncios_cancelados _desc& eatc_stadistic_value= 100 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 kg cancelados (lbl_kg_cancelados)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc-total_weight_kg 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_kg_cancelados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_kg_cancelados _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=cancelled&eatc-pod_id=42 & eatc_cua_origin =exito&_sum= eatc-total_weight_kg   

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_kg_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_kg_cancelados _desc 
eatc_stadistic_value= 64.42 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_kg_cancelados & eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_kg_cancelados _desc& eatc_stadistic_value= 64.42 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 KG totales anunciados (lbl_kg_totales_anunciados)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}& eatc-state= _* & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc-total_weight_kg 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_kg_totales_anunciados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_kg_totales_anunciados _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=_*&eatc-pod_id=42 & eatc_cua_origin =exito&_sum= eatc-total_weight_kg   

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_kg_totales_anunciados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_kg_totales_anunciados _desc 
eatc_stadistic_value= 64.42 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_kg_totales_anunciados & eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_kg_totales_anunciados _desc& eatc_stadistic_value= 64.42 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 % de kilogramos cancelados ( lbl_pct_kg_cancelados ) 

 El sistema a partir de los cálculos anteriores determina que: 

 lbl_pct_kg_cancelados = ( lbl_kg_cancelados / lbl_kg_totales_anunciados ) * 100 

 Con la información obtenida en esta operación y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_pct_kg_cancelados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= l bl_pct_kg_cancelados_desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ lbl_pct_kg_cancelados }}   ***Sacado del cálculo anterior*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 

 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 Dadas las anteriores estadísticas el sistema determina que 

 lbl_pct_kg_cancelados = ( 64.42 / 64.42 ) * 100 =100 

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_pct_kg_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_pct_kg_cancelados_desc 
eatc_stadistic_value= 100 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_pct_kg_cancelados& eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_pct_kg_cancelados_desc& eatc_stadistic_value= 100 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 Valor al costo anuncios cancelados (lbl_valor_al_costo_cancelados)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc-total_cost 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_valor_al_costo_cancelados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_valor_al_costo_cancelados _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=cancelled&eatc-pod_id=42 & eatc_cua_origin =exito&_sum= eatc-total_cost     

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_valor_al_costo_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_valor_al_costo_cancelados _desc 
eatc_stadistic_value= 603198.15 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_kg_cancelados & eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_kg_cancelados _desc& eatc_stadistic_value= 603198.15 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 Valor al costo de los anuncios (lbl_valor_al_costo_anuncios)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}& eatc-state= _* & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc-total_cost 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_valor_al_costo_anuncios ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_valor_al_costo_anuncios _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 El sistema realiza la siguiente consulta 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-01-01&eatc-publication_date[1]=2024-01-31&eatc-state=_*&eatc-pod_id=42 & eatc_cua_origin =exito&_sum= eatc-total_cost     

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_valor_al_costo_anuncios 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_valor_al_costo_anuncios _desc 
eatc_stadistic_value= 603198.15 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_kg_totales_anunciados & eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_kg_totales_anunciados _desc& eatc_stadistic_value= 64.42 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 % de cancelados en valor al costo ( lbl_pct_valor_al_costo_cancelados ) 

 El sistema a partir de los cálculos anteriores determina que: 

 lbl_pct_valor_al_costo_cancelados = ( lbl_valor_al_costo_cancelados / lbl_valor_al_costo_anuncios ) * 100 

 Con la información obtenida en esta operación y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_pct_valor_al_costo_cancelados ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_pct_valor_al_costo_cancelados_desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ lbl_pct_valor_al_costo_cancelados }}   ***Sacado del cálculo anterior*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 

 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 Ejemplo: ambiente de pruebas, eatc_cua_master. eatc_cua=abaco, eatc_dona_headers. eatc-pod_id=42, cálculos realizados el 1 de febrero de 2024 en horas de la madrugada (a las 2 AM) 

 Dadas las anteriores estadísticas el sistema determina que 

 lbl_pct_valor_al_costo_cancelados = ( 603198.15 / 603198.15 ) * 100 =100 

 Dadas las anteriores consultas, el sistema determina lo siguiente: 

 {{parametros_para_el_registro}} 

 eatc_date= 2024-02-01 
 eatc_datetime=2024-02-01 02:00:00 
 eatc_stadistic= lbl_pct_valor_al_costo_cancelados 
 eatc_period_in_day= 31 
 eatc_cua_master= abaco 
 eatc_cua=exito 
 eatc_stadistic_desc= lbl_pct_valor_al_costo_cancelados_desc 
eatc_stadistic_value= 100 
eatc_province=ANTIOQUIA 
eatc_city=RIONEGRO 
eatc_locality=     ***Como no arroja resultados, no se registra dato*** 
eatc_pod_id=42 
 eatc_stadistic_value_year=2024 
 eatc_stadistic_value_month=01 
 eatc_stadistic_value_year_month=2024-01 

 Por lo tanto el sistema realiza la siguiente inserción a la tabla de información estadística 

 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&eatc_date= 2024-02-01& eatc_datetime=2024-02-01 %20 02:00:00&eatc_stadistic= lbl_pct_valor_al_costo_cancelados& eatc_period_in_day= 31& eatc_cua_master= abaco& eatc_cua=exito & eatc_stadistic_desc= lbl_pct_valor_al_costo_cancelados_desc& eatc_stadistic_value= 100 & eatc_province=ANTIOQUIA&eatc_city=RIONEGRO&eatc_pod_id=42 &eatc_stadistic_value_year=2024&eatc_stadistic_value_month=01&eatc_stadistic_value_year_month=2024-01 

 Referencias canceladas (lbl_referencias_canceladas)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc_dona_references 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_referencias_canceladas ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_referencias_canceladas _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Referencias donadas (lbl_referencias_donadas)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}& eatc-state= _* & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc_dona_references 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_referencias_donadas ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_referencias_donadas _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Porcentaje de referencias canceladas (lbl_porcentaje_cancelados_referencias) 

 El sistema a partir de los cálculos anteriores determina que: 

 lbl_porcentaje_cancelados_referencias = ( lbl_referencias_canceladas / lbl_referencias_donadas ) * 100 

 Con la información obtenida en esta operación y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_porcentaje_cancelados_referencias ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_porcentaje_cancelados_referencias _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ lbl_porcentaje_cancelados_referencias }}   ***Sacado del cálculo anterior*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 

 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 Unidades canceladas (lbl_unidades_canceladas) 
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}&eatc-state= cancelled & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc_dona_references 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_unidades_canceladas ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_unidades_canceladas _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 Unidades (lbl_unidades)  
El sistema realiza la siguiente consulta: 
 {{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-publication_date[0]={{ primer_día_mes_anterior }}&eatc-publication_date[1]={{ ultimo_día_mes_anterior }}& eatc-state= _* & eatc-pod_id= {{eatc_dona_headers. eatc-pod_id }}& eatc_cua_origin ={{eatc_dona_headers. eatc-cua }}&_sum= eatc_dona_units 

 Con la información obtenida en esta y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_unidades ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_unidade _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_stadistic_value={{ _sum }}   ***Sacado de la anterior consulta*** 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_del_cálculo en formato AAAA}} 
 eatc_stadistic_value_month={{mes_del_cálculo en formato MM}} 
 eatc_stadistic_value_year_month={{año_mes_del_cálculo en formato AAAA-MM}} 

 Registro utilizando el servicio crd 
 {{URL_datagov}}/crd/eatcloud/?_tabla= eatc_statistical_information &_operacion=insert&{{parametros_para_el_registro}} 

 % de unidades de producto canceladas ( lbl_pct_unidades_canceladas ) 

 El sistema a partir de los cálculos anteriores determina que: 

 lbl_pct_unidades_canceladas = ( lbl_referencias_canceladas / lbl_referencias_donadas ) * 100 

 Con la información obtenida en esta operación y las anteriores consultas realiza el siguiente registro: 

 {{parametros_para_el_registro}} 
 eatc_date= {{Fecha actual en formato AAAA-MM-DD}} 
 eatc_datetime= {{Fecha y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_stadistic= lbl_pct_unidades_canceladas ***Constante*** 
 eatc_period_in_day= {{número_dias_mes_calculado}} 
 eatc_cua_master= {{ eatc_pods .eatc-cua_master }} 
 eatc_stadistic_desc= lbl_pct_unidades_canceladas _desc ***Constante*** 
 eatc_cua={{ eatc_pods .eatc-cua}} 
 eatc_stadistic_value={{ lbl_pct_unidades_canceladas }}   ***Sacado del cálculo anterior*** 
eatc_province= {{ eatc_pods .eatc-province}} 
eatc_city= {{ eatc_pods .eatc-city}} 
eatc_locality= {{ eatc_pods .eatc_comuna_localidad}} 
 eatc_pod_id={{ eatc_pods .eatc-id }} 
 eatc_stadistic_value_year={{año_mes_calculado en formato AAAA}} 

 eatc_stadistic_value_month={{mes_calculado en formato MM}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CÁLCULO DE INFORMACIÓN ESTADÍSTICA