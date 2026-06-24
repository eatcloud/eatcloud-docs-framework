# calificaciones_1.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En este apartado se documentarn procesos tcnicos necesarios para otorgar puntajes a los gestores de donaciones y a los puntos de donacin a partir de su participacin en la plataforma EatCloud. 

 Se definieron, popularon y cargaron las estructuras para definir las reglas de calificacin: 

 Beneficiarios: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_rules?id=_* 
 Donantes: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_rules?id=_* 

 Se definieron las estructuras de registro de calificacin y se cargaron datos de prueba: 
 Beneficiarios:  https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* 
 Donantes: cuenta devexito https://donantes.eatcloud.info/api/devexito/eatc_pods_qualification_registry?_id=_*   (se podran consolidar aqu https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* la informacin de las diversas cuentas)  

 Se deber documentar en cada mdulo funcional implicado en las calificaciones (Beneficiarios: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_rules?maker=app , Donantes: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_rules?maker=app ) y luego en esta seccin documentar los procesos que generan calificaciones Beneficiarios: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_rules?maker=process   , Donantes: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_rules?maker=process ). 

 PROCESOS PARA GENERAR DATOS DE CALIFICACIONES 

 Calificaciones para gestores de donaciones (beneficiarios): 

 No programar la recogida de la donacin antes del tiempo estipulado ( _id=3 ) 
 Cuando despus de 24 horas contadas a partir del dato eatc-publication_datetime del eatc_dona_headers asignado al gestor de donaciones, no se ha realizado un registro en eatc-scheduling_datetime". 

 El sistema debe realizar un registro en la estructura respectiva de la siguiente manera (evaluando previamente que no exista un registro de esta regla para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 doma_id : Corresponde al cdigo del gestor de donaciones " eatc_dona_headers.eatc-donation_manager_code". 
 eatc-dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id". 
 action_id : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato "acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-id" es 7608059 , que tiene un " eatc-publication_datetime " = 2019-09-18 15:37:54; el proceso para la generacin de calificaciones corre el 2019-09-19 14:00:00 (ms de 24 horas despus de la fecha de publicacin), como en ese momento no encuentra dato registrado en eatc-scheduling_datetime ", se debe aplicar la regla de procesamiento _id=3 y registrar en el respectivo registro de calificaciones ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-19 14:00:00", 
 doma_id : "900326456-1", 
 eatc-dona_id : " 7608059 ", 
 action_id : "3", 
 points : "-15", 
 acumulated_points : "-15" 

 Nota sobre el clculo de " acumulated_points ": el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).  Definiendo el ltimo registro ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=3 ,) toma el dato "acumulated_points = 0" y le suma los puntos que obtuvo para obtener acumulated_points : "-15". 

 Escritura con la API:  
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time =[valor]& doma_id =[valor]& eatc-dona_id =[valor]& action_id =[valor]& points =[valor]& acumulated_points =[valor] 

 Ejemplo: 
 Para el ejemplo anteriormente descrito la escritura sera as 

 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time = 2019-09-19%2014:00:00 & doma_id = 900326456-1 & eatc-dona_id = 7608059 & action_id =3& points =-15& acumulated_points =-15 

 Aqu se puede consultar el registro realizado: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=3&eatc-dona_id=7608059 

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para este identificador de regla, este identificador de "anuncio ( eatc-dona_id )" y este doma_id , antes de volver a aplicarlo (es decir, solo se puede calificar una vez esta regla): 

 Ejemplo: 
 El proceso vuelve a correr a la hora " 2019-09-19 15:00:00", entonces antes de correr o realizar un registro de calificacin debe evaluar si hay un registro previo correspondiente a esa regla y a ese anuncio de donacin ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=3&eatc-dona_id=7608059 ). Como para efectos del ejemplo, el registro existe, no debe registrar una nueva calificacin para esa regla  

 Llegar a tiempo a la recogida de la donacin ( _id=5 ) 
 Cuando el tiempo eatc-picking_checkin_datetime es igual o menor a eatc-programed_picking_datetime . (en el encabezado de anuncio de donacin) 

 El sistema debe realizar un registro en la estructura respectiva de la siguiente manera (evaluando previamente que no exista un registro de esta regla para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 doma_id : Corresponde al cdigo del gestor de donaciones " eatc_dona_headers.eatc-donation_manager_code ". 
 eatc-dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id ". 
 action_id : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato " acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo " eatc-code=40717 ", que tiene un " eatc-picking_checkin_datetime " = 2019-09-19 01:35:54  que es una fecha menor a la registrada en eatc-programed_picking_datetime : (2019-09-19 01:37:54) el proceso para la generacin de calificaciones corre el 2019-09-19 02:00:00 , se debe aplicar la regla de procesamiento _id=5 y registrar en el respectivo registro de calificaciones ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-19 02:00:00", 
 doma_id : "900326456-1", 
 eatc-dona_id : "5252095", 
 action_id : "5", 
 points : "10", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones o beneficiario respectivo ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id= 900326456-1 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (10) . 

 Escritura con la API:  
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &_operacion=insert& date_time = 2019-09-19%2002:00:00 & doma_id = 900326456-1 & eatc-dona_id = 5252095 & action_id =5& points =10& acumulated_points = clculo%20de%20puntos%20acumulados   

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

 Aqu se puede consultar el registro realizado: https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=5&eatc-dona_id=5252095          

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para este identificador de regla, este identificador de "anuncio ( eatc-dona_id )" y este doma_id , antes de volver a aplicarlo (es decir, solo se puede calificar una vez esta regla): 

 Ejemplo: 
 El proceso vuelve a correr a la hora " 2019-09-19 03:00:00", entonces antes de correr o realizar un registro de calificacin debe evaluar si hay un registro previo correspondiente a esa regla y a ese anuncio de donacin ( https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=5&eatc-dona_id=5252095 ).Como para efectos del ejemplo, el registro existe, no debe registrar una nueva calificacin para esa regla  

 Retrasarse en la recogida ( _id=6,7,8,9 ) 
 El sistema debe evaluar las diferencias entre las fechas eatc-picking_checkin_datetime y eatc-programed_picking_datetime que se van generando en los encabezados de donacin (eatc_dona_headers) y de acuerdo a las diferencias se debern las reglas de calificacin correspondientes a dichos retrasos: 

 Cuando el tiempo eatc-picking_checkin_datetime es mayor hasta por 10 minutos a eatc-programed_picking_datetime aplica la regla _id=6 
 Cuando el tiempo eatc-picking_checkin_datetime es  entre 10 y 20 minutos mayor a eatc-programed_picking_datetime aplica la regla _id=7 
 Cuando el tiempo eatc-picking_checkin_datetime es entre 20 y 30 minutos mayor a eatc-programed_picking_datetime aplica la regla _id=8 
 Cuando el tiempo eatc-picking_checkin_datetime es imayor por ms de 30 minutos a eatc-programed_picking_datetime aplica la regla _id=9 

 La escritura y validaciones previas deben funcionar tal como se explic en los ejemplos anteriores. 

 No recoger un anuncio de donacin en el rango de tiempo mximo estipulado ( _id=10 ) 
 Cuando despus de 24 horas contadas a partir del dato eatc-publication_datetime del eatc_dona_headers asignado al gestor de donaciones, no se ha realizado un registro en eatc-picking_checkin_datetime 

 La escritura y validaciones previas deben funcionar tal como se explic en los ejemplos anteriores. 

 Calificaciones para puntos de donacin (donantes): 

 Que el chequeo de la donacin resulte adecuado ( _id=3 ) 
 Cuando un  encabezado de donacin ( eatc_dona_headers ) se le estampa el dato eatc-picking_checkout_datetime y su respecivo detalle  (eatc_dona) no posee ningn item con registro en eatc-odd_state que contenga la palabra rechazado 

 El sistema debe realizar un registro en la estructura respectiva de la siguiente manera (evaluando previamente que no exista un registro de esta regla para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id : Corresponde al cdigo del gestor de donaciones " eatc_dona_headers.eatc-pod_id ". 
 dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id". 
 action : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato " acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo eatc-code = 2019209714 ( eatc-id=8687012 y cuyo detalle eatc_dona se consulta aqu ) ; el proceso para la generacin de calificaciones corre el 2019-09-19 10:00:00 como encuentra un dato registrado en eatc-picking_checkout_datetime ", verifica su respectivo detalle y dado que no encuentra en el dato eatc-odd_rejection_cause de todos los registros datos consignados debe aplicar la regla de calificacin _id=3 y registrar en el respectivo registro de calificaciones ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-19 10:00:00", 
 pod_id : "31", 
 dona_id : " 8687012 ", 
 action : "3", 
 points : "10", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones o beneficiario respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id= 31 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (10) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-19%2010:00:00 & pod_id = 31 & dona_id = 8687012 & action =3& points =10& acumulated_points = clculo%20de%20puntos%20acumulados 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=3&dona_id= 8687012   

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para este identificador de regla, este identificador de "anuncio ( dona_id )" y este pod_id , antes de volver a aplicarlo (es decir, solo se puede calificar una vez esta regla): 

 Ejemplo: 
 El proceso vuelve a correr a la hora " 2019-09-19 11:00:00", entonces antes de correr o realizar un registro de calificacin debe evaluar si hay un registro previo correspondiente a esa regla y a ese anuncio de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=3&dona_id= 8687012 ).Como para efectos del ejemplo, el registro existe, no debe registrar una nueva calificacin para esa regla  

 Que la validacin de la donacin sea exitosa ( _id=4 ) 
 Cuando un  encabezado de donacin ( eatc_dona_headers ) tiene estado "recibido" ( eatc-state= received ) y su respecivo detalle  (eatc_dona) no posee ningn item con registro en eatc-odd_state que contenga la palabra rechazado 

 El sistema debe realizar un registro en la estructura respectiva de la siguiente manera (evaluando previamente que no exista un registro de esta regla para el mismo anuncio de donacin, como se explicar ms adelante): 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id : Corresponde al cdigo del gestor de donaciones " eatc_dona_headers.eatc-pod_id ". 
 dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id". 
 action : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato " acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo eatc-code=2019321188 ( eatc-id= 5786547 y cuyo detalle eatc_dona se consulta aqu ) ; el proceso para la generacin de calificaciones corre el 2019-09-19 11:00:00 como encuentra que el anuncio de donacin tiene estado "recibido" ( eatc-state=received ), verifica su respectivo detalle y dado que no encuentra en los datos consignados en eatc-odd_rejection_cause informacin consignada, debe aplicar la regla de calificacin _id=4 y registrar en el respectivo registro de calificaciones ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-19 11:00:00", 
 pod_id : "84", 
 dona_id : "5786547", 
 action : "4", 
 points : "20", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones o beneficiario respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id= 84 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (20) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-19%2011:00:00 & pod_id = 84 & dona_id = 5786547 & action =4& points =20& acumulated_points = clculo%20de%20puntos%20acumulados 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=4&dona_id=5786547     

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para este identificador de regla, este identificador de "anuncio ( dona_id )" y este pod_id , antes de volver a aplicarlo (es decir, solo se puede calificar una vez esta regla): 

 Ejemplo: 
 El proceso vuelve a correr a la hora " 2019-09-19 12:00:00", entonces antes de correr o realizar un registro de calificacin debe evaluar si hay un registro previo correspondiente a esa regla y a ese anuncio de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=4&dona_id=5786547 ).Como para efectos del ejemplo, el registro existe, no debe registrar una nueva calificacin para esa regla  

 Verificaciones con novedades ( _id=5,6,7,8 ) 
 Cuando un  encabezado de donacin ( eatc_dona_headers ) tiene estado "recibido" ( eatc-state= received ) y su respecivo detalle  (eatc_dona) no tienen registrados rechazos en (es decir que en los datos consignados en eatc-odd_state exista palabra rechazado 

 El sistema debe realizar un registro en la estructura respectiva de la siguiente manera (evaluando previamente que no exista un registro de esta regla para el mismo anuncio de donacin, como se explicar ms adelante): 

 Cuando en eatc_dona hay entre el 0,1 y el 5% de items  con registro en eatc-odd_state que contienen la palabra rechazado aplica la regla _id=5 
 Cuando en eatc_dona hay entre el 5,1 y el 10% de items  con registro en eatc-odd_state que contienen la palabra rechazado aplica la regla _id=6 
 Cuando en eatc_dona hay entre el 10,1 y el 15% de items  con registro en eatc-odd_state que contienen la palabra rechazado aplica la regla _id=7 
 Cuando en eatc_dona hay entre el 10,1 y el 15% de items  con registro en eatc-odd_state que contienen la palabra rechazado aplica la regla _id=8 

 Ejemplo: 

 Para el anuncio de donacin cuyo eatc-code = 40716 (eatc-id : 7608059 y cuyo detalle eatc_dona se consulta aqu ) el proceso para la generacin de calificaciones corre el 2019-09-19 11:00:00 como encuentra que el anuncio de donacin tiene estado "recibido" ( eatc-state=received ), verifica su respectivo detalle y encuentra que dos referencias tienen informacin consignada en eatc-odd_rejection_cause. Como estos 2 registros corresponden al 12,5% (2/16*100) del total de los detalles, se debe aplicar la regla _id=7 y registrar en el respectivo registro de calificaciones 
 ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=_* ) de la siguiente manera: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-09-19 11:00:00", 
 pod_id : "339", 
 dona_id : "7608059", 
 action : "7", 
 points : "-10", 
 acumulated_points : "Clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el gestor de donaciones o beneficiario respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id= 339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (-10) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-09-19%2011:00:00 & pod_id = 334 & dona_id = 7608059 & action =7& points =-10& acumulated_points = clculo%20de%20puntos%20acumulados 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=7&dona_id=7608059      

 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para este identificador de regla, este identificador de "anuncio ( dona_id )" y este pod_id , antes de volver a aplicarlo (es decir, solo se puede calificar una vez esta regla): 

 Ejemplo: 
 El proceso vuelve a correr a la hora " 2019-09-19 12:00:00", entonces antes de correr o realizar un registro de calificacin debe evaluar si hay un registro previo correspondiente a esa regla y a ese anuncio de donacin ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=4&dona_id=5786547 ).Como para efectos del ejemplo, el registro existe, no debe registrar una nueva calificacin para esa regla  

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CALIFICACIONES