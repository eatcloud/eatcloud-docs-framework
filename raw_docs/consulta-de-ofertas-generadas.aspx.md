# consulta-de-ofertas-generadas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 EatCloud Donantes: basado en Seguimiento de anuncios (eatc_dona_lst) : se puede utilizar la misma plantilla de diseo 

 Esta funcionalidad, similar al Seguimiento de anuncio servir para que los oferentes puedan consultar las ofertas ( eatc_sale ) que van generando (mediante la funcionalidad de Creacin de Venta de ltimo Minuto ) y poder ir monitoreando el comportamiento de las mismas.  En la especificacin se establece una franja superior de indicadores que se implementar en una segunda etapa, por lo tanto  

 Franja de indicadores de ofertas (puede implementarse en una segunda etapa) 
 En la parte superior de la vista se deben mostrar indicadores, teniendo en cuenta las disposiciones que se hicieron con respecto a este tipo de visualizaciones aqu , sobre todo en lo concerniente al filtro principal y a la card de inidicador o KPI . 

 Los KPIs a visualizar son los siguientes: 

 Valor total de las ofertas 
 (?) Tooltip 
 Valor total de las ofertas generadas por periodo de tiempo 

 Cmo se calcula 
 Es la sumatoria de la multiplicacin de los parmetro eatc_sale. eatc-odd_original_quantity por (*)  eatc_sale. eatc-odd_min_sale_unit_price de las ofertas realizadas por el punto de despacho ( eatc_sale. eatc-pod_id ) en el periodo de tiempo definido 

 Valor total de las ofertas adquiridas 
 (?) Tooltip 
 Valor total de las ofertas que han sido adquiridas por el pblico en el periodo de tiempo seleccionado 

 Cmo se calcula 
 Es la sumatoria de la multiplicacin siguiente multiplicacin: 
  ( eatc_sale. eatc-odd_original_quantity   - eatc_sale. eatc-odd_quantity ) * eatc_sale. eatc-odd_min_sale_unit_price   
 de las ofertas realizadas por el punto de despacho ( eatc_sale. eatc-pod_id ) en el periodo de tiempo definido. 

 Efectividad comercial de las ofertas 
 (?) Tooltip 
 Porcentaje de las ofertas que han sido adquiridas por el pblico en general 

 Cmo se calcula 
 Partiendo de los dos clculos anteriores se calcula de la siguiente manera 
Valor total de las ofertas adquiridas / Valor total de las ofertas 

 Lista de ofertas creadas 
 En esta lista se mostrarn las ofertas (eatc-sale) que han sido creadas en el punto de venta particular  ( eatc_sale. eatc-pod_id ) en la semana en curso 

 Filtro por defecto de la lista 
 En su vista por defecto se deben presentar las ofertas de los ltimos tres das. El sistema debe permitir ampliar la fecha de consulta para traer ofertas de semanas anteriores al listado 

 Consulta de ofertas 
 El sistema toma el parmetro " eatc-id " del punto de despacho ( eatc_pods ) respectivo y con este dato se efecta la consulta para traer las ofertas del da actual y los dos das anteriores: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale?eatc-pod_id= {{eatc-id}} &eatc-date_time_2 ={{dia_actual,dia_anterior,dia_trasanterior}} 

 Ejemplo: 
 El usuario "EXITO SAN ANTONIO", cuyo " eatc-id " = 39 consulta en ambiente de pruebas el da 2020-08-04 de la siguiente manera 

 Ambiente de pruebas: https://devdonantes.eatcloud.info//api/eatcloud/eatc_sale?eatc-pod_id= 39 & eatc-date_time_2= 2020-08-04,2020-08-03,2020-08-02   para mostrar la informacin por defecto (filtro por defecto) 

 y esta consulta, para mostrar toda la informacin: 

 https://devdonantes.eatcloud.info//api/eatcloud/eatc_sale?eatc-pod_id= 39    

 Filtro por fechas 
 El sistema debe permitir seleccionar una fecha inicial y final para traer las ofertas cuya eatc-date_time_2 se encuentre en dicho rango de fechas. 

 Filtro eatc-odd_state 
 Los filtros deben realizar llamados al API, para traer ofertas con diferentes estados de las ofertas, por lo tanto el sistema debe presentar un selector con los diferentes estados de la oferta (entre parntesis se muestra como debe ser invocado el estado= 
 Ofertado ( sale ) 
 Parcialmente pedido u ordenado ( partially_orderer ) 
 Totalmente pedidas u ordenadas ( ordered ) 
 Saldado ( balance ) 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale?eatc-pod_id= {{eatc-id}} &eatc-odd_state={{estado_seleccionado}} 

 Ejemplo (ambiente de pruebas): 
 El usuario "EXITO SAN ANTONIO", cuyo " eatc-id ""= 39 ( eatc-pod_id ) , desea consultar las ofertas cuyo estado sea "totalmente pedidas" (eatc-odd_state=ordered): 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale?eatc-pod_id= 39 &eatc-odd_state= ordered   

 Card de la oferta (eatc_sale) 

 El informe debe ser construido en tiempo real para mostrar la fotografa de las ofertas en el momento que se  carga el informe.  Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.  
 Cada  oferta ( eatc_sale ) se presenta en una tarjeta que contiene la siguiente informacin: 

 Fecha y hora de la oferta: 
  eatc_sale. eatc-date_time 

 Vigente hasta 
  eatc_sale. eatc-offer_lifetime_until 

 Artculo - producto 
  eatc_sale. eatc-odd_name 

 Descripcin 
  eatc_sale. eatc-odd_description 

 Cantidad ofertada 
  eatc_sale. eatc-odd_original_quantity 

 Cantidad disponible 
  eatc_sale. eatc-odd_quantity 

 Cantidad Vendida 
 eatc_sale. eatc-odd_original_quantity - eatc_sale. eatc-odd_quantity 

 Estado del la orden 
  eatc_sale. eatc-odd_state 

 Alerta 
  eatc_sale. eatc-warning 

 Botn: ver ms  
 Al oprimir este botn, se debe mostrar toda la informacin de la eatc_sale.  Con posterioridad se determinar si de acuerdo al estado ser necesario habilitar edicin de campos para la orden. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-ofertas-generadas%2F2972198678-6-seguimiento-anuncios--eatc_dona_lst---1-.png&ow=375&oh=2866, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-ofertas-generadas%2F2972198678-6-seguimiento-anuncios--eatc_dona_lst---1-.png&ow=375&oh=2866 

 144.000000000000 

 CONSULTA DE OFERTAS GENERADAS