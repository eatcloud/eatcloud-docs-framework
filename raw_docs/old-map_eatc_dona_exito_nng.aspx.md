# old-map_eatc_dona_exito_nng.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Enriquecimiento del anuncio de donacin ( eatc_dona ) a partir de la informacin de mercanca negociada (mercanca que pertenece al xito) que se nos entrega en la respectiva estructura . 
&#160; 
 Solo se deben pasar a la tabla que agrupa los anuncios (donantes.eatcloud.info/api/abaco/eatc_dona) aquellos cuyo eatc-pod_id se encuentre en la tabla donantes.eatcloud.info/api/cua/eatc_pods. 

Archivo de trabajo&#58; DEP_map_eatc_dona_exito_nng.cfg 

 #nombre del archivo externo 
 name = Devoluciones 
 extension = txt //lo convert a .csv para analizarlo es es texto separado por tabulaciones 
 separadores = tabulaciones 
&#160; 
 #vector de encabezados 
 headers_vector = Dependencia Despacha Dependencia Despacha ID,Dependencia Despacha Dependencia Despacha DESC,Ciudad Dep.Despacha Ciudad SINCO,Ciudad Dep.Despacha Ciudad Dep.Despacha DESC,Dependencia Recibe Dependencia Recibe ID,Dependencia Recibe Dependencia Recibe DESC,Ciudad Dep.Recibe Ciudad SINCO,Ciudad Dep.Recibe Ciudad Dep.Recibe DESC,Direccion ID,Direccion DESC,Subdireccion ID,Subdireccion DESC,Sublinea ID,Sublinea DESC,Categoria ID sublinea,Categoria ID categoria,Categoria DESC,Subcategoria IDsubcategoria,Subcategoria DESC,Articulo Cdigo,Articulo DESC,Clase Marca Clase Marca DESC,Plu PluCD,Plu DESC,Ao ID,Mes DESC,Dia DiaID,Estado Plu x Dependencia Desc Estado x Dependencia,Proveedor Nit,Proveedor NombreProveedor,Metodo de compra ID,Metodo de compra DESC,Tipo Devolucion ID,Tipo Devolucion DESC,Causa de Devolucion Causa Devolucion ID,Causa de Devolucion Causa Devolucion DESC,Fecha Transporte Cedi ID,FechaRealRecibo ID,Fecha Entrega Proveedor ID,Codigo Destinacion ID,Codigo Destinacion DESC,Orden Proveedor ID,Numero Viaje ID,Orden Despacho/Devolucion ID,# Unidades Despachadas,$ CtoCantDespachada 
&#160; 
 headers_action = validate //insert&#58; se debe insertar el vector de encabezados al archivo que se carga (porque no lo tiene); validate&#58; se debe validar que el vector de encabezados siempre sea uniforme 
&#160; 
&#160; 
 #eatc_dona&#58; detalle de anuncio de donacin&#58; coleccin de productos a ser donados 
&#160; 
 #transformaciones 
 eatc-dona_header_code = Orden Despacho/Devolucion ID //Cdigo de la cabecera del anuncio de donacin 
 eatc-date_time = Dia DiaID //Fecha y hora del anuncio de donacin (en formato&#58; AAAAMMDDHHMMSS) 
 eatc-pod_id = Dependencia Despacha Dependencia Despacha ID //Identificador nico del punto de donacin 
 eatc-odd_id = Plu PluCD //Identificador nico del producto o artculo donado 
 eatc-odd_name = Plu DESC //Nombre o descripcin del producto a susceptible de donacin 
 eatc-odd_quantity = # Unidades Despachadas//Cantidad del producto o artculo donado 
 eatc-odd_total_cost = $ CtoCantDespachada//Costo total del o de los productos o artculos donados (eatc-quantity * eatc-unit_cost) 
&#160; 
 ***NUEVO*** 
 eatc_VAT_percentage = //Porcentaje del impuesto al valor agregado aplicable al producto 
&#160; 
 ***NUEVO*** 
 eatc-provider_id = // Cdigo del proveedor del artculo 
&#160; 
 eatc_donor_code = Proveedor Nit//Identificador o cdigo del donante 
 origin_odds_typology_a = Sublinea ID//Primera tipologa origen del artculo o producto donado 
 origin_odds_typology_b = Categoria ID categoria//Segunda tipologa origen del artculo o producto donado&#160; 
 origin_odds_typology_c = Subcategoria ID//Segunda tipologa origen del artculo o producto donado 
&#160; 
 #tipo de transformacin 
 m2z-map-type = cambio_nombre_campo //adicion_columnas,cambio_nombre_campo 
