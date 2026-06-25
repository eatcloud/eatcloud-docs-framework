# listado-beneficiarios-finales.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 L ISTADO DE GESTORES DE DONACIONES 
 Label&#58; class=&quot;lb_listado_doma&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lb_listado_doma 
&#160; 
 Label&#58; class=&quot;lb_listado_doma_desc&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lb_listado_doma_desc &#160; 
&#160; 
 En esta seccin encontrars informacin sobre el rescate de alimentos de las instituciones inscritas 

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
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_consultar ) &#160; 

&#160; 
 Llamado para obtener los datos ***NUEVO&#58; filtro diferenciado por tipo de organizacin&#58; *** 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 Para obtener los datos de las organizaciones que se presentarn en el listado el sistema debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_BdeA) &#125;&#125; &amp;_distinct= eatc-donation_manager_code 
&#160; 
 A partir de esta informacin obtenida ( array_eatc_donation_manager_codes ) se aplicarn los filtros abajo descritos. 
&#160; 
 Filtro de estados 
 Para obtener los estados que se desplegarn en un selector nico como criterios de filtro, se debe realizar la siguiente consulta&#58; 
&#160; 
&#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_doma_states?active_status=y&amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct=eatc_state_lbl 
&#160; 
 Ejemplo &#58; cua_master&#58; abaco , ambiente de pruebas 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_states?active_status=y&amp;eatc_cua_master= abaco&amp;_distinct=eatc_state_lbl &#160;&#160; 
&#160; 
 A los filtros que se obtienen en la consulta, se les deber adicionar la opcin &quot; Todos &quot;, como se indica ms adelante 
&#160; 
 Filtro&#58; &quot;Inactivo&quot;&#160; 
 class=&quot; lbl_inactivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_inactivo )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_eatc_donation_manager_codes &#125;&#125;&amp;eatc_state =inactivo 
&#160; 
 Filtro&#58; &quot;Activo&quot; = &gt; Valor por defecto 
 class=&quot; lbl_activo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_activo )&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_eatc_donation_manager_codes &#125;&#125; &amp;eatc_state =activo 
&#160; 
 Filtro&#58; &quot;Suspendido&quot; 
 class=&quot; lbl_suspendido &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_suspendido )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_eatc_donation_manager_codes &#125;&#125; &amp;eatc_state =suspendido 
&#160; 
 Filtro&#58; &quot;Expulsado&quot; 
 class=&quot; lbl_expulsado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_expulsado )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_eatc_donation_manager_codes &#125;&#125; &amp;eatc_state =expulsado 
&#160; 
 Filtro&#58; &quot;Todos&quot; 
 class=&quot; lbl_todos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_todos ) 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista (todos los gestores de donaciones)&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_eatc_donation_manager_codes &#125;&#125; &amp;eatc_state =suspendido,activo,inactivo,expulsado,&quot;&quot; 

&#160; 
 Botn&#58; &quot;Descargar&quot; 
 class=&quot; lbl_descargar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_descargar )&#160; 
&#160; 
 Al presionar este botn se descargarn los datos de la siguiente lista segn el criterio de filtro aplicado. 

 L ISTADO DE GESTORES DE DONACIONES 
 Listado paginado y ordenado 
 Se deben utilizar las funciones de paginado y ordenamiento definidas para las consultas (si las mismas no funcionan como estn en la documentacin se deber contactar a Jess Ramrez para la revisin de las funciones y su despliegue en los ambientes &quot;beneficiario&quot;&#58; dev y produccin), con el nimo de construir un listado paginado (con 20 resultados mximo por pgina) y ordenado por el campo que se estipula ms adelante . Se puede implementar la paginacin como una segunda etapa de la funcionalidad y tambin se puede reutilizar cdigo que se utiliz en la funcionalidad de la nueva WAPP Donantes &quot; Listado de donaciones &quot; (implementado por Jean) y la funcionalidad de la APP beneficiarios &quot; Mis donaciones &quot; (implementada por Ivn). 
&#160; 
 El listado estar compuesto por las siguientes columnas&#58; 
&#160; 
 Nombre de la organizacin&#58; 
 class=&quot; lbl_nombre_organizacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_nombre_organizacion )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . organizacin 
&#160; 
 NIT&#58; 
 class=&quot; lbl_identificacion_tributaria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_identificacion_tributaria )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . identificador_unico_registro 
&#160; 
 Ciudad&#58; 
 class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ciudad )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . municipio 
&#160; 
 ***NUEVO&#58; Correo electrnico&#58; *** 
 class=&quot; lbl_correo_electronico &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_correo_electronico )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . correo_electronico 
