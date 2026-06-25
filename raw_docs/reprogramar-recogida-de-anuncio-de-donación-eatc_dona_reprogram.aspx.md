# reprogramar-recogida-de-anuncio-de-donación-eatc_dona_reprogram.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO &#58; ANUNCIO DE &quot;REPROGRAMACIONES&quot; RESTANTES *** 
 El sistema deber establecer a cuantos intentos de reprogramacin tiene derecho el gestor de donaciones y a partir de este dato, restndole las veces que ha programado la donacin, se le deber reprogramar o no la misma. 
&#160; 
 Datos necesarios para realizar la consulta de los intentos permitidos y realizados de reprogramacin &#58; 
 Se toman los siguientes datos del gestor de donaciones 
&#160; 
 eatc_donation_managers. identificador_unico_registro 
 eatc_donation_managers. eatc_doma_typology_b 
 _DOM. cua_master 
 eatc_dona_headers. eatc-code 
&#160; 
 Con estos datos se realiza la siguiente consulta&#58; 
&#160; 
 Consulta de los intentos permitidos de reprogramacin&#58; 
 La estructura de datos en donde se consultan los intentos permitidos de reprogramacin, se dise para que pueda funcionar definiendo dato por gestor de donaciones y por tipologa b de gestor de donaciones.&#160; Tambin permitir realizar configuraciones diferenciales por cuenta maestra, por este motivo se deber realizar primero una consulta particular, para ir llegando a lo ms general.&#160; En la medida en que se encuentre o no datos, se van utilizando valores por &quot; _default &quot; para obtener un valor registrado.&#160; En primera instancia la consulta por identificador_unico_registro no ser necesaria, pero se sugiere tenerla en cuenta en el desarrollo para que de una vez se pueda manejar esta posible volatilidad en el requisito. 
&#160; 
 Primera consulta&#58; consulta ms particular&#58; por cdigo de gestor de donaciones (no es totalmente necesaria en un primer momento) 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reprogr_attemps ? eatc_cua_master= &#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_doma_code= &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= eatc_reprogr_attemps 
&#160; 
 Si no se obtiene un resultado, se procede con la siguiente consulta&#58; 
&#160; 
 Segunda consulta&#58; consulta por tipologa b de gestor de donaciones 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reprogr_attemps ? eatc_cua_master= &#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_doma_typology_b= &#123;&#123;eatc_donation_managers. eatc_doma_typology_b &#125;&#125;&amp; eatc_doma_code= _default &amp;_cmp= eatc_reprogr_attemps 
&#160; 
 Si no se obtiene un resultado, se procede con la siguiente consulta&#58; 
&#160; 
 Tercera consulta&#58; consulta por cuenta maestra 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reprogr_attemps ? eatc_cua_master= &#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_doma_typology_b= _default &amp; eatc_doma_code= _default &amp;_cmp= eatc_reprogr_attemps 
&#160; 
 Si no se obtiene un resultado, se procede con la siguiente consulta&#58; 
&#160; 
 Cuarta consulta&#58; consulta por default 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reprogr_attemps ? eatc_cua_master= _default &amp; eatc_doma_typology_b= _default &amp; eatc_doma_code= _default &amp;_cmp= eatc_reprogr_attemps 
&#160; 
 El valor obtenido se guarda en la variable 
 &#123;&#123; intentos_reprogramacion_permitidos &#125;&#125; 

&#160; 
 Ejemplo&#58; ambiente de pruebas, cuenta maestra &quot;esp&quot;, tipologa b de gestor de donacin = 1, gestor de donacin con cdigo 123456789 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_dona_reprogr_attemps ?eatc_cua_master=esp&amp;eatc_doma_code=123456789&amp;_cmp=eatc_reprogr_attemps &#160; &#160; 
&#160; 
 Como no se obtiene un resultado, se procede con la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_dona_reprogr_attemps ?eatc_cua_master=esp&amp;eatc_doma_typology_b=1&amp;eatc_doma_code= _default &amp;_cmp=eatc_reprogr_attemps &#160; &#160; 
