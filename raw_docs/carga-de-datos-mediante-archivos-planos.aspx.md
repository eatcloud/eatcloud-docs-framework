# carga-de-datos-mediante-archivos-planos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Validacin del tipo de licencia para el despliegue de la funcionalidad 
 Antes de desplegar el formulario, el sistema deber realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&_distinct= type 

 Corresponde eatc_cua. type = impacto eatc_cua. type = activo y en ese caso permitir pasar a la funcionalidad de mapeo de datos. 

 Si la licencia es diferente a impacto activo (es decir: eatc_cua. type = esencial eatc_cua. type = free ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 

 {{parametros_registro}} 

 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_flat_file_upload 
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
 eatc_upgrade_event = upgrade_by_flat_file_upload 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = upgrade_by_flat_file_upload & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free   

 Redireccin a pgina de upgrade por archivos planos 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_by_flat_file_upload 

 F UNCIONALIDAD DE CARGA DE DATOS A PARTIR DE ARCHIVOS PLANOS 
 Lo primero que se despliega en esta funcionalidad, es un listado de los posibles maestros que podr cargar la cuenta que son aquellos que cuentan con un mapa previamente creado con la respectiva funcionalidad 
 . 
 Label del ttulo: Carga de datos 
 class=" lbl_titulo_carga_datos " (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_titulo_carga_datos )  

 Label de la descripcin: 
 class=" lbl_carga_datos_desc " (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_mapeo_datos_desc )   

 "Con esta funcionalidad podrs cargar informacin de diversos maestros (previamente mapeados) a partir de archivos planos.  Sigue los pasos que a continuacin de describimos, para realizar dicha carga de informacin." 

 1. Selector del maestro a cargar 
 Label del ttulo del selector: Seleccione el maestro a cargar 
 class=" lbl_seleccione_maestro_a_cargar " (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_seleccione_maestro_a_cargar ) 

 1.1. Construccin del selector de maestros a cargar: 
 El sistema armar un selector con el resultado de la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &_distinct= eatc_objectstore 

 Los posibles valores que se obtienen de esta consulta, a saber: 
 { 
 eatc_objectstore : "eatc_dona" 
 }, 
 { 
 eatc_objectstore : "eatc_odds" 
 }, 
 { 
 eatc_objectstore : "eatc_pods" 
 } 

  Estn configurados como labels, entonces el sistema debe arma un selector con los siguientes valores (en idioma espaol): 

 Detalles de anuncios de donacin ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=es&pais=_*&idlabel=eatc_dona )  
 Maestro de productos (artculos) donables ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=es&pais=_*&idlabel=eatc_odds )  
 Maestro de puntos de donacin ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=es&pais=_*&idlabel=eatc_pods )  

 Si la consulta 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &_distinct= eatc_objectstore 

 no arroja un resultado vlido o genera un resultado vaco, el sistema deber desplegar el siguiente label: 
 class=" lbl_sin_mapa_preparado " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_sin_mapa_preparado )   "En la actualidad no cuentas con un mapa de datos preparado. Consulta con tu ejecutivo de cuenta EatCloud" 

 1.1. Validacin de un mapa configurado ante un "maestro seleccionado para ser cargado": 
 Una vez el usuario selecciona un valor {{eatc_data_map. eatc_objectstore }}, el sistema debe realizar la siguiente consulta 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}&_distinct= eatc_equivalent 

 Si la consulta no arroja un resultado vlido o genera un resultado vaco, el sistema deber desplegar el siguiente label: 

 class=" lbl_sin_mapa_configurado " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_sin_mapa_configurado )   "En la actualidad no cuentas con un mapa de datos configurado para el maestro seleccionado. Por favor dirgete a la funcionalidad respectiva para hacerlo" 

 Y mostrar el botn: "Ir a mapeo de datos" 
 class=" lbl_ir_a_mapeo " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_ir_a_mapeo ) 

 El botn deber llevar a la funcionalidad " Mapeo de datos " 

 2. Cargador de archivos 
 class=" lbl_cargar_fuente_datos_desc " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_cargar_fuente_datos_desc )  

 "A continuacin debes proveer un archivo en formato .csv o .xlsx, que contenga en la primera fila el nombre de las respectivas columnas de datos y que corresponda a la estructura de datos previamente mapeada, que contiene por lo menos las columnas:" 

 El sistema debe mostrar las columnas que aparecen a partir de la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}&_distinct= eatc_equivalent 

 Selector de separadores de campo ( Se deja a criterio del desarrollador la implementacin de este selector, dado que se podra obviar con la realizada durante el mapeo y aqu simplemente se utiliza la definida all, o simplemente la que contenga el archivo => Si es una selecci) 
 class=" lbl_selecciona_separador_desc " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_selecciona_separador_desc ) 

 Selecciona el carcter que es utilizado para separar las respectivas columnas de datos en el archivo que ests cargando. 

 class=" lbl_selecciona_separador " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_selecciona_separador ) 
 El sistema deber mostrar en selector de posibles separadores de datos de archivos planos, para que  el usuario determine cul es, y el sistema lo utilice para determinar las diversas columnas de datos 
 ; 
 tab 
 pipe 

 A continuacin, el sistema deber presentar un botn que permita cargar el archivo de datos respectivo (file picker): 
 class=" lbl_cargar_fuente_datos " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_cargar_fuente_datos )  "Cargar fuente de datos estndar" 

 Una vez el usuario seleccione el archivo a cargar, el sistema lo procesar como se indica a continuacin. 

 3. Procesamiento previo de datos de la fuente de datos 
 Validaciones previas a la carga del archivo 

 El sistema debe validar que el archivo est bien formateado (formato de archivo, separadores, que tenga datos en la primera fila diferentes a los datos de las filas subsiguientes), y que los valores del vector de encabezados del archivo cargado, correspondan a las equivalencias mapeadas: 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}&_distinct= eatc_equivalent 

 De acuerdo a las validaciones, si las mismas no fueron exitosas, se debern presentar los siguientes labels (que pueden aparecer en modales o toast)  y que al aceptarlos el usuario retornarn a la funcionalidad del cargador de archivos (file picker), para realizar el respectivo reintento. 

 class=" lbl_archivo_mal_formateado " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_archivo_mal_formateado ) 

 "El archivo que acabas de cargar est mal formateado. Por favor revisa que la extensin del mismo sea la adecuada, que tenga el nombre de las columnas en la primera fila.  Intntalo de nuevo. 

 [Aceptar (class=lbl_aceptar)] 

 class=" lbl_no_corresponde_al_mapa " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_no_corresponde_al_mapa )  

 "El archivo que acabas de cargar no corresponde al mapa de datos previamente configurado. Por favor revisa el nombre de las columnas en la primera fila (que sean "exactamente el mismo" al definido en el mapa) e intntalo de nuevo." 

 [Aceptar (class=lbl_aceptar)] 

 Selector del tipo de carga  
 Este selector solo se habilita para los maestros: 

 Maestro de productos (artculos) donables ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=es&pais=_*&idlabel=eatc_odds )  
 Maestro de puntos de donacin ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=es&pais=_*&idlabel=eatc_pods )  

 Para el maestro de detalle de anuncios de donacin siempre se realizar carga tipo delta (sin borrar datos anteriores). 

 class=" lbl_selector_tipo_carga_desc " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_selector_tipo_carga_desc )  

 "A continuacin podrs seleccionar si deseas borrar todos los datos del maestro para volverlos a cargar de nuevo, o simplemente deseas cargar una porcin nueva de datos, preservando todos los datos previamente cargados." 

 Selector tipo de carga: 

 class=" lbl_selector_tipo_carga " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_selector_tipo_carga )  

 El sistema presenta un selector nico, con las siguientes opciones: 

 class=" lbl_bulk " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_bulk ) 
 class=" lbl_delta " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_delta )  

 3. Procesamiento de datos de la fuente de datos 
 Si las validaciones son correctas, y el archivo de datos cumple con los requisitos para ser cargado, entonces el sistema procede a realizar las respectivas transformaciones y enriquecimientos, para luego subirlos en las respectivas estructuras definitivas para el sistema, a saber: 

 eatc_objectstore : "eatc_dona" => {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona 
 eatc_objectstore : "eatc_odds" => {{ URL_entorno_donantes }}/api/{{_DOM. cua_user }}/eatc_odds 
 eatc_objectstore : "eatc_pods" => {{ URL_entorno_donantes }}/api/{{_DOM. cua_user }}/eatc_pods 
 eatc_objectstore : "eatc_pods" => {{ URL_entorno_donantes }}/api/allpods/eatc_pods 

 Transformaciones 
 El sistema deber llamar los datos subidos, como su correspondiente equivalente 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}& eatc_parameter ={{eatc_data_map. eatc_parameter }}&_distinct= eatc_equivalent 

 Constantes 
 El sistema tomar los datos contenidos en el registro: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}& eatc_parameter ={{eatc_data_map. eatc_parameter }}& eatc_requiered = y &_distinct= eatc_constant_formula 

 o 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}& eatc_parameter ={{eatc_data_map. eatc_parameter }}& eatc_requiered = y &_distinct= eatc_constant_value 

 Para establecer las constantes para este tipo de carga, con lo cual se indica que correspondern a un mismo valor para todos los datos que se cargan a partir de un mismo archivo. 

 El sistema deber validar que todos los campos que sean requeridos ( eatc_data_map. eatc_requiered = y ), y que tengan una frmula o un valor constante, sean llevados al archivo que se va a cargar definitivamente. 

 NOTA PARA EL PROGRAMADOR: se deber evaluar si las notaciones utilizadas para las frmulas requeridas para generar las constantes (eatc_data_map. eatc_constant_formula ), son las ms adecuadas para generarlas de manera automtica (leyendo de la persistencia). De no serlo se sugiere cambiar los datos almacenados en la respectiva persistencia (eatc_data_map. eatc_constant_formula ) para tener una notacin ms adecuada para esta automatizacin. 

 Variables 
 El sistema tomar los datos contenidos en el registro: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_cua={{_DOM. cua_user }}&eatc_platform= bo &eatc_objectstore={{eatc_data_map. eatc_objectstore }}& eatc_parameter ={{eatc_data_map. eatc_parameter }}& eatc_requiered = y &_distinct= eatc_variable_formula 

 Para establecer las variables que debern generarse como datos. 

 El sistema deber validar que todos los campos que sean requeridos ( eatc_data_map. eatc_requiered = y ), y que tengan una frmula para el clculo de variable, sean llevados al archivo que se va a cargar definitivamente. 

 NOTA PARA EL PROGRAMADOR: se deber evaluar si las notaciones utilizadas para las frmulas requeridas para generar las variables (eatc_data_map. eatc_ variable _formula ), son las ms adecuadas para generarlas de manera automtica (leyendo de la persistencia). De no serlo se sugiere cambiar los datos almacenados en la respectiva persistencia (eatc_data_map. eatc_ variable _formula ) para tener una notacin ms adecuada para esta automatizacin. 

 4. Carga de datos 
 Una vez se realicen las transformaciones, se construyan las constantes y las variables, el sistema puede utilizar los servicios para la carga de informacin a partir de archivos planos a saber: 

 eatc_objectstore : "eatc_dona" => {{ URL_entorno_donantes }}/mstr/{{_DOM. cua_master }}/eatc_dona 
 eatc_objectstore : "eatc_odds" => {{ URL_entorno_donantes }}/mstr/{{_DOM. cua_user }}/eatc_odds 
 eatc_objectstore : "eatc_pods" => {{ URL_entorno_donantes }}/mstr/{{_DOM. cua_user }}/eatc_pods 
 eatc_objectstore : "eatc_pods" => {{ URL_entorno_donantes }}/mstr/allpods/eatc_pods 

 5. Mensaje de xito 
 Una vez se carguen de manera correcta los registros el sistema deber desplegar los siguientes labels y la siguiente informacin. 
 class=" lbl_cargados_con_exito_un_total " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_cargados_con_exito_un_total )  

 "Se han cargado con xito un total de:" 

 [ numero_registros_cargados ] 

 class=" lbl_registros_cargados " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_registros_cargados )  

 "Registros" 

 6. Mensaje de error 
 Si se produce algn error en la carga de la informacin el sistema debe desplegar el siguiente label. 
 class=" lbl_error_carga_datos " ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_error_carga_datos ) 

 "Se produjo un error en la carga de datos. Por favor intntalo de nuevo." 

 [Aceptar (class=lbl_aceptar)] 

 Y se retorna a la pantalla de carga del archivo plano 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CARGA DE DATOS (MEDIANTE ARCHIVOS PLANOS)