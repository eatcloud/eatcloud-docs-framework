# nuevo-menú-lateral-de-navegación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo&#58; 
 http&#58;//repograf.eatcloud.info/home.html# 

 El men deber poderse colapsar hacia la izquierda, ampliando el rea de pantalla respectiva, dejando solo el cono en una franja delgada, cuando el mismo est colapsado 

 Consulta necesaria para construir el men&#58; 
 Para construir el men lateral se deber realizar la consulta de los datos del punto de donacin que se ha autenticado en la plataforma 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?login=&#123;&#123;usuario&#125;&#125;&amp;password=&#123;&#123;password&#125;&#125; 

 Datos del punto de donacin 
 En la parte superior del men se presentarn los siguientes datos, obtenidos de la anterior consulta&#58; 
&#160; 
 Nombre del punto de donacin 
 eatc_pods. eatc-name 
&#160; 
 Direccin del punto de donacin 
 eatc_pods. eatc-adress 
&#160; 
 E-mail del punto de donacin 
 eatc_pods. eatc-email 
&#160; 
 Al hacer clic en estos datos, se debe direccionar al nuevo dashboard . 

 Crear anuncio de donacin 
 class=&quot; lbl_crear_anuncios &quot; 
&#160; 
 Dar acceso a la funcionalidad respectiva.&#160; En una primera versin, se utilizar la misma funcionalidad que hasta el momento ha funcionado .&#160; En una segunda etapa se desplegar una funcionalidad mejorada . 

 ***Nuevo&#58; Crear anuncio con archivo plano *** 
 class=&quot; lbl_crear_anuncio_archivo_plano &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel=lbl_crear_anuncio_archivo_plano ) 
&#160; 
 El botn del men lateral, se desplegar, si y solo si, la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_objectstore= eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent 
&#160; 
 Entrega un resultado vlido.&#160; En caso contrario no se muestra el botn. 
 Ejemplo 1&#58; ambiente de pruebas, cuenta &quot;exito&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua=exito&amp;eatc_platform= wapp &amp;eatc_objectstore= eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent &#160; 
&#160; 
 Como la consulta arroja un resultado vlido , entonces se procede a desplegar el elemento del men lateral. 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta &quot;alqueria&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua=alqueria&amp;eatc_platform= wapp &amp;eatc_objectstore= eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent &#160; 
&#160; 
 Como la consulta NO arroja un resultado vlido, entonces no se despliega el botn en el men lateral. 
 Este botn dar acceso a la funcionalidad respectiva&#58; Creacin de anuncios de donacin mediante archivo plano . 

&#160; 
 ***Nuevo&#58; Venta de ltimo minuto *** 
 class=&quot; lbl_venta_ultimo_minuto &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_venta_ultimo_minuto ) 
&#160; 
 El botn del men lateral, se desplegar, si y solo si, la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; sale_wapp=y&amp;_cont 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega el boton.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra el botn. 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas, cuenta &quot;exito&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;0&quot; , entonces no se despliega el botn en el men lateral. 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta &quot;alqueria&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name= alqueria &amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;1&quot; , entonces se procede a desplegar el elemento del men lateral. 
 Este botn dar acceso a la funcionalidad respectiva&#58; Creacin de venta de ltimo minuto . 

&#160; 
 Listado de donaciones 
 class=&quot; lbl_dona_list &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_dona_list ) 
&#160; 
 Dar acceso a la nueva funcionalidad de Listado de donaciones . 

&#160; 
 ***Nuevo&#58; Listado de ofertas *** 
 class=&quot; lbl_sale_list &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_sale_list ) 
&#160; 
 El botn del men lateral, se desplegar, si y solo si, la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; sale_wapp=y&amp;_cont 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega el boton.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra el botn. 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas, cuenta &quot;exito&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;0&quot; , entonces no se despliega el botn en el men lateral. 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta &quot;alqueria&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name= alqueria &amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;1&quot; , entonces se procede a desplegar el elemento del men lateral. 
 Este botn dar acceso a la funcionalidad respectiva&#58; Consulta de ofertas de ltimo minuto . 

&#160; 
 Resultados 
 class=&quot;lbl_resultados&quot; 
&#160; 
 Dar acceso a nueva funcionalidad de Resultados . 

&#160; 
 ***Nuevo&#58; Comprar ofertas cercanas *** 
 class=&quot; lbl_comprar_ofertas_cercanas &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_comprar_ofertas_cercanas ) 
&#160; 
 El botn del men lateral, se desplegar, si y solo si, la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; sale_pwa=y&amp;_cont 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega el boton.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra el botn. 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas, cuenta &quot;exito&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;sale_pwa=y&amp;_cont &#160;&#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;0&quot; , entonces no se despliega el botn en el men lateral. 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta &quot;alqueria&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name= alqueria &amp;sale_pwa=y&amp;_cont &#160;&#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;1&quot; , entonces se procede a desplegar el elemento del men lateral. 
