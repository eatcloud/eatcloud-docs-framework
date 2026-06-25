# edición-de-capacidades-de-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar nicamente la edicin de los datos de capacidad (recogida y gestin), por parte de los beneficiarios (sin tener que recorrer todo el formulario de edicin de informacin del donante. Este formulario se puede construir, copiando el formulario de edicin de datos del beneficiario y dejando solamente dos datos para ingresar&#58; capacidad de recogida por donacin en KG 
&#160; 
 Label del botn de men para ingresar 
 class=&quot; lbl_btn_editar_capacidades &quot; 
&#160; 
 Ttulo del formulario 
 class=&quot; lbl_editar_capacidades &quot; 
&#160; 
 Descripcin del formulario 
 class=&quot; lbl_editar_capacidades_desc &quot; 
&#160; 
 Campos del formulario del formulario 
 Capacidad de recogida por donacin (en KG) 
 class=&quot; lbl_actualizar_capacidad_recogida &quot; 
 Descripcin (tooltip&#58; class=&quot; lbl_actualizar_capacidad_recogida_desc &quot; )&#58; Ajusta la capacidad de recogida en KG por donacin que tiene su organizacin. 
 Informacin tcnica del parmetro&#58; eatc_donation_managers . capacidad_recogida 
 Tipo de dato&#58; varchar 
 Tipo de input&#58; number input 
 Valor por defecto&#58; el que se obtiene del parmetro eatc_donation_managers . capacidad_recogida para el gestor de donacin especfico (&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_donation_managers ? identificador_unico_registro =identificador_unico_registro 
 Obligatoriedad &#58; si 
 Validaciones &#58; obligatoriedad, diferente de 0, y validacin de lmite superior &#58; 
&#160; 
 Se debe comparar esta cifra que el usuario introduce para el campo &quot; capacidad_recogida &quot; ( Capacidad de Recogida por Donacin en Kilogramos ) para que no sea mayor al dato &quot; limite_superior_kg &quot; que arroja la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 .&#160; 
&#160; 
 Al hacer la comparacin hay dos posibilidades 
&#160; 
 El dato ingresado por el usuario es mayor al &quot; limite_superior_kg &quot;&#58; se le debe informar al usuario que el valor mximo permitido en este campo y corregir automticamente el valor introducido para que sea igual a &quot; limite_superior_kg &quot; que arroja la consulta respectiva 
&#160; 
 El dato ingresado por el usuario es menor al &quot; limite_superior_kg &quot;&#58; se realiza el registro del dato sin inconvenientes 
&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_donation_managers ? capacidad_recogida =&#123;&#123; input &#125;&#125; 

&#160; 
 Capacidad total de gestin de donaciones (en KG diarios) 
 class=&quot; lbl_actualizar_capacidad_gestion &quot; 
&#160; 
 Descripcin (tooltip&#58; class=&quot; lbl_actualizar_capacidad_gestion_desc &quot; )&#58; Ajusta la capacidad de gestin diaria en KG que tiene su organizacin. 
 Informacin tcnica del parmetro&#58; eatc_donation_managers . capacidad_gestion 
 Tipo de dato&#58; varchar 
 Tipo de input&#58; number input 
 Valor por defecto&#58; el que se obtiene del parmetro eatc_donation_managers . capacidad_gestion para el gestor de donacin especfico (&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_donation_managers ? identificador_unico_registro =identificador_unico_registro 
 Obligatoriedad &#58; si 
 Validaciones &#58; obligatoriedad, diferente de 0, y valor mximo de capacidad de gestin &#58; 
&#160; 
 Se debe comparar esta cifra que el usuario introduce para el campo &quot; capacidad_gestion &quot; ( Capacidad de Total de Gestin de Donaciones en Kilogramos por da ) para que no sea mayor al dato &quot; limite_superior_kg &quot; que arroja la siguiente consulta&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 
 &#160; 
 Al hacer la comparacin hay dos posibilidades 
&#160; 
 El dato ingresado por el usuario es mayor al &quot; limite_superior_kg &quot;&#58; se le debe informar al usuario que el valor mximo permitido en este campo y corregir automticamente el valor introducido para que sea igual a &quot; limite_superior_kg &quot; que arroja la consulta respectiva. 
&#160; 
 El dato ingresado por el usuario es menor al &quot; limite_superior_kg &quot;&#58; se realiza el registro del dato sin inconvenientes. 
&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_donation_managers ? capacidad_gestion =&#123;&#123; input &#125;&#125; 

 Botn &quot;Editar datos&quot; 
 class=&quot; lbl_editar_datos &quot; 
&#160; 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado al CRD para la incorporacin de la informacin (Mtodo POST)&#160; al registro del gestor de donaciones en cuestin (beneficiario) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion=update&amp; capacidad_recogida=&#123;&#123;input&#125;&#125;&amp;capacidad_gestion=&#123;&#123;input&#125;&#125; &amp;WHEREidentificador_unico_registro=&#123;&#123;identificador_unico_registro&#125;&#125; 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la edicin correcta de los datos del beneficiario y desplegar el siguiente mensaje&#58; 
&#160; 
 class=&quot; lbl_capacidades_doma_editados_ok &quot;&#58; Datos de capacidades del gestor de donaciones correctamente editados. 

&#160; 
 Envo de correo electrnico con los datos editados&#160; 
 Se deber enviar un correo electrnico al gestor de donaciones (al correo registrado en eatc_donation_managers ( correo_electronico ) y eatc_users ( correo_electronico )) que contenga los datos que fueron editados. Ese correo debe contener una URL a https&#58;//www.facebook.com/Eatcloud-Help-Desk-109080137438743/ 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 EDICIN DE CAPACIDADES DE BENEFICIARIOS DESDE LA APP