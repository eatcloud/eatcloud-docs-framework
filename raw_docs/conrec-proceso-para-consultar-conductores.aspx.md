# conrec-proceso-para-consultar-conductores.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 

 El presente servicio se especifica como respuesta a problemas de seguridad que se han detectado en la plataforma, en dnde redes organizadas de delincuentes, roban u obtienen de manera irregular accesos de fundaciones y programan recogidas con conductores y placas (identificadas) de manera fraudulenta, violando las polticas de la plataforma.  Por lo tanto se debe crear un servicio con pautas de seguridad, que permita a la aplicacin validar si un conductor puede ser registrado en la plataforma para realizar recogidas de donaciones, o si por el contrario est en lista negra, lo que desencadenar registros y acciones de seguridad y entregar una respuesta de fallo de validacin a la App lo cual suspender el proceso.  El servicio se deber implementar como una API Pblica, siguiendo los lineamientos de la primera implementacin al respecto.   Para ello se ha desarrollado una documentacin que establece el respectivo EndPoint, y los parmetros con los cuales se invoca el servicio y las respuestas que debe entregar 

 Documentacin de API pblica para consulta de recolectores 

 Para evitar duplicidad en la documentacin, la implementacin del servicio deber basarse en dicha documentacin (si se deben hacer cambios se debe intervenir dicha documentacin), y a continuacin se explica lo que el servicio debe realizar con la informacin recibida. 

 ESTRUCTURAS DE DATOS PARA VALIDACIN Y REGISTRO 

 En la presente documentacin se establecen tres estructuras de datos, cuya denominacin no es semntica y cuyos campos no son semnticos (para dificultar su lectura por parte de un tercero).   

 Lista negra de recolectores 
 En esta estructura de datos se recolectan placas de vehculos y documentos de identidad, que se han definido que pertenecen  a organizaciones fraudulentas o personas mal intencionadas y que no se debe permitir que operen la plataforma. 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_kms?_id=_* 

 Lista negra de dispositivos 
 En esta estructura de datos se registrarn dispositivos desde los cuales se intent programar una recoleccin con un individuo presente en la lista negra, con el nimo de poder tener informacin para sacar del sistema a dispositivos identificados que intenten desarrollar actividades fraudulentas en la plataforma. 

 {{URL_entorno_datagov}}/ api/eatcloud/eatc_ims?_id=_* 

 A continuacin se muestran los campos de la estructura de datos, con el nimo de configurar la respectiva clave primara del repositorio 

 cua_master : "Cuenta maestra" , 
 imei : "IMEI del dispositivo" , => CLAVE PRIMARIA 
 pa : "doc_id en lista negra que se intent registrar" , 
 pk : "Placa en lista negra que se intent registrar" , 
 dt : "timestamp" , 
 eatc_doma_user_email : "Correo electrnico del usuario de la App" , 
 eatc_doma_id : "Documento de identidad de la institucin beneficiaria" , 
 eatc_pod_id : "Identificador del punto de donacin" , 
 eatc_cua_origin : "Cuenta usuario del punto de donacin" , 
 eatc_dona_header_code : "Cdigo del anuncio de donacin" 

 Registro de recolectores 
 En esta estructura se registrarn los recolectores propuestos por los gestores de donacin y que pasan el proceso de validacin contra la lista negra.  Se implementa para tener ms informacin sobre estas personas que brindan servicios a la comunidad EatCloud 
 {{URL_entorno_datagov}}/ api/eatcloud/eatc_mv?_id=_*   

 A continuacin se muestran los campos de la estructura de datos, con el nimo de configurar la respectiva clave compuesta del repositorio 

 cua_master : "Cuenta maestra" , => CLAVE COMPUESTA 
 cua_user : "Cuenta usuario" , => CLAVE COMPUESTA 
 imei : "IMEI del dispositivo" , => CLAVE COMPUESTA 
 n0k : "nombre del recolector autorizado" , 
 pa : "Doc id autorizado" , => CLAVE COMPUESTA 
 pk : "Placa autorizada" , => CLAVE COMPUESTA 
 dt : "timestamp" , 
 uz : "Empresa de transporte" , 
 uzik : "Documento de identificacin Empresa de transporte" , => CLAVE COMPUESTA 
 nv : "Observaciones" , 
 eatc_doma_id : "Documento de identificacin de la organizacin beneficiaria que realiza la consulta" => CLAVE COMPUESTA 

 ***NUEVO: ktm: "telfono del recolector autorizado" *** 

 Notacin de campos para estas estructuras 
 En las tres anteriores estructuras se manejar la siguiente notacin para los diversos campos con informacin de los recolectores: 

 n0k: nombre del recolector  
 pa : documento de identidad del recolector 
 pk : placa del vehculo del recolector 
 dt : estampe de tiempo 
 uz : compaa de transporte a la cual se adscribe el recolector (para futuras  
 uzik : documento de identidad de la compaa de transporte 
 ktm : telfono del recolector 

 NOTA IMPORTANTE: Para la elaboracin de esta documentacin, en dichas estructuras se presentan datos sin encripcin, y se ejemplifican llamados a API bajo esa premisa; pero para la implementacin de la funcionalidad se debern encriptar todos los datos de dichas estructuras y realizar llamados con los servicios de consulta a datos encriptados respectivos. 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 

 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta: 
 retry 

 1. VALIDACIN DE DATOS COMPLETOS 

 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de . Parmetros del body de la peticin   de la especificacin de la API Pblica . Si lo son, seguir adelante con el prximo paso.  Si no lo son deber entregar una respuesta de error: 
 incomplete_data 

 2. VALIDACIN DEL DISPOSITIVO EN LISTA NEGRA DE DISPOSITIVOS 
 Con el dato que llega en el parmetro: 
 imei 

 El sistema deber consultar si existe un registro en la estructura de datos de lista negra de placas y conductores 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_ims?imei={{ imei }} 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 
 Ejemplo:https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_ims&fieldname=imei&fieldvalue=IMEI%20del%20dispositivo 

 Si la consulta arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail 

 ***NUEVO: suspensin de la organizacin *** 
 Adicional a esto, el sistema debe proceder con la suspensin de la organizacin a la cual est afiliado el usuario, tal como se detalla ms adelante. 

 Si la consulta no arroja respuesta el sistema sigue con la siguiente validacin: 

 3. VALIDACIN DE DOCUMENTO DE IDENTIDAD DEL RECOLECTOR 
 Con el dato que llega en el parmetro: 
 doc_id 

 El sistema deber consultar si existe un registro en la estructura de datos de lista negra de placas y conductores 

 {{URL_entorno_datagov}}/api/eatcloud/api/eatcloud/eatc_kms?pa={{ doc_id }} 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 

 Si la consulta arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail 

 Y deber realizar el respectivo registro en la estructura de Lista Negra de Dispositivos ( eatc_ims ), con los parmetros recibidos de la invocacin en la invocacin del servicio, de la siguiente manera: 

 {{ parmetros_invocacin_CRD }} 

 cua_master ={{ cua_master }}, 
 imei ={{ imei }}, 
 pa ={{ doc_id }}, 
 pk ={{ lic_plate }}, 
 dt =[ timestamp_realizacion_registro] , 
 eatc_doma_user_email ={{ eatc_doma_user_email }}, 
 eatc_doma_id ={{ eatc_doma_id }}, 
 eatc_pod_id ={{ eatc_pod_id }}, 
 eatc_cua_origin ={{ eatc_cua_origin }}, 
 eatc_dona_header_code ={{ eatc_dona_header_code }} 

 Llamado al CRD: 

 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_ims&_operacion=insert&{{ parmetros_invocacin_CRD }} 

 Una vez se realiza la operacin insert, se deber invocar al servicio de encripcin de datos para que los mismos reposen de manera segura en el respectivo repositorio. 

 ***NUEVO: suspensin de la organizacin *** 
 Adicional a esto, el sistema debe proceder con la suspensin de la organizacin a la cual est afiliado el usuario, tal como se detalla ms adelante. 

 Si la consulta no arroja respuesta el sistema sigue con la siguiente validacin: 

 4. Validacin de la placa del recolector 
 En caso de llegar un dato vlido en el campo  
 lic_plate 

 El sistema deber consultar si existe un registro en la estructura de datos de lista negra de placas y conductores 

 {{URL_entorno_datagov}}/api/eatcloud/api/eatcloud/eatc_kms?pk={{ lic_plate }} 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 

 Si la consulta arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail 

 Y deber realizar el respectivo registro en la estructura de Lista Negra de Dispositivos ( eatc_ims ), con los parmetros recibidos de la invocacin en la invocacin del servicio, de la siguiente manera: 

 {{ parmetros_invocacin_CRD }} 

 cua_master ={{ cua_master }}, 
 imei ={{ imei }}, 
 pa ={{ doc_id }}, 
 pk ={{ lic_plate }}, 
 dt =[ timestamp_realizacion_registro] , 
 eatc_doma_user_email ={{ eatc_doma_user_email }}, 
 eatc_doma_id ={{ eatc_doma_id }}, 
 eatc_pod_id ={{ eatc_pod_id }}, 
 eatc_cua_origin ={{ eatc_cua_origin }}, 
 eatc_dona_header_code ={{ eatc_dona_header_code }} 

 Llamado al CRD: 

 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_ims&_operacion=insert&{{ parmetros_invocacin_CRD }} 

 Una vez se realiza la operacin insert, se deber invocar al servicio de encripcin de datos para que los mismos reposen de manera segura en el respectivo repositorio. 

 ***NUEVO: suspensin de la organizacin *** 
 Adicional a esto, el sistema debe proceder con la suspensin de la organizacin a la cual est afiliado el usuario, tal como se detalla ms adelante. 

 Si la consulta no arroja respuesta el sistema sigue con la siguiente operacin: 

 5. CONSULTA EN EL REGISTRO DE RECOLECTORES 
 El sistema con los campos (que lleguen en el llamado al servicio) 
 cua_master, eatc_cua_origin , imei, doc_id, lic_plate, company_doc_id, eatc_doma_id 

 El sistema realiza la siguiente consulta: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_mv? cua_master ={{ cua_master }}& cua_user ={{ eatc_cua_origin }}& imei ={{ imei }}& pa ={{ doc_id }}& pk ={{ lic_plate }}& uzik ={{ company_doc_id }}& eatc_doma_id ={{ eatc_doma_id }}&_cmp= _id 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 

 Ejemplo encriptar datos: https://dev.datagov.eatcloud.info/crypt/eatcloud/encrypt?table=eatc_mv&fieldname=cua_master,imei,pa 

 Ejemplo1 consultar datos encriptados: 
 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_mv&fieldname=cua_master&fieldvalue=Cuenta%20maestra 

 Ejemplo 2 consultar datos encriptados:  
 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_mv&filterfield_1=cua_master&filtervalue_1=Cuenta%20maestra&filterfield_2=imei&filtervalue_2=IMEI%20del%20dispositivo 

 Ejemplo 3 consultar datos encriptados, retornando datos desencriptados: 
 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_mv&filterfield_1=cua_master&filtervalue_1=Cuenta%20maestra&filterfield_2=imei&filtervalue_2=IMEI%20del%20dispositivo&fielddecrypt=imei,pa 

 Si la consulta arroja un resultado, el servicio deber entregar como respuesta: 
 eatc_collector_id ={{ _id }} 

 Si la consulta no arroja respuesta el sistema deber realizar el siguiente proceso: 

 6. REGISTRO DEL RECOLECTOR 

 Con los parmetros con los cuales se invocaron el servicio, el registro del respectivo recolector como se indica a continuacin: 

 {{ parmetros_invocacin_CRD }} 

 cua_master ={{ cua_master }}, 
 cua_user ={{ eatc_cua_origin }}, 
 imei ={{ imei }}, 
 n0k ={{ name }, 
 pa ={{ doc_id }}, 
 pk ={{ lic_plate }}, 
 dt =[ timestamp_realizacion_registro] , 
 uz ={{ company }}, 
 uzik ={{ company_doc_id }}, 
 nv = registro_automatico , => CONSTANTE 
 eatc_doma_id ={{ eatc_doma_id }}, 

 ***NUEVO: ktm= {{ eatc_picker_phone }} *** 

 Llamado al CRD: 

 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_mv&_operacion=insert&{{ parmetros_invocacin_CRD }} 

 Una vez se realiza la operacin insert, se deber invocar al servicio de encripcin de datos para que los mismos reposen de manera segura en el respectivo repositorio. 

 De igual manera el servicio deber responder con el _id del registro recientemente creado: 
 eatc_collector_id ={{ _id }} 

 SUSPENCIN DE LA ORGANIZACIN 

 Cuando falle una validacin, bien sea por encontrar el dispositivo o los datos del recolector en listas negras, se deber proceder a realizar la suspensin de la institucin beneficiaria, de la siguiente manera: 

 Registro de la informacin del cambio de estado: 

 Actualizacin de datos del beneficiario en eatc_donation_managers 

 El sistema deber realizar la siguiente actualizacin de datos 

 {{ URL_entorno_beneficarios }}/crd/{{_DOM. cua_master }} / ?_tabla= eatc_donation_managers &_operacion= update & eatc_state= suspendido &fecha2= [timestamp_realizacion_registro] &causal_inactivo= programacion_irregular_c007 &WHERE identificador_unico_registro = {{ eatc_doma_id }} 

 Para este proceso los valores suspendido y programacion_irregular_c007 son constantes. 

 Creacin de registro en en eatc_doma_state_change_history 

 El sistema deber realizar la siguiente actualizacin de datos 

 {{ URL_entorno_datagov }}/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &_operacion= insert & eatc_code= {{ codigo_autogenerado_anticolisiones }} &eatc_date= {{ date_stamp }} &eatc_datetime= {{ datetime_stamp }} &eatc_cua_master={{ cua_master }}&eatc_doma_code = {{ eatc_doma_id }}&eatc_bo_user= eatcloud_tech &eatc_doma_prev_state= activo &eatc_doma_new_state= suspendido &eatc_cause_code= programacion_irregular_c007 &eatc_notes= {{ URL_registro_ims_con_llamado_servicio_desencripcion }} 

 llamado a servicio de desencripcin: 
 fielddecrypt=pa,pk,dt 

 Ejemplo: https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_ims&fieldname=imei&fieldvalue=123&fielddecrypt=pa,pk,dt   

 Para este proceso los valores eatcloud_tech , activo , suspendido y programacion_irregular_c007 son constantes. 

 ***NUEVO: Cuando se "suspende", a un beneficiario: liberacin de donaciones pendientes de gestin por parte del beneficiario. *** 

 El sistema deber consultar las donaciones que estn pendientes de gestin por parte del beneficiario suspendido, mediante la siguiente consulta. 

 {{ URL_entorno_donantes }}/api/{{ _DOM.cua_master }} / eatc_dona_headers & eatc-donation_manager_code= {{ eatc_donation_managers .identificador_unico_registro }}&eatc-state=awarded,scheduled&_cmp=eatc-code, eatc_cua_master,eatc-donor,eatc-state,eatc-pod_id 

 Con la consulta se obtiene un array de cdigos de anuncios de donacin.  Segn sea el caso (o estado al cual se cambia) se definen las siguientes constantes: 

 eatc_dona_release_cause: lbl_liberacion_por_suspension_automatica_beneficiario  

 Con los parmetros de la consulta y la constante definida, se realizan invocaciones al servicio de liberacin de donaciones , de acuerdo a la documentacin respectiva . 

 ***NUEVO: LIBERACIN DE ANUNCIOS DE LA ORGANIZACIN SUSPENDIDA *** 

 Cuando se suspenda a una organizacin, bien sea por encontrar el dispositivo o los datos del recolector en listas negras, o cuando falle la validacin asociada al proceso de CONREC, el sistema deber liberar los anuncios que dicha organizacin tenga pendientes por gestionar: 

 Consulta de informacin de anuncios pendientes por gestionar: 

 El sistema deber realizar la siguiente consulta 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }} / eatc_dona_headers? eatc-donation_manager_code = {{ eatc_doma_id }} &eatc-state= awarded,scheduled&_cmp=eatc_cua_master,eatc_cua_origin,eatc-code,eatc-state,eatc-pod_id 

 Con esta consulta el sistema obtiene un array de los anuncios que estn pendientes por gestin de la organizacin que ha sido suspendida 

 Invocacin del servicio "libdona": 
 El sistema deber realizar la invocacin al servicio de liberacin de anuncios, de la siguiente manera: 

 {{ parmetros_invocacin_libdona }} 

 cua_master ={{ eatc_dona_headers. eatc_cua_master }}, 
 cua_user ={{ eatc_dona_headers. eatc_cua_origin }}, 
 eatc_dona_header_code ={{ eatc_dona_headers. eatc-code }}, 
 eatc_dona_state ={{ eatc_dona_headers. eatc-state }}, 
 eatc_dona_release_cause = lbl_beneficiario_sin_requisitos , (CONSTANTE PARA ESTA INVOCACIN) 
 eatc-pod_id ={{ eatc_dona_headers. eatc-pod_id }}, 

 ***NUEVO: BORRADO DE REGISTRO DE PROGRAMACIN DIRECTA A ORGANIZACIN SUSPENDIDA *** 
 Cuando se suspenda a una organizacin, bien sea por encontrar el dispositivo o los datos del recolector en listas negras, o cuando falle la validacin asociada al proceso de CONREC, el sistema deber borrar los registros de programacin directa que estn asociados a la organizacin suspendida. 
 Borrado de registros de programacin directa: 
 El sistema deber realizar la siguiente operacin de borrado de registros de asignacin directa: 
 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla=eatc_direct_dona&_operacion=delete&WHERE eatc-donation_manager_code = {{ eatc_doma_id }} 

 ***NUEVO: ENVO DE CORREO A LA MESA DE SERVICIO *** 
 Cuando se suspenda a una organizacin, bien sea por encontrar el dispositivo o los datos del recolector en listas negras, o cuando falle la validacin asociada al proceso de CONREC, el sistema deber enviar un correo a la mesa de servicio ( soporte@eatcloud.com ) con la siguiente informacin: 

 From: noreply@eatcloud.com 
 to: soporte@eatcloud.com   
 Asunto: Nueva organizacin suspendida automticamente 
 Cuerpo: 
 Se ha suspendido automticamente por programacin irregular a la organizacin con identificador nico de registro cua_master }}/eatc_donation_managers?identificador_unico_registro= {{ eatc_doma_id }}> {{ eatc_doma_id }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONREC: SERVICIO PARA CONSULTAR RECOLECTORES DE DONACIONES