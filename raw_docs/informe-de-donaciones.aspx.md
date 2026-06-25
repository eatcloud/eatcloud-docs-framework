# informe-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación&#58;&#160; 
 en esta implementación se deben utilizar de raíz (es decir, desde su implementación inicial) en vez de los textos que se presentan a continuación, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementación de base sea internacionalizada. 

 ID Funcionalidad 
 consulta_datagov_cua ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= consulta_datagov_cua ) 
&#160; 
 Label Botón Menú ( más información )&#58; 
 id=&quot;lb_btn_consulta_datagov_cua&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_consulta_datagov_cua ) 
&#160; 
 Label Título de la Vista&#58; 
 id=&quot;lb_consulta_datagov_cua&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_consulta_datagov_cua ) 
&#160; 
 Label Descripción de la Vista&#58; 
 class=&quot;lb_consulta_tus_resultados_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_consulta_tus_resultados_desc ) 

 Mockup propuesto 
 Nos han propuesto este mockup (no se debe prestar mucha atención a la definición del menú lateral, ya que la misma se está armonizando en la respectiva documentació) para la funcionalidad.&#160; Se puede tener como base la misma funcionalidad de &quot; Resultados &quot; propuesta para la nueva WAPP, pero en este caso las consultas no se realizarán por punto de donación sino por cuenta, para obtener los datos de toda la cuenta.&#160; 

 El gráfico (que en el diseño está como un gráfico de barras) debe mostrar el comportamiento en el tiempo (diario) de cada uno de los KPIs que se encuentran en la línea principal de cards (ver imagen siguiente). El usuario podrá presionar cada una de las cards, para mostrar el gráfico de tendencia particular de dicho KPI (A excepción del caso en donde se ha solicitado estadísticas del día actual&#58; en este caso no se genera gráfico).&#160; 

 Se trabajarán entonces con estos 4 KPIs básicos ya implementados en &quot; Resultados &quot; (a excepción del KPI de CO2) 

 El filtro del informe trabajará de igual manera a como trabaja en el informe que se tomará como base y que fue desarrollado para la nueva WAPP 

 El listado de productos funcionará de manera similar al informe ya implementado 

 Descripción técnica&#58; 
 Se toman todos los labels implementados en &quot; Resultados de la nueva WAPP &quot; 

 Subtítulo&#58; 
 class=&quot; lbl_indicadores_clave &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_indicadores_clave ) 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hoy ) 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 

 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_personalizar ) 
&#160; 
 ***NUEVO &#58; Este filtro debe aparecer, pero si la licencia rescate es &quot;free&quot;, al accionarlo no debe abrir el selector de fecha inicial y final, sino que debe redireccionar a página de upgrade *** 
 Actualmente la opción de filtro &quot;personalizar&quot; se ocultó, permitiendo solamente la opción &quot;mes actual&quot;.&#160; La idea es reactivar la opción, pero el sistema debe evaluar mediante la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= type 
&#160; 
 La respuesta corresponde a eatc_cua. type = free caso en el cual en vez de presentarle las opciones de seleccionar las fechas inicial o final, se debe redireccionar a la página de upgrade por configuración de fechas . 
&#160; 
 Si la respuesta a la anterior consulta da como resultado 
eatc_cua. type = esencial ó eatc_cua. type = activo &#160; ó eatc_cua. type = impacto se permitirá configurar las fechas del informe mediante la funcionalidad que se define adelante . 

&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial ) 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 

 Monto donado 
 class=&quot; lbl_monto_donado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_monto_donado ) 
&#160; 
 class=&quot; lbl_monto_donado_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_monto_donado_desc ) 
&#160; 
 Kilogramos entregados 
 class=&quot; lbl_kg_entregados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados ) 
&#160; 
 class=&quot; lbl_kg_entregados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_entregados_desc ) 
&#160; 
 Número de anuncios realizados 
 class=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios ) 
&#160; 
 class=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_numero_anuncios_desc ) 
&#160; 
 Anuncios cancelados 
 class=&quot; lbl_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados ) 
