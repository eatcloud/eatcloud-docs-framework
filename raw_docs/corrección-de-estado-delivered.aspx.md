# corrección-de-estado-delivered.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando hay fechas de " eatc-receipt_datetime " y de " eatc_code_verification_datetime " registradas en el anuncio este debe pasar a estado " received " (en muchos casos se est quedando como " delivered ") 

 A partir de analizar el caso en donde el nmero de anuncios con estado " delivered " no guardaba correspondencia con el nmero de anuncios pendientes de verificacin del cdigo y el nmero de anuncios pendientes de verificacin detallada, se pudo comprobar que algunos anuncios, que poseen registros vlidos en ambas fechas, estn quedando en estado " delivered " en vez de " received ".  Dado que esto puede deberse a un bug en la APP o en el proceso de verificacin de anuncios que puede ser difcil de ubicar y corregir, se deber implementar un proceso nocturno que revise para las donaciones cuyo eatc-state=" delivered " si se cumple la doble condicin (prueba lgica "y") de tener una fecha vlida registrada en " eatc-receipt_datetime " (es decir que sea diferente a " 0000-00-00 00:00:00 ") "y" de tener una fecha vlida registrada en " eatc-eatc_code_verification_datetime " (es decir que sea diferente a " 0000-00-00 00:00:00 ") , para cambiarles el estado de " delivered " a " received ". 

 Este proceso deber programarse en todas las nubes (abaco, argentina, mexico) en todos los ambientes. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CORRECIN DE ESTADO "DELIVERED" MAL REGISTRADO