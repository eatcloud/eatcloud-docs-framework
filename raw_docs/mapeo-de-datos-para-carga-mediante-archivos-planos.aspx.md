# mapeo-de-datos-para-carga-mediante-archivos-planos.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Validación del tipo de licencia para el despliegue de la funcionalidad ***NUEVO &#58; disponible también para impactoplus *** 
 Antes de desplegar el formulario, el sistema deberá realizar validar si la licencia rescate (que se obtiene con la siguiente consulta) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= type 
&#160; 
 Corresponde a eatc_cua. type = impactoplus , eatc_cua. type = impacto ó eatc_cua. type = activo y en ese caso permitirá pasar a la funcionalidad de mapeo de datos . 
&#160; 
 Si la licencia es diferente a impactoplus, impacto &#160; ó activo (es decir&#58; ó eatc_cua. type = esencial ó eatc_cua. type = free ) debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla a continuación y posteriormente lo redireccionará a la página de upgrade respectiva . 

&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events ) 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = upgrade_by_flat_file_upload 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parámetros se separan por &quot; &amp; &quot;) 
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
 eatc_upgrade_event = upgrade_by_flat_file_upload 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creación de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = upgrade_by_flat_file_upload &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free &#160; 

&#160; 
 Redirección a página de upgrade por archivos planos 
 Una vez realizado el registro del evento de upgrade, se procede a redireccionar al usuario a 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/_dgbo/#!/ upgradebyflatfiles 

 F UNCIONALIDAD DE MAPEO DE DATOS 
 Lo primero que se despliega en esta funcionalidad, es un listado de los posibles maestros que podrá cargar la cuenta y por lo tanto que será necesario realizarles un mapa de datos.&#160; Para ello se desplegará un selector que permitirá seleccionar el maestro que se desea mapear.&#160; [En una segunda etapa de implementación =&gt;] El sistema verificará si existe un mapa preparado para dicho maestro y de no ser así, deberá invocar el servicio para la preparación de dicho mapa (esto se realizará en una etapa posterior de la implementación). &#160; En una etapa inicial se mostrarán en el selector solo los mapas que estén previamente preparados mediante carga manual de datos. 
&#160; 
 Label del título&#58; Mapeo de datos 
 class=&quot; lbl_titulo_mapeo_datos &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_titulo_mapeo_datos )&#160; 
&#160; 
 Label de la descripción&#58; 
 class=&quot; lbl_mapeo_datos_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_mapeo_datos_desc )&#160;&#160; 
&#160; 
 &quot;Con esta funcionalidad podrás realizar un mapa de datos, que es una herramienta que sirve para relacionar los datos que se nos entregan en una tabla propia de cada empresa, con los datos que son requeridos para el funcionamiento de diversas funcionalidades en EatCloud.&#160; Sigue los pasos que a continuación de describimos, para realizar dicho relacionamiento de información.&quot; 

&#160; 
 1. Implementación inicial&#58; selector de maestros a mapear 
 En la implementación inicial (cuando aún no está implementado el servicio; preparemap ) se basa en un mapa preparado manualmente y que se consulta de la siguiente manera, para establecer los maestros que pueden ser mapeados en el momento (dado que tienen un mapa previamente preparado manualmente).&#160; 
&#160; 
 Label del título del selector&#58; Paso 1&#58; Seleccione el maestro a mapear (con su descripción a continuación) 
 class=&quot; lbl_seleccione_maestro_mapear &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_seleccione_maestro_mapear ) 
&#160; 
 class=&quot; lbl_seleccione_maestro_mapear_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_seleccione_maestro_mapear_desc )&#160; 
&#160; 
 &quot;Tu podrás, según sea el caso, realizar cargas de información a través de archivos planos, desde ésta plataforma (entorno administrativo, back office o &quot;bo&quot;&#58; para cargas de información general que tienen que ver con toda tu compañía), o desde la interfaz web de cada punto de donación (aplicación web o &quot;wapp&quot;&#58; para cargas de información que tienen que ver con cada punto en específico, como por ejemplo&#58; anuncios de donación)&quot; 
&#160; 
 1.1. Desde dónde deseas cargar la información 
 class=&quot; lbl_carga_de_datos_desde &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_carga_de_datos_desde )&#160; 
