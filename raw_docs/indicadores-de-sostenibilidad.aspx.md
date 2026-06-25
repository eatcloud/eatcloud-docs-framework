# indicadores-de-sostenibilidad.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Indicadores de sostenibilidad 
 Label&#58; class=&quot; lbl_indicadores_sostenbilidad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_indicadores_sostenbilidad )&#160; 

 F ILTRO PRINCIPAL DEL INFORME&#58; 

 &#160;Filtro por donante&#58; Donante 
 Label&#58; class=&quot; lbl_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donante )&#160;&#160; 
&#160; 
 Opcin &quot;Todos&quot;&#58; valor del selector por defecto&#58; 
&#160; 
 Trae todos los datos del periodo para el respectivo KPI.&#160; Esta opcin implica que en el parmetro eatc_dona_kpi. eatc_donor_code se enviar el valor _* para las consultas 
&#160; 
 Dems selectores&#58;&#160; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 Los dems selectores del filtro se arman de acuerdo a los donantes que realizaron donaciones en el periodo segn el filtro de fechas aplicado (y que tienen un estado que permite hacer los clculos de los indicadores de sostenibilidad) de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state=received,pre-certified,certified &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_distinct= eatc_donor_fiscal_name 
&#160; 
 Al seleccionar un eatc_dona_headers. eatc_donor_fiscal_name se debe tomar el respectivo identificador del donante ( eatc_dona_headers. eatc-donor_code ) para realizar consultas subsecuentes. 

&#160; 
 Botn consultar&#58; 
 Label&#58; class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar )&#160; 

 KPIS PRINCIPALES 

 De acuerdo al filtro de fechas aplicado , y al filtro de &quot; Donante &quot; el sistema construye los siguientes indicadores&#58; 

&#160; 
 Ahorros de donantes ($) 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_ahorros_donantes_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes_desc &#160; 
&#160; 
 &quot; Sumatoria de los ahorros generados a los donantes (o el donante) en el periodo seleccionado &quot; 
&#160; 
 Llamado para el clculo&#58; &#160; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc_donor_code=&#123;&#123; eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-kpi_type= Economic%20impact &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Huella de carbono mitigada (TONS CO2) 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_huella_carbono_mitigada_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada_desc 
&#160; 
 &quot; Corresponde a las emisiones de CO2 mitigadas por los donantes (o el donante) en el periodo seleccionado al tomar la decisin de donar en vez de botar &quot; 
&#160; 
 Llamado para el clculo&#58; &#160; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc_donor_code=&#123;&#123; eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-kpi= CO2_tons &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Raciones entregadas 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_raciones_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_raciones_entregadas_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas_desc &#160; 
&#160; 
 &quot; Nmero de platos de comida entregados a poblacin final beneficiaria por parte de los donantes (o el donante) en el periodo seleccionado &quot; 
&#160; 
 Llamado para el clculo&#58; &#160; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc_donor_code=&#123;&#123;eatc_dona_headers.eatc-donor_code&#125;&#125;&amp;eatc-kpi= total_portions 
 &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

 EVOLUCIN DE MTRICAS 
 ***NUEVO &#58; Filtro (a quienes se le muestra el grfico)&#58; *** 
 A los todos los usuarios. 
&#160; 
 Ttulo del informe (Evolucin de mtricas) 
 Label&#58; class=&quot; lbl_evolucion_metricas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_evolucion_metricas )&#160; 

 Se debe mostrar en un grfico de tendencia los indicadores principales anteriormente calculados, permitiendo la seleccin del indicador para su visualizacin en la serie de tiempo (tal como se implement en el nuevo BO cuentas Analytics). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Findicadores-de-sostenibilidad%2F48309094-sostenibilidad--1-.jpg&ow=574&oh=644, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Findicadores-de-sostenibilidad%2F48309094-sostenibilidad--1-.jpg&ow=574&oh=644 
 Nuevo BO CUA MASTER Beneficiarios 

 669.000000000000 

 SOSTENIBILIDAD > INDICADORES DE SOSTENIBILIDAD