# sostenibilidad-tablero-impacto-ambiental.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Se puede basar en la implementacin&#58;&#160; 
 Eficiencia &gt; Tablero &gt; Rendimiento ( Franja de KPIs principales y su respectivo grfico ) y 
&#160; 
 Eficiencia &gt; Tablero &gt; Resultados avanzados ( Resultados por tipologas a y b de puntos de donacin ) 

&#160; 
 Mockup&#58; 

 Sostenibilidad&#160; &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Impacto ambiental 
 class=&quot; lbl_impacto_ambiental &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_impacto_ambiental ) 

 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto . El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer&#58; en este caso no se genera grfico).&#160; 

 Indicadores de impacto ambiental 
 Nmero de anuncios entregados =&gt; KPI por defecto 
 class=&quot; lbl_numero_anuncios_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_entregados ) 
&#160; 
 class=&quot; lbl_numero_anuncios_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_entregados_desc ) 
&#160; 
 Cantidad de anuncios de donacin cuyos estados son &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot; (aquellos que poseen cdigo de recogida validado y verificacin detallada del anuncio por parte de los beneficiarios) en el periodo seleccionado. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicio_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_fin_periodo&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= received,pre-certified,certified &amp;_cont 
&#160; 
 Ejemplo&#58; entorno productivo del da 7 al 8 de junio de 2021 para la cuenta &quot;exito&quot; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-06_07&amp;eatc-publication_date[1]=2021-06_08&amp;eatc-donor= exito &amp;eatc-state= received,pre-certified,certified &amp;_cont = 111 

&#160; 
 KG de CO2 ahorrados (en el diseo&#58; Emisiones de CO2&#160; (Ton)) =&gt; Se puede basar en la implementacin de BO o en la de Antigua WAPP 
 class=&quot; lbl_kg_CO2_ahorrados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_desc ) 
&#160; 
 Corresponde a la cantidad de KG de CO2 que le ests ahorrando al planeta por tu decisin de donar en vez de botar, en el periodo establecido (para anuncios cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;).&#160; 
&#160; 
 Nota para el desarrollo&#58; Se puede obtener del KPI &quot; CO2_tons &quot; (multiplicndolo por 1000). 

&#160; 
 KG de CO2 ahorrados&#160; por da (en el diseo&#58; Emisiones de CO2 por da (Ton)) =&gt; Se basa en la implementacin del anterior KPI 
 class=&quot; lbl_kg_CO2_ahorrados_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_dia ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados_por_dia _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_dia_desc ) 
&#160; 
 Corresponde a la cantidad de KG de CO2 que le ests ahorrando&#160; en promedio al da al planeta, por tu decisin de donar en vez de botar, en el periodo establecido (para anuncios cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;).&#160;&#160; 
&#160; 
 Nota para el desarrollo&#58; Se obtiene dividiendo el anterior KPI (KG de CO2 ahorrados en el periodo) sobre el nmero de das del periodo.&#160;&#160; 
&#160; 
 Nota para el grfico de tendencia&#58; En vez de mostrar otra grfica de tendencia, al seleccionar este KPI se puede mostrar la lnea de promedio sobre la grfica de tendencia de los KG de CO2 ahorrados. 

&#160; 
 KG de CO2 ahorrados&#160; por anuncio (en el diseo&#58; Emisiones de CO2&#160; por anuncio entregado (Ton))&#160; 
 class=&quot; lbl_kg_CO2_ahorrados_por_anuncio &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_anuncio ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados_por_anuncio _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_anuncio_desc ) 
&#160; 
 Corresponde a la cantidad de KG de CO2 que le ests ahorrando&#160; en promedio por cada anuncio de donacin efectivamente entregado&#160; (es decir anuncios cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;) al planeta, en el periodo establecido.&#160; 
