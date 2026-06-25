# servicio-para-la-evaluación-peso-excesivo-exw.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 JUSTIFICACIN DE LA NO DOCUMENTACIN COMO SERVICIO PBLICO 
&#160; 
 Este servicio no ser invocado por ninguna plataforma, sino por el proceso de creacin de encabezados, por este motivo no se considera necesario (en primera instancia) documentar el servicio como uno pblico.&#160; De todas maneras se recomienda incorporarle mecanismos de seguridad para que la invocacin sea segura. 

 ENDPOINT PROPUESTO&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/exw 
&#160; 
 Se puede variar a eleccin del desarrollador si esto facilita la implementacin. 
&#160; 
 Se propone incorporarle seguridad para su invocacin (mediante envo de parmetros de autenticacin en el encabezado). 

&#160; 
 PARMETROS QUE RECIBE EL SERVICIO&#58; 
 eatc_dona_code&#58; 
 Cdigo del anuncio de donacin, que corresponde al parmetro&#58; eatc_dona_heaaders. eatc-code =&gt; parmetro de carcter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) =&gt; parmetro de carcter obligatorio 
&#160; 
 eatc_telgram_msg&#58; 
 &quot;y&quot; o &quot;n&quot; =&gt; Opcional 

 CONSULTAS QUE REALIZA EL SERVICIO PARA SU OPERACIN&#58; 
 Consulta de los datos bsicos de la donacin&#58; 
 Con los datos recibidos el servicio realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_code &#125;&#125;&amp;_cmp=eatc-pod_id,eatc_cua_origin,eatc-original_weight_kg 
&#160; 
 Ejemplo ambiente de pruebas&#58; eatc_cua_master= abaco , eatc_dona_code= 00002003310565 &#58; 
 https&#58;// devdonantes .eatcloud.info/api/ abaco /eatc_dona_headers?eatc-code= 00002003310565 &amp;_cmp=eatc-pod_id,eatc_cua_origin,eatc-original_weight_kg &#160; 
&#160; 
 El sistema arroja la siguiente respuesta&#58; 
 res &#58; [&#123; eatc-pod_id &#58; &quot;565&quot; , eatc_cua_origin &#58; &quot;exito&quot; , eatc-original_weight_kg &#58; &quot;2&quot; &#125;], 

&#160; 
 Consulta del peso excesivo de referencia para el punto de donacin en cuestin&#58; 
 Con los datos obtenidos en la anterior consulta, el sistema consulta si existe un registro de peso excesivo de referencia para el punto de donacin en cuestin, realizando la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master=&#123;&#123; eatc_cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123; eatc_cua_origin &#125;&#125;&amp;eatc_pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;_cmp= eatc_excessive_weight_kg 
&#160; 
 Continuando con el ejemplo ambiente de pruebas &#58; eatc_cua_master= abaco , eatc_cua_origin= exito , eatc-pod_id= 565 &#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master=abaco&amp;eatc_cua=exito&amp;eatc_pod_id=565&amp;_cmp= eatc_excessive_weight_kg &#160; 
&#160; 
 Cuando la consulta no arroja resultados (como es el caso del ejemplo anterior), se deber pasar a realizar la consulta del valor por defecto para todos los puntos de la cuenta respectiva. 
&#160; 
 Si la consulta arroja resultados, con el valor obtenido en el parmetro &quot; eatc_excessive_weight_kg &quot; se pasar al proceso de validacin del peso excesivo . 

&#160; 
 Consulta del peso excesivo de referencia por defecto para los puntos de la respectiva cua_user&#58; 
&#160; 
 Cuando no se tiene un valor particular de peso para el punto de donacin en particular, se procede a consultar el valor de referencia por defecto para los puntos de esa cuenta usuario, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master=&#123;&#123; eatc_cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123; eatc_cua_origin &#125;&#125;&amp;eatc_pod_id= _default 
&#160; 
 Ejemplo ambiente de pruebas &#58; eatc_cua_master= abaco, eatc_cua_origin= exito , eatc-pod_id= _default &#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master=abaco&amp;eatc_cua=exito&amp;eatc_pod_id=_default&amp;_cmp= eatc_excessive_weight_kg &#160; 
&#160; 
 res &#58;[&#123; eatc_excessive_weight_kg &#58; &quot;500&quot; &#125;], 
&#160; 
 Cuando la consulta no arroja resultados, se deber pasar a realizar la consulta del valor por defecto para la cuenta maestra respectiva. 
 Si la consulta arroja resultados (como es el caso del ejemplo anterior), con el valor obtenido en el parmetro &quot; eatc_excessive_weight_kg &quot; se pasar al proceso de validacin del peso excesivo . 

&#160; 
 Consulta del peso excesivo de referencia por defecto para los puntos de la respectiva cua_master&#58; 
&#160; 
 Cuando no se tiene un valor particular de peso para los puntos de donacin de una cuenta usuario especfica, se procede a consultar el valor de referencia por defecto para los puntos de la cuenta maestra, realizando la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &amp;eatc_cua= _default &amp;eatc_pod_id= _default 
&#160; 
 Ejemplo ambiente de pruebas &#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master=_default&amp;eatc_cua=_default&amp;eatc_pod_id=_default&amp;_cmp= eatc_excessive_weight_kg &#160; 