&#160; 
 Cada dato deber incorporar un vnculo &quot;mailto&quot; que al presionarlo permita generar un correo electrnico a la respectiva direccin 
&#160; 
 Nmero de donaciones&#58; =&gt; Se debe ordenar por esta columna, mostrando primero las instituciones beneficiarias con ms donaciones . 
 class=&quot; lbl_numero_dona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_numero_dona ) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc-donation_manager_code &#125;&#125;&amp;_cont 
&#160; 
 Se toma el &quot; cont &quot; de la respuesta para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;anuncios_totales&#125;&#125; 
&#160; 
 KG totales aprovechados&#58; 
 class=&quot; lbl_kg_totales_aprovechados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_aprovechados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_kg_totales_aprovechados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_kg_totales_aprovechados_desc &#160; 
&#160; 
 Sumatoria de los KG efectivamente recibidos por los gestores de donacin (beneficiarios) despus de proceso de verificacin de la donacin en el periodo seleccionado. 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc-donation_manager_code &#125;&#125;&amp; eatc-state= received,pre-certified,certified 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-total_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_aprovechados&#125;&#125; 

&#160; 
 Porcentaje de aprovechamiento 
 class=&quot; lbl_pct_aprovechamiento &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pct_aprovechamiento_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_aprovechamiento_desc &#160;&#160; 
&#160; 
 Corresponde a la divisin entre la sumatoria de los KG efectivamente recibidos por los gestores de donacin (instituciones beneficiarias) despus de proceso de verificacin de la donacin en el periodo seleccionado, y la sumatoria de los kilogramos originales (Kg netos que el donante anunci) de los anuncios efectivamente recibidos por las instituciones beneficiarias. 
&#160; 
 Llamado para el clculo&#58; 
 El numerador para calcular el porcentaje ser &#123;&#123;kg_totales_aprovechados&#125;&#125; 
&#160; 
 Para obtener el denominador, el sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc-donation_manager_code &#125;&#125;&amp; eatc-state= received,pre-certified,certified 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_headers. eatc-original_weight_kg de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;kg_totales_anunciados&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123; pct_aprovechamiento &#125;&#125; = (&#123;&#123;kg_totales_aprovechados&#125;&#125;/&#123;&#123;kg_totales_anunciados&#125;&#125; )*100 
&#160; 
 El porcentaje calculado se guarda en la respectiva variable. 

&#160; 
 Raciones totales entregadas (en el diseo&#58; &quot; Cantidad poblacin beneficiaria &quot;) 
 class=&quot; lbl_raciones_totales_entregadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_totales_entregadas &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_raciones_totales_entregadas_desc2 &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_raciones_totales_entregadas_desc2 &#160; 
&#160; 
 Corresponde a la sumatoria del total de raciones entregadas por el respectivo gestor de donaciones en el periodo seleccionado 
&#160; 
 Llamado para el clculo&#58; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_kpi?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc-donation_manager_code &#125;&#125;&amp; kpi = total_portions 
&#160; 
 El sistema toma el dato que se encuentra registrado en eatc_dona_kpi. value de la anterior consulta y realiza una sumatoria del mismo para obtener el indicador. El indicador se lleva a la variable&#58; &#123;&#123;raciones_totales_entregadas&#125;&#125; 

&#160; 
 % de efectividad de anuncios recibidos (en el diseo&#58; % de efectividad de anuncios recogidos ) 
 class=&quot; lbl_pct_efectividad_anuncios_recibidos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_efectividad_anuncios_recibidos ) 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pct_efectividad_anuncios_recibidos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pct_efectividad_anuncios_recibidos_desc &#160;&#160; 
&#160; 
 Corresponde a la divisin entre el nmero de donaciones que fueron despachadas a la institucin beneficiaria, sobre el total de donaciones adjudicadas a dicha institucin en el periodo seleccionado. 
&#160; 
 Llamado para el clculo&#58; 
 Para obtener el numerador, el sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc-donation_manager_code &#125;&#125;&amp; eatc-state= delivered,received,pre-certified,certified &amp;_cont 
&#160; 
 La respuesta de la anterior consulta se guarda en la variable&#58; &#123;&#123;anuncios_recibidos&#125;&#125; 
&#160; 
 El denominador para calcular el porcentaje ser &#123;&#123;anuncios_totales&#125;&#125; 
&#160; 
 Para el clculo del porcentaje se realiza el siguiente clculo&#58; 
 &#123;&#123;pct_efectividad_anuncios_recibidos&#125;&#125; = ( &#123;&#123;anuncios_recibidos&#125;&#125; / &#123;&#123;anuncios_totales&#125;&#125; )*100 
&#160; 
 El porcentaje calculado se guarda en la respectiva variable. 

&#160; 
 Ver detalles&#58; 
 class=&quot; lbl_ver_detalles &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ver_detalles )&#160; 
