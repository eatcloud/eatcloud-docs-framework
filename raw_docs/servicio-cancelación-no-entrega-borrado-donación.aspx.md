# servicio-cancelación-no-entrega-borrado-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar el API pública de cancelación - no entrega - borrado de una donación.&#160; La siguiente documentación es indicativa de los temas que se deben tener en cuenta para este desarrollo, y se debe tomar como una guía (no como una camisa de fuerza). 

 Validación de existencia de cuenta maestra y la cuenta usuario&#58; 
&#160; 
 El sistema valida si existe la cuenta maestra y la cuenta usuario con la cual se invocó el servicio. Si no existen el servicio retornará un mensaje de error 
 cua_master does not exist 
 cua_user does not exist 

 CANCELACIÓN UNA DONACIÓN 
&#160; 
 Se basa en la documentación del API pública respectiva y en la documentación del proceso de cancelación de donaciones (del cual se puede reciclar código para el presente servicio) 
&#160; 
 Comparaciones (para no cancelar anuncios con estado&#58; pre-certificado, certificado, cancelado eatc-state=_nin_pre-certified,certified,cancelled )&#58; 
 Si el estado del anuncio (eatc-state) del anuncio no es programado, despachado, recibido, pre-certificado, certificado ( scheduled, delivered, received, pre-certified, certified ) (es decir si la donación tiene estado &quot; announced &quot; o &quot; awarded &quot;) o (es posible que estas validaciones ya no sean necesarias al utilizar el estado como validador) no hay información registrada (o está en cero o que no tenga una fecha de programación válida) en cualquiera de estos campos &quot; eatc-picking_checkin_datetime o eatc-check_datetime o eatc-picking_checkout_datetime &quot; debe ejecutar las siguientes acciones&#58; 

&#160; 
 Actualización de la información del encabezado de donación ( eatc_dona_headers ) 
&#160; 
 Al liberar el anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 
 eatc-state&#58; debe cambiar de &quot;cancelled&quot;. 
 eatc_state_2 &#58; (OPCIONAL)&#58; debe incorporarse según lo que llegue en el parámetro respectivo del llamado ( es un campo que no existe en eatc_dona_headers , por lo tanto se debe crear en todos los eatc_dona_headers de todas las cuentas maestras ) 
&#160; 
 Registro del estado &quot;cancelled&quot; &#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_headers &amp;_operacion=update &amp; eatc-state = cancelled &amp; eatc_state_2 =&#123;&#123; eatc_state_2 &#125;&#125; &amp;WHERE eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125; 

&#160; 
 Registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history )&#58; 
 eatc-dona_header_code = &#123;&#123; eatc-dona_header_code &#125;&#125; 
 eatc-state = cancelled 
 eatc_state_2 =&#123;&#123;eatc_state_2&#125;&#125; =&gt; es un campo que no existe en eatc_dona_header_history , por lo tanto se debe crear en todos los eatc_dona_header_history de todas las cuentas maestras. 
 eatc-date_time =&#123;&#123;datetime&#125;&#125; 
 eatc-log =&quot;pbapi_cancel user &quot;&#123;&#123;user&#125;&#125;&quot; 

&#160; 
 Registro del estado &quot;cancelled&quot; &#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125;&amp; eatc-state = cancelled &amp; eatc_state_2 =&#123;&#123; eatc_state_2 &#125;&#125;&amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log =&quot;pbapi_cancel user &quot;&#123;&#123;user&#125;&#125;&quot; 
&#160; 
 ***NUEVO&#58; Borrado de KPIs *** 
 El sistema deberá borrar los KPIs del anuncio correspondiente&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_kpi&amp;_operacion=delete&amp;WHEREeatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125; 
&#160; 
 DEPRECADO&#58; Creación de registro en eatc_doma_state_change_history 
 Nota para el desarrollo&#58; Esta escritura se basa en una homóloga que se realiza en el servicio &quot; libdona &quot; y es posible que se pueda reciclar código para realizarla. 
&#160; 
 Este llamado se hace si la donación tiene estado&#58; 
 awarded 
 scheduled 
 delivered 
 received 
&#160; 
 Para realizar las anotaciones de la donación cancelada, se toma la información del llamado al servicio y se genera la siguiente concatenación de información (para una nota privada) 
