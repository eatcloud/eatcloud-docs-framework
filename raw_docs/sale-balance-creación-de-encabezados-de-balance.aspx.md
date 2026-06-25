# sale-balance-creación-de-encabezados-de-balance.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Una vez se realiza el proceso de enriquecimiento de datos de oferta de ltimo minuto para su liquidacin (balance), el sistema debe consolidar en un encabezado los valores econmicos que se deben liquidar, con el nimo de obtener informacin que ser bsica para la realizacin de pagos a proveedores y la facturacin de EatCloud 
&#160; 
 Dicho encabezado se crear en la cuenta de el entorno donantes, eatcloud 
&#160; 
 https&#58;//datagov.eatcloud.inf/crd/eatcloud/?_tabla= eatc_sale_balance_headers &amp;_operacion=insert&amp; &#123;&#123;Parmetros creacin eatc_sale_balance_headers &#125;&#125; 
&#160; 
 _crear_sale_balance_headers.php 

 &#123;&#123;PARMETROS CREACIN EATC_SALE_BALANCE_HEADERS&#125;&#125; 

 Parmetros para la creacin del registro 
 Los siguientes parmetros los debe recibir el servicio de creacin del encabezado de la orden para poder operar, y a partir de ellos realizar los registros de informacin correspondientes. 

 eatc_code &#160; 