&#160; 
 En cada registro mostrar un vnculo a la prxima pantalla de la funcionalidad, que permitir ver una ficha del gestor de donaciones.&#160; Al hacer clic en un &quot; Ver detalles &quot; particular,&#160; con el cdigo del beneficiario seleccionado ( eatc_donation_managers . identificador_unico_registro ) el sistema deber realizar la siguiente consulta con el fin de obtener los datos requeridos para la siguiente vista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125; 

&#160; 
 Ejemplo &#58; entorno&#160; de pruebas, cuenta maestra Abaco , identificador_unico_registro = 900326456 &#160; 
&#160; 
El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios .eatcloud.info /api/abaco/ eatc_donation_managers? identificador_unico_registro = 900326456 &#160; &#160; 
&#160; 
 Con los datos obtenidos de la consulta se procede a pintar los datos de la siguiente pantalla o funcionalidad. 

&#160; 
 F ICHA DEL GESTOR DE DONACIONES 
 class=&quot; lbl_ficha_doma &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ficha_doma ) 

 Descripcin general 
 En esta ficha se mostrar informacin completa del beneficiario,&#160; que podr ser editada por el usuario administrador respectivo. 
&#160; 
 Tambin se podr consultar informacin sobre los grupos etarios registrados por la organizacin. 
&#160; 
 Mostrar tambin el listado de donaciones que ha manejado la organizacin beneficiaria. 
&#160; 
 Por ltimo (en una etapa posterior), se mostrar informacin sobre los conductores que son autorizados para recolectar donaciones para la respectiva fundacin. 
&#160; 
 A continuacin se establecen los detalles para la implementacin de estas secciones interactivas e informativas sobre los gestores de donaciones. 

 D ATOS DE LA ORGANIZACIN 

 I NFORMACIN DE LA ORGANIZACIN =&gt; MEJORA&#58; Que el formulario se abra antes del listado (no despus como est hoy) y con un ancla para que cuando se oprima el nit, el usuario se ubique en el inicio del formulario 
 class=&quot; lbl_info_doma &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_info_doma ) 
&#160; 
 El sistema desplegar un formulario que permitir consultar y editar los datos bsicos del gestor de donaciones de la siguiente manera&#58; 

 Nombre de la organizacin 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_nombre_org &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_nombre_org )&#160; 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= organizacin 

 Tipo de campo de captura 
 Text input 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el nombre anterior de la organizacin ( nombre_org ) y el nuevo nombre registrado por el usuario ( text_input_nuevo_nombre_org ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; organizacin =&#123;&#123; text_input_nuevo_nombre_org &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= organizacin &amp;eatc_doma_prev_value= &#123;&#123; nombre_org &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; text_input_nuevo_nombre_org &#125;&#125; 

&#160; 
 Tipo de institucin 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_tipo_institucion (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_tipo_institucion) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= tipo_organizacion 
&#160; 
 Tipo de campo de captura 
 Selector nico 
&#160; 
 De dnde toma los datos el selector 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_doma_typology_a ?_id=_*&amp;_distinct =eatc_label 
&#160; 
 A partir de un cambio, se lleva al registro ( selector_nuevo_tipo_org )&#58; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_doma_typology_a ? eatc_label=&#123;&#123;opcion_seleccionada&#125;&#125; &amp;_distinct = eatc_name 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el tipo anterior de la organizacin ( tipo_org ) y el nuevo tipo seleccionado por el usuario ( selector_nuevo_tipo_org ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; tipo_organizacion =&#123;&#123; selector_nuevo_tipo_org &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= tipo_organizacion &amp;eatc_doma_prev_value= &#123;&#123; tipo_org &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; selector_nuevo_tipo_org &#125;&#125; 

&#160; 
 ***NUEVO&#58; Clasificacin de la organizacin *** 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_clasificacion_org &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_clasificacion_org ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= eatc_doma_typology_b 
&#160; 
 Concatenada con&#58; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_doma_typology_b ? eatc_code =&#123;&#123;eatc_donation_managers . eatc_doma_typology_b &#125;&#125; &amp;_distinct = eatc_name 
&#160; 
 Tipo de campo de captura 
 Selector nico 
&#160; 
 De dnde toma los datos el selector 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_doma_typology_b ?_id=_*&amp;_distinct = eatc_name 
&#160; 
 A partir de un cambio, se lleva al registro ( selector_nueva_clasificacion_org )&#58; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_doma_typology_a ? eatc_name =&#123;&#123;opcion_seleccionada&#125;&#125; &amp;_distinct = eatc_code 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable la anterior clasificacin de la organizacin ( clasificacion_org ) y el nuevo tipo seleccionado por el usuario ( selector_nueva_clasificacion_org ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; eatc_doma_typology_b =&#123;&#123; selector_nueva_clasificacion_org &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= eatc_doma_typology_b &amp;eatc_doma_prev_value= &#123;&#123; clasificacion_org &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; selector_nueva_clasificacion_org &#125;&#125; 

&#160; 
 NIT 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_identificacion_tributaria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_identificacion_tributaria ) 
