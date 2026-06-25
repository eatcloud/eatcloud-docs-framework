# resultado-de-donaciones-donaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Donaciones 

 Label&#58; class=&quot; lbl_donaciones &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donaciones ) 
&#160; 
 Subttulo del informe&#58; Consolidado de donaciones 
 Label&#58; class=&quot; lbl_consolidado_donaciones &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consolidado_donaciones ) 

 F ILTRO PRINCIPAL DEL INFORME 

 Filtro por tipo de instituciones&#58; Tipo de institucin beneficiaria (en el diseo est como &quot;Instituciones beneficiarias&quot;) 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra este filtro)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 

&#160; 
 Label&#58; class=&quot; lbl_tipo_institucion_beneficiaria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_tipo_institucion_beneficiaria )&#160;&#160; 
&#160; 
 El&#160; los selectores del filtro se arman de acuerdo a la tipologa b de las instituciones que se obtiene de la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_doma_typology_b ?_id=_*&amp;_distinct= eatc_name 
&#160; 
 Adicionando la opcin &quot; Todos &quot; (que ser el valor por defecto) 
 Label&#58; class=&quot; lbl_todos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_todos ) 
&#160; 
 Al seleccionar una opcin se debe obtener el &quot; eatc_doma_typology_b. eatc_code &quot; respectivo&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_doma_typology_b ?eatc_name=&#123;&#123; opcion_seleccionada &#125;&#125;&amp;_distinct= eatc_code 
&#160; 
 Para el caso de la opcin &quot; Todos &quot; el parmetro de consulta ser &quot; _* &quot; 
&#160; 
 Botn consultar&#58; 
 Label&#58; class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar )&#160; 

 KPIS PRINCIPALES 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra toda la seccin / grupo de indicadores, incluyendo su ttulo)&#58; *** 
&#160; 
 A los todos los usuarios. 

 Nota para el desarrollo&#58; algunos de los indicadores se han implementado en la funcionalidad &quot; LISTADO DE GESTORES DE DONACIONES &quot; (quizs sin tener en cuenta el filtro por &quot;tipo de institucin beneficiaria, pero si por institucin), por lo tanto, se debe revisar dicha implementacin para reciclar el cdigo correspondiente. 
&#160; 
 De acuerdo al filtro de fechas aplicado , y al filtro de &quot; Tipo de institucin beneficiaria &quot; el sistema construye los siguientes indicadores&#58; 

&#160; 
 KG anunciados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_kg_anunciados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_anunciados 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_anunciados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_anunciados_desc 
&#160; 
 &quot; Sumatoria de los kilogramos originalmente anunciados de todos los anuncios de donacin realizados &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125; 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. 

&#160; 
 KG recibidos antes de verificacin 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_recibidos_antes_verificacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_recibidos_antes_verificacion_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion_desc &#160; &#160; &#160; 
&#160; 
 &quot; Sumatoria de los kilogramos originalmente anunciados de todos los anuncios de donacin con estado &quot;despachado&quot; &quot; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado para los usuarios tipo eatc_cua_master 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-state=delivered &amp;_cmp= eatc-original_weight_kg 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;eatc-state=delivered &amp;_cmp= eatc-original_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. 

&#160; 
 Anuncios realizados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_numero_anuncios_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios_desc 
&#160; 
 &quot; Cantidad de anuncios de donacin generados &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

&#160; 
 KG aprovechados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados_desc &#160; 
&#160; 
 &quot; KG que han sido efectivamente recibidos por los beneficiarios &quot; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-state=received,pre-certified,certified &amp;_cmp= eatc-total_weight_kg 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;eatc-state=received,pre-certified,certified &amp;_cmp= eatc-total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; El resultado se lleva a la variable &#123;&#123;kg_totales_aprovechados&#125;&#125; para futuros clculos 

&#160; 
 % de aprovechamiento 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_pct_aprovechamiento &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pct_aprovechamiento_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento_desc &#160; 
