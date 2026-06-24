# actualización-de-precios-en-eatc_licenses_prices.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se deber programar un proceso peridico que corra todas las noches, que actualice los precios que se encuentran registrados en la estructura {{eatc_licenses_prices .default_price }} para que correspondan a los guardados en el ERP. 

 Consulta del cdigo del producto en el erp 
 El sistema deber consultar los cdigos de ERP registrados en la estructura {{eatc_licenses_prices .erp_product_id }}   mediante la siguiente consulta  
 {{URL_entorno_datagov}}/api/eatcloud/ eatc_licenses_prices ?_id=_*&_distinct= erp_product_id 

 Con los datos obtenidos se proceder a realizar la siguiente consulta 

 Consulta de precio en ERP (consulta principal): {{precio}} 

 Documentacin Alegra: https://developer.alegra.com/docs/consultar-un-producto-o-servicio   

 Con el dato obtenido en {{eatc_licenses_prices .erp_product_id }} se procede a realizar la siguiente consulta 

 cURL 
 curl -v -H "Accept: application/json" -H "Content-type: application/json" -X GET https://api.alegra.com/api/v1/items/ {{eatc_licenses_prices .erp_product_id }} ?fields=price -u 'diana.alvarez@eatcloud: 6505f78dbfb7dfb38bfe ' 

 se toma el valor que llega en el parmetro 

 "price": [ { "price": " price.valor "} ] 

 Con el dato obtenido se procede a realizar la siguiente actualizacin: 

 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla= eatc_licenses_prices &_operacion=update& default_price={{ price.valor }} &WHERE erp_product_id= {{eatc_licenses_prices .erp_product_id }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ACTUALIZACIN DE PRECIOS EN EATC_LICENSES_PRICES