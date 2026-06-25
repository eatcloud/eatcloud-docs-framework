# informes-de-anuncios-cancelados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

&#160; 
 Nota importante de implementacin&#58; se basa enteramente en funcionalidad ya implementada 
 Esta implementacin debe constar en el traspaso (o copa exacta) de la funcionalidad &quot; Informe de cancelados &quot; del BO legacy, con la incorporacin de los labels que se relacionan a continuacin 

 ***NUEVO&#58; Validacin del tipo de licencia para el despliegue de la funcionalidad*** 
 Este informe solo estar disponible para la licencia analytics 360.&#160; Por lo tanto si un usuario sin licencia analytics o con licencia diferente a la 360 intenta ingresar al informe, el sistema capturar un evento de upgrade y direccionar a la pgina de upgrade respectiva. 
&#160; 
 Por lo tanto, antes de desplegar el informe, el sistema deber realizar validar si la licencia Analytics (que se obtiene con la siguiente consulta) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_data_analytics_cua? eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
&#160; 
 Corresponde eatc_data_analytics_cua. eatc_data_analytics_code = 360 y en ese caso permitir pasar al informe. 
&#160; 
 Si la licencia es diferente a 360 (es decir&#58; eatc_data_analytics_cua. eatc_data_analytics_code = eficiencia eatc_data_analytics_cua. eatc_data_analytics_code = sostenibilidad eatc_data_analytics_cua. eatc_data_analytics_code = ahorro o si no se obtiene respuesta ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin y posteriormente lo redireccionar a la pgina de upgrade respectiva . 

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
 eatc_upgrade_event = upgrade_by_info_cancel 
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
 eatc_upgrade_event = upgrade_by_info_cancel 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
 eatc_actual_analytics_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua ? eatc_cua =abaco&amp;_distinct= eatc_data_analytics_code = &quot;&quot; (vaco, porque la consulta no arroja resultados) 

&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_info_cancel &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free&amp; eatc_actual_analytics_plan = 

&#160; 
 Redireccin a pgina de upgrade por informe de cancelaciones 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/upgrade_by_info_cancel 
&#160; 
 Titulo de la vista&#58; Informe de cancelaciones 
 class=&quot; lbl_informe_cancelaciones &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_cancelaciones ) 
&#160; 
 Descripcin del informe 
 class=&quot; lbl_informe_cancelaciones_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_cancelaciones_desc ) 
&#160; 
 &quot;En este informe podrs encontrar el detalle de los anuncios que fueron cancelados, porque excedieron el tiempo estipulado para su asignacin a un beneficiario y su debida gestin.&quot; 
&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
 Valor por defecto&#58; primer da del mes actual. 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 
 Valor por defecto&#58; da actual. 
&#160; 
 Cargar nueva Info =&gt; Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 
&#160; 
 La informacin que se visualiza corresponde a los datos en el rango de fechas seleccionado arriba 
 clase=&quot; lbl_info_rango_fechas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_rango_fechas ) 

 Anuncios =&gt; Anuncios de donacin 
 clase=&quot; lbl_anuncios_de_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_de_donacion ) 
&#160; 
 Total anuncios&#58; se puede cambiar por un tooltip =&gt; Conteo de anuncios de donacin realizados 
 clase=&quot; lbl_anuncios_de_donacion_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_de_donacion_desc ) 
&#160; 
 Anuncios =&gt; Peso total de los anuncios 
 clase=&quot; lbl_peso_anuncios_de_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_peso_anuncios_de_donacion ) 
&#160; 
 Total kg&#58; se puede cambiar por un tooltip =&gt; Sumatoria del peso de todos los anuncios realizados en kilogramos 
 clase=&quot; lbl_peso_anuncios_de_donacion_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_peso_anuncios_de_donacion_desc ) 

&#160; 
 Anuncios =&gt; Valor al costo de los anuncios 
 clase=&quot; lbl_valor_al_costo_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_anuncios )&#160; 
