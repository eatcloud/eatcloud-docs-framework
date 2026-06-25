# informes-de-anuncios-rechazos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

&#160; 
 Nota importante de implementacin&#58; se basa parcialmente en funcionalidad ya implementada 
 Esta implementacin debe constar en el traspaso y mejora de la funcionalidad &quot; Informe de excepciones &quot; de la WAPP legacy, con la incorporacin de los ajustes que se relacionan a continuacin 

 Titulo de la vista&#58; Informe de rechazos 
 class=&quot; lbl_informe_rechazos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_rechazos ) 
&#160; 
 Descripcin del informe 
 class=&quot; lbl_informe_rechazos_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_rechazos_desc ) 
&#160; 
 &quot;En este informe podrs encontrar el detalle de los productos que no fueron recibidos efectivamente por los beneficiarios (bien sea porque no fueron encontrados dentro de los artculos entregados, o porque no son aptos para el consumo humano).&quot; 
&#160; 
 Filtro de fechas =&gt; No exista en el reporte original 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
 Valor por defecto&#58; primer da del mes actual. 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 
 Valor por defecto&#58; da actual. 

&#160; 
 Selector de NITs 
 label&#58; class=&quot; lbl_selecciona_nit &quot;&#160; 
&#160; 
 El sistema debe realizar un &quot; _istinct &quot; del dato eatc_dona_headers. eatc-donor_code , de los anuncios del periodo seleccionado en los selectores de fechas y los debe traer a un selector. El usuario deber escoger un &quot;NIT&quot; y dicho filtro se aplicar al listado de anuncios soportados (es decir que solamente se mostrarn los datos correspondientes al NIT seleccionado) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct=eatc-donor_code 
&#160; 
 Si la anterior consulta genera un solo valor, este se coloca por defecto en el selector.&#160; Si genera varios se arma el selector. 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 

&#160; 
&#160; 
 Consulta para generar la tabla de informacin 
 Con la seleccin, anterior, se deben realizar las siguientes consultas para traer la informacin que se mostrar en la tabla 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-donor_code=&#123;&#123; donor_code_seleccionado &#125;&#125;&amp;_distinct=eatc-code 
&#160; 
 La anterior consulta traer como resultado un array de cdigos de donaciones (en adelante array_eatc_code ) y con este dato, los datos anteriores se realiza la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_odd_rejection_registry?eatc-donation_manager_code=&#123;&#123; donor_code_seleccionado &#125;&#125;&amp;eatc-dona_header_code=&#123;&#123; array_eatc_code &#125;&#125; 
&#160; 
 Con la informacin obtenida, se arma la tabla de informacin de la funcionalidad. 

&#160; 
 Funcionalidades de la tabla de informacin 
 Las funcionalidades propias de datatables (como bajar el archivo, realizar una bsqueda, etc) se deben conservar. 

&#160; 
 Tabla de informacin 
 En la tabla de la funcionalidad original se incorporan como nombres de las columnas los nombres de los campos. Esto cambiar con los siguientes labels 
&#160; 
 _id =&gt; No va 
&#160; 
 date_time =&gt; Fecha y hora 
 clase=&quot; lbl_fecha_hora &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_hora ) 
&#160; 
 date_time =&gt; Fecha y hora 
 clase=&quot; lbl_fecha_hora &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_hora ) 
&#160; 
 eatc-donation_manager_code =&gt; Cdigo del beneficiario 
 clase=&quot; lbl_codigo_beneficiario &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_beneficiario ) 
&#160; 
 eatc-donation_manager_user_doc_id =&gt; Identificacin de quien rechaz (por defecto oculto) 
 clase=&quot; lbl_id_usuario_rechazo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_id_usuario_rechazo ) 
&#160; 
 eatc_donor_code =&gt; Cdigo del donante (por defecto oculto) 
 clase=&quot; lbl_codigo_donante &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_donante ) 
&#160; 
 eatc-dona_header_code =&gt; Cdigo de la donacin 
 clase=&quot; lbl_codigo_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_donacion ) 
&#160; 
 eatc-pod_id =&gt; ID punto de donacin 
 clase=&quot; lbl_codigo_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_donacion ) 
&#160; 
 eatc-odd_id =&gt; Cdigo del producto 
 clase=&quot; lbl_codigo_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo_producto ) 
&#160; 
 No est en el actual informe =&gt; Nombre del producto 
 clase=&quot; lbl_nombre_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_nombre_producto ) 
&#160; 
 verification_type =&gt; Tipo de verificacin 
 clase=&quot; lbl_tipo_verificacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tipo_verificacion ) 
&#160; 
 eatc-odd_rejetion_cause =&gt; Causal de rechazo 
 clase=&quot; lbl_causal_rechazo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_causal_rechazo ) 
&#160; 
 eatc-odd_rejetion_cause_id =&gt; No va 
&#160; 
 quantity =&gt; Cantidad 
 clase=&quot; lbl_cantidad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_cantidad ) 
&#160; 
 evidence =&gt; Evidencia 
 clase=&quot; lbl_evidencia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_evidencia ) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformes-de-anuncios-rechazos%2F1134706867-informe_excepciones.jpg&ow=1078&oh=541, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformes-de-anuncios-rechazos%2F1134706867-informe_excepciones.jpg&ow=1078&oh=541 
 Cuentas datagov 

 436.000000000000 

 DATA ANALYTICS: INFORMES DE ANUNCIOS > RECHAZOS