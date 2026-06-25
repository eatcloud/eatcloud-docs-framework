# registro-de-usuario.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Metodologa de autenticacin 
 API de consulta&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?_campos &#160;&#160; 
&#160; 
 Usuarios (eatc_users) disponibles&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?numero_documento=_* &#160; 
&#160; 
 El usuario digita en el campo &quot;nombre de usuario&quot; su &quot;correo_electronico&quot; y en el campo &quot;contrasea&quot; su &quot;numero_cedula&quot; . Con estos datos debe utilizar el API respectiva y realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?correo_electronico=[valor]&amp;numero_documento=[valor] 
&#160; 
 Ejemplo&#58; 
 El usuario Juan Carlos, cuyo &quot;correo_electronico&quot; = juan@eatcloud.com y &quot;numero_cedula&quot;= 8161174 , la consulta sera para una autenticacin correcta&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?correo_electronico=juan@eatcloud.com&amp;numero_documento=8161174 &#160; 

 Trminos del servicio 

 La pantalla de autenticacin presenta un vnculo a los &quot;terminos del servicio&quot;, que ser una vista en donde se muestra esta informacin.&#160; Es ideal que esta informacin se consulte de manera remota (a fin de poder hacer modificaciones a dichos trminos sin tener que realizar cambios en la App). 

 Botn&#58; Registrate 
 Si el usuario no est registrado, podr acceder a un formulario que capture los siguientes campos &#58; 
&#160; 

 _id &#58; identificador nico del donante&#58; cdigo que genera la App para identificar de manera nica a todos los usuarios que se registran a travs de la App. Es un dato obligatorio que lo genera la automticamente la App. tipo de dato&#58; string. 
&#160; 
 fecha_inicio_la_atencin_o_vinculacion &#58; fecha y hora del dispositivo (current date). Es un dato obligatorio y lo debe colocar automticamente la App. Tipo de dato&#58; datetime. 

 tipo_documento &#58; selector con las siguientes opciones&#58; cdula, tarjeta de identidad, cdula de extranjeria, nit. Es un dato obligatorio. Tipo de dato&#58; string. 
 numero_documento&#58; es un dato obligatorio. Tipo de dato&#58; string. 
 primer_nombre &#58; es un dato obligatorio. Tipo de dato&#58; string. 
 segundo_nombre &#58; opcional. Tipo de dato&#58; string. 
 primer_apellido &#58; es un dato obligatorio. Tipo de dato&#58; string. 
 segundo_apellido &#58; es un dato opcional. Tipo de dato&#58; string. 
 edad &#58; es un dato opcional.&#160; Tipo de dato&#58; integer. 
 sexo &#58; es un dato opcional. Tipo de dato&#58; string. 
 municipio_residencia &#58; texto predictivo con los datos de los municipios de Colombia que se pueden consultar mediante el API (parmetro&#58; nombre_municipio)&#58; https&#58;//donantes.eatcloud.info/api/data/municipios_colombia?nombre_municipio=_* . 
 numero_telefonico &#58; es un dato opcional.&#160; Tipo de dato&#58; integer. 
 correo_electronico &#58; es un dato obligatorio. Tipo de dato&#58; email. 

&#160; 
 Escritura de datos en estructura para almacenar datos de voluntarios (eatc_volunteers) 
 Escritura con la API&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_volunteers &amp;_operacion=insert&amp; fecha_inicio_la_atencin_o_vinculacion =[valor]&amp; tipo_documento =[valor]&amp; numero_documento =[valor]&amp; primer_nombre =[valor]&amp; segundo_nombre =[valor]&amp; primer_apellido =[valor]&amp; segundo_apellido =[valor]&amp; edad =[valor]&amp; sexo =[valor]&amp; municipio_residencia =[valor]&amp; numero_telefonico =[valor]&amp; correo_electronico =[valor]&amp; lugar_voluntariado=ND&amp;dias=ND&amp;horario=0 
&#160; 
 Ejemplo&#58; 
 Un voluntario escribi los siguentes datos el 2019-10-24 11&#58;11&#58;11 
&#160; 
 tipo_documento &#58; cdula 
 numero_documento&#58; 71773955 
 primer_nombre &#58; Jorge 
 segundo_nombre &#58; William 
 primer_apellido &#58; Correa 
 segundo_apellido &#58; Toro 
 edad &#58; 43 
 sexo &#58; masculino 
 municipio_residencia &#58; Medelln 
 numero_telefonico &#58; 3113581681 
 correo_electronico &#58; jorgecorrea@nodrizza.com 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_volunteers &amp;_operacion=insert&amp; fecha_inicio_la_atencin_o_vinculacion = 2019-10-24%2011&#58;11&#58;11 &amp; tipo_documento = cdula &amp; numero_documento = 71773955 &amp; primer_nombre = Jorge &amp; segundo_nombre = William &amp; primer_apellido = Correa &amp; segundo_apellido =Toro&amp; edad =43&amp; sexo =masculino&amp; municipio_residencia =Medelln&amp; numero_telefonico =3113581682&amp; correo_electronico = jorgecorrea@nodrizza.com&amp; lugar_voluntariado=ND&amp;dias=ND&amp;horario=0 
&#160; 
 Nota &#58; los valores lugar_voluntariado y das se envan como ND (no disponible) y horario=0 
 Nota&#58; si se desean probar nuevos registros se pueden variar los datos para hacer pruebas. 
&#160; 
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
 El usuario registrado se puede consultar en https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?numero_documento=71773955 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-de-usuario%2F2428092745-7-login--eatc_alim_aut---1-.png&ow=750&oh=1336, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-de-usuario%2F2428092745-7-login--eatc_alim_aut---1-.png&ow=750&oh=1336 
 App usuario final - Alimentatn 

 759.000000000000 

 REGISTRO DE USUARIO