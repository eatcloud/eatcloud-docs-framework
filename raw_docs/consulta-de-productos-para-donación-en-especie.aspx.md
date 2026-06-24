# consulta-de-productos-para-donación-en-especie.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta funcionalidad se le INFORMAR (solamente) al usuario una serie de opciones definidas por baco como  alimentos que pueden ser donados en la Alimentatn. El usuario leer en pantalla la informacin y no registrar ninguna otra informacin adicional 

 Consulta de categoras: 
 El sistema coNsulta el API de eatc_odds_alimentaton (Objetos de donacin para la Alimentatn), para determinar que categoras estn disponibles 

 Ejemplo: 
 para consultar el API se utiliza la siguiente sentencia 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria= _* 

 Las categoras que se muestran en los encabezados de los colapsibles corresponden a un " select distinct " del parmetro " categoria " que arroja la anterior consulta. 

 El usuario podr descolapsar las categoras disponibles a fin de ver los productos pueden ser donados. 

 Consulta de productos susceptibles de ser donados 
 Teniendo la " categoria " seleccionada, se utiliza el API para traer los productos que se listan en la vista. 

 Ejemplo: 

 El usuario selecciona la categoras " no perecederos ", la consulta que se debe realizar para listar los productos es la siguiente: 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria=no perecederos 

 Listado de productos: 
 En el listado de productos se coloca la informacin correspondiente al parmetro "alimentos" que trae la anterior consulta. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-productos-para-donaci%C3%B3n-en-especie%2F1831581382-6-Dashboard-Donacion-Alimentos--eatc_alim_dona-.png&ow=750&oh=2322, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconsulta-de-productos-para-donaci%C3%B3n-en-especie%2F1831581382-6-Dashboard-Donacion-Alimentos--eatc_alim_dona-.png&ow=750&oh=2322 
 App usuario final - Alimentatn 

 755.000000000000 

 CONSULTA DE PRODUCTOS PARA LA DONACIN EN ESPECIE (EATC_ALIM_DONA)