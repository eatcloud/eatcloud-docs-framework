# creación-de-cuentas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La primera versin de la creacin de cuentas EatCloud: https://datagov.eatcloud.info/eatc/new_account , deber estar vinculada desde esta funcionalidad para convertirla en una herramienta de resorte interno (sobre todo en lo referente a la creacin de entornos.  La versin revisada de creacin de cuentas en el flujo de onboarding (que ser la pblica), tendr ajustes en la UX/UI y crear ambientes solamente de productivo. 

 ","cachedEmbedCode":" ","shouldScaleWidth":true,"tempState":{},"thumbnailUrl":"","cachedEmbedCodeThumbnail":""},"containsDynamicDataSource":false}">

 FORMULARIO PARA CREACIN DE CUENTAS (DATOS MNIMOS REQUERIDOS) 

 Pas: 
 Informacin tcnica del parmetro: eatc_cua.eatc_country (***EL PARMETRO NO SE LLAMABA AS EN LA ANTERIOR VERSIN DE LA ESTRUCTURA***) eatc_cua.eatc-master_cua (***NUEVO: NO ESTABA EN LA ANTERIOR VERSIN DE LA ESTRUCTURA***)  
 Tipo de dato: string 
 Tipo de input: selector nico 
 La informacin del selector se toma de: 

 ***REVISIN data maestra y registro de datos*** 
 ***REVISAR PORQUE ESTABA APUNTANDO A UN MAESTRO EN BENEFICIARIOS Y AHORA DEBE APUNTAR A DATAGOV*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country=_* eatc_country , eatc_cua (se muestra en el selector: https://datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2={{eatc_country}} nombre) 

 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
https://datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_country={{ eatc_master_cua. eatc_country }} 
https://datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc-cua_master={{ eatc_master_cua. eatc_cua }} 

 Vertical de negocio *** NUEVO: maestro migra a datagov  y se internacionaliza***: 
 Informacin tcnica del parmetro: eatc_cua. vertical   
 Tipo de dato: string 
 Tipo de input: selector nico 
 La informacin del selector se toma de: 

 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 

 ***NUEVO: Paso 3: consulta de verticales disponibles para este onboarding: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?eatc_onboarding=1   

 El sistema toma el array de valores del parmetro eatc_verticals_mt. _id para realizar la siguiente consulta 

 Ejemplo: a 11 de noviembre de 2020: 
 el array de _id sera 4,5,6,7 

 ***NUEVO: Paso 3: consulta de las verticales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language={{codigo_dos_digitos_idioma}}& eatc_data_id={{array( eatc_verticals_mt. _id)}} 
 (Anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&onboarding=1 ) 

 Ejemplo: idioma espaol a 11 de noviembre de 2020: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language=es& eatc_data_id=4,5,6,7   

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language=en& eatc_data_id={{array( eatc_verticals_mt. eatc_code)}} 

 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en el selector   

 Ejemplo: idioma espaol a 11 de noviembre de 2020: 
 Se mostraran en el selector los valores 

Hoteles, restaurantes y casinos 
Industria 
Retail 
Sector agrcola 

 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id ={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro el valor eatc_verticales_mt. eatc_code 

 Ejemplo, continuando con el anterior 
 Si el usuario selecciona "retail" entonces eatc_internationalize_dt. eatc_data_id=6 por lo tanto al hacer la siguiente consulta: https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id=6 al registro se llevara el valor "eatc_verticales_mt. eatc_code " = "retail" 

 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua?vertical={{ eatc_verticales_mt. eatc_code }} 

 Tipo de licencia *** NUEVO: maestro migra a datagov y se internacionaliza***: 
 Informacin tcnica del parmetro: eatc_cua. type 
 Tipo de dato: string 
 Tipo de input: oculto (si el registro viene despus de un proceso de pago se coloca "hero", si no es as se coloca "free") 
 La informacin del selector se toma de: 

 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de los tipos de licencias 

 ***NUEVO: Paso 2: consulta de las licencias para generar el selector 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_types_of_licenses&eatc_language={{codigo_dos_digitos_idioma}} 
 (Anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_customer_type&type=_todos ) 

 Ejemplo: idioma espaol a 11 de noviembre de 2020: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_types_of_licenses&eatc_language=es   

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_types_of_licenses&eatc_language=en    

 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en el selector   

 Ejemplo: idioma espaol a 11 de noviembre de 2020: 
 Se mostraran en el selector los valores 

Prueba gratis 
Licencia gratis 
Licencia hero 

 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/ eatc_types_of_licenses ?_id={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro el valor eatc_verticales_mt. eatc_code 

 Ejemplo, continuando con el anterior 
 Si el usuario selecciona "licencia hero" entonces eatc_internationalize_dt. eatc_data_id=3 por lo tanto al hacer la siguiente consulta: https://datagov.eatcloud.info/api/eatcloud/ eatc_types_of_licenses ?_id=3 al registro se llevara el valor "eatc_verticales_mt. eatc_code " = " hero " 

 Valor por defecto: free 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua?type={{ eatc_customer_type. type }} 

 Nombre de la cuenta ***NUEVO: evaluar unicidad por nombre (antes se haba definido que por nombre o por pas)**** 
 tooltip: ingrese un nombre corto que lo identificar en la plataforma.  El mismo no debe tener espacios ni caracteres especiales 

 Informacin tcnica del parmetro: eatc_cua. name 
 Tipo de dato: string 
 Tipo de input: text input 
 Valor por defecto: vaco 
 Obligatoriedad : si 
 Validacin ***NUEVO*** : obligatoriedad , unicidad: no deben existir dos registros con el mismo nombre. Si alguien quiere registrar un nombre que ya est registrado, se le debe informar que el nombre no est disponible y sugerirle que registre ese mismo nombre, seguido por un _{{eatc_cua.eatc_country}} , simpre y cuando en el pas de origen no exista una cuenta con ese mismo nombre.  Si en el pas existe una cuenta con ese mismo nombre, el sistema informar que el nombre ya est siendo utilizado y que por favor cambie su nombre de cuenta. 

 Ejemplo 1 (hipottico): 
 Alguien en Brasil (iso2=br) desea registrar la cuenta " exito ", el sistema valida y ya encuentra una cuenta con ese nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.  El sistema valida si en el pas en el cual se est registrando existe una cuenta con ese mismo nombre: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&eatc_country=br y como no existe le sugiere registrar" exito_br" como nombre de cuenta alternativo para seguir adelante. 

 Ejemplo 2: 
 Alguien en Colombia (iso2=co) desea registrar la cuenta " exito ", el sistema valida y ya encuentra una cuenta con ese nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.  El sistema valida si en el pas en el cual se est registrando existe una cuenta con ese mismo nombre: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&eatc_country=co   y como si existe simplemente le dice que el nombre de cuenta ya est siendo utilizado y que debe registrar otro diferente. 

 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{ input }} 

 Datos automticos para la creacin de cuenta 
 Los siguientes datos los generar automticamente el sistema, sin que tenga que mediar intervencin humana.  Algunos de los mismos son datos por defecto que deben quedar as configurados sobre todo para una operacin inicial de la funcionalidad de creacin manual de anuncios de donacin. 

 Fecha y hora de creacin: 
 Informacin tcnica del parmetro: eatc_cua. creation_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_datetime ={{ current_datetime }} 

 Fecha de creacin: 
 Informacin tcnica del parmetro: eatc_cua. creation_date 
 Tipo de dato: date 
 Tipo de input: datestamp 
 Valor por defecto: fecha actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_date ={{ current_date }} 

 Fecha y hora de ltima modificacin: 
 Informacin tcnica del parmetro: eatc_cua. last_modification_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_datetime ={{ current_datetime }} 

 Fecha de ltima modificacin: 
 Informacin tcnica del parmetro: eatc_cua. last_modification_date 
 Tipo de dato: date 
 Tipo de input: datestamp 
 Valor por defecto: fecha actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_date ={{ current_date }} 

 eatc_dona_upl 
 Informacin tcnica del parmetro: eatc_cua. eatc_dona_upl 
 Tipo de dato: string 
 Input: "yes" 
 Valor por defecto: "yes" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_dona_upl =yes 

 multiple_donors 
 Informacin tcnica del parmetro: eatc_cua. multiple_donors 
 Tipo de dato: string 
 Input: "no" 
 Valor por defecto: "no" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? multiple_donors =no 

 edit_coordinates 
 Informacin tcnica del parmetro: eatc_cua. edit_coordinates 
 Tipo de dato: string 
 Input: "no" 
 Valor por defecto: "no" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? edit_coordinates =no 

 eatc_odds_app 
 Informacin tcnica del parmetro: eatc_cua. eatc_odds_app 
 Tipo de dato: string 
 Input: "eatc_dona_app" 
 Valor por defecto: "eatc_dona_app" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_odds_app =eatc_dona_app 

 odds_weight 
 Informacin tcnica del parmetro: eatc_cua. odds_weight 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? odds_weight =eatc_dona 

 costs 
 Informacin tcnica del parmetro: eatc_cua. costs 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? costs =eatc_dona 

 taxes 
 Informacin tcnica del parmetro: eatc_cua. taxes 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? taxes =eatc_dona 

 days_before_expiration 
 Informacin tcnica del parmetro: eatc_cua. days_before_expiration 
 Tipo de dato: integer 
 Input: "3" 
 Valor por defecto: "3" 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? days_before_expiration =3 

 Non award alert 
 Con el dato guardado en eatc_cua. name , se activa el servicio para la creacin de un "non_award_alert" realizando el siguiente llamado: 
 {{URL_entorno_donantes}}/casebd/{{eatc_cua. name }}/non_award_alert 

 CREACIN DE TABLAS NECESARIAS PARA ALTA DE CUENTA 

 Panorama actual: 
 Se realiza una creacin manual de las tablas. 

 Panorama deseado: 
 Cuando se cree la cuenta se debera realizar un proceso automtico de creacin de tablas (puede ser una serie de casedb que se activen una vez se termina de completar los datos mnimos para la creacin de la cuenta).  El proceso debera recibir un parmetro adicional ambiente_de_pruebas={{si/no}} (por defecto debe estar en "no"), que defina si las tablas se crean solo en ambiente productivo ( ambiente_de_pruebas=no ) o en ambos ambientes ( ambiente_de_pruebas=si )  

 Tablas que se deben crear 

 eatc_pods_login_history 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc-pod_id;eatc-login_datetime 

 eatc_attention_schedule 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 

 eatc_sale_schedule 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 

 eatc_sale_prd_mstr 
 Cmo se crea : se crea con datos 
 Datos (las URLs de imagen cambiarn): 

 eatc-odd_id;eatc-odd_code;eatc-odd_code_type;eatc-odd_name;eatc_odd_description;eatc_odd_image;eatc-odd_unit_weight_kg;eatc_VAT_percentage;eatc-other_taxes_percentage;eatc-contains_alergens;eatc-odd_typology_a 
 1;box_1;;Caja sorpesa de 1 KG;Caja con productos sorpresa con un peso de 1 KG; http://repograf.eatcloud.info/img/box-prd-1kg.png ;1;;;;box 
 2;box_2;;Caja sorpesa de 2 KG;Caja con productos sorpresa con un peso de 2 KG; http://repograf.eatcloud.info/img/box-prd-2kg.png ;2;;;;box 
 5;box_5;;Caja sorpesa de 5 KG;Caja con productos sorpresa con un peso de 2 KG; http://repograf.eatcloud.info/img/box-prd-5kg.png ;5;;;;box 
 10;box_10;;Caja sorpesa de 10 KG;Caja con productos sorpresa con un peso de 10 KG; http://repograf.eatcloud.info/img/box-prd-10kg.png ;10;;;;box 

 eatc_dona_return_causes 
 Cmo se crea : se crea con datos 
 Datos: 

 eatc-return_cause_code;eatc-return_cause 
 1;Avera 
 2;Prximo a vencerse 
 3;Dao en el empaque 
 4;Temporada 
 5;Donacin humanitaria 

 eatc_pods 
 Cmo se crea : Se crea sin datos 

 Vector de encabezados :  eatc-province;eatc-city;eatc-email;eatc-adress;eatc-dona_packing;eatc-lat;eatc-lon;eatc-name;eatc-country;eatc-responsable;eatc-phone;eatc-typology_a;eatc-typology_b;eatc-typology_c;password;eatc-production_date;eatc_coordinate_id;eatc-donor;eatc-donor_code;eatc-size;eatc-creation_datetime;eatc-last_modification_datetime 

 [***NUEVO***] eatc_pods_coordinates 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc-city;eatc-adress;eatc-id;eatc-lat;eatc-lon;eatc-name;eatc-country;eatc-warning;eatc-province 

 eatc_pods_typolgy_a 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc_code;eatc_name 

 eatc_pods_typolgy_b 
 Cmo se crea : Se crea sin datos 
 Vector de encabezados : eatc_code;eatc_name 

 ENVO DE CORREOS PARA CONFIGURACIN DE CRONJOBS PARA CONSOLIDACIN DE DATOS Y KPIS 
 Panorama actual: 
 Este proceso se realiza de manera manual. 

 Panorama deseado: 
 Cada vez que se cree una cuenta debera generarse un correo electrnico (que incluya correo electrnico a Tablero de Asana: ) para crear los conjobs necesarios para la correcta operacin del sistema.  Lo que es ideal a futuro es ingeniarse una manera para crear estos cronjobs de manera automtica. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE CUENTAS