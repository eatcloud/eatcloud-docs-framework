# registro-simple-registro-eatc_pods.aspx

0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

 Mecanismo para habilitar el registro de puntos de donacin en la plataforma a partir de un registro en la misma (dada de alta por parte del usuario final, a diferencia de lo que se manej asta marzo de 2020, en donde esto se realizaba a travs de carga de datos. 

 Registro a cuenta usuario especfica (***NUEVO&#58; cambio de la consulta de eatc_cua hacia datagov***) 

 El registro de punto de donacin se debe generar para una cuenta usuario especfica la cual se debe generar a partir de la URL respectiva&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/registro/&#123;&#123;cua_user&#125;&#125; =&gt; &#123;&#123;URL_entorno_donantes&#125;&#125; /_registro/index.html? &#123;&#123;cua_user&#125;&#125; 

&#160; 
 Ejemplo&#58; 
&#160; 
 Si se van a registrar puntos de donacin para la cuenta &quot; colombia &quot; en ambiente productivo, se debera realizar mediante el vnculo https&#58;//donantes.eatcloud.info/registro/colombia/ &#160; (en pruebas&#58; https&#58;//devdonantes.eatcloud.info/registro/colombia). En una etapa posterior la app deber validar que la cuenta, en este caso &quot;colombia&quot; est registrada en datagov, es decir, que la siguiente consulta&#58;&#160; 

&#160; 
 ***NUEVO*** Validacin de existencia de cuenta para despliegue de formulario 
 &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; (Anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia ) traiga un resultado vlido.&#160; 
&#160; 
 Los datos que trae la consulta de ser exitosa, se deben guardar en una variable, porque sern utilizados posteriormente. 
&#160; 
 Los datos del presente registro se deben guardar en la estructura eatc_pods de la cuenta respectiva, que se consulta mediante la API de la siguiente manera&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/ &#123;&#123;cua_user&#125;&#125; /eatc_pods 

&#160; 
 Para el ejemplo anterior&#58; 
 https&#58;//donantes.eatcloud.info/api/colombia/eatc_pods (en pruebas https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods ) 

 ***NUEVO*** Validacin de tope de puntos de donacin por cuenta 

 Antes de desplegar el formulario, el sistema deber realizar la siguiente consulta, teniendo en cuenta los datos alojados en la informacin de la cuenta y que se consultan mediante este llamado 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123; cua_user &#125;&#125;&amp;_distinct=type 
&#160; 
 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_types_of_licenses? eatc_code =&#123;&#123;eatc_cua. type &#125;&#125;&amp;_distinct= eatc_pods_limit 
&#160; 
 Si esta ltima consulta no trae ningn valor, se utilizar esta consulta por defecto&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_types_of_licenses? eatc_code =free&amp;_distinct= eatc_pods_limit 
&#160; 
 El sistema debe evaluar si el nmero que se obtiene en el parmetro eatc_types_of_licenses. eatc_pods_limit es mayor al valor del count de la siguiente consulta. 

&#160; 
 &#160;Consulta del nmero de puntos de donacin ***ACTIVOS*** por la cuenta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont 
&#160; 
 Si es mayor &#160; (eatc_types_of_licenses. eatc_pods_limit &gt; eatc_pods. eatc_active =y) pasar la Validacin del tipo de licencia para despliegue de pop-up informativo (que se detalla ms adelante). 
&#160; 
 Si es menor o igual (eatc_types_of_licenses. eatc_pods_limit = &lt; eatc_pods. eatc_active =y) &#160; no lo debe dejar pasar al formulario de creacin de punto de donacin, debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuacin, para posteriormente desplegar un popup informativo que a su vez no permitir desplegar el formulario de creacin del pod. 

&#160; 
 Ejemplo &#58; ambiente de pruebas , _DOM. cua_user = oma 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= oma &amp;_distinct=type 
&#160; 
 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =esencial&amp;_distinct= eatc_pods_limit &#160; 
&#160; 
 Dado que el servicio responde&#58; eatc_pods_limit &#58; &quot;1000000&quot; 
&#160; 
 El sistema debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=oma&amp;_cont &#160; 
&#160; 
 Dado que el servicio responde&#58; count &#58; &quot;1&quot; 
&#160; 
 Dado que (eatc_types_of_licenses. eatc_pods_limit &gt; eatc_pods. eatc_active =y)&#58; &quot;1000000&quot; &gt; &quot;1&quot;, entonces se debe mostrar el formulario de registro del POD . 

&#160; 
 ***NUEVO&#58; Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events )*** 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_pods_limit 
 eatc_user = anonymous_web_user 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_pods_limit 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = eatc_pods_limit &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free &#160; 
&#160; 
 Una vez se realiza el registro en la estructura de &quot;upgrade_events&quot; se despliega el siguiente mensaje y no permite seguir adelante con el formulario 
&#160; 
 Tu cuenta EatCloud con el plan rescate (concat) &#123;&#123;plan_rescate&#125;&#125; (concat) ha llegado al lmite de puntos de donacin.&#160; Por favor comuncate con el administrador del sistema para realizar una actualizacin de licencia y as poder registrar ms puntos de donacin. 
 class= lbl_tu_cuenta_con_plan_rescate ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_cuenta_con_plan_rescate )&#160;&#160;&#160; 
&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125; (en el ejemplo &quot;Activo&quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
&#160; 
 class= lbl_limite_pods ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_limite_pods )&#160; &#160; 

&#160; 
 ***NUEVO&#58; Validacin del tipo de licencia para despliegue de pop-up informativo por registro de nuevo pod*** 
 Si la licencia es diferente a &quot;free&quot;, es decir si eatc_cua. type &#160; es &quot; esencial &quot;, &quot; activo &quot;, &quot; impacto &quot;, entonces el sistema deber desplegar, antes de direccionar al formulario de ingreso del nuevo punto de donacin un pop-up de la siguiente manera&#58; 

 Tu cuenta EatCloud con el plan rescate (concat) &#123;&#123;plan_rescate&#125;&#125; (concat) tiene (concat) &#123;&#123;numero_pods&#125;&#125; (concat) punto(s) de donacin activo(s) 
 class= lbl_tu_cuenta_con_plan_rescate ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_cuenta_con_plan_rescate )&#160;&#160;&#160; 