&#160; 
 class=&quot; lbl_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_anuncios_cancelados_desc &#160; ) 

 Top 10 referencias que más donan 
 class=&quot; lbl_top_10_referencias_donadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_top_10_referencias_donadas ) 
&#160; 
 Código de producto 
 class=&quot; lbl_codigo_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_codigo_producto ) 
&#160; 
 Nombre de producto 
 class=&quot; lbl_nombre_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_nombre_producto ) 
&#160; 
 Cantidad 
 class=&quot; lbl_cantidad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_cantidad ) 

 ***NUEVO INDICADOR&#58; POBLACIÓN ATENDIDA *** 
 class=&quot; lbl_poblacion_atendida &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_poblacion_atendida )&#160; 

 tooltip class=&quot; lbl_poblacion_atendida_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_poblacion_atendida_desc )&#160; 
&#160; 
 &quot;Corresponde a la población que se está atendiendo con las donaciones entregadas a través de la Asociación Nacional de Bancos de Alimentos (ABACO) y su red de Bancos y Organizaciones Sociales. Para realizar el cálculo nos apoyamos en la metodología y los datos maestros proporcionados por ABACO. El indicador se calcula el primer día con los datos del mes inmediatamente anterior.&quot; 

 Se presentará a parte como un&#160; indicador que tiene un selector de fechas particulares (selector de meses) y que podrá aparecer o no para la cuenta en cuestión, si hay o no datos calculados. 
&#160; 
 Si no se obtienen resultados en la siguiente consulta, el sistema no mostrará el indicador (debería esconder todo el &quot;DIV&quot; correspondiente) 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_registro_poblacion_atendida_cua? eatc_cua_user= &#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont 

 &quot;Selecciona el mes&quot; Selector de meses 
 class=&quot; lbl_selecciona_mes &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_poblacion_atendida )&#160; 
&#160; 
 Valor por defecto&#58; 
 Mes inmediatamente anterior. 
&#160; 
 Demás valores del selector&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_registro_poblacion_atendida_cua? eatc_cua_user= &#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_mes_kpi 
&#160; 
 El usuario podrá seleccionar un mes diferente, al valor por defecto ( mes_seleccionado ) para realizar la consulta. 

