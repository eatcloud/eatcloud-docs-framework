# configuración-kg-máximos-gestionables-por-tipología-b.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Label Ttulo de la Vista: 
 id = lb_cnf_max_kg_x_doma_tip_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_max_kg_x_doma_tip_b )  

 Label Descripcin de la Vista: 
 id = lb_cnf_max_kg_x_doma_tip_b_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_max_kg_x_doma_tip_b_desc ) 

 Cuando no hay registros en el respectivo repositorio de tipologas b 
 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b?_id=_* 

 Si la consulta no trae resultados, el sistema debe desplegar la concatenacin de los siguientes labels: 

 La presente cuenta maestra no tiene registros de tipologas b en el respectivo maestro . Debes registrar tipologas B para clasificar tus gestores de donacin antes de proceder con la presente configuracin 

 concat( id= lb_sin_doma_tip_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_sin_doma_tip_b ) ) concat(.) concat( id= lb_registra_doma_tip_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_registra_doma_tip_b ) ) 

 En caso de no tener tipologas b de gestores de donacin registradas, despus de mostrar los labels definidos anteriormente se debe mostrar el siguiente botn: 

 Botn: Configurar tipologas B de gestores de donacin 
 label: id=lb_btn_cnf_doma_tipologias_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_btn_cnf_doma_tipologias_b ) 
 Dirige a: Configuracin de tipologas B de gestores de donacin   

 Si la cuenta tiene tipologas registradas se despliega el siguiente formulario. 

 FORMULARIO PARA CREACIN DE LMITE MXIMO DE KILOGRAMOS QUE PUEDEN SER GESTIONADOS SEGN LA TIPOLOGA B DE LOS GESTORES DE DONACIN 

 Tipologa B: seleccione una tipologa B previamente registrada a configurar 
 Label: 
 id=lb_cnf_doma_tip_b_selector ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_cnf_doma_tip_b_selector )  

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_max_kg_x_doma_typology_b. eatc_doma_typology_b 
 Tipo de dato: string 
 Tipo de input: selector nico 
 De dnde proviene la informacin del selector: 
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_name =_* 
 Aparece en el selector: eatc_doma_typology_b. eatc_name 
 Se lleva al registro: eatc_doma_typology_b. eatc_code 
 Obligatoriedad : si 
 Validacin : obligatoriedad, unicidad (este dato es un identificador nico del registro, por lo tanto no se puede duplicar registros para una misma tipologa) 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b? eatc_doma_typology_b ={{eatc_doma_typology_b. eatc_code }} 

 Cantidad mxima de kilogramos gestionables para organizaciones en la anterior tipologa (B) 
 Label: 
 id = lb_max_kg_x_doma_tip_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_max_kg_x_doma_tip_b )  

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: eatc_max_kg_x_doma_typology_b. limite_superior_kg 
 Tipo de dato: integer 
 Tipo de input: number input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b? limite_superior_kg ={{number_input}} 

 Llamado al CRD para realizar el registro 
 {{URL_entorno_beneficiarios}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_max_kg_x_doma_typology_b&_operacin=insert& eatc_doma_typology_b ={{eatc_doma_typology_b. eatc_code }}& limite_superior_kg ={{number_input}} 

 LISTADO DE REGISTROS REALIZADOS (PARA CONSULTAR Y EDITAR) 

 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b? eatc_doma_typology_b =_* 

 Para presentar una lista de los registros realizados.  Dicha lista deber permitir borrar y editar los registros realizados. La lista deber contener las siguientes columnas: 

 Tipologa B 
 Label: 
 id = lb_tip_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_tip_b )  
 De donde se toma la informacin: eatc_max_kg_x_doma_typology_b. eatc_doma_typology_b 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Tipo de dato: string 
 Tipo de input: selector nico 
 De dnde proviene la informacin del selector: 
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_typology_b? eatc_name =_* 
 Aparece en el selector: eatc_doma_typology_b. eatc_name 
 Se lleva al registro: eatc_doma_typology_b. eatc_code 
 Obligatoriedad : si 
 Validacin : obligatoriedad, unicidad (este dato es un identificador nico del registro, por lo tanto no se puede duplicar registros para una misma tipologa) 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b? eatc_doma_typology_b ={{eatc_doma_typology_b. eatc_code }} 

 Cantidad mxima de kilogramos 
 Label: 
 lb_max_kg ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lb_max_kg )  

 Caracterizacin del Input: 
 De donde se toma la informacin: eatc_max_kg_x_doma_typology_b. limite_superior_kg 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Tipo de dato: integer 
 Tipo de input: number input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) 
{{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b.? limite_superior_kg ={{number_input}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 CONFIGURACIN DE LOS KILOGRAMOS MXIMOS GESTIONABLES POR TIPOLOGA B DE GESTOR DE DONACIONES