&#160; 
 Total $ pesos&#58; se puede cambiar por un tooltip =&gt; Sumatoria del valor al costo de los anuncios realizados en el periodo 
 clase=&quot; lbl_valor_al_costo_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_anuncios_desc )&#160; 

&#160; 
 Referencias 
 clase=&quot; lbl_referencias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_referencias )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al conteo de cdigos de producto (referencias&#58; PLUs, SKUs, EANs, ...) donados en el periodo 
 clase=&quot; lbl_referencias_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_referencias_desc )&#160; 
&#160; 
 Unidades 
 clase=&quot; lbl_unidades &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_unidades )&#160; 
&#160; 
 No esta&#58; se puede incorporar como un tooltip =&gt; Corresponde al conteo de unidades de producto donadas en el periodo 
 clase=&quot; lbl_unidades_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_unidades_desc )&#160; 

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

 Indicadores 
 clase=&quot; lbl_indicadores &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_indicadores )&#160; 
&#160; 
 Cantidad de anuncios cancelados por + &quot; lbl_eatc_pods_typolgy_a &quot; (marca en el ejemplo) 
 clase=&quot; lbl_cnt_anuncios_cancelados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cnt_anuncios_cancelados_por )&#160; 
&#160; 
 clase=&quot; lbl_eatc_pods_typolgy_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_eatc_pods_typolgy_a ) 

&#160; 
 Cantidad de anuncios cancelados por + &quot; lbl_eatc_pods_typolgy_b &quot; (Subzona en el ejemplo) 
 clase=&quot; lbl_cnt_anuncios_cancelados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cnt_anuncios_cancelados_por )&#160; 
&#160; 
 clase=&quot; lbl_eatc_pods_typolgy_b &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_eatc_pods_typolgy_b ) 

 &#160;Cantidad de anuncios cancelados por da&#160; 
 clase=&quot; lbl_cnt_anuncios_cancelados_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cnt_anuncios_cancelados_por_dia )&#160; 

 Kilogramos cancelados por + &quot;lbl_pod&quot; (almacn en el ejemplo) 
 clase=&quot; lbl_kg_cancelados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_cancelados_por )&#160; 
&#160; 
 clase=&quot; lbl_pod &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pod )&#160; 

&#160; 
 Cantidad por =&gt; Cantidad de anuncios cancelados por + &quot; lbl_pod &quot; (almacn en el ejemplo) 
 clase=&quot; lbl_cnt_anuncios_cancelados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cnt_anuncios_cancelados_por )&#160; 
&#160; 
 clase=&quot; lbl_pod &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pod ) 

&#160; 
 $ pesos =&gt; Valor al costo cancelado por + &quot; lbl_pod &quot; (almacn en el ejemplo) 
 clase=&quot; lbl_valor_al_costo_cancelado_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_cancelado_por )&#160; 
&#160; 
 clase=&quot; lbl_pod &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pod ) 

&#160; 
 KG por ciudad =&gt; Kilogramos cancelados por ciudad 
 clase=&quot; lbl_kg_cancelados_por_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_cancelados_por_ciudad )&#160; 

&#160; 
 Cantidad por ciudad=&gt; Cantidad de anuncios cancelados por ciudad (almacn en el ejemplo) 
 clase=&quot; lbl_cnt_anuncios_cancelados_por_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cnt_anuncios_cancelados_por_ciudad )&#160; 

&#160; 
 $ pesos&#160; por ciudad =&gt; Valor al costo cancelado por ciudad 
 clase=&quot; lbl_valor_al_costo_cancelado_por_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_cancelado_por_ciudad )&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformes-de-anuncios-cancelados%2F1280606033-informe_cancelaciones_1.jpg&ow=1280&oh=543, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformes-de-anuncios-cancelados%2F1280606033-informe_cancelaciones_1.jpg&ow=1280&oh=543 
 Cuentas datagov 

 438.000000000000 

 DATA ANALYTICS: INFORMES DE ANUNCIOS > CANCELADOS