&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125; (en el ejemplo &quot;Activo&quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 class= lbl_tiene ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tiene ) &#160;&#160; 
&#160; 
 &#123;&#123;numero_pods&#125;&#125; (en el ejemplo &quot; 1 &quot;) 
 &#123;&#123; URL_entorno_donantes &#125;&#125;api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 class= lbl_pods_activos_2 ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_pods_activos_2 )&#160;&#160; 
&#160; 
 Al adicionar un nuevo punto de donacin actualizaremos la informacin de puntos de donacin de tu plan rescate (concat) &#123;&#123;plan_rescate&#125;&#125; (concat) EatCloud. Vers el cambio reflejado en tu factura. 
 class= lbl_al_adicionar_pod ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_al_adicionar_pod )&#160;&#160;&#160; 
&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125; (en el ejemplo &quot;Activo&quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 class= lbl_veras_cambio_en_factura ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_veras_cambio_en_factura )&#160;&#160; 

&#160; 
 Cancelar 
 class= lbl_cancelar ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cancelar )&#160;&#160; 
&#160; 
 Este botn devuelve a la pgina de ingreso al Nuevo BO&#58;&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/_dgbo/#!/start 
&#160; 
 (sin abrir el formulario de creacin del punto) pero permitiendo ver el listado y editar puntos. 
&#160; 
&#160; 
 Continuar 
 class= lbl_continuar ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_pods&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_continuar )&#160; 
&#160; 
 Este botn abre el formulario de creacin de nuevo punto de donacin descrito a continuacin 

 Campos para el registro 

 Los campos de captura se disponen en el siguiente orden. 
&#160; 
 Identificador nico del punto de donacin ***Nuevo&#58; campo de captura de texto *** 
 Place holder&#58; 
 class=&quot; lbl_pod_id &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =ONB_pods&amp;idlabel=lbl_pod_id )&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pod_id_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =ONB_pods&amp;idlabel=lbl_pod_id_desc )&#160; 
&#160; 
 &quot;Ingresa un identificador nico para tu punto de donacin. Este identificador no se puede repetir en tu organizacin. Si no ingresas un valor, nuestro sistema te asignar un identificador para el punto de donacin que ests registrando&quot; 
&#160; 
 Valor por defecto para el cuadro de texto&#58; 
 Ninguno (es decir, debe mostrar el place holder) 
&#160; 
 Validacin para el cuadro de texto&#58; 
 Se deber validar que la combinacin entre&#160; el input que se est realizando ( eatc-pod_id ) y la cuenta usuario ( _DOM. cua_user ), sea nica en el objectstore allpods de la siguiente manera 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/ allpods /eatc_pods?eatc-id=&#123;&#123; text_input &#125;&#125;&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cmp=eatc-id,eatc-name 
&#160; 
 Si la anterior consulta trae un resultado, quiere decir que el id que se est ingresando ya est utilizado por lo tanto el sistema debe desplegar un mensaje de alerta&#58; 
 class=&quot; lbl_pod_id_duplicado_intro &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =ONB_pods&amp;idlabel=lbl_pod_id_duplicado_intro )&#160; 
 concat 
 &#123;&#123;eatc_pods. eatc-name &#125;&#125; 
 concat 
 class=&quot; lbl_pod_id_duplicado_intentalo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =ONB_pods&amp;idlabel=lbl_pod_id_duplicado_intentalo )&#160; 
