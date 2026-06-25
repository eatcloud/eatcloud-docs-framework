# crm-freshworks-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del cliente y del usuario y a partir de ellos generar un registro de cuenta y de contacto en el CRM de la empresa (Freshworks). 

 La URL que se propone para este es: 
 https://datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 https://datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= update 

 A partir de este llamado el sistema debe realizar las siguientes operaciones: 

 Lectura de los datos del cliente 
 La lectura de datos del cliente funcionar de la misma manera como se estableci para el servicio de integracin con el ERP (por lo tanto se podr reciclar cdigo para esta implementacin).  Los datos que se obtienen y que servirn para el registro son los siguientes: 

 eatc_customer. eatc_fiscal_name 
 eatc_customer. eatc_fiscal_id 
 eatc_customer. eatc_email 
 eatc_customer. eatc_phone 
 eatc_customer. eatc_address 
 eatc_customer. eatc_city 
 eatc_customer. eatc_country 

 Lectura de los datos del contacto 
 La lectura de datos del cliente funcionar de la misma manera como se estableci para el servicio de integracin con el ERP (por lo tanto se podr reciclar cdigo para esta implementacin).  Los datos que se obtienen y que servirn para el registro son los siguientes: 

bo_usuarios. nombre_usuario 
bo_usuarios. email 
bo_usuarios. telefono 

 Validacin previa de la existencia del contacto (cliente) ante un llamado _operacion=insert 
 Antes de realizar la creacin de un contacto, se debe proceder a utilizar el siguiente llamado CURL 

 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json " -X GET " https://eatcloud-team.myfreshworks.com/crm/sales /api/sales_accounts/{{eatc_customer. eatc_fiscal_id }} " 

 Para establecer si el contacto ya existe en el CRM.  De existir el cliente en el CRM, se procede a realizar el registro de la fecha y hora de creacin en CRM ( crm_creation_datetime ) en el la tabla eatc_customers   y a crear el registro de su id en eatc_customers. erp_id con el siguiente llamado: 

 {{ URL_entorno_datagov }}/crd/ eatcloud /?tabla= eatc_customers &_operacin=update& crm_id= {{eatc_customer. eatc_fiscal_id }} & crm_creation_datetime = {{timestamp. AAA-MM-DD }} &WHERE eatc_fiscal_id ={{eatc_customers. eatc_fiscal_id }} 

 Y se procede con una operacin tipo update. 

 Si el cliente no existe, se procede a su creacin . 

 INTEGRACIN CON EL API DE FRESHWORKS 
 Se debe consultar la documentacin , para realizar el llamado al API respectivo con las credenciales abajo documentadas 

 token= REDACTED 

 CREACIN DE LA CUENTA (CLIENTE): _OPERACION=INSERT 
 https://developers.freshworks.com/crm/api/#create_account   

 Los datos que se deben enviar al API, segn la documentacin deben tener una estructura como la siguiente (se realizar referencia a la tabla y al campo de datagov.eatcloud.info/api/eatcloud donde se obtienen los datos requeridos en cada caso.  

 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json " -d '{"sales_account":{"name":" [[eatc_customer. eatc_fiscal_name ]] ","phone":" [[eatc_customer. eatc_phone ]] ","address":" [[eatc_customer. eatc_address ]] ","city":" [[eatc_customer. eatc_city ]] ","country":" [[eatc_customer. eatc_country ]] ","custom_field":{"cf_fiscal_id":" [[eatc_customer. eatc_fiscal_id ]] "}}' -X POST " https://eatcloud-team.myfreshworks.com/ crm/sales/api/sales_accounts " 

 Nota para la implementacin: el llamado cURL no estaba presente en la documentacin , as que el mismo se document abstrayendo de otro llamado similar.  Por ese motivo se deber probar si el llamado funciona y de no funcionar revisar con llamados cURL documentados en otras partes de la API.  Se debe verificar si la respuesta al llamado de creacin devuelve el ID de la cuenta recien creada (esto no est en la documentacin).  En caso de que no lo haga, se debe consultar la documentacin para determinar un llamado de consulta del cliente recin creado ( https://developers.freshworks.com/crm/api/#view_account / https://developers.freshworks.com/crm/api/#list_all_accounts ) para consultar su ID y llevar este dato ( {{ crm_id }} ) a los registros correspondientes ( Creacin del contacto y actualizacin de datos en eatc_customers ). 

 **NUEVO : CREACIN DEL CONTACTO (DEL CLIENTE): _OPERACION=INSERT ** 
 https://developers.freshworks.com/crm/api/#create_contact   

 Los datos que se deben enviar al API, segn la documentacin deben tener una estructura como la siguiente (se realizar referencia a la tabla y al campo de datagov.eatcloud.info/api/eatcloud donde se obtienen los datos requeridos en cada caso.  Para realizar el registro del contacto se deber consultar el usuario tipo A que debe ser el recientemente creado: 

 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json " -d '{"contact": {"first_name":" [[ bo_usuarios. nombre_usuario ]] ", "email":" [[ bo_usuarios. email ]] ", "work_number":" [[ bo_usuarios. telefono ]] ", "sales_account_id":" [[ crm_id ]] "}}' -X POST " https://eatcloud-team.myfreshworks.com/ crm/sales/api/sales_accounts " 

 Nota para la implementacin: el llamado cURL no estaba presente en la documentacin , as que el mismo se document abstrayendo de otro llamado similar.  Por ese motivo se deber probar si el llamado funciona y de no funcionar revisar con llamados cURL documentados en otras partes de la API.   

 ***NUEVO: Consulta del dato "id" de la cuenta que se crea *** 
 Se debe verificar si la respuesta al llamado de creacin devuelve el ID de la cuenta recien creada (esto no est en la documentacin).  En caso de que no lo haga, se debe consultar la documentacin para determinar un llamado de consulta del cliente recin creado ( https://developers.freshworks.com/crm/api/#view_account / https://developers.freshworks.com/crm/api/#list_all_accounts ) para consultar su ID y llevar este dato ( {{ crm_id }} ) al registro correspondiente ( ms abajo descrito ). 

 Registro de la fecha y hora de creacin en el CRM 
 Una vez se reciba una respuesta de Creacin exitosa como se indica en la documentacin, se deber proceder a realizar la siguiente edicin de datos (con el timestamp en formato AAAA-MM-DD HH:MM:SS de cuando se realiz la insercin exitosa) para la cuenta en cuestin y se toma el id que tiene la respuesta para almacenarlo en el campo erp_id 

 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla= eatc_customers &_operacion=update& crm_creation_datetime = {{timestamp. AAA-MM-DD }} &crm_id= {{crm _id }} &WHERE_id={{eatc_customer. _id }} 

 EDICIN DE LA CUENTA: _OPERACION=UPDATE 
 https://developers.freshworks.com/crm/api/#update_a_account   

 Con el dato registrado en eatc_customers. crm_id se procede a realizar el siguiente llamado, segn sea el caso: 

 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json " -d '{"sales_account":{"name":" [[eatc_customer. eatc_fiscal_name ]] ","phone":" [[eatc_customer. eatc_phone ]] ","address":" [[eatc_customer. eatc_address ]] ","city":" [[eatc_customer. eatc_city ]] ","country":" [[eatc_customer. eatc_country ]] "}' -X POST " https://eatcloud-team.myfreshworks.com/ crm/sales/api/sales_accounts/ [[ crm_id ]] " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE INTEGRACIN CON EL CRM FRESHWORKS