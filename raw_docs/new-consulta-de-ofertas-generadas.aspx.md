# new-consulta-de-ofertas-generadas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 EatCloud Donantes&#58; basado en Seguimiento de anuncios (eatc_dona_lst) &#58; se puede utilizar la misma plantilla de diseo 

 Esta funcionalidad, similar al Seguimiento de anuncio servir para que los oferentes puedan consultar las ofertas ( eatc_sale ) que van generando (mediante la funcionalidad de Creacin de Venta de ltimo Minuto ) y poder ir monitoreando el comportamiento de las mismas.&#160; En la especificacin se establece una franja superior de indicadores que se implementar en una segunda etapa, por lo tanto&#160; 

 Franja de indicadores de ofertas (puede implementarse en una segunda etapa) 
 En la parte superior de la vista se deben mostrar indicadores, teniendo en cuenta las disposiciones que se hicieron con respecto a este tipo de visualizaciones aqu , sobre todo en lo concerniente al filtro principal y a la card de inidicador o KPI . 
&#160; 
 Los KPIs a visualizar son los siguientes&#58; 
&#160; 
 Valor total de las ofertas 
 (?) Tooltip 
 Valor total de las ofertas generadas por periodo de tiempo 
&#160; 
 Cmo se calcula 
 Es la sumatoria de la multiplicacin de los parmetro eatc_sale. eatc-odd_original_quantity por (*)&#160; eatc_sale. eatc-odd_min_sale_unit_price de las ofertas realizadas por el punto de despacho ( eatc_sale. eatc-pod_id ) en el periodo de tiempo definido 
&#160; 
&#160; 
 Valor total de las ofertas adquiridas 
 (?) Tooltip 
 Valor total de las ofertas que han sido adquiridas por el pblico en el periodo de tiempo seleccionado 
&#160; 
 Cmo se calcula 
 Es la sumatoria de la multiplicacin siguiente multiplicacin&#58; 
 &#160;( eatc_sale. eatc-odd_original_quantity &#160; - eatc_sale. eatc-odd_quantity ) * eatc_sale. eatc-odd_min_sale_unit_price &#160; 
 de las ofertas realizadas por el punto de despacho ( eatc_sale. eatc-pod_id ) en el periodo de tiempo definido. 

&#160; 
 Efectividad comercial de las ofertas 
 (?) Tooltip 
 Porcentaje de las ofertas que han sido adquiridas por el pblico en general 
&#160; 
 Cmo se calcula 
 Partiendo de los dos clculos anteriores se calcula de la siguiente manera 
Valor total de las ofertas adquiridas / Valor total de las ofertas 

 Lista de ofertas creadas 
 En esta lista se mostrarn las ofertas (eatc-sale) que han sido creadas en el punto de venta particular&#160; ( eatc_sale. eatc-pod_id ) en la semana en curso 

 Filtro por defecto de la lista 
 En su vista por defecto se deben presentar las ofertas de los ltimos tres das. El sistema debe permitir ampliar la fecha de consulta para traer ofertas de semanas anteriores al listado 
&#160; 
 Consulta de ofertas 
 El sistema toma el parmetro &quot; eatc-id &quot; del punto de despacho ( eatc_pods ) respectivo y con este dato se efecta la consulta para traer las ofertas del da actual y los dos das anteriores&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id= &#123;&#123;eatc-id&#125;&#125; &amp;eatc-date_time_2 =&#123;&#123;dia_actual,dia_anterior,dia_trasanterior&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO SAN ANTONIO&quot;, cuyo &quot; eatc-id &quot; = 39 consulta en ambiente de pruebas el da 2020-08-04 de la siguiente manera 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info//api/eatcloud/eatc_sale?eatc-pod_id= 39 &amp; eatc-date_time_2= 2020-08-04,2020-08-03,2020-08-02 &#160; para mostrar la informacin por defecto (filtro por defecto) 
&#160; 
 y esta consulta, para mostrar toda la informacin&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info//api/eatcloud/eatc_sale?eatc-pod_id= 39 &#160;&#160; 

 Filtro por fechas 
 El sistema debe permitir seleccionar una fecha inicial y final para traer las ofertas cuya eatc-date_time_2 se encuentre en dicho rango de fechas. 
&#160; 
 Filtro eatc-odd_state 
 Los filtros deben realizar llamados al API, para traer ofertas con diferentes estados de las ofertas, por lo tanto el sistema debe presentar un selector con los diferentes estados de la oferta (entre parntesis se muestra como debe ser invocado el estado= 
 Ofertado ( sale ) 
 Parcialmente pedido u ordenado ( partially_orderer ) 
 Totalmente pedidas u ordenadas ( ordered ) 
 Saldado ( balance ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id= &#123;&#123;eatc-id&#125;&#125; &amp;eatc-odd_state=&#123;&#123;estado_seleccionado&#125;&#125; 

&#160; 
 Ejemplo (ambiente de pruebas)&#58; 
 El usuario &quot;EXITO SAN ANTONIO&quot;, cuyo &quot; eatc-id &quot;&quot;= 39 ( eatc-pod_id ) , desea consultar las ofertas cuyo estado sea &quot;totalmente pedidas&quot; (eatc-odd_state=ordered)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale?eatc-pod_id= 39 &amp;eatc-odd_state= ordered &#160; 

 Card de la oferta (eatc_sale) 

 El informe debe ser construido en tiempo real para mostrar la fotografa de las ofertas en el momento que se&#160; carga el informe.&#160; Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
 Cada&#160; oferta ( eatc_sale ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 
&#160; 
 Fecha y hora de la oferta&#58; 
 &#160;eatc_sale. eatc-date_time 
&#160; 
 Vigente hasta 
 &#160;eatc_sale. eatc-offer_lifetime_until 
&#160; 
 Artculo - producto 
 &#160;eatc_sale. eatc-odd_name 
&#160; 
 Descripcin 
 &#160;eatc_sale. eatc-odd_description 
&#160; 
 Cantidad ofertada 
 &#160;eatc_sale. eatc-odd_original_quantity 
&#160; 
 Cantidad disponible 
 &#160;eatc_sale. eatc-odd_quantity 
&#160; 
 Cantidad Vendida 
 eatc_sale. eatc-odd_original_quantity - eatc_sale. eatc-odd_quantity 
&#160; 
 Estado del la orden 
 &#160;eatc_sale. eatc-odd_state 
&#160; 
 Alerta 
 &#160;eatc_sale. eatc-warning 

 Botn&#58; ver ms&#160; 
 Al oprimir este botn, se debe mostrar toda la informacin de la eatc_sale.&#160; Con posterioridad se determinar si de acuerdo al estado ser necesario habilitar edicin de campos para la orden. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-ofertas-generadas%2F2972198678-6-seguimiento-anuncios--eatc_dona_lst---1-.png&ow=375&oh=2866, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-ofertas-generadas%2F2972198678-6-seguimiento-anuncios--eatc_dona_lst---1-.png&ow=375&oh=2866 
 NUEVA WAPP 

 CONSULTA DE OFERTAS CREADAS (EAT_SALE_LST)