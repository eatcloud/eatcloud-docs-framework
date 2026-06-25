# reclasificación-de-anuncios-por-tiempo.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Reclasificacin de anuncios por tiempo&#160; 
&#160; 
 El sistema deber implementar un proceso que corra cada 10 minutos y que&#160; permita reclasificar anuncios que tengan definida una regla de reclasificacin por tiempo.&#160;&#160; 
&#160; 
 En primera instancia aplica para anuncios del piloto de Nestl 
 Estas reglas de reclasificacin solo aplicarn para anuncios en estado &quot;anunciado&quot; y cuya regla de clasificacin pertenece al piloto de Nestl. Para ello el sistema deber realizar la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_dona_headers?eatc-state= announced &amp; eatc_match_asignation_rule =&#123;&#123; _lk pacadi_nestle _lk &#125;&#125;&amp;_cmp= eatc-code , eatc_match_asignation_rule,eatc-publication_datetime 
&#160; 
 o ms especficamente&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/mexico/ eatc_dona_headers?eatc-state= announced &amp; eatc_match_asignation_rule =&#123;&#123; _lk pacadi_nestle _lk &#125;&#125;&amp;_cmp= eatc-code , eatc_match_asignation_rule,eatc-publication_datetime 

&#160; 
 Consulta de tiempo y destino de reclasificacin 
 El sistema debe consultar aquellos anuncios encontrados por la consulta anterior, cul es el destino de reclasificacin definido y cul es el tiempo definido para hacer el cambio de estado, con la siguiente consulta&#160;&#160; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reclassification_rules?eatc_origin_match_asignation_rule=&#123;&#123;eatc_dona_headers. eatc_match_asignation_rule &#125;&#125;&amp;_cmp=eatc_origin_match_asignation_rule,eatc_destiny_match_asignation_rule,eatc_timeout_from,eatc_timeout_in_minutes 

&#160; 
 Comparacin de fechas y horas para establecer si el anuncio debe reclasificarse (inicialmente con el parmetro eatc-publication_datetime &quot;quemado&quot;&#58; luego si es necesario se dinamizar) 
&#160; 
 El sistema debe comparar el dato (fecha y hora) que llega &quot; eatc-publication_datetime &quot;, sumndole el timeout en minutos respectivo ( eatc_dona_reclassification_rules. eatc_timeout_in_minutes ) con la fecha y hora actual.&#160; Si la diferencia entre la fecha (de la sumantoria del publication_datetime y el timeout&#58; minuendo) y la fecha y hora actual (sustraendo) es mayor que cero (es decir que la fecha de de publicacin ms el timeout&#160; es posterior a la fecha y hora actual) el sistema no reclasificar el anuncio.&#160; Por el contrario si la fecha de publicacin ms el timeout es anterior a la fecha y hora actual, entonces se deber realizar la clasificacin mediante estas acciones&#58; 
&#160; 
 Accin 1&#58; Actualizacin de la informacin del encabezado de donacin ( eatc_dona_headers ) 
 El sistema deber realizar la siguiente escritura 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_headers&amp;_operacion=update&amp; eatc_match_asignation_rule =&#123;&#123;eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125;&amp;WHERE eatc_dona_header_code =&#123;&#123;eatc_dona_headers. eatc_dona_header_code &#125;&#125; 
&#160; 
 Accin 2&#58; registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) 
&#160; 
 Se utilizar el log de cambio de estados para dejar traza de la reclasificacin realizada. Utilizando el API el registro sera algo como lo siguiente 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125; /?_tabla= eatc_dona_header_state_history &amp;_operacion=insert&amp; eatc-dona_header_code = &#123;&#123;eatc_dona_headers. eatc_dona_header_code &#125;&#125; &amp; eatc-state = announced &amp; eatc-date_time =&#123;&#123;datetimestamp&#125;&#125;&amp; eatc-log =&quot;EatCloud cambi la regla de asignacin del anuncio de &#123;&#123;eatc_dona_reclassification_rules. eatc_origin_match_asignation_rule &#125;&#125; a &#123;&#123;eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125; porque se cumpli el plazo de &#123;&#123;eatc_dona_reclassification_rules. eatc_timeout_in_minutes &#125;&#125; minutos 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 RECLASIFICACIN DE ANUNCIOS POR TIEMPO