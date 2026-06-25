# revisión-estado-recibido.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 A solicitud del xito, los anuncios solo podrn marcarse como recibidos, si poseen una validacin del cdigo de recogida.&#160; Dada esta circunstancia se realiz un ajuste en la App, pero se propone esta proceso automtico, para corregir aquellos casos que se presenten por actualizacin extempornea de la App por parte de los gestores de donaciones. 

 Criterios para establecer los anuncios sobre los cuales aplicar la correccin de estado&#58; 
 Los anuncios a los cuales se les debe aplicar este proceso automtico de correccin, deben cumplir dos criterios&#58; 
&#160; 
 Su fecha de publicacin ( eatc-publication_date ) debe ser posterior la implementacin del proceso (se corre hacia adelante y no corrige informacin hacia atrs). 
 Solo aplica anuncios de cuentas ( eatc_cua_origin ) a cuentas cuyo parmetro multiple_donors sea no 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua? multiple_donors = no 

 Ajuste automtico de estado recibido&#58; 
 Para los anuncios cuyo estado sea &quot; received &quot;, el sistema debe validar si existe un registro vlido en &quot; eatc_code_verification_datetime &quot;&#160; (fecha vlida), si no existe dicha fecha vlida, entonces el sistema deber cambiar el estado del anuncio a &quot;delivered&quot;. 
&#160; 
 Los anuncios a los cuales se les debe cambiar el estado a &quot; delivered &quot;, respondern entonces a esta consulta (siempre y cuando cumplan tambin con los criterios definidos en el punto anterior )&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc_code_verification_datetime =0000-00-00%2000&#58;00&#58;00&amp; eatc-state = received 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 REVISIN ESTADO RECIBIDO