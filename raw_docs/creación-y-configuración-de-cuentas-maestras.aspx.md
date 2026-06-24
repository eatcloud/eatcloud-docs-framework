# creación-y-configuración-de-cuentas-maestras.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Una cuenta maestra es aquella donde confluyen en ambientes de donantes y beneficiarios, informacin necesaria para la mecnica de la plataforma, como son los anuncios de donacin, los match, algunas configuraciones regionales etc..  Por lo tanto es necesario darlas de  alta, primero mediante un formulario muy simple que guarda datos en la siguiente estructura 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 

 Y luego generando registros de datos y creacin de tablas, necesarias para el funcionamiento de la plataforma en otros pases.  A continuacin se detallan dichos procesos de creacin y configuracin automtica que se deben surtir. 

 CREACIN DE LA CUENTA MAESTRA 
 Para la creacin de la cuenta maestra se deber desplegar un formulario de las siguientes caractersticas 

 Formulario para creacin de cuentas maestras 
 La informacin que se recauda con este formulario se constituye en los  
 {{parametros_registro_cuenta_maestra}} 

 y sern los siguientes:  

 Nombre de la cuenta: 
 Tooltip: por favor digite el nombre de la cuenta maestra 
 Tipo de dato: string 
 Tipo de input: text input 
 Obligatoriedad : si 
 Validacin : obligatoriedad y unicidad en (en eatc_cua_master   no deben existir registros con el mismo nombre) 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua={{ input }} 

 Pas: 
 Tooltip: Seleccione el pas de la cuenta maestra  (si el pas no est creado, por favor ingrselo por la funcionalidad de configuracin de pases )  

 ***NOTA*** : se muestra a manera de ejemplo un vnculo a la pgina de documentacin de la funcionalidad.  El tooltip implementado deber contener un vnculo a la funcionalidad implementada. Tipo de dato: string 

 Tipo de input: selector nico 
 La informacin del selector se toma de: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_* eatc_countries. iso2 (se muestra en el selector eatc_countries. nombre ) 

 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_country ={{ eatc_countries. iso2 }} 

 Idioma: 
 Tooltip: Seleccione el idioma principal que utilizar la cuenta  (si el idioma no est creado, por favor ingrselo por la funcionalidad de configuracin de idiomas ) 

 ***NOTA*** : se muestra a manera de ejemplo un vnculo a la pgina de documentacin de la funcionalidad.  El tooltip implementado deber contener un vnculo a la funcionalidad implementada. 

 Tipo de dato: string 
 Tipo de input: selector nico 
 La informacin del selector se toma de: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* eatc_languages. iso2 (se muestra en el selector eatc_countries. name ) 

 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_eatc_main_language ={{ eatc_language. iso2 }} 

 Nmero mnimo de dgitos de la identificacin fiscal de las organizaciones sociales afiliadas: 
 Tooltip: Establezca cul es el nmero mnimo de dgitos del nmero de identificacin fiscal de las organizaciones afiliadas a la cuenta maestra.  Esta informacin nos ayudar a validar el ingreso de un dato correcto cuando se registren organizaciones en la plataforma. 
 Tipo de dato: integer 
 Tipo de input: numrico 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad, valor numrico y mayor que 0. 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_doma_id_min_digit_val ={{ input }} 

 Nmero mximo de dgitos de la identificacin fiscal de las organizaciones sociales afiliadas: 
 Tooltip: Establezca cul es el nmero mximo de dgitos del nmero de identificacin fiscal de las organizaciones afiliadas a la cuenta maestra.  Esta informacin nos ayudar a validar el ingreso de un dato correcto cuando se registren organizaciones en la plataforma. 
 Tipo de dato: integer 
 Tipo de input: numrico 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad, valor numrico y mayor o igual a eatc_cua_master. eatc_doma_id_min_digit_val . 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_doma_id_max_digit_val ={{ input }} 

 Nmero de telefnico (whatsapp) para soporte de beneficiarios (gestores de donaciones): 
 Tooltip: establezca un nmero de whatsapp con el cul se brindar soporte tcnico a las organizaciones beneficarias 
 Tipo de dato: integer 
 Tipo de input: phone_number 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin :  obligatoriedad y phone number 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_doma_wa ={{ input }} 

 Nmero de telefnico (whatsapp) para soporte de donantes 
 Tooltip: establezca un nmero de whatsapp con el cul se brindar soporte tcnico a los donantes 
 Tipo de dato: integer 
 Tipo de input: phone_number 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin :  obligatoriedad y phone number 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_donors_wa ={{ input }} 

 Valor por defecto de porcentaje de IVA para la cuenta maestra 
 Tooltip: establezca un valor que aparecer por defecto como porcentaje de IVA aplicable, al crear una donacin.  Por lo tanto elija el valor del porcentaje de IVA que ms frecuencia tenga en la creacin de donaciones de alimentos para la cuenta maestra particular. 
 Tipo de dato: integer 
 Tipo de input: numrico (dos dgitos) 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin :  obligatoriedad, entero, de 0 a 99, 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_default_VAT ={{ input }} 

 Tipo de dato para validacin de doc_id de organizaciones 
 Tooltip: establezca el tipo de dato que se utiliza para el documento de identidad de las organizaciones en la cuenta maestra particular.  Por ejemplo si dicho documento est compuesto de solmamente nmeros, seleccione "integer".  Si est compuesto por un valor alfanumrico, seleccione "sting". 
 Tipo de dato: integer 
 Tipo de input: Seleccin nica 
 Valores del selector: integer,string 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin :  obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_doma_id_datatype ={{ input }} 

 Radio para consultas geogrficas 
 Tooltip: establezca un radio en KM para las consultas geogrficas para seleccionar "Provincias / Estados / Departamentos" y "municipios" a partir de coordenadas fijadas en los mapas de registro de beneficiarios y puntos de donacin. SI el dato se deja vaco, el sistema tomar como valor por defecto un radio de 15 KM para la realizacin de dichas consultas. 
 Tipo de dato: integer 
 Tipo de input: numrico (tres dgitos) 
 Valor por defecto: vaco 
 Obligatoriedad : no 
 Validacin :  entero, de 0 a 999, 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_geo_query_radius_km ={{ input }} 

 ***NUEVO: Nmero mnimo de dgitos del documento de identidad de personas naturales: *** 
 Tooltip: Establezca cul es el nmero mnimo de dgitos del nmero de identificacin de las personas naturales en la cuenta maestra.  Esta informacin nos ayudar a validar el ingreso de un dato correcto cuando se registren organizaciones en la plataforma. 
 Tipo de dato: integer 
 Tipo de input: numrico 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad, valor numrico y mayor que 0. 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_ user_id _min_digit_val ={{ input }} 

 ***NUEVO: Nmero mximo de dgitos del documento de identidad de personas naturales: *** 
 Tooltip: Establezca cul es el nmero mximo de dgitos del nmero de identificacin de las personas naturales en la cuenta maestra.  Esta informacin nos ayudar a validar el ingreso de un dato correcto cuando se registren organizaciones en la plataforma. 
 Tipo de dato: integer 
 Tipo de input: numrico 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad, valor numrico y mayor o igual a eatc_cua_master. eatc_ user_id _min_digit_val . 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_ user_id _max_digit_val ={{ input }} 

 ***NUEVO: Tipo de dato para validacin de doc_id de personas naturales *** 
 Tooltip: establezca el tipo de dato que se utiliza para el documento de identidad de las personas naturales en la cuenta maestra particular.  Por ejemplo si dicho documento est compuesto de solmamente nmeros, seleccione "integer".  Si est compuesto por un valor alfanumrico, seleccione "string". 
 Tipo de dato: integer 
 Tipo de input: Seleccin nica 
 Valores del selector: integer,string 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin :  obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua_master? eatc_user_id_datatype ={{ input }} 

 Llamado a CRD para creacin de datos de cuenta maestra ***NUEVOS datos a incorporar*** 
 Con los parmetros incorporados en el formulario se realiza la siguiente escritura 

 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla= eatc_cua_master &_operacion= insert & eatc_cua ={{input}}& eatc_country ={{ eatc_countries. iso2 }}& eatc_eatc_main_language ={{ eatc_language. iso2 }}& eatc_doma_id_min_digit_val ={{input}}& eatc_doma_id_max_digit_val ={{input}}& eatc_doma_wa ={{input}}& eatc_donors_wa ={{input}}& eatc_default_VAT ={{ input }} & eatc_doma_id_datatype ={{ input }}& eatc_geo_query_radius_km ={{ input }} & eatc_user_id_min_digit_val ={{ input }}& eatc_user_id_max_digit_val ={{ input }}& eatc_user_id_datatype ={{ input }} 

 Una vez se reciba respuesta exitosa de la operacin de insert, se debern realizar los siguientes llamados para la creacin de las tablas necesarias para darle de alta a la cuenta: 

 {{URL_entorno_donantes}}/maestracuad/{{ eatc_cua_master . eatc_cua }} 
 {{URL_entorno_beneficiarios}}/maestracuab/{{ eatc_cua_master . eatc_cua }} => REVISAR ESTE LLAMADO PORQUE EN LA MS RECIENTE CREACIN DE CUENTA MAESTRA POR LA FUNCIONALIDAD NO FUNCION 

 En la interfaz de usuario se debe mostrar las tablas que se crearon (lo cual se toma de la respuesta de los respectivos servicios. 

 Ejemplo: ambiente de pruebas , eatc_cua_master .eatc_cua = argentina 
 Para la cuenta maestra argentina se deben realizar estos dos llamados: 

 https:// devdonantes .eatcloud.info/maestracuad/ argentina 
 https:// devbeneficiarios .eatcloud.info/maestracuab/ argentina 

 CREACIN DE TABLAS NECESARIAS PARA ALTA DE LA CUENTA MAESTRA 
 Cuando se crean los datos de la cuenta maestra se debe encadenar (un) proceso(s) automtico(s) de creacin de tablas similar a lo implementado en la creacin de tablas necesarias para alta de cuenta (usuario) .  Del anterior proceso se difiere principalmente por la caracterstica de este proceso de crear tablas en entorno donantes y entorno beneficiarios al mismo tiempo (el proceso anteriormente implementado solo creaba tablas en el entorno donantes). Al igual que el proceso anteriormente creado, este tambin debera recibir un parmetro adicional ambiente_de_pruebas={{si/no}} (por defecto debe estar en "si"), que defina si las tablas se crean en ambos ambientes ( ambiente_de_pruebas=si ) .  

 Tablas que se deben crear en entorno donantes {{URL_entorno_donantes}}/maestracuad/{{ eatc_cua_master . eatc_cua }} 

 De manera indicativa, la accin de creacin de estas tablas operara con la funcin mstr de la siguiente manera: 
 {{URL_entorno_donantes}}/mstr/{{eatc_cua_master. eatc_cua }}/{{tabla_a_crear}} 

 Las tablas a crear son las siguientes: 

 eatc_dona 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_dona_headers 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona_headers   (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_dona_header_state_history => OJO: Se est creando con campos diferentes (menos campos) que el vector de encabezados definido 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona_header_state_history 

 eatc_dona_kpi 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_kpi?_campos (en los prximos das habr adicin de campos en esta estructura para clasificaciones adicionales) 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona_kpi (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_dona_header_geo_history 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?_campos 

 eatc_odd_rejection_registry ***NUEVO: se le adiciona el campo: eatc-odd_rejection_cause_id*** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?_campos 

 eatc_pods_qualification_registry 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_pods_qualification_registry?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_pods_qualification_registry 

 eatc_pod_tag_registry 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_pod_tag_registry?_campos 

 bo_usuarios 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/bo_usuarios?_campos 

 eatc_timeout_rules ***NUEVO: se incorporaron dos nuevos registros de timeout *** 
 Cmo se crea : se crea con datos por defecto 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_timeout_rules?_campos 

 Datos: 

 eatc-code;cua;eatc-timeout_name;eatc-timeout_description;eatc-timeout_in_minutes;eatc-timeout_in_hours;eatc-timeout_from;eatc-doma_typolgy_b;eatc-since_kg;eatc-city 
 checkin_timeout;_default;checkin_timeout;Tiempo mximo para aceptar un checkin utilizando solamente la fecha y hora actual del dispositivo. A partir de este timeout se pregunta si quiere utilizar dicha fecha y hora o si desea registrar una fecha y hora diferente;60;1;eatc-programed_picking_datetime;;; 
 checkout_timeout;_default;checkout_timeout;Tiempo entre el check-in y el check-out (para generacin de alertas);20;0,3333333333333;eatc-picking_checkin_datetime;;; 
 dona_cancellation_timeout;_default;dona_cancellation_timeout;Tiempo mximo entre la generacin del anuncio y su cancelacin;2880;48;eatc-publication_datetime;;; 
 dona_global_scheduling_timeout;_default;dona_global_scheduling_timeout;Tiempo mximo entre la publicacin del anuncio de donacin y la programacin de la recogida;5760;96;eatc-publication_datetime;;; 
 dona_nng_cancellation_timeout;_default;dona_nng_cancellation_timeout;Tiempo mximo entre la generacin del anuncio y su cancelacin para mercanca de terceros;5760;96;eatc-publication_datetime;;; 
 dona_particular_scheduling_timeout;_default;dona_particular_scheduling_timeout;Tiempo mximo entre la adjudicacin del anuncio y su programacin;60;1;eatc-adjudication_datetime;;; 
 eatc_doma_typolgy_b1;_default;eatc_doma_typolgy_b;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 1;0;0;eatc-publication_datetime;1;20; 
 eatc_doma_typolgy_b2;_default;eatc_doma_typolgy_b;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 2;120;2;eatc-publication_datetime;2;20; 
 eatc_doma_typolgy_b3;_default;eatc_doma_typolgy_b;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 3;140;2,33333333333333;eatc-publication_datetime;3;20; 
 eatc_doma_typolgy_b4;_default;eatc_doma_typolgy_b;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 4;140;2,33333333333333;eatc-publication_datetime;4;20; 
 eatc_doma_typolgy_b5;_default;eatc_doma_typolgy_b;Tiempo entre la generacin de un anuncio y el match para organizaciones (eatc_donation_managers) cuyo eatc_typology_b es igual a 5;120;2;eatc-publication_datetime;5;20; 
 non_award_alert;_default;non_award_alert;Alerta cuando un anuncio no ha sido adjudicado despus de un tiempo prudente;180;3;eatc-publication_datetime;;; 
 non_picking_alert;_default;non_picking_alert;Alerta cuando un anuncio no ha sido recogido despu├s de un tiempo prudente posterior a la hora programada;60;1;eatc-programed_picking_datetime;;; 
 sale_timeout;_default;sale_timeout;Tiempo mximo para vender un producto de ltimo minuto;1440;24;eatc-publication_datetime;;0; 
 verification_timeout;_default;verification_timeout;Tiempo entre el check-out y la verificacin (para generacin de alertas);120;2;eatc-picking_checkout_datetime;;; 
 def_dona_release_from_scheduled;_default;dona_release_from_scheduled;Tiempo mnimo para liberar una donacin a partir de la fecha de la fecha y hora de recogida programada;1440;24;eatc-programed_picking_datetime;;; 
 def_dona_release_from_cancelled;_default;dona_release_from_cancelled;Tiempo mximo para liberar una donacin a partir de la fecha de la fecha y hora de cancelacion;60000;1000;eatc-cancellation_datetime;;; 
 def_dona_management_timeout;_default;dona_management_timeout;Tiempo mximo entre la salida del punto de donacin y la verificacin de dicho anuncio;1440;24;eatc-picking_checkout_datetime;!1;; 
 def_dona_pickup_timeout;_default;dona_pickup_timeout;Tiempo mximo entre la programacin de recogida de un anuncio y su recogida real;480;8;eatc-programed_picking_datetime;!1;; 

 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_timeout_rules 

 eatc_certification_supports_headers 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certification_supports_headers?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_certification_supports_headers (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_certification_supports_details 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certification_supports_details?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_certification_supports_details (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_certification_products_details 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certification_products_details?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_certification_products_details (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_dona_certifications 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_certifications?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona_certifications (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 ***NUEVO: Relacin certificados soportes eatc_certifications_supports *** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certifications_supports?_campos   

 ***NUEVO: Registro de aprobaciones de certificados eatc_certification_approval_registry *** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certification_approval_registry?_campos   

 ***NUEVO: Registro de desaprobaciones de certificados eatc_certification_disapproval_registry *** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_certification_disapproval_registry?_campos   

 ***NUEVO: Firmas certificados eatc_dona_certifications_sgs *** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://donantes.eatcloud.info/api/abaco/eatc_dona_certifications_sgs?_campos   

 Tablas que se deben crear en entorno beneficiario {{URL_entorno_beneficiarios}}/maestracuab/{{ eatc_cua_master . eatc_cua }} 
 De manera indicativa, la accin de creacin de estas tablas operara con la funcin mstr de la siguiente manera: 
 {{URL_entorno_beneficiarios}}/mstr/{{eatc_cua_master. eatc_cua }}/{{tabla_a_crear}} 

 Las tablas a crear son las siguientes: 

 eatc_donation_managers 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_donation_managers (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_users 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_users?_campos 

 eatc_final_beneficiaries_lt 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_final_beneficiaries_lt (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_match_registry 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?_campos 
 ndices: eatc_indexes .eatc_key: https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_match_registry (se deben crear los de primera prioridad dejando que los de segunda prioridad sean creados siempre y cuando las restricciones de la base de datos lo permitan) 

 eatc_doma_tag_registry 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_tag_registry?_campos 

 eatc_doma_typology_a 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_typology_a?_campos 

 eatc_doma_typology_b  
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_typology_b?_campos   

 eatc_max_fibe_x_doma 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_max_fibe_x_doma?_campos 

 eatc_max_fibe_x_doma_typology_b 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_max_fibe_x_doma_typology_b?_campos 

 eatc_max_kg_x_doma_typology_b 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_max_kg_x_doma_typology_b?_campos 

 eatc_age_groups 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_age_groups?_campos 

 ***NUEVO: eatc_doma_messages *** 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_messages?_campos   

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN Y CONFIGURACIN DE CUENTAS MAESTRAS EATCLOUD