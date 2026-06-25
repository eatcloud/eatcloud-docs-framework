# donaciones-en-curso.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Donaciones en curso 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el informe, incluyendo su título)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 Título del informe 
 Label&#58; class=&quot; lbl_donaciones_en_curso &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_donaciones_en_curso )&#160; 

 Filtro de fechas 
 Nota para el desarrollo&#58; este filtro debe funcionar como en anteriores implementaciones, preservando su valor así se navegue por varios informes de esta misma sección ( Generalidades , Detalle de anuncios cancelados ). 
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

 KPIS PRINCIPALES 

 Anuncios programados 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_anuncios_programados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_programados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_anuncios_programados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_)programados_desc &#160;&#160; 
&#160; 
 &quot; Corresponde al conteo de los anuncios, del periodo seleccionado, que han sido programados (es decir, cuyo estado es &quot;programado&quot;) &quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state=scheduled&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 
&#160; 
 El resultado entregado en &quot;count&quot; corresponderá al KPI en cuestión. 

&#160; 
 Anuncios despachados 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_anuncios_despachados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_despachados &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_anuncios_despachados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_despachados_desc &#160;&#160;&#160; 
&#160; 
 &quot; Corresponde al conteo de los anuncios, del periodo seleccionado, que han sido despachados (es decir, cuyo estado es &quot;despachado&quot;) &quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= delivered &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 
&#160; 
 El resultado entregado en &quot; count &quot; corresponderá al KPI en cuestión. 

&#160; 
 Anuncios por verificar 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
&#160; 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_anuncios_por_verificar &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_por_verificar &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_anuncios_por_verificar_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_por_verificar_desc &#160; &#160; 
&#160; 
 &quot; Corresponde al conteo de los anuncios, del periodo seleccionado, a los cuales las instituciones beneficiarias no le han realizado la verificación detallada de los productos del anuncio &quot; 
&#160; 
 Llamado para el cálculo&#58;&#160; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado (para determinar los anuncios que no tienen una fecha y hora válida de recepción registrada)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-receipt_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp;eatc-state= scheduled , delivered&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 
&#160; 
 El resultado entregado en &quot;count&quot; corresponderá al KPI en cuestión. 

&#160; 
 Anuncios sin códigos de recogida 
&#160; 
 ***NUEVO &#58; Filtro (a quienes se le muestra el indicador)&#58; *** 
 A los todos los usuarios. 
&#160; 
 class=&quot; lbl_anuncios_sin_cod_recogida &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_sin_cod_recogida &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_anuncios_sin_cod_recogida_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_anuncios_sin_cod_recogida_desc &#160; 
&#160; 
 &quot; Corresponde al conteo de los anuncios, del periodo seleccionado, a los cuales el punto de donación no les ha realizado el proceso de verificación del código de recepción, que debe entregar el recolector para recibir la donación &quot; 
&#160; 
 Llamado para el cálculo&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado (para determinar los anuncios que no tienen una fecha y hora válida de recepción registrada)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc_code_verification_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp;eatc-state= scheduled , delivered&amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 
&#160; 
 El resultado entregado en &quot; count &quot; corresponderá al KPI en cuestión. 

 LISTADO DE ANUNCIOS DE DONACIÓN EN CURSO 

 Filtro principal 
 class=&quot; lbl_estado_dona &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_estado_dona &#160;&#160; 
&#160; 
 class=&quot; lbl_buscar &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_buscar &#160; 
 ***NUEVO&#58; Filtro por donante (cua_user) *** 
El sistema deberá generar un filtro por “donante” presentando un selector múltiple, con la opción de “´Todos los donantes”(opción por defecto) que se construya con las opciones que se generan con la siguiente consulta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= announced,awarded,scheduled,delivered &amp;_distinct= eatc-donor 
Si el usuario selecciona la opción “Todos los donantes” o no selecciona ningún donante, se entenderá que el funcionamiento del informe será como el que hasta ahora se tiene (sin la presencia de ese filtro). 
Si el usuario selecciona uno o múltiples donantes, el sistema incorporará a los llamados que se documentan a continuación el siguiente parámetro para la búsqueda 
 eatc-donor=&#123;&#123;array_donors&#125;&#125; 
 Programado ***NUEVO &#58; parámetro eatc-donor=&#123;&#123;array_donors&#125;&#125; si se selecciona una o múltiples cuentas *** 
 class=&quot; lbl_programado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabl=lbl_programado &#160; &#160; 
