# sale-balance-enriquecimiento-de-información-de-eatc_sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 A partir de los datos oferta de ltimo minuto, en el momento de realizar el balance o de saldar la cuenta para realizar el pago al oferente, el cual se realizar en una periodicidad definida por el maestro&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_balance_timeout?_id=_* y por cada NIT de Oferente ( eatc_sale. eatc_donor_code ), se realizan una serie de operaciones aritmticas para determinar los valores a pagar por cada detalle de oferta.&#160; Luego, a partir de esta informacin se realizar la liquidacin de los valores a pagar a los oferentes. 
&#160; 
 _enriquecer_sale_balance.php 

 En trminos generales se debern realizar los siguientes registros en la estructura&#58; 
 &#160;&#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/ eatc_sale ?_operacion= update&amp;&#123;&#123; parametros_enriquecidos &#125;&#125;&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 

 &#123;&#123;PARMETROS_ENRIQUECIDOS&#125;&#125; 

 eatc_sale_balance_quantity &#160; 
&#160; 
 Corresponde a la cantidad de productos ofertados que se saldarn, porque fueron vendidos , por lo tanto esta cantidad corresponder a la resta de las cantidades originales, de las cantidades actuales, las cantidades transformadas y las cantidades rechazadas 
&#160; 
 eatc_sale. eatc_sale_balance_quantity = eatc_sale. eatc-odd_original_quantity - eatc_sale. eatc-odd_quantity - eatc_sale. eatc_odd_sale_transformed_quantity - eatc_sale. eatc_odd_sale_rejected_quantity 
&#160; 
 ERROR HANDLERS 
 Si esta resta da un nmero negativo, entonces&#58; eatc_sale. eatc_sale_balance_quantity = 0 
 Si dicha resta da un nmero mayor a eatc_sale. eatc-odd_original_quantity entonces &#58;&#160; eatc_sale. eatc_sale_balance_quantity = eatc_sale. eatc-odd_original_quantity 

&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=7 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_sale_balance_quantity = 8 - 0 - 0 - 0 = 8 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=21 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_sale_balance_quantity = 10 - 12 - 0 - 0 = -2 entonces eatc_sale. eatc_sale_balance_quantity = 0 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=41 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_sale_balance_quantity = 50 - 49 - 0 - 0 = 1 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=55 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_sale_balance_quantity = 5 - 5 - 0 - 0 = 0 

 eatc_base_settlement_value &#160; 
&#160; 
 Corresponde al valor sobre el cual se liquida la comisin y por lo tanto surge de multiplicar las cantidades a saldar por el valor mximo 
 eatc_sale. eatc_base_settlement_value = eatc_sale. eatc_sale_balance_quantity * eatc_sale. eatc-odd_min_sale_unit_price 

&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=7 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_base_settlement_value = 8 * 6.00 = 48 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=21 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_base_settlement_value = 0 * 10.00 = 0 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=41 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_base_settlement_value = 1 * 30.00 = 30 
&#160; 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=55 , por lo tanto las cantidades a saldar sern&#58; 
&#160; 
 eatc_sale. eatc_base_settlement_value = 0 * 8 =0 

 eatc_commission_percentage 
&#160; 
 Corresponde al porcentaje de comisin aplicable a la oferta.&#160; Para obtener dicho valor el sistema deber realizar consultas ordenadas a la estructura. 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions?_id=_* 
 De la siguiente manera&#58;&#160; 

&#160; 
 1.&#160; Consulta de comisin por cuenta&#58; &#160; 
&#160; 
 Se le enva al parmetro eatc_cua el valor consignado en eatc_sale. eatc_cua_origin 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_cua=&#123;&#123; eatc_sale. eatc_cua_origin&#125;&#125; 
&#160; 
 Se toma el dato que trae el parmetro &quot; eatc_sale_commission_percentage &quot; para registrarlo en eatc_sale. eatc_commission_percentage . Si la consulta no arroja resultado pasa a la siguiente consulta&#58; 

&#160; 
 2.&#160; Consulta de comisin por tamao (NO SE IMPLEMENTA EN UNA PRIMERA INSTANCIA)&#58; 
