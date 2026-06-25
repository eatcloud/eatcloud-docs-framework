# menú-inferior-de-navegación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La App dispondr de un men inferior de navegacin conformado por los siguientes botones que se detallan a continuacin 

 Inicio 
 Direcciona a la funcionalidad de Dashboard Sale 

 Promociones 
 Lleva a una vista tipo &quot; listado de productos &quot; con los productos que tienen un dato vlido (diferente de &quot;cero&quot; o &quot;vaco&quot;) el parmetro eatc_sale. eatc-odd_max_discount &#160; .&#160; En la lista resultante los anuncios se debern ordenar mostrando primero los que tienen un mayor descuento ( eatc_sale. eatc-odd_max_discount) y luego los que van descendiendo en esta cifra. 

 Tus pedidos 
 Este botn debe mostrar una burbuja mostrando el nmero de ordenes de oferta ( eatc_sale_order_headers ) cuyo eatc-state es &quot; paid_out &quot;, para el usuario en cuestin. &#160; Para obtener dicho nmero, se debe tomar el parmetro &quot;cont&quot; de la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers?eatc-user_code=&#123;&#123;eatc_sale_users. eatc-code &#125;&#125;&amp;eatc-state=paid_out&amp;_compress 

&#160; 
 Ejemplo entorno de pruebas 
&#160; 
 Para el usuario cuyo eatc_sale_users. eatc-code es 7777, la consulta sera la siguiente&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order_headers?eatc-user_code=7777&amp;eatc-state=paid_out&amp;_compress &#160; 
&#160; 
&#160; 
 Como la consulta trae la siguiente respuesta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;200924144050&quot;, 
 op &#58; true, 
 cont &#58; 2, 
 res &#58; &quot;........ 
 _compress &#58; true, 
 mem &#58; 0.43, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Entonces en el globo debera ponerse el nmero 2 
&#160; 
 Al presionar el botn, se debe ingresar a la funcionalidad &quot; Tus pedidos &quot;. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmen%C3%BA-inferior-de-navegaci%C3%B3n%2F4256635072-EmbeddedImage--94-.jpg&ow=1280&oh=250, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmen%C3%BA-inferior-de-navegaci%C3%B3n%2F4256635072-EmbeddedImage--94-.jpg&ow=1280&oh=250 
 App usuario final - Sale 

 796.000000000000 

 MEN INFERIOR DE NAVEGACIN (PENDIENTE DE DOCUMENTACIN)