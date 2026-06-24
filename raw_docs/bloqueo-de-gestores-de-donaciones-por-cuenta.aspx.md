# bloqueo-de-gestores-de-donaciones-por-cuenta.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Validacin del tipo de licencia para el despliegue de la funcionalidad ***NUEVO : disponible tambin para impactoplus *** 
 Antes de desplegar el formulario, el sistema deber realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM. cua_user }}&_distinct= type 

 Corresponde a eatc_cua. type =impactoplus , eatc_cua. type =impacto eatc_cua. type =activo y en ese caso permitir pasar al formulario de bloqueo. 

 Si la licencia es diferente a impactoplus, impacto   activo (es decir: eatc_cua. type =esencial eatc_cua. type =free ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 

 {{parametros_registro}} 

 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_user_block 
 eatc_user = {{ URL_entorno_donantes }}/api/{{_DOM. cua_user }}/ bo_usuarios? nombre_usuario = {{ bo_usuarios. nombre_usuario }}&_distinct = email 
 eatc_actual_rescue_plan = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =type 

 Llamado al api con los {{parametros_registro}} (en el llamado los parmetros se separan por " & ") 
 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& {{parametros_registro}} 

 Ejemplo: entorno de pruebas, cuenta " abaco ", bo_usuarios. nombre_usuario " abaco ", el " 2021-09-11 14:43:00 " 

 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14:43:00 
 eatc_date = 2021-09-11 
 eatc_country = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =eatc_country = co 
 eatc_cua_master = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_user_block 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = upgrade_by_user_block & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free   

 Redireccin a pgina de upgrade por bloqueo de beneficiarios (gestores de donacin) 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_by_user_block 

 F ORMULARIO DE BLOQUEO 

 Label del ttulo: 
 class=" lbl_titulo_bloqueo_doma " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_titulo_bloqueo_doma )  

 Label de la descripcin: 
 class=" lbl_titulo_bloqueo_doma_desc " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_titulo_bloqueo_doma_desc )  

 Con esta funcionalidad se podrn bloquear beneficiarios para que no vuelvan a recibir donaciones de un donante especfico (por lo general a peticin de ste ltimo), pero dejndolos habilitados para recibir donaciones de otros donantes 

 Formulario de captura 

 Nombre del gestor de donaciones (beneficiario): 
 Place holder: class=" lbl_nombre_doma "  ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_nombre_doma )  

 Tooltip: class=" lbl_nombre_doma_tooltip " (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel=) 
 Tipo de dato: string 
 Tipo de input: text input  contexto predictivo 
 De dnde se toma la informacin para el texto predictivo :  {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?organizacin=_* 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_doma_name ={{ input }} 

 Identificacin del gestor de donaciones (beneficiario): 
 Place holder: class=" lbl_id_doma " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_id_doma )  
 Tipo de dato: string 
 Tipo de input: se obtiene a partir de la seleccin del dato anterior 
 De dnde se toma la informacin :  del parmetro: eatc_donation_managers. identificador_unico_registro   que se obtiene en la siguiente bsqueda a partir del input anterior: {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?organizacin={{eatc_blocked_doma. eatc_doma_name }} 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_doma_id ={{ input }} 

 Causal del bloqueo: 
 Place holder: class=" lbl_causal_bloqueo " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo )  

 Tooltip: class=" lbl_causal_bloqueo_tooltip " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo_tooltip )  
 Tipo de dato: string 
 Tipo de input: selector nico 
 De dnde se toma la informacin para el selector :  el label se construye (para su internacionalizacin) con la informacin que se obtiene del parmetro " eatc_blocked_doma_causes. eatc_label " de la siguiente consulta {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma_causes? eatc_handled_by_donor =y&_distinct= eatc_label (al registro se lleva el valor que se obtiene en  "eatc_blocked_doma_causes. eatc_cause ") 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cause ={{ input }} 

 eatc_cause_id (captura oculta a partir de la anterior seleccin): 
 Tipo de dato: string 
 Tipo de input: se obtiene  de manera oculta a partir de la seleccin del dato anterior 
 De dnde se toma la informacin :  del parmetro: eatc_blocked_doma_causes. eatc_cause_id   que se obtiene en la siguiente bsqueda a partir de la seleccin anterior {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma_causes? eatc_cause ={{eatc_blocked_doma_causes. eatc_cause }}&_distinct= eatc_cause_id 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cause_id ={{ input }} 

 Mayor informacin sobre la causa del bloqueo: 
 Place holder: class=" lbl_causal_bloqueo_info " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo_info )  

 Tooltip: class=" lbl_causal_bloqueo_info_tooltip " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo_info_tooltip )  

 Tipo de dato: string 
 Tipo de input: Cuadro de texto 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_note ={{ input }} 

 Botn: Registrar bloqueo 
 class=" lbl_registrar_bloqueo " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_registrar_bloqueo )  

 Cuando se oprime el botn, se realizan tambin las siguientes dos capturas automticas: 

 Cuenta para la cual se bloquea (Captura automtica en segundo plano): 
 Tipo de dato: string 
 Captura oculta: selector nico 
 De dnde se toma la informacin para el selector :  {{_DOM. cua_user }} 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_donor ={{ input }} 

 Cuenta maestra (Captura automtica en segundo plano): 
 Descripcin : cuenta maestra desde la cual se hace el registro 
 Tipo de dato: string 
 Tipo de input: se toma automticamente de la variable {{ _DOM. cua_master }} 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cua_master ={{ _DOM. cua_master }} 

 Validez del bloqueo (Captura automtica en segundo plano): 
 Descripcin : constante que le da validez al bloque 
 Tipo de dato: constante (string) 
 Valor (constante): activo 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_validity_block = activo 

 Fecha (Captura automtica en segundo plano): 
 Descripcin : fecha en la cual se hace el registro 
 Tipo de dato: date (en formato AAAA-MM-DD) 
 Tipo de input: datestamp de cuando se realiza el registro 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_date ={{ datestamp }} 

 Usuario BO (Captura automtica en segundo plano): 
 Descripcin : Usuario del BO (plaraforma EatCloud) que realiz el registro del correo electrnico. 
 Tipo de dato: string 
 Tipo de input: se toma automticamente del dato del usuario del BO que realiza el registro ({{ URL_entorno_donantes }}/api/{{_DOM. cua_user }}/ bo_usuarios? nombre_usuario = {{ bo_usuarios. nombre_usuario }}&_distinct = email ) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_bo_user ={{ input }} 

 PARMETROS PARA LA GENERACIN DEL REGISTRO: 
 parametros_registro : 

 eatc_doma_name ={{ input }}& eatc_doma_id ={{ input }}& eatc_cause ={{ input }}& eatc_cause_id ={{ input }}& eatc_note ={{ input }}& eatc_validity_block = activo & eatc_date ={{ datestamp }}& eatc_donor ={{ _DOM. cua_user }}& eatc_cua_master ={{ _DOM. cua_master }}& eatc_bo_user ={{ bo_usuarios . email }} 
 LLAMADO A CRD PARA ACTUALIZACIN DEL REGISTRO  
{{URL_entorno_datagov}} /crd/eatcloud/?_tabla= eatc_blocked_doma &_operacion= insert &{{ parametros_registro }} 

 Listado gestores de donacin bloqueados 
 A este listado, que contendr los botones modificar la validez del bloqueo (la idea es no borrarlos, para conservar el registro) 
 {URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma?_id=_* 

 Nombre del gestor de donaciones (beneficiario): 
 Label: class=" lbl_nombre_doma " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_nombre_doma ) 
 Muestra la informacin contenida en eatc_blocked_doma. eatc_doma_name 

 Identificacin del gestor de donaciones (beneficiario): 
 label: class=" lbl_id_doma " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_id_doma ) 
 Muestra la informacin contenida en eatc_blocked_doma. eatc_doma_id 

 Cuenta para la cual se bloquea: 
 label: class=" lbl_cua_bloqueada " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_cua_bloqueada ) 
 Muestra la informacin contenida en eatc_blocked_doma. eatc_donor 

 Causal del bloqueo: 
 Label: class=" lbl_causal_bloqueo " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo ) 
 Muestra la informacin contenida en eatc_blocked_doma. eatc_cause 

 Mayor informacin sobre la causa del bloqueo: 
 Label: class=" lbl_causal_bloqueo_info " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_causal_bloqueo_info ) 
 Muestra la informacin contenida en eatc_blocked_doma. eatc_note 

 Botn: Suspender el bloqueo: 
 Label: class=" lbl_suspender_bloqueo " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_suspender_bloqueo ) 
 Si se acciona este botn, para el registro especfico se realiza esta edicin de datos: {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_blocked_doma&_operacion=update& eatc_validity_block = inactivo &WHERE_id= {{eatc_blocked_doma. _id }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO (Datagov Cuentas) 

 BLOQUEO DE GESTORES DE DONACIN (BENEFICIARIOS)