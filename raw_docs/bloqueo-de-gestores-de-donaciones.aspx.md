# bloqueo-de-gestores-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para la implementación: se debe revisar si esta funcionalidad ya está implementada en el BO Abaco Legacy (el que se está actualizando con esta nueva versión) y migrar dicha funcionalidad al nuevo BO que se está construyendo 

 M ENÚ LATERAL: BLOQUEO DE GESTORES DE DONACIÓN . 
 Menú principal 
 class= lbl_bloqueo_doma ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_bloqueo_doma )  

 F ORMULARIO DE BLOQUEO 
 Label del título: Bloqueo de gestores de donación (beneficiarios) para cuentas específicas de donantes 
 class=" lbl_titulo_bloqueo_doma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_titulo_bloqueo_doma ) 

 Label de la descripción: 
 class=" lbl_titulo_bloqueo_doma_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_titulo_bloqueo_doma_desc ) 

 "Con esta funcionalidad se podrán bloquear beneficiarios para que no vuelvan a recibir donaciones de un donante específico (por lo general a petición de éste último), pero dejándolos habilitados para recibir donaciones de otros donantes" 

 Formulario de captura 

 Nombre del gestor de donaciones (beneficiario): 
 Place holder: class=" lbl_nombre_doma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre_doma ) 

 Tooltip: class=" lbl_nombre_doma_tooltip " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre_doma_tooltip ) 

 "Digita el nombre del gestor de donaciones (beneficiario) que deseas bloquear para una cuenta específica. El texto predictivo te ayudará" 

 Tipo de dato: string 
 Tipo de input: text input  contexto predictivo 
 De dónde se toma la información para el texto predictivo :  {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?organizacin=_* 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_doma_name ={{ input }} 

 Identificación del gestor de donaciones (beneficiario): 
 Place holder: class=" lbl_id_doma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_id_doma ) 

 Tipo de dato: string 
 Tipo de input: se obtiene a partir de la selección del dato anterior 
 De dónde se toma la información :  del parámetro: eatc_donation_managers. identificador_unico_registro   que se obtiene en la siguiente búsqueda a partir del input anterior: {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?organizacin={{eatc_blocked_doma. eatc_doma_name }} 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_doma_id ={{ input }} 

 Cuenta para la cual se bloquea: 
 Place holder: class=" lbl_cua_bloqueada " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cua_bloqueada ) 

 Tooltip: class=" lbl_cua_bloqueada_tooltip " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cua_bloqueada_tooltip )  

 "Selecciona la cuenta para la cual se bloqueará al beneficiario (lo cual le impedirá seguir recibiendo donaciones de ese donante)" 

 Tipo de dato: string 
 Tipo de input: selector único 
 De dónde se toma la información para el selector :  {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?eatc_cua_master={{_DOM. cua_master }} 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_donor ={{ input }} 

 Causal del bloqueo: 
 Place holder: class=" lbl_causal_bloqueo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo ) 

 Tooltip: class=" lbl_causal_bloqueo_tooltip " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo_tooltip ) 

 "Selecciona la causal por la cual se bloquea al beneficiario para esta cuenta específica" 

 Tipo de dato: string 
 Tipo de input: selector único 
 De dónde se toma la información para el selector :  el label se construye (para su internacionalización) con la información que se obtiene del parámetro " eatc_blocked_doma_causes. eatc_label " de la siguiente consulta {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma_causes?_id=_* (al registro se lleva el valor que se obtiene en  "eatc_blocked_doma_causes. eatc_cause ") 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cause ={{ input }} 

 eatc_cause_id (captura oculta a partir de la anterior selección): 
 Tipo de dato: string 
 Tipo de input: se obtiene  de manera oculta a partir de la selección del dato anterior 
 De dónde se toma la información :  del parámetro: eatc_blocked_doma_causes. eatc_cause_id   que se obtiene en la siguiente búsqueda a partir de la selección anterior {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma_causes? eatc_cause ={{eatc_blocked_doma_causes. eatc_cause }} 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cause_id ={{ input }} 

 Mayor información sobre la causa del bloqueo: 
 Place holder: class=" lbl_causal_bloqueo_info " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo_info ) 

 Tooltip: class=" lbl_causal_bloqueo_info_tooltip " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo_info_tooltip ) 

 "Complementa con mayor información la causa por la cual se ha solicitado bloquear al beneficiario para esta cuenta específica" 

 Tipo de dato: string 
 Tipo de input: Cuadro de texto 
 Valor por defecto: ninguno. 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_note ={{ input }} 

 Botón: registrar bloqueo 
 class=" lbl_registrar_bloqueo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_registrar_bloqueo ) 

 Cuando se oprime el botón, se realizan también las siguientes dos capturas automáticas: 

 Validez del bloqueo (Captura automática en segundo plano) 
 Descripción : constante que le da validez al bloque 
 Tipo de dato: constante (string) 
 Valor (constante): activo 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_validity_block = activo 

 Fecha (Captura automática en segundo plano) 
 Descripción : fecha en la cual se hace el registro 
 Tipo de dato: date (en formato AAAA-MM-DD) 
 Tipo de input: datestamp de cuando se realiza el registro 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_date ={{ datestamp }} 

 Cuenta maestra (Captura automática en segundo plano) 
 Descripción : cuenta maestra desde la cual se hace el registro 
 Tipo de dato: string 
 Tipo de input: se toma automáticamente de la variable _DOM. cua_master 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_cua_master ={{ _DOM. cua_master }} 

 Usuario BO (Captura automática en segundo plano) 
 Descripción : Usuario del BO (plaraforma EatCloud) que realizó el registro del correo electrónico. 
 Tipo de dato: string 
 Tipo de input: se toma automáticamente del dato del usuario del BO que realiza el registro 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma? eatc_bo_user ={{ input }} 

 PARÁMETROS PARA LA GENERACIÓN DEL REGISTRO: 
 parametros_registro : 
 eatc_doma_name ={{ input }}& eatc_doma_id ={{ input }}& eatc_donor ={{ input }}& eatc_cause ={{ input }}& eatc_cause_id ={{ input }}& eatc_note ={{ input }}& eatc_validity_block = activo & eatc_date ={{ datestamp }}& eatc_cua_master ={{ _DOM. cua_master }}& eatc_bo_user ={{input}} 

 LLAMADO A CRD PARA ACTUALIZACIÓN DEL REGISTRO  
{{URL_entorno_datagov}} /crd/eatcloud/?_tabla= eatc_blocked_doma &_operacion= insert &{{ parametros_registro }} 

 Listado gestores de donación bloqueados 

 A este listado, que contendrá los botones modificar la validez del bloqueo (la idea es no borrarlos, para conservar el registro) 

 {URL_entorno_datagov}}/api/eatcloud/eatc_blocked_doma?_id=_* 

 Nombre del gestor de donaciones (beneficiario): 
 Label: class=" lbl_nombre_doma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre_doma ) 
 Muestra la información contenida en eatc_blocked_doma. eatc_doma_name 

 Identificación del gestor de donaciones (beneficiario): 
 label: class=" lbl_id_doma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_id_doma ) 
 Muestra la información contenida en eatc_blocked_doma. eatc_doma_id 

 Cuenta para la cual se bloquea: 
 label: class=" lbl_cua_bloqueada " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cua_bloqueada ) 
 Muestra la información contenida en eatc_blocked_doma. eatc_donor 

 Causal del bloqueo: 
 Label: class=" lbl_causal_bloqueo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo ) 
 Muestra la información contenida en eatc_blocked_doma. eatc_cause 

 Mayor información sobre la causa del bloqueo: 
 Label: class=" lbl_causal_bloqueo_info " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_causal_bloqueo_info ) 
 Muestra la información contenida en eatc_blocked_doma. eatc_note 

 Botón: Suspender el bloqueo: 
 Label: class=" lbl_suspender_bloqueo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_suspender_bloqueo ) 
 Si se acciona este botón, para el registro específico se realiza esta edición de datos: {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_blocked_doma&_operacion=update& eatc_validity_block = inactivo &WHERE_id= {{eatc_blocked_doma. _id }} 

 ***NUEVO: Botón para descargar el listado de gestores de donación bloqueados: *** 
 Incorporar en el listado un botón que permita descargar la información de la tabla visualizada en formato .csv. 

 Envío de correo de bloqueo 
 Cuando se bloquea a un usuario para una cuenta específica, la plataforma deberá enviar de manera automática un correo electrónico a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) en donde se le informa lo siguiente 

 class=" lbl_señores " Señores ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_señores )  

 class=" lbl_bloqueado_por " A partir de la fecha se encuentra bloqueado para recibir donaciones de nuestro donante ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_bloqueado_por )  

 class=" lbl_por_motivo " por motivo de ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_por_motivo )  

 class=" lbl_informacion_bloqueo " Se nos ha informado que ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_informacion_bloqueo )  

 class=" lbl_bloqueo_efectivo_desde " por lo tanto dicho bloqueo se hace efectivo a partir de ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_bloqueo_efectivo_desde )  

 class=" lbl_atentamente " Atento saludo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_atentamente )  

 class=" lbl_equipo " Equipo EatCloud ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_equipo )  

 class="lbl_señores" 
 {{eatc_blocked_doma . eatc_doma_name }} 

 class="lbl_bloqueado_por" {{eatc_blocked_doma . eatc_doma_name }} class="lbl_por_motivo" {{eatc_blocked_doma . eatc_cause }}. class="lbl_informacion_bloqueo" {{eatc_blocked_doma . eatc_note }}, class="lbl_bloqueo_efectivo_desde" {{eatc_blocked_doma . eatc_date }}. 

 class="lbl_atentamente" 
 class="lbl_equipo" EatCloud 

 Es decir: 

 Señores 
 {{eatc_blocked_doma . eatc_doma_name }} 

 A partir de la fecha se encuentra bloqueado para recibir donaciones de nuestro donante {{eatc_blocked_doma . eatc_doma_name }} por motivo de {{eatc_blocked_doma . eatc_cause }}. Se nos ha informado que {{eatc_blocked_doma . eatc_note }}, por lo tanto dicho bloqueo se hace efectivo a partir de {{eatc_blocked_doma . eatc_date }}. 

 Atento saludo. 
 Equipo EatCloud 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 3abe79b7-dd7f-4bb7-adc4-ee3c62dda2fb 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 d94fec26-1966-46d0-a4c3-06f668efc6ed 
 2025-09-17T06:46:52.3070558Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"ae75b14e-3d9c-42bc-92d1-3e39847144b3","SequenceId":483,"FluidContainerCustomId":"9cce1dc2-3f6b-40ee-b85e-c875187e712e","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 BLOQUEO DE GESTORES DE DONACIÓN (BENEFICIARIOS)