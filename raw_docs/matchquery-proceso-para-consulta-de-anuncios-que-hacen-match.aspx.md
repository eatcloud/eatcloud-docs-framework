# matchquery-proceso-para-consulta-de-anuncios-que-hacen-match.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se implementar un servicio que tenga la siguiente estructura&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/matchquery/&#123;&#123;_DOM.cua_master&#125;&#125;/&#123;&#123;eatc_donation_managers.identificador_unico_registro&#125;&#125; ?_compress 
&#160; 
 Nota &#58; el parmetro _compress es opcional, si se enva, la respuesta final del servicio se entrega comprimida y si no, se entrega descomprimida. 

&#160; 
 EJEMPLO&#58;&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/matchquery/abaco/811018073?_compress 
 https&#58;//devbeneficiarios.eatcloud.info/matchquery/abaco/811018073 &#160; 

&#160; 
 Y cuando sea invocado realizar las siguientes consultas&#58; 
&#160; 
 NUEVO &#58; Consulta del estado del donation manager para la consulta del match 
&#160; 
 El servicio debe consultar si el gestor de donaciones tiene estatus &quot; activo &quot;,&#160; si el gestor de donacin tiene un estado diferente a &quot; activo &quot; no podr consultar la nube, y el servicio debe enviar un mensaje de error o simplemente no contestarle&#58; 

&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/ api /&#123;&#123;_DOM. cua_master &#125;&#125;/ &#123;eatc_donation_managers? identificador_unico_registro =&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;_distinct= eatc_state 

&#160; 
 Consulta de los anuncios que hacen match ***NUEVO&#58; validacin de la fecha desde la cual es vlido del match (eatc_match_registry. matching_since )*** 

&#160; 
 NOTA &#58; el campo eatc_match_registry. matching_since an no se ha creado.&#160; Para realizar esta implementacin deber implementarse primero el servicio para registro del match, en donde se llenar dicho campo. 
&#160; 
 Al recibir el llamado el sistema debe tomar la fecha actual ( fecha_actual ) y calcular la fecha de cinco das atrs ( fecha_hace_cinco_dias ) para con ella, y los parmetros recibidos en la consulta realizar la siguiente consulta sobre la tabla de match.&#160; Tambin el sistema deber calcular la fecha y hora actual ( fecha_y_hora_actual )&#160; y utilizando el operador lgico =_&gt;_ (que inicialmente se sabe funciona con nmeros) para determinar si la fecha y hora registrada en eatc_match_registry. matching_since &#160; es anterior a la fecha y hora actual (si este operador lgico no opera con fechas se debe realizar la respectiva implementacin).&#160; En caso de serlo, se desplegar el anuncio, pero si la fecha y hora desde la cual se despliega el match ( eatc_match_registry. matching_since ) es posterior, es decir, est en el futuro, no se debe traer el respectivo anuncio&#58; 

&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_match_registry? fecha_corta[0]=&#123;&#123; fecha_hace_cinco_dias &#125;&#125;&amp;fecha_corta[1]=&#123;&#123; fecha_actual &#125;&#125;&amp;eatc-donation_manager_code= &#123;&#123;eatc_donation_managers.identificador_unico_registro&#125;&#125;&amp; matching_since=_&gt;_&#123;&#123; fecha_y_hora_actual &#125;&#125; &amp;_distinct= eatc-dona_header_code &amp;_token=&#123;&#123;token_valido&#125;&#125; 
&#160; 
 NOTA &#58; a este llamado se le debe incorporar un token vlido, una vez se implemente la prohibicin de llamado al match sin token 

&#160; 
 EJEMPLO&#58; 12 de mayo 2021 (este ejemplo no incluye la prueba lgica sobre eatc_match_registry. matching_since ) 
&#160; 
 Retomando el ejemplo anterior (https&#58;//devbeneficiarios.eatcloud.info/matchquery/abaco/eatc_donation_manager_code= 811018073 &amp;_compress) 
&#160; 
 Por lo tanto como primera medida se debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_match_registry? fecha_corta[0]=2021-05-07&amp;fecha_corta[1]=2021-05-12&amp;eatc-donation_manager_code= 811018073&amp;_distinct= eatc-dona_header_code &#160; 
&#160; 

&#160; 
 Con los eatc-dona_header_code que recupera la consulta ( array_dona_header_codes) se realiza la siguiente 

&#160; 
 Para el ejemplo anterior&#58;&#160; 
&#160; 
 array_dona_header_codes= 00002105090031,00002105090075,00002105090516,00002105090728,00002105090729,exito4520210511092708124,exito4520210511121239744 

&#160; 
 Consulta de los anuncios 
 Con el array recibido de la anterior consulta se realiza la siguiente (dado que se envi el parmetro _compress) que debe constituirse en la respuesta final del servicio&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers? eatc-code=&#123;&#123; array_dona_header_codes &#125;&#125;&amp; eatc-state=announced &amp;_compress 
&#160; 
 Si no se hubiera recibido el parmetro _compress sera la misma consulta pero sin l 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers? eatc-code=&#123;&#123; array_dona_header_codes &#125;&#125;&amp; eatc-state=announced&#160; 
&#160; 
 La respuesta que entrega esta consulta es la que se entrega como respuesta del servicio. 

&#160; 
 Para el ejemplo anterior&#58;&#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-code= 00002105090031,00002105090075,00002105090516,00002105090728,00002105090729,exito4520210511092708124,exito4520210511121239744 &amp; eatc-state=announced &amp;_compress &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 MATCHQUERY: PROCESO PARA CONSULTA DE ANUNCIOS QUE HACEN MATCH