&#160; 
 Como no se obtiene un resultado, se procede con la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_dona_reprogr_attemps ?eatc_cua_master=esp&amp;eatc_doma_typology_b= _default &amp;eatc_doma_code= _default &amp;_cmp=eatc_reprogr_attemps &#160; &#160; 
&#160; 
 Como no se obtiene un resultado, se procede con la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_dona_reprogr_attemps ?eatc_cua_master= _default &amp;eatc_doma_typology_b= _default &amp;eatc_doma_code= _default &amp;_cmp=eatc_reprogr_attemps &#160; &#160; 
&#160; 
 Dada la respuesta del llamado el sistema establece que 
 &#123;&#123; intentos_reprogramacion_permitidos &#125;&#125;=1 

&#160; 
 Consulta de reprogramaciones realizadas&#58; 
 El sistema realiza esta consulta al historial de estados de la donacin en particular, para establecer las veces que la misma ha sido reprogramada&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_header_state_history ?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc_doma_id= 
 &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-state=scheduled&amp;_cont 
&#160; 
 Al valor obtenido se le resta una unidad (siempre y cuando el resultado del cont anterior sea mayor que 1).&#160; 
&#160; 
 El valor resultante se guarda en la variable 
 &#123;&#123; intentos_reprogramacion_realizados &#125;&#125; 
&#160; 
 Ejemplo&#58; ambiente productivo, cuenta maestra &quot;abaco&quot;, donacin con cdigo&#58; 00002005250523 
 El sistema realiza la consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/ eatc_dona_header_state_history ?eatc-dona_header_code=00002005250523&amp;eatc-state=scheduled&amp;_cont &#160; 
&#160; 
 Dado que la respuesta fue&#58; 
 &quot;count&quot;&#58; &quot;1&quot; 
&#160; 
 Entonces al restarle la unidad se tiene que&#58;&#160; 
 &#123;&#123; intentos_reprogramacion_realizados &#125;&#125;=1-1=0 

&#160; 
 Clculo de intentos de reprogramacin restantes&#58; 
 El sistema con los valores obtenidos calcula el nmero de intentos de reprogramacin restantes 
 &#123;&#123; intentos_reprogramacion_restantes &#125;&#125; = &#123;&#123; intentos_reprogramacion_permitidos &#125;&#125; - &#123;&#123; intentos_reprogramacion_realizados &#125;&#125; 

