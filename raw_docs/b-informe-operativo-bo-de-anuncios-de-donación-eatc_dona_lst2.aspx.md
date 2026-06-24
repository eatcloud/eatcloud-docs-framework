# b-informe-operativo-bo-de-anuncios-de-donación-eatc_dona_lst2.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Desde el BO actualmente habilitado para la cuenta maestra de beneficiarios baco (https://beneficiarios.eatcloud.info/bo/[master_CUA] ) https://beneficiarios.eatcloud.info/bo/abaco se debe realizar un informe de los anuncios de donacin generados en el sistema siguiendo las siguientes directrices 

 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado "announced" o "anunciado", "awarded" o "adjudicado" y "scheduled" o programado , es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 

 Consulta de anuncios 
 el sistema toma el parmetro " abaco " del master CUA respectivo (que se digita en la URL de ingreso al BO) y se traen todos los anuncios para dicha cuenta cuyo estado por defecto sea announced,awarded,scheduled 

 Ejemplo: 
 El BO dispuesto para BACO (https://beneficiarios.eatcloud.info/bo/[master_CUA] ) https://beneficiarios.eatcloud.info/bo/abaco se toma el  master_CUA es decir abaco y se traen todos los anuncios cuyos estados sean, anunciados, adjudicados y programados (eatc-state=announced,awarded,scheduled) 

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?_id=_*&eatc-state=announced,awarded,scheduled  
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&eatc-state=announced,awarded,scheduled&_compress   

 Filtros (segunda prioridad: no se requiere para una primera entrega) 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin con diferentes estados a los del filtro por defecto 

 Ejemplo: 
 El BO dispuesto para BACO (https://beneficiarios.eatcloud.info/bo/[master_CUA] ) https://beneficiarios.eatcloud.info/bo/abaco se toma el  master_CUA es decir abaco y se traen todos los anuncios cuyos estados sean, despachados y recividos (eatc-state=delivered,recieved): 

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? _id=_* &eatc-state=derivered,recieved  

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

 Punto de donacin: 
   eatc_dona_headers .eatc_pod_name 

 Punto de donacin: 
   eatc_dona_headers .eatc_pod_address 

 ***NUEVO:***Consulta de match 
 Se esta consulta ya la tiene el informe, la solicitud es que se coloque ms adelante, ms hacia la izquierda, porque es algo que se debe consultar de primera mano y hay veces que toca ocultar columnas (como por ejemplo la de latitud y longitud) para poder visualizarlo.   

 ***NUEVO:***Ciudad: 
 Se toma este dato eatc_dona_headers . eatc_pod_id y con l se enva la consulta a {{URL_entorno}}api/allpods/eatc_pods?eatc-id= para obtener el dato " eatc-city " 

 Estado ( eatc_dona_states ) 
   eatc_dona_headers .eatc-state 

 Peso total (del anuncio) 
 eatc_dona_headers .eatc-total_weight_kg 

 Valor total (del anuncio) 
 eatc_dona_headers .eatc-total_cost 

 Botn "Regenerar Match" 
 Este botn permitir generar un registro de match ,  y solo se podr visualizar en los anuncios cuyo estado sea announced .  Esta regeneracin del Match puede hacerse de dos maneras (inclusive pueden ser dos botones diferentes  

 Match selectivo: Consulta de eatc_donation_managers cercanos (similar a como se implement en la funcionalidad de activacin de eatc_donation_managers) 
 El sistema desplegar una lista de los Gestores de donacin ordenados por cercana y mostrando sus capacidades (gestin y recogida)  y con la posibilidad de seleccionarlos mediante un check box en cada registro.  Al regenerar el match, el anuncio se asignar en el registro de match   a los eatc_donation_managers seleccionados (sin tener en cuenta los criterios de capacidad de recogida y gestin).  En este listado se debe colocar los KM de distancia de cada eatc_donation_manager con la coordenada del anuncio respectivo, y permitir ordenar por esa columna. 

 Match por cercana (puede ser en una segunda etapa): 
 Se abre un campo de captura en donde el usuario pueda digitar los KM a la redonda a los cuales se podr hacer match.  Con este dato se se realiza la operacin de match por cercana , y se le debe informar al usuario con cuntas organizaciones se registr el match. Vale la pena resaltar que este match no tendr en cuenta el criterio de capacidad de recogida y gestin para operar. 

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
 Con este botn se debe generar una consulta al registro de de histrico de estados (eatc_dona_header_geo_history) para el anuncio particular en un mapa 

 Ejemplo: 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40717, el sistema debe realizar la siguiente consulta para mostrar los puntos en el mapa 

 https://donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?eatc-dona_header_code=40717   

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Donantes Desktop 

 INFORME OPERATIVO DE ANUNCIOS DE DONACIN (EATC_DONA_LST2)