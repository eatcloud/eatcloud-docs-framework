# tu-perfil-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta vista se presentarn datos bsicos del usuario y la posibilidad de ingresar a funcionalidades tiles para la gestin de la app. Es una vista que ser evolutiva, por eso hay algunas secciones que aun no se requiere habilitar (en una primera etapa) pero que con el tiempo se podrn ir incorporando para mejorar la experiencia del usuario.&#160; El wireframe que se presenta abajo constituye una versin avanzada de la vista, por ese motivo, abajo se indicarn que elementos de esta vista son necesarios para versiones iniciales de la App, y cuales se desarrollarn con el tiempo. 
&#160; 
 Llamado para obtener la informacin del usuario 
 Dado que los datos personales se guardarn ecriptados en la base de datos, para obtener la informacin que se mostrar en esta pantalla, se requerir hacer un llamado al servicio de desencripcin de datos (teniendo en cuenta los datos de autenticacin aqu definidos), utilizando para la llamada el cdigo del usuario que se obtuvo en la funcionalidad respectiva ,&#160; de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /crypt/ eatcloud /decrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-doc_id,eatc-address,eatc-phone &amp;filterfield_1= eatc-code &amp;filtervalue_1= &#123;&#123;eatc_sale_users.eatc-code&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas para el usuario cuyo cdigo es 7777, se requiere consultar los datos para &quot;pintar&quot; la presente vista, por lo tanto el llamado al servicio deber ser&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/ eatcloud /decrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-doc_id,eatc-address,eatc-phone &amp;filterfield_1= eatc-code &amp;filtervalue_1= 7777 &#160;&#160; 

 Botn [Ayuda] (Barra de encabezado) 
 Este botn dar acceso al help desk 

 Foto&#58; 
 Primera etapa&#58; 
 Mostrar el logotipo de EatCloud 
&#160; 
 Etapas posteriores [PENDIENTE CREACIN CAMPO]&#58; 
 Deber presentar la funcionalidad de subir una imagen del usuario para guardarla en eatc_sale_users .eatc-image de la misma manera como se estn subiendo imgenes para productos en la funcionalidad de creacin de ofertas 

 &#123;&#123;Nombre de usuario&#125;&#125; 
 Mostrar el dato que se recupera en el parmetro eatc-name ,&#160; de la consulta respectiva 

 &#123;&#123;Telfono&#125;&#125; 
 Mostrar el dato que se recupera en el parmetro eatc-phone ,&#160; de la consulta respectiva 

 &#123;&#123;Correo&#125;&#125; 
 Mostrar el dato que se recupera en el parmetro eatc-email ,&#160; de la consulta respectiva 

 Botn [Editar datos de Perfil] 
 Esta pgina dar acceso a una funcionalidad para editar los datos bsicos del perfil que obtendr informacin de la consulta respectiva , permitiendo editar dichos datos para volver a escribirlos en la base de datos y encriptarlos, de la siguiente manera.&#160; Esta funcionalidad ser muy similar a la implementacin de registro de usuario , con la principal diferencia que tomar por defecto los valores previamente registrados para realizar la edicin a partir de dichos datos. 
&#160; 
 Nombre completo 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Valor por defecto &#58; el dato que se recupera en el parmetro eatc-name ,&#160; de la consulta respectiva 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario&#58; eatc_sale_users .eatc-name 

&#160; 
 Documento de identidad 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Valor por defecto &#58; el dato que se recupera en el parmetro eatc-doc_id ,&#160; de la consulta respectiva 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-doc_id 

&#160; 
 Direccin 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Valor por defecto &#58; el dato que se recupera en el parmetro eatc-address ,&#160; de la consulta respectiva 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
Datos del usuario (se debe guardar encriptado en la base de datos)&#58; eatc_sale_users .eatc-address 

