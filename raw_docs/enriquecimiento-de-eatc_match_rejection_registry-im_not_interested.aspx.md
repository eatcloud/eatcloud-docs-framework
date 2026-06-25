# enriquecimiento-de-eatc_match_rejection_registry-im_not_interested.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Registro realizado originalmente desde el proceso im_not_interested 

 Por necesidades puntuales de Abaco, se debern crear dos campos de informacin adicionales en la estructura de datos eatc_match_rejection_registry para registrar la tipologa b de la organizacin y para registrar los KG de la respectiva donacin.&#160; Por tal motivo se deber crear un proceso nocturno que evale los registros en&#160; que no tienen datos (nulos o vacos) en esos dos nuevos datos ( eatc_match_rejection_registry. eatc_doma_typology_b y eatc_match_rejection_registry. eatc_dona_original_kg ) y para dichos registros realizar las consultas que se definen a continuacin para completarlos y enriquecer los datos como se requiere.&#160; La primera vez que corra el proceso, deber realizar un trabajo pesado para incorporar la informacin a todos los registros creados hasta ahora.&#160; Posteriormente, cada noche el proceso debera ser liviano, para incorporar solamente los que no tienen esos datos en el registro. 
&#160; 
 eatc_match_rejection_registry .eatc_doma_typology_b 
&#160; 
 Con los datos del registro se realiza una consulta similar a la siguiente 
&#160; 
 &#123;&#123;url_entorno_beneficiarios&#125;&#125;/api/&#123;&#123; eatc_match_rejection_registry. eatc_cua_master&#125;&#125;/eatc_donation_managers? identificador_unico_registro= &#123;&#123; eatc_match_rejection_registry. eatc_doma_code &#125;&#125; &amp;_cmd= eatc_doma_typology_b 
&#160; 
 El valor obtenido se lleva al campo en cuestin eatc_match_rejection_registry. eatc_doma_typology_b 
&#160; 
 eatc_match_rejection_registry .eatc_dona_original_kg 
 Con los datos del registro se realiza una consulta similar a la siguiente 
&#160; 
 &#123;&#123;url_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_match_rejection_registry. eatc_cua_master&#125;&#125;/eatc_dona_headers? eatc-code = &#123;&#123; eatc_match_rejection_registry. eatc_dona_header_code &#125;&#125; &amp;_cmd= eatc-original_weight_kg 
&#160; 
 El valor obtenido se lleva al campo en cuestin&#160; eatc_match_rejection_registry. eatc_dona_original_kg 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ENRIQUECIMIENTO DE EATC_MATCH_REJECTION_REGISTRY