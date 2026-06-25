# inicio-consolidado-de-resultados-totales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta funcionalidad se presentarn indicadores bsicos de la operacin general de la cuenta maestra. 
&#160; 
 El wireframe propuesto es el siguiente&#58; 

 T TULO DE LA VISTA&#58; INICIO 
 class=&quot; lbl_inicio &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_inicio &#160;&#160; 

 Descripcin&#58; &quot;Consolidado de resultados totales acumulados del ecosistema EatCloud.&quot; 
 class=&quot; lbl_inicio_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_inicio_desc &#160; 

 Filtro de fechas 
 El filtro de fechas tiene un funcionamiento similar al que se implement en Analytics , implementando los siguientes labels&#58; 
&#160; 
 Filtro&#58; &quot;Ayer&quot; 
 class=&quot; lbl_ayer &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ayer )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos del da anterior. 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_hoy )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos del da actual. 
&#160; 
 Filtro&#58; &quot;Esta Semana&quot; 
 class=&quot; lbl_esta_semana &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_esta_semana )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos de la presente semana (que empieza el da lunes). 
&#160; 
 Filtro&#58; &quot;ltimos 8 das&quot; 
 class=&quot; lbl_ultimos_8_dias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ultimos_8_dias )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos de los ltimos 8 das o la ltima semana. 
&#160; 
 Filtro&#58; &quot;Mes actual&quot; =&gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_mes_actual )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos del mes en curso (empezando por el primer da del mes actual). 
&#160; 
 Filtro&#58; &quot;ltimos 30 das&quot;&#160; 
 class=&quot; lbl_ultimos_30_dias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ultimos_30_dias )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos de los ltimos treinta das 
&#160; 
 Filtro&#58; &quot;ltimo trimestre&quot;&#160; 
 class=&quot; lbl_ultimo_trimestre &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ultimo_trimestre )&#160; 
&#160; 
 Si se selecciona, calcula los indicadores de la vista con los datos de los ltimos noventa das 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_personalizar )&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_inicial )&#160; 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_final )&#160; 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_consultar )&#160;&#160; 

 D ONANTES Y BENEFICIARIOS 
 ***NUEVO &#58; Filtro (a quienes se le muestra toda la seccin / grupo de indicadores, incluyendo su ttulo)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_donantes_beneficiarios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_beneficiarios 

 Descargar 
 class=&quot; lbl_descargar &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_descargar &#160;&#160;&#160;&#160; 
&#160; 
 Al presionar este botn se deber descargar en un excel el resumen de los indicadores presentados en la pantalla. 

 Donantes activos 
 class=&quot; lbl_donantes_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_activos &#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_donantes_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_activos_desc &#160; 
&#160; 
 &quot;Nmero de donantes que en el periodo seleccionado han realizado por lo menos un anuncio de donacin&quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_distinct= eatc-donor 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;donantes_activos&#125;&#125; 

 Donantes inactivos 
 class=&quot; lbl_donantes_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_inactivos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_donantes_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_inactivos_desc&#160; 
&#160; 
 &quot;Nmero de donantes que en el periodo seleccionado no han realizado anuncios de donacin&quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el nmero de &#123;&#123;donantes_totales&#125;&#125; &#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/eatcloud/ eatc_cua ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cont 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operacin 
 &#123;&#123; donantes_inactivos &#125;&#125; = &#123;&#123;donantes_totales&#125;&#125; - &#123;&#123;donantes_activos&#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123;donantes_inactivos&#125;&#125; 

 Puntos de donacin activos 
 class=&quot; lbl_pods_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pods_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_pods_desc&#160; 
&#160; 
 &quot; Puntos de donacin que han donado al menos una referencia o producto &quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_distinct= eatc-pod_id 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;pods_activos&#125;&#125; 

 Puntos de donacin inactivos 
 Nota importante&#58;&#160; 
 no se podr implementar hasta que no se tenga la implementacin para la creacin del dato allpods/eatc_pods.eatc_cua_master 
&#160; 
 class=&quot; lbl_pods_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pods_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_inactivos_desc &#160;&#160; 
&#160; 
 &quot;Nmero de puntos de donacin que en el periodo seleccionado no han realizado anuncios de donacin&quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el nmero de &#123;&#123;pods_totales&#125;&#125; &#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/ eatc_pods ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cont (el dato aun no existe, se deber implementar primero el proceso arriba descrito ) 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operacin 
&#160; 
 &#123;&#123; pods_inactivos &#125;&#125; = &#123;&#123;pods_totales&#125;&#125; - &#123;&#123;pods_activos&#125;&#125; 
