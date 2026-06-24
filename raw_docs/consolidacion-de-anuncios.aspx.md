# consolidacion-de-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripciones: 

 Naturaleza de la consolidacin 
 En la consolidacin solo deben entrar dos anuncios, uno que se constituir en origen y otro que se constituir en destino.  Por lo tanto el proceso podr ser construido para que recibiendo dos eatc-code, se pueda proceder con la consolidacin. 

 El proceso de consolidacin de anuncios es uno que toma los detalles de un anuncio mas antiguo y los adiciona a los de uno ms nuevo, con el nimo que al ir consolidando la informacin, se genere ms oportunidad para que el nuevo anuncio que incorpora ms mercanca, sea adjudicado y recogido. 

 Anuncio origen 
 Es el anuncio cuya fecha es ms antigua, y por lo tanto es consolidado en un anuncio posterior. Para consolidarse un anuncio no puede haber sido adjudicado. Los anuncios origen deben pasar a un esquema de persistencia nuevo (dado que no deben aparecer en la nube de donaciones) y que ser para anuncios que se consolidaron ( eatc_dona_headers_consolidated ) que para todo efecto tiene la misma estructura que eatc_dona_headers .  El encabezado del anuncio consolidado ( eatc_dona_headers) deber tener un nuevo parmetro ( eatc_consolidation_destination ) en donde se guardar el eatc-code del anuncio en el cual se consolida y de esta manera poder tener trazabilidad y seguimiento 

 Anuncio destino 
 Es el anuncio cuya fecha es ms nueva, y por lo tanto es consolidado en un anuncio posterior.  Para poder consolidar dos anuncios los mismos debern contener el mismo punto de donacin ( eatc-pod_id ) y el mismo donante ( eatc-donor ). Los anuncios destino deben permanecer en la estructura de persistencia eatc_dona_headers .  El encabezado del anuncio ( eatc_dona_headers)   que consolida al anterior deber tener un nuevo parmetro ( eatc_consolidation_origin ) en donde se guardar el eatc-code del anuncio que consolida y de esta manera poder tener trazabilidad y seguimiento. 

 Proceso para determinar que anuncios son susceptibles de consolidarse 
 Antes de realizar los procesos de match, se debe realizar un proceso que revise si para cada eatc_pod , existen dos anuncios, de un mismo donante ( eatc-donor ), que no han sido adjudicados (eatc-state= announced ). Cuando se encuentre un par de anuncios con esta condicin, se debe activar el proceso de consolidacin ( siguiente proceso, que idealmente debe correrse tambin antes que el match). Este proceso se debe iterar (por si hay ms de dos anuncios en esa condicin) apenas se termine el proceso de consolidacin , para garantizar que todo quede consolidado. Cuando este proceso no arroje ms resultados (es decir, cuando todo est consolidado), se podr proseguir con el match. 

 Proceso de consolidacin: 

 Revisin de condiciones para la consolidacin 

 Dados dos anuncios de donacin, el primer paso del proceso debe hacer las siguientes verificaciones para poder seguir adelante con la consolidacin: 

 Que ambos anuncios tengan estado " announced ". Si esta condicin no se cumple el proceso no puede proseguir. 
 Que ambos anuncios tengan el mismo eatc-pod_id . Si esta condicin no se cumple el proceso no puede proseguir. 
 Que ambos anuncios tengan el mismo eatc-donor . Si esta condicin no se cumple el proceso no puede proseguir con la consolidacin. 

 Determinacin del origen y del destino 

 El sistema debe comparar las fecha de publicacin de los anuncios ( eatc-publication_datetime ) y de acuerdo a ello hacer lo siguiente: 

 Al anuncio ms antiguo, se le debe considerar como el origen. 
 Al anuncio ms nuevo se le debe considerar como el destino. 

 Operaciones sobre el anuncio origen 
 Se debe generar un registro en el campo (nuevo) eatc_consolidation_destination con el cdigo ( eatc-code ) del anuncio en el cual se consolida (destino). 
 Se debe realizar una copia del anuncio (eatc_dona_headers) a la tabla (nueva) eatc_dona_headers_consolidated. 
 Una vez se valide la realizacin efectiva de la copia, se debe borrar el anuncio de la tabla eatc_dona_headers 
 Se deben consultar los detalles del respectivo anuncio (eatc_dona) y copiarlos a la tabla (nueva) eatc_dona_consolidated 
 Se deben consultar los detalles del respectivo anuncio (eatc_dona) y en el campo eatc-dona_header_code se debe colocar el eatc-code del anuncio destino. 

 Operaciones sobre el anuncio destino. 
 Se debe generar un registro en el campo (nuevo) eatc_consolidation_origin con el cdigo ( eatc-code ) del anuncio que se consolida (origen). 
 Se deben calcular de nuevo los datos que presentan totales en el anuncio, teniendo en cuenta los nuevos detalles de anuncio (eatc_dona) que se le registraron en las operaciones realizadas sobre el origen, a saber: 
 eatc-original_cost 
 eatc-total_cost 
 eatc-original_weight_kg 
 eatc-total_weight_kg 
 eatc-odd_total_volume_cm3 
 eatc-original_VAT 
 eatc-total_VAT 

 Cuando se termine el proceso de consolidacin se debe volver a llamar el proceso para determinar que anuncios son susceptibles de consolidarse a fin de garantizar que todos los anuncios se consoliden.  

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONSOLIDACIN DE ANUNCIOS