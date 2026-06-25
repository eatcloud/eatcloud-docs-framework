# pre-verificar-donación-eatc_rec_odds_pre_verification.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Esta funcionalidad eminentemente informativa, pretende recordarle al usuario que debe verificar que solo ciertos productos estn presentes en la donacin, los dems no deben ser tenidos en cuenta. 

 Pop up window con recordatorio y accin ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Al accionar el botn respectivo , se debe generar un Pop-UP informativo con la siguiente informacin 
&#160; 
 Si existe en campo eatc-warning registrado para el dona header en cuestin&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers?eatc-code=&#123;&#123;valor&#125;&#125; 

&#160; 
 alguna informacin vlida (diferente de vaco o cero) se debe mostrar lo siguiente 
 &#123;&#123;Contenido del warning eatc_dona_headers.eatc-warning&#125;&#125; 
&#160; 
 Haz verificado para solo recibir los productos autorizados (los dems debes devolverlos) 
&#160; 
 SI &#160; &#160; &#160; &#160; &#160; NO 
&#160; 
 Si no existe contenido en el warning (o este est vaco, nulo o en cero) se debe presentar el siguiente mensaje&#58; 
 Debes verificar que la donacin contenga solo los siguientes productos&#58; 
&#160; 
 [Se despliega listado con los campos &quot; eatc-odd_external_code1 (etiqueta en la columna del listado&#58; PLU )&quot; y &quot; eatc-name (etiqueta en la columna del listado&#58; Descripcin )&quot; de https&#58;//donantes.eatcloud.info/api/ $eatc_dona_header.eatc-donor /eatc_odds?_id=_*&#160; 
&#160; 
 Ejemplo para eatc_dona_header.eatc-donor = nutresa estos son los artculos que se deben presentar&#58; https&#58;//donantes.eatcloud.info/api/nutresa/eatc_odds?_id=_* ] 
&#160; 
 Haz verificado para solo recibir los productos autorizados (los dems debes devolverlos) 
&#160; 
 SI &#160; &#160; &#160; &#160; &#160; NO 
&#160; 
 Opcin SI&#58; 
 Si el usuario oprime la opcin &quot;si&quot;, el sistema estampa la fecha y hora en el campo &quot; eatc_rec_odds_pre_verification_datetime &quot; del &quot; eatc_dona_header &quot; 

&#160; 
 Opcin NO&#58; 
 Retorna al dashboard del anuncio de donacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 PRE-VERIFICAR DONACIN (EATC_REC_ODDS_PRE_VERIFICATION)