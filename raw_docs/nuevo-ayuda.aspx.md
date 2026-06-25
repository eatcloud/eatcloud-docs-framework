# nuevo-ayuda.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta funcionalidad se van a centralizar una serie de vnculos que estaban disgregados en el men y que contienen bsicamente las preguntas frecuentes generales, las preguntas frecuentes particulares, los tutoriales, los manuales de usuario y un vnculo al chat de soporte. 

 Diseo 
 http&#58;//repograf.eatcloud.info/ayuda.html 

 Se debe explorar la posibilidad de embeber en la misma pgina el contenido que a continuacin se define como acceder.&#160; Si esto no es posible, entonces se deben colocar botones vistosos que dan acceso a los diferentes recursos definidos&#58; 

 ***NUEVO &#58; &quot;Preguntas frecuentes&quot; (dropdown seleccin nica) *** 
 Label&#58; id=&quot; lbl_faqs &quot; 
&#160; 
 El sistema realiza la siguiente consulta (se vincula en el llamado un ejemplo en entorno de pruebas)&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/ eatc_faqs ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= webapp &amp;_cmp= eatc_faq,eatc_faq_label,eatc_faq_url &#160; 
&#160; 
 Si no se obtiene una respuesta vlida entonces, el sistema debe realizar la siguiente consulta (enviando el valor _default en el parmetro eatc_cua ) (se vincula en el llamado un ejemplo en entorno de pruebas)&#58; 
 &#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/ eatc_faqs? eatc_cua_master= &#123;&#123;_DOM.cua_master&#125;&#125;&amp; eatc_cua= _default &amp;eatc_platform =webapp &amp;_cmp= eatc_faq,eatc_faq_label,eatc_faq_url &#160; 
&#160; 
 &#160;Con la informacin obtenida en los valores&#58; 
&#160; 
 eatc_faqs. eatc_faq 
 eatc_faqs. eatc_faq_label 
 eatc_faqs. eatc_faq_url 
&#160; 
 Se arma el selector y su respectivo vnculo 

 DEPRECADO&#58; &quot;Preguntas frecuentes&quot; (particulares)&#58; despliegue de la funcionalidad 
 Label&#58; id=&quot; lbl_faqs &quot; 
