# cancelación-de-anuncios-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** Cancelación de anuncios para diferentes cuentas maestras: 

 El proceso de cancelación de anuncios debe correr para todas las cuentas maestras registradas en el respectivo maestro: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 

 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 

 Cancelación de anuncios de donación las horas determinadas en la persistencia eatc_timeout_rules horas después de haberse publicado ***DINAMIZAR para múltiples cuentas maestras. 

 El sistema debe cancelar los  anuncios de donación que hallan sido publicados, pero que en el tiempo determinado en el esquema de persistencia eatc_timeout_rules no hallan sido por lo menos ****NUEVO**** programada su recogida (para ello se programó inicialmente la eatc-cancellation_datetime de acuerdo a la lectura de dicho esquema de persistencia. Vale la pena resaltar que este parámetro de las 48 horas (definido a 4 de diciembre de 2019) se obtiene leyendo el parámetro " eatc-timeout_in_hours " de  

 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout 

 Consulta de anuncios ***DINAMIZAR para múltiples cuentas maestras***:  
 El sistema debe consultar aquellos anuncios con estado ( eatc-state ) "announced" (anunciados), "awarded" (adjudicados), scheduled (programados). 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona_headers?eatc-state=announced,awarded,scheduled     

 Ejemplo, eatc_cua_master. eatc_cua=abaco, ambiente de productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=announced,awarded,scheduled      
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=announced,awarded,scheduled&_compress    

 Comparaciones (para no cancelar anuncios con estado eatc-state=scheduled y posteriores):  
 Posteriormente debe comparar el campo " eatc-cancellation_datetime ", con la fecha y hora actual.  Si la diferencia entre la fecha y hora actual y la fecha de adjudicación es superior a un segundo (es decir que la fecha de cancelación es previa a la fecha y hora actual) y el estado del anuncio (eatc-state) no es programado, despachado, recibido, pre-certificado, certificado ( scheduled, delivered, received, pre-certified, certified ) (es decir si la donación tiene estado " announced " o " awarded ") o (es posible que estas validaciones ya no sean necesarias al utilizar el estado como validador) no hay información registrada (o está en cero o que no tenga una fecha de programación válida) en cualquiera de estos campos " eatc-picking_checkin_datetime o eatc-check_datetime o eatc-picking_checkout_datetime " debe ejecutar las siguientes acciones:  

 Acción 1: Actualización de la información del encabezado de donación ( eatc_dona_headers ) 
 Al liberar el  anuncio de donación se debe actualizar la siguiente información: 
 eatc-state: debe cambiar de "cancelled". 

 Acción 2: registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ): cambia el eatc-log, porque en este caso solo se cancela cuando no ha sido adjudicado, dado que si se programa se obligará a la fundación a recogerlo ***DINAMIZAR para múltiples cuentas maestras***. 

 Se debe registrar el estado "announced" procurando incorporar la información del adjudicatario al cual se le eliminó la adjudicación, en el campo ( eatc-log )  

 eatc-dona_header_code =[ eatc_dona_headers .eatc-code] 
 eatc-state = cancelled 
 eatc-date_time =[datetime] 
 eatc-log ="EatCloud canceló el anuncio porque después de {{ eatc_timeout_rules.eatc-timeout_in_hours {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}?eatc-timeout_name=dona_cancellation_timeout}} horas no de publicado no fue adjudicado" 

 Utilizando el API el registro sería algo como lo siguiente 

 Registro del estado "annouced" :  
 {{URL_entorno_donantes}}/crd/{{eatc_cua_master. eatc_cua }} /?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc-code}}& eatc-state = cancelled & eatc-date_time ={{datetime}}& eatc-log ="EatCloud canceló el anuncio porque después de 48 horas no de publicado no fue adjudicado" 

 ***NUEVO: LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN *** 
 Endpoint (según documentación ([POST] servicio: frmCancelarExcedente (Cancelar)) : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmCancelarExcedente 

 Parámetros para el llamado al servicio: 

 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio (_DOM. cua_master ) => parámetro de carácter obligatorio 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CANCELACIÓN DE ANUNCIOS DE DONACIÓN