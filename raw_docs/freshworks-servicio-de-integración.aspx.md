# freshworks-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos crear registros en las plataformas demos o apps para interactuar con la app de delivery. 
&#160; 
 La URL que se propone para este es&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= insert 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= update 
&#160; 
 A partir de este llamado el sistema debe realizar las siguientes operaciones&#58; 

 Lectura de los datos del cliente 
 El sistema deber realizar la siguiente lectura 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers. _id respectivo para con l realizar la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &amp;filterfield_1= _id &amp;filtervalue_1= &#123;&#123;eatc_customers. _id &#125;&#125; 
&#160; 
 Y con el llamado se obtienen los siguientes datos&#160; desencriptados para realizar posteriormente el llamado al API respectivo 
&#160; 
eatc_customer. eatc_fiscal_name 
eatc_customer. eatc_fiscal_id 
eatc_customer. eatc_email 
eatc_customer. eatc_phone 
eatc_customer. eatc_address 
eatc_customer. eatc_city 
eatc_customer. eatc_country 
eatc_customer. eatc_number_of_employees 
eatc_customer. crm_id 

&#160; 
 Ejemplo&#58; 
&#160; 
 Se recibe el siguiente llamado al servicio&#58; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer=811029245&amp;_operacion= insert 
&#160; 
 Entonces el sistema deber realizar el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= 811029245 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers._id= 1 y por lo tanto el sistema realiza la siguiente consulta, para obtener los datos a ingresar en el registro del ERP&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &amp;filterfield_1= _id &amp;filtervalue_1= 1 
&#160; 
 Definicin del nmero de empleados para registro en el CRM 
 De acuerdo al resultado que trae el parmetro eatc_customer. eatc_number_of_employees y al respectivo rango que define la siguiente tabla se debe definir el number_of_employees_value para llevar en el registro del cliente o cuenta que se detallar ms adelante. 
&#160; 
 rango&#160; &#160; &#160;&#160; number_of_employees_value 
 &quot;1-10&quot; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; 1 
 &quot;11-50&quot; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 11 
 &quot;51-200&quot;&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 51 
 &quot;201-500&quot;&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 201 
 &quot;501-1000&quot;&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; 501 
 &quot;1001-5000&quot; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 1001 
 &quot;5001-10000&quot;&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 5001 
 &quot;10000+&quot;&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;&#160; 10001 

 Lectura de los datos del contacto 
 El sistema deber realizar la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_customer_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. _id respectivo para con l realizar la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;filterfield_1= _id &amp;filtervalue_1=&#123;&#123; eatc_customers_cua. _id&#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. eatc_cua respectivo para con l realizar la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_customers_cua. eatc_cua&#125;&#125;/bo_usuarios?tipousuario=A&#160; 
&#160; 
 Nota al 14/12/2020&#58; el campo bo_usuarios. notificaciones no est creado aun en esta tabla bo_usuarios y debe crearse mediante el proceso automtico ) 

&#160; 
 Y con el llamado se obtienen los siguientes datos&#160; para realizar posteriormente el llamado al API respectivo&#58; 
bo_usuarios. nombre_usuario 
bo_usuarios. email 
bo_usuarios. telefono 
bo_usuarios. notificaciones 
bo_usuarios. eatc_user_profile 
&#160; 
 Ejemplo, entorno productivo 
&#160; 
 Se recibe el siguiente llamado al servicio&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer=811029245&amp;_operacion= insert 
&#160; 
 Entonces el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_customer_fiscal_id &amp;fieldvalue=811029245 &#160; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. _id=6 y por lo tanto se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;filterfield_1= _id &amp;filtervalue_1=6 &#160; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. eatc_cua= colombia por lo tanto se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/colombia/bo_usuarios?tipousuario=A 

 Credenciales para acceso al API de Freshworks (pendiente generacin del API Key) 
 API Key&#58; 
 &#123;&#123;API_Key&#125;&#125; (pendiente de generacin) 
&#160; 
 Dominio&#58; 
 &#123;&#123;dominio_eatcloud_freshworks&#125;&#125; (pendiente de definicin) 
&#160; 
 Mtodos CRUD&#58; 
 &#123;&#123;METODO_ CRUD&#125;&#125;&#160; 
 GET &#58; Consulta 
 POST &#58; Insercin 
 PUT &#58; Edicin (update) 
 DELETE &#58; Borrado 
&#160; 
 Mtodos a utilizar&#58; 
 &#123;&#123;METODO&#125;&#125;&#160; 
 contacts &#58; Contactos 
 sales_accounts &#58; Clientes - cuentas 
