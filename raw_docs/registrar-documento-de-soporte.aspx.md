# registrar-documento-de-soporte.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema debe proporcionar un campo de captura con las siguientes caractersticas 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_dona_header.eatc-doc 
 Descripcin ( tooltip ) &#58; Ingrese por favor un documento de soporte 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Valor por defecto &#58; si existe registro para el anuncio respectivo en el campo eatc-doc, se debe mostrar dicho registro 
 &#123;&#123;URL_entorno&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers.eatc-code&#125;&#125; 
&#160; 
 se coloca como valor por defecto lo que se obtiene en el parmetro eatc-doc 
&#160; 
 Si no encuentra registros en eatc-doc, se deja vaco. 
&#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Regla obligatoriedad &#58; no aplica 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-doc=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacin=insert&amp;eatc-doc=&#123;&#123;input&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 REGISTRAR DOCUMENTO DE SOPORTE