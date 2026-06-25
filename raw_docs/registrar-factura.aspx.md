# registrar-factura.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema debe proporcionar un campo de captura con las siguientes caractersticas 
 Informacin tcnica del parmetro&#58; eatc_sale_order_header. eatc-doc 
 Descripcin ( tooltip ) &#58; Ingrese por favor el nmero de factura o documento equivalente de los productos en oferta que va a entregar 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 

 Valor por defecto &#58; si existe registro para el anuncio respectivo en el campo eatc_sale_order_header. eatc-doc se debe mostrar dicho registro 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers?eatc-code=&#123;&#123;eatc_sale_order_headers.eatc-code&#125;&#125; 
&#160; 
 se coloca como valor por defecto lo que se obtiene en el parmetro eatc-doc 
&#160; 
 Si no encuentra registros en eatc-doc, se deja vaco. 
&#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; este dato ser obligatorio para realizar la entrega de la orden, por eso, si alguien entra y sale de la funcionalidad sin colocar datos debe mostrrsele un mensaje&#58; 
&#160; 
 Recuerda que la factura o documento equivalente es necesario para entregar el pedido de oferta. 
&#160; 
 Deseas ingresar una factura o documento equivalente? 
&#160; 
 Si &#160; No 
&#160; 
 Opcin Si&#58; lo deja en la funcionalidad, especficamente en el input de los datos. 
 Opcin No&#58; lo devuelve al dashboard de orden de oferta . 
&#160; 
 Se guarda en &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_order_headers?eatc-doc=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_headers&amp;_operacin=update&amp;eatc-doc=&#123;&#123;input&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_sale_order_header.eatc-code&#125;&#125; 

 Estampe de horas a partir del registro de la factura 
 Cuando se registra una factura se debe dar por entregada la orden, por lo tanto se deber tomar la fecha y hora actual y hacer un registro de la misma en los siguientes campos de eatc_sale_order_headers 
&#160; 
 eatc-picking_checkin_datetime &#58; se estampa la fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS si no el campo no existe registro de una fecha y hora vlida (esto dado que en la funcionalidad&#58; de la PWA de listado de pedidos pendientes , se podr estampar esta fecha y hora) 
 Mtodo para guardar especfico &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_headers&amp;_operacin=update&amp; e atc-picking_checkin_datetime =&#123;&#123;timestamp&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_sale_order_header.eatc-code&#125;&#125; 
 eatc-picking_checkout_datetime &#58; se estampa la fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 Mtodo para guardar especfico &#58;&#160; 
&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order_headers&amp;_operacin=update&amp; e atc-picking_checkout_datetime =&#123;&#123;timestamp&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_sale_order_header.eatc-code&#125;&#125; 

 Estampe de horas a partir del registro de la factura 
 Cuando se registra una factura se debe dar por entregada la orden, por lo tanto se deber cambiar el estado del eatc_sale_order_headers.eatc-state a delivered 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 REGISTRAR FACTURA