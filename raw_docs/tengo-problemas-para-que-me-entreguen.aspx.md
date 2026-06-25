# tengo-problemas-para-que-me-entreguen.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Instrucciones ante una no entrega despliegue&#58; 
 El sistema debe mostrar un vínculo (si lo hay) a instrucciones ante una posible no entrega.&#160; Para determinar si la cuenta específica posee este tipo de información se debe evaluar la información consignada en &quot;config&quot; de la siguiente manera 
&#160; 
 Si evaluando la información de la cuenta respectiva (cua_user) ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua]) se establece que tiene el parámetro not_delivery_instructions (es decir el parámetro existe) y la información que contiene es una URL válida, entonces se despliega información en este apartado (que tendrá una validación de lectura por parte del usuario para seguir adelante con el proceso) 
&#160; 
 Ejemplo &#58; 
 Para la cuenta &quot;exito&quot; se evalúa su respectiva configuración con el siguiente llamado&#58;&#160; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Dado que el parámetro &quot; not_delivery_instructions &quot; tiene registrada una URL válida entonces se despliega el apartado de &quot;instrucciones ante una no entrega&quot;. 
&#160; 
 Si por ejemplo el usuario es de la cuenta &quot;colombia&quot;&#160; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 dado que la misma no tiene el parámetro &quot; not_delivery_instructions &quot; se pasa directamente a la sección &quot;Registro de la no entrega&quot; 
&#160; 
 Instrucciones ante una no entrega 
 El sistema debe mostrarle al usuario lo siguiente. 
 &quot;Para evitar que su donación no te sea entregada, te pedimos el favor que leas con detenimiento y apliques las indicaciones que te entregamos en el siguiente vínculo&quot; 
&#160; 
 El sistema despliega un botón que debe llevar a la URL registrada en el parámetro &quot; not_delivery_instructions &quot; .&#160; Una vez se le de Click a este artículo, se debe desplegar la siguiente pregunta&#58; 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el caso de la cuenta &quot;exito&quot; esta es la URL que debe desplegarse en &quot;siguiente vínculo&quot; 
&#160; 
 https&#58;//eatcloud.zendesk.com/hc/es-419/articles/360044685832 (que es la URL que está en &quot; not_delivery_instructions &quot; de la CUA Respectiva (que se obtiene de la consulta&#58; *+*NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Cuando el usuario abra el vínculo, la App debe desplegar este mensaje&#58; 
&#160; 
 &quot;Leiste y aplicaste las instrucciones para evitar que no te entreguen la donación&quot; 
&#160; 
 Si &#160; No 
&#160; 
 Si el usuario selecciona &quot;NO&quot; se le debe desplegar de nuevo el botón para que ingrese a la URL registrada en &quot; not_delivery_instructions &quot; y posteriormente se le debe repetir la misma pregunta. 
&#160; 
 Si el usuario selecciona la opción &quot;Si&quot; se pasa a la sección de &quot;Registro de no entrega&quot; 
&#160; 
 Datos para comunicación con soporte&#160; 
 Se cambia el Número de WhatsApp de esta funcionalidad a el que se obtiene en el parámetro&#58; eatc_doma_wa que se obtiene de la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_doma_wa 
&#160; 
 Ejemplo&#58; 
 En ambiente productivo para la CUA_master &quot;abaco&quot; se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp= eatc_doma_wa &#160; &#160; 
&#160; 
 Por lo tanto (siendo 17 de mayo de 2024) se toma el dato eatc_doma_wa&#58; 573239023235&#160; para construir el mensaje (como se ejemplariza en el vínculo &quot;agentes de soporte&quot; presentado más adelante. 
&#160; 
 El sistema debe desplegar el siguiente mensaje&#58; 
 Comunícate con nuestro helpdesk y/o con nuestros agentes de soporte , que haremos lo que esté a nuestro alcance para que te sea entregada tu donación. 
&#160; 
 Nota &#58; las dos URLs están programadas en este CMS.&#160; La URL a WhatsApp&#160; (agentes de soporte que apunta a https&#58;//api.whatsapp.com/send?phone= &#123;&#123; eatc_doma_wa &#125;&#125; &amp;text=Voy%20para%20%24eatc_dona_headers.eatc-pod_name%20por%20el%20anuncio%20con%20eatc-code%20%24eatc_dona_headers.eatc-code%20y%20ese%20punto%20ultimamente%20ha%20presentado%20problemas%20entregando%20anuncios) debe incorporar información del Punto de donación ($eatc_dona_headers. eatc-pod_name o %24eatc_dona_headers.eatc-pod_name) y el código de la donación ($eatc_dona_headers. eatc-code o %24eatc_dona_headers.eatc-code ), Como se indica en el vínculo, pero que se genere de manera dinámica con los datos del anuncio. 
