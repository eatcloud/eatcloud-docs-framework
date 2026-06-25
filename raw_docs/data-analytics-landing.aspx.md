# data-analytics-landing.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general&#58;&#160; 
 Para las cuentas (&#123;&#123;_DOM. cua_user &#125;&#125;) que no poseen un registro vlido en&#160; &quot; eatc_data_analytics_cua&quot; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Se debe desplegar esta landing que presentar informacin comercial sobre las diferentes licencias y dirigir a una plataforma comercial 

 Mockup propuesto 
 Nos han propuesto este mockup (no se debe prestar mucha atencin a la definicin del men lateral, ya que la misma se est armonizando en la respectiva documentacin ) para la funcionalidad.&#160; En trminos generales se presenta informacin que se encuentra consignada en el maestro de licencias ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=_ *&#58; en labels de nombre de la licencia&#160; ( eatc_label ) y descripcin ( eatc_description_label ) de la misma) y tambin informacin que labels configurados para este propsito., que ms abajo sern documentados 

 Descripcin tcnica&#58; 

 Ttulo&#58; Data Analytics 
 class=&quot; lbl_data_analytics &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_data_analytics ) 
&#160; 
 Subttulo&#58; Tu organizacin an no cuenta con una licencia de Data Analytics 
 class=&quot; lbl_sin_data_analytics &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_sin_data_analytics ) 
&#160; 
 Botn&#58; Adquirela ya (en el diseo&#58; Adquirir Data Analytics) 
 class=&quot; lbl_adquierela_ya &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_adquierela_ya ) 
&#160; 
 Direcciona a&#58; PENDIENTE 
&#160; 
 Descripcin bsica&#58; Data Analytics es el centro de datos de EatCloud.... 
 class=&quot; lbl_data_analytics_desc &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_data_analytics_desc) 

 Card Eficiencia 
 Muestra las etiquetas que se obtienen con la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=eficiencia 
&#160; 
 De la siguiente manera&#58; 

 Parte izquierda de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=eficiencia&amp;_distinct= eatc_label (class= lbl_eficiencia ) 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_eficiencia &#160; 

 Parte derecha de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=eficiencia&amp;_distinct= eatc_description_label (class= lbl_eficiencia_desc ) 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_eficiencia_desc &#160; 

 Card Sostenibilidad 
 Muestra las etiquetas que se obtienen con la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=sostenibilidad 
&#160; 
 De la siguiente manera&#58; 

 Parte izquierda de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=sostenibilidad&amp;_distinct= eatc_description_label (class= lbl_sostenibilidad_desc ) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_sostenibilidad_desc 

 Parte derecha de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=sostenibilidad&amp;_distinct= eatc_label (class= lbl_sostenibilidad ) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_sostenibilidad 

 Card Ahorro 
 Muestra las etiquetas que se obtienen con la siguiente consulta&#58; 
&#160; 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=ahorro 
&#160; 
 De la siguiente manera&#58; 

 Parte izquierda de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=ahorro&amp;_distinct= eatc_label&#160; 
 (class= lbl_ahorro ) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_ahorro &#160; 

 Parte derecha de la card 
&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_licences?eatc_code=ahorro&amp;_distinct= eatc_description_label (class= lbl_ahorro_desc ) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_ahorro_desc &#160; 

 Botn&#58; Adquiere Data Analytics (en el diseo&#58; Adquirir Data Analytics) 
 class=&quot; lbl_adquiere_data_analytics &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_adquiere_data_analytics ) 
&#160; 
 Direcciona a&#58; Informacin de planes analytics 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdata-analytics-landing%2F2886754024-data_analytics_landing.jpg&ow=629&oh=747, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdata-analytics-landing%2F2886754024-data_analytics_landing.jpg&ow=629&oh=747 
 Cuentas datagov 

 350.000000000000 

 DATA ANALITICS LANDING