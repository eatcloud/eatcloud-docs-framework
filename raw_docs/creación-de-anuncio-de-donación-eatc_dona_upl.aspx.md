# creación-de-anuncio-de-donación-eatc_dona_upl.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 DESPLIEGUE DE LA FUNCIONALIDAD 
 Esta funcionalidad no se despliega para todas las cuentas de usuario (CUA), por lo tanto se debe consultar en la configuración de la cuenta ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua]), para establecer si se ha habilitado esta funcionalidad (eatc_dona_upl), y de ser así en la web app se debe desplegar el botón respectivo en el menú lateral. 
 Ejemplo : 
 Para la cuenta "prueba" se evalúa su respectiva configuración con el siguiente llamado:  

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=prueba   ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=prueba ) 

 Al comprobar que el parámetro " eatc_dona_upl " tiene como valor "yes" se debe habilitar la funcionalidad para la cuenta en cuestión. 

 Creación del anuncio de donación 
 Validación de existencia de horario de atención. 
 Antes de ingresar a la funcionalidad el sistema debe hacer la siguiente consulta, para establecer si el punto de donación tiene horarios de atención registrados en el sistema: 

 Fase inicial: estructura legacy 
 Pruebas : https://devdonantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id={{eatc-pod_id}} 
 Productivo : https://donantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id={{eatc-pod_id}} 

 Fase final: estructura definitiva 
 Pruebas : https://devdonantes.eatcloud.info/api/{{ cua_user }}/eatc_attention_schedule?eatc-pod_id={{eatc-pod_id}} 
 Productivo : https://donantes.eatcloud.info/api/{{ cua_user }}/eatc_attention_schedule?eatc-pod_id={{eatc-pod_id}} 

 Si existe un registro asociado al punto, se pasa a la siguiente validación: Horario de atención disponible antes del rango de cancelación del anuncio . 

 Si no existe un registro asociado al punto. 
 Ejemplo: un punto de donación, cuyo eatc-pod_id es 777, realiza la consulta (en ambiente de pruebas): https://devdonantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id=777 el resultado de la misma es: 
{ ts : "200504094733", op : true, cont : 0, err_msg : "No se produjeron resultados", err_num : "", mem : 0.39, time : "00:00:00"} 

 Por lo tanto se debe  desplegar el siguiente mensaje: 
 El punto de donación no tiene horarios de atención asociados, por favor ingresa a la funcionalidad " horarios de atención " para configurarlos 

 El sistema debe proporcionar un vínculo para ingresar a la funcionalidad horarios de atención , y no debe permitir al usuario hacer un registro de anuncio de donación, hasta que el punto de donación no tenga horarios de atención registrados y que cumpla con la siguiente validación. 

 Validación de horario de atención disponible antes del rango de cancelación del anuncio  
 Si existe un registro de horario de atención, el sistema debe validar que dicho horario empieza antes de que culmine el tiempo que se tiene establecido para cancelar el anuncio en el sistema  
 {{URL_entorno_donantes}}/api/{{ _DOM.cua_master }}/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout 

 (anteriormente: https://donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout ). 

 Si el inicio de por lo menos uno de los horarios de atención registrados, no se encuentra antes del tiempo establecido en el Timeout, el sistema debe mostrar el siguiente anuncio: 
 El punto de donación no tiene un horario de atención disponible antes del tiempo estipulado de [ eatc-timeout_in_hours ](nota que no va en el mensaje: tomado de https://donantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout ) horas para la cancelación del anuncio. Por favor ingresa a la funcionalidad " horarios de atención " para configurar un horario adecuado para una donación realizada en este momento o espera un poco para hacer tu donación.  

 Este mensaje  debe impedir realizar el anuncio de donación (es decir es un mensaje restrictivo como el anterior), y debe proporcionar un vínculo a la funcionalidad de " horarios de atención "  para hacer la configuración.  

 Validación de existencia de horarios de atención por defecto 
 Si el sistema obtiene una respuesta de los horarios de atención y al evaluar la misma resulta que son los horarios de atención por defecto (de lunes a viernes de 9AM a 5PM), el sistema debe desplegar otro anuncio de la siguiente manera: 

 El punto de donación tiene registrados los horarios de atención por defecto. Si estos horarios no se acomodan por favor ingresa a la funcionalidad " horarios de atención " para configurarlos. (desea seguir viendo este mensaje: si no) 

 Este mensaje no debe impedir realizar el anuncio de donación (es decir no es un mensaje restrictivo como el anterior), pero si debe proporcionar un vínculo a la funcionalidad en cuestión para hacer la configuración.  Si el usuario no desea volver a ver el mensaje, el mismo no debe mostrársele más. 

 Encabezado:  
 Los datos de encabezado se toman y se muestran al iniciar la transacción y se agregan a cada registro de detalle (eatc_dona).  Dichos datos son: 

 Datos generados por la APP 
 Código del anuncio de la donación ( eatc-dona_header_code que corresponde a un identificador único para el anuncio que se realizará).  Idealmente este código deberá contener el nombre de la cuenta [CUA], el código del punto de donación (eatc-pod_id) y una cadena (que puede ser el estampe de tiempo con milisegundos ( AAAAMMDDHHMMSSMM) . 
 Fecha actual para guardarla posteriormente en dos formatos de fecha  que se llevan al registro : 
 eatc-date_time: AAAAMMDDHHMMSS (no se muestra en la interfaz de la APP pero se guarda para el registro) 
 eatc-date_time_2: AAAA-MM-DD (se muestra en la interfaz de la APP y se guarda para el registro). Este dato se debe mostrar (pintar) en la interfaz de la APP 

 Datos del donante ***NUEVO: SE TOMAN LOS DATOS DE DATAGOV*** 
 La información de la CUA se toma del DOM, y con este dato se realizan las siguientes consultas: 

 +++[CAMBIA A CONSULTA A DATAGOV]+++ Nit del donante: se guarda en eatc_donor_code 

 Primera consulta para obtener los datos 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue={{_DOM.cua_user}} 

 Con la respuesta obtenida se toma el _id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &fieldname= eatc_cua,eatc_customer_fiscal_id &&filterfield_1=_id&filtervalue_1={{ eatc_customers_cua._id }}   

 Con esto se obtiene el valor desencriptado de eatc_customer_fiscal_id   que es el que se guarda en eatc_donor_code y también se utiliza para obtener el nombre del donante más adelante 

 (ANTERIORMENTE: se toma de eatc_cua . customer__eatc_clientes__partyidentification https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua] ) 

 =>  Este dato se debe mostrar (pintar) en la interfaz de la WAPP y se guarda para el registro . 
 Ejemplo _DOM.cua_user = colombia 

 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue=colombia   

 Dado que la respuesta es: 

 { 
 _id : "6", 
 eatc_country : "co", 
 eatc_customer_fiscal_id : "bGlzbGJKSVMydE8xT3ZQa3ByZit3Zz09", 
 eatc_cua : "Nno1dXlCdGE1dkk4dXpaUkllRFcwQT09" 
 } 

  Con la respuesta obtenida se toma el _id=6 para realizar la siguiente consulta: 

 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &fieldname= eatc_cua,eatc_customer_fiscal_id &&filterfield_1=_id&filtervalue_1=6 

 Como eatc_customer_fiscal_id : "811029245", el dato 811029245 se lleva a eatc_donor_code y se guarda para la próxima consulta 

 +++[CAMBIA A CONSULTA DATAGOV]+++ Nombre del donante: se guarda en eatc_donor   

 Se toma el dato obtenido en la anterior consulta y se realiza esta 
 eatc_cua. name https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{_DOM.cua_user}} 

 (ANTERIORMENTE: se toma de eatc_cua.name https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua]).  

 =>  Este dato se debe mostrar (pintar) en la interfaz de la APP y se guarda para el registro en eatc_donor 

 Datos del punto de donación (se toman de eatc_pods): 
 Se entiende que esta información se toma en el proceso de login . 
 https://devdonantes.eatcloud.info/api/[cua]/eatc_pods?eatc-id=_* 

 Código del punto de donación , se guarda en eatc-pod_id: ( eatc_pods.eatc-id ) =>  Este dato se debe mostrar (pintar) en la interfaz de la APP y se guarda para el registro . 

 Ejemplo: 
 Si la donación la hace el Éxito de Colombia, el dato sería "31" (eatc-pod_id) https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31   

 Nombre ( eatc_pods.eatc-name : se muestra en la interfaz gráfica pero no se lleva al registro)  =>  Este dato se debe mostrar (pintar) en la interfaz de la APP (es eminentemente informativo y no se lleva al registro) 
 Dirección ( eatc_pods.eatc-adress : se muestra en la interfaz gráfica pero no se lleva al registro) =>  Este dato se debe mostrar (pintar) en la interfaz de la APP (es eminentemente informativo y no se lleva al registro) 

 Nombre del donante, NIT o Identificación del donante (para cuentas con múltiples donantes): tratamiento diferencial cuando desde el pod se pueden realizar donaciones de no negociados y filtro especial para cuando esto no ocurre 
 multiple_donors= si   
 ({{url_entorno_datagov}} /api/eatcloud/ eatc_cua ?name= {{ _DOM .cua_user}} &multiple_donors= si &_cmp= multiple_donors) 

 Nota importante: para implementar la funcionalidad de No Negociados, que es aquella que permitirá realizar donaciones de terceros desde puntos de donación establecidos, las cuales saldrán a nombre de dichos terceros (eatc-donor), pero con origen (eatc-cua_origin) de la cuenta a la que pertenece el punto, se realizará una validación adicional, para desplegar, como múltiples donantes, la información de donantes de no negociados, y poder operar la funcionalidad de captura de información con estos datos.  En particular el encontrar y seleccionar datos de un donante de no negociados (que se identifica en la tabla " eatc_multiple_donors_info ", por tener un dato en el campo " eatc_cua_user ") se utilizará el dato contenido en " eatc_multiple_donors_info. eatc_cua_user " (que en adelante se denominará como la variable {{eatc_cua_donor_nng}} ) , para: 

 Llevar a la donación en el campo eatc-donor de la respectiva donación, el valor la cua_user del donante de no negociados: eatc_dona_headers. eatc-donor = {{eatc_cua_donor_nng}} 

 Consultar la información de los productos del donante de no negociados, mediante la consulta: {{url_donantes}} /api/ {{eatc_cua_donor_nng}} /eatc_odds?_id=_* 

 Para realizar lo anterior, se deberá identificar si el punto en cuestión, ha sido configurado para ser donante de no negociados, y de ser así, se deberá presentar como valor por defecto del selector, los datos de la cuenta a la que pertenece el punto de donación y permitir seleccionar, fuera de los NITs propios de la cuenta, aquellos que corresponden a donantes de no negociados autorizados para dicho punto de donación. 

 Información técnica del parámetro:  eatc_dona_headers. eatc_donor_fiscal_name, eatc_dona_headers. eatc-donor_code y ***NUEVO: eatc_dona_headers. eatc-donor *** 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validación : obligatoriedad 

 Tipo de campo de captura: ( multiple_donors= si ) 

 ***NUEVO: Validación si el punto es un punto origen de no negociados *** 
 El sistema realiza la siguiente consulta para establecer si es un punto de donación de no negociados 
 {{URL_donantes}} /api/allpods/eatc_pods_cua_donor_nng?eatc-id= {{ eatc_pods.eatc-id }} &eatc-cua= {{ _DOM .cua_user}} &_cmp=eatc_cua_donor_nng 

 Según sea la respuesta de la consulta (el punto de donación, tiene o no tiene registros en la respectiva tabla), se construirá el selector de maneras diferentes. 

 Si el sistema obtiene una respuesta válida, los valores contenidos en eatc_pods_cua_donor_nng. eatc_cua_donor_nng se guardan en un {{array_eatc_cua_donor_nng}} 

 Cuando el punto de donación no tiene registros en "eatc_pods_cua_donor_nng": Selector único (manera como venía funcionando anteriormente) 
 La información se toma de: 
 Deprecado 
 {{url_donantes}}/ api /{{ _DOM .cua_user}}/eatc_multiple_donors_info? _id=_*&_cmp= eatc_donor_fiscal_name,eatc_donor_code 

 ***NUEVO:   
 {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_multiple_donors_info?_id=_*& eatc_cua_user=_vacio 
 &_cmp= eatc_donor_fiscal_name,eatc_donor_code 

 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=alqueria: pod-id:alqueria1 (ficticio) 
 Se debe realizar la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alqueria &multiple_donors=si &_cmp= multiple_donors 

 Como la consulta trae un resultado válido, entonces el sistema valida si el pod respectivo está configurado para no negociados: 

 https://devdonantes.eatcloud.info/api/allpods/eatc_pods_cua_donor_nng?eatc-id= alqueria1 &eatc-cua= alqueria &_cmp=eatc_cua_donor_nng   

 Como la consulta anterior no trae un resultado válido, entonces el sistema construye un selector con los valores que arroja la siguiente consulta: 

 https://devdonantes.eatcloud.info/ api /alqueria/eatc_multiple_donors_info? _id=_*& eatc_cua_user=_vacio &_cmp= eatc_donor_fiscal_name,eatc_donor_code     

 Al seleccionar un nombre de los que traiga la respuesta, se debe obtener el valor del código del donante para  
 luego llevar los mismos a los datos de la donación ( eatc_dona_headers. eatc_donor_fiscal_name ) . 

 Cuando el punto de donación tiene registros en "eatc_pods_cua_donor_nng": Selector único: 
 La información se toma de: 
 V alor por defecto 
 {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_multiple_donors_info?_id=_*& eatc_default=y &_cmp= eatc_donor_fiscal_name,eatc_donor_code 

 O tros valores múltiples donantes: el sistema trae los nits que no tienen registro en eatc_cua_user, es decir, que son multiples donantes de la cuenta origen de la donación, mediante la siguiente consulta: 
 {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_multiple_donors_info? eatc_default=!y& eatc_cua_user= _vacio &_cmp= eatc_donor_fiscal_name,eatc_donor_code, eatc_cua_user 

 O tros valores donantes de no negociados (nng): el sistema toma el {{array_eatc_cua_donor_nng}} de la validación previa y realiza la siguiente consulta para traer la información correspondiente a los donantes de no negociados: 
 {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_multiple_donors_info? eatc_cua_user= {{array_eatc_cua_donor_nng}} &_cmp= eatc_donor_fiscal_name,eatc_donor_code, eatc_cua_user 

 ***NUEVO : Identificación de la donación como de No Negociados *** 
 Si el usuario selecciona esta opción, el fondo del formulario de captura debe cambiar a un color distintivo, y en un lugar visible del formulario de creación (al inicio de la captura de los datos de los productos) debe aparecer como un "botón" (es decir el texto contenido en una forma rectangular con bordes curvos de color distintivo) el siguiente label: 

 class=lbl_donacion_no_negociados "Donación de No Negociados" 

 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=exito, eatc-pod_id=39: 
 Se debe realizar la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &multiple_donors=si &_cmp= multiple_donors 

 Como la cuenta posee la característica de multiple_donors=si, entonces se procede a realizar esta consulta: 

 https://devdonantes.eatcloud.info/api/allpods/eatc_pods_cua_donor_nng?eatc-id=39&eatc-cua= exito &_cmp=eatc_cua_donor_nng   

 Dada la respuesta del servicio se tiene que {{array_eatc_cua_donor_nng}}= alimentoscarnicos    

 Como la consulta trae un resultado válido, entonces el sistema construye un selector con los valores que arroja la siguiente consulta: 

 Por lo tanto el sistema realiza la siguiente consulta para mostrar el valor por defecto del selector: 
 https://devdonantes.eatcloud.info/api/exito/eatc_multiple_donors_info?id=_*& eatc_default=y &_cmp= eatc_donor_fiscal_name,eatc_donor_code     
 para los demás valores del selector correspondientes a múltiples nits de la cuenta éxito, se realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/exito/eatc_multiple_donors_info? eatc_default=!y& eatc_cua_user= _vacio &_cmp= eatc_donor_fiscal_name,eatc_donor_code   

 y para los demás valores del selector, correspondientes a donantes de no negociados, se realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/exito/eatc_multiple_donors_info? eatc_cua_user= alimentoscarnicos &_cmp= eatc_donor_fiscal_name,eatc_donor_code, eatc_cua_user   

 Al seleccionar un nombre de los que traiga la respuesta, se debe obtener el valor del código del donante para  
 luego llevar los mismos a los datos de la donación ( eatc_dona_headers. eatc_donor_fiscal_name ) .  El sistema guarda el valor: eatc_multiple_donors_info . eatc_cua_user   (en caso de seleccionarse un donante de no negociados) para futuras consultas en el sistema 

 multiple_donors= no   
 ({{url_entorno_datagov}} /api/eatcloud/ eatc_cua ?name= {{ _DOM .cua_user}} &multiple_donors= no &_cmp= multiple_donors) 
 No se despliega campo de captura (debe funcionar como ha venido funcionando) 
 No se despliega ningún campo de captura ni se lleva ninguna información con respecto a este dato al registro de la donación (ya que el dato se tomará más adelante desde la información de cofiguración de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro    
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parámetro multiple_donors no existe para este registro de configuración de cuenta, no se debe mostrar ningún campo de captura. 

 Cuentas con multiple_donors=si: y el punto de donación no tiene registros en " eatc_pods_cua_donor_nng " El nombre y el código del donante que se selecciona se guardan en eatc_dona_headers. eatc_donor_fiscal_name, eatc_dona_headers. eatc-donor_code (tal cual cómo venía funcionando) 
 [+++] Se guarda en (para efectos indicativos, no prácticos) :  
 DEPRECADO : {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta información. Cuando se deja la información cómo estaba no se realiza la _operación update 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc_donor_fiscal_name={{ eatc_multiple_donors_info. eatc_donor_fiscal_name}}&eatc-donor_code={{ eatc_multiple_donors_info. eatc_donor_code}} 

 NOTA PARA EL DESARROLLO : se documenta como una sola captura, dado el nuevo maestro (por lo tanto la documentación del campo NIT por aparte se depreca). La información se llevará al encabezado del anuncio, por lo tanto se debe evaluar la manera de no hacer explícita la captura a nivel de detalle de la donación, dada que es una captura de tipo encabezado (en la actualidad estos datos se incorporan en el detalle y esto está trayendo inconvenientes cuando se oprime el botón cancelar al ingresar un detalle, dado que resetea los datos. Se debe procurar que esta captura sea más clara para el donante y que se haga una sola vez al inicio (tal como se hace una sola vez por ejemplo con la observación al final).  
 NOTA IMPORTANTE: ANTERIORMENTE SE LLEVABA A {{URL_entorno}}/api/eatcloud/eatc_dona_headers?eatc-donor={{input}} SE DEBE GARANTIZAR QUE A ESTE REGISTRO SE LLEVE SIEMPRE _DOM. cua_user 
 {{URL_entorno}}/api/eatcloud/eatc_dona_headers?eatc-donor={{_DOM. cua_user }} 

 ***NUEVO: Cuentas con multiple_donors=si: y el punto de donación tiene registros en " eatc_pods_cua_donor_nng " y se selecciona el valor por defecto :  El nombre, el código y la cua_user del donante (de no negociados) que se selecciona se guardan en eatc_dona_headers. eatc_donor_fiscal_name, 
 Se guarda en (para efectos indicativos, no prácticos) :  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc_donor_fiscal_name={{ eatc_multiple_donors_info. eatc_donor_fiscal_name}}&eatc-donor_code={{ eatc_multiple_donors_info. eatc_donor_code}} 

 ***NUEVO: Cuentas con multiple_donors=si: y el punto de donación tiene registros en " eatc_pods_cua_donor_nng " y no se selecciona el valor por defecto :  El nombre, el código y la cua_user del donante (de no negociados) que se selecciona se guardan en eatc_dona_headers. eatc_donor_fiscal_name, eatc_dona_headers. eatc-donor_code, eatc_dona_headers. eatc-donor 
 Se guarda en (para efectos indicativos, no prácticos) : 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc_donor_fiscal_name={{ eatc_multiple_donors_info. eatc_donor_fiscal_name}}&eatc-donor_code={{ eatc_multiple_donors_info. eatc_donor_code}}& eatc-donor ={{ eatc_multiple_donors_info . eatc_cua_user }} 

 ***NUEVO : Identificación de la donación como de No Negociados *** 
 Si el usuario selecciona esta opción, el fondo del formulario de captura debe cambiar a un color distintivo, y en un lugar visible del formulario de creación (al inicio de la captura de los datos de los productos) debe aparecer como un "botón" (es decir el texto contenido en una forma rectangular con bordes curvos de color distintivo) el siguiente label: 

 class= lbl_donacion_no_negociados "Donación de No Negociados" 

 ***NUEVO: Selección de punto de donación *** (anteriormente: Edición de coordenadas del punto de donación ): 
 Nota importante: Ante la necesidad de construir una funcionalidad de no negociados, y los hechos que nos han demostrado que la actual funcionalidad de edición de coordenadas, trae como resultado, al no estar respaldada enteramente en maestros de información, la creación de donaciones con información de baja calidad, se ha tomado la determinación de cambiar la anterior funcionalidad de "Edición de coordenadas de puntos de donación" por una funcionalidad que le permite al usuario elegir un punto de donación diferente al desde el cual se encuentra logueado en la App, pero previamente registrado (en lo que se procurará sea siempre la funcionalidad de creación de puntos de donación, la cual está totalmente respaldada por maestros de información) y de esta manera otorgando el control sobre las disposiciones de topes de licencias y también la calidad de los datos.  También se espera que con esta mejora se simplifique el código del la WAPP, dado que no serán necesarias muchas validaciones adicionales para obtener los datos y llevarlos al anuncio, como se planteó originalmente . 

 Despliegue de la funcionalidad 
 Si evaluando la información de la cuenta respectiva ( {{cua_user}} ) permite edición de coordinadas.  Para ello el sistema realiza la siguiente consulta: 
 {{URL_datagov}} /api/eatcloud/eatc_cua?name= {{cua_user}} & edit_coordinates=si&_cmp=name 

 Si el sistema entrega no entrega un resultado válido, entonces no es posible editar coordenadas.  Si entrega un resultado válido entonces el sistema presenta un botón que permite editar/seleccionar una dirección (coordenadas) para efectuar la donación. 

 Ejemplo : Ambiente de pruebas, cuenta "alimentoscarnicos" ambiente de pruebas: 
 El sistema realiza el siguiente llamado:  

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alimentoscarnicos& edit_coordinates=si&_cmp=name       

 Como se recibe una respuesta válida el sistema debe habilitar la funcionalidad para la cuenta en cuestión. 

 Selecciona el punto de donación: ***NUEVO : manejo diferenciado si existe un registro en {{URL_donantes}}/api/{{_DOM.cua_user}}/eatc_pod.eatc_specific_pod_dona_creation *** 
 NOTA PARA EL NUEVO DESARROLLO:  
 El sistema funcionará, como viene funcionando, si no existe registro en "eatc_pod. eatc_specific_pod_dona_creation " , el registro es diferente de "y", el registro es nulo, o no existe el campo (es decir, el punto podrá elegir cualquier punto de donación registrado en eatc_pod).  Si existe un registro en "eatc_pod. eatc_specific_pod_dona_creation " igual a " y ", querrá decir que el punto de donación podrá hacer creación de donaciónes de manera específica para puntos de donación que estén registrados en la estructura {{URL_datagov}}/api/{{_DOM. cua_user }}/ eatc_specific_dona_management , estructura que se utilizará para crear el selector, establecer el identificador (o los identificadores) del punto (de los puntos) "hijo(s)", al cual (a los cuales) le hace gestión específica como "master" el punto que está logueado en el sistema y una vez el usuario realice la selección tomar el "identificador seleccionado" y con él realizar las consultas a {{_DOM. cua_user }}/ eatc_pod (como se hace en la actualidad) para generar el anuncio de donación. 

 Label (place holder): class= lbl_selecciona_pod ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&idlabel= lbl_selecciona_pod) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validación : obligatoriedad 

 Tipo de campo de captura: ( edit_coordinates= si ) 

 ***NUEVO: funcionamiento diferenciado según parámetro de configuración *** 
 El sistema realizará la siguiente consulta:  
 {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation 

 Si en la respuesta se obtiene " y ", entonces el sistema creará el selector de la siguiente manera: 

 Selector único:   ***NUEVO: para puntos con creación para puntos específicos de donación *** 
 La información se toma de ( (en el selector se debe presentar una concatenación del campo eatc-name y eatc-city, así {{eatc-name}} - {{eatc-city}} - {{eatc-responsable}} ): 
 {{URL_datagov}} /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master={{_DOM. cua_master }}&eatc_cua_user={{_DOM. cua_user }}&eatc_master_pod_id= {{current:eatc_pods. eatc-id }} &eatc_management_type= creation &eatc_active_rel= y &_cmp=eatc_child_pod_id,eatc-name,eatc-city,eatc-responsable,eatc_default 

 Valor por defecto 
 El valor por defecto del selector será aquel que tiene un el valor eatc_specific_dona_management. eatc_default =y 

 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre : 

 Antes de crear el selector, el sistema realiza la siguiente consulta: https://devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &_cmp= eatc_specific_pod_dona_creation   

 Como el sistema retorna la respuesta "y", entonces el selector de punto de donación se crea a partir de la información que trae la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&eatc_cua_user=postobon&eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &eatc_management_type= creation &eatc_active_rel= y &_cmp=eatc_child_pod_id,eatc-name,eatc-city,eatc-responsable,eatc_default   

 Dado que la consulta arroja un solo resultado (y el mismo es el valor por defecto), el selector de puntos de donación, solo mostrará una opción (la cual no puede permitir cambiar) y el sistema tomara el dato que llega en " eatc_specific_dona_management . eatc_child_pod_id " como el identificador (eatc-id) que se utilizará posteriormente para consultar {{_DOM. cua_user }}/ eatc_pods , y traer la información que finalmente se incorporará como punto de donación el la donación. 

 Funcionamiento tradicional: 
 Si en la respuesta se obtiene un valor diferente a "y", no se obtiene respuesta, o la respuesta el vacía, nula, o incorrecta, entonces el sistema creará el selector de la siguiente manera (tal como se ha creado hasta el momento, es decir, el selector funciona de manera tradicional): 
 Ejemplo 2, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= P2130234402 : 

 Antes de crear el selector, el sistema realiza la siguiente consulta: https://devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &_cmp= eatc_specific_pod_dona_creation     

 Como el sistema retorna la respuesta vacía ("", es decir, diferente a "y"), entonces el selector de punto de donación se crea como ha venido funcionando hasta el momento 

 Selector único: 
 La información se toma de ( (en el selector se debe presentar una concatenación del campo eatc-name y eatc-city, así {{eatc-name}} - {{eatc-city}} - {{eatc-responsable}} ): 
 Valor por defecto 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= {{current:eatc_pods.eatc-id}} &_cmp= eatc-id, eatc-name,eatc-city, eatc-responsable    

 Otros puntos del mismo donante : 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= ! {{current:eatc_pods.eatc-id}}&eatc_cua_origin= _vacio &_cmp= eatc-id, eatc-name,eatc-city, eatc-responsable 

 Otros puntos no negociados : 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= ! {{current:eatc_pods.eatc-id}}&eatc_cua_origin= _no vacio &_cmp= eatc-id, eatc-name,eatc-city, eatc-responsable 

 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=alimentoscarnicos, eatc-pod_id= nutresa_bog3 : 

 El sistema realiza la siguiente consulta para mostrar el valor por defecto del selector: 
 https://devdonantes.eatcloud.info/api/alimentoscarnicos/eatc_pods?eatc-id= nutresa_bog3 &_cmp= eatc-id, eatc-name,eatc-city,eatc-responsable   

 Alimentos Carnicos Makro Avenida Boyaca  - BOGOTA  - Johana Burbano   

 Para los demás valores del selector correspondientes a puntos del mismo donante se realiza la siguente consulta: 

 https://devdonantes.eatcloud.info/api/alimentoscarnicos/eatc_pods?eatc-id= !nutresa_bog3 & eatc_cua_origin= _vacio &_cmp= eatc-id, eatc-name,eatc-city,eatc-responsable   

 Alimentos Carnicos Makro Cumara - BOGOTA - 
 Alimentos Carnicos Makro Cumara - BOGOTA - Andres Castro Cardoso 
 Alimentos Carnicos Makro Cumara - BOGOTA - Jeison Molina 
 Alimentos Carnicos Makro Cumara - BOGOTA - Paola Ricardo 
 Alimentos Carnicos Makro Cumara - BOGOTA - Yesid Sanchez 
 Alimentos Carnicos Makro Cumara - BOGOTA - Tania Zambrano 
 Alimentos Carnicos Makro Cumara - BOGOTA - "Angelica Rodr guez 
 Alimentos Carnicos Makro Villa del Rio  - Bogotá  - Miguel Yanquen 
 Alimentos Carnicos Makro Puenta Aranda - BOGOTA  - Julian Espitia  

 Para los demás valores del selector correspondientes a puntos de donación de no negociados se realiza la siguente consulta: 

 https://devdonantes.eatcloud.info/api/alimentoscarnicos/eatc_pods?eatc-id= !nutresa_bog3 & eatc_cua_origin= _novacio &_cmp= eatc-id, eatc-name,eatc-city,eatc-responsable        
 EXITO ENVIGADO - ENVIGADO - JUAN CAMILO GIRALDO  

 Selección del punto de donación por parte del usuario: 
 El usuario selecciona el valor por defecto ( en el funcionamiento tradicional , es decir cuando: {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation trae una respueta diferente a "y" ) .  
 Si el usuario selecciona el valor por defecto, el funcionamiento es similar al de al Web App cuando no hay "Edit_coordinates=si", es decir, el sistema toma los datos del Punto de Donación que está loggeado en el sistema y con ellos llena toda la información de la donación. 

 El usuario no selecciona el valor por defecto ( en el funcionamiento tradicional , es decir cuando: {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation trae una respueta diferente a "y" ) . 
 A partir de la selección del usuario (tomando el eatc_pods. eatc-id , respectivo) El sistema debe validar si el punto está activo o no, mediante la siguiente consulta: 
 {{ URL_donantes }}/api/allpods/ eatc_pods ?eatc-id={{eatc_pods. eatc-id }}&_eatc-cua= {{_DOM. cua_user }} &eatc_active= y 

 Si el sistema no arroja una respuesta válida (lo que quiere decir que el punto de donación está inactivo), el sistema debe desplegar el siguiente mensaje. 
 class= lbl_pod_inactivo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&idlabel= lbl_pod_inactivo )  

 "Punto de donación inactivo.  Por favor realiza otra selección" 

 El sistema debe volver a mostrar el valor por defecto del selector y retirar del mismo el punto de donación seleccionado, para evitar una segunda selección errónea. 

 Si el sistema arroja una respuesta válida (es decir, que el punto de donación está activo, entonces el sistema continúa con la selección realizada por el usuario. 

 El usuario selecciona un punto de donación de su propia cuenta usuario que está activo ( en el funcionamiento tradicional , es decir cuando: {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation trae una respueta diferente a "y" ) . 

 El sistema debe consultar los datos del punto de donación, a partir del {{eatc_pods. eatc-id }} seleccionado por el usuario, de la siguiente manera: 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= {{eatc_pods. eatc-id }}& _cmp= eatc-id, eatc-name,eatc-adress,eatc-phone,eatc-typology_a,eatc-typology_b,eatc-typology_c,eatc-lat,eatc-lon,eatc-city,eatc-province 

 Para llevarlos a la información de la respectiva cabecera del anuncio de donación de la siguiente manera: 
 eatc_pods. eatc-id => eatc_dona_headers. eatc-pod_id 
 eatc_pods. eatc-name => eatc_dona_headers. eatc-pod_name 
 eatc_pods. eatc-adress => eatc_dona_headers. eatc-pod_address 
 eatc_pods. eatc-phone => eatc_dona_headers. eatc-pod_phone 
 eatc_pods. eatc-typology_a => eatc_dona_headers. eatc-pod_typology_a 
 eatc_pods. eatc-typology_b => eatc_dona_headers. eatc-pod_typology_b 
 eatc_pods. eatc-typology_c => eatc_dona_headers. eatc-pod_typology_c 
 eatc_pods. eatc-lat => eatc_dona_headers. eatc-lat 
 eatc_pods. eatc-lon => eatc_dona_headers. eatc-lon 
 eatc_pods. eatc-city => eatc_dona_headers. eatc-city 
 eatc_pods. eatc-province => eatc_dona_headers. eatc-province 

 El usuario selecciona un punto de donación de no negociados ( en el funcionamiento tradicional , es decir cuando: {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation trae una respueta diferente a "y" ) . 

 A partir de la selección del usuario (tomando el eatc_pods. eatc-id , respectivo) El sistema debe validar si el punto está activo o no, mediante la siguiente consulta: 
 {{ URL_donantes }}/api/allpods/ eatc_pods ?eatc-id={{eatc_pods. eatc-id }}&_eatc-cua= {{eatc_pods. eatc_cua_origin }} &eatc_active= y 

 Si está inactivo, presenta lo mismo de la misma información de inactividad que se maneja en los puntos de donación propios del donante.  
 Cuando el punto está activo entonces:  

 El sistema debe consultar los datos del punto de donación, a partir del {{eatc_pods. eatc-id }} seleccionado por el usuario, de la siguiente manera: 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= {{eatc_pods. eatc-id }}& _cmp= eatc-id, eatc-name,eatc-adress,eatc-phone,eatc-typology_a,eatc-typology_b,eatc-typology_c,eatc-lat,eatc-lon,eatc-city,eatc-province, eatc_cua_origin 

 Para llevarlos a la información de la respectiva cabecera del anuncio de donación de la siguiente manera: 
 eatc_pods. eatc-id => eatc_dona_headers. eatc-pod_id 
 eatc_pods. eatc-name => eatc_dona_headers. eatc-pod_name 
 eatc_pods. eatc-adress => eatc_dona_headers. eatc-pod_address 
 eatc_pods. eatc-phone => eatc_dona_headers. eatc-pod_phone 
 eatc_pods. eatc-typology_a => eatc_dona_headers. eatc-pod_typology_a 
 eatc_pods. eatc-typology_b => eatc_dona_headers. eatc-pod_typology_b 
 eatc_pods. eatc-typology_c => eatc_dona_headers. eatc-pod_typology_c 
 eatc_pods. eatc-lat => eatc_dona_headers. eatc-lat 
 eatc_pods. eatc-lon => eatc_dona_headers. eatc-lon 
 eatc_pods. eatc-city => eatc_dona_headers. eatc-city 
 eatc_pods. eatc-province => eatc_dona_headers. eatc-province 
 eatc_pods. eatc_cua_origin => eatc_dona_headers. eatc_cua_origin 

 ***NUEVO: El usuario selecciona un punto de donación de creación específica ( nuevo funcionamiento , es decir cuando: {{url_donantes}} /api/ {{_DOM.cua_user}} /eatc_pods?eatc-id= {{current:eatc_pods. eatc-id }} &_cmp= eatc_specific_pod_dona_creation trae una respueta igual a "y" ) *** . 

 A partir de la selección del usuario (tomando el valor que llega en: "eatc_specific_dona_management. eatc_child_pod_id " ) El sistema debe validar si el punto está activo o no, mediante la siguiente consulta: 

 El sistema toma ese valor para realizar la validación de punto activo y para ello realiza la siguiente consulta: 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= {{ eatc_specific_dona_management. eatc_child_pod_id }}& _cmp= eatc-id, eatc-name,eatc-adress,eatc-phone,eatc-typology_a,eatc-typology_b,eatc-typology_c,eatc-lat,eatc-lon,eatc-city,eatc-province, eatc_cua_origin 

 Para realizar la validación de actividad, realiza la siguiente consulta a partir de los datos obtenidos: 
 {{ URL_donantes }}/api/allpods/ eatc_pods ?eatc-id={{eatc_pods. eatc-id }}&_eatc-cua= {{eatc_pods. eatc_cua_origin }} &eatc_active= y 

 Si está inactivo, presenta lo mismo de la misma información de inactividad que se maneja en los puntos de donación propios del donante.  

 Cuando el punto está activo entonces:  

 El sistema debe consultar los datos del punto de donación, a partir del {{ eatc_specific_dona_management. eatc_child_pod_id }} seleccionado por el usuario, de la siguiente manera: 
 {{url_donantes}} /api/ {{_DOM. cua_user }} /eatc_pods?eatc-id= {{ eatc_specific_dona_management. eatc_child_pod_id }}& _cmp= eatc-id, eatc-name,eatc-adress,eatc-phone,eatc-typology_a,eatc-typology_b,eatc-typology_c,eatc-lat,eatc-lon,eatc-city,eatc-province, eatc_cua_origin 

 Para llevarlos a la información de la respectiva cabecera del anuncio de donación de la siguiente manera: 
 eatc_pods. eatc-id => eatc_dona_headers. eatc-pod_id 
 eatc_pods. eatc-name => eatc_dona_headers. eatc-pod_name 
 eatc_pods. eatc-adress => eatc_dona_headers. eatc-pod_address 
 eatc_pods. eatc-phone => eatc_dona_headers. eatc-pod_phone 
 eatc_pods. eatc-typology_a => eatc_dona_headers. eatc-pod_typology_a 
 eatc_pods. eatc-typology_b => eatc_dona_headers. eatc-pod_typology_b 
 eatc_pods. eatc-typology_c => eatc_dona_headers. eatc-pod_typology_c 
 eatc_pods. eatc-lat => eatc_dona_headers. eatc-lat 
 eatc_pods. eatc-lon => eatc_dona_headers. eatc-lon 
 eatc_pods. eatc-city => eatc_dona_headers. eatc-city 
 eatc_pods. eatc-province => eatc_dona_headers. eatc-province 
 eatc_pods. eatc_cua_origin => eatc_dona_headers. eatc_cua_origin 

 ***NUEVO : Identificación de la donación como de No Negociados *** 
 Si el usuario selecciona esta opción, el fondo del formulario de captura debe cambiar a un color distintivo, y en un lugar visible del formulario de creación (al inicio de la captura de los datos de los productos) debe aparecer como un "botón" (es decir el texto contenido en una forma rectangular con bordes curvos de color distintivo) el siguiente label: 

 class= lbl_donacion_no_negociados "Donación de No Negociados" 

 ***NUEVO : punto creador de la donación *** 
 Punto creador de la donación (eatc_dona_creator_pod):  
 Es un nuevo campo que ayuda a identificar el punto que creó el anuncio (que es diferente al punto origen del anuncio, para el caso de los no negociados).  Este dato, combinado con el eatc_donor , servirán para identificar el punto origen y ciertos parámetros de configuración que serán necesarios a la hora de capturar la información de la donación y los productos. Es una captura automática que debe generar el sistema a partir de los datos del usuario que se encuentra loggeado en la WAPP, dado que es el código de dicho punto. 
 Información técnica del parámetro: eatc_dona. eatc_dona_creator_pod   eatc_dona_headers. eatc_dona_creator_pod 
 Tipo : corresponde al eatc_pod. eatc-id del punto que está logeado en la WAPP y que está creando la donación (para el caso de no negociados, este punto puede diferir del punto al cual se le registra la donación) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona? eatc_dona_creator_pod ={{query}} ***PENDIENTE POR CREAR*** 
 Método para guardar específico (para efectos indicativos, no prácticos, dado que los parámetros se envían todos en una sola llamada al CRD) :  

{{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona&_operación=insert& eatc_dona_creator_pod ={{query}} ***PENDIENTE POR CREAR*** 

 Datos que se digitan en el encabezado (una sola vez por anuncio): obligatoriedad según parámetro de configuración *** 
 Documento soporte:  
 Campo de texto abierto que se despliega si se cumple la siguiente condición: que en parámetro eatc_dona_upl tenga como valor "yes" ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ). En caso que el parámetro tenga como valor "no" no se debe desplegar campo de captura y se toma este dato como vacío (para posteriormente llevarlo al registro . 
 **NUEVO**:  ID Para identificar el div de la funcionalidad: id=" btn_document_soporte " 
 Información técnica del parámetro:  eatc_sale.eatc-doc 
 Descripción ( tooltip ) : Ingrese por favor un documento de soporte 
 Tipo : Pregunta abierta ( cuadro de texto ) ( información técnica sobre el tipo de pregunta : PAT ) 
 Tipo de dato: string 
 Obligatoriedad ***NUEVO: obligatoriedad según parámetro de configuración *** 
 El sistema realiza la siguiente consulta ealiza la siguiente consulta, para el punto de donación cuyo usuario está realizando el anuncio de donación (el POD en el cual el respectivo usuario está loggeado).  NOTA IMPORTANTE: este dato puede variar del dato que se incorpora en la donación como punto de donación, debido a la funcionalidad de No Negociados, y es por eso que se estableció la funcionalidad para registrar el identificador del punto que crea la donación o eatc_dona_headers. eatc_dona_creator_pod . Es a este punto creador de la donación al que se le debe consultar el parámetro de configuración que ensegida se establece y por eso se deja así la notación.  También se deberá tomar el _DOM. cua_user como el donante de la donación (eatc-donor), NO como la cua_origen . 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_user}}/eatc_pods?eatc-id={{eatc_dona_headers. eatc_dona_creator_pod }}&_cmp=eatc_doc_madatory 
 Respuesta diferente de "y", igual a "n", vacía, nula o el campo no existe. 
 Si la consulta al API define que el campo no existe, o que la respuesta es diferente a "y", es igual a "n", es nula o es vacía, entonces el sistema ha determinado que este campo no es obligatorio, por lo tanto no se exigirá su llenado para completar la donación 
 Respuesta igual a "y" 
 El sistema determinó que el campo es obligatorio, razón por la cual no dejará crear la donación hasta que se llene esta información. 

 Validación : obligatoriedad, según parámetro de configuración. 
 Se guarda en : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-doc={{input}} 
 Método para guardar específico (para efectos indicativos, no prácticos, dado que los parámetros se envían todos en una sola llamada al CRD) :  

{{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operación=insert&eatc-doc={{input}} 

 Adjuntar documentos de evidencias/soportes (opcional) *** 
 Nota desarrollo: se puede basar en funcionalidad ya implementada en el BO de Beneficiarios (funcionalidad para cua_master: usuario: logistica@abaco.org.co pass: 1abaco_2021 : Activaciones > Detalle de activación:    https://beneficiarios.eatcloud.info/_nbob/#!/bactivardetalle ), lo cual implicaría que el desarrollo sea tomar esa funcionalidad y adaptarla al presente BO.  La funcionalidad deberá permitir subir documentos (PDF, doc, exls) y también imágenes (png, jpg, gif). 

 Place holder: 
 class=" lbl_adjuntar_soportes " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =wapp&idlabel= lbl_adjuntar_soportes )  

 Botón: "Adjuntar nuevo documento" 
 class=" lbl_adjuntar_nuevo_documento " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =wapp&idlabel= lbl_adjuntar_nuevo_documento )  

 Archivos de máximo 3 Megas 

 Como indicación para la subida de documentos se debe colocar el siguiente label 
 class=" lbl_doc_maximo_peso " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =wapp&idlabel= lbl_doc_maximo_peso )  

 Validación para la subida de documentos: 

 Ninguna, dado que es un campo opcional.  Si se adjunta, el documento no debe pesar más de 3 Megas.  En caso que pese más de 3 megas se debe desplegar el siguiente mensaje: 

 class=" lbl_documento_pesado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =wapp&idlabel= lbl_documento_pesado ) 

 "El documento adjunto sobrepasa el peso máximo estipulado. Por favor inténtalo de nuevo con un archivo más liviano" 

 El documento adjunto se sube a la plataforma: 

 Asociado al código de la donación , se debe subir el documento a la plataforma (nombrándolo como se deba para identificarlo adecuadamente en el sistema de archivos definido para este fin: eatc_doc_name ) y deberá guardar también la URL desde la cuál se recupera el archivo adjunto ( eatc_doc_url ) (deberá guardar entonces eatc_doc_name y eatc_doc_url en variables que estén disponibles cuando se termina de crear la donación).  Se recomienda que el sistema de archivos definido para este fin posea carpetas por días (se deberán revisar las funciones de subida de archivos a la plataforma para adaptarlas a este requisito).  Se podrán adjuntar varios documentos o imágenes a un mismo anuncio . 

Una vez la donación es creada , el sistema deberá realizar la siguiente inserción, para referenciar el documento adjunto a la donación creada (mediante su código): 

 {{ URL_entorno_datagov }}/crd/ eatcloud /?_tabla= eatc_dona_attachments &_operacion= insert &eatc_cua_master={{_DOM. cua_master }}&eatc_cua_user={{_DOM. cua_user }}&eatc_pod_id={{eatc_pods. eatc-id }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&eatc_doc_name={{ eatc_doc_name }}&eatc_doc_url={{ eatc_doc_url }} 
 ***NUEVO: selector de comida preparada *** 
 Nota desarrollo: se deberá implementar un selector de “Comida preparada” que deberá llevar a un nuevo campo (de tipo “boleano”) del encabezado de donaciones: eatc_dona_headers. eatc_prepared_food (campo que deberá crearse en las estructuras legacy y modernizada como parte de la presente implementación), el valor “y” en caso de que el usuario confirme que la donación es de comida preparada, o el valor “n”, en caso de que no sea así.  El campo tendrá un valor por defecto de acuerdo a la vertical del donante, de tal manera que los donantes del sector horeca, tendrán como por valor por defecto del campo el “y”, y los demás donantes el “n” . 

 Place holder: Comida Preparada 
 class=" lbl_comida_preparada " 

 Botón: “Tipo prendido y apagado: posición prendido : valor de la selección “ y ”. Posición apagado : valor de la selección “ n ”" 

 Validación para definir el valor por defecto del botón: 

 El sistema deberá realizar la siguiente consulta: 

 {{URL_entorno_datagov}}/ api/eatcloud/eatc_cua?name={{_DOM. cua_user }}&_distinct= vertical 
Si la respuesta es igual a “ horeca ”, el valor por defecto del selector será “ prendido ” (valor de la selección: “ y ”) 

Si la respuesta es diferente a “horeca”, el valor por defecto del selector será “ apagado ” (valor de la selección: “ n ”) 

El usuario podrá modificar el valor de la selección, prendiendo o apagando el selector (según su decisión). 

Una vez la donación es creada , el sistema deberá llevar el respectivo valor de la selección ("y" o “n”), al encabezado de la donación (si se hiciera un registro individual de este valor, este sería el llamado de inserción, a modo indicativo): 
 {{URL_entorno_donantes} }/crd/eatcloud/?_tabla= eatc_dona_headers &_operacion= update & eatc_prepared_food = {{" y "/" n "}}& WHEREeatc-code={{eatc_dona_headers. eatc-code }} 
 Detalle de anuncio de donación 
 Los datos de detalle se pueden adicionar varias veces a la transacción (un anuncio de donación, puede tener "n" detalles, tantos como sea necesarios para registrar una donación de un conjunto de productos) a partir de la selección de un producto utilizando un buscador de productos y se hace de la siguiente manera: 

 Productos (eatc-name): 
 El sistema deberá evaluar el parámentro eatc_odds_app de la cuenta (cua) respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), para establecer el tipo de captura que utiliza para este dato:  hay tres opciones, tradicionales y una nueva opción según la escogencia realizada en la funcionalidad de Multiples Donantes (validación de punto de donación de no negociados) : 

 0. ***NUEVO: Cuentas con multiple_donors=si: y el punto de donación tiene registros en " eatc_pods_cua_donor_nng " y no se selecciona el valor por defecto : 

 Esto quiere decir que el nombre del producto se debe tomar del maestro de productos de la cuenta donante de no negociados, por lo tanto a partir de la selección realizada , se realiza la siguiente consulta. 
 {{URL_donantes}}/api/ {{ eatc_multiple_donors_info. eatc_cua_user}} /eatc_odds?_id=_* 

 [predictive text] Buscador de productos 
 La App despliega un buscador de producto, que se debe nutrir para su búsqueda, de la tabla eatc_odds de la cuenta [cua] respectiva y tener capacidades de teclado predictivo para encontrar rápidamente el producto por todas sus características ( nombre, códigos, tipologías, etc ) y lectura de código de barras (esta lectura de código de barras opera sobre: eatc_odds,eatc-odd_code ) . 
 Ejemplo : cua_user: exito, ambiente de pruebas, el usuario seleccionó mediante la funcionalidad "multiple_donors" la opción cuya " eatc_multiple_donors_info. eatc_cua_user " es " alimentoscarnicos " 

 Como el usuario no realizó la selección de la cuenta por defecto, el sistema deberá realizar la siguiente consulta para traer la información de los productos:  

 https://devdonantes.eatcloud.info/api/alimentoscarnicos/eatc_odds?_id=_*   

 En el buscador de productos, también se podrá digitar el eatc-odd_code, para traer el producto respectivo. 
 En el campo de captura del nombre del producto, también se podrá digitar el código del producto (eatc-odd_code) y que a través de dicha digitación se traiga el nombre del artículo. Esto se solicita, porque en maestros de productos con muchos productos (como es el caso por ejemplo de Makro), la búsqueda por nombre puede requerir una digitación casi que completa para lograr tener resultados en el buscador (para productos que manejan muchas referencias), y si se digita un código puede ser más fácil encontrar el producto. 

 ***LAS demás opciones funcionan tal como lo venían haciendo antes, cuando se selecciona el valor por defecto o un donante que es propio de la cuenta, es decir, que no es un donante de no negociados*** 
 1. eatc_cua.eatc_odds_app = eatc_dona_app:  
 Esto quiere decir que el nombre del producto se debe tomar de la digitación de un nombre de producto.  Por lo tanto la App debe desplegar un campo de texto [input type=textfield data type=string] para que el usuario digite el nombre del producto a donar. 

 Ejemplo: 
 Para la cuenta "prueba" el valor de eatc_odds_app   ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=prueba   ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=prueba )) es eatc_dona_app por lo tanto la App deberá proveer un campo de captura tipo texto para que el usuario digite el nombre del producto (en etapas posteriores del desarrollo con esta información digitada se debe empezar a llenar un repositorio que sirva para activar funciones de texto predictivo para futuras digitaciones de producto) 

 ***IDEA*** capturar las categorías Ábaco **** 

 2. eatc_cua.eatc_odds_app = no trae datos o es indefinido 
 Se aplica lo mismo que en el punto anterior.  

 3. eatc_cua.eatc_odds_app = eatc_odds:  
 Esto quiere decir que el nombre del producto se debe tomar del maestro de productos respectivo (eatc_odds) y se aplica el siguiente tipo de input. 
 [predictive text] Buscador de productos 
 La App despliega un buscador de producto, que se debe nutrir para su búsqueda, de la tabla eatc_odds de la cuenta [cua] respectiva y tener capacidades de teclado predictivo para encontrar rápidamente el producto por todas sus características ( nombre, códigos, tipologías, etc ) y lectura de código de barras (esta lectura de código de barras opera sobre: eatc_odds,eatc-odd_code ) . 
 Ejemplo : 

 Suponiendo que el Éxito ( cua=exito ) tuviera configurada la opción de generar anuncios de donación  desde la app ( eatc_dona_upl : " yes ", cosa que no ocurre), el buscador debería utilizar el maestro de la cuenta respectiva para alimentar el buscador: ( https://devdonantes.eatcloud.info/api/ [cua] /eatc_odds?_id=_ *) 
 Así:  
(dada la cantidad de datos que tiene el Éxito, para efectos demostrativos se utiliza la consulta de un solo artículo): 
 https://devdonantes.eatcloud.info/api/exito/eatc_odds?_id=00001 

 Nota importante :  los atributos estándar del objeto de donación se pueden consultar aquí:  https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&metodo=eatc_odds Los atributos obligatorios deben ser estos: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&metodo=eatc_odds&obligatorio=si (para el caso del Éxito por el tamaño del maestro el dato de la equivalencia a KG fue entregado en otro maestro.  Se evaluará si esta es una circunstancia normal, caso en el cual se configurará un maestro adicional para generar ese dato). 

 En el buscador de productos, también se podrá digitar el eatc-odd_code, para traer el producto respectivo. 
 En el campo de captura del nombre del producto, también se podrá digitar el código del producto (eatc-odd_code) y que a través de dicha digitación se traiga el nombre del artículo. Esto se solicita, porque en maestros de productos con muchos productos (como es el caso por ejemplo de Makro), la búsqueda por nombre puede requerir una digitación casi que completa para lograr tener resultados en el buscador (para productos que manejan muchas referencias), y si se digita un código puede ser más fácil encontrar el producto. 

 [Input] Digitación de cantidades: ***NUEVO: validación de datos en cero y negativos y permitir el ingreso de números con dos cifras decimales (no solamente enteros) *** 
 El sistema despliega un formulario para digitar las cantidades del artículo ( unidades: debe ser el label del input ). El input debe ser de tipo numérico float.  ***NUEVO: El input no debe permitir la captura de cifras negativas o de cantidades en cero.  Cuando esto ocurra el campo debe quedar coloreado en un fondo rojo, desplegar el siguiente label: class= lbl_cantidad_no_permitida_revisar :  " Cantidad no permitida, por favor revisa " , y no debe permitir grabar el registro: hasta que no se corrija el número, no se podrá guardar el registro. *** 

  Con este Input ( eatc-odd_quantity) , el sistema debe calcular los siguientes datos: 
 Peso total de la mercancía donada: eatc-odd_total_weight_kg: corresponde a la multiplicación de las unidades digitadas por eatc-odd_unit_weight_kg ( eatc-odd_quantity* eatc-odd_unit_weight_kg). En Información de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_weight_kg . 

 Costo total de la mercancía donada: eatc-odd_total_cost: corresponde a la multiplicación de las unidades digitadas por eatc-odd_unit_cost ( eatc-odd_quantity*eatc-odd_unit_cost ). En Información de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_cost . 

 Validación de peso total (eatc-odd_total_weight_kg) cuando el resultado es cero (no se deben permitir que los pesos estén en cero): 
 Si el sistema detecta que el peso total de la mercancía donada (eatc-odd_total_weight) es igual a cero, se debe mostrar en una ventana modal el siguiente mensaje: 
 Contar con un peso aproximado unitario por producto, nos es de gran ayuda para medir el impacto social y ambiental de cada donación y para asignar la donación al beneficiario más idóneo. 

 Ingresa el peso unitario 

 Si se acciona la opción Ingresa el peso unitario , el sistema se debe posar en el dato de Peso unitario en KG ( eatc-odd_unit_weight_kg ), para permitir su edición de la manera más óptima posible (por ejemplo seleccionando el cero). 
 En términos generales la validación no dejará pasar al usuario, si no digita un peso unitario. 

 Validación de peso total (eatc-odd_total_weight_kg) cuando el resultado es un peso muy elevado => MENSAJE CON NÚMEROS VIVOS PARA PROMOVER UNA EFECTIVA VERIFICACION: 
 Con el ánimo de promover una verificación de peso más efectiva (dado que siguen habiendo errores de digitación que traen como resultado anuncios con pesos erróneos exagerados), se hace la siguiente propuesta de mensaje en ventana modal, con un número vivo (equivalencia del peso en estibas llenas), que deberá presentarse cuando el peso excede un valor determinado: 

 Obtención del dato de peso excesivo ( eatc_excessive_weight_kg ): 
 Para obtener el dato del peso excesivo, a partir del cual se desplegará el modal, será el siguiente: 
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= {{_DOM. cua_user }} &eatc_pod_id= {{eatc_pod. eatc-id }} &_distinct= eatc_excessive_weight_kg 

 Si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= {{_DOM. cua_user }} &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg 

 Si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg 

 Y por último, si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg 

 Si no se obtiene respuesta (por un problema de conectividad o de respuesta del servidor, dado que la última consulta tiene datos disponibles) la wapp debe tener el valor "quemado" de 500, a manera de error handler. 

 T an pronto el sistema tenga los datos para calcular el peso total del producto donado (unidades por peso unitario) si el sistema detecta que dicho peso total de la mercancía donada ( eatc-odd_total_weight ) es mayor al parámetro que se obtiene de las anteriores consultas eatc_excessive_weight_kg se debe mostrar en una ventana modal diseñada con los siguientes labels (para que quede de una vez correctamente internacionalizado), dispuestos de la siguiente manera (más abajo se presenta un listado de los labels y las variables a utilizar): 

 DEPRECADO: (el valor de este parámetro inicialmente se quema en la APP y será igual a 500 KG , posteriormente se podrá consultar con un API que se estará ajustando diariamente) ,  

 Ejemplo 1 (ambiente de pruebas): de peso excesivo para el eatc_pod. eatc-id=20, de _DOM. cua_user=exito, _DOM. cua_master=abaco 
 Se debe realizar la siguiente consulta: 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= abaco &eatc_cua= exito &eatc_pod_id= 20 &_distinct= eatc_excessive_weight_kg 

 Dado que el sistema responde: 
 { 
 ts : "210623113311" , 
 op : true , 
 cont : 1 , 
 res :  
 [ 
 { 
 eatc_excessive_weight_kg : "1000" 
 } 
 ], 
 mem : 0.41 , 
 time : "00:00:00" 
 } 
 A los anuncios con peso mayor a 1000 KG desplegarán el pop-up de peso excesivo 

 Ejemplo 2 (ambiente de pruebas): de peso excesivo para el eatc_pod.eatc-id=9JcLv7lAdqqJ4siphIBIE, de _DOM.cua_user=argentina2, _DOM.cua_master=argentina 

 Se debe realizar la siguiente consulta: 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= argentina2 &eatc_pod_id=9JcLv7lAdqqJ4siphIBIE&_distinct= eatc_excessive_weight_kg   

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= argentina2 &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg    

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg    

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_excessive_weight_kg    

 Dado que el sistema responde: 
 { 
 ts : "210623113311" , 
 op : true , 
 cont : 1 , 
 res :  
 [ 
 { 
 eatc_excessive_weight_kg : "500" 
 } 
 ], 
 mem : 0.41 , 
 time : "00:00:00" 
 } 
 A los anuncios con peso mayor a 500 KG desplegarán el pop-up de peso excesivo 

 Diseño: https://materializecss.com/modals.html 
 Recordar colocar adentro de la etiqueta ( aquí ) el texto de la misma, para que sirva como valor por defecto (por si las funciones de internacionalización fallan). 

 class=" lbl_atencion " 
 Texto etiqueta: ¡Atención!" 
 ( título ) 

 class=" lbl_acabas_de_registrar_donacion " 
 Texto etiqueta: Acabas de registrar una donación de 
 ( texto normal ) 

 {{eatc-odd_quantity}} 
 Cantidad del producto digitada por el usuario  
 (variable resaltada en rojo y negrilla ). 

 class=" lbl_unidades_producto " 
 Texto etiqueta: unidad(es) del producto 
  ( texto normal ) 

 {{eatc-name}} 
 Nombre del producto  
 (digitado o ingresado a partir de maestro por el usuario: resaltado en negrilla ). 

 class=" lbl_tienen_peso_total " 
 Texto etiqueta: que tiene(n) un peso total de 
 ( texto normal ) 

 {{eatc-odd_total_weight_kg}} 
 Peso total del producto que corresponde a la cantidad del producto por su peso unitario  
 (Cómputo a partir de las cantidades digitadas  y los pesos digitados o ingresados a partir de maestro respectivo por el usuario: resaltado en rojo y negrilla ). 

 class=" lbl_equivalente_a " 
 Texto etiqueta: lo cual equivale aproximadamente a: 
 ( texto normal ) 

 {{n}} 
 Cálculo de la cifra viva de equivalencia a estibas del producto ( número muy grande, en rojo, muy resaltado ). En principio una estiba corresponde a 1000 KG, por lo tanto este número se obtiene de dividir {{eatc-odd_total_weight_kg}} entre 1000 .  Este valor debe tener el siguiente comportamiento, según el valor que de: 
 Si el valor se sitúa entre 0,5 y 0,6666....( o 2/3 ): se debe colocar: más de 1/2 
 Si el valor se sitúa entre (2/3) y 0,999999: se debe colocar: más de 2/3 
 Si el valor es mayor o igual a 1: se debe colocar el resultado de la división ( {{eatc-odd_total_weight_kg}} entre 1000) con dos cifras decimales cuando el resultado no sea un entero.  Si el resultado es un entero o muy cercano a un entero, NO se deben colocar cifras decimales. 

 x (imagen estiba) 
 La imagen definitiva se encuentra aquí: http://repograf.eatcloud.info/img/x_cajas_en_estiba.png   

 class=" lbl_estibas_maxima_capacidad " 
 Texto etiqueta: Estiba(s) llena(s) a su MÁXIMA capacidad 
 ( resaltado en negrilla y cursiva.  Se coloca abajo de la imagen) 

 class=" lbl_estas_seguro " 
 Texto etiqueta: ¿Estás seguro, que este es la cantidad / peso de producto donado es correcta? 
 ( texto resaltado ) 

 Botón : class=" lbl_corregir_peso_cantidad " 
 Texto etiqueta: NO, debo CORREGIR el peso y / o cantidad 
 ( Botón ): Si el usuario presiona este botón: el sistema se debe posar en el dato de Cantidad para permitir su edición y posteriormente la de peso (se debe posar en el primer de estos datos pedido por el formulario) de la manera más óptima posible (por ejemplo seleccionando todo el número de la cantidad digitada). 

 Botón : class=" lbl_confirmar_peso_cantidad " 
 Texto etiqueta: Si, deseo donar esa cantidad / peso 
 ( Botón ): Si el usuario presiona este botón: el sistema se debe permitir seguir adelante. 

 ***NUEVO: Validación de peso bloqueante ( eatc_max_weight_kg ): peso a partir del cual no se podrá ingresar datos a la donación *** 
 Con el ánimo de promover una verificación de peso más efectiva (dado que siguen habiendo errores de digitación que traen como resultado anuncios con pesos erróneos exagerados), se implementa la funcionalidad de validación de pesos máximos, o bloqueantes, que son aquellos pesos a partir de los cuales no se podrá crear donaciones (es una mejora para, además del mensaje vivo que se implementó previamente, si se llega a determinado peso, el sistema simplemente no deje realizar la donación). 

 Obtención del dato de peso máximo o bloqueante ( eatc_max_weight_kg ): 
 Para obtener el dato del peso máximo o bloqueante, a partir del cual el sistema no permitirá el ingreso de los datos , se hace la siguiente consulta: 
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= {{_DOM. cua_user }} &eatc_pod_id= {{eatc_pod. eatc-id }} &_distinct= eatc_max_weight_kg 

 Si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= {{_DOM. cua_user }} &eatc_pod_id= _default &_distinct= eatc_max_weight_kg 

 Si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= {{_DOM. cua_master }} &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_max_weight_kg 

 Y por último, si la anterior consulta no trae resultados se debe realizar esta:  
 {{URL_entorno_datagov}} /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_max_weight_kg 

 Si no se obtiene respuesta (por un problema de conectividad o de respuesta del servidor, dado que la última consulta tiene datos disponibles) la wapp debe tener el valor "quemado" de 500 , a manera de error handler. 

 T an pronto el sistema tenga los datos para calcular el peso total del producto que se están ingresando, más el peso total de los productos previamente ingresados a la donación (unidades por peso unitario + sumatoria de pesos totales de productos previamente agregados ) si el sistema detecta que dicho peso total de la mercancía donada ( sumatoria de eatc-odd_total_weight ) es mayor al parámetro que se obtiene de las anteriores consultas eatc_max_weight_kg el sistema no le deberá permitir al usuario ingresar los datos del producto que está ingresando, limpiando los datos del formulario que se está ingresando y mostrando el siguiente mensaje (puede ser en una ventana modal): 

 class= lbl_bloqueo_por_peso_max1 "La donación ha excedido el peso máximo que tu punto de donación tiene configurado:" 

 Concatenar con el dato de peso máximo obtenido, seguido de "KG" 
 {{eatc_max_weight_kg}} "KG" 

 Concatenar con la segunda parte del mensaje 
 class= lbl_bloqueo_por_peso_max2   "Por favor revisa las cantidades y los kilogramos  que estás ingresando. Si son correctos, para resolver la situación rápidamente, recomendamos que dividas la donación en varias más pequeñas que no sobrepasen el límite y comunícate con nuestra mesa de servicio con el código config_peso_max , indicando el nombre del punto de donación y el nuevo límite sugerido para darte una solución definitiva." 

 Ejemplo 1 (ambiente de pruebas): de peso excesivo para el eatc_pod. eatc-id=20, de _DOM. cua_user=exito, _DOM. cua_master=abaco 
 Se debe realizar la siguiente consulta: 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= abaco &eatc_cua= exito &eatc_pod_id= 20 &_distinct= eatc_max_weight_kg   

 Dado que el sistema responde: 
 { 
     "ts": "240410153333", 
     "op": true, 
     "cont": 1, 
     "res": [ 
         { 
             "eatc_max_weight_kg": " 5000 " 
         } 
     ], 
     "mem": 0.39, 
     "time": "00:00:00" 
 } 
 A los anuncios con peso mayor a 5000 KG se no se les permitirá ingresar el respectivo dato , y se les desplegará el mensaje :  

 "La donación ha alcanzado el peso máximo permitido. Por favor revisa los datos que estás ingresando.  Si el problema persiste, recomendamos que dividas la donación en varias donaciones más pequeñas y comunícate con nuestra mesa de servicio con el código config_peso_max , si requieres cambiar dicho límite" 

 Ejemplo 2 (ambiente de pruebas): de peso excesivo para el eatc_pod.eatc-id=9JcLv7lAdqqJ4siphIBIE, de _DOM.cua_user=argentina2, _DOM.cua_master=argentina 
 Se debe realizar la siguiente consulta: 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= argentina2 &eatc_pod_id=9JcLv7lAdqqJ4siphIBIE&_distinct= eatc_max_weight_kg   

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= argentina2 &eatc_pod_id= _default &_distinct= eatc_max_weight_kg     

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_max_weight_kg     

 Como no se obtiene una respuesta válida, se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &eatc_cua= _default &eatc_pod_id= _default &_distinct= eatc_max_weight_kg   

 Dado que el sistema responde: 
 { 
     "ts": "240410153836", 
     "op": true, 
     "cont": 1, 
     "res": [ 
         { 
             "eatc_max_weight_kg": " 500 " 
         } 
     ], 
     "mem": 0.39, 
     "time": "00:00:00" 
 } 
 A los anuncios con peso mayor a 500 KG no se les permitirá ingresar el respectivo dato , y se les desplegará el mensaje :  

 "La donación ha alcanzado el peso máximo permitido. Por favor revisa los datos que estás ingresando.  Si el problema persiste, recomendamos que dividas la donación en varias donaciones más pequeñas y comunícate con nuestra mesa de servicio con el código config_peso_max , si requieres cambiar dicho límite" 

 Unidad de medida (información al lado del campo de digitación de cantidades) 
 Al lado del campo de digitación de cantidades debe mostrarse la unidad de medida o unidad en la que se dona ( eatc_odds.eatc_dona_unit ).   
 Nota importante: esta implementación informativa no está en los maestros del Éxito, por lo tanto si no se encuentra dicho valor en el maestro respectivo (eatc_odds) el valor por defecto de dicha unidad debe ser " unidades " 

 [Dropdown] Selector de causal de la baja del producto: 
 Para cada registro se debe entregar una causal de la baja (este debe ser el label del dropdown) o retiro del producto del inventario.  Para hacerlo se debe realizar la siguiente consulta (teniendo en cuenta la respectiva Cuenta [CUA]:  
 https://devdonantes.eatcloud.info/api/[CUA]/eatc_dona_return_causes?_id=_ * 

 Ejemplo : 
 Para consultar las causales de devolución / donación de la cuenta " exito " (en ambiente de pruebas) se debe realizar la siguiente consulta 
 https://devdonantes.eatcloud.info/api/exito/eatc_dona_return_causes?_id=_*   

 En el selector se debe mostrar lo correspondiente al parámetro: eatc-return_cause.  En el objeto se deberán almacenar eatc-return_cause y eatc-return_cause_code. 

 [Dropdown (si / no)] Selector "¿Contiene alérgenos?: 
 Para cada registro se debe determinar si la donación contiene alérgenos. Para ello la App dispondrá de un selector, cuyo valor por defecto es "no".  La información se lleva al eatc-dona en el parámetro: "eatc-contains_alergens". 

 [Date picker] Fecha más próxima de vencimiento: ***NUEVO: validación condicionada de obligatoriedad para el campo eatc-closer_expiration_date, adicionando configuración por punto de donación *** 

 Obligatoriedad ***NUEVO: obligatoriedad según parámetro de configuración *** 
 El sistema realiza la siguiente consulta ealiza la siguiente consulta, para el punto de donación cuyo usuario está realizando el anuncio de donación (el POD en el cual el respectivo usuario está loggeado).  NOTA IMPORTANTE: este dato puede variar del dato que se incorpora en la donación como punto de donación, debido a la funcionalidad de No Negociados, y es por eso que se estableció la funcionalidad para registrar el identificador del punto que crea la donación o eatc_dona_headers. eatc_dona_creator_pod . Es a este punto creador de la donación al que se le debe consultar el parámetro de configuración que ensegida se establece y por eso se deja así la notación.  También se deberá tomar el _DOM. cua_user como el donante de la donación (eatc-donor), NO como la cua_origen . 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_pods?eatc-id={{eatc_dona_headers. eatc_dona_creator_pod }}&_cmp= eatc_mandatory_closer_exp_date 

 Respuesta diferente de "y", igual a "n", vacía, nula o el campo no existe. 
 Si el llamado al API responde que el campo no existe, o que la respuesta es diferente a "y", es igual a "n", es nula o es vacía, entonces se procederá a realizar la siguiente validación: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{ _DOM. cua_user }}&_cmp= eatc_mandatory_closer_exp_date 
 Respuesta diferente de "y", igual a "n", vacía, nula o el campo no existe. 
 Si la segunda consulta al API define que el campo no existe, o que la respuesta es diferente a "y", es igual a "n", es nula o es vacía, entonces el sistema ha determinado que este campo no es obligatorio, por lo tanto no se exigirá su llenado para completar la donación (campo de captura opcional). 
 Respuesta igual a "y" 
 El sistema determinó que el campo es obligatorio, razón por la cual no dejará crear la donación hasta que se llene esta información. 
 Respuesta igual a "y" 

 El sistema determinó que el campo es obligatorio, razón por la cual no dejará crear la donación hasta que se llene esta información. 

 Validación : obligatoriedad, según parámetro de configuración. 
 El sistema permitirá seleccionar la fecha más próxima de vencimiento.  Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parámetro ( eatc_dona. eatc-closer_expiration_date ) será: 0000-00-00 (siempre y cuando la captura no sea obligatoria) . Si el usuario desea registrar una fecha, deberá ingresar a un " date picker " o " selector de fechas " que presenta por defecto, como sugerencia de "fecha más próxima de vencimiento" la sumatoria de la fecha actual más el número que se encuentra en el parámetro  eatc_cua. days_before_expiration  
 {{URL_datagov]]/api/eatcloud/eatc_cua?name= {{cua_user}} 

 Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vacío o nulo, el valor por defecto que debe tomarse es "5", para realizar la sumatoria y asi sugerir la fecha .   

 ***NUEVO: el datepicker permitirá escoger como fecha de vencimiento la fecha actual: 
 El usuario podrá modificar esa fecha sugerida, y el sistema no le permitirá ingresar fechas anteriores al día actual (solo se podrán ingresar la fecha actual o posteriores) ***   (ANTERIORMENTE:  El usuario podrá modificar esa fecha sugerida, y el sistema no le permitirá ingresar fechas anteriores al día actual más 1 día. (solo se podrán ingresar fechas posteriores)) . El dato resultante (tipo fecha con formato AAAA-MM-DD) se deberá guardar en el parámetro eatc_dona. eatc-closer_expiration_date 

 Ejemplo : 
 El día 2020-02-27 se realiza un anuncio de donación para la cuenta Makro (en ambiente de pruebas).  Como en esta cuenta el parámetro eatc_cua. days_before_expiration es igual a 5 ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro)) 
 , el usuario al ingresar al selector de fechas, el mismo le debe sugerir la fecha "2020-02-27 + 5 días" es decir "2020-03-03".  Si el usuario no varía esta selección (puede hacerlo siempre y cuando la fecha del selector de fechas no sea anterior a 2020-02-28 (2020-02-27 + 1 día)), el sistema debe registrar en el eatc_dona. eatc-closer_expiration_date el dato 2020-03-03 

 Detalle: Inputs paramétricos: 
 Los siguientes inputs no estarán presentes por defecto en todas las APPs, y para desplegarse (mostrarse en el formulario de captura) la App deberá consultar parámetros registrados en DATAGOV para la cuenta en cuestión [CUA]  ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ) 

 [Input: float] Digitación de KG: 
 Si el parámetro odds_weight   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua ] ) )  tiene como valor: " eatc_dona " el sistema debe desplegar un campo de captura de KG (float) (peso unitario en KG: es el label del input) y guardarlo en:  eatc-odd_unit_weight_kg 
 Ejemplo:  
 Teniendo en cuenta que para la cuenta " exito " el parámetro odds_weight tiene como valor eatc_dona ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) ).  Entonces el sistema debe deplegar un input de datos que permita el ingreso de números flotantes (con dos cifras decimales) para que el usuario digite los KG (peso unitario en KG: es el label del input) que se donan. 

 [Input: float] Digitación del costo unitario de la mercancía donada: 
 Si el parámetro costs   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_dona " el sistema debe desplegar un campo de captura para el costo unitario (este es el label del input) del producto donado (float) y guardarlo en: eatc-unit_cost  
 Ejemplo:  
 Se supone que para la cuenta exito el parámetro costs tiene como valor eatc_dona ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) ).  Entonces el sistema debe desplegar un input de datos que permita el ingreso de números flotantes (con dos cifras decimales) para que el usuario digite el costo unitario de lo que se dona que se donan. 

 [Input: float] Digitación del porcentaje del impuesto al valor agregado (IVA) aplicable: 
 Si el parámetro taxes   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_dona " el sistema debe desplegar un campo de captura para el porcentaje de IVA aplicable (este es el label del input) del producto donado (float solo con dos cifras enteras), y guardarlo en:  [CORREGIR] eatc-VAT_percentage.  Este campo debe presentar como valor por defecto "19" (que corresponde al 19% de IVA que se le aplica a la mayoría de los productos susceptibles de donación. 
 Ejemplo:  
 Se supone que para la cuenta exito el parámetro taxes tiene como valor eatc_dona ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) ).  Entonces el sistema debe desplegar un input de datos que permita el ingreso de números flotantes (con dos cifras decimales) para que el usuario digite el el porcentaje del IVA. El sistema sugiere la cifra "19" en el respectivo campo de captura. El usuario podrá modificarla o dejarla tal como se sugiere. 

 Agregar productos: 
 El botón de agregar productos guarda la información del mismo (para su registro ) y la muestra en el listado de " Contenido del anuncio" . 

 Contenido del anuncio: 
 Listado de los productos que han sido agregados al anuncio, en donde se muestra el nombre del producto (eatc_odds. eatc-name ) , la cantidad digitada ( eatc-quantity ) la causal de baja del producto ( eatc-return_cause ) y el peso total en KG ( eatc-odd_total_weight_kg ). Este listado deberá ser accionable, de tal manera que al hacer click en una de sus líneas el producto en cuestión pueda ser editado  o borrado. 

 Editar productos: 
 Haciendo clic en la línea del listado de productos ( Contenido del anuncio ), el usuario podrá editar cantidades , causales de baja del producto . y demás inputs paramétricos (según sea el caso) o eliminar la línea de producto. 
 {{URL_entorno_donante}}/crd/ {{ _DOM.cua_master}} /?_tabla= eatc_dona &_operacion=update&{{parametros_editados}}&WHERE _id={{_id_producto_a_editar}} 

 Borrar productos: 
 Haciendo clic en el botón de borrar de un producto en particular de la lista de productos agregados, el sistema debe realizar el siguiente llamado al CRD para borarro de eatc_dona . 
 {{URL_entorno_donante}}/crd/ {{ _DOM.cua_master}} /?_tabla= eatc_dona &_operacion=delete&WHERE _id={{_id producto_a_borrar}} 

 Registro del anuncio de donación: 
 Con la información de encabezado ( generada por el sistema , tomada de la información de la cuenta ,  tomada del maestro de puntos de donación y digitada ) y cuyo carácter será repetitivo a lo largo de los registros de un mismo anuncio; y  con la información de detalle que se toma del maestro de productos susceptibles a ser donados ,  las cantidades digitadas , los cálculos a partir de las cantidades, los selectores de causales de baja y otros inputs paramétricos (según sea el caso),  se procede a realizar el registro de detalle del anuncio de donación (eatc_dona) de la siguiente manera: 

 Información de encabezado genera el sistema 
 eatc-dona_header_code = Código de la cabecera del anuncio de donación (lo genera la App para que sea único) 
 eatc-date_time = $current_datetim Fecha y hora del anuncio de donación en formato: AAAAMMDDHHMMSS 
 eatc-date_time_2 = $current_date Fecha del anuncio de donación en formato: AAAA-MM-DD 

 eatc_cua_origin = $_DOM.cua_user //Cuenta desde la cual se genera el anuncio de donación que corresponde a la cua_user de la App. 

 Información de encabezado que se toma del maestro de puntos de donación (eatc_pods) 

 eatc-pod_id = Identificador único del punto de donación ( eatc_pods.eatc-id ) 

 Información de encabezado que se toma del maestro de la información de la cuenta (eatc_cua)  
 eatc_donor_code = Proveedor Nit. eatc_cua . customer__eatc_clientes__partyidentification ( https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua] )=> la información de la CUA se toma del DOM 

 eatc_donor = eatc_cua.name 

 Nota: Si evaluando la información de la cuenta respectiva (cua_user) ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua]), se establece que la cuenta está habilitada para editar coordenadas edit_coordinates=si ), este valor será igual al parámetro eatc-name de eatc_pods ( eatc_donor =eatc_pods.eatc_name) 

 Información de encabezado que se digita 

 [INPUT] eatc-doc = Documento soporte de la transacción (se utiliza cuando se tiene un documento soporte que no puede utilizarse como código del encabezado) o a petición del cliente. 

 Información de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds): buscador de productos (o de otros maestros asociados) 
 eatc-odd_id = Identificador único del producto o artículo donado ( eatc_odds.eatc-id ). Si eatc_cua. eatc_odds_app = eatc_dona_app , el dato que se lleva a este campo es el mismo nombre del artículo, sin espacios ni caracteres especiales. 
 eatc-odd_name = Nombre o descripción del producto a susceptible de donación ( eatc_odds.eatc-odd_name ) Si eatc_cua. eatc_odds_app = eatc_dona_app , el dato que se lleva a este campo es lo que digita el usuario en el campo de texto respectivo 
 [CORREGIR] eatc-odd_code = Código internacional del artículo o producto susceptible a ser donado ( eatc_odds.eatc-odd_code ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío (eatc-code = "") . 

 [CORREGIR] eatc-odd_code_type = Tipo del código internacional del artículo o producto susceptible a ser donado (ejemplo: EAN8, EAN13, UPC...: ( eatc_odds.eatc-odd_code_type )). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 

 ***NUEVO: origin_odds_typology_a = si el producto se digita por parte del usuario, el sistema le deberá solicitar una clasificación o tipología del mismo que es propia del la organización del usuario. *** 

 Si el producto es un producto existente en el maestro de productos y  ya está clasificado, entonces el sistema procederá a realizar esto 
 ***NUEVO : llevar las tipologías origen desde el maestro de productos *** 
 Según los lineamientos de clasificación de productos , esta información debe tomarse del maestro respectivo (anteriormente estaban mapeadas de manera incorrecta. revisar la nueva información resaltada en azul 
 origin_odds_typology_a = Primera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. origin_odds_typology_a ). 
 origin_odds_typology_b = Segunda tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. origin_odds_typology_b ).  

 origin_odds_typology_c = Tercera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. origin_odds_typology_c ).  

 Deprecado 
 origin_odds_typology_b = Primera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds.eatc-odd_typology_a ) 
 origin_odds_typology_b = Segunda tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds.eatc-odd_typology_b ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 
 origin_odds_typology_c = Tercera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds.eatc-odd_typology_c ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 

 ***NUEVO : llevar la tipología a y b desde el maestro de productos *** 
 Según los lineamientos de clasificación de productos , esta información debe tomarse del maestro respectivo 
 eatc-odd_typology_a = Primera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. eatc-odd_typology_a ): food, other 
 eatc-odd_typology_b = Segunda tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. eatc-odd_typology_b ). 
 eatc-odd_typology_c = Tercera tipología consignada en el origen del producto susceptible a ser donado ( eatc_odds. eatc-odd_typology_b ). 

