# nuevo-listado-de-anuncios-eatc_dona_lst.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseño 
 https&#58;//repograf.eatcloud.info/listado_dona-old.html &#160; 

 Etiquetas encabezado del informe&#58; 

 Listado de donaciones 
 Label &#58; class=&quot;lbl_listado_donaciones&quot; 
&#160; 
 Listado de donaciones&#58; descripción 
 Label &#58; class=&quot;lbl_listado_donaciones_desc&quot; 
&#160; 
 Filtrar 
 Label &#58; class=&quot;lbl_filtrar&quot; 

 Filtro de fechas 
 Se deberá implementar un filtro de fechas, cuyo valor por defecto sea el mes actual, y que permita filtrar al seleccionar una fecha inicial y una fecha final, los anuncios de ese periodo.&#160; Los demás filtros del informe (Filtro por estados abreviados) operarán para donaciones de las fechas seleccionadas&#58; 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; 
&#160; 
 Filtro de fechas 
 Filtro&#58; &quot;El mes actual&quot; = &gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_mes_actual )&#160; 
 &#123;&#123; fecha_inicial_periodo &#125;&#125; = Primer día del mes actual 
 &#123;&#123; fecha_final_periodo &#125;&#125; &#160; = Día actual 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_personalizar )&#160;&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_fecha_inicial ) =&gt; &#123;&#123; fecha_inicial_periodo &#125;&#125;&#160; 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_fecha_final ) =&gt; &#123;&#123; fecha_final_periodo &#125;&#125; 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_consultar ) 

 FUNCIONAMIENTO DEL FILTRO POR ESTADOS ABREVIADOS 
 Con ánimo de facilitar el entendimiento de los estados de los anuncios, tanto en el filtro, como en las cards se empezarán a utilizar los &quot; estados simplificados &quot;. Dichos estados corresponden a una agrupación de estados originales del anuncio y dicha correspondencia se puede consultar en el maestro de estados 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states? eatc_simplified_label =_* 
&#160; 
 Colocar los filtros como un botón al lado izquierdo de la pantalla (actualmente están como un vínculo al lado derecho de la pantalla) 
 Se deberá cambiar la ubicación del actual &quot;vínculo&quot; para los filtros, y cambiarle el diseño a un botón (más visible) ojalá con un ícono de embudo como se muestra en la siguiente imagen.&#160; El funcionamiento de los filtros será igual al implementado en la actualidad . 

 Cambio en la interacción del ordenamiento&#58; antes aparecía solamente la opción diferente a la actual para accionarla directamente, ahora se debe mostrar un botón &quot;ordenar&quot; y las opciones de ordenamiento, identificando la que está activa y a la cual se puede cambiar) 
 Dejando las opción por defecto tal como funciona en la actualidad se propone implementar el siguiente botón&#58; 
&#160; 
 Botón&#58; &quot;Ordenar listado&quot; 
 class=&quot; lbl_ordenar_listado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_ordenar_listado &#160;&#160;&#160; 
&#160; 
 Al presionar el botón deben mostrarse un selector único con las siguientes opciones&#58; 
&#160; 
 Mostrar primero donaciones más antiguas o De donaciones más antiguas a más recientes 
 Se solicita al desarrollador indique a su criterio cuál de los anteriores labels es el más adecuado para proceder a su configuración 
&#160; 
 class=&quot; lbl_primero_mas_antiguas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_primero_mas_antiguas&#160;&#160; 
&#160; 
 Mostrar primero donaciones más nuevas o De donaciones más recientes a más antiguas 
 Se solicita al desarrollador indique a su criterio cuál de los anteriores labels es el más adecuado para proceder a su configuración 
&#160; 
 class=&quot; lbl_primero_mas_nuevas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_primero_mas_nuevas&#160;&#160; 

&#160; 
 La opción por defecto (tal cual funciona en la actualidad) debe aparecer &quot;activa o seleccionada&quot;, y se debe permitir seleccionar la otra opción. 

 Buscador de donaciones 
 Label &#58; class=&quot; lbl_buscar &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_buscar 

 class=&quot; lbl_buscar_dona_desc &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_buscar_dona_desc &#160; 

 ***NUEVO&#58; búsqueda por código del anuncio *** 
 Se deberá implementar un Text_input para efectuar búsqueda de donaciones en el informe, principalmente por dos criterios&#58; 