&#160; 
 &#160;Se consulta el tamao de la cuenta, envindole los datos eatc_sale. eatc_cua_origin y eatc_sale. eatc-pod_country al&#160; maestro de cuentas de la siguiente manera para obtener el dato&#58;&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_country=&#123;&#123; eatc_sale. eatc-pod_country&#125;&#125;&amp;name=&#123;&#123; eatc_sale. eatc_cua_origin&#125;&#125; 
&#160; 
 Se toma el dato size , para realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_size=&#123;&#123; eatc_cua. size&#125;&#125; 
&#160; 
 Se toma el dato que trae el parmetro &quot; eatc_sale_commission_percentage &quot; para registrarlo en eatc_sale. eatc_commission_percentage . Si la consulta no arroja resultado pasa a la siguiente consulta 

&#160; 
 3.&#160; Consulta de comisin por vertical&#58; se consulta el tamao de la cuenta, envindole los datos eatc_sale. eatc_cua_origin y eatc_sale. eatc-pod_country al&#160; maestro de cuentas de la siguiente manera para obtener el dato&#58;&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_country=&#123;&#123; eatc_sale. eatc-pod_country&#125;&#125;&amp;name=&#123;&#123; eatc_sale. eatc_cua_origin&#125;&#125; 
&#160; 
 Se toma el dato vertical , para realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_vertical=&#123;&#123; eatc_cua. vertical&#125;&#125; 
&#160; 
 Se toma el dato que trae el parmetro &quot; eatc_sale_commission_percentage &quot; para registrarlo en eatc_sale. eatc_commission_percentage . Si la consulta no arroja resultado pasa a la siguiente consulta 

&#160; 
 4.&#160; Consulta de comisin cuenta maestra&#58; &#160; 
&#160; 
 Se consulta el la cuenta maestra ( eatc_cua_master ) de la cuenta, envindole los datos eatc_sale. eatc_cua_origin y eatc_sale. eatc-pod_country al&#160;maestro de cuentas de la siguiente manera para obtener el dato&#58;&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_country=&#123;&#123; eatc_sale. eatc-pod_country&#125;&#125;&amp;name=&#123;&#123; eatc_sale. eatc_cua_origin&#125;&#125; 
&#160; 
 Se toma el dato eatc_cua_master , para realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_cua_master=&#123;&#123; eatc_cua. eatc_cua_master&#125;&#125; 
&#160; 
 Se toma el dato que trae el parmetro &quot; eatc_sale_commission_percentage &quot; para registrarlo en eatc_sale. eatc_commission_percentage . Si la consulta no arroja resultado pasa a la siguiente consulta se coloca como valor por defecto 15% 
&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=70 , por lo tanto se realiza primero la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_cua= colombia &#160; 
&#160; 
 Como la consulta no trae resultados se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_country=co&amp;name=colombia &#160; 
&#160; 
 Obtenindose los datos&#58; 
&#160; 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 vertical &#58; &quot;horeca&quot;, 
&#160; 
 Se procede a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_vertical= horeca &#160;&#160; 
&#160; 
 Como la consulta no trae resultados se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_sale_commissions? eatc_cua_master=abaco &#160;&#160; 
&#160; 
 Por lo tanto&#58;&#160; 
&#160; 
 eatc_sale. eatc_commission_percentage = 15 

 eatc_commission_value &#160; 
&#160; 
 Consulta sobre temas impositivos&#58; 
 Cuando se establece el porcentaje a cobrar sobre el producto que se vende, este porcentaje ya tiene implcitos el IVA o no? RTA// por general el establecimiento del precio de venta de un producto se hace sobre el valor antes de iva, al momento de facturar se cobrar el productos ms un porcentaje del 19% de iva el cual se sumar y cobrar al cliente.&#160; El iva es un valor que las empresa cobran a los clientes y que luego deben pagar a la Dian.&#160; 
&#160; 
 Corresponde al valor de la comisin liquidado sobre la base de liquidacin, por lo tanto corresponde a la multiplicacin de la base de liquidacin por el porcentaje de comisin 
&#160; 
 eatc_sale. eatc_commission_value = eatc_sale. eatc_base_settlement_value * eatc_sale. eatc_commission_percentage/100 

&#160; 
 Ejemplo&#58; Ambiente de pruebas 
&#160; 
 Se salda el anuncio cuyo _id=65 , por lo tanto el valor de la comisin ser 
&#160; 
 eatc_sale. eatc_commission_value = ((9-7-0-0)*5)*15/100 = 10 * 15/100 = 1,5 

 eatc_vat_value 
