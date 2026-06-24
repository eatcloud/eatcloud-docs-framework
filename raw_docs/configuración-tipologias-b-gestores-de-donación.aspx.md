# configuración-tipologias-b-gestores-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante para el desarrollo: 
 Esta funcionalidad es prcticamente un clon de la funcionalidad " Configuracin tipologas A Gestores de Donacin ", por lo tanto el desarrollo se puede basar enteramente en el otro, haciendo los respectivos ajustes en labels. 

 Label Ttulo de la Vista: 
 id = lb_cnf_doma_tipologias_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_doma_tipologias_b )  

 Label Descripcin de la Vista: 
 id = lb_cnf_doma_tipologias_b_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_doma_tipologias_b_desc )   

 FORMULARIO PARA CREACIN DE TIPOLOGAS B PARA GESTORES DE DONACIN (BENEFICIARIOS) 

 eatc_code (captura oculta) 

 Label: 
 no aplica 

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_doma_typology_b. eatc_code 
 Tipo de dato: integer 
 Tipo de input: autoincremental oculto 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_code ={{ autoincremental }} 

 Nombre del elemento o tem de una segunda clasificacin de los gestores de donacin (por ejemplo: Bancos de Alimentos, fundaciones adscritas a bancos de alimentos , etc.) 
 Label: Nombre 
 class = lb_nombre_doma_tipologia_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_nombre_doma_tipologia_b )  

 Tooltip: 
 class = lb_nombre_doma_tipologia_b_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_nombre_doma_tipologia_b_desc )   

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_doma_typology_b. eatc_name 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_name ={{ text_input }} 

 Llamado al CRD para creacin del registro 
 {{URL_entorno_beneficiarios}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_doma_typology_b&_operacion=insert& eatc_code ={{ autoincremental }}& eatc_name ={{ text_input }} 

 LISTADO DE REGISTROS REALIZADOS (PARA CONSULTAR Y EDITAR) 

 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_name =_* 

 Para presentar una lista de los registros realizados.  Dicha lista deber permitir borrar y editar los registros realizados. La lista deber contener las siguientes columnas: 

 Cdigo 
 Label: 
 id = lb_codigo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_codigo )  
 De donde se toma la informacin: eatc_doma_typology_b. eatc_code 
 Caracterstica: parmetro no editable, solo se muestra la informacin registrada 

 Nombre 
 Label: 
 id = lb_nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_nombre )  
 De donde se toma la informacin: eatc_doma_typology_b. eatc_name 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_name ={{ text_input }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 CONFIGURACIN DE TIPOLOGAS B DE GESTORES DE DONACIN