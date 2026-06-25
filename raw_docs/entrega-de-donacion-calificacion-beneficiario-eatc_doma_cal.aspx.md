# entrega-de-donacion-calificacion-beneficiario-eatc_doma_cal.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO&#58; centralizada consulta en datagov*** 
 A partir de la calificacin para el gestor de donacines (beneficiario), se debe generar un registro de su calificacin siguiendo las reglas estipuladas para este fin. 
 NUEVO&#58; AHORA SE ALOJAN DE MANERA CENTRALIZADA EN DATAGOV&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_doma_qualification_rules?maker=app&amp;location=eatc_dona_cal &#160; 
 &#160; 
 Tambin existen existirn reconocimientos que permitirn otorgar. 
&#160; 
 El registro de la calificacin se realizar utilizando el siguiente llamado&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entono_beneficiarios&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time =&#123;&#123;valor&#125;&#125;&amp; doma_id =&#123;&#123;valor&#125;&#125;&amp; eatc-dona_id =&#123;&#123;valor&#125;&#125;&amp; action_id =&#123;&#123;valor&#125;&#125;&amp; points =&#123;&#123;valor&#125;&#125;&amp; acumulated_points =&#123;&#123;valor&#125;&#125; 
&#160; 
 NOTA IMPORTANTE CON RESPECTO A LOS EJEMPLOS&#58; algunos de los ejemplos entregados abajo no resultan lgicos de acuerdo a lo que debera ser un funcionamiento adecuado de la App, por lo tanto se deben tomar como indicaciones ilustrativas de como funcionan los registros y el llamado a las APIs 
&#160; 
 NOTA IMPORTANTE CON RESPECTO A LAS URLs DE LAS APIs&#58; La app maneja una variable DOM, en donde se almacena la primera parte de la URL (en donde se identifica si es ambiente de pruebas o productivo).&#160; Se debe utilizar esa variable para programar las peticiones a las APIs y las escrituras. 

 Calificaciones Positivas 

 Mxima calificacin positiva ( _id=11 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante)&#58; 
&#160; 
 _id &#58; identificador nico generado por el sistema, 
 date_time &#58; corresponde a la fecha y hora en la cual se evalu la calificacin. 
 doma_id &#58; Corresponde al cdigo del gestor de donaciones &quot; eatc_dona_headers.eatc-donation_manager_code&quot;. 
 eatc-dona_id &#58; identificador del anuncio de donacin &quot; eatc_dona_headers. eatc-id&quot;. 
 action_id &#58; corresponde al identificador de la regla de calificacin &quot; eatc_doma_qualification_rules._id&quot;. 
 points &#58; corresponde a los puntos de la regla de calificacin &quot; eatc_doma_qualification_rules.points&quot;. 
 acumulated_points &#58; el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato &quot;acumulated_points &quot; y le suma los puntos que obtuvo 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente de pruebas 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es cbb00e9c-0b17-11ea-914a-0018515a556c , cuando se registr su recogida, el Donante entreg la mxima calificacin al gestor de donaciones (beneficiario) a las 2019-09-26 09&#58;30&#58;00, Por este motivo se debe aplicar la regla de procesamiento _id=11 y registrar en el respectivo registro de calificaciones ( https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-26 09&#58;30&#58;00&quot;, 
 doma_id &#58; &quot;860007305-3&quot;, 
 eatc-dona_id &#58; &quot;cbb00e9c-0b17-11ea-914a-0018515a556c&quot;, 
 action_id &#58; &quot;11&quot;, 
 points &#58; &quot;20&quot;, 
 acumulated_points &#58; 
&#160; 
 Nota sobre el clculo de &quot;acumulated_points&quot;&#58; se generar un proceso BO, o en la APP para acumular estos puntos cuando se consulten, por lo tanto se puede dejar el registro vaco en en 0. 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time =[valor]&amp; doma_id =[valor]&amp; eatc-dona_id =[valor]&amp; action_id =[valor]&amp; points =[valor]&amp; acumulated_points =[valor] 
&#160; 
 Ejemplo&#58; 
 Para el ejemplo anteriormente descrito la escritura sera as&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-26%2009&#58;300&#58;00 &amp; doma_id = 860007305-3 &amp; eatc-dona_id = cbb00e9c-0b17-11ea-914a-0018515a556c &amp; action_id =11&amp; points =20&amp; acumulated_points =0 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11&amp;eatc-dona_id=cbb00e9c-0b17-11ea-914a-0018515a556c &#160; 