&#160; 
 Llamado para la construcción de la tabla&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-state= scheduled &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X)&#125;&#125; &amp; eatc-donor=&#123;&#123;array_donors&#125;&#125; &amp;_cmp=eatc-donation_manager_name,eatc-donation_manager_phone,eatc-donation_manager_typology_a,eatc-donation_manager_typology_b,eatc-state,eatc_code_verification_datetime,eatc-receipt_datetime 

&#160; 
 &#123;&#123;estados_segun_filtro&#125;&#125;=scheduled 

&#160; 
 Despachado ***NUEVO &#58; parámetro eatc-donor=&#123;&#123;array_donors&#125;&#125; si se selecciona una o múltiples cuentas *** 
 class=&quot; lbl_despachado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_despachado &#160; &#160; 
&#160; 
 Llamado para la construcción de la tabla&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-state= delivered &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X)&#125;&#125; &amp; eatc-donor=&#123;&#123;array_donors&#125;&#125; &amp;_cmp=eatc-donation_manager_name,eatc-donation_manager_phone,eatc-donation_manager_typology_a,eatc-donation_manager_typology_b,eatc-state,eatc_code_verification_datetime,eatc-receipt_datetime 

&#160; 
 &#123;&#123;estados_segun_filtro&#125;&#125;=delivered 

&#160; 
 Todos los anuncios en curso (anunciados, adjudicados, programados, despachados) ***NUEVO &#58; parámetro eatc-donor=&#123;&#123;array_donors&#125;&#125; si se selecciona una o múltiples cuentas *** 
 class=&quot; lbl_todos_los_anuncios_en_curso &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_todos_los_anuncios_en_curso &#160; &#160; 
&#160; 
 Llamado para la construcción de la tabla&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
&#160; 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial_periodo&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final_periodo&#125;&#125;&amp;eatc-state= announced,awarded,scheduled,delivered &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X)&#125;&#125; &amp; eatc-donor=&#123;&#123;array_donors&#125;&#125; &amp;_cmp=eatc-donation_manager_name,eatc-donation_manager_phone,eatc-donation_manager_typology_a,eatc-donation_manager_typology_b,eatc-state,eatc_code_verification_datetime,eatc-receipt_datetime 

&#160; 
 &#123;&#123;estados_segun_filtro&#125;&#125;=announced,awarded,scheduled,delivered 

&#160; 
 TABLA DE DATOS 
 El sistema deberá presentar una tabla ordenable según sus columnas, con filtros de información, paginada y con posibilidades de descarga (datatable), que contenga la siguiente información&#58; 

&#160; 
 Nombre institución beneficiaria&#58; ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 class=&quot; lbl_nombre_doma &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_nombre_doma &#160;&#160;&#160; 
&#160; 
 Para llenar todos los datos de esta columna el sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= &#123;&#123;estados_segun_filtro&#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_distinct =eatc-donation_manager_name 

&#160; 
 El sistema presenta el dato&#58; 
 eatc_dona_headers. eatc-donation_manager_name 

&#160; 
 # de donaciones (en el diseño&#58; cantidad de donaciones) ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación)&#160; 
&#160; 
 class=&quot; lbl_numero_donaciones &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_numero_donaciones &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Para cada gestor de donaciones se realiza la siguiente consulta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= &#123;&#123;estados_segun_filtro&#125;&#125; &amp; eatc-donation_manager_name= &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125; &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 
&#160; 
 El valor del &quot;count&quot; será llevado como el dato de la respectiva columna. 

&#160; 
 Donaciones pend. verificación (beneficiario) ***NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 class=&quot; lbl_donaciones_pend_verificacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donaciones_pend_verificacion &#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Para cada gestor de donaciones se realiza la siguiente consulta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= &#123;&#123;estados_segun_filtro&#125;&#125; &amp; eatc-donation_manager_name= &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc-receipt_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 

&#160; 
 NOTA&#58; Se debe evaluar si cuando se seleccionan &quot;TODOS LOS ANUNCIOS&quot; se deben incorporar datos de donaciones &quot;Anunciadas&quot;, que no tiene mucho sentido que se se contabilicen como pendientes de código de recogida (y de cierta manera entran en conflicto con la definición del indicador general) 
