# agregar-usuario-nuevo-bo-cua-master-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 TTULO DEL FORMULARIO: AGREGAR USUARIO 
 clase = lbl_agregar_usuario ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_agregar_usuario )  

 E-mail (en el mockup est de segundo, pero debe mostrarse de primero): 

 Label: 
 clase = lbl_correo_electronico ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_correo_electronico )    

 Caracterizacin del campo: 
 Valor por defecto: ninguno 
 Tipo de dato: email 
 Tipo de input: email input 
 Obligatoriedad : si 
 Validacin : obligatoriedad y formato email. 
 {{ email_usuario }} 

 Nombre (en el mockup est de primero, pero debe mostrarse de segundo): 

 Label: 
 clase = lbl_nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre ) 

 Tooltip: "Nombre del nuevo usuario de la plataforma" 
 clase = lbl_nombre_nuevo_usuario_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre_nuevo_usuario_desc )    

 Caracterizacin del Input: 
 Valor por defecto: ninguno 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 {{ nombre_usuario }} 

 Cargo: 

 Label: 
 clase = lbl_cargo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cargo )     

 Tooltip: "Cargo del usuario dentro de la organizacin" 
 clase = lbl_cargo_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cargo_desc ) 

 Caracterizacin del Input: 
 Valor por defecto: ninguno 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : no 
 Validacin : ninguna 
 {{ cargo }} 

 Permisos: 

 Label: 
 clase = lbl_permisos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_permisos )  

 Tooltip: "Define si el usuario tendr privilegios de administrador o de consulta de informes de informes" 
 clase = lbl_permisos_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_permiso_desc )   

 Caracterizacin del Input: Selector nico 
 Valor por defecto: ninguno 
 Tipo de input: Selector nico 
 Clave ( Valor ) del selector: 
 Usuario administrador: clase =  lbl_usuario_administrador ( A ) ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_usuario_administrador )  
 Usuario consulta: clase =  lbl_usuario_consulta ( U ) ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_usuario_consulta )  
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad (se valida que se tenga un valor: A / U, para llevar al registro) 
 {{ permisos }} 

 Asignar contrasea: 
 Label: 
 clase = lbl_assign_pass ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_assign_pass )  

 Tooltip: "Digite una contrasea para el usuario que est creando" 
 clase = lbl_assign_pass_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_assign_pass_desc )   

 Place holders (en el diseo no est la doble digitacin de la contrasea) 
 clase = lbl_password ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_password )  

 Confirmar contrasea 
 clase = lbl_confirm_pass ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_confirm_pass )  

 Caracterizacin del Input: 
 Valor por defecto:  Ninguno 
 Tipo de dato: password 
 Tipo de input: password input 
 Obligatoriedad : si 
 Validacin : Que las dos contraseas sean idnticas 
 {{ password }} 

 Botn: Crear usuario: 

 Label: 
 clase = lbl_crear_usr ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_crear_usr )     
 Al oprimir el botn, el sistema realizar los siguientes llamados 

 Llamado al firebase para registrar el usuario 
 Se debe llamar a los servicios de firebase para registrar el usuario. Y para obtener el hash de la contrasea que se guardaa en bo_usuarios? 

 Llamado al CRD para creacin del registro en beneficiarios/ {{_DOM. cua_master }}/bo_usuarios 
 {{URL_entorno_beneficiarios}}/crd/{{_DOM. cua_master }}/?_tabla=bo_usuarios&_operacion=insert&email={{ email_usuario }}& nombre_usuario ={{ nombre_usuario }}& eatc_position ={{ cargo }}& tipousuario ={{ permisos }}& clave ={{ password }} => Se debe hashear la clave en este punto? 

 Llamado al CRD para creacin del registro en datagov/ eatcloud/eatc_users 
 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_users&_operacion=insert& eatc_email ={{ email_usuario }}& eatc_cua_master ={{_DOM. cua_master }}& last ={{datetimestamp}} 

 Envo de correo electrnico para informarle los accesos al nuevo usuario 
 Hola (class= lbl_hola https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_hola )  {{ nombre_usuario }} 

 Se han acabado de crear los siguientes datos de acceso a la plataforma EatCloud BO beneficiarios  (class= lbl_se_crearon_datos_acceso https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_se_crearon_datos_acceso )  

 URL (direccin web) de acceso (class= lbl_url_acceso https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_url_acceso ): {{URL_entorno_beneficiarios}}/signin 

 Usuario (class= lbl_usuario https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_usuario ): {{ email_usuario }} 

 Contrasea (class= lbl_password https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_password ): {{ password }} 

 Atento saludo (class= lbl_atento_saludo https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_atento_saludo )  

 Equipo EatCloud (class= lbl_equipo_eatcloud https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_equipo_eatcloud )  

 TABLA DE USUARIOS CREADOS 

 E-mail (en el mockup est de segundo, pero debe mostrarse de primero): 
 Label: 
 clase = lbl_correo_electronico ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_correo_electronico )    

 {{bo_usuarios. email }} 

 Nombre (en el mockup est de primero, pero debe mostrarse de segundo): 
 Label: 
 clase = lbl_nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre ) 

 {{bo_usuarios. nombre_usuario }} 

 Cargo (no est en el diseo) 
 Label: 
 clase = lbl_cargo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cargo )     

 {{bo_usuarios. eatc_position }} 

 Permisos (en el diseo: "Permisos") 
 Label: 
 clase = lbl_permisos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_permisos )  

 {{bo_usuarios. tipousuario }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagregar-usuario-nuevo-bo-cua-master-beneficiarios%2F844288687-agregar_usuarios.jpg&ow=653&oh=616, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fagregar-usuario-nuevo-bo-cua-master-beneficiarios%2F844288687-agregar_usuarios.jpg&ow=653&oh=616 
 Nuevo BO CUA MASTER Beneficiarios 

 725.000000000000 

 AGREGAR USUARIO