# b-activación-donation-managers.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Listado de Gestores de Donaciones Inactivos 
 Por defecto se deben mostrar los gestores de donaciones inactivos, permitiendo la visualizacin de sus datos principales 

 [NUEVO] Visualizacin de Gestores de Donacin Activos: 
 Se podr elegir ver a los gestores activos (haciendo la escogencia en un filtro o selector), y sobre los mismos tambin podrn ejercerse labores de inactivacin,  como se ver ms adelante. 

 Consulta de distancia  
 El sistema en una columna pondr la distancia ms cercana a un punto de donacin del gestor en particular.  Al hacer clic se podrn consultar las distancias a todos los puntos de donacin. 

 Edicin de datos del gestor (activacin, inactivacin) 
 Tanto de manera individual (para ello se da clic en el cono de edicin (lpiz) que se encuentra a mano izquierda del registro (columna "Operacin)) como en lote (seleccionando varios registros), se podrn editar los beneficiarios que aparecen el en listado, permitindole al usuario de la funcionalidad realizar lo siguiente: 

 Edicin del estado 
 Un selector mostrar por defecto el estado del gestor escogido.  El usuario podr seleccionar el otro estado segn la circunstancia (activo / inactivo). 

 Envo de correo de activacin 
 Cuando se activa un usuario (es decir, cuando su estado cambia de inactivo, a activo), la plataforma deber enviar de manera automtica un correo electrnico a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) en donde se entregan las instrucciones de operacin de la plataforma.  

 En la siguiente URL se podrn consultar los artes https://app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

 Selector de causal de inactivacin 
 El formulario deber presentar un nuevo selector (que debe aparecer vaco por defecto) en donde el usuario puede seleccionar una causal de inactivacin (este selector solo se podr visualizar si el estado del gestor de donaciones es inactivo).  Las opciones que se podrn seleccionar son las siguientes y a partir de cada una de ellas se deber enviar un correo a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) que ser particular a cada caso. Sera muy adecuado guardar ese causal en la informacin del gestor de donaciones, para futura referencia 

 Institucin con novedad 
 Al seleccionar esta opcin se deber enviar el siguiente correo electrnico: https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20aparecer%20en%20la%20lista%20de%20instituciones%20con%20Novedad.docx?d=wa11adb43aa034c9fa775af04f1bcdd02&csf=1&web=1&e=oanLcd 

 Rut inexistente 
 Al seleccionar esta opcin se deber enviar el siguiente correo electrnico:  
 https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20RUT%20no%20Existe.docx?d=wb31cb82e5cfc4183a32517cc133ec016&csf=1&web=1&e=CMfy2l 

 Documentos no vigentes 
 Al seleccionar esta opcin se deber enviar el siguiente correo electrnico: https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20Documentos%20no%20Vigentes.docx?d=wed6d17d1083e487992022d7e4c64b829&csf=1&web=1&e=GGEglI 

 (***NUEVO***) Bloqueo gestor de donaciones para una cuenta en particular 
 Al seleccionar un Gestor de donaciones, se debe permitir acceder a una funcionalidad mediante el Boton ( class="lbl_bloqueo_doma_cua" ) " Bloquear para una cuenta especfica ". Al presionar el botn se tomarn algunos datos del gestor de donacin (obtenidos de la siguiente consulta) 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{identificador_unico_registro}} 

 y se proporcionarn algunos campos de captura de datos adicionales para realizar un registro en la estructura de datos de Gestores de Donacin Bloqueados ( {{URL_entorno_datagov}}/api/eatcloud/ eatc_blocked_doma ) 

 Fecha del bloqueo 
 La informacin se toma un timestamp de cuando se activa la funcionalidad (en formato AAAA-MM-DD HH:MM:SS) 
 La informacin se lleva a: eatc_blocked_doma . eatc_date 

 Identificador del gestor de donaciones 
 La informacin se toma de: eatc_donation_managers. identificador_unico_registro 
 La informacin se lleva a: eatc_blocked_doma . eatc_doma_id 

 Nombre del gestor de donaciones 
 La informacin se toma de: eatc_donation_managers. organizacin 
 La informacin se lleva a: eatc_blocked_doma . eatc_doma_name 

 Cuenta maestra del gestor de donaciones 
 La informacin se toma de: eatc_donation_managers. eatc_cua_master 
 La informacin se lleva a: eatc_blocked_doma . eatc_cua_master 

 Usuario del bo que realiza el bloqueo 
 La informacin se toma del usuario de la cuenta maestra ( {{URL_entorno_datagov}}/api/{{_DOM. cua_master }}/bo_usuarios?email=_* ) respectiva: bo_usuarios. email 
 La informacin se lleva a: eatc_blocked_doma . eatc_cua_master 

 Validez del bloqueo 
 Como constante se registra " activo " 
 La informacin se lleva a: eatc_blocked_doma . eatc_validity_block 

 Selector de cuenta que bloquea 
 Label : class="lbl_bloqueado_para_el_donante" (Bloqueado para el donante) 
 Tipo de selector: Selector nico 
 El selector se construye : con la informacin que se obtiene de la siguiente consulta: {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?eatc_cua_master={{_DOM. cua_master }} 
 Validaciones : obligatoriedad 
 La informacin se lleva a: eatc_blocked_doma . eatc_donor 

 Selector de causal de bloqueo 
 Label : class="lbl_selecciona_causal_bloqueo" (Selecciona la causal del bloqueo) 
 Tipo de selector: Selector nico 
 El selector se construye : con la informacin que se obtiene de la siguiente consulta: {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma_causes?_id=_* tomando el dato que viene el en campo " eatc_label " y realizando la respectiva internacionalizacin. A partir de la seleccin se toman los datos: 
eatc_blocked_doma_causes. eatc_cause_id para llevarlo a: eatc_blocked_doma . eatc_cause_id 
eatc_blocked_doma_causes. eatc_cause para llevarlo a: eatc_blocked_doma . eatc_cause 
 Validaciones : obligatoriedad 

 Ampla la informacin sobre el bloqueo (cuadro de texto) 
 Label : class="lbl_informacion_bloqueo" (Ampla la informacin sobre el bloqueo) 
 Tipo de campo de captura: cuadro de texto 
 Validaciones : obligatoriedad, saneamiento de caracteres especiales 
 La informacin se lleva a: eatc_blocked_doma . eatc_note 

 Envo de correo de bloqueo 
 Cuando se bloquea a un usuario para una cuenta especfica, la plataforma deber enviar de manera automtica un correo electrnico a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) en donde se le informa lo siguiente 

 class="lbl_seores" 
 {{eatc_blocked_doma . eatc_doma_name }} 

 class="lbl_bloqueado_por" {{eatc_blocked_doma . eatc_doma_name }} class="lbl_por_motivo" {{eatc_blocked_doma . eatc_cause }}. class="lbl_informacion_bloqueo" {{eatc_blocked_doma . eatc_note }}, class="lbl_bloqueo_efectivo_desde" {{eatc_blocked_doma . eatc_date }}. 

 class="lbl_atentamente" 
 class="lbl_equipo" EatCloud 

 Es decir: 

 Seores 
 {{eatc_blocked_doma . eatc_doma_name }} 

 A partir de la fecha se encuentra bloqueado para recibir donaciones de nuestro donante {{eatc_blocked_doma . eatc_doma_name }} por motivo de {{eatc_blocked_doma . eatc_cause }}. Se nos ha informado que {{eatc_blocked_doma . eatc_note }}, por lo tanto dicho bloqueo se hace efectivo a partir de {{eatc_blocked_doma . eatc_date }}. 

 Atento saludo. 
 Equipo EatCloud 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 B ACTIVACIN DONATION MANAGERS