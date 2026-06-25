# sostenibilidad-por-ciudad-y-depto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Ttulo del informe&#58; Resultados por ciudad y departamento 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe, incluyendo todos los indicadores)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 Label&#58; class=&quot; lbl_resultados_por_ciudad_y &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_por_ciudad_y )&#160; 
&#160; 
 Concatenado con&#58; 
&#160; 
 Label&#58; class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_departamento_provincia_estado ) 

 Grfico de barras horizontales para mostrar el TOP 10 por ciudad 
 Se desplegar un grfico de barras horizontales, que mostrar de mayor a menor el respectivo indicador seleccionado, el top 10 de ciudades por cada indicador que ms adelante se determina&#58; 

 Ahorros de donantes ($) 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi_type= Economic%20impact &amp;_distinct=eatc-city 
&#160; 
 El sistema obtiene un array de ciudades, y para cada una ( &#123;&#123;ciudad&#125;&#125; ) deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi_type=Economic%20impact&amp;eatc-city=&#123;&#123;ciudad&#125;&#125;&amp;_cmp=value,eatc-province 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value ) por la dupla eatc-city / eatc-province obtenidos para cada ciudad en el Array y se ordena por ciudad de mayor a menor para mostrar el TOP 10 en el grfico. 

&#160; 
 Huella de carbono mitigada (TONS CO2) 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada &#160; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=CO2_tons&amp;_distinct=eatc-city 
&#160; 
 El sistema obtiene un array de ciudades, y para cada una ( &#123;&#123;ciudad&#125;&#125; ) deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=CO2_tons&amp;eatc-city=&#123;&#123;ciudad&#125;&#125;&amp;_cmp=value,eatc-province 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value ) por la dupla eatc-city / eatc-province obtenidos para cada ciudad en el Array y se ordena por ciudad de mayor a menor para mostrar el TOP 10 en el grfico. 

&#160; 
 Raciones entregadas 
 class=&quot; lbl_raciones_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=total_portions&amp;_distinct=eatc-city 
&#160; 
 El sistema obtiene un array de ciudades, y para cada una ( &#123;&#123;ciudad&#125;&#125; ) deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=total_portions&amp;eatc-city=&#123;&#123;ciudad&#125;&#125;&amp;_cmp=value,eatc-province 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value ) por la dupla eatc-city / eatc-province obtenidos para cada ciudad en el Array y se ordena por ciudad de mayor a menor para mostrar el TOP 10 en el grfico. 

 T ABLA DE RESULTADOS POR CIUDAD / DEPARTAMENTO 
 Se deber implementar una tabla paginada, que permita ordenar por los diferentes campos, que tenga filtros (datatable), que se pueda descargar y que contenga la siguiente informacin por la dupla &quot;departamento - ciudad&quot; 

 Departamento 
 Label&#58; class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_departamento_provincia_estado ) 
&#160; 
 Para determinar los departamentos que deben incorporarse en el informe (en cada fila), se debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_distinct=eatc-province 
&#160; 
 Por cada departamento encontrado &#123;&#123; DEPARTAMENTO &#125;&#125;, se debe establecer las respectivas ciudades que debern aparecer pareadas en la siguiente columna. 

&#160; 
 Ciudad 
 Label&#58; class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ciudad ) 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;_distinct=eatc-city 
&#160; 
 Cada ciudad encontrada y pareada con su respectivo departamento se deber guardar en la variable&#160; &#123;&#123; CIUDAD &#125;&#125;para las dems consultas. 

&#160; 
 Ahorros de donantes ($) 
 class=&quot; lbl_ahorros_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_donantes 
&#160; 
 Llamado para el clculo&#58; 
 El sistema para cada dupla &#123;&#123; DEPARTAMENTO &#125;&#125; / &#123;&#123; CIUDAD &#125;&#125; deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi_type=Economic%20impact&amp;eatc-province= &#123;&#123;DEPARTAMENTO&#125;&#125; &amp;eatc-city= &#123;&#123;CIUDAD&#125;&#125; &amp;_cmp=value 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value )&#160; para mostrar el indicador. 

&#160; 
 Huella de carbono mitigada (TONS CO2) 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada &#160; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema para cada dupla &#123;&#123; DEPARTAMENTO &#125;&#125; / &#123;&#123; CIUDAD &#125;&#125; deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=CO2_tons&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125;&amp;_cmp= value 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value )&#160; para mostrar el indicador. 

&#160; 
 Raciones entregadas 
 class=&quot; lbl_raciones_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_entregadas 
&#160; 
 Llamado para el clculo&#58; 
 El sistema para cada dupla &#123;&#123; DEPARTAMENTO &#125;&#125; / &#123;&#123; CIUDAD &#125;&#125; deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-kpi=total_portions&amp;eatc-province=&#123;&#123;DEPARTAMENTO&#125;&#125;&amp;eatc-city=&#123;&#123;CIUDAD&#125;&#125;&amp;_cmp=value 
&#160; 
 El sistema realiza la sumatoria de los valores ( eatc_dona_kpi . value )&#160; para mostrar el indicador. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-ciudad-y-depto%2F703359160-sostenibilidad_ciudad_depto.jpg&ow=568&oh=590, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsostenibilidad-por-ciudad-y-depto%2F703359160-sostenibilidad_ciudad_depto.jpg&ow=568&oh=590 
 Nuevo BO CUA MASTER Beneficiarios 

 674.000000000000 

 SOSTENIBILIDAD > RESULTADOS POR CIUDAD Y DEPTO.