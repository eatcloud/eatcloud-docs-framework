# entrega-de-donacion-hora-de-salida-eatc_doma_checkout.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Registro de salida de beneficiario 
 Cuando el anuncio tiene registrada una fecha y hora de llegada a la recogida ( eatc-picking_checkin_datetime ) debe aparecer el botn &quot;registro de salida beneficiario&quot; que da la entrada a la funcionalidad &quot; Entrega de donacin&#58; hora de salida &quot;.&#160; Con esta accin se deben realizar las siguientes acciones&#58; 1. Actualizar la informacin de encabezados; 2. Realizar un registro en el histrico de estados de donacin; 3. Realizar las calificaciones correspondientes. 
&#160; 
Actualizacin de informacin de encabezados de donacin ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Al accionar este botn el sistema debe realizar la siguiente labor, mediante el API&#58; registrar la fecha y hora de salida ( eatc-picking_checkout_datetime ) y cambiar el estado a &quot;delivered&quot; en el respectivo encabezado ( eatc_dona_headers ) 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123; _DOM.cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= delivered &amp;eatc-picking_checkout_datetime=&#123;&#123;fecha_hora&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;valor&#125;&#125; 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , y que mediante la App se accion el botn de registro de salida de beneficiario a las 2019-11-01 11&#58;11&#58;11&#160; mediante la API se debe hacer la siguiente escritura 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update &amp;eatc-state= delivered &amp;eatc-picking_checkout_datetime=2019-11-01%2011&#58;11&#58;11&amp;WHEREeatc-code=40717 &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114847&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) *** Revisar dinamismo a partir de _DOM.cua_master*** 
 Para el registro del estado &quot; delivered &quot; se toma la fecha en la que se entreg el anuncio ( eatc-picking_checkout_datetime ) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123; _DOM.cua_master &#125;&#125; /?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125;&amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;AAAA-MM-DD%20HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123; eatc-pod_id&#125;&#125; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
&#160; 
 Para el anuncio de donacin cuyo eatc-code = 40717 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-code&#58; &quot;40717&quot;, 
 eatc-picking_checkout_datetime &#58; &quot;2019-11-01 11&#58;11&#58;11&quot;, 
 eatc-pod_id &#58; &quot;339&quot; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 Registro del estado &quot;delivered&quot; &#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =40717&amp; eatc-state = delivered &amp; eatc-date_time =2019-11-01%2012&#58;11&#58;11&amp; eatc-log = eatc-pod_id &#58;339 
 Para consultar los estados registrados&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 
 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925174723&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;7&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;15&quot; 
&#160; 
 &#125; 

&#160; 
 ***REVISIN CALIFICACIN*** Calificacin para el punto de donacin (pod) por registrar el check out de un gestor de donaciones ( _id=2 ) 
 Cuando se presiona el botn &quot; registro de salida beneficiario &quot;, el sistema debe realizar un registro de calificacin de la siguiente manera&#58; 
 _id &#58; identificador nico generado por el sistema, 
 date_time &#58; corresponde a la fecha y hora en la cual se registr la salida, que en este caso corresponde a eatc-picking_checkout_datetime . 
 pod_id &#58; Corresponde al cdigo del punto de donaciones &quot;eatc_dona_headers.eatc-pod_id&quot;. 
 eatc-dona_id &#58; identificador del anuncio de donacin &quot; eatc_dona_headers. eatc-id &quot;. 
 action_id &#58; corresponde al identificador de la regla de calificacin &quot; eatc_pods_qualification_rules._id &quot; (en este caso&#58; 2). 
 points &#58; corresponde a los puntos de la regla de calificacin &quot; eatc_doma_qualification_rules.points &quot; (en este caso&#58; 5). 
 acumulated_points &#58; el sistema debe establecer cual fue el ltimo registro realizado para el gestor de donacin y sobre el mismo, se toma el dato &quot;acumulated_points &quot; y le suma los puntos que obtuvo 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donacin cuyo eatc-code = 40717 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-picking_checkout_datetime &#58; &quot;2019-11-01 11&#58;11&#58;11&quot;, 
 El registro resultante sera&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-11-01 11&#58;11&#58;11&quot;, 
 pod_id &#58; &quot;339&quot;, 
 eatc-dona_id &#58; &quot;5252095&quot;, 
 action &#58; &quot;2&quot;, 
 points &#58; &quot;5&quot;, 
 acumulated_points &#58; &quot;clculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el clculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la ltima calificacin registrada para el gestor de donaciones respectivo ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?pod_id= 339 ).&#160; Definiendo el ltimo registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificacin (5) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_pods_qualification_registry&amp;_operacion=insert&amp; date_time = 2019-11-01%2011&#58;11&#58;11 &amp; pod_id = 339 &amp; eatc-dona_id = 5252095 &amp; action =2&amp; points =5&amp; acumulated_points = clculo%20de%20puntos%20acumulados &#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;191001115829&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;16&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;01&quot; 
 &#125; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aqu se puede consultar el registro realizado&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_id=7 &#160; &#160;&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=58794d6b3c174b249a03ac6cdd71c097&ext=png&ow=375&oh=667, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=58794d6b3c174b249a03ac6cdd71c097&ext=png&ow=375&oh=667 
 EatCloud Donantes WEB-APP 

 100.000000000000 

 ENTREGA DE DONACIN: HORA DE SALIDA (EATC_DOMA_CHECKOUT)