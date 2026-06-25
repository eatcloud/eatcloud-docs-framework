# sostenibilidad-tablero-resultados-generales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Se puede basar en la implementacin&#58;&#160; 
 Eficiencia &gt; Tablero &gt; Resultados Generales &#160; 

&#160; 
 Mockup&#58; 

 Sostenibilidad&#160; &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Resultados generales 
 class=&quot; lbl_resultados_generales &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_resultados_generales ) 

 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario&#58; grfico de tendencia) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto . El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer&#58; en este caso no se genera grfico).&#160; 

 Kilogramos entregados (en el diseo Kg Donados) =&gt; nos podemos basar en la implementacin de &quot; Eficiencia &gt; Tablero &gt; Resultados generales &gt; KPIs Principales &gt; Kilogramos entregados &quot;&#58; KPI por defecto 
&#160; 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Corresponde al total de kg entregados, es decir, aquellos KG que fueron efectivamente despachados (se valid el cdigo de entrega) y recibidos por los beneficiarios (se verific el contenido de la donacin) para los anuncios (cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;) del periodo en cuestin. 

&#160; 
 Nmero de anuncios realizados (en el diseo Anuncios publicados) =&gt; nos podemos basar en la implementacin de &quot; Eficiencia &gt; Tablero &gt; Resultados generales &gt; KPIs Principales &gt; Nmero de anuncios realizados &quot; 
&#160; 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Cantidad de anuncios de donacin generados en el periodo en cuestin. 

&#160; 
 KG de CO2 ahorrados (en el diseo&#58; Emisiones de CO2 (Ton)) =&gt; Se puede basar en la implementacin de BO o en la de Antigua WAPP 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_desc ) 
&#160; 
 Corresponde a la cantidad de KG de CO2 que le ests ahorrando al planeta por tu decisin de donar en vez de botar, en el periodo establecido (para anuncios cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;).&#160; 
 Nota para el desarrollo&#58; Se puede obtener del KPI &quot; CO2_tons &quot; (multiplicndolo por 1000). 

&#160; 
 Platos servidos (en el diseo&#58; &quot;Raciones servidas) =&gt; Se puede basar en la implementacin de BO o en la de Antigua WAPP 
&#160; 
 class=&quot; lbl_platos_servidos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_platos_servidos ) 
&#160; 
 class=&quot; lbl_platos_servidos_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_platos_servidos_desc ) 
&#160; 
 Corresponde a la sumatoria del total de porciones servidas a partir de las donaciones entregadas (con verificacin del cdigo de recogida y verificacin detallada de la donacin por por parte de los beneficiarios), en el periodo seleccionado. 
&#160; 
 Nota para el desarrollo&#58; Se puede obtener del KPI &quot; total_portions &quot; 

&#160; 
 Nmero de organizaciones beneficiadas 
 class=&quot; lbl_organizaciones_beneficiadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_organizaciones_beneficiadas ) 
&#160; 
 class=&quot; lbl_organizaciones_beneficiadas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_organizaciones_beneficiadas_desc ) 
&#160; 
 Corresponde a la cantidad de organizaciones sociales que se le han despachado por lo menos una donacin en el periodo en cuestin 
 cont de &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= received,pre-certified,certified &amp;_distinct= eatc-donation_manager_code 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= received,pre-certified,certified &amp;_distinct=eatc-donation_manager_code = 49 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-resultados-generales%2F1013193413-sostenibilidad_tablero_resultados_generales.jpg&ow=936&oh=600, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-resultados-generales%2F1013193413-sostenibilidad_tablero_resultados_generales.jpg&ow=936&oh=600 
 Cuentas datagov 

 389.000000000000 

 DATA ANALYTICS: SOSTENIBILIDAD > TABLERO > RESULTADOS GENERALES (INFORME POR DEFECTO)