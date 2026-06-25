# entrega-de-donación-beneficiario-hora-de-salida-eatc_doma_checkout.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 [**NUEVO**]&#160; 
 En adelante esta funcionalidad siempre estampará la fecha y hora de check-out (incluyendo la nueva funcionalidad de check-out extemporáneo) siempre cambiará el estado de &quot;programado&quot; a &quot;despachado&quot; ( delivered ) 
&#160; 
 ANTERIORMENTE&#58; y solo cambiara el estado de &quot;programado&quot; a &quot;despachado&quot; si existe un registro válido de &quot;eatc_code_verification_datetime&quot; para el anuncio en cuestión. 
&#160; 
 VALIDACIÓN DE LA FECHA Y HORA ACTUAL VS LA FECHA Y HORA DE CHECK-IN 
 (eatc-picking_checkin_datetime) 
&#160; 
 El sistema debe comparar la fecha y hora actual ( current_datetime ) con la fecha y hora de de check-in estampada en el anuncio ( eatc_dona_headers. eatc-picking_checkin_datetime ).&#160; 

&#160; 

 La diferencia entre la fecha y hora actual con respecto a la fecha y hora del check-in es menor que el tiempo definido por el &quot;checkout_timeout&quot; ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Si la diferencia entre la hora actual y la hora del check-in (eatc-picking_checkin_datetime) es inferior a la cantidad de tiempo definido por el timeout &quot; checkout_timeout &quot; en sus parámetros&#58; eatc-timeout_in_minutes o eatc-timeout_in_hours , y cuyos datos se obtienen realizando la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name= checkout_timeout 
&#160; 
 el sistema debe tomar la fecha y&#160; hora actual para realizar el siguiente registro que contiene la fecha y hora de salida. 