&#160; 
 Telfono 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Valor por defecto &#58; el dato que se recupera en el parmetro eatc-phone ,&#160; de la consulta respectiva 
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
 &#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla= eatc_sale_users &amp;_operacion=update&amp; eatc-email =&#123;&#123;e_mail&#125;&#125;&amp; eatc-user_name =&#123;&#123;e_mail&#125;&#125;&amp; eatc-name =&#123;&#123;nombre_completo&#125;&#125;&amp; eatc-doc_id =&#123;&#123;doc_id&#125;&#125;&amp; eatc-address =&#123;&#123;direccion&#125;&#125;&amp; eatc-phone =&#123;&#123;telefono&#125;&#125;&amp; WHEREeatc-code =&#123;&#123;eatc-code&#125;&#125; 
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
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /crypt/ eatcloud /encrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-doc_id,eatc-address,eatc-phone 
&#160; 
 Ejemplo&#58; 
&#160; 
 En ambiente de pruebas, se acaba de realizar un registro de usuario, entonces el llamado al servicio debe ser el siguiente&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/ eatcloud /encrypt?table= eatc_sale_users &amp;fieldname= eatc-email,eatc-user_name,eatc-name,eatc-doc_id,eatc-address,eatc-phone &#160;&#160;&#160; 
&#160; 
 Como se puede observar en la siguiente consulta, los datos de dicha tabla quedan encriptados despus de correr el servicio&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud / eatc_sale_users ? eatc-code=_* 

 Botn [Editar datos de Acceso] (no est en el diseo del wireframe) 
&#160; 
 Primera etapa&#58; 
 No se mostrar esta funcionalidad 
&#160; 
 Etapas posteriores&#58; 
 Se deber permitir editar la seleccin de datos de acceso, que se obtuvo en esta funcionalidad , y que debe tener en cuenta procedimientos de social login. 

 Botn [Direccin para envos (solo delivery)] 
&#160; 
 Primera etapa&#58; 
 No se mostrar esta funcionalidad 
&#160; 
 Etapas posteriores&#58; 
 Permitir registrar y editar direcciones a partir de interaccin con herramientas de georeferenciacin y mapas (muy similar a lo implementado en la funcionalidad de registro de ofertas ) para guardarlas y tenerlas disponibles para configurar entregas mediante domiciliarios. 

 Botn [Tus favoritos] 
&#160; 
 Primera etapa&#58; 
 No se mostrar esta funcionalidad 
&#160; 
 Etapas posteriores&#58; 
 Permitir registrar ver productos favoritos del usuario (planteamiento aun no establecido desde lo tcnico) 

 Botn [Tus pedidos] (en el diseo est como &quot;lista de pedidos&quot;) 
 Direccionar a la funcionalidad &quot; Tus pedidos &quot;.&#160; El botn deber tener un globo que muestre la cantidad de pedidos cuyo estado sea &quot; paid_out &quot; (no est en el wireframe pero funciona de manera similar a los globos que se colocan en los botones de nube de donaciones y mis donaciones ) y que se obtendr del parmetro &quot;cont&quot; de la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers?eatc-user_code=&#123;&#123;eatc_sale_users. eatc-code&#125;&#125; &amp;eatc-state=paid_out 

 Botn [Configuracin de notificaciones] 
&#160; 
 Primera etapa&#58; 
 No se mostrar esta funcionalidad 
&#160; 
 Etapas posteriores&#58; 
 Permitir configurar notificaciones que se realizarn mediante la App (mensajes emergentes).&#160; Aun no se ha definido desde lo tcnico 

 Botn [Mtodos de pago] 
 En esta funcionalidad se debe permitir consultar, adicionar y quitar mtodos de pago que se agregan en la funcionalidad de check-out . 

 Botn [Trminos y condiciones] ***PENDIENTE VNCULO*** 
 Este botn debe direccionar a los trminos y condiciones de la plataforma. 

 Botn [Ayuda] 
 Este botn debe direccionar al centro de ayuda al siguiente vnculo&#58; https&#58;//m.me/eatcloudhelpdesk &#160;&#160; 

 Botn [Preguntas Frecuentes] ***PENDIENTE VNCULO*** 
 Este botn debe direccionar a las preguntas frecuentes 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftu-perfil-sale%2F2133876428-EmbeddedImage---2024-07-30T012713.872.jpg&ow=667&oh=1090, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftu-perfil-sale%2F2133876428-EmbeddedImage---2024-07-30T012713.872.jpg&ow=667&oh=1090 
 App usuario final - Sale 

 845.000000000000 

 TU PERFIL - SALE