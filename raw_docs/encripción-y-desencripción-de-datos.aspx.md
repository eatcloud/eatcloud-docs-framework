# encripción-y-desencripción-de-datos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se implementaron dos servicios que permiten encriptar y desencriptar datos en tablas de la plataforma, esto con el nimo de poder guardar de manera segura datos personales en la plataforma (encriptados en base de datos) y luego poderlos recuperar de manera legible, en capas de presentacin de datos, solo por aplicaciones que tengan parmetros de autenticacin necesarios para operar estos servicios. 
&#160; 
 Parmetros de autenticacin&#160; (informacin confidencial) 
 user&#58; eatcloud 
 pass&#58; nzzn;4118869;eatc 
&#160; 
 Acceder desde JS&#58; 
&#160; 
 Para acceder desde las Apps, se puede utilizar el siguiente script 
&#160; 
 &#160;$.ajax(&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;url&#58; &quot; https&#58;//devdonantes.eatcloud.info/crypt/abaco/decrypt?table=prueba&amp;fieldname=nom &quot;, 
 beforeSend&#58; function (xhr) &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;xhr.setRequestHeader (&quot;Authorization&quot;, &quot;Basic &quot; + btoa(&quot;eatcloud&#58;nzzn;4118869;eatc&quot;)); 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#125;).done(function (data, textStatus, jqXHR) &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;console.log(data); 
 &#125;).fail(function (jqXHR, textStatus, errorThrown) &#123;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;console.log(&quot;error&quot;); 
 &#160;&#160;&#160;&#160;&#125;); 
&#160; 
 Ideal que las claves estn en el archivo donde estn las variables globales.&#160; 

&#160; 
 ENCRIPTACIN DE DATOS 
 Llamado al servicio 
 Para realizar encriptacin de datos en la base de datos se debe llamar el siguiente servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125; /crypt/ &#123;&#123;CUA&#125;&#125; /encrypt?table= &#123;&#123;table&#125;&#125; &amp;fieldname= &#123;&#123;fieldnames_separados_por_comas&#125;&#125; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125; 
 Aplica para los entornos&#58; 
 https&#58;//donantes.eatcloud.info 
 https&#58;//devdonantes.eatcloud.info &#160; 
 https&#58;//beneficiarios.eatcloud.info &#160; 
 https&#58;//devbeneficiarios.eatcloud.info &#160; 
 https&#58;//datagov.eatcloud.info &#160; 
&#160; 
 NOTA IMPORTANTE SOBRE EL PROCESO &#58;&#160; Los datos encriptados el presente proceso no los vuelve a encriptar, solo trabaja sobre los no encriptados. 
&#160; 
 Parmetros del llamado al servicio 
 &#123;&#123;CUA&#125;&#125; 
 Nombre de la cuenta en dnde se alberga la tabla en particular. 
&#160; 
 &#123;&#123;table&#125;&#125; 
 Nombre de la tabla que se va afectar con la encriptacin de datos. 
&#160; 
 &#123;&#123;fieldanames_separados_por_comas&#125;&#125; 
 Campos de la tabla que se desea encriptar separados por comas 

&#160; 
 Ejemplos&#58; 
&#160; 
 Ejemplo 1&#58; 
 Se desea en el entorno devbeneficarios encriptar los datos nombre y cdula de la tabla prueba1 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/abaco/encrypt?table=prueba1&amp;fieldname=nombre,cedula 
&#160; 
 Como se puede observar en el llamado de API respectivo, la informacin en una consulta simple mostrar informacin encriptada&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/prueba1?nombre=_* 

&#160; 
 Ejemplo 2&#58; 
 Se desea en el entorno devbeneficarios encriptar los datos nombre y cdula de la tabla prueba2 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/encrypt?table=prueba2&amp;fieldname=nombre,cedula 
&#160; 
 Como se puede observar en el llamado de API respectivo, la informacin en una consulta simple mostrar informacin encriptada&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/prueba2?nombre=_* 
&#160; 
 Ejemplo 3&#58; 
 Se desea en el entorno datagov encriptar los datos privados&#160; de la tabla eatc_customers , entonces este sera el llamado&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/encrypt?table=eatc_customers&amp;fieldname=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email &#160; 
&#160; 
 Como se puede observar en el llamado de API respectivo, la informacin en una consulta simple mostrar informacin encriptada&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_customers?_id=_* 

 CONSULTA DE DATOS ENCRIPTADOS 
 Llamado al servicio 
 Para realizar encriptacin de datos en la base de datos se debe llamar el siguiente servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125; /crypt/ &#123;&#123;CUA&#125;&#125; /getcrypt?table= &#123;&#123;table&#125;&#125; &amp;fieldname= &#123;&#123;parmetro&#125;&#125;&amp; fieldvalue= &#123;&#123;valor_desencriptado_a_consultar&#125;&#125;&amp; fielddecrypt =&#123;&#123;parmetros_a_desencriptar&#125;&#125; 
&#160; 
 Parmetros del llamado al servicio 
 &#123;&#123;CUA&#125;&#125; 
 Nombre de la cuenta en dnde se alberga la tabla en particular. 
&#160; 
 &#123;&#123;table&#125;&#125; 
 Nombre de la tabla sobre la cual se consulta un dato que est encriptado. 
&#160; 
 &#123;&#123;parmetro&#125;&#125; 
 Campo en el cual se encuentra el valor encritpado a consultar 
&#160; 
 &#123;&#123;valor_desencriptado_a_consultar&#125;&#125; 
 Valor desencriptado que se consulta encriptado&#160; en la base de datos 
