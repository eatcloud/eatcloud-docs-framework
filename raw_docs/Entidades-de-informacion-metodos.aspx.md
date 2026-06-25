# Entidades-de-informacion-metodos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general&#58; 
 Las entidades de informacin han sido definidas dentro de la plataforma como los &quot;mtodos&quot; de la misma. Dichos mtodos contienen &quot;parmetros&quot; (o datos) que han sido documentados tcnicamente para su manejo estndar. 

 Mtodos (entidades de informacin)&#58; 
 Para consultar los mtodos o entidades de informacin de nuestra plataforma se ingresa el siguiente recurso&#58; 

 Vista tabla 
 https&#58;//config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?maestro=eatc_metodos&amp;lista=si&amp;atrib_filtro_tb=nombre&amp;val_filtro_tb=_todos 
 Vista json 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_metodos&amp;nombre=_todos &#160; 

 Documentacin de mtodos&#58; 
 Cada mtodo documentado, contiene un nombre (que tambin sirve de identificador), un tipo, una descripcin, una URL, y una URL de parmetros. 

 Ejemplo&#58; mtodo &quot;eatc_pods&quot; 
 Vista json&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_metodos&amp;nombre=eatc_pods &#160; 

 &#123; 
 timestamp &#58; &quot;190703105642&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 res &#58;&#160; 
 [ 
 &#123; 
 descripcion &#58; &quot;Mtodo para incorporar &quot;puntos de donacin&quot; (lugares en donde se genera una donacin que deber ser entregada a un beneficiario) a la plataforma EatCloud.&quot;, 
 id__ &#58; &quot;eatc_pods&quot;, 
 nombre &#58; &quot;eatc_pods&quot;, 
 tipo &#58; &quot;maestro&quot;, 
 url &#58; &quot; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_metodos&amp;nombre=eatc_pods &quot;, 
 url_parametros &#58; &quot; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=eatc_pods &quot; 
 &#125; 
 ], 
 memoria &#58; 0.29, 
 duracion &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 

 Parmetros (datos)&#58; 
 Para consultar los parmetros de los diferentes mtodos o entidades de informacin de nuestra plataforma se ingresa el siguiente recurso&#58; 

Vista tabla 
 https&#58;//config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?maestro=eatc_parametros&amp;lista=si&amp;atrib_filtro_tb=metodo&amp;val_filtro_tb=_todos &#160; 
Vista json 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=_todos &#160; 

Documentacin de parmetros&#58; 
 Cada parmetro documentado, corresponde a un mtodo en particular &quot;a_metodo&quot; (con su respectivo tipo&#58; &quot;a_metodo__mzzaafv_metodos__c_tipo&quot; ), un orden ( &quot;a_orden&quot; ) posee un nombre ( &quot;b_nombre&quot; ) y una etiqueta ( &quot;b_etiqueta&quot; ), una descripcin ( &quot;c_descripcion&quot; ), se define si el parmetro es obligatorio o no ( &quot;d_obligatorio&quot; ), un tipo ( &quot;d_tipo_de_dato&quot; ), la definicin se hace parte del ID (si hace parte de una clave compuesta o es una clave nica&#58; &quot;e_hace_parte_del_id&quot; ), se define si es un ndice (en el sistema Back Office&#58; &quot;f_es_indice&quot; o en el dispositivo mvil&#58; &quot;f_es_indice_dm&quot; ), una longitud mxima en caracteres ( &quot;f_longitud_caracteres&quot; ), un valor por defecto ( &quot;g_valor_por_defecto&quot; ), un estado (Activo o Inactivo&#58; &quot;h_estado&quot; ), la definicin de si es informacin protegida ( &quot;j_protegido&quot; ), y un formato ( &quot;k_formato&quot; ). Algunos de estos atributos son obligatorios y otros no (por ejemplo&#58; valor por defecto y formato). Con toda esta informacin se pueden crear a partir de la documentacin de la configuracin los esquemas de persistencia en los diferentes entornos. 

Ejemplo&#58; mtodo &quot;eatc_pods&quot;, parmetro &quot;name&quot; 
 Vista json&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=mzzaafv_parametros&amp;a_metodo=eatc_pods&amp;nombre=name &#160; 

 &#123; 
 &quot;a_metodo&quot;&#58; &quot;users&quot;, 
 &quot;a_metodo__mzzaafv_metodos__c_tipo&quot;&#58; &quot;maestro&quot;, 
 &quot;a_orden&quot;&#58; &quot;5&quot;, 
 &quot;b_etiqueta&quot;&#58; &quot;Name&quot;, 
 &quot;b_nombre&quot;&#58; &quot;name&quot;, 
 &quot;c_descripcion&quot;&#58; &quot;Nombre completo del usuario &quot;, 
 &quot;d_obligatorio&quot;&#58; &quot;si&quot;, 
 &quot;d_tipo_de_dato&quot;&#58; &quot;string&quot;, 
 &quot;e_hace_parte_del_id&quot;&#58; &quot;no&quot;, 
 &quot;f_es_indice&quot;&#58; &quot;no&quot;, 
 &quot;f_es_indice_dm&quot;&#58; &quot;no&quot;, 
 &quot;f_longitud_caracteres&quot;&#58; &quot;100&quot;, 
 &quot;g_valor_por_defecto&quot;&#58; &quot;&quot;, 
 &quot;h_estado&quot;&#58; &quot;Activo&quot;, 
 &quot;id__&quot;&#58; &quot;usersmaestroname&quot;, 
 &quot;j_protegido&quot;&#58; &quot;si&quot;, 
 &quot;k_formato&quot;&#58; &quot;&quot; 
 &#125; 

 ndice de mtodos y parmetros&#58; 
 A continuacin la relacin de los mtodos y parmetros definidos para la plataforma&#58; 
 Mtodos tcnicos&#58; 
 eatc_contexts &#160; 
 etiquetas 
 int_per_etiquetas 
 eatc_typologies&#58; maestro de tipologas 
 eatc_typology_registrer 
 kpis 

&#160; 
 Mtodos Operativos&#58; 
 eatc_pods&#58; puntos de donacin 
 eatc_attention_schedule&#58; horarios de atencin 
 eatc_odds&#58; objetos de donacin 
 eatc_donation_managers&#58; gestores de donaciones 
 eatc_final_beneficiaries&#58; beneficiarios finales 

&#160; 
 Mtodos Transaccionales&#58; 
 eatc_dona&#58; anuncios de donacin 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 User Administrator 

 CARACTERIZACIN DE ENTIDADES DE INFORMACIN