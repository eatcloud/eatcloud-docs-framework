# new-informe-de-donaciones-eliminadas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Label Ttulo de la Vista&#58; Informe de donaciones eliminadas 
 id=&quot;lbl_informe_donaciones_eliminadas&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_donaciones_eliminadas )&#160; 
&#160; 
 Label Descripcin de la Vista&#58; 
 class=&quot;lbl_informe_donaciones_eliminadas_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_donaciones_eliminadas_desc )&#160; 
&#160; 
 &quot;En este informe se podrn consultar los anuncios eliminados por los usuarios de la Webapp EatCloud en los diferentes puntos de donacin.&#160; Se recuerda que para realizar esta accin se requiere una doble confirmacin por parte del usuario que elimina.&quot; 

 Filtro por fechas&#58; 

 Subttulo&#58; 
 class=&quot; lbl_filtro_fechas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_filtro_fechas )&#160; 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hoy ) 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 

 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_personalizar ) 

&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial ) 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 

 Filtro por ciudades (selector mltiple, con opcin &quot;Todas&quot;) 
 Seleccionar ciudad&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_selector_ciudad &#160; 
&#160; 
 Con la seleccin anterior de fechas, el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 Consulta de las ciudades en donde se realizaron anuncios en las fechas establecidas (para armar el selector mltiple) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_deleted_dona_header ?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;_distinct= eatc-city 
&#160; 
 Si no se obtienen resultados en la consulta , se muestra el toast &quot;No se obtubieron resultados &quot;&#160; class=&quot; lbl_toast_sin_resultados &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentasficiarios&amp;idlabel=lbl_toast_sin_resultados &#160; 
&#160; 
 Con las respuestas, el sistema arma un selector mltiple que permitir seleccionar una, varias o todas las ciudades presentes en el selector.&#160; Una vez el usuario realice su seleccin, con ella el sistema arma un &#123;&#123; array_de_ciudades &#125;&#125; que utiliza para la siguiente consulta&#58; 
&#160; 
 Consulta de anuncios borrados (para las fechas en las ciudades seleccionadas) 
 Con las fechas seleccionadas en el primer selector y las ciudades seleccionadas en el segundo, el sistema realiza la siguiente consulta para traer los datos&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_deleted_dona_header ?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp; eatc-city= &#123;&#123; array_de_ciudades &#125;&#125; &amp;_cmp= eatc-code,eatc-publication_date,eatc-publication_datetime,eatc-state,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-city,eatc-province, eatc-original_weight_kg, eatc-donation_manager_name,eatc-donation_manager_adress,eatc-donation_manager_phone,eatc-adjudication_datetime, eatc-donor_code, eatc-doc,eatc-warning 
&#160; 
 Consulta de datos de eliminacin 
 Con los cdigos de los anuncios que se reciben ( eatc_deleted_dona_header. eatc-code ) que el sistema recoge en un &#123;&#123; array_codigos_anuncios_eliminados &#125;&#125; . el sistema realiza la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_header_state_history ? eatc-dona_header_code = &#123;&#123; array_codigos_anuncios_eliminados &#125;&#125; &amp; eatc-state = deleted &amp;_cmp= eatc-dona_header_code, eatc-date_time,eatc_doma_user_doc_id 

&#160; 
 Tabla de de anuncios de donacin borrados 
 Se debe mostrar en una datatable que permita ordenar por columnas, realizar bsquedas y descargar informacin (en formato .csv), la siguiente informacin 
&#160; 
 Cdigo del anuncio 
 Label &#58; class=&quot;lbl_codigo_anuncio&quot;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_codigo_anuncio 
 Orden&#58; 1ra columna 

 La informacin se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Fecha 
 Label &#58; class=&quot; lbl_fecha &quot; 
 Orden&#58; 2da columna 

 La informacin se toma de&#58; eatc_dona_headers .eatc-publication_date 
&#160; 
 Fecha y hora 
 Label &#58; class=&quot; lbl_fecha_hora &quot; 
 Orden&#58; 3ra columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Estado 
 Label &#58; class=&quot; lbl_estado &quot; 
 Orden&#58; 5 ta columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-state 
