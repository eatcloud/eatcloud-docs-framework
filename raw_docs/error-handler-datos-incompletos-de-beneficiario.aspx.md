# error-handler-datos-incompletos-de-beneficiario.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En un horario nocturno, se debe correr un proceso que realice la siguiente comprobacin&#58; 
&#160; 
 Que para los anuncios cuyo estado es&#58; awarded, scheduled, delivered, received, pre-certified, certified ,&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc-state =awarded,scheduled,delivered,received,pre-certified,certified 
&#160; 
 El sistema debe verificar inicialmente que tenga un cdigo de beneficiario ( eatc-donation_manager_code )&#160; vlido (diferente de cero, nulo, vaco). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc-state =awarded,scheduled,delivered,received,pre-certified,certified &amp;eatc-donation_manager_code=_vacio 

&#160; 
 eatc-donation_manager_code en cero, vaco o nulo 
&#160; 
 Cuando el sistema detecte esta situacin, debe ir al registro de historial de estados con el cdigo del anuncio 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_header_state_history? eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &amp; eatc-log= eatc-donation_manager_code&#58; _lk 
&#160; 
 Al realizar esta consulta el sistema debe buscar si en la respuesta obtenida existe un registro en los parmetros eatc_dona_header_state_history. eatc-log que contenga en su interior un cdigo precedido de eatc-donation_manager_code&#58; si hay varios registros con un mismo cdigo, se procede a utilizar dicho cdigo para realizar el registro del cdigo del donante en el registro que tena algn problema con ese dato&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-donation_manager_code=&#123;&#123;codigo_obtenido_de_ eatc_dona_header_state_history. eatc-log&#125;&#125;&amp;WHEREeatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si se obtienen varios cdigos diferentes se debe hacer dicha actualizacin con el cdigo cuya eatc_dona_header_state_history .eatc-date_time &#160; sea ms reciente. 
&#160; 
 Posteriormente se deben consultar los datos del beneficiario con el cdigo obtenido 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro = &#123;&#123;codigo_obtenido_de_ eatc_dona_header_state_history. eatc-log&#125;&#125; &amp;_cmp=eatc-donation_manager_name,eatc-donation_manager_address,eatc-donation_manager_phone,eatc-donation_manager_typology_a,eatc-donation_manager_typology_b,eatc-donation_manager_typology_c , latitud , longitud 
&#160; 
 Y con los datos que arroja la consulta, actualizar los datos del beneficiario, de la siguiente manera&#58; 
&#160; 
 parametros_actualizacion_datos_beneficiario 
 eatc-donation_manager_name&#58; corresponde a eatc_donation_managers. organizacin 
 eatc-donation_manager_address&#58; corresponde a eatc_donation_managers. unidad_territorial 
 eatc-donation_manager_phone &#58; corresponde a eatc_donation_managers. telefono1 
 eatc-donation_manager_typology_a&#58; corresponde a eatc_donation_managers. organizacion_vinculada 
 eatc-donation_manager_typology_b&#58; corresponde a eatc_donation_managers. eatc_doma_typology_b 
 eatc-donation_manager_typology_c&#58; corresponde a eatc_donation_managers. tipo_organizacion 
&#160; 
 ***NUEVO&#58; campos pendientes por crear en eatc_dona_headers y eatc_deleted_dona_header*** 
 eatc_destination_lat&#58; corresponde a eatc_donation_managers. latitud 
 eatc_destination_lon&#58; corresponde a eatc_donation_managers. longitud 
&#160; 
 Para luego realizar la siguiente actualizacin&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; &#123;&#123;parametros_actualizacion_datos_beneficiario&#125;&#125;&amp;WHEREeatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 

 eatc-donation_manager_code existe 
&#160; 
 El sistema debe evaluar si alguno de los siguientes datos est vaco, nulo, o en cero en eatc_dona_headers&#160; 
 eatc-donation_manager_name 
 eatc-donation_manager_address 
 eatc-donation_manager_phone 
 eatc-donation_manager_typology_a 
 eatc-donation_manager_typology_b 
 eatc-donation_manager_typology_c 
&#160; 
 ***NUEVO&#58; campos pendientes por crear en eatc_dona_headers y eatc_deleted_dona_header*** 
 eatc_destination_lat 
 eatc_destination_lon 
&#160; 
 y haciendo la consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123;eatc-donation_manager_code&#125;&#125; &amp;_cmp=eatc-donation_manager_name,eatc-donation_manager_address,eatc-donation_manager_phone,eatc-donation_manager_typology_a,eatc-donation_manager_typology_b,eatc-donation_manager_typology_c , latitud , longitud 
&#160; 
 Debe proceder a realizar la actualizacin del dato o los datos que no se encontraron en el registro, as&#58; 
&#160; 
 eatc-donation_manager_name&#58; corresponde a eatc_donation_managers. organizacin 
 eatc-donation_manager_address&#58; corresponde a eatc_donation_managers. unidad_territorial 
 eatc-donation_manager_phone &#58; corresponde a eatc_donation_managers. telefono1 
 eatc-donation_manager_typology_a&#58; corresponde a eatc_donation_managers. organizacion_vinculada 
 eatc-donation_manager_typology_b&#58; corresponde a eatc_donation_managers. eatc_doma_typology_b 
 eatc-donation_manager_typology_c&#58; corresponde a eatc_donation_managers. tipo_organizacion 
&#160; 
 ***NUEVO&#58; campos pendientes por crear en eatc_dona_headers y eatc_deleted_dona_header*** 
 eatc_destination_lat&#58; corresponde a eatc_donation_managers. latitud 
 eatc_destination_lon&#58; corresponde a eatc_donation_managers. longitud 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ERROR HANDLER: DATOS INCOMPLETOS DE BENEFICIARIO