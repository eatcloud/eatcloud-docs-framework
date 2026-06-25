# programdona-proceso-para-la-programación-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica como respuesta a problemas de seguridad que se han detectado en la plataforma, en dónde redes organizadas de delincuentes, roban u obtienen de manera irregular accesos de fundaciones y programan recogidas con conductores y placas (identificadas) de manera fraudulenta, violando las políticas de la plataforma.&#160; Por lo tanto se debe crear un servicio con pautas de seguridad, que permita a la aplicación programar un anuncio donación de forma segura.&#160; El servicio se deberá implementar como una API Pública, siguiendo los lineamientos de la primera implementación al respecto. &#160; Para ello se ha desarrollado una documentación que establece el respectivo EndPoint, y los parámetros con los cuales se invoca el servicio y las respuestas que debe entregar&#160;&#160; 
&#160; 
 Documentación de API pública para programación de donaciones 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 

 ESTRUCTURAS DE DATOS PARA VALIDACIÓN Y CONSULTA 
&#160; 
 En la presente documentación se establecen tres estructuras de datos, cuya denominación no es semántica y cuyos campos no son semánticos (para dificultar su lectura por parte de un tercero).&#160;&#160; 
&#160; 
 Lista negra de dispositivos 
 En esta estructura de datos se registran dispositivos desde los cuales se intentó programar una recolección con un individuo presente en la lista negra, se utilizará también en este proceso como una especie de error handler del proceso de consulta de recolectores (que se invoca de manera previa a este servicio) 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/ api/eatcloud/eatc_ims?_id=_* 
&#160; 
 A continuación se muestran los campos de la estructura de datos, con el ánimo de configurar la respectiva clave primaria del repositorio 
&#160; 
 cua_master &#58; &quot;Cuenta maestra&quot; , 
 imei &#58; &quot;IMEI del dispositivo&quot; , =&gt; CLAVE PRIMARIA 
 pa &#58; &quot;doc_id en lista negra que se intentó registrar&quot; , 
 pk &#58; &quot;Placa en lista negra que se intentó registrar&quot; , 
 dt &#58; &quot;timestamp&quot; , 
 eatc_doma_user_email &#58; &quot;Correo electrónico del usuario de la App&quot; , 
 eatc_doma_id &#58; &quot;Documento de identidad de la institución beneficiaria&quot; , 
 eatc_pod_id &#58; &quot;Identificador del punto de donación&quot; , 
 eatc_cua_origin &#58; &quot;Cuenta usuario del punto de donación&quot; , 
 eatc_dona_header_code &#58; &quot;Código del anuncio de donación&quot; 

&#160; 
 Registro de recolectores 
&#160; 
 En esta estructura se registrarán los recolectores propuestos por los gestores de donación y que pasan el proceso de validación contra la lista negra.&#160; Se implementa para tener más información sobre estas personas que brindan servicios a la comunidad EatCloud 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/ api/eatcloud/eatc_mv?_id=_* &#160; 
&#160; 
 A continuación se muestran los campos de la estructura de datos, con el ánimo de configurar la respectiva clave compuesta del repositorio 

&#160; 
 cua_master &#58; &quot;Cuenta maestra&quot; , =&gt; CLAVE COMPUESTA 
 cua_user &#58; &quot;Cuenta usuario&quot; , =&gt; CLAVE COMPUESTA 
 imei &#58; &quot;IMEI del dispositivo&quot; , =&gt; CLAVE COMPUESTA 
 n0k &#58; &quot;nombre del recolector autorizado&quot; , 
 pa &#58; &quot;Doc id autorizado&quot; , =&gt; CLAVE COMPUESTA 
 pk &#58; &quot;Placa autorizada&quot; , =&gt; CLAVE COMPUESTA 
 dt &#58; &quot;timestamp&quot; , 
 uz &#58; &quot;Empresa de transporte&quot; , 
 uzik &#58; &quot;Documento de identificación Empresa de transporte&quot; , =&gt; CLAVE COMPUESTA 
 nv &#58; &quot;Observaciones&quot; , 
 eatc_doma_id &#58; &quot;Documento de identificación de la organización beneficiaria que realiza la consulta&quot; =&gt; CLAVE COMPUESTA 
&#160; 
 NOTA IMPORTANTE&#58; Para la elaboración de esta documentación, en la anterior estructura se presentan datos sin encripción, y se ejemplifican llamados a API bajo esa premisa; pero para la implementación de la funcionalidad se deberán encriptar todos los datos de dichas estructuras y realizar llamados con los servicios de consulta a datos encriptados respectivos. 

 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 retry 

 1. VALIDACIÓN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación de la API Pública . Si lo son, seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIÓN DEL DISPOSITIVO EN LISTA NEGRA DE DISPOSITIVOS 
 Con el dato que llega en el parámetro&#58; 
 imei 
