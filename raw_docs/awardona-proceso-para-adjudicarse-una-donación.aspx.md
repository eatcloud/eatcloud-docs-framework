# awardona-proceso-para-adjudicarse-una-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 AWARDONA: PROCESO PARA ADJUDICARSE UNA DONACIÓN ","showTimeToRead":false,"encodedImage":"BBR:HGxufQ~qj[fQ"},"containsDynamicDataSource":false}">

 Se implementará un servicio que tenga la siguiente estructura: 
 {{URL_entorno_beneficiarios}} /awardona/{{_DOM. cua_master }}?code={{eatc_dona_headers.e atc-code }}&id_unico_registro={{eatc_donation_managers. identificador_unico_registro }}&id_user={{eatc_users. _id }} 

 Y cuando sea invocado realizará las siguientes consultas: 

DEFINICIÓN SI LA CUENTA MAESTRA POSEE MONETIZACIÓN, PARA VALIDACIÓN DE TOPES 

 El sistema realiza la siguiente consulta con los datos de la cuenta maestra: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua_master_doma_monetization?eatc_cua_master={{_DOM.cua_master}}&active_since[0]=2019-11-20&active_since[1]={{fecha_actual}} 

 Si el servicio recibe una respuesta valida entonces se procede a la " Validación de tope de KG por gestor de donación por mes según su licencia ".  Si la respuesta no es válida, entonces no se realiza la anterior validación y pasa directamente a " Establecer si el anuncio está dentro del match ". 

Ejemplo 1: ambiente de pruebas cua_master abaco, 2022-08-09 
 El sistema realiza la siguiente consulta: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master_doma_monetization? eatc_cua_master =abaco& active_since[0]=2019-11-20 & active_since[1]= 2022-08-09   

 Dado que se obtiene una respuesta válida entonces se procede a realizar la validación de tope de KG por gestor de donación. 

Ejemplo 2: ambiente productivo cua_master abaco, 2022-08-09 
 El sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master_doma_monetization? eatc_cua_master =abaco& active_since[0]=2019-11-20 & active_since[1]= 2022-08-09    

 Como no se obtienen resultados, el proceso pasa directamente a pasa directamente a " Establecer si el anuncio está dentro del match ", sin hacer validación de topes por licencia. 

VALIDACIÓN DE TOPE POR KG GESTOR DE DONACIÓNPOR MES SEGÚN SU LICENCIA 
 Antes de desplegar el formulario, el sistema deberá realizar la siguiente consulta, teniendo en cuenta los datos alojados en la información de la cuenta y que se consultan mediante este llamado 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_donation_managers.identificador_unico_registro}}&_cmp=eatc_doma_typology_b,eatc_license,eatc_license_valid_until,eatc_cua_master 

Ejemplo Pruebas: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers. identificador_unico_registro }} &_cmp= eatc_doma_typology_b,eatc_license,eatc_license_valid_until,eatc_cua_master 

La validación de tope no aplica para bancos de alimentos 

 Si el dato obtenido en 
 {{eatc_donation_managers. eatc_doma_typology_b }} = 1 

 Entonces el sistema, no procede con la presente validación y pasa directamente a " Establecer si el anuncio está dentro del match " 
 Si la tipología B de la organización es diferente, entonces continua la presente validación. 