&#160; 
 ***NUEVO &#58; habilitar funcionalidad de registro de no entrega *** 
 En el mismo cuadro de diálogo que se habilita en la funcionalidad &quot;Tengo problemas para que me entreguen&quot;, se debe habilitar un nuevo botón que de entrada a la funcionalidad de &quot;Registro de no entrega&quot;, 
 &#160; 
 class= lbl_registro_no_entrega 
&#160; 
 ***NUEVO&#58; Llamado al API pública para enviar un mensaje de notificación ante una no entrega *** 
 Con la siguiente información, el sistema realiza el llamado al API correspondiente &#58; 
&#160; 
 cua_master = &#123;&#123;eatc_dona_headers. eatc_cua_master &#125;&#125; 
 eatc_user &#160; =&#160; &#123;&#123;usuario_logueado_en_la_app&#125;&#125; 
 eatc_doma_id =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125; 
 eatc_doma =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125; 
 eatc_dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
 ***NUEVO&#58; eatc_state_2 = not_delivered_registered_by_doma 
&#160; 
 Endpoints=&gt; documentados aquí 

&#160; 
 R EGISTRO DE NO ENTREGA 
 El sistema debe permitir realizar el registro de la no entrega, desplegando un formulario de captura de información, y con ello realizar un registro en &quot; eatc_checkin_and_deliver_issues &quot; y hacerle el cambio de estado al anuncio (con el respectivo registro en el historial de estados). 
&#160; 
 El formulario posee los siguientes campos de captura&#58; 
&#160; 
 Motivo de no entrega&#58; ***Nuevo &#58; incorporar causal “otra&quot; y captura de “cuál” *** &#160; 
 Tipo de dato &#58; sting 
 Tipo de input de datos&#58; dropdown único 
 Valor por defecto &#58; vacío 
 Obligatoriedad &#58; si 
 Validación &#58; obligatoriedad 
 La información se toma de (maestro)&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/api/eatcloud/eatc_not_deliver_causes?_id=_*&amp;_cmp= eatc-issue_cause_code &#160; 
 ***ACTUALIZACION&#58; 
 Esta tabla se ha modernizado con el nombre de “not_deliver_causes”, para consultarla seguir las reglas de consulta de consultas públicas . 
 *Los labels de las causas corresponden a los códigos de las causas como clases 
 ***Nuevo&#58; El formulario deberá incorporar la causal “otra” que al ser seleccionada despliega un cuadro de texto obligatorio para capturar&#58; “Cuál”. &#160;Esta causal (la que se digita en “cuál” se debe guardar en una persistencia que permita eventualmente pasarla a &#123;&#123;URL_donantes&#125;&#125;/api/eatcloud/eatc_not_deliver_causes 
 Se guarda en &#58; 
Registro de problemas de checkin y despacho&#58; eatc_checkin_and_deliver_issues .eatc-issue_cause. Más adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es&#160; wrongly_delivered y cuando es diferente a wrongly_delivered . 
&#160; 
 ¿A qué organización se la entregaron?&#58; 
 [Despliegue condicionado] 
&#160; 
 Despliegue condicionado&#58; se despliega si en el selector anterior se realizó la siguiente elección&#58; eatc_not_deliver_causes .eatc-issue_cause_code= wrongly_delivered 
 Tipo de dato &#58; sting compuesto (el auto selector se llena con el&#160; dato organizacin y se obtiene con él tamién el dato identificador_unico_registro 
 Tipo de input de datos&#58; texto predictivo 

 De donde toma los datos para realizar el texto predictivo &#58;&#160; 
&#160; 
 Con el ánimo de reducir el universo de datos posibles a uno que sea razonable, se realiza una consulta para traer los puntos de donación que estén a máximo 150 KM del punto de donación utilizando los siguientes datos&#58; 
&#160; 
 table = constante para esta funcionalidad&#58; eatc_donation_managers 
 fieldname = constante para esta funcionalidad&#58; coordenadas 
 fieldvalue = se toman los datos de eatc_dona_headers. eatc-lat y eatc_dona_headers. eatc-lon y se colocan separados por comas 
 howfield = constante para esta funcionalidad&#58; identificador_unico_registro,organizacin,eatc_state 

 km = constante para esta funcionalidad&#58; 150 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/get/&#123;&#123;_DOM. cua_master &#125;&#125;/getpuntos?table=eatc_donation_managers&amp;fieldname=coordenadas&amp;fieldvalue=&#123;&#123;eatc_dona_headers. eatc-lat &#125;&#125;,&#123;&#123;eatc_dona_headers. eatc-lon &#125;&#125;&amp;showfield=identificador_unico_registro,organizacin&amp;km=150 
