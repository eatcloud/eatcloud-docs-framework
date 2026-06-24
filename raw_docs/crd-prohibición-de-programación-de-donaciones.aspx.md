# crd-prohibición-de-programación-de-donaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando el CRD reciba un llamado para cambiar el estado de un anuncio, que tengan las siguientes caractersticas 

 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_headers &_operacion= update &{{...}}& eatc-state = scheduled &WHERE{{...}} 

 Ejemplo: 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla=eatc_dona_headers&_operacion=update& eatc-scheduling_datetime= {{datetime}} &eatc-programed_picking_datetime= {{datetime}}] & eatc-state= scheduled & eatc-picker_name ={{valor}}& eatc-picker_doc_id ={{valor}}& eatc-picker_license_plate ={{valor}}&WHEREeatc-code={{valor}} 

 Si la donacin o las donaciones tienen un estado previo eatc-state = announced , eatc-state = awarded ,  la respuesta que debe entregar el CRD es un " Forbidden " y no se debe efectuar el cambio (no se realiza el update) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CRD: PROHIBICIN DE PROGRAMACIN DE DONACIONES