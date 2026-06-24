# borrado-de-cuentas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Los siguientes labels se proponen pero como en una primera etapa no son necesarios porque el BO de EatCloud ser en espaol, entonces simplemente se coloca la clase (que no funcionar) y la etiqueta por defecto. 

 La documentacin se realiz basndonos en Postman, con los siguientes enviroments 

 Pruebas: https://go.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-c18041c8-e224-4485-94e5-5b462b66436f   
 Produccin: https://go.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-866b076d-41f4-4102-aade-7f4da0d32617   

 El JSON de la coleccin se comparte aqu 

 Selector de cuenta maestra 
 Label : class="lbl_selecciona_cua_master" Selecciona una cuenta maestra 
 Tipo de selector: Selector nico 
 El selector se construye : con la informacin que se obtiene de la siguiente consulta:  
 {{URL_datagov}} /api/eatcloud/eatc_cua_master?_id=_*&_cmp=eatc_cua 
 Validaciones : obligatoriedad 
 La cuenta maestra seleccionada se lleva a: {{ cua_master }} 

 Selector de cuenta usuario 
 Label : class="lbl_selecciona_cua_user" Selecciona una cuenta usuario 
 Tipo de selector: Selector nico 
 El selector se construye : con la informacin que se obtiene de la siguiente consulta:  
 {{URL_datagov}} /api/eatcloud/eatc_cua?eatc_cua_master= {{cua_master}} &_cmp=name 
 Validaciones : obligatoriedad 
 La cuenta usuario seleccionada se lleva a: {{ cua_user }} 

 Consulta y despliegue de los datos de la cuenta 

 Label de la seccin 
 class=lbl_datos_cua "Datos de la cuenta" 

 El sistema realiza la siguiente consulta para obtener los datos de la cuenta: 

 Consulta y visualizacin de los datos de la cuenta: 
 El sistema realiza la siguiente consulta 
 {{URL_datagov}} /api/eatcloud/eatc_cua?name= {{ cua_user }} 

 El sistema presenta los datos del cliente recibidos en el respectivo JSON (res). 

 Si la consulta no arroja resultados el sistema deber desplegar en la seccin el mensaje: 
 class=lbl_sin_resultados "Sin resultados" 

 Botn: Borrar Datos: 
 El sistema debe presentar un botn para borrar datos, cuyo valor por defecto debe ser "no" (deshabilitado) 

 Botn: Hacer Backup: 
 El sistema debe presentar un botn para hacer backup de los datos de la cuenta, cuyo valor por defecto debe ser "si" (habilitado) 

 Consulta y despliegue de los datos del cliente 
 Label de la seccin 
 class=lbl_datos_cua "Datos del cliente" 

 El sistema realiza la siguiente consulta para obtener los datos del cliente: 

 Consulta del cliente asociado a la cuenta 
 El sistema realiza la siguiente consulta 
 {{URL_datagov}} /crypt/eatcloud/getcrypt?table=eatc_customers_cua&fieldname=eatc_cua&fieldvalue= {{ cua_user }} &fielddecrypt=eatc_cua,eatc_customer_fiscal_id 

 El dato que se recibe en el parmetro eatc_customer_fiscal_id se lleva a: {{ eatc_customer_fiscal_id }} 

 Consulta y visualizacin de los datos del cliente: 
 {{URL_datagov}} /crypt/eatcloud/getcrypt?table=eatc_customers&fieldname=eatc_fiscal_id&fieldvalue= {{ eatc_customer_fiscal_id }} &fielddecrypt=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email 

 El sistema presenta los datos del cliente recibidos en el respectivo JSON (res). 

 Botn: Borrar Datos: 
 El sistema debe presentar un botn para borrar datos, cuyo valor por defecto debe ser "no" (deshabilitado) 

 Botn: Hacer Backup: 
 El sistema debe presentar un botn para hacer backup de los datos de la cuenta, cuyo valor por defecto debe ser "si" (habilitado) 

 Consulta y despliegue de los datos de puntos de donacin inscritos 
 Label de la seccin 
 class=lbl_datos_cua "Datos de puntos de donacin inscritos" 

 El sistema realiza la siguiente consulta para obtener los datos de la cuenta: 

 Consulta y visualizacin de los datos de puntos de donacin: 
 El sistema realiza la siguiente consulta 
 {{URL_datagov}} /api/eatcloud/eatc_cua?name= {{ cua_user }} 

 El sistema presenta los datos del cliente recibidos en el respectivo JSON (res). 

 Si la consulta no arroja resultados el sistema deber desplegar en la seccin el mensaje: 
 class=lbl_sin_resultados "Sin resultados" 

 Botn: Borrar Datos: 
 El sistema debe presentar un botn para borrar datos, cuyo valor por defecto debe ser "no" (deshabilitado) 

 Botn: Hacer Backup: 
 El sistema debe presentar un botn para hacer backup de los datos de la cuenta, cuyo valor por defecto debe ser "si" (habilitado) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 BORRADO DE CUENTAS