&#160; 
 Llamado al API con el API Key&#58; 
 Para realizar los llamados al API se deber implementar lo siguiente 
 curl -H &quot;Authorization&#58; Token token= &#123;&#123;API_Key&#125;&#125; &quot; -H &quot;Content-Type&#58; application/json&quot; -X &#123;&#123;METODO_CRUD&#125;&#125;&#160; &#123;&#123;dominio_eatcloud_freshworks&#125;&#125; /crm/sales/api/ &#123;&#123;METODO&#125;&#125; / &#123;&#123;PARAMETRO&#125;&#125; 
&#160; 
 A partir de este llamado el sistema debe realizar las siguientes operaciones&#58; 

 Validacin previa de la existencia de de un cliente (sales_accounts) ante un llamado _operacion=insert 
 Documentacin&#58; 
 https&#58;//developers.freshworks.com/crm/api/#view_account 
&#160; 
 Para establecer si el cliente ya existe en el CRM.&#160; Se debe realizar la siguiente consulta&#58; 
&#160; 
 curl -H &quot;Authorization&#58; Token token= &#123;&#123;API_Key&#125;&#125; &quot; -H &quot;Content-Type&#58; application/json&quot; -X GET&#160; &#123;&#123;dominio_eatcloud_freshworks&#125;&#125; /crm/sales/api/ sales_accounts / &#123;&#123; eatc_customer. crm_id&#125;&#125; 
&#160; 
 De existir el cliente en el CRM, se procede a realizar el registro de la fecha y hora de creacin en CRM en el la tabla eatc_customers y a crear el registro de su id en eatc_customers. crm_id con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/ eatcloud /?tabla= eatc_customers &amp;_operaci n=update&amp; crm_id=&#123;&#123;sales_account.id&#125;&#125; &amp;WHERE eatc_fiscal_id =&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Y se procede con una operacin tipo update . 
&#160; 
 Si el cliente no existe, se procede a su creacin 

 INTEGRACIN CON EL API DE DATACRM 
 Se debe consultar la documentacin , para realizar el llamado al API respectivo con los datos de sesin indicados. 
