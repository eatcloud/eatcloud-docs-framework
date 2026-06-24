# botones-de-acción-donante.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Desde el dashboard se podr ingresar a los siguientes botones: 

 Seguimiento de anuncios ***Revisar dinamismo en consulta a partir de: _DOM.cua_master*** 
 El globo de notificacin presenta los anuncios de donacin ( eatc_dona_headers ) cuyo estado es "anunciado" y presenta un vnculo a la funcionalidad " seguimiento de anuncios ".  
 {{URL_entorno_donantes}}/api/ {{_DOM.cua_master}} /eatc_dona_headers?eatc-pod_id={{eatc-pod_id}}&eatc-state=announced&_compress 

 Ejemplo: 
 El usuario "EXITO COLOMBIA", cuyo " eatc-id ""= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id para establecer el nmero de anuncios de donacin con estado "anunciados" (eatc-state=announced): 

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&eatc-state=announced   

 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&eatc-state=announced&_compress    

 Siendo 20 de septiembre de 2019, el API responde de la siguiente manera: 
 { 
 ts : "190920144333", 
 op : true, 
 cont : 43, 
 - res : ... 
 } 

 Por lo tanto el nmero que se debe pintar en el globo sera " 43 " 

 Entrega de donacin ***Revisar dinamismo en consulta a partir de: _DOM.cua_master*** 
 el globo de notificacin presenta los anuncios de donacin ( eatc_dona_headers ) cuyo estado es "programado (scheduled)". Este listado es similar a " seguimiento de anuncios de donaciones ", pero debe presentar un acceso directo para cada anuncio a la funcionalidad  " entrega de donacin " (en vez que el "+" dirija al dashboard del anuncio de donacin debe dirigir directamente a la " entrega de donacin " ). 
 {{URL_entorno_donantes}}/api/ {{_DOM.cua_master}} /eatc_dona_headers?eatc-pod_id={{eatc-pod_id}}&eatc-state=scheduled&_compress 

 Ejemplo: 
 El usuario "CARULLA PALMAS", cuyo " eatc-id ""= 339 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id para establecer el nmero de anuncios de donacin con estado "programados" (eatc-state=scheduled): 

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=339&eatc-state=scheduled   

 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=339&eatc-state=scheduled&_compress     

 Siendo 20 de septiembre de 2019, el API responde de la siguiente manera: 
 { 
 ts : "190920144333", 
 op : true, 
 cont : 1, 
 - res : ... 
 } 

 Por lo tanto el nmero que se debe pintar en el globo sera " 1 " 

 Anuncio de donacin: 
  para el piloto del xito este botn puede estar deshabilitado.  Debe presentar un acceso a la funcionalidad " Creacin de anuncio de donacin ". 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbotones-de-acci%C3%B3n-donante%2F2781385317-EmbeddedImage.png&ow=1024&oh=351, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbotones-de-acci%C3%B3n-donante%2F2781385317-EmbeddedImage.png&ow=1024&oh=351 
 EatCloud Donantes 

 76.0000000000000 

 BOTONES DE ACCIN (EATC_PODS_BTN)