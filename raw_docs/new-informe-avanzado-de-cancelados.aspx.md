# new-informe-avanzado-de-cancelados.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo&#58; El presente informe tendrá dos sabores&#58;&#160; El primero, será un informe estadístico, mensual, cuyas cifras se presentarán en un arreglo por punto de donación (cada fila representará estadísticas con respecto a los cancelados, de un punto de donación en particular, para cada uno de los meses que componen el periodo de tiempo que se consulta), de acuerdo a filtros aplicados. 
 El segundo sabor del informe será uno comparativo&#160; y cuya comparación será con el mes homólogo del año anterior, determinando porcentaje de variación positiva o negativa. 
&#160; 
 La siguiente imagen, muestra una idea general de cómo se construye la tabla del informe, aunque en la especificación se agregarán algunas columnas adicionales para representar de manera más exacta los filtros (en particular se adiciona una columna de ciudades). &#160;El informe muestra datos por meses (que serán títulos de columnas). En cada casilla de intersección entre el mes y el punto de donación se presentará una estadística (Por el momento se establecen 5 estadísticas diferentes sobre cancelados, que se mostrarán en el informe) 

 Filtro de fechas 
&#160; 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_fecha_inicial ) 
&#160; 
 Valor por defecto&#58; el primer día del mes, tres meses más atrás contados a partir del primer día del mes actual). 
&#160; 
 Valor más antiguo permitido (inicialmente)&#58; primer día del mes del mes anterior pero del año anterior (es decir por el momento el informe solamente podrá cubrir 12 meses calendario. 
&#160; 
 El valor seleccionado se llevará a la variable &#123;&#123;fecha_inicial&#125;&#125; 
&#160; 
 Validaciones&#58; no permitirá una fecha más próxima que el primer día del mes del mes anterior, dado que el informe como mínimo deberá presentar información de un mes. &#160;Solamente permitirá seleccionar primeros días del mes (1 del mes, no se podrán seleccionar fechas diferentes al primer día del mes en el selector de fecha inicial. El valor debe ser anterior que la fecha final (un mes anterior &#160;por lo menos) 
&#160; 
&#160; 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_fecha_final ) 
&#160; 
 Valor por defecto&#58; Último día del mes anterior (es decir el informe solamente presentará información de mes vencido). Posteriormente podrá presentar información parcial del mes en curso, así es que cuando se implemente ese caso, el valor por defecto será el día actual). 
&#160; 
 El valor seleccionado se llevará a la variable &#123;&#123;fecha_final&#125;&#125; 
&#160; 
 Validaciones&#58; no permitirá una fecha más antigua que el último día del mes anterior del año anterior, dado que el informe como mínimo deberá presentar información de un mes. &#160;Solamente permitirá seleccionar últimos días del mes (28, 29, 30, 31 del mes (según sea el caso), no se podrán seleccionar fechas diferentes al último día del mes en el selector de fecha final. El valor debe ser posterior que la fecha inicial (un mes posterior por lo menos) 
&#160; 
 Filtro por cuentas (selector múltiple, con opción &quot;Todas&quot;) 
 Seleccionar cuenta&#58; 
 class=&quot; lbl_selector_cuenta &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_selector_cuenta &#160; &#160; 
&#160; 
 Con la selección anterior de fechas, el sistema deberá realizar la siguiente consulta 
&#160; 
 Consulta de las cuentas que tuvieron donaciones canceladas en las fechas establecidas (para armar el selector múltiple)&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ? eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;eatc-state= cancelled &amp;_distinct= eatc-donor 
&#160; 
 Si no se obtienen resultados en la consulta , se muestra el toast &quot;No se obtubieron resultados &quot;&#160; class=&quot; lbl_toast_sin_resultados &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_toast_sin_resultados &#160; 

&#160; 
 Con las respuestas, el sistema arma un selector múltiple que permitirá seleccionar una, varias o todas las ciudades presentes en el selector.&#160; Una vez el usuario realice su selección, con ella el sistema arma un &#123;&#123; array_de_donantes &#125;&#125; que utiliza para la siguiente consulta&#58; 

