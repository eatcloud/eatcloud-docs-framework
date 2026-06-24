# activación-beneficiarios.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ACTIVACIÓN (BENEFICIARIOS) ","showTimeToRead":false,"encodedImage":"BBR:HGxufQ~qj[fQ"},"containsDynamicDataSource":false}">

 En esta funcionalidad que es homóloga en su parte operativa gruesa, a la que está implementada actualmente en el BO Abaco para activar y desactivar organizaciones, se incluye como novedad una franja de indicadores que pretende entregar información sobre el estado de actividad del ecosistema en su punta de rescate. 

 T ÍTULO: ACTIVACIONES 

 label: class="lb_activaciones": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_activaciones     

 Descripción: "En esta sección encontrarás el estado de los gestores de donaciones en EatCloud" 

 label: class="lb_activaciones_desc": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_activaciones_desc 

 E STADO GENERAL DE LOS GESTORES DE DONACIONES 

 label: class="lb_estado_gral_doma": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_estado_gral_doma   

 Cards de indicadores generales 
 Instituciones inscritas (doma_inscritas): 
 label: class="lb_doma_inscritas": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_inscritas   

 La información se toma de la siguiente consulta (todas las organizaciones registradas a excepción de las marcadas en eatc_state= persona_natural ) 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =suspendido,activo,inactivo,"" &_cont 

 Porcentaje 