&#160; 
 ¿Desde dónde deseas cargar la información? bo&#58; plataforma administrativa (éste entorno) ó wapp&#58; aplicación web de cada punto de donación 
&#160; 
 El sistema armará un selector con el resultado de la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= eatc_platform 
&#160; 
 Si la consulta no arroja un resultado válido o genera un resultado vacío, el sistema deberá desplegar el siguiente label&#58; 
 class=&quot; lbl_sin_mapa_preparado &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_sin_mapa_preparado ) &#160; &quot;En la actualidad no cuentas con un mapa de datos preparado. Consulta con tu ejecutivo de cuenta EatCloud&quot; 
&#160; 
 Si el sistema encuentra datos, entonces permitirá al usuario seleccionar una opción &#123;&#123;eatc_data_map. eatc_platform &#125;&#125; y a partir de dicha selección se continúa adelante. Es importante anotar que los nombres de las plataformas&#160; ( bo , wapp ) han sido configurados como etiquetas tipo class ), por lo tanto al desplegar los datos de la respectiva consulta deberán ser manejados como etiquetas&#58; 

&#160; 
 Ejemplo 1&#58; entorno de pruebas , _DOM. cua_user=alqueria (22/11/2021) 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev. datagov .eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= alqueria &amp;_distinct= eatc_platform &#160; 
&#160; 
 Como la consulta no arroja un resultado, entonces se despliega el label&#58; 
&#160; 
 class=&quot; lbl_sin_mapa_preparado &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_sin_mapa_preparado ) &#160; &quot;En la actualidad no cuentas con un mapa de datos preparado. Consulta con tu ejecutivo de cuenta EatCloud&quot; 

&#160; 
 Ejemplo 2&#58; entorno de pruebas , _DOM. cua_user=exito 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev. datagov .eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= exito &amp;_distinct= eatc_platform &#160; 
&#160; 
 Como la consulta arroja el siguiente resultado&#58; 
 eatc_platform &#58; &quot;wapp&quot; 
&#160; 
 El sistema le presenta esta opción (en idioma español) para seleccionar y seguir adelante con el proceso. 
 Web App (de los puntos de donación) ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel= wapp )&#160;&#160; 

&#160; 
 Ejemplo 3&#58; entorno de pruebas, cuenta &quot; ara &quot; 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= ara &amp;&amp;_distinct= eatc_platform &#160; 
&#160; 
 Por lo tanto deberá presentar el siguiente selector&#58; 
 ¿Desde dónde desea cargar la información? 
 Back Office (este entorno) ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel= bo ) 
 Web App (de los puntos de donación) ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel= wapp ) 

&#160; 
 1.2. Selecciona el maestro o tabla de datos que deseas cargar&#58; 
 class=&quot; lbl_seleccionar_objctst &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_seleccionar_objctst )&#160; 
&#160; 
 El sistema construirá un selector a partir de la siguiente consulta (y que toma en cuenta la selección anterior&#58; &#123;&#123;eatc_data_map. eatc_platform &#125;&#125; ). Es importante anotar que los nombres de los maestros&#160; (por ejemplo&#58; eatc_dona , eatc_odds , eatc_pods ) han sido configurados como etiquetas tipo class ), por lo tanto al desplegar los datos de la siguiente consulta deberán ser manejados como etiquetas&#58; 

 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc_platform= &#123;&#123;eatc_data_map. eatc_platform &#125;&#125;&amp;_distinct= eatc_objectstore 

 Ejemplo 1&#58; entorno de pruebas, cuenta &quot; ara &quot;, selección paso anterior anterior &quot; bo &quot; 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= ara &amp;&amp;eatc_platform= bo &amp;_distinct= eatc_objectstore &#160;&#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 &#123; 
 eatc_objectstore &#58; &quot;eatc_dona&quot; 
 &#125;, 
 &#123; 
 eatc_objectstore &#58; &quot;eatc_odds&quot; 
 &#125;, 
 &#123; 
 eatc_objectstore &#58; &quot;eatc_pods&quot; 
 &#125; 
&#160; 
 &#160;Entonces el sistema debe armar un selector con los siguientes valores (en idioma español)&#58; 
&#160; 
 Detalles de anuncios de donación ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=eatc_dona ) 
 Maestro de productos (artículos) donables ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=eatc_odds ) 
 Maestro de puntos de donación ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=eatc_pods )&#160; 

