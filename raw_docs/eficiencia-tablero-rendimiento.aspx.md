# eficiencia-tablero-rendimiento.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Mockup&#58; 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Rendimiento 
 class=&quot; lbl_rendimiento &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_rendimiento ) 

 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto .&#160; El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer&#58; en este caso no se genera grfico).&#160; 

 Porcentaje de anuncios despachados =&gt; KPI por defecto 
 class=&quot; lbl_pct_anuncios_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados ) 
&#160; 
 class=&quot; lbl_pct_anuncios_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados_desc ) 
&#160; 
 Corresponde a la divisin del nmero de anuncios despachados por el donante (es decir, con estados&#58; &quot;despachado (delivered)&quot;, &quot;recibido (received)&quot;, &quot;pre-certificado (pre-certified)&quot; y &quot;certificado (certified)&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. 
 ( ( &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= delivered , received,pre-certified,certified &amp;_cont ) / ( &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont ) )*100% 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 ( ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= received,pre-certified,certified &amp;_cont ) / ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;_cont ) )*100% = ( 82 / 169 )*100% = 48% 

&#160; 
 % Kilogramos despachados 
 class=&quot; lbl_pct_kilogramos_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_kilogramos_entregados ) 
&#160; 
 class=&quot; lbl_pct_kilogramos_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_kilogramos_entregados_desc ) 
&#160; 
 Corresponde a la divisin del total de kilogramos de los anuncios efectivamente despachados ( eatc-total_weight_kg ) por los beneficiarios (es decir, con estados&#58; &quot;despachado (delivered)&quot;, &quot;recibido (received)&quot;, &quot;pre-certificado (pre-certified)&quot; y &quot;certificados (certified)&quot;),&#160; sobre el peso original ( original_weight_kg ) de los anuncios (todos los anuncios) generados en el periodo. 

&#160; 
 Tiempo promedio de adjudicacin de anuncios en minutos 
 class=&quot; lbl_tiempo_promedio_adjudicacion_min &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_promedio_adjudicacion_min ) 
&#160; 
 class=&quot; lbl_tiempo_promedio_adjudicacion_min_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_promedio_adjudicacion_min_desc ) 
&#160; 
 Corresponde a el promedio&#160; del tiempo de adjudicacin (medido en minutos) de los anuncios despachados en el periodo, el cual se calcula (para cada anuncio despachado) restndole a la fecha y hora de adjudicacin la fecha y hora en que los anuncios son publicados) *** (Nota&#58; revisar el KPI&#58;&#160; tiempo_de_adjudicacion_del_anuncio porque la idea es simplificar el guarismo calculndolo desde la fecha y hora de publicacin y no la fecha y hora del match) *** 

&#160; 
 Tiempo promedio de recogida de los anuncios en horas 
 class=&quot; lbl_tiempo_promedio_recogida_horas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_promedio_recogida_horas ) 
&#160; 
 class=&quot; lbl_tiempo_promedio_recogida_horas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_promedio_recogida_horas_desc ) 
 Corresponde a el promedio&#160; del tiempo de recogida (medido en horas y minutos) de los anuncios despachados en el periodo, el cual se calcula (para cada anuncio despachado) restndole a la fecha y hora de llegada del beneficiario al punto de donacin,&#160; la fecha y hora de adjudicacin del anuncio. *** (Nota&#58; se puede tomar del KPI&#58;&#160; tiempo_de_total_para_la_recogida ) *** 

&#160; 
 Porcentaje de anuncios cancelados ( en nmero de anuncios ) 
 class=&quot; lbl_pct_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_cancelados ) 
&#160; 
 class=&quot; lbl_pct_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_cancelados_desc ) 
&#160; 
 Corresponde a la divisin del nmero de anuncios efectivamente cancelados (es decir, con estado &quot;cancelado&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. 
 ( ( &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= cancelled &amp;_cont ) / ( &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont ) )*100% 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 ( ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= cancelled &amp;_cont ) / ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;_cont ) )*100% = ( 2 / 169 )*100% = 1.18% 

 KPIs secundarios&#160; 

 Anuncios no entregados&#160; 
 class=&quot; lbl_anuncios_no_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_no_entregados ) 
&#160; 
 class=&quot; lbl_anuncios_no_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_no_entregados_desc ) 
&#160; 
 Corresponde al nmero de anuncios cuyo estado es &quot;no entregado&quot; para el periodo en cuestin (son aquellos anuncios generados y adjudicados, y que el beneficiario inform que no se le entregaron al acercarse al punto de donacin). 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= not_delivered &amp;_cont 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= not_delivered &amp;_cont = 2 

&#160; 
 Kilogramos no entregados 
 class=&quot; lbl_kg_no_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_entregados ) 
&#160; 
 class=&quot; lbl_no_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_entregados_desc ) 
&#160; 
 Corresponde a la sumatoria de los kilogramos totales ( eatc-total_weight_kg ) de los anuncios cuyo estado es &quot;no entregado&quot; para el periodo en cuestin (son aquellos anuncios generados y adjudicados, y que el beneficiario inform que no se le entregaron al acercarse al punto de donacin). 

&#160; 
 Promedio de kilogramos entregados por da (no est en el diseo) 
 class=&quot; lbl_prom_kg_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_prom_kg_dia ) 
&#160; 
 class=&quot; lbl_prom_kg_dia_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_prom_kg_dia_desc ) 
 Corresponde a la divisin del total de kilogramos de los anuncios efectivamente recibidos ( eatc-total_weight_kg ) por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;),&#160; sobre el nmero de das del periodo seleccionado. 

&#160; 
 Kilogramos no recogidos (awarded, scheduled) 
 class=&quot; lbl_kg_no_recogidos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_recogidos ) 
&#160; 
 class=&quot; lbl_kg_no_recogidos_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_recogidos_desc ) 
&#160; 
 Corresponde a la sumatoria de los kilogramos totales ( eatc-total_weight_kg ) de los anuncios cuyo estado es &quot;adjudicado (awarded)&quot; y &quot;programado (scheduled)&quot; para el periodo en cuestin (son aquellos anuncios que han sido asignados a un beneficiario pero que no han sido recogidos an). 

&#160; 
 Anuncios cancelados&#160; 
 class=&quot; lbl_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados ) 
&#160; 
 class=&quot; lbl_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados_desc ) 
&#160; 
 Corresponde al nmero de anuncios que el sistema cancela porque no fueron adjudicados en el tiempo estipulado para ello en el periodo en cuestin. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= cancelled &amp;_cont 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= cancelled &amp;_cont = 2 

&#160; 
 Tiempo promedio de espera para la recogida en horas 
 class=&quot; lbl_tiempo_prom_espera_recogida_horas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_prom_espera_recogida_horas ) 
&#160; 
 class=&quot; lbl_tiempo_prom_espera_recogida_horas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_tiempo_prom_espera_recogida_horas_desc ) 
 Corresponde al promedio de la diferencia entre la hora programada de recogida y la hora real de la recogida de las donaciones expresada en horas y minutos. 
 Promedio para el periodo de tiempo del KPI&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_kpi_rules?eatc_type=process&amp;_id=21 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-rendimiento%2F2489000862-eficiencia_tablero_rendimiento.jpg&ow=968&oh=754, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-rendimiento%2F2489000862-eficiencia_tablero_rendimiento.jpg&ow=968&oh=754 
 Cuentas datagov 

 367.000000000000 

 DATA ANALYTICS: EFICIENCIA > TABLERO > RENDIMIENTO