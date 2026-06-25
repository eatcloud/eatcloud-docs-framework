# erp-alegra-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos crear registros en las plataformas demos o apps para interactuar con la app de delivery. 
&#160; 
 La URL que se propone para este es&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ierp/eatcloud?fiscalid=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 A partir de este llamado el sistema debe realizar las siguientes operaciones&#58; 

 Lectura de los datos del cliente 
 El sistema deber realizar la siguiente lectura 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers. _id respectivo para con l realizar la siguiente consulta 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /crypt/ eatcloud /decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &amp;filterfield_1= _id &amp;filtervalue_1= &#123;&#123;eatc_customers. _id &#125;&#125; 
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
 Ejemplo&#58; ambiente de pruebas, &#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;= 811029245 
&#160; 
 Se recibe el siguiente llamado al servicio&#58; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer=811029245&amp;_operacion= insert 
&#160; 
 Entonces el sistema deber realizar el siguiente llamado&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= 811029245 &#160; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers._id= 1 y por lo tanto el sistema realiza la siguiente consulta, para obtener los datos a ingresar en el registro del ERP&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &amp;filterfield_1= _id &amp;filtervalue_1= 1 &#160;&#160; 

 Lectura de los datos del contacto 
&#160; 
 El sistema deber realizar la siguiente consulta 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_customer_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. _id respectivo para con l realizar la siguiente consulta 
 https&#58;//datagov.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;filterfield_1= _id &amp;filtervalue_1=&#123;&#123; eatc_customers_cua. _id&#125;&#125; 
&#160; 
 Con la anterior consulta se obtiene el eatc_customers_cua. eatc_cua respectivo para con l realizar la siguiente consulta 
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
 https&#58;//developer.alegra.com/docs/lista-de-contactos 
&#160; 
 Enviando para la siguiente consulta 
 https&#58;//api.alegra.com/api/v1/contacts/?query=&#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125; 
&#160; 
 Para establecer si el contacto ya existe en el ERP.&#160; De existir el cliente en el ERP, se procede a realizar el registro de la fecha y hora de creacin en erp en el la tabla eatc_customers &#160; y a crear el registro de su id en eatc_customers. erp_id con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/ eatcloud /?tabla= eatc_customers &amp;_operacin=update&amp; erp_id=&#123;&#123;id&#125;&#125; &amp;WHERE eatc_fiscal_id =&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Y se procede con una operacin tipo update. 
&#160; 
 Si el cliente no existe, se procede a su creacin . 

 INTEGRACIN CON EL API DE ALEGRA 
 Se debe consultar la documentacin, para realizar el llamado al API respectivo con las credenciales abajo documentadas 

 6505f78dbfb7dfb38bfe 

 Creacin del contacto (cliente)&#58; _operacion=insert 
 https&#58;//developer.alegra.com/docs/crear-contacto &#160; 
