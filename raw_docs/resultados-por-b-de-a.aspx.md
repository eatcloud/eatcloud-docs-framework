# resultados-por-b-de-a.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Resultados por bancos de alimentos 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestrael informe)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 

 Label&#58; class=&quot; lbl_resultados_b_de_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_b_de_a )&#160; 

 F RANJA SUPERIOR DE NAVEGACIN Y FILTRO DE FECHAS 
 Aunque no est en el diseo, se debe preservar el&#160; filtro de fechas junto con la franja de navegacin superio r, tal como se document en la &quot;Resultados de donaciones&quot; 

 F ILTRO PRINCIPAL DEL INFORME 

 Filtro por&#58; Bancos de alimentos&#58; ***NUEVO&#58; se incorpora tipologa B para depurar el filtro *** 
 Label&#58; class=&quot; lbl_bancos_de_alimentos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_bancos_de_alimentos )&#160; 
&#160; 
 El&#160; los selectores del filtro se arman de acuerdo a los datos que se obtienen en la&#160; siguiente consulta (siendo el valor eatc_donation_managers. organizacin y el valor eatc_donation_managers. identificador_unico_registro el que se guarda como cdigo para las siguientes consultas 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? tipo_organizacion= BdeA &amp;eatc_doma_typology_b=1 &amp;_cmp= organizacin,identificador_unico_registro 
&#160; 
 Adicionando la opcin &quot; Todos &quot; (que ser el valor por defecto) 
&#160; 
 Label&#58; class=&quot; lbl_todos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_todos ) 
&#160; 
 Al seleccionar una opcin se debe obtener el &quot; eatc_donation_managers. identificador_unico_registro &quot; respectivo, para las siguientes consultas 
&#160; 
 Para el caso de la opcin &quot; Todos &quot; el parmetro de consulta ser el array de &quot; eatc_donation_managers. identificador_unico_registro &quot; obtenido. 
&#160; 
 Botn consultar&#58; 
 Label&#58; class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar )&#160; 

 KPIS PRINCIPALES 

 Nota para el desarrollo&#58; algunos de los indicadores se han implementado en la funcionalidad &quot; LISTADO DE GESTORES DE DONACIONES &quot; (quizs sin tener en cuenta el filtro por &quot;Banco de alimentos&quot;, pero si por institucin individual) y tambin son similares a los implementados en el informe Resultados de donaciones &gt; Donaciones , por lo tanto, se deben revisar dichas implementaciones previas para reciclar el cdigo correspondiente. 
&#160; 
 De acuerdo al filtro de fechas aplicado , y al filtro de &quot; Bancos de alimentos &quot; el sistema construye los siguientes indicadores&#58; 

&#160; 
 KG recibidos antes de verificacin 
 class=&quot; lbl_kg_recibidos_antes_verificacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_recibidos_antes_verificacion_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion_desc &#160; &#160; 
&#160; 
 &quot; Sumatoria de los kilogramos originalmente anunciados de todos los anuncios de donacin con estado &quot;despachado&quot; &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc-state=delivered 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. 

&#160; 
 KG aprovechados 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados_desc &#160; 
&#160; 
 &quot; KG que han sido efectivamente recibidos por los beneficiarios &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc-state=received 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; El resultado se lleva a la variable &#123;&#123;kg_totales_aprovechados&#125;&#125; para futuros clculos 

&#160; 
 % de aprovechamiento 
 class=&quot; lbl_pct_aprovechamiento &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pct_aprovechamiento_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento_desc &#160; 
&#160; 
 &quot; Corresponde a la divisin entre la sumatoria de los KG efectivamente recibidos por los gestores de donacin (instituciones beneficiarias) despus de proceso de verificacin de la donacin en el periodo seleccionado, y la sumatoria de los kilogramos originales (Kg netos que el donante anunci) de los anuncios efectivamente recibidos por las instituciones beneficiarias.&quot; &quot; 
&#160; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125; &amp; eatc-state= received,pre-certified,certified 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123; pct_aprovechamiento &#125;&#125; = ( &#123;&#123;kg_totales_aprovechados&#125;&#125; / &#123;&#123;kg_totales_anunciados&#125;&#125; ) * 100 

&#160; 
 KG no aprovechados 
 class=&quot; lbl_kg_no_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_no_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados_desc &#160; 
&#160; 
 &quot; KG que no fueron recibidos por los beneficiarios &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc-state= received 
&#160; 
 El sistema realiza una resta de&#160; la sumatoria de los KG Originales ( eatc_dona_headers. eatc-original_weight_kg )&#160; menos la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; El resultado se lleva a la variable &#123;&#123;kg_no_aprovechados&#125;&#125; para futuros clculos 

 G RFICO DE BARRAS HORIZONTALES DE KG RECIBIDOS ANTES DE VERIFICACIN 

 Con los resultados de todos los bancos del siguiente indicador, se arma un grfico de barras horizontales (que pueda ser ordenado ascendente o descendentemente, ordenado por defecto en orden ascendente por KG recibidos antes de verificacin). 
&#160; 
 KG recibidos antes de verificacin 
 class=&quot; lbl_kg_recibidos_antes_verificacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion &#160; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc-state=delivered 
&#160; 
 El sistema realiza la sumatoria de los KG_originales ( eatc_dona_headers. eatc-original_weight_kg ) obtenidos. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultados-por-b-de-a%2F1028245597-resultados_x_BdeA2.jpg&ow=974&oh=876, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresultados-por-b-de-a%2F1028245597-resultados_x_BdeA2.jpg&ow=974&oh=876 
 Nuevo BO CUA MASTER Beneficiarios 

 646.000000000000 

 RESULTADOS DE DONACIONES > RESULTADOS POR BANCOS DE ALIMENTOS