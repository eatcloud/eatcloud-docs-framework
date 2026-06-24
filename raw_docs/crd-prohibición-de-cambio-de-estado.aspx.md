# crd-prohibición-de-cambio-de-estado.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando el CRD reciba un llamado para cambiar el estado de un anuncio, que tengan las siguientes caractersiticas 

 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_headers &_operacion= update & eatc-state = announced &WHERE{{...}} 

 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_headers &_operacion= update & eatc-state = awarded &WHERE{{...}} 

 El sistema deber analizar, si la donacin o las donaciones a las cuales se les est intentando cambiar el estado tienen estado atc-state = announced o eatc-state = awarded y se permtir realizar el cambio. 

 Si la donacin o las donaciones no tienen uno de los anteriores estados (es decir si tienen un estado eatc-state = scheduled o eatc-state = delivered o eatc-state = pre-certified o eatc-state = certified) ,  la respuesta que debe entregar el CRD es un " Forbidden " y no se debe efectuar el cambio (no se realiza el update) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CRD: PROHIBICIN DE CAMBIO DE ESTADO ANTERIOR (ANNOUNCED, AWARDED) PARA DONACIN CON ESTADO "SCHEDULED"