&#160; 
 El sistema deberá consultar si existe un registro en la estructura de datos de lista negra de placas y conductores 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_ims?imei=&#123;&#123; imei &#125;&#125; 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 
&#160; 
 Si la consulta arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Si la consulta no arroja respuesta el sistema sigue con el siguiente paso&#58; 

 3. VALIDACIÓN DEL CÓDIGO DE LA ORGANIZACIÓN (PARA EVITAR PROGRAMACIONES CRUZADAS) 
 Se detectó un caso en donde una organización que se adjudicó una donación, afirma que fué programada por otra.&#160; Al revisar esa organización, parece ser una organización activa en EatCloud, y por lo tanto se puede estar observando un bug que permitió realizar esta programación de manera no adecuada.&#160; Por lo tanto el proceso tendrá una validación para establecer si los datos de la organización que está programando, corresponden a los datos de la organización a la cual se le asignó la donación.&#160; Si los datos no corresponden, el servicio deberá responder con un error y no permitir la programación.&#160; 
&#160; 
 El sistema con los datos que llegan en la invocación del servicio 
&#160; 
 eatc_cua_master 
 eatc_doma_id &#160; 
 eatc_dona_header_code &#160; 
&#160; 
 Realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_doma_id &#125;&#125;&amp;_cmp=eatc-code 

&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta el sistema sigue con el siguiente paso&#58; 

 4. CONSULTA EN EL REGISTRO DE RECOLECTORES &#58; CONSULTA DEL TELÉFONO DEL RECOLECTOR 
&#160; 
 El sistema con el&#160; siguiente dato que llega en la invocación del servicio 
 eatc_collector_id 
&#160; 
 Realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_mv? _id =&#123;&#123; eatc_collector_id &#125;&#125;&amp; _cmp = n0k , pa , pk, ktm 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 
&#160; 
 Los datos (desencriptados) obtenidos se guardan en las siguientes variables 
&#160; 
 n0k &#58; &quot;nombre_recolector_autorizado&quot; , 
 pa &#58; &quot;doc_id_autorizado&quot; , 
 pk &#58; &quot;placa_autorizada&quot; 
 ktm&#58; &quot;telefono_recolector&quot; 

&#160; 
 Con estas variables y los demás datos del llamado al servicio se procede a realizar los siguientes pasos 

 5. ACTUALIZACIÓN DE INFORMACIÓN DEL ENCABEZADO DE ANUNCIO DE DONACIÓN ***NUEVO&#58; REGISTRO DEL TELÉFONO DEL RECOLECTOR *** Y ***NUEVO&#58; REGISTRO DE MÚLTIPLES RECOLECTORES *** 
&#160; 
 REGISTRO DE MÚLTIPLES RECOLECTORES&#58;&#160; Se implementará una mejora, que permitirá registrarle a una donación, múltiples recolectores (que funciona para donaciones de más de 10 toneladas, que requieren en algunos casos múltiples camiones para ser recolectadas).&#160; Para ello, el servicio evalúa si hay datos de recolector en el encabezado de donación&#58; si no existen, procede como de costumbre, pero si existe ya&#160; un registro de recolector, procederá a registrar esa información en una estructura de datos alterna 
&#160; 
 Con la información obtenida en la consulta anterior y los datos obtenidos en la invocación del servicio, se procede a realizar la actualización del encabezado de anuncio de donación de la siguiente manera. 
 Validación de fecha y hora de recogida&#160; 
 El sistema establece la cuenta desde la cual se realiza el anuncio&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; _DOM .cua_master&#125;&#125;/eatc_dona_headers?e atc-code =&#123; &#123;eatc_dona_headers .eatc-code&#125;&#125; &amp;_cmp= eatc-donor,eatc-publication_datetime 
&#160; 
 Con el dato obtenido en&#160; &#123;&#123;eatc_dona_headers.eatc-donor&#125;&#125; &#160;el sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123; _DOM .cua_master&#125;&#125;/eatc_timeout_rules?e atc-timeout_name= dona_global_scheduling_timeout &amp;cua= &#123;&#123; eatc_dona_headers .eatc-donor&#125;&#125; &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
 Si la consulta anterior no trae resultados deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&amp; cua= _default &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
Una vez obtenida la fecha máxima para programar según el timeout, que se obtiene al sumar a la fecha y hora que determina el timeout (que para el caso específico es eatc-publication_datetime), los minutos definidos por el timeout&#58; 
&#160; 
 &#160;eatc_dona_headers.&#123;&#123; eatc_timeout_rules . eatc-timeout_from &#125;&#125; +&#160; &#123;&#123; eatc_timeout_rules . eatc-timeout_in_minutes &#125;&#125;),&#160; 
