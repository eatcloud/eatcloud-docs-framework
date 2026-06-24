# configura-tu-plan-y-facturación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin: en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 ID Funcionalidad (no es necesario programarlo) 
 cnf_pl_fc_datagov_cua ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= cnf_pl_fc_datagov_cua ) 

 Esta funcionalidad debe estar siempre visible para cualquier tipo de licencia rescate / analytics 

 WIREFRAME PROPUESTO 

 Consulta del tipo de licencia para despliegue de "warning" (no est en el wireframe) 
 En la parte superior de la vista, el sistema debe mostrar un anuncio o alerta, visible, si alguna de las consultas abajo descritas arroja resultados. Si ninguna de las consultas arrojan resultados, no se muestra la alerta 

 El sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua? name ={{_DOM.cua_user }} 

 type=free 

 Si el type=free el sistema deber  desplegar el siguiente warning 
 lb_cnf_pl_fc_datagov_cua_free_wrn ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_pl_fc_datagov_cua_free_wrn )  

 Label Botn Men: 
 class=lbl_tu_plan_y_facturacion ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_tu_plan_y_facturacion )  

 Encabezado y descripcin 
 En la parte superior de la vista, el sistema debe mostrar un anuncio o alerta, visible, si alguna de las consultas abajo descritas arroja resultados. Si ninguna de las consultas arrojan resultados, no se muestra la alerta 

 Label Ttulo de la Vista: 
 class=lbl_tu_plan_y_facturacion ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_tu_plan_y_facturacion ) 

 Label Descripcin de la Vista (No est en el diseo): 
 id=lb_cnf_pl_fc_datagov_cua_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_pl_fc_datagov_cua_desc ) 

 Botn: "Upgrade EatCloud" 
 class=lbl_upgrade_eatcloud ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_upgrade_eatcloud )  
 Al hacer clic en el botn, el sistema realizar dos acciones: Registro del evento de upgrade y redireccin a pgina de upgrade por accin directa. 

 Registro evento de upgrade 
 Al hacer clic en el botn, se debe capturar un evento de upgrade debe ser registrado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 
 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade 
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
 eatc_upgrade_event = upgrade 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event =upgrade& eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free 

 Redireccin a pgina de upgrade 
 El sistema redireccionar a: 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_rescue_plan 

 CARDS DE INFORMACIN DE LICENCIAS 

 Licencias EatCloud: 
 class=lbl_licencias_eatcloud ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_licencias_eatcloud )  

 Card: Licencia Rescate 
 Licencia Rescate: Plan (concat) {{Plan_rescate}} 
 class=lbl_licencia_rescate_plan ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_licencia_rescate_plan )  

 {{plan_rescate}} 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =type  

 Con el resultado de la anterior consulta se realiza la siguiente para mostrar el label correspondiente 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_types_of_licenses?eatc_code={{eatc_cua. type }}&_distinct= eatc_name_lbl 

 Ejemplo: entorno de pruebas, cuenta ara 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ara &_distinct =type    = impacto 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses?eatc_code=impacto&_distinct= eatc_name_lbl   

 por lo tanto en la interfaz deber aparecer el label: lbl_impacto 

 Ver caractersticas 
 class=lbl_ver_caracteristicas ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_ver_caracteristicas )   

 El vnculo debe direccionar a un popup window que muestre las siguientes caractersticas (labels): 

 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_details_of_licenses? eatc_licence_code = {{eatc_cua. type }} 
 & eatc_implemented =y& eatc_additional_info =n & _distinct = eatc_detail_description_lbl 

 Ejemplo: entorno de pruebas, cuenta ara 

 Dado el anterior ejemplo, la consulta sera: 

 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_details_of_licenses? eatc_licence_code= impacto & eatc_implemented =y& eatc_additional_info =n & _distinct =eatc_detail_description_lbl   

 A 22 e agosto de 2021, el sistema deber desplegar 7 labels ( lbl_activo_ast_mas hasta lbl_usuarios_administradores_ilimitados ) que contendrn la descripcin del plan en el idioma respectivo 

 Tienes activos (concat) {{puntos_donacion_activos}} (concat) puntos de donacin 
 class=lbl_tienes_activos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_tienes_activos )   

 {{puntos_donacion_activos}} 
 {{ URL_entorno_donantes }}/api/allpods/eatc_pods?eatc_active=y&eatc-cua={{_DOM. cua_user }}& _cont 

 Ejemplo: entorno de pruebas, cuenta ara 
 La consulta sera: 
 https://devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&eatc-cua= ara & _cont por lo tanto el nmero de pods a mostrar ser de 273 

 class=lbl_pods ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_pods )  

 Tu plan actual est en el rango de.... => NO VA 
 Botn: Cambiar plan 
 class=lbl_cambiar_plan ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_cambiar_plan )    

 AL presionar el botn el sistema deber realizar dos operaciones: 

 REGISTRO DE EVENTO DE UPGRADE 
 Se debe capturar cuando se oprime este botn como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin (eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 

 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = change_rescue_plan 
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
 eatc_upgrade_event = change_rescue_plan 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = change_rescue_plan & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free 

 REDIRECCIN A PGINA DE UPGRADE 

 El sistema deber redirigir a la pgina: 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_rescue_plan 

 Tu prxima fecha de facturacin ser el (concat) {{fecha_facturacion}} 
 class=lbl_tu_proxima_fecha_facturacin (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_licencia_rescate_plan )  

 {{fecha_facturacion}} 
 Si eatc_cua. type_period ({{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = type_period ) = lbl_mensual : el primer da del prximo mes 
 Si eatc_cua. type_period ({{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = type_period ) = lbl_anual_ahoras_15pc : => PENDIENTE POR DEFINIR . 

 ***NUEVO: Burbuja de alerta en el botn "Cambiar Plan" con informacin al hacer clic en la burbuja*** 
 Al lado del botn "Cambiar licencia" debe aparecer una burbuja con un nmero, como se muestra en el siguiente grfico 

 Y que funcionar de la siguiente manera: 

 Nmero (#) a mostrar en la burbuja 
 Con el dato de la cuenta usuario, y el tipo actual de la cuenta (eatc_cua. type ) El sistema debe realizar la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_upgrade_events ?eatc_cua={{_DOM. cua_user }}&eatc_actual_rescue_plan={{eatc_cua. type }}&eatc_upgrade_event= eatc_pods_limit , eatc_dona_x_pod_mes_limit , eatc_bo_users_limit , upgrade_by_flat_file_upload , upgrade_by_direct_dona , upgrade_by_user_block , upgrade_rescue_plan &_cont 

 El nmero con el que responde el servicio ser el que se pinte en la burbuja (#) 

 Ejemplo: ambiente de pruebas, cuenta colombia 
 Como la cuenta colombia tiene como type: free , entonces la consulta es la siguiente: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_upgrade_events?eatc_cua=colombia&eatc_actual_rescue_plan=free&eatc_upgrade_event=eatc_pods_limit,eatc_dona_x_pod_mes_limit,eatc_bo_users_limit,upgrade_by_flat_file_upload,upgrade_by_direct_dona,upgrade_by_user_block,upgrade_rescue_plan 

 Por lo tanto ( a 9 de septiembre de 2021 ) el nmero que se pinta en la burbuja es " 3 " (este valor puede cambiar si se realizan pruebas de las funcionalidades) 

 Card: EatCloud Analytics 

 Licencia Data Analytics (concat) {{licencia_analytics}} 
 class=lbl_licencia_data_analytics ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_licencia_data_analytics )  

 {{licencia_analytics}} 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_data_analytics_cua? eatc_cua ={{_DOM. cua_user }}&_distinct = eatc_data_analytics_code   

 Con el resultado de la anterior consulta se realiza la siguiente para mostrar el label correspondiente 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_data_analytics_licences?eatc_code={{ eatc_data_analytics_cua . eatc_data_analytics_code }}&_distinct= eatc_label  

 Ejemplo: entorno de pruebas, cuenta ara 
 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua? eatc_cua = ara &_distinct =eatc_data_analytics_code = 360 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_data_analytics_licences?eatc_code= 360 &_distinct= eatc_label   

 por lo tanto en la interfaz deber aparecer el label: lbl_360 

 Ver caractersticas 
 class=lbl_ver_caracteristicas ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_ver_caracteristicas )   

 El vnculo debe direccionar a un popup window que muestre el siguiente label: 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_data_analytics_licences?eatc_code={{ eatc_data_analytics_cua . eatc_data_analytics_code }}&_distinct= eatc_description_label 

 Ejemplo: entorno de pruebas, cuenta ara 

 Dado el anterior ejemplo, la consulta sera: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_data_analytics_licences?eatc_code= 360 &_distinct= eatc_description_label   

 A 22 e agosto de 2021, el sistema deber desplegar el label: lbl_360_desc 

 Botn: Cambiar licencia 
 class=lbl_cambiar_licencia ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_cambiar_licencia )    

 AL presionar el botn el sistema deber realizar dos operaciones: 

 REGISTRO DE EVENTO DE UPGRADE 

 Se debe capturar cuando se oprime este botn como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin (eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 

 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = change_eatcloud_analytics 
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
 eatc_upgrade_event = change_eatcloud_analytics 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = change_eatcloud_analytics & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free 

 REDIRECCIN A ***NUEVO : Informacin de planes analytics *** 
 El sistema deber redirigir la pgina de " informacin de planes analytics " 

 Tu prxima fecha de facturacin ser el (concat) {{fecha_facturacion}} 
 class=lbl_tu_proxima_fecha_facturacin ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_tu_proxima_fecha_facturacin )   

 {{fecha_facturacion}} 
 Si eatc_cua. type_period ({{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = type_period ) = lbl_mensual : el primer da del prximo mes 
 Si eatc_cua. type_period ({{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = type_period ) = lbl_anual_ahoras_15pc : => PENDIENTE POR DEFINIR . 

 HISTORIAL DE FACTURACIN 
 Label: class=" lbl_historial_facturacion " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_historial_facturacion )  

 El sistema deber establece cual es el eatc_customer. erp_id de el respectivo cliente  ( Para mayor informacin revisar la  documentacin para consultar datos de la tabla eatc_customers que guarda datos encriptados ) y con ese valor y las instrucciones que se entregan en la documentacin del ERP (y las respectivas credenciales de acceso), se hace el siguiente llamado: 

 curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET  https://api.alegra.com/api/v1/invoices/?start=0&limit=30&order_direction=DESC&order_field=date&client_id= {{eatc_customers .erp_id }} -u 'usuario@alegra.com: mitoken ' 
 Es decir: 
 curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET  https://api.alegra.com/api/v1/invoices/?start=0&limit=30&order_direction=DESC&order_field=date&client_id= {{eatc_customers .erp_id }} -u 'diana.alvarez@eatcloud: 6505f78dbfb7dfb38bfe ' 

 Ejemplo: Postobn en ambiente de pruebas: 

 Dado que eatc_customers .erp_id para el caso de Postobn es 2, (https://dev.datagov.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_customers&fieldname=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email&filterfield_1=_id&filtervalue_1=17 ) entonces la consulta que se debe realizar es la siguiente: 
 curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET  https://api.alegra.com/api/v1/invoices/?start=0&limit=30&order_direction=DESC&order_field=date&client_id= 7 -u 'diana.alvarez@eatcloud: 6505f78dbfb7dfb38bfe ' 

 Con la respuesta se formatea una tabla que contiene la siguiente informacin 

 Fecha 
 Label: class=" lbl_fecha " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_fecha ) 

 La informacin se toma de: "date" 

 # de factura 
 Label: class=" lbl_numero_factura " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_numero_factura )   

 La informacin se toma de: "numberTemplate": {"fullNumber":} 

 Precio 
 Label: class=" lbl_precio " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_precio )  

 La informacin se toma de: "total" 

 Estado 
 Label: class=" lbl_estado " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_estado )  

 La informacin se toma de: "status" 

  Estado legal 
 Label: class=" lbl_estado_legal " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_estado_legal )   

 La informacin se toma de: " stamp": {"legalStatus":} 

 Informacin de la factura 
 Label: class=" lbl_info_factura " 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_info_factura )   

 Vnculo "Descargar" ( class=" lbl_descargar " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_descargar )) : toma la informacin de la URL que comienza por " https://catalogo-vpfe.dian.gov.co/document/ShowDocumentToPublic/ " y que se encuentra en el tag: "stamp": {"barCodeContent":}  

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-plan-y-facturaci%C3%B3n%2F776963832-tu_plan_y_facturacion.jpg&ow=686&oh=761, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-plan-y-facturaci%C3%B3n%2F776963832-tu_plan_y_facturacion.jpg&ow=686&oh=761 
 Cuentas datagov 

 319.000000000000 

 CONFIGURACIN PLANES Y FACTURACIN