Para realizar la clasificación de eatc_dona a partir de la información consignada en eatc_odds, se deberán invocar los servicios cuya documentación está aquí . 

 ***NUEVO :  Si el producto es un producto es nuevo (no existe en el maestro) o no está clasificado, entonces el sistema procederá a realizar esto *** 
 Inclusión del producto en el maestro modernizado (odds) 
Como primera medida se deben llevar los datos del producto al maestro de productos modernizado.  Una vez se complete este registro de manera exitosa, se procede a realizar la invocación del clasificador unificado (en la anterior especificación había 4 llamados endpoints diferentes, que se convirtieron en uno, pero su condición de operación es que el producto esté registrado en el maestro. 

El nombre del producto no debe contener comas, dobles espacios al medio, debe estar “Trimiado” (sin espacios al inicio y al final) para ser registrado en el maestro y que el clasificador funcione adecuadamente. 

Invocación del clasificador: 
El sistema realizará el siguiente llamado para invocar el clasificador 
 Método: POST 
 Endpoint: http://20.83.146.184/api/v1/webhooks/h3XsPnbataR114sxkvGDF   (si este no funciona, se puede utilizar este como redundancia: http://20.83.146.184/api/v1/webhooks/p8lkMtp8lc7E7Jq20CToo ) 
 Json body: 
{
 "data": {
   "rows": [
     {
       "ambiente": "prd",    ***prd o dev, según sea el ambiente*** 
       "odd_name": " {{odd_name}} ", ***obligatorio*** 
       "cua_master": " {{cua_master}} ", ***obligatorio*** 
       "odd_category": " {{odd_origin_typology_a}} " ***opcional*** 
     }
   ]
 }
} 

 DEPRECADO 
 Invocación del primer clasificador 
 El sistema procederá a realizar el siguiente llamado, con la información del “nombre del producto” ( {{ eatc-odd_name }} ) digitado por el usuario y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class1/categorize?cua_master= {{_DOM. cua_master }} &odd_name= {{ eatc-odd_name }} 
 Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 }   
 Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
 En caso de no obtener respuesta deberá invocar el segundo clasificador. 

 Invocación del segundo clasificador 
 Si no obtuvo una clasificación con el primer clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class2/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
 Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 } 
 Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
 En caso de no obtener respuesta deberá invocar el tercer clasificador. 

 Invocación del tercer clasificador 
 Si no obtuvo una clasificación con el segundo clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class3/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
 Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 } 
 Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
 En caso de no obtener respuesta deberá invocar el cuarto clasificador. 

 Invocación del cuarto clasificador 
 Si no obtuvo una clasificación con el tercer clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class4/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
 Si se llega a este punto se deberá utilizar la información generada por el clasificador 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}", 
   "probabilidad": {{ porcentaje_probabilidad }}, 
   "modelo_usado": {{ modelo }} 

 } 

 Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
 Para porcentajes de probabilidad por debajo de 90%, se deberá generar una alerta, a un grupo de Telegram o Teams, en donde se informe, fuera de la respuesta que arroja el clasificador (y que se expuso más arriba), los datos de la cuenta maestra, cuenta usuario, nombre, código y tipología a del articulo.. 

 [CORREGIR] [ESTOS TRES NO SE ENVÍAN EN EL JSON] 

 eatc-height_cm = Altura unitaria en centímetros del artículo o producto susceptible a ser donado ( eatc_odds.eatc-height_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 
 eatc-width_cm = Ancho unitario en centímetros del artículo o producto susceptible a ser donado (eatc_odds.eatc-width_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 

 eatc-length_cm = Longitud unitaria en centímetros del artículo o producto susceptible a ser donado (eatc_odds.eatc-length_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vacío. 

 [LOS ANTERIORES TRES NO SE ENVÍAN EN EL JSON] 

 Información de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos y parámetros del sistema 

 Peso unitario en kilogramos del artículo o producto donado: eatc-odd_unit_weight_kg.  

 Para tomar este dato tenemos las siguientes opciones: 
 El dato se encuentra en el maestro de productos ( eact_odds. eatc-odd_unit_weight_kg ): esta circunstancia se da si el parámetro odds_weight de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ,  tiene como valor: " eatc_odds " 
 El dato se encuentra en un maestro de conversión a kg (se envía el eatc-odd_id al mismo parámetro de del maestro eatc_odds_weight para traer eatc-odd_unit_weight_kg) :  esta circunstancia se da si el parámetro odds_weight   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_odds_weight " 
 Ejemplo:  
 Se supone que para la cuenta "exito" el parámetro odds_weight tiene como valor eatc_odds_weight ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) cosa que no es cierta (el valor de ese parámetro es eatc_dona ), así que se debe suponer inyectándola en el código).  Entonces el sistema debe realizar la siguiente búsqueda, tomando el eatc-odd_id que se tomó en el selector (suponiendo que eatc-odd_id sea 243448 ): https://devdonantes.eatcloud.info/api/exito/eatc_odds_weight?eatc-odd_id=243448 para tomar lo que retorna el parámetro eatc-odd_unit_weight_kg que en este ejemplo es "2" 

 El dato se toma en la donación: se toma del input respectivo realizado en la APP :  esta circunstancia se da si el parámetro odds_weight   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_dona " 

 Costo unitario del artículo o producto donado: eatc-unit_cost. 
 Para tomar este dato tenemos las siguientes opciones: 
 El dato se encuentra en el maestro de productos ( eatc_odds. eatc-unit_cost ): esta circunstancia se da si el parámetro costs de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_odds " 
 Ejemplo:  
 Para la cuenta makro el parámetro costs tiene como valor eatc_odds ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) ).  Entonces el sistema debe realizar la siguiente búsqueda, tomando el eatc-odd_id que se tomó en el selector (suponiendo que eatc-odd_id sea 2704 ): https://devdonantes.eatcloud.info/api/makro/eatc_odds? eatc-id = 2704     para tomar lo que retorna el parámetro eatc-unit_cost que en este ejemplo es " 2829 " 
 El dato se encuentra en un maestro de costos (se envía el eatc-odd_id al mismo parámetro de del maestro eatc_odds_cost  para traer eatc-odd_unit_cost) :  esta circunstancia se da si el parámetro costs   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_odds_costs " 
 Ejemplo:  
 Se supone que para la cuenta exito el parámetro costs tiene como valor eatc_odds_costs ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) cosa que no es cierta (el valor de ese parámetro es eatc_dona ), así que se debe suponer inyectándola en el código).  Entonces el sistema debe realizar la siguiente búsqueda, tomando el eatc-odd_id que se tomó en el selector (suponiendo que eatc-odd_id sea 243448 ): https://devdonantes.eatcloud.info/api/exito/eatc_odds_costs?eatc-odd_id=243448   para tomar lo que retorna el parámetro eatc-odd_unit_cost que en este ejemplo es "10000" 

 El dato se toma en la donación: se toma del input respectivo realizado en la APP :  esta circunstancia se da si el parámetro costs   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_dona " 

 Porcentaje del impuesto al valor agregado aplicable al artículo: eatc-VAT_percentage.   
 Para tomar este dato tenemos las siguientes opciones: 
 El dato se encuentra en el maestro de productos ( eatc_odds. eatc-vat_percentage ): esta circunstancia se da si el parámetro taxes de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_odds " 
 El dato se encuentra en un maestro de costos (se envía el eatc-odd_id al mismo parámetro de del maestro eatc_odds_cost  para traer eatc-odd_unit_cost) :  esta circunstancia se da si el parámetro taxes   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_odds_costs " 
 Ejemplo:  
 Se supone que para la cuenta exito el parámetro taxes tiene como valor eatc_odds_costs ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) cosa que no es cierta (el valor de ese parámetro es eatc_dona ), así que se debe suponer inyectándola en el código).  Entonces el sistema debe realizar la siguiente búsqueda, tomando el eatc-odd_id que se tomó en el selector (suponiendo que eatc-odd_id sea 243448 ): https://devdonantes.eatcloud.info/api/exito/eatc_odds_costs?eatc-odd_id=243448   para tomar lo que retorna el parámetro eatc-vat_percentage que en este ejemplo es "19" 

 El dato se encuentra en un maestro de impuestos  (se envía el eatc-odd_id al mismo parámetro de del maestro eatc_odds_taxes  para traer eatc-vat_percentage) :  esta circunstancia se da si el parámetro taxes   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) , tiene como valor: " eatc_odds_taxess " 
 Ejemplo:  
 Se supone que para la cuenta exito el parámetro taxes tiene como valor eatc_odds_taxes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) cosa que no es cierta (el valor de ese parámetro es eatc_dona ), así que se debe suponer inyectándola en el código).  Entonces el sistema debe realizar la siguiente búsqueda, tomando el eatc-odd_id que se tomó en el selector (suponiendo que eatc-odd_id sea 243448 ): https://devdonantes.eatcloud.info/api/exito/eatc_odds_taxes?eatc-odd_id=243448   para tomar lo que retorna el parámetro eatc-vat_percentage que en este ejemplo es "19" 
 El dato se toma en la donación: se toma del input respectivo realizado en la APP :  esta circunstancia se da si el parámetro taxes   de la cuenta respectiva ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ) ), tiene como valor: " eatc_dona " 

 Información que se toma a partir de inputs y selectores de la APP 
 [INPUT] eatc-odd_quantity = Cantidad del producto o artículo donado (cantidad digitada por el usuario para generar el anuncio) 
 [INPUT] eatc-odd_original_quantity = Cantidad del producto o artículo donado: Se toma del input anterior 
 [DROPDOWN] eatc-return_cause = Causa de Devolucion Causa Devolucion DESC // Descripción del causal de devolución 
 eatc-return_cause_code = Causa de Devolucion Causa Devolucion ID //Código del causal de devolución se toma a partir del anterior dropdown 
 [DROPDOWN] eatc-contains_alergens = definición si la donación contiene alérgenos. 

 [DATE DATEPICKER] eatc-closer_expiration_date = fecha más próxima de expiración del producto (o los productos) anunciado(s). 

 Información que se toma a partir de cálculos a partir de los inputs y selectores de la APP 
 eatc-odd_total_weight_kg = Peso total en kilogramos del artículo o producto donado, es decir, peso unitario por cantidad donada (eatc_odds_kg.valor_kg*eatc-odd_quantity) 
 eatc-total_cost = Costo total del o de los productos o artículos donados ( eatc-quantity * eatc-unit_cost ) 
 eatc-original_VAT = Valor original total del impuesto a las ventas (eatc-odd_original_quantity*eatc-odd_unit_cost*eatc-VAT_percentage) 

 eatc-total_VAT = Valor definitivo total del impuesto a las ventas  (eatc-odd_quantity*eatc-odd_unit_cost*eatc-VAT_percentage), después del proceso de verificación.  Como aun no se ha efectuado la verificación es similar a eatc-original_VAT 

 Datos que se pasan con cero (se deben enviar así porque la tabla tiene que recibir números) 
 eatc-odd_total_height_cm = 0 // No aplica por no tener datos 
 eatc-odd_total_width_cm = 0 // No aplica por no tener datos 
 eatc-odd_total_length_cm = 0 // No aplica por no tener datos 

 eatc-odd_total_volume_cm3 = 0 // No aplica por no tener datos 

