# Listado-de-donantes.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Perfil al que se le desplegará este informe 
BO Beneficiario&#58; cua_master (líder de ecosistema social&#58; por ejemplo&#58; ABACO, BAMX) 

 Filtro por cuentas (selector múltiple, con opción &quot;Todas&quot;) 
 El sistema deberá tener un selector múltiple que permitirá seleccionar una, varias o todas las cuentas (cua_user) presentes en el selector (en las estructuras legacy el selector se armaría con esta consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/eatc_cua?eatc_cua_master=&#123;&#123;DOM. eatc_cua_master &#125;&#125;&amp;_cmp= name &#160;&#160; 
 Una vez el usuario realice su selección, con ella el sistema arma un &#123;&#123; array_de_donantes &#125;&#125; que utiliza para generar la tabla del informe. 
&#160; 
 Buscador en la tabla 
 El sistema deberá tener un buscador que busque principalmente por nombre de cuenta e identificación (pero idealmente por los demás campos) y filtre los resultados de la tabla 
&#160; 
 Tabla de información de los donantes 
 El sistema deberá armar una tabla que contenga la siguiente información para cada donante que halla pasado los anteriores filtros 
_id 
Número consecutivo que identifica a la cuenta 
&#160; 
Código 
Lo que en la estructura legacy se conocía co eatc_cua. name 
&#160; 
Nombre del donante 
o que en la estructura legacy se conocía co eatc_customers. eatc_fiscal_name 
&#160; 
Identificación 
o que en la estructura legacy se conocía co eatc_customers. eatc_fiscal_id 
&#160; 
Tipo licencia rescate 
Lo que en la estructura legacy se conocía co eatc_cua. type 
&#160; 
Tipo licencia analytics 
Lo que en la estructura legacy se obtenía con esta consulta 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_data_analytics_cua?eatc_cua=&#123;&#123; eatc_cua. name &#125;&#125;&amp;_cmp= eatc_data_analytics_code 
&#160; 
Regla de match que le aplica 
Lo que en la estructura legacy se obtenía con esta consulta 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/dona_match_classification_querys?eatc_cua_master=&#123;&#123;DOM. eatc_cua_master &#125;&#125;&amp;eatc-donor=&#123;&#123; eatc_cua. name &#125;&#125;&amp;_cmp=eatc_result 
Si la consulta no arroja resultados entonces el valor que debe aparecer será 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/dona_match_classification_querys?eatc_cua_master=&#123;&#123;DOM. eatc_cua_master &#125;&#125;&amp;eatc-donor = _nin_lk &amp;_cmp=eatc_result 
Si la consulta no arroja resultados entonces el valor que debe aparecer será 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/dona_match_classification_querys?eatc_cua_master=&#123;&#123;DOM.eatc_cua_master&#125;&#125;&amp;eatc-donor = _vacio &amp;_cmp=eatc_result 
Si la consulta no arroja resultados entonces el valor que debe aparecer será 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/dona_match_classification_querys?eatc_cua_master= _nin_lk &amp;_cmp=eatc_result 
&#160; 
Número de puntos registrados 
El sistema deberá contar los puntos de donación registrados para el donante, que en la estructura legacy se hacía con esta consulta 
&#123;&#123;URL_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-cua= &#123;&#123;DOM. eatc_cua_master &#125;&#125; &amp;eatc_active=_*&amp;_cont 
Número de puntos con estado activo 
El sistema deberá contar los puntos de donación registrados para el donante, que en la estructura legacy se hacía con esta consulta 
&#123;&#123;URL_donantes&#125;&#125;/api/allpods/eatc_pods?eatc-cua= &#123;&#123; eatc_cua. name &#125;&#125; &amp;eatc_active= y &amp;_cont 
Este número deberá tener un vínculo para a acceder acceder una tabla que se construiría a partir de esta consulta legacy 
 &#123;&#123;URL_donantes&#125;&#125;/ api/allpods/eatc_pods?eatc-cua= &#123;&#123; eatc_cua. name &#125;&#125; &amp;eatc_active= y &amp;_cmp= eatc-name,eatc-id,eatc-province,eatc-city 
Tabla de puntos activos 
La tabla de puntos activos deberá tener un buscador general y mostrar la siguiente información 
 Nombre &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-name 
 ID&#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-id 
 Provincia &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-province 
 Ciudad &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-city 
&#160; 
Puntos con actividad en los últimos 3 meses 
&#160; 
Este número deberá tener un vínculo para a acceder una tabla que se construiría a partir de esta consulta legacy (el cont de la misma) 
 &#123;&#123;URL_donantes&#125;&#125;/ api/ &#123;&#123;DOM. eatc_cua_master &#125;&#125; /eatc_dona_headers?eatc-donor= &#123;&#123; eatc_cua. name &#125;&#125; &amp;eatc-publication_date[0]= &#123;&#123;fecha_de_hace_tres_meses&#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123;fecha_actual&#125;&#125; &amp;_distinct= eatc-pod_id 
Con el array &#160;de eatc-pod_id obtenidos, se realiza la siguiente consulta 
 &#123;&#123;URL_donantes&#125;&#125;/ api/allpods/eatc_pods?eatc-cua= &#123;&#123; eatc_cua. name &#125;&#125; &amp; eatc-id = &#123;&#123;array_pod_id&#125;&#125; &amp;_cmp= eatc-name,eatc-id,eatc-province,eatc-city 
Tabla de puntos con actividad 
La tabla de puntos activos deberá tener un buscador general y mostrar la siguiente información 
 Nombre &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-name 
 ID&#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-id 
 Provincia &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-province 
 Ciudad &#58; lo que en la estructura legacy se obtenía en el campo eatc_pods. eatc-city 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 Listado de donantes