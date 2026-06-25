# informes-de-anuncios-informe-avanzado-de-cancelados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Validacin del tipo de licencia para el despliegue de la funcionalidad 
 Este informe solo estar disponible para cualquier licencia de Analytics (por confirmar) .&#160; Por lo tanto si un usuario sin licencia analytics o con licencia diferente a la 360 intenta ingresar al informe, el sistema capturar un evento de upgrade y direccionar a la pgina de upgrade respectiva. 
 Por lo tanto, antes de desplegar el informe, el sistema deber realizar validar si la licencia Analytics (que se obtiene con la siguiente consulta) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_data_analytics_cua? eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
 Si la cuenta usuario no tiene licencia analytics, entonces se deber realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

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
 eatc_upgrade_event = upgrade_by_info_avanzado_cancel 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
 eatc_actual_analytics_plan =cua_user_without_analytics_plan 

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
 eatc_upgrade_event = upgrade_by_info_avanzado_cancel 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
 eatc_actual_analytics_plan = cua_user_without_analytics_plan 

&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_info_cancel &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free&amp; eatc_actual_analytics_plan = cua_user_without_analytics_plan 

&#160; 
 Redireccin a pgina de upgrade por informe avanzado de cancelaciones 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/upgrade_by_info_avd_cancel 

&#160; 
 Titulo de la vista&#58; Informe de avanzado de cancelados 
 class=&quot; lbl_info_avanzado_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_avanzado_cancelados )&#160; 
&#160; 
 Descripcin del informe 
 class=&quot; lbl_info_avanzado_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_avanzado_cancelados_desc )&#160; 
&#160; 
 &quot;En este informe podrs encontrar informacin histrica de los cancelados en cantidades y pesos y posiblidad de compar con periodos anteriores.&quot; 
&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
 Valor por defecto&#58; el mismo da del mes, tres meses ms atrs. 
 Valor ms antiguo permitido (inicialmente)&#58; fecha actual del ao anterior (o fecha un ao atrs contada a partir de la fecha final seleccionada). 
&#160; 
 El valor seleccionado se llevar a la variable &#123;&#123;fecha_inicial&#125;&#125; 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 
 Valor por defecto&#58; da actual. 
&#160; 
 El valor seleccionado se llevar a la variable &#123;&#123;fecha_final&#125;&#125; 
&#160; 
 Cargar nueva Info =&gt; Consultar =&gt; SE DEBE EVALUAR SI ESTO ES NECESARIO O SE PUEDE OBVIAR (que simplemente cuando se terminen de seleccionar las fechas se lance el prximo selector) 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 
&#160; 
 La informacin que se visualiza corresponde a los datos en el rango de fechas seleccionado arriba 
 clase=&quot; lbl_info_rango_fechas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_rango_fechas ) 
&#160; 
 Selector mltiple de Departamentos 
 Con el rango de fechas seleccionado el sistema realiza la siguiente consulta para construir un selector mltiple de departamentos (y mostrar solamente aquellos departamentos que poseen cancelados en la fecha), 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125; &amp;eatc-donor=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc-state=cancelled&amp;_distinct= eatc-province 
&#160; 
 &#160;Si la consulta no arroja resultados el sistema deber desplegar el siguiente label&#58; 
 clase=&quot; lbl_sinresultados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_sinresultados )&#160; 
&#160; 
 Si la consulta arroja resultados,&#160; con&#160; el los valores obtenidos de la consulta se conconstruir el siguiente selector mltiple&#58; 
 clase=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_departamento_provincia_estado ) 
&#160; 
 Porcentaje cantidad cancelados =&gt; Porcentaje de anuncios cancelados 
 clase=&quot; lbl_pct_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_anuncios_cancelados ) 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde a la divisin del nmero de anuncios efectivamente cancelados (es decir, con estado &quot;cancelado&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. 
 clase=&quot; lbl_pct_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_anuncios_cancelados_desc )&#160; 
&#160; 
 anuncios cancelados 
 clase=&quot; lbl_anuncios_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_cancelados )&#160; 

&#160; 
 Porcentaje kilogramos cancelados =&gt; % de kilogramos cancelados 
 clase=&quot; lbl_pct_kg_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kg_cancelados )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al peso total de los anuncios cancelados sobre el peso total de anuncios realizados en el periodo 
 clase=&quot; lbl_pct_kg_cancelados_desc &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kg_cancelados_desc) 
&#160; 
 kg cancelados 
 clase=&quot; lbl_kg_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_cancelados )&#160; 

&#160; 
 Porcentaje $pesos cancelados =&gt; % de cancelados en valor al costo 
 clase=&quot; lbl_pct_valor_al_costo_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_valor_al_costo_cancelados )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al valor al costo de los anuncios cancelados sobre el valor al costo de los anuncios realizados en el periodo 
 clase=&quot; lbl_pct_valor_al_costo_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_valor_al_costo_cancelados_desc )&#160; 
&#160; 
 pesos cancelados =&gt;Valor al costo anuncios cancelados 
 clase=&quot; lbl_valor_al_costo_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_cancelados )&#160; 

&#160; 
 Porcentaje referencias canceladas =&gt; % de referencias canceladas 
 clase=&quot; lbl_pct_referencias_canceladas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_referencias_canceladas )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al nmero de referencias canceladas sobre el nmero total de referencias anunciadas en el periodo 
 clase=&quot; lbl_pct_referencias_canceladas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_referencias_canceladas_desc )&#160; 
&#160; 
 Referencias canceladas 
 clase=&quot; lbl_referencias_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_referencias_canceladas ) 

&#160; 
 Porcentaje unidades canceladas =&gt; % de unidades de producto canceladas 
 clase=&quot; lbl_pct_unidades_canceladas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_unidades_canceladas )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al nmero de unidades de producto canceladas sobre el nmero total de unidades de producto anunciadas en el periodo 
 clase=&quot; lbl_pct_unidades_canceladas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=llbl_pct_unidades_canceladas_desc )&#160; 
&#160; 
 Unidades canceladas 
 clase=&quot; lbl_unidades_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_unidades_canceladas )&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 CUENTAS DATAGOV 

 DATA ANALYTICS: INFORMES DE ANUNCIOS > INFORME AVANZADO DE CANCELADOS