&#160; 
 Despliege de anuncio de intentos de reprogramacin restantes y formulario de reprogramacin&#58; 
 No se tienen intentos de reprogramacin disponibles&#58; 
 Si el valor de los intentos de reprogramacin restantes ( &#123;&#123; intentos_reprogramacion_restantes &#125;&#125; ), es igual o menor que 0, entonces el sistema deber desplegar el siguiente anuncio&#58; 
&#160; 
 &quot;No tienes reprogramaciones disponibles para esta donacin, por favor gestiona tu donacin en los tiempos previamente estipulados&quot; &#58;&#160; label&#58; class=&quot;lbl_sin_reprogramaciones&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_sin_reprogramaciones ) 
&#160; 
 Se debe desplegar un botn para retornar al dashboard del anuncio de donacin (o hacer dicho retorno automtico, despus de un tiempo que permita leer el anuncio desplegado. 

&#160; 
 Se tienen intentos de reprogramacin disponibles&#58; 
 Si el valor de los intentos de reprogramacin restantes ( &#123;&#123; intentos_reprogramacion_restantes &#125;&#125; ), es igual o mayor que 1, entonces el sistema deber desplegar el siguiente anuncio (concatenando los siguientes labels y resultados)&#58; 
&#160; 
 &quot;Tienes&quot; &#58;&#160; label&#58; class=&quot;lbl_tienes&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_tienes ) 
 &#123;&#123; intentos_reprogramacion_restantes &#125;&#125; 
 &quot;intento(s) de reprogramacin restante(s).&#160; Utilzalo(s) bien&quot; &#58;&#160; label&#58; class=&quot;lbl_intentos_repr_rest&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_intentos_repr_rest ) 
&#160; 
 Y se despliega el siguiente formulario de reprogramacin. 
&#160; 
 Formulario de reprogramacin&#58; 
 Debe funcionar igual al formulario de programacin que est implementado en la actualidad y que contiene los elementos de seguridad para validacin de datos en listas negras.&#160; Se debe tener en cuenta que la primera versin de la funcionalidad de reprogramacin no tena estas caractersticas , por lo tanto es necesario implementarla a partir de lo realizado en el nuevo proceso de programacin . 

 ----DEPRECADO (de aqu en adelante) ----- 

 Formulario de edicin&#58; 
 El sistema debe presentar un formulario de edicin de los datos de programacin de recogida de anuncios con los siguientes campos y validaciones (esta funcionalidad se debe extender a partir de la funcionalidad original de Programacin de recogida de la donacin ).&#160; Esto se implementa, porque hay circunstancias de fuerza mayor que implican cambiar los datos de recogida.&#160; Esto se realizar escogiendo una causal y dicha causal ir al registro de estados para dejar evidencia de la edicin. 
&#160; 
 Validacin previa a la reprogramacin de la recogida ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Dada la rara circunstancia detectada , que en algunos pocos casos se est permitiendo manipulacin doble (dos organizaciones en simultneo) de una donacin, se propone realizar esta validacin, antes de hacer el proceso de programacin, para garantizar que dicha programacin solo pueda ser realizada por la organizacin a la cual se le adjudic el anuncio. 
&#160; 
 Antes de realizar el proceso, el sistema debe tomar el eatc_donation_manager.identificador_unico_registro y enviarlo al parmetro &quot;eatc-donation_manager_code&quot; del eatc_dona_headers de la donacin en la que se est (es decir en la consulta se enva el eatc-code de la donacin tambin). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-code= &#123;&#123; eatc_dona_headers. eatc-code&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_donation_manager. identificador_unico_registro&#125;&#125; &amp;_compress 
&#160; 
 Si la respuesta contiene un resultado, se le deja seguir adelante en el proceso de programacin.&#160; Si la respuesta es con un resultado sin conteo (cont &quot;0&quot;) entonces debe salir el siguiente mensaje&#58; 
&#160; 
 La presente donacin ya fue adjudicada a otra organizacin. Te solicitamos seguir pendiente de la nube para acceder a futuras oportunidades. 
&#160; 
 ACEPTAR 
&#160; 
 El botn aceptar debe devolver a la nube de donaciones . 

 Ejemplo ( tomando como referencia el caso real detectado )&#58; 
&#160; 
 La fundacin &quot;FUNDACION PAYASITOS CON ESPERANZA&quot;, con el Identificador nico de registro &quot;830903608&quot;, se encontraba (por una muy rara razn que aun no se logra identificar) en el dashboard de la donacin eatc-code= colombiaLF4RMQ4qXVPpnKgc8lBya20200509093441354 a las &quot;2020-05-09 18&#58;46&#58;13&quot; y procedi a intentar programar la recogida de la donacin. 
&#160; 
 El sistema debi realizar la siguiente consulta&#58; 
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
 Se le debi desplegar el mensaje arriba descrito (La presente donacin ya fue adjudicada a otra organizacin. Te solicitamos seguir pendiente de la nube para acceder a futuras oportunidades.) y redireccionarla a la nube de donaciones, evitando de esta manera una nueva programacin del anuncio ( como ocurri originalmente ). 

&#160; 
 Causal de reprogramacin ***NUEVO&#58; internacionalizacin*** 
 El sistema debe presentar un selector, para seleccionar un causal de reprogramacin del anuncio.&#160; El selector se nutre de los datos de se obtienen con las siguientes consultas&#58; 
&#160; 
 NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los causales 
&#160; 
 NUEVO&#58; Paso 2&#58; consulta de los causales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_causes_of_reschedule&amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125; 
 Anteriormente &#58; &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_causes_of_reschedule?_id=_* 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_causes_of_reschedule&amp;eatc_language=en&#160; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en el selector y llevarlos al registro junto con el dato consignado en &quot; eatc_internationalize_dt. eatc_data_id 
&#160; 
 El usuario seleccionar una causa y la misma ( eatc_internationalize_dt. eatc_int_data e eatc_internationalize_dt. eatc_data_id) se guardar en una variable causa para posterior registro en el historial de estados ( eatc-log) 

&#160; 
 ***NUEVO&#58; validacin previa del dato &quot;eatc_dona_headers&quot;&#58; &quot;eatc_last_p_day&quot; para establecer fecha lmite de recogida diferente a lo que se establece con eatc_timeout_rules*** 
 El sistema debe evaluar si existe un dato vlido de fecha (en formato AAAA-MM-DD) en eatc_dona_headers. eatc_last_p_day 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM.c ua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_distinct= eatc_last_p_day 
&#160; 
 y&#160; de encontrarlo, debe presentar opcin de escoger una fecha y hora que sea mximo para ese da.&#160; 
&#160; 
 De no encontrar un dato vlido para eatc_last_p_day (nulo, vaco, o con el dato 0000-00-00) entonces se proceder con el proceso tal como est implementado hasta la fecha. 

&#160; 
 Fecha y hora de recogida&#58; 
 Debe presentar opcin de editar la fecha y hora de recogida original, teniendo en cuenta que la nueva fecha y hora programada est dentro de del rango de tiempo mximo definido en el timeout particular a partir de la fecha&#160; de publicacin del anuncio &quot; eatc-publication_datetime &quot;.&#160; 
&#160; 
 Para conocer dicha regla de timeout se debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout&#160; 
&#160; 
 Y para validar se debe realizar esta consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;valor&#125;&#125; 

&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout &#160; 
 Dado que la respuesta (a 4 de diciembre de 2019) es&#58; 
 &#123; 
 _id &#58; &quot;1&quot;, 
 eatc-code &#58; &quot;1&quot;, 
 cua &#58; &quot;exito&quot;, 
 eatc-timeout_name &#58; &quot;dona_global_scheduling_timeout&quot;, 
 eatc-timeout_description &#58; &quot;Tiempo mximo entre la publicacin del anuncio de donacin y la programacin de la recogida&quot;, 
 eatc-timeout_in_minutes &#58; &quot;2880&quot;, 
 eatc-timeout_in_hours &#58; &quot;48,00&quot;, 
 eatc-timeout_from &#58; &quot;eatc-publication_datetime&quot; 
 &#125; 
 El sistema no debe permitir que despus de ( eatc-timeout_in_minutes ) 48,00 horas o ( eatc-timeout_in_hours ) 2880 minutos contados a partir del ( eatc-timeout_from ) eatc-publication_datetime, se pueda reprogramar la recogida de una donacin. 
&#160; 
 Tambin debe tomar en cuenta los respectivos horarios de atencin del punto de donacin, para validar que la fecha y hora estn en el rango de horario de atencin. 
 Ejemplo LEGACY&#58; 
&#160; 
 Para el anuncio de donacin cuyo eatc-code es &quot; 40716 &quot; ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40716 ), el selector de fecha y hora no debe permitir seleccionar fechas y horas posteriores a &quot;2019-09-19 15&#58;37&#58;54&quot; (dado que &quot; eatc-publication_datetime &quot; es igual a &quot;2019-09-18 15&#58;37&#58;54&quot;). 
&#160; 
 Por otro lado el sistema debe consultar los horarios de atencin del respectivo punto de donacin&#160; ( eatc-pod_id &#58; &quot;339&quot;) de la siguiente manera&#58; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id=339 &#160; 
&#160; 
 Y no permitir seleccionar horarios que no estn entre la franja de&#58; 07&#58;00&#58;00 a 14&#58;00&#58;00 , dado que los das mircoles y jueves (que son los que caen en las 24 horas posteriores a la fecha de publicacin), tienen esa disponibilidad de horario de atencin&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339&amp;eatc-day=mi,ju &#160;&#160; 
&#160; 
 ***NUEVO***IMPLEMENTACIN A PARTIR DE LA NUEVA ESTRUCTURA POR CUENTA DE HORARIOS DE ATENCIN&#160; 
 Para realizar la consulta adecuada para cada anuncio de donacin, se debe utilizar el parmetro eatc_dona_header. eatc_cua_origin para incorporarlo a la URL que consulta los horarios de atencin. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_dona_header. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 Suponiendo que un anuncio de donacin tiene el parmetro eatc_dona_header. eatc_cua_origin = makro y el eatc_dona_header.eatc_pod es igual a st01 , el sistema deber realizar la siguiente consulta para traer los horarios de atencin&#58; 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/&#123;&#123;eatc_dona_header. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/&#123;&#123;eatc_dona_header. eatc_cua_origin &#125;&#125;/eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc_pod&#125;&#125; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/makro/eatc_attention_schedule?eatc-pod_id=st01 &#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/makro/eatc_attention_schedule?eatc-pod_id=st01 &#160; 
&#160; 
 Y no permitir seleccionar horarios que no estn entre la franja de&#58; 07&#58;00&#58;00 a 14&#58;00&#58;00 , dado que los das mircoles y jueves (que son los que caen en las 24 horas posteriores a la fecha de publicacin), tienen esa disponibilidad de horario de atencin&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_attention_schedule?eatc-pod_id=339&amp;eatc-day=mi,ju &#160;&#160; 
&#160; 
 Nombre de quien recoge&#58; 
 Campo de texto obligatorio, que sugiere el registro previo de &quot; eatc-picker_name &quot; y cuyo input (si se edita el registro) debe guardarse en la variable &quot; eatc-picker_name &quot;. 
&#160; 
 Documento de identidad de quien recoge&#58; 
 Campo de texto obligatorio, que sugiere el registro previo de &quot; eatc-picker_doc_id &quot;&#160; cuyo input (si se edita el registro) debe guardarse en la variable &quot; eatc-picker_doc_id &quot;. 
&#160; 
 Placa del vehculo&#58; 
 Campo de texto opcional, que sugiere el registro previo de &quot; eatc-picker_license_plate &quot; cuyo input (si se edita el registro) debe guardarse en la variable &quot; eatc-picker_license_plate &quot;. 

&#160; 
 Botn &quot;Confirmar programacin&quot; 
 Cuando se oprime el botn de confirmar programacin se realizan dos acciones&#58; 1. Actualizar la informacin del encabezado de anuncio de donacin; 2. Se realiza un registro en el histrico de estados de donaciones ; 
&#160; 
 Actualizacin de informacin del encabezado de anuncio de donacin ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Cuando se confirma la programacin, se actualiza informacin del encabezado de donacin, de la siguiente manera. 
&#160; 
 eatc-scheduling_datetime&#58; Fecha y hora en la cual se programa la recogida (es decir la fecha y la hora en que se oprime el botn &quot;Confirmar Programacin&quot; 
 eatc-programed_picking_datetime&#58; fecha de recogida programada por el usuario (si la misma cambi). 
 eatc-picker_name&#58; Nombre de quien recoge (si el mismo cambi) 
 eatc-picker_doc_id &#58; Documento de identidad de quien recoge (si el mismo cambi) 
 eatc-picker_license_plate &#58; Placa del vehculo de quien recoge (si el mismo cambi) 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-scheduling_datetime= &#123;&#123;datetime&#125;&#125; &amp;eatc-programed_picking_datetime= &#123;&#123;datetime&#125;&#125;&amp; eatc-picker_name =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_doc_id =&#123;&#123;valor&#125;&#125;&amp; eatc-picker_license_plate =&#123;&#123;valor&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;valor&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , y que mediante la App se editaron los valores dejandolos, a las 2019-09-18 17&#58;00&#58;00&quot; se registr la siguiente informacin&#58; &quot;Fecha y hora recogida&#58; 2019-09-19 01&#58;37&#58;54&quot; &quot;Nombre de quien recoge&#58; Juan Prez&quot;, &quot;Documento de identidad de quien recoge&#58; 77777777&quot; y &quot;Placa del vehculo&#58; HHH777&quot;. 
&#160; 
 Mediante la API se debe hacer la siguiente escritura&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;&amp; eatc-scheduling_datetime= 2019-09-18%2017&#58;00&#58;00 &amp;eatc-programed_picking_datetime= 2019-09-19%2001&#58;37&#58;54 &amp; eatc-picker_name = Juan%20Prez &amp; eatc-picker_doc_id = 77777777 &amp; eatc-picker_license_plate = HHH777 &amp;WHEREeatc-code=40717 
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
 Para consultar el registro de encabezado actualizado&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=40717 

&#160; 
 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) ***REVISAR dinamismo a partir de _DOM.cua_master e incorporacin de eatc_internationalize_dt.eatc_data_id*** 
 Para el registro del estado &quot; scheduled &quot; se toma la fecha en la que se program la recogida del anuncio (eatc-scheduling_datetime) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-donation_manager_code y el eatc-donation_manager_user_doc_id incluyendo la declaracin de los campos) y la causa de la reprogramacin (eatc_cause) 
