# deprecado-datacrm-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos crear registros en las plataformas demos o apps para interactuar con la app de delivery. 
&#160; 
 La URL que se propone para este es&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_crm_datacrm?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= insert 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_crm_datacrm?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= update 
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
eatc_customer. eatc_fiscal_name 
eatc_customer. eatc_fiscal_id 
eatc_customer. eatc_email 
eatc_customer. eatc_phone 
eatc_customer. eatc_address 
eatc_customer. eatc_city 
eatc_customer. eatc_country 

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
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &amp;filterfield_1= _id &amp;filtervalue_1= 1 &#160; 

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

&#160; 
 Ejemplo, entorno productivo 
&#160; 
 Se recibe el siguiente llamado al servicio&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_crm_datacrm?eatc_customer=811029245&amp;_operacion= insert 
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

 Validacin previa de la existencia del contacto (cliente) ante un llamado _operacion=insert 
 Antes de realizar la creacin de un contacto, se debe proceder a utilizar el siguiente mtodo 
 https&#58;//api.datacrm.la/#6050c93f-3355-4571-a262-5a3b1db962f8 
&#160; 
 Para establecer si el cliente ya existe en el CRM.&#160; De existir el cliente en el CRM, se procede a realizar el registro de la fecha y hora de creacin en CRM en el la tabla eatc_customers y a crear el registro de su id en eatc_customers. crm_id con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/ eatcloud /?tabla= eatc_customers &amp;_operacin=update&amp; crm_id=&#123;&#123;id&#125;&#125; &amp;WHERE eatc_fiscal_id =&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Y se procede con una operacin tipo update . 
&#160; 
 Si el cliente no existe, se procede a su creacin 

 INTEGRACIN CON EL API DE DATACRM 
 Se debe consultar la documentacin , para realizar el llamado al API respectivo con los datos de sesin indicados. 

 _OPETACION=INSERT 
 Creacin del cliente 
 https&#58;//api.datacrm.la/#adabc726-5a9f-4f05-8d55-1b6ea4218b64 &#160; 
&#160; 
 Los datos que se deben enviar al API, segn la documentacin deben tener una estructura como la siguiente (se realizar referencia a la tabla y al campo de datagov.eatcloud.info/api/eatcloud donde se obtienen los datos requeridos en cada caso).&#160; 
&#160; 
 A continuacin se presenta la porcin de los datos que se deben enviar en el llamado documentado aqu (los encabezados del llamado los deber determinar el desarrollador a partir del estudio de la documentacin relacionada) 
&#160; 
 &#123;&quot;accountname&quot; &#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_name &#125;&#125; - &#123;&#123;eatc_cua. name &#125;&#125;&quot;, &quot;account_no&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125;&quot;, &quot;phone&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_phone &#125;&#125;&quot;, &quot;email&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_email &#125;&#125;&quot;, &quot;rating&quot;&#58; &quot; potencial &quot;, &quot;siccode&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125;&quot;, &quot;assigned_user_id&quot;&#58; &quot; 19x19 &quot;, &quot;createdtime&quot;&#58; &quot;eatc_customer. creation_datetime &quot;, &quot;bill_street&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_address &#125;&#125;&quot;, &quot;bill_city&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_city &#125;&#125;&quot;, &quot;bill_country&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_country &#125;&#125;&quot;, &quot;alegraid&quot;&#58; &quot;&#123;&#123;eatc_customer. erp_id &#125;&#125;&quot;&#125; 
&#160; 
 De la respuesta que trae el servicio, se toma el dato account_no para realizar el prximo registro. 
&#160; 
 Creacin del contacto 
 https&#58;//api.datacrm.la/#89d2801a-15c5-4260-a418-d4a1f643f34e &#160; 
&#160; 
 A continuacin se presenta la porcin de los datos que se deben enviar en el llamado documentado aqu (los encabezados del llamado los deber determinar el desarrollador a partir del estudio de la documentacin relacionada) 
&#160; 
 &#123;&quot;lastName&quot; &#58; &quot;&#123;&#123;bo_usuarios. nombre_usuario &#125;&#125;&quot;, &quot;phone&quot; &#58; &quot;&#123;&#123;bo_usuarios. telefono &#125;&#125;&quot;, &quot;email&quot; &#58; &quot;&#123;&#123;bo_usuarios. email &#125;&#125;&quot;, &quot;assigned_user_id&quot;&#58; &quot; 19x19 &quot;, &quot;account_id&quot; &#58; &quot;&#123;&#123; account_no &#125;&#125;&quot;; &quot;createdtime&quot;&#58; &quot;eatc_customer. creation_datetime &quot;, &quot;mailingstreet&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_address &#125;&#125;&quot;, &quot;mailingcity&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_city &#125;&#125;&quot;, &quot;mailingcountry&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_country &#125;&#125;&quot;&#125; 

 Registro de la fecha y hora de creacin en el CRM 
 Una vez se reciba una respuesta de creacin exitosa se deber proceder a realizar la siguiente edicin de datos (con el timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS de cuando se realiz la insercin exitosa) para la cuenta en cuestin y se toma el account_no que tiene la respuesta para almacenarlo en el campo crm_id 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_customers &amp;_operacion=update&amp; crm_creation_datetime =&#123;&#123; timestamp &#125;&#125;&amp;crm_id=&#123;&#123; account_no &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_customer._id&#125;&#125; 

 _OPERACION=UPDATE 
&#160; 
 Edicin del cliente 
 https&#58;//api.datacrm.la/#fe448477-c733-41e3-8b17-98d08406d953 
&#160; 
 Edicin del contacto 
 https&#58;//api.datacrm.la/#871d932f-1331-4bba-8cde-2bce23be74b2 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE INTEGRACIN CON DATA CRM