&#160; 
 ***NUEVO&#58; código de la donación ( eatc_dona_headers. eatc-code ) *** 

 Identificación del beneficiario&#58; ( eatc_dona_headers. eatc-donation_manager_code ) 
 Nombre del beneficiario&#58; ( eatc_dona_headers. eatc-donation_manager_name ) 
 Nombre del recolector&#58; ( eatc_dona_headers. eatc-picker_name ) 
 Identificación del recolector&#160; ( eatc_dona_headers. eatc-picker_id ) 
 Placa del vehículo ( eatc_dona_headers. eatc-picker_license_plate ) 
&#160; 
 Si se puede ampliar a más términos contenidos en la información del anuncio mucho mejor.&#160; Lo ideal es que funcione con texto predictivo y de manera muy fluída, filtrando de los anuncios que tiene el punto de donación y que se encuentran dentro del criterio de búsqueda ingresado. 

 Los estados simplificados son&#58; 
&#160; 
 Donación en curso&#58; 
 Label &#58; class=&quot; lbl_donacion_en_curso &quot; 
&#160; 
 Corresponde a los anuncios cuyo estado original es &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o &quot;programado&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?eatc_simplified_label=lbl_donacion_en_curso &#160; 
&#160; 
 Filtro por defecto de la lista&#58; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centraliced_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id 
&#160; 
 el sistema toma el dato (o los datos) que&#160; llega(n) en el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=announced,awarded,scheduled 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp;eatc-state=announced,awarded,scheduled &#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta,&#160; el sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 El sistema toma el parámetro &quot; eatc-id &quot; del punto de donación ( eatc_pods ) respectivo y su _DOM.cua_user 
&#160; 
 El filtro por defecto de la lista, será aquel que muestre las donaciones en curso (es decir anuncios de donación del punto de donación en cuestión con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o &quot;programado&quot;) 
