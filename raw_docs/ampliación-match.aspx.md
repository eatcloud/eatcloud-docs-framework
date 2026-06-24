# ampliación-match.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El match crece automticamente hasta 120 km, hace 4 iteraciones sumando 30 km en cada una. 

 Descripcin de proceso: 
 1.  Trae los match del da de anterior y actual (al da de hoy 2021-02-04,2021-02-05) son aproximadamente 30.000 registros 

 2.  Trae los anuncios cuyo estado sea announced del da anterior y actual. 

 3.  Trae eatc_donation_managers cuyo estado sea activo. 

 4.   Se revisa si el anuncio del punto 2 ya tiene match, en caso de que si, revisa si la distancia es menor a 25 km y tambin si han pasado 120 min desde la publicacin para enviar un mensaje indicando que existe un anuncio cerca. Adems, se hace match hasta los 120 km de distancia (si la distancia es mayor a 70 km y la carga menos a 1000kg, no hace match) 

 5.  Se revisa si el anuncio del punto 2 ya tiene match, en caso de que no, se hace match hasta los 120 km de distancia (si la distancia es mayor a 70 km y la carga menos a 1000kg, no hace match) 

 6.  Este proceso corre a las 10 y 11 am , tambin 14 y 16 pm 

 ANTERIORMENTE:  
 Realizando anlisis de datos de la plataforma, aproximadamente a mayo de 2020, se definieron las siguientes reglas para realizar una ampliacin del radio del match original 
 1. Si la distancia es mayor a 70km y los kg es menor a 1000, no se ampla el radio.  
 2. Ampliacin de radio en KM para hacer match: el radio comienza en 30 km y con esta distancia el sistema intenta hacer match, si no result nada (es decir, no se produjo ningn match), vuelve a intentar sumando 30 km ms (es decir, el radio para hacer match ya es de 60 km) ; si no consigui match, vuelve a sumar 30 km, as sucesivamente hasta que sume 120 km, es decir 4 veces hace el intento. 
 3. Dado lo anterior si no hubo match, se queda sin match. 

 El proceso se corre a las siguientes horas : 10,11,14,16 minuto 0 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 AMPLIACIN DEL MATCH