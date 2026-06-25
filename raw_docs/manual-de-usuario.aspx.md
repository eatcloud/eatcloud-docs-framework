# manual-de-usuario.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Implementacin muy similar a la que se hizo en su momento para &quot; faqs_url &quot; 
&#160; 
 Se deber colocar en el men lateral un vnculo al &quot;Manual de usuario&quot; que se desplegar s y solo si hay informacin en el parmetro de la cuenta en config &quot;eatc_user_manual&quot;. Si no existe informacin en ese parmetro o el parmetro no existe, no se debe desplegar el botn que conducir a la URL que se obtiene de leer dicho parmetro. 
&#160; 
 Nota importante para la implementacin 
 Esta implementacin de deber realizar de base con un _id ( eatc_user_manual ) para mostrar y ocultar&#160; a partir del configurador de funcionalidades 

 Y deber ubicarse entre el vnculo &quot;tutoriales&quot; y el vnculo &quot;preguntas frecuentes&quot; 

 Y tambin se le deber incorporar en vez del label &quot;Manual de usuario&quot;, el _id &#58;&quot; lb_eatc_user_manual &quot;, para dejarla lista para la internacionalizacin. 

 &quot;Manual de usuario&quot; (particular)&#58; despliegue de la funcionalidad 
 Realizando una consulta de los datos respectivos de la cuenta (eatc_cua), el botn de men lateral se desplegar si existe el campo eatc_user_manual y tiene informacin (una URL) (cono del botn&#58; https&#58;//zeroheight.com/174b8a276/p/23c5a2-iconos/b/69b2e6/i/3809849 ). 
 Ejemplo 1&#58; se despliega la funcionalidad&#58; 
&#160; 
 Para un punto de donacin de la cuenta &quot;exito&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
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
 eatc_rec_doc_signature &#58; &quot;n&quot;, 
 eatc_rec_odds_pre_verification &#58; &quot;n&quot;, 
 faqs_url &#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/categories/360003405071-Clientes-Corporativos &quot;, 
 not_delivery_instructions &#58; &quot; https&#58;//eatcloud.zendesk.com/hc/es-419/articles/360044685832 
 eatc_user_manual &#58; &quot; https&#58;//sites.google.com/view/eatcloudmanualesexito/inicio &quot; 
&#160; 
&#160; 
 Y se tiene un dato vlido en &quot; eatc_user_manual &quot;, se le debe desplegar un botn de men&#58; &quot; Manual de usuario &quot; que conduzca a la URL que est registrada en dicho parmetro, es decir&#58; https&#58;//sites.google.com/view/eatcloudmanualesexito/inicio . Esta pagina se deber abrir en una nueva pestaa. 
&#160; 
&#160; 
 Ejemplo 2&#58; no se despliega la funcionalidad&#58; 
&#160; 
 Para un punto de donacin de la cuenta &quot;makro&quot;, el sistema deber realizar la siguiente consulta para determinar el tipo de cliente&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Dado que el resultado de la consulta es el siguiente&#58; 
&#160; 
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
 eatc_user_manual &#58; &quot;&quot; 
&#160; 
 y como en el mismo registro no existe un registro vlido (URL), entonces no se despliega el botn &quot; Manual de usuario &quot;. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmanual-de-usuario%2F2894233882-EmbeddedImage--26-.jpg&ow=1280&oh=371, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmanual-de-usuario%2F2894233882-EmbeddedImage--26-.jpg&ow=1280&oh=371 
 WAPP Donantes 

 153.000000000000 

 MANUAL DE USUARIO