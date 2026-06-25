# extcanceldona--SERVICIO-PARA-EXTENDER-LA-VIDA-ÚLTIL-DE-LAS-DONACIONES.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO (se basa en libdona) 
 El presente servicio se especifica para entregar una herramienta segura, que le permita a los puntos de donación (validando correctamente sus credenciales de manera), y si las condiciones de la donación así lo permiten, extender la vida útil de una donación, es decir, prolongar la fecha y hora de cancelación de la misma.&#160; Se determina este servicio, dado que se solicitó una funcionalidad de generación de un mensaje de correo electrónico que alerte ante las donaciones que están a punto de cancelarse, y a partir de dicha alerta, permitirle al usuario alargar la vida útil de dichas donaciones. &#160;Por lo tanto se documentará una funcionalidad en la WAPP modernizada que permita invocar este servicio para realizar dicho alargue de la vida, siempre y cuando se cumplan algunas condiciones definidas en la solicitud (como por ejemplo que la donación esté a unas cuantas horas de cancelarse). Se debe implementar como un servicio público, cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento.&#160;&#160; 
&#160; 
 Documentación de API pública para alargar la vida útil de una donación 
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
&#160; 
 incomplete_data 

 2. VALIDACIÓN DEL ESTADO DEL PUNTO 
 Con el dato que llega en los parámetros&#58; 
&#160; 
 eatc_cua 
 eatc_pod_id 
&#160; 
 El sistema deberá realizar la siguiente validación del punto de donación, antes de desplegarle la funcionalidad de captura de anuncios de donación (en entorno modernizado, con los respectivos datos de autenticación)&#58; 
&#160; 
 &#123;&#123;DOMINIO_modernizado&#125;&#125;/api/pods?code_cua_user=&#123;&#123; eatc_cua &#125;&#125;&amp;code_pod=&#123;&#123; eatc_pod_id &#125;&#125;&amp;_scmp=code&amp;status=1 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación&#58; 

 3. VALIDACIÓN DE LOS DATOS DE LA DONACIÓN QUE SE LE ALARGARÁ LA VIDA ÚTIL 
&#160; 
 Con los datos que llegan en los parámetros&#58; 
&#160; 
 cua_master 
 eatc_cua 
 eatc_dona_header_code 
 eatc_pod_id 
&#160; 
 El sistema deberá consultar si la donación en cuestión corresponde a los datos entregados y si está en estado anunciado ( eatc_dona_state= announced) 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-pod_id 
 =&#123;&#123; eatc_pod_id &#125;&#125;&amp;eatc_cua_origin=&#123;&#123; eatc_cua &#125;&#125;&amp;eatc-state= announced &amp;_cmp= eatc-cancelation_datetime 
&#160; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail&#58; dona_already_picked 
&#160; 
 Si la consulta arroja una respuesta válida, el sistema guarda en una variable 
 &#123;&#123;eatc_dona_headers. eatc-cancelation_datetime &#125;&#125;=&#123;&#123; eatc_old_cancelation_datetime &#125;&#125; 
&#160; 
 y sigue con la siguiente validación ( validación de fechas ). 

&#160; 

 4. VALIDACIÓN DE FECHAS PARA DETERMINAR SI A UNA DONACIÓN SE PUEDE ALARGAR LA VIDA ÚTIL 
&#160; 
 Nota importante para este desarrollo &#58; se deberá tener en cuenta que estas mismas validaciones se deberán implementar en la wapp modernizada, para desplegar el botón que permitirá realizar la ampliación de la vida útil de la donación (siendo estas validaciones una especie de &quot;error handler&quot;), en ese sentido se debe trabajar de manera que se pueda reciclar al máximo el código (o la lógica) aquí empleado 
