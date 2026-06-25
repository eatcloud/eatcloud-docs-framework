# eficiencia-tablero-resultados-avanzados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementacin&#58;&#160; 
 en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 
&#160; 
 Mockup&#58; 

 Eficiencia &gt; Tableros &gt; Franja de navegacin superior 
&#160; 
 El tablero deber incorporar dicha franja de botones 

&#160; 
 Label Ttulo de la Vista&#58; Resultados avanzados 
 class=&quot; lbl_resutados_avanzados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_resutados_avanzados ) 

 RESULTADOS Y EFICIENCIA SEGN TIPOLOGA A 
 Se mostrarn en una franja horizontal en primer lugar, los resultados por la tipologa a ( class=&quot; lbl_eatc_pods_typolgy_a &quot; ) de los puntos de donacin de la cuenta respectiva 

RESULTADOS SEGN TIPOLOGA A DE PUNTOS DE DONACIN 

 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
 class=&quot; lbl_resultados_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_resultados_segun ) 
&#160; 
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
 Estos indicadores son los mismos que se implementaron en Eficiencia &gt; Tablero &gt; Resultados generales , y por lo tanto se podr basar la implementacin en esa implementacin previa. 
&#160; 
 Kilogramos entregados (en el diseo Kg Donados)&#160; =&gt; KPI por defecto 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Nmero de anuncios realizados 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Porcentaje de aprovechamiento en kilogramos promedio 
 class=&quot; lbl_porcentaje_promedio_kg_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_promedio_kg_aprovechados ) 
&#160; 
 class=&quot; lbl_porcentaje_promedio_kg_aprovechados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_porcentaje_promedio_kg_aprovechados_desc ) 
&#160; 
 Nmero de referencias donadas 
 class=&quot; lbl_referencias_donadas &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas ) 
&#160; 
 class=&quot; lbl_referencias_donadas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_referencias_donadas_desc ) 

EFICIENCIA SEGN TIPOLOGA A DE PUNTOS DE DONACIN 

 La implementacin tiene la misma dinmica de la anteriormente documentada (selector de KPIs, Grfico de Barras por Tipologa A), por lo tanto solo haremos referencia la aquello que vara con respecto a la anterior implementacin 
&#160; 
 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
&#160; 
 class=&quot; lbl_eficiencia_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eficiencia_segun ) 
&#160; 
 Seguido de&#160; 
&#160; 
 class=&quot; lbl_eatc_pods_typolgy_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_a ) 
 (valor por defecto&#58; &quot; tipologa a de puntos de donacin &quot; 

 Indicadores de Eficiencia 
 Estos indicadores son los mismos que se implementaron en Eficiencia &gt; Tablero &gt; Rendimiento , y por lo tanto se podr basar la implementacin en esa implementacin previa. 
&#160; 
 % Anuncios entregados&#160; =&gt; Indicador por defecto 
 class=&quot; lbl_pct_anuncios_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados ) 
&#160; 
 class=&quot; lbl_pct_anuncios_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados_desc ) 
&#160; 
 Corresponde a la divisin del nmero de anuncios efectivamente recibidos por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. 

&#160; 
 % Kilogramos entregados 
 class=&quot; lbl_pct_kilogramos_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_kilogramos_entregados ) 
&#160; 
 class=&quot; lbl_pct_kilogramos_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_kilogramos_entregados_desc ) 
&#160; 
 Corresponde a la divisin del total de kilogramos de los anuncios efectivamente recibidos ( eatc-total_weight_kg ) por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;),&#160; sobre el peso original ( original_weight_kg ) de los anuncios (todos los anuncios) generados en el periodo. 

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
&#160; 
 Corresponde a el promedio&#160; del tiempo de recogida (medido en horas y minutos) de los anuncios despachados en el periodo, el cual se calcula (para cada anuncio despachado) restndole a la fecha y hora de llegada del beneficiario al punto de donacin,&#160; la fecha y hora de adjudicacin del anuncio. *** (Nota&#58; se puede tomar del KPI&#58;&#160; tiempo_de_total_para_la_recogida ) *** 

&#160; 
 Porcentaje de anuncios cancelados ( en nmero de anuncios ) 
 class=&quot; lbl_pct_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_cancelados ) 