&#160; 
 Valor que se muestra 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= identificador_unico_registro 
&#160; 
 Por ser el identificador del registro, el mismo no se debe permitir editar. 

&#160; 
 Representante legal 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_representante_legal &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_representante_legal ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= representante_legal 
&#160; 
 Tipo de campo de captura 
 Text input 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el nombre del anterior representante legal ( nombre_rep_legal ) y el nuevo nombre registrado por el usuario ( text_input_nuevo_rep_leg ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; representante_legal =&#123;&#123; text_input_nuevo_rep_leg &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= representante_legal &amp;eatc_doma_prev_value= &#123;&#123; nombre_rep_legal &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; text_input_nuevo_rep_leg &#125;&#125; 

&#160; 
 Organizacin vinculada 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_organziacin_vinculada ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_organziacin_vinculada ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= tipo_organizacion 
&#160; 
 Tipo de campo de captura 
 Selector nico 
&#160; 
 De dnde toma los datos el selector 
 En un selector se debe mostrar el campo &quot; eatc_donation_managers. organizacin &quot; y al seleccionarlo llevar al registro &quot; eatc_donation_managers. identificador_unico_registro &quot;, los valores que se pueden mostrar corresponden a&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers? tipo_organizacion =BdeA,Agremiaci%C3%B3n,Arquidi%C3%B3sesis,Di%C3%B3sesis,Confederaci%C3%B3n,Federaci%C3%B3n&amp;eatc_state=activo&amp;_distinct= organizacin 
&#160; 
 Y se debe adicionar la opcin &quot;exito&quot;. 
&#160; 
 Ejemplo&#58; ABACO entorno de pruebas&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?tipo_organizacion=BdeA,Agremiaci%C3%B3n,Arquidi%C3%B3sesis,Di%C3%B3sesis,Confederaci%C3%B3n,Federaci%C3%B3n&amp;eatc_state=activo&amp;_distinct= organizacin &#160; 
&#160; 
 A los anteriores valores se les debe adicionar el valor &quot;Exito&quot; 
&#160; 
 A partir de un cambio, se lleva al registro ( selector_nuevo_org_vinculada )&#58; 
 eatc_donation_managers. identificador_unico_registro 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el la organizacin vinculada anterior ( org_vinculada ) y la nueva organizacin vinculada seleccionada por el usuario ( selector_nuevo_org_vinculada ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; organizacion_vinculada =&#123;&#123; selector_nuevo_org_vinculada &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= organizacion_vinculada &amp;eatc_doma_prev_value= &#123;&#123; org_vinculada &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; selector_nuevo_org_vinculada &#125;&#125; 

&#160; 
 Capacidad de recogida ( no est en el mockup ) 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_capacidad_recogida &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_capacidad_recogida ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= capacidad_recogida 
&#160; 
 Tipo de campo de captura 
 Integer input 
&#160; 
 Validaciones 
 Las siguiente validaciones ya se implementaron en el formulario de registro de beneficiarios ( &#123;&#123; URL_entorno_beneficarios &#125;&#125;/_registro/index.html?&#123;&#123;_DOM. cua_master &#125;&#125; ) por lo tanto se recomienda reciclar el cdigo de dicho formulario. 
&#160; 
 No puede estar vaco. 
 Debe ser mayor que &quot;0&quot; (cero) 
 Debe ser menor a&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_max_kg_x_doma_typology_b ?eatc_doma_typology_b=&#123;&#123;eatc_donation_managers. eatc_doma_typology_b &#125;&#125; 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable la capacidad anterior ( capacidad_recogida ) y la nueva registrada por el usuario ( int_input_nueva_capacidad_recogida ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; capacidad_recogida =&#123;&#123; int_input_nueva_capacidad_recogida &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= capacidad_recogida &amp;eatc_doma_prev_value= &#123;&#123; capacidad_recogida &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; int_input_nueva_capacidad_recogida &#125;&#125; 

&#160; 
 Capacidad de gestin ( no est en el mockup ) 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_capacidad_gestion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_capacidad_gestion ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= capacidad_gestion 
&#160; 
 Tipo de campo de captura 
 Integer input 
&#160; 
 Validaciones 
 Las siguiente validaciones ya se implementaron en el formulario de registro de beneficiarios ( &#123;&#123; URL_entorno_beneficarios &#125;&#125;/_registro/index.html?&#123;&#123;_DOM. cua_master &#125;&#125; ) por lo tanto se recomienda reciclar el cdigo de dicho formulario. 
&#160; 
 No puede estar vaco. 
 Debe ser mayor que &quot;0&quot; (cero) 
 Debe ser menor a&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_max_kg_x_doma_typology_b ?eatc_doma_typology_b=&#123;&#123;eatc_donation_managers. eatc_doma_typology_b &#125;&#125; 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable la capacidad anterior ( capacidad_gestion ) y la nueva registrada por el usuario ( int_input_nueva_capacidad_gestion ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; capacidad_gestion =&#123;&#123; int_input_nueva_capacidad_gestion &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= capacidad_gestion &amp;eatc_doma_prev_value= &#123;&#123; capacidad_gestion &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; int_input_nueva_capacidad_gestion &#125;&#125; 

 U BICACIN 
 class=&quot; lbl_ubicacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ubicacion ) 
&#160; 
 El sistema desplegar un formulario que permitir consultar y editar los datos de la ubicacin del donante.&#160; Para esta implementacin, a diferencia de lo que se propone en el mockup, nos debemos basar en la implementacin realizada para el formulario de registro de donantes, con el fin de presentar (de ser necesaria la edicin) un mapa con la coordenada y a partir del cambio del mismo, desplegar los datos de departamento y ciudad (con el nimo de procurar calidad en los datos). 

 Coordenadas (no est en el mockup) 
 La idea es que se muestre el dato de las coordenadas y al lado de las mismas un botn que diga &quot;mapa&quot; ( class=&quot; lbl_mapa &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_mapa ) ), que al presionarlo despliegue un mapa que permita editar las coordenadas 
&#160; 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_coordenadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_coordenadas ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= coordenadas 
&#160; 
 Tipo de campo de captura 
 Map input (similar a la implementacin para el registro de beneficiarios&#58; &#123;&#123; URL_entorno_beneficarios &#125;&#125;/_registro/index.html?&#123;&#123;_DOM. cua_master &#125;&#125; ), que se activa mediante el botn&#58; &quot;Mapa&quot; ( class=&quot; lbl_mapa &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_mapa ) 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable las coordenadas anteriores ( coordenadas ) y haciendo un split la respectiva latitud &#160; y lonitud y las nuevos coordenadas registradas por el usuario ( map_input_nuevas_coordenadas ) con su respectivo split para guardar la nueva latitud ( map_input_nueva_latitud ) y la nueva longitud ( map_input_nueva_longitud ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; coordenadas =&#123;&#123; map_input_nuevas_coordenadas &#125;&#125;&amp; coordenadas =&#123;&#123; map_input_nuevas_coordenadas &#125;&#125;&amp; latitud =&#123;&#123; map_input_nueva_latitud &#125;&#125;&amp; longitud =&#123;&#123; map_input_nueva_longitud &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones (por actualizarse tres datos, se debern realizar tres registros en el historial)&#58; 
&#160; 
 Coordenadas&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= coordenadas &amp;eatc_doma_prev_value= &#123;&#123; coordenadas &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; map_input_nuevas_coordenadas &#125;&#125; 
&#160; 
 Latitud&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= latitud &amp;eatc_doma_prev_value= &#123;&#123; latitud &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; map_input_nueva_latitud &#125;&#125; 
&#160; 
 Longitud&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= longitud &amp;eatc_doma_prev_value= &#123;&#123; longitud &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; map_input_nueva_longitud &#125;&#125; 

&#160; 
 Departamento / Provincia / Estado 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_departamento_provincia_estado ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_departamento_provincia_estado ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= departamento 
&#160; 
 Tipo de campo de captura 
 Selector nico 
&#160; 
 De dnde toma los datos el selector 
 El selector debe funcionar de la misma manera a cmo se implement en el formulario de registro de beneficiarios ( Selector de &quot;Provincias, departamentos, estados&quot; y luego de &quot;Ciudades&quot; genrico segn el pas de la cuenta y validando informacin de los selectores con la coordenada previamente seleccionada ). 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el anterior departamento / provincia / estado ( departamento ) y el nuevo seleccionado por el usuario ( selector_nuevo_departamento ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; departamento =&#123;&#123; selector_nuevo_departamento &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= departamento &amp;eatc_doma_prev_value= &#123;&#123; departamento &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; selector_nuevo_departamento &#125;&#125; 

&#160; 
 Ciudad 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_ciudad ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ciudad ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= municipio 
&#160; 
 Tipo de campo de captura 
 Selector nico 
&#160; 
 De dnde toma los datos el selector 
 El selector debe funcionar de la misma manera a cmo se implement en el formulario de registro de beneficiarios ( Selector de &quot;Provincias, departamentos, estados&quot; y luego de &quot;Ciudades&quot; genrico segn el pas de la cuenta y validando informacin de los selectores con la coordenada previamente seleccionada ). 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable la anterior ciudad / municipio ( municipio ) y la nueva seleccionada por el usuario ( selector_nuevo_municipio ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; municipio =&#123;&#123; selector_nuevo_municipio &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= municipio &amp;eatc_doma_prev_value= &#123;&#123; municipio &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; selector_nuevo_municipio &#125;&#125; 

&#160; 
 Direccin 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_direccion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_direccion ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= unidad_territorial 
&#160; 
 Tipo de campo de captura 
 Text input 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable la anterior direccin ( direccion ) y la nueva registrada por el usuario ( text_input_nueva_direccion ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; unidad_territorial =&#123;&#123; text_input_nueva_direccion &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= unidad_territorial &amp;eatc_doma_prev_value= &#123;&#123; direccion &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; text_input_nueva_direccion &#125;&#125; 

&#160; 
 Telfono 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_telefono &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_telefono ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= telefono1 
&#160; 
 Tipo de campo de captura 
 Phone input 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el anterior telfono ( telefono ) y el nuevo registrado por el usuario ( phone_input_nuevo_telefono ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; telefono1 =&#123;&#123; phone_input_nuevo_telefono &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= telefono1 &amp;eatc_doma_prev_value= &#123;&#123; telefono &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; phone_input_nuevo_telefono &#125;&#125; 

&#160; 
 Telfono 2 
 Placeholder (que fluya como nombre del campo) 
 class=&quot; lbl_telefono2 &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_telefono2 ) 
&#160; 
 Valor por defecto 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= telefono2 
&#160; 
 Tipo de campo de captura 
 Phone input 
&#160; 
 Validaciones 
 No puede estar vaco 
&#160; 
 En caso de cambio a dnde se lleva el registro 
 El sistema deber guardar en una variable el anterior telfono ( telefono2 ) y el nuevo registrado por el usuario ( phone_input_nuevo_telefono2 ).&#160; De igual manera deber tomar un estampe de fecha ( datestamp ) y estampe de fecha y hora ( datetimestamp ) y tambin deber tomar el dato &quot; email &quot; contenido en la estructura &quot; bo_usuarios &quot; de la respectiva cuenta maestra (entorno beneficiarios&#58; ejemplo para ambiente de pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?nombre_usuario=logistica&amp;_distinct=email )&#160; y llevarlo&#160; &quot; eatc_bo_user &quot; para su registro. 
&#160; 
 Con la informacin recolectada debe realizar los siguientes registros&#58; 
&#160; 
 Informacin del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= update &amp; telefono2 =&#123;&#123; phone_input_nuevo_telefono2 &#125;&#125;&amp;WHEREidentificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 Historial de cambios de datos del gestor de donaciones&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_change_history &amp;_operacion= insert &amp; eatc_code= &#123;&#123; codigo_autogenerado &#125;&#125; &amp;eatc_date= &#123;&#123; datestamp &#125;&#125; &amp;eatc_datetime= &#123;&#123; datetimestamp &#125;&#125; &amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_doma_code = &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user= &#123;&#123; eatc_bo_user &#125;&#125;&amp; eatc_doma_parameter= telefono2 &amp;eatc_doma_prev_value= &#123;&#123; telefono2 &#125;&#125; &amp;eatc_doma_new_value= &#123;&#123; phone_input_nuevo_telefono2 &#125;&#125; 

 DOCUMENTOS 
 class=&quot; lbl_documentos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_documentos ) 
&#160; 
 El sistema desplegar un formulario que permitir consultar e incorporar nuevos documentos legales de la organizacin.&#160; Para la edicin o incorporacin de nuevos documentos, el sistema deber funcionar de manera enteramente similar (labels incluidos) a cmo funciona el registro de Beneficiarios ( &#123;&#123; URL_entorno_beneficarios &#125;&#125;/_registro/index.html?&#123;&#123;_DOM. cua_master &#125;&#125; ). 

 Para su consulta el desarrollo se debe basar en la implementacin inicial realizada en el BO Abaco Legacy, en dnde se realiza esta consulta de documentos (cmo se ve a continuacin). 

 Adicional a lo anterior, el sistema presentar la siguiente informacin (el sistema no permitir editarla)&#58; 
&#160; 
 Fecha de registro en EatCloud 
 class=&quot; lbl_fecha_registro_eatcloud &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_registro_eatcloud ) 
&#160; 
 Valor&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;_distinct= fecha1 
&#160; 
 Tipo de campo 
 Solamente informativo, no permitir edicin del campo. 

&#160; 
 Selector tipo de licencia [Pendiente para una etapa posterior] 
 Se presentar posteriormente un selector del tipo de licencia, el cual aun no se ha definido cmo se manejar. Por lo tanto en una primera etapa quedar pendiente su implementacin. 

 Grupos etarios registrados 
 class=&quot; lbl_grupos_etarios_registrados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_grupos_etarios_registrados ) 
&#160; 
 El sistema desplegar una tabla con los datos de los grupos etarios registrados por cada institucin beneficiaria&#160; de la siguiente manera&#58; 

 Total&#58; 
 Aunque el total es lo ltimo que se muestra, para efectos de la presente documentacin se documentar de primero, ya que este nmero tiene incidencia en los clculos posteriores de porcentaje que se presentan. 
 class=&quot; lbl_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_total ) 
&#160; 
 Valor&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende= &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;_cont 
&#160; 
 El sistema deber guardar en una variable el valor obtenido ( numero_total_beneficiarios_finales ) para utilizarlo en los clculos para generar la tabla de datos 
&#160; 
 Grupo 
 class=&quot; lbl_grupo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_grupo ) 
&#160; 
 Valores 
 Del siguiente listado 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_age_groups?_id=_*&amp;_distinct=age_group_label 
&#160; 
 Se coloca un &quot;label&quot; por fila. 
&#160; 
 Para cada &quot;valor de label&quot; se toma el respectivo cdigo &#123;&#123;eatc_age_groups. age_group_code &#125;&#125;, para con realizar con ese dato consultas posteriores 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_age_groups?_id=_*&amp;_distinct=age_group_code 

&#160; 
 Poblacin beneficiada&#58; 
 Aunque en la tabla de datos, segn el mockup propuesto, es la ltima columna, para efectos de la presente documentacin se documentar de primero, ya que este nmero tiene incidencia en los clculos posteriores de porcentajes. 
&#160; 
 class=&quot; lbl_poblacion_beneficiada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_poblacion_beneficiada ) 
