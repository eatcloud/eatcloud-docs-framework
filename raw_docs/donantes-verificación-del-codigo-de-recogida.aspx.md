# donantes-verificación-del-codigo-de-recogida.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Antes&#58; Entrega de donación&#58; hora de llegada (eatc_doma_checkin) 

 VALIDACIÓN&#58; El anuncio posee un registro no resuelto en &quot;eatc_checkin_and_deliver_issues&quot; 
 El sistema deberá validar si existe un registro para este anuncio en la tabla de registro de &quot;issues&quot; ( eatc_checkin_and_deliver_issues ), para eso debe realizar una consulta a la API de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; resolved =no 
&#160; 
 Posible mejora en la consulta anterior (se adiciona&#58; 
 eatc-issue_cause_code = extemporaneous_code_verification 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-issue_cause_code = extemporaneous_code_verification &amp; resolved =no 

 E L ANUNCIO TIENE UN REGISTRO DE ISSUE NO RESUELTO&#58; 
 [Primera etapa] Verificación remota simple 
 Si el registro del issue ( eatc_checkin_and_deliver_issues ) trae un dato en el campo eatc-verification_code , entonces se debe presentar un botón que diga&#58; &quot; copiar el código enviado por el beneficiario &quot;. Al presionar esta opción se toma el valor recuperado de ese campo y se coloca el en campo de verificación del código para pasar a la funcionalidad de &quot;verificación del código de recogida de la donación&quot; 

 Verificación del código de recogida de donación&#160; 
 El sistema dispone un formulario para ingresar el Código de recogida del beneficiario que toma la donación.&#160; Este código corresponde al parámetro &quot; eatc-verification_code &quot;, del respectivo encabezado de donación ( eatc_dona_headers ). 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-code= &#123;&#123; eatc-code&#125;&#125; 

&#160; 
 Ejemplo validación remota&#58; 
 El para el anuncio del éxito de San Antonio (eatc_pod_id= 39 ) cuyo &quot; eatc-code = exito3920200714174214720 
&#160; 
 Ambiente pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= exito3920200714174214720 
&#160; 
 El sistema consulta si tiene un registro de &quot;issue&quot; no resuelto en eatc_checkin_and_deliver_issues para el anuncio en cuestión&#58; 
&#160; 
 Ambiente pruebas&#58; https&#58;//devdonantes.eatcloud.info/ api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code = exito3920200714174214720 &amp; resolved =no &#160; 
&#160; 
 Como existe un registro, se debe desplegar al lado de la casilla de verificación el botón [copiar el código enviado por el beneficiario] (si el registro no existe, o existe, y está resuelto, o existe y no tiene registro en eatc-verification_code, el botón no se despliega). Si se oprime este botón debe colocar el valor que está en el campo eatc-verification_code de la anterior consulta, es decir &quot; 299025 &quot; en la casilla para verificar (es decir como si fuera un copy paste) 
&#160; 
 El usuario puede o no presionar dicho botón para llenar la casilla, y esta también se puede llenar manualmente. 
&#160; 
 [el siguiente funcionamiento es similar a lo ya implementado] Por lo tanto si el usuario digita el número 299025 (o lo copia a partir del registro del &quot;issue&quot;) y se oprime el botón &quot; valida el código &quot; ( https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= exito3920200714174214720 &amp;eatc-verification_code= 299025 ) el sistema lo debe dejar pasar. y debe traer a pantalla la siguiente información&#58; 
 eatc-donation_manager_name = Nombre del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-picker_name = Nombre de la persona quien recoge la donación 
 eatc-picker_doc_id = Documento de identidad de la persona quien recoge la donación 
 eatc-picker_license_plate = Nombre de la persona quien recoge la donación 
 eatc-adjudication_datetime = Fecha y hora de adjudicación 
 eatc-programed_picking_datetime = Fecha y hora de recogida programada 
 eatc-code = código de la donación a recoger 
 Si se digita un código diferente, se debe anunciar que el código no es válido y no dejar continuar. 

&#160; 
 Registro de la fecha y hora de verificación de código 
 Si la verificación del código resulta exitosa, el sistema debe tomar la fecha y hora actual ( current_datetime ) y con ella realizar el registro en &quot; eatc_code_verification_datetime &quot; en el respectivo encabezado ( eatc_dona_headers ), utilizando el siguiente llamado al CRD&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp;eatc_code_verification_datetime =&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 

&#160; 
 Para el ejemplo anterior sería&#58; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update &amp;eatc_code_verification_datetime =&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code= exito3920200714174214720 

&#160; 
 Registro de la fecha y hora de llegada (eatc-picking_checkin_datetime) si no hay fecha y hora de llegada registrada 
 El sistema debe validar si para el anuncio en cuestión existe una fecha y hora de llegada registrada ( eatc-picking_checkin_datetime ) . Si existe no realiza ningún registro de hora de llegada, es decir que deja la hora de llegada previamente registrada y pasa al siguiente proceso de validación ( Cambio de estado del anuncio si se encuentra un registro válido en “eatc-picking_checkout_datetime” ). Si no existe el registro de check-in, el sistema debe registrar la fecha y hora de llegada ( eatc-picking_checkin_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime=&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers.eatc-code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 En ambiente de pruebas, para el anuncio de donación cuyo eatc-code = exito3920200714174214720 , y que mediante la web app se le acaba de realizar un registro de validación de código a las 2019-09-19 01&#58;35&#58;54&#160; mediante la API se debe hacer la siguiente escritura 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime= 2019-09-19%2001&#58;35&#58;54 &amp;WHEREeatc-code= exito3920200714174214720 
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
 Cambio de estado del anuncio a “delivered” ***Nuevo&#58; cambio de eatc_state3 *** 
&#160; 
 El sistema debe proceder con el cambio del estado del anuncio y el respectivo registro en el historial de estados. 
&#160; 
 Cuando no existe una fecha y hora válida en “eatc-receipt_datetime” 

 (ANTERIORMENTE&#58; Si el anuncio tiene el registro de una fecha válida en el campo &quot;eatc-picking_checkout_datetime&quot; entonces se procedía con el cambio a &quot;delivered&quot;. Si no posee un registro válido en eatc-picking_checkout_datetime, termina el proceso y hace una última actualización (que puede entenderse como un &quot;error handler&quot; ya que no deben existir Issues abiertos cuando no hay hora de check-out).) 
&#160; 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado (se entiende que como se está en el proceso de verificación, existe una fecha válidad en eatc_code_verification_datetime, por lo tanto)&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= delivered &amp;eatc_state3=Verificado &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
 Se realiza el registro correspondiente a través del llamado al CRD. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
 Para el registro del estado &quot; delivered &quot; se toma la fecha en la que se entregó el anuncio ( eatc-picking_checkout_datetime ) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id )&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
&#160; 
 Para el anuncio de donación (en ambiente de pruebas) cuyo eatc-code = exito8620200709153619358 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-code&#58; &quot;exito8620200709153619358&quot;, 
 eatc-picking_checkout_datetime &#58; &quot;2020-07-09 19&#58;07&#58;07&quot;, 
 eatc-pod_id &#58; &quot;86&quot; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =exito8620200709153619358&amp; eatc-state = delivered &amp; eatc-date_time =2020-07-09%2019&#58;07&#58;07&amp; eatc-log = eatc-pod_id &#58;86 &#160; 
&#160; 
 Para consultar los estados registrados&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=exito8620200709153619358 
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
 Actualización del registro del Issue 
 Como el issue se resuelve con la validación del código, entonces se debe proceder a realizar la actualización del registro del issue (el sistema toma el respectivo _id para realizar la actualización) de la siguiente manera&#58; 
 eatc-dona_final_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state que debe corresponder a &quot;delivered&quot; 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration_solved_by_pod 
 resolved &#58; se coloca en este punto&#58; si 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=update&amp; eatc-dona_final_state = delivered &amp; log =app_automated_issue_registration_solved_by_pod&amp; resolved =si&amp;WHERE_id=&#123;&#123;eatc_checkin_and_deliver_issues._id&#125;&#125; 
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
 Actualización del registro del Issue (cuando no hay registro de fecha y hora de check-out) 
 Como el issue se resuelve con la validación del código, entonces se debe proceder a realizar la actualización del registro del issue (el sistema toma el respectivo _id para realizar la actualización) de la siguiente manera&#58; 
 eatc-dona_final_state &#58; se toma de la información del anuncio respectivo y corresponde a eatc_dona_headers. eatc-state 
 eatc-log &#58; se coloca lo siguiente (constante para la funcionalidad)&#58; app_automated_issue_registration_solved_by_pod 
 resolved &#58; se coloca en este punto&#58; si 
 Escritura con la API (METODO POST)&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &amp;_operacion=update&amp; eatc-dona_final_state = &#123;&#123; eatc_dona_headers. eatc-state&#125;&#125; &amp; log =app_automated_issue_registration_solved_by_pod&amp; resolved =si&amp;WHERE_id=&#123;&#123;eatc_checkin_and_deliver_issues._id&#125;&#125; 
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
 Cambio de estado del anuncio a &quot;a &quot;received&quot; (recibido) &quot; si se encuentra un registro válido en &quot;eatc-receipt_datetime&quot; para el anuncio en cuestión ***NUEVO&#58; registro eatc_state3 *** 
 Si el anuncio tiene el registro de una fecha válida en el campo &quot; eatc-receipt_datetime &quot; entonces el sistema debe proceder con el cambio del estado del anuncio y el respectivo registro en el historial de estados. Si no posee un registro válido en eatc-receipt_datetime , termina el proceso. 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= received &amp;eatc_state3=Recibido &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
 Se realiza el registro correspondiente a través del llamado al CRD. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = received &amp; eatc-date_time =&#123;&#123;eatc_dona_headers. eatc-receipt_datetime &#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
&#160; 
&#160; 
 Para el registro del estado &quot; received &quot; se toma la fecha en la que se verificó el el anuncio (eatc-receipt_datetime) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id) 

&#160; 
 El ANUNCIO TIENE UN REGISTRO DE ISSUE (NO RESUELTO)&#58; 
 Verificación del código de recogida 
 El sistema funciona de manera muy similar a la implementación anterior, con la diferencia que no se realiza la actualización del Issue porque este no existe 
&#160; 
 El sistema dispone un formulario para ingresar el Código de recogida del beneficiario que toma la donación.&#160; Este código corresponde al parámetro &quot; eatc-verification_code &quot;, del respectivo encabezado de donación ( eatc_dona_headers ). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-code= &#123;&#123; eatc-code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 El para el cuyo &quot; eatc-id &quot; = 8687012&#160; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
&#160; 
 El código de verificación (eatc-verification_code) es&#58; 715518 &#160;&#160; 
&#160; 
 Por lo tanto si el usuario digita dicho número (o lo copia a partir del registro del &quot;issue&quot;) y se oprime el botón &quot; valida el código &quot; ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;eatc-verification_code=715518 ) el sistema lo debe dejar pasar. y debe traer a pantalla la siguiente información&#58; 
 eatc-donation_manager_name = Nombre del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-picker_name = Nombre de la persona quien recoge la donación 
 eatc-picker_doc_id = Documento de identidad de la persona quien recoge la donación 
 eatc-picker_license_plate = Nombre de la persona quien recoge la donación 
 eatc-adjudication_datetime = Fecha y hora de adjudicación 
 eatc-programed_picking_datetime = Fecha y hora de recogida programada 
 eatc-code = código de la donación a recoger 
 Si se digita un código diferente, se debe anunciar que el código no es válido y no dejar continuar. 

