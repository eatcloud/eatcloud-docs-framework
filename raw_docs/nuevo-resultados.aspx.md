# nuevo-resultados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 (Indicadores del anterior eatc_pods_dsh) 

 Los indicadores que se mostaban anteriormente en el dashboard general de la Web App, pasarn a una pgina interna, cuyo diseo se presenta a continuacin 
&#160; 
 Diseo&#58; 
 http&#58;//repograf.eatcloud.info/resultados.html 

 Etiquetas principales de la vista 
&#160; 
 Resultados&#58; 
 class=&quot; lbl_resultados &quot; 
&#160; 
 Indicadores clave&#58; 
 class=&quot; lbl_indicadores_clave &quot; 
&#160; 
 Top 10 referencias que ms donan (en el diseo&#58; Referencias donadas) 
 id =&quot; lbl_top_10_referencias_donadas &quot; 

 Selector de fechas (difiere de lo establecido en el diseo par conservar el selector previamente implementado) 
&#160; 
 Se debe presentar un selector de fecha inicial y final para la consulta de los indicadores, cuyo valor por defecto es del 1 del mes actual a la fecha actual (tal como est en el BO de donantes) y que contenga la siguiente leyenda&#58; 
&#160; 
 La informacin que se visualiza en los indicadores corresponde a los datos en la fecha seleccionada. Si deseas consultar fechas diferentes por favor vara la fecha inicial y la fecha final 

 La informacin que se visualiza corresponde a los datos en la fecha seleccionada. 
 clase =&quot; lbl_info_visualiza_fechas &quot; 
&#160; 
 Si deseas consultar fechas diferentes por favor vara la fecha inicial y la fecha final 
 clase =&quot; lbl_consultar_otras_fechas &quot; 
&#160; 
 Fecha inicial&#58; 
 id =&quot; lbl_fecha_inicial &quot; 
&#160; 
 Fecha final&#58; 
 id =&quot; lbl_fecha_final &quot; 
&#160; 
 Botn&#58; Cargar nueva informacion&#58; 
 id =&quot; lbl_cargar_nueva_info &quot; 

 Card de indicador&#58; 

 Diseo simplificado &#58; 
 &#160; El principal cambio es que la ficha tcnica no aparecer como una leyenda en la card del indicador, sino como un tooltip que aparece cuando se da clic al icono del signo de interrogacin encerrado en un crculo 
&#160; 
 Se mantiene el mecanismo para ocultar estos indicadores 
 Tal cual se implement originalmente (agregando una clase o id de funcionalidad que podr ocultarse desde una funcionalidad administrativa) 

 Los indicadores a continuacin descritos, correspondern al rango de fechas seleccionado y mostrarn solo los datos del punto de donacin ( eatc_pod ) desde el cual se accedi a la web app de donantes. 

&#160; 
 *****NUEVO****&#58; dinamizar las consultas necesarias para mostrar las estadsticas a partir de la cuenta maestra. 
 Cuando se ingrese a un BO, el sistema debe consultar la cuenta maestra de dicha cuenta, y a partir de dicho valor realizar las consultas necesarias para traer la informacin y los KPIs que se muestra en el dashboard. 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; =&gt; eatc_cua_master 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona_kpi?&#123;&#123;parametro_consulta&#125;&#125;=&#123;&#123;VALOR&#125;&#125; 
&#160; 
 NOTA &#58; como no se tiene informacin de los mecanismos con los cuales se consultan los KPIs y la informacin que se despliega en el dashboard de del BO, se realiza esta documentacin de manera general, por lo tanto el desarrollador deber realizar las abstracciones necesarias a partir de la misma para realizar la implementacin que lo que busca es permitir la evolucin del sistema a uno donde se manejen mltiples cuentas maestras. 

 Monto donado&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; id=&quot; lbl_monto_donado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_monto_donado ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_monto_donando_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_monto_donando_desc ) 

 ***NUEVO*** KG anunciados&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; clase=&quot; lbl_kg_anunciados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_kg_anunciados ) 
&#160; 
 Tooltip&#58; clase=&quot; lbl_kg_anunciados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_kg_anunciados_desc ) 