&#160; 
 Tipo creacin 
 Label &#58; class=&quot; lbl_tipo_creacion &quot; 
 Orden&#58; 6ta columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-code con las siguientes pruebas lgicas&#58; 
 Si el cdigo del anuncio (eatc_dona_headers .eatc-code ) es propio del cliente (no empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lgica &quot;y&quot;) el cdigo del producto (eatc_dona .eatc-odd_id ) no es alfanumrico (es decir no fue creado manualmente dado que cuando esto ocurre los cdigos del producto son alfanumricos)&#160; se debe colocar &quot;automatica&quot; (es decir los anuncios que vienen de interfaz o integracin).&#160; De otra manera (Els)e se debe colocar &quot;manual&quot; 
 Si el cdigo del anuncio (eatc_dona_headers .eatc-code ) es del sistema (empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lgica &quot;y&quot;) el cdigo del producto (eatc_dona .eatc-odd_id ) es alfanumrico (es decir fue creado manualmente dado que cuando esto ocurre los cdigos del producto son alfanumricos)&#160; se debe colocar &quot;manual&quot; (es decir los anuncios que vienen de interfaz o integracin).&#160; De otra manera (Els)e se debe colocar &quot;automatica&quot; 
&#160; 
 Se debe evaluar si solo haciendo la prueba lgica sobre&#160; eatc_dona_headers .eatc-code se lograr atender la necesidad planteada con las pruebas lgicas arriba propuestas 
&#160; 
 Cdigo Punto de donacin 
 Label &#58; class=&quot; lbl_codigo_punto_donacion &quot; 
 Orden&#58; /ma columna 
 La informacin se toma de&#58; eatc_dona .eatc-pod_id 
&#160; 
 Punto de donacin 
 Label &#58; class=&quot; lbl_pod &quot; 
 Orden&#58; 8va columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Direccin punto de donacin 
 Label &#58; class=&quot; lbl_direccion_pod &quot; 
 Orden&#58; 9na columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-pod_address 
&#160; 
 Ciudad 
 Label &#58; class=&quot; lbl_ciudad &quot; 
 Orden&#58; 10ma columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-city 
&#160; 
 Departamento 
 Label &#58; class=&quot; lbl_departamento_provincia_estado &quot; 
 Orden&#58; 11ava columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-province 
&#160; 
 KG Originales 
 Label &#58; class=&quot; kg_originales &quot; 
 Orden&#58; 12ava columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-original_weight_kg 
&#160; 
 Beneficiario 
 Label &#58; class=&quot; lbl_beneficiario &quot; 
 Orden&#58; 13ava&#160; columna 
 La informacin se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Beneficiario direccin 
 Label &#58; class=&quot; lbl_direccion_beneficiario &quot; 
 Orden&#58; 14ava&#160; columna 
 La informacin se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_adress 
&#160; 
 Beneficiario telfono 
 Label &#58; class=&quot; lbl_telefono_beneficiario &quot; 
 Orden&#58; 15ava&#160; columna 
 La informacin se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_phone 
&#160; 
 Fecha de adjudicacin 
 Label &#58; class=&quot; lbl_hora_adjudicacion &quot; 
 Orden&#58; 16ava&#160; columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Fecha eliminacin 
 Label &#58; class=&quot; lbl_fecha_eliminacion &quot; 
 Orden&#58; 17ava columna 
 La informacin se toma de&#58; eatc_dona_header_state_history . eatc-date_time 
&#160; 
 Usuario que elimin 
 Label &#58; class=&quot; lbl_usuario_eliminacion &quot; 
 Orden&#58; 18ava columna 
 La informacin se toma de&#58; eatc_dona_header_state_history . eatc_doma_user_doc_id 
&#160; 
 Doc ID donante 
 Label &#58; class=&quot; lbl_doc_id_donante &quot; 
 Orden&#58; 19ava columna 
 La informacin se toma de&#58; eatc_dona_headers . eatc-donor_code 
&#160; 
 Doc 
 Label &#58; class=&quot; lbl_documento_soporte &quot; 
 Orden&#58; 20ava columna 
 La informacin se toma de&#58; eatc_dona_headers .eatc-doc 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-de-donaciones-eliminadas%2F389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-de-donaciones-eliminadas%2F389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181 
 Cuentas datagov 

 339.000000000000 

 INFORME DE DONACIONES ELIMINADAS