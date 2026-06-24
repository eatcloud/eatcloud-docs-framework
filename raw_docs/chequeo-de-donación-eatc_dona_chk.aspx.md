# chequeo-de-donación-eatc_dona_chk.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Esta funcionalidad propende por una revisin lo ms gil posible de la mercanca que se est recogiendo, procurando cumplir con el estndar de revisin establecido ( https://drive.google.com/drive/folders/1zfJZoOiKbpfF8sxZa3qLSwNaKWQpT1YA : De 0 a 10 PLU o SKU se debe revisar el 90%;11 o ms el 60%) 

 Definicin de los productos a chequear (PLUs para el caso del piloto) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 El sistema debe leer el anuncio de donacin (eatc_dona) y establecer las referencias que se deben chequear.  Si se donan de 1 a 10 referencias (o PLUs para el caso del piloto), el sistema debe sugerir un listado aleatorio del 90% de dichas referencias ( eatc-odd_id ) para que el usuario las chequee.  Si de donan 11 o ms, el sistema debe arrojar un listado del 60% de las referencias o PLUs ( eatc-odd_id ) para que el usuario las chequee. 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona? eatc-dona_header_code = 40716  

 Ejemplo _DOM. cua_master=abaco: 
 El para el anuncio cuyo " eatc-code " = 40716 ( anuncio cuyo " eatc-id " = 7608059 ) (Carulla Palmas: user : 339; password : (4) 6050294) 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716   
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716&_compress   

 El sistema determina que hay 16 eatc-odd_id diferentes en el anuncio, por lo tanto debe sugerir el 60% de los mismos para ser chequeados (16*0,6=9,6, redondeando: 10 eatc-odd_id) 

 Encabezado del listado de eatc-odd_id 
 El listado de eatc-odd_id debe tener el siguiente encabezado.  Por favor determine de las siguientes referencias de productos, cuales han sido entregadas adecuadamente y cuales faltan o no son aptas para el consumo humano. 

 Formulario de chequeo gil (OJO que difiere el diseo preliminar) 
 El sistema arroja un listado que debe aleatorio de eatc-odd_id , mostrando para cada uno de ellos su nombre ( eatc-odd_name ) y su cdigo ( eatc-odd_id ).  Al frente de cada referencia debe haber dos botones: 

 Chequeo exitoso 
 Al oprimir esta opcin el sistema da por exitoso el chequeo y no realiza ninguna opcin adicional. 

 Chequeo no exitoso 
 Si el usuario presiona esta opcin, el sistema debe proveer herramientas de captura de informacin para registrar el motivo del chequeo no exitoso ( eatc-odd_rejection_cause) . 

 Registro de causales o motivo de chequeo no exitoso ***NUEVO: cambio en el maestro de resultados del chequeo *** 
 Con el nimo de conectar los procesos de chequeo y verificacin de anuncios , se establecieron nuevos causales o resultados de chequeo no exitoso.  La idea es que la informacin que se recolecte en el chequeo permita establecer si hay un rechazo parcial o un rechazo total del producto y a partir de estos datos crear acciones y validaciones en el proceso de verificacin , con el nimo de coordinar ambos procesos. 

 ***NUEVO: consulta de los causales (resultados de chequeo no exitoso)*** 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_odds_chk_negative_result?_id=_*&_cmp=code,eatc_label,eatc_desc_label   
 (Anteriormente: https://datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=_* ) 

 El sistema toma los datos consignados en el campo "eatc_odds_chk_negative_result. eatc_label "   y  "eatc_odds_chk_negative_result. eatc_desc_label " para construir el selector nico (con descripcin) y de acuerdo a la opcin seleccionada se toman los datos "eatc_odds_chk_negative_result. eatc_label "   y  " eatc_odds_chk_negative_result. code " para llevarlos al registro del resultado del chequeo: 

 Escritura en eatc_odd_rejection_registry ***NUEVO: registro segn datos de nuevo maestro *** 
 Con los datos del  encabezado del anuncio de donacin y del detalle respectivo (tal como se viene haciendo en el actual proceso de chequeo) y con los datos del nuevo resultado negativo del chequeo, se realiza la siguiente escritura (en verde lo que debe funcionar tal cual est en el momento y en rojo lo que se debe ajustar) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_odd_rejection_registry&_operacion=insert&date_time={{ DATETIME}}& eatc-donation_manager_code={{VALOR}}&eatc-donation_manager_user_doc_id={{VALOR}}&eatc_donor_code={{VALOR}}&eatc-dona_header_code={{VALOR}}&eatc-pod_id={{VALOR}}&eatc-odd_id={{VALOR}}&verification_type= chk &eatc-odd_rejection_cause={{ eatc_odds_chk_negative_result. eatc_label }}&eatc-odd_rejection_cause_id={{ eatc_odds_chk_negative_result. code }} &evidence={{url_recurso}} 

 Ejemplo 1, _DOM. cua_master,ambiente de pruebas : 

 Para el hipottico anuncio de donacin cuyo eatc-code = 40716 , El usuario El usuario Juan Carlos Buitrago (numero_cedula = 8161174 ; que tiene como organizacin el dato: 900326456-1 https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 ) realiza un chequeo a las 16:00:00 del da 2019-09-26 definiendo mediante los formularios de captura de la App, que el artculo "AHUYAMA PORCIO TRANSF" ( eatc-odd_id : "1005125") es parcialmente rechazado 

 Dado que se tienen los siguientes datos: 

 date_time: 2019-09-26 16:00:00  
 eatc-donation_manager_code= 900326456-1 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_user_doc_id= 8161174 (que corresponde a numero_cedula ) 
 eatc_donor_code= 890.900.608-9 (que corresponde a eatc_dona. eatc_donor_code) 
 eatc-dona_header_code= 40716 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-pod_id= 339 (que corresponde a eatc_dona. eatc-pod_id) 
 eatc-odd_id= 1005125 (que corresponde a eatc_dona. eatc-odd_id) 
 verification_type= chk (que corresponde a chequeo. Sera una constante en todo registro de esta funcionalidad ) 
 eatc-odd_rejection_cause= lbl_rechazo_parcial 
 eatc-odd_rejection_cause_id= rechazo_parcial 
 quantity= NA 
 evidence = corresponde a la URL del recurso (fotografa) de evidencia que se guarda en el servidor 

 Utilizando el API se realiza el siguiente registro: 

 https://devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_odd_rejection_registry&_operacion=insert&date_time= 2019-09-26%2016:00:00& eatc-donation_manager_code= 900326456-1 &eatc-donation_manager_user_doc_id= 8161174 &eatc_donor_code= 890.900.608-9 &eatc-dona_header_code= 40716 &eatc-pod_id= 339 &eatc-odd_id= 1005125 &verification_type= chk & eatc-odd_rejection_cause= lbl_rechazo_parcial& eatc-odd_rejection_cause_id= rechazo_parcial &quantity=NA&evidence=url      

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 last : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 El registro se puede consultar aqu: https://devdonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? eatc-dona_header_code =40716& eatc-odd_id= 1005125   

 Actualizacin en eatc_dona ***NUEVO: al registro se lleva el eatc-odd_rejection_cause_id anteriormente recolectado *** 

 Dado el anterior registro, se determina el _id del registro de detalle de anuncio de donacin (eatc_dona): 

 Dado que se tienen los siguientes datos: 
 eatc-dona_header_code= 40716 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-odd_id= 1005125 (que corresponde a eatc_dona. eatc-odd_id) 

 Se puede determinar el _id: "1195" con la siguiente consulta al API: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code =40716& eatc-odd_id= 1005125   

 Con este dato se lleva la relacin del anterior registro (URL JSON) al campo " odd_rejection_cause "  
 odd_rejection_cause= https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2   
 eatc-odd_state= rechazo_parcial 

 Actualizacin con la API 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona&_operacion=update& eatc-odd_rejection_cause ={{URL}}& eatc-odd_state= rechazo_parcial & WHERE_id ={{VALOR}} 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo : 

 Como el registro completo de las causas de rechazo se puede consultar aqu: https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2   

 Utilizando el API se realiza la siguiente actualizacin: 

 https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona&_operacion=update&eatc-odd_rejection_cause= https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2 & eatc-odd_state= rechazo_parcial &WHERE_id= 1195      

 Nota importante: Si se envan los parmetros por mtodo GET (URL), no se puede enviar una URL que contenga "&" dado que el sistema la toma como otro atributo a actualizar.  Por eso se debe mandar como parmetro (en este caso " eatc-odd_rejection_cause ") una URL, no se debe mandar una que contenga &.  Utilizando el mtodo POST (con el tester por ejemplo), si se podra enviar una URL con "&" 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 El registro se puede consultar aqu: https://donantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=40716&eatc-odd_id=1005125    

 DEPRECADO: Registro de causales o motivo de chequeo no exitoso ***NUEVO: internacionalizacin*** 

 El sistema debe consultar las causales disponibles para despus, segn el idioma de la App, mostrar el dato internacionalizado en el selector: 

 (***NUEVO***) consulta de los causales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 

 https://datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=_* 
 (Anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_odd_rejection_cause&code=_todos ) 

 El sistema toma los datos consignados en el campo " eatc_odd_rejection_causes. eatc_label " para construir el selector internacionalizado y de acuerdo a la opcin seleccionada se toman los datos " eatc_odd_rejection_causes. nombre " y " eatc_odd_rejection_causes. code " para llevarlos al registro del causal de rechazo: 

 Escritura en eatc_odd_rejection_registry con la API ***REVISAR dinamismo a partir de _DOM.cua_master y nuevo dato: odd_rejection_cause_id*** 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_odd_rejection_registry&_operacion=insert&date_time={{ DATETIME}}& eatc-donation_manager_code={{VALOR}}&eatc-donation_manager_user_doc_id={{VALOR}}&eatc_donor_code={{VALOR}}&eatc-dona_header_code={{VALOR}}&eatc-pod_id={{VALOR}}&eatc-odd_id={{VALOR}}&verification_type= chk &eatc-odd_rejection_cause={{ eatc_odd_rejection_causes. nombre }}&eatc-odd_rejection_cause_id={{ eatc_odd_rejection_causes. code }}&quantity={{VALOR}}&evidence={{VALOR}} 

 Ejemplo, _DOM. cua_master,ambiente de pruebas : 

 Para el hipottico anuncio de donacin cuyo eatc-code = 40716 , El usuario El usuario Juan Carlos Buitrago (numero_cedula = 8161174 ; que tiene como organizacin el dato: 900326456-1 https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 ) realiza un chequeo a las 16:00:00 del da 2019-09-26 definiendo mediante los formularios de captura de la App, que el artculo "AHUYAMA PORCIO TRANSF" ( eatc-odd_id : "1005125") no es apto para el consumo humano (el sistema le permite tomar una fotografa como evidencia y guarda la URL con la cual se puede obtener el recurso en el repositorio del sistema). 

 Dado que se tienen los siguientes datos: 
 date_time: 2019-09-26 16:00:00  
 eatc-donation_manager_code= 900326456-1 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_user_doc_id= 8161174 (que corresponde a numero_cedula ) 
 eatc_donor_code= 890.900.608-9 (que corresponde a eatc_dona. eatc_donor_code) 
 eatc-dona_header_code= 40716 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-pod_id= 339 (que corresponde a eatc_dona. eatc-pod_id) 
 eatc-odd_id= 1005125 (que corresponde a eatc_dona. eatc-odd_id) 
 verification_type= chk (que corresponde a chequeo. Sera una constante en todo registro de esta funcionalidad ) 

 eatc-odd_rejection_cause= No apta para el consumo humano (que corresponde a https://datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?code=2 ) 
 anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_odd_rejection_cause&code=2 ) 
 eatc-odd_rejection_cause_id=2 (que corresponde a: https://datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?code=2 ) 
 quantity = NA (no aplica porque cuando se chequea no se pueden contar cantidades. Sera una constante en todo registro de esta funcionalidad) 
 evidence = corresponde a la URL del recurso (fotografa) de evidencia que se guarda en el servidor 

 Utilizando el API se realiza el siguiente registro: 

 https://devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_odd_rejection_registry&_operacion=insert&date_time= 2019-09-26%2016:00:00& eatc-donation_manager_code= 900326456-1 &eatc-donation_manager_user_doc_id= 8161174 &eatc_donor_code= 890.900.608-9 &eatc-dona_header_code= 40716 &eatc-pod_id= 339 &eatc-odd_id= 1005125 &verification_type= chk &eatc-odd_rejection_cause= No%20apta%20para%20el%20consumo%20humano& eatc-odd_rejection_cause_id=2 &quantity=NA&evidence=url     

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 last : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 El registro se puede consultar aqu: https://devdonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? eatc-dona_header_code =40716& eatc-odd_id= 1005125   

 Actualizacin en eatc_dona con la API ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Dado el anterior registro, se determina el _id del registro de detalle de anuncio de donacin (eatc_dona): 

 Dado que se tienen los siguientes datos: 
 eatc-dona_header_code= 40716 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-odd_id= 1005125 (que corresponde a eatc_dona. eatc-odd_id) 

 Se puede determinar el _id: "1195" con la siguiente consulta al API: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code =40716& eatc-odd_id= 1005125   

 Con este dato se lleva la relacin del anterior registro (URL JSON) al campo " odd_rejection_cause "  
 odd_rejection_cause = https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2   
 eatc-odd_state= rechazado 

 Actualizacin con la API 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona&_operacion=update& eatc-odd_rejection_cause ={{URL}}& eatc-odd_state= rechazado& WHERE_id ={{VALOR}} 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo : 

 Como el registro completo de las causas de rechazo se puede consultar aqu: https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2   

 Utilizando el API se realiza la siguiente actualizacin: 

 https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona&_operacion=update&eatc-odd_rejection_cause= https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =2 & eatc-odd_state= rechazado &WHERE_id= 1195       

 Nota importante: Si se envan los parmetros por mtodo GET (URL), no se puede enviar una URL que contenga "&" dado que el sistema la toma como otro atributo a actualizar.  Por eso se debe mandar como parmetro (en este caso " eatc-odd_rejection_cause ") una URL, no se debe mandar una que contenga &.  Utilizando el mtodo POST (con el tester por ejemplo), si se podra enviar una URL con "&" 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 El registro se puede consultar aqu: https://donantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=40716&eatc-odd_id=1005125    

 Finalizacin del chequeo (en ambos casos: exitoso y no exitoso) 
 El sistema debe guardar la fecha y hora en la que se termina el chequeo en los datos de encabezado de anuncio de donacin. 

 Actualizacin en eatc_dona_headers con la API ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Dado que se tienen los siguientes datos: 
 eatc-dona_header_code= 40716 (que corresponde a eatc_dona_headers. eatc-code) 

 Se debe registrar la fecha y hora del registro del chequeo ( eatc-check_datetime ) 

 Actualizacin con la API 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update& eatc-check_datetime={{ Fecha y hora en la que se termina el chequeo}}& WHERE eatc-code ={{VALOR}} 

 Ejemplo _DOM. cua_master=abaco, ambiente productivo : 

 Se termin de realizar el chequeo de la mercanca a las 2019-09-24 13:00:00 

 Utilizando el API se realiza la siguiente actualizacin: 

 https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&_operacion=update& eatc-check_datetime= 2019-09-24%2013:00:00& WHERE eatc-code = 40716 (Solo funcionar cuando esta tarea quede completada: https://app.asana.com/0/1124372722088662/1146115664949793 ) 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
 El registro se puede consultar aqu: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40716    

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fchequeo-de-donaci%C3%B3n-eatc_dona_chk%2F1752939627-15-chequear-recogida--eatc_dona_chk-.png&ow=750&oh=1936, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fchequeo-de-donaci%C3%B3n-eatc_dona_chk%2F1752939627-15-chequear-recogida--eatc_dona_chk-.png&ow=750&oh=1936 
 EatCloud Beneficiarios 

 554.000000000000 

 CHEQUEO DE DONACIN (EATC_DONA_CHK)