# Informe-de-calificaciones-a-puntos-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación&#58;&#160; 
 Se implementa este informe como una mejora que permitirá a los donantes y a los puntos de donación ver cómo son calificados inicialmente cualitativamente (con tags de calificación, que se almacenan aquí ) para posteriormente pensar en las calificaciones cuantitativas (que se encuentran aquí , pero en una etapa posterior). 
&#160; 
 Para el correcto funcionamiento de las consultas requeridas para este informe, se debe revisar la implementación del “ Error Handler eatc_cua_origin en eatc_pod_tag_registry a partir de información registrada en eatc_dona_headers ”. 

&#160;Este informe deberá estar disponible a nivel general en el BO de donantes (en donde se podrá consultar información de todos los puntos de donación), y en la WAPP (en donde cada punto podrá consultar sus calificaciones). 
&#160; 
Dado que el informe debe representar la incidencia de cada uno de los “tags” de calificación para el punto en cuestión, se deberá desarrollar una manera para presentar el porcentaje que representa cada tag dentro del total de tags de calificación recibidos, de tal manera que haya manera también de visualizar esta estadística de manera gráfica. 
&#160; 
Dada esta condición del informe se recomienda evaluar la posibilidad de implementar el informe tipo tabla dinámica, que permita jugar con diversas visualizaciones de esta información. &#160;También revisar la posibilidad de presentar la información de manera gráfica (sobre todo si se selecciona o corresponde a la información de un solo POD, como sería el caso de la funcionalidad para la WAPP&#58; presentar los porcentajes como una torta o un diagrama de barras (el que más convenga de acuerdo al criterio del desarrollador). 
&#160; 
Por último, todos los labels de este informe se deberán internacionalizar con el estándar que se viene utilizando para ello (por esa razón no se entregan lables “legacy” para la construcción del mismo). 

 Titulo de la vista&#58; Informe de calificaciones cualitativas para los puntos de donación 
 Descripción del informe 
En este informe podrás ver cómo están calificando los gestores de donaciones (organizaciones beneficiarias) a tus diversos puntos de donación, con respecto a la operación de rescate humanitario de alimentos a través de las plataformas EatCloud. 
&#160; 
 Filtro de fechas 
El sistema presentará campos de captura para obtener la fecha inicial y final 
 Fecha inicial 
Tipo&#58; date 
Input&#58; &#123;&#123;fecha_inicial&#125;&#125; 
Validación&#58; campo requerido. &#160;Debe ser inferior a la fecha final 
 Fecha final 
Tipo&#58; date 
Input&#58; &#123;&#123;fecha_final&#125;&#125; 
Validación&#58; campo requerido. &#160;Debe ser superior a la fecha final 
&#160; 
 Botón consultar Consultar 
 Al oprimir el botón el sistema realiza la siguiente consulta 

&#160; 
Consulta de información en la tabla eatc_pod_tag_registry 
El sistema deberá realizar una serie de consultas para generar una tabla de estadísticas por punto de donación 
&#160; 
PODs calificados en el periodo seleccionado 
El sistema realizará la siguiente consulta para establecer los pods que fueron calificados en el periodo seleccionado 
 &#123;&#123;URL_donantes&#125;&#125; /api/abaco/ eatc_pod_tag_registry ?eatc_cua_origin=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;_distinct=pod_id 
 Nota&#58; cuando el usuario es del BO donante &#123;&#123;eatc_pod_id&#125;&#125; = _* 
Para cada uno de los pods obtenidos, se realizarán las siguientes consultas con miras a construir información estadística. 
Porcentaje de calificaciones positivas y negativas 
El sistema deberá contar el total de calificaciones cuantitativas que recibió cada uno de los puntos que arroja la anterior consulta&#58; 
 &#123;&#123;total_calificaciones&#125;&#125; = &#123;&#123;URL_donantes&#125;&#125;/api/abaco/ eatc_pod_tag_registry ?eatc_cua_origin=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;_cont 
