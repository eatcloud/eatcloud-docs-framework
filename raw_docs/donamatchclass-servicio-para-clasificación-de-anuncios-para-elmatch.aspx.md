# donamatchclass-servicio-para-clasificación-de-anuncios-para-elmatch.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general del servicio 
 El presente servicio se especifica como parte del proyecto que está encaminado a mejorar y permitir auditar el match que se genera.&#160; Como parte del análisis se determinó partir el proceso del match (que anteriormente se realizaba mediante diversos procesos que no estaban claramente estructurados y por lo tanto representaban dificultades para el análisis y la auditoría) en tres procesos independientes&#58; 
&#160; 
 &#160;Clasificación de las donaciones con respecto al match (el presente servicio) 
 Realización del registro del match de acuerdo a la clasificación dada a la donación&#160; 
 Ampliación del match 
&#160; 
 En ese orden de ideas se debe implementar como un servicio privado (inicialmente invocado directamente desde la plataforma, pero puede darse el caso que a futuro se libere como un servicio público), cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento (para tener en cuenta en la implementación, las cualidades de autenticación para acceder al servicio, podrían obviarse en una primera implementación, pero deben ser consideradas a futuro)&#160;&#160; 
&#160; 
 Documentación servicio privado para clasificación de anuncios para el match 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 

 LOG DEL SERVICIO 
 El sistema deberá guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqué de un llamado no exitoso (datos incompletos, fallo de ejecución, fallos validación entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
&#160; 
 &#160;“op”&#58;”false” 

 1. VALIDACIÓN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación del servicio privado . Si lo son, seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIÓN DEL ESTADO DEL ANUNCIO (EL MATCH SOLO DEBE GENERARSE PARA ANUNCIOS EN ESTADO “ANNOUNCED”) 
&#160; 
 Con el dato que llega en los parámetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 El sistema deberá realizar la siguiente validación del punto de donación, antes de desplegarle la funcionalidad de captura de anuncios de donación&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc-state= announced &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta ( validación de datos de la donación )&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; 00002203030033 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =00002203030033&amp; eatc-state= announced&amp;_cmp=_id &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; exito72820220324122850387 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =exito72820220324122850387&amp; eatc-state= announced&amp;_cmp=_id &#160;&#160; &#160; 
&#160; 
&#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta &quot; fail &quot;&#58; 

 3. CONSULTA DE LOS PARÁMETROS PARA EVALUACIÓN DE LA DONACIÓN&#160; 
 ***NUEVO&#58; &quot; eatc_conditions y eatc_priority &quot; para evaluar diversas reglas para generar la clasificación *** 
&#160; 
 El sistema genera la clasificación consultando los nuevos campos “ eatc_conditions ” (json que contiene todas las reglas para la clasificación) y “ eatc_priority ” (en este campo se asignan diversas prioridades, dado que a partir de la fecha una donación puede caer en varias clasificaciones, pero el sistema le asignará aquella que tenga prioridad más alta (es decir el número más bajo&#58; si un anuncio es clasificado en una regla con prioridad 2 y otra con prioridad 10, el sistema clasificará con la de prioridad 2).&#160; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Y deberá generar una alerta a un grupo de Telegram en donde se exprese hay un problema con la tabla de querys de clasificación de anuncios para el match. 
&#160; 
 Si la consulta arroja una respuesta válida, a partir de los datos obtenidos y exceptuando los parámetros _id y eatc_result, se tomarán los campos para realizar la consulta de parámetros del anuncio en cuestión para determinar su clasificación. 
&#160; 
 ***NUEVO&#58; &quot; eatc-original_weight_kg_2 &quot; para evaluar rangos de peso*** 
&#160; 
 Nuevo campo a crear&#58;&#160; dona_match_classification_querys . eatc-original_weight_kg_2 
&#160; 
 El sistema deberá consultar los parámetros que se utilizan para evaluar el anuncio.&#160; Para ello deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/dona_match_classification_querys?_campos 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Y deberá generar una alerta a un grupo de Telegram en donde se exprese hay un problema con la tabla de querys de clasificación de anuncios para el match. 
&#160; 
 Si la consulta arroja una respuesta válida, a partir de los datos obtenidos y exceptuando los parámetros _id y eatc_result, se tomarán los campos para realizar la consulta de parámetros del anuncio en cuestión para determinar su clasificación. 
&#160; 
 Ejemplo ambiente de pruebas&#58; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/dona_match_classification_querys?_campos &#160; 
&#160; 
 El sistema obtiene la siguiente respuesta, la cual contendrá datos parámetros a evaluar para clasificar la donación para el match (a excepción de _id y eatc_result&#58; 
&#160; 
 res &#58;[ 
 &#123; 
 nombre &#58; &quot;_id&quot;, 
 tipo &#58; &quot;numerico&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc_cua_master&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc_dona_typology_a&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc-donor&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc-city&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc-original_weight_kg&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc-original_weight_kg_2&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 
 &#123; 
 nombre &#58; &quot;eatc_result&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#123; 
 nombre &#58; &quot;eatc_alert_label&quot;, 
 tipo &#58; &quot;texto&quot; 
 &#125;, 

&#160; 

 4. CLASIFICACIÓN DE DONACIÓN PARA EL MATCH 
&#160; 
 ***NUEVO&#58; &quot; eatc-original_weight_kg_2 &quot; para evaluar rangos de peso *** 
 Nota para el desarrollador&#58; en esta especificación se darán lineamientos muy generales, pero que deben respetarse en aras de realizar un proceso que sea escalable y personalizable en un futuro. 
&#160; 
 A partir de los datos registrados en &quot;dona_match_classification_querys&quot; (o en estructura de datos alternativa que cumpla con la misma función), el sistema deberá clasificar la donación con respecto al match, obteniendo para cada donación una clasificación.&#160; Si para una donación no se obtiene una clasificación se debe informar del error y generar una alerta en un grupo de Telegram. 
&#160; 
 Si el sistema encuentra un registro válido en el nuevo campo&#58;&#160; dona_match_classification_querys . eatc-original_weight_kg_2, entonces evaluará que el anuncio se encuentre entre el rango de pesos que se informa en los campos dona_match_classification_querys . eatc-original_weight_kg y dona_match_classification_querys . eatc-original_weight_kg_2 
&#160; 
 Si el sistema no encuentra un registro válido en el campo dona_match_classification_querys . eatc-original_weight_kg_2 entonces funcionará tal cual funciona en la actualidad 
&#160; 
 Si la claisficación respectiva tiene un dato en &quot;dona_match_classification_querys. eatc_alert_label &quot; (estos labels deberán ser clases y estar registrados para datagov ( eatcloud )) , se debe generar un mensaje a un grupo de Telegram con el respectivo label, el código de la donación ( eatc_dona_header_code ) y un vínculo a la información de la donación y al match respectivo. 
&#160; 
 Ejemplo&#58; ambiente de pruebas&#58; donación cuya clasificación fue&#58; abaco_bogota_fruver 
 Como para la clasificación respectiva existe un label&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/dona_match_classification_querys?eatc_result=abaco_bogota_fruver&amp;_cmp=eatc_alert_label 
&#160; 
 Entonces el sistema consulta el label respectivo (registrado en la plataforma datagov eatcloud) 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov&amp;idlabel=lbl_nueva_dona_fruver &#160; 
&#160; 
 Y por lo tanto se deberá enviar a un grupo de Telegram el siguiente mensaje&#58; 
 ATENCIÓN&#58; nueva donación de fruver&#58; &#123;&#123;eatc_dona_header_code&#125;&#125; &#123;&#123;link_donacion&#125;&#125; link_registro_match_donacion&#125;&#125; 

 5. REGISTRO DE LA CLASIFICACIÓN DE LA DOANCIÓN PARA EL MATCH 
 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
&#160; 
 Con los vectores de resultados obtenidos en el proceso anterior se realiza la escritura en el match de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125; /crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_headers&amp;_operacion=uptade&amp; eatc_match_asignation_rule =&#123;&#123; eatc_result &#125;&#125;&amp;WHERE eatc_dona_header_code =&#123;&#123; eatc_dona_header_code &#125;&#125; 

 6. Llamado al servicio de registro del match 
 Una vez se termina de registrar la regla de clasificación del match match, se realiza el llamado al servicio de registro del match . 

 7. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si la clasificación fue exitosa, entonces entregará la respuesta&#58; 
&#160; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 35d075dd-2568-4366-8165-7344a7059c60 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 0520ce64-5cbc-475a-8d7a-123f23379fee 
 2025-12-24T04:33:15.7482476Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"d54ad9aa-372c-4933-b9cf-b8e1159ccc73","SequenceId":1462,"FluidContainerCustomId":"cf9156a2-b17e-4dbb-9479-c87bad560a93","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 DONAMATCHCLASS: SERVICIO PARA CLASIFICACIÓN DE ANUNCIOS PARA EL MATCH