&#160; 
 De la información que se recupera en la consulta solo se debe llevar al texto predictivo aquellos registros cuyo eatc_state sea “ activo ” 
&#160; 
 Ejemplo &#58; ambiente de pruebas para un anuncio cuyas coordenadas son eatc-lat=6.2049127 y eatc-lon=-75.59999 
 https&#58;//devbeneficiarios/get/abaco/getpuntos?table=eatc_donation_managers&amp;fieldname=coordenadas&amp;fieldvalue=6.2049127,-75.59999&amp;showfield=identificador_unico_registro,organizacin,eatc_state&amp;km=150 &#160; 
&#160; 
 Valor por defecto &#58; vacío 
 Obligatoriedad &#58; no 
 Validación &#58; que los datos guardados correspondan a unos que hallan sido traídos en la consulta de datos para la función de autocompletar 
 Se guarda en (si hay un registro válido) &#58; 
Registro de problemas de checkin y despacho&#58; identificador_unico_registro se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_code y organizacin se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_name. Más adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es&#160; wrongly_delivered 
 Actualización de datos del encabezado de anuncio de donación&#58; con los datos capturados se realiza el proceso de actualización de datos del encabezado que se detalla más adelante cuando la causa es&#160; wrongly_delivered . 

&#160; 
 ¿A qué hora le entregaron a la otra organización?&#58; 
 [Despliegue condicionado] 
&#160; 
 Despliegue condicionado&#58; se despliega si en el selector anterior se realizó la siguiente elección&#58; eatc_not_deliver_causes .eatc-issue_cause_code= wrongly_delivered 
 Tipo de dato &#58; datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 Tipo de input de datos&#58; datetime picker 
 Valor por defecto &#58; 
 Obligatoriedad &#58; no 
 Validaciones &#58; 
 Se guarda en &#58; 
 Actualización de datos del encabezado de anuncio de donación (eatc_dona_headers) con los datos capturados se realiza el proceso de actualización de datos del encabezado que se detalla más adelante cuando la causa es&#160; wrongly_delivered .. 

 Actualización de información cuando la causa es diferente a wrongly_delivered 
&#160; 
 Cuando el causar de la no entrega de la donación es diferente a &quot; wrongly_delivered &quot;, se procede a realizar el cambio de estado en el encabezado de anuncio de donación a &quot; not_delivered &quot;, el respectivo registro en el historial de estado, y el registro del Issue en &quot; eatc_checkin_and_deliver_issues &quot; 
&#160; 
 Registro en eatc_checkin_and_deliver_issues cuando la causa es diferente a wrongly_delivered&#58; 
&#160; 
 Se hace el registro de un issue, por la no entrega de la donación de la siguiente manera&#58; 
&#160; 
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
 eatc-token &#58; por el momento se deja vacío. En un futuro será la clave criptográfica para decodificar el código de verificación (que se enviará encriptado). 
 eatc-dona_final_state &#58; se registra &quot; not_delivered &quot; 
 eatc-issue_cause_code &#58; se toma de a partir de la información del selector respectivo de la funcionalidad eatc-issue_cause_code 
 eatc-issue_cause &#58; se toma de a partir de la información del selector respectivo de la funcionalidad eatc-issue_cause 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration 
 resolved &#58; se coloca en este punto&#58; si 