&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin ( _id&#58; 11,12,13,14,15 ) , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio)&#58; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este gestor de donacin ( doma_id= 860007305-3) bajo este anuncio ( eatc-dona_id =cbb00e9c-0b17-11ea-914a-0018515a556c) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin yt a este gestor ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11,12,13,14,15&amp;eatc-dona_id=cbb00e9c-0b17-11ea-914a-0018515a556c&amp;doma_id=860007305-3 ).Como para efectos del ejemplo, ya existe un registro, no debe registrar una nueva calificacin para esa regla. 

 Segunda mxima calificacin positiva ( _id=12 )&#160; 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante)&#58; 

&#160; 
 _id &#58; identificador nico generado por el sistema, 
 date_time &#58; corresponde a la fecha y hora en la cual se evalu la calificacin. 
 doma_id &#58; Corresponde al cdigo del gestor de donaciones &quot; eatc_dona_headers.eatc-donation_manager_code&quot;. 
 eatc-dona_id &#58; identificador del anuncio de donacin &quot; eatc_dona_headers. eatc-id&quot;. 
 action_id &#58; corresponde al identificador de la regla de calificacin &quot; eatc_doma_qualification_rules._id&quot;. 
 points &#58; corresponde a los puntos de la regla de calificacin &quot; eatc_doma_qualification_rules.points&quot;. 
 acumulated_points &#58; el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato &quot;acumulated_points &quot; y le suma los puntos que obtuvo 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente de productivo 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg la segunda mxima calificacin al gestor de donaciones (beneficiario), Por este motivo se debe aplicar la regla de procesamiento _id=12 y registrar en el respectivo registro de calificaciones ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-20 06&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;12&quot;, 
 points &#58; &quot;10&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (10) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-20%2006&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =12&amp; points =10&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=12&amp;eatc-dona_id=7608059 
 &#160;&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin&#160; ( _id&#58; 11,12,13,14,15 ) , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio)&#58; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este gestor de donacin ( doma_id= 900326456-1) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11,12,13,14,15&amp; eatc-dona_id =7608059&amp; doma_id= 900326456-1 ).Como para efectos del ejemplo, ya existen dos registros, no debe registrar una nueva calificacin para esa regla. 

 Calificacin neutra ( _id=13 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante)&#58; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg la calificacin neutra al gestor de donaciones (beneficiario), Por este motivo se debe aplicar la regla de procesamiento _id=13 y registrar en el respectivo registro de calificaciones ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-20 06&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;13&quot;, 
 points &#58; &quot;2&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (2) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-20%2006&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =13&amp; points =2&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=13&amp;eatc-dona_id=7608059 &#160;&#160;&#160; 
&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin&#160; ( _id&#58; 11,12,13,14,15 )&#160; , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio)&#58; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este gestor de donacin ( doma_id= 900326456-1) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11,12,13,14,15&amp; eatc-dona_id =7608059&amp; doma_id= 900326456-1 ).Como para efectos del ejemplo, ya existen varios registros, no debe registrar una nueva calificacin para esa regla. 

 Calificaciones Negativas 

 Mnima calificacin negativa ( _id=14 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante)&#58; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg la mnima calificacin negativa al gestor de donaciones (beneficiario), Por este motivo se debe aplicar la regla de procesamiento _id=14 y registrar en el respectivo registro de calificaciones ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-20 06&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;14&quot;, 
 points &#58; &quot;-10&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (-10) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-20%2006&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =14&amp; points =-10&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160;&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=14&amp;eatc-dona_id=7608059 &#160;&#160;&#160; 
&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin&#160; ( _id&#58; 11,12,13,14,15 )&#160; , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio)&#58; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este gestor de donacin ( doma_id= 900326456-1) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11,12,13,14,15&amp; eatc-dona_id =7608059&amp; doma_id= 900326456-1 ).Como para efectos del ejemplo, ya existen varios registros, no debe registrar una nueva calificacin para esa regla. 

 Mxima calificacin negativa ( _id=15 ) 
 Cuando se presiona el emoji respectivo, el sistema debe realizar un registro de calificacin de la siguiente manera (evaluando previamente que no exista un registro calificacin para el mismo anuncio de donacin, como se explicar ms adelante)&#58; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente de productivo 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg la mxima calificacin negativa al gestor de donaciones (beneficiario), Por este motivo se debe aplicar la regla de procesamiento _id=15 y registrar en el respectivo registro de calificaciones ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-20 06&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;15&quot;, 
 points &#58; &quot;-20&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (-20) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-20%2006&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =15&amp; points =-20&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=15&amp;eatc-dona_id=7608059 &#160;&#160;&#160;&#160; 
&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para las reglas respectivas a la calificacin&#160; ( _id&#58; 11,12,13,14,15 )&#160; , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este Gestor de Donaciones ( doma_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez un un gestor de donaciones por anuncio)&#58; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este gestor de donacin ( doma_id= 900326456-1) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=11,12,13,14,15&amp; eatc-dona_id =7608059&amp; doma_id= 900326456-1 ).Como para efectos del ejemplo, ya existen varios registros, no debe registrar una nueva calificacin para esa regla. 

 Reconocimientos (tags) ***NUEVO&#58; internacionalizacin, centralizacin en datagov y dinamismo a partir de _DOM.cua_master*** 

 El sistema debe realizar las siguientes consultas para realizar el despliegue de los tags de calificacin, segn el idioma&#58; 
&#160; 
 NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los tags positivos para calificacin de beneficiarios 
 https&#58;//datagov.eatcloud.info/api/ eatcloud /eatc_calification_tags?sujeto_calificacion=doma&amp;tipo_calificacion=positiva &#160;&#160; 
 (anteriormente&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_calification_tags?sujeto_calificacion=doma&amp;tipo_calificacion=positiva ) 
 El sistema recolecta los _id de los registros obtenidos ( array_ids_recolectados ) para realizar la siguiente consulta. 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los tags internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&amp;eatc_language=&#123;&#123; codigo_dos_digitos_idioma &#125;&#125;&amp;eatc_data_id=&#123;&#123; array_ids_recolectados &#125;&#125; 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&amp;eatc_language=en&amp;eatc_data_id=&#123;&#123; array_ids_recolectados &#125;&#125;&#160; 
&#160; 
 El sistema toma los valores consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en el selector y llevarlos al registro junto con la clave consignada en &quot; eatc_internationalize_dt. eatc_data_id &quot; .&#160; Cuando el usuario realiza una seleccin mltiple en el selector internacionalizado, el sistema toma los pares &quot;clave ( eatc_data_id ), valor ( eatc_int_data )&quot; para realizar&#160; el registro del reconocimiento utilizando el siguiente servicio&#58; 
 ***NUEVO&#58; dinamismo a partir de _DOM. cua_master y adicin del campo tag_id*** 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time =&#123;&#123;valor&#125;&#125;&amp; doma_id =&#123;&#123;valor&#125;&#125;&amp; eatc-dona_id =&#123;&#123;valor&#125;&#125;&amp; tag =&#123;&#123; eatc_internationalize_dt. eatc_int_data &#125;&#125;&amp; tag_id=&#123;&#123; eatc_internationalize_dt. eatc_data_id&#125;&#125; &amp; type =positiva 
&#160; 
 *** 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot;, entorno productivo **EL EJEMPLO A CONTINUACIN NO SE REVIS CON RESPECTO A LAS NUEVAS DISPOSICIONES, POR LO TANTO EST DESACTUALIZADO** 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg una calificacin positiva al gestor de donaciones, Por este motivo el sistema despleg los tags de reconocimiento (aplicables a los gestores de donaciones o doma) y el usuario seleccion los 3 tags disponibles, por lo tanto se debern realizar tres registros (uno por tag entregado) en la estructura para registro de tags de calificacin&#160; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_tag_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time =[valor]&amp; doma_id =[valor]&amp; eatc-dona_id =[valor]&amp; tag =[valor]&amp; type =positivo 
&#160; 
 Los registros resultantes seran&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot;7608059&quot;, 
 tag &#58; &quot;Presentacin personal&quot;, 
 type &#58; &quot;positivo&quot; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; tag = Presentacin%20personal &amp; type =positivo 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot;7608059&quot;, 
 tag &#58; &quot;Puntualidad en la recoleccin&quot;, 
 type &#58; &quot;positivo&quot; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; tag = Puntualidad%20en%20la%20recoleccin &amp; type =positivo 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot;7608059&quot;, 
 tag &#58; &quot;Amabilidad durante el proceso&quot;, 
 type &#58; &quot;positivo&quot; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; tag = Amabilidad%20durante%20el%20proceso &amp; type =positivo 
 La App debe validar que los registros se realicen, es decir que se obtengan respuestas de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
 Aqu se puede consultar los regalizados&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_tag_registry?eatc-dona_id=7608059 
&#160; 
 Calificaciones a partir de los reconocimientos ( _id=16,17,18,19 ) ***REVISIN CALIFICACIN*** 
 Aunque dados los tags actualmente registrados solo aplicaran las reglas de calificacin _id=16,17,18 , existe una regla adicional (que por el momento no se aplicara&#58; _id=19 ) para cuando se configuren ms tags de calificacin. 
 El sistema debe definir cuantos reconocimientos se aplicaron y de esta manera aplicar las reglas de calificacin de la siguiente manera&#58; 
 Si se entreg 1 reconocimiento, aplica la regla _id=16 (5 puntos) 
 Si se entregaron 2 reconocimientos, aplica la regla _id=17 (10 puntos) 

 Si se entregaron 3 reconocimientos, aplica la regla _id=18 (15 puntos) 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot;, entorno productivo 
&#160; 
 Siguiendo el ejemplo anterior, como se entregaron 3 reconocimientos (aplicando la regla id=18 )&#160; para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;18&quot;, 
 points &#58; &quot;15&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (15) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =18&amp; points =15&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;21&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=18&amp;eatc-dona_id=7608059 &#160;&#160;&#160;&#160;&#160; 

 Aspectos a mejorar (tags) ***NUEVO&#58; internacionalizacin, centralizacin en datagov y dinamismo a partir de _DOM.cua_master*** 

 El sistema debe realizar las siguientes consultas para realizar el despliegue de los tags de calificacin, segn el idioma&#58; 
&#160; 
 NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los tags positivos para calificacin de beneficiarios 
 https&#58;//datagov.eatcloud.info/api/ eatcloud /eatc_calification_tags?sujeto_calificacion=doma&amp;tipo_calificacion=negativa &#160;&#160; 
 (anteriormente&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_calification_tags?sujeto_calificacion=doma&amp;tipo_calificacion=positiva ) 
&#160; 
 El sistema recolecta los _id de los registros obtenidos ( array_ids_recolectados ) para realizar la siguiente consulta. 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los tags internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&amp;eatc_language=&#123;&#123; codigo_dos_digitos_idioma &#125;&#125;&amp;eatc_data_id=&#123;&#123; array_ids_recolectados &#125;&#125; 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_calification_tags&amp;eatc_language=en&amp;eatc_data_id=&#123;&#123; array_ids_recolectados &#125;&#125;&#160; 
&#160; 
 El sistema toma los valores consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en el selector y llevarlos al registro junto con la clave consignada en &quot; eatc_internationalize_dt. eatc_data_id &quot; .&#160; Cuando el usuario realiza una seleccin mltiple en el selector internacionalizado, el sistema toma los pares &quot;clave ( eatc_data_id ), valor ( eatc_int_data )&quot; para realizar&#160; el registro del reconocimiento utilizando el siguiente servicio&#58; 
&#160; 
 ***NUEVO&#58; dinamismo a partir de _DOM. cua_master y adicin del campo tag_id*** 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time =&#123;&#123;valor&#125;&#125;&amp; doma_id =&#123;&#123;valor&#125;&#125;&amp; eatc-dona_id =&#123;&#123;valor&#125;&#125;&amp; tag =&#123;&#123; eatc_internationalize_dt. eatc_int_data &#125;&#125;&amp; tag_id=&#123;&#123; eatc_internationalize_dt. eatc_data_id&#125;&#125; &amp; type =negativa 
&#160; 
 *** 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo **EL EJEMPLO A CONTINUACIN NO SE REVIS CON RESPECTO A LAS NUEVAS DISPOSICIONES, POR LO TANTO EST DESACTUALIZADO** 
&#160; 
 Para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 , cuando se registr su recogida, el Donante entreg una calificacin negativa al gestor de donaciones, Por este motivo el sistema despleg los tags de aspectos a mejorar (aplicables a los gestores de donaciones o doma) y el usuario seleccion el tag &quot;Impuntualidad en la recogida de la donacin&quot;, por lo tanto se deber realizar el siguiente registro en la estructura para registro de tags de calificacin&#160; ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_tag_registry?_id=_* ) de la siguiente manera&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time =[valor]&amp; doma_id =[valor]&amp; eatc-dona_id =[valor]&amp; tag =[valor]&amp; type =negativo 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot;7608059&quot;, 
 tag &#58; &quot;Impuntualidad en la recogida de la donacin&quot;, 
 type &#58; &quot;negativo&quot; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_tag_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; tag = Impuntualidad%20en%20la%20recogida%20de%20la%20donacin &amp; type =negativo 
&#160; 
 La App debe validar que los registros se realicen, es decir que se obtengan respuestas de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;12&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar los regalizados&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_tag_registry? _id =7 
&#160; 
 Calificaciones a partir de los los aspectos por mejorar ( _id=20,21,22,23 ) ***REVISIN CALIFICACIN*** 
 Aunque dados los tags actualmente registrados solo aplicaran las reglas de calificacin _id=20,21,22 , existe una regla adicional (que por el momento no se aplicara&#58; _id=23 ) para cuando se configuren ms tags de calificacin. 
&#160; 
 El sistema debe definir cuantos reconocimientos se aplicaron y de esta manera aplicar las reglas de calificacin de la siguiente manera&#58; 
 Si se entreg 1 aspecto a mejorar, aplica la regla _id=20 (-5 puntos) 
 Si se entregaron 2 aspectos a mejorar, aplica la regla _id=21 (-10 puntos) 

 Si se entregaron 3 aspectos a mejorar, aplica la regla _id=22 (-15 puntos) 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Siguiendo el ejemplo anterior, como se seleccion un aspecto por mejorar (aplicando la regla id=20 )&#160; para el anuncio de donacin cuyo &quot; eatc-id&quot; es 7608059 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-10-17 20&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action_id &#58; &quot;20&quot;, 
 points &#58; &quot;-5&quot;, 
 acumulated_points &#58; &quot;Clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (15) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-10-17%2020&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 7608059 &amp; action_id =20&amp; points =-5&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925141807&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;21&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=18&amp;eatc-dona_id=7608059 &#160;&#160;&#160;&#160;&#160; 

 [Standby&#58; NO SE VA A IMPLEMENTAR DESDE LA APP, SINO POR UN PROCESO DESDE EL SERVIDOR] Calificacin para el punto de donacin por efectuar la calificacin ( _id=22 ) ***REVISIN CALIFICACIN*** 
 Cuando un punto de donacin entrega calificacin a un gestor de donaciones o beneficiario, el sistema le entrega un puntaje (Regla _id=22 &#58; como incentivo a la realizacin de calificaciones).&#160; El sistema debe realizar un registro de calificacin de la siguiente manera&#58; 
 _id &#58; identificador nico generado por el sistema, 
 date_time &#58; corresponde a la fecha y hora en la cual se evalu la calificacin. 
 pod_id &#58; Corresponde al punto de donacin &quot; eatc_dona_headers.eatc-pod_id&quot; . 
 eatc-dona_id &#58; identificador del anuncio de donacin &quot; eatc_dona_headers. eatc-id &quot;. 
 action &#58; corresponde al identificador de la regla de calificacin &quot; eatc_doma_qualification_rules._id &quot;. 
 points &#58; corresponde a los puntos de la regla de calificacin &quot; eatc_doma_qualification_rules.points &quot;. 

 acumulated_points &#58; el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato &quot; acumulated_points &quot; y le suma los puntos que obtuvo 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donacin cuyo eatc-dona_id es 7608059 del ejemplo anterior, dado que el usuario en cuestin realiz la calificacin a las 2019-09-20 06&#58;00&#58;00, utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-20 06&#58;00&#58;00&quot;, 
 pod_id &#58; &quot;339&quot;, 
 eatc-dona_id &#58; &quot; 7608059 &quot;, 
 action &#58; &quot;22&quot;, 
 points &#58; &quot;5&quot;, 
 acumulated_points &#58; &quot;clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el punto de donacin respectivo ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id=339 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (10) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_pods_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-20%2006&#58;00&#58;00 &amp; pod_id = 339 &amp; eatc-dona_id = 7608059 &amp; action =22&amp; points =5&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;191001115829&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;9&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;01&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=22&amp;eatc-dona_id= 7608059 &#160; &#160;&#160;&#160; 
&#160; 
 El sistema debe evaluar cada vez que corre el proceso de calificacin que no exista un registro previo en la tabla respectiva para la presente regla ( id=22 ) , este identificador de &quot;anuncio ( eatc-dona_id )&quot; y este punto de donacin ( pod_id) , antes de volver a aplicarlo (es decir, solo se puede calificar una vez al punto de donacin por entregarle calificacin a un gestor de donaciones o beneficiario)&#58; 
&#160; 
 Ejemplo&#58; 
 Por alguna razn (que no debe ocurrir) se vuelve a calificar este punto de donacin ( pod_id=339 ) bajo este anuncio ( eatc-dona_id = 7608059 ) , entonces antes de correr o realizar un registro de calificacin el sistema debe evaluar si hay un registro previo de calificacin y a ese anuncio de donacin y a este gestor ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?action=22&amp; eatc-dona_id =7608059&amp; pod_id= 339 ).Como para efectos del ejemplo, ya existe un registro, no debera registrar una nueva calificacin para esa regla. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=46f03dd0389a4788970526d46660135d&ext=png&ow=375&oh=667, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=46f03dd0389a4788970526d46660135d&ext=png&ow=375&oh=667 

 102.000000000000 

 ENTREGA DE DONACIN: CALIFICACIN BENEFICIARIO (EATC_DOMA_CAL)