&#160; 
 &#123;&#123;notas_donacion_liberada&#125;&#125; 
 pbapi_cancel&#58; Donación&#58; &#123;&#123; eatc_dona_header_code &#125;&#125;, Cuenta&#58; &#123;&#123; eatc_cua &#125;&#125;, pod_id&#58; &#123;&#123; eatc_pod_id &#125;&#125;, e-mail pod&#58; &#123;&#123; eatc_pod_email &#125;&#125; 
&#160; 
 Nota púbica 
&#160; 
 De igual manera se toma la información del llamado a servicio, se obtiene con ella otra información 
 &#123;&#123; nombre_pod &#125;&#125; = &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123; eatc_cua &#125;&#125;/eatc_pods? eatc-id =&#123;&#123; eatc_pod_id &#125;&#125;&amp;_cmp=eatc-name 
&#160; 
 y se genera la siguiente concatenación de información (que debe armarse con labels para su internacionalización) una nota pública, que se entregará al beneficiario 
&#160; 
 &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
 La donación ( label (class)= lbl_la_donacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_la_donacion ) ) &#58; &#123;&#123; eatc_dona_header_code &#125;&#125; de nuestro donante (label (class)= lbl_de_nuestro_donante ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_de_nuestro_donante )) &#58; &#123;&#123; eatc_cua &#125;&#125;, fue cancelada por el punto de donación (label (class)= lbl_fue_cancelada_por_pod (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel= lbl_fue_cancelada_por_pod ) ) &#58; &#123;&#123; nombre_pod &#125;&#125; 
&#160; 
 Consulta del estado actual del gestor de donaciones&#58; 
&#160; 
 El sistema deberá consultar el estado actual del gestor de donaciones (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) para colocarlo en el registro del historial 
&#160; 
 El sistema deberá realizar la siguiente actualización de datos (como ya no se suspende, en el historial debe aparecer, tanto en el actual, como en el nuevo estado con el estado del donante a la hora de realizar el cambio (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) . Además se deberá crear el campo &quot;eatc_public_notes&quot; en la tabla respectiva para realizar el nuevo registro de la Nota Pública) 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state=&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp; eatc_doma_new_state =&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125;&amp; eatc_public_notes= &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 
 LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN 
