# upgrade-por-configura-productos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 R EGISTRO DE EVENTO DE UPGRADE AL INGRESAR A LA PGINA 
 El ingresar a la pgina, se debe capturar el ingreso a la misma como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuent eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_configure_products 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; ramo &quot;, bo_usuarios. nombre_usuario &quot; Ramo &quot;, el &quot; 2021-11-16 10&#58;20&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-11-16 10&#58;20&#58;00 
 eatc_date = 2021-11-16 
 eatc_country =https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &amp;_distinct =eatc_country = co 
 eatc_cua_master =https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = ramo 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_configure_products 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ ramo / bo_usuarios? nombre_usuario = Ramo&amp;_distinct =email &#160; &#160; = hquintero@ramo.com.co 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= ramo &amp;_distinct =type = esencial 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime = 2021-11-16%2010&#58;20&#58;00 &amp; eatc_date = 2021-11-16 &amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua = ramo &amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_configure_products &amp; eatc_user = hquintero@ramo.com.co &amp; eatc_actual_rescue_plan = esencial&#160;&#160; 

 M ENSAJE PERSONALIZADO 
 [USER_FIRST_NAME] 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios ?id=&#123;&#123;bo_usuarios. usuario &#125;&#125;&amp;_distinct =nombre_usuario 
&#160; 
 lo sentimos!... &#58;( 
 class= lbl_lo_sentimos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_lo_sentimos ) 
&#160; 
 Tu plan (concat) &#123;&#123;Plan_de_rescate&#125;&#125; (concat) no cuenta con la funcionalidad (concat) de configuracin de productos. 
 class= lbl_tu_plan ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_plan )&#160; 
&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125;&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
&#160; 
 class= lbl_no_cuenta_con_funcionalidad ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_no_cuenta_con_funcionalidad )&#160; 
&#160; 
 class= lbl_de_configuracion_productos (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_de_configuracion_productos )&#160; 
&#160; 
 Actualiza tu plan de rescate (concat) para contar con esta funcionalidad que te permitir agilizar el registro de donaciones y otra informacin importante para el sistema. 
 class= lbl_actualiza_plan_rescate ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_actualiza_plan_rescate ) 
&#160; 
 class= lbl_para_subida_archivos_planos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_para_subida_archivos_planos )&#160; 

 I NFORMACIN DE LOS PLANES 
 Como es estndar para todos los planes, su documentacin se puede consultar aqu&#58; 

Informacin Planes 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 UPGRADE POR CONFIGURA PRODUCTOS