Siempre será (100%) 

 Instituciones activas (doma_activas) 
 label: class="lb_doma_activas": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_activas 

 La información se toma de la siguiente consulta (las organizaciones con estado eatc_state= activo ) 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers eatc_state =activo &_cont 

 Porcentaje 
 (doma_activas/doma_inscritas) * 100 

 Instituciones inactivas (doma_inactivas) 
 label: class="lb_doma_inactivas": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_inactivas   

 La información se toma de la siguiente consulta (las organizaciones con estado eatc_state= inactivo ) 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers eatc_state =inactivo &_cont 

 Porcentaje 
 (doma_inactivas / doma_inscritas) * 100 

 Instituciones suspendidas (doma_suspendidas) 
 label: class="lb_doma_suspendidas": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_suspendidas 

 La información se toma de la siguiente consulta (las organizaciones con estado eatc_state= suspendido ) 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers eatc_state =suspendido &_cont 

 Porcentaje 
 (doma_suspendidas/doma_inscritas) * 100 

 E STADO ESPECÍFICO DE LAS INSTITUCIONES 
 label: class="lb_estado_esp_doma": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_estado_esp_doma    

 Filtro de fechas 

 Filtro: "El mes actual" = > Valor por defecto 
 class=" lbl_mes_actual " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_mes_actual )  

 Filtro: "Personalizar" 
 class=" lbl_personalizar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_personalizar )  

 id=" lbl_fecha_inicial " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_fecha_inicial )  

 id=" lbl_fecha_final " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_fecha_final )  

 class=" lbl_consultar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_consultar ) 

 Cards de indicadores específicos 
 Instituciones inscritas: 
 Label: class="lb_doma_inscritas": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_inscritas 

 Tooltip: class="lb_doma_inscritas_desc": Gestores de donación (instituciones beneficiarias) que se inscribieron en el periodo seleccionado en la plataforma EatCloud 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_inscritas_desc   

 La información se toma de la siguiente consulta (todas las organizaciones registradas en el periodo a excepción de las marcadas en eatc_state= persona_natural ) 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? fecha1 [0] = {{ fecha_inicial }}& fecha1 [1] = {{ fecha_final }}&eatc_state =suspendido,activo,inactivo,expulsado,"" &_cont 

 Instituciones con actividad: 
 Label: class="lb_doma_con_actividad": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_con_actividad 

 Tooltip: class="lb_doma_con_actividad_desc": Gestores de donación (instituciones beneficiarias) que han gestionado por lo menos una donación en el periodo seleccionado 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_doma_con_actividad_desc 

 La información se toma de la siguiente consulta (el cont de la siguiente consulta) 
{{ URL_entorno_donantes }}/api/{{_DOM. cua_master }} /eatc_dona_headers? eatc-publication_date [0] = {{ fecha_inicial }}& eatc-publication_date [1] = {{ fecha_final }}&_distinct= eatc-donation_manager_name 

 NOTA: en una primera etapa de implementación solo se colocarán estos dos indicadores en la franja de indicadores específicos de actividad 

 L ISTADO DE GESTORES DE DONACIONES 
 Label: class="lb_listado_doma": 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_listado_doma   

 Por defecto se deben mostrar los gestores de donaciones inactivos, permitiendo la visualización de sus datos principales 

 Listado paginado y ordenado 
 Se deben utilizar las funciones de paginado y ordenamiento definidas para las consultas (si las mismas no funcionan como están en la documentación se deberá contactar a Jesús Ramírez para la revisión de las funciones y su despliegue en los ambientes "beneficiario": dev y producción), con el ánimo de construir un listado paginado (con 20 resultados máximo por página) y ordenado por el campo que se estipula más adelante . Se puede implementar la paginación como una segunda etapa de la funcionalidad y también se puede reutilizar código que se utilizó en la funcionalidad de la nueva WAPP Donantes " Listado de donaciones " (implementado por Jean) y la funcionalidad de la APP beneficiarios " Mis donaciones " (implementada por Iván). 

 Filtro de estados 
 Para obtener los estados que se desplegarán en un selector único como criterios de filtro, se debe realizar la siguiente consulta: 
{{ URL_entorno_datagov }} /api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master= {{_DOM. cua_master }}&_distinct=eatc_state_lbl 

 ***NUEVO: filtro con selección múltiple de estados *** 
 En la actualidad el filtro funciona con selección única y una opción de todos los estados.  A partir de la fecha el filtro deberá funcionar con selección múltiple de los estados y la opción “todos” debe marcar todas las opciones.  Esto principalmente se debe desarrollar para permitir la descarga del informe de la tabla incorporando varios estados (como por ejemplo “activo” y “pasivo”: que el listado de organizaciones con estos dos estados puedan descargarse en un mismo archivo). 

 ***NUEVO: cambian los estados *** 
 Ejemplo : cua_master: abaco , ambiente de pruebas 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master= abaco&_distinct=eatc_state_lbl    

 A los filtros que se obtienen en la consulta, se les deberá adicionar la opción " Todos ", como se indica más adelante 

 Filtro: "Todos" =>Filtro por defecto ***NUEVO: cambian los estados *** 
 class=" lbl_todos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_todos ) 

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista (todos los gestores de donaciones): 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state = inscrito,en_activacion,rechazado ,activo, pasivo , suspendido,expulsado, 

 Anteriormente: 
 {{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =suspendido,activo,inactivo,expulsado, 

 DEPRECADO: Filtro: "Inactivo" (ANTERIORMENTE ERA EL FILTRO POR DEFECTO: el nuevo filtro será " Todos ") 
 class=" lbl_inactivo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_inactivo )   

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
 {{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =inactivo 

 Ejemplo: ambiente de pruebas, cuenta maestra: abaco 
 Por defecto el sistema deberá realizar la siguiente consulta: 

 https://devbeneficiarios.eatcloud.info/api/abaco /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =inactivo   

 Con los registros obtenidos, se debe construir el listado que más abajo se especifica. 
 ***NUEVO: Filtro: "En activación" *** 
 class=" lbl_en_activacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_en_activacion )  

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state = en_activacion 

 ***NUEVO: Filtro: "En activación" *** 
 class=" lbl_en_activacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_en_activacion )  

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state = en_activacion 

 ***NUEVO: Filtro: "Rechazado" *** 
 class=" lbl_rechazado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_rechazado )  

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =rechazado 

 Filtro: "Activo" 
 class=" lbl_activo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_activo )  

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =activo 

 ***NUEVO: Filtro: "Pasivo" *** 
 class=" lbl_pasivo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_pasivo )  

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =pasivo 

 Filtro: "Suspendido" 
 class=" lbl_suspendido " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_suspendido )   

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =suspendido 

 Filtro: "Expulsado" 
 class=" lbl_expulsado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_expulsado )   

 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista: 
{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_state =expulsado 

 Botón: "Descargar" 
 class=" lbl_descargar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_descargar )  

 Al presionar este botón se descargarán los datos de la siguiente lista según el criterio de filtro aplicado. 

 Listado de Gestores de Donaciones 
 El listado estará compuesto por las siguientes columnas 

 Nombre de la organización: 
 class=" lbl_nombre_organizacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_nombre_organizacion )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . organizacin 

 NIT: 
 class=" lbl_identificacion_tributaria " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_identificacion_tributaria )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . identificador_unico_registro 

 Tipo organización: 
 class=" lbl_tipo_organizacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_tipo_organizacion )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . tipo_organizacion 

 Estado: 
 class=" lbl_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_estado )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . eatc_state 

 Ciudad: 
 class=" lbl_ciudad " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_ciudad )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . municipio 

 Último cambio (no está en el diseño): => Se debe ordenar por esta columna, mostrando primero las instituciones beneficiarias con cambios más recientes . 
 class=" lbl_ultimo_cambio " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_ultimo_cambio )  

 Mostrará la información contenida en el parámetro: eatc_donation_managers . fecha2 

 Causal cambio estado (en el diseño: Causal inactividad): 
 class=" lbl_causal_cambio_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_causal_cambio_estado ) 

 Mostrará la información contenida en el parámetro: eatc_donation_managers . causal_inactivo 

 Ver detalles: 
 class=" lbl_ver_detalles " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_ver_detalles )  

 En cada registro mostrará un vínculo a la próxima pantalla de la funcionalidad, que permitirá ver los detalles del gestor de donaciones y editar tu estado (activar, inactivar, suspender o expulsar una organización).  Al hacer clic en un " Ver detalles " particular,  con el código del beneficiario seleccionado ( eatc_donation_managers . identificador_unico_registro ) el sistema deberá realizar la siguiente consulta con el fin de obtener los datos requeridos para la siguiente vista: 