&#160; 
 Cdigo de la cabecera del encabezado del balance que corresponde al parmetro que se utiliza para invocar el proceso y con l se identifican los registros de detalle que se liquidan, por lo tanto el valor debe corresponder a 
 eatc_sale_balance_headers. eatc_code =eatc_sale. eatc-sale_balance_header_code 

 Identificador nico de transaccin 

 eatc_id &#160; 
 identificador nico del registro en la base de datos. puede ser similar al tradicional _id 

 Constantes 

 eatc_state &#160; 
 Se utilizarn dos estados, uno para indicar que el encabezado ha sido liquidado ( balance )&#160; y por esto, este ser el estado con el cual se crea y otro que indicar cuando la liquidacin ha sido pagada ( paid_out) 
 eatc_sale_balance_headers. eatc_state = balance //El estado al crearse el encabezado debe ser &quot;balance&quot;&#160; 

 Time stamps 

 eatc_date &#160; 
 Fecha de creacin de del presente encabezado&#160; (en formato AAAA-MM-DD) 

 eatc_datetime 
 Fecha y hora de creacin del presente encabezado(en formato AAAA-MM-DD HH&#58;MM&#58;SS) 

 Transformaciones internas 

 eatc_donor_code &#160; 
 Identificador nico del vendedor, que se obtiene de la informacin del detalle de la oferta (debe ser nico.&#160; Al recorrer todos los detalles de la oferta, si se hace un distinct sobre el parmetro abajo descrito, solo debe aparecer un valor, segn lo que se determina en el proceso de generacin de la liquidacin o balance )&#58; 
 eatc_sale_balance_headers. eatc_donor_code= eatc_sale. eatc_donor_code 

 eatc_donor &#160; 
 Nombre del vendedor, que se obtiene de la informacin del detalle de oferta (debe ser nico.&#160; Al recorrer todos los detalles de la oferta, si se hace un distinct sobre el parmetro abajo descrito, solo debe aparecer un valor, segn lo que se determina en el proceso de generacin de la liquidacin o balance ) 
 eatc_sale_balance_headers. eatc_donor= eatc_sale. eatc_donor 

 eatc_country &#160; 
 Pas desde el cual se crea la oferta, y que se toma del detalle de la oferta (debe ser nico.&#160; Al recorrer todos los detalles de la oferta, si se hace un distinct sobre el parmetro abajo descrito, solo debe aparecer un valor, segn lo que se determina en el proceso de generacin de la liquidacin o balance ) 
 eatc_sale_balance_headers. eatc_cua_origin= eatc_sale. eatc-pod_country 

 eatc_cua_origin &#160; 
 Cuenta desde la cual se crea la oferta, y que se toma del detalle de la oferta (debe ser nico.&#160; Al recorrer todos los detalles de la oferta, si se hace un distinct sobre el parmetro abajo descrito, solo debe aparecer un valor, segn lo que se determina en el proceso de generacin de la liquidacin o balance ) 
 eatc_sale_balance_headers. eatc_cua_origin= eatc_sale. eatc-cua_origin 

 eatc_enviroment_origin &#160; 
 Ambiente desde el cual se crea la liquidacin o balance de cuentas&#58; devdonantes o donantes 
 eatc_sale_balance_headers. eatc_enviroment_origin= devdonantes/donantes (se toma de la base de datos dnde reside la tabla eatc_sale.&#160; Se sugieren estos registros devdonantes/donantes, pero si existen otros que sean ms fciles de obtener el desarrollador los debe sugerir) 

 eatc_pod_names &#160; 
 Array del (de los) nombre(s) del punto(s) de venta (punto(s) de entrega),&#160; desde los cuales se realizaron las ofertas que se saldarn&#58; 
 eatc_sale_balance_headers. eatc_pod_names= array(eatc_sale. eatc-pod_name ) 

 eatc_sale_codes 
 Array de cdigos de las ofertas que se van a saldar. 
 eatc_sale_balance_headers. eatc_sale_codes= array(eatc_sale_order. eatc-code ) 

 Querys 

 eatc_vertical &#160; 
 Este dato corresponde al valor del parmetro vertical , de la cuenta respectiva ( eatc_cua_origin ) 
 eatc_sale_balance_headers. eatc_vertical= eatc_cua. vertical &#160; 
 (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc_cua_origin &#125;&#125;) 

&#160; 
 Ejemplo&#58; cuenta &quot;starbucks&quot; 
 Para un anuncio cuyo eatc_cua_origin es &quot; starbucks &quot; este parmetro debe guardar &quot; horeca &quot; dado que en la consulta respectiva ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= starbucks ) este es el dato guardado en el parmetro de la cuenta (CUA) vertical 

 eatc_cua_size&#160; 
 Este dato corresponde al valor del parmetro eatc_cua_size , de la cuenta respectiva ( eatc_cua_origin ) 
 eatc_sale_balance_headers. eatc_cua_size= eatc_cua. eatc_cua_size (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc_cua_origin &#125;&#125;) 
&#160; 
&#160; 
 Ejemplo&#58; cuenta &quot;starbucks&quot; 
 Para un anuncio cuyo eatc_cua_origin es &quot; starbucks &quot; este parmetro debe guardar &quot; big_restaurant &quot; dado que en la consulta respectiva ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= starbucks ) este es el dato guardado en el parmetro de la cuenta (CUA) eatc_cua_size 

 Funciones 

 eatc_base_settlement_value &#160; ***REVISAR CUANDO SE GENERE EJEMPLO DE LIQUIDACIN*** 
Es decir, cuando se implemente el proceso de enriquecimiento de eatc_sale para el balance 
&#160; 
 Valor base de liquidacin, es decir la sumatoria de &quot; eatc_sale. eatc_base_settlement_value &quot;&#160; de las ofertas a saldar o liquidar. 
&#160; 
 eatc_sale_balance_headers. eatc_ base_settlement_value = suma ( eatc_sale. eatc_base_settlement_value ) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &#123;&#123; eatc-sale_balance_header_code &#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas) ***PENDIENTE REVISIN*** 
&#160; 
 Para la(s) oferta(s) cuyo &quot; eatc-sale_balance_header_code &quot; es &quot;_____&quot;, el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &quot;_____&quot; 
&#160; 
 &#160;y por lo tanto &quot; eatc_base_settlement_value &quot; es&#58; &quot; _____ &quot;( eatc_sale. eatc_base_settlement_value ) 

 eatc_commission_value &#160; ***REVISAR CUANDO SE GENERE EJEMPLO DE LIQUIDACIN*** 
Es decir, cuando se implemente el proceso de enriquecimiento de eatc_sale para el balance 
&#160; 
 Es el valor&#160; total de las comisiones a cobrar, es decir la sumatoria de &quot; eatc_sale. eatc_commission_value &quot;&#160; de las ofertas a saldar o liquidar. 
 eatc_sale_balance_headers. eatc_ commission_value = suma( eatc_sale. eatc_commission_value ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &#123;&#123; eatc-sale_balance_header_code &#125;&#125; 
&#160; 
 Ejemplo (entorno de pruebas) ***PENDIENTE REVISIN*** 
&#160; 
 Para la(s) oferta(s) cuyo &quot; eatc-sale_balance_header_code &quot; es &quot;_____&quot;, el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &quot;_____&quot; 
&#160; 
 &#160;y por lo tanto &quot; eatc_commission_value &quot; es&#58; &quot; ______ &quot;( eatc_sale. eeatc_commission_value ) 

 eatc_total_vat &#160; ***REVISAR CUANDO SE GENERE EJEMPLO DE LIQUIDACIN*** 
Es decir, cuando se implemente el proceso de enriquecimiento de eatc_sale para el balance 
&#160; 
 Valor definitivo del impuesto a las ventas aplicable a la comisin cobrada, es decir la sumatoria de &quot; eatc_sale. eatc_vat_value &quot;&#160; de las ofertas a saldar o liquidar. 
 eatc_sale_balance_headers. eatc_total_vat = suma ( eatc_sale. eatc_vat_value) 

&#160; 
 Ejemplo (entorno de pruebas) ***PENDIENTE REVISIN*** 
&#160; 
 Para la(s) oferta(s) cuyo &quot; eatc-sale_balance_header_code &quot; es &quot;_____&quot;, el sistema realiza la siguiente consulta&#58; 
&#160; 
 _________________________________ 
&#160; 
 &#160;y por lo tanto &quot; eatc-total_vat &quot; es&#58; ____________________- 

 eatc_total_other_taxes &#160; ***REVISAR CUANDO SE GENERE EJEMPLO DE LIQUIDACIN*** 
Es decir, cuando se implemente el proceso de enriquecimiento de eatc_sale para el balance 
&#160; 
 Valor definitivo de otros impuestos aplicables a la comisin cobrada, es decir la sumatoria de &quot; eatc_sale. eatc_other_taxes_value &quot;&#160; de las ofertas a saldar o liquidar. 
 eatc_sale_balance_headers. eatc_total_other_taxes = suma ( eatc_sale. eatc_other_taxes_value) 

&#160; 
 Ejemplo (entorno de pruebas) ***PENDIENTE REVISIN*** 
&#160; 
 Para la(s) oferta(s) cuyo &quot; eatc-sale_balance_header_code &quot; es &quot;_____&quot;, el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &quot;_____&quot; 
&#160; 
&#160; 
 &#160;y por lo tanto &quot; eatc_total_other_taxes &quot; es&#58; ___________________________ 

 eatc_amount_to_be_paid &#160; ***REVISAR CUANDO SE GENERE EJEMPLO DE LIQUIDACIN*** 
Es decir, cuando se implemente el proceso de enriquecimiento de eatc_sale para el balance 
&#160; 
 Corresponde al valor que hay que pagar al cliente, una vez se descuentan las comisiones y los impuestos 
 eatc_sale_balance_headers. eatc_ amount_to_be_paid = suma( eatc_sale. eatc_amount_to_be_paid ) 
&#160; 
 &#123;&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &#123;&#123; eatc-sale_balance_header_code &#125;&#125; 
&#160; 
&#160; 
 Ejemplo (entorno de pruebas) ***PENDIENTE REVISIN*** 
&#160; 
 Para la(s) oferta(s) cuyo &quot; eatc-sale_balance_header_code &quot; es &quot;_____&quot;, el sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/ eatcloud /eatc_sale? eatc-sale_balance_header_code = &quot;_____&quot; 
&#160; 
 &#160;y por lo tanto &quot; eatc_amount_to_be_paid &quot; es&#58; __________________________________ 

 EatCloud 
 Corresponde a informacin que se agrega a partir de la interaccin con la plataforma.&#160; Por este motivo, cuando se crea un encabezado de orden, estos datos no se envan en la creacin, para que queden vacos y sean complementados luego por procesos de las plataformas. 

 eatc_sale_balance_headers. eatc_paiment_datetime = //Fecha y hora en la cual se efecta el pago de la compensacin al cliente 
&#160; 
 eatc_sale_balance_headers. eatc_paiment_date = //Fecha en la cual se efecta el pago de la compensacin al cliente 
&#160; 
 eatc_sale_balance_headers. eatc_paiment_doc = //Documento soporte de pago o transferencia 
&#160; 
 eatc_sale_balance_headers. eatc_invoice = //Factura EatCloud con a cual se legaliza el pago 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE ENCABEZADOS DE BALANCE (EATC_SALE_BALANCE_HEADERS)