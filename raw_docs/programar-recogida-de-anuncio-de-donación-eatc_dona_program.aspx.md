# programar-recogida-de-anuncio-de-donación-eatc_dona_program.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Formulario de captura&#58; 
 El sistema debe presentar un formulario de captura con los siguientes campos y validaciones&#58; 
&#160; 
 Nuevo&#58; validación previa a la programación de la recogida ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Dada la rara circunstancia detectada , que en algunos pocos casos se está permitiendo manipulación doble (dos organizaciones en simultáneo) de una donación, se propone realizar esta validación, antes de hacer el proceso de programación, para garantizar que dicha programación solo pueda ser realizada por la organización a la cual se le adjudicó el anuncio. 
&#160; 
 Antes de realizar el proceso, el sistema debe tomar el eatc_donation_manager.identificador_unico_registro y enviarlo al parámetro &quot;eatc-donation_manager_code&quot; del eatc_dona_headers de la donación en la que se está (es decir en la consulta se envía el eatc-code de la donación también). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-code= &#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_donation_manager. identificador_unico_registro&#125;&#125; &amp;_compress 
&#160; 
 Si la respuesta contiene un resultado, se le deja seguir adelante en el proceso de programación.&#160; Si la respuesta es con un resultado sin conteo (cont &quot;0&quot;) entonces debe salir el siguiente mensaje&#58; 
&#160; 
 La presente donación ya fue adjudicada a otra organización. Te solicitamos seguir pendiente de la nube para acceder a futuras oportunidades. 
&#160; 
 ACEPTAR 
&#160; 
 El botón aceptar debe devolver a la nube de donaciones . 

&#160; 
 Ejemplo _DOM. cua_master=abaco ( tomando como referencia el caso real detectado )&#58; 
&#160; 
 La fundación &quot;FUNDACION PAYASITOS CON ESPERANZA&quot;, con el Identificador único de registro &quot;830903608&quot;, se encontraba (por una muy rara razón que aun no se logra identificar) en el dashboard de la donación eatc-code= colombiaLF4RMQ4qXVPpnKgc8lBya20200509093441354 a las &quot;2020-05-09 18&#58;46&#58;13&quot; y procedió a intentar programar la recogida de la donación. 
 El sistema debió realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= colombiaLF4RMQ4qXVPpnKgc8lBya20200509093441354 &amp;eatc-donation_manager_code= 830903608 &amp;_compress &#160; 
&#160; 
 Como la respuesta fue esta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;200509184613&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.44, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Se le debió desplegar el mensaje arriba descrito (La presente donación ya fue adjudicada a otra organización. Te solicitamos seguir pendiente de la nube para acceder a futuras oportunidades.) y redireccionarla a la nube de donaciones, evitando de esta manera una nueva programación del anuncio ( como ocurrió originalmente ). 

 ***NUEVO&#58; validación previa del dato &quot;eatc_dona_headers&quot;&#58; &quot; eatc_last_p_day &quot; para establecer fecha límite de recogida diferente a lo que se establece con eatc_timeout_rules *** 
&#160; 
 El sistema debe evaluar si existe un dato válido de fecha (en formato AAAA-MM-DD) en eatc_dona_headers. eatc_last_p_day 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM.c ua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_distinct= eatc_last_p_day 
&#160; 
 y&#160; de encontrarlo, debe presentar opción de escoger una fecha y hora que sea máximo para ese día.&#160; 
&#160; 
 De no encontrar un dato válido para eatc_last_p_day (nulo, vacío, o con el dato 0000-00-00) entonces se procederá con el proceso tal como está implementado hasta la fecha. 
&#160; 
 Fecha y hora de recogida ***REVISAR&#58; incorporación del dato de la cua_user desde la cual se genera el anuncio para establecer el timeout *** 
 El sistema establece la cuenta desde la cual se realiza el anuncio&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM.c ua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp= eatc-donor, eatc-publication_datetime 