&#160; 
 Realizando una consulta de los datos respectivos de la cuenta (eatc_cua), el botn de men lateral se desplegar si existe el campo faqs_url y tiene informacin (cono del botn&#58; https&#58;//zeroheight.com/174b8a276/p/23c5a2-iconos/b/69b2e6/i/3810402 ). 
&#160; 
 Ejemplo 1&#58; se despliega la funcionalidad&#58; 
&#160; 
 Para un punto de donacin de la cuenta &quot;exito&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;_distinct= faqs_url &#160; 
 (anteriormente&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Dado que la respuesta es la siguiente&#58; 
&#160; 
 _id &#58; &quot;8&quot;, 
 name &#58; &quot;exito&quot;, 
 eatc_country &#58; &quot;co&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 vertical &#58; &quot;retail&quot;, 
 type &#58; &quot;hero&quot;, 
 creation_datetime &#58; &quot;2019-11-18 00&#58;00&#58;00&quot;, 
 creation_date &#58; &quot;2019-11-18&quot;, 
 last_modification_datetime &#58; &quot;2020-10-07 11&#58;08&#58;16&quot;, 
 last_modification_date &#58; &quot;2020-10-01&quot;, 
 eatc_dona_upl &#58; &quot;si&quot;, 
 edit_coordinates &#58; &quot;no&quot;, 
 multiple_donors &#58; &quot;no&quot;, 
 eatc_odds_app &#58; &quot;eatc_dona_app&quot;, 
 odds_weight &#58; &quot;eatc_dona&quot;, 
 costs &#58; &quot;eatc_dona&quot;, 
 taxes &#58; &quot;eatc_dona&quot;, 
 days_before_expiration &#58; &quot;3&quot;, 
 eatc_rec_doc &#58; &quot;no&quot;, 
 eatc_rec_doc_signature &#58; n, 
 eatc_rec_odds_pre_verification &#58; &quot;n&quot;, 
 faqs_url &#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/categories/360003405071-Clientes-Corporativos &quot;, 
 not_delivery_instructions &#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/articles/360044685832 
&#160; 
 Con la respuesta obtenida ( https&#58;//bit.ly/eatc_faqs_exito ), se le debe desplegar un botn cuyo label es &quot; lbl_faqs &quot; 
&#160; 
&#160; 
 Ejemplo 2&#58; no se despliega la funcionalidad&#58; 
&#160; 
 Para un punto de donacin de la cuenta &quot;makro&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro&amp;_distinct=faqs_url &#160;&#160; 
 (anteriormente&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Dado que el resultado de la consulta es el siguiente&#58; 

 _id &#58; &quot;15&quot;, 
 name &#58; &quot;makro&quot;, 
 eatc_country &#58; &quot;co&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 vertical &#58; &quot;retail&quot;, 
 type &#58; &quot;free&quot;, 
 creation_datetime &#58; &quot;2020-10-01 00&#58;00&#58;00&quot;, 
 creation_date &#58; &quot;2020-10-01&quot;, 
 last_modification_datetime &#58; &quot;2020-10-07 11&#58;08&#58;16&quot;, 
 last_modification_date &#58; &quot;2020-10-01&quot;, 
 eatc_dona_upl &#58; &quot;si&quot;, 
 edit_coordinates &#58; &quot;si&quot;, 
 multiple_donors &#58; &quot;no&quot;, 
 eatc_odds_app &#58; &quot;eatc_odds&quot;, 
 odds_weight &#58; &quot;eatc_dona&quot;, 
 costs &#58; &quot;eatc_dona&quot;, 
 taxes &#58; &quot;eatc_dona&quot;, 
 days_before_expiration &#58; &quot;5&quot;, 
 eatc_rec_doc &#58; &quot;no&quot;, 
 eatc_rec_doc_signature &#58; &quot;n&quot;, 
 eatc_rec_odds_pre_verification &#58; &quot;n&quot;, 
 faqs_url &#58; &quot;&quot;, 
 not_delivery_instructions &#58; &quot;&quot; 
&#160; 
 y como en el mismo registro no existe el parmetro &quot; faqs_url &quot;, entonces se despliega el vnculo por defecto de faqs que es este&#58; https&#58;//newaccount1617917381065.freshdesk.com/support/solutions/folders/67000563057 

 DEPRECADO&#58; Preguntas frecuentes generales 
 Label&#58; id=&quot; lbl_preguntas_generales &quot; 
&#160; 
 Se debe colocar tambin un botn de men&#160; visible a todas las cuentas que se llame &quot; Preguntas generales &quot; (debajo del de &quot;preguntas frecuentes&quot; que se describi anteriormente) y que apunte a esta URL&#58; https&#58;//eatcloud.zendesk.com/hc/es-419/categories/360002989692-General (cono del botn&#58; https&#58;//zeroheight.com/174b8a276/p/23c5a2-iconos/b/69b2e6/i/3810402 ). 

 Tutoriales 
 Label&#58; id=&quot;lbl_tutoriales&quot; 
&#160; 
 Creacin de anuncio de donacin&#58; 
 Label&#58; clase=&quot;lbl_creacion_anuncio_donacion&quot; 
&#160; 
 https&#58;//www.eatcloud.com/project/2-creacion-anuncio-de-donacion/ &#160; 
&#160; 
 Entrega de donacin&#58; 
 Label&#58; clase=&quot;lbl_entrega_donacion&quot; 
&#160; 
 https&#58;//www.eatcloud.com/project/3-entrega-de-donacion/ &#160; 

 Manual de usuario 
 Label&#58; id=&quot; lb_eatc_user_manual &quot; 
&#160; 
 &quot;Manual de usuario&quot; (particular)&#58; despliegue de la funcionalidad 
 Realizando una consulta de los datos respectivos de la cuenta (eatc_cua), el botn de men lateral se desplegar si existe el campo eatc_user_manual y tiene informacin (una URL) (cono del botn&#58; https&#58;//zeroheight.com/174b8a276/p/23c5a2-iconos/b/69b2e6/i/3809849 ). 
&#160; 
 Ejemplo 1&#58; se despliega la funcionalidad&#58; 
 Para un punto de donacin de la cuenta &quot;exito&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;_distinct=eatc_user_manual &#160; 
&#160; 
 Dado que la respuesta es la siguiente&#58; 
&#160; 
 _id&#58; &quot;8&quot;, 
 name&#58; &quot;exito&quot;, 
 eatc_country&#58; &quot;co&quot;, 
 eatc_cua_master&#58; &quot;abaco&quot;, 
 vertical&#58; &quot;retail&quot;, 
 type&#58; &quot;hero&quot;, 
 creation_datetime&#58; &quot;2019-11-18 00&#58;00&#58;00&quot;, 
 creation_date&#58; &quot;2019-11-18&quot;, 
 last_modification_datetime&#58; &quot;2020-10-07 11&#58;08&#58;16&quot;, 
 last_modification_date&#58; &quot;2020-10-01&quot;, 
 eatc_dona_upl&#58; &quot;si&quot;, 
 edit_coordinates&#58; &quot;no&quot;, 
 multiple_donors&#58; &quot;no&quot;, 
 eatc_odds_app&#58; &quot;eatc_dona_app&quot;, 
 odds_weight&#58; &quot;eatc_dona&quot;, 
 costs&#58; &quot;eatc_dona&quot;, 
 taxes&#58; &quot;eatc_dona&quot;, 
 days_before_expiration&#58; &quot;3&quot;, 
 eatc_rec_doc&#58; &quot;no&quot;, 
 eatc_rec_doc_signature&#58; &quot;n&quot;, 
 eatc_rec_odds_pre_verification&#58; &quot;n&quot;, 
 faqs_url&#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/categories/360003405071-Clientes-Corporativos &quot;, 
 not_delivery_instructions&#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/articles/360044685832 
 eatc_user_manual&#58; &quot; https&#58;//sites.google.com/view/eatcloudmanualesexito/inicio &quot; 
&#160; 
 El dato que se obtiene en &quot; eatc_user_manual &quot;, se le debe desplegar un botn de men&#58; &quot;Manual de usuario&quot; que conduzca a la URL que est registrada en dicho parmetro, es decir&#58; https&#58;//sites.google.com/view/eatcloudmanualesexito/inicio . Esta pgina se deber abrir en una nueva pestaa. 

&#160; 
 Ejemplo 2&#58; no tiene un manual particular&#58; 
 Para un punto de donacin de la cuenta &quot;makro&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro&amp;_distinct=eatc_user_manual &#160; 

 ( anteriormente&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro 
 &#160;&#160;&#160; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
 Dado que el resultado de la consulta es el siguiente&#58; 
&#160; 
 _id&#58; &quot;15&quot;, 
 name&#58; &quot;makro&quot;, 
 eatc_country&#58; &quot;co&quot;, 
 eatc_cua_master&#58; &quot;abaco&quot;, 
 vertical&#58; &quot;retail&quot;, 
 type&#58; &quot;free&quot;, 
 creation_datetime&#58; &quot;2020-10-01 00&#58;00&#58;00&quot;, 
 creation_date&#58; &quot;2020-10-01&quot;, 
 last_modification_datetime&#58; &quot;2020-10-07 11&#58;08&#58;16&quot;, 
 last_modification_date&#58; &quot;2020-10-01&quot;, 
 eatc_dona_upl&#58; &quot;si&quot;, 
 edit_coordinates&#58; &quot;si&quot;, 
 multiple_donors&#58; &quot;no&quot;, 
 eatc_odds_app&#58; &quot;eatc_odds&quot;, 
 odds_weight&#58; &quot;eatc_dona&quot;, 
 costs&#58; &quot;eatc_dona&quot;, 
 taxes&#58; &quot;eatc_dona&quot;, 
 days_before_expiration&#58; &quot;5&quot;, 
 eatc_rec_doc&#58; &quot;no&quot;, 
 eatc_rec_doc_signature&#58; &quot;n&quot;, 
 eatc_rec_odds_pre_verification&#58; &quot;n&quot;, 
 faqs_url&#58; &quot;&quot;, 
 not_delivery_instructions&#58; &quot;&quot; 
 eatc_user_manual&#58; &quot;&quot; 
&#160; 
 y como en el mismo registro no existe un registro vlido (URL), entonces se despliega &quot;Manual de usuario genrico&#58; https&#58;//sites.google.com/view/eatcloudmanualeswebapp/inicio &quot;. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 NUEVO: AYUDA