&#160; 
 El valor del &quot;count&quot; será llevado como el dato de la respectiva columna. 

&#160; 
 Donaciones pend. cod. recolección (donantes) **NUEVO&#58; filtro diferenciado por tipo de organización&#58; *** 
 Según sea el tipo de organización determinada en el proceso de login , se aplicará un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de información y por lo tanto para ellos el BO funciona tal como funciona en su primera implementación) 
&#160; 
 class=&quot; lbl_donaciones_pend_cod_rec &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donaciones_pend_cod_rec &#160;&#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Para cada gestor de donaciones se realiza la siguiente consulta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= &#123;&#123;estados_segun_filtro&#125;&#125; &amp; eatc-donation_manager_name= &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc_code_verification_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cont 

&#160; 
 NOTA&#58; Se debe evaluar si cuando se seleccionan &quot;TODOS LOS ANUNCIOS&quot; se deben incorporar datos de donaciones &quot;Anunciadas&quot;, que no tiene mucho sentido que se se contabilicen como pendientes de código de recogida (y de cierta manera entran en conflicto con la definición del indicador general) 
&#160; 
 El valor del &quot;count&quot; será llevado como el dato de la respectiva columna. 
&#160; 
 ***NUEVO&#58; vínculo en la cifra que abre una tabla con información básica de las donaciones *** 
 Al hacer click en la cifra el sistema deberá realizar el siguiente llamado (igual que el llamado anterior, que hace el conteo pero cambiando el parámetro &amp;_cont por un &amp;_cmp que trae datos específicos)&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-state= &#123;&#123;estados_segun_filtro&#125;&#125; &amp; eatc-donation_manager_name= &#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125;&amp; eatc_code_verification_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp; &#123;&#123;filtro_eatc_dona_headers (tipo_X) &#125;&#125; &amp;_cmp=eatc-code,eatc-publication_date, eatc-verification_code ,eatc-total_weight_kg,eatc-total_cost,eatc-state 
&#160; 
 El sistema desplegará una tabla paginada, con un buscador general (que permita buscar por cualquier campo de la misma), que contendrá las siguientes columnas&#58; 
&#160; 
 Código ( class=&quot; lbl_codigo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_codigo )&#58; presenta la información contenida en eatc_dona_headers. eatc-code 
 Fecha publicación ( class=&quot; lbl_fecha_publicacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_fecha_publicacion )&#58; presenta la información contenida en eatc_dona_headers. eatc-publication_date 
 Código recogida ( class=&quot; lbl_codigo_recogida &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_codigo_recogida )&#58; presenta la información contenida en eatc_dona_headers. eatc-verification_code 
 Peso total donación ( class=&quot; lbl_peso_total_donacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_peso_total_donacion )&#58; presenta la información contenida en eatc_dona_headers. eatc-total_weight_kg 
 Costo total donación ( class=&quot; lbl_costo_total_donacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_costo_total_donacion )&#58; presenta la información contenida en eatc_dona_headers. eatc-total_cost 
 Estado ( class=&quot; lbl_estado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_estado )&#58; presenta la información contenida en eatc_dona_headers. eatc-state 

&#160; 
 Teléfono 
 class=&quot; lbl_telefono &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_telefono &#160;&#160;&#160;&#160; 
&#160; 
 El sistema presenta el dato&#58; 
 eatc_dona_headers. eatc-donation_manager_phone 

&#160; 
 Tipo 
 class=&quot; lbl_tipo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_tipo &#160;&#160;&#160;&#160;&#160; 
 El sistema presenta el dato&#58; 
 eatc_dona_headers. eatc-donation_manager_typology_a,eatc-donation_manager_typology_b 

 Estado del anuncio =&gt; NO VA 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonaciones-en-curso%281%29%2F3463671087-donaciones_en_curso_lst.jpg&ow=1280&oh=487, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonaciones-en-curso%281%29%2F3463671087-donaciones_en_curso_lst.jpg&ow=1280&oh=487 
 Nuevo BO CUA MASTER Beneficiarios 

 717.000000000000 

 DONACIONES EN CURSO