&#160; 
 Con el dato obtenido en &#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125; el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&amp; cua= &#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125; &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
 Si la consulta anterior no trae resultados deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&amp; cua= _default &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
 ***NUEVO &#58; evaluar también los datos&#58; &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; y &#123;&#123; eatc_dona_headers. eatc-cancellation_datetime &#125;&#125; para determinar la máxima fecha y hora que el usuario debe utilizar para cancelar. *** 
 Una vez obtenido la fecha máxima para programar según el timeout, que se obtiene al sumar a la fecha y hora que determina el timeout (que para el caso específico es eatc-publication_datetime, los minutos definidos por el timeout&#58; eatc_dona_headers. &#123;&#123; eatc_timeout_rules. eatc-timeout_from &#125;&#125; + &#123;&#123; eatc_timeout_rules. eatc-timeout_in_minutes &#125;&#125;), el sistema deberá obtener las fechas (válidas&#58; si alguna de las fechas está en cero, o por defecto (y por error) se se tiene una fecha anterior al día de publicación, no se deberá tomar en cuenta la fecha con esa característica) más próxima de expiración &#123;&#123; eatc_dona_headers. eatc_closer_expiration_date &#125;&#125; y de cancelación &#123;&#123; eatc_dona_headers. eatc-cancellation_datetime &#125;&#125; &#160;del anuncio en cuestión, para compararlas y tomar como referencia para limitar el datetime picker, la que resulte más próxima de las tres (es decir la fecha y hora) que primero ocurre). 
&#160; 
 NOTA IMPORTANTE&#58; esto deberá ser tomado en cuenta también para el proceso de reprogramación del anuncio y es menester hacerlo tanto en legacy como en modernización. 
&#160; 
&#160; 
 Con esta información el sistema debe presentar opción de escoger una fecha y hora que sea máximo el tiempo definido en el timeout particular de la fecha&#160; de publicación del anuncio &quot; eatc-publication_datetime &quot; (limitando el datetime picker para que no pueda seleccionar fechas y horas posteriores a la fecha de publicación del anuncio ( eatc_dona_headers. eatc-publication_datetime ), más el timeout ( eatc_timeout_rules. eatc-timeout_in_minutes )) 

&#160; 
 Ejemplo, _DOM. cua_master=abaco,&#160; donación&#58; eatc-code &#58; &quot;exito3920220726110423320 , ambiente de pruebas&#58; 
 El sistema establece la cuenta desde la cual se realiza el anuncio&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=exito3920220726110423320&amp;_cmp=eatc-donor,eatc-publication_datetime &#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 &#123; 
 eatc-donor &#58; &quot;exito&quot;, 
 eatc-publication_datetime &#58; &quot;2022-07-26 11&#58;05&#58;39&quot; 
 &#125; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&amp;cua=exito&amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
 Como no se obtienen resultados, el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&amp;cua=_default&amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from &#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 &#123; 
 eatc-timeout_in_minutes &#58; &quot;5760&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot; 
 &#125; 
&#160; 
 El sistema no debe permitir que después de ( eatc-timeout_in_minutes ) 5760 minutos contados a partir del ( eatc-timeout_from ) eatc-publication_datetime ( 2022-07-26 11&#58;05&#58;39 ), se pueda programar la recogida de una donación. 

&#160; 
 También debe tomar en cuenta los respectivos horarios de atención del punto de donación, para validar que la fecha y hora estén en el rango de horario de atención. 
&#160; 
 Ejemplo, _DOM. cua_master=abaco&#58; 
&#160; 
 Para el anuncio de donación cuyo eatc-code es &quot; 40716 &quot; ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40716 ), el selector de fecha y hora no debe permitir seleccionar fechas y horas posteriores a &quot;2019-09-19 15&#58;37&#58;54&quot; (dado que &quot; eatc-publication_datetime &quot; es igual a &quot;2019-09-18 15&#58;37&#58;54&quot;). 
 Por otro lado el sistema debe consultar los horarios de atención del respectivo punto de donación&#160; ( eatc-pod_id &#58; &quot;339&quot;) de la siguiente manera&#58; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id=339 &#160; 
&#160; 
 Y no permitir seleccionar horarios que no estén entre la franja de&#58; 07&#58;00&#58;00 a 14&#58;00&#58;00 , dado que los días miércoles y jueves (que son los que caen en las 24 horas posteriores a la fecha de publicación), tienen esa disponibilidad de horario de atención&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339&amp;eatc-day=mi,ju &#160;&#160; 

&#160; 
 Incorporación eatc_cua_origin en la consulta 
&#160; 
 Para realizar la consulta adecuada para cada anuncio de donación, se debe utilizar el parámetro eatc_dona_header. eatc_cua_origin para incorporarlo a la URL que consulta los horarios de atención. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_dona_headers. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 

&#160; 
 Ejemplo&#58; 
&#160; 
 Suponiendo que un anuncio de donación tiene el parámetro eatc_dona_headers. eatc_cua_origin = makro y el eatc_dona_header.eatc_pod es igual a st01 , el sistema deberá realizar la siguiente consulta para traer los horarios de atención&#58; 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/&#123;&#123;eatc_dona_headers. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/&#123;&#123;eatc_dona_headers. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/makro/eatc_attention_schedule?eatc-pod_id=st01 &#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/makro/eatc_attention_schedule?eatc-pod_id=st01 &#160; 

&#160; 
 Y no permitir seleccionar horarios que no estén entre la franja de&#58; 07&#58;00&#58;00 a 14&#58;00&#58;00 , dado que los días miércoles y jueves (que son los que caen en las 24 horas posteriores a la fecha de publicación), tienen esa disponibilidad de horario de atención&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339&amp;eatc-day=mi,ju &#160;&#160; 

 La fecha y hora que se programa en el sistema se debe guardar en la variable&#58; eatc_programed_picking_datetime 

 F ORMULARIO DE CAPTURA DE DATOS DEL RECOLECTOR&#160; 
 ***NUEVO&#58; VALIDACIONES DOC ID *** 
 NOTA IMPORTANTE PARA LAS MEJORAS&#58; En términos generales el formulario deberá funcionar como lo viene haciendo, simplemente que se añadieron validaciones sobre todo en el campo de documento de identidad del recolector.&#160; Por lo demás el formulario debe funcionar de manera idéntica a como lo viene haciendo.&#160; Recomendamos leer la especificación como guía, pero no intervenir mucho el formulario como tal, solo en lo referente a las validaciones del documento de identidad adicionales. 
&#160; 
 El formulario de captura de datos del recolector tiene los siguientes datos 
&#160; 
 Nombre de quien recoge&#58; 
&#160; 
 Tipo de input&#58;&#160; 
 Text field 
&#160; 
 Tipo de dato&#58; 
 &#160; String 
&#160; 
 Obligatoriedad&#58; 
 Si 
&#160; 
 Validación&#58;&#160; 
 Obligatoriedad 
&#160; 
 Se guarda en&#58;&#160; 
 La variable &quot; eatc_picker_name &quot;, que se utilizará posteriormente para llamado a servicios. 

&#160; 
 Documento de identidad de quien recoge&#58; ***NUEVO&#58; validación y tooltip *** 
&#160; 
 Tooltip&#58;&#160; 
 clase = lbl_doc_id_recolector_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_doc_id_recolector_desc )&#160; 
