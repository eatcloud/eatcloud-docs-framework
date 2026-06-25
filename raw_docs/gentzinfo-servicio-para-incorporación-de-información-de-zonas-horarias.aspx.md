# gentzinfo-servicio-para-incorporación-de-información-de-zonas-horarias.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio (que podr ser invocado desde un cron o desde una URL) recibir el cdigo de un beneficiario (junto con la respectiva cua_master ), o de un punto de donacin (junto con la respectiva cua_user ), y con esta informacin realizar una consulta de las respectivas coordenadas. 
&#160; 
 eatc_donation_managers&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_donation_managers ?identificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= coordenadas 
&#160; 
 eatc_pods&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/ eatc_pods ?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;eatc-cua=&#123;&#123; cua_user &#125;&#125;&amp;_cmp= eatc-lat,eatc-lon,_id 

&#160; 
 Para obtener las respectivos datos de &#123;&#123;lat&#125;&#125; , &#123;&#123;lon&#125;&#125; (e &#123;&#123;_id&#125;&#125; para los eatc_pods) 
 Con los datos obtenidos el sistema deber realizar la siguiente consulta (no se puede realizar ms de una consulta por segundo dado que es un API gratuita)&#58; 

&#160; 
 https&#58;//api.timezonedb.com/v2.1/get-time-zone?key=CU0WU4CJSKYT&amp;format=json&amp;fields=countryCode,zoneName&amp;by=position&amp;lat= &#123;&#123;lat&#125;&#125; &amp;lng= &#123;&#123;lon &#125;&#125; 
&#160; 
 Ms informacin de la API&#58; 
 https&#58;//timezonedb.com/references/get-time-zone 
 user&#58; eatcloud (jdc@eatcloud.com) y psw&#58; rBv7AuxfZ#bMj3%W* 
&#160; 
 Con los datos que devuelve el servicio como por ejemplo&#58; 
 &#123; 
 status &#58; &quot;OK&quot;, 
 message &#58; &quot;&quot;, 
 countryCode &#58; &quot;US&quot; , 
 zoneName &#58; &quot;America/New_York&quot; 
 &#125; 
&#160; 
 El servicio deber escribir los datos recibidos en countryCode .data (en el ejemplo &quot;US&quot; ) y zoneName .data (en el ejemplo &quot;America/New_York&quot; ) tal como se hara con el CRD de la siguiente manera (los campos&#58;&#160; 
 &#123;&#123;eatc_donation_managers. countryCode &#125;&#125; 
 &#123;&#123;eatc_donation_managers. zoneName &#125;&#125; &#160; 
 &#123;&#123;eatc_pods. countryCode &#125;&#125; 
 &#123;&#123;eatc_pods. zoneName &#125;&#125; &#160; 
 &#160;no existen, hay que crearlos en las diferentes tablas) 

&#160; 
 eatc_donation_managers&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_donation_managers &amp;_operacion= _update &amp; countryCode= &#123;&#123;countryCode. data &#125;&#125; &amp; zoneName =&#123;&#123; zoneName .data &#125;&#125; &amp;WHERE identificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 eatc_pods&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/?_tabla= eatc_pods &amp;_operacion= _update &amp; countryCode= &#123;&#123;countryCode. data &#125;&#125; &amp; zoneName =&#123;&#123;zoneName. data &#125;&#125; &amp;WHERE _ id=&#123;&#123;eatc_pods._ id &#125;&#125; 
&#160; 
 Como parte de la respuesta del servicio se deben incluir&#58; 
 countryCode= &#123;&#123;countryCode. data &#125;&#125; 
 zoneName =&#123;&#123;zoneName. data &#125;&#125; 
&#160; 
 HASTA AQU SE HACE DOCUMENTACIN PRELIMINAR,&#160; EN ADELANTE EST PENDIENTE SU REVISIN DE ACUERDO A LOS RESULTADOS DE LA IMPLEMENTACIN INICIAL. 

 LOG DEL SERVICIO 
 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 
&#160; 
 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;op&#58;false 

 1. VALIDACIN DE DATOS COMPLETOS 
&#160; 
 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de . Parmetros del body de la peticin &#160; de la especificacin del servicio privado . Si lo son, seguir adelante con el prximo paso.&#160; Si no lo son deber entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIN.... 
&#160; 
 Con los datos que llega en los parmetros&#58; 
 ..... 
 ..... 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123; eatc_donation_manager_code &#125;&#125;&amp; eatc_state = activo &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail_not_active_doma 
&#160; 
 Si la consulta arroja respuesta una respuesta vlida el sistema sigue con la siguiente validacin&#58; 

 3. ACTUALIZACIN DE DATOS ...... 
&#160; 
 Con los datos que llega en los parmetros&#58; 
 ..... 
&#160; 
 El sistema deber realizar una operacin homloga a la siguiente (dado que se deber bannear precisamente este llamado o cualquier llamado similar que vare los datos de licenciamiento del gestor de donaciones a partir del CRD) 
&#160; 
 ..... 

 4. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
&#160; 
 Si la actualizacin de datos fue exitosa, entonces entregar la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 GENTZINFO: SERVICIO PRIVADO PARA INCORPORACIN DE INFORMACIN DE ZONAS HORARIAS Y CDIGO DE PAS