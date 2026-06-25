# upgrade-por-fechas-indicadores-generales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 URL&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/ upgradebyindicatorsdates 

 R EGISTRO DE EVENTO DE UPGRADE AL INGRESAR A LA PGINA 
 El ingresar a la pgina, se debe capturar el ingreso a la misma como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_indicators_dates 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_indicators_dates 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_indicators_dates &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free 
&#160; 
 M ENSAJE PERSONALIZADO 

 [USER_FIRST_NAME] 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios ?id=&#123;&#123;bo_usuarios. usuario &#125;&#125;&amp;_distinct =nombre_usuario 
&#160; 
 lo sentimos!... &#58;( 
 class= lbl_lo_sentimos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_lo_sentimos ) 
&#160; 
 Tu plan (concat) &#123;&#123;Plan_de_rescate&#125;&#125; (concat) no cuenta con la funcionalidad (concat) de visualizacin de indicadores para fechas diferentes al mes actual . 
 class= lbl_tu_plan ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_plan )&#160; 
&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125;&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
&#160; 
 class= lbl_no_cuenta_con_funcionalidad ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_no_cuenta_con_funcionalidad )&#160; 
&#160; 
 class= lbl_cnf_fechas_indicadores ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cnf_fechas_indicadores )&#160;&#160;&#160; 
&#160; 
 Actualiza tu plan de rescate (concat) para contar con esta funcionalidad que te permite visualizar indicadores generales en para rangos de fechas diferentes al mes actual. 
 class= lbl_actualiza_plan_rescate ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_actualiza_plan_rescate ) 
&#160; 
 class= lbl_para_cnf_fechas_indicadores ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_para_cnf_fechas_indicadores )&#160; 

 I NFORMACIN DE LOS PLANES 
 Como es estndar para todos los planes, su documentacin se puede consultar aqu&#58; 

Informacin Planes 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 UPGRADE POR CONFIGURACIN DE FECHAS PARA INFORMES DE DONACIONES