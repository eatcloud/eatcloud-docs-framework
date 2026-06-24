# b-mapa-de-operaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En este mapa se podrn ver principalmente los puntos de donacin activos en la plataforma, los beneficiarios y los anuncios de donacin. 

 Una vez se tenga una versin inicial del mapa, se debe poder generar una manera de embeber el mapa en sitios web externos. 

 Puntos de donacin (eatc_pods) 
 Se deber consultar la tabla que se cre para consolidar los puntos de donacin de todas las cuentas ( https://donantes.eatcloud.info/api/ all pods/eatc_pods?_id=_* ) y ubicar en el mapa la correspondiente eatc-lat y eatc-lon de los puntos de donacin habilitados.  Estos puntos de donacin se debern distinguir por el grado de actividad que tienen en la plataforma (haciendo una consulta con su respectivo eatc-code al API de eatc_dona_headers as: 

 https://donantes.eatcloud.info/api/[cua]/eatc_dona_headers?eatc-pod_id=[eatc_pods.eatc-id]&_compress 

 Ejemplo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=abaco_bog3&_compress   

 De acuerdo al conteo de la respuesta " cont ", se deben clasificar los puntos en tres categoras (clasificacin dinmica). (La clasificacin del ejemplo anteriormente entregado sera con poca actividad (siendo 2020-04-06) dado que el cont =10 y como se podr ver abajo, cae en esta categora. 

 Pines para puntos de donacin (eatc_pods que se toman de la tabla de consolidacin de puntos de donacin de todas las cuentas https://donantes.eatcloud.info/api/allpods/eatc_pods?_id=_* ) 
 Sin actividad : pin de color plido para puntos de donacin que no hallan tenido donaciones ( cont : 0, err_msg : "No se produjeron resultados") 
 Con poca actividad : pin de color opaco para puntos de donacin que hallan tenido hasta 10 donaciones ( cont 
 Con buena actividad : pin de color vivo para puntos de donacin que hallan tenido 11 o ms anuncios ( cont > 10) 

 Filtros del mapa 
 El mapa deber tener filtros para filtrar por los tres tipos de clasificacin dinmica de los puntos arriba descritos. 

 Informacin que se debe mostrar al hacerle clic al PIN 
 Al hacerle clic al PIN se debe mostrar la siguiente informacin (https://donantes.eatcloud.info/api/[cua]/eatc_pods?_id=_*):  
 eatc-id : bajo la etiqueta: "id" 
 eatc-name : bajo la etiqueta: "Nombre" 
 eatc-phone : bajo la etiqueta: "Telfono" 
 eatc-adress : "bajo la etiqueta: "Direccin" 
 eatc-city : bajo la etiqueta: "Ciudad" 
 eatc-country : bajo la etiqueta: "Pas" 

 [***Nuevo***] Listado de puntos de donacin con actividad 
 Se deja a criterio del ingeniero de implementacin si este informe se coloca en la parte baja del mapa de la presente funcionalidad, o se despliega como una funcionalidad independiente (se coloca en este apartado porque los filtros y las funciones que traen la informacin para el mapa pueden funcionar con pequeos ajustes para la implementacin de esta funcionalidad): 

 Informacin que se debe mostrar en el listado 
 La informacin se trae del maestro unificado de puntos de donacin para la respectiva cuenta maestra: 

 Se consulta la cuenta maestra en cuestin 

 https://beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_cua={{ CUA_master }} 

 De esa consulta se toma el parmetro " eatc-country " y se lleva a la siguiente consulta para traer los puntos de donacin que muestra este BO en particular (hasta el momento: abaco ): 

 {{URL_entorno_donantes}}/api/allpods/eatc_pods? eatc-country ={{ eatc-country }} 
 eatc-id : bajo la etiqueta: " id " 
 eatc-name : bajo la etiqueta: " Nombre " 
 eatc-phone : bajo la etiqueta: " Telfono " 
 eatc-adress : "bajo la etiqueta: " Direccin " 
 eatc-city : bajo la etiqueta: " Ciudad " 
 eatc-province : bajo la etiqueta " Departamento / Provincia " (nuevo campo que se podr traer cuando se implemente esta tarea de mejora ) 
 eatc-country : bajo la etiqueta: Pas 
 bajo la etiqueta: " Donaciones Gestionadas " el nmero de donaciones que gestion el punto en el periodo de la consulta 

 Beneficiarios (eatc_donation_managers) 
 Se deber consultar de acuerdo a la cuenta del BO los gestores de donacin (beneficiarios) y ubicar en el mapa la correspondiente eatc-lat y eatc-lon de los gestores de donacin habilitados.  Estos beneficiarios se debern distinguir por el grado de actividad que tienen en la plataforma (haciendo una consulta con su respectivo eatc-donation_manager_code al API de eatc_dona_headers as: 

 https://donantes.eatcloud.info/api/[cua]/eatc_dona_headers? eatc-donation_manager_code =[eatc_donation_managers. identificador_unico_registro ]&_compress 

 Ejemplo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=891780234&_compress    

 De acuerdo al conteo de la respuesta " cont ", se deben clasificar los beneficiarios en tres categoras (clasificacin dinmica). (La clasificacin del ejemplo anteriormente entregado sera con poca actividad (siendo 2020-04-06) dado que el cont =4 y como se podr ver abajo, cae en esta categora. 

 Pines para beneficiarios (eatc_donation_managers) 
 Sin actividad : pin de color plido para puntos de donacin que no se hallan adjudicado donaciones ( cont : 0, err_msg : "No se produjeron resultados") 
 Con poca actividad : pi de color opaco para puntos de donacin que se hallan adjudicado hasta 10 donaciones ( cont 
 Con buena actividad : pin de color vivo para puntos de donacin que se hallan adjudicado 11 o ms anuncios ( cont > 10) 

 Filtros del mapa 
 El mapa deber tener filtros para filtrar por los tres tipos de clasificacin dinmica de los beneficiarios arriba descritos. 

 Informacin que se debe mostrar al hacerle clic al PIN 
 Al hacerle clic al PIN se debe mostrar la siguiente informacin (https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_manages?_id=_*) 
 identificador_unico_registro : bajo la etiqueta: "Identificacin" 
 organizacin : bajo la etiqueta: "Nombre" 
 telefono1 : bajo la etiqueta: "Telfono" 
 unidad_territorial : "bajo la etiqueta: "Direccin" 
 municipio : bajo la etiqueta: "Ciudad" 
 departamento : bajo la etiqueta: "Departamento" 

 [***Nuevo***] Listado de gestores de donaciones con actividad 
 Se deja a criterio del ingeniero de implementacin si este informe se coloca en la parte baja del mapa de la presente funcionalidad, o se despliega como una funcionalidad independiente (se coloca en este apartado porque los filtros y las funciones que traen la informacin para el mapa pueden funcionar con pequeos ajustes para la implementacin de esta funcionalidad). 

 Informacin que se debe mostrar en el listado 
 La informacin se trae del maestro de gestores de donacin respectivo: 
 {{URL_entorno_beneficiarios}}/api/{{cua_master}}/eatc_donation_managers?_id=_* 
 identificador_unico_registro : bajo la etiqueta: " Identificacin " 
 organizacin : bajo la etiqueta: " Nombre " 
 telefono1 : bajo la etiqueta: " Telfono " 
 unidad_territorial : "bajo la etiqueta: " Direccin " 
 municipio : bajo la etiqueta: " Ciudad " 
 departamento : bajo la etiqueta: " Departamento " 
 eatc_doma_typology_b ; bajo la etiqueta: " Tipologa B " 
 eatc_state : bajo la etiqueta: Estado 
 bajo la etiqueta: " Donaciones Gestionadas " el nmero de donaciones que gestion el punto en el periodo de la consulta. 

 Anuncios de donacin (eatc_dona_headers) 
 Se deber consultar de acuerdo a la cuenta del BO los anuncios de donacin (encabezados) y ubicar en el mapa la correspondiente eatc-lat y eatc-lon de los anuncios que se han producido.  Estos anuncios  se debern distinguir por su estado ( eatc_state) 

 https://donantes.eatcloud.info/api/[cua]/eatc_dona_headers? _id=_* 

 Pines para anuncios de donacin (eatc_dona_headers): 
 Anunciado: pin rojo para estado: announced. 
 Adjudicado: pin naranja para estado:  awarded 
 Programado: pin amarillo para estado:  scheduled 
 Despachado: pin plido para estado: delivered 
 Recibido: pin verde vivo para estado:  recieved 

 Filtros del mapa 
 El mapa deber tener filtros para filtrar por los estados.  Tambin se debe evaluar un filtro por fechas (inicial y final) para traer los anuncios que estn en el rango determinado ( eatc-publication_date) 

 Informacin que se debe mostrar al hacerle clic al PIN 
 Al hacerle clic al PIN se debe mostrar la siguiente informacin ( https://donantes.eatcloud.info/api/[cua]/eatc_dona_headers? _id=_* ) 
 eatc-publication_datetime : bajo la etiqueta: "Fecha y hora de publicacin" 
 eatc-donor : bajo la etiqueta: "Donante" 
 eatc-pod_name : bajo la etiqueta: "Nombre del punto de donacin" 
 eatc-pod_address : bajo la etiqueta: "Direccin del punto de donacin" 
 eatc-pod_phone : bajo la etiqueta: "Telfono del punto de donacin" 
 eatc-total_weight_kg : bajo la etiqueta: "Peso total del anuncio" 
 eatc-total_cost : bajo la etiqueta: "Costo total del anuncio" 
 eatc-state : bajo la etiqueta: "Estado" 
 eatc-adjudication_datetime : bajo la etiqueta: "Fecha y hora de adjudicacin" 
 eatc-donation_manager_name : bajo la etiqueta: "Nombre del gestor de donaciones" 
 eatc-donation_manager_address : bajo la etiqueta: "Direccin del gestor de donaciones", 
 eatc-donation_manager_phone : bajo la etiqueta: "Telfono del gestor de donaciones" 
 eatc_cua_origin : bajo la etiqueta: "Cuenta origen" 

 [***Nuevo***] Listado de donaciones 
 Se deja a criterio del ingeniero de implementacin si este informe se coloca en la parte baja del mapa de la presente funcionalidad, o se despliega como una funcionalidad independiente (se coloca en este apartado porque los filtros y las funciones que traen la informacin para el mapa pueden funcionar con pequeos ajustes para la implementacin de esta funcionalidad). 

 Informacin que se debe mostrar en el listado 
 La informacin se trae del maestro de encabezados de anuncios de donacin: 
 {{URL_entorno_donantes}}/api/{{cua_master}}/ eatc_dona_headers? _id=_* 
 eatc-publication_datetime : bajo la etiqueta: " Fecha y hora de publicacin " 
 eatc-donor : bajo la etiqueta: " Donante " 
 eatc-pod_name : bajo la etiqueta: " Nombre del punto de donacin " 
 eatc-pod_address : bajo la etiqueta: " Direccin del punto de donacin " 
 eatc-pod_phone : bajo la etiqueta: " Telfono del punto de donacin " 
 eatc-total_weight_kg : bajo la etiqueta: " Peso total del anuncio " 
 eatc-total_cost : bajo la etiqueta: " Costo total del anuncio " 
 eatc-state : bajo la etiqueta: " Estado " 
 eatc-adjudication_datetime : bajo la etiqueta: " Fecha y hora de adjudicacin " 
 eatc-donation_manager_name : bajo la etiqueta: " Nombre del gestor de donaciones " 
 eatc-donation_manager_address : bajo la etiqueta: " Direccin del gestor de donaciones ", 
 eatc-donation_manager_phone : bajo la etiqueta: Telfono del gestor de donaciones 
 eatc_cua_origin : bajo la etiqueta: " Cuenta origen " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 B MAPA DE OPERACIONES