&#160; 
 el sistema deberá obtener las fechas (válidas&#58; si alguna de las fechas está en cero, o por defecto (y por error&#58; si se tiene una fecha anterior al día de publicación, no se deberá tomar en cuenta la fecha con esa característica)&#58; 
&#160; 

 &#160;más próxima de expiración&#160; &#123;&#123;eatc_dona_headers. eatc_closer_expiration_date &#125;&#125;&#160; 

 y de cancelación&#160; &#123;&#123;eatc_dona_headers. eatc-cancellation_datetime &#125;&#125; &#160; 
&#160; 
 del anuncio en cuestión, para compararlas y tomar como fecha máxima de &#160;referencia de programación ( eatc-programed_picking_datetime) , la que resulte más próxima de las tres. Si la fecha que llega por el API es posterior a esta, el sistema deberá tomar como la feca de programación, la que calculó para estamparla en el encabezado. &#160;Si la fecha de programación de recogida, es anterior a la determinada por el sistema, entonces estampará la fecha que le llega del API. 
&#160; 
 ***NUEVO &#58;&#160;Validación&#58; fecha y hora de recogida programada dentro de los horarios de atención del punto de donación 
 El sistema deberá validar que la fecha y hora de recogida programada ( &#123;&#123; eatc-programed_picking_datetime &#125;&#125; , se encuentre dentro de los horarios de atención del POD en cuestión. &#160;Si la fecha y hora programada de recogida no está dentro de los horarios de atención el servicio debe retornar un mensaje de error, que le indique a la APP que la fecha y hora de programación está por fuera de los horarios de atención del POD (que se deben consultar en la estructura modernizada&#58; pods_schedules ). 
&#160; 
 fail_programed_picking_datetime_out_of_ pods_schedules 
&#160; 
&#160; 
 ***NUEVO&#58; validación de la existencia previa de un registro en el encabezado *** 
 El sistema validará si en el registro del encabezado, ya existe un registro previo de datos de recolector realizando una consulta de este tipo&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc-picker_name=_vacio 
&#160; 
 Si la consulta arroja una respuesta válida (es decir está vacío el nombre del recolector en el encabezado) 
&#160; 
 El sistema funciona tal cual viene funcionado, creando lo que sería el primer registro de datos del recolector en el encabezado de donación (que a partir de la fecha podrá ser múltiple, es decir una donación podrá tener múltiples recolectores). 
&#160; 
 &#123;&#123; parámetros_update_CRD &#125;&#125; 
&#160; 
 eatc-scheduling_datetime =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se programa la recogida (es decir la fecha y la hora en que corre el presente proceso)&quot; 
 eatc-state = scheduled &#160; =&gt; Constante&#58; el estado debe cambiar de &quot;awarded&quot; a &quot;scheduled&quot; =&gt; Se debe implementar una manera de prohibir este cambio por el CRD normal y permitirlo solamente a través de este proceso. Esta prohibición se debe implementar posteriormente a la implementación del servicio (según tarea en el ASANA).&#160; Se nombra aquí para que sea tenida en cuenta. 
 eatc-programed_picking_datetime =&#123;&#123; eatc-programed_picking_datetime &#125;&#125; =&gt; fecha de recogida programada por el usuario, enviada como parámetro de invocación del servicio. 
 eatc-picker_name =&#123;&#123; nombre_recolector_autorizado &#125;&#125; =&gt; Consultado en el paso anterior 
 eatc-picker_doc_id =&#123;&#123; doc_id_autorizado &#125;&#125; =&gt; Consultado en el paso anterior 
 eatc-picker_license_plate =&#123;&#123; placa_autorizada &#125;&#125; =&gt; Consultado en el paso anterior 
 eatc_picker_phone = &#123;&#123;telefono_recolector&#125;&#125; =&gt; Consultado en el paso anterior 
&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; eatc_cua_master &#125;&#125; =&gt; Cuenta maestra, enviada como parámetro de invocación del servicio. 
 eatc_dona_header_code=&#123;&#123;eatc_dona_header_code&#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 

&#160; 
 Actualización del eatc_dona_headers con el CRD&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; &#123;&#123; parámetros_update_CRD &#125;&#125; 
 &amp;WHEREeatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125; 
&#160; 
 Si la consulta NO arroja una respuesta válida (es decir ya hay un recolector registrado en el encabezado)&#58; ***NUEVO&#58; registro de múltiples recolectores *** 
 El sistema permitirá el registro de múltiples recolectores, utilizando una estructura de datos alternativa para ello, de la siguiente manera. 
&#160; 
 &#123;&#123; parametros_insert_CRD &#125;&#125; 
&#160; 
 cua_master = &#123;&#123; eatc_cua_master &#125;&#125; =&gt; Cuenta maestra, enviada como parámetro de invocación del servicio. 
 eatc_dona_header_code=&#123;&#123;eatc_dona_header_code&#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 
 eatc-scheduling_datetime =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se programa la recogida (es decir la fecha y la hora en que corre el presente proceso)&quot; 
 eatc-programed_picking_datetime =&#123;&#123; eatc-programed_picking_datetime &#125;&#125; =&gt; fecha de recogida programada por el usuario, enviada como parámetro de invocación del servicio. 
 eatc-picker_name =&#123;&#123; nombre_recolector_autorizado &#125;&#125; =&gt; Consultado anteriormente 
 eatc-picker_doc_id =&#123;&#123; doc_id_autorizado &#125;&#125; =&gt; Consultado anteriormente 
 eatc-picker_license_plate =&#123;&#123; placa_autorizada &#125;&#125; =&gt; Consultado anteriormente 
 eatc_picker_phone = &#123;&#123;telefono_recolector&#125;&#125; =&gt; Consultado anteriormente 

&#160; 
 Creación de registro de múltiples recolectores con el CRD&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla=eatc_dona_multiple_pickers&amp;_operacion=insert&amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
&#160; 
 6. REGISTRO DE INFORMACIÓN EN LA TABLA DE HISTORIAL DE LOS ESTADOS DE LOS ANUNCIOS DE DONACIONES ( EATC_DONA_HEADER_STATE_HISTORY )&#160; 
&#160; 
 Se realizará la siguiente inserción de datos en el historial de cambios de estados, variando la estructura de datos, para incorporar nueva información que nos permita tener un mejor seguimiento y controls 

&#160; 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
 eatc_dona_header_code=&#123;&#123;eatc_dona_header_code&#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 
 eatc-state = scheduled &#160; =&gt; Constante 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)&quot; 
 eatc-log = new_process &#160; =&gt; Constante 

&#160; 
 Nuevos parámetros a insertar (hay que crearlos en eatc_dona_header_state_history ) 
 eatc_doma_user_doc_id= &#123;&#123; eatc_doma_user_doc_id &#125;&#125; =&gt; Documento de identidad del usuario que programa, enviado como parámetro de invocación del servicio. 
 imei = &#123;&#123; imei &#125;&#125; =&gt; IMEI del dispositivo, enviado como parámetro de invocación del servicio. 
 eatc_doma_id = &#123;&#123; eatc_doma_id &#125;&#125; =&gt; Documento de identidad de la institución beneficiaria, enviado como parámetro de invocación del servicio. 

&#160; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; eatc_cua_master &#125;&#125; =&gt; Cuenta maestra, enviada como parámetro de invocación del servicio. 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 
&#160; 
&#160; 
 ***NUEVO&#58; envío de correo electrónico ante cambio de estado *** 
 Una vez que el sistema valide que la donación ha sido programada, también validará si existe un registro para envío de correo electrónico por cambio de estado a “scheduled” en la estructura “ eatc_state_change_emails ”, de la siguiente manera&#58; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ?eatc_cua_master= &#123;&#123; cua_master &#125;&#125; &amp;eatc_cua_user= &#123;&#123; eatc_dona_header_code .eatc-donor &#125;&#125; &amp;eatc_pod= &#123;&#123; eatc_dona_header_code .eatc-pod_id &#125;&#125;&amp; eatc_state= scheduled&amp; send_at_specific_time= false 
Si la consulta no arroja una respuesta válida entonces el sistema realizará esta segunda consulta (para establecer si la configuración es para todos los puntos de donación&#160; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_state_change_emails?eatc_cua_master= &#123;&#123; cua_master &#125;&#125; &amp;eatc_cua_user= &#123;&#123; eatc_dona_header_code .eatc-donor &#125;&#125; &amp;eatc_pod= _all &amp; eatc_state= scheduled&amp; send_at_specific_time= false 
Si la consulta no arroja resultados, entonces no se invoca ningún servicio adicional. 
&#160; 
Si la consulta arroja resultados (en cualquiera de sus etapas) con los datos que devuelve el sistema debe proceder a realizar la siguiente invocación &#160;tomando la&#160; &#123;&#123;fecha_hora_actual&#125;&#125; &#160;en formato AAAA-MM-DD HH&#58;MM&#58;SS y el&#160; &#123;&#123;ambiente&#125;&#125; &#58;&#160; dev&#160; para desarrollo o&#160; prd&#160; para producción 
&#160; 
Endponint 
 http&#58;//20.83.146.184/api/v1/webhooks/tLVT1CawoKk7yxRECzvL0/sync &#160; &#160; 
&#160; 
Método&#58;&#160; POST 
&#160; 
Body 
 &#123; 
 &#160; &#160;&#160; &quot;data&quot; &#58; &#160; &#123; 
 &#160; &#160; &#160; &#160;&#160; &quot;rows&quot; &#58; &#160; [ 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#123; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;fecha_hora&quot;&#58; &#160; &quot; &#123;&#123;fecha_hora_actual&#125; &#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#160; &quot;ambiente&quot;&#58;&#160; &quot; &#123;&#123;ambiente&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_master&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_master &#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_user&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_user &#125;&#125;&quot; , 
 &#160;&quot;eatc_email&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_email &#125;&#125;&quot; , 
 &#160;&quot;dona_header_code&quot;&#58; &#160; &quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;pod_id&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_pod &#125;&#125;&quot; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#125; 
 &#160; &#160; &#160; &#160; ] 
 &#160; &#160; &#125; 
 &#125; 
El sistema podrá entregar este tipo de respuestas&#58; 
La donación no existe en estado “scheduled” para el punto de donación en cuestión&#58; 
 &#123; 
 &#160; &#160;&#160; &quot;ok&quot; &#58; &#160; false , 
 &#160; &#160;&#160; &quot;data&quot; &#58; &#160; &#123; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;fecha_hora&quot;&#58; &#160; &quot; &#123;&#123;fecha_hora_actual&#125; &#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#160; &quot;ambiente&quot;&#58;&#160; &quot; &#123;&#123;ambiente&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_master&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_master &#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_user&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_user &#125;&#125;&quot; , 
 &#160;&quot;eatc_email&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_email &#125;&#125;&quot; , 
 &#160;&quot;dona_header_code&quot;&#58; &#160; &quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;pod_id&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_pod &#125;&#125;&quot; 
 &#160; &#160;&#160; &#125;, 
 &#160; &#160;&#160; &quot;message&quot; &#58; &#160; &quot;donation_does_not_exist_for_the_pod_scheduled&quot; , 
 &#160; &#160;&#160; &quot;management_suggestion_message_created&quot; &#58; &#160; false 
 &#125; 
Es un caso que no debería ocurrir, pero en caso de ocurrencia, se debe revisar (dado que funciona como un manejador de errores). 
&#160; 
El punto de donación en cuestión no tiene configurado envío de correo&#58; 
 &#123; 
 &#160; &#160;&#160; &quot;ok&quot; &#58; &#160; false , 
 &#160; &#160;&#160; &quot;data&quot; &#58; &#160; &#123; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;fecha_hora&quot;&#58; &#160; &quot; &#123;&#123;fecha_hora_actual&#125; &#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#160; &quot;ambiente&quot;&#58;&#160; &quot; &#123;&#123;ambiente&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_master&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_master &#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_user&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_user &#125;&#125;&quot; , 
 &#160;&quot;eatc_email&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_email &#125;&#125;&quot; , 
 &#160;&quot;dona_header_code&quot;&#58; &#160; &quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;pod_id&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_pod &#125;&#125;&quot; 
 &#160; &#160;&#160; &#125;, 
 &#160; &#160;&#160; &quot;message&quot; &#58; &#160; &quot;dona_scheduled_email_not_configurated&quot; , 
 &#160; &#160;&#160; &quot;management_suggestion_message_created&quot; &#58; &#160; false 
 &#125; 
Esto quiere decir que no se encontraron los datos de configuración para el envío de correo. &#160;De nuevo, es un caso que no debería ocurrir pero se configura como un manejador de errores 
&#160; 
&#160; 
&#160; 
Se envió mensaje de correo&#58; 
 &#123; 
 &#160; &#160;&#160; &quot;ok&quot; &#58; &#160; true , 
 &#160; &#160;&#160; &quot;data&quot; &#58; &#160; &#123; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &quot;fecha_hora&quot;&#58; &#160; &quot; &#123;&#123;fecha_hora_actual&#125; &#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; &#160; &quot;ambiente&quot;&#58;&#160; &quot; &#123;&#123;ambiente&#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_master&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_master &#125;&#125;&quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;cua_user&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_cua_user &#125;&#125;&quot; , 
 &#160;&quot;eatc_email&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_email &#125;&#125;&quot; , 
 &#160;&quot;dona_header_code&quot;&#58; &#160; &quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot; , 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;pod_id&quot;&#58; &#160; &quot;&#123;&#123;eatc_state_change_emails. eatc_pod &#125;&#125;&quot;, 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&quot;msj_sent_at&quot;&#58; &#160; &quot;&#123;&#123;hora_envio_correo_electronico&#125;&#125;&quot;, 
 &#160; &quot;statusText&quot;&#58; &#160; OK 
 &#160; &#160;&#160; &#125;, 
 &#160; &#160;&#160; &quot;message&quot; &#58; &#160; &quot;dona_scheduled_message_sent&quot; , 
 &#160; &#160;&#160; &quot;management_suggestion_message_created&quot; &#58; &#160; true 
 &#125; 
Este mensaje indica que se envió el correo electrónico para anunciar la programación de la donación al donante (que solicitó que así fuera). 
&#160; 
 --HASTA AQUÍ IMPLEMENTACIÓN INICIAL.&#160; A PARTIR DE AQUÍ PARA TENER EN CUENTA EN FUTURAS IMPLEMENTACIONES --- 
&#160; 
 ****NUEVO&#58; Integración con plataforma delivery si el gestor de donaciones posee el parámetro eatc_delivery=&quot;true&quot; ***&#58;&#160; 
&#160; 
 El sistema deberá evaluar si el beneficiario que&#160; programa la donación, utiliza la app &quot;Delivery&quot; caso en el cual, se procederá a realizar el llamado al servicio de integración respectivo. 
&#160; 
 La evaluación se hace verificando se la cuenta tiene&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identifcador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code&#125;&#125; 
&#160; 
 En caso que la consulta devuelva el siguente parámetro eatc_delivery &#58; &quot;true&quot; , el sistema debe realizar el siguiente llamado al servicio de integración con la plataforma delívery &#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/int/&#123;&#123;_DOM. cua_master &#125;&#125;/int_eatc_delivery?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_operacion=insert 

&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente pruebas, eatc_dona_headers. eatc-donation_manager_code=805025018&#58; 
 Para el anuncio de donación eatc-code &#58; &quot;00002011084217&quot; cuyo eatc-donation_manager_code=805025018 ,el sistema debe realizar la siguiente consulta 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=805025018 
&#160; 
 Como la respuesta de la consulta trae el siguiente parámetro&#58; 
&#160; 
 eatc_delivery &#58; &quot;true&quot; 
&#160; 
 El sistema debe proceder a realizar el siguiente llamado al servicio de integración&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/int/abaco/int_eatc_delivery?eatc_dona_header_code=00002011084217&amp;_operacion=insert &#160; 

&#160; 
 ***REVISIÓN CALIFICACIÓN*** Calificación para el gestor de donaciones que programa la recogida ( _id=2 ) 
 Cuando se presiona el botón &quot; Confirmar programación , el sistema debe realizar un registro de calificación de la siguiente manera&#58; 
&#160; 
 _id &#58; identificador único generado por el sistema, 
 date_time &#58; corresponde a la fecha y hora en la cual se evaluó la calificación, en este caso la fecha&#160; y hora en la cual se realizó la programación ( eatc-scheduling_datetime ). 
 doma_id &#58; Corresponde al código del gestor de donaciones &quot; eatc_dona_headers.eatc-donation_manager_code&quot;. 
 eatc-dona_id &#58; identificador del anuncio de donación &quot; eatc_dona_headers. eatc-id&quot;. 
 action_id &#58; corresponde al identificador de la regla de calificación &quot; eatc_doma_qualification_rules._id&quot; (en este caso&#58; 2). 
 points &#58; corresponde a los puntos de la regla de calificación &quot; eatc_doma_qualification_rules.points&quot; (en este caso&#58; 10). 
 acumulated_points &#58; el sistema debe establecer cual fue el último registro realizado para el gestor de donación y sobre el mismo, se toma el dato &quot;acumulated_points &quot; y le suma los puntos que obtuvo 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donación cuyo eatc-code = 40717 ( eatc-id &#58; &quot;5252095) del ejemplo anterior, con fecha de realización de la programación ( eatc-scheduling_datetime) 2019-09-18 17&#58;00&#58;00. 
 El registro resultante sería&#58; 
&#160; 
 _id &#58; &quot;#####&quot;, 
 date_time &#58; &quot;2019-09-18 17&#58;00&#58;00&quot;, 
 doma_id &#58; &quot;900326456-1&quot;, 
 eatc-dona_id &#58; &quot; 5252095 &quot;, 
 action_id &#58; &quot;2&quot;, 
 points &#58; &quot;10&quot;, 
 acumulated_points &#58; &quot;cálculo de puntos acumulados&quot; 
&#160; 
 Nota sobre el cálculo de puntos acumulados &quot;acumulated_points&quot; &#58; el sistema busca la última calificación registrada para el gestor de donaciones respectivo ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?doma_id=900326456-1 ).&#160; Definiendo el último registro, toma el dato &quot;acumulated_points&quot; y le suma los puntos que obtuvo en esta calificación (10) . 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla= eatc_doma_qualification_registry &amp;_operacion=insert&amp; date_time = 2019-09-18%2017&#58;00&#58;00 &amp; doma_id = 900326456-1 &amp; eatc-dona_id = 5252095 &amp; action_id =2&amp; points =10&amp; acumulated_points = cálculo%20de%20puntos%20acumulados 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925163748&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;15&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Aquí se puede consultar el registro realizado&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_qualification_registry?action_id=2&amp;eatc-dona_id=5252095 &#160;&#160;&#160;&#160; 

 7. VALIDACIÓN DE LA PLACA DEL RECOLECTOR 
&#160; 
 En caso de llegar un dato válido en el campo&#160; 
 lic_plate 
&#160; 
 El sistema deberá consultar si existe un registro en la estructura de datos de lista negra de placas y conductores 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/api/eatcloud/eatc_kms?pk=&#123;&#123; lic_plate &#125;&#125; 
 * Ejemplo de consulta en estructura desencriptada. Al encriptar los datos se deben utilizar los llamados para consulta de datos encriptados. 
&#160; 
 Si la consulta arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Y deberá realizar el respectivo registro en la estructura de Lista Negra de Dispositivos, con los parámetros recibidos de la invocación en la invocación del servicio, de la siguiente manera&#58; 
&#160; 
 &#123;&#123; parámetros_invocación_CRD &#125;&#125; 
&#160; 
 cua_master =&#123;&#123; cua_master &#125;&#125;, 
 imei =&#123;&#123; imei &#125;&#125;, 
 pa =&#123;&#123; doc_id &#125;&#125;, 
 pk =&#123;&#123; lic_plate &#125;&#125;, 
 dt =[ timestamp_realizacion_registro] , 
 eatc_doma_user_email =&#123;&#123; eatc_doma_user_email &#125;&#125;, 
 eatc_doma_id =&#123;&#123; eatc_doma_id &#125;&#125;, 
 eatc_pod_id =&#123;&#123; eatc_pod_id &#125;&#125;, 
 eatc_cua_origin =&#123;&#123; eatc_cua_origin &#125;&#125;, 
 eatc_dona_header_code =&#123;&#123; eatc_dona_header_code &#125;&#125; 

&#160; 
 Llamado al CRD&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/crd/eatcloud/?_tabla=eatc_kms&amp;_operacion=insert&amp;&#123;&#123; parámetros_invocación_CRD &#125;&#125; 
&#160; 
 Una vez se realiza la operación insert, se deberá invocar al servicio de encripción de datos para que los mismos reposen de manera segura en el respectivo repositorio. 

&#160; 
 Si la consulta no arroja respuesta el sistema sigue con la siguiente operación&#58; 

 8. REGISTRO DEL RECOLECTOR 
 Con los parámetros con los cuales se invocaron el servicio, el registro del respectivo recolector como se indica a continuación&#58; 
&#160; 
 &#123;&#123; parámetros_invocación_CRD &#125;&#125; 
&#160; 
 cua_master =&#123;&#123; cua_master &#125;&#125;, 
 cua_user =&#123;&#123; eatc_cua_origin &#125;&#125;, 
 imei =&#123;&#123; imei &#125;&#125;, 
 n0k =&#123;&#123; name &#125;, 
 pa =&#123;&#123; doc_id &#125;&#125;, 
 pk =&#123;&#123; lic_plate &#125;&#125;, 
 dt =[ timestamp_realizacion_registro] , 
 uz =&#123;&#123; company &#125;&#125;, 
 uzik =&#123;&#123; company_doc_id &#125;&#125;, 
 nv = registro_automatico , =&gt; CONSTANTE 
 eatc_doma_id =&#123;&#123; eatc_doma_id &#125;&#125;, 

&#160; 
 Llamado al CRD&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/crd/eatcloud/?_tabla=eatc_mv&amp;_operacion=insert&amp;&#123;&#123; parámetros_invocación_CRD &#125;&#125; 
&#160; 
 Una vez se realiza la operación insert, se deberá invocar al servicio de encripción de datos para que los mismos reposen de manera segura en el respectivo repositorio. 
&#160; 
 De igual manera el servicio deberá responder con el _id del registro recientemente creado&#58; 
 eatc_collector_id =&#123;&#123; _id &#125;&#125; 

 9. ***NUEVO&#58; ENVIO DE CORREO CON DATOS DE PROGRAMACIÓN, AL ENCARGADO DEL PUNTO QUE CREA EL ANUNCIO *** 
&#160; 
 Una vez se han incorporado en la donación los datos de la programación, con los parámetros con los cuales se invocaron el servicio, el sistema realiza las siguientes consultas&#58; 
&#160; 
 Establecimiento de si el punto de donación envía correo con datos de programación al encargado del punto de creación del anuncio 
&#160; 
 El sistema con los datos que llegan en la invocación del servicio 
 eatc_cua_master 
 eatc_dona_header_code &#160; 
&#160; 
 Realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;_cmp= eatc-donor,eatc_dona_creator_pod 
&#160; 
 Con los datos obtenidos, procederá a establecer si el punto creador de la donación posee la configuración que indica que se le envía al encargado un email con la información de la programación, de la siguiente manera 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_dona_headers. eatc_dona_creator_pod &#125;&#125;&amp;_cmp=eatc_program_dona_email 
&#160; 
 Respuesta diferente de &quot;y&quot;, igual a &quot;n&quot;, vacía, nula o el campo no existe. 
&#160; 
 Si el servicio dice que el campo no existe, o que la respuesta es diferente a &quot;y&quot;, es igual a &quot;n&quot;, es nula o es vacía, entonces se procederá a realizar la siguiente validación&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;_cmp=eatc_program_dona_email 
&#160; 
 Respuesta diferente de &quot;y&quot;, igual a &quot;n&quot;, vacía, nula o el campo no existe. 
&#160; 
 Si el servicio dice que el campo no existe, o que la respuesta es diferente a &quot;y&quot;, es igual a &quot;n&quot;, es nula o es vacía, entonces el sistema ha determinado que para el caso particular no se envía correo electrónico 
&#160; 
 Respuesta igual a &quot;y&quot; 
&#160; 
 El sistema determinó que hay que enviar un correo electrónico, como se detalla más adelante. 
&#160; 
 Respuesta igual a &quot;y&quot; 
&#160; 
 El sistema determinó que hay que enviar un correo electrónico, como se detalla más adelante. 

&#160; 
 Consulta de información para el envío del correo electrónico 
&#160; 
 El sistema realiza la siguiente consulta de los datos del anuncio (recien programado), para la construcción del correo eletrónico a enviar&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;_cmp= eatc-donor,eatc_dona_creator_pod,eatc-code,eatc-donation_manager_name,eatc-picker_name,eatc-picker_doc_id,eatc-picker_license_plate,eatc-programed_picking_datetime 
&#160; 
 El sistema realiza tambien la siguiente consulta, para determinar la dirección de correo eletrónico a la cual se enviará el correo 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_dona_headers. eatc_dona_creator_pod &#125;&#125;&amp;_cmp= eatc-email 

&#160; 
 Creación del correo electrónico 
 To&#58; &#123;&#123;eatc_pods. eatc-email &#125;&#125; 
&#160; 
 From&#58; eatcloud_norepy 
&#160; 
 Asunto&#58; Nueva programación de anuncio de donación creado 
&#160; 
 Cuerpo&#58; 
&#160; 
 Código de la Donación&#58;&#160; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Beneficiario quien recoge&#58;&#160; &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125; 
&#160; 
 Persona quien recoge&#58; &#123;&#123;eatc_dona_headers. eatc-picker_name &#125;&#125; Doc_id&#58; &#123;&#123; eatc-picker_doc_id &#125;&#125; 
&#160; 
 Placa de Vehículo&#58; &#123;&#123;eatc_dona_headers. eatc-picker_license_plate &#125;&#125; 
&#160; 
 Fecha y Hora de recolección&#58; &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; 

 DEPRECADO&#58; LLAMADO AL SERVICIO DE INTEGRACIÓN BLOCKCHAIN 
 Nota importante&#58; este llamado debe funcionar tanto para los procesos de programación como los de reprogramación. 
&#160; 
 Endpoint (según documentación ([POST] servicio&#58; frmAgendarDonacion (Programar donación))&#58; sujeto a revisión) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio=frmAgendarDonacion 

&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación recientemente creado&#58; eatc_dona_heaaders. eatc-code =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) =&gt; parámetro de carácter obligatorio 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 eeeb9879-b42a-4ca9-96f1-2b8ad1a866ad 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 0fd13db1-e0d1-44b7-a869-d4428b2b505e 
 2026-02-06T03:35:25.7664778Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"edc0f5c3-b4de-44f8-a845-c0cf377b4313","SequenceId":4185,"FluidContainerCustomId":"12db94f4-f170-43f8-9e70-b47fab75d990","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 PROGRAMDONA: SERVICIO PARA PROGRAMACIÓN DE DONACIONES