Para poder alargarle la vida útil a una donación la fecha y hora actual debe estar en el rango de tiempo comprendido entre&#58; dos horas antes de la fecha y hora de cancelación y la fecha de cancelación 
Según el requerimiento planteado solamente se deberán alargarle la vida útil a las donaciones cuya fecha de cancelación está a máximo dos horas en el futuro, por lo tanto el sistema deberá tomar la fecha y hora en la cual se realizó la solicitud para alargar la vida útil de la donación y realizar la siguiente validación 
 (&#123;&#123; eatc_old_cancelation_datetime &#125;&#125; - 2 horas ) =&lt; &#123;&#123;fecha_hora_actual&#125;&#125; =&lt; &#123;&#123; eatc_old_cancelation_datetime &#125;&#125;&#160; 
 Si la validación falla, el servicio deberá contestar&#58; 
 fail_extcanceldona_out_of_time_range 
&#160; 
 ó (Como mejor sea, de cara a la arquitectura del servicio y su interacción con la webapp) 
&#160; 
 fail&#58; extcanceldona_out_of_time_range 

 5. Actualización de información en eatc_dona_headers 
 Con los datos que llegan en los parámetros&#58; 
&#160; 
 cua_master 
 eatc_dona_header_code 
 ext_cancel_dona_in_hours &#160; 
&#160; 
 Aunque es posible que por las restricciones que se le han impuesto al CRD para actuar sobre ciertas donaciones, el servicio no funcione en este caso, se documenta basándose en su funcionamiento. &#160;En términos generales, el servicio deberá reescribir la fecha y hora de cancelación, sumándole las horas que llegan en el parámetro de invocación del servicio “ ext_cancel_dona_in_hours ” 
&#160; 
 &#123;&#123; parámetros_update_CRD &#125;&#125; 
&#160; 
 eatc-cancellation_datetime = &#123;&#123; eatc_old_cancelation_datetime &#125;&#125; + &#123;&#123; ext_cancel_dona_in_hours &#125;&#125; 

&#160; Inserción en eatc_dona_header_state_history con el CRD 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_headers &amp;_operacion= update &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125;&amp;WHEREeatc-code=&#123;&#123; eatc_dona_header_code&#125;&#125; 
&#160; 
&#160; 
 6. Escritura en el historial de estados de la donación 
 Con los datos que llegan en los parámetros&#58; 
 Con los datos que llegan en los parámetros&#58; 
&#160; 
 cua_master 
 eatc_cua 
 eatc_dona_header_code 
 eatc_pod_id 
 eatc_pod_resp 
 eatc_pod_email 
 ext_cancel_dona_in_hours &#160; 
&#160; 
&#160; 
 &#123;&#123; parámetros_insert_CRD &#125;&#125;&#125; 
&#160; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; =&gt; Código del encabezado del anuncio de donación a programar, enviado como parámetro de invocación del servicio 
 eatc-state = announced &#160; =&gt; Constante 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; =&gt; Fecha y hora en la cual se alarga la vida de la donación (es decir la fecha y la hora en que corre el presente proceso) 
 eatc-log = por solicitud del POD&#58; &#123;&#123; eatc_pod_id &#125;&#125; (responsable&#58; &#123;&#123; eatc_pod_resp&#125;&#125;. email&#58; &#123;&#123;eatc_pod_email&#125;&#125;, se alargó la vida útil de la daonación en &#123;&#123; ext_cancel_dona_in_hours &#125;&#125; horas, quedando como nueva fecha y hora de cancelación &#123;&#123;nueva_fecha_hora_cancelación&#125;&#125; 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 7. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si las actualizaciones de información realizadas por el servicio se realizan de manera adecuada, entonces entregará la respuesta&#58; 
 success 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 8ecf6704-07aa-4d69-95ff-41ca58e74a8d 
 3!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 e227a263-18fc-441c-935b-788ba1d96809 
 2025-09-03T05:17:09.3542817Z 

 {"SessionId":"67befbcc-56ea-4e06-b36f-8a9ebe098337","SequenceId":3920,"FluidContainerCustomId":"ec238554-3480-42fe-bfed-2569bb27c2a3","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 extcanceldona: SERVICIO PARA EXTENDER LA VIDA ÚLTIL DE LAS DONACIONES