&#160; 
 Los datos que se deben enviar al API, segn la documentacin deben tener una estructura como la siguiente (se realizar referencia a la tabla y al campo de datagov.eatcloud.info/api/eatcloud donde se obtienen los datos requeridos en cada caso.&#160; Para realizar el registro del usuario se deber consultar el usuario tipo A que debe ser el recientemente creado de la siguiente manera&#58; 
&#160; 
 &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;name&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_name &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;identification&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;email&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_email &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;phonePrimary&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_phone &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;seller&quot;&#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot; &#58; &quot; 1 &quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;term&quot; &#58;&#160; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot; &#58; 1 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;type&quot; &#58; [&quot; client &quot;], 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;address&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;address&quot; &#58; &quot;&#123;&#123;eatc_customer. eatc_address &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;city&quot; &#58; &quot;&#123;&#123;eatc_customer. eatc_city &#125;&#125;-&#123;&#123;eatc_customer. eatc_country &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;internalContacts&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;name&quot; &#58; &quot;&#123;&#123;bo_usuarios. nombre_usuario &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;email&quot; &#58; &quot;&#123;&#123;bo_usuarios. email &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;phone&quot; &#58; &quot;&#123;&#123;bo_usuarios. telefono &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;sendNotifications&quot; &#58; &quot;&#123;&#123;bo_usuarios. notificaciones &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;], 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 

 curl -v -H &quot;Accept&#58; application/json&quot; -H &quot;Content-type&#58; application/json&quot; -X POST&#160; https&#58;//api.alegra.com/api/v1/contacts -u 'diana.alvarez@eatcloud&#58; 6505f78dbfb7dfb38bfe ' -d ' &#123;&quot;name&quot;&#58; &quot; &#123;&#123;eatc_customer. eatc_fiscal_name &#125;&#125; &quot;,&quot;identification&quot;&#58; &quot; &#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125; &quot;,&quot;email&quot;&#58; &quot; &#123;&#123;eatc_customer. eatc_email &#125;&#125; &quot;,&quot;phonePrimary&quot;&#58; &quot; &#123;&#123;eatc_customer. eatc_phone &#125;&#125; &quot;,&quot;seller&quot;&#58; &#123;&quot;id&quot; &#58; &quot; 1 &quot;&#125;,&quot;term&quot;&#58; &#123;&quot;id&quot; &#58; 1 &#125;,&quot;type&quot; &#58; [&quot; client &quot;],&quot;address&quot; &#58; &#123;&quot;address&quot; &#58; &quot; &#123;&#123;eatc_customer. eatc_address &#125;&#125; &quot;,&quot;city&quot; &#58; &quot; &#123;&#123;eatc_customer. eatc_city &#125;&#125; - &#123;&#123;eatc_customer. eatc_country &#125;&#125; &quot;&#125;,&quot;internalContacts&quot; &#58; [&#123;&quot;name&quot; &#58; &quot; &#123;&#123;bo_usuarios. nombre_usuario &#125;&#125; &quot;,&quot;email&quot; &#58; &quot; &#123;&#123;bo_usuarios. email &#125;&#125; &quot;,&quot;phone&quot; &#58; &quot; &#123;&#123;bo_usuarios. telefono &#125;&#125; &quot;,&quot;sendNotifications&quot; &#58; &quot; &#123;&#123;bo_usuarios. notificaciones &#125;&#125; &quot;&#125;],&#125; ' 
&#160; 
 Nota para la implementacin&#58; el llamado cURL no estaba presente en la documentacin , as que el mismo se document abstrayendo de otro llamado similar .&#160; Por ese motivo se deber probar si el llamado funciona y de no funcionar revisar con llamados cURL documentados en otras partes de la API, como el que se muestra a continuacin&#58; 

 Registro de la fecha y hora de creacin en el ERP 
 Una vez se reciba una respuesta 201 Creacin exitosa se deber proceder a realizar la siguiente edicin de datos (con el timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS de cuando se realiz la insercin exitosa) para la cuenta en cuestin y se toma el id que tiene la respuesta para almacenarlo en el campo erp_id 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_customers &amp;_operacion=update&amp; erp_creation_datetime =&#123;&#123; timestamp &#125;&#125;&amp;erp_id=&#123;&#123; id &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_customer._id&#125;&#125; 

 EDICIN DEL CONTACTO (CLIENTE)&#58; _OPERACION=UPDATE 
 https&#58;//developer.alegra.com/docs/editar-contacto 
&#160; 
 Con el dato registrado en eatc_customers. erp_id se procede a realizar el siguiente llamado&#58; 
&#160; 
 https&#58;//api.alegra.com/api/v1/contacts/&#123;&#123;eatc_customers. erp_id &#125;&#125; 

&#160; 
 &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;name&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_name &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;identification&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_fiscal_id &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;email&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_email &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;phonePrimary&quot;&#58; &quot;&#123;&#123;eatc_customer. eatc_phone &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;address&quot; &#58; &quot;&#123;&#123;eatc_customer. eatc_address &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;city&quot; &#58; &quot;&#123;&#123;eatc_customer. eatc_city &#125;&#125;-&#123;&#123;eatc_customer. eatc_country &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;internalContacts&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;name&quot; &#58; &quot;&#123;&#123;bo_usuarios. nombre_usuario &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;email&quot; &#58; &quot;&#123;&#123;bo_usuarios. email &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;phone&quot; &#58; &quot;&#123;&#123;bo_usuarios. telefono &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;sendNotifications&quot; &#58; &quot;&#123;&#123;bo_usuarios. notificaciones &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;], 
 &#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=45f4be94a1f148498925787566e49e20&ext=jpg&ow=812&oh=214, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=45f4be94a1f148498925787566e49e20&ext=jpg&ow=812&oh=214 

 957.000000000000 

 SERVICIOS DE INTEGRACIN CON ERP ALEGRA