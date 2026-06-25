# donantes-y-beneficiarios.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mockup propuesto 

 Título del informe 
 ***NUEVO &#58; Filtro (a quienes se le muestra toda la funcionalidad)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 

 Label&#58; class=&quot; lbl_donantes_beneficiarios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donantes_beneficiarios ) 

 Filtro de fechas 
 Nota para el desarrollo&#58; este filtro debe funcionar como en anteriores implementaciones, 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; = &gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_mes_actual )&#160; 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_personalizar )&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_inicial )&#160; 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_final )&#160; 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_consultar ) 

 I NDICADORES PRINCIPALES&#58; 

 Nota para el desarrollo&#58; estos indicadores ya fueron implementados en el &quot;inicio&quot; de la presente plataforma , por lo tanto se puede reciclar su código para agilizar la implementación 
&#160; 
 De acuerdo al filtro de fechas aplicado , el sistema construye los siguientes indicadores&#58; 

&#160; 
 Donantes activos 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 
&#160; 
 class=&quot; lbl_donantes_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_activos &#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_donantes_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_activos_desc &#160; 
&#160; 
 &quot;Número de donantes que en el periodo seleccionado han realizado por lo menos un anuncio de donación&quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-donor 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;donantes_activos&#125;&#125; 

&#160; 
 Donantes inactivos 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_donantes_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_inactivos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_donantes_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_inactivos_desc &#160;&#160; 
&#160; 
 &quot;Número de donantes que en el periodo seleccionado no han realizado anuncios de donación&quot; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;donantes_totales&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/eatcloud/ eatc_cua ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cont 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
&#160; 
 &#123;&#123; donantes_inactivos &#125;&#125; = &#123;&#123;donantes_totales&#125;&#125; - &#123;&#123;donantes_activos&#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123;donantes_inactivos&#125;&#125; 

&#160; 
 Puntos de donación activos 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 
&#160; 
 class=&quot; lbl_pods_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pods_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_activos_desc &#160;&#160; 
&#160; 
 &quot; Puntos de donación que han donado al menos una referencia o producto &quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-pod_id 
&#160; 
 ***NUEVO&#58; Listado de puntos de donación activos en el territorio *** 
 El sistema deberá construir una tabla en donde se muestre&#58; 

Nombre el punto de donación 

Dirección 

Ciudad 

Departamento 

Donante 

Número de donaciones realizdas 
&#160; 
Para construir la tabla, el sistema deberá consultar el departamento al cuál pertenece el Banco (eatc_donation_managers. departamento ) y con el dato recibido deberá realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-province=&#123;&#123; eatc_donation_managers. departamento&#125;&#125;&amp;_cmp=eatc-pod_name,eatc-pod_address,eatc-city 
&#160; 
 Por cada punto de donación establecerá el número de donaciones generadas en el periodo y lo presentará en la tabla. 
&#160; 
 El sistema de permitirá al usuario del BdeA, cambiar el departamento por el cual se filtra, para encontrar donaciones que para el periodo de tiempo estubieron en otros departamentos (ojalá aledaños al departamento origen solamente) 

&#160; 
 Puntos de donación inactivos 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 class=&quot; lbl_pods_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pods_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_inactivos_desc &#160;&#160; 
&#160; 
 &quot;Número de puntos de donación que en el periodo seleccionado no han realizado anuncios de donación&quot; 
&#160; 
 Llamado para el cálculo&#58;&#160; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;pods_totales&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/ eatc_pods ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cont (Se entiende que el proceso necesario para obtener este indicador ya fue implementado anteriormente) 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
&#160; 
 &#123;&#123; pods_inactivos &#125;&#125; = &#123;&#123;pods_totales&#125;&#125; - &#123;&#123;pods_activos&#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123;pods_inactivos&#125;&#125; 