&#160; 
 &#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;valor&#125;&#125;&amp; eatc-state = scheduled &amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log = eatc-donation_manager_code&#58; &#123;&#123;valor&#125;&#125;%20 eatc-donation_manager_user_doc_id&#58; &#123;&#123;valor&#125;&#125; causa&#58;&#123;&#123; eatc_internationalize_dt. eatc_int_data&#125;&#125;%20id&#58; &#123;&#123; eatc_internationalize_dt. eatc_data_id&#125;&#125; 

&#160; 
 Ejemplo _DOM. cua_master=abaco 
&#160; 
 Para el anuncio de donacin cuyo eatc-code = 40717 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
 eatc-code&#58; &quot;40717&quot;, 
 eatc-scheduling_datetime &#58; &quot;2019-09-18 17&#58;00&#58;00&quot;, 
 eatc-donation_manager_code&#58; &quot; 900326456-1&quot; 
 eatc-donation_manager_user_doc_id &#58; &quot;8161174 
 eatc_cause&#58; enfermedad del recolector 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
 Registro del estado &quot;scheduled&quot; &#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =40717&amp; eatc-state = scheduled &amp; eatc-date_time =2019-09-18%2017&#58;00&#58;00&amp; eatc-log = eatc-donation_manager_code&#58; 900326456-1%20 eatc-donation_manager_user_doc_id&#58; 8161174%20 causa&#58; %20enfermedad%20del%20recolector 
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
 Terminada la operacin se devuelve al dashboard del anuncio de donacin. 

