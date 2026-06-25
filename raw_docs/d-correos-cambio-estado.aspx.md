# d-correos-cambio-estado.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante para el desarrollo 
 Esta funcionalidad deber estar disponible en&#58; BO Donantes.&#160; Dado que en un cercano futuro se pretende migrar el BO a Datagov Cuentas, entonces el desarrollador debe plantearse cmo ser la mejor manera para abordar el desarrollo sin generar muchos reprocesos (una opcin puede ser en primera instancia hacer una implementacin sobre datagov cuentas y luego a partir de la misma la implementacin en el BO Donantes legacy).&#160; Aunque se documenta la funcionalidad como parte del BO de Donantes, se deja igualmente documentados los accesos en el men lateral de Datagov Cuentas , para realizar la incorporacin a dicha plataforma. 

 Generalidades de la funcionalidad 
 Con esta funcionalidad, el usuario Super administrador (Tipo A) podr configurar correos electrnicos, para que (inicialmente) a dos cortes diarios de su eleccin (11&#58;50&#58;00 y 17&#58;50&#58;00) le llegue un correo electrnico con el reporte de los anuncios que en ese momento estn en un determinado estado. Es importante generarle al men y la funcionalidad como tal un id de funcionalidad, para que se pueda perfilar por vertical y tipo de licencia 

 Descripcin de la funcionalidad 
&#160; 
 Ttulo&#58; 
 class=&quot; lbl_config_correos_info_anuncios &quot; 
&#160; 
 Descripcin&#58; 
 class=&quot; lbl_config_correos_info_anuncios_desc &quot; 
&#160; 
 Formulario para la creacin de correos 
&#160; 
 Correo electrnico&#58; 
 Place holder&#58; class=&quot; lbl_email_reporte_estados &quot; 
 Tooltip&#58; class=&quot; lbl_email_reporte_estados_desc &quot; 
 Tipo de dato&#58; email 
 Tipo de input&#58; text input 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad y formato email 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_email =&#123;&#123; input &#125;&#125; 

&#160; 
 Estado del anuncio&#58; 
 Place holder&#58; class=&quot; lbl_estado_anuncio &quot; 
 Tooltip&#58; class=&quot; lbl_estado_anuncio_desc &quot; 
 Tipo de dato&#58; string 
 Tipo de input&#58; Selector mltiple construdo con la etiqueta ( eatc_dona_headers_states. eatc_plural_label ) y el valor ( eatc_dona_headers_states. eatc_code que ser el valor que se lleve al registro) que se obtiene de la siguiente consulta&#58;&#160;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_headers_states?_id=_* 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad (de por lo menos seleccionar un valor) 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_state =&#123;&#123; input &#125;&#125; 
&#160; 
 Nota&#58; Si hay mltiples selecciones, se guarda un registro por estado seleccionado, similar a como se guardan los registros en eatc_config_labels 

&#160; 
 Hora de corte para el envo&#58; 
 Place holder&#58; class=&quot; lbl_hora_corte_envio &quot; 
 Tooltip&#58; class=&quot; lbl_hora_corte_envio_desc &quot; 
 Tipo de dato&#58; hora militar 
 Tipo de input&#58; Selector mltiple construdo con las etiquetas&#58; 
 label &#58; class=&quot; lbl_final_jornada_matutina &quot;&#160; valor &#58; 11&#58;50&#58;00 
 label &#58; class=&quot; lbl_final_jornada_vespertina &quot;&#160; valor &#58; 17&#58;50&#58;00 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad (de por lo menos seleccionar un valor) 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_send_time =&#123;&#123; input &#125;&#125; 
&#160; 
 Nota&#58; Si hay mltiples selecciones, se guarda un registro por estado seleccionado, similar a como se guardan los registros en eatc_config_labels 

&#160; 
 Botn&#58; registrar correo 
 class=&quot; lbl_registrar_correo &quot; 
&#160; 
 Cuando se oprime el botn, se realizan tambin las siguientes dos capturas automticas&#58; 

&#160; 
 Cuenta maestra (Captura automtica en segundo plano) 
 Descripcin &#58; cuenta maestra desde la cual se hace el registro 
 Tipo de dato&#58; string 
 Tipo de input&#58; se toma automticamente de la variable _DOM. cua_master 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_cua_master =&#123;&#123; _DOM. cua_master &#125;&#125; 

&#160; 
 Cuenta (Captura automtica en segundo plano) 
 Descripcin &#58; cuenta usuario desde la cual se hace el registro 
 Tipo de dato&#58; string 
 Tipo de input&#58; se toma automticamente de la variable _DOM. cua_user 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_cua_user =&#123;&#123; _DOM. cua_user &#125;&#125; 

&#160; 
 Fecha y hora del registro (Captura automtica en segundo plano) 
 Descripcin &#58; Fecha y hora en la cual el usuario del BO realiza el registro del correo electrnico. 
 Tipo de dato&#58; datetime (en formato AAAA-MM-DD HH&#58;MM&#58;SS ) 
 Tipo de input&#58; timestamp automtico 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_datetime =&#123;&#123; timestamp &#125;&#125; 

&#160; 
 Usuario BO (Captura automtica en segundo plano) 
 Descripcin &#58; Usuario del BO (plaraforma EatCloud) que realiz el registro del correo electrnico. 
 Tipo de dato&#58; string 
 Tipo de input&#58; se toma automticamente del dato del usuario del BO que realiza el registro 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_bo_user =&#123;&#123; input &#125;&#125; 

&#160; 
 PARMETROS PARA LA GENERACIN DEL REGISTRO&#58; 
 parametros_registro &#58; 
&#160; 
 eatc_email =&#123;&#123; input &#125;&#125; &amp; eatc_state =&#123;&#123; input &#125;&#125;&amp; eatc_send_time =&#123;&#123; input &#125;&#125; &amp; eatc_cua_master =&#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_cua_user =&#123;&#123; _DOM. cua_user &#125;&#125;&amp; eatc_datetime =&#123;&#123; timestamp &#125;&#125; &amp; eatc_bo_user =&#123;&#123;input&#125;&#125; 
 LLAMADO A CRD PARA ACTUALIZACIN DEL REGISTRO&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_state_change_emails &amp;_operacion= insert &amp;&#123;&#123; parametros_registro &#125;&#125; 
&#160; 
 Nota&#58; cada registro tiene un dato individual en los campos&#58; eatc_state y eatc_send_time, por lo tanto en casos con selecciones mltiples se deben hacer mltiples registros, como se realiza en el registro de etiquetas 

 Listado de correos creados 
 La funcionalidad debe mostrar un listado, que consolide, por correo electrnico creado, los datos de estado y hora de corte del correo, es decir, en el listado debe haber un solo registro por correo electrnico creado y arrays de registros en las columnas Estado del anuncio y Hora corte para el envo , de ser el caso.&#160; Este listado debe permitir, borrar y editar registros. A continuacin se muestran los campos para&#160; 
&#160; 
 Correo electrnico&#58; 
 class=&quot; lbl_email_reporte_estados &quot; 
 Caracterstica del informe &#58; en la tabla solo se debe mostrar un registro de cada correo registrado (as en la respectiva columna del object store existan muchos registros para el mismo correo) 
 La informacin se obtiene de &#58;&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_email =&#123;&#123; email &#125;&#125; 

&#160; 
 Estado del anuncio&#58; 
 class=&quot; lbl_estado_anuncio &quot; 
 Caracterstica del informe &#58; se podr mostrar un array de valores, si para este correo existen varios estados registrados que generarn correos electrnicos. 
 La informacin se obtiene de &#58;&#160; 
 eatc_state_change_emails. eatc_state de la siguiente consulta &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_email =&#123;&#123; email &#125;&#125; 

&#160; 
 Hora de corte para el envo&#58; 
 class=&quot; lbl_hora_corte_envio &quot; 
 Caracterstica del informe &#58; se podr mostrar un array de valores, si para este correo existen varios horarios registrados para un mismo correo electrnico. 
 La informacin se obtiene de &#58;&#160; 
 eatc_state_change_emails. eatc_send_time de la siguiente consulta &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_state_change_emails ? eatc_email =&#123;&#123; email &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Donantes 

 CONFIGURACIN DE CORREOS PARA ENVO DE INFORMACIN DE ANUNCIOS POR ESTADO