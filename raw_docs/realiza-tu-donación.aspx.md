# realiza-tu-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 ID Funcionalidad 
 dona_datagov_cua (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= dona_datagov_cua ) 
&#160; 
 Label Botn Men&#58; 
 lb_btn_dona_datagov_cua (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_dona_datagov_cua ) 
&#160; 
 Label Ttulo de la Vista&#58; 
 lb_dona_datagov_cua (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_dona_datagov_cua ) 
&#160; 
 Label Descripcin de la Vista&#58; 
 lb_dona_datagov_cua_desc (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_dona_datagov_cua_desc ) 

 Wireframe propuesto 
 Nos han propuesto este wireframe para la funcionalidad, por lo tanto hay que tenerlo en cuenta, pero reutilizando al mximo la funcionalidad en la cual se debe basar esta implementacin y que se presentar ms adelante 

 Cuando no hay registros en el respectivo repositorio de puntos de donacin 
 El sistema debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/eatc_pods?_id=_* 
&#160; 
 Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de la informacin a mostrar (ttulo, cuerpo, video, botn para direccionar a la plataforma de creacin de anuncios. 
&#160; 
 Si la consulta de puntos de donacin no trae resultados, el sistema debe desplegar el label&#58; 
 &#123;&#123; lb_sin_pods &#125;&#125;. &#123;&#123; lb_registra_pods &#125;&#125; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov_cuentas &amp;idlabel= lb_sin_pods 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov_cuentas &amp;idlabel= lb_registra_pods 
&#160; 
 El idioma por defecto ser &quot;en &quot; (si la anterior consulta no trae resultados) 
&#160; 
 En caso de no tener puntos de donacin registrados, despus de mostrar los labels definidos se debe mostrar un botn&#160; con el label&#58; 
 lb_btn_registrar_pods ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma =datagov &amp;idlabel= lb_btn_registrar_pods ) 
 Que al presionarlo direccione al usuario a la funcionalidad respectiva . 
&#160; 

 Si la cuenta tiene puntos registrados se pasa al paso siguiente para consultar los datos para mostrar en la plataforma 
&#160; 
 Paso 2&#58; consulta mensaje 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= dona &amp;eatc-language= &#123;&#123;iso2_idioma_browser &#125;&#125; 
&#160; 
 El idioma por defecto ser &quot;en &quot; (si la anterior consulta no trae resultados) 
 Para el idioma espaol (es) , la consulta sera la siguiente 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= dona &amp;eatc-language= es &#160; 
&#160; 
 Teniendo en cuenta la informacin que arroja la siguiente consulta&#58; 
 &#123; 
 _id &#58; &quot;4&quot;, 
 code &#58; &quot;4&quot;, 
 date &#58; &quot;2020-12-01&quot;, 
 title &#58; &quot;Realiza tu primera donacin&quot;, 
 message &#58; &quot;En el siguiente video corto podrs consultar cmo realizar tu primera donacin&quot;, 
 url &#58; &quot; https&#58;//donantes.eatcloud.info/apl/&#123;&#123;_DOM.cua_master&#125;&#125;/&#123;&#123;_DOM.cua_user&#125;&#125; &quot;, 
 eatc-lat &#58; &quot;&quot;, 
 eatc-lon &#58; &quot;&quot;, 
 eatc-country &#58; &quot;&quot;, 
 order &#58; &quot;1&quot;, 
 eatc_message_type &#58; &quot;dona&quot;, 
 display_conditions &#58; &quot;first_admission&quot;, 
 display_time_sec &#58; &quot;fix&quot;, 
 url_button_legend &#58; &quot;Realiza tu primera donacin&quot;, 
 url_button_icon &#58; &quot;&quot;, 
 image_url &#58; &quot;&quot;, 
 published_since &#58; &quot;2020-12-01&quot;, 
 published_until &#58; &quot;&quot;, 
 eatc-language &#58; &quot;es&quot;, 
 video_url &#58; &quot; https&#58;//youtu.be/IxRJpB8z5-I &quot;, 
 video_code &#58; &quot;&quot;&lt;iframe width=&quot;&quot;560&quot;&quot; height=&quot;&quot;315&quot;&quot; src=&quot;&quot;https&#58;//www.youtube.com/embed/IxRJpB8z5-I&quot;&quot; frameborder=&quot;&quot;0&quot;&quot; allow=&quot;&quot;encrypted-media&quot;&quot; allowfullscreen&gt;&lt;/iframe&gt;&quot;&quot; 
 &#125; 
&#160; 
 El sistema deber desplegar lo siguiente en su interfase&#58; 
&#160; 
 Ttulo del mensaje&#58; segn el dato que trae el parmetro&#58; title 
 Cuerpo del mensaje&#58; segn el dato que trae el parmetro&#58; message 
 Video explicativo&#58; segn el dato que trae el parmetro&#58; video_code (para embeberlo en la pantalla, o en su defecto incorporarlo a partir del dato que se encuentra en video_url ) 
 Leyenda del botn para direccionar a la plataforma de donaciones &#58; segn el dato que trae el parmetro&#58; url_button_legend 
 URL a la que direcciona el botn&#58; segn el dato que trae el parmetro&#58; url (dinamizando los datos&#58; &#123;&#123;_DOM. cua_master &#125;&#125; y &#123;&#123;_DOM. cua_user &#125;&#125; en dicha URL) 
&#160; 
 La dems informacin por el momento no se utilizar en esta implementacin, pero a futuro podrn hacerse mejoras que manejen dichos datos. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Frealiza-tu-donaci%C3%B3n%2F2183914550-EmbeddedImage--63-.jpg&ow=968&oh=658, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Frealiza-tu-donaci%C3%B3n%2F2183914550-EmbeddedImage--63-.jpg&ow=968&oh=658 
 Cuentas datagov 

 348.000000000000 

 REALIZA UNA DONACIN