&#160; 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=insert&amp; eatc-date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125; &amp; eatc-datetime =&#123;&#123;fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; eatc-donor =&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp; eatc-pod_id =&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&amp; eatc-pod_name =&#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-donation_manager_code =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp; eatc-donation_manager_name =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-final_doma_code =&quot;&quot;&amp; eatc-final_doma_name =&quot;&quot;&amp; eatc-dona_initial_state =&#123;&#123;atc_dona_headers. eatc-state &#125;&#125;&amp; eatc-verification_code =&quot;&quot;&amp; eatc-token =&quot;&quot;&amp; eatc-dona_final_state = not_delivered &amp; eatc-issue_cause_code =&#123;&#123; eatc-issue_cause_code &#125;&#125;&amp; eatc-issue_cause =&#123;&#123; eatc-issue_caus &#125;&#125;&amp; eatc-log =app_automated_issue_registration&amp; resolved =si 
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
 Actualización de información de encabezados de donación cuando la causa es diferente a wrongly_delivered ***REVISAR dinamismo a partir de _DOM.cua_master***&#58; 
 Al accionar este botón el sistema debe realizar la siguiente labor, mediante el API&#58; registrar la fecha y hora de salida ( eatc-picking_checkout_datetime ) y cambiar el estado a &quot;delivered&quot; en el respectivo encabezado ( eatc_dona_headers ) 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers &amp;_operacion= update &amp;eatc-state= not_delivered &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; ( el parámetro que se envia en el WHEREeatc-code es el código de la donación que se está marcando como no entregada ) 
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
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es diferente a wrongly_delivered&#160; ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 Para el registro del estado &quot; not_delivered &quot; se toma la fecha fecha y hora actual (current_datetime) y el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues”) , para llevarlo al respectivo log, realizando el siguiente llamado al CRD 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp;eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;eatc-state= not_delivered &amp;eatc-date_time=&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125;&amp;eatc-log=&#123;&#123;eatc_checkin_and_deliver_issues. eatc-issue_cause_code &#125;&#125;&#58;&#123;&#123;eatc_checkin_and_deliver_issues. eatc-issue_cause &#125;&#125; 
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

 Actualización de información cuando la causa es wrongly_delivered 
 Cuando el causal de la no entrega de la donación es&#160; &quot; wrongly_delivered &quot;, se procede a realizar el respectivo registro del Issue en &quot; eatc_checkin_and_deliver_issues &quot; a realizar el cambio de estado en el encabezado de anuncio de donación a &quot; not_delivered &quot; con el correspondiente registro en el historial de estados en el historial de estado, y el registro.&#160; Para hacer estos cambios se debe tomar en cuenta si se entegó o no información del donante al que se le entregó y de cuándo se entrego. 
&#160; 
 Registro en eatc_checkin_and_deliver_issues cuando la causa es wrongly_delivered&#58; 
&#160; 
 Se hace el registro de un issue, por la no entrega de la donación de la siguiente manera&#58; 
&#160; 
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
 eatc-final_doma_code&#58; 
 Si el usuario NO entregó información sobre a quién le entregaron la donación , se deja vacío . o en cero 
 Si el usuario entregó información información de a quién le entregaron la donación se coloca dicha información correspondiente al dato identificador_unico_registro de dicha captura. 
 eatc-final_doma_name&#58; 
 Si el usuario NO entregó información sobre a quién le entregaron la donación , se deja vacío . 
 Si el usuario entregó información información de a quién le entregaron la donación se coloca dicha información correspondiente al dato&#160; organizacin de dicha captura. 
 eatc-dona_initial_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-verification_code&#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token &#58; por el momento se deja vacío. En un futuro será la clave criptográfica para decodificar el código de verificación (que se enviará encriptado). 
 eatc-dona_final_state &#58; 
 Si el usuario NO entregó información de la organización que recibió la donación se coloca &quot; not_delivered &quot;. 
 Si el usuario entregó información de la organización que recibió la donación se coloca &quot; delivered &quot;. 
 eatc-issue_cause_code &#58; se coloca&#160; wrongly_delivered 
 eatc-issue_cause &#58; se coloca Entregaron a otra fundación 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration 
 resolved &#58; 
 Si el usuario NO entregó información de la organización que recibió la donación se coloca &quot; no &quot;. 
 Si el usuario entregó información de la organización que recibió la donación se coloca &quot; si &quot;.&#160; 
&#160; 
 Escritura con la API (METODO POST)&#58;&#160;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=insert&amp; eatc-date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125; &amp; eatc-datetime =&#123;&#123;fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; eatc-donor =&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp; eatc-pod_id =&#123;&#123; eatc_dona_headers. eatc-pod_id &#125;&#125;&amp; eatc-pod_name =&#123;&#123;eatc_dona_headers. eatc-pod_name &#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-donation_manager_code =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp; eatc-donation_manager_name =&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-final_doma_code =&#123;&#123; eatc-final_doma_code &#125;&#125;&amp; eatc-final_doma_name =&#123;&#123; eatc-final_doma_name &#125;&#125;&amp; eatc-dona_initial_state =&#123;&#123;atc_dona_headers. eatc-state &#125;&#125;&amp; eatc-verification_code =&#123;&#123;eatc_dona_headers. eatc-verification_code &#125;&#125;&amp; eatc-token =&quot;&quot;&amp; eatc-dona_final_state =&#123;&#123; eatc-dona_final_state &#125;&#125;&amp; eatc-issue_cause_code = wrongly_delivere &amp; eatc-issue_cause =Entregaron%20a%20otra fundación&amp; eatc-log =app_automated_issue_registration&amp; resolved =&#123;&#123; resolved &#125;&#125; 
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
 Actualización de información de encabezados de donación cuando la causa es wrongly_delivered&#58; 
 De acuerdo a la información suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en , eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualización de información del anuncio en el respectivo encabezado ( eatc_dona_headers ) 