&#160; 
 Nota para el desarrollo&#58; Se obtiene dividiendo el anterior KPI (KG de CO2 ahorrados en el periodo) sobre el nmero de anuncios del periodo. 

 R ESULTADOS SEGN TIPOLOGA A 
 Se mostrarn, los resultados por la tipologa a ( class=&quot; lbl_eatc_pods_typolgy_a &quot; ) de los puntos de donacin de la cuenta respectiva 

 RESULTADOS SEGN TIPOLOGA A DE PUNTOS DE DONACIN 

 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
 class=&quot; lbl_resultados_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_resultados_segun ) 
 Seguido de&#160; 
 class=&quot; lbl_eatc_pods_typolgy_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_a ) 
 (valor por defecto&#58; &quot; tipologa a de puntos de donacin &quot; 

 Selector de KPI 
 La interfaz presentar un selector de KPIs de resultados, que permitir al usuario elegir uno (entre los que a continuacin se relacionan) y poder visualizar el grfico de barras, con los datos del indicador seleccionado para cada una de las tipologas a de puntos de donacin de la cuenta en particular en el periodo seleccionado .&#160; El label del indicador, estar acompaado tambin de un tooltip que desplegar la descripcin del mismo ( _desc ).&#160; 
&#160; 
 Existir un KPI por defecto , que ser el que se muestre cuando, se abra el informe y que ms adelante se especifica. Cuando se cambia a otro indicador, el grfico de tendencia variar segn la seleccin.&#160; 

 Grfico de barras por tipologa a de puntos de donacin 
 En las barras se podr observar el indicador para cada uno de las tipologas a de los puntos de donacin que la cuenta tiene registradas, para el periodo seleccionado. 
&#160; 
 A continuacin se presentarn los indicadores o KPIs de resultados que se desplegarn en el selector (y por ende, al presionarlo, en las grficas de barras) 

 Indicadores de resultados 
 Estos indicadores son los mismos que se implementaron en Sostenibilidad &gt; Tablero &gt; Impacto Ambiental &gt; Indicadores de impacto ambiental (arriba descritos) , y por lo tanto se podr basar la implementacin en ello. 
&#160; 
 Anuncios entregados =&gt; KPI por defecto 
 class=&quot; lbl_numero_anuncios_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_entregados ) 
&#160; 
 class=&quot; lbl_numero_anuncios_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_entregados_desc ) 

&#160; 
 KG de CO2 ahorrados 
 class=&quot; lbl_kg_CO2_ahorrados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_desc ) 

&#160; 
 KG de CO2 ahorrados&#160; por da 
 class=&quot; lbl_kg_CO2_ahorrados_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_dia ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados_por_dia _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_dia_desc ) 

&#160; 
 KG de CO2 ahorrados&#160; por anuncio 
 class=&quot; lbl_kg_CO2_ahorrados_por_anuncio &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_anuncio ) 
&#160; 
 class=&quot; lbl_kg_CO2_ahorrados_por_anuncio _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_CO2_ahorrados_por_anuncio_desc ) 

 R ESULTADOS SEGN TIPOLOGA B 
 Se mostrarn en una franja horizontal en segundo lugar, los resultados por la tipologa b ( class=&quot; lbl_eatc_pods_typolgy_b &quot; ) de los puntos de donacin de la cuenta respectiva 

 La dinmica de presentacin es similar a la de los Resultados por tipologa A (arriba descrita) , variando simplemente los ttulos y el criterio de agrupacin de la estadstica de barras (que en este caso ser la tipologa B de los puntos de donacin).&#160; Los indicadores de resultados sern los mismos que los arriba documentados. 

 R ESULTADOS SEGN TIPOLOGA B DE PUNTOS DE DONACIN 

 La implementacin tiene la misma dinmica de la anteriormente documentada (selector de KPIs, Grfico de Barras por Tipologa A), por lo tanto solo haremos referencia la aquello que vara con respecto a la anterior implementacin 
&#160; 
 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
&#160; 
 class=&quot; lbl_resultados_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_resultados_segun ) 
&#160; 
 Seguido de&#160; 
&#160; 
 class=&quot; lbl_eatc_pods_typolgy_b &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_b ) 
 (valor por defecto&#58; &quot; tipologa b de puntos de donacin &quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 Cuentas datagov 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-impacto-ambiental%2F300280782-sostenibilidad_Imp_ambiental.jpg&ow=668&oh=633, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-tablero-impacto-ambiental%2F300280782-sostenibilidad_Imp_ambiental.jpg&ow=668&oh=633 

 392.000000000000 

 DATA ANALYTICS: SOSTENIBILIDAD > TABLERO > IMPACTO AMBIENTAL