&#160; 
 Registro de la fecha y hora de verificación de código 
 Si la verificación del código resulta exitosa, el sistema debe tomar la fecha y hora actual (current_datetime) y con ella realizar el registro en &quot; eatc_code_verification_datetime &quot; en el respectivo encabezado ( eatc_dona_headers ), utilizando el siguiente llamado al CRD.&#160;&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123; &#123;_DOM.CUA_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update &amp;eatc_code_verification_datetime =&#123;&#123; current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 

&#160; 
 Registro de la fecha y hora de llegada (eatc-picking_checkin_datetime) si no hay fecha y hora de llegada registrada 
 El sistema debe validar si para el anuncio en cuestión existe una fecha y hora de llegada registrada ( eatc-picking_checkin_datetime ) . Si existe no realiza ningún registro de hora de llegada, es decir que deja la hora de llegada previamente registrada y pasa al siguiente proceso de validación ( Cambio de estado del anuncio si se encuentra un registro válido en “eatc-picking_checkout_datetime” ). Si no existe el registro de check-in, el sistema debe registrar la fecha y hora de llegada ( eatc-picking_checkin_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime=&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers.eatc-code&#125;&#125; 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
 En ambiente de pruebas, para el anuncio de donación del éxito de San Antonio (eatc-pod_id=39) cuyo eatc-code = exito3920200715094304826 ,&#160; 
&#160; 
 Se realiza la siguiente consulta&#58; 
&#160; 
 Ambiente pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= exito3920200715094304826 &#160; 
&#160; 
 Dado que no tiene un registro válido en eatc-picking_checkin_datetime , entonces debe proceder a realizarse el respectivo registro con la fecha y hora actual de la siguiente manera 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime=&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp;WHEREeatc-code= exito3920200715094304826 &#160; 
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
 Cambio de estado del anuncio a &quot;delivered&quot;&#160; ** Revisar dinamismo a partir de _DOM.cua_master*** 
 Anteriormente&#58; ...si se encuentra un registro válido en &quot;eatc-picking_checkout_datetime&quot; para el anuncio en cuestión * 
&#160; 
 El sistema debe proceder con el cambio del estado del anuncio y el respectivo registro en el historial de estados, cuando no existe una fecha y hora válida en “eatc-receipt_datetime” . 

 (ANTERIORMENTE&#58; Si el anuncio tiene el registro de una fecha válida en el campo &quot;eatc-picking_checkout_datetime&quot; entonces el sistema debe proceder con el cambio del estado del anuncio y el respectivo registro en el historial de estados. Consulta con la API&#58;&#160; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.CUA_master&#125;&#125; /eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; Ejemplo anuncio sin registro válido en &quot;eatc-picking_checkout_datetime&quot; &#58; El para el anuncio del éxito de San Antonio en ambiente de pruebas cuyo &quot; eatc-code = exito3920200715091708845 Se realiza la siguiente consulta&#58; Ambiente pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= exito3920200715091708845 Como la misma trae un dato válido en el parámetro &quot;eatc-picking_checkout_datetime&quot;, entonces se debe proceder con el cambio de estado) 
&#160; 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= delivered &amp;eatc_state3=Verificado &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header ) 
 Se realiza el registro correspondiente a través del llamado al CRD. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
 Para el registro del estado &quot; delivered &quot; se toma la fecha en la que se entregó el anuncio ( eatc-picking_checkout_datetime ) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id )&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
&#160; 
 Para el anuncio de donación (en ambiente de pruebas) cuyo eatc-code = exito3920200715091708845 (del ejemplo anterior), dado que se tienen los siguientes datos&#58; 
 eatc-code&#58; &quot; exito3920200715091708845 &quot;, 
 eatc-picking_checkout_datetime &#58; Fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS, 

 eatc-pod_id &#58; &quot;39&quot; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code = exito3920200715091708845 &amp; eatc-state = delivered &amp; eatc-date_time =&#123;&#123;current_datetime en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; eatc-log = eatc-pod_id &#58;39&#160; 
&#160; 
 Para consultar los estados registrados&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code= exito3920200715091708845 &#160; 
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
 ***NUEVO***Cambio de estado del anuncio a &quot;a &quot;received&quot; (recibido) &quot; si se encuentra un registro válido en &quot;eatc-receipt_datetime&quot; para el anuncio en cuestión ***NUEVO&#58; registro eatc_state3 *** 
 Si el anuncio tiene el registro de una fecha válida en el campo &quot; eatc-receipt_datetime &quot; entonces el sistema debe proceder con el cambio del estado del anuncio y el respectivo registro en el historial de estados. Si no posee un registro válido en eatc-receipt_datetime , termina el proceso. 
&#160; 
 Utilizando el CRD se realiza el siguiente llamado para cambiar el estado&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-state= received &amp;eatc_state3=Recibido &amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
&#160; 
&#160; 
 Registro de información en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
&#160; 
 Se realiza el registro correspondiente a través del llamado al CRD. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc-state = received &amp; eatc-date_time =&#123;&#123;eatc_dona_headers. eatc-receipt_datetime &#125;&#125;&amp; eatc-log = eatc-pod_id &#58;&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125;&#160; 
&#160; 
 Para el registro del estado &quot; received &quot; se toma la fecha en la que se verificó el el anuncio (eatc-receipt_datetime) y en log ( eatc-log ) se colocan los datos de quienes cambiaron el estado (el eatc-pod_id) 

&#160; 
 [Segunda etapa&#58; planteamiento inicial en borrador] verificación remota criptográfica 
 Si el registro del issue trae un dato en el campo eatc-verification_code ,&#160; el sistema debe presentar un botón que diga&#58; &quot; copiar el código enviado por el beneficiario.&#160; Al usuario presionar este botón el sistema se debe tomar el dato que viene en eatc-verification_code y desencriptarlo con la clave que provee el eatc-token del registro de issue.&#160; El valor&#160; del código desencriptado recuperado se coloca el en campo de verificación del código para pasar a la funcionalidad de &quot;verificación del código de recogida de la donación&quot; 

&#160; 
 Captura de documento soporte 
 El propósito de esta nueva funcionalidad es desplegar un campo de captura obligatorio para el documento de soporte (en el mismo lugar en donde se captura el código de verificación del anuncio) para aquellas eatc_cua que tengan el campo &quot; eatc_doc_madatory=y &quot;.&#160; Si las cuentas no tienen marcado este parámetro como &quot;y&quot; (vacío, nulo, &quot;n&quot;), entonces la funcionalidad de captura del código de verificación se realizará tal y como se realiza hasta el momento, capturando solamente dicho código.&#160; El botón de &quot;verificar&#160; 

 Despliegue de la funcionalidad 
 Si evaluando la información de la cuenta respectiva ( &#123;&#123;cua_user&#125;&#125; ) se determina que la cuenta tiene como mandatorio la captura de eatc-doc ( eatc_doc_madatory=y ).&#160; Para ello el sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; &amp; eatc_doc_madatory=y&amp;_cmp=name´ 
&#160; 
 Nota implementación modernización&#58; En modernizacion existe la configuración que es en la tabla &quot; pods &quot; o en la tabla &quot; cua_users &quot; en la columna &quot; document_mandatory &quot; que por defecto es &quot; NA &quot; poner &quot; mandatory_verification &quot;, si ese es el caso se pide la referencia del documento de soporte al momento de validar el codigo de la donación 
&#160; 
 Si el sistema entrega no entrega un resultado válido, entonces no se despliega la funcionalidad.&#160; Si entrega un resultado válido entonces el sistema despliega un campo de captura que se describe más abajo. 
&#160; 
 Ejemplo 1 &#58; Ambiente de pruebas, cuenta &quot;exito&quot;&#58; 
 El sistema realiza el siguiente llamado&#58;&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp; eatc_doc_madatory=y&amp;_cmp=name&#160; &#160;&#160; &#160;&#160; 
 Como NO se recibe una respuesta válida el sistema NO habilita el campo de captura (es decir el funcionamiento de esta funcionalidad es tal y como ha sido hasta el momento). 
&#160; 
 Ejemplo 2 &#58; Ambiente de pruebas, cuenta &quot;postobon&quot;&#58; 
 El sistema realiza el siguiente llamado&#58;&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=postobon&amp; eatc_doc_madatory=y&amp;_cmp=name &#160; &#160;&#160; &#160;&#160; 
 Como se recibe una respuesta válida el sistema debe habilitar El siguiente campo de captura. 

 Documento soporte 
 Place holder&#58; class=&quot; lbl_digitar_documento_soporte &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_digitar_documento_soporte )&#160; 
&#160; 
 Tooltip&#58; class=&quot; lbl_digitar_documento_soporte_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_digitar_documento_soporte_desc )&#160; 
&#160; 
 Tipo de campo de captura&#58; text_input 
&#160; 
 Tipo de dato&#58; string (alfanumérico) 
&#160; 
 ****NUEVO&#58; Valor por defecto *** 
 El sistema deberá cargar como valor por defecto del input respectivo, el valor que esté registrado en &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; en caso de que exista 
 &#123;&#123;URL_beneficiarios&#125;&#125; /api/ &#123;&#123;_DOM. cua_master &#125;&#125; ?_tabla=eatc_dona_headers? eatc-code= &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &amp;_cmp= eatc-doc 
&#160; 
 Si no existe valor en eatc-doc entonces no se coloca valor por por defecto en el input 
&#160; 
 Validación&#58;&#160; obligatoriedad (cuando se despliega la funcionalidad, este dato es obligatorio)&#58; cuando el usuario no ingrese el valor e intente presionar el botón &quot;Validar código&quot; , el sistema desplegará el siguiente mensaje&#58; 
 class=&quot; lbl_digitar_documento_soporte_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_digitar_documento_soporte_desc )&#160; 
&#160; 
 Se escribe en (al accionar el botón &quot;Validar código&quot; )&#58; eatc_dona_headers. eatc-doc 
 &#123;&#123;URL_beneficiarios&#125;&#125; /crd/ &#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-doc= &#123;&#123;input&#125;&#125; &amp;WHERE= &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 

 ***NUEVO &#58; CUADRO DE DIÁLOGO PARA DESCARGAR SOPORTE DE ENTREGA *** 
 Una vez exista una validación exitosa del código de recogida, el sistema deberá desplegar un cuadro de diálogo (para aquellas cuentas que cumplan con los requisitos de despliegue de esta funcionalidad) en donde se le preguntará al usuario si desea descargar la constancia de donación.&#160; El cuadro de diálogo tendrá dos opciones,&#160; 

&#160; 
 Condición de despliegue de la funcionalidad 
 Cuenta con licencia impactoplus 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; &amp; type= impactoplus &amp;_cmp=name 
&#160; 
 Si el sistema entrega una respuesta válida, se desplegará la funcionalidad 

 Pregunta del cuadro de texto&#58; 
 ¿Desea descargar la constancia de entrega de la presente donación? 
&#160; 
 Label 
 class=lbl_desea_constancia_entrega&#160; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_desea_constancia_entrega )&#160; 

 Botón &quot;No&quot;&#58; 
 Label 
 class=lbl_no&#160; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_no )&#160; 
 El usuario cuando oprime este botón, cierra el cuadro de diálogo y retorna a la funcionalidad que retorna la verificación del código de recogida ante una validación exitosa 

 Botón &quot;Si&quot;&#58; 
 Label 
 class=lbl_si&#160; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_si )&#160; 
 SI el usuario oprime este botón, el sistema ejecuta la funcionalidad de &quot; Constancia de entrega &quot; descargando un PDF con dicha constancia 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-verificaci%C3%B3n-del-codigo-de-recogida%2F4131612634-8-entrega-de-donaciones--eatc_dona_checkin-.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-verificaci%C3%B3n-del-codigo-de-recogida%2F4131612634-8-entrega-de-donaciones--eatc_dona_checkin-.png 
 eatcloud donantes web-app 

 94.0000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 65e452d2-5318-4c9d-8f19-4773bccd3b00 
 1!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 4b11ce09-a6d6-48a5-9f5d-2c5423c07712 
 2025-06-13T06:08:21.1678815Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"2558d6f1-9bff-4ce0-b582-632a9a0c8a9c","SequenceId":1217,"FluidContainerCustomId":"08b4a819-75e3-43fb-b9b7-c82dd498ae62","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 VERIFICACIÓN DEL CÓDIGO DE RECOGIDA