&#160; 
 ***NUEVO*** &#123;&#123;parmetros_a_desencriptar&#125;&#125; 
 El array (separado por comas) de los parmetros que se desean obtener desencriptados a partir de la consulta 
&#160; 
 Ejemplos&#58; 
&#160; 
 Ejemplo 1&#58; 
&#160; 
 Se desea en el entorno devbeneficarios se consulta si existe un &#160;&#160; eatc_email cuyo valor desencriptado es&#160; &quot;jdc@nodrizza.com&quot; , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_sale_users&amp;fieldname=eatc-email&amp;fieldvalue=%22jdc@eatcloud.com%22 
&#160; 
 Ejemplo 2&#58; 
 Se desea en el entorno devbeneficarios se consulta si existe un &#160;&#160; eatc_email cuyo valor desencriptado es&#160; &quot; jdc@nodrizza.com &quot; , y traer la informacin del nombre y el telfono desencriptada, entonces este sera el llamado&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_sale_users&amp;fieldname=eatc-email&amp;fieldvalue=%22jdc@eatcloud.com%22 &amp; fielddecrypt =eatc-name,eatc-phone &#160; 
&#160; 
 Ejemplo 3&#58; 
 Se desea en el entorno datagov se consulta si existe una en la tabla eatc_customer_cua existe&#160; eatc_cua cuyo valor desencriptado es&#160; exito , entonces este sera el llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua&amp;fieldvalue=exito &#160; 
&#160; 
 Ejemplo 4&#58; 
 Se desea en el entorno datagov se consulta si existe una en la tabla eatc_customer_cua existe&#160; eatc_cua cuyo valor desencriptado es&#160; exito , para trer su eatc_customer_fiscal_id, entonces este sera el llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua&amp;fieldvalue=exito&amp;fielddecrypt= eatc_customer_fiscal_id &#160; 

 DESENCRIPCIN DE DATOS 
 Llamado al servicio 
 Para realizar encriptacin de datos en la base de datos se debe llamar el siguiente servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125; /crypt/ &#123;&#123;CUA&#125;&#125; /decrypt?table= &#123;&#123;table&#125;&#125; &amp;fieldname= &#123;&#123;fieldnames_separados_por_comas&#125;&#125; &amp;filterfield_1= &#123;&#123;nombre_campo_para_filtrar&#125;&#125; &amp;filtervalue_1= &#123;&#123;valor_para_filtrar&#125;&#125; 
&#160; 
 Parmetros del llamado al servicio 
 &#123;&#123;CUA&#125;&#125; 
 Nombre de la cuenta en dnde se alberga la tabla en particular. 
&#160; 
 &#123;&#123;table&#125;&#125; 
 Nombre de la tabla que se va afectar con la encriptacin de datos. 
&#160; 
 &#123;&#123;fieldanames_separados_por_comas&#125;&#125; 
 Campos de la tabla que se desea encriptar separados por comas 
&#160; 
 &#123;&#123;filterfield_1&#125;&#125;&#58; opcional 
 Con el propsito de desencriptar solo una porcin de los datos, se puede enviar un nombre de campo de la tabla, por el cual aplicar un filtro 
&#160; 
 &#123;&#123;filtervalue_1&#125;&#125;&#58; opcional 
 &#160;En este parmetro se manda el valor o valores (separados por comas) del campo por el cual se quiere filtrar la respuestas 
&#160; 
 Filtros sucesivos 
 Si se desea agregar otro filtro, entonces agregue, filterfield_2 y&#160; filtervalue_2 y as sucesivamente.&#160; 

&#160; 
 Ejemplos&#58; 
 Ejemplo 1&#58; 
 Se desea en el entorno devbeneficarios desencriptar los datos nombre y cdula de la tabla prueba1 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/abaco/decrypt?table=prueba1&amp;fieldname=nombre,cedula 
&#160; 
 Ejemplo 2&#58; 
 Se desea en el entorno devbeneficarios desencriptar el dato nombre de la tabla prueba2 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=prueba2&amp;fieldname=nombre 
&#160; 
 Ejemplo 3&#58; 
 Se desea en el entorno devbeneficarios desencriptar los datos nombre y cdula &#160; de la tabla prueba1 , recuperando solamente el dato cuyo _id es 5 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/abaco/decrypt?table=prueba1&amp;fieldname=nombre,cedula,fecha&amp;filterfield_1=_id&amp;filtervalue_1=5 
&#160; 
 Ejemplo 4&#58; 
 Se desea en el entorno devbeneficarios desencriptar los datos nombre, cdula y fecha de la tabla prueba1 , recuperando solamente los datos cuyo _id es 5 y 3 , entonces este sera el llamado&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/abaco/decrypt?table=prueba1&amp;fieldname=nombre,cedula,fecha&amp;filterfield_1=_id&amp;filtervalue_1=5,3 
&#160; 
 Ejemplo 5&#58; 
 Se desea en el entorno datagov consultar los datos de la tabla eatc_customers , para un pas (eatc_country=co) y eatc_fiscal_id determinado 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_customers&amp;fieldname=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email&amp;filterfield_1=eatc_country&amp;filtervalue_1=co&amp;filterfield_2=eatc_fiscal_id&amp;filtervalue_1=890900608 &#160; 
&#160; 
 Ejemplo 6&#58; 
 Se desea en el entorno datagov consultar los datos de la tabla eatc_customers_cua , para un pas (eatc_country=co)determinado 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_customers_cua&amp;fieldname=eatc_cua,eatc_customer_fiscal_id&amp;filterfield_1=eatc_country&amp;filtervalue_1=co &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ENCRIPCIN Y DESENCRIPCIN DE DATOS