&#160; 
 &quot;Digita el documento de identidad del recolector, utilizando solamente los números&quot; 
&#160; 
 Tipo de input&#58;&#160; 
 Según el tipo de dato que se define a continuación&#58; por ejemplo&#58; si el tipo de dato es &quot; Integer &quot;, el campo de captura deberá ser numérico (desplegando solo el teclado numérico), si es &quot; string &quot; deberá ser alfanumérico (desplegando todo el teclado). 
&#160; 
 Tipo de dato&#58; 
 Para establecer el tipo de dato el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_user_id_data_type 
&#160; 
 Si el sistema no arroja un dato en la anterior consulta por defecto el valor para el tipo de dato será &quot; string &quot; 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; en ambiente de pruebas&#58; 
&#160; 
 El sistema realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp=eatc_user_id_data_type &#160; 
&#160; 
 Como la respuesta es &quot; integer &quot;, entonces el sistema deberá desplegar un teclado de captura numérico para permitir la captura 
&#160; 
 Obligatoriedad&#58; 
 Si. 
&#160; 
 Validaciones&#58;&#160; 
 Obligatoriedad 
 Tipo de dato 
 ***NUEVO&#58; Número mínimo de dígitos *** 
&#160; 
 Para realizar esta validación el sistema debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp=eatc_user_id_min_digit_val 
