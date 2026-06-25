# sostenibilidad-por-b-de-a.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Resultados por bancos de alimentos 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe, incluyendo todos los indicadores)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 

 Label&#58; class=&quot; lbl_resultados_b_de_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_b_de_a )&#160; 

 F RANJA SUPERIOR DE NAVEGACIN Y FILTRO DE FECHAS 
 Aunque no est en el diseo, se debe preservar el&#160; filtro de fechas junto con la franja de navegacin superio r, tal como se document en &quot;Sostenibilidad&quot; 

 F ILTRO PRINCIPAL DEL INFORME 
&#160; 
 Filtro por&#58; Bancos de alimentos ***NUEVO&#58; se incorpora tipologa B para depurar el filtro *** 
 Label&#58; class=&quot; lbl_bancos_de_alimentos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_bancos_de_alimentos )&#160; 
&#160; 
 El&#160; los selectores del filtro se arman de acuerdo a los datos que se obtienen en la&#160; siguiente consulta (siendo el valor eatc_donation_managers. organizacin y el valor eatc_donation_managers. identificador_unico_registro el que se guarda como cdigo para las siguientes consultas 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? tipo_organizacion= BdeA &amp;eatc_doma_typology_b=1 &amp;_cmp= organizacin,identificador_unico_registro 
&#160; 
 Adicionando la opcin &quot; Todos &quot; (que ser el valor por defecto) 
 Label&#58; class=&quot; lbl_todos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_todos ) 
&#160; 
 Al seleccionar una opcin se debe obtener el &quot; eatc_donation_managers. identificador_unico_registro &quot; respectivo, para las siguientes consultas 
&#160; 
 Para el caso de la opcin &quot; Todos &quot; el parmetro de consulta ser el array de &quot; eatc_donation_managers. identificador_unico_registro &quot; obtenido. 
&#160; 
 Botn consultar&#58; 
 Label&#58; class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar ) 

 KPIS PRINCIPALES 

 Ahorros de donantes ($) 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_ahorros_donantes_bdea_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes_bdea_desc &#160; 
&#160; 
 &quot; Sumatoria de los ahorros generados a los donantes en el periodo seleccionado con las donaciones entregadas a los bancos (o al banco de alimentos) &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-kpi_type= Economic%20impact &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Huella de carbono mitigada (TONS CO2) 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_huella_carbono_mitigada_bdea_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada_bdea_desc &#160; 
&#160; 
 &quot; Corresponde a las emisiones de CO2 mitigadas por los donantes en el periodo seleccionado, con las donaciones entregadas a los bancos (o al banco de alimentos) &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-kpi= CO2_tons &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Raciones entregadas 
 class=&quot; lbl_raciones_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_raciones_entregadas_bdea_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas_bdea_desc &#160; 
&#160; 
 &quot; Nmero de platos de comida entregados a poblacin final beneficiaria por parte de los bancos de alimentos (o el banco de alimentos) en el periodo seleccionado &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-kpi= total_portions &amp;_cmp= value 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 
&#160; 

 G RFICO DE BARRAS HORIZONTALES DE AHORROS DE DONANTES ($) 

 Con los resultados de todos los bancos del siguiente indicador, se arma un grfico de barras horizontales (que pueda ser ordenado ascendente o descendentemente, ordenado por defecto en orden ascendente por Ahorros de donantes). 
&#160; 
 Ahorros de donantes ($) 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ahorros_donantes 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-kpi_type= Economic%20impact &amp;_cmp= value 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 
&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-b-de-a%2F2318853778-Sostenibilidad_resultados_por_BdeA.jpg&ow=1160&oh=1046, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-b-de-a%2F2318853778-Sostenibilidad_resultados_por_BdeA.jpg&ow=1160&oh=1046 
 Nuevo BO CUA MASTER Beneficiarios 

 678.000000000000 

 SOSTENIBILIDAD > RESULTADOS POR BANCOS DE ALIMENTOS