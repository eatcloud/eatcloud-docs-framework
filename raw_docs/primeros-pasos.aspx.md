# primeros-pasos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 SIGUE ESTOS PASOS PARA EMPEZAR&#58; &#160; 
 En la plataforma se mostrar, encima del men, una barra de progreso que mostrar el avance de los siguientes cuatro pasos del onboarding, estableciendo cuantos de los cuatro pasos se han completado. 
&#160; 
 1. A GREGA NUEVO PUNTO DE DONACIN &#58; 
 Nota importante de implementacin (implementar internacionalizando)&#58;&#160; 
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Tener en cuenta esta funcionalidad al realizar la implementacin (con el nimo de reutilizar) 
 En el BO de cuentas en Datagov existir la funcionalidad&#58; Agrega puntos de donacin .&#160; Al realizar esta implementacin de debe realizar pensando cmo reutilizar el cdigo en la implementacin de la otra funcionalidad, con el nimo de tener una implementacin eficiente (esto puede implicar segn criterio del programador, implementar primero la funcionalidad del BO de cuentas, que la del Onboarding, por ejemplo, o o hacer primero esta implementacin para hacer la segunda reutilizando llamando el mismo formulario de una manera diferente.&#160; Lo ideal es que los formularios en ambas funcionalidades sean el mismo). 

 Botn&#58; Agrega punto de donacin&#58; 
 Este botn que aparece al principio del formulario debe mostrarse con un color o un smbolo que denote que no se ha creado el primer punto de donacin, es decir que si la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/eatc_pods?_id=_* 
&#160; 
 No trae datos, se muestra en ese estado y si trae datos debe mostrar un color y smbolo (puede ser un chulo) que denote que la tarea ya est realizada. 
&#160; 
 Formulario&#58; Agregar nuevo punto de donacin (implementacin basada en una implementacin previa) 
 Se debe buscar una manera para utilizar la implementacin de Registro Simple de Punto de Donacin , (no se debe tomar en cuenta lo propuesto en el diseo arriba adjunto en lo que al formulario se refiere), al cual se puede acceder de la siguiente manera&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/registro/&#123;&#123;eatc_cua. name &#125;&#125; 
&#160; 
 Lo ideal sera llamar ese mismo cdigo (es decir que cualquier intervencin del cdigo se haga en un solo lugar) y traerlo a esta pantalla.&#160; Es importante limpiar el formulario de los mensajes que aparecen al principio. 

 Y al final del mismo (el label de la aceptacin de trminos debe quedar)&#58; 

 Al realizar esta implementacin se deber revisar la incorporacin del Llamado al servicio de creacin de configuracin de funcionalidades en AllPods 

 2. REALIZA TU PRIMERA DONACIN &#58; 
 Nota importante de implementacin (implementar internacionalizando) 
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Tener en cuenta esta funcionalidad al realizar la implementacin (con el nimo de reutilizar) 
 En el BO de cuentas en Datagov existir la funcionalidad&#58; Realiza una donacin .&#160; Al realizar esta implementacin de debe realizar pensando cmo reutilizar el cdigo en la implementacin de la otra funcionalidad, con el nimo de tener una implementacin eficiente (esto puede implicar segn criterio del programador, implementar primero la funcionalidad del BO de cuentas, que la del Onboarding, por ejemplo, o o hacer primero esta implementacin para hacer la segunda reutilizando llamando a la misma pgina de una manera diferente.&#160; Lo ideal es que las pginas en ambas funcionalidades sean la misma). 

 Descripcin tcnica&#58; 
 En esta funcionalidad se presentar un ttulo, un cuerpo de mensaje, un video ilustrativo que permitir informarle al usuario cmo realizar su primera donacin y tambin un botn que deber presentar un vnculo a la plataforma WAPP respectiva&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/apl/&#123;&#123;_DOM. cua_master &#125;&#125;/&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Para que el usuario ingrese con los datos registrados en la creacin inicial de puntos de donacin .&#160; La funcionalidad deber desplegarse, con un warning vistoso indicando que primero se deben crear puntos de donacin y con un botn que direccione a la funcionalidad respectiva , si al realizar la siguiente consulta no existen resultados. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?_id=_* 
