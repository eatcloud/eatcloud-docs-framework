# recalkpi-servicio-para-recalcular-los-kpis-de-una-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica ya que ha surgido la necesidad de editar anuncios cuyo estado es &quot;recibido&quot;.&#160; Anteriormente la edicin de estos anuncios estaba restringida, precisamente porque a los anuncios con este estado se les calculaban los KPIs. Con este servicio se espera abrir la posibilidad de editar anuncios &quot;recibidos&quot; y realizar el reclculo de los KPIs para dichos anuncios. 
&#160; 
 Los llamados al servicio se documentan aqu&#58;&#160; Servicio privado para reclculo de KPIs de una donacin 
&#160; 
 A continuacin se documenta el proceso que debe llevarse a partir del llamado que se hace al servicio en cuestin. 

 LOG DEL SERVICIO 
 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 
 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;op&#58;false 

 1. VALIDACIN DE DATOS COMPLETOS 
&#160; 
 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de . Parmetros del body de la peticin &#160; de la especificacin del servicio privado . Si lo son, seguir adelante con el prximo paso.&#160; Si no lo son deber entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIN DEL ESTADO DEL ANUNCIO (SOLO SE RECALCULAN LOS KPIS PARA ANUNCIOS CUYO ESTADO ES &quot;DELIVERED&quot; O &quot;RECEIVED&quot;) 
&#160; 
 Con el dato que llega en los parmetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc-state= delivered,received &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta ( validacin de datos de la donacin )&#58; 
 fail 
&#160; 
 Si la consulta arroja respuesta una respuesta vlida el sistema sigue con la siguiente validacin&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; 00002203030033 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =00002203030033&amp; eatc-state= delivered , received&amp;_cmp=_id &#160; &#160;&#160; &#160; 
&#160; 
 Dado que no se obtiene una respuesta vlida por parte del sistema entonces el sistema despliega la respuesta &quot; fail &quot;&#58; 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_header_code = &quot; 00001911190031 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code =00001911190031&amp; eatc-state= delivered , received&amp;_cmp=_id &#160; &#160;&#160; &#160; 
&#160; 
&#160; 
 Dado que se obtiene una respuesta vlida por parte del sistema entonces el servicio sigue adelante con su proceso 

 3. BORRADO DE LOS REGISTROS PREVIOS EN LA TABLA DE KPIS 
&#160; 
 El sistema, con los parmetros enviados para la invocacin del servicio, deber implementar el siguiente borrado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_kpi &amp;_operacion= delete &amp;WHEREeatc-dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; 
&#160; 
 Si el borrado no es exitoso, el servicio deber retornar&#58; 
 fail 
&#160; 
 Y deber generar una alerta a un grupo de Telegram en donde se exprese hay un problema con el borrado de los KPIs enviando la URL de borrado. 
&#160; 
 Si el borrado es exitoso el sistema sigue adelante con el siguiente paso. 

 4. LLAMADO AL PROCESO DE GENERACIN DE KPIS 
&#160; 
 Una vez borrados los datos de los KPIs, el servicio deber llamar al proceso que genera los KPIs para el anuncio en cuestin .&#160;&#160; 
&#160; 
 KPIs para donaciones con estado despachado 
 KPIs para donaciones con estado recibido 

 Nota para el desarrollador &#58; si dicho servicio no fue diseado para ser invocado bajo demanda, y corre a partir de un cronjob, el sistema deber asegurarse que las condiciones para que el servicio genere los KPIs para el anuncio en cuestin sean dadas, de tal manera que cuando vuelva a correr el proceso se vuelvan a generar los KPIs que fueron previamente borrados. 

 5. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si la clasificacin fue exitosa, entonces entregar la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 RECALKPI: SERVICIO PARA EL RECLCULO DE LOS KPIS DE UNA DONACIN