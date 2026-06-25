# información-del-usuario-eatc_user_doma_info.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 Pop up, o pgina que muestra la informacin bsica del usuario (en este caso&#58; eatc_users y su respectivo eatc_donation_managers), para su consulta. ESTA VISTA NO TIENE AUN DISEO, ES DECIR QUE NO SE ENTREG MOCKUP 

 Ingreso a la vista&#58; 
 Se ingresa desde el botn usuario (que aparece en la parte superior derecha en el dashboard de escritorio) 

 Informacin a mostrar ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 El sistema realizar las siguientes consultas para traer la informacin a mostrar&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_users?numero_cedula=&#123;&#123;valor&#125;&#125; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;valor&#125;&#125; 
&#160; 
 La vista debe mostrar la siguiente informacin usuario&#58; 
&#160; 
 contratista &#58; (nombre) 
 numero_cedula &#58;&#160; 
 correo_electronico &#58;&#160; 
 organizacion &#58; &quot;900326456-1&quot;, 
 tipo_organizacion &#58; &quot;BdeA&quot; 
&#160; 
 Y del gestor de donaciones (eatc_donation_managers) 
&#160; 
 departamento &#58; &quot;Cundinamarca&quot;, 
 municipio &#58; &quot;Bogot&quot;, 
 organizacin &#58; &quot;ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA&quot;, 
 unidad_territorial &#58; &quot;Cll. 19 A N 32 - 50 Barrio Cundinamarca&quot;, 
 telefono1 &#58; &quot;4029305&quot;, 

&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente productivo 
&#160; 
 Para el usuario &quot;JUAN CARLOS BUITRAGO&quot; debe mostrar la siguiente informacin&#58; 
 &#160; 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174 
&#160; 
 usuario (contratista) &#58; &quot;Juan Carlos Buitrago ortiz&quot;, 
 Documento de identidad (numero_cedula) &#58; &quot;8161174&quot;, 
 correo_electronico &#58; &quot;direccion@abaco.org.co&quot;, 
 Organizacion &#58; &quot;900326456-1&quot;, 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 
 departamento &#58; &quot;Cundinamarca&quot;, 
 municipio &#58; &quot;Bogot&quot;, 
 Gestor de Donaciones (organizacin) &#58; &quot;ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA&quot;, 
 Direccin (unidad_territorial) &#58; &quot;Cll. 19 A N 32 - 50 Barrio Cundinamarca&quot;, 
 Telfono (telefono1) &#58; &quot;4029305&quot;, 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=d9902da2d36f4ccb9c53ee67a73e1ee1&ext=png&ow=48&oh=48, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=d9902da2d36f4ccb9c53ee67a73e1ee1&ext=png&ow=48&oh=48 
 EatCloud Beneficiarios 

 518.000000000000 

 INFORMACIN DEL USUARIO: EATC_USER_DOMA_INFO