&#160; 
 Endpoint (según documentación ([POST] servicio&#58; frmCancelarExcedente (Cancelar) ) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio=frmCancelarExcedente 
&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
 El código que llega en el parámetro &#123;&#123; eatc-dona_header_code &#125;&#125; &#160;=&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio ( cua_master ) =&gt; parámetro de carácter obligatorio 
&#160; 
 Si falta algún parámetro para realizar los respectivos registros, el servicio debe responder&#58; 
 retry&#58; incomplete data 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de Éxito 
 Success 
&#160; 
 Creación de traza de auditoría 
 El servicio deberá crear un log para determinar desde dónde se llamó el servicio, el usuario que lo hizo y la fecha y hora. 

 REGISTRO DE NO ENTREGA DE UNA DONACIÓN 
&#160; 
 Se basa en la documentación del API pública respectiva &#160; 
&#160; 
 Comparaciones&#160; (para no cancelar anuncios con estado&#58; pre-certificado, certificado, not_delivered eatc-state=_nin_ received, pre-certified,certified,not_delivered ) 
&#160; 
 Si el estado del anuncio (eatc-state) no es recibido, pre-certificado, certificado ( received, pre-certified, certified, not_delivered ) es decir, si la donación es se deben ejecutar las siguientes acciones&#58; 
 ***NUEVO&#58; validación para asegurar que el _doma sea la organización que tiene asignada la donación que se va a marcar como no entregada y que la donación esté en estado “scheduled” (que es el estado que permite esta funcionalidad) 
&#160; 
 Si en los parámetros de invocación se recibe el nuevo parámetro _platform= app , entonces el sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; _cuamaster &#125;&#125; / eatc_dona_headers ? eatc-state = scheduled &amp; eatc-code =&#123;&#123; eatc-code &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; _doma &#125;&#125;&amp;_cont 
&#160; 
 Si el resultado es igual a 1, entonces el sistema deberá permitir seguir adelante. &#160;Si el resultado es 0, entonces el servicio deberá responder con un mensaje de error y no realizará acción alguna. 
&#160; 
 Actualización de la información del encabezado de donación ( eatc_dona_headers ) 
&#160; 
 Al liberar el anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 
 eatc-state&#58; debe cambiar de &quot;cancelled&quot;. 
 Registro del estado &quot; not_delivered &quot; &#58; 
&#160; 
 eatc_state_2 &#58; (OPCIONAL)&#58; debe incorporarse según lo que llegue en el parámetro respectivo del llamado ( es un campo que no existe en eatc_dona_headers , por lo tanto se debe crear en todos los eatc_dona_headers de todas las cuentas maestras ) 

&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_headers &amp;_operacion=update &amp; eatc-state = not_delivered &amp; eatc_state_2 =&#123;&#123; eatc_state_2 &#125;&#125; &amp;WHERE eatc-code =&#123;&#123; eatc-dona_header_code &#125;&#125; 
&#160; 
 Registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history )&#58; 
 eatc-dona_header_code = &#123;&#123; eatc-dona_header_code &#125;&#125; 
 eatc-state = not_delivered 
 eatc_state_2 =&#123;&#123;eatc_state_2&#125;&#125; =&gt; es un campo que no existe en eatc_dona_header_history , por lo tanto se debe crear en todos los eatc_dona_header_history de todas las cuentas maestras. 
 eatc-date_time =&#123;&#123;datetime&#125;&#125; 
 eatc-log =&quot;pbapi_ not_delivered user &quot;&#123;&#123;user&#125;&#125;&quot; 

&#160; 
 Registro del estado &quot; not_delivered &quot; &#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125;&amp; eatc-state = not_delivered &amp; eatc_state_2 =&#123;&#123; eatc_state_2 &#125;&#125;&amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log =&quot;pbapi_ not_delivered user &quot;&#123;&#123;user&#125;&#125;&quot; 

&#160; 
 ***NUEVO&#58; Borrado de KPIs *** 
 El sistema deberá borrar los KPIs del anuncio correspondiente&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_kpi&amp; _operacion = delete &amp;WHEREeatc-dona_header_code=&#123;&#123; eatc-dona_header_code &#125;&#125; 
&#160; 
 DEPRECADO&#58; Creación de registro en eatc_doma_state_change_history 
 Nota para el desarrollo&#58; Esta escritura se basa en una homóloga que se realiza en el servicio &quot; libdona &quot; y es posible que se pueda reciclar código para realizarla. 
&#160; 
 Este llamado se hace si la donación tiene estado&#58; 
 awarded 
 scheduled 
 delivered 
 received 
&#160; 
 Para realizar las anotaciones de la donación cancelada, se toma la información del llamado al servicio y se genera la siguiente concatenación de información (para una nota privada) 
&#160; 
 &#123;&#123;notas_donacion_liberada&#125;&#125; 
 pbapi_not_delivered&#58; Donación&#58; &#123;&#123; eatc_dona_header_code &#125;&#125;, Cuenta&#58; &#123;&#123; eatc_cua &#125;&#125;, pod_id&#58; &#123;&#123; eatc_pod_id &#125;&#125;, e-mail pod&#58; &#123;&#123; eatc_pod_email &#125;&#125; 
&#160; 
 Nota púbica 
&#160; 
 De igual manera se toma la información del llamado a servicio, se obtiene con ella otra información 
 &#123;&#123; nombre_pod &#125;&#125; = &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123; eatc_cua &#125;&#125;/eatc_pods? eatc-id =&#123;&#123; eatc_pod_id &#125;&#125;&amp;_cmp=eatc-name 
&#160; 
 y se genera la siguiente concatenación de información (que debe armarse con labels para su internacionalización) una nota pública, que se entregará al beneficiario 
&#160; 
 &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 
 La donación ( label (class)= lbl_la_donacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_la_donacion ) ) &#58; &#123;&#123; eatc_dona_header_code &#125;&#125; de nuestro donante (label (class)= lbl_de_nuestro_donante ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_de_nuestro_donante )) &#58; &#123;&#123; eatc_cua &#125;&#125;, fue marcada como no entregada por el punto de donación (label (class)= lbl_fue_no_entregada_por_pod ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel= lbl_fue_no_entregada_por_pod ) ) &#58; &#123;&#123; nombre_pod &#125;&#125; 
