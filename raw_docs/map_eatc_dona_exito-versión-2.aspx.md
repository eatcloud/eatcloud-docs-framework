# map_eatc_dona_exito-versión-2.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Enriquecimiento del anuncio de donacin ( eatc_dona ) a partir de la informacin de mercanca negociada (mercanca que pertenece al xito) que se entrega a partir del da 3 de febrero de 2020 y que incorpora optimizaciones para no recibir toda la informacin de los movimientos de inventarios, solamente la informacin&#160; de averas. 
&#160; 
 Solo se deben pasar a la tabla que agrupa los anuncios (donantes.eatcloud.info/api/abaco/eatc_dona) aquellos cuyo eatc-pod_id se encuentre en la tabla donantes.eatcloud.info/api/cua/eatc_pods. 

 Archivo de trabajo&#58;&#160; DEP_map_eatc_dona_exito.cfg 

 #nombre del archivo externo 
 #nombre del archivo externo 
 name = MOVINV_IEMOI_EATCLOUD_aaaammdd 
 extension = txt (revisar) 
 separador = pipe (revisar) 
 ruta = Z&#58;\Produccion\BancoDonaciones\DONMOVISINE 
&#160; 
 #vector de encabezados ***Nuevo&#58; peso unitario en gramos *** 
 NOTA SOBRE NUEVO CAMPO&#58; Se adiciona al final un campo de 10 dgitos, con ceros a la izquierda, con el peso en gramos.&#160; Para obtener el peso en KG hay que quitar los ceros a la izquierda y dividir por mil. 
&#160; 
 headers_vector =&#160; 
&#160; 
 Accion,Dependencia,Numdoc,CodMov3,FechaDocumento,Plu,Cantidad,Signo,TipoMarca,FechaHora,FechaIng,FechaUlAct,Causa,Destino,Costo,PreVta,Cedula,IdeConf,Sublinea,TipoNegociacion, PLU_ID,Descripcion Plu,Categoria,Descr Categoria,Subcategoria,Descr Subcategoria,Tarifa IVA, pesoUndGR 
&#160; 
 headers_action = insert //insert&#58; se debe insertar el vector de encabezados al archivo que se carga (porque no lo tiene); validate&#58; se debe validar que el vector de encabezados siempre sea uniforme 
&#160; 
&#160; 
 #eatc_dona&#58; detalle de anuncio de donacin&#58; coleccin de productos a ser donados 
&#160; 
 #transformaciones 
 eatc-dona_header_code = Numdoc concat Dependencia//Cdigo de la cabecera del anuncio de donacin (se concatena el nmero de documento con el cdigo de la dependencia) =&gt; SIGUE IGUAL 
 eatc-date_time = FechaHora//Fecha y hora del anuncio de donacin (en formato&#58; AAAAMMDDHHMMSS)&#160; =&gt; SIGUE IGUAL 
 eatc-odd_id = Plu//Identificador nico del producto o artculo donado&#160; =&gt; SIGUE IGUAL 
 eatc-odd_quantity = Cantidad//Cantidad del producto o artculo donado&#160; =&gt; VERIFICAR&#58; si la cantidad la siguen entregando en centenas o ya la estn entregando con el nmero real 
 origin_odds_typology_a = Sublinea//Primera tipologa origen del artculo o producto donado&#160; =&gt; SIGUE IGUAL 
 eatc_VAT_percentage = Tarifa IVA //Porcentaje del impuesto al valor agregado aplicable al producto =&gt; NUEVO 
 eatc-odd_name = Descripcion Plu // Nombre del artculo&#160; =&gt; NUEVO&#58; anteriormente haba que hacer un query para obtener esta informacin, ya llega directamente en el anuncio 
 origin_odds_typology_b = Categoria // Nombre del artculo&#160; =&gt; NUEVO&#58; anteriormente haba que hacer un query para obtener esta informacin, ya llega directamente en el anuncio 
 origin_odds_typology_c = Subcategoria // Nombre del artculo&#160; =&gt; NUEVO&#58; anteriormente haba que hacer un query para obtener esta informacin, ya llega directamente en el anuncioto 
