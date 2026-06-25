# verificación-de-la-compra-sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta funcionalidad se le INFORMAR (solamente) al usuario una serie de opciones definidas por baco como&#160; alimentos que pueden ser donados en la Alimentatn. El usuario leer en pantalla la informacin y no registrar ninguna otra informacin adicional 

 Consulta de categoras&#58; 
 El sistema cosulta el API de eatc_odds_alimentaton (Objetos de donacin para la Alimentatn), para determinar que categoras estn disponibles 
&#160; 
 Ejemplo&#58; 
 para consultar el API se utiliza la siguiente sentencia 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria= _* 
&#160; 
 Las categoras que se muestran en los encabezados de los colapsibles corresponden a un &quot; select distinct &quot; del parmetro &quot; categoria &quot; que arroja la anterior consulta. 
&#160; 
 El usuario podr descolapsar las categoras disponibles a fin de ver los productos pueden ser donados. 

&#160; 
 Consulta de productos susceptibles de ser donados 
 Teniendo la &quot; categoria &quot; seleccionada, se utiliza el API para traer los productos que se listan en la vista. 
&#160; 
 Ejemplo&#58; 
 El usuario selecciona la categoras &quot; no perecederos &quot;, la consulta que se debe realizar para listar los productos es la siguiente&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria=no perecederos 
&#160; 
 Listado de productos&#58; 
 En el listado de productos se coloca la informacin correspondiente al parmetro &quot;alimentos&quot; que trae la anterior consulta. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fverificaci%C3%B3n-de-la-compra-sale%2F55013929-6-Dashboard-Donacion-Alimentos--eatc_alim_dona---2-.png&ow=750&oh=2322, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fverificaci%C3%B3n-de-la-compra-sale%2F55013929-6-Dashboard-Donacion-Alimentos--eatc_alim_dona---2-.png&ow=750&oh=2322 
 App usuario final - Sale 

 847.000000000000 

 SEGUIMIENTO DE LA COMPRA (EATC_SALE_SEG)