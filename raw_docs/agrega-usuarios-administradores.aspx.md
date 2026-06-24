# agrega-usuarios-administradores.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CRUD Usuarios BO 

 Nota importante de implementacin: en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Esta funcionalidad se debe basar en la implementacin que ya se tiene en los BO de donantes para el usuario superadmin, en la cual se crean y editan usuarios de BO. 

 ID Funcionalidad 
 cnf_bo_user_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= cnf_bo_user_datagov_cua ) 

 Label Botn Men: 
 lb_btn_cnf_bo_user_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_bo_user_datagov_cua ) 

 Label Ttulo de la Vista: 
 lb_cnf_bo_user_datagov_cua ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_bo_user_datagov_cua ) 

 Label Descripcin de la Vista: 
 lb_cnf_bo_user_datagov_cua_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_bo_user_datagov_cua_desc ) 

 Funcionalidad disponible solo para usuarios superadmin 
 Solo los usuarios con perfil de superadmin ( tipo= A ) 

 Cuando no hay registros en el respectivo repositorio de usuarios 
 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{eatc_cua. name }}/bo_usuarios?tipo=U 

 Si la misma no trae datos se debe mostrar el siguiente anuncio al inicio de la funcionalidad (que debe estar internacionalizado de raz) 
 lb_cnf_bo_user_datagov_cua_wrn ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_bo_user_datagov_cua_wrn ) 

 Validacin de tope de usuarios por cuenta (***NUEVO: valor por defecto " free " en vez de " free_trial ") 
 Antes de desplegar el formulario, el sistema deber realizar la siguiente consulta, teniendo en cuenta los datos alojados en la informacin de la cuenta y que se consultan mediante este llamado 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&_distinct= type 

 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta: 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_types_of_licenses? eatc_code ={{eatc_cua. type }}&_distinct= eatc_bo_users_limit 

 Si esta ltima consulta no trae ningn valor, se utilizar esta consulta por defecto: 
 {{ URL_entorno_datagov }}/api/eatcloud/eatc_types_of_licenses? eatc_code =free&_distinct= eatc_bo_users_limit 
 Anteriormente : https://datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =free_trial  

 El sistema debe evaluar si el nmero que se obtiene en el parmetro eatc_types_of_licenses. eatc_bo_users_limit es mayor al valor del count de la siguiente consulta. 

 ***NUEVO: SE CAMBIA el parmetro _compress por el parmetro _cont en la consulta y se cuentan todos los usuarios registrados*** 
 {{URL_entorno_donantes}}/api/{{eatc_cua.name}}/bo_usuarios?id=_*& _cont 

 Anteriormente : {{URL_entorno_donantes}}/api/{{eatc_cua.name}}/bo_usuarios?tipousuario=u& _cont 
 Anteriormente : {{URL_entorno_donantes}}/api/{{eatc_cua.name}}/bo_usuarios?tipousuario=u& _compress 

 Si es mayor lo dejar pasar al formulario de creacin de usuario administrador . 

 Si es menor o igual no lo debe dejar tomar el anuncio, debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva 

 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 
 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master = {{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct = eatc_cua_master 
 eatc_cua = {{_DOM. cua_user }} 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_bo_users_limit 
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
 eatc_upgrade_event = eatc_bo_users_limit 
 eatc_user = https://devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &_distinct =type = free 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_platform =datagov_cuentas& eatc_upgrade_event =eatc_bo_users_limit& eatc_user =jdr@nodrizza.com& eatc_actual_rescue_plan =free   

 Redireccin a pgina de upgrade por sobrepaso del lmite de usuarios administradores 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/upgrade_by_admin_users 

 Ejemplo 1: Ambiente productivo 
 Un usuario de la cuenta "exito" desea crear manualmente un punto de donacin, por lo tanto dado que los datos de la cuenta son los siguientes: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito    
 type: " impacto " 

 Entonces se debe proceder en primera instancia con esta consulta, para establecer el lmite de usuarios BO para el tipo de licencia en cuestin: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =impacto   

 Como se obtiene en el parmetro eatc_bo_users_limit : "1000000" es mayor al valor del count de la consulta: 

 https://donantes.eatcloud.info/api/exito/bo_usuarios?tipousuario=u&_cont   

 El sistema le desplegar el formulario de creacin de usuario de consulta (que se describe a continuacin). 

 Formulario: Agregar usuarios administradores 

 ***NUEVO: permitir la configuracin del rol*** 
 Se debe presentar un selector nico que contenga que despliegue las siguientes opciones: 

 Consulta de informes (class= lbl_consulta_informes https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel=lbl_consulta_informes ): valor por defecto . Si se selecciona se debe llevar al registro el rol tipo: U 

 Consulta de informes y configuracin (class= lbl_consulta_informes_config https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel=lbl_consulta_informes_config ): Si se selecciona se debe llevar al registro el rol tipo: A 

 Esta funcionalidad debe guardar datos en la estructura de usuarios de bo 
 {{URL_entorno_donantes}}/crd/{{eatc_cua. name }}/?_tabla=bo_usuarios&_operacion=insert&{{parametros_creados}} 

 Listado de usuarios que se van creando 
 El sistema debe presentar un listado de usuarios que se van creando y a partir del mismo consultar y editar datos 
 {{URL_entorno_donantes}}/crd/{{eatc_cua. name }}/?_tabla=bo_usuarios&_operacion=update&{{parametros_editados}}&WHEREid={{bo_usuarios. id }} 

 ***NUEVO: en el listado en vez de mostrar ROL A y U, mostrar el label correspondiente*** 
 En el listado de usuarios registrados se debe en vez de mostrar ROL A y U, desplegar el respectivo label de la siguiente manera 

 U:  se deslpliega el label: class= lbl_consulta_informes https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel=lbl_consulta_informes ) 

 A:  se deslpliega el label: class= lbl_consulta_informes_config https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel=lbl_consulta_informes_config ) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagrega-usuarios-administradores%2F1451554003-EmbeddedImage--61-.jpg&ow=1280&oh=843, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagrega-usuarios-administradores%2F1451554003-EmbeddedImage--61-.jpg&ow=1280&oh=843 
 Cuentas datagov 

 316.000000000000 

 AGREGAR USUARIOS ADMINISTRADORES