&#160; 
 Ejemplo 2&#58; entorno de pruebas, cuenta &quot; exito &quot;, , selección paso anterior anterior &quot; wapp &quot; 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= exito &amp;eatc_platform= wapp &amp;_distinct= eatc_objectstore &#160;&#160;&#160;&#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 &#123; 
 eatc_objectstore &#58; &quot;eatc_dona&quot; 
 &#125;, 
 &#160; 
 Entonces el sistema debe armar un selector con el siguiente valore (en idioma español)&#58; 
 Detalles de anuncios de donación ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=eatc_dona ) 

 1. Implementación avanzada&#58; selector de maestros a mapear [en una etapa posterior, cuando se implemente el servicio &quot; preparemap &quot;] 
&#160; 
 Label del título del selector&#58; Paso 1&#58; Seleccione el maestro a mapear 
 class=&quot; lbl_seleccione_maestro_mapear &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_seleccione_maestro_mapear )&#160;&#160; 
&#160; 
 class=&quot; lbl_seleccione_maestro_mapear_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_seleccione_maestro_mapear_desc )&#160; 
&#160; 
 &quot;Tu podrás, según sea el caso, realizar cargas de información a través de archivos planos, desde ésta plataforma (entorno administrativo, back office o &quot;bo&quot;&#58; para cargas de información general que tienen que ver con toda tu compañía), o desde la interfaz web de cada punto de donación (aplicación web o &quot;wapp&quot;&#58; para cargas de información que tienen que ver con cada punto en específico, como por ejemplo&#58; anuncios de donación)&quot; 
 En la implementación avanzada (cuando se cuente con el servicio; preparemap ) el sistema realiza una consulta para establecer las posibles estructuras de datos o maestros a mapear, y una vez el usuario realiza la selección de la misma, establece si ya existe un mapa preparado para dicha estructura, en caso de que no lo exista, hace un llamado al servicio de preparación de mapa ( preparemap ) respectivo para que el sistema lo prepare automáticamente. 

&#160; 
 1.1. Desde dónde lo desea cargar la información 
 class=&quot; lbl_carga_de_datos_desde &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_carga_de_datos_desde )&#160;&#160; 
&#160; 
 ¿Desde dónde desea cargar la información? bo&#58; plataforma administrativa (éste entorno) ó wapp&#58; aplicación web de cada punto de donación 
&#160; 
 El sistema armará un selector con el resultado de la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_mandatory_info ?eatc_objectstore=_*&amp;_distinct= eatc_platform 
&#160; 
 Si el sistema encuentra datos, entonces permitirá al usuario seleccionar una opción &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; y a partir de dicha selección se continúa adelante 

&#160; 
 1.2. Consulta de posibles estructuras a mapear 
 Con la siguiente consulta, se armará el selector de posibles maestros o estructuras de datos a mapear&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_mandatory_info? eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125;&amp;_distinct= eatc_objectstore 
