# edición-de-coordenadas-de-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar la edicin de las coordenadas&#160; de los beneficiarios&#160; (eatc_donation_managers) desde la App, utilizando las capacidades GPS del dispositivo. 

 Editar coordenada 
 Acceso a la funcionalidad 
 En el men lateral de la APP beneficiarios, debe existir un acceso, para editar coordenada. 
&#160; 
 Presentacin de la coordenada actual en el mapa 
 Al ingresar a la funcionalidad, la misma debe mostrar en el mapa la ubicacin de la coordenada actual y abajo de la misma un botn que diga &quot;editar coordenada con posicin actual&quot; 
&#160; 
 Editar coordenada con posicin actual&#58; ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Al presionar este botn, se debe mostrar en un segundo mapa la coordenada que arroja el dispositivo. &#160; Una vez logre obtener coordenada y se muestre esta en el mapa, se desplegar un botn que diga &quot;reemplazar la anterior coordenada&quot;, al accionar esta opcin, el sistema debe guardar la nueva coordenada en los [parmetros] correspondientes (eatc-lat y eatc-lon) y hacer el registro en la base de datos con el llamado respectivo al CRD&#160; 
&#160; 
 Mtodo POST&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_manages &amp;_operacion=update&amp;[parametros]&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la creacin correcta de la nueva coordenada y desplegar el siguiente mensaje&#58; 
&#160; 
 &quot;Nueva coordenada correctamente registrada&quot;.&#160;&#160; 
&#160; 
 Envo de correo electrnico 
 Se deber enviar un correo electrnico al gestor de donaciones (al correo registrado en eatc_donation_managers ( correo_electronico ) y eatc_users ( correo_electronico )) que contenga la informacin de la nueva coordenada guardada (preferiblemente mostrndola en un mapa) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 EDICIN DE COORDENADAS DE BENEFICIARIOS DESDE LA APP