&#160; 
 class=&quot; lbl_pct_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_cancelados_desc ) 
&#160; 
 Corresponde a la divisin del nmero de anuncios efectivamente cancelados (es decir, con estado &quot;cancelado&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo. 

 RESULTADOS Y EFICIENCIA SEGN TIPOLOGA B 
 Se mostrarn en una franja horizontal en segundo lugar, los resultados por la tipologa b ( class=&quot; lbl_eatc_pods_typolgy_b &quot; ) de los puntos de donacin de la cuenta respectiva 

 La dinmica de presentacin es similar a la de los resultados y eficiencia por tipologa A, variando simplemente los ttulos y el criterio de agrupacin de la estadstica de barras.&#160; Los indicadores de eficiencia y resultados sern los mismos que los arriba documentados 

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

 EFICIENCIA SEGN TIPOLOGA B DE PUNTOS DE DONACIN 

 La implementacin tiene la misma dinmica de la anteriormente documentada (selector de KPIs, Grfico de Barras por Tipologa A), por lo tanto solo haremos referencia la aquello que vara con respecto a la anterior implementacin 
&#160; 
 Ttulo de la seccin 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
&#160; 
 class=&quot; lbl_eficiencia_segun &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eficiencia_segun ) 
&#160; 
 Seguido de&#160; 
&#160; 
 class=&quot; lbl_eatc_pods_typolgy_b &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_eatc_pods_typolgy_b ) 
 (valor por defecto&#58; &quot; tipologa b de puntos de donacin &quot; 

 D ONACIONES POR CIUDAD 
 En un grfico de torta (o circular) se debe mostrar el nmero de anuncios por ciudad para la cuenta en cuestin, presentando un listado accesorio, con datos que completen la informacin del grfico (sobre todo para donantes con muchas ciudades y dnde algunas de ellas tienen resultados poco significativos en el total).&#160; 

 Aquel grupo de ciudades que pesen en conjunto menos del 7% del total, se debern agrupar en la torta como &quot;otras ciudades, tal como se ejemplifica en el siguiente grfico (para el caso de pases) 

 Ttulo de la seccin&#58; Donaciones por ciudad 
 El ttulo de esta seccin lo componen la concatenacin de los siguientes labels 
 class=&quot; lbl_donaciones_por_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_donaciones_por_ciudad ) 
&#160; 
 Tabla de informacin por ciudad&#58; 
 La tabla contendr la siguiente informacin. 
&#160; 
 Ciudad 
 class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_ciudad ) 
 Muestra la ciudad sobre la cual se presentan estadsticas&#160; 
&#160; 
 Kilogramos entregados (en el diseo Kg Donados) 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Corresponde a la sumatoria del total de kilogramos de los anuncios efectivamente recibidos ( eatc-total_weight_kg ) por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;) para el periodo en cuestin en la ciudad determinada. 
&#160; 
 Nmero de anuncios realizados (en el diseo Anuncios publicados) 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Corresponde al nmero de anuncios realizados por el donante (la cuenta) en el periodo en cuestin en la ciudad determinada. 
&#160; 
 % Anuncios entregados 
 class=&quot; lbl_pct_anuncios_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados ) 
&#160; 
 class=&quot; lbl_pct_anuncios_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pct_anuncios_entregados_desc ) 
&#160; 
 Corresponde a la divisin del nmero de anuncios efectivamente recibidos por los beneficiarios (es decir, con estados &quot;recibidos (received)&quot;, &quot;pre-certificados (pre-certified)&quot; y &quot;certificados (certified)&quot;) sobre el nmero total de anuncios (todos los anuncios) generados en el periodo para la ciudad en cuestin. 
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

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-avanzados%2F1699989434-eficiencia_tablero_resultados_avanzados.jpg&ow=701&oh=764, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Feficiencia-tablero-resultados-avanzados%2F1699989434-eficiencia_tablero_resultados_avanzados.jpg&ow=701&oh=764 
 Cuentas datagov 

 371.000000000000 

 DATA ANALYTICS: EFICIENCIA > TABLERO > RESULTADOS AVANZADOS