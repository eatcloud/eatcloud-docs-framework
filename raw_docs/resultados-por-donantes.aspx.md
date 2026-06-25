# resultados-por-donantes.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Resultados por donantes 
 Label&#58; class=&quot; lbl_resultados_por_donantes &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_por_donantes )&#160; 

 F RANJA SUPERIOR DE NAVEGACIN Y FILTRO DE FECHAS 
 Aunque no est en el diseo, se debe preservar el&#160; filtro de fechas junto con la franja de navegacin superio r, tal como se document en la &quot;Resultados de donaciones&quot; 

 F ILTRO PRINCIPAL DEL INFORME 
 Filtro por donante&#58; Donante&#160; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 

&#160; 
 Label&#58; class=&quot; lbl_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donante )&#160;&#160; 
&#160; 
 El&#160; los selectores del filtro se arman de acuerdo a los donantes que realizaron donaciones en el periodo seleccionado de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_distinct= eatc_donor_fiscal_name 
&#160; 
 Al seleccionar un eatc_dona_headers. eatc_donor_fiscal_name se debe tomar el respectivo identificador del donante ( eatc_dona_headers. eatc-donor_code ) para realizar consultas subsecuentes. 
&#160; 
 Botn consultar&#58; 
 Label&#58; class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar )&#160; 

 KPIS PRINCIPALES 

 Nota para el desarrollo&#58; algunos de los indicadores se han implementado en la funcionalidad &quot; LISTADO DE GESTORES DE DONACIONES &quot; (quizs sin tener en cuenta el filtro por &quot;Banco de alimentos&quot;, pero si por institucin individual) y tambin son similares a los implementados en el informe Resultados de donaciones &gt; Donaciones , por lo tanto, se deben revisar dichas implementaciones previas para reciclar el cdigo correspondiente. 
 De acuerdo al filtro de fechas aplicado , y al filtro de &quot; Tipo de institucin beneficiaria &quot; el sistema construye los siguientes indicadores&#58; 

&#160; 
 ***NUEVO&#58; Nmero de donaciones recibidas *** 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_num_donaciones_recibidas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_num_donaciones_recibidas &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_num_donaciones_recibidas_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_num_donaciones_recibidas_desc 
&#160; 
 &quot; Corresponde al nmero de donaciones efectivamente recibidas (con estado &quot;recibido&quot;, &quot;pre-certificado&quot; &quot;certificado&quot;) el el periodo en cuestin &quot; 
&#160; 
 Llamado obtener el valor&#58;&#160; 
 El sistema debe realizar el siguiente llamado (tomando en cuenta las fechas seleccionadas en el filtro respectivo y el donante seleccionado)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor = &#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state=received,pre-certified,certified&amp;_cont 

&#160; 
 Ejemplo&#58; ambiente productivo, cua_user&#58; exito, 10 al 12 de mayo de 2023 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2023-05-10&amp;eatc-publication_date[1]=2023-05-12&amp;eatc-donor = exito&amp;eatc-state=received,pre-certified,certified&amp;_cont &#160;&#160;&#160; 
&#160; 
 El indicador muestra el valor &quot; 300 &quot; 

&#160; 
 KG anunciados 
&#160; 
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
 Llamado para el clculo&#58;&#160; 
 El sistema debe realizar el siguiente llamado (tomando en cuenta las fechas seleccionadas en el filtro respectivo y el donante seleccionado)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;_cmp= e atc-original_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. 

&#160; 
 KG despachados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A todos los usuarios 
&#160; 
 class=&quot; lbl_kg_despachados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_despachados &#160; &#160; 
&#160; 
 Tooltip (corresponde a la misma informacin del tooltip que se informa abajo)&#58; =&gt; REVISAR 
 class=&quot; lbl_kg_recibidos_antes_verificacion_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion_desc &#160; &#160; 
&#160; 
 &quot; Sumatoria de los kilogramos originalmente anunciados de todos los anuncios de donacin con estado &quot;despachado&quot; &quot; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-state=delivered &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= e atc-original_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. El resultado se lleva a la variable &#123;&#123;kg_despachados&#125;&#125; para futuros clculos 

&#160; 
 KG aprovechados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A todos los usuarios 