&#160; 
 Corresponde a la sumatoria de los KG_originales de todos los anuncios generados por el punto de donacin. 

 KG aprovechados&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; clase=&quot; lbl_kg_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_kg_aprovechados ) 
&#160; 
 Tooltip&#58; clase=&quot; lbl_kg_aprovechados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_kg_aprovechados_desc &#160; ) 

 Huella de carbono mitigada (en el diseo&#58; Huella de carbono; anteriormente&#58; Impacto ambiental ) 
 Label&#58; class=&quot; lbl_huella_carbono &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_huella_carbono ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_impacto_ambiental_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_impacto_ambiental_desc ) 

 Nmero de anuncios&#58; 
 Label&#58; id=&quot; lbl_numero_anuncios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_numero_anuncios ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_numero_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_numero_anuncios_desc ) 

 Referencias donadas&#58; 
 &#160; No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; id=&quot; lbl_referencias_donadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_referencias_donadas ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_referencias_donadas_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_referencias_donadas_desc ) 

 Platos servidos&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; id=&quot; lbl_platos_servidos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_platos_servidos ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_platos_servidos_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_platos_servidos_desc ) 

 Nuevo&#58; Numero de anuncios cancelados 
 Label&#58; class=&quot; lbl_numero_anuncios_cancelados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_numero_anuncios_cancelados ) 
&#160; 
 Tooltip&#58; class=&quot; lbl_numero_anuncios_cancelados_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_numero_anuncios_cancelados_desc ) 

 Porcentaje de cancelados (segn nmero de anuncios)&#58; 
 &#160; No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; id=&quot; lbl_porcentaje_cancelados_num &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_num ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_porcentaje_cancelados_num_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_num_desc ) 

 Porcentaje de kilogramos cancelados&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; clase=&quot; lbl_porcentaje_cancelados_kg &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_kg ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_porcentaje_cancelados_kg_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_kg_desc ) 

 Porcentaje de cancelados (segn valor de las donaciones)&#58; 
 No est incorporada en el nuevo diseo 
&#160; 
 Label&#58; id=&quot; lbl_porcentaje_cancelados_valor &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_valor ) 
&#160; 
 Tooltip&#58; id=&quot; lbl_porcentaje_cancelados_valor_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_porcentaje_cancelados_valor_desc ) 

 ***Nuevo&#58; Productos ms donados *** 
 Label&#58; class=&quot; lbl_productos_mas_donados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_productos_mas_donados )&#160; 

 NOTA PARA EL DESARROLLO &#58;&#160; los planteamientos de esta funcionalidad se basaron en la funcionalidad de&#160; Datagov Cuentas &quot; Eficiencia &gt; Tablero &gt; Resultados por referencia de producto &quot;, por lo tanto su implementacin podr basarse en ella. 

 El sistema mostrar una tabla con los productos ms donados.&#160; La cantidad de productos ms donados se mostrar de la siguiente manera&#58; 
&#160; 
 Top 5 
 Label&#58; class=&quot; lbl_top_5 &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_top_5 )&#160; 
&#160; 
 Solo se le mostrarn los 5 productos ms donados (en KG por producto) a las cuentas cuyo tipo ( eatc_cua. type ) sea &quot; free &quot; para el periodo de tiempo seleccionado 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type=free 
&#160; 
 Top 20 
 Label&#58; class=&quot; lbl_top_20 &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_top_20 )&#160;&#160; 
&#160; 
 Solo se le mostrarn los 20 productos ms donados (en KG por producto) a las cuentas cuyo tipo ( eatc_cua. type ) sea &quot; esencial &quot; para el periodo de tiempo seleccionado 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= esencial 
&#160; 
 Todos los productos 
 Para las licencias ( eatc_cua. type ) activo e impacto se mostrarn todos los productos donados en el respectivo periodo de tiempo seleccionado 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= activo,impacto 
&#160; 

