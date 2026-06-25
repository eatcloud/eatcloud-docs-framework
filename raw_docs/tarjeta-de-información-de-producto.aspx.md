# tarjeta-de-información-de-producto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Tarjeta de producto en formato vertical&#58; 
&#160; 
 Diseo&#58; https&#58;//zeroheight.com/6217d62d5/p/30e9f2-cardsec/t/25efda &#160; 
&#160; 
 A partir de los datos que trae&#160; &quot; consulta de ofertas cercanas &quot; se muestra la informacin bsica del producto de la siguiente manera&#58; 
&#160; 

 Tumbnail &#58; corresponde a la informacin que se recibe en el parmetro eatc-odd_image 
&#160; 

 -X% (porcentaje de descuento) &#58; crculo en la parte superior derecha del tumbnail, que muestra&#160; la informacin que se recibe en el parmetro eatc-odd_max_discount 
&#160; 

 Nombre plato (producto)&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_name 
&#160; 

 A X KM &#58; Corresponde al dato km &#160; 
&#160; 

 Precio antes de la oferta&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_unit_price. Se debe colocar ms pequeo y tachado ates del precio de la oferta 
&#160; 
 Precio en oferta&#58; corresponde a la informacin que se&#160; recibe en el parmetro eatc-odd_min_sale_unit_price 

 Tarjeta de producto en formato horizontal&#58; 
 Diseo&#58; https&#58;//zeroheight.com/6217d62d5/p/30e9f2-cardsec/t/18db0a &#160; 
&#160; 
 Muestra informacin la misma informacin que la tarjeta en formato vertical arriba descrita pero en una disposicin diferente&#58; 

 Al hacerle click a la&#160; anterior tarjeta 
 Como primera medida, el sistema deber consultar los datos de orden abierta , los cuales servirn para popular con informacin de unidades previamente ordenadas el botn de agregar al carrito de compras . 
&#160; 
 Luego el sistema debe consultar los datos completos de la oferta para el producto seleccionado de la siguiente manera&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale? eatc-code=&#123;&#123;eatc-code&#125;&#125;&#160; 
 Al anterior dato se le debe adicionar la informacin de km obtenida de la &quot; consulta de ofertas cercanas &quot;&#160; 
&#160; 
 Ejemplo 
&#160; 
 en ambiente de pruebas se seleccion un registro cuyo &quot; eatc-code&quot; es &quot;65&quot;, por lo tanto la consulta respectiva ser&#58; 
 https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale? eatc-code=64 &#160; 
&#160; 
 Y con esa informacin redirigirse a la vista de &quot; detalle de producto &quot;. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftarjeta-de-informaci%C3%B3n-de-producto%2F2787775100-EmbeddedImage--92-.jpg&ow=422&oh=612, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Ftarjeta-de-informaci%C3%B3n-de-producto%2F2787775100-EmbeddedImage--92-.jpg&ow=422&oh=612 
 App usuario final - Sale 

 793.000000000000 

 TARJETA (CARD) DE INFORMACIN DE PRODUCTO