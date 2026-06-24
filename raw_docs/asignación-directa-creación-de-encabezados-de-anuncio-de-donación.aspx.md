# asignación-directa-creación-de-encabezados-de-anuncio-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** proceso dinámico que opera sobre múltiples cuentas maestras 
 El proceso de creación de encabezados de donación debe correr para todas las cuentas maestras registradas en el respectivo maestro: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 

 Este ajuste aplica tanto para los procesos de creación de encabezados activados por tareas programadas como los que son activados mediante servicios web. 

 Dado un anuncio de donación ( eatc_dona )  
 {{URL_entorno_donantes}}/api/{{eatc_cua. eatc_cua_master }}/eatc_dona?eatc-dona_header_code={{eatc-dona_header_code}} 

 la plataforma debe crear un encabezado en donde se deberán realizar algunas operaciones de totalización de información, y se adicionará información para facilitar las búsquedas en la plataforma.  Esta información se consolida en eatc_dona_headers 
 _DOM.base + "headersApp/" + _DOM.cua_master + _DOM.cua_user + code, 

 _crear_dona_headers.php 

 Proceso que opera en días hábiles (inicialmente para _DOM.cua_master = abaco) 
 Inicialmente a nivel de cronjob se debe programar para que solo opere en días hábiles (después de la generación de encabezados que corre a primera hora de la mañana. Se habló con el Banco de Cali y estuvieron de acuerdo a que el proceso corra una sola vez en el día, para no tener que programar cronjobs periódicos que capturen anuncios manuales.  Los que se generen en un día quedarán a primera hora del día siguiente asignados al Banco en cuestión.).  En fines de semana y días festivos (se sabe que el tema de festivos puede tener su complejidad), se correrá otro proceso que generará los encabezados de manera tradicional, y deberá disparar un proceso de match de manera tradicional, para que dichos anuncios (en fines de semana y festivos) estén disponibles para todo el ecosistema y no solamente para quienes tienen asignación directa. 

 NOTA PARA POSIBLE MEJORAMIENTO FUTURO: Se deberá evaluar si hay alguna manera de incorporar las condiciones de temporalidad en una persistencia para poderlas hacer dinámicas.  En una primera instancia se establecen como condiciones estáticas que se programan a través de cronjobs. 
 Opera sobre encabezados de anuncios ya creados (eatc-state: "announced")  dato válido (y) en "eatc_with_last_p_day" 
 El sistema deberá realizar la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?_id=_*&_distinct=eatc-pod_id 

 Si se requieren procesos diferentes por cuentas maestras, la consulta sería: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc_cua_master={{_DOM. cua_master }}&_distinct= eatc-pod_id 

 Para establecer un array de códigos  de puntos de donación {{array_codigos}} , sobre los cuales este proceso especial de generación de encabezados operará . 
 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/ eatc_dona_headers ?eatc-pod_id={{ array_codigos }}&eatc-state= announced &eatc_with_last_p_day= y 

 Opera sobre anuncios cuyos puntos de donación poseen asignación directa ***NUEVO : asignación directa por punto y NIT (eatc_donor_code) *** 
