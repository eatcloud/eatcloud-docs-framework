# recuperación-de-contraseña-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo web para que un usuario que se registr y por algn motivo no pudo acceder a la aplicacin (porque olvid su contrasea), pueda, por fuera de ella, recuperar la contrasea. 
&#160; 
 URL con indicacin de la cuenta ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Se debe crear una pgina web responsive con la siguiente notacin 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/recpass/&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Que para el caso inicial&#160; ( _DOM. cua_master=abaco) &#160; en ambiente productivo ser&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/recpass/abaco&#160; 
&#160; 
 Formulario alternativo de autenticacin (con datos de fcil recordacin) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 En esta pgina se le preguntar al usuario que digite en un formulario&#160; la siguiente informacin que incorpor en su registro&#58;&#160; 
&#160; 
 NIT de la organizacin&#58; tel, obligatorio (eatc_users.organizacion) Nota&#58; en este campo se deben permitir caracteres diferentes a los numricos, porque hay nits registrados de esta manera 
 Correo electrnico usuario&#58; email, obligatorio (eatc_users.correo_electronico) 
&#160; 
 con esta informacin el sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_users? organizacion =&#123;&#123; NIT &#125;&#125;&amp; correo_electronico =&#123;&#123; email &#125;&#125;&amp;_compress 

&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente de produccin 
 El usuario con ingres el NIT&#58; 830045172-1 y el correo electrnico jdc@nodrizza.com y se est trabajando sobre la pgina de recuperacin de la cuenta &quot;abaco&quot; (https&#58;//beneficiarios.eatcloud.info/recpass/abaco) entonces la consulta es la siguiente&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/api/ abaco /eatc_users? organizacion =830045172-1&amp; correo_electronico =jdc@nodrizza.com&amp;_compress &#160; 
&#160; 
 Como el sistema entrega una respuesta vlida (cont&#58; 1) 
 &#123; 
 ts &#58; &quot;200414102717&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 res &#58; [ 
 _id &#58; &quot;1&quot;, 
 eatc-city &#58; &quot;MEDELLIN&quot;, 
 ...... 
 ] 
 &#125; 
 mem &#58; 0.31, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 le manda un correo electronico al email registrado con el vnculo al formulario de recuperacin de contrasea , con _id del registro (eatc_user) como parmetros. 
&#160; 
 Si los datos ingresados no correspondieran y la respuesta hubiera sido&#58; 
 &#123; 
 ts &#58; &quot;200414102934&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.3, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Se le debe informar al usuario que los datos ingresados no corresponden a los registrados en la plataforma y que debe intentar ingresarlos nuevamente 
&#160; 
 Formulario de recuperacin de contrasea ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 La URL del formulario deber pasar por parmetro el _id del usuario (pero de manera oculta, como se hace actualmente para ingresar a la plataforma web de beneficiarios&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/recpass/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_user?[_id] 
&#160; 
 El formulario web despliega con un campo para escribir un nuevo password y otro para confirmarlo.&#160; Si los passwords coinciden se guardan en la base de datos con el siguiente llamado&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_userss&amp;_operacion=update&amp; numero_cedula =&#123;&#123; nuevo_password &#125;&#125;&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 y se le informa al usuario que el proceso fue exitoso, redirigiendo a la landing para beneficiarios registrados&#58; https&#58;//www.eatcloud.com/beneficiarios-inscritos/ .&#160; Si la informacin no coincide, se le debe informar al usuario para que intente de nuevo. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 RECUPERACIN DE CONTRASEA BENEFICIARIOS