&#160; 
 Si el sistema no arroja un dato en la anterior consulta por defecto el valor para el número mínimo de dígitos será 6. 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; en ambiente de pruebas&#58; 
&#160; 
 El sistema realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp=eatc_user_id_min_digit_val &#160; 
&#160; 
 Como la respuesta es &quot; 7 &quot;, entonces el sistema deberá validar que el número digitado tenga como mínimo 7 dígitos. Si el usuario digita un número con menos dígitos el sistema deberá desplegar el siguiente mensaje&#58; 
&#160; 
 clase = lbl_doc_id_errado (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_doc_id_errado ) 
&#160; 
 &quot;El documento de identidad digitado está errado. Por favor intenta de nuevo&quot; 
&#160; 
 ***NUEVO&#58; Número máximo de dígitos *** 
&#160; 
 Para realizar esta validación el sistema debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp=eatc_user_id_max_digit_val 
&#160; 
 Si el sistema no arroja un dato en la anterior consulta por defecto el valor para el número mínimo de dígitos será 11. 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; en ambiente de pruebas&#58; 
&#160; 
 El sistema realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp=eatc_user_id_max_digit_val &#160; 
&#160; 
 Como la respuesta es &quot; 10 &quot;, entonces el sistema deberá validar que el número digitado tenga como máximo 10 dígitos. Si el usuario digita un número con más dígitos el sistema deberá desplegar el siguiente mensaje&#58; 
 clase = lbl_doc_id_errado ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_doc_id_errado )&#160; 
&#160; 
 &quot;El documento de identidad digitado está errado. Por favor intenta de nuevo.&quot; 

&#160; 
 Se guarda en&#58;&#160; 
 La variable &quot; eatc_picker_doc_id &quot;, que se utilizará posteriormente para llamado a servicios. 

&#160; 
 Placa del vehículo&#58; 
&#160; 
 Tipo de input&#58;&#160; 
 Text field 
&#160; 
 Tipo de dato&#58; 
 &#160; String 
&#160; 
 Obligatoriedad&#58; 
 No (si se escoge el tipo de transporte &quot;Otro&quot; no es obligatoria.&#160; Si se escoge &quot;carro&quot; o &quot;moto&quot;, si es obligatorio. 
&#160; 
 Validación&#58;&#160; 
 Obligatoriedad condicionada. 
 Se implementaron validaciones diferenciadas por cuenta maestra para validar el formato de la placa.&#160; Estas validaciones se deben preservar 
&#160; 
 Se guarda en&#58;&#160; 
 La variable &quot; eatc_picker_license_plate &quot;, que se utilizará posteriormente para llamado a servicios. 

&#160; 
 ***NUEVO&#58; Teléfono de quien recoge *** 
&#160; 
 label&#58;&#160; 
 clase = lbl_tel_recolector ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_tel_recolector )&#160;&#160; 
&#160; 
&#160; 
 &quot;Teléfono del recolector&quot; 
 Tooltip&#58;&#160; 
 clase = lbl_tel_recolector_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_tel_recolector_desc )&#160;&#160; 