Validación de la fecha de validez de la licencia 
 Con la consulta se obtiene el dato eatc_donation_managers. eatc_license_valid_until . Si la fecha actual es posterior a la fecha registrada (es decir que la fecha de validez de la licencia está en el pasado), entonces el servicio debe validar como si la licencia fuera "free" (actualizando el dato en la información del eatc_donation_manager) tal como se establece en el siguiente punto, mediante la siguiente consulta: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_licences_prices? doma_license = free&_cmp= cua_mensual_kg_sup_limit 

 Ejemplo entorno de pruebas: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_licenses_prices?doma_license=free&_cmp=cua_mensual_kg_sup_limit   

 Si la fecha actual es anterior a la fecha registrada (es decir que la fecha de validez de la licencia está en el futuro), entonces el servicio sigue adelante con el siguiente proceso: 

 Validación de tope de KG por gestor de donación por mes según su licencia 
 Antes de desplegar el formulario, el sistema deberá realizar la siguiente consulta, teniendo en cuenta los datos alojados en la información de la cuenta y que se consultan mediante este llamado 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers. identificador_unico_registro }} &_cmp= eatc_doma_typology_b,eatc_license,eatc_license_valid_until,eatc_cua_master 

 La validación de tope no aplica para bancos de alimentos 
 Si el dato obtenido en 
 {{eatc_donation_managers. eatc_doma_typology_b }} = 1 

 Entonces el sistema, no procede con la presente validación y pasa directamente a " Establecer si el anuncio está dentro del match " 

 Si la tipología B de la organización es diferente, entonces continua la presente validación. 

 Consulta del límite de KG por licencia 
 El sistema realiza  la siguiente consulta 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_licences_prices? doma_license = {{eatc_donation_managers. eatc_license }}&_cmp= cua_mensual_kg_sup_limit 

 Ejemplo entorno de pruebas: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_licenses_prices?doma_license=superhero&_cmp=cua_mensual_kg_sup_limit    

 Si esta última consulta no trae ningún valor, se utilizará esta consulta por defecto: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_licences_prices? doma_license = free&_cmp= cua_mensual_kg_sup_limit 

 Ejemplo entorno de pruebas: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_licenses_prices?doma_license=free&_cmp=cua_mensual_kg_sup_limit   

 Consulta del peso acumulado en el mes actual de las donaciones  
 El sistema realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/ {{eatc_donation_managers. eatc_cua_master }} /eatc_dona_headers? eatc-donation_manager_code = {{eatc_donation_managers. identificador_unico_registro }} &eatc-publication_date[0]={{fecha_primer_dia_mes_actual}}&eatc-publication_date[1]={{fecha_actual}}&eatc-state= awarded,scheduled,delivered,received,pre-certified,certified &_cmp= eatc-original_weight_kg 

 Y con los resultados, hace la sumatoria de kilogramos gestionados en el mes {{ kg_gestionados_mes }}. 

 Comparación de KG gestionados con el límite por licencia: se le adicionan a los kg_gestionados_mes los kg originales de la donación que se está adjudicando para realizar la comparación 

 Si los KG gestionados en el mes {{ kg_gestionados_mes }} más los kg originales de la donación que se está adjudicando (eatc_dona_headers( {{eatc_dona_headers. eatc-code }} ). eatc-original_weight_kg ) , son inferiores al límite por la licencia {{eatc_doma_licences_prices. cua_mensual_kg_sup_limit }} , entonces el proceso seguirá,  pasando directamente a " Establecer si el anuncio está dentro del match " 

 Si los KG gestionados en el mes {{ kg_gestionados_mes }} más los kg originales de la donación que se está adjudicando (eatc_dona_headers( {{eatc_dona_headers. eatc-code }} ). eatc-original_weight_kg ) , son superiores o iguales al límite por la licencia {{eatc_doma_licences_prices. cua_mensual_kg_sup_limit }}, entonces el sistema deberá lanzar el Mensaje de error por sobrepaso de límite de licencia, que se especifica a continuación. 

 Mensaje de error por sobrepaso de límite de licencia 
 El servicio deberá responder con un mensaje: 
 awardona_fail_for_exceeding_doma_license_limit 

 De igual manera deberá realizar una escritura en la estructura de de eventos de upgrade: 

 parametros_escritura_eventos_upgrade 

 eatc_datetime : "{{current_date_time}}", 
 eatc_date : "{{current_date}}", 
 eatc_country : "{{eatc_cua_master( eatc_cua = {{eatc_donation_managers. eatc_cua_master }} ). eatc_country }}", 
 eatc_cua_master : " {{eatc_donation_managers. eatc_cua_master }} ", 
 eatc_cua : "" => *** No se envía registro *** 
 eatc_doma : " {{eatc_donation_managers. identificador_unico_registro }} ", => *** Campo nuevo , se debe adicionar a la tabla *** 
 eatc_platform : " app_beneficiarios ", 
 eatc_upgrade_event : " awardona_fail_for_exceeding_doma_license_limit ", 
 eatc_user : " {{eatc_users. _id }} ", 
 eatc_actual_rescue_plan : "free", 
 eatc_actual_analytics_plan : "", 
 eatc_actual_doma_license : " {{eatc_donation_managers. eatc_license }} ", => *** Campo nuevo , se debe adicionar a la tabla *** 
 eatc_note : "awardona_automatic", 
 eatc_type_period : "", 
 eatc_type_upgrade : "" 

 Establecer si el anuncio está dentro del match 
 Al recibir el llamado el sistema debe consultar si el anuncio de donación en particular se encuentra dentro de los que hacen match para la organización en cuestión mediante la siguiente consulta. 

 {{URL_entorno_beneficiarios}}/ matchquery /{{_DOM. cua_master }}/ {{eatc_donation_managers. identificador_unico_registro }} 

 EJEMPLO (retomando el anterior):  
 https://beneficiarios.eatcloud.info/matchquery/abaco/811018073 

 Si el anuncio no se encuentra entre los que devuelve la consulta, entonces el servicio debe retornar un mensaje de error con la siguiente información 

 award_error_code:001 "El anuncio no puede ser asignado porque no se encuentra entre aquellos que hacen match con la organización"  

 Consulta del estado del donation manager para la adjudicación de la donación 
 El servicio debe consultar si el gestor de donaciones tiene estatus "activo", si el gestor de donación tiene un estado diferente a " activo " el anuncio no podrá adjudicarse: 

 {{URL_entorno_beneficiarios}}/ api /{{_DOM. cua_master }}/ {eatc_donation_managers? identificador_unico_registro ={{eatc_donation_managers. identificador_unico_registro }}&_distinct= eatc_state 

 Si el gestor de donaciones no pasa esta validación, se despliega el siguiente error 

 award_error_code:002 "El anuncio no puede ser asignado porque se encuentra bloqueado" 

 Si el gestor está en estado " activo ", el servicio debe proceder a bloquearlo (incorporando la información respectiva en el parámetro de bloqueo), para seguir con su proceso de asignación. 

 Consulta de bloqueo del anuncio que va a ser adjudicado 
 El servicio debe consultar si el anuncio sobre el cuál se van a efectuar los procesos de adjudicación, se encuentra bloqueado.  En caso de ser así (el anuncio se encuentra bloqueado), el servicio debe contestar con un mensaje de error con la siguiente información 

 award_error_code:002 "El anuncio no puede ser asignado porque se encuentra bloqueado" 

 Si el anuncio no se encuentra bloqueado, el servicio debe proceder a bloquearlo (incorporando la información respectiva en el parámetro de bloqueo), para seguir con su proceso de asignación. 

 Validación del estado del anuncio (announced) para poder ser adjudicado: mensaje diferenciado si el anuncio fue adjudicado al mismo beneficiario 
 A manera de error handler o proceso redundante (dado que al establecer si el anuncio está en el match, se realiza la misma función), el sistema debe comprobar si el anuncio en cuestión posee estado " announced ".   

 Validación de si el anuncio fue adjudicado al mismo beneficiario que se lo está adjudicando 
 El sistema realiza la siguiente consulta 

 {{URL_entorno_donantes}}/ api /{{_DOM. cua_master }}/eatc_dona_headers?eatc-state=!announced&eatc-code= {{eatc_dona_headers. eatc-code }} & eatc-donation_manager_code = {{eatc_donation_managers. identificador_unico_registro }}&_cont 

 Si la consulta entrega una respuesta válida, entonces el sistema entrega el siguiente mensaje: 

 award_error_code:003a "El anuncio de donación ya te fue asignado. Puedes continuar con su gestión" 

 En caso de no recibir respuesta válida, entonces el sistema valida lo siguiente: 

 {{URL_entorno_donantes}}/ api /{{_DOM. cua_master }}/eatc_dona_headers?eatc-state=!announced&eatc-code= {{eatc_dona_headers. eatc-code }} &_cont 

 Si el anuncio no posee el estado anunciado y fue asignado a otro gestor de donaciones diferente, entonces el sistema debe retornar un mensaje de error con la siguiente información (cómo lo había venido haciendo hasta el momento) 

 award_error_code:003 "El anuncio no puede ser asignado porque ya ha sido adjudicado" 

 Si el anuncio posee estado " announced ", entonces el proceso sigue su curso. 

 Validación de existencia de datos de adjudicación 
 A manera de error handler el sistema debe verificar si el anuncio tiene datos en los parámetros " eatc-donation_manager_code " o " eatc-donation_manager_name ", en caso de ser así, se debe enviar un mensaje de error con la siguiente información 

 award_error_code:004 "El anuncio no puede ser asignado porque ya ha sido adjudicado y hay problemas con el registro de su estado" 

 Cuando el proceso detecte este caso, deberá correr el Error Handler: datos incompletos del gestor de donación y realizar las siguientes validaciones para corregir el estado del anuncio: 

 Corrección del estado del anuncio (debe implementarse como un servicio aparte que se invoque desde "awardona") 
 Si el anuncio tiene una fecha válida en el registro " eatc-certification_datetime ", entonces el estado del anuncio deberá cambiar a " certified " 
 Si el anuncio tiene una fecha válida en el registro " eatc-pre_certification_datetime ", entonces el estado del anuncio deberá cambiar a " pre-certified " 
 Si el anuncio tiene una fecha válida en el registro " eatc-receipt_datetime ", entonces el estado del anuncio deberá cambiar a " received " 
 Si el anuncio tiene una fecha válida en el registro " eatc-picking_checkout_datetime ", entonces el estado del anuncio deberá cambiar a " delivered " 
 Si el anuncio tiene una fecha válida en el registro " eatc-scheduling_datetime ", entonces el estado del anuncio deberá cambiar a " scheduled " 
 Si el anuncio tiene una fecha válida en el registro " eatc-adjudication_datetime ", entonces el estado del anuncio deberá cambiar a " awarded " 

 Si el anuncio no tiene datos de adjudicación (beneficiario) entonces se puede proceder a realizar los siguientes registros para adjudicar el anuncio a quien lo ha solicitado: 

 Registro de datos de adjudicación 
 Actualización de la información del encabezado de donación ( eatc_dona_headers ) 
{{parametros_actualizacion_encabezado}} 
 Al aceptar un anuncio de donación se debe actualizar la siguiente información: 
 eatc-state : debe cambiar de " announced " a " awarded ". 

 eatc-adjudication_datetime :   Fecha y hora de la adjudicación del anuncio de donación.  El sistema toma el TIMESTAMP del momento en el cual se realiza la adjudicación en formato AAAA-MM-DD HH:MM:SS . 

 eatc-donation_manager_user_doc_id : corresponde al dato que llega en el parámetro " {{eatc_users._id}} " de la invocación del servicio. 

 eatc-donation_manager_code : corresponde al dato que llega en el parámetro " {{eatc_donation_managers.identificador_unico_registro}} " de la invocación del servicio 

 eatc-donation_manager_name : nombre del gestor de donaciones al cual se le adjudica el anuncio, que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &_distinct=organizacin 

 eatc-donation_manager_address : dirección del gestor de donaciones al cual se le adjudica el anuncio, que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &_distinct=unidad_territorial 

 eatc-donation_manager_phone : teléfono del gestor de donaciones al cual se le adjudica el anuncio, que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &_distinct=telefono1 

 eatc-donation_manager_typology_a : corresponde a la organización vinculada, que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &_distinct = organizacion_vinculada 

 eatc-donation_manager_typology_b : corresponde a eatc_doma_doma_typology_b, que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM. cua_maste r}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers. identificador_unico_registro }} &_distinct = eatc_doma_typology_b 

 eatc-donation_manager_typology_c: c orresponde a tipo_organizacion , que se puede obtener con el siguiente llamado: 
 {{URL_entorno_beneficiarios}}/ api /{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &_distinct = tipo_organizacion 

 ***NUEVO: registro de “eatc_destination_lat” y “eatc_destination_lon” *** 

 eatc_destination_lat: c orresponde al dato “latitud” , que se puede obtener con el siguiente llamado: 

 {{URL_entorno_beneficiarios}}/ api /{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers. identificador_unico_registro }} &_cmp = latitud 

 eatc_destination_lon: c orresponde al dato “longitud” ,, que se puede obtener con el siguiente llamado: 

 {{URL_entorno_beneficiarios}}/ api /{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro= {{eatc_donation_managers. identificador_unico_registro }} &_cmp = longitud 

 ***NUEVO: registro de “eatc_state3”

 eatc_state3: “Por entregar” 

Escritura con la API 
 {{ URL_entorno_donantes }}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion= update &{{ parametros_actualizacion_encabezado }}&WHEREeatc-code={{eatc_dona_headers. eatc-code }} 

 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history )  

 Se deberán registrar  los estados " annouced " (en caso de que este estado no se esté registrando en el proceso de creación del anuncio) y " awarded " 

 Registro del estado "annouced" :  
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code = {{eatc_dona_headers.eatc-code}} & eatc-state = annouced & eatc-date_time ={{eatc_dona_headers.eatc-publication_datetime}}& eatc-log = EatCloud: proceso awardona. 

 Registro del estado "awarded" :  
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code = {{eatc_dona_headers.eatc-code}} & eatc-state = awarded & eatc-date_time ={{ eatc_dona_headers. eatc-adjudication_datetime }}& eatc-log = EatCloud: proceso awardona eatc-donation_manager_code: {{eatc_donation_managers.identificador_unico_registro}} eatc-donation_manager_user_doc_id: {{eatc_users._id}} 

 El sistema debe validar una escritura correcta en los datos del anuncio y su historial y si la misma fue realizada debe entregar un mensaje de éxito de la siguiente manera: 

 eatc-adjudication_datetime: AAAA-MM-DD HH:MM:SS "El anuncio fue adjudicado con éxito" 

 Si existe algún problema con la escritura de los datos del anuncio y el historial se deberá proceder a reintentar la escritura hasta que la misma sea realizada de manera adecuada. 

 Reorganización de turnos ante la asignación de un anuncio que le apliquen reglas PACADI => PILOTO NESTLE 

 Si la  clasificación del anuncio, corresponde a una regla pacadi, es decir si la consulta 
 {{ URL_entorno_donantes }}/api/{{ cua_master }}/ eatc_dona_headers& eatc_dona_header_code ={{ eatc_dona_header_code }}& eatc_match_asignation_rule ={{ _lk pacadi_nestle _lk }}   

 ó más específicamente: 
 {{ URL_entorno_donantes }}/api/mexico/ eatc_dona_headers& eatc_dona_header_code ={{ eatc_dona_header_code }}& eatc_match_asignation_rule ={{ _lk pacadi_nestle _lk }}   

 Arroja una respuesta válida, entonces se deberá a realizar un registro, que implique que quien se adjudicó la donación, "utilice" su turno PACADI, y por lo tantos el orden de turnos avancen. 

 Para ello se debe borrar el turno respectivo del beneficiario que se adjudica y en la medida de las posibilidades reescribir los turnos PACADI para el resto de los bancos que les aplica esto, con el ánimo de que avancen en el turno 

 Borrado del turno PACADI 

 El sistema deberá borrar el registro de los turnos PACADI, del presente beneficiario (al sugerir que el valor es "" se indica que se debe borrar el registro: 
 {{url_entorno_beneficiarios}}/crd/mexico/?_tabla=eatc_donation_managers&_operacion=update& eatc_pacadi_nestle_turn_under_1_ton ="" & eatc_pacadi_nestle_turn_over_1_ton =""&WHERE identificador= {{eatc_donation_managers. identificador_unico_registro }} 

 Actualización de turnos PACADI para los demás Bancos que les aplica 

 El sistema deberá consultar los demás bancos que les aplica turno (en este caso particular de Nestlé): 

 {{url_entorno_beneficiarios}}/api/mexico/eatc_donation_managers&_ eatc_pacadi_nestle_turn_under_1_ton =_novacio & eatc_pacadi_nestle_turn_over_1_ton =_novacio&_cmp= identificador_unico_registro, _ eatc_pacadi_nestle_turn_under_1_ton,eatc_pacadi_nestle_turn_over_1_ton 

 Y para ellos deberá adelantarles a cada uno, el turno (para compensar el turno que se borró) 

 {{url_entorno_beneficiarios}}/crd/mexico/?_tabla=eatc_donation_managers&_operacion=update& eatc_pacadi_nestle_turn_under_1_ton = {{ {{ eatc_donation_managers. eatc_pacadi_nestle_turn_under_1_ton }} -1 }} & eatc_pacadi_nestle_turn_over_1_ton = {{ {{ eatc_donation_managers. eatc_pacadi_nestle_turn_over_1_ton }} -1 }} &WHERE identificador= {{eatc_donation_managers. identificador_unico_registro }} 

 ***NUEVO : Invocación webhook para envío de mensajería push para promover gestión de donaciones cercanas ***=> Mejora 

 Una vez efectuados los procesos para adjudicar la donación y validando que la misma halla sido correctamente adjudicada, el sistema debe proceder a realizar la siguiente invocación  tomando la {{fecha_hora_actual}} en formato AAAA-MM-DD HH:MM:SS y el {{ambiente}} : dev para desarrollo o prd para producción 
Endponint 
 http://20.83.146.184/api/v1/webhooks/BZsCki29YAdnANpgKAsvi/sync   
Método: POST 
Body 
 { 
     "data" : { 
         "rows" : [ 
                 { 
                 "Fecha y Hora": " {{fecha_hora_actual}} " , 
                 "Ambiente": "{{ambiente}}" , 
                 "cua_master": "{{cua_master}}" , 
                 "codigo_donacion": "{{eatc_dona_header_code}}" 
                 } 
         ] 
     } 
 } 
El sistema podrá entregar este tipo de respuestas: 
La donación no existe: 
 { 
     "ok" : false , 
     "data" : { 
         "ambiente" : "{{ambiente}}" , 
         "cua_master" : "{{cua_master}}" , 
         "fecha_hora" : " {{fecha_hora_actual}} " , 
         "codigo_donacion" : "{{eatc_dona_header_code}}" 
     }, 
     "message" : "donation_does_not_exist" , 
     "management_suggestion_message_created" : false 
 } 
Es un caso que no debería ocurrir, pero en caso de ocurrencia, se debe revisar. 
La donación no tiene otras donaciones cercanas: 
 { 
      "ok" : false , 
      "data" : { 
          "ambiente" : "{{ambiente}}" , 
          "cua_master" : "{{cua_master}}" , 
          "fecha_hora" : " {{fecha_hora_actual}} " , 
          "codigo_donacion" : "{{eatc_dona_header_code}}" 
      }, 
      "message" : "near_donations_does_not_exist" , 
      "management_suggestion_message_created" : false 
 } 
Esto quiere decir que no se encontraron donaciones cercanas, y por lo tanto no se envía ningún mensaje 

La donación tiene donaciones cercanas, pero aun no se han enviado mensajes: 
 { 
      "ok" : true , 
      "data" : { 
          "ambiente" : "{{ambiente}}" , 
          "cua_master" : "{{cua_master}}" , 
          "fecha_hora" : " {{fecha_hora_actual}} " , 
          "codigo_donacion" : "{{eatc_dona_header_code}}" 
      }, 
      "message" : "near_dona_exist" , 
      "management_suggestion_message_created" : false 
 } 
Quiere decir que se encontraron donaciones cercanas y se enviará un mensaje asociado a cada donación. Se puede entender como un mensaje intermedio, pero que para efectos del presente proceso puede ser concluyente. 

Se enviaron mensajes para promover gestión de donaciones cercnas: 
 { 
      "ok" : true , 
      "data" : { 
          "ambiente" : "{{ambiente}}" , 
          "cua_master" : "{{cua_master}}" , 
          "fecha_hora" : " {{fecha_hora_actual}} " , 
          "codigo_donacion" : "{{eatc_dona_header_code}}" 
      }, 
      "message" : "management_suggestion_mesages_created" , 
      "management_suggestion_message_created" : true 
 } 
Este mensaje indica que se enviaron sendos mensajes para promover la gestión de donaciones cercanas a la actualmente adjudicada. 

 ***DEPRECADO: LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN*** 

 Nota importante: este llamado debe funcionar tanto para los procesos que se llaman desde la APP como en los procesos de asignación automática de donaciones. 

 Endpoint (según documentación : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmAdjudicarDonacion 

 Parámetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio 

 ****HASTA AQUÍ IMPLEMENTACIÓN URGENTE*** 

 ***Pendiente de revisión del ejemplo*** 
 Ejemplo _DOM.cua_master=abaco, entorno de pruebas: 

 Para el anuncio de donación cuyo eatc-code = 2019209714 , El usuario El usuario Juan Carlos Buitrago (numero_cedula = 8161174) que tiene como organización el dato: 900326456-1 ( https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 ) oprime el botón "Aceptar" a las 20:00:00 del día 2019-09-23.   

 Dado que se tienen los siguientes datos: 

 eatc-donation_manager_user_doc_id= 8161174 (que corresponde a numero_cedula ) 
 eatc-donation_manager_code= 900326456-1 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_name= ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA (que corresponde a eatc_donation_managers. organizacin) 
 eatc-donation_manager_address= Cll. 19 A Nº 32 - 50 Barrio Cundinamarca (que corresponde a eatc_donation_managers. unidad_territorial) 
 eatc-donation_manager_phone= 4029305 (que corresponde a eatc_donation_managers. telefono1) 
 eatc-donation_manager_typology_a= corresponde a {{eatc_donation_managers. organizacion_vinculada}} 
 eatc-donation_manager_typology_b= corresponde a {{eatc_donation_managers. eatc_doma_typology_b}} 
 eatc-donation_manager_typology_c= corresponde a {{eatc_donation_managers. tipo_organizacion}} 

 Utilizando el API se realiza el siguiente registro: 

 https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= awarded & eatc-adjudication_datetime = 2019-09-23%2020:00:00& eatc-donation_manager_user_doc_id= 8161174 & eatc-donation_manager_code= 900326456-1& eatc-donation_manager_name= ASOCIACION%20DE%20BANCOS%20DE%20ALIMENTOS%20DE%20COLOMBIA& eatc-donation_manager_address= Cll.%2019%20A%20Nº%2032%20-%2050%20Barrio%20Cundinamarca& eatc-donation_manager_phone= 4029305& eatc-donation_manager_typology_a= BdeA& eatc-donation_manager_typology_b= ABACO& eatc-donation_manager_typology_c= Bogotá& WHEREeatc-code= 2019209714 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924182418", 
 op : true, 
 cont : 1, 
 mem : 0.75, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 El registro se puede consultar aquí: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=2019209714 

 Para el registro del estado "awarded" se toma la fecha de adjudicación del anuncio ( eatc-publication_datetime) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-donation_manager_code y el eatc-donation_manager_user_doc_id incluyendo la declaración de los campos)  
 Ejemplo _DOM. cua_master=abaco : 

 Para el anuncio de donación cuyo eatc-code = 2019209714 (del ejemplo anterior), dado que se tienen los siguientes datos: 

 eatc-code: "2019209714", 
 eatc-publication_datetime : "2019-09-18 15:37:54", 
 eatc-adjudication_datetime : "2019-09-23 20:00:00", 
 eatc-donation_manager_code: " 900326456-1" 
 eatc-donation_manager_user_doc_id : "8161174 

 Utilizando el API se realizan los siguientes registros: 

 Registro del estado "annouced" :  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code =2019209714& eatc-state = annouced & eatc-date_time =2019-09-18%2015:37:54& eatc-log =EatCloud 

 Registro del estado "awarded" :  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code =2019209714& eatc-state = awarded & eatc-date_time =2019-09-23%2020:00:00& eatc-log = eatc-donation_manager_code: 900326456-1%20 eatc-donation_manager_user_doc_id: 8161174 

 Para consultar los estados registrados: https://donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=2019209714 

 La app en ambos casos debe validar que los registros se realicen, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925154048", 
 op : true, 
 cont : 1, 
 last : "3", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 ***PENDIENTE ***: REVISIÓN CALIFICACIÓN ***Registro de la calificación por aceptar un anuncio de donación ( _id=1 ) 
 Cuando se presiona el botón " Acepto ", el sistema debe realizar un registro de calificación de la siguiente manera: 
 _id : identificador único generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evaluó la calificación, en este caso la fecha  y hora de adjudicación. 
 doma_id : Corresponde al código del gestor de donaciones " eatc_dona_headers.eatc-donation_manager_code". 
 eatc-dona_id : identificador del anuncio de donación " eatc_dona_headers. eatc-id". 
 action_id : corresponde al identificador de la regla de calificación " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificación " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el último registro realizado para el gestor de donación y sobre el mismo, se toma el dato "acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donación cuyo eatc-code = 2019209714 (eatc-id=8687012) del ejemplo anterior, con fecha de adjudicación ( eatc-adjudication_datetime) 2019-09-23 20:00:00 

 El registro resultante sería: 

 _id : "#####", 
 date_time : "2019-09-23 20:00:00", 
 doma_id : "900326456-1", 
 eatc-dona_id : "8687012", 
 action_id : "1", 
 points : "10", 
 acumulated_points : "cálculo de puntos acumulados" 

 Nota sobre el cálculo de puntos acumulados "acumulated_points" : el sistema busca la última calificación registrada para el gestor de donaciones respectivo ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).  Definiendo el último registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificación (10) . 

 Escritura con la API:  
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time = 2019-09-23%2020:00:00 & doma_id = 900326456-1 & eatc-dona_id = 8687012 & action_id =1& points =10& acumulated_points = cálculo%20de%20puntos%20acumulados 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925163748", 
 op : true, 
 cont : 1, 
 last : "14", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aquí se puede consultar el registro realizado: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=1&eatc-dona_id=8687012    

 ***PENDIENTE*** Actualización de información de KPIs 
 Se deberán realizar los registros en la estructura eatc_dona_kpi correspondientes a las transformaciones al adjudicar el anuncio (ver documentación vinculada). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 786cc017-480e-4684-be26-9f079acde7d3 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 41fc704f-5c22-4f6b-9d8d-c87e36c35fd2 
 2026-01-07T00:33:43.1610100Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"0a623a63-ed0b-4937-95ea-b73a0f63045c","SequenceId":3526,"FluidContainerCustomId":"928365cf-df43-4b69-a299-8351c37bb201","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 AWARDONA: PROCESO PARA ADJUDICARSE UNA DONACIÓN