&#160; 
 Mediante el API (CRUD), el sistema debe registrar la fecha y hora de salida del punto de donación ( eatc-picking_checkout_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 

&#160; 
 SIEMPRE SE MARCA EN ESTADO delivered ***NUEVO &#58; eatc_state3=Despachado *** 
El sistema valida si existe o no fecha y hora de verificación del código (eatc_code_verification_datetime). 
&#160; 
Si hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;!= &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Despachado &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
Si NO hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;== &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando NO existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Por %20 verificar &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Realizada este registro se debe pasar a la &quot; Validación de la existencia de una fecha y hora de verificación del código de salida cuando no se ha hecho un registro de fecha y hora extemporáneo &quot;. 

&#160; 
 La fecha y hora actual es mayor en el tiempo definido por el &quot;checkout_timeout&quot; que la fecha y hora programada de recogida ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Si la hora actual es superior a la hora del checkin en la cantidad de tiempo definido por el timeout &quot; checkout_timeout &quot; en sus parámetros&#58; eatc-timeout_in_minutes o eatc-timeout_in_hours , y cuyos datos se obtienen realizando la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name= checkout_timeout 
&#160; 
 Entonces el sistema debe mostrar el siguiente mensaje&#58; 
&#160; 
 Ya han pasado más de &#123;&#123; ( eatc_timeout_rules?eatc-timeout_name= checkout_timeout). eatc-timeout_in_minutes&#125;&#125; minutos desde que se registró la llegad al punto de donación.&#160; Deseas registrar la fecha y hora actual como la correspondiente a tu salida del punto de donación 
&#160; 
 SI &#160; NO 

&#160; 
 OPCIÓN SI&#58; 
 Si el usuario acciona la opción &quot;SI&quot;, el sistema debe tomar la fecha y&#160; hora actual (current_datetime) para realizar el siguiente registro que contiene la fecha y hora de salida. 
&#160; 
 Mediante el API (CRUD), el sistema debe registrar la fecha y hora de salida del punto de donación (eatc-picking_checkout_datetime) en el respectivo encabezado (eatc_dona_headers) 
&#160; 
 SIEMPRE SE MARCA EN ESTADO delivered&#58; ***NUEVO &#58; eatc_state3=Despachado *** 
El sistema valida si existe o no fecha y hora de verificación del código (eatc_code_verification_datetime). 
&#160; 
Si hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;!= &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Despachado &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
Si NO hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;== &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando NO existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Por %20 verificar &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Realizada este registro se debe pasar a la &quot; Validación de la existencia de una fecha y hora de verificación del código de salida cuando no se ha hecho un registro de fecha y hora extemporáneo &quot;. 

&#160; 
 OPCIÓN NO (FUNCIONALIDAD DE REGISTRO DE FECHA Y HORA DE SALIDA EXTEMPORÁNEO)&#58; 
 El sistema debe preguntar el motivo por el registro extemporáneo presentando un selector de motivos de registro extemporáneos y luego debe presentar un datetime picker para registrar la hora del checkout, de la siguiente manera. 

&#160; 
 Motivo del registro de salida extemporáneo&#58; 
 Tipo de dato &#58; sting 
 Tipo de input de datos&#58; dropdown único 
 Valor por defecto &#58; vacío 
 Obligatoriedad &#58; si 
 Validación &#58; obligatoriedad 
 La información se toma de (maestro)&#58; 
&#160; 
 *** NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (código de dos dígitos) del dispositivo para con él realizar la nueva consulta de las verticales 
&#160; 
 ***NUEVO&#58; Paso 2&#58; consulta de los causales de checkin extemporáneos en datos internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125;&amp;eatc_mt= eatc_extemporaneous_checkout_causes 

&#160; 
 Ejemplo&#58; idioma español a 10 de diciembre de 2020&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=es&amp;eatc_mt= eatc_extemporaneous_checkout_causes 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto (inglés= en idioma por defecto)&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_extemporaneous_checkout_causes &amp;eatc_language= en &#160;&#160; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en los selectores&#58; 
&#160; 
 Ejemplo&#58; idioma español a 10 de diciembre de 2020, entorno productivo&#58; 
 Se mostrarían los selectores con los siguientes labels 
&#160; 
 Me olvidé registrar la salida cuando efectivamente salí del punto 
 Tuve problemas con la aplicación y cuando quise hacer el registro de salida, no funcionó 
 No me validaron el código para la recogida de la donación&#160; a tiempo 
 El que recogió la donación no tiene el aplicativo 
&#160; 
 cuándo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/ eatc_extemporaneous_checkout_causes ?_id=&#123;&#123; eatc_internationalize_dt. eatc_int_data_id &#125;&#125; para llevar al registro los valores eatc_extemporaneous_checkout_causes. eatc-issue_cause_code y eatc_extemporaneous_checkout_causes. eatc-issue_cause 
&#160; 
 Ejemplo, continuando con el anterior 
 Si el usuario selecciona &quot; El que recogió la donación no tiene el aplicativo &quot; entonces eatc_internationalize_dt. eatc_data_id= 4 por lo tanto al hacer la siguiente consulta&#58; https&#58;//beneficiarios.eatcloud.info/api/eatcloud/ eatc_extemporaneous_checkout_causes ?_id=4 &#160; al registro se llevaría el valor &quot; eatc_checkin_and_deliver_issues . eatc-issue_cause_code &quot; = &quot; e_chkout4 &quot; y &quot; eatc_checkin_and_deliver_issues . eatc-issue_cause &quot; = &quot; El que recogió la donación no tiene el aplicativo&quot; 
&#160; 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validación &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos)&#58; 
Registro de problemas de checkin y despacho&#58; eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause &#160; (más adelante se muestra como se hace el registro completo del issue en este object store ) 
 Se guarda con (para efectos indicativos, no prácticos)&#58; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_user &#125;&#125;/?_tabla=eatc_checkin_and_deliver_issues&amp;_operacion=insert&amp; eatc-issue_cause_code =&#123;&#123; eatc_extemporaneous_checkout_causes. eatc-issue_cause_code &#125;&#125;&amp; eatc-issue_cause =&#123;&#123; eatc_extemporaneous_checkout_causes. eatc-issue_cause &#125;&#125; 
&#160; 
 Fecha y hora de salida del punto de donación&#58; 
 Tipo de dato &#58; datetime 
 Obligatorio &#58; si 
 Valor por defecto &#58; el sistema debe sugerir o poner por defecto la fecha y hora que resulta de sumar la fecha y hora de check-in ( eatc_dona_headers .eatc-picking_checkin_datetime ) más los minutos registrados en el checkout_timeout ( &#123;&#123;URL_entorno_donantes&#125;&#125;api/abaco/eatc_timeout_rules?eatc-timeout_name= checkout_timeout). eatc-timeout_in_minutes . 
 Validaciones &#58; 
 La fecha y hora no puede ser menor a la fecha y hora de check-in ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora de check-in ( eatc_dona_headers .eatc-picking_checkin_datetime ) más tres horas. 
 Se guarda en &#58; 
Encabezado de anuncio de donación&#58; eatc_dona_headers .eatc-picking_checkout_datetime &#160; 

&#160; 
 Registro en el encabezado de anuncio de donación de la fecha y hora de salida (de manera extemporánea) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Se realiza el siguiente registro utilizando el CRD respectivo 
&#160; 
 SIEMPRE SE MARCA EN ESTADO delivered&#58; ***NUEVO &#58; eatc_state3=Despachado *** 
Si hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;!= &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Despachado &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
Si NO hay fecha y hora de verificación del código de recogida, , es decir [&quot;eatc_code_verification_datetime&quot;] &#160;== &quot;0000-00-00 00&#58;00&#58;00&quot;, entonces realiza la siguiente escritura&#58; 
 Escritura con la API cuando NO existe fecha y hora de verificación del código de recogida&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp; eatc-picking_checkout_datetime=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc-state= delivered &amp; eatc_state3= Por %20 verificar &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

&#160; 
 ***NUEVO&#58; LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN *** 
 Endpoint (según documentación ( [POST] servicio&#58; frmDespachar (Enviar donación) )&#58; sujeto a revisión) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio=frmDespachar 

&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación recientemente creado&#58; eatc_dona_heaaders. eatc-code =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) =&gt; parámetro de carácter obligatorio 

 [ DE AQUÍ PARA ABAJO DEPRECADO ]&#160; 
 Realizados estos registros se debe pasar a la &quot; Validación de la existencia de una fecha y hora de verificación del código de salida cuándo se ha hecho un registro de fecha y hora extemporáneo &quot;. 
&#160; 
 V ALIDACIÓN DE LA EXISTENCIA DE UNA FECHA Y HORA DE VERIFICACIÓN DEL CÓDIGO DE RECOGIDA CUANDO NO SE HA REALIZADO UN REGISTRO DE FECHA Y HORA EXTEMPORÁNEO &#58; 
 La app debe validar si existe un registro de fecha y hora de verificación del código de recogida. Cuando existe un registro de fecha y hora de verificación del código de recogida para el anuncio en cuestión ( eatc_dona_headers. eatc_code_verification_datetime ), entonces se debe marcar el anuncio cómo &quot;despachado&quot; y realizar el respectivo registro en el historial de estados.&#160; Si no existe un registro, se debe generar un registro automático del &quot;issue&quot; para su resolución. 

 &#160; 
 Existe un registro válido en eatc_code_verification_datetime del anuncio respectivo (eatc_dona_headers) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 El sistema debe proceder a realizar el cambio de estado del anuncio a &quot;delivered&quot; y a realizar el registro en el historial de estados. 
&#160; 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= delivered &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
&#160; 
 Se realiza el registro correspondiente a través del llamado al CRD. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
&#160; 
 Para el registro del estado &quot; delivered &quot; se toma la fecha en la que se entregó el anuncio ( eatc-picking_checkout_datetime ) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id )&#160; 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente de pruebas&#58; 
&#160; 
 Para el anuncio de donación (en ambiente de pruebas) cuyo eatc-code = exito8620200709153619358 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-code&#58; &quot;exito8620200709153619358&quot;, 
 eatc-picking_checkout_datetime &#58; &quot;2020-07-09 19&#58;07&#58;07&quot;, 
 eatc-pod_id &#58; &quot;86&quot; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =exito8620200709153619358&amp; eatc-state = delivered &amp; eatc-date_time =2020-07-09%2019&#58;07&#58;07&amp; eatc-log = eatc-pod_id &#58;86 &#160; 
&#160; 
 Para consultar los estados registrados&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=exito8620200709153619358 
&#160; 
 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925174723&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;7&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;15&quot; 
 &#125; 

 &#160; 
 No existe un registro válido en eatc_code_verification_datetime del anuncio respectivo (eatc_dona_headers)&#160; 
 El sistema debe presentar el siguiente mensaje&#58; 
&#160; 
 El punto de donación no ha realizado aún el proceso de verificación de código de recogida.&#160; Te solicitamos el favor que te cerciores con los&#160; 
 encargados para que hagan el correspondiente proceso y así evitar bloqueos de la aplicación para obtener futuras donaciones. 
&#160; 
 &quot;He solicitado al almacén me verifiquen el código de recogida&quot; 
&#160; 
 Cuando se oprima el botón, el sistema realiza las siguientes operaciones si la condición de que aun no exista registro válido en eatc_dona_headers. eatc_code_verification_datetime 
&#160; 
 Se hace el registro de un issue, por la no realización de la validación a tiempo. de la siguiente manera&#58; 
 eatc-date &#58; fecha actual en formato AAAA-MM-DD 
 eatc-datetime &#58; fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 eatc-donor_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code&#58; se deja vacío. 
 eatc-final_doma_name&#58; se deja vacío. 
 eatc-dona_initial_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-verification_code&#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token &#58; por el momento se deja vacío.&#160; En un futuro será la clave criptográfica para decodificar el código de verificación (que se enviará encriptado). 
 eatc-dona_final_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-issue_cause_code &#58; se debe colocar lo siguiente&#58; extemporaneous_code_verification . 
 eatc-issue_cause &#58; se debe colocar lo siguiente&#58; El punto de donación no validó el código de recogida antes de la salida del gestor de sus instalaciones. 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration 
 resolved &#58; se coloca en este punto&#58; no 
&#160; 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=insert&amp; eatc-date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125; &amp; eatc-datetime =&#123;&#123;fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; eatc-donor =&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp; eatc-pod_id =&#123;&#123; eatc_dona_headers. eatc-pod_id &#125;&#125;&amp; eatc-pod_name =&#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-donation_manager_code =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp; eatc-donation_manager_name =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-final_doma_code= &quot;&quot;&amp; eatc-final_doma_name =&quot;&quot;&amp; eatc-dona_initial_state =&#123;&#123;atc_dona_headers. eatc-state &#125;&#125;&amp; eatc-verification_code= &#123;&#123;eatc_dona_headers. eatc-verification_code &#125;&#125;&amp; eatc-token =&quot;&quot;&amp; eatc-dona_final_state =&#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;&amp; eatc-issue_cause_code =extemporaneous_code_verification&amp; eatc-issue_cause =El%20punto%20de%20donación%20no%20validó%20el%20código%20de%20recogida%20antes%20de%20la%20salida%20del%20gestor%20de%20sus%20instalaciones&amp; eatc-log =app_automated_issue_registration&amp; resolved =no 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 V ALIDACIÓN DE LA EXISTENCIA DE UNA FECHA Y HORA DE VERIFICACIÓN DEL CÓDIGO DE SALIDA CUANDO SE HA REALIZADO UN REGISTRO DE FECHA Y HORA EXTEMPORÁNEO &#58; 
 La app debe validar si existe un registro de fecha y hora de verificación del código de recogida. Cuando existe un registro de fecha y hora de verificación del código de recogida para el anuncio en cuestión ( eatc_dona_headers. eatc_code_verification_datetime ), entonces se debe marcar el anuncio cómo &quot;despachado&quot; y realizar el respectivo registro en el historial de estados.&#160; Si no existe un registro, se debe generar un registro automático del &quot;issue&quot; para su resolución. 

 &#160; 
 Existe un registro válido en eatc_code_verification_datetime del anuncio respectivo (eatc_dona_headers)&#160; ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 El sistema debe proceder a realizar el cambio de estado del anuncio a &quot;delivered&quot; y a realizar el registro en el historial de estados y luego se hace un registro de un issue resuelto por registro extemporáneo de fecha y hora de check-out. 
&#160; 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= delivered &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
&#160; 
 Se realiza el registro correspondiente a través del llamado al CRD. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
&#160; 
 Para el registro del estado &quot; delivered &quot; se toma la fecha en la que se entregó el anuncio ( eatc-picking_checkout_datetime ) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id )&#160; 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente de pruebas&#58; 
&#160; 
 Para el anuncio de donación (en ambiente de pruebas) cuyo eatc-code = exito8620200709153619358 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-code&#58; &quot;exito8620200709153619358&quot;, 
 eatc-picking_checkout_datetime &#58; &quot;2020-07-09 19&#58;07&#58;07&quot;, 
 eatc-pod_id &#58; &quot;86&quot; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =exito8620200709153619358&amp; eatc-state = delivered &amp; eatc-date_time =2020-07-09%2019&#58;07&#58;07&amp; eatc-log = eatc-pod_id &#58;86 &#160; 
&#160; 
 Para consultar los estados registrados&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=exito8620200709153619358 
&#160; 
 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925174723&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;7&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;15&quot; 
 &#125; 

 &#160; 
 Registro en eatc_checkin_and_deliver_issues&#58; 
 El registro en este object store de issues de checkin y despacho, toma datos de de la fecha y hora actual, el anuncio de donación y los registros de fecha y hora para llevarlos a un repositorio en donde los mismos estarán disponibles para futuras validaciones.&#160; El registro involucra los siguientes parámetros&#58; 
&#160; 
 eatc-date &#58; fecha actual en formato AAAA-MM-DD 
 eatc-datetime &#58; fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 eatc-donor_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 [FALTA EN LA ESTRUCTURA] eatc-city &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code&#58; se deja vacío. 
 eatc-final_doma_name&#58; se deja vacío. 
 eatc-dona_initial_state &#58; se coloca scheduled 
 eatc-verification_code&#58; se deja vacío 
 eatc-token &#58; por el momento se deja vacío.&#160; En un futuro será la clave criptográfica para decodificar el código de verificación (que se enviará encriptado). 
 eatc-dona_final_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-issue_cause_code &#58; se toma de a partir de la información del selector respectivo de la funcionalidad eatc-issue_cause_code 
 eatc-issue_cause &#58; se toma de a partir de la información del selector respectivo de la funcionalidad eatc-issue_cause 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration 
 resolved &#58; se coloca en este punto&#58; si 
&#160; 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=insert&amp; eatc-date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125; &amp; eatc-datetime =&#123;&#123;fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; eatc-donor =&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp; eatc-pod_id =&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&amp; eatc-pod_name =&#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-donation_manager_code =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp; eatc-donation_manager_name =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-final_doma_code= &quot;&quot;&amp; eatc-final_doma_name =&quot;&quot;&amp; eatc-dona_initial_state =scheduled&amp; eatc-verification_code =&quot;&quot;&amp; eatc-token =&quot;&quot;&amp; eatc-dona_final_state =&#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;&amp; eatc-issue_cause_code =&#123;&#123;se toma de a partir de la información del selector respectivo de la funcionalidad&#125;&#125;&amp; eatc-issue_cause =&#123;&#123;se toma de a partir de la información del selector respectivo de la funcionalidad&#125;&#125;&amp; eatc-log =app_automated_issue_registration&amp; resolved =si 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 &#160; 
 NO existe un registro válido en eatc_code_verification_datetime del anuncio respectivo (eatc_dona_headers) 
 Se hace el registro automático de un issue, por la no realización de la validación a tiempo. de la siguiente manera&#58; 
&#160; 
 eatc-date &#58; fecha actual en formato AAAA-MM-DD 
 eatc-datetime &#58; fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 eatc-donor_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 [FALTA EN LA ESTRUCTURA] eatc-city &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-dona_initial_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-verification_code&#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token &#58; por el momento se deja vacío.&#160; En un futuro será la clave criptográfica para decodificar el código de verificación (que se enviará encriptado). 
 eatc-dona_final_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-issue_cause_code &#58; se debe colocar lo siguiente&#58; extemporaneous_code_verification . 
 eatc-issue_cause &#58; se debe colocar lo siguiente&#58; El punto de donación no validó el código de recogida antes de la salida del gestor de sus instalaciones. 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration 
 resolved &#58; se coloca en este punto&#58; no 
&#160; 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=insert&amp; eatc-date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125; &amp; eatc-datetime =&#123;&#123;fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; eatc-donor =&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp; eatc-pod_id =&#123;&#123; eatc_dona_headers. eatc-pod_id &#125;&#125;&amp; eatc-pod_name =&#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-donation_manager_code =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp; eatc-donation_manager_name =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-dona_initial_state =&#123;&#123;atc_dona_headers. eatc-state &#125;&#125;&amp; eatc-verification_code =&#123;&#123;eatc_dona_headers. eatc-verification_code &#125;&#125;&amp; eatc-token =&quot;&quot;&amp; eatc-dona_final_state =&#123;&#123;eatc_dona_headers. eatc-state &#125;&#125;&amp; eatc-issue_cause_code =extemporaneous_code_verification&amp; eatc-issue_cause =El%20punto%20de%20donación%20no%20validó%20el%20código%20de%20recogida%20antes%20de%20la%20salida%20del%20gestor%20de%20sus%20instalaciones. eatc-log =app_automated_issue_registration&amp; resolved =no 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=91c1f3e9897c43fca67dee4241d83798&ext=png&ow=375&oh=667, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=91c1f3e9897c43fca67dee4241d83798&ext=png&ow=375&oh=667 
 EatCloud Beneficiarios APP 

 558.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 bbf8fb00-c371-445f-bcf2-86c457a32204 
 1!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 1b4c1cd7-e03c-4ec6-80f2-03a046301a3c 
 2025-06-13T05:55:38.2356062Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"f61df419-24d4-4f3b-9795-4a28a1c7a57d","SequenceId":1060,"FluidContainerCustomId":"41683302-56d6-46e4-b639-2a2c00613e14","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 ENTREGA DE DONACIÓN: HORA DE SALIDA (EATC_DOMA_CHECKOUT)