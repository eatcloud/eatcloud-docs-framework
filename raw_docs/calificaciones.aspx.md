# calificaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 (PENDIENTE DOCUMENTACIN) 

 Registro de la calificacin por validar la llegada de un beneficiario ( _id=1 ) 
 Cuando se presiona el botn " Valida el cdigo "  el sistema debe realizar un registro de calificacin de la siguiente manera: 

 _id : identificador nico generado por el sistema, 
 date_time : corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id : Corresponde al punto de donacin " eatc_dona_headers.eatc-pod_id" . 
 eatc-dona_id : identificador del anuncio de donacin " eatc_dona_headers. eatc-id ". 
 action : corresponde al identificador de la regla de calificacin " eatc_doma_qualification_rules._id ". 
 points : corresponde a los puntos de la regla de calificacin " eatc_doma_qualification_rules.points ". 
 acumulated_points : el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato " acumulated_points " y le suma los puntos que obtuvo 

 Ejemplo: 

 Para el anuncio de donacin cuyo eatc-id: 5252095 ( eatc-code = 40717 ) del ejemplo anterior, dado que el usuario en cuestin oprime el botn " Valida el cdigo " a las 2019-11-01 10:10:00, utilizando el API se realiza el siguiente registro: 

 El registro resultante sera: 

 _id : "#####", 
 date_time : "2019-11-01 10:10:00", 
 pod_id : "339", 
 eatc-dona_id : "5252095", 
 action : "1", 
 points : "10", 
 acumulated_points : "clculo de puntos acumulados" 

 Nota sobre el clculo de puntos acumulados "acumulated_points" : el sistema busca la ltima calificacin registrada para el punto de donacin respectivo ( https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).  Definiendo el ltimo registro, toma el dato "acumulated_points" y le suma los puntos que obtuvo en esta calificacin (10) . 

 Escritura con la API:  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &_operacion=insert& date_time = 2019-11-01%2010:10:00 & pod_id = 339 & eatc-dona_id = 5252095 & action =1& points =10& acumulated_points = clculo%20de%20puntos%20acumulados   

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "191001115829", 
 op : true, 
 cont : 1, 
 last : "8", 
 mem : 0.72, 
 time : "00:00:01" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Aqu se puede consultar el registro realizado: https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=1&eatc-dona_id=5252095       

 El sistema debe validar que un nuevo registro para el mismo anuncio de donacin, no se realice de nuevo en un periodo de 10 minutos (esto con el nimo de no realizar mltiples calificaciones cuando hubo un error en el ingreso del cdigo por ejemplo). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CALIFICACIONES