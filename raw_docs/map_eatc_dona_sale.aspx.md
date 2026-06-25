# map_eatc_dona_sale.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mapeo de los datos de eatc_sale a la estructura del anuncio de donacin ( eatc_dona )&#160; 

 #origen de datos 
 name = dona_sale 
 extension = json 
 ruta = &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale?_id=&#123;&#123;eatc_sale._id&#125;&#125; 
&#160; 
 #vector de encabezados 
 headers_vector = &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale?_campos 
 ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale?_campos &#160; 
 ambiente de poduccin&#58; https&#58;//donantes.eatcloud.info/api/eatcloud/eatc_sale?_campos &#160;&#160; 
&#160; 
&#160; 
 headers_action = insert //insert&#58; se debe insertar el vector de encabezados al archivo que se carga (porque no lo tiene); validate&#58; se debe validar que el vector de encabezados siempre sea uniforme 
&#160; 
&#160; 
 #eatc_dona&#58; detalle de anuncio de donacin&#58; coleccin de productos a ser donados 
&#160; 
 #transformaciones 
 eatc-dona_header_code = eatc_sale. eatc-dona_header_code //Cdigo de la cabecera del anuncio de donacin 
 eatc-date_time = eatc_sale. eatc-date_time //Fecha y hora del anuncio de donacin 
 eatc-date_time_2 = eatc_sale. eatc-date_time_2 //Fecha del anuncio de donacin 
 eatc-pod_id = eatc_sale. eatc-pod_id //Identificador nico del punto de donacin&#160; 
 eatc-odd_id = eatc_sale. eatc-odd_id //Identificador nico del producto o artculo donado 
&#160; 
 ***OJO&#58; LOS NICOS PARMETROS QUE NO SE TRANSFORMAN CON EL DE SU MISMO NOMBRE*** 
 eatc-odd_code = eatc_sale. eatc-odd_id //Se toma eatc-odd_id 
 eatc-odd_original_quantity = eatc_sale. eatc_odd_sale_transformed_quantity //Cantidad del producto transformado 
 eatc-odd_quantity = eatc_sale. eatc_odd_sale_transformed_quantity //Cantidad del producto transformado 
 eatc-unit_cost = etc-total_cost / eatc-quantity //Costo unitario del artculo o producto donado&#58; se divide el eatc-total_cost sobre eatc-quantity&#160; 
&#160; 
 *** 
 eatc_VAT_percentage = eatc_sale. eatc_VAT_percentage //Porcentaje del impuesto al valor agregado aplicable al producto 
 eatc-odd_name = eatc_sale. eatc-odd_name // Nombre del artculo&#160; 
 eatc_donor_code = eatc_sale. eatc_donor_code //Identificador o cdigo del donante &#160; =&gt; SIGUE IGUAL 
 eatc_donor = eatc_sale. eatc_donor //Nombre del donante &#160; =&gt; SIGUE IGUAL 
 eatc_cua_origin = eatc_sale. eatc_cua_origin //Cuenta desde la cual se genera el anuncio de donacin 
 eatc-odd_unit_weight_kg = eatc_sale. eatc-odd_unit_weight_kg //Peso unitario del artculo en kilogramos 
 eatc-contains_alergens = eatc_sale. eatc-contains_alergens // Definicin si la donacin contiene alrgenos 
 eatc-closer_expiration_date = eatc_sale. eatc-closer_expiration_date //(tipo date) fecha ms prxima de expiracin del producto (o los productos) anunciado(s) 
&#160; 
 #clasificaciones (por el momento se dejan vacas) 
 origin_odds_typology_a =&#160; //Primera tipologa origen del artculo o producto donado 
 origin_odds_typology_b =&#160; //Segunda tipologa origen del artculo o producto donado 
 origin_odds_typology_c = &#160; //Tercera tipologa origen del artculo o producto donado 
 eatc-odd_typology_a = //Primera tipologa del artculo o producto donado 
 eatc-odd_typology_b = //Segunda tipologa del artculo o producto donado 
 eatc-odd_typology_c = //Tercera tipologa del artculo o producto donado 
 eatc-provider_id = // Cdigo del proveedor del artculo 
 eatc-odd_code_type = // para el caso particular (EXITO) siempre ser &quot;ean&quot; &#160; =&gt; SIGUE IGUAL 
