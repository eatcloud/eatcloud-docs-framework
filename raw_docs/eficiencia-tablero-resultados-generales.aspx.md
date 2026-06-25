# eficiencia-tablero-resultados-generales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Mockup&#58; 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones. 

&#160; 
 Label Ttulo de la Vista&#58; Resultados generales 
 class=&quot; lbl_resultados_generales &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_resultados_generales ) 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 
 El tablero deber incorporar dicha franja de botones 
&#160; 
 KPIs principales 
 El grfico (que en el diseo est como un grfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la lnea principal de cards (ver imagen siguiente). Al ingresar a la vista, se deber mostrar el grfico de tendencia del KPI por defecto . El usuario podr presionar cada una de las cards, para mostrar el grfico de tendencia particular de dicho KPI (A excepcin del caso en donde se ha solicitado estadsticas del da actual, o del da de ayer&#58; en este caso no se genera grfico).&#160; 

 Kilogramos entregados (en el diseo Kg Donados) =&gt; nos podemos basar en la implementacin de &quot; consulta tus resultados &quot;&#58; KPI por defecto 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Corresponde al total de KG entregados, es decir, aquellos KG que fueron efectivamente despachados (se valid el cdigo de entrega) y recibidos por los beneficiarios (se verific el contenido de la donacin) para los anuncios (cuyo estado es &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot;) del periodo en cuestin. 

&#160; 
 Nmero de anuncios realizados (en el diseo Anuncios publicados) =&gt; nos podemos basar en la implementacin de &quot; consulta tus resultados &quot; 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Cantidad de anuncios de donacin generados en el periodo en cuestin. 

&#160; 
 Porcentaje de aprovechamiento en kilogramos =&gt; Se puede basar en la i mplementacin de BO o en la de Antigua WAPP 
 class=&quot; lbl_porcentaje_promedio_kg_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_promedio_kg_aprovechados ) 
&#160; 
 class=&quot; lbl_porcentaje_promedio_kg_aprovechados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_promedio_kg_aprovechados_desc ) 

&#160; 
 Porcentaje de efectividad en KG ***NUEVO*** 
 class=&quot; lbl_porcentaje_efectividad_kg &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_efectividad_kg )&#160; 
&#160; 
 class=&quot; lbl_porcentaje_efectividad_kg _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_efectividad_kg_desc )&#160; 
&#160; 
 &quot;Corresponde a la sumatoria de los KG totales de las donaciones efectivamente recibidas por los beneficiarios sobre la sumatoria de los KG Originales de todos los anuncios en el periodo establecido&quot; 

 Nmero de referencias donadas=&gt; ***NUEVO*** &#58; se pasa como un KPI Secundario 

 KPIs secundarios 
 Con base en los KPIs calculados anteriormente se saca un promedio diario para el periodo consultado y tambin se realizan otros clculos para presentar informacin estadstica 

 Kilogramos entregados por da (en el diseo Kg Donados por da)&#160; 
 class=&quot; lbl_kg_entregados_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_por_dia ) 
&#160; 
 class=&quot; lbl_kg_entregados_por_dia_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_por_dia_desc ) 
&#160; 
 Se dividen los KG entregados (que se calcularon en el KPI Principal respectivo &quot; Kilogramos Entregados &quot;) por el nmero de das que contiene el informe (segn el filtro de fechas aplicado ) 

&#160; 
 Anuncios realizados por da (en el diseo Anuncios publicados por da)&#160; 
 class=&quot; lbl_anuncios_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_por_dia ) 
&#160; 
 class=&quot; lbl_anuncios_por_dia_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_por_dia_desc ) 
&#160; 
 Se divide el nmero de anuncios realizados (que se calcularon en el KPI Principal respectivo &quot; Nmero de anuncios realizados &quot;) por el nmero de das que contiene el informe (segn el filtro de fechas aplicado ). 

&#160; 
 Anuncios realizados por semana (en el diseo Anuncios publicados por semana)&#160; 
 class=&quot; lbl_anuncios_por_semana &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_por_semana ) 
&#160; 
 class=&quot; lbl_anuncios_por_dia_semana_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_por_semana_desc ) 
&#160; 
 Se multiplica el anterior indicador &quot;Anuncios realizados por da&quot; por 7 (para obtener el clculo de lo que se obtendra en una semana) 

&#160; 
 Porcentaje de efectividad en nmero de anuncios ***NUEVO*** 
 class=&quot; lbl_porcentaje_efectividad_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_efectividad_anuncios )&#160;&#160; 
&#160; 
 class=&quot; lbl_porcentaje_efectividad_anuncios _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_efectividad_anuncios_desc )&#160; 
&#160; 
 &quot;Corresponde al nmero de las donaciones efectivamente recibidas por los beneficiarios sobre el nmero total de anuncios de donacin realizados en el periodo establecido&quot; 

&#160; 
 Nmero de referencias donadas=&gt; Se puede basar en la implementacin de BO o en la de Antigua WAPP &#58; =&gt; ***NUEVO*** &#58; se pasa como un KPI Secundario 
 class=&quot; lbl_referencias_donadas &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas ) 
&#160; 
 class=&quot; lbl_referencias_donadas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas_desc ) 
&#160; 
 &quot;Conteo de todas las referencias (tems) que se han donado en el periodo seleccionado&quot; 

&#160; 
 Referencias donadas por da 
 class=&quot; lbl_referencias_donadas_por_dia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas_por_dia ) 
&#160; 
 class=&quot; lbl_referencias_donadas_por_dia_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas_por_dia_desc ) 
&#160; 
 Se debe sacar un promedio del nmero de referencias donadas cada da del periodo seleccionado 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-generales%2F2717863084-eficiencia_tablero_resultados_generales.jpg&ow=580&oh=474, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-generales%2F2717863084-eficiencia_tablero_resultados_generales.jpg&ow=580&oh=474 
 Cuentas datagov 

 363.000000000000 

 DATA ANALYTICS: EFICIENCIA > TABLERO > RESULTADOS GENERALES (INFORME POR DEFECTO)