&#160; 
 &#160;El indicador se lleva a la variable&#58; &#123;&#123;pods_inactivos&#125;&#125; 

 Gestores de donacin activos (en el diseo&#58; Instituciones activas) 
 class=&quot; lbl_doma_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activos_desc &#160;&#160; 
&#160; 
 &quot;Nmero de instituciones gestoras de donaciones, que en el periodo seleccionado se les ha adjudicado por lo menos una donacin&quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_distinct= eatc-donation_manager_name 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;doma_activos&#125;&#125; 

 Gestores de donacin inactivos (en el diseo&#58; poblacin beneficiada) 
 class=&quot; lbl_doma_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivos_desc &#160;&#160; 
&#160; 
 &quot;Nmero de instituciones gestoras de donacin habilitadas en la plataforma, que en el periodo seleccionado no han realizado anuncios de donacin&quot; 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el nmero de &#123;&#123;doma_totales&#125;&#125; &#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? eatc_state =activo &amp;_cont 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operacin 
&#160; 
 &#123;&#123; doma_inactivos &#125;&#125; = &#123;&#123;doma_totales&#125;&#125; - &#123;&#123;doma_activos&#125;&#125; 
&#160; 
 &#160;El indicador se lleva a la variable&#58; &#123;&#123;doma_inactivos&#125;&#125; 

 C ONSOLIDADO DE DONACIONES 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra toda la seccin / grupo de indicadores, incluyendo su ttulo)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_consolidado_dona &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_consolidado_dona 

 KG totales anunciados 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_kg_totales_anunciados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_anunciados &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_totales_anunciados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_anunciados_desc &#160;&#160; 
&#160; 
 Sumatoria de los de KG totales anunciados (todos los anuncios de donacin) en EatCloud por parte de todos sus clientes en el periodo seleccionado. 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-total_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 

 KG totales recibidos antes de verificacin 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_recibidos_antes_verificacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_recibidos_antes_verificacion_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_recibidos_antes_verificacion_desc &#160;&#160; 
&#160; 
 Sumatoria de los de KG totales recibidos en EatCloud de todos sus clientes en el periodo seleccionado, antes del proceso de verificacin del anuncio. 
&#160; 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin),&#160; tal como se documenta all (en este primer ejemplo de documentacin se vuelve a mostrar el filtro pero en adelante solo se especificar su naturaleza que consta en la documentacin respectiva )&#58; 

&#160; 
 &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &#58; eatc-donation_manager_code= &#123;&#123; array_beneficiarios_adscritos &#125;&#125; 

&#160; 
 &#123;&#123;filtro_eatc_dona_headers (tipo_no_BdeA) &#125;&#125; &#58; eatc-donation_manager_code= &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 

&#160; 
 El sistema debe realizar el siguiente llamado&#58; 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-state= delivered,received,pre-certified,certified&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= eatc-total_weight_kg 

 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-total_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_recibidos_antes_verificacion&#125;&#125; 

 Anuncios realizados 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_anuncios_realizados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_realizados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_anuncios_realizados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_realizados_desc&#160; 
&#160; 
 Nmero total de anuncios de donacin realizados por los clientes de EatCloud en el periodo seleccionado 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_cont 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;anuncios_realizados&#125;&#125; 

 KG totales aprovechados 
 ***NUEVO &#58; (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_totales_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_aprovechados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_totales_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_aprovechados_desc &#160; 
&#160; 
 Sumatoria de los KG efectivamente recibidos por los gestores de donacin (beneficiarios) despus de proceso de verificacin de la donacin en el periodo seleccionado. 
&#160; 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin). 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-state= received,pre-certified,certified&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= eatc-total_weight_kg 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-total_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_aprovechados&#125;&#125; 

 Porcentaje de aprovechamiento 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_pct_aprovechamiento &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pct_aprovechamiento_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento_desc &#160;&#160; 
&#160; 
 Corresponde a la divisin entre la sumatoria de los KG efectivamente recibidos por los gestores de donacin (instituciones beneficiarias) despus de proceso de verificacin de la donacin en el periodo seleccionado, y la sumatoria de los kilogramos originales (Kg netos que el donante anunci) de los anuncios efectivamente recibidos por las instituciones beneficiarias. 
&#160; 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin). 
&#160; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-state= received,pre-certified,certified&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp= eatc-original_weight_kg 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123; pct_aprovechamiento &#125;&#125; = (&#123;&#123;kg_totales_aprovechados&#125;&#125;/&#123;&#123;kg_totales_anunciados&#125;&#125; )*100 
&#160; 
 El porcentaje calculado se guarda en la respectiva variable. 

 KG no aprovechados 
 ***NUEVO &#58; Filtro&#160; (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_kg_no_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_no_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_no_aprovechados_desc &#160;&#160; 
&#160; 
 Corresponde a la diferencia (resta) entre los kilogramos originales anunciados de anuncios efectivamente recibidos por las instituciones beneficiarias (gestores de donacin) y&#160; los kilogramos efectivamente recibidos por dichas instituciones en el periodo seleccionado.&#160; 
&#160; 
 Llamado para el clculo&#58; 
 A partir de los clculos anteriormente realizados se realiza la siguiente sustraccin para obtener el indicador&#58; 
 &#123;&#123; kg_no_aprovechados &#125;&#125; = &#123;&#123;kg_totales_anunciados&#125;&#125; - &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 El porcentaje calculado se guarda en la respectiva variable. 

 S OSTENIBILIDAD 
 ***NUEVO &#58; Filtro (a quienes se le muestra toda la seccin / grupo de indicadores, incluyendo su ttulo)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_sostenibilidad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_sostenibilidad &#160; 

 Ahorros totales donantes 
 ***NUEVO &#58; Filtro&#160; (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_ahorros_totales_donantes &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_totales_donantes &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_ahorros_totales_donantes_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ahorros_totales_donantes_desc &#160; 
&#160; 
 Sumatoria de ahorros generados para todos los clientes en el periodo seleccionado 
&#160; 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin). 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-kpi_type=Economic%20impact&amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_kpi. value de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_ahorros_totales_donantes&#125;&#125; 

 Huella de carbono mitigada (Ton-CO2) 
 ***NUEVO &#58; Filtro&#160; (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_huella_carbono_mitigada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_huella_carbono_mitigada_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_huella_carbono_mitigada_desc &#160;&#160; 
&#160; 
 Sumatoria de los ahorros en CO2 para todos los clientes en el periodo seleccionado 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin). 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; kpi = CO2_tons &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_kpi. value de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;huella_carbono_mitigada&#125;&#125; 

 Raciones totales entregadas 
 ***NUEVO &#58; Filtro&#160; (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_raciones_totales_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_totales_entregadas &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_raciones_totales_entregadas_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_totales_entregadas_desc &#160;&#160; 
