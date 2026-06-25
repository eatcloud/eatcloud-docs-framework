# informes-de-anuncios-detalle-de-anuncios.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación&#58;&#160; 
 en esta implementación se deben utilizar de raíz (es decir, desde su implementación inicial) en vez de los textos que se presentan a continuación, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementación de base sea internacionalizada. 

&#160; 
 Nota importante de implementación&#58; se basa enteramente en funcionalidad ya implementada 
 Esta implementación debe constar en el traspaso (o copia exacta) de la funcionalidad &quot; Informe de detalle de anuncios &quot; del BO legacy, con la incorporación de los labels que se relacionan a continuación 

 ***NUEVO&#58; Validación del tipo de licencia para el despliegue de la funcionalidad*** 
 Este informe solo estará disponible para la licencia analytics 360.&#160; Por lo tanto si un usuario sin licencia analytics o con licencia diferente a la 360 intenta ingresar al informe, el sistema capturará un evento de upgrade y direccionará a la página de upgrade respectiva. 
&#160; 
 Antes de desplegar el formulario, el sistema deberá realizar validar si la licencia Analytics (que se obtiene con la siguiente consulta) 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_data_analytics_cua? eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
&#160; 
 Corresponde eatc_data_analytics_cua. eatc_data_analytics_code = 360 y en ese caso permitirá pasar al informe. 
&#160; 
 Si la licencia es diferente a 360 (es decir&#58; eatc_data_analytics_cua. eatc_data_analytics_code = eficiencia ó eatc_data_analytics_cua. eatc_data_analytics_code = sostenibilidad ó&#160; 
eatc_data_analytics_cua. eatc_data_analytics_code = ahorro o si no se obtiene respuesta ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuación y posteriormente lo redireccionará a la página de upgrade respectiva . 

&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_info_dona 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
 eatc_actual_analytics_plan =&#123;&#123; URL_entorno_datagov &#125;&#125;/ api/eatcloud/ eatc_data_analytics_cua ? eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parámetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
&#160; 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_info_dona 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
 eatc_actual_analytics_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua ? eatc_cua =abaco&amp;_distinct= eatc_data_analytics_code = &quot;&quot; (vacío, porque la consulta no arroja resultados) 

&#160; 
 Entonces se realiza el siguiente llamado al API de creación de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_info_dona &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free&amp; eatc_actual_analytics_plan = 

&#160; 
 Redirección a página de upgrade por informe de detalle de donaciones 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/upgrade_by_info_dona 

&#160; 
 Titulo de la vista&#58; Informe de detalle de anuncios 
 class=&quot; lbl_informe_detalle_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_detalle_anuncios ) 
&#160; 
 Descripción del informe 
 class=&quot; lbl_informe_detalle_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_detalle_anuncios_desc ) 

&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 

&#160; ***NUEVO&#58;&#160; Selector de ciudad&#58; *** 
Solo se desplegará este ´filtro, si la cuenta usuario que está logeada en la plataforma tiene licencia rescate (eatc_cua.type) “impacto” o “impactoplus”. 
&#160; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_cua ?name= &#123;&#123;cua_en_el_sistema&#125;&#125; &amp;type= impacto,impactoplus 
&#160; 
 Permite seleccionar la ciudad de la cuál se quiere traer los detalles del anuncio (el selector se construye consultando las ciudades de las donaciones (eatc_dona_headers. eatc-city ) &#160;que corresponden a la selección de los filtros de fechas, con el ánimo de colocar en el selector solamente las ciudades que tienen donaciones en las fechas seleccionadas) 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donor= &#123;&#123;cua_en_el_sistema&#125;&#125; &amp;eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;_distinct=eatc-city 
&#160; 
OPCIÓN DE SELECCIONAR TODAS LAS CIUDADES O ALGUNAS DE ELLAS (SELECTOR MÚLTIPLE) 
 El selector debe traer la opción &quot;Todas&quot; ( class=&quot;lbl_todas&quot; ), que permita seleccionar todas las ciudades y sacar la información de todas ellas. 
 Selector de estados 
 Selecciona el estado 
 clase=&quot; lbl_seleccionar_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_seleccionar_estado ) 
&#160; 
 Labels de estados 
 Se toman del campo &quot; eatc_plural_label &quot; del maestro de estados. 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_headers_states?_id=_* 
 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?_id=_* ) 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 

 &#160; 
&#160; 
 Sumatoria totales 
 class=&quot; lbl_sumatoria_totales &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cu 
 entas&amp;idlabel=lbl_sumatoria_totales ) 
&#160; 
 KG aprovechados 
 clase=&quot; lbl_kg_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_aprovechados ) 
&#160; 
 KG&#160; no aprovechados 
 clase=&quot; lbl_kg_no_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_aprovechados ) 
&#160; 
 Unidades aprovechados 
 clase=&quot; lbl_unidades_aprovechadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_unidades_aprovechadas ) 
&#160; 
 Unidades&#160; no aprovechados 
 clase=&quot; lbl_unidades_no_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_unidades_no_aprovechados ) 
&#160; 
 Costo total 
 clase=&quot; lbl_costo_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_costo_total ) 

&#160; 
 Tabla de información de detalle de anuncios 
La tabla deberá incorporar los labels previamente documentados en la documentación original de la funcionalidad&#58; Información a mostrar en el listado de detalle 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Cuentas datagov 

 432.000000000000 

 DATA ANALYTICS: INFORMES DE ANUNCIOS > DETALLES DE ANUNCIOS