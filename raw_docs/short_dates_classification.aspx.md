# short_dates_classification.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se implementará un servicio que tenga la siguiente estructura&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/ short_dates_classification /&#123;&#123; _DOM. cua_master &#125;&#125;/?eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc_donor = &#123;&#123; eatc_dona_headers. eatc-donor &#125; &#125;&amp; eatc_closer_expiration_date=&#123;&#123; eatc_dona_headers .eatc_closer_expiration_date &#125; &#125; 
&#160; 
 EJEMPLO (ambiente de pruebas)&#58;&#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/ short_dates_classification /abaco/? eatc_dona_header_code = 00002108194223 &amp; eatc_donor = &#123;&#123; eatc_dona_headers. eatc-donor &#125; &#125;&amp; eatc_closer_expiration_date=2021-09-01 

 Nota importante &#58; el presente servicio de clasificación se deberá llamar antes de que se invoque el servicio para realizar el match, ya que su resultado infiere en el proceso de match (inicialmente para el caso específico de Mexico) 

 Consulta de datos para hacer el cálculo para clasificar por fecha corta 
&#160; 
 Cada donante o cada cuenta maestra, podrá establecer un número de días a partir de los cuales se considera que una donación tiene una fecha larga de caducidad (y por ende, antes de los cuales tiene una fecha corta de caducidad).&#160; Por ese motivo, el sistema debe realizar las siguientes consultas con la información que llega del llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua? name = &#123;&#123; eatc_dona_headers. eatc-donor &#125; &#125;&amp;_cmp= eatc_days_to_short_date 
&#160; 
 Si la consulta no trae resultados entonces el sistema realizará la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua_master? eatc_cua = &#123;&#123; _DOM. cua_master &#125;&#125; &amp;_cmp= eatc_days_to_short_date 
&#160; 
 Si el sistema no recibe una respuesta, el servicio deberá responder con el mensaje&#58; 
 Unable to classify by short date 
&#160; 
 Si el sistema no recibe una fecha válida en el campo &quot;eatc_closer_expiration_date&quot;, (por ejemplo, recibe 0000-00-00), entonces deberá responder con el mensaje 
 Unable to classify by short date 
&#160; 
 El sistema deberá guardar un log de estas consultas, guardando la fecha y hora, los mensajes que desplegó el servicio y las causas por las cuales no pudo clasificar (de ser necesario) 
&#160; 
&#160; 
 Clasificación con respecto a la fecha corta&#58; 
&#160; 
 dias_para_la_caducidad 
 Con el dato obtenido en la consulta anterior (bien sea &#123;&#123;eatc_cua. eatc_days_to_short_date &#125;&#125; o&#160; &#123;&#123;eatc_cua_master. eatc_days_to_short_date &#125;&#125; en adelante eatc_days_to_short_date ) el sistema deberá calcular, para la fecha en la cual se realiza la consulta (es decir la fecha en la cual se invoca el servicio), a cuantos días está distanciada la fecha más próxima de caducidad de la donación ( &#123;&#123; eatc_dona_headers .eatc_closer_expiration_date &#125; &#125; ), es decir, calcular cuantos días faltan para que se de la caducidad de los alimentos donados. 
&#160; 
 &#123;&#123; dias_para_la_caducidad &#125;&#125;=&#123;&#123; eatc_dona_headers .eatc_closer_expiration_date &#125; &#125; - &#123;&#123; current_date &#125;&#125; 
&#160; 
 Clasificación a partir de los dias_para_la_caducidad y eatc_days_to_short_date 
 Tomando el dato de &#123;&#123; dias_para_la_caducidad &#125;&#125; y el dato de&#160; &#123;&#123; eatc_days_to_short_date &#125;&#125; el sistema deberá clasifcicar de la siguiente manera, al comparar los dos números&#58; 

&#160; 
 &#123;&#123;dias_para_la_caducidad&#125;&#125;&lt;= 0 
&#160; 
 Cuando los días para la caduciad son menores o iguales a cero, quiere decir que el alimento ya caducó por lo tanto&#58; 
 &#123;&#123;resultado_clasificacion&#125;&#125; = anuncio_caducado 

&#160; 
 eatc_days_to_short_date =&gt; &#123;&#123;dias_para_la_caducidad&#125;&#125; &gt; 0 
&#160; 
 Si los días para la caducidad, son mayores que cero y menores o iguales de los días para establecer una fecha corta, quiere decir que el anuncio se clasifica como de fecha corta&#58;&#160; 
 &#123;&#123;resultado_clasificacion&#125;&#125; = fecha_corta 

&#160; 
 eatc_days_to_short_date &lt; &#123;&#123;dias_para_la_caducidad&#125;&#125; &gt; 0 
&#160; 
 Si los días para la caducidad, son mayores que cero y mayores a los días para establecer una fecha corta, quiere decir que el anuncio se clasifica como de fecha larga&#58;&#160; 
 &#123;&#123;resultado_clasificacion&#125;&#125; = fecha_larga 

&#160; 
 Escritura del resultado de la clasificación en la donación específica 
 Teniendo determinado el &#123;&#123;resultado_clasificacion&#125;&#125;, el sistema realiza el siguiente registro&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers ?&amp;_operacion=update&amp; eatc_dona_typology_a = &#123;&#123;resultado_clasificacion&#125;&#125;&amp; eatc_dona_classification_datetime =&#123;&#123;datetime_stamp &#125;&#125;&amp;WHEREeatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 

&#160; 
 Generar Nuevo Match&#160; 
 El sistema deberá evaluar si para la donación en cuestión existe un match previo, mediante la consulta 
&#160; 
 &#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers ?eatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp= eatc_match_asignation_rule 
&#160; 
 Si el sistema arroja un dato válido en esta consulta, querrá decir que el anuncio en cuestión ya tiene una clasificación de cara al match previa y por lo tanto, dado que la nueva clasificación de la donación (en cuanto a su fecha corta) puede influir en dicho match, el sistema procede a lanzar de nuevo el proceso para clasificar la donación para el match (donamatchclass&#58; cuya documentación se puede consultar aquí ), y por ende los posteriores procesos para asignar la donación según sus respectivas reglas. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SHORT_DATES_CLASSIFICATION: PROCESO PARA CLASIFICAR ANUNCIOS DE DONACIÓN CON FECHAS CORTAS