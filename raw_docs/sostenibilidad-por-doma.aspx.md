# sostenibilidad-por-doma.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Ttulo del informe&#58; Resultados por institucin beneficiaria 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe)&#58; *** 
 A los todos los usuarios. 
&#160; 
 Nota ; a los usuarios tipo_no_BdeA les aparecer una tabla de una sola fila 

&#160; 
 Label&#58; class=&quot; lbl_resultados_por_doma &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_por_doma ) 
&#160; 
 La tabla debe permitir ordenar por cada columna (descendente y ascendentemente).&#160; El ordenamiento por defecto debe ser por la columna KG aprovechados descendente (mostrando primero los donantes ms KG aprovechados).&#160; Adems debe poder filtrar por diversos criterios (datatable).&#160; Adicionalmente deber permitir descargar la informacin en formato CSV a nivel de encabezado (presente tabla).&#160; 

 NIT Institucin beneficiaria 
 class=&quot; lbl_identificacion_tributaria &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_identificacion_tributaria &#160; &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 class=&quot; lbl_institucion_benficiaria &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_institucion_benficiaria &#160; &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para construir los registros de cada fila&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state=received,pre-certified,certified &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_distinct= eatc-donation_manager_code 
&#160; 
 Al seleccionar un eatc_dona_headers. eatc-donation_manager_code se debe tomar el respectivo identificador del donante ( eatc_dona_headers. eatc-donation_manager_name ) para llenar la siguiente columna. 

&#160; 
 Institucin beneficiaria 
 class=&quot; lbl_institucion_benficiaria &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_institucion_benficiaria &#160; &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Corresponde a 
&#160; 
eatc_dona_headers. eatc-donation_manager_name 

&#160; 
 Ahorros de donantes ($) 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ahorros_donantes 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-kpi_type= Economic%20impact &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Huella de carbono mitigada (TONS CO2) 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_huella_carbono_mitigada 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-kpi= CO2_tons &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Raciones entregadas 
 class=&quot; lbl_raciones_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_raciones_entregadas 
&#160; 
 Llamado para el clculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-kpi= total_portion &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; s &amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los Valores ( eatc_dona_kpi . value ) obtenidos. 

&#160; 
 Poblacin beneficiada =&gt; Inicialmente no va 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-doma%2F766414919-Sostenibilidad_resultados_por_doma.jpg&ow=1280&oh=661, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-doma%2F766414919-Sostenibilidad_resultados_por_doma.jpg&ow=1280&oh=661 
 Nuevo BO CUA MASTER Beneficiarios 

 682.000000000000 

 SOSTENIBILIDAD > RESULTADOS POR INSTITUCIONES BENEFICIARIAS