&#160; 
 &quot; Corresponde a la divisin entre la sumatoria de los KG efectivamente recibidos por los gestores de donacin (instituciones beneficiarias) despus de proceso de verificacin de la donacin en el periodo seleccionado, y la sumatoria de los kilogramos originales (Kg netos que el donante anunci) de los anuncios efectivamente recibidos por las instituciones beneficiarias.&quot; &quot; 
&#160; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code&#125;&#125; &amp; eatc-state= received,pre-certified,certified &amp;_cmp=eatc-original_weight_kg&#160; 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp; eatc-state= received,pre-certified,certified &amp;_cmp=eatc-original_weight_kg&#160; 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
&#160; 
 &#123;&#123; pct_aprovechamiento &#125;&#125; = ( &#123;&#123;kg_totales_aprovechados&#125;&#125; / &#123;&#123;kg_totales_anunciados&#125;&#125; ) * 100 

&#160; 
 KG no aprovechados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_no_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_no_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados_desc &#160; &#160; 
&#160; 
 &quot; KG que no fueron recibidos por los beneficiarios &quot; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-state=received,pre-certified,certified &amp;_cmp=eatc-original_weight_kg ,&amp;_cmp=eatc-total_weight_kg&#160; 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;eatc-state=received,pre-certified,certified &amp;_cmp=eatc-original_weight_kg ,&amp;_cmp=eatc-total_weight_kg&#160; 
&#160; 
 El sistema realiza una resta de&#160; la sumatoria de los KG Originales ( eatc_dona_headers. eatc-original_weight_kg )&#160; menos la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; El resultado se lleva a la variable &#123;&#123;kg_no_aprovechados&#125;&#125; para futuros clculos 

 T ORTAS DE DISTRIBUCIN DE DONACIONES 

 Distribucin de KG recibidos 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_distribucion_kg_recibidos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_distribucion_kg_recibidos &#160; 

&#160; 
 En una torta se coloca el &#123;&#123; pct_aprovechamiento &#125;&#125; , Vs lo que le faltara para llegar al 100% (100% - &#123;&#123; pct_aprovechamiento &#125;&#125; ) 
&#160; 
 class=&quot; lbl_pct_aprovechamiento &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento 
&#160; 
 class=&quot; lbl_pct_kg_no_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_kg_no_aprovechados &#160; 

 Distribucin de donaciones 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_distribucion_donaciones &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_distribucion_donaciones &#160; 

 Se saca el indicador &quot; Anuncios Realizados &quot; por cada tipologa, siendo la sumatoria de todos los anuncios (o sea el indicador para el selector &quot;Todos&quot;) el universo, sobre el cual se calcula el peso (porcentaje) del nmero de donaciones entregada a cada tipologa b de institucin beneficiaria (sobre el total). 

 DONACIONES POR CIUDAD (EN EL DISEO &quot;LISTADO DE DONACIONES POR CIUDAD&quot;) 
 ***NUEVO &#58; Filtro (a quienes se le muestra la tabla)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_donaciones_x &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donaciones_x &#160; 
