# edición-de-datos-de-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar la edicin de los datos de los beneficiarios&#160; (eatc_donation_managers) desde la App y con esto permitir el autosoporte (dado que hay gran proliferacin de datos de soporte solicitando edicin de datos previamente registrados). Esta funcionalidad se puede basar en gran medida en lo implementado para el Registro simple de beneficiarios 
&#160; 
 Campos para la edicin de datos ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Los campos para el registro debern ser los siguientes&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?_campos&#160;&#160; 
 https&#58;//beneficiarios.eatcloud.info/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_users?_campos.&#160;&#160; 
&#160; 
 El sistema traer los datos previamente guardados en el registro de la organizacin (eatc_donation_managers) y el usuario (eatc_user) y los dispondr en un formulario en el cual pueden ser editados en el siguiente orden (los campos que tienen en la columna &quot; Edicin &quot;, pueden ser editados. Los dems no lo sern, se pueden mostrar a nivel informativo). 
&#160; 
 Nota Importante sobre la latitud y la longitud&#58; 
 &#160;Los datos de latitud y longitud podrn ser editados pero no en esta funcionalidad, sino en una funcionalidad a parte ( edicin de coordenadas beneficiarios ) 

ONB_beneficiarios 

 Validacin de valor mximo para el dato &quot;capacidad_recogida&quot; ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 Se debe comparar esta cifra que el usuario introduce para el campo &quot; capacidad_recogida &quot; ( Capacidad de Recogida por Donacin en Kilogramos ) para que no sea mayor al dato &quot; limite_superior_kg &quot; que arroja la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 .&#160; 
&#160; 
 Al hacer la comparacin hay dos posibilidades 
&#160; 
 El dato ingresado por el usuario es mayor al &quot; limite_superior_kg &quot;&#58; se le debe informar al usuario que el valor mximo permitido en este campo y corregir automticamente el valor introducido para que sea igual a &quot; limite_superior_kg &quot; que arroja la consulta respectiva 
 El dato ingresado por el usuario es menor al &quot; limite_superior_kg &quot;&#58; se realiza el registro del dato sin inconvenientes 

&#160; 
 Validacin de valor mximo para el dato &quot;capacidad_gestion&quot; 
 Se debe comparar esta cifra que el usuario introduce para el campo &quot; capacidad_gestion &quot; ( Capacidad de Total de Gestin de Donaciones en Kilogramos por da ) para que no sea mayor al dato &quot; limite_superior_kg &quot; que arroja la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 
&#160; 
 Al hacer la comparacin hay dos posibilidades 
&#160; 
 El dato ingresado por el usuario es mayor al &quot; limite_superior_kg &quot;&#58; se le debe informar al usuario que el valor mximo permitido en este campo y corregir automticamente el valor introducido para que sea igual a &quot; limite_superior_kg &quot; que arroja la consulta respectiva. 
 El dato ingresado por el usuario es menor al &quot; limite_superior_kg &quot;&#58; se realiza el registro del dato sin inconvenientes. 

&#160; 
 Selector de departamentos y ciudades pegado a ***NUEVO*** maestro de municipalidades en datagov 
 Para realizar popular estos selectores se deben realizar dos procesos&#58; 
&#160; 
 1. NUEVO&#58; Determinacin del pas de la cuenta maestra&#58; 
&#160; 
 A partir de la consulta genrica&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 El sistema toma el dato eatc_cua_master. eatc-country &#160; para realizar la siguiente consulta. 
&#160; 
 2. Determinacin de la provincia segn el maestro eatc_municipalities respectivo 
&#160; 
 Con los datos recolectados se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/&#123;&#123;eatc_cua_master. eatc-country &#125;&#125;/eatc_municipalities?_id=_* 
&#160; 
 Los campos de ciudad ( eatc-city ) y provincia / departamento / estado ( eatc -province ) debern funcionar con texto predictivo a partir de los datos de la anterior consulta. 
&#160; 
 Botn &quot;Editar datos&quot; 
&#160; 
 Realizacin del &quot;update&quot; en la base de datos de beneficiarios ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado para la incorporacin de la informacin (Mtodo POST)&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la edicin correcta de los datos del beneficiario y desplegar el siguiente mensaje&#58; 
&#160; 
 &quot;Datos del Gestor de donaciones correctamente editados&quot;. 

&#160; 
 Envo de correo electrnico con los datos editados&#160; 
 Se deber enviar un correo electrnico al gestor de donaciones (al correo registrado en eatc_donation_managers ( correo_electronico ) y eatc_users ( correo_electronico )) que contenga los datos que fueron editados. Ese correo debe contener una URL a https&#58;//www.facebook.com/Eatcloud-Help-Desk-109080137438743/ 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FONB_beneficiarios.xlsx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FONB_beneficiarios.xlsx 

 EDICIN DE DATOS DE BENEFICIARIOS DESDE LA APP