&#160; 
 Es importante anotar que los nombres de los maestros (por ejemplo&#58; eatc_dona , eatc_odds , eatc_pods ) han sido configurados como etiquetas tipo class ), por lo tanto al desplegar los datos de la anterior consulta deberán ser manejados como etiquetas. 
&#160; 
 El usuario podrá señalar uno de los valores y con el respectivo dato ( eatc_dona , eatc_odds o eatc_pods ) el mismo se realiza la siguiente consulta 

&#160; 
 1.3. Determinación si la estructura de datos seleccionada tiene mapa preparado 
 Con la siguiente consulta, se armará el selector de posibles maestros o estructuras de datos a mapear&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125;&amp;eatc_objectstore = &#123;&#123;eatc_mandatory_info .eatc_objectstore &#125;&#125; 
&#160; 
 Si la consulta presenta un resultado válido, querrá decir que existe un mapa preparado y por lo tanto podrá seguir adelante.&#160; Si no arroja un resultado válido, el sistema deberá invocar el servicio de preparación de mapa, de la siguiente manera&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; / preparemap / &#123;&#123;_DOM.cua_user&#125;&#125; ?eatc_objectstore= &#123;&#123;objectstore_a_mapear&#125;&#125; &amp;eatc_platform=eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;tk= &#123;&#123;aut_token&#125;&#125; 

 2. Presentación de información básica del maestro seleccionado para solicitud de carga de archivo de datos 
 Según la selección realizada en el anterior selector ( &#123;&#123;eatc_data_map .eatc_objectstore &#125;&#125; ), se presenta la siguiente información (labels). 

&#160; 
 2.1. Descripción general del maestro a cargar 
 Según la selección se presentará el siguiente label 
 eatc_dona &#58; eatc_dona_desc ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;pais=_*&amp;idlabel=eatc_dona_desc ) 
 eatc_pods &#58; eatc_pods_desc ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;pais=_*&amp;idlabel=eatc_pods_desc ) 
 eatc_odds &#58; eatc_odds_desc ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;pais=_*&amp;idlabel=eatc_odds_desc ) 

&#160; 
 Ejemplo 2&#58; entorno de pruebas, cuenta &quot; exito &quot;, selección paso anterior anterior &quot; eatc_dona &quot; 
&#160; 
 El sistema deberá mostrar el siguiente label (en idioma español)&#58; 
&#160; 
 &quot;En esta tabla se deberá informar el detalle de las donaciones, es decir la lista de productos con sus respectivas cantidades, que serán anunciados como donación&quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=eatc_dona_desc )&#160; 

&#160; 
 2.2. Información mínima que deberá contener el archivo de datos a mapear 
 class=&quot; lbl_fuente_de_datos_con_minimo &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_fuente_de_datos_con_minimo )&#160; &quot;A continuación nos deberá proporcionar una tabla de datos, con el nombre de las columnas en la primera fila, que contenga como mínimo la siguiente información&#58;&quot; 
&#160; 
 El sistema deberá realizar la siguiente consulta para presentar la siguiente información&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map? &amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;eatc_objectstore=&#123;&#123; eatc_objectstore &#125;&#125;&amp; eatc_madatory_map = y &amp;_distinct= eatc_descripcion_lbl 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cuenta &quot; ara &quot;, plataforma&#58; wapp , maestro&#58; eatc_dona . 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map? &amp;eatc_cua= ara &amp;eatc_platform = wapp &amp;eatc_objectstore= eatc_dona &amp;&amp; eatc_madatory_map =y&amp;_distinct= eatc_descripcion_lbl 
&#160; 
 Dado que el sistema responde con lo siguiente&#58; 
 &#123; 
 eatc_descripcion_lbl &#58; &quot;lbl_eatc_odd_id_desc&quot; 
 &#125;, 
 &#123; 
 eatc_descripcion_lbl &#58; &quot;lbl_eatc_odd_original_quantity_desc&quot; 
 &#125; 
&#160; 
 Entonces el sistema debe presentar la siguiente información (en idioma español)&#58; 
 El identificador único del producto o artículo donado es un código que sirve para identificar de manera única el producto o referencia que se dona ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=lbl_eatc_odd_id_desc ) 
 La cantidad original del anuncio de donación, son las unidades del producto o artículo donado (antes del proceso de verificación por parte del beneficiario) ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=es&amp;pais=_*&amp;idlabel=lbl_eatc_odd_original_quantity_desc )&#160; 

&#160; 
 2. Cargador de archivo de datos 
 Información que se debe presentar antes del botón para cargar datos 
 Antes del botón para cargar la fuente de datos 
 class=&quot; lbl_fuente_datos_estandar &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_fuente_datos_estandar ) &#160; &quot;En adelante, cuando se desee cargar un nuevo archivo de datos, la tabla respectiva deberá tener la misma estructura que la que se va a cargar, es decir, los nombres de las columnas deberán ser &quot;IDÉNTICOS&quot; a los que contiene el siguiente archivo.&#160; Si se desea cargar datos desde una nueva estructura, se deberá repetir este proceso con ella.&quot; 
&#160; 
 Cargador de archivos 
 class=&quot; lbl_cargar_fuente_datos_mapa_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cargar_fuente_datos_mapa_desc )&#160;&#160; 
