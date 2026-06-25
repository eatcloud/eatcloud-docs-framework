# donantes-recuperacion-de-contraseña.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 URL con indicacin de la cuenta 
 Se debe crear una pgina web responsive con la siguiente notacin 
 https&#58;//donantes.eatcloud.info/recpass/&#123;&#123;CUA_user&#125;&#125; 
&#160; 
 Que para el caso inicial ser&#58; 

 https&#58;//donantes.eatcloud.info/recpass/colombia &#160; 
&#160; 
 Formulario alternativo de autenticacin (con datos de fcil recordacin) 
 En esta pgina se le preguntar al usuario que digite en un formulario&#160; la siguiente informacin que incorpor en su registro&#58;&#160; 
&#160; 
 Telfono&#58; tel, obligatorio (eatc-phone) 
 Correo electrnico&#58; email, obligatorio (eatc-email) 
&#160; 
 con esta informacin el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/ [cua] /eatc_pods?eatc-phone= [Tlefono] &amp;eatc-email= [email] &amp;_compress 
&#160; 
 Ejemplo&#58; 
 El usuario con ingres el telfono&#58; 5744441274 y el correo electrnico soporte@nodrizza.com y se est trabajando sobre la pgina de recuperacin de la cuenta &quot;colombia&quot; ( ttps&#58;//donantes.eatcloud.info/recpass/colombia ) entonces la consulta es la siguiente&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/colombia/eatc_pods?eatc-phone=5744441274&amp;eatc-email=soporte@nodrizza.com 
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
 El sistema le permite seguir con la recuperacin, es decir, se despliega el formulario de recuperacin de contrasea , guardando el _id del registro.&#160; Si los datos ingresados no correspondieran y la respuesta hubiera sido&#58; 
&#123; 
 ts &#58; &quot;200414102934&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.3, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
&#125; 
 Se le debe informar al usuario que los datos ingresados no corresponden a los registrados en la plataforma y que debe intentar ingresarlos nuevamente 
&#160; 
 Formulario de recuperacin de contrasea 
 Una vez el usuario se autentique con datos de fcil recordacin, se le brindar un formulario web con un campo para escribir un nuevo password y otro para confirmarlo.&#160; Si los passwords coinciden se &quot;hashean&quot; para ser guardados en la base de datos con el siguiente llamado 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/colombia/?_tabla=eatc_pods&amp;_operacion=update&amp;password= [password_hasheado] &amp;WHERE_id=[_id] 
&#160; 
 y se le informa al usuario que el proceso fue exitoso, redirigiendo a la pgina de autenticacin segura de la plataforma.&#160; Si la informacin no coincide, se le debe informar al usuario para que intente de nuevo. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 RECUPERACIN DE CONTRASEA (DONANTES)