&#160; 
 Sumatoria del total de raciones entregadas por todos los clientes en el periodo seleccionado 
&#160; 
 Llamado para el clculo ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin). 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; kpi = total_portions &amp; &#123;&#123;filtro_eatc_dona_kpi (tipo_X) &#125;&#125; &amp;_cmp= value 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_kpi. value de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;raciones_totales_entregadas&#125;&#125; 

 ***NUEVO&#58; FORMULARIO NET PROMOTER SCORE **** 
 Llamado del servicio 
&#160; 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= beneficiarios &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;usuario&quot; del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/bo_usuarios?id=&#123;&#123;id&#125;&#125; 
&#160; 
 eatc_plataform 
 beneficiarios (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
&#160; 
 Si el servicio responde de manera negativa, no se despliega el formulario. 
&#160; 
 Si el servicio responde de manera afirmativa se desplegar el formulario respectivo. 
&#160; 
 Despliegue del formulario 
 El formulario se deber desplegar segn su definicin y los mecanismos de integracin que se provean para este fin.&#160; Se debe mirar si se despliega como un modal (que tendr dos formularios sucesivos adentro), en la parte superior de la pantalla o en la parte inferior de la&#160; 
 pantalla. 
&#160; 
 Registro del NPS ( nps_main_question ) 

 Edicin&#160; del NPS ( nps_secondary_question ) 

 Llamado para el registro del NPS ( nps_main_question ) 
 Se deber realizar el siguiente llamado para realizar el registro del NPS 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= beneficiarios &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125;&amp;_operacion= insert 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;usuario&quot; del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/bo_usuarios?id=&#123;&#123;id&#125;&#125; 
&#160; 
 eatc_plataform 
 beneficiarios (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
&#160; 
 entero_de_0_a_10 
 input del formulario respectivo 
&#160; 
 Llamado para la edicin&#160; del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma= beneficiarios &amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
&#160; 
 Este llamado se debe realizar cuando se oprime el botn cuyo label es &quot; nps_submit_btn &quot; . 
&#160; 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .&#160; Si no se encuentra registrado por defecto se enviar &quot; en &quot;) 
&#160; 
 eatc_plataform 
 beneficiarios (constante para este llamado) 
&#160; 
 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finicio-consolidado-de-resultados-totales%2F4078887803-inicio.jpg&ow=564&oh=614, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finicio-consolidado-de-resultados-totales%2F4078887803-inicio.jpg&ow=564&oh=614 
 Nuevo BO CUA MASTER Beneficiarios 

 595.000000000000 

 INICIO: CONSOLIDADO DE RESULTADOS TOTALES