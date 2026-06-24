# corrección-de-estados-de-las-ofertas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Con el nimo de garantizar que las ofertas tengan un estado acorde con sus caractersticas y de esta manera no desplegar ofertas que ya han sido totalmente ordenadas, se establece el siguiente proceso que debe correr de manera peridica para corregir los estados de las ofertas. 

 Consulta de las ofertas cuyo estado debe ser coregido 
 El sistema debe consultar aquellas ofertas cuyo estado () debe ser corregido porque el mismo presenta inconsistencias con los datos guardados (la principal inconsistencia que se va a corregir, es cuando una oferta no tiene productos disponibles y la misma sigue apareciendo como "ofertada" o "parcialmente ordenada", como se deriva de la siguiente consulta) 

 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale?eatc-odd_quantity= 0& eatc-odd_state= sale,partially_ordered &blocked=no 

 Los registros que se obtienen de la anterior consulta, deben ser editados de la siguiente manera: 

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla=eatc_sale&_operacion=update&eatc-odd_state= ordered &WHERE_id={{array_ids}} 

 Ejemplo (ambiente de pruebas): 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale?eatc-odd_quantity= 0& eatc-odd_state= sale,partially_ordered &blocked=no 

 Como la consulta (al momento de hacer el ejemplo) trae 6 _id diferentes, se deben conformar un array de los mismos y hacer el siguiente llamado (se hace el mismo solo con 2 para dejar los otros 4 para probar la implementacin) 

 https://devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&_operacion=update&eatc-odd_state= ordered &WHERE_id=2,4   

 Nota importante: al momento de hacer la prueba con el array de _id (2 y 4) el sistema solo hizo la actualizacin del registro cuyo _id=2 (el otro no se efectu).  Es un tema que se debe revisar 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CORRECIN DE ESTADOS DE LAS OFERTAS