&#160; 
 Consulta del estado actual del gestor de donaciones&#58; 
&#160; 
 El sistema deberá consultar el estado actual del gestor de donaciones (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) para colocarlo en el registro del historial 
&#160; 
 El sistema deberá realizar la siguiente actualización de datos (como ya no se suspende, en el historial debe aparecer, tanto en el actual, como en el nuevo estado con el estado del donante a la hora de realizar el cambio (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) . Además se deberá crear el campo &quot;eatc_public_notes&quot; en la tabla respectiva para realizar el nuevo registro de la Nota Pública) 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state=&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp; eatc_doma_new_state =&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125;&amp; eatc_public_notes= &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 
&#160; 
 Llamado al servicio de integración con blockchain 
&#160; 
 Endpoint (según documentación ([POST] servicio&#58; frmNoEnviadoExcedente ) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio= frmNoEnviadoExcedente 

&#160; 
 Parámetros para el llamado al servicio&#58; 
 eatc_dona_header_code&#58; 
&#160; 
 El código que llega en el parámetro &#123;&#123; eatc-dona_header_code &#125;&#125; &#160;=&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
&#160; 
 Cuenta maestra a la cual pertenece el anuncio ( cua_master ) =&gt; parámetro de carácter obligatorio 
&#160; 
 Si falta algún parámetro para realizar los respectivos registros, el servicio debe responder&#58; 
 retry&#58; incomplete data 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de Éxito 
 Success 
&#160; 
 Creación de traza de auditoría 
 El servicio deberá crear un log para determinar desde dónde se llamó el servicio, el usuario que lo hizo y la fecha y hora. 

 BORRADO DE UNA DONACIÓN 
&#160; 
 Se basa en la documentación del API pública respectiva &#160; 
&#160; 
 Registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history )&#58; 
 eatc-dona_header_code = &#123;&#123; eatc-dona_header_code &#125;&#125; 
 eatc-state = deleted 
 eatc-date_time =&#123;&#123;datetime&#125;&#125; 
 eatc-log =&quot;pbapi_ deleted user &#123;user&#125;&#125;&quot; 

&#160; 
 Registro del estado &quot; deleted &quot; &#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125;&amp; eatc-state = deleted &amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log =&quot;pbapi_ deleted user &#123;user&#125;&#125;&quot; 
&#160; 
 Copiado del encabezado de donación ( eatc_dona_headers ) en estructura homóloga eatc_deleted_dona_header de la cuenta &quot;eatcloud&quot; 
&#160; 
 En una estructura homóloga a la estructura de eatc_dona_headers que se debe crear en la cuenta eatcloud, adicionando los siguientes campos 
 eatc_delete_datetime = &#123;&#123;timestamp&#125;&#125; 
 eatc_delete_by =&#160; &#123;&#123;user&#125;&#125; 

&#160; 
 Copiado de los detalles de la donación ( eatc_dona ) en estructura homóloga eatc_deleted_dona de la cuenta &quot;eatcloud&quot; 
&#160; 
 En una estructura homóloga a la estructura de eatc_dona que se debe crear en la cuenta eatcloud, adicionando los siguientes campos 
 eatc_delete_datetime = &#123;&#123;timestamp&#125;&#125; 
 eatc_delete_by =&#160; &#123;&#123;user&#125;&#125; 
&#160; 
 DEPRECADO&#58; Creación de registro en eatc_doma_state_change_history 
 Nota para el desarrollo&#58; Esta escritura se basa en una homóloga que se realiza en el servicio &quot; libdona &quot; y es posible que se pueda reciclar código para realizarla. 
&#160; 
 Este llamado se hace si la donación tiene estado&#58; 
 awarded 
 scheduled 
 delivered 
 received 
&#160; 
 Para realizar las anotaciones de la donación cancelada, se toma la información del llamado al servicio y se genera la siguiente concatenación de información (para una nota privada) 
&#160; 
 &#123;&#123;notas_donacion_liberada&#125;&#125; 
 pbapi_deleted&#58; Donación&#58; &#123;&#123; eatc_dona_header_code &#125;&#125;, Cuenta&#58; &#123;&#123; eatc_cua &#125;&#125;, pod_id&#58; &#123;&#123; eatc_pod_id &#125;&#125;, e-mail pod&#58; &#123;&#123; eatc_pod_email &#125;&#125; 
&#160; 
 Nota púbica 
&#160; 
 De igual manera se toma la información del llamado a servicio, se obtiene con ella otra información 
 &#123;&#123; nombre_pod &#125;&#125; = &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123; eatc_cua &#125;&#125;/eatc_pods? eatc-id =&#123;&#123; eatc_pod_id &#125;&#125;&amp;_cmp=eatc-name 
&#160; 
 y se genera la siguiente concatenación de información (que debe armarse con labels para su internacionalización) una nota pública, que se entregará al beneficiario 
&#160; 
 &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 
&#160; 
 La donación ( label (class)= lbl_la_donacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_la_donacion ) ) &#58; &#123;&#123; eatc_dona_header_code &#125;&#125; de nuestro donante (label (class)= lbl_de_nuestro_donante ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_de_nuestro_donante )) &#58; &#123;&#123; eatc_cua &#125;&#125;, fue borrada por el punto de donación (label (class)= lbl_fue_borrada_por_pod ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel= lbl_fue_borrada_por_pod ) ) &#58; &#123;&#123; nombre_pod &#125;&#125; 