&#160; 
 ****NUEVO&#58; Integracin con plataforma delivery si el gestor de donaciones posee el parmetro eatc_delivery=&quot;true&quot; ***&#58;&#160; 
 &#160;El sistema deber evaluar si el beneficiario que&#160; programa la donacin, utiliza la app &quot; Delivery &quot; caso en el cual, se proceder a realizar el llamado al servicio de integracin respectivo . 
&#160; 
 La evaluacin se hace verificando se la cuenta tiene&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identifcador_unico_registro=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code&#125;&#125; 
&#160; 
 En caso que la consulta devuelva el siguente parmetro eatc_delivery &#58; &quot;true&quot; , el sistema debe realizar el siguiente llamado al servicio de integracin con la plataforma delvery&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/int/&#123;&#123;_DOM. cua_master &#125;&#125;/int_eatc_delivery?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_operacion=update 

&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente pruebas, eatc_dona_headers. eatc-donation_manager_code=805025018&#58; 
 Para el anuncio de donacin eatc-code &#58; &quot;00002011084217&quot; cuyo eatc-donation_manager_code=805025018 ,el sistema debe realizar la siguiente consulta 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=805025018 &#160; 
&#160; 
 Como la respuesta de la consulta trae el siguiente parmetro&#58; 
&#160; 
 eatc_delivery &#58; &quot;true&quot; 
&#160; 
 El sistema debe proceder a realizar el siguiente llamado al servicio de integracin&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/int/abaco/int_eatc_delivery?eatc_dona_header_code=00002011084217&amp;_operacion=update 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=172bf4b72ce0487d82c76faf2ab2866b&ext=png&ow=750&oh=1326, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=172bf4b72ce0487d82c76faf2ab2866b&ext=png&ow=750&oh=1326 

 548.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"On"}] 
 960b880f-40bb-4040-9e63-347934abd36e 
 1!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 593e363f-4130-42e7-b0f1-d55d8c270d0a 
 2025-08-15T08:14:10.5753745Z 

 REPROGRAMAR RECOGIDA DE ANUNCIO DE DONACIN (EATC_DONA_REPROGRAM)