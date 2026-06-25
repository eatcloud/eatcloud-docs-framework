# procesos-de-configuración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ENVIROMENTS 
 Pruebas 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-c18041c8-e224-4485-94e5-5b462b66436f &#160; 
&#160; 
 Produccin 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-866b076d-41f4-4102-aade-7f4da0d32617 &#160; 
&#160; 
 ASIGNACIN / PROGRAMACIN DIRECTA 
 Coleccin Postman&#58; 
 https&#58;//api.postman.com/collections/11174160-361e8d36-2ab6-4b4b-aa59-84195f3c566b?access_key=REDACTED &#160; 
&#160; 
 Sirve para importar la coleccin con la cual se realizan los llamados para esta configuracin 
&#160; 
 Informacin inicial para realizar el procedimiento&#58; 
 Se configura en el respectivo enviroment 
&#160; 
 Cuenta maestra&#58; 
 cua_master &#160; 
&#160; 
 Cuenta usuario&#58; 
 cua_user &#160; 
&#160; 
 Punto de donacin desde el cual se va a realizar la programacin directa&#58; 
 eatc_pod_id&#160; 

&#160; 
 Paso 1&#58; consulta de una posible programacin previa 
 Se realiza el llamado a la consulta de la asignacin directa para determinar que no exista un registrro previo. 