&#160; 
 Consulta del estado actual del gestor de donaciones&#58; 
&#160; 
 El sistema deberá consultar el estado actual del gestor de donaciones (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) para colocarlo en el registro del historial 
&#160; 
 El sistema deberá realizar la siguiente actualización de datos (como ya no se suspende, en el historial debe aparecer, tanto en el actual, como en el nuevo estado con el estado del donante a la hora de realizar el cambio (&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;) . Además se deberá crear el campo &quot;eatc_public_notes&quot; en la tabla respectiva para realizar el nuevo registro de la Nota Pública) 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; codigo_autogenerado_anticolisiones &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_bo_user= eatcloud_tech &amp;eatc_doma_prev_state=&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp; eatc_doma_new_state =&#123;&#123;eatc_donation_managers. eatc_state &#125;&#125;&amp;eatc_cause_code= susp_autom_no_recogió_donacion &amp;eatc_notes= &#123;&#123;notas_donacion_liberada&#125;&#125;&amp; eatc_public_notes= &#123;&#123;notas_publicas_donacion_liberada&#125;&#125; 

&#160; 
 Borrado del encabezado de donación ( eatc_dona_headers ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_headers &amp;_operacion=delete&amp;WHERE eatc-code =&#123;&#123; eatc-dona_header_code &#125;&#125; 

&#160; 
 Borrado de los detalles de la donación ( eatc_dona ) del anuncio de donación 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona &amp;_operacion=delete&amp;WHERE eatc-dona_header_code =&#123;&#123; eatc-dona_header_code &#125;&#125; 

&#160; 
 ***NUEVO&#58; Borrado de KPIs *** 
 El sistema deberá borrar los KPIs del anuncio correspondiente&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master&#125;&#125; /?_tabla= eatc_dona_kpi&amp; _operacion = delete &amp;WHEREeatc-dona_header_code=&#123;&#123; eatc-dona_header_code &#125;&#125; 

&#160; 
 Si falta algún parámetro para realizar los respectivos registros, el servicio debe responder&#58; 
 retry&#58; incomplete data 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de Éxito 
 Success 
&#160; 
 Creación de traza de auditoría 
 El servicio deberá crear un log para determinar desde dónde se llamó el servicio, el usuario que lo hizo y la fecha y hora. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 
 67b7e1a1-6a66-4fb8-b501-671dbfe73038 
 1!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 b5eb4229-f714-4689-a2e7-8d18a8529829 
 2025-07-23T05:48:12.4509741Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"e6b4e973-6713-4fbf-bbcf-31a48a240133","SequenceId":119,"FluidContainerCustomId":"dd985022-269c-417a-9021-bc52e6684c0b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 SERVICIO PÚBLICO DE CANCELACIÓN - NO ENTREGA - BORRADO DE DONACIÓN