&#160; 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados_desc &#160; 
&#160; 
 &quot; KG que han sido efectivamente recibidos por los beneficiarios &quot; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-state= received,pre-certified,certified &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= e atc- total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; El resultado se lleva a la variable &#123;&#123;kg_totales_aprovechados&#125;&#125; para futuros clculos 

&#160; 
 % KG despachados =&gt; REVISAR 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A todos los usuarios 
&#160; 
 class=&quot; lbl_pct_kg_despachados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_pct_kg_despachados 
&#160; 
 Tooltip (Y este tiene que ver con la divisin de los Kilogramos que se despacharon, divididos, los kilogramos anunciados.) &#58; 
 class=&quot; lbl_pct_kg_despachados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_pct_kg_despachados_desc&#160; 
&#160; 
 &quot; Corresponde a la divisin entre la sumatoria de los KG despachados por el donante, y la sumatoria de los kilogramos originales (Kg que el donante anunci originalmente) reportados por el donante &quot; 
&#160; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_despachados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125; &amp; eatc-state= received,pre-certified,certified&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= e atc- original_weight_kg 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123; pct_KG_despachados &#125;&#125; = ( &#123;&#123;kg_despachados&#125;&#125; / &#123;&#123;kg_totales_anunciados&#125;&#125; ) * 100 

&#160; 
 % KG aprovechados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A todos los usuarios 
&#160; 
 class=&quot; lbl_pct_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_kg_aprovechados &#160; 
&#160; 
 Tooltip (es el mismo que le aplica a porcentaje de aprovechamiento, simplemente en este punto quieren ese nombre para el indicador)&#58; 
 class=&quot; lbl_pct_aprovechamiento_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento_desc &#160; 
&#160; 
 &quot; Corresponde a la divisin entre la sumatoria de los KG efectivamente recibidos por los gestores de donacin (instituciones beneficiarias) despus de proceso de verificacin de la donacin en el periodo seleccionado, y la sumatoria de los kilogramos originales (Kg netos que el donante anunci) de los anuncios efectivamente recibidos por las instituciones beneficiarias.&quot; &quot; 
&#160; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125; &amp; eatc-state= received,pre-certified,certified&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= e atc- original_weight_kg 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123; pct_aprovechamiento &#125;&#125; = ( &#123;&#123;kg_totales_aprovechados&#125;&#125; / &#123;&#123;kg_totales_anunciados&#125;&#125; ) * 100 

&#160; 
 % efectividad de donaciones &#160; =&gt; REVISAR 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_pct_efectividad_donaciones &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_pct_efectividad_donaciones 
