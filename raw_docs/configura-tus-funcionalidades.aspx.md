# configura-tus-funcionalidades.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ID Funcionalidad 
 cnf_fun_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= cnf_fun_datagov_cua ) 

 Label Botn Men: 
 lb_btn_cnf_fun_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_fun_datagov_cua ) 

 Label Ttulo de la Vista: 
 lb_cnf_fun_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_fun_datagov_cua ) 

 Label Descripcin de la Vista: 
 lb_cnf_fun_datagov_cua_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_fun_datagov_cua_desc ) 

 Determinacin de funcionalidades que se podrn administrar 
 El sistema debe consultar los datos bsicos de la cuenta, mediante el siguiente llamado: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{_DOM. cua_user }} 

 Con el llamado se obtienen los valores contenidos en los parmetros 
 eatc_cua. vertical 
 eatc_cua. type 

 Y con ellos se hace el siguiente llamado para establecer las funcionalidades que podr prender o apagar el administrador: 

 Funcionalidades WEB APP: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades? ambiente =produ& plataforma =webapp& plan ={{eatc_cua. type }}& vertical ={{eatc_cua. vertical }} 

 Funcionalidades BO (viejo): 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades? ambiente =produ& plataforma =donantes& plan ={{eatc_cua. type }}& vertical ={{eatc_cua. vertical }} 

 Funcionalidades BO Nuevo: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?ambiente=produ&plataforma=datagov_cuentas& plan ={{eatc_cua. type }}& vertical ={{eatc_cua. vertical }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Cuentas datagov 

 CONFIGURACIN DE FUNCIONALIDADES