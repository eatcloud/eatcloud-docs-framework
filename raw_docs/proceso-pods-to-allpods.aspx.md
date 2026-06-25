# proceso-pods-to-allpods.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema realiza un proceso peridico que pasa registros en la tabla &quot;eatc_pods&quot; de cada donante, a la tabla general &quot;eatc_pods&quot; en &quot;allpods&quot;. 

 ***NUEVO&#58; MENSAJE PARA ANUNCIAR A LA COMUNIDAD DE BENEFICIARIOS LA CREACIN DE UN PUNTO DE DONACIN EN SU REA DE INFLUENCIA *** 
&#160; 
 Se implementar una mejora, que generar un mensaje que se visualizar en el dashboard de la aplicacin de beneficiarios, y que informar al ecosistema de organizaciones sociales, la creacin de un punto de donacin en su rea de influencia.&#160; En primera instancia el rea de influencia ser definida de manera general por cada cuenta maestra, y posteriormente se establecern algoritmos ms avanzados para establecer el rea de influencia de cada punto de donacin. 
&#160; 
 Inicialmente este servicio se habilitar para la cuenta maestra &quot; ABACO &quot; con proyeccin de implementacin futura en otras cuentas. 

&#160; 
 Consulta de los datos del punto de donacin recin creado&#58; 
 El sistema tomar lo siguientes datos del punto recientemente creado en allpods (se hace un simil con el siguiente llamado) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-id=&#123;&#123;pod_id&#125;&#125;&amp;_cmp=eatc-cua_master,eatc-cua,eatc-name,eatc-lat,eatc-lon 
&#160; 
 Con los datos obtenidos, se realizarn las siguientes operaciones 
&#160; 
 Consulta del radio del rea de influencia&#58; 
 El sistema realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_cua_master ?eatc_cua=&#123;&#123;eatc_pods. eatc-cua_master &#125;&#125;&amp;_cmp= eatc_pods_infuence_zone_radius_km 
 Para obtener el radio de influencia 

&#160; 
 Consulta de las organizaciones sociales en el radio de influencia&#58; 
 Con los valores obtenidos en las consultas previas, el sistema realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/ get/&#123;&#123;cua_master&#125;&#125;/getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = &#123;&#123; eatc_pods. eatc-lat &#125;&#125; , &#123;&#123; eatc_pods. eatc-lon &#125;&#125; &amp; showfield = identificador_unico_registro&amp; &amp;filterfield_1= eatc_state &amp;filtervalue_1= activo &amp; km = &#123;&#123; eatc_cua_master .eatc_pods_infuence_zone_radius_km &#125;&#125; 
&#160; 
 Con esta consulta se obtiene un array de puntos de donacin que estn en el rea de influencia.&#160;&#160; 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master&#58; abaco, radio de influencia 20 KM y POD con coordenada&#58; 6.1523152,-75.6085845 . 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/get/abaco/getpuntos? table = eatc_donation_managers &amp; fieldname = coordenadas &amp; fieldvalue = 6.1523152,-75.6085845 &amp; showfield =identificador_unico_registro&amp; &amp;filterfield_1= eatc_state &amp;filtervalue_1= activo &amp; km = 20 &#160; 
&#160; 
 ***NUEVO&#58; Determinacin del correo electrnico al cul se enva&#58; *** 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_pod_creation_notification_emails 
&#160; 
 Con la respuesta, el sistema construye un &#123;&#123; array_destinatarios &#125;&#125; a los cuales enviar el siguiente correo electrnico.&#160; Si la consulta no arroja resultados el correo no se enva. El correo crea una tabla con los puntos que pasaron de pods a Allpods en el da, es decir los nuevos puntos que se crearon. 
&#160; 
 Envo de correo, ante punto de donacin sin gestores de donacin en su zona de influencia **NUEVO&#58; consulta eatc_cua_master para destinatarios y vnculo a mapa *** 
&#160; 
 Si la consulta no arroja datos el sistema deber generar el siguiente correo electrnico para la mesa de servicio&#58; 
&#160; 
 From&#58; noreply@eatcloud.com 
&#160; 
 to&#58; ***NUEVO&#58; &#123;&#123; array_destinatarios &#125;&#125; *** 
&#160; 
 Asunto&#58; Punto de donacin recientemente creado sin organizaciones sociales en su rea de influencia 
&#160; 
 Cuerpo&#58; 