&#160; 
 Valor&#160; 
 Por cada fila, se toma el respectivo cdigo del grupo etario &#123;&#123;eatc_age_groups. age_group_code &#125;&#125; para realizar el clculo de la cantidad de poblacin beneficiada. 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende= &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp; age_group_code= &#123;&#123;eatc_age_groups. age_group_code &#125;&#125; &amp;_cont 
&#160; 
 El sistema deber guardar en una variable el valor obtenido ( numero_beneficiarios_finales_&#123;&#123;eatc_age_groups. age_group_code &#125;&#125; ) para utilizarlo en los clculos de porcentaje. 

&#160; 
 % de poblacin beneficiada&#58; 
 Aunque en la tabla de datos, segn el mockup propuesto, es la ltima columna, para efectos de la presente documentacin se documentar de primero, ya que este nmero tiene incidencia en los clculos posteriores de porcentajes. 
&#160; 
 class=&quot; lbl_pct_poblacion_beneficiada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_pct_poblacion_beneficiada ) 
&#160; 
 Valor&#160; 
 Por cada fila, los valores del total de beneficiarios finales para cada grupo etario y se dividen por el nmero total de beneficiarios 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende= &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp; age_group_code= &#123;&#123;eatc_age_groups. age_group_code &#125;&#125; &amp;_cont 
