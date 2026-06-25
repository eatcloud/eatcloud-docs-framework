# d-kpis-de-proceso-eatc_pods_process_kpi.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se han definido&#160; 8 indicadores de proceso (adicional a otros indicadores globales, como es el caso del nmero de anuncios) que permitirn revisar cmo est operando el sistema y revisar sus diferentes indicativos. 
&#160; 
 Se presentarn todos los indicadores e informes para&#160; el mes en curso con posibilidad de cambiar fechas de anlisis para ajustar la informacin a las mismas 

 Nmero de anuncios 
 KPI Nmero de anuncios 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;_compress &#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_a=exito&amp;_compress &#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_b=MEDELLIN&amp;_compress 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA&amp;_compress 
&#160; 
 Se toma el dato &quot; cont &quot; que entrega el API y se pinta en la tarjeta 

&#160; 
 Nmero de anuncios por estado 
 Se tomarn los anteriores datos y en barras o en tortas se mostrarn los diversos estados a los cuales corresponden 

&#160; 
 Nmero de anuncios por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se mostrar el nmero de anuncios para los almacenes que le corresponden a usuario segn su perfil 

&#160; 
 Nmero de anuncios en lnea de tiempo 
 En un grfico de tendencias se mostrarn el nmero de donaciones por da, mostrando tambin el nmero de donaciones por da por almacn. 

 Kilogramos entregados 
 KPI Kilos entregados 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_id=31 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_a=exito 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_b=MEDELLIN 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA 
&#160; 
 Se toma el dato &quot; value &quot; y realiza una sumatoria 

&#160; 
 Kilogramos promedio por anuncio 
 Se mostrar el peso promedio por anuncio (se divide el peso por el nmero de anuncios). 

&#160; 
 Kilogramos entregados por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se mostrar los kilogramos entregados para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Kilogramos en lnea de tiempo 
 En un grfico de tendencias se mostrarn los kilogramos entregados por da, mostrando tambin los kilogramos por da por almacn. 

 Porcentaje de aprovechamiento 
 KPI Porcentaje de aprovechamiento 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=porcentaje_aprovechamiento&amp;eatc-pod_id=31 &#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=porcentaje_aprovechamiento&amp;eatc-pod_typology_a=exito &#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=porcentaje_aprovechamiento&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=porcentaje_aprovechamiento&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y calcula un promedio. 

&#160; 
 Porcentaje de aprovechamiento por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio del porcentaje de aprovechamiento por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Porcentaje de aprovechamiento en lnea de tiempo 
 En un grfico de tendencias se mostrarn los porcentajes de aprovechamiento por da, mostrando tambin los porcentajes de aprovechamiento por da por almacn. 

 Tiempo de adjudicacin de los anuncios 
 KPI tiempo de adjudicacin de los anuncios 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_adjudicacin_del_anuncio&amp;eatc-pod_id=31 &#160;&#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_adjudicacin_del_anuncio&amp;eatc-pod_typology_a=exit o&#160;&#160;&#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_adjudicacin_del_anuncio&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_adjudicacin_del_anuncio&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y se muestran percentiles&#58;&#160; 
 Porcentaje de anuncios que se adjudican en menos de 10 minutos 
 Porcentaje de anuncios que se adjudican en menos de 10 minutos a 1 hora 
 Porcentaje de anuncios que se adjudican en menos de 1 a 3 horas 
 Porcentaje de anuncios que se adjudican en menos de 3 a 9 horas 
 Porcentaje de anuncios que se adjudican al da siguiente 

&#160; 
 Tiempo de adjudicacin por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio del tiempo de adjudicacin por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Tiempo de adjudicacin en lnea de tiempo 
 En un grfico de tendencias se mostrarn los tiempos de adjudicacin por da, mostrando tambin los tiempos de adjudicacin por da por almacn. 

 Tiempo de espera en recogida 
 KPI tiempo de espera en recogida de los anuncios 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_espera_en_la_recogida&amp;eatc-pod_id=31 &#160;&#160;&#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_espera_en_la_recogida&amp;eatc-pod_typology_a=exito &#160;&#160;&#160;&#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_espera_en_la_recogida&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_espera_en_la_recogida&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y se muestran percentiles&#58;&#160; 
 Porcentaje de anuncios que se adjudican en menos de 30 minutos 
 Porcentaje de anuncios que se adjudican en menos de 30 minutos a 1 hora 
 Porcentaje de anuncios que se adjudican en menos de 1 a 2 horas 
 Porcentaje de anuncios que se adjudican en menos de 2 a 7 horas 
 Porcentaje de anuncios que se adjudican al da siguiente 