&#160; 
 class=&quot; lbl_ciudad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ciudad 

 Tabla de donaciones por ciudad 
 La tabla debe permitir ordenar por cada columna (descendendente y ascendentemente).&#160; El ordenamiento por defecto debe ser por la columna KG aprovechados descendente (mostrando primero las ciudades con ms KG aprovechados). 

 Llamado para construir las filas (columna&#58; Ciudad)&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 class=&quot; lbl_ciudad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ciudad 

 El sistema debe realizar el siguiente llamado&#160; para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;_distinct= eatc-city 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_distinct= eatc-city 

&#160; 
 Con la respuesta obtenida se colocan los registros en el la columna CiudadKG aprovechados 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado (para cada fila de registros) para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-state= received &amp;eatc-city=&#123;&#123; eatc-city &#125;&#125; &amp;_cmp= eatc-total_weight_kg 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado (para cada fila de registros)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;eatc-state= received &amp;eatc-city=&#123;&#123; eatc-city &#125;&#125; &amp;_cmp= eatc-total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; 

&#160; 
 Nmero de anuncios (en el diseo&#58; &quot;Anuncios&quot;) 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; llamado diferenciado para usuarios tipo eatc_cua_master y el resto de usuarios *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado (para cada fila de registros) para los usuarios tipo eatc_cua_master &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-city=&#123;&#123; eatc-city &#125;&#125;&amp;_cont 
&#160; 
 Para los usuarios tipo_BdeA y tipo_no_BdeA (que no tendrn habilitado el filtro por tipo de organizacin), el sistema realizar el siguiente llamado (para cada fila de registros)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;eatc-city=&#123;&#123; eatc-city &#125;&#125;&amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

 Grfico de donaciones por ciudad 
 No es necesario repetir el mismo ttulo del informe en la grfica .&#160; Es una grfica de barras horizontales, que muestra el TOP 10 de ciudades (tal como se implement en Datagov Cuentas Analytics) por KG aprovechados es decir que no incluye en la grfica (como est en el diseo) los valores del &quot; (Consolidado del 30%) &quot; 

 La grfica debe mostrar los valores (arriba descritos para la lista) de&#58; 
&#160; 

 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados 
&#160; 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios (en el diseo &quot;Anuncios realizados&quot;) 

 DONACIONES POR D EPARTAMENTO (EN EL DISEO &quot;LISTADO DE DONACIONES POR DEPARTAMENTO&quot;) 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra la tabla y los grficos)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_donaciones_x &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donaciones_x &#160; 
&#160; 
 class=&quot; lbl_departamento_provincia_estado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_departamento_provincia_estado 

 Tabla de donaciones por Departamento 
 La tabla debe permitir ordenar por cada columna (descendendente y ascendentemente).&#160; El ordenamiento por defecto debe ser por la columna KG aprovechados descendente (mostrando primero las ciudades con ms KG aprovechados). 

 Llamado para construir las filas (columna&#58; Departamento)&#58; 
 class=&quot; lbl_departamento_provincia_estado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_departamento_provincia_estado 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;_distinct= eatc-province 
&#160; 
 Con la respuesta obtenida se colocan los registros en el la columna &quot; Departamento &quot; 

 KG aprovechados 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el clculo&#58; 
&#160; 
 El sistema debe realizar el siguiente llamado (para cada fila de registros)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp;eatc-state= received &amp; eatc-province =&#123;&#123; eatc-province &#125;&#125; 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; 

&#160; 
 Nmero de anuncios (en el diseo&#58; &quot;Anuncios&quot;) 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios 
&#160; 
 Llamado para el clculo&#58; 
&#160; 
 El sistema debe realizar el siguiente llamado (para cada fila de registros)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_typology_b=&#123;&#123; eatc_doma_typology_b. eatc_code &#125;&#125;&amp; eatc-province =&#123;&#123; eatc-province &#125;&#125;&amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

 Grfico de donaciones por departamento 
 No es necesario repetir el mismo ttulo del informe en la grfica .&#160; Es una grfica de barras horizontales, que muestra el TOP 10 de departamento (tal como se implement en Datagov Cuentas Analytics) por KG aprovechados. 

 La grfica debe mostrar los valores (arriba descritos para la lista) de&#58; 
&#160; 

 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados 
&#160; 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios (en el diseo &quot;Anuncios realizados&quot;) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultado-de-donaciones-donaciones%2F1832686457-donacioneciones_mockup.jpg&ow=777&oh=621, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultado-de-donaciones-donaciones%2F1832686457-donacioneciones_mockup.jpg&ow=777&oh=621 
 Nuevo BO CUA MASTER Beneficiarios 

 635.000000000000 

 RESULTADOS DE DONACIONES > DONACIONES