&#160; 
pct_poblacion_beneficiada= ( numero_beneficiarios_finales_&#123;&#123;eatc_age_groups. age_group_code &#125;&#125;/numero_total_beneficiarios_finales ) *100 

&#160; 
 % mujeres&#58; 
 class=&quot; lbl_pct_mujeres_beneficiadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_pct_mujeres_beneficiadas ) 
&#160; 
 Valor&#160; 
 Por cada fila, los valores del total de beneficiarios finales para cada grupo etario, se debe determinar cuntos corresponden a &quot;Mujeres&quot; y se dividen por el nmero total de beneficiarios 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende= &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp; age_group_code= &#123;&#123;eatc_age_groups. age_group_code &#125;&#125; &amp; sexo= &#123;&#123; dato_encriptado_mujeres &#125;&#125; &amp;_cont 
&#160; 
pct_mujeres_beneficiadas= ( numero_beneficiarios_finales_mujeres_&#123;&#123;eatc_age_groups. age_group_code &#125;&#125;/numero_total_beneficiarios_finales ) *100 

&#160; 
 % hombres&#58; 
 class=&quot; lbl_pct_hombres_beneficiados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_pct_hombres_beneficiados ) 
&#160; 
 Valor&#160; 
 Por cada fila, los valores del total de beneficiarios finales para cada grupo etario, se debe determinar cuntos corresponden a &quot;Mujeres&quot; y se dividen por el nmero total de beneficiarios 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende= &#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp; age_group_code= &#123;&#123;eatc_age_groups. age_group_code &#125;&#125; &amp; sexo= &#123;&#123; dato_encriptado_hombres &#125;&#125; &amp;_cont 
