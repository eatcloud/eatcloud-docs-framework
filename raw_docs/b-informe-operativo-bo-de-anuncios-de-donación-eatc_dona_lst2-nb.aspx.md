# b-informe-operativo-bo-de-anuncios-de-donación-eatc_dona_lst2-nb.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo: 
 En la actualidad este informe est habilitado en el BO Legacy de Abaco ({{ URL_entorno_beneficiarios }}.eatcloud.info/bo/{{_DOM. cua_master }}, ejemplo: https://beneficiarios.eatcloud.info/bo/abaco ).  Este informe, enfocndose en la funcionalidad de " Permitir descargar los anuncios en formato .csv " debe migrarse al nuevo BO ({{ URL_entorno_beneficiarios }}.eatcloud.info/signin ejemplo: https://beneficiarios.eatcloud.info/signin ).  Se copia la documentacin legacy en este punto, pero se debe tener en cuenta que la misma es ya antigua y por lo tanto susceptible a mejoras.  Por este motivo, el desarrollo debe centrarse en realizar la migracin de lo que se tiene actualmente en el BO legacy y hacerlo disponible en el nuevo BO (no tanto en lo que dicta la documentacin). 

 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado "announced" o "anunciado", "awarded" o "adjudicado" y "scheduled" o programado , es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 

 ***NUEVO: Filtro de fechas por defecto *** 
 El sistema deber colocar por defecto como fecha inicial , dos das antes de la fecha actual, es decir, si la consulta se hace el 4 de julio de 2024 ( fecha final ), debe aparecer por defecto fecha inicial (2 de julio de 2024). La fecha final por defecto es la fecha actual. 
 En la actualidad, como se muestra en la siguiente imagen , la fecha inicial por defecto es la misma fecha final (fecha actual) 

 Consulta de anuncios 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 

 El sistema toma el parmetro " {{_DOM. cua_master }} " del master y se traen todos los anuncios para dicha cuenta cuyo estado por defecto sea announced,awarded,scheduled 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/ eatc_dona_headers ?eatc-state=announced,awarded,scheduled & {{filtro_eatc_dona_headers (tipo_X) }} 

 Filtros 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin con diferentes estados a los del filtro por defecto 

 {{ URL_entorno_donantes }}.eatcloud.info/api/{{_DOM. cua_master }}/ eatc_dona_headers ?eatc-state=announced,awarded,scheduled& & {{filtro_eatc_dona_headers (tipo_X) }} 

 Listado de anuncio de donacin 
 Un listado en data tables, con las funcionalidades clsicas de ordenamiento, bsqueda y dems. 

 Ordenamiento: 
 El listado de anuncios debe mostrar primero los con estado announced , ordenados mostrando primero el ms antiguo y de ltimo el ms viejo (segn eatc-publication_datetime) , luego los awarded ordenados tambin del ms antiguo al ms viejo y por ltimo los scheduled ordenados de la misma forma 

 El informe debe ser construido en tiempo real para mostrar la fotografa (o estado actual) de los anuncios en el momento que se carga el informe. Se debe habilitar un botn para "refrescar" la carga de informacin.  

 Cada anuncio de donacin ( eatc_dona_headers ) se presenta la siguiente informacin: 

 Cdigo del anuncio: 
   eatc_dona_headers .eatc-code 

 Fecha y hora del anuncio: 
   eatc_dona_headers .eatc-publication_datetime 

 Estado ( eatc_dona_states ) 
   eatc_dona_headers .eatc-state 

 Beneficiario (class=lbl_beneficiario): 
 eatc_dona_headers . eatc-donation_manager_name   

 Punto de donacin: 
   eatc_dona_headers .eatc_pod_name 

 Punto de donacin: 
   eatc_dona_headers .eatc_pod_address 

 Consulta de match 
 Se esta consulta ya la tiene el informe, la solicitud es que se coloque ms adelante, ms hacia la izquierda, porque es algo que se debe consultar de primera mano y hay veces que toca ocultar columnas (como por ejemplo la de latitud y longitud) para poder visualizarlo.   

 ***NUEVO: Veces con match (class= lbl_veces_con_match => crear label ) *** 
 El sistema realiza la siguiente consulta:  

 {{ URL_beneficiarios }}/api/{{_DOM. cua_master }}/eatc_match_registry?eatc-dona_header_code={{ eatc_dona_headers . eatc-code }}&_cont 

 Si el nmero es menor que 5 el mismo se debe presentar en fondo rojo 
 Si el nmero est entre 5 y 10 el mismo se debe presentar en fondo naranja 
 Si el nmero es mayor que 10 se presenta en forndo verde 
 ***NUEVO: El nmero deber presentar un vinculo con el siguiente enlace *** 

 Ambiente de pruebas: https://mobixconsulting-dev-bo-audit.hf.space/eatc-headers?eatc_code= {{ eatc_dona_headers . eatc-code }} 

 Ambiente de produccin: https://mobixconsulting-prod-bo-audit.hf.space/eatc-headers?eatc_code= {{ eatc_dona_headers . eatc-code }} 
 La respuesta del endpoint deber mostrarse en un modal. 

 Ciudad: 
 Se toma este dato eatc_dona_headers . eatc_pod_id y con l se enva la consulta a {{URL_entorno}}api/allpods/eatc_pods?eatc-id= para obtener el dato " eatc-city " 

 Peso total (del anuncio) 
 eatc_dona_headers .eatc-total_weight_kg 

 Valor total (del anuncio) 
 eatc_dona_headers .eatc-total_cost 

 ***NUEVO: Fecha ms prxima de vencimiento (class=lbl_fecha_proxima_vencimiento) *** 
 eatc_dona_headers . eatc_closer_expiration_date  

 ***NUEVO: Botones (vnculos) a archivos adjuntos *** 
 El sistema realiza la siguiente consulta:  
 {{ URL_datagov }}/api/eatcloud/eatc_photo_registry?eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_cmp=eatc_label,eatc_photo   

 Si la consulta trae una respuesta, entonces el sistema pinta en la interfaz, el label o los labels que devuelve la consulta 
 class="{{eatc_photo_registry. eatc_label }}"  

 Y los vincula (al hacer clic en los mismos desplegando en pestaa separada), al archivo (ruta) que llega en el parmetro {{eatc_photo_registry. eatc_photo }} 

 eatc_photo }}>{{eatc_photo_registry. eatc_label }} 

 Al presionar el botn / vnculo se deber permitir descargar el adjunto respectivo. 

 Botn "Regenerar Match" ***NUEVO: Filtro (a quienes se le muestra esta funcionalidad): *** 
 A los usuarios tipo  eatc_cua_master 

 Toda la funcioalidad para regenerar el match y hacer match manual estar restringida a los usuarios pertenecientes a la cuenta maestra 
 Este botn permitir generar un registro de match ,  y solo se podr visualizar en los anuncios cuyo estado sea announced .  Esta regeneracin del Match puede hacerse de dos maneras (inclusive pueden ser dos botones diferentes  

 Match selectivo: Consulta de eatc_donation_managers cercanos (similar a como se implement en la funcionalidad de activacin de eatc_donation_managers) 
 El sistema desplegar una lista de los Gestores de donacin ordenados por cercana y mostrando sus capacidades (gestin y recogida)  y con la posibilidad de seleccionarlos mediante un check box en cada registro.  Al regenerar el match, el anuncio se asignar en el registro de match   a los eatc_donation_managers seleccionados (sin tener en cuenta los criterios de capacidad de recogida y gestin).  En este listado se debe colocar los KM de distancia de cada eatc_donation_manager con la coordenada del anuncio respectivo, y permitir ordenar por esa columna. 

 Match por cercana: 
 Se abre un campo de captura en donde el usuario pueda digitar los KM a la redonda a los cuales se podr hacer match.  Con este dato se se realiza la operacin de match por cercana , y se le debe informar al usuario con cuntas organizaciones se registr el match. Vale la pena resaltar que este match no tendr en cuenta el criterio de capacidad de recogida y gestin para operar. 

 ***NUEVO : DATO DE DONACIONES GESTIONADAS EN LOS LTIMOS 60 DAS EN LA INFORMACIN DEL BENEFICIARIO *** 
 En el anterior listado incorporar la siguiente columna (despus del campo " organizacion " =>Pasar el campo " Coordenadas " para despus del e-mail ): 

 Donaciones gestionadas 
 class=" lbl_donaciones_gestionadas ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donaciones_gestionadas   

 class=" lbl_donaciones_gestionadas_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel=lbl_donaciones_gestionadas_desc   

 "Donaciones gestionadas por el beneficiario en los ltimos 60 das (a partir de estado "delivered")" 

 Llamado para el clculo: 
 Para obtener el numerador del dato solicitado se realiza el siguiente llamado: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-publication_date[0]={{ fecha_de_un_mes_atras }}&eatc-publication_date[1]={{ fecha_actual }}& eatc-donation_manager_code = {{eatc_donation_managers. identificador_unico_registro }}&eatc-state=delivered,received,pre-certified,certified&_cont 

 Se toma el " count " de la respuesta obtenida como el dato que se presenta en la columna 

 Datos que se muestran despus del botn de "Regenerar Match" 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre: eatc_dona_headers .eatc-donation_manager_name 
 Direccin: eatc_dona_headers .eatc-donation_manager_address 
 Telfono: eatc_dona_headers .eatc-donation_manager_address 
 Ver mapa (Puede ser en una segunda etapa): consulta de las coordenadas del anuncio eatc_dona_headers .eatc-lat, eatc_dona_headers .eatc-long 

 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga "PENDIENTE DE ADJUDICACIN" 

 TRACKING: 
 Hora adjudicacin 
 eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega programada 
 eatc_dona_headers .eatc-programed_picking_datetime 

 Hora de entrega real llegada 
 eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real salida 
 eatc_dona_headers .eatc-picking_checkout_datetime 

 Hora de recepcin 
 eatc_dona_headers .eatc-receipt_datetime 

 Vnculo: consulta del match del anuncio: 
 Por cada anuncio debe haber un vnculo "match" para consultar los registros de match de dicho anuncio, desplegando informacin bsica del punto de donacin y de la organizacin con la cual hizo match (funcionalidad ya implementada). 

 [NUEVO] Borrado del registro de match 
 Cada registro de match debe tener la posibilidad de seleccionarse y borrarse (borrado del registro en la tabla eatc_match_registry).  

 [NUEVO] Borrado en lote del registro de match 
 Se podrn seleccionar varios registros de match de manera simultnea para hacer un borrado en lote (borrado del registro en la tabla eatc_match_registry).  

 Botn: consulta de novedades de anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de novedades ( eatc_odd_rejection_registry ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. 

 Ejemplo: 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40716, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 

 https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code=40716 

 Botn: consulta de histrico de estados del anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de de histrico de estados ( eatc_dona_header_state_history ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. Esta informacin debe estar ordenada ascendentemente por fecha ( eatc-date_time ) 

 Ejemplo: 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40717, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 

 https://donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 

 Botn: consulta de histrico de coordenadas del anuncio de donacin (puede ser en una segunda etapa) 
 Con este botn se debe generar una consulta al registro de histrico de estados (eatc_dona_header_geo_history) para el anuncio particular en un mapa 

 Ejemplo: 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40717, el sistema debe realizar la siguiente consulta para mostrar los puntos en el mapa 

 https://donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?eatc-dona_header_code=40717   

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-informe-operativo-bo-de-anuncios-de-donaci%C3%B3n-eatc_dona_lst2-nb%2F2717826648-Informe_encabezados_donaciones.jpg&ow=1280&oh=503, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-informe-operativo-bo-de-anuncios-de-donaci%C3%B3n-eatc_dona_lst2-nb%2F2717826648-Informe_encabezados_donaciones.jpg&ow=1280&oh=503 
 EATCLOUD Nuevo BO CUA MASTER 

 627.000000000000 

 B INFORME OPERATIVO BO DE ANUNCIOS DE DONACIN (EATC_DONA_LST2) NB