&#160; 
 #querys 
 eatc-odd_code = eatc_odds.eatc-code https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id//Cdigo internacional del artculo o producto susceptible a ser donado 
 eatc-odd_code_type = constant(EAN)//Tipo del cdigo internacional del artculo o producto susceptible a ser donado (ejemplo&#58; EAN8, EAN13, UPC...) 
 eatc_donor = eatc_cua.name https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;customer__eatc_clientes__partyidentification=eatc_donor_code //Con el eatc_donor_code, se realiza una consulta al WS de Cuentas (eatc_cua) y se coloca el &quot;name&quot; 
&#160; 
 #constantes 
 eatc-odd_code_type = constant (ean) // para el caso particular (EXITO) siempre ser &quot;ean&quot; 
&#160; 
 #Clasificaciones 
 eatc-odd_typology_a = //Primera tipologa del artculo o producto donado 
 eatc-odd_typology_b = //Segunda tipologa del artculo o producto donado 
 eatc-odd_typology_c = //Tercera tipologa del artculo o producto donado 
&#160; 
 #funciones 
 eatc-unit_cost = etc-total_cost / eatc-quantity //Costo unitario del artculo o producto donado, etc-total_cost sobre eatc-quantity 
&#160; 
 ***NUEVO*** 
 eatc-original_VAT = eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor original total del impuesto a las ventas (eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage) 
 eatc-total_VAT = eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor definitivo total del impuesto a las ventas&#160; (eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage), despus del proceso de verificacin 
&#160; 
&#160; 
 eatc-odd_unit_weight_kg = //if (&quot;presentacion&quot;=KG,(eatc_odds.numer(medida)/1000) https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id) else if (&quot;presentacion&quot;=G,(eatc_odds.numer(medida)/1000000) https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id), else eatc_odds_kg.valor_kg https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds_kg?plu=$numer(eatc-odd_id), else = 0 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;//si la presentacin es G (gramo) o KG (kilogramo), se puede calcular con los datos del maestro eatc_odds respectivo. Si no corresponden, se debe ir al maestro eatc_odds_kg y consultar por PLU (a este PLU se le deben quitar los ceros a la izquierda 
 eatc-odd_total_weight_kg = eatc-odd_unit_weight_kg*eatc-odd_quantity //if (&quot;presentacion&quot;=KG,(eatc_odds.numer(medida)/1000)*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id) else if (&quot;presentacion&quot;=G,(eatc_odds.numer(medida)/1000000)*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id), else eatc_odds_kg.valor_kg*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds_kg?plu=$numer(eatc-odd_id), else = 0 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;//si la presentacin es G (gramo) o KG (kilogramo), se puede calcular con los datos del maestro eatc_odds respectivo. Si no corresponden, se debe ir al maestro eatc_odds_kg y consultar por PLU (a este PLU se le deben quitar los ceros a la izquierda) 
&#160; 
 eatc-odd_total_height_cm = // No aplica por no tener datos 
 eatc-odd_total_width_cm = // No aplica por no tener datos 
 eatc-odd_total_length_cm = // No aplica por no tener datos 
 eatc-odd_total_volume_cm3 = // No aplica por no tener datos 
&#160; 
 #EatCloud 
 eatc-odd_state = //Estado producto&#58; certificable, rechazado. Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin 
 eatc-odd_rejection_cause = //Causal del rechazo de un producto donado.&#160; Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin 

 QUERYS 

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
 donang.orden_despachodevolucion_id, 
 donang.dia_diaid, 
 donang.dependencia_despacha_dependencia_despacha_id, 
 donang.plu_plucd, 
 donang.unidades_despachadas, 
 donang.ctocantdespachada, 
 donang.plu_desc, 
 donang.unidades_despachadas*(select if(count(odds.`eatc-code`)=1, odds.`eatc-code`, 0) from donanteseatcloud_devexito.eatc_odds odds where TRIM(LEADING '0' FROM odds.`eatc-id`) = TRIM(LEADING '0' FROM donang.plu_plucd) limit 1), 
 'ean', 
 donang.proveedor_nit,&#160; 
 pvd.name , 
 '', 
 '', 
 '', 
 donang.sublinea_id, 
 donang.categoria_id_categoria, 
 donang.subcategoria_idsubcategoria, 
 if(donang.ctocantdespachada = 0, 0, round(donang.ctocantdespachada / donang.unidades_despachadas,2)) as unit_cost, 
&#160; 
 (select if(count(kg.valor_kg)=1,kg.valor_kg,0)*donang.unidades_despachadas from donanteseatcloud_devexito.eatc_odds_kg kg where kg.plu=donang.plu_plucd), 
 0, 
 0, 
 0, 
 0, 
 '', 
 'certificable', 
 'donanteseatcloud_devexito.eatc_dona_nng' 
 from donanteseatcloud_devexito.eatc_nng_providers pvd 
 inner join donanteseatcloud_devexito.eatc_dona_nng donang 
 on pvd.code =&#160; donang.proveedor_nit 
 ; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MAP_EATC_DONA_EXITO_NNG