&#160; 
pct_mujeres_beneficiadas= ( numero_beneficiarios_finales_hombres_&#123;&#123;eatc_age_groups. age_group_code &#125;&#125;/numero_total_beneficiarios_finales ) *100 

 CONDUCTORES AUTORIZADOS 
 class=&quot; lbl_conductores_autorizados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_conductores_autorizados ) 
&#160; 
 Llamado para obtener los datos de la tabla&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125; /crypt/ eatcloud /getcrypt?table= eatc_mv &amp;fieldname= eatc_doma_id &amp; fieldvalue= &#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125; &amp; fielddecrypt = uz,uzik,n0k,pa,pk 
&#160; 
 Nota para el desarrollador&#58; a la consulta sera importante enviarle tambin el dato de la cuenta maestra ( eatc_mv . cua_master con el nimo de evitar futuros duplicados) pero no se tiene claro si a esta funcin se le puede enviar otro parmetro desencriptado para la bsqueda 
&#160; 
 uz =transport_company; uzik =transport_company_id; n0k =name; pa =doc_id; pk =licence_plate;&#160; 
&#160; 
 El sistema desplegar una tabla con los datos de los conductores autorizados&#160; de la siguiente manera&#58; 

 Empresa logstica&#58; 
 Aunque el total es lo ltimo que se muestra, para efectos de la presente documentacin se documentar de primero, ya que este nmero tiene incidencia en los clculos posteriores de porcentaje que se presentan. 
