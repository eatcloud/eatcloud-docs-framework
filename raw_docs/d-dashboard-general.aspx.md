# d-dashboard-general.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** Mensaje parte superior del dashboard (se debe mostrar despus de un login exitoso) 
 *** Ver documentacin *** 
&#160; 
 INDICADORES CLAVE&#58; 
 Mediante cuatro pestaas presenta los principales indicadores por tipo de indicador, y el botn (+) que da acceso a la funcionalidad&#58; detalle de KPI . El valor por defecto ser el mes en curso, pero se podrn ingresar fecha inicial y fecha final para ajustar los clculos presentados en el dashboard. Las pestaas son las siguientes&#58; 

&#160; 
 *****NUEVO****&#58; dinamizar las consultas necesarias para mostrar las estadsticas a partir de la cuenta maestra. 
 Cuando se ingrese a un BO, el sistema debe consultar la cuenta maestra de dicha cuenta, y a partir de dicho valor realizar las consultas necesarias para traer la informacin y los KPIs que se muestra en el dashboard. 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; =&gt; eatc_cua_master 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona_kpi?&#123;&#123;parametro_consulta&#125;&#125;=&#123;&#123;VALOR&#125;&#125; 
&#160; 
 NOTA &#58; como no se tiene informacin de los mecanismos con los cuales se consultan los KPIs y la informacin que se despliega en el dashboard de del BO, se realiza esta documentacin de manera general, por lo tanto el desarrollador deber realizar las abstracciones necesarias a partir de la misma para realizar la implementacin que lo que busca es permitir la evolucin del sistema a uno donde se manejen mltiples cuentas maestras. 

&#160; 
 *****NUEVO****&#58; en los informes y grficos donde aparecen los estados, mostrar tambin la descripcin de los estados (internacionalizada) 
 En los informes del BO en dnde se muestran los estados de los anuncios de donacin, como por ejemplo en este que se muestra a continuacin&#58; 

 En las respectivas etiquetas colocar informacin internacionalizada de la siguiente manera y tambin un cuadro de convenciones en dnde se muestre la descripcin de cada estado en el idioma respectivo&#58; 
&#160; 
 *** NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo o browser para con l realizar la nueva consulta de los estados de encabezados de anuncios de donacin. 
&#160; 
 ***NUEVO&#58; Paso 2&#58; consulta de los estados y sus descripciones 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_dona_headers_states&amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125; 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_dona_headers_states&amp;eatc_language=en&#160;&#160; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrar la informacin respectiva de la etiqueta ( eatc_nombre ) y la descripcin ( eatc_description ) 

&#160; 
 Indicadores de proceso &#58; 
 Muestra el total anuncios gestionados por el o los puntos de donacin ( eatc_pods &#58; segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_process_kpi ) 
&#160; 
 KPI Nmero de anuncios 
&#160; 
 Para realizar el clculo se debe invocar el API&#58;&#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;_compress &#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_a=exito&amp;_compress &#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_b=MEDELLIN&amp;_compress 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA&amp;_compress 
&#160; 
 Se toma el dato &quot; cont &quot; que entrega el API y se pinta en la tarjeta 

&#160; 
 Ejemplo&#58; 
 Un usuario asignado al (eatc_tipology_c) DISTRITO MEDELLIN B, el sistema deber realizar la siguiente consulta&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_c=DISTRITO%20MEDELLIN%20B&amp;_compress , como la respuesta del API es&#58;&#160; 
 &#123; 
 ts &#58; &quot;191216153945&quot;, 
 op &#58; true, 
 cont &#58; 39, 
 res &#58; 
 Debe mostrar el nmero 39 como KPI principal de proceso 

&#160; 
 Impacto Social 
 Muestra el total de Kilogramos donados por el o los puntos de donacin ( eatc_pods &#58; segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_social_impact_kpi ) 
&#160; 
 KPI KG 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_id=31 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_a=exito 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_b=MEDELLIN 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA 
&#160; 
 Se toma el dato &quot; value &quot; y realiza una sumatoria 

&#160; 
 Impacto econmico &#58; 
 Muestra el total de ahorros generados por el o los puntos de donacin ( eatc_pods &#58; segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI&#160; ( eatc_pods_economic_impact_kpi ) 
&#160; 
 KPI total ahorros 
&#160; 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Economic%20impact&amp;eatc-pod_id=31 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Economic%20impact&amp;eatc-pod_typology_a=exito 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Economic%20impact&amp;eatc-pod_typology_b=MEDELLIN 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Economic%20impact&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA 
&#160; 
 Se toma el dato &quot; value &quot; y realiza una sumatoria 

&#160; 
 Impacto ambiental &#58;&#160; 
 Muestra el total de toneladas de CO2&#160; ahorradas por el o los puntos de donacin ( eatc_pods &#58; segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_enviromental_impact_kpi ) 

&#160; 
 KPI toneladas de CO2 [PENDIENTE POR REVISAR] 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]&#58; &#160; 
 Por almacn o grupo de almacenes&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Environmental%20impact&amp;eatc-pod_id=31 &#160; 
 Por marca&#58; ejemplo https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Environmental%20impact&amp;eatc-pod_typology_a=exito &#160; 
 Por subzona&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Environmental%20impact&amp;eatc-pod_typology_b=MEDELLIN &#160; 
 Por distrito&#58; ejemplo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Environmental%20impact&amp;eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA &#160; 
&#160; 
 Se toma el dato &quot; value &quot; y realiza una sumatoria 

&#160; 
 Tablero de liderazgo 
 El dashboard presentar un &quot;Tablero de Liderazgo&quot; en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso. 

 ***NUEVO&#58; FORMULARIO NET PROMOTER SCORE**** 
&#160; 
 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio&#58; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= donantes &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;usuario&quot; del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/bo_usuarios?_id=&#123;&#123;id&#125;&#125; 
&#160; 
 eatc_plataform 
 donantes (constante para este llamado) 
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
&#160; 
 Se deber realizar el siguiente llamado para realizar el registro del NPS 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= donantes &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125;&amp;_operacion= insert 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;usuario&quot; del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/bo_usuarios?id=&#123;&#123;id&#125;&#125; 
&#160; 
 eatc_plataform 
 donantes (constante para este llamado) 
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
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma=&#123;&#123; plataforma &#125;&#125;&amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
&#160; 
 Este llamado se debe realizar cuando se oprime el botn cuyo label es &quot; nps_submit_btn &quot; . 
&#160; 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .&#160; Si no se encuentra registrado por defecto se enviar &quot; en &quot;) 
&#160; 
 eatc_plataform 
 donantes (constante para este llamado) 
&#160; 
 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fd-dashboard-general%2F1680952832-EmbeddedImage--39-.jpg&ow=1118&oh=626, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fd-dashboard-general%2F1680952832-EmbeddedImage--39-.jpg&ow=1118&oh=626 

 248.000000000000 

 DASHBOARD GENERAL (BO DONANTES)