&#160; 
 &quot;A continuación debes proveer un archivo en formato .xlsx o .csv separado por &quot;puntos y comas&quot; o &quot;pipes&quot;, que contenga en la primera fila el nombre de las respectivas columnas de datos y que corresponda a la estructura de datos estándar que será utilizada en adelante para cargar la información del respectivo maestro&quot; 
&#160; 
 Selector de separadores de campo 
 class=&quot; lbl_selecciona_separador_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_selecciona_separador_desc )&#160; 
&#160; 
 Selecciona el caracter que es utilizado para separar las respectivas columnas de datos en el archivo que estás cargando. 

&#160; 
 Selecciona el separador 
 class=&quot; lbl_selecciona_separador &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_selecciona_separador )&#160; 
&#160; 
 El sistema deberá mostrar en selector de posibles separadores de datos de archivos planos, para que&#160; el usuario determine cuál es, y el sistema lo utilice para determinar las diversas columnas de datos 
 punto y coma (;) 
 pipe (|) 
 tabulador (tab) 

&#160; 
 A continuación el sistema deberá presentar un botón que permita cargar el archivo de datos respectivo (file picker)&#58; 
 class=&quot; lbl_cargar_fuente_datos &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cargar_fuente_datos )&#160; &quot;Cargar fuente de datos estándar&quot; 
&#160; 
 Una vez el usuario seleccione un archivo de su computador, se deberá procesar el mismo como se indica a continuación. 
&#160; 
 3. Procesamiento de datos de la fuente de datos 
 El sistema debe validar que el archivo está bien formateado (separadores, que tenga datos en la primera fila diferentes a los datos de las filas subsiguientes) 
&#160; 
 El sistema debe leer los datos del encabezado del archivo adjunto ( vector de encabezados ) y guardarlos como variables. 

&#160; 
 3. Tabla para mapeo de datos 
 class=&quot; lbl_tabla_mapeo_datos &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tabla_mapeo_datos )&#160;&#160; 
&#160; 
 class=&quot; lbl_tabla_mapeo_datos_desc &quot; ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tabla_mapeo_datos_desc )&#160; 
&#160; 
 &quot;En la siguiente tabla se presentan cada uno de los datos de la estructura estándar de EatCloud, con el ánimo de establecer su correspondencia con la fuente de datos estándar que se acabas de subir.&#160; Por favor completa como mínimo los datos cuyo mapeo es obligatorio y termina con el botón &quot;Terminar mapeo de datos&quot;. 
&#160; 
 Posteriormente deberá formar una tabla, con el nombre y la información estándar en la estructura de datos de EatCloud y un selector con los valores del vector de encabezados de la siguiente manera&#58; 

 La siguiente tabla mostrará primero los datos del mapa de datos, con valor &quot;y&quot; en el parámetro eatc_data_map . eatc_madatory_map =y es decir, aquellos campos que son mandatorios de mapear.&#160;&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map? &amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;eatc_objectstore=&#123;&#123; eatc_objectstore &#125;&#125;&amp; eatc_madatory_map = y 
&#160; 
 Posteriormente mostrará los datos con valor &quot;n&quot; en el parámetro eatc_data_map . eatc_madatory_map =n.&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map? &amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;eatc_objectstore=&#123;&#123; eatc_objectstore &#125;&#125;&amp; eatc_madatory_map = n 
&#160; 
 Cada fila de la tabla corresponderá a un parámetro de la estructura estándar de EatCloud&#160; (ordenado por el dato eatc_data_map. _id &#160; es decir, con el ordenamiento por defecto) que deberá ser mapeado a un dato de los cargados en la estructura de cada cuenta usuario . La tabla desplegará la siguiente información&#58; 

&#160; 
 Nombre del dato 
 class=&quot; lbl_nombre_dato &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_nombre_dato ) 
&#160; 
 Mostrará la información contenida en el parámetro&#58; &#123;&#123; eatc_data_map . eatc_parameter_lbl &#125;&#125; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map? &amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;eatc_objectstore=&#123;&#123; eatc_objectstore &#125;&#125;&amp; eatc_madatory_map = &#123;&#123; y/o &#125;&#125;&amp;_distinct= eatc_parameter_lbl 

