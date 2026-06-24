# configura-tu-de-cuenta-de-usuario.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Configuracin usuario (superadmin) 

 Nota importante de implementacin: en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 ID Funcionalidad 
 cnf_user_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= cnf_user_datagov_cua ) 

 Label Botn Men: 
 lb_btn_cnf_user_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_user_datagov_cua ) 

 Label Ttulo de la Vista: 
 lb_cnf_user_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_user_datagov_cua ) 

 Label Descripcin de la Vista: 
 lb_cnf_user_datagov_cua_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_user_datagov_cua_desc ) 

 Esta funcionalidad debe estar conectada con el social login, desplegar el mismo formulario de captura que se despliega en la funcionalidad homloga del onboarding (junto con la configuracin del nombre y del perfil del usuario ) y debe guardar datos en la estructura de usuarios de BO 

 {{URL_entorno_donantes}}/crd/{{eatc_cua. name }}/?_tabla=bo_usuarios&_operacion=update&{{parametros_editados}}&WHEREid={{bo_usuarios. id }} 

 Una vez se realiza cualquier edicin de los datos se debe realizar el llamado para editar los datos en las plataformas externas segn los servicios desarrollados para tal fin: 

 Edicin datos de contacto ERP 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 

 https://datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 Edicin datos de contacto CRM=>STANDBY hasta tener seleccin de herramienta 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 

 https://datagov.eatcloud.info/int/eatcloud/int_crm_datacrm?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 Edicin datos de contacto RD Station 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 

 https://datagov.eatcloud.info/int/eatcloud/int_mat_rdstation?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-de-cuenta-de-usuario%2F1697966814-PT5awSx7M7.png&ow=893&oh=786, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-de-cuenta-de-usuario%2F1697966814-PT5awSx7M7.png&ow=893&oh=786 
 Cuentas datagov 

 312.000000000000 

 CONFIGURACIN DE TU CUENTA