&#160; 
 &quot;Digita un número telefónico de contacto de quien recibirá la donación&quot; 
&#160; 
 Tipo de input&#58;&#160; 
 El tipo de dato es &quot; Integer &quot;, el campo de captura deberá ser numérico (desplegando solo el teclado numérico).&#160; Se le deberá adicionar a la captura el prefijo del teléfono (para facilitar contacto por ejemplo a través de WhatsApp) &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_phone_prefix 

 NOTA &#58; Revisar este código para ver si a partir del mismo se puede realizar el desarrollo&#58; https&#58;//community.unbounce.com/tips-scripts-43/phone-number-field-with-country-code-dropdown-list-6925 &#160; 

 Longitud del dato a capturar&#58; 
 Para establecer la longitud del teléfono a capturar el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_phone_digit_lengh &#160; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; en ambiente de pruebas&#58; 
&#160; 
 El sistema realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp= eatc_phone_digit_lengh &#160;&#160; 
&#160; 
 Como la respuesta es &quot; 10 &quot;, entonces el sistema deberá desplegar un teclado de captura numérico para permitir lacampo de captura de longitud de 10 dígitos para capturar el teléfono (y a este teléfono se le deberá adicionar el prefijo 57 ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_cmp=eatc_phone_prefix,eatc_phone_digit_lengh ) antecedido de un &quot;+&quot; para su funcionamiento con plataformas de comunicación como whatsapp 
&#160; 
 Obligatoriedad&#58; 
 No. 
&#160; 
 Validaciones&#58;&#160; 
 Longitud 
 Tipo de dato (INTEGER) 
 Adición del prefijo 

&#160; 
 Se guarda en&#58;&#160; 
 La variable &quot; eatc_picker_phone &quot;, que se utilizará posteriormente para llamado a servicios. 

 nación y podrá ser adjudicada a otro beneficiario. Contamos con tu celeridad en el proceso.&quot; 
&#160; 
 Botón &quot;Confirmar programación&quot;&#58; funcionamiento con nuevos servicios públicos de consulta de recolector y programación de donaciones *** 
 A diferencia de la implementación previa, al presionar este botón se harán dos llamados a nuevos servicios de la plataforma, que ayudarán a establecer si el conductor que se quiere registrar, no está en una lista negra de conductores no autorizados, y de estar en dicha lista, bloquear el dispositivo desde el cual se está intentando hacer el registro (para evitar programaciones fraudulentas).&#160; Para realizar dichos llamados el sistema deberá en este punto tener a mano las siguientes variables (entre paréntesis se aportan ejemplos que sirven para identificar la procedencia de las variables, pero que no son indicativos de consultas que deben realizarse, dado que las variables pueden ser recolectadas desde procesos anteriores en la APP)&#58; 
