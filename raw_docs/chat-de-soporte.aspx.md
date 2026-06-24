# chat-de-soporte.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se habilitar un chat de soporte que debe estar visible en la parte inferior derecha de las diferentes pginas de la App (empezando por el dashboard general). Esta funcionalidad se le debe mostrar solo a clientes cuya categorizacin (en primera instancia) sea diferente a "free". 

 Despliegue de la funcionalidad 
 Realizando una consulta de los datos respectivos de la cuenta (eatc_cua), la funcionalidad se les desplegar a los clientes cuyo tipo (type) exista y sea diferente de "free".  Si no existe el campo o si est vaco, no se debe desplegar la funcionalidad. 

 Ejemplo 1: se despliega la funcionalidad: 

 Para un punto de donacin de la cuenta "exito", el sistema deber realizar la siguiente consulta para determinar el tipo de cliente: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito ) 

 Dado que la respuesta es la siguiente: 

 costs : "eatc_dona", 
 eatc-country: "co", 
 days_before_expiration : "3", 
 eatc_dona_upl : "no", 
 eatc_odds_app : "eatc_dona_app", 
 eatc_rec_doc : "no", 
 eatc_rec_doc_signature : "n", 
 eatc_rec_odds_pre_verification : "n", 
 edit_coordinates : "no", 
 id__ : "exito", 
 name : "exito", 
 odds_weight : "eatc_dona", 
 taxes : "eatc_dona", 
 type : "hero" 

 Y se tine un " type " diferente (=!) a "free", se le debe desplegar el chat de soporte. 

 Ejemplo 2: no se despliega la funcionalidad: 

 Para un punto de donacin de la cuenta "makro", el sistema deber realizar la siguiente consulta para determinar el tipo de cliente: 
 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro    
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro ) 

 Dado que el resultado de la consulta es el siguiente: 

 costs : "eatc_dona", 
 eatc_contry : "co", 
 days_before_expiration : "5", 
 eatc_dona_upl : "yes", 
 eatc_odds_app : "eatc_odds", 
 eatc_rec_doc : "no", 
 eatc_rec_doc_signature : "n", 
 eatc_rec_odds_pre_verification : "n", 
 edit_coordinates : "si", 
 id__ : "makro", 
 name : "makro", 
 odds_weight : "eatc_dona", 
 taxes : "eatc_dona" 
 type : "free", 

 y como en el registro el parmetro " type " es diferente a " hero ", entonces no se despliega la funcionalidad (si el registro existiera y estuviera vaco o nulo, o si existiera y tuviera como registro "free", la funcionalidad no se desplegara tampoco. 

 Widget para mostrar el chat  ***NUEVO*** 
 En la parte inferior derecha de las pginas de la web app, empezando por el dashboard, se debe, si se cumple la condicin arriba descrita, se debe incorporar el siguiente widget en un botn que diga "soporte" (ver cono de salvavidas en fondo fucsia en la parte inferior derecha del sitio web: https://www.eatcloud.com/ ) 

 window.fwSettings={ 
 'widget_id':67000003386 
 }; 
 !function(){if("function"!=typeof window.FreshworksWidget){var n=function(){n.q.push(arguments)};n.q=[],window.FreshworksWidget=n}}()  

 El despliegue del widget debe visualizarse como se muestra en la siguiente imagen: 

 Para mayor informacin sobre esta herramienta se puede consultar la siguiente documentacin: 

 ACCESOS: 
 https://eatcloud.zendesk.com/admin   
 usuario: isisespitia@nodrizza.com 
 Clave: Amarillo2021 

 DOCUMENTACIN: 
 https://eatcloud.zendesk.com/agent/admin/widget   
 https://support.zendesk.com/hc/es/articles/203908456 
 https://support.zendesk.com/hc/es/articles/115009692388-Configuring-components-in-the-Web-Widget 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fchat-de-soporte%2F637745911-EmbeddedImage--15-.png&ow=1280&oh=714, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fchat-de-soporte%2F637745911-EmbeddedImage--15-.png&ow=1280&oh=714 

 151.000000000000 

 CHAT DE SOPORTE