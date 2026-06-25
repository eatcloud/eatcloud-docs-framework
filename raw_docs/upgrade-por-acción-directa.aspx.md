# upgrade-por-acción-directa.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 URL&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/upgrade_rescue_plan 

 R EGISTRO DE EVENTO DE UPGRADE AL INGRESAR A LA PÁGINA 
 El ingresar a la página, se debe capturar el ingreso a la misma como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_rescue_plan 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parámetros se separan por &quot; &amp; &quot;) 
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
 eatc_upgrade_event = upgrade_rescue_plan 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creación de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_rescue_plan &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free 
&#160; 
 WIREFRAME PROPUESTO 

 E NCABEZADO DE CONTACTO 

 ¿Tienes dudas acerca del precio o de la facturación? 
 class= lbl_dudas_plan ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_dudas_plan )&#160;&#160; 

&#160; 
 Botón&#58; Chatea con nosotros 
 class= lbl_chatea_con_nosotros ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_chatea_con_nosotros )&#160; 
&#160; 
 ***NUEVO*** Script de chat de ventas 
 Se debe incorporar el siguiente script que debe desplegarse cuando se hace clic en el botón&#58; 
 &lt;script type='text/javascript'&gt; 
 var fc_JS=document.createElement('script'); 
 fc_JS.type='text/javascript'; 
 fc_JS.src='https&#58;//wchat.freshchat.com/js/widget.js?t='+Date.now(); 
 (document.body?document.body&#58;document.getElementsByTagName('head')[0]).appendChild(fc_JS);&#160; 
 window.fcSettings = &#123; token&#58;'215398d9-f3d5-4d5b-9834-0255cea3dfe8', host &#58; 'https&#58;//wchat.freshchat.com'&#125;; 
 &lt;/script&gt; 

 Nota para la implementación&#58; una vez implementado se deberán realizar pruebas unitarias, para determinar si el script funciona.&#160; En caso de que no lo haga se debe informar a Juan David Correa, para solicitar de nuevo la información (dado que con la que se ha obtenido hasta el momento no se puede verificar el correcto funcionamiento de la misma. 

 M ENSAJE PERSONALIZADO 

 Elige tu plan 
 class= lbl_elige_tu_plan ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_elige_tu_plan )&#160; 
&#160; 
 Amplía tu capacidad para darle una segunda oportunidad a tus alimentos, más donaciones y mejor soporte 
 class= lbl_elige_tu_plan_desc ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_elige_tu_plan_desc )&#160; 

 S ELECTOR DE TIPO DE ACTUALIZACIÓN 

 Planes Rescate&#160; =&gt; Valor por defecto (en el diseño&#58; Licencias EatCloud) 
 class= lbl_planes_rescate ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_planes_rescate )&#160; 
&#160; 
 Estos cuando se selecciona esta opción, en la parte inferior de la página se muestra la Información de los Planes Rescate (tal como se define más adelante ). 
&#160; 
 EatCloud Analytics (en el diseño&#58; Data Analítica) 
 class= lbl_eatcloud_analytics ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_eatcloud_analytics )&#160;&#160; 
&#160; 
 Registro de evento de upgrade 
 El ingresar a la página, se debe capturar el ingreso a la misma como un evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_eatcloud_analytics 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parámetros se separan por &quot; &amp; &quot;) 
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
 eatc_upgrade_event = upgrade_eatcloud_analytics 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creación de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_eatcloud_analytics &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free 
&#160; 
 Redirecciona ( provisional ) 
 Al oprimir el botón, se redireccionará a la &quot; Landing analytics &quot;. 

 INFORMACIÓN DE LOS PLANES 
 Como es estándar para todos los planes, su documentación se puede consultar aquí&#58; Información Planes 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fupgrade-por-acci%C3%B3n-directa%2F2320922813-upgrade_directo_2.jpg&ow=862&oh=262, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fupgrade-por-acci%C3%B3n-directa%2F2320922813-upgrade_directo_2.jpg&ow=862&oh=262 

 457.000000000000 

 UPGRADE POR ACCIÓN DIRECTA