&#160; 
 cua_master&#58; _DOM. cua_master 
 imei&#58; Imei del dispositivo.&#160; Este dato, deberá extraerse desde el proceso de login , porque en el futuro podrá requerirse en dicho proceso para validar el dispositivo contra listas negras. 
 eatc_doma_user_email&#58; email del usuario que está logueado en la plataforma ( eatc_users. correo_electronico . Ejemplo&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_users?_id=1&amp;_cmp= correo_electronico ) 
 eatc_doma_user_doc_id&#58; documento de identidad del usuario que está logueado en la plataforma ( eatc_users. numero_cedula . Ejemplo&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_users?_id=1&amp;_cmp= numero_cedula ). 
 eatc_doma_id&#58; Documento de identidad de la Entidad Beneficiaria de la donación particular (eatc_donation_managers. identificador_unico_registro.&#160; Ejemplo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=1&amp;_cmp= identificador_unico_registro ). 
 eatc_dona_header_code &#58; Código de la donación que se está programando (eatc_dona_headers. eatc-code.&#160; Ejemplo&#58; https&#58;//devdonantes.eatcloud.info/api/ abaco/eatc_dona_headers ?_id=77&amp;_cmp= eatc-code ). 
 eatc_pod_id &#58; Identificación del punto de donación desde el cual se realiza la donación en particular(eatc_dona_headers. eatc-pod_id.&#160; Ejemplo&#58; https&#58;//devdonantes.eatcloud.info/api/ abaco/eatc_dona_headers ?_id=77&amp;_cmp= eatc-pod_id ) 
 eatc_cua_origin &#58; Cuenta de usuario desde la cual se realiza la donación (eatc_dona_headers. eatc_cua_origin.&#160; Ejemplo&#58; https&#58;//devdonantes.eatcloud.info/api/ abaco/eatc_dona_headers ?_id=77&amp;_cmp= eatc_cua_origin ) 
 name&#58; nombre del recolector capturado en el formulario anterior (variable &quot; eatc_picker_name &quot;) 
 doc_id&#58; Documento de identidad del recolector capturado en el formulario anterior (variable &quot; eatc_picker_doc_id &quot;) 
 lic_plate&#58; Documento de identidad del recolector capturado en el formulario anterior (variable &quot; eatc_picker_license_plate &quot;) 
 eatc_programed_picking_datetime&#58; Fecha y hora programada para la recolección, realizada en formulario previo al de los datos del recolector (variable &quot; eatc_programed_picking_datetime &quot;). 

 ***NUEVO&#58; eatc_picker_phone&#58; teléfono de contacto del recolector. *** 
&#160; 
 Llamado al servicio &quot;conrec&quot; (para validar datos de los recolectores) 
 Según lo expuesto en la documentación del API Pública para Consulta de Recolectores (en el vínculo se podrá consultar la documentación para realizar el llamado. No se documenta aquí para evitar duplicidad), el sistema deberá hacer un llamado al servicio respectivo (si se desea conocer la naturaleza de dicho servicio puede consultarse aquí ).&#160; Según su respuesta deberá realizar las siguientes acciones&#58; 
&#160; 
 Respuesta exitosa&#58;&#160; se obtiene un eatc_collector_id&#58; El sistema guarda el dato para realizar el llamado al próximo servicio. 
 Respuesta no exitosa&#58; incomplete_data&#58; El sistema deberá validar de nuevo los datos necesarios en el llamado e intentarlo de nuevo 
 Respuesta no exitosa&#58; retry&#58; El sistema deberá reintentar el llamado y desplegarle al usuario un solo toast (con control para que no se despliegue varias veces), con el siguiente label&#58; 
 clase = lbl_reintentando2 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_reintentando2 )&#160;&#160; 
&#160; 
 &quot;Reintentando, espera por favor unos segundos&quot; 
&#160; 
 Respuesta no exitosa&#58; fail&#58; El sistema deberá responder con el siguiente mensaje para posteriormente sacar al usuario de la funcionalidad de programación. 
 clase = lbl_ocurrio_un_problema_007 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_ocurrio_un_problema_007 )&#160;&#160;&#160; 
&#160; 
 &quot;Ocurrió un problema. CODIGO 007&quot; 

&#160; 
 Llamado al servicio &quot;programdona&quot; (para programar donaciones) 
 Según lo expuesto en la documentación del API Pública para la programación de donaciones (en el vínculo se podrá consultar la documentación para realizar el llamado. No se documenta aquí para evitar duplicidad), el sistema deberá hacer un llamado al servicio respectivo (si se desea conocer la naturaleza de dicho servicio puede consultarse aquí , pero básicamente realizará las labores que anteriormente se realizaban desde el dispositivo para programar una donación y llevar a cabo el registro en el historial de estados. Por esta circunstancia los llamados al CRD de eatc_dona_headers y eatc_dona_state_history que se activaban con este botón deberán desactivarse).&#160; Según su respuesta deberá realizar las siguientes acciones&#58; 