y contar también el número de calificaciones positivas &#58; 
 &#123;&#123;total_calificaciones_positivas&#125;&#125; &#160;= &#123;&#123;URL_donantes&#125;&#125; /api/abaco/ eatc_pod_tag_registry ?eatc_cua_origin=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;type= positiva &amp;_cont 
y negativas recibidas por cada punto&#58; 
 &#123;&#123;total_calificaciones_negativas&#125;&#125; &#160;=&#160; &#123;&#123;URL_donantes&#125;&#125; /api/abaco/ eatc_pod_tag_registry ?eatc_cua_origin=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;type= negativa &amp;_cont 
Porcentaje de tags 
El sistema deberá contar los diferentes tags que están disponibles en la plataforma, que se obtienen de la siguiente consulta&#58; 
 &#123;&#123;tags&#125;&#125; &#160;= &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_calification_tags ?sujeto_calificacion= pods &amp;_cmp= tag 
Cuantas veces obtuvo el punto en cuestión la respectiva calificación, iterando, para cada uno de los tags de la anterior consulta, la siguiente consulta 
 &#123;&#123;total_calificaciones_por_tag&#125;&#125; &#160;=&#160; &#123;&#123;URL_donantes&#125;&#125; /api/abaco/ eatc_pod_tag_registry ?eatc_cua_origin=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;tag= &#123;&#123;tags&#125;&#125; &amp;_cont 
&#160; 
 Tabla de información de calificaciones&#58; 
 Filtro por pod&#58; selección múltiple (para perfil BO Donantes) 
 Con la siguiente consulta el informe debe construir un filtro de selección múltiple, con opción de “todos los pods” que permita filtrar por&#160; 
&#160; 
 Información a mostrar en la tabla de información 
 Se debe mostrar la información del detalle de cada donación acompañada de cierta información de encabezado 
&#160; 
 ID Punto de donación 
Los registros se obtendrán a partir de la consulta de los pods con calificaciones en el periodo , y se obtendrán del dato &#123;&#123; eatc_pod_tag_registry .pod_id&#125;&#125; 

&#160; 
 % calificaciones positivas 
 Para el punto del respectivo registro y a partir de las consultas para construir la información estadística , el sistema presentará el dato que se obtiene al realizar la siguiente división (y multiplicarla por 100 para obtener el porcentaje) 
 &#123;&#123;total_calificaciones_positivas&#125;&#125; / &#123;&#123;total_calificaciones&#125;&#125; &#160;* 100 
 &#160; 
 % calificaciones negativas 
 Para el punto del respectivo registro y a partir de las consultas para construir la información estadística , el sistema presentará el dato que se obtiene al realizar la siguiente división (y multiplicarla por 100 para obtener el porcentaje) 
 &#123;&#123;total_calificaciones_negativas&#125;&#125; / &#123;&#123;total_calificaciones&#125;&#125; &#160;* 100 
&#160; 

&#160; 
 Columnas por Tag calificado 
 Para cada uno de los tags que se utilizan en la plataforma y que se consultaron anteriormente , el sistema construirá una columna&#160; 
&#160; 
 % &#123;&#123;tag&#125;&#125; 
Contendrá el porcentaje de ocurrencia del respectivo tag en el total de las calificaciones&#58; 
 &#123;&#123;total_calificaciones_por_tag&#125;&#125; / &#123;&#123;total_calificaciones&#125;&#125; &#160;* 100 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 a654f76a-389b-48f8-884b-3d95fc7dbdef 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 ee2ed3a1-7afc-4655-b496-a67336a4e656 
 2025-04-16T03:51:56.1111240Z 

 {"SessionId":"aa1e3a09-ea15-41a5-90f9-1c61d4085253","SequenceId":7976,"FluidContainerCustomId":"a46ab484-d455-435e-9476-21182564a31b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 

 Informe de calificaciones a puntos de donación: modernización