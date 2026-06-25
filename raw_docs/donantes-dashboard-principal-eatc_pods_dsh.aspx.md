# donantes-dashboard-principal-eatc_pods_dsh.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 El dashboard general presenta de manera agradable y vistosa las principales mtricas o KPIs ( key performance indicators) de la operacin general de cada punto de donacin, mediante cards y pestaas que abajo se describen 

&#160; 
 ***NUEVO*** Mensaje parte superior del dashboard (se debe mostrar despus de un login exitoso) 
 *** Ver documentacin *** 

 Botones de accin 

 [NUEVO] Cards de anuncios pendientes de verificacin (OJO QUE NO EST EN EL DISEO) 
 Esta funcionalidad se constituir en una alerta flotante con posicin destacada y&#160; siempre visible a primera vista en el dashboard, que dar muy fcil acceso al proceso de verificacin de cdigo de recogida (que se ha identificado como un proceso problemtico y por lo tanto se propone esta facilidad buscando que el mismo sea de ms fcil operacin. Puede ser similar a la card de anuncio de donacin que se implementa en la funcionalidad &quot; seguimiento de anuncio de donacin &quot; con algunos ajustes que se documentan ms abajo) &#160; cada vez que una de las donaciones cambie su estado de &quot;adjudicado&quot; a &quot;programado&quot;. 