&#160; 
 Descripción 
 class=&quot; lbl_descripcion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_descripcion ) 
&#160; 
 Mostrará la información contenida en el parámetro&#58; &#123;&#123; eatc_data_map . eatc_descripcion_lbl &#125;&#125; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map? eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform = &#123;&#123;eatc_mandatory_info. eatc_platform &#125;&#125; &amp;eatc_objectstore=&#123;&#123; eatc_objectstore &#125;&#125;&amp;_distinct= eatc_descripcion_lbl 

&#160; 
 Corresponde a 
 class=&quot; lbl_corresponde_a &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_corresponde_a ) 
&#160; 
 Deberá desplegar un selector único, que cargue los valores&#160; del vector de encabezados de la fuente de datos previamente cargada con las siguientes especificaciones&#58; 
&#160; 
 Place holder&#58; 
 class=&quot; lbl_selecciona_un_dato &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_selecciona_un_dato ) &quot;Selecciona un dato&quot; 
&#160; 
 Valor por defecto para el selector&#58; 
&#160; 
 Ninguno (es decir, debe mostrar el place holder) 
&#160; 
 Demás valores del selector&#58; 
&#160; 
 Corresponderán a los valores del vector de encabezados de la fuente de datos subida en la respectiva funcionalidad 
&#160; 
 Validación para el selector único&#58; 
&#160; 
 Si el dato es mandatorio de mapear ( eatc_data_map . eatc_madatory_map =y ) entonces se deberá validar que exista un valor seleccionado. Si no es mandatorio su mapeo ( eatc_data_map . eatc_madatory_map =n ) no se requiere validación adicional 
&#160; 
 La opción seleccionada se lleva 
&#160; 
 Se debe guardar en una variable &#123;&#123;eatc_data_map .eatc_equivalent &#125;&#125; para realizar el registro respectivo&#58; 

&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_data_map &amp;_operacion =update &amp;eatc_equivalent= &#123;&#123;eatc_data_map .eatc_equivalent &#125;&#125; &amp;WHERE_id=&#123;&#123; eatc_data_map. _id &#125;&#125; 

&#160; 
 Obligatorio mapear 
 class=&quot; lbl_obligatorio_mapear &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_obligatorio_mapear ) 
&#160; 
 Mostrará, de acuerdo a la información contenida en el parámetro&#58; &#123;&#123; eatc_data_map . eatc_madatory_map &#125;&#125; los labels 
 &#123;&#123; eatc_data_map . eatc_madatory_map &#125;&#125;=y&#58;&#160; class=&quot; lbl_si &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_si ) 
 &#123;&#123; eatc_data_map . eatc_madatory_map &#125;&#125;=n&#58;&#160; class=&quot; lbl_no &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_no ) 

&#160; 
 Al finalizar la tabla se deberá desplegar el botón&#58; 
&#160; 
 Botón&#58; &quot;Terminar mapeo de datos&quot; 
 class=&quot; lbl_terminar_mapeo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_terminar_mapeo ) 
&#160; 
 Al presionarlo, el sistema deberá validar que todos los campos mandatorios hallan sido mapeados, y podrá realizar los registros de las equivalencias en el mapa.&#160; Si para completar el mapa&#160; falta algún dato (es decir que algún campo mandatorio para mapear no tiene equivalencia) el sistema deberá desplegar el siguiente label 
&#160; 
 class=&quot; lbl_mapeo_incompleto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mapeo_incompleto ) 
&#160; 
&quot;Aún no has terminado de mapear los campos obligatorios.&#160; Por favor termina de asignar las correspondencias entre los datos estándar y tu estructura de datos, para poder terminar el proceso.&quot; 
&#160; 
 Cuando el proceso está completo, se presiona el botón y se completa el registro de las equivalencias, se deberá&#160; mostrar el siguiente label 
 class=&quot; lbl_mapeo_exitoso &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mapeo_exitoso ) 
&#160; 
&quot;Has completado el mapeo de datos con éxito.&#160; En adelante podrás cargar los datos de maestro de datos mapeado a partir de un archivo plano.&quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 User Administrator 
 449.000000000000 

 MAPEO DE DATOS (PARA CARGA MEDIANTE ARCHIVOS PLANOS)