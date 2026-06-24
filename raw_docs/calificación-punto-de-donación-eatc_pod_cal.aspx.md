# calificación-punto-de-donación-eatc_pod_cal.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Consulta de reglas ***NUEVO: reglas centralizadas en datagov*** 
 A partir de la calificacin para el punto de donacin (pod), se debe generar un registro de su calificacin siguiendo las reglas estipuladas para este fin: 

 **NUEVO: reglas centralizadas en datagov***  
 { https://datagov.eatcloud.info/api/eatcloud/eatc_pods_qualification_rules?maker=app&location=eatc_dona_cal    

 Tambin existen existirn reconocimientos que permitirn otorgar. 

 NOTA IMPORTANTE CON RESPECTO A LOS EJEMPLOS: algunos de los ejemplos entregados abajo no resultan lgicos de acuerdo a lo que debera ser un funcionamiento adecuado de la App (por cuestiones de temporalidad, redundancia, etc.), por lo tanto se deben tomar como indicaciones ilustrativas de como funcionan los registros y el llamado a las APIs 

 Calificaciones Positivas 

 Mxima calificacin positiva ( _id=9 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id : Corresponde al cdigo del punto de donacin " eatc_dona_headers.eatc-pod_id" . 
 dona_id : identificador del anuncio de donacin " eatc_dona_headers.eatc-id ". 
 action : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato "acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , el beneficiario entreg la mxima calificacin al punto de donacin (donate), Por este motivo se debe aplicar la regla de procesamiento _id=9 y registrar en el respectivo registro de calificaciones ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 

 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 

 *** 

 eatc-dona_id : " 7608059 ", 
 action : "9", 
 points : "20", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (20) . 

 Se incorpora en el registro de calificaciones el parmetro eatc_cua_origin ***Revisar dinamismo a partir de _DOM.cua_master*** 

 Escritura con la API: (insumo para hacer esto: https://app.asana.com/0/698639369029630/1164988456082561 ) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }} ?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc-dona_id ={{valor}}& action ={{valor}}& points ={{valor}}& acumulated_points ={{valor}}& eatc_cua_origin= {{valor}} 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo: 
 Para el ejemplo anteriormente descrito la escritura sera as 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339& dona_id = 7608059 & action =9& points =20& acumulated_points = clculo%20de%20puntos%20acumulados & eatc_cua_origin=exito 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=9&eatc-dona_id=7608059    

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id: 9,10,11,12,13 ) , este identificador de "anuncio ( eatc-dona_id )" y este punto de donacin (pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio): 

 Ejemplo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id= 339) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y este punto de donacin  
 ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action_id=9,10,11,12,13& dona_id =7608059& pod_id= 339 ).Como para efectos del ejemplo, ya existe un registro, no debe registrar una nueva calificacin para esa regla. 

 Segunda mxima calificacin positiva ( _id=10 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id : Corresponde al cdigo del punto de donacin " eatc_dona_headers.eatc-pod_id" . 
 dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id ". 
 action : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato "acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , el gestor de donaciones o beneficiario entreg la segunda mxima calificacin al punto de donacin (donante), Por este motivo se debe aplicar la regla de procesamiento _id=10 y registrar en el respectivo registro de calificaciones ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 

 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 

 *** 

 dona_id : " 7608059 ", 
 action : "10", 
 points : "10", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (10) . 

 Se incorpora en el registro de calificaciones el parmetro eatc_cua_origin ***Revisar dinamismo a partir de _DOM.cua_master*** 

 Escritura con la API: (insumo para hacer esto: https://app.asana.com/0/698639369029630/1164988456082561 ) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }} ?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time =[valor]& pod_id =[valor]& eatc-dona_id =[valor]& action =[valor]& points =[valor]& acumulated_points =[valor]& eatc_cua_origin=[**NUEVO**valor] 

 Ejemplo _DOM. cua_master=abaco, ambiente productivo: 

 Para el ejemplo anteriormente descrito la escritura sera as 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339& dona_id = 7608059 & action =10& points =10& acumulated_points = clculo%20de%20puntos%20acumulados & eatc_cua_origin=exito 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=10&dona_id=7608059     

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id: 9,10,11,12,13 ) , este identificador de "anuncio ( dona_id )" y este punto de donacin (pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio): 

 Ejemplo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id= 339) bajo este anuncio ( dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y este punto de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action_id=9,10,11,12,13& dona_id =7608059& pod_id= 339 ).Como para efectos del ejemplo, ya existen registros, no debe registrar una nueva calificacin para esa regla. 

 Calificacin neutra ( _id=11 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante): 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , el gestor de donaciones o beneficiario entreg la calificacin neutra al punto de donacin (donante), Por este motivo se debe aplicar la regla de procesamiento _id=11 y registrar la respectiva calificacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 
 eatc-dona_id : " 7608059 ", 
 action : "11", 
 points : "2", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (2) . 

 Se incorpora en el registro de calificaciones el parmetro eatc_cua_origin ***Revisar dinamismo a partir de _DOM.cua_master*** 

 Escritura con la API: (insumo para hacer esto: https://app.asana.com/0/698639369029630/1164988456082561 ) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }} /?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc-dona_id ={{valor}}& action ={{valor}}& points ={{valor}}& acumulated_points ={{valor}}& eatc_cua_origin= {{valor}} 

 Ejemplo, _DOM. cua_master, ambiente productivo: 

 Para el ejemplo anteriormente descrito la escritura sera as 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339& dona_id = 7608059 & action =11& points =2& acumulated_points = clculo%20de%20puntos%20acumulados & eatc_cua_origin=exito 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=11&eatc-dona_id=7608059     

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id: 9,10,11,12,13 ) , este identificador de "anuncio ( dona_id )" y este punto de donacin (pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio): 

 Ejemplo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id= 339) bajo este anuncio ( dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y este punto de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action_id=9,10,11,12,13& dona_id =7608059& pod_id= 339 ).Como para efectos del ejemplo, ya existe un registro, no debe registrar una nueva calificacin para esa regla. 

 Calificaciones Negativas 

 Mnima calificacin negativa ( _id=12 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante): 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , el gestor de donacin o beneficiario entreg la mnima calificacin negativa al punto de donacin (donante), Por este motivo se debe aplicar la regla de procesamiento _id=12 y registrar la respectiva calificacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 
 eatc-dona_id : " 7608059 ", 
 action : "12", 
 points : "-10", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (-10) . 

 Se incorpora en el registro de calificaciones el parmetro eatc_cua_origin ***REVISAR dinamismo a partir de _DOM.cua_master*** 

 Escritura con la API: (insumo para hacer esto: https://app.asana.com/0/698639369029630/1164988456082561 ) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }} /?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time ={{valor}} pod_id ={{valor}}& eatc-dona_id ={{valor}}& action ={{valor}}& points ={{valor}}& acumulated_points ={{valor}}& eatc_cua_origin= {{valor}} 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo: 
 Para el ejemplo anteriormente descrito la escritura sera as 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339& dona_id = 7608059 & action =12& points =-10& acumulated_points = clculo%20de%20puntos%20acumulados 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=12&dona_id=7608059    

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id: 9,10,11,12,13 ) , este identificador de "anuncio ( dona_id )" y este punto de donacin (pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio): 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id= 339) bajo este anuncio ( dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y este punto de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action_id=9,10,11,12,13& dona_id =7608059& pod_id= 339 ).Como para efectos del ejemplo, ya existe un registro, no debe registrar una nueva calificacin para esa regla. 

 Mxima calificacin negativa ( _id=13 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante): 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , el gestor de donaciones (beneficiario) entreg la mxima calificacin negativa al punto de donacin (donante), Por este motivo se debe aplicar la regla de procesamiento _id=13 y registrar la respectiva calificacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 
 dona_id : " 7608059 ", 
 action : "13", 
 points : "-20", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (-20) . 

 Se incorpora en el registro de calificaciones el parmetro eatc_cua_origin ***REVISAR dinamismo a paritir de _DOM.cua_master*** 

 Escritura con la API: (insumo para hacer esto: https://app.asana.com/0/698639369029630/1164988456082561 ) 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }} ?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc-dona_id ={{valor}}& action ={{valor}}& points ={{valor}}& acumulated_points ={{valor}}& eatc_cua_origin= {{valor}} 

 Ejemplo, _DOM. cua_master=abaco, ambiente productivo:  

 Para el ejemplo anteriormente descrito la escritura sera as 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339& dona_id = 7608059 & action =13& points =-20& acumulated_points = clculo%20de%20puntos%20acumulados   

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=13&dona_id=7608059   

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id: 9,10,11,12,13 ) , este identificador de "anuncio ( dona_id )" y este punto de donacin (pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio): 
 Ejemplo, _DOM. cua_master= abaco, ambiente productivo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id= 339) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este punto de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action_id=9,10,11,12,13& dona_id =7608059& pod_id= 339 ).Como para efectos del ejemplo, ya existe un registro, no debe registrar una nueva calificacin para esa regla. 

 Reconocimientos (tags) ***NUEVO: internacionalizacin, centralizacin en datagov y dinamismo a partir de _DOM.cua_master*** 

 El sistema debe realizar las siguientes consultas para realizar el despliegue de los tags de calificacin, segn el idioma: 

 NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 

 NUEVO: Paso 2: consulta de los tags positivos para calificacin de beneficiarios 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_calification_tags?sujeto_calificacion=pods&tipo_calificacion=positiva     
 (anteriormente: https://beneficiarios.eatcloud.info/api/abaco/eatc_calification_tags?sujeto_calificacion=pods&tipo_calificacion=positiva) 

 El sistema recolecta los _id de los registros obtenidos ( array_ids_recolectados ) para realizar la siguiente consulta. 

 NUEVO: Paso 2: consulta de los tags internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&eatc_language={{ codigo_dos_digitos_idioma }}&eatc_data_id={{ array_ids_recolectados }} 

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&eatc_language=en&eatc_data_id={{ array_ids_recolectados }}  

 El sistema toma los valores consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en el selector y llevarlos al registro junto con la clave consignada en " eatc_internationalize_dt. eatc_data_id " .  Cuando el usuario realiza una seleccin mltiple en el selector internacionalizado, el sistema toma los pares "clave ( eatc_data_id ), valor ( eatc_int_data )" para realizar  el registro del reconocimiento utilizando el siguiente servicio: 

 ***NUEVO: dinamismo a partir de _DOM. cua_master y adicin del campo tag_id*** 

 {URL_entorno_donantes}} /crd/ {{_DOM.cua_master}} /?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc_cua_origin={{ eatc_dona_header. eatc_cua_origin}} & eatc-dona_id ={{valor}}& tag ={{ eatc_internationalize_dt. eatc_int_data }}& tag_id={{ eatc_internationalize_dt. eatc_data_id}} & type =positiva 

 *** 
 Ejemplo, _DOM.cua_master=abaco, entorno productivo **EL EJEMPLO A CONTINUACIN NO SE REVIS CON RESPECTO A LAS NUEVAS DISPOSICIONES, POR LO TANTO EST DESACTUALIZADO**:: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , cuando se registr su recogida, el Donante entreg una calificacin positiva al gestor de donaciones, Por este motivo el sistema despleg los tags de reconocimiento (aplicables a los puntos de donacin o pods) y el usuario seleccion los 3 tags disponibles, por lo tanto se debern realizar tres registros (uno por tag entregado) en la estructura para registro de tags de calificacin  ( https://donantes.eatcloud.info/api/abaco/eatc_pod_tag_registry?_id=_* ) de la siguiente manera: 

 Llamado crd para escritura de registro de tag ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time ={{valor}}& doma_id ={{valor}}& eatc-dona_id ={{valor}}& tag ={{valor}}& type =positivo 

 Los registros resultantes seran: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : "7608059", 
 tag : "Entrega completa y de producto apto en donacin", 
 type : "positivo" 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339 & eatc-dona_id = 7608059 & tag = Entrega%20completa%20y%20de%20producto%20apto%20en%20donacin & type =positivo 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : "7608059", 
 tag : "Puntualidad en la entrega de la donacin", 
 type : "positivo" 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339 & eatc-dona_id = 7608059 & tag = Puntualidad%20en%20la%20entrega%20de%20la%20donacin & type =positivo 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : "7608059", 
 tag : "Amabilidad de la persona que entrega la donacin", 
 type : "positivo" 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & pod_id = 339 & eatc-dona_id = 7608059 & tag = Amabilidad%20de%20la%20persona%20que%20entrega%20la%20donacin & type =positivo 

 La App debe validar que los registros se realicen, es decir que se obtengan respuestas de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar los registros realizados: https://donantes.eatcloud.info/api/abaco/eatc_pod_tag_registry?eatc-dona_id=7608059     

 Calificaciones a partir de los reconocimientos ( _id=14,15,16,17 ) 
 Aunque dados los tags actualmente registrados solo aplicaran las reglas de calificacin _id=14,15,16 , existe una regla adicional (que por el momento no se aplicara: _id=17 ) para cuando se configuren ms tags de calificacin. 

 El sistema debe definir cuantos reconocimientos se aplicaron y de esta manera aplicar las reglas de calificacin de la siguiente manera: 
 Si se entreg 1 reconocimiento, aplica la regla _id=14 (5 puntos) 
 Si se entregaron 2 reconocimientos, aplica la regla _id=15 (10 puntos) 
 Si se entregaron 2 reconocimientos, aplica la regla _id=16 (15 puntos) 

 Ejemplo: 

 Siguiendo el ejemplo anterior, como se entregaron 3 reconocimientos (aplicando la regla _id=16 )  para el anuncio de donacin cuyo " eatc-id" es 7608059 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-10-17 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : " 7608059 ", 
 action : "16", 
 points : "15", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (15) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-10-17%2007:07:07 & pod_id = 339 & dona_id = 7608059 & action =16& points =15& acumulated_points = clculo%20de%20puntos%20acumulados     

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "21", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=16&dona_id=7608059       

 Aspectos a mejorar (tags) ***NUEVO: internacionalizacin, centralizacin en datagov y dinamismo a partir de _DOM.cua_master*** 

 El sistema debe realizar las siguientes consultas para realizar el despliegue de los tags de calificacin, segn el idioma: 

 NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 

 NUEVO: Paso 2: consulta de los tags positivos para calificacin de beneficiarios 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_calification_tags?sujeto_calificacion=pods&tipo_calificacion=negativa      
 (anteriormente: https://beneficiarios.eatcloud.info/api/abaco/eatc_calification_tags?sujeto_calificacion=pods&tipo_calificacion=positiva) 

 El sistema recolecta los _id de los registros obtenidos ( array_ids_recolectados ) para realizar la siguiente consulta. 

 NUEVO: Paso 2: consulta de los tags internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&eatc_language={{ codigo_dos_digitos_idioma }}&eatc_data_id={{ array_ids_recolectados }} 

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&eatc_language=en&eatc_data_id={{ array_ids_recolectados }}  

 El sistema toma los valores consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en el selector y llevarlos al registro junto con la clave consignada en " eatc_internationalize_dt. eatc_data_id " .  Cuando el usuario realiza una seleccin mltiple en el selector internacionalizado, el sistema toma los pares "clave ( eatc_data_id ), valor ( eatc_int_data )" para realizar  el registro del reconocimiento utilizando el siguiente servicio: 

 ***NUEVO: dinamismo a partir de _DOM. cua_master y adicin del campo tag_id*** 

 {URL_entorno_donantes}} /crd/ {{_DOM.cua_master}} /?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc_cua_origin={{ eatc_dona_header. eatc_cua_origin}} & eatc-dona_id ={{valor}}& tag ={{ eatc_internationalize_dt. eatc_int_data }}& tag_id={{ eatc_internationalize_dt. eatc_data_id}} & type =negativa 

 *** 
 Ejemplo **EL EJEMPLO A CONTINUACIN NO SE REVIS CON RESPECTO A LAS NUEVAS DISPOSICIONES, POR LO TANTO EST DESACTUALIZADO**: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , cuando se verific su recogida, el beneficiario o gestor de donaciones entreg una calificacin negativa al punto de donacin o donante, Por este motivo el sistema despleg los tags de aspectos a mejorar (aplicables a los puntos de donacin o pods) y el usuario seleccion el tag "Tiempo de demora en la entrega", por lo tanto se deber realizar el siguiente registro en la estructura para registro de tags de calificacin  ( https://donantes.eatcloud.info/api/abaco/eatc_pod_tag_registry?_id=_* ) de la siguiente manera: 

 Llamado crd para escritura de registro de tag ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time ={{valor}}& pod_id ={{valor}}& eatc-dona_id ={{valor}}& tag ={{valor}}& type =negativo 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-10-17 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : "7608059", 
 tag : "Tiempo de demora en la entrega", 
 type : "negativo" 

 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pod_tag_registry &_operacion=insert& date_time = 2019-10-17%2007:07:07 & pod_id = 339 & eatc-dona_id = 7608059 & tag = Tiempo%20de%20demora%20en%20la%20entrega & type =negativo 

 La App debe validar que los registros se realicen, es decir que se obtengan respuestas de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "12", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar los regalizados: https://donantes.eatcloud.info/api/abaco/eatc_pod_tag_registry? pod_id=339&eatc-dona_id=7608059&type=negativo    

 Calificaciones a partir de los los aspectos por mejorar ( _id=18,19,20,21 ) 
 Aunque dados los tags actualmente registrados solo aplicaran las reglas de calificacin _id=18,19,20 , existe una regla adicional (que por el momento no se aplicara: _id=21 ) para cuando se configuren ms tags de calificacin. 

 El sistema debe definir cuantos reconocimientos se aplicaron y de esta manera aplicar las reglas de calificacin de la siguiente manera: 
 Si se entreg 1 aspecto a mejorar, aplica la regla _id=18 (-5 puntos) 
 Si se entregaron 2 reconocimientos, aplica la regla _id=19 (-10 puntos) 
 Si se entregaron 2 reconocimientos, aplica la regla _id=20 (-15 puntos) 

 Ejemplo: 

 Siguiendo el ejemplo anterior, como se seleccion un aspecto por mejorar (aplicando la regla _id=18 )  para el anuncio de donacin cuyo " eatc-id" es 7608059 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-10-17 07:07:07", 
 pod_id : "339", 

 ***NUEVO***: se incorpora en el registro de calificaciones el parmetro eatc_cua_origin 
 eatc_cua_origin: "exito" ( eatc_dona_header. eatc_cua_origin) 
 *** 
 eatc-dona_id : " 7608059 ", 
 action : "18", 
 points : "-5", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://donanes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (-5) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-10-17%2007:07:07 & pod_id = 339 & dona_id = 7608059 & action =18& points =-5& acumulated_points = clculo%20de%20puntos%20acumulados     

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925141807", 
 op : true, 
 cont : 1, 
 last : "21", 
 mem : 0.72, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=18&dona_id=7608059          

 ***REVISIN CALIFICACIN***[STANDBY: porque se  va a implementar mediante un proceso BO) Calificacin para el gestor de donaciones (beneficiario) por efectuar la calificacin ( _id=24 ) 
 Cuando un gestor de donaciones o beneficiario entrega calificacin a un punto de donacin, el sistema le entrega un puntaje (Regla _id=24 : como incentivo a la realizacin de calificaciones).  El sistema debe realizar un registro de calificacin de la siguiente manera: 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 doma_id : Corresponde al gestor de donaciones que realiz la calificacin " eatc_dona_headers.eatc-doma_id" . 
 eatc-dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id ". 
 action_id : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato " acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo eatc-dona_id es 7608059 del ejemplo anterior, dado que el usuario en cuestin realiz la calificacin a las 2019-09-20 07:07:07, utilizando el API se realiza el siguiente registro: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-20 07:07:07", 
 doma_id : "900326456-1", 
 eatc-dona_id : " 7608059 ", 
 action_id : "24", 
 points : "5", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones o beneficiario respectivo ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id= 900326456-1 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (5) . 

 Escritura con la API:  
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time = 2019-09-20%2007:07:07 & doma_id = 900326456-1 & eatc-dona_id = 7608059 & action_id =24& points =5& acumulated_points = clculo%20de%20puntos%20acumulados   

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "191001115829", 
 op : true, 
 cont : 1, 
 last : "9", 
 mem : 0.72, 
 time : "00:00:01" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=24&eatc-dona_id= 7608059        

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para la presente regla ( _id=24 ) , este identificador de "anuncio ( eatc-dona_id )" y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez al gestor de donaciones o beneficiario por entregarle calificacin a un punto de donacin o donante): 

 Ejemplo: 

 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( doma_id= 900326456-1) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=24& eatc-dona_id =7608059& doma_id= 900326456-1 ).Como para efectos del ejemplo, ya existe un registro, no debera registrar una nueva calificacin para esa regla. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=f80132d3d8ec4f2fac2c82cd6c9d6a9a&ext=png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=f80132d3d8ec4f2fac2c82cd6c9d6a9a&ext=png&ow=750&oh=1334 
 EatCloud Beneficiarios 

 560.000000000000 

 CALIFICACIN PUNTO DE DONACIN (EATC_POD_CAL) ***REVISIN CALIFICACIN***