&#160; 
 Respuesta exitosa&#58;&#160; se obtienen los siguientes parámetros en la respuesta&#58; 
 eatc_dona_header_code&#58; “ &#123;&#123;valor&#125;&#125;” , 
 eatc-state &#58; “ scheduled”, 
 eatc-scheduling_datetime&#58; “ &#123;&#123;datetime&#125;&#125;”, 
 eatc-programed_picking_datetime&#58; “ &#123;&#123;datetime&#125;&#125;” . 
&#160; 
 El sistema deberá responder con el siguiente mensaje para posteriormente sacar al usuario a &quot; Mis donaciones &quot;. 
 clase = lbl_programacion_exitosa ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_programacion_exitosa )&#160; 
&#160; 
 &quot;Haz programado exitosamente la recolección de tu donación&quot; 
&#160; 
 Respuesta no exitosa&#58; incomplete_data&#58; El sistema deberá validar de nuevo los datos necesarios en el llamado e intentarlo de nuevo 
 Respuesta no exitosa&#58; retry&#58; El sistema deberá reintentar el llamado y desplegarle al usuario un solo toast (con control para que no se despliegue varias veces), con el siguiente label&#58; 
&#160; 
 clase = lbl_reintentando2 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_reintentando2 )&#160; 
&#160; 
 &quot;Reintentando, espera por favor unos segundos&quot; 
&#160; 
 Respuesta no exitosa&#58; fail&#58; El sistema deberá responder con el siguiente mensaje para posteriormente sacar al usuario de la funcionalidad de programación. 
&#160; 
 clase = lbl_ocurrio_un_problema_007 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_ocurrio_un_problema_007 )&#160; 
&#160; 
 &quot;Ocurrió un problema. CODIGO 007&quot; 

&#160; 
 DEPRECADO (por implementación de servicios de consulta de conductores y programación de anuncios)&#58; 
 Cuando se oprime el botón de confirmar programación se realizan tres acciones&#58; 1. Actualizar la información del encabezado de anuncio de donación; 2. Se realiza un registro en el histórico de estados de donaciones ; 3. Se realiza una calificación para el gestor de donaciones (según corresponda). 
&#160; 
 Actualización de información del encabezado de anuncio de donación ***REVISAR dinamismo a partir de _DOM.cua_master***&#58;&#160; 
 Cuando se confirma la programación, se actualiza información del encabezado de donación, de la siguiente manera. 
 eatc-scheduling_datetime&#58; Fecha y hora en la cual se programa la recogida (es decir la fecha y la hora en que se oprime el botón &quot;Confirmar Programación&quot; 
 eatc-state&#58; el estado debe cambiar de &quot;awarded&quot; a &quot;scheduled&quot; 
 eatc-programed_picking_datetime&#58; fecha de recogida programada por el usuario. 
 eatc-picker_name&#58; Nombre de quien recoge (y que se capturó en el formulario respectivo) 
 eatc-picker_doc_id &#58; Documento de identidad de quien recoge (y que se capturó en el formulario respectivo) 
 eatc-picker_license_plate &#58; Placa del vehículo de quien recoge (y que se capturó en el formulario respectivo) 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-scheduling_datetime= &#123;&#123;datetime&#125;&#125; &amp;eatc-programed_picking_datetime= &#123;&#123;datetime&#125;&#125;] &amp; eatc-state= scheduled &amp; eatc-picker_name =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_doc_id =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_license_plate =&#123;&#123;valor&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;valor&#125;&#125; 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente productivo &#58; 
 Para el anuncio de donación cuyo eatc-code = 40717 , y que mediante la App se registraron, a las 2019-09-18 17&#58;00&#58;00&quot; se registró la siguiente información&#58; &quot;Fecha y hora recogida&#58; 2019-09-19 01&#58;37&#58;54&quot; &quot;Nombre de quien recoge&#58; Juan Pérez&quot;, &quot;Documento de identidad de quien recoge&#58; 77777777&quot; y &quot;Placa del vehículo&#58; HHH777&quot;. 
