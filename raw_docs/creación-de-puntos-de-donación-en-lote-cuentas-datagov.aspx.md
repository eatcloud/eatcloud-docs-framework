# creación-de-puntos-de-donación-en-lote-cuentas-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Validacin del tipo de licencia para el despliegue de la funcionalidad 
 Antes de desplegar el formulario (botn colapsible para subida de archivos planos), el sistema deber realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&_distinct= type 

Nota: 
Cuando se inicia sesin en datgov_cuentas el tipo de licencia se obtiene del localStorage, para el requisito seria as: localStorage . getItem ( ' licencia ' ) == ' impacto ' || localStorage . getItem ( ' licencia ' ) == ' activo ' 

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

 Nota: En el cdigo los datos anteriores se pueden obtener del localStorage y de funciones, de la siguiente manera 
 " _tabla " : " eatc_upgrade_events " , 
                 " _operacion " : " insert " , 
                 " eatc_datetime " : fn_get_datetime () . datetime , 
                 " eatc_date " : fn_get_datetime () . date , 
                 " eatc_country " : localStorage . getItem ( ' pais ' ) , 
                 " eatc_cua_master " : localStorage . getItem ( ' cua_master ' ) , 
                 " eatc_cua " : localStorage . getItem ( ' cua_user ' ) , 
                 " eatc_platform " : ' datagov_cuentas ' , 
                 " eatc_upgrade_event " : ' upgrade_by_flat_file_upload ' , 
                 " eatc_user " : localStorage . getItem ( ' email ' ) , 
                 " eatc_actual_rescue_plan " : localStorage . getItem ( ' licencia ' ) 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = upgrade_by_flat_file_upload & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free   

 Redireccin a pgina de upgrade por archivos planos 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/ upgradebyflatfiles 

 BOTN COLAPSIBLE PARA DESPLEGAR FORMULARIO PARA SUBIDA DE ARCHIVOS PLANOS 
 Mockup propuesto: 

 Botn colapsible "Agregar en lote mediante archivo plano": 
 class=" lbl_agregar_en_lote " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_agregar_en_lote )  

 Al presionar el botn se deber descolapsar un formulario para la carga de los puntos de la donacin que contendr la siguiente informacin: 

 Descarga archivo de muestra  (csv /xls) : 
 class=" lbl_descarga_archivo_muestra " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_descarga_archivo_muestra )  

 Debe funcionar similar a como se implement en la primera versin. 

 Mensaje introductorio para descarga de muestra y llenado de archivo: 
 class=" lbl_intro_subida_pods_fl_file " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_intro_subida_pods_fl_file )   

 "Si deseas cargar puntos de donacin mediante archivo plano, descarga el anterior archivo y llnalo con la siguiente informacin de los puntos de donacin a crear:" 

 Listado de campos obligatorios (con sus respectivas descripciones): 
 El sistema deber realizar la siguiente consulta para mostrarle al usuario (mediante sus respectivos labels) los campos o columnas obligatorias a llenar ( eatc_parameter_lbl ) y su respectiva descripcin ( eatc_descripcion_lbl ): 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_map ?eatc_objectstore=eatc_pods&eatc_cua=default&eatc_platform= datagov_cuentas &eatc_requiered=y&_cmp=eatc_parameter_lbl,eatc_descripcion_lbl 

 Mensaje final: 
 class=" lbl_fin_subida_pods_fl_file " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_fin_subida_pods_fl_file)  

 "Recuerda que no puedes incluir en el archivo un punto de donacin previamente creado." 
 _________ 

 Seleccionar archivo: 
 class=" lbl_seleccionar_archivo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_seleccionar_archivo )  

 Debe funcionar similar a como se implement en la primera versin. 

 No se eligi archivo: 
 class=" lbl_no_eligio_archivo " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_no_eligio_archivo )   

 Debe funcionar similar a como se implement en la primera versin. 

 Botn: "Cargar informacin" 
 class=" lbl_cargar_informacion " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_cargar_informacion)   

 Debe funcionar similar a como se implement en la primera versin. 

 Labels de validaciones 
 - No se pudieron validar puntos repetidos. Por favor contacta a la mesa de servicio. 
 class=" lbl_sin_validacion_pods_repetidos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_sin_validacion_pods_repetidos )    

 - Identificadores repetidos: {{id1,id2,id3}} 
 class=" lbl_identificadores_repetidos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_identificadores_repetidos )   

 - Carga exitosa! {{cantidad}} puntos agregados. 
 class=" lbl_carga_exitosa " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_carga_exitosa ) 

 {{cantidad}} 
 class=" lbl_puntos_agregados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_puntos_agregados )   

 - Algunos datos no son vlidos. Por favor corrgelos y vuelve a subir el archivo. (este label tiene que ver con que enven un campo no vlido o falte un campo en el archivo). 
 class=" lbl_algunos_datos_invalidos " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_algunos_datos_invalidos )    

 - Tu licencia rescate no permite cargar ms puntos. Para ms informacin comuncate con nuestra mesa de servicio. 
 class=" lbl_limite_licencia_rescate_carga_pods " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel=lbl_limite_licencia_rescate_carga_pods )  

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreaci%C3%B3n-de-puntos-de-donaci%C3%B3n-en-lote-cuentas-datagov%2F2521978876-pods_flat_file_datagov_donantes.jpg&ow=1280&oh=775, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreaci%C3%B3n-de-puntos-de-donaci%C3%B3n-en-lote-cuentas-datagov%2F2521978876-pods_flat_file_datagov_donantes.jpg&ow=1280&oh=775 

 346.000000000000 

 CREACIN DE PUNTOS DE DONACIN EN LOTE - CUENTAS DATAGOV