&#160; 

 Consulta para obtener la informacin necesaria (revisar dinamismo del _DOM.cua_master) 
 Para traer la informacin se deber realizar la siguiente consulta el sistema toma el parmetro &quot; eatc-id &quot; del punto de donacin ( eatc_pods ) respectivo&#58; 
 Deprecado&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;CUA_master&#125;&#125;/eatc_dona_headers?eatc-pod_id=&#123;&#123;eatc_pods.eatc_id&#125;&#125;&amp;eatc-state=scheduled 
 NUEVA Consulta de los anuncios que no se les ha puesto una fecha vlida en &quot;eatc_code_verification_datetime&quot;&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125;&amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 

 Se depreca una vez se implemente esta tarea&#58; https&#58;//app.asana.com/0/1193204835809005/1200125520147978 Con la informacin obtenida, el sistema debe mostrar aquellos anuncios cuya fecha de publicacin (eatc-publication_date) est dentro de la ltima semana (dejar estos das&#58; 8 en un parmetro que se pueda variar fcilmente, por si toca reducirlo o ampliarlo). 

 ****NUEVO****Das atrs para realizar la siguiente consulta&#58; 
 Por defecto, se debe colocar el valor de 30 das (cmo est actualmente configurado), pero este nmero se debe traer dinmicamente por cuenta realizando la siguiente consulta&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125; 
 y obteniendo el dato consignado en eatc_cua. eatc_days_back_pending_code_vrf para establecer los das hacia atrs que se muestran en el dashboard antes del botn para consultar el resto de los anuncios pendientes de verificacin (si no se trae un dato vlido se debe utilizar el actual default de 30 das. 
 Ejemplo ambiente de pruebas EXITO&#58; 
 Se realiza la siguiente consulta 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
&#160; 
 Como el valor que se obtiene en eatc_cua. eatc_days_back_pending_code_vrf es 8 entonces se deben mostrar anuncios de 8 das atrs. 
&#160; 
 Ejemplo (con base en el prximo ejemplo&#58; siendo el 2021-04-30) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp; eatc-publication_date[0]=2021-04-22 &amp; eatc-publication_date[1]=2021-04-30 &amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 &#160; 
 Consulta de donaciones pendientes de verificacin 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id (teniendo en cuenta solamente el estado &quot;scheduled&quot; (eatc-state=scheduled) a fin de no sobrecargar la consulta&#58; 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 &#160;&#160; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 &#160; 
 La informacin obtenida se presenta en cards por anuncio de la siguiente manera,&#160; colocando primero los que tienen eatc_dona_headers .eatc-picking_checkout_datetime ms antigua (hasta los de fecha ms reciente) y luego los que tienen eatc_dona_headers .eatc-picking_checkin_datetime ms antigua (hasta los de fecha ms reciente) y por ltimo los que tengan eatc_dona_headers .eatc-publication_datetime ms antigua (hasta los de fecha ms reciente)&#58; 
 Fecha y hora del anuncio&#58; 
 eatc_dona_headers .eatc-publication_datetime 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio y program su recogida 
 Nombre&#58; eatc_dona_headers .eatc-donation_manager_name 
 Direccin&#58; eatc_dona_headers .eatc-donation_manager_address 
 Telfono&#58; eatc_dona_headers .eatc-donation_manager_address 
 Total de kilos que contiene el anuncio 
 eatc_dona_headers .eatc-total_weight_kg 
 Fecha y hora programada de recogida 
 eatc_dona_headers .eatc-programed_picking_datetime 
 El donante lleg al punto de donacin a las&#58; (informacin que solo se debe mostrar si existe un registro vlido en eatc-picking_checkin_datetime) 
 eatc_dona_headers .eatc-picking_checkin_datetime 
 El donante sali del punto de donacin a las&#58; (informacin que solo se debe mostrar si existe un registro vlido en eatc-picking_checkout_datetime) 
 eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Cuando este dato esta presente la card debe aparecer de primera en un color muy vistoso (o con un letrero distitivo como&#58; &quot;verificar cdigo de inmediato&quot;) que invite a tomar accin de verificacin 

&#160; 
 Cdigo de verificacin&#58; 
 En este punto debe presentar un campo de captura para ingresar el cdigo, el nuevo botn de la funcionalidad para realizar verificacin de manera remota &quot; copiar el cdigo enviado por el beneficiario &quot;, y un botn para realizar la verificacin.&#160; El funcionamiento de esta verificacin debe ser totalmente similar al que se implementa con las nuevas definiciones en la funcionalidad &quot; Verificacin del cdigo de recogida &quot;. 
&#160; 
 En una primera etapa de implementacin se puede simplemente colocar un botn que lleve directamente a la funcionalidad de &quot; Verificacin del cdigo de recogida &quot;, pero lo ideal es que el proceso de verificacin puede hacerse directamente en el dashboard, para hacerlo ms gil y usuable. 

&#160; 
 [***NUEVO***] Indicadores clave 
 A partir del rodaje que se han tenido con los indicadores desarrollados para los BO de Donantes y beneficiarios, se proponen el siguiente set de indicadores que deben disponerse en cards en el lugar donde estaban las secciones&#58; Card tus mtricas e Indicadores de impacto (justo debajo de la nueva funcionalidad de Cards de anuncios pendientes de verificacin ) 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125; 
 Ambiente de productivo&#58; https&#58;//donantes.eatcloud.info/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125; 

 Diseo similar a cmo se estableci en el BO donantes&#58; 
 &#160; El diseo deber ser similar al definido para&#160; dicho BO en cuanto a sus elementos constitutivos (pero el mismo ser definido en estilos y disposicin grfica en la plataforma de documentacin de diseo&#58; https&#58;//zeroheight.com/6217d62d5/p/27eb58-dashboards ).&#160; Siempre se deber incorporar la ficha tcnica del indicador, y los dems elementos como se establece en el siguiente esquema ===&gt; 

 Se deben sentar las bases para poder luego ocultar un conjunto de indicadores de acuerdo a la tipologa de la cuenta 
 Como se solicito en su momento para el BO de donantes, esta funcionalidad de indicadores tambin deber permitir en un futuro, mostrar u ocultar indicadores de acuerdo a tipologas de la cuenta respectiva. 
&#160; 
 Selector de fechas 
 Se debe presentar un selector de fecha inicial y final para la consulta de los indicadores, cuyo valor por defecto es del 1 del mes actual a la fecha actual (tal como est en el BO de donantes) y que contenga la siguiente leyenda&#58; 
 La informacin que se visualiza en los indicadores corresponde a los datos en la fecha seleccionada. Si deseas consultar fechas diferentes por favor vara la fecha inicial y la fecha final 

 Los indicadores a continuacin descritos, correspondern al rango de fechas seleccionado y mostrarn solo los datos del punto de donacin ( eatc_pod ) desde el cual se accedi a la web app de donantes. 

&#160; 
 *****NUEVO****&#58; dinamizar las consultas necesarias para mostrar las estadsticas a partir de la cuenta maestra. 
 Cuando se ingrese a un BO, el sistema debe consultar la cuenta maestra de dicha cuenta, y a partir de dicho valor realizar las consultas necesarias para traer la informacin y los KPIs que se muestra en el dashboard. 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; =&gt; eatc_cua_master 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona_kpi?&#123;&#123;parametro_consulta&#125;&#125;=&#123;&#123;VALOR&#125;&#125; 
&#160; 
 NOTA &#58; como no se tiene informacin de los mecanismos con los cuales se consultan los KPIs y la informacin que se despliega en el dashboard de del BO, se realiza esta documentacin de manera general, por lo tanto el desarrollador deber realizar las abstracciones necesarias a partir de la misma para realizar la implementacin que lo que busca es permitir la evolucin del sistema a uno donde se manejen mltiples cuentas maestras. 

 Monto donado&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes, pero solo muestra informacin para el punto de donacin (eatc_pod) desde el cual se consulta (lo mismo aplica para los dems indicadores). 

 KG aprovechados&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes, , pero solo muestra informacin para el punto de donacin (eatc_pod) desde el cual se consulta. (lo mismo aplica para los dems indicadores). 

 Referencias donadas&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes (nombre del indicador, ficha tcnica, cono), y en la funcionalidad de cancelaciones (con respecto a su informacin alternativa&#58; unidades donadas) 

 Nmero de anuncios&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes (aunque su nombre ser &quot;Nmero de anuncios&quot; en vez de &quot;Anuncios&quot;) 

 Kilogramos donados consolidados&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes (aunque su nombre ser &quot;KG donados consolidados&quot; en vez de &quot;Impacto social&quot; y en la informacin complementaria en vez de &quot;Kilogramos donados consolidados&quot; debe ir &quot;Difiere de los KG donados en tiempo real dado que la consolidacin se hace da vencido&quot;) 

 Platos servidos&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes (aunque su nombre ser &quot;Platos servidos&quot; en vez de &quot;Porciones&quot;) 

 Impacto ambiental&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes. 

 Porcentaje de cancelados (segn nmero de anuncios)&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes (aunque su nombre ser &quot;Porcentaje de cancelados (segn nmero de anuncios)&quot; en vez de &quot;Porcentaje cantidad cancelados&quot;) 

 Porcentaje de kilogramos cancelados&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes . 

 Porcentaje de cancelados (segn valor de las donaciones)&#58; 
 &#160; Funciona de manera similar al indicador del mismo nombre definido para el BO de donantes&#160; (aunque su nombre ser &quot;Porcentaje de cancelados (segn valor de las donaciones)&quot; en vez de &quot;Porcentaje $pesos cancelados&quot;) 

 Card Tus mtricas (deprecado)&#58; 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el mes en curso 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el ao en curso 
 #KPI de impacto social 
 kg = eatc_dona_headers .eatc-total_weight_kg 

&#160; 
 Indicadores de impacto (deprecado)&#58; 
 Mediante tres pestaas presenta los principales indicadores por tipo de indicador, y el botn (+) que da acceso a la funcionalidad&#58; detalle de KPI .&#160; Las pestaas son las siguientes&#58; 
 Impacto Social 
 Muestra el total de kilogramos donados por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
 #KPI KG&#58; Regla de clculo 
 kg = eatc_dona_headers .eatc-total_weight_kg. 
&#160; 
 Para realizar el clculo se debe invocar el API&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=kg&amp;eatc-pod_id=[id ] 
&#160; 
 Ejemplo&#58; 
 Para el punto de donacin &quot;&quot;, cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=kg&amp;eatc-pod_id= [valor] . Luego se realiza una sumatoria del campo &quot;Value&quot; y esta ser el resultado 
&#160; 
 Impacto econmico&#58; 
 &#160; muestra el total de dinero ahorrado por cuenta de las donaciones&#160; por parte del punto de donacin ( eatc_pods ), es decir la sumatoria de todos los ahorros y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
 #KPI de impacto econmico&#58; Reglas de clculo 
&#160; 
 Para realizar el clculo se debe invocar el API&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_kpi?eatc-kpi_type=Economic impact&amp;eatc-pod_id=[id] 
&#160; 
 Ejemplo&#58; 
 Para el punto de donacin &quot;&quot;, cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 ?eatc-kpi_type=Economic impact&amp;eatc-pod_id = [valor] . Luego se realiza una sumatoria del campo &quot;Value&quot; y esta ser el resultado 
&#160; 
 Impacto ambiental&#58;&#160; 
 Muestra el total de las emisiones de C02 en toneladas ahorradas por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ). 
 #KPI C02_tons&#58; regla de clculo 
 CO2_tons = eatc_dona_headers .eatc-total_weight_kg*(0,023/1000) 
&#160; 
 Para realizar el clculo se debe invocar el API&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=CO2_tons&amp;eatc-pod_id=[id] 
&#160; 
 Ejemplo&#58; 
 Para el punto de donacin &quot;&quot;, cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=CO2_tons&amp;eatc-pod_id= [valor] . Luego se realiza una sumatoria del campo &quot;Value&quot; y esta ser el resultado 

 Tablero de liderazgo 
 El dashboard presentar un &quot;Tablero de Liderazgo&quot; en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso 

 ***NUEVO&#58; formulario Net Promoter Score**** 
 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio&#58; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= webapp &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 
 eatc_user_code 
 Corresponde al parmetro &quot;eatc-id&quot; del punto de donacin que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?_id=&#123;&#123;_id&#125;&#125; 
 eatc_plataform 
 webapp (constante para este llamado) 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
 Si el servicio responde de manera negativa, no se despliega el formulario. 
 Si el servicio responde de manera afirmativa se desplegar el formulario respectivo. 
 Despliegue del formulario 
 El formulario se deber desplegar segn su definicin y los mecanismos de integracin que se provean para este fin.&#160; Se debe mirar si se despliega como un modal (que tendr dos formularios sucesivos adentro), en la parte superior de la pantalla o en la parte inferior de la&#160; 
 pantalla. 
 Registro del NPS ( nps_main_question ) 

 Edicin&#160; del NPS ( nps_secondary_question ) 

 Ejemplo de cdigo html para la implementacin del formulario 
 &lt;!-- MODAL NPS DATAGOV --&gt; 
 &lt;div id=&quot;modal_nps&quot; class=&quot;modal bottom-sheet&quot;&gt; 
 &#160;&#160;&#160;&#160;&lt;div class=&quot;modal-content&quot; style=&quot;text-align&#58;center&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;h4 id=&quot;nps_main_question&quot; style=&quot;display&#58;inline-block&quot;&gt;titulo&lt;/h4&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;widget widget-sm&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;button-container&quot; id=&quot;div_primer_nps&quot; style=&quot;display&#58;inline-block&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;span class=&quot;negative-text&quot; id=&quot;nps_lower_limit_label&quot; &gt;Limite inferior&lt;/span&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(1)&quot;&gt;1&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(2)&quot;&gt;2&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(3)&quot;&gt;3&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(4)&quot;&gt;4&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(5)&quot;&gt;5&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(6)&quot;&gt;6&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(7)&quot;&gt;7&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(8)&quot;&gt;8&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(9)&quot;&gt;9&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;a class=&quot;btn-floating btn-large waves-effect waves-light blue changecolor&quot; onclick=&quot;fn_valor_nps(10)&quot;&gt;10&lt;/a&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;span class=&quot;positive-text&quot; id=&quot;nps_upper_limit_label &quot;&gt;Limite superior&lt;/span&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div id=&quot;div_segundo_nps&quot; style=&quot;display&#58;none&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;row&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;div class=&quot;input-field col s12&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;p class=&quot;lbl_opcional&quot; style=&quot;text-align&#58; right; color&#58;#9e9e9e;&quot;&gt;Opcional&lt;/p&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;textarea id=&quot;nps_secundary_answer&quot; class=&quot;materialize-textarea&quot; data-length=&quot;120&quot;&gt;&lt;/textarea&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;label id=&quot;nps_secundary_question&quot; for=&quot;nps_secundary_answer&quot;&gt;Textarea&lt;/label&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&lt;/div&gt; 
 &#160;&#160;&#160;&#160;&lt;div class=&quot;modal-footer&quot; style=&quot;display&#58;none&quot; id=&quot;nps_footer&quot;&gt; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;button type=&quot;button&quot; id=&quot;nps_submit_btn&quot; class=&quot;btn btn-default lbl_enviar&quot; data-dismiss=&quot;modal&quot; onclick=&quot;fn_registrar_nps()&quot;&gt;enviar&lt;/button&gt; 
 &#160;&#160;&#160;&#160;&lt;/div&gt; 
 &lt;/div&gt; 

 Llamado para el registro del NPS ( nps_main_question ) ***NUEVO*** adicin de parmetros de clasificacin (se resaltan en rojo) 
 Se deber realizar el siguiente llamado para realizar el registro del NPS 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= webapp &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125; &amp; eatc_vertical =&#123;&#123;eatc_cua .vertical &#125;&#125;&amp; eatc_cua_size =&#123;&#123;eatc_cua .eatc_cua_size &#125;&#125;&amp; eatc_licence_type =&#123;&#123;eatc_cua .type &#125;&#125; &amp;_operacion= insert 
 Los parmetros para realizar la consulta son los siguientes&#58; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
 eatc_user_code 
 Corresponde al parmetro &quot;eatc-id&quot; del punto de donacin que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?_id=&#123;&#123;_id&#125;&#125; 
 eatc_plataform 
 webapp (constante para este llamado) 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
 entero_de_0_a_10 
 input del formulario respectivo 
 eatc_vertical 
 Corresponde al parmetro eatc_cua .vertical de la cuenta especfica (&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua? name =&#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_cua_size 
 Corresponde al parmetro eatc_cua .eatc_cua_size de la cuenta especfica (&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua? name =&#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_licence_type 
 Corresponde al parmetro eatc_cua .eatc_licence_type de la cuenta especfica (&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua? name =&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 Llamado para la edicin&#160; del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma= webapp &amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
 Este llamado se debe realizar cuando se oprime el botn cuyo label es &quot; nps_submit_btn &quot; . 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .&#160; Si no se encuentra registrado por defecto se enviar &quot; en &quot;) 
 eatc_plataform 
 webapp (constante para este llamado) 
 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-dashboard-principal-eatc_pods_dsh%2F2946953406-EmbeddedImage--6-.jpg&ow=1280&oh=657, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-dashboard-principal-eatc_pods_dsh%2F2946953406-EmbeddedImage--6-.jpg&ow=1280&oh=657 
 EatCloud Donantes 

 54.0000000000000 

 DASHBOARD PRINCIPAL: EATC_PODS_DSH