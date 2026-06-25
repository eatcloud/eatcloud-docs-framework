# Informe-de-calificaciones-al-donante--modernización-BO-Beneficiarios-(líder-de-ecosistema).aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación&#58;&#160; 
Esta implementación es una ampliación de la implementación definida aquí (para el perfil beneficiario), pero en esta ocasión, el líder de ecosistema tendrá acceso a todas las calificaciones de los diferentes donantes de su ecosistema. 
&#160; 
Por lo tanto deberá tomar en cuenta las mismas consideraciones establecidas para dicho informe y simplemente deberá contener filtros adicionales que permitan consultar la información por diferentes donantes (y no la información de un solo donante, que es como funciona el informe previamente documentado) 

 Titulo de la vista&#58; Informe de calificaciones cualitativas para los puntos de donación 
 Descripción del informe 
En este informe podrás ver cómo están calificando los gestores de donaciones (organizaciones beneficiarias) a los diversos puntos de donación de los donantes del ecosistema, con respecto a la operación de rescate humanitario de alimentos a través de las plataformas EatCloud. 
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
El sistema deberá realizar una serie de consultas para generar una tabla de estadísticas por punto de donación de los puntos adscritos a una cuenta maestra (&#123;&#123;_DOM. cua_master &#125;&#125;). &#160;En primera instancia el sistema deberá crear un selector múltiple de&#160; 
&#160; 
Selector múltiple de cuentas usuario para construir el informe 
El sistema realizará la siguiente consulta para establecer las cuentas usuario que fueron calificadas en el periodo definido 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_pod_tag_registry? date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;_distinct=eatc_cua_origin 
El sistema, construirá un selector múltiple (con opción de seleccionar todas las opciones) con las respuestas obtenidas. &#160;El usuario seleccionará las cuentas usuario sobre las cuales quiere que se construya el informe y por lo tanto construirá un &#123;&#123;array_cua_users&#125;&#125; que será utilizado, en la próxima consulta para establecer los PODs sobre los cuales se construirá el informe. 
 &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_pod_tag_registry ?eatc_cua_origin= &#123;&#123;array_cua_users&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;_distinct=pod_id 
Para cada uno de los pods obtenidos, se realizarán las siguientes consultas con miras a construir información estadística. Para cada uno de los pods obtenidos, se realizarán las siguientes consultas con miras a construir información estadística (si existen identificadores de pods similares a la consulta también se le tendrá que incorporar el parámetro eatc_cua_origin para obtener valores que correspondan a pods por cuenta). 
Porcentaje de calificaciones positivas y negativas 
El sistema deberá contar el total de calificaciones cuantitativas que recibió cada uno de los puntos que arroja la anterior consulta&#58; 
 &#123;&#123;total_calificaciones&#125;&#125; = &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_pod_tag_registry ?pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;_cont 
y contar también el número de calificaciones positivas &#58; 
 &#123;&#123;total_calificaciones_positivas&#125;&#125; &#160;= &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_pod_tag_registry ?pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;type= positiva &amp;_cont 
y negativas recibidas por cada punto&#58; 
 &#123;&#123;total_calificaciones_negativas&#125;&#125; &#160;=&#160; &#123;&#123;URL_donantes&#125;&#125; /api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_pod_tag_registry ?&amp;pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;type= negativa &amp;_cont 
Porcentaje de tags 
El sistema deberá contar los diferentes tags que están disponibles en la plataforma, que se obtienen de la siguiente consulta&#58; 
 &#123;&#123;tags&#125;&#125; &#160;= &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_calification_tags ?sujeto_calificacion= pods &amp;_cmp= tag 
Cuantas veces obtuvo el punto en cuestión la respectiva calificación, iterando, para cada uno de los tags de la anterior consulta, la siguiente consulta 
 &#123;&#123;total_calificaciones_por_tag&#125;&#125; &#160;=&#160; &#123;&#123;URL_donantes&#125;&#125; /api/abaco/ eatc_pod_tag_registry ?pod_id= &#123;&#123;eatc_pod_id&#125;&#125; &amp;date_time[0]= &#123;&#123;fecha_inicial&#125;&#125; %2000&#58;00&#58;00&amp;date_time[1]= &#123;&#123;fecha_final&#125;&#125; %2023&#58;59&#58;59&amp;tag= &#123;&#123;tags&#125;&#125; &amp;_cont 
&#160; 
 Tabla de información de calificaciones&#58; 
 Filtro por eatc_cua_origin &#160; &#58; selección múltiple (para perfil BO Donantes) 
 Con la siguiente consulta el informe debe construir un filtro de selección múltiple, con opción de “todas las cuentas” que permita filtrar por&#160; 
&#160; 
 Información a mostrar en la tabla de información 
 Se debe mostrar la información del detalle de cada donación acompañada de cierta información de encabezado 
&#160; 
 eatc_cua_origin &#160; 
Muestra la cuenta a la cual pertenece cada POD. 
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

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 0c65e0da-a657-4197-a126-ac39d5b58b64 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 3990186d-b050-471d-807f-430aeb5bcbad 
 2025-08-27T04:05:38.0744103Z 

 {"SessionId":"58860632-a8f6-4d17-a8a9-c86106e8dac8","SequenceId":4256,"FluidContainerCustomId":"0df21d66-4dee-459b-9157-e64ed732fe0e","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Informe de calificaciones al donante: modernización BO Beneficiarios (líder de ecosistema)