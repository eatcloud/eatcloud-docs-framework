# abortar-anuncio-de-donación-eatc_dona_abort.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Sobre la leyenda: 
 Se debe incorporar sin el anglicismo "Score": "Recuerda que la cancelación de esta donación afectará tu puntaje EatCloud.  Te recomendamos no hacerlo" 

 Botón "confirmar cancelación": 
 El botón debe realizar tres acciones primordialmente: quitar los datos de asignación, hacer un registro en el historial de estados, y realizar el registro de calificación. 

 Quitar datos de asignación ***REVISAR dinamismo a partir de _DOM.cua_master***: 
 Para que sea consistente debe haberse llevado a cabo anteriormente este ejemplo .  El sistema debe quitar los siguientes datos del encabezado de donación respectivo: 

 eatc-state 
 eatc-adjudication_datetime 
 eatc-donation_manager_user_doc_id 
 eatc-donation_manager_code 
 eatc-donation_manager_name 
 eatc-donation_manager_address 
 eatc-donation_manager_phone 
 eatc-donation_manager_typology_a 
 eatc-donation_manager_typology_b 
 eatc-donation_manager_typology_c 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= announced &eatc-adjudication_datetime = 0& eatc-donation_manager_user_doc_id=0 & eatc-donation_manager_code= 0& eatc-donation_manager_name= 0& eatc-donation_manager_address= 0& eatc-donation_manager_phone= 0& eatc-donation_manager_typology_a= 0& eatc-donation_manager_typology_b= 0& eatc-donation_manager_typology_c= 0& WHEREeatc-code={{ VALOR}} 

 Ejemplo _DOM. cua_master=abaco : 

 Para el anuncio de donación cuyo eatc-code = 2019209714 , El usuario El usuario Juan Carlos Buitrago (numero_cedula = 8161174) que tiene como organización el dato: 900326456-1 ( https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 ) oprime el botón "Confirmar cancelación" a las 21:00:00 del día 2019-09-23.   

 Por lo tanto se debe realizar el siguiente registro: https://donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= announced & eatc-adjudication_datetime = 0& eatc-donation_manager_user_doc_id=0 & eatc-donation_manager_code= 0& eatc-donation_manager_name= 0& eatc-donation_manager_address= 0& eatc-donation_manager_phone= 0& eatc-donation_manager_typology_a= 0& eatc-donation_manager_typology_b= 0& eatc-donation_manager_typology_c= 0& WHEREeatc-code= 2019209714 

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
 Como el anuncio cambió de "awarded" a "announced", en el registro de historial de estado se debe registrar dicho cambio 

 Para el registro de estado "announced" se toma la fecha en la que se oprimió el botón de " Confirmar cancelación" y en el log se coloca los datos de quien realizó dicha cancelación (el eatc-donation_manager_code y el eatc-donation_manager_user_doc_id incluyendo la declaración de los campos) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code ={{valor}}& eatc-state = annouced & eatc-date_time ={{datetime}}& eatc-log =ABORTADA eatc-donation_manager_code: {{valor}}%20 eatc-donation_manager_user_doc_id: {{valor}} 

 Ejemplo: 

 Para el anuncio de donación cuyo eatc-id: 8687012 (eatc-code=2019209714) del ejemplo anterior, dado que el usuario en cuestión oprime el botón "Confirmar cancelación" a las 21:00:00 del día 2019-09-23, utilizando el API se realiza el siguiente registro: 

 Registro del estado "annouced" (dada la cancelación que hizo el usuario) :  

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code =2019209714& eatc-state = annouced & eatc-date_time =2019-09-23%2021:00:00& eatc-log =ABORTADA eatc-donation_manager_code: 900326456-1%20 eatc-donation_manager_user_doc_id: 8161174 

 Para consultar los estados registrados: https://donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=2019209714 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190925155221", 
 op : true, 
 cont : 1, 
 last : "5", 
 mem : 0.72, 
 time : “00:00:15” 
 } 

 ***REVISIÓN CALIFICACIÓN*** Registro de la calificación por abortar un anuncio de donación ( _id=4 ) 
 Cuando se presiona el botón " Confirmar cancelación ", el sistema debe realizar un registro de calificación de la siguiente manera: 

 _id : identificador único generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evaluó la calificación. 
 doma_id : Corresponde al código del gestor de donaciones " eatc_dona_headers.eatc-donation_manager_code". 
 eatc-dona_id : identificador del anuncio de donación " eatc_dona_headers. eatc-id". 
 action_id : corresponde al identificador de la regla de calificación " eatc_doma_qualification_rules._id". 
 points : corresponde a los puntos de la regla de calificación " eatc_doma_qualification_rules.points". 
 acumulated_points : el sistema debe establecer cual fue el último registro realizado para el gestor de donación y sobre el mismo, se toma el dato "acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donación cuyo eatc-id: 8687012 (eatc-code=2019209714) del ejemplo anterior, dado que el usuario en cuestión oprime el botón "Confirmar cancelación" a las 21:00:00 del día 2019-09-23, utilizando el API se realiza el siguiente registro: 

 El registro resultante sería: 

 _id : "#####", 
 date_time : "2019-09-23 21:00:00", 
 doma_id : "900326456-1", 
 eatc-dona_id : "8687012", 
 action_id : "4", 
 points : "-20", 
 acumulated_points : "cálculo de puntos acumulados" 

 Nota sobre el cálculo de puntos acumulados "acumulated_points" : el sistema busca la última calificación registrada para el gestor de donaciones respectivo ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).  Definiendo el último registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificación (-20) . 

 Escritura con la API:  
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time = 2019-09-23%2021:00:00 & doma_id = 900326456-1 & eatc-dona_id = 8687012 & action_id =4& points =-20& acumulated_points = cálculo%20de%20puntos%20acumulados 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 

 { 
 ts : "190925161942", 
 op : true, 
 cont : 1, 
 last : "13", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aquí se puede consultar el registro realizado: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=4&eatc-dona_id=8687012   

 Vínculo "No cancelar": 
 Este vínculo retorna a la anterior vista sin realizar ninguna operación. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fabortar-anuncio-de-donaci%C3%B3n-eatc_dona_abort%2F1474777002-10.2-no-interesado-aborta--eatc_dona_abort-.png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fabortar-anuncio-de-donaci%C3%B3n-eatc_dona_abort%2F1474777002-10.2-no-interesado-aborta--eatc_dona_abort-.png&ow=750&oh=1334 
 EatCloud Beneficiarios 

 544.000000000000 

 DEPRECADO: ABORTAR ANUNCIO DE DONACIÓN (EATC_DONA_ABORT)