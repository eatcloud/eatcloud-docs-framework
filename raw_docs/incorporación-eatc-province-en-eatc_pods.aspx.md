# incorporación-eatc-province-en-eatc_pods.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Tomando los datos del eatc_pods realizar una rutina peridica que revise si hay un registro vlido en eatc-province .&#160;&#160; 
 Si no tiene un dato vlido, el sistema debe ralizar una rutina peridica que incorpore las siguientes tareas&#58; 
&#160; 
 1. Determinacin del pas del punto de donacin, para a partir del mismo consultar los datos maestos de municipalidades&#58; 
 A partir de la consulta genrica&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua&#125;&#125;/eatc_pods?_id=&#123;&#123;eatc_pods._id&#125;&#125;&#160; 
&#160; 
 El sistema toma el dato eatc_pods. eatc-country y el dato eatc_pods. eatc-city para realizar la siguiente consulta.&#160; Es posible que se requieran los datos eatc_pods. eatc-lat y eatc_pods. eatc-lon para refinar la bsqueda. 
&#160; 
 2. Determinacin de la provincia segn el maestro eatc_municipalities respectivo 
 Con los datos recolectados se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/&#123;&#123;eatc_pods. eatc-country &#125;&#125;/eatc_municipalities?eatc-city=&#123;&#123;eatc_pods. eatc-city &#125;&#125; 
&#160; 
 El sistema debe tomar el dato eatc_municipalies. eatc-province para incorporarlo al parmetro eatc_pods. eatc-province con lo que sera el siguiente llamado al CRD. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;eatc-province=&#123;&#123;eatc_municipalies. eatc-province &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_pods._id&#125;&#125; 
&#160; 
 En caso que la consulta arroje datos mltiples (es decir, que al hacer un distinct por el dato eatc-province, se obtiene ms de un resultado) se debe proceder a refinar la consulta utilizando los datos eatc_pods. eatc-lat y eatc_pods. eatc-lon 
&#160; 
 3. Refinamiento de la consulta para obtener datos ms precisos. 
 Con los datos recolectados se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/get/&#123;&#123;eatc_pods. eatc-country &#125;&#125;/getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =&#123;&#123;eatc_pods. eatc-lat &#125;&#125;,&#123;&#123;eatc_pods. eatc-lon &#125;&#125;&amp; showfield = eatc-province &amp; km = 10 &amp;filterfield_1= eatc-city &amp;filtervalue_1= &#123;&#123; eatc_pods. eatc-city &#125;&#125; 
&#160; 
 El sistema debe tomar el dato eatc_municipalies. eatc-province para incorporarlo al parmetro eatc_pods. eatc-province con lo que sera el siguiente llamado al CRD. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;eatc-province=&#123;&#123;eatc_municipalies. eatc-province &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_pods._id&#125;&#125; 

&#160; 
 Ejemplo (ambiente de pruebas) 
&#160; 
 Suponiendo que para la cuenta xito, en su punto de donacin cuyo _id=111, no se tiene registro en el campo (eatc-province) o se quiere realizar un proceso de depuracin de datos para incorporar el dato ms reciente de provincia registrado a la informacin del pod, entonces el sistema debe proceder con la primera consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?_id=111 &#160; 
&#160; 
 Como el sistema arroja la siguiente informacin&#58; 
&#160; 
 eatc-city &#58; &quot;BOGOTA&quot;, 
 eatc-country &#58; &quot;CO&quot;, 
 eatc-lat &#58; &quot;4.595721&quot;, 
 eatc-lon &#58; &quot;-74.121706&quot;, 
&#160; 
 El sistema debe proceder con la siguiente consulta de esta manera&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/co/eatc_municipalities?eatc-city=BOGOTA &#160; 
&#160; 
&#160; 
 Como la consulta arroja mltiples resultados (y suponiendo que si se hace un distinct por eatc-province obtenemos ms de un dato), el sistema debe realizar la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/get/co/getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =4.595721,-74.121706&amp; showfield = eatc-province &amp; km = 10 &amp;filterfield_1= eatc-city &amp;filtervalue_1= BOGOTA &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 INCORPORACIN EATC-PROVINCE EN EATC_PODS