&#160; 
 Filtro por departamentos (selector múltiple, con opción &quot;Todas&quot;) 
 Departamento - provincia - estado&#58; 
 class=&quot; lbl_departamento_provincia_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_departamento_provincia_estado ) 
&#160; 
 Con la selección anterior de fechas y el &#123;&#123; array_de_donantes &#125;&#125; , el sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 Consulta de los departamentos (provincias, estados) en donde hay donaciones canceladas para los donantes seleccionados (para armar el selector)&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_dona_headers ? eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;eatc-donor= &#123;&#123; array_de_donantes &#125;&#125; &amp;eatc-state= cancelled &amp;_distinct= eatc-province 
&#160; 
 Si no se obtienen resultados en la consulta , se muestra el toast &quot;No se obtubieron resultados &quot;&#160; class=&quot; lbl_toast_sin_resultados &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_toast_sin_resultados &#160; 

&#160; 
 Con las respuestas, el sistema arma un selector múltiple que permitirá seleccionar una, varias o todas las ciudades presentes en el selector.&#160; Una vez el usuario realice su selección, con ella el sistema arma un &#123;&#123; array_de_dptos &#125;&#125; que utiliza para la siguiente consulta&#58; 

&#160; 
 Filtro por ciudades (selector múltiple, con opción &quot;Todas&quot;) 
 Seleccionar ciudad&#58; 
 class=&quot; lbl_selector_ciudad &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_selector_ciudad &#160; 
&#160; 
 Con la selección anterior de fechas, el &#123;&#123; array_de_donantes &#125;&#125; , y el &#123;&#123; array_de_dptos &#125;&#125; el sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 Consulta de las ciudades en donde hay donaciones eliminadas para los donantes seleccionados (para armar el selector)&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_deleted_dona_header ? eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;eatc-donor= &#123;&#123; array_de_donantes &#125;&#125; &amp; eatc-province= &#123;&#123; array_de_dptos &#125;&#125; &amp;eatc-state= cancelled &amp;_distinct= eatc-city 
&#160; 
 Si no se obtienen resultados en la consulta , se muestra el toast &quot;No se obtubieron resultados &quot;&#160; class=&quot; lbl_toast_sin_resultados &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_toast_sin_resultados &#160; 

&#160; 
 Con las respuestas, el sistema arma un selector múltiple que permitirá seleccionar una, varias o todas las ciudades presentes en el selector.&#160; Una vez el usuario realice su selección, con ella el sistema arma un &#123;&#123; array_de_ciudades &#125;&#125; que utiliza para la siguiente consulta&#58; 

&#160; 
 Consulta de anuncios cancelados 
 Consulta de PODs con anuncios cancelados 
 Con las fechas seleccionadas en el primer selector y las ciudades seleccionadas en el segundo, el sistema realiza la siguiente consulta para traer los datos&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?&amp; eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125;&amp;eatc-donor= &#123;&#123; array_de_donantes &#125;&#125; &amp; eatc-province= &#123;&#123; array_de_dptos &#125;&#125; &amp; eatc-city= &#123;&#123; array_de_ciudades &#125;&#125; &amp;eatc-state= cancelled &amp;_cmp= eatc-code, eatc-pod_id , eatc-pod_name ,eatc-publication_date, eatc-total_weight_kg , eatc-total_cost,eatc_dona_references,eatc_dona_units &#160; 
&#160; 
 Con estos puntos de donación, organizados por Cuentas, Departamentos, ciudades, en las filas de la tabla, se armará la misma para presentar la información estadística de Cancelados, que podrá ser de varios tipos&#58; &#160;Número de anuncios cancelados, Porcentaje en cantidad de anuncios cancelados,&#160; 
&#160; 
&#160; 
Selector de tipo de estadística a visualizar 
El informe de podrá presentar información de 5 tipos (con su respectivo porcentaje), por lo tanto el sistema deberá presentar un selector único con estos valores. 
&#160; 
 Anuncios cancelados ( clase=&quot; lbl_anuncios_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_cancelados )) 
 KG Cancelados ( clase=&quot; lbl_kg_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_cancelados )&#160; ) 
 Valor al costo de anuncios cancelados ( lbl_valor_al_costo_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_cancelados )&#160; ) 
 Referencias canceladas ( clase=&quot; lbl_referencias_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_referencias_canceladas ) ) 
 Unidades Canceladas ( clase=&quot; lbl_unidades_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_unidades_canceladas )&#160; ) 
