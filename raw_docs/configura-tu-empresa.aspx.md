# configura-tu-empresa.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Configuracin de datos del cliente ( y algunos datos de la cuenta ) 

 Nota importante de implementacin: en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 ID Funcionalidad 
 cnf_emp_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= cnf_emp_datagov_cua ) 

 Label Botn Men: 
 lb_btn_cnf_emp_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_emp_datagov_cua ) 

 Label Ttulo de la Vista: 
 lb_cnf_emp_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_emp_datagov_cua ) 

 Label Descripcin de la Vista: 
 lb_cnf_emp_datagov_cua_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_emp_datagov_cua_desc ) 

 EDICIN DE DATOS BSICOS DEL CLIENTE 
 Primera sesin del usuario superadmin paso E 
 Nota importante de implementacin: en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 En esta funcionalidad se debe presentar el mismo formulario que se utiliz el el Onoboarding , pero precargando los datos del cliente segn su consulta para obtenerlos sin encripcin (decript). 

 Primera consulta para obtener los datos 
 {{URL_entorno_datagov}}/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue={{_DOM.cua_user}}&fielddecrypt=eatc_customer_fiscal_id 

 Con la respuesta obtenida se toma el eatc_customer_fiscal_id para realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/crypt/eatcloud/getcrypt?table=eatc_customers&&fieldname=eatc_fiscal_id&fieldvalue={{ eatc_customer_fiscal_id }}&fielddecrypt=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email 

 Con esto los valores desencriptados para mostrar en el formulario . 
 Ejemplo: ambiente de pruebas _DOM.cua_user = exito 

 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue=exito&fielddecrypt=eatc_customer_fiscal_id     

 Dado que la respuesta es: 

 { 
 _id : "8" , 
 eatc_country : "co" , 
 eatc_customer_fiscal_id : "890900608" , 
 eatc_cua : "a0dDNVhkOGpLMkxmeDhmL3pzTkxFQT09" 
 } 

 Entonces se toma eatc_customer_fiscal_id : "890900608" para realizar la siguiente consulta: 

 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers&&fieldname=eatc_fiscal_id&fieldvalue=890900608&fielddecrypt=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email 

 Con los datos obtenidos se popula el formulario 

 Si la anterior consulta no trae resultados, el sistema deber presentar el siguiente warning: 
 lb_cnf_emp_datagov_cua_wrn ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_cnf_emp_datagov_cua_wrn ) 

 Nota sobre la anterior imagen: solo se toma como referencia porque el formulario en esta funcionalidad por ejemplo no debe decir "3. Agrega la informacin de la empresa" sino que la debe traer para que el usuario la edite de acuerdo a su necesidad. 

 Formulario de edicin de datos del cliente 

 Los siguientes datos se guardan encriptados (utilizando los servicios de encripcin de la plataforma) 
 Con el nimo de proteger la informacin privada y confidencial que se recolecta de los clientes. 

 Razn social 
 Informacin tcnica del parmetro: eatc_customer. eatc_fiscal_name 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_fiscal_name ={{ input}} 

 Direccin 
 Informacin tcnica del parmetro: eatc_customer. eatc_address 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_address ={{ input }} 

 Ciudad 
 Informacin tcnica del parmetro: eatc_customer. eatc_city 
 Tipo de dato: string 
 Tipo de input: Selector nico con texto predictivo 
 De dnde se toman los datos del selector: 

 A partir de la seleccin anterior se debe realizar la siguiente consulta 
 https://datagov.eatcloud.info/api/{{eatc_cua. eatc_country }}/eatc_municipalities?_id=_* 

 El sistema debe colocar en el selector una sola vez cada ciudad - provincia , por lo tanto se debe hacer distinct sobre el dato eatc-city - eatc-province (estos datos son los que se muestran en el selector / teclado predictivo) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda  en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_city ={{ input }} 
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_province ={{ input }} 

 Telfono 
 Informacin tcnica del parmetro: eatc_customer. eatc_phone 
 Tipo de dato: string 
 Tipo de input: phone input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_phone ={{ input }} 

 E-mail notificaciones (en vez de usuario responsable) 
 Informacin tcnica del parmetro: eatc_customer. eatc_email 
 Tipo de dato: email 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad, email 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_email ={{ input }} 

 Nmero de empleados 
 Informacin tcnica del parmetro: eatc_customer. eatc_number_of_employees   
 Tipo de dato: string 
 Tipo de input: selector nico (se guarda encriptado) 
 Opciones del selector :  
 1 - 3 
 4 - 20 
 21 - 100 
 101 - 500 
 501 - 1500 
 1501 - 5000 
 Ms de 5000 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_customer? eatc_number_of_employees ={{ input }}} 

 ***NUEVO : Vertical de la cuenta: *** 
 Informacin tcnica del parmetro: eatc_cua. vertical   
 Tipo de dato: string 
 Tipo de input: selector nico 
 Valor por defecto: el registrado eatc_cua. vertical 
 Validacin : Ser obligatorio si no hay dato en eatc_cua. vertical . 
 Label de validacin: class= lbl_ingresa_vertical   (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_ingresa_vertical) "Por favor ingresa una vertical para tu cuenta (empresa)" 
 La informacin del selector se toma de: class={{ eatc_verticals_mt .eatc_name }} (se deber configurar para que los valores que se obtienen de la siguiente consulta, sean tratados como labels) 

 Consulta de verticales disponibles para este onboarding: 
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_verticals_mt?eatc_onboarding=1 &_distinct= eatc_name 

 Ejemplo en ambiente productivo: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?eatc_onboarding=1&_distinct= eatc_name   

 Como el sistema responde: 
 res :  
 [ 
 { 
 eatc_name : "horeca" 
 }, 
 { 
 eatc_name : "industria" 
 }, 
 { 
 eatc_name : "retail" 
 }, 
 { 
 eatc_name : "agro" 
 } 
 ], 

 Entonces los selectores se deben popular con los siguientes labels: 
 class=" horeca ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=horeca 
 class=" industria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=industria 
 class=" retail ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=retail 
 class=" agro ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=agro   

 Modal de confirmacin 
 Al seleccionar una opcin, debe salir un modal de advertencia con la siguiente informacin: 
 class= lbl_estas_seguro_cambio_vertical (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_estas_seguro_cambio_vertical )  
 "Ests seguro que deseas cambiar la vertical de tu cuenta (empresa)?" 

 Opcin SI 
 class= lbl_si ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_si )  
 Se guarda en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_cua? vertical ={{ input: {{ eatc_verticals_mt .eatc_name }} }} 

 Opcin NO 
 class= lbl_no ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_no )  
 El sistema no realiza ningn cambio, ni registro. 

 ***NUEVO : Tamao de la cuenta: *** 
 Informacin tcnica del parmetro: eatc_cua. eatc_cua_size   
 Tipo de dato: string 
 Tipo de input: Selector nico 
 Valor por defecto: el registrado eatc_cua. eatc_cua_size   
 Validacin : si se vari previamente la vertical, ser obligatorio el cambio. Si no hay dato en eatc_cua. eatc_cua_size   ser obligatorio tambin. 
 Label de validacin: class= lbl_ingresa_tamano   ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_ingresa_tamano ) "Por favor ingresa un tamao para tu cuenta, de acuerdo a tu vertical" 
 La informacin del selector se toma de class={{ eatc_cua_size_mt . eatc_code }} concatenado con {{ eatc_cua_size_mt . eatc_description_lbl }} (se deber configurar para que los valores que se obtienen de la siguiente consulta, sean tratados como labels) 

 Consulta de tamaos segn la vertical: 
 {{ URL_entorno_datagov }} /api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= {{ eatc_cua.vertical }}&eatc_onboarding=1 &_distinct= eatc_code 

 {{ URL_entorno_datagov }} /api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= {{ eatc_cua.vertical }}&eatc_onboarding=1 &_distinct= eatc_description_lbl 

 Ejemplo en ambiente productivo, para la vertical "retail": 
 https://datagov.eatcloud.info//api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= retail&eatc_onboarding=1&_distinct= eatc_code 

 Dado que la respuesta del servicio es: 
 res :  
 [ 
 { 
 eatc_code : little_retail 
 }, 
 { 
 eatc_code : "medium_retail" 
 }, 
 { 
 eatc_code : "big_retail" 
 } 
 ], 

 https://datagov.eatcloud.info//api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= retail&eatc_onboarding=1&_distinct= eatc_description_lbl   

 Dado que la respuesta del servicio es: 
 res :  
 [ 
 { 
 eatc_description_lbl : "little_retail_desc" 
 }, 
 { 
 eatc_description_lbl : "medium_retail_desc" 
 }, 
 { 
 eatc_description_lbl : "big_retail_desc" 
 } 
 ], 

 Entonces los selectores se deben popular con los siguientes labels: 
 class=" little_retail " - class=" little_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=little_retail  - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=little_retail_desc   
 class=" medium_retail " - class=" medium_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=medium_retail    - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=medium_retail_desc   
 class=" big_retail " - class=" big_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=big_retail    - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=big_retail_desc 

 Modal de confirmacin 
 Al seleccionar una opcin, debe salir un modal de advertencia con la siguiente informacin: 
 class= lbl_estas_seguro_cambio_tamao ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel= lbl_estas_seguro_cambio_tamao )  
 "Ests seguro que deseas cambiar el tamao de tu cuenta?" 

 Opcin SI 
 class= lbl_si ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_si )  
 Se guarda en (para efectos indicativos, no prcticos) :  
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_cua? eatc_cua_size ={{ input: {{ eatc_cua_size_mt . eatc_code }} }} 

 Opcin NO 
 class= lbl_no ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_no )  
 El sistema no realiza ningn cambio, ni registro. 

 Fecha y hora de ltima modificacin (captura oculta de timestamp): 
 Informacin tcnica del parmetro: eatc_customer. last_modification_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp (oculto) 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? last_modification_datetime ={{ current_datetime }} 

 Edicin de datos del contacto (cliente) ERP 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 

 Si no existan datos registrados del cliente: 
 https://datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 Si existan datos registrados del cliente: 
 https://datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 Edicin de los datos del cliente: CRM 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 

 Si no existan datos registrados del cliente: 
 https://datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 Si existan datos registrados del cliente: 
 https://datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-empresa%2F634704867-abQA5u4BKg.png&ow=928&oh=490, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfigura-tu-empresa%2F634704867-abQA5u4BKg.png&ow=928&oh=490 
 Cuentas datagov 

 314.000000000000 

 CONFIGURACIN DE TU EMPRESA