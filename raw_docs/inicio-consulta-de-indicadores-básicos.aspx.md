# inicio-consulta-de-indicadores-básicos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Label Ttulo de la Vista ***NUEVO*** &#58; 
 class=&quot;lbl_inicio&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_inicio ) 
&#160; 
 Label Descripcin de la Vista&#58; 
 class=&quot;lb_consulta_tus_resultados_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_consulta_tus_resultados_desc ) 

 Mockup propuesto 
 Nos han propuesto este mockup (no se debe prestar mucha atencin a la definicin del men lateral, ya que la misma se est armonizando en la respectiva documentaci) para la funcionalidad.&#160; Se puede tener como base la misma funcionalidad de &quot; Resultados &quot; propuesta para la nueva WAPP, pero en este caso las consultas no se realizarn por punto de donacin sino por cuenta, para obtener los datos de toda la cuenta.&#160; 

 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual&#58; en este caso no se genera grfico).&#160; 

 Se trabajarn entonces con estos 4 KPIs bsicos ya implementados en &quot; Resultados &quot; (a excepcin del KPI de CO2) 

 El filtro del informe trabajar de igual manera a como trabaja en el informe que se tomar como base y que fue desarrollado para la nueva WAPP 

 Descripcin tcnica&#58; 
 Se toman todos los labels implementados en &quot; Resultados de la nueva WAPP &quot; 

 Subttulo&#58; 
 class=&quot; lbl_indicadores_clave &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_indicadores_clave ) 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hoy ) 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
&#160; 
 *** NUEVO &#58; Validacin del tipo de licencia para el despliegue de la funcionalidad&#58; personalizacin de fechas*** 
 La posibilidad de consultar indicadores en periodos diferentes al mes actual no estar disponible para licencias &quot;free&quot;.&#160; Por lo tanto si un usuario con licencia free intenta personalizar la fecha para la presentacin de indicadores, el sistema capturar un evento de upgrade y direccionar a la pgina de upgrade respectiva. 
&#160; 
 Antes de desplegar el formulario, el sistema deber realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua? name =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= type 
&#160; 
 Corresponde eatc_cua. type = free debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_indicators_dates 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
 eatc_actual_analytics_plan =&#123;&#123; URL_entorno_datagov &#125;&#125;/ api/eatcloud/ eatc_data_analytics_cua ? eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
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
 eatc_actual_analytics_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua ? eatc_cua =abaco&amp;_distinct= eatc_data_analytics_code = &quot;&quot; (vaco, porque la consulta no arroja resultados) 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_indicators_dates &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free&amp; eatc_actual_analytics_plan = 

&#160; 
 Redireccin a pgina de upgrade por informe de detalle de donaciones 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/ upgradebyindicatorsdates 
&#160; 
 En caso que la cuenta tenga una licencia diferente a eatc_cua. type = free entonces el sistema permitir la configuracin de fechas para el despliegue de indicadores, mostrando los siguientes labels y funcionalidades&#58; 

&#160; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial ) 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 

 Monto donado 
 class=&quot; lbl_monto_donado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_monto_donado ) 
&#160; 
 class=&quot; lbl_monto_donado_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_monto_donado_desc ) 
&#160; 
 Kilogramos entregados 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Nmero de anuncios realizados 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Anuncios cancelados 
 class=&quot; lbl_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados ) 
&#160; 
 class=&quot; lbl_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados_desc &#160; ) 

 NPS 
 Se deber implementar la medicin del NPS, tal como se implement en su momento para el BO Donantes . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finicio-consulta-de-indicadores-b%C3%A1sicos%2F3841115728-linea_kpis.jpg&ow=472&oh=99, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finicio-consulta-de-indicadores-b%C3%A1sicos%2F3841115728-linea_kpis.jpg&ow=472&oh=99 
 Cuentas datagov 

 306.000000000000 

 INICIO - CONSULTA DE INDICADORES BSICOS