&#160; 
 ***NUEVO&#58; VERIFICAR*** 
 eatc-provider_id = Cedula (VALIDAR&#58; analizar si los datos de este nuevo archivo y de este campo se asimilan al NIT del proveedor) // Cdigo del proveedor del artculo 
&#160; 
 #tipo de transformacin 
 m2z-map-type = //adicion_columnas,cambio_nombre_campo 
&#160; 
 #querys 
 **Nuevo**&#58; si no encuentra informacin en el maestro de productos, deja el campo vaco y contina (se debe registrar el producto en el eatc_dona) 
 eatc-odd_code = si el dato https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id existe, entonces&#58;&#160; eatc_odds.eatc-code https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id , si no existe el dato https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds?eatc-id=$eatc-odd_id se deja vaco //Se toma eatc-odd_id del respectivo anuncio y utilizando la API respectiva para la consulta de eatc_odds se consulta enviando dicho valor al parmetro eatc-id. El valor necesario corresponde al eatc-code que retorna el objeto &#160; =&gt; SIGUE IGUAL 
&#160; 
 ****NUEVO*** Transformacin de sub_pods en pods 
 eatc-pod_id = si el dato &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_sub_pods?eatc_sub_pod_id=&#123;&#123;Dependencia&#125;&#125; trae una respuesta vlida, entonces el valor que se lleva a eatc-pod_id es el que se obtiene en el parmetro eatc_pod_id de esa consulta.&#160; Si no se obtiene un valor vlido en dicha consulta entonces el valor que se lleva a eatc-pod_id es el que llega en el archivo como&#58; Dependencia 
&#160; 
 Ejemplo 1 ambiente de pruebas&#58; 
&#160; 
 En el dato Dependencia lleva el valor&#58; 943, entonces el sistema debe proceder a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_sub_pods?eatc_sub_pod_id=943 &#160; &#160; 
&#160; 
 Como la respuesta del llamado es una respuesta vlida&#58; 
 &#123; 
 _id &#58; &quot;2&quot;, 
 eatc_pod_id &#58; &quot;20&quot;, 
 eatc_pod_name &#58; &quot;CEDI VEGAS MEDELLIN&quot;, 
 eatc_sub_pod_id &#58; &quot;943&quot;, 
 eatc_sub_pod_name &#58; &quot;CEDI VEGAS 2&quot; 
 &#125; 
&#160; 
 Entonces el valor que se lleva a eatc-pod_id es &quot;20&quot; 
&#160; 
 Ejemplo 2 ambiente de pruebas&#58; 
&#160; 
 En el dato Dependencia lleva el valor&#58; 20, entonces el sistema debe proceder a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_sub_pods?eatc_sub_pod_id=20 &#160;&#160; &#160; 
&#160; 
 Como la respuesta del llamado es una respuesta&#160; no es vlida&#58; 
 &#123; 
 ts&#58; &quot;210405102005&quot;, 
 op&#58; true, 
 cont&#58; 0, 
 err_msg&#58; &quot;No se produjeron resultados&quot;, 
 err_num&#58; &quot;&quot;, 
 mem&#58; 0.42, 
 time&#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Entonces el valor que se lleva a eatc-pod_id el mismo dato que se obtiene de Dependencia es decir &quot;20&quot; 
&#160; 
 #constantes 
 eatc-odd_code_type = constant (ean) // para el caso particular (EXITO) siempre ser &quot;ean&quot; &#160; =&gt; SIGUE IGUAL 
 eatc_donor_code = constant(890.900.608-9)//Identificador o cdigo del donante &#160; =&gt; SIGUE IGUAL 
 eatc_donor = constant(exito)//Nombre del donante &#160; =&gt; SIGUE IGUAL 
&#160; 
 ***NUEVO***&#160; 
 eatc_cua_origin = constant (exito) //Cuenta desde la cual se genera el anuncio de donacin 
&#160; 
 #clasificaciones 
 eatc-odd_typology_a = //Primera tipologa del artculo o producto donado 
 eatc-odd_typology_b = //Segunda tipologa del artculo o producto donado 
 eatc-odd_typology_c = //Tercera tipologa del artculo o producto donado 
&#160; 
 #funciones 
&#160; 
 eatc-odd_total_cost = Costo / 100 //El dato que trae el archivo se debe dividir en 100. Costo total del o de los productos o artculos donados (eatc-quantity * eatc-unit_cost)&#160; =&gt; SIGUE IGUAL 
 eatc-unit_cost = eatc-total_cost / eatc-quantity //Costo unitario del artculo o producto donado&#58; se divide el eatc-total_cost sobre eatc-quantity &#160; =&gt; SIGUE IGUAL 
 eatc-original_VAT = eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor original total del impuesto a las ventas (eatc-odd_original_quantity*eatc-odd_unit_cost*eatc_VAT_percentage) &#160; =&gt; SIGUE IGUAL 
 eatc-total_VAT = eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage //Valor definitivo total del impuesto a las ventas&#160; (eatc-odd_quantity*eatc-odd_unit_cost*eatc_VAT_percentage), despus del proceso de verificacin &#160; =&gt; SIGUE IGUAL 
&#160; 
 ***NUEVO&#58; se calcula el peso con el nuevo campo &quot; pesoUndGR &quot; *** 
 eatc-odd_unit_weight_kg = pesoUndGR/1000 //Peso unitario del artculo en kilogramos 
&#160; 
 DEPRECADO&#58; eatc-odd_unit_weight_kg = if (&quot;presentacion&quot;=KG,(eatc_odds.numer(medida)/1000) https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds=$eatc-odd_id) else if (&quot;presentacion&quot;=G,(eatc_odds.numer(medida)/1000000) https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds=$eatc-odd_id), else eatc_odds_kg.valor_kg https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds_kg?plu=$numer(eatc-odd_id), else = 1//Peso unitario del artculo en kilogramos 
&#160; 
&#160; 
 eatc-odd_total_weight_kg = eatc-odd_unit_weight_kg*eatc-odd_quantity &#160; 
&#160; 
 DEPRECADO&#58; //if (&quot;presentacion&quot;=KG,(eatc_odds.numer(medida)/1000)*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds=$eatc-odd_id) else if (&quot;presentacion&quot;=G,(eatc_odds.numer(medida)/1000000)*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds=$eatc-odd_id), else eatc_odds_kg.valor_kg*eatc-odd_quantity https&#58;//donantes.eatcloud.info/api/devexito/eatc_odds_kg?plu=$numer(eatc-odd_id), else = 1&#160; 
&#160; 
 *** 
&#160; 
 eatc-odd_total_height_cm &#160; = // No aplica por no tener datos &#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_width_cm &#160; = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_length_cm &#160; = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
 eatc-odd_total_volume_cm3 = // No aplica por no tener datos&#160; =&gt; SIGUE IGUAL 
&#160; 
 ***NUEVO*** 
 eatc-contains_alergens = // Definicin si la donacin contiene alrgenos.Se enva vaco (ser un campo boleano) 
 eatc-closer_expiration_date = 0000-00-00 //(tipo date) fecha ms prxima de expiracin del producto (o los productos) anunciado(s) 
&#160; 
 #EatCloud 
 eatc-odd_state = //Estado producto&#58; certificable, rechazado. Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin &#160; =&gt; SIGUE IGUAL 
 eatc-odd_rejection_cause = //Causal del rechazo de un producto donado.&#160; Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin&#160; =&gt; SIGUE IGUAL 

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

 MAP_EATC_DONA_EXITO VERSN 2