{{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = {{eatc_donation_managers . identificador_unico_registro }} 

 Ejemplo : entorno  de pruebas, cuenta maestra Abaco , identificador_unico_registro = 900326456   

El sistema realiza la siguiente consulta: 

 https://devbeneficiarios .eatcloud.info /api/abaco/ eatc_donation_managers? identificador_unico_registro = 900326456     

 Con los datos obtenidos de la consulta se procede a pintar los datos de la siguiente pantalla o funcionalidad. 

 D ETALLES DEL GESTOR DE DONACIONES 
 Detalle de activación: Edición de datos del gestor (activación, inactivación, suspensión, expulsión) 
 class=" lbl_detalle_activacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_detalle_activacion ) 

 En esta vista se podrán ver los detalles básicos del gestor de donaciones y poder realizar labores de activación / inactivación / suspensión / expulsión.  La información que se muestra en la vista es la siguiente: 

 Datos básicos del Gestor de donaciones 
 En la parte izquierda de la pantalla se presentarán los siguientes datos de la institución sobre la cual se abre la funcionalidad 

 Nombre de la institución: Mostrará la información contenida en el parámetro:   {{eatc_donation_managers . organizacin }} 

 NIT: Mostrará la información contenida en el parámetro: {{ eatc_donation_managers .identificador_unico_registro }} 

 Representante legal: Mostrará la información contenida en el parámetro: {{eatc_donation_managers . representante_legal }} 

 Correo electrónico: Mostrará la información contenida en el parámetro: {{eatc_donation_managers . correo_electronico }} (con programación de vínculo mailto: para envío de correo al hacerle clic) 

 Teléfono 1: Mostrará la información contenida en el parámetro: {{eatc_donation_managers . telefono1 }} 

 Estado (selector único de estado) 
 class=" lbl_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_estado )  

 Valor por defecto: 
 El selector mostrará por defecto el siguiente valor: tomando el dato que se encuentra registrado en el parámetro: {{eatc_donation_managers . eatc_state }} 

{{ URL_entorno_datagov }}/api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master={{_DOM. cua_master }}& eatc_state_code= {{eatc_donation_managers . eatc_state }}&_distinct=eatc_state_lbl 

 Ejemplo : entorno  de pruebas, cuenta maestra Abaco , para una institución beneficiaria cuyo eatc_donation_managers . eatc_state=inactivo   

El sistema realiza la siguiente consulta: 

 https://dev. datagov.eatcloud.info /api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master=abaco& eatc_state_code= inactivo&_distinct=eatc_state_lbl 

Dado que la respuesta es: 
 res :  [{ eatc_state_lbl : "lbl_inactivo" } ] 

Entonces en el selector se debe desplegar como valor por defecto (a partir de las funciones de internacionalización propias del sistema para el idioma español): 
 Inactivo ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_inactivo ) 

 Demás valores del selector único: 
 Para obtener los otros estados que se desplegarán en un selector único como criterios de filtro, se debe realizar la siguiente consulta: 
{{ URL_entorno_datagov }} /api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master= {{_DOM. cua_master }}&_distinct=eatc_state_lbl 

 Ejemplo : entorno  de pruebas, cuenta maestra Abaco 

El sistema realiza la siguiente consulta: 

 https://dev. datagov.eatcloud.info /api/eatcloud/eatc_doma_states?active_status=y&eatc_cua_master=abaco&_distinct=eatc_state_lbl   

Dado que la respuesta es: 
 res : [ { eatc_state_lbl : "lbl_activo" },{ eatc_state_lbl : "lbl_inactivo" },{ eatc_state_lbl : "lbl_suspendido" },{ eatc_state_lbl : "lbl_expulsado" } ] 

Entonces el selector podrá tener las siguientes opciones (a partir de las funciones de internacionalización propias del sistema para el idioma español): 

 Activo ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_activo ) 
 Inactivo ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_inactivo ) 
 Suspendido ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_suspendido ) 
 Expulsadoo ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_expulsado )  

 Cuándo se cambia a un estado diferente al estado por defecto: 
 El sistema deberá guardar en una variable el nuevo_estado ( eatc_doma_states. eatc_state_lbl ) y desplegará el siguiente formulario para adicionarle información concerniente al cambio realizado: 

 Confirmación de cambio de estado (Formulario de edición de estado): 
 class=" lbl_confirmacion_cambio_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_confirmacion_cambio_estado ) 

 Retorna a la vista anterior sin hacer ningún cambio y coloca en el campo estado el valor por defecto determinado anteriormente (deshace la selección realizada y que envió al presente formulario de confirmación). 

 Generación de código del registro de historial (captura oculta) 
 El sistema deberá generar un código para el presente registro de historial, que deberá ser único y se deberá guardar en la variable " eatc_code " para su posterior registro. 

 Fecha (captura oculta) 
 El sistema deberá capturar un datestamp (en formato AAAA-MM-SS ) y guardarlo en la variable " eatc_date " para su posterior registro. 

 Usuario del BO que realiza el cambio de estado (captura oculta) 
 El sistema deberá tomar el dato " email " contenido en la estructura " bo_usuarios " de la respectiva cuenta maestra (entorno beneficiarios: ejemplo para ambiente de pruebas: https://devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&_distinct=email )  y llevarlo  " eatc_bo_user " para su posterior registro. 

 ¿Deseas cambiar el estado estado_actual a nuevo_estado ? 

 ¿Deseas cambiar el estado:  
 class=" lbl_deseas_cambiar_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_deseas_cambiar_estado ) 

 estado_actual : corresponde al valor por defecto del selector de estado, descrito anteriormente . 

 a  

 class=" lbl_to " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_to ) 

 nuevo_estado : corresponde a la respectiva variable como se indicó anteriormente . 

 ?: se puede quemar en el código 

 Estado => NO VA 
 Se considera que no debe ir, dado que en anterior letrero se muestra. 

 Causal de cambio de estado (selector único) 
 Place holder: 
 class=" lbl_causal_cambio_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_causal_cambio_estado )  

 Valor por defecto para selector: 
 Ninguno (es decir, debe mostrar el place holder) 

 Valores que puede desplegar el selector: 
 Con el dato previamente obtenido como  nuevo_estado ( eatc_doma_states. eatc_state_lbl )  el sistema deberá realizar la siguiente consulta: 