&#160; 
 Parámetros_a_actualizar 
 eatc-state&#58; se toma la información del anterior registro de issue así eatc_checkin_and_deliver_issues. eatc-dona_final_state 
 eatc-verification_code&#58; se toma la información del anterior registro de issue así eatc_checkin_and_deliver_issues. eatc-verification_codeeatc-verification_code 
 eatc-adjudication_datetime&#58; se toma la información del anterior registro de issue así eatc_checkin_and_deliver_issues. eatc-datetime 
 eatc-donation_manager_user_doc_id&#58; &#160; se deja = &quot;0&quot; 
 eatc-donation_manager_code&#58; se toma la información del anterior registro de issue así eatc_checkin_and_deliver_issues. eatc-final_doma_code 
 eatc-donation_manager_name&#58; &#160; se toma la información del anterior registro de issue así eatc_checkin_and_deliver_issues. eatc-final_doma_name 
 eatc-donation_manager_address&#58; si el dato que se incorporó en el anterior campo es diferente de &quot;0&quot; o &quot;vacío&quot; se utiliza para ir al maestro de gestores de donación (enviando ese dato al parámetro &quot; identificador_unico_registro &quot;) para traer el dato &quot; unidad_territorial &quot;.&#160; La consulta que se hace es la siguiente 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro= eatc-donation_manager_code 
 eatc-donation_manager_phone&#58; utilizando la misma consulta anterior se coloca el dato recuperado en el parámetro &quot; telefono1 &quot;. 
 eatc-donation_manager_typology_a&#58; utilizando la misma consulta anterior se coloca el dato recuperado en el parámetro &quot; organizacion_vinculada &quot;. 
 eatc-donation_manager_typology_b&#58; utilizando la misma consulta anterior se coloca el dato recuperado en el parámetro &quot; eatc_doma_typology_b &quot;. 
 eatc-donation_manager_typology_c&#58; utilizando la misma consulta anterior se coloca el dato recuperado en el parámetro &quot; tipo_organizacion &quot;. 
 eatc-scheduling_datetime&#58; se deja = &quot;0&quot; 
 eatc-programed_picking_datetime&#58; se toma el dato provisto en el selector&#58;&#160; ¿ A qué hora le entregaron ? de la presente funcionalidad. . Si no se obtuvo dato en ese selector se coloca la fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 eatc-picker_name&#58; se deja = &quot;0&quot; 
 eatc-picker_doc_id&#58; se deja = &quot;0&quot; 
 eatc-picker_license_plate&#58; se deja = &quot;0&quot; 
 eatc-picker_start_datetime&#58; se deja = &quot;0&quot; 
 eatc-picker_lat&#58; se deja = &quot;0&quot; 
 eatc-picker_lon&#58; se deja = &quot;0&quot; 
 eatc-picking_checkin_datetime&#58; se toma el dato provisto en el selector&#58;&#160; ¿ A qué hora le entregaron ? de la presente funcionalidad. Si no se obtuvo dato en ese selector se coloca la fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/ crd /&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers &amp;_operacion= update &amp;&#123;&#123;Parámetros_a_actualizar&#125;&#125;&amp; WHEREeatc-code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; ( el parámetro que se envia en el WHEREeatc-code es el código de la donación que se está marcando como no entregada ) 
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

&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es wrongly_delivered&#160; 
&#160; 
 Para el registro del estado en &quot; eatc_checkin_and_deliver_issues. eatc-dona_final_state &quot; se toma la fecha fecha y hora actual (current_datetime) y el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues”) , para llevarlo al respectivo log, realizando el siguiente llamado al CRD 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state =&#123;&#123;eatc_checkin_and_deliver_issues. eatc-dona_final_state &#125;&#125;&amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log =&#123;&#123;eatc_checkin_and_deliver_issues. eatc-issue_cause_code &#125;&#125;&#58;&#123;&#123;eatc_checkin_and_deliver_issues. eatc-issue_cause &#125;&#125; 
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

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 ace5158b-76cb-4643-a5bc-37cdd2c33e38 
 3!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 9d626af3-baeb-4e20-bcc0-4396f2c7cdcf 
 2025-10-28T05:06:53.4175211Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"173594ba-2bcd-4f10-a530-22e6b14b9f9f","SequenceId":872,"FluidContainerCustomId":"62cdb98b-b24c-4bac-822a-70aedd344f4e","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 TENGO PROBLEMAS PARA QUE ME ENTREGUEN