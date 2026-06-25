# registro-de-usuario-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Metodologa de Registro&#58; social login 
 Se debern utilizar utilizar servicios de registro y autenticacin utilizando cuentas previamente creadas (como por ejemplo Google , Facebook , Twitter , e-mail ) que proveen plataformas como Firebase , para obtener datos bsicos para el registro a saber (lo que abajo se propone se hace sin tener mucho conocimiento de cmo funciona el mecanismo de social login.&#160; Por ese motivo se debe tomar como referencia, sabiendo por ejemplo que el campo e-mail es requerido para otro tipo de transacciones como por ejemplo las de pasarela de pagos)&#58; 
&#160; 
 e-mail 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; a partir de social login 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 

Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-email y&#160; eatc_sale_users .eatc-user_name 
&#160; 
 Password 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; a partir de social login 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 

Datos del usuario (se debe guardar hasheado)&#58; eatc_sale_users .eatc-password 
&#160; 
 Token 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; a partir de social login (esto se plantea porque se sabe que el proceso oaut genera tokens de autenticacin, pero es un simple planteamiento.&#160; Si este campo se est utilizando en el proceso de obtencin del cdigo del usuario , entonces se debe proceder de acuerdo a dicha definicin) 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar hasheado)&#58; eatc_sale_users .eatc-token 

 Trminos del servicio 

 La pantalla de autenticacin presenta un vnculo a los &quot; trminos del servicio&quot;, que ser una vista en donde se muestra esta informacin.&#160; Es ideal que esta informacin se consulte de manera remota (a fin de poder hacer modificaciones a dichos trminos sin tener que realizar cambios en la App). 

 Datos adicionales (diferentes a los que se obtienen desde el social login y del proceso de obtencin de cdigo del usuario) 
 Adicional a los datos obtenidos para la creacin del cdigo del usuario y los obtenidos en el proceso de social login , la aplicacin deber solicitar los siguientes datos adicionales&#58; 
&#160; 
 eatc-state 
 Tipo de dato &#58; cuando se realiza este registro, el usuario pasa de ser annimo a activo, por eso se guarda como constante en este punto el valor&#58; activo 
 Tipo de input de datos&#58; oculto 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario&#58; eatc_sale_users .eatc-state 

&#160; 
 Nombre completo 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario&#58; eatc_sale_users .eatc-name 

&#160; 
 Documento de identidad 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-doc_id 

&#160; 
 Direccin 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-address 

&#160; 
 Telfono 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-phone 

&#160; 
 Escritura de datos en estructura para almacenar datos de usuarios 
 Dado que se tiene un cdigo que identifica al usuario de manera annima, y otros datos que fueron recolectados en el proceso de obtencin de dicho cdigo, al obtener los dems datos de registro se realizar un update sobre el registro previamente realizado, obteniendo el cdigo que genera la app para dicho usuario y realizando con l el update. 
&#160; 
 Escritura con la API&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla= eatc_sale_users &amp;_operacion=update&amp; eatc-email =&#123;&#123;e_mail&#125;&#125;&amp; eatc-user_name =&#123;&#123;e_mail&#125;&#125;&amp; eatc-password= &#123;&#123;password&#125;&#125;&amp; eatc-token =&#123;&#123;token&#125;&#125;&amp; eatc-state =activo&amp; eatc-name =&#123;&#123;nombre_completo&#125;&#125;&amp; eatc-doc_id =&#123;&#123;doc_id&#125;&#125;&amp; eatc-address =&#123;&#123;direccion&#125;&#125;&amp; eatc-phone =&#123;&#123;telefono&#125;&#125;&amp; WHEREeatc-code =&#123;&#123;eatc-code&#125;&#125; 
 . 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;190924171428&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; &quot;15&quot;, 
 mem &#58; 0.73, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Encriptacin de datos 
 Para darle cumplimiento a disposiciones de Habeas Data, los datos de carcter personal se guardarn encriptados en nuestra base de datos, por este motivo, cuando se obtenga una respuesta satisfactoria de la escritura de los datos del usuario, y teniendo en cuenta los datos de autenticacin que se documentan aqu , se debe realizar el siguiente llamado a el servicio de encriptacin de datos&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /crypt/ eatcloud /encrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-password,eatc-doc_id,eatc-address,eatc-phone 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas, se acaba de realizar un registro de usuario, entonces el llamado al servicio debe ser el siguiente&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/ eatcloud /encrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-password,eatc-doc_id,eatc-address,eatc-phone &#160;&#160; 
&#160; 
 Como se puede observar en la siguiente consulta, los datos de dicha tabla quedan encriptados despus de correr el servicio&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud / eatc_sale_users ? eatc-code=_* 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-de-usuario-sale%2F2419802250-EmbeddedImage---2024-07-30T001541.593.jpg&ow=426&oh=872, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-de-usuario-sale%2F2419802250-EmbeddedImage---2024-07-30T001541.593.jpg&ow=426&oh=872 
 App usuario final - Sale 

 829.000000000000 

 AUTENTICACIN Y REGISTRO DE USUARIO (EATC_SALE_AUT)