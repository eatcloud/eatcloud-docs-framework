# mapa-público.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se dispondr de un mapa que debe estar abierto al pblico en general (y que debe vincularse desde el sitio web https://eatcloud.com , por lo tanto debe incorporar aspectos de diseo que estn presente en esa web y apartarse un poco de lo que se ha venido utilizando en plataformas back), para visualizar la ubicacin de los puntos de donacin y de los beneficiarios de un pas particular (y sera muy bueno tener un contador de Puntos de donacin y Beneficiarios mostrados en el mapa).  Por esta razn se debern disponibilizar mapas pblicos por pas (comenzando con Colombia) los cuales debern mostrar la siguiente informacin: 

 Nota importante 1: persistencia: 
 Puede ser importante  una persistencia adicional en donantes/allpods ( eatc_pods_map ) y en beneficiarios/abaco ( eatc_doma_map ) en donde se guarde solo la informacin requerida para este mapa, esto con el nimo de no exponer al pblico servicios con datos relevantes y no sobrecargar la consulta de tablas que se utilizan en produccin (se puede activar un proceso nocturno que genere la informacin de estas tablas desde donantes/allpods/eatc_pods y beneficiarios/abaco/eatc_donation_managers estos esquemas de persistencia solo guardaran lo siguiente: 

 donantes/allpods (eatc_pods_map) 

 eatc-name 
 eatc-city 
 eatc-country 
 eatc-lat 
 eatc-lon 

 beneficiarios/abaco (eatc_doma_map) 

 organizacin 
 municipio 
 departamento 
 eatc-lat 
 eatc-lon 

 Tambin podr explorarse la generacin de un archivo KML que pueda ser cargado al Mapa con esa informacin, en vez del manejo de  llamados al API para mostrar los puntos. 

 Nota importante 2: mapa 
 Actualmente utilizamos OpenStreetMap para el mapa.  En una segunda etapa debemos poder cambiar este mapa por uno de Google que nos lo suministrar Servinformacin (aliado de EatCloud en actividades en el marco de la coyuntura COVID-19) 

 Nota importante 3: convensiones 
 Este mapa solo contar con dos tipos de Pines, que deben poderse diferenciar a simple vista y contar con una indicacin de convenciones en el mapa para donantes y beneficiarios .  Los pines deben identificar los puntos de donacin y los beneficiarios abajo descritos 

 Puntos de donacin (eatc_pods) 

 Se deber consultar la tabla que se cre para consolidar los puntos de donacin de todas las cuentas par establecer los puntos de donacin en cada pas (para el caso de Colombia la consulta es: https://donantes.eatcloud.info/api/allpods/eatc_pods?eatc-country=co o https://donantes.eatcloud.info/api/allpods/eatc_pods_map?eatc-country=co ) y ubicar en el mapa la correspondiente eatc-lat y eatc-lon de los puntos de donacin habilitados.  

 Informacin que se debe mostrar al hacerle clic al PIN 

 Al hacerle clic al PIN se debe mostrar la siguiente informacin: 

 [Titulo] DONANTE: 

 eatc-name : bajo la etiqueta: "Nombre" 
 eatc-city : bajo la etiqueta: Ciudad 
 eatc-country : bajo la etiqueta: "Pas" 

 Beneficiarios (eatc_donation_managers) 
 Se deber consultar de acuerdo a la cuenta del BO los gestores de donacin (beneficiarios) y ubicar en el mapa la correspondiente eatc-lat y eatc-lon de los gestores de donacin habilitados (para el caso de Colombia la consulta ser:  https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=_*   o    https://beneficiarios.eatcloud.info/api/abaco/eatc_doma_map?_id=_ * dado que baco es la cuenta maestra para Colombia) 

 Informacin que se debe mostrar al hacerle clic al PIN 

 Al hacerle clic al PIN se debe mostrar la siguiente informacin: 

 [Titulo] BENEFICIARIOS: 

 organizacin : bajo la etiqueta: "Nombre" 
 municipio : bajo la etiqueta: Ciudad 
 departamento : bajo la etiqueta: "Departamento" 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MAPA PBLICO