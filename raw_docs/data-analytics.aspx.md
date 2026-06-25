# data-analytics.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general&#58;&#160; 
 La seccin General de Data Analytics tendr disposiciones diferentes de KPIs por el tipo de licencia.&#160; En estas disposiciones se manejarn dos grandes apartados&#58; 
&#160; 
 Tableros &#58; mostrarn KPIs, Grficas y algunos listados consolidando informacin 
 Detalle de anuncios &#58; mostrarn listados detallados de los anuncios y quizs algunos informes especializados al respecto. 

 Men lateral de navegacin para Analytics 
 La conforman los elementos principales de navegacin, que se ubicarn en un men lateral, que ser distintivo de la seccin &quot;Analytics&quot;, a diferencia del men lateral del resto del BO (para retornar a la interfaz en donde se puede visualizar dicho men general se dispondr del botn &quot;Regresa a administrativo&quot;) 

 cono, Nombre del usuario y Nombre de la empresa 
 Funcionar de la misma manera como funciona para el men lateral general del nuevo BO 

 1. SELECCIONAR REPORTE &#58; AGRUPACIN DE ELEMENTOS DEL MEN 
&#160; 
 label&#58; class=&quot;lb_seleccionar_reporte&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_seleccionar_reporte &#160; 
 cono&#58; PENDIENTE 
&#160; 
 De acuerdo a lo configurado para la cuenta que accede al tablero ( &#123;&#123;_DOM. cua_user &#125;&#125; ) en&#160; &quot; eatc_data_analytics_cua &quot; , que se consulta de la siguiente manera&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
&#160; 
 Se debern mostrar los selectores con los labels que se obtienen de las siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=&#123;&#123; eatc_data_analytics_code &#125;&#125;&amp;_distinct=eatc_label 
&#160; 
 Como el grupo grupo de elementos de men,&#160; agrupados por este y que se relacionan a continuacin. 

 1.1. Eficiencia&#58; elemento de men 
 label&#58; ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=eficiencia&amp;_distinct=eatc_label ) 
 class=&quot; lbl_eficiencia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_eficiencia ) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Eficiencia &gt; Tablero &gt; Resultados Generales 
&#160; 
 Si la cuenta tiene licencia 360 o la licencia &quot;eficiencia&quot; esta ser la vista por defecto de, es decir, al abrir Analytics se deber abrir este informe. 

&#160; 
 1.2. Sostenibilidad&#58; elemento demen 
 label&#58; ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=sostenibilidad&amp;_distinct=eatc_label ) 
 class=&quot; lbl_sostenibilidad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_sostenibilidad ) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Sostenibilidad &gt; Tablero &gt; Resultados Generales 
&#160; 
 Si la cuenta tiene solamente la licencia &quot;sostenibilidad&quot; esta ser la vista por defecto de, es decir, al abrir Analytics se deber abrir este informe. 

&#160; 
 1.3. Ahorro&#58; elemento de men 
 label&#58; ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=ahorro&amp;_distinct=eatc_label ) 
 class=&quot; lbl_ahorro &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ahorro &#160; 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Ahorro &gt; Tablero &gt; Resultados Generales 
&#160; 
 Si la cuenta tiene solamente la licencia &quot;ahorro&quot; esta ser la vista por defecto de, es decir, al abrir Analytics se deber abrir este informe. 

&#160; 
 2. Informes de anuncios&#58; Agrupacin de elementos del men 
 label&#58; class=&quot;lb_informes_anuncios&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_informes_anuncios &#160; 
 cono&#58; PENDIENTE 
&#160; 
 En esta agrupacin de elementos de mens se dispondrn vnculos para los siguientes informes&#58; 
&#160; 
 2.1. Detalle de anuncios&#58; elemento de men 
 label&#58;&#160; 
 class=&quot; lbl_detalle_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_detalle_anuncios ) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Informes de anuncios &gt; Detalles de anuncios 

&#160; 
 2.2. Programados y despachados&#58; elemento de men 
 label&#58;&#160; 
 class=&quot; lbl_programados_despachados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_programados_despachados ) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Informes de anuncios &gt; Programados y despachados 

&#160; 
 2.3. Rechazos&#58; elemento de men 
 label&#58;&#160; 
 class=&quot; lbl_rechazos &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_rechazos) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Informes de anuncios &gt; Rechazos 

&#160; 
 2.3. Cancelados&#58; elemento de men 
 label&#58;&#160; 
 class=&quot; lbl_cancelados &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cancelados) 
 cono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Informes de anuncios &gt; Cancelados 

&#160; 

 Filtro de fechas&#58; 
 Se implementarn filtros de fechas que tendrn los siguientes valores.&#160; Siendo el valor por defecto &quot;Este mes&quot; (Mes Actual) 

 Se podra implementar tomando como base la implementado en resultados, adicionando los valores faltantes de filtro como se especifica a continuacin 

 Filtro&#58; &quot;Ayer&quot; 
 class=&quot; lbl_ayer &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ayer ) 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero del da anterior. 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hoy ) 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero del da actual. 
&#160; 
 Filtro&#58; &quot;Esta Semana&quot; 
 class=&quot; lbl_esta_semana &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_esta_semana ) 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero de la presente semana (que empieza el da lunes). 
&#160; 
 Filtro&#58; &quot;ltimos 8 das&quot; 
 class=&quot; lbl_ultimos_8_dias &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ultimos_8_dias) 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero de los ltimos 8 das o la ltima semana. 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; =&gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero del mes en curso (empezando por el primer da del mes actual). 
&#160; 
 Filtro&#58; &quot;ltimos 30 das&quot;&#160; 
 class=&quot; lbl_ultimos_30_dias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ultimos_30_dias ) 
&#160; 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero de los ltimos treinta das 
&#160; 
 Filtro&#58; &quot;ltimo trimestre&quot;&#160; 
 class=&quot; lbl_ultimo_trimestre &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ultimo_trimestre ) 
&#160; 
 Si se selecciona, muestra datos en las diferentes pginas o secciones del tablero de los ltimos noventa das 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial ) 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 

 Botones de acceso a informes o secciones del tablero =&gt; Franja superior de navegacin 
 Todos los Tableros (eficiencia&#58; 4 tableros, sostenibilidad&#58; 3 tableros, ahorro&#58; 4 tableros), tendrn una barra de botones inmediatamente despus de los filtros, que dar ingreso a los diferentes tableros de BO que se han diseado para el nuevo BO (Datagov Cuentas).&#160; A continuacin se muestra el mockup de cmo seran estos botones para el Tablero &quot;eficiencia&quot;. 

 Para cada barra de navegacin se cre una pgina de documentacin a parte, dado que se repiten tablero, tras tablero. 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 

 Sostenibilidad&#160; &gt; Tableros &gt; Franja de navegacin superior 

 Ahorro&#160; &gt; Tableros &gt; Franja de navegacin superior 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdata-analytics%2F646132265-Analytics_general.jpg&ow=1055&oh=706, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdata-analytics%2F646132265-Analytics_general.jpg&ow=1055&oh=706 
 Cuentas datagov 

 355.000000000000 

 DATA ANALYTICS