&#160; 
 class=&quot; lbl_empresa_logistica &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_empresa_logistica ) 
&#160; 
 Valor&#160; 
 &#123;&#123;eatc_mv. uz &#125;&#125; 

&#160; 
 NIT 
 class=&quot; lbl_identificacion_tributaria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_identificacion_tributaria ) 
&#160; 
 Valor que se muestra 
 &#123;&#123;eatc_mv. uzik &#125;&#125; 

&#160; 
 Nombre&#58; 
 class=&quot; lbl_nombre &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_nombre )&#160; 
&#160; 
 Valor que se muestra 
 &#123;&#123;eatc_mv. n0k &#125;&#125; 

&#160; 
 Documento de identidad&#58; 
 class=&quot; lbl_doc_id &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_doc_id ) 
&#160; 
 Valor que se muestra 
 &#123;&#123;eatc_mv. pa &#125;&#125; 

&#160; 
 Celular&#58; =&gt; POR EL MOMENTO NO VA 
 class=&quot; lbl_celular &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_celular ) 
&#160; 
 Valor que se muestra 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; / 

&#160; 
 Correo electrnico&#58; =&gt; POR EL MOMENTO NO VA 
 class=&quot; lbl_correo_electronico &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_correo_electronico ) 
&#160; 
 Valor que se muestra 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; / 

&#160; 
 Placa vehculo&#58; 
 class=&quot; lbl_placa_vehiculo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_placa_vehiculo ) 
&#160; 
 Valor que se muestra 
 &#123;&#123;eatc_mv. pk &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 Nuevo BO CUA MASTER Beneficiarios 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Flistado-beneficiarios%2F2704265466-listado_beneficiarios.jpg&ow=742&oh=642, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Flistado-beneficiarios%2F2704265466-listado_beneficiarios.jpg&ow=742&oh=642 

 LISTADO BENEFICIARIOS FINALES