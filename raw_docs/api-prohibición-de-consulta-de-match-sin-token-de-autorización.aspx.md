# api-prohibición-de-consulta-de-match-sin-token-de-autorización.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando el API reciba un llamado para consultar un anuncio por el identificador_unico_registro de una organizacin, llamado que tiene las siguientes caractersticas 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/ eatc_match_registry? eatc-donation_manager_code = {{ identificador_unico_registro }} 

 La no entrega de respuesta sin token, tambin deber operar, si el valor {{ identificador_unico_registro }} es indefinido ( undefined ), nulo ( null ), vaco, o con el operador _* 

 El sistema deber solicitar un TOKEN vlido para poder retornar una respuesta vlida, el cul podr hacerse de esta manera :  

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/ eatc_match_registry? eatc-donation_manager_code = {{identificador_unico_registro}} &_token={{token_valido}} 

 (La anterior es una propuesta, pero el desarrollador podr definir una manera que considere ms conveniente teniendo siempre como objetivo la seguridad del sistema) 

 Sistema de persistencia de tokens 
 Se propone  

 Hay que revisar estas consultas y procesos para implementar el ajuste . 

 Match query: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/matchquery-proceso-para-consulta-de-anuncios-que-hacen-match.aspx   
 Mensajera PUSH: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/mensajer%C3%ADa-push-eatc_dona_card.aspx   

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 API: PROHIBICIN DE CONSULTA DE MATCH A LLAMADOS SIN TOKENS