&#160; 
 Tiempo de espera en recogida por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio del tiempo de espera en recogida por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Tiempo de espera en recogida en lnea de tiempo 
 En un grfico de tendencias se mostrarn los tiempos de espera en recogida por da, mostrando tambin los tiempos de espera en recogida por da por almacn. 

 Tiempo total para la recogida 
 KPI tiempo total para la recogida de los anuncios 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_total_para_la_recogida&amp;eatc-pod_id=31 &#160;&#160;&#160;&#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_total_para_la_recogida&amp;eatc-pod_typology_a=exito &#160;&#160;&#160;&#160;&#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_total_para_la_recogida&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160;&#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_de_total_para_la_recogida&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160;&#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y se muestran percentiles&#58;&#160; 
 Porcentaje de anuncios que se adjudican en menos de 3 horas 
 Porcentaje de anuncios que se adjudican en menos de 3&#160; a 5 horas 
 Porcentaje de anuncios que se adjudican en menos de 5 a 8 horas 
 Porcentaje de anuncios que se adjudican al da siguiente 

&#160; 
 Tiempo total para la recogida por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio del tiempo total para la recogida por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Tiempo de espera en recogida en lnea de tiempo 
 En un grfico de tendencias se mostrarn los tiempos totales para la recogida por da, mostrando tambin los tiempos totales para la recogida por da por almacn. 

 Niveles de servicio (se debe ajustar para mostrar tipo percentil) 
 KPI Nivel de servicio check-in 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkin&amp;eatc-pod_id=31 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkin&amp;eatc-pod_typology_a=exito &#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkin&amp;eatc-pod_typology_b=MEDELLIN &#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkin&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160; 
&#160; 
 Se toma el dato &quot; value &quot; y calcula un promedio. 

&#160; 
 Nivel de servicio check-in por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio de nivel de servicio por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Nivel de servicio check-in en lnea de tiempo 
 En un grfico de tendencias se mostrarn los niveles de servicio por da, mostrando tambin los niveles de servicio por da por almacn. 

 KPI Nivel de servicio check-out 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkout&amp;eatc-pod_id=31 &#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkout&amp;eatc-pod_typology_a=exito &#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkout&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=nivel_de_servicio_checkout&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y calcula un promedio. 

&#160; 
 Nivel de servicio check-out por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio de nivel de servicio por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Nivel de servicio check-out en lnea de tiempo 
 En un grfico de tendencias se mostrarn los niveles de servicio por da, mostrando tambin los niveles de servicio por da por almacn. 

 Tiempo recorrido para la recogida del anuncio 
 KPI tiempo de recorrido para la recogida de los anuncios 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_recorrido_recogida_anuncio&amp;eatc-pod_id=31 &#160;&#160;&#160;&#160;&#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_recorrido_recogida_anuncio&amp;eatc-pod_typology_a=exito &#160;&#160;&#160;&#160;&#160;&#160;&#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_recorrido_recogida_anuncio&amp;eatc-pod_typology_b=MEDELLIN &#160;&#160;&#160;&#160;&#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=tiempo_recorrido_recogida_anuncio&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Se toma el dato &quot; value &quot; y calcula un promedio. 

&#160; 
 Tiempo recorrido para la recogida por punto de donacin 
 Se tomarn los anteriores datos y en barras o en tortas se muestra el promedio del tiempo recorrido para la recogida por almacn para los almacenes que le corresponden a usuario segn su perfil. 

&#160; 
 Tiempo de recorrido en recogida en lnea de tiempo 
 En un grfico de tendencias se mostrarn los tiempos recorridos para la recogida por da, mostrando tambin los tiempos recorridos para la recogida por da por almacn. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 KPIS DE PROCESO