&#160; 
 En su vista por defecto se debe ordenar el listado mostrando primero los más antiguos y luego los más recientes (según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=announced,awarded,scheduled 
&#160; 
 Cuando un filtro sea aplicado, su &quot;TAG&quot; debe aparecer al lado de la funcionalidad de filtro 
&#160; 
 Si la respuesta es &quot;y&quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=announced,awarded,scheduled 

&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 

&#160; 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-donor= postobon &amp;eatc-state=announced,awarded,scheduled &#160; 

 Donación despachada&#58; 
 Label &#58; class=&quot; lbl_donacion_despachada &quot; 
&#160; 
 Corresponde a los anuncios cuyo estado original es &quot;delivered&quot; o &quot;despachado&quot;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?eatc_simplified_label=lbl_donacion_despachada &#160; 
&#160; 
 Segundo filtro por defecto de la lista&#58; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id 
&#160; 
 el sistema toma el dato (o los datos) que&#160; llega(n) en el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; &#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=delivered 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp;eatc-state=delivered &#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta,&#160; El sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 Si el primer filtro por defecto no trae resultados, se debe adicionar el presente filtro para mostrar las donaciones despachadas 
&#160; 
 En esta vista por defecto también se debe ordenar el listado mostrando primero los más antiguos y luego los más recientes (según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=delivered 
&#160; 
 Cuando un filtro sea aplicado, su &quot;TAG&quot; debe aparecer al lado de la funcionalidad de filtro 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=delivered 

&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
&#160; 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-donor= postobon &amp;eatc-state=delivered &#160; 

 Si la anterior consulta no trae resultados, se debe agregar al filtro por defecto el siguiente estado simplificado 

 Por verificar &#58; solo aplica para donaciones cuyo estado es &quot;scheduled&quot; y &quot;delivered&quot; 
 Label &#58; class=&quot; lbl_por_verificar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_por_verificar )&#160; 
&#160; 
 Al lado del label del filtro deberá aparecer una burbuja roja, con el conteo de donaciones pendientes de verificación del código recogida&#58; 

 El conteo (N) &#160; se obtiene con la siguiente consulta ( se ingresan los estados particulares &quot;scheduled&quot; y &quot;delivered&quot; dado que en los estados anteriores (announced, awarded) y posteriores (received, pre-certified, certified, cancelled, not_delivered), se justifica que la fecha y hora de verificación esté en cero )&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered &amp;_cont 

&#160; 
 El nuevo filtro ( Por verificar ) corresponde a los anuncios cuyo código de recogida no ha sido verificado por el punto de donación, es decir aquellos que no poseen una fecha y hora válida (tienen el dato 0000-00-00 00&#58;00&#58;00 ) en el campo eatc_dona_headers. eatc_code_verification_datetime 
&#160; 
 Tercer filtro por defecto de la lista&#58; solo aplica para donaciones cuyo estado es &quot;scheduled&quot; y &quot;delivered&quot; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id 
&#160; 
 el sistema toma el dato (o los datos) que&#160; llega(n) en el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; 
 &#160;&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered &#160; &#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta, el sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 En esta vista por defecto se debe ordenar el listado mostrando primero los más antiguos y luego los más recientes (según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered 

&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp; eatc_code_verification_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled , delivered &#160; &#160; 

 Donación recibida&#58; 
 Label &#58; class=&quot; lbl_donacion_recibida &quot; 
 Corresponde a los anuncios cuyo estado original es &quot; received &quot; o &quot;recibido&quot;, &quot; pre-certified &quot; o &quot;pre-certificado&quot;, , &quot; certified &quot; o &quot;certificado&quot;, 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?eatc_simplified_label=lbl_donacion_recibida &#160; 
&#160; 
 Cuarto filtro por defecto de la lista&#58; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id 
&#160; 
 el sistema toma el dato (o los datos) que&#160; llega(n) en el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; 
 &#160;&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= received,pre-certified,certified 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp;eatc-state=received,pre-certified,certified &#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta, el sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 Si el tercer filtro por defecto no trae resultados, se debe adicionar el presente filtro para mostrar las donaciones despachadas 
&#160; 
 En esta vista por defecto también se debe ordenar el listado mostrando primero los más nuevos y luego los más antiguos (OJO que cambia el ordenamiento con respecto a los filtros pasados &#58; según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= received,pre-certified,certified 
&#160; 
 Cuando un filtro sea aplicado, su &quot;TAG&quot; debe aparecer al lado de la funcionalidad de filtro 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= received,pre-certified,certified 

&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp;eatc-state=received,pre-certified,certified &#160; 

 Si la anterior consulta no trae resultados, se debe agregar al filtro por defecto el siguiente estado simplificado 

 Donación cancelada&#58; 
 Label &#58; class=&quot; lbl_donacion_cancelada &quot; 
&#160; 
 Corresponde a los anuncios cuyo estado original es &quot; cancelled &quot; o &quot;cancelada&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?eatc_simplified_label=lbl_donacion_cancelada &#160; 
&#160; 
 Quinto filtro por defecto de la lista&#58; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id el sistema toma el dato (o los datos) que&#160; llega(n) en&#160; 
&#160; 
 el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; 
 &#160;&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= cancelled 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp;eatc-state=cancelled &#160;&#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta, el sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 Si el cuarto filtro por defecto no trae resultados, se debe adicionar el presente filtro para mostrar las donaciones despachadas 
&#160; 
 En esta vista por defecto también se debe ordenar el listado mostrando primero los más antiguos y luego los más recientes (según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= cancelled 
&#160; 
 Cuando un filtro sea aplicado, su &quot;TAG&quot; debe aparecer al lado de la funcionalidad de filtro 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= cancelled 
&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp;eatc-state=cancelled &#160;&#160; 

 Si la anterior consulta no trae resultados, se debe agregar al filtro por defecto el siguiente estado simplificado 

 Donación no entregada&#58; 
 Label &#58; class=&quot; lbl_no_entregado &quot; 
&#160; 
 Corresponde a los anuncios cuyo estado original es &quot; not_delivered &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?eatc_simplified_label=lbl_no_entregado &#160; 
&#160; 
 Sexto filtro por defecto de la lista&#58; ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; o diferente de &quot;y&quot; (la consulta no trae respuesta válida) 
 ***NUEVO&#58; consulta del parámetro de configuración specific_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=specific_management_pod 
&#160; 
 Si la respuesta es &quot;y&quot;, entonces el sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/ eatcloud /eatc_specific_dona_management?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_cua_user=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_master_pod_id= &#123;&#123;current&#58;eatc_pods. eatc-id &#125;&#125; &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id 
&#160; 
 el sistema toma el dato (o los datos) que&#160; llega(n) en el parámetro&#160; eatc_specific_dona_management. eatc_child_pod_id &#160; en adelante &#123;&#123; array_child_pods &#125;&#125; para consultar la información de las donaciones a gestionar&#58;&#160; 
 &#160;&#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123; array_child_pods &#125;&#125; &amp; eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= not_delivered 

&#160; 
 Ejemplo 1, ambiente de pruebas, _DOM .cua_user=postobon, eatc-pod_id= t4sxTlcnPzi2puNrFNDre &#58; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= t4sxTlcnPzi2puNrFNDre &amp;_cmp= specific_management_pod &#160; &#160; 
&#160; 
 Como el sistema retorna la respuesta &quot;y&quot;, entonces el sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_specific_dona_management?eatc_cua_master=abaco&amp;eatc_cua_user=postobon&amp;eatc_master_pod_id= t4sxTlcnPzi2puNrFNDre &amp;eatc_management_type= management &amp;eatc_active_rel= y &amp;_cmp=eatc_child_pod_id &#160; 
&#160; 
 Como el valor que trae la consulta es st05 , entonces procede a realizar la siguiente consulta para traer la información de las donaciones&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-pod_id= st05 &amp;eatc-donor=postobon&amp;eatc-state=not_delivered &#160; 

&#160; 
 Si la respuesta es &quot;n&quot;, &quot;vacía&quot;, diferente de &quot;y&quot;, o incorrecta, el sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 Si el quinto filtro por defecto no trae resultados, se debe adicionar el presente filtro para mostrar las donaciones despachadas 
&#160; 
 En esta vista por defecto también se debe ordenar el listado mostrando primero los más recientes y luego los más antiguos (según el dato&#58; eatc_dona_headers. eatc-publication_datetime ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= not_delivered 
&#160; 
 Cuando un filtro sea aplicado, su &quot;TAG&quot; debe aparecer al lado de la funcionalidad de filtro 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state= not_delivered 
&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp;eatc-state=not_delivered &#160; 

 Si la anterior consulta no trae resultados, se debe agregar mostrar el label&#58; 
&#160; 
 label&#58; class=&quot;lbl_listado_sin_donaciones&quot; 
 &quot;Aún no tienes donaciones para consultar&quot; 

 Funcionamiento del filtro 
 Teniendo en cuenta las consultas de filtro simplificado que se documentaron arriba, la funcionalidad de filtro, a la cual se accede al presionar el botón específico 

 Deberán desplegar los diferentes filtros de estados simplificado (cuyos labels se especificaron más arriba) adicionando uno 
 Label &#58; class=&quot;lbl_todas&quot; 
&#160; 
 El botón deberá cambiar de diseño y label por 
 Label &#58; class=&quot;lbl_aplicar&quot; 
&#160; 
 Y deberá desplegar los botones de los filtros que ya están aplicados (con color sólido) y los que no están aplicados (sin color). 

 Al presionar un botón inactivo (fondo blanco) se activa (debe cambiar el color a sólido) 

 Se activa (debe cambiar el color a sólido) 

 Y viceversa&#58; cuando se presiona un filtro activo (color sólido) se inactiva (fondo blanco). 
&#160; 
 Cuando se presiona el botón aplicar con un filtro seleccionado&#58; 

 Se colapsan todos los filtros no seleccionados (con fondo blanco) y se muestra el botón con su estado original y el filtro aplicado, realizando la consulta respectiva (como se indicó más arriba). 

 Cuando se selecciona el filtro &quot;Todas&quot;, 

 Cuando presionar el botón aplicar, estando activo este filtro 

 Se deberá desplegar todos los filtros, 

 ***NUEVO&#58; consulta diferencial según el dato registrado en eatc_pods. centralized_management_pod *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; (la consulta no trae respuesta) 
 El sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta.&#160; 
&#160; 
 Y consultar todas las donaciones del punto en cuestión&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; _compress 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; _compress 
&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp; _compress &#160; 

 El usuario podrá utilizar cualquier combinación de filtros de los arriba expuestos y una vez se apliquen se deberán combinar las búsquedas que por etiquieta simplificada se establecieron más arriba. 
&#160; 
 Si alguna de las búsquedas no trae resultados, se debe desplegar una card alargada con el respectivo label que se establece a continuación, según sea el caso 
&#160; 
 Sin donaciones en curso&#58; 
 Label &#58; class=&quot;lbl_sin_donaciones_en_curso&quot; 

 Sin donaciones despachadas&#58; 
 Label &#58; class=&quot;lbl_sin_donaciones_despachadas&quot; 

 Sin donaciones recibidas&#58; 
 Label &#58; class=&quot;lbl_sin_donaciones_recibidas&quot; 

 Sin donaciones canceladas&#58; 
 Label &#58; class=&quot;lbl_sin_donaciones_canceladas&quot; 

 Sin donaciones no entregadas&#58; 
 Label &#58; class=&quot;lbl_sin_donaciones_no_entregadas&quot; 

 Según los filtros aplicados y la información obtenida de cada llamado al API, se presenta información de los anuncios (con un funcionamiento similar a como se implementó en las originales&#58; Entrega de donaciones y Seguimiento de anuncios ) en una card rediseñada que se especifica a continuación&#58; 

 Listado de cards paginado 
 Se deben paginar el listado de cards, para mostrar en primera instancia un número reducido de anuncios, los cuales deberán tener siempre el siguiente ordenamiento (en caso de traer todas las donaciones del punto en cuestión)&#58; 
&#160; 

 Donaciones en curso &#58; ordenadas poniendo primero las más antiguas y luego las más recientes 

 Donaciones despachadas &#58; ordenadas poniendo primero las más antiguas y luego las más recientes 

 Donaciones recibidas , canceladas y no entregadas &#58; ordenadas poniendo primero las más recientes y luego las más antiguas 

 La card se ha rediseñado, para mostrar de manera más limpia la información que le interesa al donante de la siguiente manera&#58;. 

 Mitad izquierda de la card 

 Estado simplificado de la donación&#58; 
 Con el dato que se obtiene del parámetro del anuncio respectivo&#58; 
 eatc_dona_headers. eatc-state 
&#160; 
 Se realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_headers_states ? eatc_code =&#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; 
&#160; 
 El label de la etiqueta del estado es el que se obtiene del parámetro&#58; 
 eatc_dona_headers_states . eatc_simplified_label 

&#160; 
 Fecha de anuncio&#58; 
 Label &#58; class=&quot; lbl_fecha_anuncio &quot; 
&#160; 
 La información se toma de&#58; 
 &#160; eatc_dona_headers .eatc-publication_datetime 

&#160; 
 Código del anuncio (donación)&#58; 
 Label &#58; class=&quot; lbl_fecha_anuncio &quot; 
&#160; 
 La información se toma de&#58; 
 &#160; eatc_dona_headers .eatc-code 

&#160; 
 Nombre beneficiario 
 La información se toma de&#58; 
 eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 En caso que aún no haya sido adjudicado el anuncio ( eatc_dona_headers. eatc-state = announced ), se debe mostrar un letrero vistoso con el siguiente label 
 &#160; Label &#58; class=&quot; lbl_adjudicacion_pendiente &quot; 
 &quot; PENDIENTE DE ADJUDICACIÓN &quot; 

&#160; 
 Teléfono (no está en el diseño)&#58; 
 class=&quot;lbl_telefono_doma&quot; 
&#160; 
 La información se toma de&#58; 
 eatc_dona_headers .eatc-donation_manager_phone 

&#160; 
 Peso de la donación (en el diseño&#58; cantidad de alimentos) 
 Label &#58; class=&quot; lbl_peso_donacion &quot; 
&#160; 
 La información se toma de&#58; 
 &#160; eatc_dona_headers . eatc-total_weight_kg 
&#160; 
 ***NUEVO&#58; Donante y punto origen de la donación *** 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_dona_headers ? eatc_code =&#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;&amp;_cmp=eatc-donor,eatc_cua_origin 
&#160; 
 Si los datos que eatc-donor y eatc_cua_origin son diferentes, quiere decir que la donación es de No Negociados, entonces el sistema realizará dos cosas&#58; 
&#160; 
 Pintará la card con un color diferente a las demás cards (para que se distinga de las demás como una donación de No Negociados) 
 Desplegará la siguiente información adicional en la CARD&#58; 
&#160; 
 Label &#58; class=&quot; lbl_marca_donante &quot; Marca donante 
&#160; 
 La información se toma de&#58; 
 &#160; eatc_dona_headers . eatc-donor 

&#160; 
 Label &#58; class=&quot; lbl_pod_origen &quot; Punto origen de la donación&#160; 
&#160; 
 La información se toma de (colocando ambas informaciones separadas por un guión)&#58; 
 eatc_dona_headers . eatc-pod_name - eatc_dona_headers . eatc-pod_address&#160; 
&#160; 
 T ag&#58; ¡Verifica de inmediato! Nuevo&#58; solo se muestra si no existe una fecha y hora válida en eatc_code_verification_datetim e &#160; 
 (Se debe mostrar si existe un registro válido en eatc_dona_headers .eatc- picking_checkout_datetime ) y no posee una fecha y hora válida en el campo &quot; eatc_code_verification_datetime &quot; 
&#160; 
 Debe ser vistoso, puede ser acompañado de un icono de signo de admiración en un círculo rojo 
 class=&quot;lbl_verificar_inmediatamente&quot; 

 Mitad derecha de la card 

 Datos de recogida&#58; 
 Label &#58; class=&quot; lbl_card_datos_de_recogida &quot; 
&#160; 
 En caso que la donación no tenga aun datos de recogida ( eatc_dona_headers. eatc-state = announced,awarded ), se debe mostrar un letrero vistoso con el siguiente label 
&#160; 
 &#160; Label &#58; class=&quot; lbl_programacion_pendiente &quot; 
 &quot; PENDIENTE DE&#160; PROGRAMACIÓN DE RECOGIDA &quot; 

&#160; 
 Fecha y hora programada de recogida (no está en el diseño) 
 class=&quot; lbl_fecha_hora_recogida_programada &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-programed_picking_datetime 

&#160; 
 Recoge (En el diseño está como &quot;Nombre&quot;) 
 class=&quot; lbl_recolector &quot; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_name 

&#160; 
 Identificación (En el diseño está como &quot;Teléfono&quot;) 
 class=&quot; lbl_doc_id_recolector &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_doc_id 

&#160; 
 Placa 
 class=&quot; lbl_placa_recolector &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_license_plate 

&#160; 
 Llegó al punto de donación a las (no está en el diseño)&#58; 
 (información que solo se debe mostrar si existe un registro válido en eatc_dona_headers .eatc-picking_checkin_datetime ) 
 class=&quot; lbl_fecha_hora_llegada &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-picking_checkin_datetime 

&#160; 
 Salió del punto de donación a las&#58; 
 (información que solo se debe mostrar si existe un registro válido en eatc_dona_headers .eatc- picking_checkout_datetime ) 
 class=&quot; lbl_fecha_hora_salida &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-picking_checkout_datetime 

&#160; 
 Botón&#58; Verificar código&#58; 
 El botón aparece si no existe un dato válido en el campo (un valor diferente a 0000-00-00 00&#58;00&#58;00, a nulo o vacío)&#58; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; btn_init_verf_codrecg &quot; 
&#160; 
 Da ingreso a la funcionalidad de &quot; Verificación de código de recogida &quot; (que permanece igual en funcionamiento a como se ha implementado anteriormente) 
&#160; 
 Si en el campo&#160; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Hay un dato 0000-00-00 00&#58;00&#58;00, nulo o vacío). la wapp, en vez del botón deberá desplegar el label&#160; 
 class=&quot; lbl_codigo_verificado &quot; 

&#160; 
 Botón&#58; Detalle donación (en el diseño está como &quot;Detalle anuncio&quot;)&#58; 
 class=&quot; lbl_detalle_donacion &quot; 
&#160; 
 Da ingreso al dahsboard del anuncio de donación (que permanece igual en funcionamiento a como se ha implementado anteriormente) 

&#160; 
 Botón&#58; Liberar donación&#58; 
 El botón aparece solamente a donaciones con estado (eatc-state) &quot; scheduled &quot; y &quot; cancelled &quot;, que cumplan con estas condiciones de timeout (se referencia a documentación de &quot; liberación de donaciones &quot;. 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; lbl_libdona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_libdona )&#160; 
&#160; 
 Al presionar el botón se deberá llevar a la funcionalidad &quot; liberación de donaciones &quot;. 
&#160; 
 ***NUEVO&#58; Botón&#58; Constancia de entrega&#58; *** 
 El botón aparece solamente cuando se cumplan las dos siguientes condiciones (ambas). 
&#160; 
 La cuenta tiene licencia &quot;impactoplus&quot; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= impactoplus &amp;_cmp=name,type 
 La donación tiene una fecha válida de verificación del código de recogida 
&#160; 
 Si en el campo&#160; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Hay un dato diferente de&#160; 0000-00-00 00&#58;00&#58;00 , nulo o vacío) 
&#160; 
 Si se cumplen estas dos condiciones al mismo tiempo ( prueba lógica &quot; y &quot; ) entonces se despliega el botón 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; lbl_constancia_entrega &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_constancia_entrega )&#160;&#160; 
&#160; 
 Al presionar el botón se deberá llevar a la funcionalidad &quot; Constancia de entrega &quot;. 

&#160; 
 ***NUEVO&#58; Botones (vínculos) a archivos adjuntos *** 
 El (los) botones (o vínculos) solamente aparece(n) cuando se cumplan las dos siguientes condiciones (ambas). 
&#160; 
 La cuenta tiene licencia &quot; impactoplus &quot; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= impactoplus &amp;_cmp=name,type 
 La donación tiene adjuntos registrados 
&#160; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_photo_registry?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp=eatc_label,eatc_photo &#160; 
&#160; 
 Si la consulta trae una respuesta, entonces el sistema pinta en la interfaz, el label o los labels que devuelve la consulta 
 class=&quot;&#123;&#123;eatc_photo_registry. eatc_label &#125;&#125;&quot;&#160; 
&#160; 
 Y los vincula (al hacer clic en los mismos desplegando en pestaña separada), al archivo (ruta) que llega en el parámetro &#123;&#123;eatc_photo_registry. eatc_photo &#125;&#125;
&#160; 
 &lt;a href=&#123;&#123;eatc_photo_registry. eatc_photo &#125;&#125;&gt;&#123;&#123;eatc_photo_registry. eatc_label &#125;&#125;&lt;/a&gt; 
&#160; 
 Al presionar el botón / vínculo se deberá permitir descargar el adjunto respectivo. 

 Datos de recogida&#58; 
 Label &#58; class=&quot; lbl_card_datos_de_recogida &quot; 
&#160; 
 En caso que la donación no tenga aun datos de recogida ( eatc_dona_headers. eatc-state = announced,awarded ), se debe mostrar un letrero vistoso con el siguiente label 
&#160; 
 &#160; Label &#58; class=&quot; lbl_programacion_pendiente &quot; 
 &quot; PENDIENTE DE&#160; PROGRAMACIÓN DE RECOGIDA &quot; 

&#160; 
 Fecha y hora programada de recogida (no está en el diseño) 
 class=&quot; lbl_fecha_hora_recogida_programada &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-programed_picking_datetime 

&#160; 
 Recoge (En el diseño está como &quot;Nombre&quot;) 
 class=&quot; lbl_recolector &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_name 

&#160; 
 Identificación (En el diseño está como &quot;Teléfono&quot;) 
 class=&quot; lbl_doc_id_recolector &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_doc_id 

&#160; 
 Placa 
 class=&quot; lbl_placa_recolector &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers . eatc-picker_license_plate 

&#160; 
 Llegó al punto de donación a las (no está en el diseño)&#58; 
 (información que solo se debe mostrar si existe un registro válido en eatc_dona_headers .eatc-picking_checkin_datetime ) 
 class=&quot; lbl_fecha_hora_llegada &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-picking_checkin_datetime 

&#160; 
 Salió del punto de donación a las&#58; 
 (información que solo se debe mostrar si existe un registro válido en eatc_dona_headers .eatc- picking_checkout_datetime ) 
 class=&quot; lbl_fecha_hora_salida &quot; 
&#160; 
 La información se toma de 
 eatc_dona_headers .eatc-picking_checkout_datetime 

&#160; 
 Botón&#58; Verificar código&#58; 
 El botón aparece si no existe un dato válido en el campo (un valor diferente a 0000-00-00 00&#58;00&#58;00, a nulo o vacío)&#58; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; btn_init_verf_codrecg &quot; 
&#160; 
 Da ingreso a la funcionalidad de &quot; Verificación de código de recogida &quot; (que permanece igual en funcionamiento a como se ha implementado anteriormente) 
&#160; 
 Si en el campo&#160; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Hay un dato 0000-00-00 00&#58;00&#58;00, nulo o vacío). la wapp, en vez del botón deberá desplegar el label&#160; 
 class=&quot; lbl_codigo_verificado &quot; 

&#160; 
 Botón&#58; Detalle donación (en el diseño está como &quot;Detalle anuncio&quot;)&#58; 
 class=&quot; lbl_detalle_donacion &quot; 
 Da ingreso al dahsboard del anuncio de donación (que permanece igual en funcionamiento a como se ha implementado anteriormente) 

&#160; 
 Botón&#58; Liberar donación&#58; 
 El botón aparece solamente a donaciones con estado (eatc-state) &quot; scheduled &quot; y &quot; cancelled &quot;, que cumplan con estas condiciones de timeout (se referencia a documentación de &quot; liberación de donaciones &quot;. 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; lbl_libdona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_libdona )&#160; 
&#160; 
 Al presionar el botón se deberá llevar a la funcionalidad &quot; liberación de donaciones &quot;. 
&#160; 
 ***NUEVO&#58; Botón&#58; Constancia de entrega&#58; *** 
 El botón aparece solamente cuando se cumplan las dos siguientes condiciones (ambas). 
&#160; 
 La cuenta tiene licencia &quot;impactoplus&quot; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= impactoplus &amp;_cmp=name,type 
 La donación tiene una fecha válida de verificación del código de recogida 
&#160; 
 Si en el campo&#160; 
 eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Hay un dato diferente de&#160; 0000-00-00 00&#58;00&#58;00 , nulo o vacío) 
&#160; 
 Si se cumplen estas dos condiciones al mismo tiempo ( prueba lógica &quot; y &quot; ) entonces se despliega el botón 
&#160; 
 El label del mismo será&#58;&#160; 
 class=&quot; lbl_constancia_entrega &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_constancia_entrega )&#160;&#160; 
&#160; 
 Al presionar el botón se deberá llevar a la funcionalidad &quot; Constancia de entrega &quot;. 

&#160; 
 ***NUEVO&#58; Botones (vínculos) a archivos adjuntos *** 
 El (los) botones (o vínculos) solamente aparece(n) cuando se cumplan las dos siguientes condiciones (ambas). 
&#160; 
 La cuenta tiene licencia &quot; impactoplus &quot; 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;type= impactoplus &amp;_cmp=name,type 
 La donación tiene adjuntos registrados 
&#160; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_photo_registry?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp=eatc_label,eatc_photo &#160; 
&#160; 
 Si la consulta trae una respuesta, entonces el sistema pinta en la interfaz, el label o los labels que devuelve la consulta 
&#160; 
 class=&quot;&#123;&#123;eatc_photo_registry. eatc_label &#125;&#125;&quot;&#160; 
&#160; 
 Y los vincula (al hacer clic en los mismos desplegando en pestaña separada), al archivo (ruta) que llega en el parámetro &#123;&#123;eatc_photo_registry. eatc_photo &#125;&#125; 
&#160; 
 &lt;a href=&#123;&#123;eatc_photo_registry. eatc_photo &#125;&#125;&gt;&#123;&#123;eatc_photo_registry. eatc_label &#125;&#125;&lt;/a&gt; 
&#160; 
 Al presionar el botón / vínculo se deberá permitir descargar el adjunto respectivo. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-listado-de-anuncios-eatc_dona_lst%2F2257040130-filtro_por_defecto_4_dona_list.jpg&ow=1280&oh=279, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-listado-de-anuncios-eatc_dona_lst%2F2257040130-filtro_por_defecto_4_dona_list.jpg&ow=1280&oh=279 
 EatCloud Donantes 

 186.000000000000 

 NUEVO: LISTADO DE DONACIONES (EATC_DONA_LST)