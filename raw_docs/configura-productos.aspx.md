# configura-productos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***DEPRECADO: Validacin del tipo de licencia para el despliegue de la funcionalidad *** 
 Antes de desplegar el formulario, el sistema deber realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 

 {{ URL_entorno_datagov }}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&_distinct= type 

 Corresponde eatc_cua. type =impacto eatc_cua. type =activo y en ese caso permitir pasar a la funcionalidad de mapeo de datos. 

 Si la licencia es diferente a impacto activo (es decir: eatc_cua. type =esencial eatc_cua. type =free ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera: 

 {{parametros_registro}} 

 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country ={{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_country 
 eatc_cua_master ={{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =eatc_cua_master 
 eatc_cua ={{_DOM. cua_user }} 
 eatc_platform =datagov_cuentas 
 eatc_upgrade_event =upgrade_by_configure_products 
 eatc_user ={{ URL_entorno_donantes }}/api/{{_DOM. cua_user }}/ bo_usuarios? nombre_usuario = {{ bo_usuarios. nombre_usuario }}&_distinct =email 
 eatc_actual_rescue_plan ={{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua ?name={{_DOM. cua_user }}&_distinct =type 

 Llamado al api con los {{parametros_registro}} (en el llamado los parmetros se separan por " & ") 
 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& {{parametros_registro}} 

 Ejemplo: entorno de pruebas, cuenta "ramo", bo_usuarios. nombre_usuario " Ramo ", el " 2021-11-16 10:20:00 " 

 El sistema toma los siguientes datos 

 eatc_datetime =2021-11-16 10:20:00 
 eatc_date =2021-11-16 
 eatc_country =https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &_distinct =eatc_country = co 
 eatc_cua_master =https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &_distinct =eatc_cua_master =abaco 
 eatc_cua = ramo 
 eatc_platform =datagov_cuentas 
 eatc_upgrade_event =upgrade_by_configure_products 
 eatc_user = https://devdonantes.eatcloud.info//api/ ramo / bo_usuarios? nombre_usuario = Ramo&_distinct =email    =hquintero@ramo.com.co 
 eatc_actual_rescue_plan = https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &_distinct =type =esencial 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&_operacion=insert& eatc_datetime =2021-11-16%2010:20:00& eatc_date =2021-11-16& eatc_country= co& eatc_cua_master =abaco& eatc_cua = ramo & eatc_platform =datagov_cuentas& eatc_upgrade_event =upgrade_by_configure_products& eatc_user =hquintero@ramo.com.co& eatc_actual_rescue_plan =esencial   

 Redireccin a pgina de upgrade por archivos planos 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 

 {{URL_entorno_datagov}}/_dgbo/#!/ upgrade_by_configure_products 

 Label Ttulo de la Vista: 
 lbl_configura_productos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_configura_productos )  

 Label Descripcin de la Vista: 
 lbl_configura_productos_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_configura_productos_desc )    

 En esta funcionalidad podrs configurar los datos de los productos susceptibles a ser donados desde la plataforma. 

 F ORMULARIO PARA CREACIN DE PRODUCTOS 
 Identificador nico del producto ***NUEVO:   llevar el dato tambin a eatc-odd_code *** 

 Label: 
 clase = lbl_eatc_odd_id ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_id )     

 Tooltip: " El identificador nico del producto o artculo donado es un cdigo que sirve para identificar de manera nica el producto o referencia que se dona " 
 clase = lbl_eatc_odd_id_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_id_desc )   

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-id,eatc-odd_code   
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad, ***NUEVO: unicidad *** 
 Se guarda en (para efectos indicativos, no prcticos) :  ***NUEVO: llevar tambin el textinput a eatc-odd_code *** 
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-id ={{ text_input }} 
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-odd_code ={{ text_input }} 

 Nombre del producto 
 Label: 
 clase = lbl_eatc_odd_name ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_name )     

 Tooltip: " El nombre del producto, corresponde al nombre el artculo o producto donado " 
 clase = lbl_eatc_odd_name_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_name_desc )   

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-odd_name 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-odd_name ={{ text_input }} 

 Peso unitario en KG 
 Label: 
 clase = lbl_eatc_odd_unit_weight_kg ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_unit_weight_kg )      

 Tooltip: " El peso unitario del artculo o anuncio en kilogramos, corresponde a lo que pesa una sola unidad del artculo o producto donado " 
 clase = lbl_eatc_odd_unit_weight_kg_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_unit_weight_kg_desc )    

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-odd_unit_weight_kg   
 Tipo de dato: float 
 Tipo de input: float input 
 Obligatoriedad 

 Ser obligatorio si la siguiente consulta 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&odds_weight=eatc_odds&_cont 

 Da como resultado: 
 count=1 

 De lo contrario ser opcional. 
 Ejemplo: entorno de pruebas, cuenta "alqueria" 

 El sistema realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alqueria&odds_weight=eatc_odds&_cont   

 Dado que el resultado es: 
 count=1 

 Entonces el dato ser obligatorio para esa cuenta. 

 Validacin : obligatoriedad (en los casos en que aplique, segn lo estipulado anteriormente) 
 Se guarda en (para efectos indicativos, no prcticos) :  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-odd_unit_weight_kg ={{ float_input }} 

 Unidad de donacin 
 Label: 
 clase = lbl_eatc_dona_unit ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_dona_unit )      

 Tooltip: " La unidad de donacin corresponde a la unidad en la que se dona el artculo (ejemplo: unidad, kilogramos, etc.) " 
 clase = lbl_eatc_dona_unit_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_dona_unit_desc )    

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc_dona_unit 
 Tipo de dato: string 
 Tipo de input: text input 
 Valor por defecto :  ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc_dona_unit ={{ text_input }} 

 Costo unitario 
 Label: 
 clase = lbl_eatc_unit_cost ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_unit_cost ) 

 Tooltip: " Costo unitario corresponde a costo unitario del artculo o producto donado " 
 clase = lbl_eatc_unit_cost_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_unit_cost_desc )     

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-unit_cost 
 Tipo de dato: float 
 Tipo de input: float input 
 Valor por defecto :  ninguno 
 Obligatoriedad 

 Ser obligatorio si la siguiente consulta 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&costs=eatc_odds&_cont 

 Da como resultado: 
 count=1 

 De lo contrario ser opcional. 
 Ejemplo: entorno de pruebas, cuenta "alqueria" 

 El sistema realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alqueria&costs=eatc_odds&_cont     

 Dado que el resultado es: 
 count=1 

 Entonces el dato ser obligatorio para esa cuenta. 

 Validacin : obligatoriedad (en los casos en que aplique, segn lo estipulado anteriormente) 
 Se guarda en (para efectos indicativos, no prcticos) :  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-unit_cost ={{ float_input }} 

 Porcentaje de IVA 
 Label: 
 clase = lbl_eatc_VAT_percentage ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_VAT_percentage )  

 Tooltip: " El porcentaje de IVA corresponde al porcentaje del impuesto al valor agregado que es aplicable al producto donado " 
 clase = lbl_eatc_VAT_percentage_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_VAT_percentage_desc ) 

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-VAT_percentage 
 Tipo de dato: float 
 Tipo de input: float input 
 Valor por defecto :  el que d como resultado la siguiente consulta: 
 {{URL_entorno_datagov}} /api/eatcloud/ eatc_cua_master ?eatc_cua= {{_DOM. cua_master }} &_distinct= eatc_default_VAT 

 Ejemplo: entorno de pruebas, cuenta maestra "argentina" 

 El sistema realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua_master ?eatc_cua=argentina&_distinct= eatc_default_VAT 

 Dado que el resultado es: 
 eatc_default_VAT : "21" 

 Entonces el valor por defecto ser "21.00". 

 Obligatoriedad 
 Ser obligatorio si la siguiente consulta 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{_DOM.cua_master}}&taxes=eatc_odds&_cont) cont=1 

 Da como resultado: 
 count=1 

 De lo contrario ser opcional. 
 Ejemplo: entorno de pruebas, cuenta "alqueria" 

 El sistema realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alqueria&taxes=eatc_odds&_cont   

 Dado que el resultado es: 
 count=0 

 Entonces el dato NO ser obligatorio para esa cuenta. 

 Validacin : obligatoriedad (en los casos en que aplique, segn lo estipulado anteriormente) 
 Se guarda en (para efectos indicativos, no prcticos) :  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc_vat_percentage ={{ float_input }} 

 Primera tipologa del producto 
 Label: 
 clase = lbl_origin_odds_typology_a ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_a )       

 Tooltip: " La primera tipologa del producto corresponde al valor de una primera clasificacin del artculo o producto donado. Es una definicin propia de cada donante " 
 clase = lbl_origin_odds_typology_a_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_a_desc )    

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-odd_typology_a 
 Tipo de dato: string 
 Tipo de input: text input, con texto predictivo a partir de los datos que se obtienen a partir de la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? _id =_*&_distinct= eatc-odd_typology_a 
 Valor por defecto :  ninguno 
 Obligatoriedad : no 
 Validacin : ninguna 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-odd_typology_a ={{ text_input }} 

 Segunda tipologa del producto 
 Label: 
 clase = lbl_origin_odds_typology_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_b )       

 Tooltip: " La segunda tipologa del producto corresponde al valor de una segunda clasificacin del artculo o producto donado. Es una definicin propia de cada donante " 
 clase = lbl_origin_odds_typology_b_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_b_desc )    

 Caracterizacin del Input: 
 Informacin tcnica del parmetro: https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_odds&eatc_parameter=eatc-odd_typology_b 
 Tipo de dato: string 
 Tipo de input: text input, con texto predictivo a partir de los datos que se obtienen a partir de la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? _id =_*&_distinct= eatc-odd_typology_b 
 Valor por defecto :  ninguno 
 Obligatoriedad : no 
 Validacin : ninguna 
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? eatc-odd_typology_b ={{ text_input }} 

 Llamado al CRD para creacin del registro 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/?_tabla=eatc_odds&_operacion=insert& eatc-id ={{ text_input }}& eatc-odd_name ={{ text_input }}& eatc-odd_unit_weight_kg ={{ float_input }}& eatc_dona_unit ={{ text_input }}& eatc-unit_cost ={{ float_input }}& eatc_vat_percentage ={{ float_input }}& eatc-odd_typology_a ={{ text_input }}& eatc-odd_typology_b ={{ text_input }} 

 L ISTADO DE REGISTROS REALIZADOS (PARA CONSULTAR Y EDITAR) 
 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_odds? _id =_* 

 Para presentar una lista de los registros realizados.  Dicha lista deber permitir borrar y editar los registros realizados. La lista debe presentarse paginada y debe tener un buscador que permita encontrar rpidamente por cualquier criterio alguno de los productos registrados (muy al estilo del buscador que maneja " Datatables "). La lista deber contener las siguientes columnas: 

 Identificador nico del producto 
 Label: 
 class= lbl_eatc_odd_id ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_eatc_odd_id )  

 De donde se toma la informacin: eatc_odds. eatc-id 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito. 

 Nombre del producto 
 Label: 
 class= lbl_eatc_odd_name ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_name )  

 De donde se toma la informacin: eatc_odds. eatc-odd_name 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Peso unitario en KG 
 Label: 
 class= lbl_eatc_odd_unit_weight_kg ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_odd_unit_weight_kg )  

 De donde se toma la informacin: eatc_odds. eatc-odd_unit_weight_kg 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Unidad de donacin 
 Label: 
 class= lbl_eatc_dona_unit ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_dona_unit )  

 De donde se toma la informacin: eatc_odds. eatc_dona_unit 

 Caracterizacin del Input para editar el dato contenido en el informe 

 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Costo unitario 
 Label: 
 class= lbl_eatc_unit_cost ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_unit_cost )  

 De donde se toma la informacin: eatc_odds. eatc-unit_cost 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Porcentaje de IVA 
 Label: 
 class= lbl_eatc_VAT_percentage ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_eatc_VAT_percentage )  

 De donde se toma la informacin: eatc_odds. eatc-VAT_percentage 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Primera tipologa del producto 
 Label: 
 class= lbl_origin_odds_typology_a ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_a )  

 De donde se toma la informacin: eatc_odds. eatc-odd_typology_a 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 Segunda tipologa del producto 
 Label: 
 class= lbl_origin_odds_typology_b ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_origin_odds_typology_b )   

 De donde se toma la informacin: eatc_odds. eatc-odd_typology_b 

 Caracterizacin del Input para editar el dato contenido en el informe 
 Aplican las mismas estipulaciones del formulario anteriormente descrito . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONFIGURA PRODUCTOS