&#160; 
 Nota con respecto a la notacin de parmetro variable 
 Desde hace un tiempo he venido utilizando corchetes dobles (por lo general &#123;&#123;tabla. parametro &#125;&#125; ) para encerrar los parmetros variables en la documentacin (dado que as lo utiliza Postman).&#160; En este punto particular se van a utilzar mejor llaves [ tabla. parametro] dado que la notacin del JSON de los siguientes llamados al API, manejan muchos corchetes y se pueden confundir si se utiliza el doble corchete de manera adicional. 

 _OPERACION=INSERT 
 Creacin del cliente&#58; 
 https&#58;//developers.freshworks.com/crm/api/#create_account 
&#160; 
 Los datos que se deben enviar al API, segn la documentacin deben tener una estructura como la siguiente (se realizar referencia a la tabla y al campo de datagov.eatcloud.info/api/eatcloud donde se obtienen los datos requeridos en cada caso).&#160; 
&#160; 
 curl -H &quot;Authorization&#58; Token token= [API_Key] &quot; -H &quot;Content-Type&#58; application/json&quot; -d '&#123;&quot;sales_account&quot;&#58;&#123;&quot;name&quot;&#58;&quot;[eatc_customer. eatc_fiscal_name ] - [eatc_cua. name ]&quot;,&quot;address&quot;&#58;&quot;[eatc_customer. eatc_address ]&quot;,&quot;city&quot;&#58;&quot;[eatc_customer. eatc_city ]&quot;,&quot;country&quot;&#58;&quot;[eatc_customer. eatc_country ]&quot;,&quot;number_of_employees&quot;&#58;&quot;[ number_of_employees_value ]&quot;,&quot;phone&quot;&#58;&quot;[eatc_customer. eatc_phone ]&quot;,&quot;custom_field&quot;&#58;&#123;&quot; eatc_fiscal_id &quot;&#58;&quot;[eatc_customer. eatc_fiscal_id ]&quot;&#125;,&quot;custom_field&quot;&#58;&#123;&quot; eatc_email &quot;&#58;&quot;[eatc_customer. eatc_email ]&quot;&#125;&#125;&#125;' -X POST &quot;[ dominio_eatcloud_freshworks ]/crm/sales/api/ sales_accounts &quot; 
&#160; 
 De la respuesta que trae el servicio, se toma el dato &quot;sales_account&quot;&#58; &#123; &quot;id&quot;&#58; (en adelante [ sales_account_id ])&#160; para realizar el prximo registro. 
&#160; 
 Creacin del contacto 
 Documentacin 
 https&#58;//developers.freshworks.com/crm/api/#create_contact 
&#160; 
 A continuacin se presenta un modelo bsico del llamado que se debe realizar&#58; 
&#160; 
 curl -H &quot;Authorization&#58; Token token= [API_Key] &quot; -H &quot;Content-Type&#58; application/json&quot; -d '&#123;&quot;contact&quot;&#58;&#123;&quot;last_name&quot;&#58;&quot;[bo_usuarios. nombre_usuario ]&quot;,&quot;job_title&quot;&#58;&quot;[bo_usuarios. eatc_user_profile ]&quot;,&quot;email&quot;&#58;&quot;[bo_usuarios. email ]&quot;,&quot;work_number&quot;&#58;&quot;[bo_usuarios. telefono ]&quot;,&quot;address&quot;&#58;&quot;[eatc_customer. eatc_address ]&quot;,&quot;city&quot;&#58;&quot;[eatc_customer. eatc_city ]&quot;,&quot;country&quot;&#58;&quot;[eatc_customer. eatc_country] &quot;,&quot;sales_accounts&quot;&#58;&#123;&quot;id&quot;&#58;[ sales_account_id ]&#125;&#125;&#125;' -X POST &quot;[ dominio_eatcloud_freshworks ]/crm/sales/api/ contacts &quot; 

 Registro de la fecha y hora de creacin en el CRM 
 Una vez se reciba una respuesta de creacin exitosa se deber proceder a realizar la siguiente edicin de datos (con el timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS de cuando se realiz la insercin exitosa) para la cuenta en cuestin y se toma el account_no que tiene la respuesta para almacenarlo en el campo crm_id 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_customers &amp;_operacion=update&amp; crm_creation_datetime =&#123;&#123; timestamp &#125;&#125;&amp;crm_id=&#123;&#123; account_no &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_customer. _id &#125;&#125; 

 _OPERACION=UPDATE 
 Edicin del cliente 
 https&#58;//developers.freshworks.com/crm/api/#update_a_account 
&#160; 
 A continuacin se presenta un modelo bsico del llamado que se debe realizar&#58; 
&#160; 
 curl -H &quot;Authorization&#58; Token token= [API_Key] &quot; -H &quot;Content-Type&#58; application/json&quot; -d '&#123;&quot;sales_account&quot;&#58;&#123;&quot;name&quot;&#58;&quot;[eatc_customer. eatc_fiscal_name ] - [eatc_cua. name ]&quot;,&quot;address&quot;&#58;&quot;[eatc_customer. eatc_address ]&quot;,&quot;city&quot;&#58;&quot;[eatc_customer. eatc_city ]&quot;,&quot;country&quot;&#58;&quot;[eatc_customer. eatc_country ]&quot;,&quot;number_of_employees&quot;&#58;&quot;[ number_of_employees_value ]&quot;,&quot;phone&quot;&#58;&quot;[eatc_customer. eatc_phone ]&quot;,&quot;custom_field&quot;&#58;&#123;&quot; eatc_fiscal_id &quot;&#58;&quot;[eatc_customer. eatc_fiscal_id ]&quot;&#125;,&quot;custom_field&quot;&#58;&#123;&quot; eatc_email &quot;&#58;&quot;[eatc_customer. eatc_email ]&quot;&#125;&#125;&#125;' -X PUT &quot;[ dominio_eatcloud_freshworks ]/crm/sales/api/ sales_accounts/[sales_account_id] &quot; 

&#160; 
 Edicin del contacto 
 https&#58;//developers.freshworks.com/crm/api/#update_a_contact 
&#160; 
 A continuacin se presenta un modelo bsico del llamado que se debe realizar&#58; 
&#160; 
 curl -H &quot;Authorization&#58; Token token= [API_Key] &quot; -H &quot;Content-Type&#58; application/json&quot; -d '&#123;&quot;contact&quot;&#58;&#123;&quot;last_name&quot;&#58;&quot;[bo_usuarios. nombre_usuario ]&quot;,&quot;job_title&quot;&#58;&quot;[bo_usuarios. eatc_user_profile ]&quot;,&quot;email&quot;&#58;&quot;[bo_usuarios. email ]&quot;,&quot;work_number&quot;&#58;&quot;[bo_usuarios. telefono ]&quot;,&quot;address&quot;&#58;&quot;[eatc_customer. eatc_address ]&quot;,&quot;city&quot;&#58;&quot;[eatc_customer. eatc_city ]&quot;,&quot;country&quot;&#58;&quot;[eatc_customer. eatc_country] &quot;,&quot;sales_accounts&quot;&#58;&#123;&quot;id&quot;&#58;[ id ]&#125;&#125;&#125;' -X PUT &quot;[ dominio_eatcloud_freshworks ]/crm/sales/api/ contacts/[contact_id] &quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE INTEGRACIN CON FRESHWORKS