&#160; 
 Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de la informacin a mostrar (ttulo, cuerpo, video, botn para direccionar a la plataforma de creacin de anuncios. 
&#160; 
 Si la consulta de puntos de donacin no trae resultados, el sistema debe desplegar el label&#58; 
 &#123;&#123; lb_sin_pods &#125;&#125;. &#123;&#123; lb_registra_pods &#125;&#125; 
&#160; 
 Cuyos datos ya estn registrados en el administrador de labels&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_sin_pods 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_registra_pods 
&#160; 
 El idioma por defecto ser &quot;en &quot; (si la anterior consulta no trae resultados) 
&#160; 
 Y un botn con el label&#58; 
 lb_btn_registrar_pods 
&#160; 
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
 Ttulo del mensaje&#58; segn el dato que trae el parmetro&#58; title 
 Cuerpo del mensaje&#58; segn el dato que trae el parmetro&#58; message 
 Video explicativo&#58; segn el dato que trae el parmetro&#58; video_code (para embeberlo en la pantalla, o en su defecto incorporarlo a partir del dato que se encuentra en video_url ) 
 Leyenda del botn para direccionar a la plataforma de donaciones &#58; segn el dato que trae el parmetro&#58; url_button_legend 
 URL a la que direcciona el botn&#58; segn el dato que trae el parmetro&#58; url (dinamizando los datos&#58; &#123;&#123;_DOM. cua_master &#125;&#125; y &#123;&#123;_DOM. cua_user &#125;&#125; en dicha URL) 
&#160; 
 La dems informacin por el momento no se utilizar en esta implementacin, pero a futuro podrn hacerse mejoras que manejen dichos datos. 

 3. AGREGA USUARIOS DE DASHBOARD ADMINISTRATIVO&#58; 
&#160; 
 Nota importante de implementacin (implementar internacionalizando)&#58;&#160; 
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Tener en cuenta esta funcionalidad al realizar la implementacin (con el nimo de reutilizar) 
 En el BO de cuentas en Datagov existir la funcionalidad&#58; Agrega usuarios de consulta .&#160; Al realizar esta implementacin de debe realizar pensando cmo reutilizar el cdigo en la implementacin de la otra funcionalidad, con el nimo de tener una implementacin eficiente (esto puede implicar segn criterio del programador, implementar primero la funcionalidad del BO de cuentas, que la del Onboarding, por ejemplo, o o hacer primero esta implementacin para hacer la segunda reutilizando llamando el mismo formulario de una manera diferente.&#160; Lo ideal es que los formularios en ambas funcionalidades sean el mismo). 
&#160; 
 ***NUEVO&#58; permitir la configuracin del rol*** 
 Se debe presentar un selector nico que contenga que despliegue las siguientes opciones&#58; 
 Consulta de informes (class= lbl_consulta_informes https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel=lbl_consulta_informes )&#58; valor por defecto .&#160; Si se selecciona se debe llevar al registro el rol tipo&#58; U 
 Consulta de informes y configuracin (class= lbl_consulta_informes_config https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel=lbl_consulta_informes_config )&#58;&#160; Si se selecciona se debe llevar al registro el rol tipo&#58; A 

 4. REVISA TUS PRIMEROS RESULTADOS &#58; 
 Nota importante de implementacin&#58; en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Tener en cuenta esta funcionalidad al realizar la implementacin (con el nimo de reutilizar) 
 En el BO de cuentas en Datagov existir la funcionalidad&#58; Consulta tus resultados .&#160; Al realizar esta implementacin de debe realizar pensando cmo reutilizar el cdigo en la implementacin de la otra funcionalidad, con el nimo de tener una implementacin eficiente (esto puede implicar segn criterio del programador, implementar primero la funcionalidad del BO de cuentas, que la del Onboarding, por ejemplo, o o hacer primero esta implementacin para hacer la segunda reutilizando llamando a la misma pgina de una manera diferente.&#160; Lo ideal es que las pginas en ambas funcionalidades sean la misma). 

 Descripcin tcnica&#58; 
 En esta funcionalidad se presentar un ttulo, un cuerpo de mensaje, un video ilustrativo que permitir informarle al usuario cmo realizar consultas en su plaforma Back Office y un botn para acceder a la misma&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/bo/&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Para que el usuario ingrese con los datos registrados en l a creacin de usuarios del Back Office .&#160; La funcionalidad deber desplegarse, con un warning vistoso indicando que primero se deben crear los usuarios y con un botn que direccione a la funcionalidad respectiva , si al realizar la siguiente consulta no existen resultados. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/bo_usuarios?tipousuario=U 
&#160; 
 De igual manera se debe informar que para consultar resultados previamente se debern haber realizado anuncios de donacin, y para definir ello se debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de la informacin a mostrar (ttulo, cuerpo, video, botn para direccionar a la plataforma de creacin de anuncios. 
&#160; 
 Si la consulta de puntos de donacin no trae resultados, el sistema debe desplegar el label&#58; 
 &#123;&#123; lb_sin_usuarios_bo &#125;&#125;. &#123;&#123; lb_registra_usuarios_bo &#125;&#125; 
&#160; 
 Cuyos datos ya estn registrados en el administrador de labels&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_sin_usuarios_bo 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_registra_usuarios_bo 
&#160; 
 El idioma por defecto ser &quot; en &quot; (si la anterior consulta no trae resultados). 
&#160; 
 Y un botn con el label&#58; 
 lb_btn_registrar_usuarios_bo 
&#160; 
 Cuyos datos ya estn registrados en el administrador de labels&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_btn_registrar_usuarios_bo 
&#160; 
 Que al presionarlo direccione al usuario a la funcionalidad respectiva . 
&#160; 
 Si la consulta de anuncios de donacin no trae resultados, el sistema debe desplegar el label&#58; 
 &#123;&#123; lb_sin_anuncios &#125;&#125;. &#123;&#123; lb_registra_anuncios &#125;&#125; 
&#160; 
 Cuyos datos ya estn registrados en el administrador de labels&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_sin_anuncios 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_registra_anuncios 
&#160; 
 El idioma por defecto ser &quot; en &quot; (si la anterior consulta no trae resultados). 
&#160; 
 Y un botn con el label&#58; 
 lb_btn_registrar_anuncios 
&#160; 
 Cuyos datos ya estn registrados en el administrador de labels&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;plataforma =datagov &amp;idlabel= lb_btn_registrar_anuncios 
&#160; 
 Que al presionarlo direccione al usuario a la funcionalidad respectiva . 
&#160; 
 Si la cuenta tiene usuarios BO registrados y anuncios realizados se pasa al paso siguiente para consultar los datos para mostrar en la plataforma. 
&#160; 
 Paso 2&#58; consulta mensaje 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= consulta &amp;eatc-language= &#123;&#123;iso2_idioma_browser&#125;&#125; 
&#160; 
 El idioma por defecto ser &quot;en &quot; (si la anterior consulta no trae resultados) 
 Para el idioma espaol (es) , la consulta sera la siguiente 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= consulta &amp;eatc-language= es &#160; 
&#160; 
 Teniendo en cuenta la informacin que arroja la siguiente consulta&#58; 
 &#123; 
 _id &#58; &quot;6&quot;, 
 code &#58; &quot;6&quot;, 
 date &#58; &quot;2020-12-02&quot;, 
 title &#58; &quot;Consulta tus resultados&quot;, 
 message &#58; &quot;En el siguiente video podrs ver cmo consultar tus resultados en la plataforma Back Office dispuesta para ello&quot;, 
 url &#58; &quot; https&#58;//donantes.eatcloud.info/bo/&#123;&#123;_DOM.cua_user&#125;&#125; &quot;, 
 eatc-lat &#58; &quot;&quot;, 
 eatc-lon &#58; &quot;&quot;, 
 eatc-country &#58; &quot;&quot;, 
 order &#58; &quot;1&quot;, 
 eatc_message_type &#58; &quot;consulta&quot;, 
 display_conditions &#58; &quot;first_admission&quot;, 
 display_time_sec &#58; &quot;fix&quot;, 
 url_button_legend &#58; &quot;Consulta tus resultados&quot;, 
 url_button_icon &#58; &quot;&quot;, 
 image_url &#58; &quot;&quot;, 
 published_since &#58; &quot;2020-12-01&quot;, 
 published_until &#58; &quot;&quot;, 
 eatc-language &#58; &quot;es&quot;, 
 video_url &#58; &quot; https&#58;//youtu.be/EqtZChI_tHM &quot;, 
 video_code &#58; &quot;&quot;&lt;iframe width=&quot;&quot;560&quot;&quot; height=&quot;&quot;315&quot;&quot; src=&quot;&quot;https&#58;//www.youtube.com/embed/EqtZChI_tHM&quot;&quot; frameborder=&quot;&quot;0&quot;&quot; allow=&quot;&quot;encrypted-media&quot;&quot; allowfullscreen&gt;&lt;/iframe&gt;&quot;&quot; 
 &#125; 
&#160; 
 El sistema deber desplegar lo siguiente en su interfase&#58; 
 Ttulo del mensaje&#58; segn el dato que trae el parmetro&#58; title 
 Cuerpo del mensaje&#58; segn el dato que trae el parmetro&#58; message 
 Video explicativo&#58; segn el dato que trae el parmetro&#58; video_code (para embeberlo en la pantalla, o en su defecto incorporarlo a partir del dato que se encuentra en video_url ) 
 Leyenda del botn para direccionar a la plataforma de donaciones &#58; segn el dato que trae el parmetro&#58; url_button_legend 
 URL a la que direcciona el botn&#58; segn el dato que trae el parmetro&#58; url (dinamizando el dato &#123;&#123;_DOM. cua_user &#125;&#125; en dicha URL) 
&#160; 
 La dems informacin por el momento no se utilizar en esta implementacin, pero a futuro podrn hacerse mejoras que manejen dichos datos. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fprimeros-pasos%2F3797386938-primeros_passos.jpg&ow=1265&oh=482, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fprimeros-pasos%2F3797386938-primeros_passos.jpg&ow=1265&oh=482 

 297.000000000000 

 PRIMEROS PASOS