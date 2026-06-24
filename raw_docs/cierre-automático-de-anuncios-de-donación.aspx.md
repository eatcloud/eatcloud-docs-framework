# cierre-automático-de-anuncios-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CREACIN DE INFORMACIN ESTADSTICA PARA CIERRE AUTOMTICO DE ANUNCIOS 

 En un proceso que puede correr de manera diferenciada (con un script y un cronjob a parte) del proceso de cierre automtico de anuncios.  En este proceso el sistema consulta informacin y realiza clculos para generar informacin estadstica. 

 Consulta del periodo para generacin de estadsticas de tipo dona_time_lapse 

 Para determinar el periodo de tiempo con el cul se realizan las consultas y por ende los clculos estadsticos de lapso de tiempo para el cierre automtico de donaciones, el sistema realiza el siguiente llamado 

 {{URL_datagov}}/ api/eatcloud/eatc_statistical_information_periods?eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_stadistic= dona_time_lapse &_cmp=eatc_period_in_day  

 El valor que trae la consulta (nmero entero), ser utilizado para calcular la fecha inicial para la realizacin de la prxima consulta: 

 {{ fecha_inicial }} = {{ fecha_actual }} - {{eatc_statistical_information_periods. eatc_period_in_day }} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024: 

 El sistema realiza la siguiente consulta 
 https://dev.datagov.eatcloud.info/ api/eatcloud/eatc_statistical_information_periods?eatc_cua_master={{eatc_cua_master. eatc_cua }}&eatc_stadistic= dona_time_lapse &_cmp=eatc_period_in_day   

 Dado que  {{eatc_statistical_information_periods. eatc_period_in_day }} = 7  entonces 
 {{ fecha_inicial }} = 2024-05-2 - 7 (das) = 2024-04-25 

 Consulta de informacin para el clculo de estadsticas 
 Teniendo en cuenta la consulta anterior, el sistema realiza el siguiente llamado al API para obtener la informacin necesaria para realizar el clculo de las estadticas 

 {{URL_donantes}} /api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_inicial }}&eatc-publication_date[1]={{ fecha_actual }}&eatc-state=received,pre-certificated,certificated&_cmp=eatc-programed_picking_datetime,eatc-picking_checkin_datetime,eatc-picking_checkout_datetime,eatc-receipt_datetime,eatc-state  

 Con los datos recibidos realiza el clculo de las siguientes estadsticas 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024: 

 El sistema realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2024-04-25&eatc-publication_date[1]=2024-05-02&eatc-state=received,pre-certificated,certificated&_cmp=eatc-programed_picking_datetime,eatc-picking_checkin_datetime,eatc-picking_checkout_datetime,eatc-receipt_datetime,eatc-state    

 Lapso de tiempo promedio para el checkin a partir de la fecha y hora programada de recogida ( checkin_time_lapse) 

 El sistema para cada registro obtenido en la consulta, realiza la siguiente operacin: 

 {{ individual_checkin_time_lapse }}={{eatc_dona_headers. eatc-picking_checkin_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el nmero de registros obtenidos: 
 {{ checkin_time_lapse }}= SUMATORIA ({{ individual_checkin_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024: 

 {{ individual_checkin_time_lapse_1 }}= 2024-04-30 15:05:00 - 2024-04-30 15:00:00 = 5 minutos 
 {{ individual_checkin_time_lapse_2 }}= 2024-05-03 15:10:00 - 2024-05-03 15:00:00 = 10 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (5 minutos + 10 minutos) / 2 = 15 minutos / 2 = 7.5 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los clculos en minutos, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 Con la informacin obtenida el sistema realiza el siguiente registro: 

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

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=checkin_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_checkin_time_lapse_desc&eatc_stadistic_value=7.5  

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los clculos en minutos, as se registran, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 Lapso de tiempo promedio para el checkout a partir de la fecha y hora programada de recogida ( checkout_time_lapse) 
 El sistema para cada registro obtenido en la consulta, realiza la siguiente operacin: 

 {{ individual_checkout_time_lapse }}={{eatc_dona_headers. eatc-picking_checkout_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el nmero de registros obtenidos: 
 {{ checkout_time_lapse }}= SUMATORIA ({{ individual_checkout_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024: 

 {{ individual_checkout_time_lapse_1 }}= 2024-04-30 15:10:00 - 2024-04-30 15:00:00 = 10 minutos 
 {{ individual_checkout_time_lapse_2 }}= 2024-05-03 15:20:00 - 2024-05-03 15:00:00 = 20 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (10 minutos + 20 minutos) / 2 = 30 minutos / 2 = 15 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los clculos en minutos, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 Con la informacin obtenida el sistema realiza el siguiente registro: 

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

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=checkout_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_checkout_time_lapse_desc&eatc_stadistic_value=15 

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los clculos en minutos, as se registran, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 Lapso de tiempo promedio para la recepcin a partir de la fecha y hora programada de recogida ( receipt_time_lapse) 

 El sistema para cada registro obtenido en la consulta, realiza la siguiente operacin: 
 {{ individual_receipt_time_lapse }}={{eatc_dona_headers. eatc-receipt_datetime }} - {{eatc_dona_headers. eatc-programed_picking_datetime }} 

 Luego realiza un promedio de dichas cifras, dividiendo la sumatoria de las mismas entre el nmero de registros obtenidos: 
 {{ receipt_time_lapse }}= SUMATORIA ({{ individual_receipt_time_lapse }}) / cont 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024: 

 {{ individual_receipt_time_lapse_1 }}= 2024-04-30 16:00:00 - 2024-04-30 15:00:00 = 60 minutos 
 {{ individual_receipt_time_lapse_2 }}= 2024-05-03 17:00:00 - 2024-05-03 15:00:00 = 120 minutos 

 {{ checkin_time_lapse }}= SUMATORIA (60 minutos + 120 minutos) / 2 = 180 minutos / 2 = 90 minutos 

 Nota para el desarrollador: para el ejemplo se realizaron los clculos en minutos, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 Con la informacin obtenida el sistema realiza el siguiente registro: 

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

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de pruebas, da actual: 2 de mayo de 2024, hora 11:59 PM 

 https://dev.datagov.info/crd/eatcloud/?_tabla=eatc_statistical_information&_operacion=insert&eatc_date=2024-05-02 23:59:59&eatc_datetime=2024-05-02 23:59:59&eatc_stadistic=receipt_time_lapse&eatc_period_in_day=7&eatc_cua_master=abaco&eatc_stadistic_desc=lbl_receipt_time_lapse_desc&eatc_stadistic_value=90 

 Nota para el desarrollador: para el ejemplo y dado que se realizaron los clculos en minutos, as se registran, pero el desarrollador deber definir la unidad de medida que ms le facilite sumarle a fechas y horas y  obtener los resultados que se calcularn con estas estadsticas. 

 CIERRE AUTOMTICO DE ANUNCIOS: 
 El proceso de cierre automtico de anuncios debe correr para todas las cuentas maestras registradas en el respectivo maestro, por lo menos una vez al da (preferiblemente en horario nocturno) mediante cronjob  
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 

 Su corrida debe ser posterior a la del proceso de generacin de datos estadsticos, con el nimo de garantizar tener dichos datos estadsticos para realizar las respectivas operaciones: 

 Consulta del timeout " dona_aut_closing_timeout " en eatc_timeout_rules 

 El sistema debe cerrar automticamente los  anuncios de donacin que hallan sido programados, pero que en el tiempo determinado en el esquema de persistencia eatc_timeout_rules no hallan sido cerrados por el gestor de donaciones (es decir, cuando no han sido gestionados hasta su verificacin detallada) se obtiene leyendo el parmetro " eatc-timeout_in_hours " del respectivo timeout 

 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_timeout_rules?eatc-timeout_name= dona_aut_closing_timeout &_cmp= eatc-timeout_from, eatc-timeout_in_hours 

 Los valores que trae la consulta ( {{eatc_timeout_rules. eatc-timeout_from }} , {{eatc_timeout_rules. eatc-timeout_in_hours }} ), se guardan para los procesos posteriores 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_aut_closing_timeout&_cmp= eatc-timeout_from, eatc-timeout_in_hours   

 Consulta de anuncios:  

 El sistema debe consultar aquellos anuncios con estado ( eatc-state ) "scheduled" (programados) y "delivered" (entregados). 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc-state=scheduled,delivered&_cmp=eatc-code, {{eatc_timeout_rules. eatc-timeout_from }} 

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 
 Como la primera consulta trajo que {{eatc_timeout_rules. eatc-timeout_from }}= eatc-programed_picking_datetime el sistema realiza la siguiente consulta: 

 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=scheduled,delivered&_cmp=eatc-code, eatc-programed_picking_datetime   

 Comparaciones (para cerrar los anuncios a partir del timeout):  

 Posteriormente deben comparar los datos que llegan en " eatc_dona_headers. {{eatc_timeout_rules. eatc-timeout_from }} ", con la fecha y hora actual.  Si la diferencia entre la fecha de recogida programada y la fecha y hora actual es mayor o igual al dato recibido en  {{eatc_timeout_rules. eatc-timeout_in_hours }}   para cada anuncio se deben ejecutar las siguientes acciones:  

 Acciones para el cierre de donaciones 

 Accin 1: Consulta de datos estadsticos aplicables 
 El sistema realiza la siguiente consulta.   
 {{URL_datagov}}api/eatcloud/eatc_statistical_information?eatc_date={{fecha_actual}}&eatc_cua_master=abaco&eatc_stadistic=checkin_time_lapse,checkout_time_lapse,receipt_time_lapse&_cmp=eatc_stadistic, eatc_stadistic_value 

 Si el sistema no trae resultados (por algn problema en el proceso de generacin de datos estadsticos), se debe intentar con la fecha del da anterior, y as sucesivamente hasta obtener un registro vlido, y deber generar una alerta a un grupo de Telegram, para anunciar que existe un problema en la generacin de datos estadsticos. 

 Accin 2: Clculo de fechas y horas a partir de datos estadsticos 
 Con los datos estadsticos previamente consultados, el sistema calcular las siguientes fechas, para llevarlas a la actualizacin  a los diferentes encabezados de anuncios de donacin a los cuales les aplica el proceso de cierre automtico. 

 {{ eatc-picking_checkin_datetime }} = {{eatc-programed_picking_datetime}} + {{ {{URL_datagov}}api/eatcloud/eatc_statistical_information?eatc_date={{fecha_actual}}&eatc_cua_master=abaco&eatc_stadistic=checkin_time_lapse&_cmp= eatc_stadistic_value }} 
 {{ eatc-picking_checkout_datetime }} = {{eatc-programed_picking_datetime}} + {{ {{URL_datagov}}api/eatcloud/eatc_statistical_information?eatc_date={{fecha_actual}}&eatc_cua_master=abaco&eatc_stadistic=checkout_time_lapse&_cmp= eatc_stadistic_value }} 
 {{ eatc-receipt_datetime }} = {{eatc-programed_picking_datetime}} + {{ {{URL_datagov}}api/eatcloud/eatc_statistical_information?eatc_date={{fecha_actual}}&eatc_cua_master=abaco&eatc_stadisticreceipt_time_lapse&_cmp= eatc_stadistic_value }} 

 Accin 3: Actualizacin de la informacin del encabezado de donacin ( eatc_dona_headers ) 

 Con el clculo de las nuevas fechas realizadas en la accin anterior, el sistema deber realizar la siguiente actualizacin de datos del encabezado del anuncio de donacin 

 {{URL_donantes}} /crd/{{eatc_cua_master. eatc_cua }}/?_tabla=eatc_dona_headers&_operacion=update&eatc-picking_checkin_datetime= {{ eatc-picking_checkin_datetime }} &eatc-picking_checkout_datetime= {{ eatc-picking_checkout_datetime }} &eatc-receipt_datetime= {{ eatc-receipt_datetime }} &eatc-state= received &WHEREeatc-code={{eatc_dona_headers. eatc-code }}  

 Accin 4: registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 

 Se debe registrar el estado "announced" procurando incorporar la informacin del adjudicatario al cual se le elimin la adjudicacin, en el campo ( eatc-log )  
 eatc-dona_header_code = {{eatc_dona_headers. eatc-code }} 
 eatc-state = received 
 eatc-date_time ={{Fecha  y hora actual en formato AAAA-MM-DD HH:MM:SS}} 
 eatc-log ="EatCloud cerr automticamente esta donacin, porque despus de {{eatc_timeout_rules. eatc-timeout_in_hours }} horas el beneficiario no complet la gestin del anuncio" 

 Utilizando el API el registro sera algo como lo siguiente 

 {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }} /?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state = received & eatc-date_time = {{Fecha  y hora actual en formato AAAA-MM-DD HH:MM:SS}} & eatc-log =" EatCloud cerr automticamente esta donacin, porque despus de {{eatc_timeout_rules. eatc-timeout_in_hours }} horas el beneficiario no complet la gestin del anuncio " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CIERRE AUTOMTICO DE ANUNCIOS DE DONACIN