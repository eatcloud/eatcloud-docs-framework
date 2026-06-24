# agrega-puntos-de-donación-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Creacin manual de puntos de donacin 

 Nota importante de implementacin:  
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Funcionalidad disponible solo para usuarios superadmin 
 Solo los usuarios con perfil de superadmin ( tipo= A ) 

 Label Botn Men: 
 lb_btn_cnf_pods_datagov_cua ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lb_btn_cnf_pods_datagov_cua )  

 Label Ttulo de la Vista: 
 lb_cnf_pods_datagov_cua ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lb_cnf_pods_datagov_cua )  

 Label Descripcin de la Vista: 
 lb_cnf_pods_datagov_cua_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lb_cnf_pods_datagov_cua_desc )  

 Cuando no hay registros en el respectivo repositorio de puntos de donacin 
 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_pods?_id=_* 

 Si la misma no trae datos se debe mostrar el siguiente anuncio al inicio de la funcionalidad (que debe estar internacionalizado de raz) 
 lb_cnf_pods_datagov_cua_wrn ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_pods_datagov_cua_wrn )  

 Diseo 

 Botn: Agregar un nuevo punto de donacin: 
 class= lb_agregar_nuevo_pod (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lb_agregar_nuevo_pod ) 

 Cuando se presiona este botn, se debe realizar primero la validacin del nmero de puntos permitidos por la licencia rescate de la cuenta respectiva (lo cual puede dar lugar a la captura de un evento de upgrade y de una redireccin a pgina de upgrade respectiva ), y posteriormente anunciar, dado unos tipos de licencia rescate particulares , que la adicin del nuevo punto implicar un cobro adicional. 

 Validacin de tope de puntos de donacin por cuenta segn licencia rescate 
 Cuando se accione el botn para agregar un nuevo punto de donacin, el sistema deber realizar la siguientes consulta 

 Antes de desplegar el formulario, el sistema deber realizar la siguiente consulta, teniendo en cuenta los datos alojados en la informacin de la cuenta y que se consultan mediante este llamado 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM. cua_user }}&_distinct= type 

 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_types_of_licenses? eatc_code ={{eatc_cua. type }}&_distinct= eatc_bo_users_limit 

 Si esta ltima consulta no trae ningn valor, se utilizar esta consulta por defecto: 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_types_of_licenses? eatc_code =free&_distinct= eatc_pods_limit 
 Anteriormente : https://datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =free_trial  

 El sistema debe evaluar si el nmero que se obtiene en el parmetro eatc_types_of_licenses. eatc_pods_limit es mayor al valor del count de la siguiente consulta. 

  Consulta del nmero de puntos de donacin ***ACTIVOS*** por la cuenta 
 {{ URL_entorno_donantes }}api/allpods/eatc_pods?eatc_active=y&eatc-cua={{_DOM. cua_user }} 

 Si es mayor pasar la Validacin del tipo de licencia para despliegue de pop-up informativo (que se detalla ms adelante). 

 Si es menor o igual no lo debe dejar pasar al formulario de creacin de punto de donacin, debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla ms adelante para posteriormente redireccionar a la pgina de upgrade respectiva 

 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 
 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_pods_limit 
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
 eatc_upgrade_event = eatc_pods_limit 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event = eatc_pods_limit & eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free   

 Redireccin a pgina de upgrade por sobrepaso del lmite de puntos de donacin permitidos por la licencia rescate 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_by_pods 

 Validacin del tipo de licencia para despliegue de pop-up informativo por registro de nuevo pod 
 Si la licencia es diferente a "free", es decir si eatc_cua. type   es" esencial ", " activo ", " impacto ", entonces el sistema deber desplegar, antes de direccionar al formulario de ingreso del nuevo punto de donacin un pop-up de la siguiente manera: 

 Tu cuenta EatCloud con el plan rescate (concat) {{plan_rescate}} (concat) tiene (concat) {{numero_pods}} (concat) punto(s) de donacin activo(s) 
 class= lbl_tu_cuenta_con_plan_rescate ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_tu_cuenta_con_plan_rescate )   

 {{Plan_de_rescate}} (en el ejemplo "Activo") 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =type 

 class= lbl_tiene ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_tiene )  

 {{numero_pods}} (en el ejemplo " 1 ") 
 {{ URL_entorno_donantes }}api/allpods/eatc_pods?eatc_active=y&eatc-cua={{_DOM. cua_user }} 

 class= lbl_pods_activos_2 ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_pods_activos_2 )  

 Al adicionar un nuevo punto de donacin actualizaremos la informacin de puntos de donacin de tu plan rescate (concat) {{plan_rescate}} (concat) EatCloud. Vers el cambio reflejado en tu factura. 
 class= lbl_al_adicionar_pod ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_al_adicionar_pod )   

 {{Plan_de_rescate}} (en el ejemplo "Activo") 
 {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =type 

 class= lbl_veras_cambio_en_factura ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_veras_cambio_en_factura )  

 Cancelar 
 class= lbl_cancelar ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_cancelar )  

 Este botn devuelve a la pgina de adicin de puntos:  
 {{ URL_entorno_datagov }}/_dgbo/#!/pods 

 (sin abrir el formulario de creacin del punto) pero permitiendo ver el listado y editar puntos. 

 Continuar 
 class= lbl_continuar ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_continuar ) 

 Este botn abre el formulario de creacin de nuevo punto de donacin descrito a continuacin 

 Formulario: Agregar nuevo punto de donacin (implementacin basada en una implementacion previa) 
 Se debe buscar una manera para utilizar la implementacin de Registro Simple de Punto de Donacin , (no se debe tomar en cuenta lo propuesto en el diseo arriba adjunto en lo que al formulario se refiere), al cual se puede acceder de la siguiente manera: 
 {{URL_entorno_donantes}}/registro/{{eatc_cua. name }} 

 Lo ideal sera llamar ese mismo cdigo (es decir que cualquier intervencin del cdigo se haga en un solo lugar) y traerlo a esta pantalla.  Es importante limpiar el formulario de los mensajes que aparecen al principio. 

 Y al final del mismo (el label de la aceptacin de trminos debe quedar): 

 Los procesos de envo de correo electrnico ante la creacin del registro se deben tambin incorporar y el CASEDB que crea los datos por defecto para la configuracin de funcionalidades.  Por otro lado, las redirecciones que hace el formulario original, en este caso deben adaptarse para que no redireccione a la pgina en donde originalmente se redireccionaba cuando se completaba el formulario, sino que redireccione a la nueva pgina. 

 LISTADO DE PUNTOS DE DONACIN CREADOS 
 El sistema debe presentar un listado de puntos de donacin creados para la cuenta en particular, que permita consultarlos y editarlos de ser necesario. 
 {{URL_entorno_donantes}}/api/{{eatc_cua. name }}/eatc_pods?_id=_* 

 Una vez se editen los datos de los puntos de donacin se procede a realizar la respectiva edicin con el servicio correspondiente: 
 {{URL_entorno_donantes}}/crd/{{eatc_cua. name }}/?_tabla=eatc_pods&_operacion=update&{{parametros_editados}}&WHERE_id={{eatc_pods. _id }} 

 ***NUEVO: Primera columna de datos con el estado, activo o inactivo en allpods de cada punto de donacin*** 

 En una nueva columna, que ser la primera despus de la columna " operacin " se presentar el estado de actividad de cada punto (y que se registra en allpods ).  En dicha columna tambin se tendr la oportunidad de "editar el estado" para pasarlo de "Activo" a "Inactivo" (Inactivacin) o visceversa (Activacin).  Cuando un punto se active se deber validar si al hacerlo se sobrepasa el tope que permite la licencia rescate, para desplegar o no la ventana informativa que invita a realizar un upgrade.  Tambin al activar un punto de donacin se deber desplegar el pop-up informativo previamente  

 Ttulo de la columna: Estado 
 class= lbl_estado (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_estado )  

 Valores que van en cada registro 
 El sistema deber realizar la siguiente consulta:  
 {{ URL_entorno_donantes }}/api/allpods/eatc_pods?eatc-cua={{_DOM. cua_user }}&eatc-id={{eatc_pods. eatc-id }}&_distinct= eatc_active 
 Si la respuesta es: ; entonces deber desplegar el label: class= lbl_activo (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_activo ) y al lado un botn con el label lbl_inactivar ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_inactivar ) que activar la funcin de Inactivacin de punto que se documenta ms adelante. 
 Si la respuesta es: ; entonces deber desplegarl el label: class= lbl_inactivo (https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_inactivo ) y al lado un botn con el label lbl_activar ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_inactivar ) que activar la funcin de Activacin de punto que se documenta ms adelante. 

 Inactivacin de punto 
 El sistema deber desplegar un pop-up con la siguiente informacin 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagrega-puntos-de-donaci%C3%B3n-datagov%2F2641543550-add_pods.jpg&ow=1280&oh=513, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagrega-puntos-de-donaci%C3%B3n-datagov%2F2641543550-add_pods.jpg&ow=1280&oh=513 
 Cuentas datagov 

 341.000000000000 

 AGREGAR PUNTOS DE DONACIN