&#160; 
 &quot;El identificador ingresado ya est siendo utilizado por otro punto de donacin de tu organizacin (&#123;&#123;eatc_pods. eatc-name &#125;&#125;). Por favor intntalo de nuevo&quot; 
&#160; 
 Y se debe limpiar el campo de captura para que el usuario intente de nuevo. 
 Si el usuario no ingresa un dato en este campo de captura, el sistema debe generar el identificador (como lo vena haciendo en segundo plano). 
&#160; 
 El texto digitado se lleva&#58; 
 Se debe guardar en una variable ( eatc-id ) para posteriormente realizar los respectivos registros. 
&#160; 
 Nombre el punto de donacin&#58; text_field, obligatorio (eatc-name) 
 Responsable&#58; text_field, obligatorio (eatc-responsable) 
 Telfono&#58; tel, obligatorio (eatc-phone) 

 Correo electrnico&#58; email, obligatorio (eatc-email) 
&#160; 
 Datos asociados con la localizacin (se debe solicitar permiso para identificar la geoposicin y localizar en el mapa, a partir de esta geolocalizacin se debe sugerir lo siguiente. 
 eatc-lat &#58; oculto, de acuerdo a lo seleccionado en el mapa (separador punto), 
 eatc-lon &#58; oculto, de acuerdo a lo seleccionado en el mapa (separador punto). 

&#160; 
 ***NUEVO***Coordenada por defecto cuando no se logra obtener una desde el navegador&#58; dinmica de acuerdo al pas 
 Si el sistema no logra obtener una coordenada desde el navegador, debe proporcionar unas coordenadas por defecto, con un zoom por defecto que se determina por pas realizando la siguiente consulta&#58; 
&#160; 
 A partir de la consulta genrica&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua&#125;&#125; 
&#160; 
 El sistema toma el dato eatc_cua. eatc-country y luego se procede a realizar la siguiente consulta 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2=&#123;&#123;eatc_cua. eatc_country &#125;&#125; 
&#160; 
 La coordenada por defecto corresponde a los parmetros eatc_countries. eatc_lat y eatc_countries. eatc_lon y el zoom aplicable al mapa al parmetro eatc_countries. eatc_zoom . Este zoom debe ser calibrado de tal manera que permita visualizar la mayor parte del pas (en este caso Colombia) en el mapa que utiliza el formulario, ya que el valor que en este momento est en eatc_countries corresponde a un dato extractado de google maps.&#160; El desarrollador deber establecer el valor de zoom adecuado para el mapa y registrarlo en el API. 
 &#160;https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_countries&amp;_operacion=update&amp;eatc_zoom=&#123;&#123; valor_calibrado &#125;&#125;&amp;WHEREiso2=co 

&#160; 
 ***NUEVO***Mensaje cuando se despliega la coordenada por defecto 
 &#160;Cuando se despliegue esta coordenada por defecto se deber mostrar arriba del mapa un mensaje de alerta que contenga el siguiente label&#58; 
 class=&quot; lbl_coordenada_por_defecto &quot; 

 Cundo la coordenada por defecto vare (la coordenada por defecto se estableci en medio de un parque as que se deber variar para colocar un punto vlido), el mensaje de alerta ocultarse de inmediato. 

 Direccin &#58; Sugerida de acuerdo a la seleccin del mapa, pero editable&#58; text_field obligatorio&#160; ( eatc-adress ) 

&#160; 
 ***NUEVO*** PAS TOMADO DE LA CONFIGURACIN DE EATC_CUA 

 Pas&#58;&#160; &#160; 
&#160; 
 A partir de la consulta genrica&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua&#125;&#125; 
&#160; 
 El sistema toma el dato eatc_cua. eatc-country&#160; para incorporarlo en este parmetro (eatc-pods. eatc-country ) 

&#160; 
 Selector de &quot;Provincias, departamentos, estados&quot; y luego de &quot;Ciudades&quot; genrico segn el pas de la cuenta y validando informacin de los selectores con la coordenada previamente seleccionada ****NUEVO&#58; dinamizando el radio de consulta segn cuenta maestra**** 
 Para poder popular el&#160; 
 1. Determinacin del pas de la cuenta maestra, para a partir del mismo consultar los datos maestos de municipalidades&#58; 
&#160; 
 A partir de la consulta genrica&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125; 
&#160; 
 El sistema toma los siguientes datos&#160; 
 eatc_cua_master. eatc-country&#160; &#160; 

 eatc_cua_master. eatc_geo_query_radius_km 
&#160; 
 Para realizar la siguiente consulta. 
&#160; 
 Ejemplo Argentina ambiente de pruebas&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=argentina ( 
 eatc_cua_master. eatc-country = ar 

 eatc_cua_master. eatc_geo_query_radius_km =&#160; (vaco) 
&#160; 
 Ejemplo Mxico ambiente de pruebas 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=mexico &#160; 
 eatc_cua_master. eatc-country = mx 
 eatc_cua_master. eatc_geo_query_radius_km = 25 

&#160; 
 2. Determinacin de la provincia (eatc-province) segn el maestro eatc_municipalities respectivo y sus coordenadas 
&#160; 
 Con los datos recolectados se realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /get/&#123;&#123;eatc_cua_master.eatc-country&#125;&#125;/getpuntos?table=eatc_municipalities&amp;fieldname=eatc-lat,eatc-lon&amp;fieldvalue=&#123;&#123;latitud_seleccionada_mapa&#125;&#125;,&#123;&#123;longitud_seleccionada_mapa&#125;&#125;&amp;showfield= eatc-province &amp;km=&#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; 
&#160; 
 Si la consulta del dato &#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; arroja un dato vacio, nulo, o en cero, el valor por defecto sera &quot; 15 &quot;&#160; 
&#160; 
 Ejemplo Argentina ambiente de pruebas&#58; 
 https&#58;//dev.datagov.eatcloud.info/get/ar/getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =-34.6156624,-58.50351&amp; showfield = eatc-province &amp; km = 15 
&#160; 
 Ejemplo Mxico ambiente de pruebas 
 https&#58;//dev.datagov.eatcloud.info/get/mx/getpuntos?table=eatc_municipalities&amp;fieldname=eatc-lat,eatc-lon&amp;fieldvalue=19.4410303,-99.2000994&amp;showfield=eatc-province&amp;km= 25 &#160; 

&#160; 
 El sistema debe tomar el dato eatc_municipalies. eatc-province ( haciendo un distinct sobre las respuestas obtenidas ) para incorporarlo al selector. 
&#160; 
 3. Determinacin de la ciudad segn el maestro eatc_municipalities y la seleccin previa de departamento 
&#160; 
 A partir de la seleccin anterior se debe realizar la siguiente consulta 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /get/&#123;&#123;eatc_cua_master. eatc-country &#125;&#125;/getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =&#123;&#123;latitud_seleccionada_mapa&#125;&#125;,&#123;&#123;longitud_seleccionada_mapa&#125;&#125;&amp; showfield = eatc-city &amp; km =&#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; 
 &amp;filterfield_1= eatc-province &amp;filtervalue_1= &#123;&#123; eatc-province_seleccionada &#125;&#125; 
&#160; 
 Si la consulta del dato &#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; arroja un dato vacio, nulo, o en cero, el valor por defecto sera &quot; 15 &quot;&#160; 
&#160; 
 El sistema debe tomar el dato eatc_municipalies. eatc-city ( haciendo un distinct sobre las respuestas obtenidas ) para incorporarlo al selector. 

&#160; 
 Ejemplo (ambiente de pruebas) 
&#160; 
 Suponiendo que para la cuenta maestra abaco , un usuario cuya latitud ( eatc-lat ) es&#58; 6.2045697, y longitud ( eatc-lon ) es&#58; -75.60157 (previamente seleccionadas en el mapa), entonces el sistema deber como primera medida realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco &#160; 
&#160; 
 la cual determina que eatc_cua_master. eatc-country es &quot;co&quot; y &quot; eatc_cua_master. eatc_geo_query_radius_km&quot; es 15 
&#160; 
 Por lo tanto el sistema realiza la siguiente consulta para determinar los datos del selector de departamentos&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/get/ co /getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =6.2045697,-75.60157&amp; showfield = eatc-province &amp; km = 15 &#160; 
&#160; 
 Como el sistema arroja la siguiente informacin&#58; 
 eatc-province &#58; &quot;ANTIOQUIA&quot; (93 veces) 
 El sistema debe colocar en el selector de &quot;Provincia, departamento, estado&quot; &quot;ANTIOQUIA&quot; (una sola vez, porque hace distinct sobre el dato eatc-province ) 
&#160; 
 Posteriormente, cuando el usuario seleccione el departamento (si es uno solo se puede realizar una seleccin automtica) con este dato se procede a generar la informacin para el selector de ciudad&#58;&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/get/ co /getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =6.2045697,-75.60157&amp; showfield = eatc-city &amp; km =1 5 &amp;filterfield_1= eatc-province &amp;filtervalue_1= ANTIOQUIA &#160;&#160;&#160; 
&#160; 
 Como el sistema arroja la siguiente informacin&#58; 
&#160; 

 eatc-city &#58; &quot;MEDELLIN&quot; (26 veces), &quot;ENVIGADO&quot; (23 vez), e &quot;ITAGUI&quot; (7 veces), LA ESTRELLA (10), EL RETIRO (3),SABANETA (9) 
&#160; 
 El sistema debe colocar en el selector de &quot;Ciudad&quot; &quot;MEDELLIN,ENVIGADO,ITAGUI,LA ESTRELLA,EL RETIRO,SABANETA&quot; (una sola vez cada ciudad, porque hace distinct sobre el dato eatc-city ) 
&#160; 
 Ejemplo argentina en pruebas (con datos de ejemplo anterior) 
&#160; 
 Como el sistema no arroja datos en la consulta de &#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; entonces se coloca el valor por defecto de 15 KM 
 https&#58;//dev.datagov.eatcloud.info/get/ ar /getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =-34.6156624,-58.50351&amp; showfield = eatc-city &amp; km = 15 &amp;filterfield_1= eatc-province &amp;filtervalue_1= Buenos%20Aires &#160; &#160; &#160; 
&#160; 
 Ejemplo&#58; mexico en pruebas (con datos de ejemplo anterior) 
 Como el sistema arroja en la consulta de &#123;&#123;eatc_cua_master. eatc_geo_query_radius_km &#125;&#125; el dato &quot; 25 &quot; entonces se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/get/ mx /getpuntos? table =eatc_municipalities&amp; fieldname =eatc-lat,eatc-lon&amp; fieldvalue =19.4410303,-99.2000994&amp; showfield = eatc-city &amp; km = 25 &amp;filterfield_1= eatc-province &amp;filtervalue_1= Ciudad%20de%20Mxico &#160; 

&#160; 
 ****NUEVO&#58; selector de tamao del punto de donacin**** 
 El sistema desplegar un selector nico&#160; para que el usuario pueda registrar el tamao del punto de donacin (el selector deber mostrar una descripcin), segn la respectiva vertical. El usuario deber elegir uno de los tamaos y esta informacin se adjuntar en la informacin del respectivo punto de donacin 
 Label&#58; class= &quot;lbl_pod_size&quot; 
 Informacin tcnica del parmetro&#58; eatc_pods. eatc-size 
 Tipo de dato&#58; string 
 Tipo de input&#58; Selector nico 
 La informacin del selector se toma de&#58; 

&#160; 
 *** NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 
&#160; 
 ***NUEVO&#58; Paso 2&#58; consulta de los tamaos de puntos de donacin para la vertical de la cuenta respectiva (con su respectiva descripcin)&#58;&#160; 
 Con&#160; el dato eatc_cua .vertical de la _DOM. cua_user respectiva, se debe realizar la consulta al maestro de tamaos de puntos de donacin para traer los tamaos y sus descripciones, que le aplican a la cuenta particular. 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_pods_size_mt?eatc_vertical_code=&#123;&#123;eatc_cua. vertical &#125;&#125; 
&#160; 
 El sistema toma el array de valores del parmetro eatc_pods_size_mt . _id para realizar la siguiente consulta 
&#160; 
 ***NUEVO&#58; Paso 3&#58; consulta de los tamaos en datos internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125;&amp;eatc_mt= eatc_pods_size_mt &amp; eatc_data_id=&#123;&#123;array( eatc_pods_size_mt . _id)&#125;&#125; 

&#160; 
 Ejemplo&#58; idioma espaol para la vertical &quot;retail&quot; a 3 de diciembre de 2020&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_pods_size_mt?eatc_vertical_code=retail &#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=es&amp;eatc_mt=eatc_pods_size_mt&amp;eatc_data_id=1,2,3,4,5 &#160; 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto (ingls=en idioma por defecto)&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_pods_size_mt &amp;eatc_language= en &amp;eatc_data_id= &#123;&#123;array( eatc_pods_size_mt. _id)&#125;&#125; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en los selectores&#58; &#123;&#123;eatc_name&#125;&#125;&#58; &#123;&#123;eatc_description&#125;&#125; 
 Ejemplo&#58; idioma espaol a 3 de diciembre de 2020, vertical retail&#58; 
 Se mostraran los selectores con los siguientes labels 
 Mini Mercado&#58; de 0 a 2000 m 
 Mercado&#58;&#160; de 2001 a 4000 m 
 Supermercado&#58;&#160; de 4001 a 9000 m 
 Hipermercado&#58; mayor a 9000 m 

 Cedi Retail&#58; Centro de Distribucin 
&#160; 
 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_pods_size_mt?_id=&#123;&#123; eatc_internationalize_dt. eatc_int_data_id &#125;&#125; para llevar al registro el valor eatc_pods_size_mt. eatc_code 
&#160; 
 Ejemplo, continuando con el anterior 
 Si el usuario selecciona &quot; Hipermecado &quot; entonces eatc_internationalize_dt. eatc_data_id= 4 por lo tanto al hacer la siguiente consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_pods_size_mt?_id=4 al registro se llevara el valor &quot; eatc_pods. eatc-size &quot; = &quot; hipermercado &quot; 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods? eatc-size =&#123;&#123; eatc_pods_size_mt. eatc_code &#125;&#125; 
 Se guarda con &#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_user &#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp; eatc-size =&#123;&#123; eatc_pods_size_mt. eatc_code &#125;&#125;&amp;WHERE eatc-id =&#123;&#123;eatc_pods. eatc-id &#125;&#125; 

&#160; 
 ***NUEVO&#58; configuracin de tipologas a medida que se van incorporando a los puntos de donacin*** 
 Situacin actual&#58; 
 Las tipologas se toman de maestros que deben estar precargados en la plataforma. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/ eatc_pods_typolgy_a ?_id=_* 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/ eatc_pods_typolgy_b ?_id=_* 
&#160; 
 Mejora propuesta&#58; 
 Con el nimo de mejorar la experiencia de usuario y no tener que realizar una precarga de maestros, se propone que para ciertos tipos de licencias (diferentes de la licencia &quot;free&quot;), se permita ir llenando los maestros de tipologas, a medida que se van agregando los puntos de donacin. Tambin, cuando se opere por primera vez la funcionalidad de agregar puntos de donacin, se preguntar el nombre de la primera y segunda tipologa de los pods, para utilizar dicha etiqueta en adelante a lo largo de la interfaz de usuario. 
&#160; 
 ***NUEVO***Despliegue de la funcionalidad de configuracin&#58; 
 La funcionalidad de configuracin de cada tipologa ( eatc_pods_typolgy_a,eatc_pods_typolgy_b ) se desplegar para usuarios con licencias diferentes a la free , por lo tanto, por lo tanto se deber establecer el tipo de licencia de la cuenta y si la misma es diferente a &quot;free&quot; se desplegar el selector con capacidades de configuracin . 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp; eatc_cua_master=&#123;&#123; _DOM.cua_master&#125;&#125; type =!free 
&#160; 
 Si el tipo de licencia es free, entonces se evala si existe informacin (o si existen los maestros) de tipologas&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/ eatc_pods_typolgy_a ?_id=_* 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/ eatc_pods_typolgy_b ?_id=_* 
&#160; 
 Si no existen, o no tienen informacin, el sistema no despliega los selectores y por lo tanto deja sin registro el o los campos respectivos ( eatc-pods. eatc_pods_typolgy_b, eatc-pods. eatc_pods_typolgy_b ). 
&#160; 
 Si existen los repositorios y tienen registros, entonces se despliega el selector sin capacidades de configuracin . 
&#160; 
 Si la licencia es diferente a Free, se se desplegar el selector con capacidades de configuracin , pero antes se deber realizar la validacin respectiva para el despliegue de de la configuracin de las etiquetas &quot;lbl_eatc_pods_typolgy_a&quot; y &quot;lbl_eatc_pods_typolgy_b&quot;. 
&#160; 
 ***NUEVO***Despliegue de la funcionalidad de configuracin cuando se accede por primera vez&#58; configuracin de las etiquetas &quot;lbl_eatc_pods_typolgy_a&quot; y &quot;lbl_eatc_pods_typolgy_b&quot; 
&#160; 
 En vez del copy que se est desplegando como etiqueta para esta funcionalidad (ver etiqueta resaltada para el caso de&#58; https&#58;//donantes.eatcloud.info/_registro/index.html?colombia en imagen abajo adjunta) 

 Debern ir los siguientes ids (esto se implement con esta tarea ). 
 lbl_eatc_pods_typolgy_a ( en lo que en la imagen arriba se muestra como tipo de donante) 
 lbl_eatc_pods_typolgy_b ( en lo que en la imagen arriba se muestra como tipo de contribucin) 
&#160; 
 El sistema debe realizar la siguiente consulta, para determinar si existen registros vlidos para estas etiquetas de la siguiente manera&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_a 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_b 
&#160; 
 Si el idioma del browser, no se encuentra en el siguiente registro&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* 
&#160; 
 Entonces por defecto al consulta ser&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= en &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_a 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= en &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_b 
&#160; 
 Si la consulta arroja un registro vlido, el sistema debe desplegar esa informacin en el label respectivo (con la configuracin del label el sistema ya realiza esto de manera automtica).&#160;&#160; 
&#160; 
 De no ser as el sistema (no se obtiene informacin con la consulta) deber desplegar campos de captura que le pregunte al usuario, respectivamente lo siguiente (que debe configurarse como un label, para su internacionalizacin&#58; 
 &#160;lbl_non_pods_typology_a_alert [text_input_field]&#160; 
&#160; 
 Al configurar el label (como un id) en vez de quemarlo en el cdigo el sistema, de manera automtica deber desplegar la informacin que se tiene almacenada en&#160; &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125;&amp; plataforma =ONB_PODS &amp;idlabel= lbl_non_pods_typology_a_alert 
&#160; 
 La anterior consulta (a 4 de diciembre de 2020) en idioma espaol trae la siguiente informacin&#58; &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= es&amp; plataforma =ONB_PODS &amp;idlabel= lbl_non_pods_typology_a_alert 
&#160; 
 Cmo llamars a la primera clasificacin de tus puntos de donacin? algunas empresas llaman por ejemplo a esta clasificacin&#58; marca, distrito, departamento, etc... (llmala como ms se ajuste a tus necesidades y posteriormente te servir para visualizar informacin por esta clasificacin) 
&#160; 
 Que deber estar antes de un campo de captura de texto ( text_input_field ) para que el usuario entregue el nombre de la tipologa que se le est solicitando, siguiendo esta regla de obligatoriedad&#58;&#160; 
 Obligatoriedad &#58; si, si la cuenta es diferente a &quot; free &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp; eatc_cua_master=&#123;&#123; _DOM.cua_user&#125;&#125; type =!free) se solicita el dato de manera obligatoria, para la cuenta free no es obligatorio incorporar el dato. 

&#160; 
 lbl_non_pods_typology_b_alert [text_input_field]&#160; 
&#160; 
 Al configurar el label (como un id) en vez de quemarlo en el cdigo el sistema, de manera automtica deber desplegar la informacin que se tiene almacenada en&#160; &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= &#123;&#123;iso2_idioma_browser&#125;&#125;&amp; plataforma =ONB_PODS &amp;idlabel= lbl_non_pods_typology_a_alert 
&#160; 
 La anterior consulta (a 4 de diciembre de 2020) en idioma espaol trae la siguiente informacin&#58; &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= es&amp; plataforma =ONB_PODS &amp;idlabel= lbl_non_pods_typology_a_alert &#160; 
&#160; 
 Cmo llamars a la segunda clasificacin de tus puntos de donacin? por ejemplo algunas empresas llaman a esta clasificacin&#58; distrito, subzona, municipio, etc... (llmala como ms se ajuste a tus necesidades y posteriormente te servir para visualizar informacin por esta clasificacin) 
&#160; 
 Que deber estar antes de un campo de captura de texto ( text_input_field ) para que el usuario entregue el nombre de la tipologa que se le est solicitando, de manera opcional 
&#160; 
 El usuario entregar en el campo de captura de texto la informacin del nombre de la tipologa a y la tipologa b y el sistema proceder a realizar el los siguientes registros (a diciembre 4 de 2020 dos registros por cada tipologa, diferenciados por el campo plataforma 
 lbl_eatc_pods_typolgy_a 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp; &amp; plataforma =ONB_PODS&amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_a&amp; comportamiento =clase 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp;plataforma =donantes&amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_a&amp; comportamiento =clase 
&#160; 
 ***NUEVO REGISTRO PARA DATAGOV_CUENTAS*** 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp;plataforma = datagov_cuentas &amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_a&amp; comportamiento =clase 
&#160; 
&#160; 
&#160; 
 lbl_eatc_pods_typolgy_b 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp; &amp; plataforma =ONB_PODS&amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_b&amp; comportamiento =clase 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp; &amp; plataforma =donantes&amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_b&amp; comportamiento =clase 
&#160; 
 ***NUEVO REGISTRO PARA DATAGOV_CUENTAS*** 
 &#123;&#123; URL_entorno_datagov &#125;&#125; /crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= &#123;&#123;iso2_idioma_browser&#125;&#125; &amp;cua= &#123;&#123; eatc_cua. name&#125;&#125; &amp;copy= &#123;&#123;INPUT&#125;&#125; &amp;plataforma = datagov_cuentas &amp; lastupdate= &#123;&#123;timestamp AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; idlabel= lbl_eatc_pods_typolgy_b&amp; comportamiento =clase 
&#160; 

&#160; 
 Ejemplo registro en la cuenta prueba ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=prueba ) desde un browser con idioma espaol=es&#58;&#160; 
&#160; 
 Como el idioma est configurado en la plataforma ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages? iso2 =es ) 
&#160; 
 Entonces se realizan las siguientes bsquedas&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= en &amp;cua= prueba &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_a 
 &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?lang= en &amp;cua= prueba &amp;plataforma =ONB_PODS &amp;idlabel= lbl_eatc_pods_typolgy_b 
&#160; 
 Cmo el sistema no arroja resultados, el formulario debe preguntar (El usuario responde lo que est despus de =&gt;)&#58; 
&#160; 
 Cmo llamars a la primera clasificacin de tus puntos de donacin? por ejemplo algunas empresas llaman a esta clasificacin&#58; distrito, subzona, municipio, etc... (llmala como ms se ajuste a tus necesidades y posteriormente te servir para visualizar informacin por esta clasificacin) 
&#160; 
 =&gt; MARCA 
&#160; 
 Cmo llamars a la segunda clasificacin de tus puntos de donacin? por ejemplo algunas empresas llaman a esta clasificacin&#58; distrito, subzona, municipio, etc... (llmala como ms se ajuste a tus necesidades y posteriormente te servir para visualizar informacin por esta clasificacin) 
&#160; 
 =&gt; El usuario no entrega un nombre para esta clasificacin 
&#160; 
 Entonces el sistema debe proceder a realizar los siguientes registros&#58; 
&#160; 
 lbl_eatc_pods_typolgy_a 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= es &amp;cua= prueba &amp;copy= marca &amp;plataforma =ONB_PODS&amp; lastupdate= 2020-12-04%2012&#58;29&#58;00&amp; idlabel= lbl_eatc_pods_typolgy_a 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_config_labels&amp;_operacion= insert &amp;lang= es &amp;cua= prueba &amp;copy= marca &amp;plataforma =donantes&amp; lastupdate= 2020-12-04%2012&#58;29&#58;00&amp; idlabel= lbl_eatc_pods_typolgy_a 
&#160; 
&#160; 
 lbl_eatc_pods_typolgy_b 
&#160; 
 Como el usuario no entrega un nombre no se realiza el registro 

 ***NUEVO&#58; CAMBIO EN LA OBLIGATORIEDAD***Despliegue del selector con capacidades de configuracin&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc_pods_typolgy_a y eatc_pods.eatc_pods_typolgy_b 
 Tipo de dato&#58; string 
 TIpo de input de datos &#58; selector nico con texto predictivo y capacidades de ingresar valores nuevos (que no estn en el listado maestro de datos&#160; de los cuales se nutre el selector) a travs de &quot;text input&quot;. 
 Obligatoriedad &#58; 
 eatc_pods.eatc_pods_typolgy_a &#160; si, si la cuenta es diferente a &quot; free &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp; eatc_cua_master=&#123;&#123; _DOM.cua_user&#125;&#125; type =!free ) 
 eatc_pods.eatc_pods_typolgy_b &#58; no 
 Validacin &#58; obligatoriedad, y que no se repitan datos en los maestros eatc_pods_typolgy_a y eatc_pods_typolgy_b 
 La informacin se toma de&#58; 
 eatc_pods.eatc_pods_typology_a 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods_typolgy_a?_id=_* 
&#160; 
 eatc_pods.eatc_pods_typology_b 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods_typolgy_b?_id=_* 
&#160; 
 El usuario puede digitar un valor en el input diferente a los que se traen del maestro y en este caso se actualiza la informacin del eatc_pod y tambin se actualiza la informacin del maestro respectivo de tipologas (eatc_pods_typolgy_a / eatc_pods_typolgy_b) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods? eatc-typology_a =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_pods? eatc-typology_b =&#123;&#123;input&#125;&#125; 
 [+++] Cuando se ingresa un valor que no est presente en el maestro respectivo ( eatc_pods_typolgy_a y eatc_pods_typolgy_b ), este valor se lleva al maestro a partir de la siguiente escritura &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_user&#125;&#125;/?_tabla= eatc_pods_typolgy_a &amp;_operacion= insert &amp; eatc_code= &#123;&#123;input_sin_caracteres_especiales_y_espacios&#125;&#125;&amp; eatc_name= &#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_user&#125;&#125;/?_tabla= eatc_pods_typolgy_b &amp;_operacion= insert &amp; eatc_code= &#123;&#123;input_sin_caracteres_especiales_y_espacios&#125;&#125;&amp; eatc_name= &#123;&#123;input&#125;&#125; 

&#160; 
 ***NUEVO&#58; CAMBIO EN LA OBLIGATORIEDAD***Despliegue del selector sin capacidades de configuracin&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc_pods_typolgy_a y eatc_pods.eatc_pods_typolgy_b 
 Tipo de dato&#58; string 
 TIpo de input de datos &#58; selector nico. 
 Obligatoriedad &#58; 
 eatc_pods.eatc_pods_typolgy_a &#160; si, si la cuenta es diferente a &quot; free &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp; eatc_cua_master=&#123;&#123; _DOM.cua_user&#125;&#125; type =!free ) 
 eatc_pods.eatc_pods_typolgy_b &#58; no 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods.eatc_pods_typology_a 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods_typolgy_a?_id=_* 
&#160; 
 eatc_pods.eatc_pods_typology_b 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods_typolgy_b?_id=_* 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods? eatc-typology_a =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_pods? eatc-typology_b =&#123;&#123;input&#125; 

&#160; 
 *** HASTA AQU MEJORA DE TIPOLOGAS*** 
 (por el momento se puede dejar vaco, mientras lo definimos) eatc-dona_packing &#58; &quot;Cajas Bolsas Garrafas&quot;, 
 Nombre de usuario&#58; text_field obligatorio (login) 
 Contrasea&#58; password, obigatorio con validacin de fortaleza (password ), se debe procurar guardarlo hasheado y permitir que la webapp de donantes lo valide hasheado. 

 Botn &quot;Registrar punto de donacin&quot; 
 ***NUEVO***Validacin coordenada por defecto 
 Si el sistema detecta que la coordenada por defecto no fue cambiada por el usuario en el mapa,&#160; deber mostrar un modal que le informe de esta situacin (impidiendo el registro de los datos en la base de datos) y&#160; que lo invitar a cambiar la coordenada en el mapa.&#160; El modal deber tener la siguiente informacin&#58; 
 Ttulo del modal 
 class=&quot; lbl_por_favor_cambia_tu_ubicacion &quot; 
 Cuerpo del modal 
 class=&quot; lbl_por_favor_cambia_tu_ubicacion_desc &quot; 
 Vnculo o botn del modal 
 class=&quot; lbl_actualizar_ubicacion &quot; 
 Este vnculo debe cerrar el modal y retornar al usuario al ancla del mapa, para que pueda realizar el cambio de la ubicacin de manera ms fcil. 
 Hasta que el usuario no cambie la coordenada no se le permitir realizar el registro de los datos. 

&#160; 
 Validacin de coordenada ***REVISAR*** con la implementacin de la validacin del municipio y departamento con la coordenada es posible que no se requiera esta validacin, si se requiere se debe apuntar al maestro de municipalidades en datagov 
 Dada la circunstancia que nos estn ingresando coordenadas al sistema que no corresponden a las direcciones, municipios y departamentos registrados, se hace necesario establecer un mecanismo de validacin que ayude a garantizar en alguna medida calidad con los datos de georeferenciacin desde la fuente. 
 La validacin operara de la siguiente manera&#58; 
 Se toman las coordenadas registradas en el formulario&#58; coordenadas y se guardan en variables ( lat1,lon1 ) 
 Con el dato ciudad (centro poblado) y sus respectivos cdigos se consulta la coordenada asociada a este punto 
 https&#58;//datagov.eatcloud.info/api/&#123;&#123;eatc_cua. eatc-country &#125;&#125;/eatc_municipalities?eatc-city=&#123;&#123;ciudad_seleccionada&#125;&#125; 
 Si la consulta arroja varios resultados, se debe refinar con el siguiente llamado&#58; 
 https&#58;//datagov.eatcloud.info/api/&#123;&#123;eatc_cua_master. eatc-country &#125;&#125;/eatc_municipalities?eatc-city=&#123;&#123;ciudad_seleccionada&#125;&#125;&amp;eatc-populated_center_type=CABECERA%20MUNICIPAL 

&#160; 
 Ejemplo&#58; 
 Para una seleccin de la cabecera municipal de Medelln, la consulta sera as&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/co/eatc_municipalities?eatc-city=MEDELLIN &#160; 
&#160; 
 Como la bsqueda da respuesta mltiple, entonces se refina con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/co/eatc_municipalities?eatc-city=MEDELLIN&amp;eatc-populated_center_type=CABECERA%20MUNICIPAL &#160; 
&#160; 
 de esta consulta se toman los datos eatc-lat y eatc-lon y se guardan en variables ( lat2,lon2 ). 
&#160; 
 Con el siguiente script se calcula la distancia entre estas dos coordenadas&#58; 
&#160; 
 function getKilometros(lat1,lon1,lat2,lon2)&#123; 
 &#160;rad = function(x) &#123;return x*Math.PI/180;&#125; 
 &#160;&#160;&#160;//var R = 6378.137; //Radio de la tierra en km 
 &#160;&#160;&#160;var R = 63781; //Radio de la tierra en km 
 &#160;&#160;&#160;var dLat = rad( lat2 - lat1 ); 
 &#160;&#160;&#160;var dLong = rad( lon2 - lon1 ); 
 &#160;&#160;&#160;var a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(dLong/2) * Math.sin(dLong/2); 
 &#160;&#160;&#160;var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
 &#160;&#160;&#160;var d = R * c; 
 &#160;&#160;return d.toFixed(3); //Retorna tres decimales 
 &#160;&#125; 
&#160; 
 Si la distancia es mayor a 50 KM para ciudades principales y 20 KM para ciudades pequeas (o en general 50 KM), se debe mostrar el siguiente anuncio&#58; 
&#160; 
 La coordenada registrada parece estar muy distante del municipio seleccionado.&#160; Le solicitamos el favor revise el &quot;pin&quot; en el mapa e intente nuevamente realizar el registro. 
&#160; 
 Y no debe permitir realizar el registro. Si la distancia es menor a la estipulada, se debe dejar pasar. 

&#160; 
 Realizacin del registro en la base de datos de donantes 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado &#160; para la incorporacin de la informacin&#160; 
 Mtodo POST &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla= eatc_pods &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 

&#160; 
 ****NUEVO**** Llamado al servicio de creacin de configuracin de funcionalidades en AllPods (llamado con plan= free ) 
 Dado que en el nuevo esquema de licenciamiento se elimina el tipo de licencia free_trial y se deja solamente la &quot;free&quot;, se debe revisar el llamado que anteriormente se haca con plan= free_trial y hacerlo con plan= free 
&#160; 
 Al presionar este botn el formulario debe realizar tambin el siguiente llamado al servicio desarrollado para este fin 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/allpods/pods_default_features?eatc-cua=&#123;&#123; _DOM .cua_user &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;plan= free 

 Anteriormente&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/allpods/pods_default_features?eatc-cua=&#123;&#123; _DOM .cua_user &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;plan= free_trial 
&#160; 
 ****NUEVO**** Al terminar el formulario&#58; modal para redireccin 
 (ANTERIORMENTE&#58; Mostrado el mensaje se debe redireccionar a la landing&#58; https&#58;//www.eatcloud.com/donantes-inscritos/ y Posteriormente se deber configurar la funcionalidad &quot; Configuracin de horarios de atencin &quot; para completar este registro.) 
&#160; 
 El sistema debe mostrar un modal con el siguiente label&#58; 
 lbl_agradecimiento_registro_pod (clase) 
&#160; 
 &quot;Gracias por registrar tu punto de donacin&quot; (a manera de ttulo del Modal) 
 lbl_donacion_o_registro_pod (clase) 
&#160; 
 Has creado una fuente de recursos y esperanza! Desde ya estas listo para donar desde este punto. Juntos demostraremos que es mucho mejor donar en vez de botar. Quieres registrar otro punto de donacin o realizar una donacin desde un punto previamente registrado? 
&#160; 
 El modal debe proporcionar las siguientes dos opciones&#58; 
 lbl_registrar_nuevo_punto (clase) 
&#160; 
 &#160;Lleva al inicio del formulario del presente formulario 
 lbl_hacer_una_donacion (clase) 
&#160; 
 Lleva al login de la webapp donantes&#160; &#123;&#123; URL_entorno_donantes &#125;&#125;/apl/&#123;&#123; DOM. cua_master &#125;&#125;/&#123;&#123;DOM. cua _user &#125;&#125; 

 Registro de horario de atencin 
 Por defecto se debe utilizar la API respectiva , para realizar un registro de horario de atencin ( eatc_attention_schedule ) de lunes a viernes de 9 AM a 5 PM (lo cual genera 5 llamadas con los siguientes parmetros al crd respectivo&#58; 
&#160; 
 Parmetros_por_defecto&#58; 
 eatc-pod_id=&#123;&#123; eatc_pods .eatc-id&#125;&#125; &amp; eatc-day =lu&amp; eatc-start_hour= 09&#58;00&#58;00&amp; eatc-final_hour= 17&#58;00&#58;00 
 eatc-pod_id=&#123;&#123; eatc_pods .eatc-id&#125;&#125; &amp; eatc-day =ma&amp; eatc-start_hour= 09&#58;00&#58;00&amp; eatc-final_hour= 17&#58;00&#58;00 
 eatc-pod_id=&#123;&#123; eatc_pods .eatc-id&#125;&#125; &amp; eatc-day =mi&amp; eatc-start_hour= 09&#58;00&#58;00&amp; eatc-final_hour= 17&#58;00&#58;00 
 eatc-pod_id=&#123;&#123; eatc_pods .eatc-id&#125;&#125; &amp; eatc-day =ju&amp; eatc-start_hour= 09&#58;00&#58;00&amp; eatc-final_hour= 17&#58;00&#58;00 
 eatc-pod_id=&#123;&#123; eatc_pods .eatc-id&#125;&#125; &amp; eatc-day =vi&amp; eatc-start_hour= 09&#58;00&#58;00&amp; eatc-final_hour= 17&#58;00&#58;00 
&#160; 
 Fase inicial&#58; en la estructura legacy 
 Se deber utilizar la estructura que se utiliza en este momento para hacer el registro respectivo&#58; 
 &#160; &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ exito /?_tabla=eatc_attention _schedule &amp;_operacion=insert&amp;&#123;&#123;parametros_por_defecto&#125;&#125; 
&#160; 
 Fase definitiva&#58; en la estructura definitiva 
 Se debe implementar de una vez (coexistiendo con la anterior escritura legacy), pero se vern los frutos de la implementacin cuando cuando se implemente la tarea&#58; https&#58;//app.asana.com/0/698639369029630/1164232107266018 est completada&#160;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; _DOM.cua_user &#125;&#125;?_tabla=eatc_attention _schedule &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 

 Confirmacin de registro realizado 
 El formulario se debe confirmar la creacin correcta del punto de donacin y desplegar el siguiente mensaje&#58; 
&#160; 
 Confirmacin de datos completos 
 Una vez enviado el registro y que el CRD responda adecuadamente, se debe realizar la siguiente consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/[cua_user]/eatc_pods? eatc-id=[eatc-id ] 
&#160; 
 Si la consulta no trae informacin o al evaluar los resultados, faltan campos obligatorios, el sistema debe proceder a borrar el registro creado de manera incompleta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_user &#125;&#125;/?_tabla=eatc_pods&amp;_operacion=delete&amp;WHERE eatc-id=&#123;&#123;eatc_pods.eatc-id&#125;&#125; 
&#160; 
 Y se le debe informar al usuario que debe intentar de nuevo la creacin del registro .&#160;&#160; 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de xito en la creacin (definido por el comit de comunicaciones)&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-simple-registro-eatc_pods%2F1514837470-pop-up_nuevo_pod.jpg&ow=563&oh=324, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fregistro-simple-registro-eatc_pods%2F1514837470-pop-up_nuevo_pod.jpg&ow=563&oh=324 

 User Administrator 
 39.0000000000000 

 REGISTRO SIMPLE: PUNTOS DE DONACIN (EATC_PODS)