&#160; 
 Tabla de productos ms donados =&gt; debe mostrar informacin de anuncios con estados &quot;despachado&quot;,&#160; &quot;recibido&quot;, &quot;pre-certificado&quot; y &quot;certificado&quot; (las consultas indicativas y ejemplos abajo definidos no tienen en cuenta lo anterior y hay que incorporarlo) 
 Se presentar una tabla, paginada, de los productos ms donados por KG despachados (los valores de la tabla se agruparn por cdigo de producto), mostrando primero los productos ms donados por KG despachados , en donde se incorporar la siguiente informacin. 

&#160; 
 Cdigo del producto 
 class=&quot; lbl_codigo_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_codigo_producto )&#160; 
&#160; 
 Corresponde al distinct sobre el campo &quot; eatc-odd_id &quot; de la tabla &quot; eatc_dona &quot; para el periodo de tiempo seleccionado . 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ?eatc-date_time_2[0]=&#123;&#123; fecha_inicial &#125;&#125;&amp;eatc-date_time_2[1]=2&#123;&#123; fecha_final &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp; eatc_donor =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc -odd_id&#160; 
&#160; 
 Ejemplo&#58; entorno de pruebas, exito, eatc-pod_id=39, 7 y 8 de junio de 2021 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&amp;eatc-date_time_2[1]=2021-06-08&amp;eatc-pod_id=39&amp;eatc_donor=exito&amp;_distinct=eatc-odd_id &#160; 
&#160; 
 Entonces el sistema arroja la siguiente respuesta&#58; 
 &#123; ts &#58; &quot;220216153738&quot; , op &#58; true , cont &#58; 5 , res &#58;[&#123; eatc-odd_id &#58; &quot;1274311&quot; &#125;,&#123; eatc-odd_id &#58; &quot;0021991&quot; &#125;,&#123; eatc-odd_id &#58; &quot;0614335&quot; &#125;,&#123; eatc-odd_id &#58; &quot;0523968&quot; &#125;,&#123; eatc-odd_id &#58; &quot;1414326&quot; &#125;], mem &#58; 0.44 , time &#58; &quot;00&#58;00&#58;01&quot; &#125; 
&#160; 
 Para cada cdigo obtenido ( eatc-odd_id ) con la anterior consulta, el sistema deber realizar la siguiente consulta, con el nimo de mostrar la dems informacin de la tabla 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ?eatc-date_time_2[0]=&#123;&#123; fecha_inicial &#125;&#125;&amp;eatc-date_time_2[1]=2&#123;&#123; fecha_final &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp; eatc_donor =&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc -odd_id =&#123;&#123;eatc-odd_id&#125;&#125;&amp;_cmp= eatc -odd_id, eatc-odd_name,eatc-odd_total_weight_kg 
&#160; 
 Siguiendo con el ejemplo anterior, para uno de los items la consulta sera la siguiente&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-date_time_2[0]=2021-06-07&amp;eatc-date_time_2[1]=2021-06-08&amp;eatc-pod_id=39&amp;eatc_donor=exito&amp; eatc-odd_id =1274311,0021991,0614335,0523968,1414326&amp;_cmp= eatc -odd_id,eatc-odd_name,eatc-odd_total_weight_kg &#160; 
&#160; 
 Nombre del producto (en el diseo est en primer orden pero debe estar de segundo)&#160; 
 class=&quot; lbl_nombre_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_nombre_producto ) 
 Corresponde al nombre asignado a cada uno de los cdigos anteriormente definidos (puede asimilarse al distinct sobre el campo &quot; eatc-odd_name &quot; de la tabla &quot; eatc_dona &quot; para el periodo de tiempo seleccionado ). 

&#160; 
 Kilogramos despachados 
 class=&quot; lbl_kg_despachados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_kg_despachados )&#160; 
 Corresponde a la sumatoria de los Kilogramos Totales ( eatc-odd_total_weight_kg de los anuncios con estados,&#160; &quot;delivered&quot;, &quot;received&quot;, &quot;pre-certified&quot;, &quot;certified&quot;, para el periodo de tiempo seleccionado 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-resultados%2F969443836-EmbeddedImage--31-.jpg&ow=1280&oh=210, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-resultados%2F969443836-EmbeddedImage--31-.jpg&ow=1280&oh=210 
 EATCLOUD DONANTES 

 223.000000000000 

 NUEVO: RESULTADOS