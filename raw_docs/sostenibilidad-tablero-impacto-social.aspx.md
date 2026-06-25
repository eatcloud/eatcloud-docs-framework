# sostenibilidad-tablero-impacto-social.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Se puede basar en la implementacin&#58;&#160; 
 Eficiencia &gt; Tablero &gt; Resultados avanzados 
&#160; 
 Mockup&#58; 

 Sostenibilidad&#160; &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Impacto social 
 class=&quot; lbl_impacto_social &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_impacto_social) 

 R ESULTADOS SEGN TIPOLOGA A 
 Se mostrarn en un primer grfico, los resultados por la tipologa a ( class=&quot; lbl_eatc_pods_typolgy_a &quot; ) de los puntos de donacin de la cuenta respectiva. 

 R ESULTADOS SEGN TIPOLOGA A DE PUNTOS DE DONACIN 

 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
&#160; 
 class=&quot; lbl_resultados_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_resultados_segun ) 
&#160; 
 Seguido de&#160; 
&#160; 
 class=&quot; lbl_eatc_pods_typolgy_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_a ) 
 (valor por defecto&#58; &quot; tipologa a de puntos de donacin &quot; 

 Selector de KPI 
 La interfaz presentar un selector de KPIs de resultados, que permitir al usuario elegir uno (entre los que a continuacin se relacionan) y poder visualizar el grfico de barras, con los datos del indicador seleccionado para cada una de las tipologas a de puntos de donacin de la cuenta en particular en el periodo seleccionado .&#160; El label del indicador, estar acompaado tambin de un tooltip que desplegar la descripcin del mismo ( _desc ).&#160; 
&#160; 
 Existir un KPI por defecto , que ser el que se muestre cuando, se abra el informe y que ms adelante se especifica. Cuando se cambia a otro indicador, el grfico de tendencia variar segn la seleccin.&#160; 

 Grfico de barras por tipologa a de puntos de donacin 
 En las barras se podr observar el indicador para cada uno de las tipologas a de los puntos de donacin que la cuenta tiene registradas, para el periodo seleccionado. 
&#160; 
 A continuacin se presentarn los indicadores o KPIs de resultados que se desplegarn en el selector (y por ende, al presionarlo, en las grficas de barras). 

 Indicadores de resultados 
 Estos indicadores son dos de los que se implementaron en Sostenibilidad &gt; Tablero &gt; Resultados generales &gt; KPIs Principales , y por lo tanto se podr basar la implementacin en esa implementacin previa. 
&#160; 
 Platos servidos (en el diseo&#58; &quot;Raciones servidas) =&gt; Se puede basar la implementacin de Sostenibilidad &gt; Tablero &gt; Resultados generales &gt; KPIs Principales &gt; Platos&#160; servidos &#58; KPI por defecto 
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

 R ESULTADOS SEGN TIPOLOGA B 
 Se mostrarn en segundo lugar, los resultados por la tipologa b ( class=&quot; lbl_eatc_pods_typolgy_b &quot; ) de los puntos de donacin de la cuenta respectiva. 

 La dinmica de presentacin es similar a la de los resultados por tipologa A (arriba descritos) , variando simplemente los ttulos y el criterio de agrupacin de la estadstica de barras (ahora ser la tipologa b de los puntos de donacin.&#160; Los indicadores sern los mismos que los arriba documentados (por lo tanto no se vuelven a relacionar) 

 R ESULTADOS SEGN TIPOLOGA B DE PUNTOS DE DONACIN 

 La implementacin tiene la misma dinmica de la anteriormente documentada (selector de KPIs, Grfico de Barras por Tipologa A), por lo tanto solo haremos referencia la aquello que vara con respecto a la anterior implementacin 
 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
 class=&quot; lbl_resultados_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_resultados_segun ) 
 Seguido de&#160; 
 class=&quot; lbl_eatc_pods_typolgy_b &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_b ) 
 (valor por defecto&#58; &quot; tipologa b de puntos de donacin &quot; 

 P LATOS SERVIDOS POR CIUDAD (EN EL DISEO&#58; RACIONES SERVIDAS POR CIUDAD ) 
 En un grfico de torta (o circular) se debe mostrar el nmero de platos servidos por ciudad para la cuenta en cuestin, presentando un listado accesorio, con datos que completen la informacin del grfico (sobre todo para donantes con muchas ciudades y donde algunas de ellas, tienen resultados poco significativos en el total). 

 Aquel grupo de ciudades que pesen en conjunto menos del 7% del total, se debern agrupar en la torta como &quot;otras ciudades, tal como se ejemplifica en el siguiente grfico (para el caso de pases) 

 Ttulo de la seccin&#58; Platos servidos por ciudad 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
&#160; 
 class=&quot; lbl_platos_servidos_por_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_platos_servidos_por_ciudad ) 
&#160; 
 Tabla de informacin por ciudad&#58; 

 La tabla contendr la siguiente informacin. 
&#160; 
 Ciudad 
 class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_ciudad ) 
&#160; 
 Muestra la ciudad sobre la cual se presentan estadsticas&#160; 
&#160; 
 Platos servidos (en el diseo&#58; Raciones servidas) 
 class=&quot; lbl_platos_servidos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_platos_servidos ) 
&#160; 
 class=&quot; lbl_platos_servidos_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_platos_servidos_desc ) 