Se solicitó una mejora, para establecer asignación directa por la dupla del código del punto de donación y el “NIT” (eatc_donor_code) de la donación. 
En ese orden de ideas se establece lo siguiente: 
En la tabla eatc_direct_dona se crea el campo eatc_donor_code 
Este campo deberá ser parte de la clave compuesta de la tabla y se deberá indexar la tabla por el mismo para facilitar encontrar información. 
En la tabla eatc_direct_dona podrán haber registros que incorporen este nuevo dato 
Cuando esto ocurre, solamente se generarán los encabezados de asignación directa, a las donaciones en donde coincidan eatc_dona.eatc-pod_id y eatc_dona.eatc_donor_code con los registros de la tabla eatc_direct_dona (eatc-pod_id y el nuevo eatc_donor_code, respectivamente). 
Si no hay correspondencia, entonces la donación no se le generará asignación / programación directa. 
En ese orden del ideas, si para una cuenta se requieren varias asignaciones directas por la dupla, se deberán crear los registros correspondientes en la tabla.  
Si hay un registro particular, las donaciones que no cumplan con ese registro particular, no generarán asignación / programación directa, por lo tanto si se requieren que otras donaciones se asignen de manera directa, se deberán crear los registros particulares respectivos. 
Lo anterior también implica que no podrá existir un registro que no contenga dato particular para un pod y otro que si lo contenga (son caminos excluyentes en la lógica establecida, por lo tanto se deberá revisar para que la base de datos no permita que para un mismo punto de donación, exista un registro con eatc_donor_code vacío, y a la vez uno o varios con eatc_donor_code con datos (si se podrán tener varios registros con eatc_donor_code con datos pero sin el vacío). 
Lógica para la creación de la nueva asignación directa 
Se propone la siguiente lógica para la generación de la asignación directa (se deberá revisar para abarcar los diferentes casos y no dejar donaciones o casos por fuera: 

 DEPRECADO : 

 El sistema deberá realizar la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?_id=_*&_distinct=eatc-pod_id 

 Si se requieren procesos diferentes por cuentas maestras, la consulta sería: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc_cua_master={{_DOM. cua_master }}&_distinct= eatc-pod_id 

 Para establecer un array de códigos  de puntos de donación {{array_codigos}} , sobre los cuales este proceso especial de generación de encabezados operará. Esto aplica también para anuncios cuyo origen es a través de la Nueva WAPP (anuncios manuales) que se crean a través del servicio de creación de encabezados. _crear_dona_headers.php . 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/ eatc_dona ?eatc-pod_id={{ array_codigos }} 

 PROCESO SIMILAR AL DE CREACIÓN TRADICIONAL PERO CON ALGUNAS DIFERENCIAS 
 El proceso de generación de encabezados será muy similar al proceso tradicional (se puede reciclar mucho código para su construcción), pero con las siguientes adiciones de información (información que no se genera en el proceso tradicional y que para el caso particular será información de programación del anuncio) o variaciones de información (en específico se varía la información que se lleva al campo eatc_dona_headers. eatc-state dado que el anuncio se creará en estado diferente a "announced"). 

 Querys 
 En adelante se establece un query ilustrativo por cada campo del encabezado que se obtiene o se registra de manera diferente al proceso tradicional, sabiendo que en una sola consulta se podrán obtener muchos de los datos que se establecen abajo. 

  eatc-state 
 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-state = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-state 

 Ejemplo 1: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 55 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=55&_distinct= eatc-state   

 Por lo tanto se lleva al registro del encabezado: 
 eatc-state : "scheduled" 

 ***NUEVO: Ejemplo 2: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 39 *** 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=39&_distinct= eatc-state    

 Por lo tanto se lleva al registro del encabezado: 
 eatc-state : "awarded" 

 eatc-donation_manager_user_doc_id 

 El dato se obtiene para cada anuncio de la siguiente consulta: 

 eatc_dona_headers. eatc-donation_manager_user_doc_id = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_user_doc_id 

 eatc-donation_manager_code 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_code = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_code 

 eatc-donation_manager_name 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_name = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_name 

 eatc-donation_manager_address 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_address = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_address 

 eatc-donation_manager_phone 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_phone = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_phone 

 eatc-donation_manager_typology_a 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_typology_a = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_typology_a 

 eatc-donation_manager_typology_b 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_typology_b = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_typology_b 

 eatc-donation_manager_typology_c 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_typology_c = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_typology_c 

 eatc-donation_manager_typology_c 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-donation_manager_typology_c = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-donation_manager_typology_c 

 eatc-picker_name 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-picker_name = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-picker_name 

 Ejemplo 1: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 55 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=55&_distinct= eatc-picker_name   

 Por lo tanto se lleva al registro del encabezado: 
 eatc-picker_name : "NESTOR GASPAR" 

 ***NUEVO: Ejemplo 2: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 39 *** 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=39&_distinct= eatc-picker_name   

 Como la consulta no arroja resultados se debe dejar el registro correspondiente vacío: 
 eatc-picker_name : "" 

 eatc-picker_doc_id 
 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-picker_doc_id = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-picker_doc_id 

 Ejemplo 1: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 55 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=55&_distinct= eatc-picker_doc_id   

 Por lo tanto se lleva al registro del encabezado: 
 eatc-picker_doc_id : "16943399" 

 ***NUEVO: Ejemplo 2: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 39 *** 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=39&_distinct= eatc-picker_doc_id   

 Como la consulta no arroja resultados se debe dejar el registro correspondiente vacío: 
 eatc-picker_doc_id : "" 

 eatc-picker_license_plate 

 El dato se obtiene para cada anuncio de la siguiente consulta: 
 eatc_dona_headers. eatc-picker_license_plate = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-picker_license_plate 

 Ejemplo 1: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 55 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=55&_distinct= eatc-picker_license_plate   

 Por lo tanto se lleva al registro del encabezado: 
 eatc-picker_license_plate : "BTM000" 

 ***NUEVO: Ejemplo 2: ambiente de pruebas, donación cuyo eatc_dona.eatc-pod_id= 39 *** 

 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_direct_dona ?eatc-pod_id=39&_distinct= eatc-picker_license_plate   

 Como la consulta no arroja resultados se debe dejar el registro correspondiente vacío: 
 eatc-picker_license_plate : "" 

 eatc-verification_code 

 El código de verificación se construirá concatenando (sin espacios, guiones ni puntos) el  número de la cédula y la placa de vehículo del recolector asignado a cada punto: 

 eatc_dona_headers. eatc-verification_code = concat( { { URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-picker_doc_id , {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-picker_license_plate ) 

 ***NUEVO: si no hay datos de programación el código se genera como se hace en un anuncio tradicional*** 

 Si en la persistencia eatc_direct_dona, no hay datos de programación ( eatc-picker_doc_id, eatc-picker_license_plate ) entonces el código de verificación se tiene que generar tal como se genera para las donaciones tradicionales (código de 6 dígitos aleatorios) 

 Funciones 

 eatc-adjudication_datetime 

 Será igual a la fecha y hora en la cual se realiza el proceso: 
 eatc_dona_headers. eatc-adjudication_datetime = {{ timestamp en formato AAAA-MM-DD HH:MM:SS }} 

 eatc- scheduling _datetime ***NUEVO : manejo diferencial según estado registrado en la persistencia eatc_direct_dona *** 
 eatc_direct_dona. eatc-state : "scheduled" 

 Será igual a la fecha y hora en la cual se realiza el proceso: 
 eatc_dona_headers. eatc- scheduling _ datetime = {{ timestamp en formato AAAA-MM-DD HH:MM:SS }} 

 eatc_direct_dona. eatc-state : "awarded" 

 Se dejará la fecha vacía (0000-00-00 00:00:00) 

 eatc-programed_picking_datetime ***NUEVO : manejo diferencial según estado registrado en la persistencia eatc_direct_dona *** 
 eatc_direct_dona. eatc-state : "scheduled" 

 Con el dato se obtiene para cada anuncio de la siguiente consulta: 
 {{ hora_recogida_programada }} = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_direct_dona ?eatc-pod_id={{eatc_dona. eatc-pod_id }}&_distinct= eatc-programed_picking_time 

 ***Nuevo : funcionamiento diferenciado para el día domingo *** 
 Para todos los días diferentes al día domingo (debe funcionar como venía funcionando antes). 

 Se concatena la la hora obtenida en la anterior consulta, con la fecha actual para obtener un dato en formato: AAAA-MM-DD HH:MM:SS 
 eatc_dona_headers. eatc-programed_picking_datetime = {{ datestamp en formato AAAA-MM-DD }} {{ hora_recogida_programada }} 

 Para el día domingo (nuevo funcionamiento, adicionando un día para que la programación quede para el siguiente día ). 

 Se concatena la la hora obtenida en la anterior consulta, con la fecha actual más un día para obtener un dato en formato: AAAA-MM-DD HH:MM:SS 
 eatc_dona_headers. eatc-programed_picking_datetime = {{ datestamp en formato AAAA-MM-DD + 1 }} {{ hora_recogida_programada }} 

 Para donaciones que se realizan a través del servicio (que se invoca para donaciones manuales), el sistema deberá evaluar el dato eatc_direct_dona. eatc-programed_picking_time .  Si la hora informada es anterior a la hora actual, entonces el día ({{ datestamp en formato AAAA-MM-DD }}) será igual al día actual.  Si es posterior entonces el estampe de la fecha será la del día posterior (para que quede programada para el próximo día). 

 eatc_direct_dona. eatc-state : "awarded" 

 Se dejará la fecha vacía (0000-00-00 00:00:00) 

 Constantes ***NUEVO CAMPO A AGREGAR A eatc_dona_headers**** 

 eatc_not_interested_btn (boleano) 

 Cuando se crea un anuncio con este proceso se debe ingresar un campo boleano afirmativo, para este nuevo campo (que deberá crearse en eatc_dona_headers con las diferentes precauciones y ajustes en otros procesos para que el sistema siga funcionando de manera adecuada) 
 eatc_dona_headers. eatc_not_interested_btn = y 

 EatCloud 

 Dada la nueva información que se genera con este proceso especial, los datos que quedarían vacíos en el anuncio de donación serán los siguientes: 

 eatc-picker_start_datetime = // Fecha y hora en que se activa la funcionalidad de "recoger anuncio de donación" 
 eatc-picker_lat = // Latitud de quien recoge 
 eatc-picker_lon = // Longitud de quien recoge 
 eatc-picking_checkin_datetime = //Fecha y hora real del ingreso a la recogida del anuncio de donación 
 eatc-check_datetime = //Fecha y hora cuando se termina el chequeo de la donación en el punto de donación 
 eatc-picking_checkout_datetime = //Fecha y hora real de la salida de la recogida del anuncio de donación 
 eatc-receipt_datetime = //Fecha y hora de la recepción del anuncio de donación en las instalaciones del gestor de las donaciones 
 eatc-pre_certification_datetime = //Fecha y hora de la certificación preliminar del anuncio de donación 
 eatc-certification_datetime = //Fecha y hora de la certificación del anuncio de donación 
 eatc_doc_datetime = //Fecha y hora de subida de documentos al sistema 
 eatc_doc_url = //URL de los documentos guardados 
 eatc_rec_doc_signature_datetime = //Fecha y hora de la verificación de la firma del documento soporte 
 eatc_rec_odds_pre_verification_datetime = //Fecha y hora de la pre-verificación de los artículos 

 ***NUEVO: escritura en el historial de cambio de estados de la donación *** 
 Se deberá dejar traza de auditoría en el historial de estados de cuando una donación ha sido asignada o programada de manera directa, para ello se deberá realizar la siguiente escritura en la respectiva tabla 

 Escritura en el historial de estados de la donación ante una asignación / programación directa. 
 {{ parámetros_insert_CRD }} 

 eatc_dona_header_code={{eatc_dona_header_code}} ***de la donación que fue asignada o programada*** 

 eatc-state = {{eatc-state}}  ***Debe corresponder al dato que se obtiene en  {{eatc_dona_headers. eatc-state }} después del proceso (awarded: asignación.  Scheduled: programación)*** 

 eatc-date_time ={{timestamp}}***Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 

 eatc-log =EatCloud asignó / programó directamente esta donación según los datos extraídos {{url_datagov}}/api/eatcloud/eatc_direct_dona?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= {{_DOM. cua_user }} &eatc-pod_id={{eatc-pod_id}} 

 eatc_doma_id= {{ eatc_doma_id }} ***Se coloca el identificador_unico_registro del beneficiario al que se le asignó o programó la donación*** 

 Inserción en eatc_dona_header_state_history con el CRD 
 {{URL_entorno_donantes}}/crd/{{ cua_master }}/?_tabla= eatc_dona_header_state_history &_operacion= insert & {{ parámetros_insert_CRD }} 

 ***NUEVO: LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN (ASIGNACIÓN DIRECTA)*** 

 Nota importante: este llamado debe funcionar cuando las donaciones quedan en estado tanto para las donaciones que quedan con estado "AWARDED" o "SCHEDULED". 

 Endpoint (según documentación : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmAdjudicarDonacion 

 Parámetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio 

 ***NUEVO: LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN (PROGRAMACIÓN DIRECTA)*** 

 Nota importante: este llamado debe funcionar cuando las donaciones quedan en estado tanto para las donaciones que quedan con estado "SCHEDULED" 

 Endpoint (según documentación : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmAgendarDonacion 

 Parámetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=4a5d468a13a040dfa7d1b7912eb17e41&ext=png&ow=2462&oh=1172, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=4a5d468a13a040dfa7d1b7912eb17e41&ext=png&ow=2462&oh=1172 

 972.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"Off"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 5f2d628c-1e2c-49a3-aef5-4b015f45369c 
 1!1!2 
 https://eastus1-1.pushfp.svc.ms/fluid 
 2c99c2af-935c-401d-89f1-049b4c23099d 
 2025-04-09T22:32:41.7177691Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"16d31c0b-433e-416e-b620-ebfced935d86","SequenceId":1065,"FluidContainerCustomId":"09590a52-44bd-444d-9022-628829f092e9","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 DONACIONES CON ASIGNACIÓN DIRECTA: CREACIÓN DE ENCABEZADOS DE ANUNCIO DE DONACIÓN