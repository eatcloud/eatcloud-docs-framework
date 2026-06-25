# eatc_kms.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 PASO 1&#58; REGISTRO DE LOS DATOS EN G-DOCS&#160; 
 Para preservar la aplicacin de ambos mtodos en el futuro, es necesario que se registren los datos que se van ingresar en la hoja de G-Doc, (Hoja&#58; placas y conductores&#58; https&#58;//bit.ly/eatc_kms ) 

&#160; 
 MTODO 1&#58; DESCARGA DEL ARCHIVO 
 Descargar datos actualizados de lista negra de conductores (Hoja&#58; placas y conductores&#58; https&#58;//bit.ly/eatc_kms ) 
 Borrar la primera fila (nombre semntico de las columnas) de la hoja de datos descargada 

 3. Convertir el archivo a .csv separado por punto y coma (;) 
&#160; 
 4. Utilizar el cargador dispuesto para cargar la informacin al respectivo ambiente (haciendo truncado de datos)&#58; 
&#160; 

 Pruebas&#58; https&#58;//dev.datagov.eatcloud.info/2b7018e29de6cfedc0dbed32f57ab08f/eatcloud/eatc_kms &#160; 
&#160; 
 Produccin&#58; https&#58;//datagov.eatcloud.info/2b7018e29de6cfedc0dbed32f57ab08f/eatcloud/eatc_kms &#160; 

 MTODO 2&#58; GENERACIN DE NUIEVO REGISTRO 
 ENVIROMENTS 
 Pruebas 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-c18041c8-e224-4485-94e5-5b462b66436f &#160; 
&#160; 
 Produccin 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-866b076d-41f4-4102-aade-7f4da0d32617 &#160; 
&#160; 
 Bloqueo de usuario por lista negra 
 Coleccin Postman (Letn Warrior)&#58; 
 https&#58;//api.postman.com/collections/11174160-15dc9c25-ac5e-477c-874f-27099514283c?access_key=REDACTED &#160; 
&#160; 
 Sirve para importar la coleccin con la cual se realizan los llamados para este procedimiento 
&#160; 
 Informacin inicial para realizar el procedimiento (todos los datos son obligatorios)&#58; 
&#160; 
 Cuenta maestra&#58; 
 cua_master &#160; 
&#160; 
 Nombre&#58; 
 n0k&#160;&#160; 
&#160; 
 Documento de identidad 
 pa 
&#160; 
 Placa 
 pk 
&#160; 
 Paso 0&#58; consulta de donaciones, para obtener datos faltantes 
 Si por algn motivo no se tiene por ejemplo, la placa del conductor, se debe proceder a realizar una consulta con&#160; &quot; Consulta dona_headers &quot;, para determinar los datos faltantes y poder realizar un registro completo.&#160; Tambin conviene realizar consultas por placa o por documento solamente, para poder establecer posibles bloqueos adicionales a realizar a partir de la informacin inicial. 
&#160; 
 Paso 1&#58; consulta de un posible registro previo 
 user&#58; eatcloud 
 pass&#58; nzzn;4118869;eatc 
 &#123;&#123;URL_entorno&#125;&#125; /crypt/ &#123;&#123;CUA&#125;&#125; /getcrypt?table= &#123;&#123;table&#125;&#125; &amp;fieldname= &#123;&#123;parmetro&#125;&#125;&amp; fieldvalue= &#123;&#123;valor_desencriptado_a_consultar&#125;&#125;&amp; fielddecrypt =&#123;&#123;parmetros_a_desencriptar&#125;&#125; &#160; 

&#160; 
 Pruebas&#58; https&#58;//dev.datagov.eatcloud.info /crypt/ eatcloud /getcrypt?table= eatc_kms &amp;fieldname= pa&amp; fieldvalue= &#123;&#123;valor_documento_identidad&#125;&#125;&amp; fielddecrypt =n0k,pa,pk&#160; &#160; 
 Produccin&#58; https&#58;//datagov.eatcloud.info /crypt/ eatcloud /getcrypt?table= eatc_kms &amp;fieldname= pa&amp; fieldvalue= &#123;&#123;valor_documento_identidad&#125;&#125;&amp; fielddecrypt =n0k,pa,pk 
&#160; 
 Paso 2&#58; consulta de los datos de la lista 
 Se realiza el llamado a la consulta de lista encriptada , primordialmente para consultar el nmero de registros 
&#160; 
 Paso 3&#58; Realizacin del nuevo registro&#160; 
 Se realiza el llamado a Adicin registro lista , para realizar el nuevo registro. 

&#160; 
 VALIDACIN Y ENCRIPTACIN&#58; APLICA PARA AMBOS MTODOS 
&#160; 
 5. Verificar los datos cargados / Adicionados&#58; 

 Pruebas&#58; https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_kms?_id=_* &#160; 
&#160; 
 Produccin&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_kms?_id=_* &#160; 

&#160; 
 6. Utilizar el servicio de encriptacin de datos para encriptar la informacin requerida&#58;&#160; 
&#160; 
 Parmetros de autenticacin&#160; (informacin confidencial) 
 user&#58; eatcloud 
 pass&#58; nzzn;4118869;eatc 
&#160; 

 Pruebas&#58; https&#58;//dev.datagov.eatcloud.info /crypt/ eatcloud /encrypt?table= eatc_kms &amp;fieldname=cua_master, n0k,pa,pk &#160;&#160; 
&#160; 
 Produccin&#58; https&#58;//datagov.eatcloud.info /crypt/ eatcloud /encrypt?table= eatc_kms &amp;fieldname=cua_master, n0k,pa,pk &#160;&#160; 
&#160; 
 7 . Consultar la informacin encriptada para determinar que todo qued correctamente encriptado 
&#160; 

 Pruebas&#58; https&#58;//dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_kms&amp;filterfield_1=cua_master&amp;filtervalue_1=abaco&amp;fielddecrypt=n0k,pa,pk &#160; 
&#160; 
 Produccin&#58; https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_kms&amp;filterfield_1=cua_master&amp;filtervalue_1=abaco&amp;fielddecrypt=n0k,pa,pk &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Featc_kms%2F3686261456-borrar_primera_linea.jpg&ow=742&oh=234, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Featc_kms%2F3686261456-borrar_primera_linea.jpg&ow=742&oh=234 

 954.000000000000 

 EATC_KMS UPLOAD (ACTUALIZACIN DE DATOS)