&#160; 
 Muestra el total de platos servidos para la ciudad en cuestin. 
&#160; 
 Nota para el desarrollo&#58; Se puede obtener del KPI &quot; total_portions &quot;. 

&#160; 
 Grupo Etario 
 class=&quot; lbl_grupo_etario &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_grupo_etario ) 
&#160; 
 class=&quot; lbl_grupo_etario_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_grupo_etario_desc ) 
&#160; 
 Corresponde a los grupos poblacionales que son atendidos por las organizaciones sociales a las que se les entreg por lo menos un anuncio de donacin en la ciudad respectiva para el periodo seleccionado 
&#160; 
 Se puede obtener, consultando los cdigos de las organizaciones beneficiadas para la ciudad en particular&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= delivered , received,pre-certified,certified&amp;eatc-city=&#123;&#123;CIUDAD&#125;&#125; &amp;_distinct= eatc-donation_manager_code = &#123;&#123;array_ids&#125;&#125; 
&#160; 
 &#160;luego con los cdigos obtenidos se realiza una bsqueda de los grupos etarios que atienden dichas organizaciones, el maestro de beneficiarios.&#160;Se coloca el conjunto de grupos etarios que abarque los grupos etarios atendidos por las organizaciones buscadas 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro= &#123;&#123;array_ids&#125;&#125; &amp;_distinct=tipo_poblacion_beneficiaria 

&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot;, ciudad&#58; Medelln 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor=exito&amp;&amp;eatc-state=delivered,received,pre-certified,certified&amp;eatc-city=Medelln&amp;_distinct=eatc-donation_manager_code = 901221249_001,901096189-3,811018073,900639899,900870717,860056930-6 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=901221249_001,901096189-3,811018073,900639899,900870717,860056930-6&amp;_distinct=tipo_poblacion_beneficiaria 
&#160; 
 Por lo tanto se muestra como poblacin beneficiaria&#58;&#160; 

&#160; 
 Nmero de organizaciones beneficiadas (en el diseo&#58; fundaciones beneficiadas) 
 class=&quot; lbl_organizaciones_beneficiadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_organizaciones_beneficiadas ) 
&#160; 
 class=&quot; lbl_organizaciones_beneficiadas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_organizaciones_beneficiadas_desc ) 
&#160; 
 Corresponde a la cantidad de organizaciones sociales que se le han despachado por lo menos una donacin en el periodo en cuestin para la ciudad determinada 
&#160; 
 cont de &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= received,pre-certified,certified&amp; eatc-city =&#123;&#123;CIUDAD&#125;&#125; &amp;_distinct= eatc-donation_manager_code 
&#160; 
 Tabla de informacin por ciudad&#58; ordenamiento 
 La tabla debe permitir ordenar ascendente y descendentemente por todas sus columnas. 
&#160; 
 Tabla de informacin por ciudad&#58; paginacin 
 La tabla debe mostrarse de manera paginada (de 7 en 7 resultados) 
&#160; 
 Tabla de informacin por ciudad&#58; Filtros 
 Se proponen los siguientes filtros, los cuales deben irse implementando de manera paulatina 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-impacto-social%2F430422939-sostenibilidad_imp_social.jpg&ow=691&oh=802, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-impacto-social%2F430422939-sostenibilidad_imp_social.jpg&ow=691&oh=802 
 Cuentas datagov 

 399.000000000000 

 DATA ANALYTICS: SOSTENIBILIDAD > TABLERO > IMPACTO SOCIAL