&#160; 
 Paso 2&#58; consulta de los datos del punto de donacin para generar variables correspondientes 
 Se realiza el llamado a la consulta de POD para la asignacin directa , con el nimo de setear las siguientes variables ( parmetro respuesta =&gt; &#123;&#123;variable seteada&#125;&#125; ) 
&#160; 
 Ciudad&#58; 
 eatc-city =&gt; &#123;&#123;eatc-city&#125;&#125; 
&#160; 
 Nombre del punto de donacin&#58; 
 eatc-name =&gt; &#123;&#123;eatc-pod_name&#125;&#125; 

&#160; 
 Paso 3&#58; consulta de los datos del beneficiario 
 Se realiza el llamado a la consulta del Gestor de Donaciones para la asignacin directa , con el nimo de setear las siguientes variables&#160; ( parmetro respuesta =&gt; &#123;&#123;variable seteada&#125;&#125; ) 
&#160; 
 Identificador nico&#58; 
 identificador_unico_registro =&gt; &#123;&#123;eatc-donation_manager_code&#125;&#125; &#160; 
&#160; 
 Nombre del gestor de donaciones&#58; 
 organizacin =&gt; &#123;&#123;eatc-donation_manager_name&#125;&#125; &#160; 
&#160; 
 Direccin del gestor de donaciones&#58; 
 unidad_territorial =&gt; &#123;&#123;eatc-donation_manager_address&#125;&#125; &#160; 
&#160; 
 Telfono del gestor de donaciones&#58; 
 telefono1 =&gt; &#123;&#123;eatc-donation_manager_phone&#125;&#125; &#160; 
&#160; 
 Tipologa &quot;a&quot; del&#160; gestor de donaciones&#58; 
 identificador =&gt; &#123;&#123;eatc-donation_manager_typology_a&#125;&#125; &#160; 
&#160; 
 Tipologa &quot;b&quot; del&#160; gestor de donaciones&#58; 
 eatc_doma_typology_b =&gt; &#123;&#123;doma_typology_b&#125;&#125; &#160; 
&#160; 
 Tipologa &quot;c&quot; del&#160; gestor de donaciones&#58; 
 tipo_organizacion =&gt; &#123;&#123;eatc-donation_manager_typology_c&#125;&#125; &#160; 

&#160; 
&#160; 
 Paso 4&#58; creacin del registro en la estructura &quot;eatc_direct_dona &quot; para la configuracin de la asignacin directa 
 Asignacin directa&#58; 
 Con las variables seteadas en los pasos 2 y 3, se procede a realizar el llamado &quot; Creacin asignacin directa &quot;&#160; para crear el registro. 
&#160; 
 Programacin directa&#58; 
 Con las variables seteadas en los pasos 2 y 3, se procede a realizar el llamado &quot; Creacin programacin directa &quot;&#160; llenando la siguiente informacin; para crear el registro. 
&#160; 
 eatc-picker_name &#58; Nombre de la persona que realizar la recoleccin. 
 eatc-picker_doc_id &#58; Documento de identidad de lapersona que realizar la recoleccin. 
 eatc-picker_license_plate &#58; Placa del vehculo que realizar la recoleccin. 
 eatc-programed_picking_time &#58; Hora de programacin de la recogida en formato HH&#58;MM&#58;SS 
&#160; 
 Paso 5&#58; consulta del registro para verificar su correcta creacin 
 Se realiza el llamado a la consulta de la asignacin directa para revisar la creacion del respectivo registro. 

 CONFIGURACIN WARNING AUTOMTICO 
&#160; 
 CREACIN&#58; Estructuras de datos&#160; 
 A continuacin se brindan vnculos en dnde se pueden bajar estructuras de datos de ejemplo, que sirven como plantillas para crear los mensajes automticos, bajando el archivo .csv, editndolo con la informacin de los puntos de donacin&#160; con&#160; mensajes automticos y con los mensajes automticos como tal y luego subindolos mediante los cargadores respectivos 
&#160; 
 Puntos de donacin con Warning automtico&#58; 
 Ejemplo&#58;&#160; 
 &#160; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods_with_aut_warning?_id=1&amp;_csv &#160; 
&#160; 
 (al descargar se debe borrar la columna _id antes de subir los nuevos datos) 
&#160; 
 Warning automtico&#58; 
 Ejemplo&#58;&#160; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_aut_warning?eatc-warning_code=1&amp;_csv &#160; 
&#160; 
 (al descargar se debe borrar la columna _id antes de subir los nuevos datos) 
&#160; 
 CREACIN&#58; subida de datos mediante cargadores 
 Puntos de donacin con Warning automtico&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/mstr/&#123;&#123;cua_user]]/eatc_pods_with_aut_warning 
&#160; 
 Ejemplo&#58;&#160; 
 &#160; https&#58;//donantes.eatcloud.info/2b7018e29de6cfedc0dbed32f57ab08f/oxxo/eatc_pods_with_aut_warning &#160; 
&#160; 
 Warning automtico&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/mstr/&#123;&#123;cua_user]]/eatc_aut_warning 
&#160; 
 Ejemplo&#58;&#160; 
 &#160; https&#58;//donantes.eatcloud.info/2b7018e29de6cfedc0dbed32f57ab08f/oxxo/eatc_aut_warning &#160; 

&#160; 
 ***PENDIENTE&#58; Coleccin Postman&#58;*** 
 https&#58;//api.postman.com/collections/11174160-361e8d36-2ab6-4b4b-aa59-84195f3c566b?access_key=REDACTED &#160; 
&#160; 
 Sirve para importar la coleccin con la cual se realizan los llamados para esta configuracin 
&#160; 
 Informacin inicial para realizar el procedimiento&#58; 
 Se configura en el respectivo enviroment 
&#160; 
 Cuenta usuario&#58; 
 cua_user&#160; 
&#160; 
 Punto de donacin desde el cual se genera el mensaje automtico&#58; 
 eatc_pod_id&#160; 

&#160; 
 Paso 1&#58; consulta de una posible programacin previa 
 Se realiza el llamado a la consulta de la asignacin directa para determinar que no exista un registrro previo. 

&#160; 
 Paso 2&#58; consulta de los datos del punto de donacin para generar variables correspondientes 
 Se realiza el llamado a la consulta de POD para la asignacin directa , con el nimo de setear las siguientes variables ( parmetro respuesta =&gt; &#123;&#123;variable seteada&#125;&#125; ) 
&#160; 
 Ciudad&#58; 
 eatc-city =&gt; &#123;&#123;eatc-city&#125;&#125; 
&#160; 
 Nombre del punto de donacin&#58; 
 eatc-name =&gt; &#123;&#123;eatc-pod_name&#125;&#125; 

&#160; 
 Paso 3&#58; consulta de los datos del beneficiario 
 Se realiza el llamado a la consulta del Gestor de Donaciones para la asignacin directa , con el nimo de setear las siguientes variables&#160; ( parmetro respuesta =&gt; &#123;&#123;variable seteada&#125;&#125; ) 
&#160; 
 Identificador nico&#58; 
 identificador_unico_registro =&gt; &#123;&#123;eatc-donation_manager_code&#125;&#125;&#160; 
&#160; 
 Nombre del gestor de donaciones&#58; 
 organizacin =&gt; &#123;&#123;eatc-donation_manager_name&#125;&#125;&#160; 
&#160; 
 Direccin del gestor de donaciones&#58; 
 unidad_territorial =&gt; &#123;&#123;eatc-donation_manager_address&#125;&#125;&#160; 
&#160; 
 Telfono del gestor de donaciones&#58; 
 telefono1 =&gt; &#123;&#123;eatc-donation_manager_phone&#125;&#125;&#160; 
&#160; 
 Tipologa &quot;a&quot; del&#160; gestor de donaciones&#58; 
 identificador =&gt; &#123;&#123;eatc-donation_manager_typology_a&#125;&#125;&#160; 
&#160; 
 Tipologa &quot;b&quot; del&#160; gestor de donaciones&#58; 
 eatc_doma_typology_b =&gt; &#123;&#123;doma_typology_b&#125;&#125;&#160; 
&#160; 
 Tipologa &quot;c&quot; del&#160; gestor de donaciones&#58; 
 tipo_organizacion =&gt; &#123;&#123;eatc-donation_manager_typology_c&#125;&#125;&#160; 
&#160; 
&#160; 
 Paso 4&#58; creacin del registro en la estructura &quot;eatc_direct_dona &quot; para la configuracin de la asignacin directa 
&#160; 
 Asignacin directa&#58; 
 Con las variables seteadas en los pasos 2 y 3, se procede a realizar el llamado &quot; Creacin asignacin directa &quot;&#160; para crear el registro. 
&#160; 
 Programacin directa&#58; 
 Con las variables seteadas en los pasos 2 y 3, se procede a realizar el llamado &quot; Creacin programacin directa &quot;&#160; llenando la siguiente informacin; para crear el registro. 
&#160; 
 eatc-picker_name &#58; Nombre de la persona que realizar la recoleccin. 
 eatc-picker_doc_id &#58; Documento de identidad de lapersona que realizar la recoleccin. 
 eatc-picker_license_plate &#58; Placa del vehculo que realizar la recoleccin. 
 eatc-programed_picking_time &#58; Hora de programacin de la recogida en formato HH&#58;MM&#58;SS 
&#160; 
 Paso 5&#58; consulta del registro para verificar su correcta creacin 
 Se realiza el llamado a la consulta de la asignacin directa para revisar la creacion del respectivo registro. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESOS DE CONFIGURACIN