{{ URL_entorno_datagov }} /api/eatcloud/eatc_doma_state_change_causes?eatc_cua_master= {{_DOM. cua_master }} &active_status=y&eatc_change_to_state_lbl= {{eatc_doma_states. eatc_state_lbl }}&_distinct= eatc_cause_code 

 Con los valores que arroja la consulta al servicio (que están configurados como labels) se arma el selector. 

 Ejemplo : Ambiente de pruebas, _DOM. cua_master =abaco nuevo_estado=lbl_inactivo 

 Si en la vista anterior el usuario eligió la opción " lbl_inactivo " entonces el sistema debe realizar la siguiente consulta: 

 https://dev.datagov.eatcloud.info /api/eatcloud/eatc_doma_state_change_causes?eatc_cua_master= abaco &active_status=y&eatc_change_to_state_lbl= lbl_inactivo &_distinct= eatc_cause_code   

 Dado que el sistema responde: 

 res :  
 [ 
 { eatc_cause_code : “documentos_incompletos” }, 
 { eatc_cause_code : "sin_cert_constitucion" }, 
 { eatc_cause_code : "incompleto_cert_camara_ccio" }, 
 { eatc_cause_code : "incompleto_rut" }, 
 { eatc_cause_code : "incompleto_decreto_constitucion" }, 
 { eatc_cause_code : "incompleto_cert_icbf" }, 
 { eatc_cause_code : "rut_no_vigente" }, 
 { eatc_cause_code : "cert_camara_ccio_no_vigente" }, 
 { eatc_cause_code : "institucion_con_novedad" } 
 ], 

 Entonces el selector contendrá los siguientes valores (para el idioma " es " , utilizando sus funciones de internacionalización ): 

 Documentos incompletos ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= documentos_incompletos ) 
 Incompleto Certificado de Constitución ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= sin_cert_constitucion ) 
 .... 
 Institución con novedad ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= institucion_con_novedad )   

 Validación para el selector: 
 El formulario deberá validar que se escoja un valor de causal para cambio de estado (no se puede dejar sin selección ni con el placeholder). 

 Valor seleccionado se lleva: 
 Se debe guardar en una variable ( {{ eatc_doma_state_change_causes. eatc_cause_code }} ) para posteriormente realizar los respectivos registros. 

 Observaciones (cuadro de captura de texto) 
 Place holder: 
 class=" lbl_observaciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_observaciones ) 

 Valor por defecto para el cuadro de texto: 
 Ninguno (es decir, debe mostrar el place holder) 

 Validación para el cuadro de texto: 
 El formulario deberá validar que se agregue una observación. 

 El texto digitado se lleva: 
 Se debe guardar en una variable ( eatc_notes ) para posteriormente realizar los respectivos registros. 

 Adjuntar documentos de evidencias/soportes (opcional) 
 Place holder: 
 class=" lbl_adjuntar_soportes " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_adjuntar_soportes )  

 Botón: "Adjuntar nuevo documento" 
 class=" lbl_adjuntar_nuevo_documento " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_adjuntar_nuevo_documento )  

 Archivos de máximo 3 Megas (no está en el diseño) 

 Como indicación para la subida de documentos se debe colocar el siguiente label 
 class=" lbl_doc_maximo_peso " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_doc_maximo_peso )  

 Validación para la subida de documentos: 

 Ninguna, dado que es un campo opcional.  Si se adjunta, el documento no debe pesar más de 3 Megas.  En caso que pese más de 3 megas se debe desplegar el siguiente mensaje: 

 class=" lbl_documento_pesado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_documento_pesado ) 

 "El documento adjunto sobrepasa el peso máximo estipulado. Por favor inténtalo de nuevo con un archivo más liviano" 

 El documento adjunto se sube a la plataforma: 

 Asociado al código del registro en el historial , se debe subir el documento a la plataforma (nombrándolo como se deba para identificarlo adecuadamente en el sistema de archivos definido para este fin: eatc_doc_name ) y deberá guardar también la URL desde la cuál se recupera el archivo adjunto ( eatc_doc_url ).  Se recomienda que el sistema de archivos definido para este fin posea carpetas por días.  Con los datos de eatc_doc_name y eatc_doc_url se realizará el registro en la tabla ( {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_state_change_docs?eatc_doma_state_change_code=_* ) donde se guardará la relación entre el código del caso de cambio de estado en el historial y el documento subido a la plataforma.  Se podrán adjuntar varios documentos a un mismo caso. 

 Botón: Confirmar: 
 class=" lbl_confirmar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_confirmar )  

 Al presionar este botón el sistema debe tomar un estampe de tiempo en formato (en formato AAAA-MM-SS HH:MM:SS) y guardarlo en la variable " eatc_datetime " para su posterior registro.  También al oprimir el botón el sistema deberá realizar los siguientes registros con la respectiva información del cambio de estado, tal como se muestra a continuación: 

 Registro de la información del cambio de estado: 
 El sistema deberá realizar actualización de información en la tabla de beneficiarios ( {{ URL_entorno_beneficarios }}/api/{{_DOM. cua_master }} /eatc_donation_managers? identificador_unico_registro = _*&eatc_identificador_unico_registro =_* ), en la tabla de historial de cambio de estados ( {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_state_change_history?eatc_code=_* )  y en la tabla de documentos soporte del cambio de estado ( {{URL_entorno_datagov}}/api/eatcloud/eatc_doma_state_change_docs?eatc_doma_state_change_code=_* ) con las variables capturadas en las anteriores funcionalidades de la siguiente manera: 

 Actualización de datos del beneficiario en eatc_donation_managers 
 El sistema deberá realizar la siguiente actualización de datos 

 {{ URL_entorno_beneficarios }}/crd/{{_DOM. cua_master }} / ?_tabla= eatc_donation_managers &_operacion= update & eatc_state={{ nuevo_estado }}&fecha2={{ eatc_datetime }}&causal_inactivo= {{ eatc_doma_state_change_causes. eatc_cause_code }} &WHERE identificador_unico_registro = {{ eatc_donation_managers .identificador_unico_registro }} 

 Creación de registro en en eatc_doma_state_change_history 
 El sistema deberá realizar la siguiente actualización de datos 

 {{ URL_entorno_datagov }}/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &_operacion= insert & eatc_code= {{ eatc_code }} &eatc_date= {{ eatc_date }} &eatc_datetime= {{ eatc_datetime }} &eatc_cua_master= {{_DOM. cua_master }} &eatc_doma_code = {{ eatc_donation_managers .identificador_unico_registro }}&eatc_bo_user= {{ eatc_bo_user }} &eatc_doma_prev_state= {{ estado_actual }} &eatc_doma_new_state= {{ nuevo_estado }} &eatc_cause_code= {{ eatc_doma_state_change_causes. eatc_cause_code }} &eatc_notes= {{ eatc_notes }} 

 Creación de registro(s) en en eatc_doma_state_change_docs 
 El sistema deberá realizar la siguiente actualización de datos, una por cada documento adjunto. 

 {{ URL_entorno_datagov }}/crd/eatcloud / ?_tabla= eatc_doma_state_change_docs &_operacion= insert & eatc_doma_state_change_code= {{ eatc_code }} &eatc_doc_name= {{ eatc_doc_name }} &eatc_doc_url= {{ eatc_doc_url }} 

 ***NUEVO: Cuando se "suspende", "inactiva" o "expulsa" a un beneficiario: liberación de donaciones pendientes de gestión por parte del beneficiario. *** 
 El sistema deberá consultar las donaciones que están pendientes de gestión por parte del beneficiario suspendido, mediante la siguiente consulta. 

 {{ URL_entorno_donantes }}/api/{{ _DOM.cua_master }} / eatc_dona_headers & eatc-donation_manager_code= {{ eatc_donation_managers .identificador_unico_registro }}&eatc-state=awarded,scheduled&_cmp=eatc-code, eatc_cua_master,eatc-donor,eatc-state,eatc-pod_id 

 Con la consulta se obtiene un array de códigos de anuncios de donación.  Según sea el caso (o estado al cual se cambia) se definen las siguientes constantes: 

 eatc_dona_release_cause: lbl_liberacion_por_suspension_manual_beneficiario / lbl_liberacion_por_inactiviacion_manual_beneficiario / lbl_liberacion_por_expulsion_manual_beneficiario 

 Con los parámetros de la consulta y la constante definida, se realizan invocaciones al servicio de liberación de donaciones , de acuerdo a la documentación respectiva . 

 ***NUEVO: Cuando se "suspende", "inactiva" o "expulsa" a un beneficiario: Borrado de registro de asignación directa *** 
 Cuando se suspende, inactiva, o expulsa a un beneficairio, el sistema deberá borrar los registros de programación directa que estén asociados a la organización suspendida. 

 El sistema deberá realizar la siguiente operación de borrado de registros de asignación directa: 
 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla=eatc_direct_dona&_operacion=delete&WHERE eatc-donation_manager_code = {{ eatc_doma_id }} 

 Mensajes para informar sobre el proceso 
 Los siguientes mensajes se deberán ir desplegando al usuario a medida que progresa el proceso de edición de datos y registro de datos, para mantenerlo informado del progreso y resultado del proceso (puede ser mediante toast por ejemplo) 

 Mensaje que se despliega mientras el proceso se está ejecutando: "Actualizando datos de la institución beneficiaria" 
 class=lbl_actualizando_doma ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_actualizando_doma )    

 Mensaje actualización fallida, reintento: "Error al actualizar datos de la institución beneficiaria, reintentando..." 
 class=lbl_actualizando_doma_reintento ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_actualizando_doma_reintento )    

 Mensaje actualización exitosa: "Datos de la institución beneficiaria exitosamente editados" 
 class=lbl_actualizando_doma_exito ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_actualizando_doma_exito )   

 Mensaje actualización fallida (definitiva: después de tres reintentos): "No pudimos actualizar los datos de la institución beneficiaria" 
 class=lbl_actualizando_doma_falla ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_actualizando_doma_falla )    

 Este mensaje debe mostrar la opción de realizar el reintento, desplegando un vínculo en el toast con el siguiente label: 

 class=lbl_reintentar ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_reintentar )    

 Y que funcione de manera similar al botón " confirmar " arriba descrito .  La idea con esto es que el usuario no salga de la pantalla de actualización del estado hasta que no exista un registro exitoso en todos las tablas requeridas 

 Redirección ante actualización exitosa 
 Cuando se efectúe una actualización exitosa, el sistema debe retornar a la vista de detalle de la institución en cuestión de la presente funcionalidad. En dicha vista, en el listado del respectivo historial se debe visualizar el registro actualmente realizado y el estado por defecto de la institución, por efecto de la actualización de datos en eatc_donation_managers , debe ser el nuevo estado. 

 Envío de correos ante cambios de estados preestablecidos 
 En la actual funcionalidad del BO Abaco ya se tiene implementado esto (la idea es utilizar dicha implementación en la fase inicial para posteriormente refinarla) y con ello se han estipulado una serie de correos proforma que se envían cuando se realiza un cambio de estado y que en este caso se enviarán inicialmente para algunos casos particulares  

 nuevo_estado=activo ***NUEVO: cambio en el contenido del correo electrónico *** 

 Cuando se activa un usuario (es decir, cuando su estado cambia a activo ), la plataforma deberá enviar de manera automática un correo electrónico a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) en donde se entregan las instrucciones de operación de la plataforma.  

 Este es el correo a enviar: 

 Bienvenido a Eatcloud. 

 Cumpliste con los requisitos para usar Eatcloud. Ahora, entra a la Aplicacion Movil con tu usuario y contraseña. 

 Te compartimos los videos de capacitacion: 

 ¿Como descargar mi nueva App Beneficiarios?: 
 https://youtu.be/qQSm3EVFd4Y 

 ¿Como configurar mi nueva App Beneficiarios ?: 
 https://youtu.be/QLodWKuPeRM 

 Gestiona tus donaciones en 4 pasos: 
 https://youtu.be/3LHOrOZrUGU 

 ¿Como elegir una donación?: 
 https://youtu.be/txNOkIgqUeE 

 ¿Como programar una donación?: 
 https://youtu.be/aJsHwQXl33Q 

 ¿Como recoger una donación?: 
 https://youtu.be/L2g01jlb2dE 

 ¿Como Verificar una donación?: 
 https://youtu.be/JXd43x-ZPIs 

 ¿Como calificar a tu donante?: 
 https://youtu.be/QZz4Jxcudwg 

 ¿Como editar los datos de programación en una donación?: 
 https://youtu.be/oj68X8vuOzQ 

 ¿Como reportar un problema de recolección al momento de la entrega?: 
 https://youtu.be/6-5oCORQouY 

 DEPRECADO: No olvides apoyarte en los videos tutoriales ( https://www.eatcloud.com/tutoriales-eatcloud/ ) para rescatar muchos alimentos con nosotros. 

 En la siguiente URL se podrán consultar los artes https://app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

 Institución con novedad 
 eatc_cause_code= {{ eatc_doma_state_change_causes. eatc_cause_code }}= institucion_con_novedad 

 Al seleccionar esta causal de cambio de estado ( institucion_con_novedad ) se deberá enviar el siguiente correo electrónico: https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20aparecer%20en%20la%20lista%20de%20instituciones%20con%20Novedad.docx?d=wa11adb43aa034c9fa775af04f1bcdd02&csf=1&web=1&e=tMZMZ3 

 a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) 

 Rut inexistente 
 eatc_cause_code= {{ eatc_doma_state_change_causes. eatc_cause_code }}= sin_rut 

 Al seleccionar esta esta causal de cambio de estado ( sin_rut ) se deberá enviar el siguiente correo electrónico:  
 https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20RUT%20no%20Existe.docx?d=wb31cb82e5cfc4183a32517cc133ec016&csf=1&web=1&e=qqADlY 

 a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) 

 Documentos no vigentes 
 eatc_cause_code= {{ eatc_doma_state_change_causes. eatc_cause_code }}= rut_no_vigente,cert_camara_ccio_no_vigente 

 Al seleccionar cualquiera de estos dos causales de cambio de estado ( rut_no_vigente,cert_camara_ccio_no_vigente ) se deberá enviar el siguiente correo electrónico: https://eatcloudcorp.sharepoint.com/:w:/r/sites/EatCloud2/Documentos%20compartidos/Mensaje%20de%20la%20No%20activaci%C3%B3n%20por%20Documentos%20no%20Vigentes.docx?d=wed6d17d1083e487992022d7e4c64b829&csf=1&web=1&e=J72SMb 

 a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) 

 nuevo_estado=suspendido 

 Cuando se suspende una institución (es decir, cuando su estado cambia a suspendido ), la plataforma deberá enviar de manera automática un correo electrónico a eatc_donation_managers. correo_electronico   y eatc_users. correo_electronico (si ambas direcciones son diferentes) en donde se entregan las instrucciones de operación de la plataforma.  

 El correo tiene la siguiente estructura, incluyendo vínculos a otra información (por favor revisar los vínculos para programarlos como href; más adelante se colocan los respectivos labels): 
 Hola 

 {{ NOMBRE ORGANIZACIÓN }}  

 ¡Oh! El sistema te suspendió. 

 ¿Conoces los términos de uso y requisitos para usar EatCloud?  

 Por favor escribe por chat a la mesa de servicios ( +57 305 2423193 ). Ellos te responderán y te darán un número de ticket. Luego, escribe un correo electrónico a documentos@eatcloud.com y en el asunto coloca: SOLICITUD DE ACTIVACIÓN + El NÚMERO DE TICKET ASIGNADO POR LA MESA DE SERVICIOS . Si sigues estos pasos, obtendrás una respuesta rápida.  

 Gracias por tu comprensión.  

 Equipo EatCloud 

 Labels 
 Hola (class=lbl_hola https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_hola )  

 {{ eatc_donation_managers. organizacin }}  

 ¡Oh! El sistema te suspendió. ( class=lbl_susp_sistema https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_susp_sistema ) 

 ¿Conoces los términos de uso y requisitos para usar EatCloud? ( class=lbl_conoces_terminos https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_conoces_terminos ) 

 términos de uso y requisitos para usar EatCloud?  

 Por favor escribe por chat a la mesa de servicios (+57 305 2423193). Ellos te responderán y te darán un número de ticket. Luego, escribe un correo electrónico a documentos@eatcloud.com y en el asunto coloca: SOLICITUD DE ACTIVACIÓN + El NÚMERO DE TICKET ASIGNADO POR LA MESA DE SERVICIOS . Si sigues estos pasos, obtendrás una respuesta rápida.  

 Gracias por tu comprensión.  

 Equipo EatCloud 

 ***PENDIENTE DE REVISIÓN: NO TENERLO EN CUENTA PARA EL DESARROLLO INICIAL*** 
 Estamos muy felices de continuar juntos rescatando alimentos. Al día de hoy hemos entregado más de 15 millones de kilos de comestibles a los colombianos. Este logro se debe a ustedes y a nuestros donantes. ¡Vamos por más! 
 Para continuar con esta labor conjunta, solicitamos el envío de la cámara de comercio y RUT de tu organización con expedición igual o menor a 90 días. Debes enviar la documentación al correo electrónico documentos@eatcloud.com en los próximos 15 días. 

 En caso de no recibir los documentos en el plazo especificado, se procederá a inactivar la organización. 
 ¡Esperamos seguir contando con ustedes! 

 EatCloud, más alimentos con hogar y menos hogares sin alimentos 

 Documentos: Funcionalidad para subida y consulta de documentos jurídicos 
 class=lbl_documentos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_documentos )   

 En el diseño está esta propuesta 

 La idea es implementar, de la mano de funcionalidades ya desarrolladas, una funcionalidad para subir documentos jurídicos y otra para consultar 

 Subida de documentos jurídicos 

 Se debe reciclar el código de la funcionalidad implementada en el formulario de Onboarding de Beneficiarios, y que permite esta subida de documentos jurídicos: 

 https://devbeneficiarios.eatcloud.info/_registro/index.html?abaco 

 https://beneficiarios.eatcloud.info/_registro/index.html?abaco   

 Consulta de documentos jurídicos 

 Se debe reciclar el código de la funcionalidad implementada en el BO Beneficiarios Abaco ( https://beneficiarios.eatcloud.info/bo/abaco )  en la funcionalidad de activación , y que permite consultar los documentos jurídicos previamente subidos por el formulario de Onboarding 

 Historial de cambios (lista que muestra el registro del historial de cambios en la vista de detalle de la institución) 

 class=" lbl_historial_cambios " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_historial_cambios )  

  Consulta para construcción de la tabla 
 El sistema deberá realizar la siguiente consulta, para presentar la tabla de datos respectiva: 

 {{ URL_entorno_datagov }}/api/eatcloud /eatc_doma_state_change_history ? eatc_cua_master= {{_DOM. cua_master }} &eatc_doma_code = {{ eatc_donation_managers .identificador_unico_registro }} 

 A partir de la respuesta de la anterior consulta, se muestran los resultados en las siguientes columnas: 

 Listado paginado y ordenado => Puede implementarse en una segunda etapa 
 Se deben utilizar las funciones de paginado y ordenamiento definidas para las consultas (si las mismas no funcionan como están en la documentación se deberá contactar a Jesús Ramírez para la revisión de las funciones y su despliegue en los ambientes "beneficiario": dev y producción), con el ánimo de construir un listado paginado (con 20 resultados máximo por página) y ordenado por el campo que se estipula más adelante . Se puede implementar la paginación como una segunda etapa de la funcionalidad y también se puede reutilizar código que se utilizó en la funcionalidad de la nueva WAPP Donantes " Listado de donaciones " (implementado por Jean) y la funcionalidad de la APP beneficiarios " Mis donaciones " (implementada por Iván). 

 Botón: "Filtro" => Puede implementarse en una segunda etapa 
 class=" lbl_filtro " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_filtro )   

 Al presionar este botón se deberá generar filtro por diversos aspectos presentes en la tabla (se puede utilizar las funciones de filtro propias por ejemplo del "Datatables" para implementar este filtro. 

 Botón: "Descargar" 
 class=" lbl_descargar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_descargar )  

 Al presionar este botón se descargarán los datos de la siguiente lista según el criterio de filtro aplicado. 

 Fecha de cambio: => Se debe ordenar por esta columna, mostrando primero los registros de cambio de estado más recientes . 
 class=" lbl_fecha_cambio " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_fecha_cambio ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_datetime 

 Estado inicial: 
 class=" lbl_estado_inicial " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_estado_inicial ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_doma_prev_state 

 Nuevo estado: 
 class=" lbl_nuevo_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_nuevo_estado ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_doma_new_state 

 Causal de cambio de estado: 
 class=" lbl_causal_cambio_estado " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_causal_cambio_estado ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_cause_code 

 Usuario: 
 class=" lbl_usuario " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_usuario ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_bo_user 

 Observaciones: 
 class=" lbl_observaciones " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_observaciones ) 

 Muestra el dato consignado en: 
 eatc_doma_state_change_history . eatc_notes 

 Documentos soporte: 
 class=" lbl_docs_soporte " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_docs_soporte ) 

 El sistema realiza la siguiente consulta para cada registro en el historial: 
 {{ URL_entorno_datagov }}/api/eatcloud /eatc_doma_state_change_docs ? eatc_doma_state_change_code= {{ eatc_code }} 

 Muestra con los datos guardados : 
 eatc_doma_state_change_docs . eatc_doc_url 
 eatc_doma_state_change_docs . eatc_doc_name 

 Uno o varios vínculos para descargar los documentos adjuntos al registro particular del historial 

 Botón: "Cerrar" 
 class=" lbl_cerrar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_cerrar ) 

 Al presionar este botón se retorna a la vista anterior de " Listado de gestores de donaciones " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Factivaci%C3%B3n-beneficiarios%2F3626312696-detalle_doma_2.jpg&ow=797&oh=652, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Factivaci%C3%B3n-beneficiarios%2F3626312696-detalle_doma_2.jpg&ow=797&oh=652 
 Nuevo BO CUA MASTER Beneficiarios 

 603.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 9ce0c5e4-92d3-4ce3-8ef8-812091508357 
 3!1!2 
 https://southcentralus0-1.pushfp.svc.ms/fluid 
 14768e58-fa84-47eb-ae19-edcec5345e2b 
 2026-05-27T05:30:56.4428268Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"8e3c25af-520d-4187-98b2-c3d4578f42c0","SequenceId":104,"FluidContainerCustomId":"2509d134-c069-44be-8bb3-d8935beaff74","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-05-26T21:33:19.6854381Z"}] 

 ACTIVACIÓN (BENEFICIARIOS)