Datos que se pasan vacíos por el momento pero que podrán ser objeto de un proceso de clasificación (según lineamientos ) 
 eatc -odd_ typology_a = Primera tipología (alimento / no alimento) 
 eatc- odd_ typology_b = Segunda tipología (Clasificaciones BAMX / ABACO) 

 ***NUEVO Campo: eatc- odd_ typology_b_code= Código de la segunda tipología (Clasificaciones BAMX / ABACO) 
 eatc- odd_ typology_c = Tercera tipología EatCloud (equivalente) del artículo o producto donado: clasificaciones para composición nutricional. 

 ***NUEVO Campo: eatc- odd_ typology_c_code= Código de la tercera tipología 

Datos que se pasan vacíos 
 eatc-odd_state = //Estado producto: certificable, rechazado. Lo incorpora la App en el proceso de chequeo o verificación del anuncio de donación 

 eatc-odd_rejection_cause = //Causal del rechazo de un producto donado.  Lo incorpora la App en el proceso de chequeo o verificación del anuncio de donación 

 [NUEVO: observaciones para la recogida]:  

 eatc-warning = OBSERVACIONES PARA LA RECOGIDA //A tener en cuenta: también se coloca información según lo planteado aquí 

 PENDIENTE DE DEFINICIONES (Por el momento dejarlos vacíos):  

 eatc-odd_external_code = Código del artículo entregado por el proveedor del mismo: se utiliza cuando un donante informa mercancía que pertenece a un tercero identificado en el sistema (que debería ser una nueva cuenta  (CUA) en el sistema) 

 BOTÓN "AGREGAR PRODUCTO" ***REVISAR DINAMIZACIÓN A PARTIR DE CUENTA MAESTRA*** 
 Al presionar este botón la app se debe asegurar que todos los registros de detalle (eatc_dona) hallan sido realizados mediante el API respectiva   
 Método POST: 
 {{URL_entorno_donante}}/crd/ {{ _DOM.cua_master}} /?_tabla= eatc_dona &_operacion=insert 

 DEPRECADO: Si la cuenta permite editar las coordenadas ( edit_coordinates ) y las mismas se editaron 
 Se realiza el anterior registro  y cuando se registra el primer producto se realizan las siguientes operaciones: 

 Edición registro en eatc_pods: 
 Método POST 
 https://devdonantes.eatcloud.info/crd/ {{ _DOM.cua_user}} /?_tabla=eatc_pods_coordinates&_operacion=update& {{ Parametros edición en eatc_pods }} &WHEREeatc-id={{ eatc_pods. eatc-id }} 

 Se debe validar que la edición halla sido realizada correctamente porque será muy importante a la hora de generar los anuncios de donación (anunciar donación). 

 Creación del registro en eatc_pods_coordinates: 
 Método POST 
 https://devdonantes.eatcloud.info/crd/ {{ _DOM.cua_user}} /?_tabla=eatc_pods_coordinates&_operacion=insert& {{ Parametros edición en eatc_pods }} 

 BOTÓN "ANUNCIA DONACIÓN" ***REVISAR DINAMISMO A PARTIR DE _DOM.CUA_USER 
 Se debe llamar al proceso en el servidor que genera los encabezados del anuncio de donación , para que corra, y una vez corra, debe llamar al proceso que genera la clasificación para el match para el presente anuncio de donación. 
 Se debe verificar que los procesos que se llaman, reciben como parámetro _DOM.cua_user para la creación de los mismos y su match en múltiples cuentas maestras. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 114.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 3b2503cb-9e0b-45eb-9cea-f9362fbd7fd1 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 ac3d19ec-fa5f-4fc3-870e-02876212f48a 
 2025-11-07T05:07:10.5391868Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"7d04b269-483b-49f9-a4f8-810c64a1b818","SequenceId":2505,"FluidContainerCustomId":"6853c836-d4a7-4ac4-9cac-be9b1b4950d4","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 CREACIÓN DE ANUNCIO DE DONACIÓN (EATC_DONA_UPL)