&#160; 
 res &#58;[&#123; eatc_excessive_weight_kg &#58; &quot;500&quot; &#125;], 
&#160; 
 Con el valor obtenido en el parmetro &quot; eatc_excessive_weight_kg &quot; se pasar al proceso de validacin del peso excesivo . 
&#160; 
&#160; 
 VALIDACIN DEL PESO EXCESIVO 
 Con los datos obtenidos en las anteriores consultas y en el llamado al servicio el sistema deber validar si el anuncio en cuestin posee peso excesivo o no, realizando la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_code &#125;&#125;&amp;eatc-original_weight_kg=_&gt;_&#123;&#123; eatc_excessive_weight_kg &#125;&#125; 
&#160; 
 Si la anterior consulta arroja un resultado, quiere decir que el anuncio en cuestin posee peso excesivo, por lo tanto el sistema deber realizar el siguiente registro&#58; 
&#160; 
 Registro eatc_dona_headers. eatc_excessive_weight =y&#160; (campo boleano),&#160; eatc_dona_headers. eatc_excessive_weight_kg_ref=&#123;&#123; eatc_excessive_weight_kg &#125;&#125;(campo entero) 
 Nota importante&#58; creacin de campos 
 eatc_dona_headers.eatc_excessive_weight (campo boleanoy),&#160; eatc_dona_headers.eatc_excessive_weight_kg_reference (campo entero), que no existen an en eatc_dona_headers y debern crearse en todas las cuentas maestras (con las precauciones necesarias en otros proceso) y tenerse en cuenta en el proceso de creacin de maestros para la&#160; creacin de cuentas maestras. 
&#160; 
 El sistema deber realizar el siguiente registro&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123; eatc_cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_excessive_weight = y &amp;eatc_excessive_weight_kg_ref=&#123;&#123; eatc_excessive_weight_kg &#125;&#125;&amp;WHEREeatc-code=&#123;&#123; eatc_dona_code &#125;&#125; 

&#160; 
 Ejemplo ambiente de pruebas &#58; eatc_cua_master= abaco, eatc_cua_origin= exito , eatc_dona_code= exito53920200617171154100, eatc_excessive_weight_kg = 500&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=exito53920200617171154100&amp;eatc-original_weight_kg=_&gt;_500 &#160; &#160; 
&#160; 
 Como la consulta arroja resultados, entonces el sistema deber realizar el siguiente registro (una vez se hayan creado los campos correspondientes de manera correcta) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_excessive_weight = y &amp; eatc_excessive_weight_kg_ref = 500 &amp;WHEREeatc-code= exito53920200617171154100 

&#160; 
 Si la anterior consulta no arroja resultados, quiere decir que el anuncio en cuestin no posee peso excesivo, por lo tanto el sistema deber realizar el siguiente registro&#58; 
&#160; 
 Registro eatc_dona_headers. eatc_excessive_weight =n (campo boleano) 
&#160; 
 El sistema deber realizar el siguiente registro&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123; eatc_cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_excessive_weight = n &amp;WHEREeatc-code=&#123;&#123; eatc_dona_code &#125;&#125; 

&#160; 
 Ejemplo ambiente de pruebas &#58; eatc_cua_master= abaco, eatc_cua_origin= exito , eatc_dona_code= 00002003310565 , eatc_excessive_weight_kg = 500&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00002003310565&amp;eatc-original_weight_kg=_&gt;_500 &#160; 
&#160; 
 Como la consulta no arroja resultados, entonces el sistema deber realizar el siguiente registro (una vez se hayan creado los campos correspondientes de manera correcta) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc_excessive_weight = n &amp;WHEREeatc-code=00002003310565 

 ENVO DE MENSAJE A GRUPO DE TELEGRAM CON INFORMACIN DEL ANUNCIO CON PESO EXCESIVO 
&#160; 
 Si en el parmetro &quot; eatc_telgram_msg &quot; del llamado al servicio llega el valor &quot; y &quot; entonces el sistema deber realizar el siguiente llamado ( que tiene una porcin que obra como error handler ) para enviar dicha informacin (o una introduccin de la misma y el vnculo de consulta) a un grupo de Telegram que se deber crear con este fin (inicialmente agregar a Daniel, a Juan David y a Jess al grupo)&#58; 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_code &#125;&#125;&amp; eatc_excessive_weight= y &amp;_cmp=eatc-code,eatc-publication_datetime,eatc-state,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-pod_id,eatc-original_weight_kg, eatc_excessive_weight_kg_ref, eatc-state,eatc-donation_manager_name,eatc-donation_manager_phone 
&#160; 
 Ejemplo parcial del llamado (sin incluir parmetros que estn pendientes por crearse y con un llamado error handler alternativo ) 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=exito53920200617171154100&amp;eatc-original_weight_kg=_&gt;_500&amp;_cmp=eatc-code,eatc-publication_datetime,eatc-state,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-pod_id,eatc-original_weight_kg,eatc-donation_manager_name,eatc-donation_manager_phone,eatc-state 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIO PARA LA EVALUACIN PESO EXCESIVO - EXW