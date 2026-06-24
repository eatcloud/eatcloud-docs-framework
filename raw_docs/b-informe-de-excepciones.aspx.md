# b-informe-de-excepciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***REVISAR*** 

 Este informe presenta consulta de las novedades de los anuncios de donacin, para un rango de fechas especfico (el valor por defecto del rango de fechas al presentar el informe debe ser el da actual) y funcionalidades propias de "data-tables" (exportacin a excel, csv, filtros, ordenamientos, etc), para el punto de donacin respectivo. 

 Este informe debe ser accedido desde un botn en el men lateral izquierdo (abajo del vnculo al informe operativo de donaciones y encima del botn salir) 

 Se debe generar mediante una consulta al registro de novedades ( eatc_odd_rejection_registry ) el punto de donacin en particular. 

 Por almacn o grupo de almacenes: ejemplo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&_compress   
 Por marca: ejemplo https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_a=exito&_compress   
 Por subzona: ejemplo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_b=MEDELLIN&_compress 
 Por distrito: ejemplo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_c=DISTRITO%20BODEGA%204%20ANTIOQUIA&_compress 

 Se toma el dato " cont " que entrega el API y se pinta en la tarjeta 

 Ejemplo: 
 Para el punto de donacin xito de San Antonio cuyo cdigo es 39 ( eatc-pod_id), el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 

 NOTA : tener en cuenta la variable DOM en la implementacin para la primera parte de los llamados a las APIs 

 https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-pod_id=39   

 Si la consulta por algn motivo no arroja resultados, se debe informar de esto mediante un mensaje que salga en la pantalla 

 Para realizar el clculo se debe invocar el API:  

 Ejemplo: 
 Un usuario asignado al (eatc_tipology_c) DISTRITO MEDELLIN B, el sistema deber realizar la siguiente consulta: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_typology_c=DISTRITO%20MEDELLIN%20B&_compress , como la respuesta del API es:  
 { 
 ts : "191216153945", 
 op : true, 
 cont : 39, 
 res : 

 Debe mostrar el nmero 39 como KPI principal de proceso 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 INFORME DE EXCEPCIONES (BO BENEFICIARIOS) PENDIENTE REVISAR