&#160; 
 Recientemente se ha creado el punto de donacin &lt;a href=((URL_entorno_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-id= &#123;&#123; pod_id &#125;&#125;&gt; &#123;&#123;eatc_pods. eatc-name &#125;&#125; &lt;/a&gt; del donante &#123;&#123;eatc_pods. eatc-cua &#125;&#125;, que no tiene organizaciones sociales en su rea de influencia, que tiene un radio de &#123;&#123; eatc_cua_master .eatc_pods_infuence_zone_radius_km &#125;&#125; KM ***NUEVO&#58; &lt;a href=( https&#58;//maps.google.com/?q= &#123;&#123; eatc_pods. eatc-lat &#125;&#125; , &#123;&#123; eatc_pods. eatc-lon &#125;&#125; &gt; Ver Mapa &lt;/a&gt; *** . Se aconseja estar pendiente de las donaciones de este punto para garantizar que las mismas hagan match con el ecosistema de gestores de donaciones. 
&#160; 
 Si el sistema retorna una respuesta vlida, deber crear mensajes de dashboard (tantos como posiciones del array de respuesta, es decir un mensaje por cada una de las organizaciones cuyo &quot; identificador_unico_registro &quot; se obtiene con la respuesta), de la manera como se detalla a continuacin&#58; 

&#160; 
 Mensaje para anunciar el nuevo pod en el rea de influencia&#58; 
 Consulta del ordenamiento de los mensajes existentes, con el nimo de garantizar que el mensaje salga en primera posicin 
&#160; 
 El sistema deber realizar la siguiente consulta, para establecer cual es el orden mnimo presente en los mensajes de dashboard. 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_doma_messages?eatc_message_type=doma_dashboard&amp;_cmp=order 
&#160; 
 Obtenido este valor, deber restar 10 (posiciones) al nmero para obtener el valor &#123;&#123;order&#125;&#125; que le aplicar al mensaje que se crear 
&#160; 
 Creacin del mensaje. 
 El sistema crear con los siguientes parmetro el mensaje para anunciar el inicio del nuevo punto de donacin. 
&#160; 
 &#123;&#123;parametros_creacion_mensaje&#125;&#125; 
 &#160; &#160; &#160; code = &#123;&#123;codigo_autogenerado&#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; date = &#123;&#123;date_stamp_en_formato_AAAA-MM-DD&#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; title =Damos la bienvenida a un nuevo punto de donacin 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; message =Hemos activado al punto de donacin &#123;&#123;eatc_pods. eatc-name &#125;&#125; del donante &#123;&#123;eatc_pods. eatc-cua &#125;&#125; . Esperamos con ello aumentar los alimentos para tu comunidad 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; url = https&#58;//maps.google.com/?q= &#123;&#123; eatc_pods. eatc-lat &#125;&#125; , &#123;&#123; eatc_pods. eatc-lon &#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; eatc_doma_code = &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; order = &#123;&#123;order&#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; eatc_message_type =doma_dashboard 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; display_conditions =always 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; display_time_sec =fix 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; url_button_legend =lbl_ver_mas 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; eatc_country =co 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; published_since = &#123;&#123;date_stamp_en_formato_AAAA-MM-DD&#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; published_until = &#123;&#123;&#123;&#123;date_stamp_en_formato_AAAA-MM-DD&#125;&#125;+8dias&#125;&#125; 

&#160; 
 Con estos parmetros el sistema realiza tantos llamados de creacin de anuncios, como identificadores unicos de organizaciones encontradas en el rea de influencia. 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/abaco/?_tabla=eatc_doma_messages&amp;_operacion=insert&amp; &#123;&#123;parametros_creacion_mensaje&#125;&#125; 

&#160; 
 ***NUEVO&#58; Envo de correo electrnico al gestor del ecosistema social ante la creacin de nuevos PODs *** 
&#160; 
 Determinacin del correo electrnico al cul se enva&#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= eatc_pod_creation_notification_emails 
&#160; 
 Con la respuesta, el sistema construye un &#123;&#123; array_destinatarios &#125;&#125; a los cuales enviar el siguiente correo electrnico.&#160; Si la consulta no arroja resultados el correo no se enva. El correo crea una tabla con los puntos que pasaron de pods a Allpods en el da, es decir los nuevos puntos que se crearon. 
&#160; 
 Envo de correo, ante punto de donacin creado ***NUEVO&#58; vista tipo &quot;vietas&quot; y vnculo a mapa en la direccin *** 
 from &#58; noreply@eatcloud.com 
&#160; 
 to &#58; &#123;&#123; array_destinatarios &#125;&#125;&#160; 
&#160; 
 Asunto &#58; Nuevo Punto de Donacin Inscrito 
&#160; 
 Cuerpo &#58; 
&#160; 
 El da de hoy se ha inscrito en EatCloud el siguiente punto de donacin 
 Nombre&#58;&#123;&#123;eatc_pods. eatc-name &#125;&#125; 
 Donante&#58; &#123;&#123;eatc_pods. eatc-cua &#125;&#125; 
 Departamento&#58; &#123;&#123;eatc_pods. eatc-province &#125;&#125; 
 Ciudad&#58; &#123;&#123;eatc_pods. eatc-city &#125;&#125;&#160; 
 Direccin&#58; ***NUEVO&#58; &lt;a href=( https&#58;//maps.google.com/?q= &#123;&#123; eatc_pods. eatc-lat &#125;&#125; , &#123;&#123; eatc_pods. eatc-lon &#125;&#125; &gt; &#123;&#123;eatc_pods. eatc-adress &#125;&#125;&lt;/a&gt; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESO PODS TO ALLPODS