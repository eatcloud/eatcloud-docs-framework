# rd-station-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos crear registros en las plataformas demos o apps para interactuar con la app de delivery. 
&#160; 
 La URL que se propone para este es&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_mat_rdstation?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= insert 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_mat_rdstation?eatc_customer=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;&amp;_operacion= update 
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
&#160; 
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

 Validacin previa de la existencia del contacto (cliente) ante un llamado _operacion=insert 
&#160; 
 Antes de realizar la creacin de un contacto, se debe proceder a utilizar el siguiente mtodo 
&#160; 
 https&#58;//developers.rdstation.com/es/reference/contacts#methodGetDetailsemail 
&#160; 
 Para establecer si el cliente ya existe en la herramienta de automatizacin de marketing.&#160; Si el contacto ya existe se procede a realizar el registro de la fecha y hora de creacin en erp en el la tabla eatc_customers y a crear el registro de su uuid en eatc_customers. mat_id con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/ eatcloud /?tabla= eatc_customers &amp;_operacin=update&amp; mat_id=&#123;&#123;uuid&#125;&#125; &amp;WHERE eatc_fiscal_id =&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Y se procede con una operacin tipo update . 
&#160; 
 Si el cliente no existe, se procede a su creacin 

 INTEGRACIN CON EL API DE RD STATION 
 Revisar la integracin nativa antes de hacer esta implementacin&#58; 
 La siguiente implementacin puede reemplazar la necesidad de hacer esta integracin, por lo tanto hay que revisarla. 
&#160; 
 https&#58;//ayuda.datacrm.com/es/articles/2440628-integracion-con-rd-station &#160; 

 _OPERACION=INSERT 
 Creacin del contacto 
 Creacin del contacto 
 Se debe consultar la documentacin para establecer cmo realizar el registro&#58; 
&#160; 
 https&#58;//developers.rdstation.com/es/reference/contacts 
&#160; 
 El llamado al servicio de integracin sera 
&#160; 
 https&#58;//api.rd.services/platform/contacts/email&#58;&#123;&#123;bo_usuarios. email &#125;&#125; 

 Registro de la fecha y hora de creacin en el RDStation (marketing automation tool) 
 Una vez se reciba una respuesta de creacin exitososa se deber proceder a realizar la siguiente edicin de datos (con el timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS de cuando se realiz la insercin exitosa) para la cuenta en cuestin (estos campos&#58; mat_creation_datetime y mat_id &#160; no existen en la base de datos&#160; por lo tanto se deben crear 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_customers &amp;_operacion=update&amp; mat_creation_datetime =&#123;&#123; timestamp &#125;&#125;&amp;mat_id=&#123;&#123; account_no &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_customer._id&#125;&#125; 

 _OPERACION=UPDATE 
 Edicin del contacto 
 https&#58;//developers.rdstation.com/es/reference/contacts#methodPatchDetails &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE INTEGRACIN CON RD STATION