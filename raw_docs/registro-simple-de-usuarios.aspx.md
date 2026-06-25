# registro-simple-de-usuarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar el registro usuarios a una cuenta y un identificador_unico_registro u eatc_donation_manager especfico.&#160; Es ideal que en la URL que da acceso a la funcionalidad se pase el dato &quot; identificador_unico_registro &quot; , que servir para consultar los datos de la organizacin respectiva en eatc_donation_managers lo cual traer datos bsicos de la organizacin y el formulario de registro del usuario de la siguiente manera 
&#160; 
 Registro de usuario a &quot;cuenta usuario&quot;&#160; y&#160; &quot;donation manager&quot; especfico ***Revisar dinamismo a partir de _DOM.cua_master*** 
 El registro del usuario se debe generar para una cuenta usuario especfica y un eatc_donation_manager especfico los cuales se deben informar a partir de la URL respectiva&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/registro_usuario/&#123;&#123;_DOM. cua_master &#125;&#125;/&#123;&#123; identificador_unico_registro&#125;&#125; 

&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente productivo 
 Si se va a registrar un usuario para la cuenta &quot; abaco &quot; y la organizacin &quot;ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA&quot; ( identificador_unico_registro &#58; &quot;900326456-1), se debera realizar mediante el vnculo https&#58;//beneficiarios.eatcloud.info/registro_usuario/abaco/900326456-1&#160; (en pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/registro_usuario/abaco/900326456-1 ). En una etapa posterior la app deber validar que la cuenta, en este caso &quot;colombia&quot; est registrada en datagov, es decir, que la siguiente consulta&#58; ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=abaco (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=abaco ) traiga un resultado vlido.&#160; 
&#160; 
 Campos para el registro ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Los campos para el registro debern ser los siguientes&#160;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_users?_campos 
 (se deben presentar a nivel informativo algunos datos que se consultan en &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers?_campos) 

Formulario_registro_simple_usuarios 

 Botn &quot;usuario&quot; ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado para la incorporacin de la informacin 
&#160; 
 Mtodo POST 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_users &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la creacin correcta del punto de donacin y desplegar el siguiente mensaje&#58; 
&#160; 
 &quot;Usuario correctamente registrado&quot;.&#160;&#160; 
&#160; 
 Y desplegar el siguiente html (el que est contenido en la siguiente tarea del Asana) 
&#160; 
 https&#58;//app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

&#160; 
 Envo de correo electrnico (en BO) 
 Se deber enviar un correo electrnico al gestor de donaciones (al correo registrado en eatc_donation_managers ( correo_electronico ) y eatc_users ( correo_electronico )) que contenga la informacin del html contenido en la siguiente tarea del Asana 
 https&#58;//app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FFormulario_registro_simple_usuarios.xlsx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FFormulario_registro_simple_usuarios.xlsx 

 REGISTRO SIMPLE DE USUARIOS