&#160; 
 Valor del KPI 
 Con la selección del mes, el sistema realiza la siguiente consulta para presentar el indicador 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_registro_poblacion_atendida_cua? eatc_cua_user= &#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc_mes_kpi = &#123;&#123; mes_seleccionado &#125;&#125;&amp;_cmp= poblacion_atendida 

 ***nuevo &#58; informe de encabezado de donaciones ***&#160; 
 =&gt; Debe funcionar con los filtros de fechas documentados anteriormente 

 Nota importante para el desarrollo &#58; el presente informe deberá basarse en la implementación realizada para el BO Donantes legacy y que en su momento se denominó &quot;Informe Operativo &gt; Anuncios&quot;.&#160; También se basa en la implementación del &quot; Informe de detalles de anuncios &quot; (labels e información propia del encabezado del anuncio).&#160; Por lo tanto la documentación de esta funcionalidad se basó en la que en su momento se definió, incorporando labels para su internacionalización.&#160; Este solamente implementará la pestaña &quot;Encabezado&quot; y los filtros de fecha operarán según lo definido anteriormente ( personalización solo para licencias pagas ). 

 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados del anuncio de donación ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donación con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o “programado” , (&#123;&#123;estados&#125;&#125;) es decir, en la lista se deben mostrar los anuncios que aun están en el almacén y están pendientes de ser entregados &#123;. 
&#160; 
 Consulta de anuncios 
 El sistema debe tomar la cuenta maestra, y los filtros de fechas, establecidos al inicio del informe , de la cuenta respectiva para realizar la consulta de los anuncios que le corresponden&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state=&#123;&#123;estados&#125;&#125;&amp; eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;_cmp= eatc-code,eatc-publication_date,.eatc-publication_datetime,eatc-state,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-city,eatc-province, consolidation_origin, eatc-original_weight_kg,eatc-total_weight_kg, eatc-donation_manager_name,eatc-donation_manager_adress,eatc-donation_manager_phone,eatc-adjudication_datetime,eatc-programed_picking_datetime,eatc-picking_checkin_datetime, eatc_code_verification_datetime, eatc-picking_checkout_datetime,eatc-receipt_datetime, eatc_constancy_datetime, eatc-pre_certification_datetime,eatc-certification_datetime, eatc-donor_code, eatc-doc,eatc-warning 
&#160; 
 Tabla de encabezados de anuncio de donación 
 Se debe mostrar en una datatable que permita ordenar por columnas, realizar búsquedas y descargar información (en formato .csv), la siguiente información 
&#160; 
 Código del anuncio 
 Label &#58; class=&quot;lbl_codigo_anuncio&quot;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_codigo_anuncio 
 Orden&#58; 1ra columna 
 La información se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Fecha 
 Label &#58; class=&quot; lbl_fecha &quot; 
 Orden&#58; 2da columna 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date 
&#160; 
 Fecha y hora 
 Label &#58; class=&quot; lbl_fecha_hora &quot; 
 Orden&#58; 3ra columna 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Mes 
 Label &#58; class=&quot; lbl_mes &quot; 
 Orden&#58; 4ta columna 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date (trayendo el mes) 
&#160; 
 Estado 
 Label &#58; class=&quot; lbl_estado &quot; 
 Orden&#58; 5 ta columna 
 La información se toma de&#58; eatc_dona_headers .eatc-state 

&#160; 
 ***NUEVO&#58; &#160; Causal no entrega *** 
 Label &#58; class=&quot; lbl_causal_not_delivered &quot; 

 La información se toma de&#58;&#160; eatc_dona_headers . eatc_not_delivery_cause 
&#160; 
 Tipo creación 
 Label &#58; class=&quot; lbl_tipo_creacion &quot; 
 Orden&#58; 5.5 columna 
 La información se toma de&#58; eatc_dona_headers .eatc-code con las siguientes pruebas lógicas&#58; 
 Si el código del anuncio (eatc_dona_headers .eatc-code ) es propio del cliente (no empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lógica &quot;y&quot;) el código del producto (eatc_dona .eatc-odd_id ) no es alfanumérico (es decir no fue creado manualmente dado que cuando esto ocurre los códigos del producto son alfanuméricos)&#160; se debe colocar &quot;automatica&quot; (es decir los anuncios que vienen de interfaz o integración).&#160; De otra manera (Els)e se debe colocar &quot;manual&quot; 
 Si el código del anuncio (eatc_dona_headers .eatc-code ) es del sistema (empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lógica &quot;y&quot;) el código del producto (eatc_dona .eatc-odd_id ) es alfanumérico (es decir fue creado manualmente dado que cuando esto ocurre los códigos del producto son alfanuméricos)&#160; se debe colocar &quot;manual&quot; (es decir los anuncios que vienen de interfaz o integración).&#160; De otra manera (Els)e se debe colocar &quot;automatica&quot; 
&#160; 
 Se debe evaluar si solo haciendo la prueba lógica sobre&#160; eatc_dona_headers .eatc-code se logrará atender la necesidad planteada con las pruebas lógicas arriba propuestas 
&#160; 
 Código Punto de donación 
 Label &#58; class=&quot; lbl_codigo_punto_donacion &quot; 
 Orden&#58; 6ta columna 
 La información se toma de&#58; eatc_dona .eatc-pod_id 
&#160; 
 Punto de donación 
 Label &#58; class=&quot; lbl_pod &quot; 
 Orden&#58; 7ma columna 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Dirección punto de donación 
 Label &#58; class=&quot; lbl_direccion_pod &quot; 
 Orden&#58; 8ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_address 
&#160; 
 Ciudad 
 Label &#58; class=&quot; lbl_ciudad &quot; 
 Orden&#58; 9na columna 
 La información se toma de&#58; eatc_dona_headers .eatc-city 
&#160; 
 Departamento 
 Label &#58; class=&quot; lbl_departamento_provincia_estado &quot; 
 Orden&#58; 10ma columna 
 La información se toma de&#58; eatc_dona_headers .eatc-province 
&#160; 
 Anuncio Origen 
 Label &#58; class=&quot; lbl_anuncio_origen &quot; 
 Orden&#58; 11ava columna 
 La información se toma de&#58; eatc_dona_headers . eatc_consolidation_origin 
&#160; 
 KG Originales 
 Label &#58; class=&quot; kg_originales &quot; 
 Orden&#58; 12ava columna 
 La información se toma de&#58; eatc_dona_headers . eatc-original_weight_kg 
&#160; 
 KG aprovechados 
 Label &#58; class=&quot; lbl_kg_aprovechados &quot; 
 Orden&#58; 13ava columna 
 La información se toma de&#58; eatc_dona_headers . eatc-total_weight_kg 
&#160; 
 Beneficiario 
 Label &#58; class=&quot; lbl_beneficiario &quot; 
 Orden&#58; 14ava&#160; columna 
 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Beneficiario dirección 
 Label &#58; class=&quot; lbl_direccion_beneficiario &quot; 
 Orden&#58; 15ava&#160; columna 
 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_adress 
&#160; 
 Beneficiario teléfono 
 Label &#58; class=&quot; lbl_telefono_beneficiario &quot; 
 Orden&#58; 16ava&#160; columna 
 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_phone 
&#160; 
 Fecha de adjudicación 
 Label &#58; class=&quot; lbl_hora_adjudicacion &quot; 
 Orden&#58; 17ava&#160; columna 
 La información se toma de&#58; eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Fecha programada 
 Label &#58; class=&quot; lbl_hora_entrega_programada &quot; 
 Orden&#58; 18ava&#160; columna 
 La información se toma de&#58; eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Fecha entrada 
 Label &#58; class=&quot; lbl_hora_entrega_real_llegada &quot; 
 Orden&#58; 19ava&#160; columna 
 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Fecha verificación de código de recogida 
 Label &#58; class=&quot; lbl_fecha_verificacion_codigo &quot; 
 Orden&#58; 20ava&#160; columna 
 La información se toma de&#58; eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Fecha salida 
 Label &#58; class=&quot; lbl_hora_entrega_real_salida &quot; 
 Orden&#58; 21ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Fecha recepción 
 Label &#58; class=&quot; lbl_hora_recepcion &quot; 
 Orden&#58; 22ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime 
&#160; 
 Fecha constancia 
 Label &#58; class=&quot; lbl_fecha_constancia &quot; 
 Orden&#58; 23ava columna 
 La información se toma de&#58; eatc_dona_headers . eatc_constancy_datetime 
&#160; 
 Fecha pre-certificación 
 Label &#58; class=&quot; lbl_hora_precertificacion &quot; 
 Orden&#58; 24ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-pre_certification_datetime 
&#160; 
 Fecha Certificación 
 Label &#58; class=&quot; lbl_fecha_certificacion &quot; 
 Orden&#58; 25 ava columna 
&#160; 
 Doc ID donante 
 Label &#58; class=&quot; lbl_doc_id_donante &quot; 
 Orden&#58; 26ava columna 
 La información se toma de&#58; eatc_dona_headers . eatc-donor_code 
&#160; 
 Doc 
 Label &#58; class=&quot; lbl_documento_soporte &quot; 
 Orden&#58; 27ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-doc 
&#160; 
 Warning 
 Label &#58; class=&quot; lbl_alerta &quot; 
 Orden&#58; 28ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-warning 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finforme-de-donaciones%2F35982524-top_10_productos.jpg&ow=1137&oh=507, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finforme-de-donaciones%2F35982524-top_10_productos.jpg&ow=1137&oh=507 
 Cuentas datagov 

 327.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 355307bf-0407-4775-a8c3-7bdaa476fd96 
 3!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 a05f9ac2-7135-46c6-8866-31ac544cb3ee 
 2025-12-24T03:11:11.6240254Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"7f647959-d0b3-4aed-a33e-7ff5fbbcf4b8","SequenceId":27,"FluidContainerCustomId":"47363f22-a812-49b6-b21f-5301a2c5ccc2","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 INFORMES DE DONACIONES