&#160; 
 Este botn dar acceso a la PWA EatCloud Sale - Usuario final masivo, autenticando de manera transparente con las credenciales de acceso del Punto de Donacin en la PWA y accediendo al Dashboard de la PWA .&#160; 

&#160; 
 ***Nuevo&#58; Informe de peso excesivo *** 
 Label &#58; class=&quot;lbl_info_peso_excesivo&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_info_peso_excesivo )&#160; 
&#160; 
 El botn del men lateral, deber presentar una alerta (puede ser un signo de admiracin en un globo rojo), cuando la s&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123;_DOM .cua_user &#125;&#125; &amp; eatc_excessive_weight= y &amp;_cont 
&#160; 
 Siendo 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;&#58; tres das antes del da actual 
 &#123;&#123; fecha_final_periodo &#125;&#125;&#58; dia actual 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega la alerta.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra la alerta. 
&#160; 
 El elemento de men da ingreso al Informe de Peso Excesivo 

&#160; 
 Ejemplo 1&#58; ambiente productivo, _DOM .cua_master &quot;abaco&quot;, _DOM .cua_user &quot;exito&quot;, eatc-pod_id &quot; 616 &quot;, mayo 31 de 2022 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-05-28&amp;eatc-publication_date[1]=2022-05-31&amp;eatc-pod_id=616&amp; eatc_cua_origin = exito &amp;eatc_excessive_weight= y &amp;_cont &#160; &#160; 
&#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;1&quot; , entonces no se despliega la alerta en el botn del men lateral. 
&#160; 
 ***Nuevo&#58; Cancelados a revisar *** 
 Label &#58; class=&quot;lbl_cancelados_a_revisar&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_cancelados_a_revisar )&#160;&#160;&#160;&#160; 
&#160; 
 El botn del men lateral, deber presentar una alerta (puede ser un signo de admiracin en un globo rojo), cuando la s&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; eatc_cua_origin =&#123;&#123;_DOM .cua_user &#125;&#125; &amp; eatc-original_weight_kg = _&gt;_ 50 &amp; eatc-pod_id =&#123;&#123; eatc-pod_id &#125;&#125;&amp; eatc-state = cancelled &amp;_cont 
&#160; 
 Siendo 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;&#58; siete das antes del da actual 
 &#123;&#123; fecha_final_periodo &#125;&#125;&#58; dia actual 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega la alerta.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra la alerta. 
&#160; 
 El elemento de men da ingreso al Informe de Revisin de Cancelados 
&#160; 
 Centro de ayuda 
 class=&quot;lbl_centro_ayuda&quot; 
&#160; 
 Dar acceso a nueva funcionalidad de Ayuda . 
&#160; 
 Configuracin 
 class=&quot;lbl_configuracion&quot; 
&#160; 
 Dar acceso a nueva funcionalidad de Configuracin . 
&#160; 
 Si el punto de donacin no tiene horarios de atencin configurados, el botn deber mostrar un signo distintivo (un smbolo de interrogacin encerrado en un crculo rojo) con el siguiente tooltip 
 class=&quot;lbl_configuracion_h_a_tooltip&quot; 

&#160; 
 ***Nuevo&#58; Configuracin horarios de venta *** 
 class=&quot; lbl_cnf_horarios_venta &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cnf_horarios_venta )&#160; 
&#160; 
 El botn del men lateral, se desplegar, si y solo si, la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; sale_wapp=y&amp;_cont 
&#160; 
 Si la consulta en el parmetro &quot; count &quot; entrega un valor diferente a cero, se despliega el boton.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra el botn. 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas, cuenta &quot;exito&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;0&quot; , entonces no se despliega el botn en el men lateral. 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta &quot;alqueria&quot;&#160; 
 El sistema evala la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name= alqueria &amp;sale_wapp=y&amp;_cont &#160; &#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;1&quot; , entonces se procede a desplegar el elemento del men lateral. 
&#160; 
 Este botn dar acceso a la funcionalidad respectiva&#58; Configuracin de horarios de venta . 

&#160; 
 Cerrar sesin 
 class=&quot;lbl_cerrar_sesion&quot; 
&#160; 
 Cierra sesin y direcciona a la pantalla de login 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-men%C3%BA-lateral-de-navegaci%C3%B3n%2F3562625902-menu_lateral--1-.jpg&ow=550&oh=1046, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-men%C3%BA-lateral-de-navegaci%C3%B3n%2F3562625902-menu_lateral--1-.jpg&ow=550&oh=1046 

 User Administrator 
 168.000000000000 

 NUEVO MEN LATERAL DE NAVEGACIN