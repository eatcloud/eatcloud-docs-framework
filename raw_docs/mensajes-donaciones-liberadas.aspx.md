# mensajes-donaciones-liberadas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para la implementacin&#58; 
 Esta seccin se sugiere implementarla como un &quot;Caballo de Troya&quot; incorporando nuevos frameworks.&#160; Se debe incorporar una notificacin visible en el dashboard principal, que anuncie que existen nuevos registros de novedades en los anuncios (esto puede implementarse sobre los frameworks actuales) y luego una pgina en donde se consulten todo el historial de novedades (esta segunda pgina podra construirse con frameworks reactivos como parte del proceso de curva de aprendizaje y mejoramiento). 
&#160; 
 Llamado para mostrar una alerta en el dashboard principal ( ***NUEVO &#58; se adiciona un nuevo cdigo de causa&#58; &quot; cnebdona &quot; *** ) 
&#160; 
 El sistema deber realizar el siguiente llamado para determinar si hay informacin reciente sobre novedades por anuncios liberados&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_doma_state_change_history?eatc_doma_code=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc_cause_code= cnebdona, susp_autom_no_recogio_donacion &amp;eatc_date[0]=&#123;&#123;fecha_tres_dias_atrs_formato_AAAA-MM-DD&#125;&#125;&amp;eatc_date[1]=&#123;&#123;fecha_actual_formato_AAAA-MM-DD&#125;&#125;&amp;_cont 
&#160; 
 Si la respuesta trae un conteo vlido, entonces se deber presentar un mensaje o una alerta en el dashboard de la siguiente manera 
&#160; 
 Tienes &#123;&#123; count &#125;&#125; novedad(es) por donacin(es) liberada(s) 
&#160; 
 label (class)=lbl_tienes ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_tienes ) 
 &#123;&#123; count &#125;&#125; = Respuesta del llamado 
 label (class)=lbl_novedades_donaciones_liberadas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_novedades_donaciones_liberadas )&#160; 
&#160; 
 Al hacer clic al anuncio, la app debe pasar a una seccin en donde se muestre el detalle de dichas novedades 

&#160; 
 Novedades por donaciones liberadas ( ***NUEVO &#58; se adiciona un nuevo cdigo de causa&#58; &quot; cnebdona &quot; *** ) 
 label (class)=lbl_novedades_donaciones_liberadas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_novedades_donaciones_liberadas )&#160; 
&#160; 
 Mediante el siguiente llamado el sistema deber pintar cards que contengan la informacin obtenida, mostrando primero las ms recientes, y de ltimo las ms antiguas y paginando para mostrar 10 resultados por pgina. 
&#160; 
 Llamado para traer las novedades por donaciones liberadas&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_doma_state_change_history?eatc_doma_code=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc_cause_code= susp_autom_no_recogio_donacion, cnebdona &amp;_cmp= eatc_datetime, eatc_public_notes 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MENSAJES DE NOVEDADES SOBRE DONACIONES LIBERADAS