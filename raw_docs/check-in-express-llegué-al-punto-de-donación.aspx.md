# check-in-express-llegué-al-punto-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 [NUEVO] Este proceso se habilitar para todos los usuarios, sin importar si la cuenta respectiva del donante asociado a la donacin, tiene potestad de editar coordenadas.  Para todos los usuarios se habilita esta funcionalidad, registrando la fecha y hora de checkin e incorporando la funcionalidad de registro extemporneo, con registro en la nueva estructura de issues. 

 [NUEVO] V ALIDACIN DE LA FECHA Y HORA ACTUAL VS LA FECHA Y HORA PROGRAMADA DE RECOGIDA (EATC-PROGRAMED_PICKING_DATETIME) 

 El sistema debe comparar la fecha y hora actual ( current_datetime ) con la fecha y hora de recogida estampada en el anuncio ( eatc_dona_headers. eatc-programed_picking_datetime ).  

 La fecha y hora actual es menor en el tiempo definido por el "checkin_timeout" que la fecha y hora programada de recogida ***REVISAR dinamismo a partir de _DOM.cua_master*** 

 Si la hora actual es menor a la hora programada de recogida ms la cantidad de tiempo definido por el timeout " checkin_timeout " en sus parmetros: eatc-timeout_in_minutes o eatc-timeout_in_hours y cuyos datos se obtienen realizando la siguiente consulta:  

 {{URL_entorno_donantes}}api/{{_DOM. cua_master }}/eatc_timeout_rules?eatc-timeout_name= checkin_timeout 

 Entonces se procede a tomar la fecha y hora actual (current_datetime) y a realizar el registro de la fecha y hora de check-in (es un funcionamiento muy similar al original de la funcionalidad). 

 Mediante el API (CRUD), el sistema debe registrar la fecha y hora de llegada ( eatc-picking_checkin_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{ _DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update&eatc-picking_checkin_datetime={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}&WHEREeatc-code={{eatc_dona_headers.eatc-code}} 

 Ejemplo, _DOM. cua_maste=abaco, ambiente de pruebas: 

 En ambiente de pruebas, para el anuncio de donacin cuyo eatc-code = 40717 , y que mediante la App se accion el botn de registro de llegada de beneficiario a las 2019-09-19 01:35:54  mediante la API se debe hacer la siguiente escritura 

 https://devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&_operacion=update&eatc-picking_checkin_datetime= 2019-09-19%2001:35:54 &WHEREeatc-code=40717  

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 [NUEVO] La fecha y hora actual es mayor en el tiempo definido por el "checkin_timeout" que la fecha y hora programada de recogida ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Si la hora actual es superior a la hora programada de recogida en la cantidad de tiempo definido por el timeout " checkin_timeout " en sus parmetros: eatc-timeout_in_minutes o eatc-timeout_in_hours (y cuyos datos se obtienen realizando la siguiente consulta:  

 {{URL_entorno_donantes}}api/ {{ _DOM. cua_master }} /eatc_timeout_rules?eatc-timeout_name= checkin_timeout )  

 Entonces el sistema debe mostrar el siguiente mensaje: 

 Ya han pasado ms de {{(eatc_timeout_rules?eatc-timeout_name= checkin_timeout ).eatc-timeout_in_minutes}} minutos de la fecha y hora programada de recogida.  Deseas registrar la fecha y hora actual como la correspondiente a tu llegada al punto de donacin 

 SI   NO 

 OPCIN SI: 
 Si el usuario acciona la opcin "SI", el sistema debe tomar la fecha y  hora actual para realizar el siguiente registro: 

 Mediante el API (CRUD), el sistema debe registrar la fecha y hora de llegada ( eatc-picking_checkin_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{ _DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update&eatc-picking_checkin_datetime={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}&WHEREeatc-code={{eatc_dona_headers.eatc-code}} 

 Ejemplo: 
 Para el anuncio de donacin cuyo eatc-code = 40717 , y que mediante la App se accion el botn de registro de llegada de beneficiario a las 2019-09-19 01:35:54  mediante la API se debe hacer la siguiente escritura 

 https://devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&_operacion=update&eatc-picking_checkin_datetime= 2019-09-19%2001:35:54 &WHEREeatc-code=40717  

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 OPCIN NO ***Requiere internacionalizacin*** 
 El sistema debe preguntar el motivo por el registro extemporneo presentando un selector de motivos de registro extemporneos y luego debe presentar datetime pickers para registrar la hora del checki-n y check-out (este de manera opcional), de la siguiente manera. 

 Motivo del registro de llegada extemporneo: 
 Tipo de dato : sting 
 Tipo de input de datos: dropdown nico 
 Valor por defecto : vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad 

 La informacin se toma de (maestro): 

 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 

 ***NUEVO: Paso 2: consulta de los causales de checkin extemporneos en datos internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language={{codigo_dos_digitos_idioma}}&eatc_mt= eatc_extemporaneous_checkin_causes 

 Ejemplo: idioma espaol a 10 de diciembre de 2020: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=es&eatc_mt= eatc_extemporaneous_checkin_causes     

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto (ingls= en idioma por defecto): 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_extemporaneous_checkin_causes &eatc_language= en   

 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en los selectores: 

 Ejemplo: idioma espaol a 10 de diciembre de 2020, entorno productivo: 
 Se mostraran los selectores con los siguientes labels 

 Envi a otra persona y no le validaron el cdigo de llegada 
 Me olvid registrar la llegada cuando lo hice 
 Tuve problemas con la aplicacin y cuando quise hacer el registro de llegada, no funcion 
 No me validaron el cdigo para la recogida de la donacin  a tiempo 
 El que recogi la donacin no tiene el aplicativo 

 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/eatcloud/ eatc_extemporaneous_checkin_causes ?_id={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro los valores eatc_extemporaneous_checkin_causes. eatc-issue_cause_code y eatc_extemporaneous_checkin_causes. eatc-issue_cause 

 Ejemplo, continuando con el anterior 
 Si el usuario selecciona " El que recogi la donacin no tiene el aplicativo " entonces eatc_internationalize_dt. eatc_data_id= 5 por lo tanto al hacer la siguiente consulta: https://beneficiarios.eatcloud.info/api/eatcloud/ eatc_extemporaneous_checkin_causes ?_id=5 al registro se llevara el valor " eatc_checkin_and_deliver_issues . eatc-issue_cause_code " = " e_chkin5 " y " eatc_checkin_and_deliver_issues . eatc-issue_cause " = " El que recogi la donacin no tiene el aplicativo" 

 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos):  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause   (ms adelante se muestra como se hace el registro completo del issue en este object store ) 
 Se guarda con (para efectos indicativos, no prcticos): 
{{URL_entorno_donantes}}/crd/{{_DOM. cua_user }}/?_tabla=eatc_checkin_and_deliver_issues&_operacion=insert& eatc-issue_cause_code ={{ eatc_extemporaneous_checkin_causes. eatc-issue_cause_code }}& eatc-issue_cause ={{ eatc_extemporaneous_checkin_causes. eatc-issue_cause }} 

 Fecha y hora de llegada al punto de donacin:   
 Tipo de dato : datetime 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la hora registrada en eatc_dona_headers .eatc-programed_picking_datetime 
 Validaciones :  
 La fecha y hora no puede ser menor a eatc_dona_headers .eatc-adjudication_datetime   
 La fecha no puede ser mayor a la que se origina de sumarle el dona_global_scheduling_timeout respectivo a la eatc_dona_headers .eatc-adjudication_datetime (que se obtiene con la consulta {{URL_entorno_donantes}}/api/ {{CUA_master}} /eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout siendo en este caso el CUA_master "abaco" 
 Se guarda en :  
Encabezado de anuncio de donacin: eatc_dona_headers .eatc-picking_checkin_datetime   

 Registro en eatc_dona_headers ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Con el llamado respectivo se realiza la actualizacin de las fechas y horas de check-in y check-out y el cambio de estado de la donacin a delivered 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{ _DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update&eatc-state= delivered &eatc-picking_checkin_datetime={{fecha y hora del datetime picker en formato AAAA-MM-DD HH:MM:SS}} & WHEREeatc-code={{eatc_dona_headers.eatc-code}} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro en eatc_checkin_and_deliver_issues 

 El registro en este object store de issues de checkin y despacho, toma datos de de la fecha y hora actual, el anuncio de donacin y los registros de fecha y hora para llevarlos a un repositorio en donde los mismos estarn disponibles para futuras validaciones.  El registro involucra los siguientes parmetros: 

 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: se deja vaco.  
 eatc-final_doma_name: se deja vaco.  
 eatc-dona_initial_state : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-verification_code: se enva vaco (por el momento). 
 eatc-token : por el momento se deja vaco.  En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-issue_cause_code : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc_extemporaneous_checkin_causes. eatc-issue_cause_code . 
 eatc-issue_cause : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc_extemporaneous_checkin_causes. eatc-issue_cause 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): app_extemporaneous_checkin 

 resolved : se coloca en este punto: si 

 Escritura con la API (METODO POST):  

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=insert& eatc-date ={{fecha actual en formato AAAA-MM-DD}} & eatc-datetime ={{fecha actual en formato AAAA-MM-DD HH:MM:SS}}& eatc-donor_code ={{eatc_dona_headers. eatc-donor_code }}& eatc-donor ={{eatc_dona_headers. eatc-donor }}& eatc-pod_id ={{ eatc_dona_headers. eatc-pod_id }}& eatc-pod_name ={{eatc_dona_headers. eatc-pod_name }}& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-donation_manager_code ={{eatc_dona_headers. eatc-donation_manager_code }}& eatc-donation_manager_name ={{eatc_dona_headers. eatc-donation_manager_name }}& eatc-final_doma_code= ""& eatc-final_doma_name =""& eatc-dona_initial_state ={{eatc_dona_headers. eatc-state }}& eatc-verification_code =""& eatc-token =""& eatc-dona_final_state ={{eatc_dona_headers. eatc-state }}& eatc-issue_cause_code ={{se toma de a partir de la informacin del selector respectivo de la funcionalidad}}& eatc-issue_cause ={{se toma de a partir de la informacin del selector respectivo de la funcionalidad}}& eatc-log =app_extemporaneous_checkin& resolved =si 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 CHECK-IN EXPRESS: LLEGU AL PUNTO DE DONACIN