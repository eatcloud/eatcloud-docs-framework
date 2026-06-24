# aceptación-anuncio-de-donación-eatc_dona_acc.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando se oprime el botón "Acepto" se debe realizar la actualización del estado del anuncio de donación de: publicado a adjudicado. Esta actualización debe realizarse en tiempo real utilizando el webservice para WS Cambio de estado de anuncio de donación (API CRUD) una vez aceptada la misma se lleva a la funcionalidad Controlador para Programación de recogida del anuncio de donación. eatc_dona_program . 

 Mensaje de fecha límite de recogida para donaciones con eatc_with_last_p_day = y *** (después de Ver términos y condiciones y antes del botón " Acepto ") 
 Si la donación en cuestión tiene el dato  " eatc_with_last_p_day ":" y " entonces debajo de términos y condiciones se debe presentar el siguiente label y la siguiente información (de manera vistosa, para que el usuario no la pase por alto). 

 class= lb_recoger_solo_no_habil (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel= lb_recoger_solo_no_habil ) 

 "RECOGER SOLO EN FIN DE SEMANA: Esta donación solamente la podrás recoger hasta el último día NO HÁBIL del presente fin de semana o puente festivo:" 

 A continuación del mensaje se presenta la siguiente fecha: 
 {{eatc_dona_headers. eatc_last_p_day }} 

 {{ URL_entorno_donantes }}/api/{{_DOM.c ua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_distinct= eatc_last_p_day 

 ERROR HANDLER SI NO LLEGA DATO EN eatc_dona_headers.eatc_last_p_day 

 Si esto no ocurre por un error en el proceso respectivo , entonces la APP deberá calcular el último día NO hábil del presente fin de semana o puente en formato AAAA-MM-DD (Por ejemplo si la fecha actual corresponde a un sábado de un fin de semana normal, la fecha que se registra será la del día siguiente.  Si la fecha actual es un  domingo  de un fin de semana normal, la fecha será la del mismo domingo.  (posteriormente cuando se implemente el tema de días festivos, esta fecha se deberá extender hasta el lunes correspondiente)) para mostrarlo. 

 También el sistema debería registrar este dato calculado en el respectivo campo ( eatc_dona_headers.eatc_last_p_day ) 

 {{ URL_entorno_donantes }}/crd/{{_DOM.c ua_master }}/?_tabla=eatc_dona_headers&_operacion=update&eatc_last_p_dayeatc-code={{eatc_dona_headers. eatc-code }}&_distinct= eatc_last_p_day 

 Si la donación no tiene dato válido en " eatc_with_last_p_day " (vacío, nulo, o cero, o dato: " n ") , entonces no se despliega el anterior mensaje y el dato de la fecha, y se mostrará el modal como se viene mostrando hasta el momento. 

 Vínculo "ver términos y condiciones" 
 Cuando se oprime el vínculo "ver términos y condiciones" se lleva a la vista Controlador vista términos y condiciones eatc_doma_term 

 Botones "Cancelar" y "x" 
 Si se oprime el botón "cancelar" o "x" se retorna a la vista anterior. 

 ***NUEVO: para los anuncios con registro válido en eatc-warning: mensaje de validación con valor por defecto en negativo *** 
Si el anuncio en cuestión tiene un registro válido en eatc-warning, es decir, si la siguiente consulta arroja un resultado válido 
 {{ URL_entorno_donantes }}/api/{{_DOM.c ua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}& eatc-warning = _novacio &_cmp= eatc-warning 
al accionar el botón “ Aceptar ” el sistema debe presentarle un mensaje de la siguiente manera: 
Label: “He leído la siguiente información” 
A continuación se presenta el contenido del eatc-warning respectivo 
 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/eatc_dona_headers?eatc-code={{eatc_dona_headers.eatc-code}}&_cmp= eatc-warning 
Label: “Entiendo y acepto las indicaciones entegadas por el donante” 
Por defecto debe aparecer la opción “ No acepto ”, para que el usuario tenga que hacer una acción consciente y deliverada de aceptación (pinchar en el botónd “ Aceptar ”).  Si el usuario no acepta, lo devuelve a la pantalla anterior sin hacer ninguna acción (no se adjudica el anuncio).  Cuando le da clic a la opción “ Aceptar ” entonces se dispara el siguiente proceso de llamado al servicio “awarddona” (ese botón se comporta como el botón original de aceptación, que a continuación se describe). 

Si el anuncio no tiene un registro en eatc-warning, entonces se despliega el botón “Aceptar” como de costumbre. 
 Botón Aceptar:  llamado al servicio de "awarddona": 

 Cuando se acepta una donación  se realiza el llamado al servicio "awardona" de la siguiente manera 

 {{URL_entorno_beneficiarios}}/ awardona /{{_DOM.cua_master}}?code= {{eatc_dona_headers.eatc-code}} &id_unico_registro= {{eatc_donation_managers.identificador_unico_registro}} &id_user= {{eatc_users._id}} 

 ***NUEVO: comportamiento del botón mientras recibe respuesta *** 
 Imediatamente se oprima el botón y mientras se recibe una respuesta del servicio, el botón deberá mostrar un loader, que se convertirá en un chulo verde, cuando el servicio responda, con el ánimo de evitar que el usuario accione en múltiples ocasiones el botón, por no ver una respuesta inmediata del mismo. 

 Ejemplo Ambiente de pruebas,  
 El anuncio cuyo código es: exito2020210602163155870 se lo adjudica el Gestor de donaciones cuyo identificador único de registro es 900082682 a través de su usuario con _id 8.  Este sería el llamado 

 https://devdonantes.eatcloud.info/awardona/abaco?code=exito2020210602163155870&id_unico_registro=900082682&id_user=8 

 Manejo de mensajes de error que envía el servicio: 
 Si llegan estos mensajes de error, se desplegará en la App un Mensaje en un modal con el respectivo copy internacionalizado 

 err_msg: "award_error_code:001 ..." 
 Si el servicio entrega este mensaje de error: 
 award_error_code:001 "El anuncio no puede ser asignado porque no se encuentra entre aquellos que hacen match con la organización"  

 El sistema desplegará el siguiente label: class ="lbl_award_error_code_001" 

 err_msg: "award_error_code:002 ..." 
 Si el servicio entrega este mensaje de error: 
 award_error_code:002 "El anuncio no puede ser asignado porque se encuentra bloqueado" 

 El sistema desplegará el siguiente label: class ="lbl_award_error_code_002" 

 ***NUEVO: err_msg: "award_error_code:003 a ..." *** 
 Si el servicio entrega este mensaje de error: 
 award_error_code:003 a "El anuncio de donación ya te fue asignado. Puedes continuar con su gestión" 

 El sistema desplegará el siguiente label: class ="lbl_award_error_code_003 a " 

 Y deberá desplegar el modal para sugerir la programación del anuncio . 

 err_msg: "award_error_code:003 ..." ***NUEVO: debe retornar a la nube de donaciones *** 
 Si el servicio entrega este mensaje de error: 
 award_error_code:003 "El anuncio no puede ser asignado porque ya ha sido adjudicado" 

 El sistema desplegará el siguiente label: class ="lbl_award_error_code_003" 

 Y deberá retornar a la nube de donaciones (dando un tiempo prudente para que se lea el mensaje o label desplegado). 

 err_msg: "award_error_code:004 ..." 
 Si el servicio entrega este mensaje de error: 
 award_error_code:004 "El anuncio no puede ser asignado porque ya ha sido adjudicado y hay problemas con el registro de su estado" 

 El sistema desplegará el siguiente label: class ="lbl_award_error_code_004" 

 ***NUEVO: err_msg: "award_error_code: awardona_fail_for_exceeding_doma_license_limit" *** 
 Si el servicio entrega este mensaje de error: 
 awardona_fail_for_exceeding_doma_license_limit 

 El sistema deberá presentar el siguiente mensaje: 
 "Haz sobrepasado los límites de tu licencia actual. Para adjudicarte la presente donación deberás actualizar tu licencia" 

 label (class)=lbl_awardona_fail_for_exceeding_doma_license_limit ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_awardona_fail_for_exceeding_doma_license_limit )  

 A continuación, deberá presentar un botón para direccionar a la funcionalidad de checkout: 
 Actualizar licencia 

 label (class)=lbl_actualizar_licencia ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_actualizar_licencia )  

 Al presionar el botón, se deberá redireccionar a la funcionalidad de checkout ( Información de planes ). 

 Variables que se le deberán enviar a la funcionalidad de checkout: 
 {{eatc_donation_managers. eatc_cua_master }} 
 {{eatc_donation_managers. identificador_unico_registro }} 

 Cuando se recibe una respuesta exitosa del servicio: 
 Si el servicio responde con un mensaje de éxito, se la siguiente manera: 
 { 
 ts: "210603182430", 
 op: true, 
 res: [ 
 " eatc-adjudication_datetime: AAAA-MM-DD HH:MM:SS "El anuncio fue adjudicado con éxito" 
  " 
 ], 
 mem: 0.42, 
 time: "00:00:00", 
 } 

 Entonces la App realizará lo siguiente: 

 Mensaje para informar sobre el tiempo de programación 
 Una vez se acepte del anuncio, la App deberá mostrar un anuncio, que informe al gestor de donaciones que tendrá una hora para programar el anuncio y si no logra realizar la programación en dicho lapso el anuncio será liberado de nuevo para que otra organización lo tome y lo programe.  El anuncio sería así 

 Muchas gracias por aceptar esta donación. 

 A partir del momento tendrás una hora para programar la fecha y hora de recogida de la misma. Si no logras hacerlo en este lapso, el anuncio será liberado de nuevo y otra institución lo podrá tomar y programar. 
 ¿Deseas programar la recogida la donación? 

 SI                  NO 

 La opción SI: direcciona la app a la funcionalidad de " programar recogida de donanción " 
 Con el ánimo de garantizar que el beneficiario programe la recogida, el sistema inmediatamente debe direccionar a la funcionalidad de programación. 

 La opción NO: direcciona a " mis donaciones " 
 Con el ánimo de que vea las donaciones asignadas y los contadores de tiempo que se generan. 

 DEPRECADO (DADO QUE LO MANEJARÁ EL SERVIDOR a través del servicio awardona ) 

 pasan básicamente cuatro cosas: 1. Se actualiza información del encabezado de donación ; 2. Se realizan registros en la estructura de historial de estados de anuncios de donación ; 3.Se genera una calificación para el usuario que acepta ; 4. Se actualiza información de los KPIs ; 5. Se direcciona al usuario a la funcionalidad de "programar recogida de donación". 
 Actualización de la información del encabezado de donación ( eatc_dona_headers ) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Al aceptar un anuncio de donación se debe actualizar la siguiente información: 
 eatc-state: debe cambiar de "announced" a "awarded". 
 eatc-adjudication_datetime:   Fecha y hora de la adjudicación del anuncio de donación.  El sistema toma la fecha y hora del momento en que se oprime el botón y la registra en el campo respectivo. 
 eatc-donation_manager_user_doc_id: documento de identidad (cédula) del usuario que aceptó la donación 
 eatc-donation_manager_code: código del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-donation_manager_name: nombre del gestor de donaciones al cual se le adjudica el anuncio. 
 eatc-donation_manager_address: dirección del gestor de donaciones al cual se le adjudica el anuncio. 
 eatc-donation_manager_phone : teléfono del gestor de donaciones al cual se le adjudica el anuncio. 
 eatc-donation_manager_typology_a: primera tipología del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-donation_manager_typology_b: segunda tipología del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-donation_manager_typology_c: tercera tipología del gestor de donaciones al cual se le adjudica el anuncio 

 Escritura con la API ***REVISAR dinamismo a partir de _DOM.cua_master***:  

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= awarded & eatc-adjudication_datetime ={{ DATETIME}} & eatc-donation_manager_user_doc_id= {{VALOR}}& eatc-donation_manager_code= {{VALOR}}& eatc-donation_manager_name= {{VALOR}}& eatc-donation_manager_address= {{VALOR}}& eatc-donation_manager_phone= {{VALOR}}& eatc-donation_manager_typology_a= {{VALOR}}& eatc-donation_manager_typology_b= {{VALOR}}& eatc-donation_manager_typology_c= {{VALOR}}& WHEREeatc-code= {{VALOR}} 

 Ejemplo _DOM.cua_master=abaco, entorno pruebas (suponiendo que el anuncio ha pasado todas las validaciones previas): 

 El servicio fue invocado de la siguiente manera 

 Dado que se tienen los siguientes datos: 

 eatc-donation_manager_user_doc_id= 8161174 (que corresponde a numero_cedula ) 
 eatc-donation_manager_code= 900326456-1 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_name= ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA (que corresponde a eatc_donation_managers. organizacin) 
 eatc-donation_manager_address= Cll. 19 A Nº 32 - 50 Barrio Cundinamarca (que corresponde a eatc_donation_managers. unidad_territorial) 
 eatc-donation_manager_phone= 4029305 (que corresponde a eatc_donation_managers. telefono1) 
 [***NUEVO***] Corrección para tomar la tipología A 
 eatc-donation_manager_typology_a= corresponde a {{eatc_donation_managers. organizacion_vinculada}} 
 [***NUEVO***] Corrección para tomar la tipología B real 
 eatc-donation_manager_typology_b= corresponde a {{eatc_donation_managers. eatc_doma_typology_b}} 
 [***NUEVO***] Corrección para tomar la tipología C 
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

 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Registro del estado "annouced" :  
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code ={{valor}}& eatc-state = annouced & eatc-date_time ={{datetime}}& eatc-log =EatCloud 

 Registro del estado "awarded" :  
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code ={{valor}}& eatc-state = awarded & eatc-date_time ={{datetime}}& eatc-log = eatc-donation_manager_code: {{valor}} eatc-donation_manager_user_doc_id: {{valor}} 

 Dado que esta tabla no se actualiza cuando se publica un estado de donación, en este punto se debe realizar un doble registro, primero con la fecha de publicación (estado "announced") y luego con la fecha de adjudicación (estado "awarded"). 
 Para el registro de estado "announced" se toma la fecha de publicación del anuncio y en el log se coloca "EatCloud" (dado que es la plataforma quien creó este estado en dicha fecha). 
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

 ***REVISIÓN CALIFICACIÓN***Registro de la calificación por aceptar un anuncio de donación ( _id=1 ) 
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

 Nota sobre el cálculo de puntos acumulados "acumulated_points" : el sistema busca la última calificación registrada para el gestor de donaciones respectivo   
 ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).  Definiendo el último registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificación (10) . 

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

 Actualización de información de KPIs 
 Se deberán realizar los registros en la estructura eatc_dona_kpi correspondientes a las transformaciones al adjudicar el anuncio (ver documentación vinculada). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faceptaci%C3%B3n-anuncio-de-donaci%C3%B3n-eatc_dona_acc%2F1009195450-9-aceptar-donacion--eatc_dona_acc-.png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faceptaci%C3%B3n-anuncio-de-donaci%C3%B3n-eatc_dona_acc%2F1009195450-9-aceptar-donacion--eatc_dona_acc-.png&ow=750&oh=1334 

 540.000000000000 

 ACEPTACIÓN ANUNCIO DE DONACIÓN (EATC_DONA_ACC)