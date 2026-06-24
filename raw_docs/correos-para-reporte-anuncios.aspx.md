# correos-para-reporte-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante para el desarrollo 
 Esta funcionalidad deber estar disponible en: BO Donantes.  Dado que en un cercano futuro se pretende migrar el BO a Datagov Cuentas, entonces el desarrollador debe plantearse cmo ser la mejor manera para abordar el desarrollo sin generar muchos reprocesos (una opcin puede ser en primera instancia hacer una implementacin sobre datagov cuentas y luego a partir de la misma la implementacin en el BO Donantes legacy).  Aunque se documenta la funcionalidad como parte del BO de Donantes, se deja igualmente documentados los accesos en el men lateral de Datagov Cuentas , para realizar la incorporacin a dicha plataforma. 

 Generalidades de la funcionalidad 
 Con esta funcionalidad, el usuario Super administrador (Tipo A) podr configurar correos electrnicos, para que (inicialmente) a dos cortes diarios de su eleccin (11:50:00 y 17:50:00) le llegue un correo electrnico con el reporte de los anuncios que en ese momento estn en un determinado estado. Es importante generarle al men y la funcionalidad como tal un id de funcionalidad, para que se pueda perfilar por vertical y tipo de licencia 

 Descripcin de la funcionalidad 

 Ttulo: 
 class=" lbl_config_correos_info_anuncios " 

 Descripcin: 
 class=" lbl_config_correos_info_anuncios_desc " 

 Formulario para la creacin de correos 
 Correo electrnico: 
 Place holder: class=" lbl_email_reporte_estados " 
 Tooltip: class=" lbl_email_reporte_estados_desc " 
 Tipo de dato: email 
 Tipo de input: text input 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad y formato email 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_email ={{ input }} 

 Estado del anuncio: 
 Place holder: class=" lbl_estado_anuncio " 
 Tooltip: class=" lbl_estado_anuncio_desc " 
 Tipo de dato: string 
 Tipo de input: Selector mltiple construdo con la etiqueta ( eatc_dona_headers_states. eatc_plural_label ) y el valor ( eatc_dona_headers_states. eatc_code que ser el valor que se lleve al registro) que se obtiene de la siguiente consulta:   
 {{URL_entorno_datagov}}/api/eatcloud/eatc_dona_headers_states?_id=_* 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad (de por lo menos seleccionar un valor) 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_state ={{ input }} 

 Nota: Si hay mltiples selecciones, se guarda un registro por estado seleccionado, similar a como se guardan los registros en eatc_config_labels 

 Hora de corte para el envo: 
 Place holder: class=" lbl_hora_corte_envio " 
 Tooltip: class=" lbl_hora_corte_envio_desc " 
 Tipo de dato: hora militar 
 Tipo de input: Selector mltiple construdo con las etiquetas: 
 label : class=" lbl_final_jornada_matutina "  valor : 11:50:00 
 label : class=" lbl_final_jornada_vespertina "  valor : 17:50:00 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad (de por lo menos seleccionar un valor) 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_send_time ={{ input }} 

 Nota: Si hay mltiples selecciones, se guarda un registro por estado seleccionado, similar a como se guardan los registros en eatc_config_labels 

 Botn: registrar correo 
 class=" lbl_registrar_correo " 

 Cuando se oprime el botn, se realizan tambin las siguientes dos capturas automticas: 

 Cuenta maestra (Captura automtica en segundo plano) 
 Descripcin : cuenta maestra desde la cual se hace el registro 
 Tipo de dato: string 
 Tipo de input: se toma automticamente de la variable _DOM. cua_master 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_cua_master ={{ _DOM. cua_master }} 

 Cuenta (Captura automtica en segundo plano) 
 Descripcin : cuenta usuario desde la cual se hace el registro 
 Tipo de dato: string 
 Tipo de input: se toma automticamente de la variable _DOM. cua_user 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_cua_user ={{ _DOM. cua_user }} 

 Fecha y hora del registro (Captura automtica en segundo plano) 
 Descripcin : Fecha y hora en la cual el usuario del BO realiza el registro del correo electrnico. 
 Tipo de dato: datetime (en formato AAAA-MM-DD HH:MM:SS ) 
 Tipo de input: timestamp automtico 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_datetime ={{ timestamp }} 

 Usuario BO (Captura automtica en segundo plano) 
 Descripcin : Usuario del BO (plaraforma EatCloud) que realiz el registro del correo electrnico. 
 Tipo de dato: string 
 Tipo de input: se toma automticamente del dato del usuario del BO que realiza el registro 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_bo_user ={{ input }} 

 PARMETROS PARA LA GENERACIN DEL REGISTRO: 
 parametros_registro : 
 eatc_email ={{ input }} & eatc_state ={{ input }}& eatc_send_time ={{ input }} & eatc_cua_master ={{ _DOM. cua_master }}& eatc_cua_user ={{ _DOM. cua_user }}& eatc_datetime ={{ timestamp }} & eatc_bo_user ={{input}} 

 LLAMADO A CRD PARA ACTUALIZACIN DEL REGISTRO  
 {{ URL_entorno_donantes }}/crd/{{_DOM. cua_master }}/?_tabla= eatc_state_change_emails &_operacion= insert &{{ parametros_registro }} 

 Nota: cada registro tiene un dato individual en los campos: eatc_state y eatc_send_time, por lo tanto en casos con selecciones mltiples se deben hacer mltiples registros, como se realiza en el registro de etiquetas 

 Listado de correos creados 
 La funcionalidad debe mostrar un listado, que consolide, por correo electrnico creado, los datos de estado y hora de corte del correo, es decir, en el listado debe haber un solo registro por correo electrnico creado y arrays de registros en las columnas Estado del anuncio y Hora corte para el envo , de ser el caso.  Este listado debe permitir, borrar y editar registros. A continuacin se muestran los campos para  

 Correo electrnico: 
 class=" lbl_email_reporte_estados " 
 Caracterstica del informe : en la tabla solo se debe mostrar un registro de cada correo registrado (as en la respectiva columna del object store existan muchos registros para el mismo correo) 
 La informacin se obtiene de :  
{{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_email ={{ email }} 

 Estado del anuncio: 
 class=" lbl_estado_anuncio " 
 Caracterstica del informe : se podr mostrar un array de valores, si para este correo existen varios estados registrados que generarn correos electrnicos. 
 La informacin se obtiene de :  
 eatc_state_change_emails. eatc_state de la siguiente consulta {{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_email ={{ email }} 

 Hora de corte para el envo: 
 class=" lbl_hora_corte_envio " 
 Caracterstica del informe : se podr mostrar un array de valores, si para este correo existen varios horarios registrados para un mismo correo electrnico. 
 La informacin se obtiene de :  
 eatc_state_change_emails. eatc_send_time de la siguiente consulta {{URL_entorno_datagov}}/api/eatcloud/ eatc_state_change_emails ? eatc_email ={{ email }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CORREOS PARA CAMBIOS DE ESTADO