&#160; 
 Tooltip ( Juancho este indicador es el mismo de %aprovechados, pero no teniendo en cuenta los kilogramos, si no el # de donaciones completadas con exito/ # donaciones anunciadas )&#58; 
 class=&quot; lbl_pct_efectividad_donaciones_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_pct_efectividad_donaciones_desc&#160; 
&#160; 
 &quot; Corresponde a la divisin entre el nmero de anuncios despachados (o ser recibidos efectivamente por los beneficiarios) por el donante y el nmero de anuncios que el donante anunci en el periodo seleccionado&quot; 
&#160; 
 Para obtener el numerador, el sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125; &amp; eatc-state=delivered, received,pre-certified,certified &amp;_cont 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125; &amp; _cont 

 Bancos de alimentos que recibieron donaciones del donante (en el diseo&#58; &quot;Bancos de alimentos que recibieron donaciones) 
 class=&quot; lbl_b_de_a_recibieron_dona &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_b_de_a_recibieron_dona 

 El sistema debe colocar en un grfico de barras horizontales (ordenado ascendentemente por KG aprovechados), para cada banco de donacin&#58;&#160; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? tipo_organizacion= BdeA &amp;_cmp= organizacin,identificador_unico_registro 
&#160; 
 al cual le don el donante, la siguiente informacin. 

&#160; 
 KG aprovechados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A todos los usuarios 
&#160; 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc-state= received,pre-certified,certified &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= e atc- total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; 

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
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donor_code = &#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

 TABLA&#58; D ONACIONES POR BANCO DE ALIMENTOS (EN EL DISEO&#58; DONANTES QUE DONARON A BANCO DE ALIMENTO) 
 ***NUEVO &#58; Filtro (a quienes se le muestrala tabla)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 Label&#58; class=&quot; lbl_dona_por_b_de_a &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_dona_por_b_de_a)&#160; 
&#160; 
 La tabla debe permitir ordenar por cada columna (descendente y ascendentemente).&#160; El ordenamiento por defecto debe ser por la columna KG aprovechados descendente (mostrando primero los donantes ms KG aprovechados).&#160; Adems debe poder filtrar por diversos criterios (datatable).&#160; Adicionalmente deber permitir descargar la informacin en formato CSV a nivel de encabezado (presente tabla). 

 NIT Donante 
 class=&quot; lbl_id_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_id_donante &#160; 
&#160; 
 Corresponde a&#160; 
 eatc_dona_headers. eatc-donor_code 
&#160; 
 De acuerdo a la seleccin del filtro principal del informe 
&#160; 
 Donante 
 class=&quot; lbl_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donante &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Corresponde a&#160; 
 eatc_dona_headers. eatc-donor_fiscal_name 
&#160; 
 De acuerdo a la seleccin del filtro principal del informe 

&#160; 
 Banco de alimentos 
 class=&quot; lbl_banco_de_alimentos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_banco_de_alimentos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para construir los registros de cada fila&#58; 
&#160; 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) y banco de alimentos (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;_distinct= eatc-donation_manager_name 
&#160; 
 Para colocar el nombre del Banco de alimentos. 

&#160; 
 Nmero de anuncios 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios 
&#160; 
 Llamado para el clculo&#58; 
&#160; 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) y banco de alimentos (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

&#160; 
 KG aprovechados 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el clculo&#58; 
&#160; 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) y banco de alimentos (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-state= received &amp;_cmp= total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; 

&#160; 
 Ver detalles (en el diseo &quot;Ver detalle&quot;) 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) y banco de alimentos (eatc_dona_headers. eatc-donation_manager_code ) el sistema debe presentar el vnculo 
&#160; 
 class=&quot; lbl_ver_detalles &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ver_detalle &#160; 
&#160; 
 Al hacer clic se desplegar una tabla de detalles 
&#160; 
 Tabla de detalles&#58; 
 Tabla paginada que se pueda ordenar por los diferentes campos y que sea descargable en formato Excel. 

 Al hacer clic el sistema deber realizar la siguiente consulta para amar una tabla con los resultados obtenidos&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;_cmp= eatc-code,eatc-publication_date,eatc-publication_datetime,eatc-state,eatc-pod_name,eatc-pod_address,eatc-city,eatc-total_weight_kg,eatc-total_cost 
&#160; 
 Con los datos obtenidos se arma la informacin de la tabla de la siguiente manera&#58; 
&#160; 
 Cdigo del anuncio 
 class=&quot; lbl_codigo_anuncio &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_codigo_anuncio 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-code 

&#160; 
 Fecha 
 class=&quot; lbl_fecha &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_fecha &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-publication_date 

&#160; 
 Hora 
 class=&quot; lbl_hora2 &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_hora2 &#160; &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-publication_datetime 

&#160; 
 Estado del anuncio 
 class=&quot; lbl_estado_anuncio &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_estado_anuncio &#160; &#160;&#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-state 

&#160; 
 Punto de donacin 
 class=&quot; lbl_pod &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pod &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-pod_name 

&#160; 
 Direccin (en el diseo &quot;Direccin del punto de donacin&quot;) 
 class=&quot; lbl_direccion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_direccion &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-pod_address 

&#160; 
 KG donados (Recibidos) 
 class=&quot; lbl_kg_donados_recibidos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_donados_recibidos &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-total_weight_kg 

&#160; 
 Unidades donadas =&gt; En una primera etapa no va. 

&#160; 
 Costo de la donacin 
 class=&quot; lbl_costo_donacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_costo_donacion &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-total_cost 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultados-por-donantes%2F3086890730-resultados_x_donantes2.jpg&ow=780&oh=1120, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultados-por-donantes%2F3086890730-resultados_x_donantes2.jpg&ow=780&oh=1120 
 Nuevo BO CUA MASTER Beneficiarios 

 650.000000000000 

 RESULTADOS DE DONACIONES > RESULTADOS POR DONANTES