&#160; 
Una vez se seleccione el tipo de indicador, se pintará este como el título de la tabla , y se presentará entre paréntesis el porcentaje y su tooltip 
&#160; 
&#123;&#123;lbl_indicador&#125;&#125; ( &#123;&#123;lbl_porcentaje_indicador&#125;&#125;&#58; &#160; &#123;&#123;lbl_tooltip_porcentaje_indicador&#125;&#125; ) 
&#160; 
A continuación los respectivos labels que se utilizarán para armar los títulos del informe según la selección del usuario&#58; 
&#160; 
&#160; 
Anuncios cancelados 
 clase=&quot; lbl_anuncios_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_cancelados )&#160; 
&#160; 
Porcentaje de anuncios cancelados 
 clase=&quot; lbl_pct_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_anuncios_cancelados ) 
&#160; 
Tooltip =&gt; Corresponde a la división del número de anuncios efectivamente cancelados (es decir, con estado &quot;cancelado&quot;) sobre el número total de anuncios (todos los anuncios) generados en el periodo. 
 clase=&quot; lbl_pct_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_anuncios_cancelados_desc )&#160; 

&#160; 
 kg cancelados 
 clase=&quot; lbl_kg_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg_cancelados )&#160; 
&#160; 
&#160; 
% de kilogramos cancelados 
 clase=&quot; lbl_pct_kg_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kg_cancelados )&#160; 
&#160; 
Tooltip =&gt; Corresponde al peso total de los anuncios cancelados sobre el peso total de anuncios realizados en el periodo 
 clase=&quot; lbl_pct_kg_cancelados_desc &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_kg_cancelados_desc) 
&#160; 
 Valor al costo anuncios cancelados 
 clase=&quot; lbl_valor_al_costo_cancelados ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo_cancelados )&#160; 

&#160; 
% de cancelados en valor al costo 
 clase=&quot; lbl_pct_valor_al_costo_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_valor_al_costo_cancelados )&#160; 
&#160; 
Tooltip =&gt; Corresponde al valor al costo de los anuncios cancelados sobre el valor al costo de los anuncios realizados en el periodo 
 clase=&quot; lbl_pct_valor_al_costo_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_valor_al_costo_cancelados_desc )&#160; 
&#160; 
 Referencias canceladas 
 clase=&quot; lbl_referencias_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_referencias_canceladas ) 

&#160; 
Porcentaje referencias canceladas =&gt; % de referencias canceladas 
 clase=&quot; lbl_pct_referencias_canceladas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_referencias_canceladas )&#160; 
&#160; 
Tooltip =&gt; Corresponde al número de referencias canceladas sobre el número total de referencias anunciadas en el periodo 
 clase=&quot; lbl_pct_referencias_canceladas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_referencias_canceladas_desc )&#160; 
&#160; 
 Unidades canceladas 
 clase=&quot; lbl_unidades_canceladas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_unidades_canceladas )&#160; 

&#160; 
% de unidades de producto canceladas 
 clase=&quot; lbl_pct_unidades_canceladas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pct_unidades_canceladas )&#160; 
&#160; 
Tooltip =&gt; Corresponde al número de unidades de producto canceladas sobre el número total de unidades de producto anunciadas en el periodo 
 clase=&quot; lbl_pct_unidades_canceladas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=llbl_pct_unidades_canceladas_desc )&#160; 
&#160; 
&#160; 
&#160; 
El informe presentará en cada casilla (intersección de un mes (columna) con una fila (punto de donación) el valor del indicador y entre paréntesis el porcentaje 
&#160; 
&#123;&#123;valor_indicador&#125;&#125; ( &#123;&#123;porcentaje_indicador&#125;&#125; ) 

&#160; 
&#160; 
&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-avanzado-de-cancelados%2F3045484810-imagen_info_av_cancelados.png&ow=1280&oh=297, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-avanzado-de-cancelados%2F3045484810-imagen_info_av_cancelados.png&ow=1280&oh=297 

 734.000000000000 

 NEW: INFORME AVANZADO DE CANCELADOS