&#160; 
 Gestores de donación activos (en el diseño&#58; Instituciones activas) 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 
&#160; 
 class=&quot; lbl_doma_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_activos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activos_desc &#160;&#160; 
&#160; 
 &quot;Número de instituciones gestoras de donaciones, que en el periodo seleccionado se les ha adjudicado por lo menos una donación&quot; 
&#160; 
 Llamado para el cálculo&#58;&#160; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-donation_manager_name 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;doma_activos&#125;&#125; 

&#160; 
 Gestores de donación inactivos (en el diseño&#58; población beneficiada) 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 
&#160; 
 class=&quot; lbl_doma_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_inactivos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivos_desc &#160;&#160; 
&#160; 
 &quot;Número de instituciones gestoras de donación habilitadas en la plataforma, que en el periodo seleccionado no han realizado anuncios de donación&quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;doma_totales&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? organizacion_vinculada = &#123;&#123; eatc_users .organizacion &#125;&#125; &amp; eatc_state =activo &amp;_cont 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
&#160; 
 &#123;&#123; doma_inactivos &#125;&#125; = &#123;&#123;doma_totales&#125;&#125; - &#123;&#123;doma_activos&#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123;doma_inactivos&#125;&#125; 

&#160; 
 ***NUEVO&#58; Ciudades con donaciones *** 
 Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 
&#160; 
 class=&quot; lbl_ciudades_dona &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ciudades_dona &#160; &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_ciudades_dona_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ciudades_dona_desc &#160; 
&#160; 
 &quot;Número de ciudades, que en el periodo seleccionado, han tenido anuncios de donación&quot; 
&#160; 
 Llamado para el cálculo&#58; filtro diferenciado por tipo de organización&#58; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado para obtener el número de ciudades desde las cuales se han realizado anuncios de donación 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-city 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador.&#160; 

 EVOLUCIÓN DE MÉTRICAS 
&#160; 
 Título del informe (Evolución de métricas) 
 Label&#58; class=&quot; lbl_evolucion_metricas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_evolucion_metricas )&#160; 

 Se debe mostrar en un gráfico de tendencia los indicadores principales anteriormente calculados, permitiendo la selección del indicador para su visualización en la serie de tiempo (tal como se implementó en el nuevo BO cuentas Analytics). 

 Filtros 
 Los filtros por los siguientes criterios, podrán ser implementados en una segunda etapa&#58; 

&#160; 
 Label&#58; class=&quot; lbl_filtros &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_filtros )&#160; 

&#160; 
 Label&#58; class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_departamento_provincia_estado )&#160;&#160; 

&#160; 
 Label&#58; class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ciudad )&#160;&#160; 

&#160; 
 Label&#58; class=&quot; lbl_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donante )&#160; 

 Nota importante para implementar resultados por ciudad y por departamento&#58; 
 Se puede consultar la documentación de la tabla de información por departamento - ciudad (más abajo) para tener ideas en cuanto a esta implementación. 

 RESULTADOS POR CIUDAD 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe)&#58; *** 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 Título del informe 
 CONCATENACIÓN DE&#58; Resultados por 
&#160; 
 Label&#58; class=&quot; lbl_resultados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_por )&#160; 
&#160; 
 Y&#58; Ciudad 
 Label&#58; class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ciudad )&#160; 
&#160; 

 El informe, se debe basar en los informes por ciudad implementados para el Nuevo BO Cuentas Analytics ( como por ejemplo este ), en donde (a diferencia del mockup propuesto) se mostraban barras horizontales con el top 10 y el resto se mostraba un listado. 

 RESULTADO POR DEPARTAMENTO 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 
&#160; 
 Título del informe 
 CONCATENACIÓN DE&#58; Resultados por 
&#160; 
 Label&#58; class=&quot; lbl_resultados_por &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_resultados_por )&#160; 
&#160; 
 Y&#58; Departamento 
&#160; 
 Label&#58; class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_departamento_provincia_estado )&#160; 

 El informe, se debe basar en los informes por ciudad implementados para el Nuevo BO Cuentas Analytics ( como por ejemplo este ), en donde (a diferencia del mockup propuesto) se mostraban barras horizontales con el top 10 y el resto se mostraba un listado. 

 T ABLA DE INFORMACIÓN DE INDICADORES POR DEPARTAMENTO Y CIUDAD 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master 

&#160; 
 Se deberá implementar una tabla que permita ordenar por los diferentes campos y que tenga filtros (datatable) y que contenga la siguiente información por la dupla &quot;departamento - ciudad&quot; 

 Departamento 
 Label&#58; class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_departamento_provincia_estado ) 
&#160; 
 Para determinar los departamentos que deben incorporarse en el informe (en cada fila), se debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;_distinct=eatc-province 
&#160; 
 Por cada departamento encontrado &#123;&#123; DEPARTAMENTO &#125;&#125;, se debe establecer las respectivas ciudades que deberán aparecer pareadas en la siguiente columna. 

&#160; 
 Ciudad 
 Label&#58; class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_ciudad ) 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;_distinct=eatc-city 
&#160; 
 Cada ciudad encontrada y pareada con su respectivo departamento se deberá guardar en la variable&#160; &#123;&#123; CIUDAD &#125;&#125;para las demás consultas. 

&#160; 
 Donantes activos 
 class=&quot; lbl_donantes_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_activos &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125;&amp;_distinct= eatc-donor 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;donantes_activos_dpto_ciudad&#125;&#125; 

&#160; 
 Donantes inactivos 
 class=&quot; lbl_donantes_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donantes_inactivos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;donantes_totales_depto_ciudad&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc-cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125;&amp;_distinct=eatc-cua 
&#160; 
 Se toma el cont de la respuesta y se lleva a la variable &#123;&#123;donantes_totales_depto_ciudad&#125;&#125; 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
 &#123;&#123; donantes_inactivos_depto_ciudad &#125;&#125; = &#123;&#123;donantes_totales _depto_ciudad &#125;&#125; - &#123;&#123; donantes_activos_dpto_ciudad &#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123;donantes_inactivos_depto_ciudad&#125;&#125; 

&#160; 
 Puntos de donación activos 
 class=&quot; lbl_pods_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125; &amp;_distinct= eatc-pod_id 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;pods_activos_dpto_ciudad&#125;&#125; 

&#160; 
 Puntos de donación inactivos 
 class=&quot; lbl_pods_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;pods_totales_depto_ciudad&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/ eatc_pods ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125;&amp;_cont (Se entiende que el proceso necesario para obtener este indicador ya fue implementado anteriormente) 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
 &#123;&#123; pods_inactivos_depto_ciudad &#125;&#125; = &#123;&#123; pods_totales_depto_ciudad &#125;&#125; - &#123;&#123; pods_activos_dpto_ciudad &#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123; pods_inactivos_depto_ciudad &#125;&#125; 

&#160; 
 Gestores de donación activos (en el diseño&#58; Instituciones activas) 
 class=&quot; lbl_doma_activos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activos &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-province=&#123;&#123; DEPARTAMENTO &#125;&#125;&amp;eatc-city=&#123;&#123; CIUDAD &#125;&#125;&amp;_distinct= eatc-donation_manager_name 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;doma_activos_depto_ciudad&#125;&#125; 

&#160; 
 Gestores de donación inactivos (en el diseño&#58; población beneficiada) 
 class=&quot; lbl_doma_inactivos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivos &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; 
 El sistema debe realizar el siguiente llamado para obtener el número de &#123;&#123;doma_totales_depto_ciudad&#125;&#125; &#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_donation_managers? departamento= &#123;&#123; DEPARTAMENTO &#125;&#125;&amp; municipio =&#123;&#123; CIUDAD &#125;&#125;eatc_state =activo &amp;_cont 
&#160; 
 Se toma el dato obtenido para realizar la siguiente operación 
 &#123;&#123; doma_inactivos _depto_ciudad &#125;&#125; = &#123;&#123; doma_totales_depto_ciudad &#125;&#125; - &#123;&#123; doma_activos_depto_ciudad &#125;&#125; 
&#160; 
 El indicador se lleva a la variable&#58; &#123;&#123; doma_inactivos _depto_ciudad &#125;&#125; 

 T ABLA&#58; DONACIONES POR INSTITUCIONES BENEFICIARIAS (EN EL DISEÑO&#58; NO TIENE TÍTULO) 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra la tabla)&#58; *** 
&#160; 
 A los usuarios tipo&#160; eatc_cua_master y&#160; tipo_BdeA &#160; 

&#160; 
 Label&#58; class=&quot; lbl_dona_por_doma &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_dona_por_doma )&#160; 
&#160; 
 La tabla debe permitir ordenar por cada columna (descendente y ascendentemente).&#160; El ordenamiento por defecto debe ser por la columna KG aprovechados descendente (mostrando primero los donantes más KG aprovechados).&#160; Además debe poder filtrar por diversos criterios (datatable).&#160; Adicionalmente deberá permitir descargar la información en formato CSV a nivel de encabezado (presente tabla). 

 NIT Donante 
 class=&quot; lbl_id_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_id_donante &#160; 
&#160; 
 Corresponde a&#160; 
 eatc_dona_headers. eatc-donor_code 
&#160; 
 De acuerdo a la selección del filtro de fechas del informe &#160; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-donor_code 
&#160; 
 Donante 
 class=&quot; lbl_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donante &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Corresponde a&#160; 
 eatc_dona_headers. eatc-donor_fiscal_name 
&#160; 
 De acuerdo a la selección del filtro de fechas del informe ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donor_code =&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_cmp= eatc-donor_fiscal_name 

&#160; 
 Institución beneficiaria 
 class=&quot; lbl_institucion_benficiaria &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_institucion_benficiaria &#160; &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Llamado para construir los registros de cada fila&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) e institución beneficiaria (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-donation_manager_name 
&#160; 
 Para colocar el nombre de la institución beneficiaria. 

&#160; 
 Número de anuncios 
 class=&quot; lbl_numero_anuncios &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_anuncios 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 

 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) e institución beneficiaria (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_cont 
&#160; 
 Para tomar el valor &quot; count &quot; como el valor del indicador. 

&#160; 
 KG aprovechados 
 class=&quot; lbl_kg_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_aprovechados &#160;&#160;&#160;&#160; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 

&#160; 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) e institución beneficiaria (eatc_dona_headers. eatc-donation_manager_code ) se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp;eatc-state= received &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_cmp= total_weight_kg 
&#160; 
 El sistema realiza la sumatoria de los KG totales ( eatc_dona_headers. eatc-total_weight_kg ) obtenidos.&#160; 

&#160; 
 Ver detalles (en el diseño &quot;Ver detalle&quot;) 
 Para cada par de donante (eatc_dona_headers. eatc-donor_code ) e institución beneficiaria (eatc_dona_headers. eatc-donation_manager_code ) el sistema debe presentar el vínculo 
&#160; 
 class=&quot; lbl_ver_detalles &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ver_detalle &#160; 
&#160; 
 Al hacer clic se desplegará una tabla de detalles 
&#160; 
 Tabla de detalles&#58; 
 Tabla paginada que se pueda ordenar por los diferentes campos y que sea descargable en formato Excel. 

 Al hacer clic el sistema deberá realizar la siguiente consulta para amar una tabla con los resultados obtenidos&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 

 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor_code &#125;&#125;&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_cmp= eatc-code,eatc-publication_date,eatc-publication_datetime,eatc-state,eatc-pod_name,eatc-pod_address,eatc-city,eatc-total_weight_kg,eatc-total_cost 
&#160; 
 Con los datos obtenidos se arma la información de la tabla de la siguiente manera&#58; 
&#160; 
 Código del anuncio 
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
 class=&quot; lbl_estado_anuncio &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_estado_anuncio &#160; &#160; &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-state 

&#160; 
 Punto de donación 
 class=&quot; lbl_pod &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pod &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-pod_name 

&#160; 
 Dirección (en el diseño &quot;Dirección del punto de donación&quot;) 
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
 Costo de la donación 
 class=&quot; lbl_costo_donacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_costo_donacion &#160; 
&#160; 
 Se muestra el valor obtenido en eatc_dona_headers. eatc-total_cost 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-y-beneficiarios%2F9031999-donantes_beneficiarios_tbl.jpg&ow=1280&oh=363, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-y-beneficiarios%2F9031999-donantes_beneficiarios_tbl.jpg&ow=1280&oh=363 
 Nuevo BO CUA MASTER Beneficiarios 

 656.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"}] 
 72a8d76a-c684-48c7-b245-3e8028569fa8 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 a55eeb0b-9ea9-45f5-9424-79bb4a044cb3 
 2025-04-26T06:03:05.3480530Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"b60a37d1-4d49-4005-9b9d-1fa7b0fbaf06","SequenceId":1893,"FluidContainerCustomId":"630081a5-370e-4fa2-b477-a861becbf306","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 RESULTADOS DE DONACIONES > DONANTES Y BENEFICIARIOS