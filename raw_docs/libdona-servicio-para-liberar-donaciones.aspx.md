# libdona-servicio-para-liberar-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
 El presente servicio se especifica para entregar una herramienta segura, que le permita a los puntos de donación (validando correctamente sus credenciales de manera), y si las condiciones de la donación así lo permiten, liberar las donaciones que por algún motivo no fueron recogidas y aun se pueden aprovechar o fueron canceladas por el sistema pero aún son aptas para el consumo humano.&#160; Se debe implementar como un servicio público, cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento&#160;&#160; 
&#160; 
 Documentación de API pública para liberación de donaciones 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 

 LOG DEL SERVICIO 
&#160; 
 El sistema deberá guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqué de un llamado no exitoso (datos incompletos, fallo de ejecución, fallos validación entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;“op”&#58;”false” 

 1. VALIDACIÓN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación de la API Pública . Si lo son, seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIÓN DEL ESTADO DEL PUNTO 
 Con el dato que llega en los parámetros&#58; 
 cua_master 
 eatc_cua 
 eatc_pod_id 
&#160; 
 El sistema deberá realizar la siguiente validación del punto de donación, antes de desplegarle la funcionalidad de captura de anuncios de donación&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods? eatc_active =y&amp; eatc-cua_master= &#123;&#123; cua_master &#125;&#125;&amp; eatc-cua =&#123;&#123; eatc_cua &#125;&#125;&amp; eatc-id =&#123;&#123; eatc_pod_id &#125;&#125;&amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta ( validación de datos de la donación )&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, cuenta &quot; exito &quot;, punto de donación (eatc-id) &quot; 39 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua_master= abaco &amp;eatc-cua= exito &amp;eatc-id= 39&amp;_cmp=_id &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, cuenta &quot; exito &quot; punto de donación (eatc-id) &quot; 646 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua_master= abaco &amp;eatc-cua=exito&amp;eatc-id= 646&amp;_cmp=_id &#160; &#160; 
&#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta &quot; fail &quot;&#58; 

 3. VALIDACIÓN DE LOS DATOS DE LA DONACIÓN A SER LIBERADA. 
&#160; 
 Con los datos que llegan en los parámetros&#58; 
&#160; 
 cua_master 
 eatc_cua 
 eatc_dona_header_code 
 eatc_dona_state 
 eatc_pod_id 
&#160; 
 El sistema deberá consultar si la donación en cuestión corresponde a los datos entregados y si posee un estado válido para efectuar la liberación (scheduled, cancelled) mediante las siguientes consultas&#58; 
&#160; 
 Consulta para donaciones cuyo eatc_dona_state= scheduled 
&#160; 
 Cuando la donación que se va a consultar fue enviada con el parámetro eatc_dona_state= scheduled entonces el sistema realiza la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-pod_id 
 =&#123;&#123; eatc_pod_id &#125;&#125;&amp;eatc_cua_origin=&#123;&#123; eatc_cua &#125;&#125; &amp;eatc-picking_checkin_datetime 
 =0000-00-00%2000&#58;00&#58;00&amp;eatc-picking_checkout_datetime=0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled &amp;_cmp= eatc-publication_datetime ,eatc-programed_picking_datetime,eatc-donation_manager_code,eatc-donation_manager_name,eatc-donation_manager_typology_b 
&#160; 
 **Las fechas de checkin y checkout se envían a manera de error handler para el estado (se supone que si una de estas fechas existe el estado de la donación debería ser &quot;delivered&quot; y por lo tanto no pasar la consulta 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail&#58; dona_already_picked 
&#160; 
 Si la consulta arroja una respuesta válida, el sistema guarda en una variable 
 &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125;=&#123;&#123; eatc_old_publication_datetime &#125;&#125; 
&#160; 
 y sigue con la siguiente validación ( validación de fechas ). 

&#160; 
 Consulta para donaciones cuyo eatc_dona_state= cancelled 
 Cuando la donación que se va a consultar fue enviada con el parámetro eatc_dona_state= cancelled entonces el sistema realiza la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-pod_id 
 =&#123;&#123; eatc_pod_id &#125;&#125;&amp;eatc_cua_origin=&#123;&#123; eatc_cua &#125;&#125; &amp;eatc-picking_checkin_datetime 
 =0000-00-00%2000&#58;00&#58;00&amp;eatc-picking_checkout_datetime=0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= cancelled &amp;_cmp= eatc-publication_datetime ,eatc-cancellation_datetime,eatc-donation_manager_code,eatc-donation_manager_name,eatc-donation_manager_typology_b 
&#160; 
 **Las fechas de checkin y checkout se envían a manera de error handler para el estado (se supone que si una de estas fechas existe el estado de la donación debería ser &quot;delivered&quot; y por lo tanto no pasar la consulta. 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Si la consulta arroja una respuesta válida, el sistema guarda en una variable 
 &#123;&#123;eatc_dona_headers. eatc-publication_datetime &#125;&#125;=&#123;&#123; eatc_old_publication_datetime &#125;&#125; 
&#160; 
 y sigue con la siguiente validación ( validación de fechas )&#58; 

 4. VALIDACIÓN DE FECHAS PARA DETERMINAR SI UNA DONACIÓN SE PUEDE LIBERAR 
&#160; 
 Nota importante para este desarrollo &#58; se deberá tener en cuenta que estas mismas validaciones se deberán implementar en la wapp donantes, para desplegar el botón que permitirá realizar la liberación de la donación (siendo estas validaciones una especie de &quot;error handler&quot;), en ese sentido se debe trabajar de manera que se pueda reciclar al máximo el código (o la lógica) aquí empleado 
&#160; 
 Consulta para donaciones cuyo eatc_dona_state= scheduled =&gt; IMPLEMENTAR VALIDACIÓN&#58; 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name= dona_libdona_from_scheduled 
 &amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
&#160; 
 Ejemplo cuenta maestra abaco en ambiente de pruebas &#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name= dona_libdona_from_scheduled &amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from &#160; &#160; 
&#160; 
 res &#58; 
 [ 
 &#123; 
 eatc-timeout_description &#58; &quot;Tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada&quot; , 
 eatc-timeout_in_minutes &#58; &quot;60&quot; , 
 eatc-timeout_in_hours &#58; &quot;1&quot; , 
 eatc-timeout_from &#58; &quot;eatc-programed_picking_datetime&quot; 
 &#125; 
 ], 
&#160; 
 Si la consulta no arroja respuesta, se tomará como valor por defecto&#58; 
 eatc-timeout_in_minutes &#58; &quot;60&quot; , 
 eatc-timeout_in_hours &#58; &quot;1&quot; , 
&#160; 
 Es decir que este timeout indica un tiempo mínimo que se debe esperar antes de poder liberar la donación contado a partir de la fecha de recogida programada 
&#160; 
 El sistema deberá determinar, si a la hora de correr el servicio, ese tiempo mínimo ha transcurrido o no. 
&#160; 
 El tiempo mínimo no ha transcurrido&#58; 
 Esto quiere decir que la fecha y hora actual es anterior a la sumatoria de la fecha de recogida programada y el timeout (es decir que la fecha y hora de recogida programada más el timeout está en el futuro). 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &lt; &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Si el tiempo mínimo no ha transcurrido, el servicio deberá contestar&#58; 
 fail_libdona_before_programmed_picking_datetime_plus_timeout 
&#160; 
 ó (Como mejor sea, de cara a la arquitectura del servicio y su interacción con la webapp) 
&#160; 
 fail&#58; libdona_before_programmed_picking_datetime_plus_timeout 
&#160; 
 El tiempo mínimo ya se cumplió&#58; 
 Esto quiere decir que la fecha y hora actual es posterior a la sumatoria de la fecha de recogida programada y el timeout (es decir la fecha y hora de recogida programada más un timeout, está en el pasado) 
&#160; 
 &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; &lt; &#123;&#123;fecha_hora_actual&#125;&#125; 
&#160; 
 Si el tiempo mínimo ya transcurrió, entonces se deberá continuar con el flujo de proceso para donaciones con estado “scheduled” 

&#160; 
 NO APLICA&#58; Consulta para donaciones cuyo eatc_dona_state=cancelled =&gt; NO IMPLEMENTADO (STANDBY) 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_release_from_cancelled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
&#160; 
 Ejemplo cuenta maestra abaco en ambiente de pruebas &#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_release_from_cancelled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from &#160;&#160; 
&#160; 
 res &#58; 
 [ 
 &#123; 
 eatc-timeout_description &#58; &quot;Tiempo máximo para liberar una donación a partir de la fecha de la fecha y hora de cancelacion&quot;, 
 eatc-timeout_in_minutes &#58; &quot;60000&quot;, 
 eatc-timeout_in_hours &#58; &quot;1000&quot;, 
 eatc-timeout_from &#58; &quot;eatc-cancellation_datetime&quot; 

&#160; 
 &#125; 
 ], 
 Si la consulta no arroja respuesta, se tomará como valor por defecto&#58; 
 eatc-timeout_in_minutes &#58; &quot;60000&quot;, 
 eatc-timeout_in_hours &#58; &quot;1000&quot;, 

&#160; 
 Es decir que este timeout indica un tiempo máximo (por demás muy amplio) para poder liberar una donación después de que ha sido cancelada por el sistema. 
&#160; 
 El sistema deberá determinar, si a la hora de correr el servicio, ese tiempo máximo ha transcurrido o no. 
&#160; 
 El tiempo máximo ya se cumplió&#58; 
 Esto quiere decir que la fecha y hora actual es superior a la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &gt; &#123;&#123;eatc_dona_headers.eatc-cancellation_datetime&#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Nota &#58; se corrige error en la documentación, porque estaba erróneamente &quot;eatc-programed_picking_datetime&quot; en vez de &quot;eatc-cancellation_datetime&quot; 
 Si el timeout se ha superado (es decir si la fecha y hora actual es mayor a la sumatoria de la fecha programada de recogida más el timeout) deberá contestar&#58; 
 fail 
&#160; 
 El tiempo máximo no se ha cumplido&#58; 
 Esto quiere decir que la fecha y hora actual es inferior a la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &lt; &#123;&#123;eatc_dona_headers.eatc-cancellation_datetime&#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Nota &#58; se corrige error en la documentación, porque estaba erróneamente &quot;eatc-programed_picking_datetime&quot; en vez de &quot;eatc-cancellation_datetime&quot; 
&#160; 
 Entonces se deberá continuar con el flujo de proceso para donaciones con estado &quot;cancelled&quot; 

 5. FLUJO DE PROCESO PARA DONACIONES EATC_DONA_STATE=SCHEDULED 
 DEPRECADO&#58; 5.1. Suspensión del beneficiario 
 Actualización de datos del beneficiario en eatc_donation_managers 
 Si en la respuesta que entregó la consulta de los datos de la donación , se tiene que&#160; 
&#160; 
 eatc_dona_headers.eatc-donation_manager_typology_b es diferente a &quot;1&quot; 
&#160; 
 ** Es decir que la suspensión sólo aplica a organizaciones diferentes a bancos de alimentos 
&#160; 
 Entonces el sistema deberá proceder con la suspensión de la organización de la siguiente manera 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125; / ?_tabla= eatc_donation_managers &amp;_operacion= update &amp;eatc_state= suspendido &amp;fecha2= [timestamp_realizacion_registro] &amp;causal_inactivo= susp_autom_no_recogió_donacion &amp;WHEREidentificador_unico_registro = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125; 
&#160; 
 Para este proceso los valores suspendido y susp_autom_no_recogió_donacion son constantes. 
&#160; 
 5.2. Registro en el historial de estados del beneficiario&#58; ***NUEVO Ajuste (dado que ya no se suspende)&#58; eatc_doma_new_state= &#123;&#123; current_state &#125;&#125; &#160; y generación de una nota pública (con información que se le compartirá al beneficiario)** 
&#160; 
 Creación de registro en eatc_doma_state_change_history 
&#160; 
 Para realizar las anotaciones de la donación liberada, se toma la información del llamado a servicio y se genera la siguiente concatenación de información (para una nota privada) 
&#160; 
 &#123;&#123;notas_donacion_liberada&#125;&#125; 
 libdona&#58; Donación&#58; &#123;&#123; eatc_dona_header_code &#125;&#125;, Cuenta&#58; &#123;&#123; eatc_cua &#125;&#125;, pod_id&#58; &#123;&#123; eatc_pod_id &#125;&#125;, e-mail pod&#58; &#123;&#123; eatc_pod_email &#125;&#125;, causal de liberación&#58; &#123;&#123; eatc_dona_release_cause &#125;&#125; 
&#160; 
 ***NUEVO&#58; Nota púbica *** 
&#160; 
 De igual manera se toma la información del llamado a servicio, se obtiene con ella otra información&#160; 
 &#123;&#123; nombre_pod &#125;&#125; = &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123; eatc_cua &#125;&#125;/eatc_pods? eatc-id =&#123;&#123; eatc_pod_id &#125;&#125;&amp;_cmp=eatc-name 
&#160; 
 y se genera la siguiente concatenación de información (que debe armarse&#160; con labels para su internacionalización) una nota pública, que se entregará al beneficiario 
&#160; 
 &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
 La donación ( label (class)= lbl_la_donacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_la_donacion ) )&#58; &#123;&#123; eatc_dona_header_code &#125;&#125; de nuestro donante (label (class)= lbl_de_nuestro_donante ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_de_nuestro_donante )) &#58; &#123;&#123; eatc_cua &#125;&#125;, fue liberada por el punto de donación (label (class)= lbl_fue_lib_por_pod (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_fue_lib_por_pod) )&#58; &#123;&#123; nombre_pod &#125;&#125;, por la siguiente causal (label (class)= lbl_por_causal (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_por_causal)) &#58; &#123;&#123; eatc_dona_release_cause &#125;&#125; 
&#160; 
 NUEVO&#58;&#160; Consulta del estado actual del gestor de donaciones&#58; 
&#160; 
 El sistema deberá consultar el estado actual del gestor de donaciones ( &#123;&#123;eatc_donation_managers. eatc_state &#125;&#125; ) para colocarlo en el registro del historial 
&#160; 
 El sistema deberá realizar la siguiente actualización de datos (como ya no se suspende, en el historial debe aparecer, tanto en el actual, como en el nuevo estado con el estado del donante a la hora de realizar el cambio ( &#123;&#123;eatc_donation_managers. eatc_state &#125;&#125; ) . Además se deberá crear el campo &quot; eatc_public_notes &quot; en la tabla respectiva para realizar el nuevo registro de la Nota Pública ) 

&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state= &#123;&#123;eatc_donation_managers. eatc_state &#125;&#125; &amp; e atc_doma_new_state = &#123;&#123;eatc_donation_managers. eatc_state &#125;&#125; &amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125;&amp; eatc_public_notes = &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 

&#160; 
 Anteriormente - DEPRECADO&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state= activo &amp; eatc_doma_new_state = activo &amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125;&amp; eatc_public_notes= &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 
 Anteriormente - DEPRECADO&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state= activo &amp;eatc_doma_new_state= suspendido &amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125; 
&#160; 
&#160; 
 5.2.b ***NUEVO&#58; Cuando eatc_dona_release_cause = lbl_bloqueo_pod_beneficiario , escritura de bloqueo en &quot;eatc_blocked_doma&quot; *** 
&#160; 
 Cuando el servicio reciba en el parámetro&#160; eatc_dona_release_cause el valor&#58; lbl_bloqueo_pod_beneficiario, el sistema deberá realizar lo siguiente&#58; 

&#160; 
 Consulta del identificador &#123;&#123;eatc_doma_id&#125;&#125; y el nombre del gestor de donaciones &#123;&#123;eatc_doma_name&#125;&#125; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123; cua_master &#125;&#125; / eatc_dona_header_code ?_cmp= eatc-donation_manager_code,eatc-donation_manager_name 
&#160; 
 Con el par de valores recibidos se procede a realizar la siguiente escritura y los parámetros con los que se invoca el servicio (&quot; Parámetros del Body de la petición &quot;) se realiza la siguiente escritura&#58; 

&#160; 
 Parámetros de invocación del CRD &#123;&#123;parametros_bloqueo&#125;&#125; 
 eatc_doma_id = &#123;&#123; eatc_dona_header_code. eatc-donation_manager_code&#125;&#125; ,&#125; 
 eatc_doma_name = &#123;&#123; eatc_dona_header_code. eatc-donation_manager_name&#125;&#125; ,&#125; 
 eatc_cua_master = &#123;&#123; cua_master &#125;&#125; ,&#125; 
 eatc_donor = &#123;&#123; eatc_cua &#125;&#125; , 
 eatc_date = &#123;&#123; date_stamp &#125;&#125; 
 eatc_validity_block = activo , 
 eatc_bo_user = &#123;&#123; eatc_pod_email &#125;&#125; , 
 eatc_cause_id = lbl_bloqueo_pod_beneficiario 
 eatc_cause = Preferimos no entregar más donaciones a ese beneficiario 
 eatc_note = automatic_libdona 
 , 
 Escritura con el CRD 
 Con los parámetros obtenidos se realiza la siguiente escritura&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/?_tabla= eatc_blocked_doma &amp;_operacion=insert&amp; &#123;&#123;parametros_bloqueo&#125;&#125; 

&#160; 
 5.3. Actualización de los datos de programación de la donación 
 Aunque es posible que por las restricciones que se le han impuesto al CRD para actuar sobre ciertas donaciones, el servicio no funcione en este caso, se documenta basándose en su funcionamiento (el servicio deberá implementar el mecanismo idóneo para poder realizar el borrado de datos correspondientes 
&#160; 
 &#123;&#123; parámetros_update_CRD &#125;&#125; 
&#160; 
 eatc-adjudication_datetime =0 (o vacío) 
 eatc-donation_manager_user_doc_id =0 (o vacío) 
 eatc-donation_manager_code =0 (o vacío) 
 eatc-donation_manager_name =0 (o vacío) 
 eatc-donation_manager_address =0 (o vacío) 
 eatc-donation_manager_phone =0 (o vacío) 
 eatc-donation_manager_typology_a =0 (o vacío) 
 eatc-donation_manager_typology_b =0 (o vacío) 
 eatc-donation_manager_typology_c =0 (o vacío) 
 eatc-scheduling_datetime=0000-00-00 00&#58;00&#58;00 
 eatc-programed_picking_datetime=0000-00-00 00&#58;00&#58;00 
 eatc-picker_name =0 (o vacío) 
 eatc-picker_doc_id =0 (o vacío) 
 eatc-picker_license_plate =0 (o vacío) 
 eatc-state= announced 
 eatc-publication_date =&#123;&#123;datestamp&#125;&#125; =&gt; Se coloca como nueva fecha de publicación la fecha en la cual se invoca el servicio 
 eatc-pubication_datetime =&#123;&#123;datetimestamp&#125;&#125;=&gt; Se coloca como nueva fecha y hora de publicación la fecha y hora en la cual se invoca el servicio 
&#160; 
 Nuevo campo&#58; El campo eatc_dona_headers.eatc_old_publication_datetime no existe, por lo cual se deberá crear y verificar que se cree en todos los eatc_dona_headers de las diversas cuentas maestras y se genere cuando se creen las tablas al generar una nueva cuenta maestra . 
&#160; 
 eatc_old_pubication_datetime = &#123;&#123; eatc_old_publication_datetime &#125;&#125; =&gt; Se lleva el valor anterior de fecha y hora de publicación obtenido en la consulta respectiva a este nuevo parámetro. 
 eatc-cancellation_datetime (debe funcionar como funciona en la creación de encabezados , a partir de las nuevas fechas de publicación generadas en el proceso)&#58; 
 IF eatc_cua_origin= eatc-donor ( eatc-cancellation_datetime = eatc-publication_datetime + eatc_timeout_rules. eatc-timeout_in_hours &#160;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout) ELSE 
 ( eatc-cancellation_datetime =[eatc-publication_datetime + eatc_timeout_rules. eatc-timeout_in_hours &#160;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona _nng _cancellation_timeout) 

&#160; 
 Escritura con la API&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update &amp; &#123;&#123; parámetros_update_CRD &#125;&#125; &amp; WHEREeatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125; 
&#160; 
 5.4. Escritura en el historial de estados de la donación 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 
 eatc-state = announced &#160; =&gt; Constante 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)&quot; 
 eatc-log = &#123;&#123;notas_donacion_liberada&#125;&#125; =&gt; Tal como se definieron para &quot; el cambio de estado del gestor de donaciones &quot; 
 eatc_doma_id = &#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125; 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; eatc_cua_master &#125;&#125; =&gt; Cuenta maestra, enviada como parámetro de invocación del servicio. 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 5.5. Llamado a servicios para realización del match para el anuncio liberado 
 Se deberán llamar a los procesos y servicios que generan la programación automática de la donación / match, garantizando que los mismos corran para poder tener un proceso que gestione de manera íntegra la liberación del anuncio. 

&#160; 
 5.6. ***NUEVO&#58; LLAMADO A SERVICIOS DE INTEGRACIÓN CON BLOCKCHAIN *** 
 Endpoint&#58; Creación de encabezados (según documentación &#58; sujeto a revisión) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio= frmDonacionExcedente 
&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación liberado&#58; eatc_dona_heaaders. eatc-code =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio (_DOM. cua_master ) =&gt; parámetro de carácter obligatorio 

 6. FLUJO DE PROCESO PARA DONACIONES EATC_DONA_STATE=CANCELLED&#160; 
&#160; 
 6.1. Actualización de información y cambio de estado de la donación 
&#160; 
 Aunque es posible que por las restricciones que se le han impuesto al CRD para actuar sobre ciertas donaciones, el servicio no funcione en este caso, se documenta basándose en su funcionamiento (el servicio deberá implementar el mecanismo idóneo para poder realizar el borrado de datos correspondientes 
&#160; 
 &#123;&#123; parámetros_update_CRD &#125;&#125; 
&#160; 
 eatc-state= announced 
 eatc-publication_date =&#123;&#123;datestamp&#125;&#125; =&gt; Se coloca como nueva fecha de publicación la fecha en la cual se invoca el servicio 
 eatc-pubication_datetime =&#123;&#123;datetimestamp&#125;&#125;=&gt; Se coloca como nueva fecha y hora de publicación la fecha y hora en la cual se invoca el servicio 
&#160; 
 Nuevo campo&#58; El campo eatc_dona_headers.eatc_old_publication_datetime no existe, por lo cual se deberá crear y verificar que se cree en todos los eatc_dona_headers de las diversas cuentas maestras y se genere cuando se creen las tablas al generar una nueva cuenta maestra . 
&#160; 
 eatc_old_pubication_datetime = &#123;&#123; eatc_old_publication_datetime &#125;&#125; =&gt; Se lleva el valor anterior de fecha y hora de publicación obtenido en la consulta respectiva a este nuevo parámetro. 
 eatc-cancellation_datetime (debe funcionar como funciona en la creación de encabezados , a partir de las nuevas fechas de publicación generadas en el proceso)&#58; 
 IF eatc_cua_origin= eatc-donor ( eatc-cancellation_datetime = eatc-publication_datetime + eatc_timeout_rules. eatc-timeout_in_hours &#160;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout) ELSE 
 ( eatc-cancellation_datetime =[eatc-publication_datetime + eatc_timeout_rules. eatc-timeout_in_hours &#160;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona _nng _cancellation_timeout) 

&#160; 
 6.2. Escritura en el historial de estados de la donación 
 &#123;&#123; parámetros_insert_CRD &#125;&#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 
 eatc-state = announced &#160; =&gt; Constante 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)&quot; 
 eatc-log = &#123;&#123;notas_donacion_liberada&#125;&#125; =&gt; Tal como se definieron para &quot; el cambio de estado del gestor de donaciones &quot; 
 eatc_doma_id = &#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125; 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; eatc_cua_master &#125;&#125; =&gt; Cuenta maestra, enviada como parámetro de invocación del servicio. 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
 6.5. Llamado a servicios para realización del match para el anuncio liberado 
 Se deberán llamar a los procesos y servicios que generan la programación automática de la donación / match, garantizando que los mismos corran para poder tener un proceso que gestione de manera íntegra la liberación del anuncio. 

&#160; 
 6.6. ***NUEVO&#58; LLAMADO A SERVICIOS DE INTEGRACIÓN CON BLOCKCHAIN *** 
 Endpoint&#58; Creación de encabezados (según documentación &#58; sujeto a revisión) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio= frmDonacionExcedente 
&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación liberado&#58; eatc_dona_heaaders. eatc-code =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio (_DOM. cua_master ) =&gt; parámetro de carácter obligatorio 

 7. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si las actualizaciones de información realizadas por el servicio se realizan de manera adecuada, entonces entregará la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 User Administrator 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 51acb56f-df74-4a4f-836b-bead8581cbe3 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 b82923bb-fdcb-4856-9f87-b9605c55b473 
 2025-12-19T05:55:39.2526108Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"b119df76-28c7-4336-8f2d-16d0d1466e1a","SequenceId":42,"FluidContainerCustomId":"c665c608-9025-42ec-bcd4-a48ef5ef1db2","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 LIBDONA: SERVICIO PARA LIBERAR DONACIONES