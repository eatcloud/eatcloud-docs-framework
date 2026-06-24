# api-prohibición-de-consulta-de-anuncios-a-organizaciones-inactivas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando el API reciba un llamado para consultar un anuncio por el identificador_unico_registro de una organizacin, llamado que tiene las siguientes caractersticas 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/ eatc_dona_headers ? eatc-donation_manager_code = {{identificador_unico_registro}} 

 El sistema deber validar si el beneficiario est activo o no para entregarle una respuesta. 

 Para hacer la validacin el sistema deber realizar la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro= {{identificador_unico_registro}} &eatc_state=activo&_cont 

 Si la consulta trae una respuesta vlida ( count mayor que cero ), entonces el sistema devuelve una respuesta tal y como la devuelve normalmente.  Si no debe preguntar por un TOKEN de autorizacin para poder traer la respuesta (se propone que el token tambin se puede entregar de la siguiente manera:) 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/ eatc_dona_headers ? eatc-donation_manager_code = {{identificador_unico_registro}}& _token = {{token}} 

 (La anterior es una propuesta, pero el desarrollador podr definir una manera que considere ms conveniente teniendo siempre como objetivo la seguridad del sistema) 

 NOTA Importante: se debe analizar si por esta va es plausible implementar un token general de consulta de los anuncios.  Para hacerlo que habra que revisar estos procesos y consultas : 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 API: PROHIBICIN DE CONSULTA DE ANUNCIOS DE DONACIN A ORGANIZACIONES INACTIVAS