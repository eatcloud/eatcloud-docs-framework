# informe-operativo-bo-de-anuncios-de-donación-eatc_dona_lst2.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO&#58; Selector de cuenta usuario *** 
 Label &#58; class=&quot;lbl_selecciona_cua_user&quot; Selecciona una cuenta usuario (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_eatcloud&amp;pais=_*&amp;idlabel=lbl_selecciona_cua_user) 
 Tipo de selector&#58; Selector nico 
 El selector se construye &#58; con la informacin que se obtiene de la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/eatc_cua?eatc_cua_master= &#123;&#123;cua_master&#125;&#125; &amp;_cmp=name 
 Validaciones &#58; obligatoriedad 
 La cuenta usuario seleccionada se lleva a&#58; &#123;&#123; cua_user &#125;&#125; 

&#160; 
 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o programado , es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 
&#160; 
 Consulta de anuncios 
 el sistema toma el parmetro &quot; abaco &quot; del master CUA respectivo (que se digita en la URL de ingreso al BO) y se traen todos los anuncios para dicha cuenta cuyo estado por defecto sea announced,awarded,scheduled 

 Ejemplo&#58; 
 El BO dispuesto para BACO (https&#58;//beneficiarios.eatcloud.info/bo/[master_CUA] ) https&#58;//beneficiarios.eatcloud.info/bo/abaco se toma el&#160; master_CUA es decir abaco y se traen todos los anuncios cuyos estados sean, anunciados, adjudicados y programados (eatc-state=announced,awarded,scheduled) 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?_id=_*&amp;eatc-state=announced,awarded,scheduled&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=announced,awarded,scheduled&amp;_compress &#160; 
&#160; 
 Filtros (segunda prioridad&#58; no se requiere para una primera entrega) 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin con diferentes estados a los del filtro por defecto 
&#160; 
 Ejemplo&#58; 
 El BO dispuesto para BACO (https&#58;//beneficiarios.eatcloud.info/bo/[master_CUA] ) https&#58;//beneficiarios.eatcloud.info/bo/abaco se toma el&#160; master_CUA es decir abaco y se traen todos los anuncios cuyos estados sean, despachados y recividos (eatc-state=delivered,recieved)&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? _id=_* &amp;eatc-state=derivered,recieved&#160; 
&#160; 
 Listado de anuncio de donacin 
 Un listado en data tables, con las funcionalidades clsicas de ordenamiento, bsqueda y dems. 
&#160; 
 Ordenamiento&#58; 
 El listado de anuncios debe mostrar primero los con estado announced , ordenados mostrando primero el ms antiguo y de ltimo el ms viejo (segn eatc-publication_datetime) , luego los awarded ordenados tambin del ms antiguo al ms viejo y por ltimo los scheduled ordenados de la misma forma 
&#160; 
 El informe debe ser construido en tiempo real para mostrar la fotografa (o estado actual) de los anuncios en el momento que se carga el informe. Se debe habilitar un botn para &quot;refrescar&quot; la carga de informacin.&#160; 
&#160; 
 Cada anuncio de donacin ( eatc_dona_headers ) se presenta la siguiente informacin&#58; 
&#160; 
 Cdigo del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-code 
&#160; 
 Fecha y hora del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Punto de donacin&#58; 
 &#160; eatc_dona_headers .eatc_pod_name 
&#160; 
 Punto de donacin&#58; 
 &#160; eatc_dona_headers .eatc_pod_address 
&#160; 
 ***NUEVO&#58;***Consulta de match 
 Se esta consulta ya la tiene el informe, la solicitud es que se coloque ms adelante, ms hacia la izquierda, porque es algo que se debe consultar de primera mano y hay veces que toca ocultar columnas (como por ejemplo la de latitud y longitud) para poder visualizarlo. &#160; 
&#160; 
 ***NUEVO&#58;***Ciudad&#58; 
 Se toma este dato eatc_dona_headers . eatc_pod_id y con l se enva la consulta a &#123;&#123;URL_entorno&#125;&#125;api/allpods/eatc_pods?eatc-id= para obtener el dato &quot; eatc-city &quot; 
&#160; 
 Estado ( eatc_dona_states ) 
 &#160; eatc_dona_headers .eatc-state 
&#160; 
 Peso total (del anuncio) 
 eatc_dona_headers .eatc-total_weight_kg 
&#160; 
 Valor total (del anuncio) 
 eatc_dona_headers .eatc-total_cost 
&#160; 
 Botn &quot;Regenerar Match&quot; 
 Este botn permitir generar un registro de match ,&#160; y solo se podr visualizar en los anuncios cuyo estado sea announced .&#160; Esta regeneracin del Match puede hacerse de dos maneras (inclusive pueden ser dos botones diferentes&#160; 
&#160; 
 Match selectivo&#58; Consulta de eatc_donation_managers cercanos (similar a como se implement en la funcionalidad de activacin de eatc_donation_managers) 
 El sistema desplegar una lista de los Gestores de donacin ordenados por cercana y mostrando sus capacidades (gestin y recogida)&#160; y con la posibilidad de seleccionarlos mediante un check box en cada registro.&#160; Al regenerar el match, el anuncio se asignar en el registro de match &#160; a los eatc_donation_managers seleccionados (sin tener en cuenta los criterios de capacidad de recogida y gestin).&#160; En este listado se debe colocar los KM de distancia de cada eatc_donation_manager con la coordenada del anuncio respectivo, y permitir ordenar por esa columna. 
&#160; 
 Match por cercana (puede ser en una segunda etapa)&#58; 
 Se abre un campo de captura en donde el usuario pueda digitar los KM a la redonda a los cuales se podr hacer match.&#160; Con este dato se se realiza la operacin de match por cercana , y se le debe informar al usuario con cuntas organizaciones se registr el match. Vale la pena resaltar que este match no tendr en cuenta el criterio de capacidad de recogida y gestin para operar. 
&#160; 
 Datos que se muestran despus del botn de &quot;Regenerar Match&quot; 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre&#58; eatc_dona_headers .eatc-donation_manager_name 
 Direccin&#58; eatc_dona_headers .eatc-donation_manager_address 
 Telfono&#58; eatc_dona_headers .eatc-donation_manager_address 
 Ver mapa (Puede ser en una segunda etapa)&#58; consulta de las coordenadas del anuncio eatc_dona_headers .eatc-lat, eatc_dona_headers .eatc-long 
&#160; 
 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga &quot;PENDIENTE DE ADJUDICACIN&quot; 
&#160; 
 TRACKING&#58; 
&#160; 
 Hora adjudicacin 
 eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Hora de entrega programada 
 eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Hora de entrega real llegada 
 eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Hora de entrega real salida 
 eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Hora de recepcin 
 eatc_dona_headers .eatc-receipt_datetime 

&#160; 
 Vnculo&#58; consulta del match del anuncio&#58; 
 Por cada anuncio debe haber un vnculo &quot;match&quot; para consultar los registros de match de dicho anuncio, desplegando informacin bsica del punto de donacin y de la organizacin con la cual hizo match (funcionalidad ya implementada). 
&#160; 
 [NUEVO] Borrado del registro de match 
 Cada registro de match debe tener la posibilidad de seleccionarse y borrarse (borrado del registro en la tabla eatc_match_registry).&#160; 
&#160; 
 [NUEVO] Borrado en lote del registro de match 
 Se podrn seleccionar varios registros de match de manera simultnea para hacer un borrado en lote (borrado del registro en la tabla eatc_match_registry).&#160; 
&#160; 
 Botn&#58; consulta de novedades de anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de novedades ( eatc_odd_rejection_registry ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. 
&#160; 
 Ejemplo&#58; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40716, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code=40716 
&#160; 
 Botn&#58; consulta de histrico de estados del anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de de histrico de estados ( eatc_dona_header_state_history ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. Esta informacin debe estar ordenada ascendentemente por fecha ( eatc-date_time ) 
&#160; 
 Ejemplo&#58; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40717, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 
&#160; 
 Botn&#58; consulta de histrico de coordenadas del anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de de histrico de estados (eatc_dona_header_geo_history) para el anuncio particular en un mapa 
&#160; 
 Ejemplo&#58; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40717, el sistema debe realizar la siguiente consulta para mostrar los puntos en el mapa 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?eatc-dona_header_code=40717 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Donantes Desktop 

 INFORME OPERATIVO DE ANUNCIOS DE DONACIN (EATC_DONA_LST2)