&#160; 
 #funciones 
 eatc-odd_total_cost = eatc-odd_original_quantity*eatc-odd_unit_cost //Costo unitario del artculo 
 eatc-original_VAT = eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor original total del impuesto a las ventas (eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage) 
 eatc-total_VAT = eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor definitivo total del impuesto a las ventas&#160; (eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage), despus del proceso de verificacin&#160; 
 eatc-odd_total_weight_kg = eatc-odd_unit_weight_kg*eatc-odd_quantity //Peso total de la donacin 
&#160; 
 *** 
&#160; 
 eatc-odd_total_height_cm &#160; = // No aplica por no tener datos &#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_width_cm &#160; = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_length_cm &#160; = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_volume_cm3 = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
&#160; 
 #EatCloud 
 eatc-odd_state = //Estado producto&#58; certificable, rechazado. Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin. Se deja vaco 
 eatc-odd_rejection_cause = //Causal del rechazo de un producto donado.&#160; Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin. Se deja vaco 
&#160; 
 Todos los dems parmetros que no aparezcan en este mapeo, se dejan vacos. 

 QUERYS 

 ****REVISAR A PARTIR DE LA ANTERIOR DEFINICIN*** 
&#160; 
 insert into donanteseatcloud_abaco.eatc_dona 
 ( 
 donanteseatcloud_abaco.eatc_dona.`eatc-dona_header_code`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-date_time`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-pod_id`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_id`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_quantity`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_cost`, 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_name`,&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_code`, 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_code_type`, 
 donanteseatcloud_abaco.eatc_dona.eatc_donor_code, 
 donanteseatcloud_abaco.eatc_dona.eatc_donor, 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_typology_a`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_typology_b`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_typology_c`, 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`origin_odds_typology_a`, 
 donanteseatcloud_abaco.eatc_dona.`origin_odds_typology_b`, 
 donanteseatcloud_abaco.eatc_dona.`origin_odds_typology_c`, 
&#160; 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-unit_cost`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_weight_kg`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_height_cm`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_width_cm`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_length_cm`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_total_volume_cm3`, 
&#160; 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_rejection_cause`, 
 donanteseatcloud_abaco.eatc_dona.`eatc-odd_state`, 
 donanteseatcloud_abaco.eatc_dona.origen 
&#160; 
 ) 
 select&#160; 
 dona.numdoc, 
 dona.fechahora, 
 dona.dependencia, 
 dona.plu, 
 dona.cantidad, 
 dona.costo, 
 odds.`eatc-name`,&#160; 
 odds.`eatc-code`,&#160; 
 'ean', 
 '890.900.608-9',&#160; 
 'exito', 
 '', 
 '', 
 '', 
 odds.origin_odds_typology_a, 
 odds.origin_odds_typology_b, 
 odds.origin_odds_typology_c, 
 if(dona.cantidad = 0, 0, round(dona.costo / dona.cantidad,2)) as unit_cost, 
&#160; 
 (select if(count(kg.valor_kg)=1,kg.valor_kg*dona.cantidad,&#160; 
 &#160;&#160;&#160;&#160;&#160;if(lower(odds.presentacion)='kg',round((odds.medida/1000 * dona.cantidad),2), 
 &#160;&#160;&#160;&#160;if(lower(odds.presentacion)='g',round((odds.medida/1000000 * dona.cantidad),2),0)) 
 &#160;&#160;&#160;)from donanteseatcloud_devexito.eatc_odds_kg kg where kg.plu=dona.plu), 
 0, 
 0, 
 0, 
 0, 
 '', 
 'certificable', 
 'donanteseatcloud_devexito.eatc_dona' 
 from donanteseatcloud_devexito.eatc_odds odds 
 inner join donanteseatcloud_devexito.eatc_dona dona 
 on dona.plu =&#160; odds.`eatc-id` 
&#160; 
 ////////////////////////////////////////////////////////////////////////////////// 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MAP_EATC_DONA_SALE