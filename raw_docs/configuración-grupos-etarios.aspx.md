# configuración-grupos-etarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Label Ttulo de la Vista: 
 id = lb_cnf_age_groups ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_age_groups )  

 Label Descripcin de la Vista: 
 id = lb_cnf_age_groups_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_age_groups_desc )  

 FORMULARIO PARA CREACIN DEL GRUPO ETAREO 

 Nombre del grupo etario 
 Label: 
 id = lb_age_group_name ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_age_group_name )  

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_age_groups. age_group 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? age_group ={{text_input}} 

 Cdigo del grupo etreo 
 Label: 
 id = lb_age_group_code ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_age_group_code )  

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_age_groups. age_group_code 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad, unicidad (no pueden existir dos cdigo iguales), saneamiento de espacios y caracteres especiales (deben ser retirados) 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? age_group_code ={{text_input}} 

 Porcentaje de incidencia del grupo etario en el total de la poblacin atendida 
 Label: 
 id = lb_age_group_percentaje ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_age_group_percentaje )  

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_age_groups. percentage 
 Tipo de dato: integer 
 Tipo de input: number input 
 Obligatoriedad : si 
 Validacin : obligatoriedad, menor o igual que 100, mayor que 0.  La sumatoria de los dems registros (porcentajes) no debe ser mayor a 100. 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? percentage ={{number_input}} 

 Llamado al CRD para realizar el registro 
 {{URL_entorno_beneficiarios}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_age_groups &_operacin=insert& age_group ={{text_input}}& age_group_code ={{text_input}} & percentage ={{number_input}} 

 LISTADO DE REGISTROS REALIZADOS (PARA CONSULTAR Y EDITAR) 

 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? age_group =_* 

 Para presentar una lista de los registros realizados.  Dicha lista deber permitir borrar y editar los registros realizados. La lista deber contener las siguientes columnas: 

 Cdigo 
 Label: 
 id = lb_codigo ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_codigo )  

 Caracterizacin del Input: 
 De donde se toma la informacin: eatc_age_groups. age_group_code 
 Caracterstica: parmetro no editable, solo se muestra la informacin registrada 

 Nombre 
 Label: 
 id = lb_nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_nombre )  

 Caracterizacin del Input: 
 De donde se toma la informacin: eatc_age_groups. age_group 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? age_group ={{text_input}} 

 Porcentaje 
 Label: 
 id = lb_porcentaje ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_porcentaje )  
 De donde se toma la informacin: eatc_age_groups. percentage 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Tipo de dato: integer 
 Tipo de input: number input 
 Obligatoriedad : si 
 Validacin : obligatoriedad, menor o igual que 100, mayor que 0.  La sumatoria de los dems registros (porcentajes) no debe ser mayor a 100. 
 Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_age_groups? percentage ={{number_input}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 CONFIGURACIN GRUPOS ETARIOS