&#160; 
 Corresponde al valor del IVA aplicable a la comisin 
&#160; 
 Para establecer el valor aplicable se debe realizar la siguiente consulta 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_taxes? eatc_country=&#123;&#123; eatc_sale. eatc-pod_country&#125;&#125;&amp; eatc_product =sale_commission&amp; tax_type =vat 
&#160; 
 Al obtener el valor del impuesto, se realiza la siguiente operacin para obtener el valor 
 eatc_taxes. percentaje 
&#160; 
 Con el valor obtenido se realiza la siguiente operacin 
 eatc_sale. eatc_vat_value = ( eatc_taxes. percentaje * eatc_sale. eatc_commission_value)/100 

&#160; 
 Ejemplo&#58; Ambiente de pruebas&#160; 
&#160; 
 Se salda el anuncio cuyo _id=65 , por lo tanto el sistema realiza la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_taxes? eatc_country=co&amp; eatc_product =sale_commission&amp; tax_type =vat 
&#160; 
 Como eatc_taxes. percentaje=19 
&#160; 
 Entonces&#58; 
&#160; 
 eatc_sale. eatc_vat_value = ( 19 * 1,5 )/100 = 0,285 

 eatc_other_taxes_value 
&#160; 
 Corresponde al valor del otros impuestos aplicables a la comisin 
&#160; 
 Para establecer el valor aplicable se debe realizar la siguiente consulta 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_taxes? eatc_country=&#123;&#123; eatc_sale. eatc-pod_country&#125;&#125;&amp; eatc_product =sale_commission&amp; tax_type =other 
&#160; 
 Al obtener el valor del impuesto, se realiza la siguiente operacin para obtener el valor 
 eatc_taxes. percentaje 
&#160; 
 Con el valor obtenido se realiza la siguiente operacin 
 eatc_sale. eatc_other_taxes_value = ( eatc_taxes. percentaje * eatc_sale. eatc_commission_value)/100 

&#160; 
 Ejemplo&#58; Ambiente de pruebas&#160; 
&#160; 
 Se salda el anuncio cuyo _id=65 , por lo tanto el sistema realiza la siguiente consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_taxes? eatc_country=co&amp; eatc_product =sale_commission&amp; tax_type =other 
&#160; 
 Como no el sistema no trae ningn valor, se toma como si el mismo fuera cero por lo tanto&#160; 
&#160; 
 Entonces&#58; 
&#160; 
 eatc_sale. eatc_other_taxes_value = ( 0 * 1,5 )/100 = 0 

 eatc_amount_to_be_paid 
&#160; 
 Corresponde a la diferencia entre la base de liquidacin de la comisin y la comisin pagada 
 eatc_sale. eatc_amount_to_be_paid = eatc_sale. eatc_base_settlement_value - eatc_sale. eatc_commission_value - eatc_sale. eatc_vat_value - eatc_sale. eatc_other_taxes_value 

&#160; 
 Ejemplo&#58; Ambiente de pruebas ***PENDIENTE DE REVISAR*** 
&#160; 
 Se salda el anuncio cuyo _id=65 , por lo tanto el valor de la comisin ser 
&#160; 
 eatc_sale. eatc_amount_to_be_paid =&#160; 10 - 1,5 - 0,285 - 0 = 8,215 

 eatc-sale_balance_header_code &#160; 
&#160; 
 Corresponde a un identificador de todos los registros &quot;saldados&quot; o a los cuales se le realiz el &quot;balance&quot;, para una cuenta en particular en una fecha y hora en particular.&#160; Por lo tanto puede ser la concatenacin del nombre de la cuenta ( eatc_sale. eatc_cua_origin ) un estampe de tiempo (con milisegundos) de cuando comienza el proceso de &quot;balance&quot; 
&#160; 
 eatc_sale. eatc-sale_balance_header_code = &#123;&#123; eatc_sale. eatc_cua_origin&#125;&#125;&#123;&#123; timestamp &#125;&#125; 

 eatc-odd_state &#160; 
&#160; 
 Cuando se realiza el proceso para saldar cuentas (y que genera los registros anteriores), el estado de los artculos pasa a&#160; &quot;balance&quot; 
 eatc_sale. eatc-odd_state = balance 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ENRIQUECIMIENTO DE INFORMACIN DE EATC_SALE PARA PROCESO DE BALANCE