&#160; 
 Mediante la API se debe hacer la siguiente escritura&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;&amp; eatc-scheduling_datetime= 2019-09-18%2017&#58;00&#58;00 &amp;eatc-programed_picking_datetime= 2019-09-19%2001&#58;37&#58;54 &amp; eatc-state= scheduled &amp; eatc-picker_name = Juan%20Pérez &amp; eatc-picker_doc_id = 77777777 &amp; eatc-picker_license_plate = HHH777 &amp;WHEREeatc-code=40717 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Para consultar el registro de encabezado actualizado&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717 
&#160; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 Para el registro del estado &quot;scheduled&quot; se toma la fecha en la que se programó la recogida del anuncio (eatc-scheduling_datetime) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-donation_manager_code y el eatc-donation_manager_user_doc_id incluyendo la declaración de los campos)&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;valor&#125;&#125;&amp; eatc-state = scheduled &amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log = eatc-donation_manager_code&#58; &#123;&#123;valor&#125;&#125; eatc-donation_manager_user_doc_id&#58; &#123;&#123;valor&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donación cuyo eatc-code = 40717 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-code&#58; &quot;40717&quot;, 
 eatc-scheduling_datetime &#58; &quot;2019-09-18 17&#58;00&#58;00&quot;, 
 eatc-donation_manager_code&#58; &quot; 900326456-1&quot; 
 eatc-donation_manager_user_doc_id &#58; &quot;8161174 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 Registro del estado &quot;scheduled&quot; &#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =40717&amp; eatc-state = scheduled &amp; eatc-date_time =2019-09-18%2017&#58;00&#58;00&amp; eatc-log = eatc-donation_manager_code&#58; 900326456-1%20 eatc-donation_manager_user_doc_id&#58; 8161174 
&#160; 
 Para consultar los estados registrados&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 
&#160; 
 La app&#160; debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190925174723&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;6&quot;, 
 mem &#58; 0.72, 
 time &#58; &quot;00&#58;00&#58;15&quot; 
&#160; 
 &#125; 

&#160; 
 ****NUEVO&#58; Integración con plataforma delivery si el gestor de donaciones posee el parámetro eatc_delivery=&quot;true&quot; ***&#58;&#160; 
 El sistema deberá evaluar si el beneficiario que&#160; programa la donación, utiliza la app &quot;Delivery&quot; caso en el cual, se procederá a realizar el llamado al servicio de integración respectivo. 
&#160; 
 La evaluación se hace verificando se la cuenta tiene&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identifcador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code&#125;&#125; 
&#160; 
 En caso que la consulta devuelva el siguente parámetro eatc_delivery &#58; &quot;true&quot; , el sistema debe realizar el siguiente llamado al servicio de integración con la plataforma delívery &#58; 
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

&#160; 
 Vínculo &quot;Programar luego&quot; (o volver, o cancelar) 
 Si el usuario presiona este vínculo, el sistema toma el dato &quot; eatc-adjudication_datetime &quot; le suma una hora y toma ese dato como la &quot;fecha y hora límite para programar el anuncio&quot; 
&#160; 
 El sistema le despliega al usuario el siguiente mensaje &quot;Recuerde que debes programar la recogida de la donación antes de [fecha y hora límite para programar el anuncio] . Si no lo haces el sistema liberará la do 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=fe4fc0b539644012b9c5ddc980f3e924&ext=png&ow=750&oh=1326, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=fe4fc0b539644012b9c5ddc980f3e924&ext=png&ow=750&oh=1326 

 546.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 
 07a415b5-82d1-47fb-9f19-2e4ac34a64ac 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 cd493964-b8b0-4801-b038-b39431821916 
 2025-07-10T02:20:24.4623254Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"fe3ce37c-db3d-44d2-acab-8359bc1b52f2","SequenceId":2704,"FluidContainerCustomId":"ed0f4551-fa94-4a96-952c-cc16aaf8d392","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 PROGRAMAR RECOGIDA DE ANUNCIO DE DONACIÓN (EATC_DONA_PROGRAM)