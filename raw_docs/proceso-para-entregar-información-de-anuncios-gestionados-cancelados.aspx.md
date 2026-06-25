# proceso-para-entregar-información-de-anuncios-gestionados-cancelados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 A travs del API pblica para crear donaciones , se recibirn parmetros adicionales, para consultar donaciones en estados que correspondan a una &quot;gestin exitosa&quot; o a donaciones que correspondan a una gestin &quot;no exitosa&quot;&#160; 
&#160; 
 Consulta de anuncios con gestin exitosa 
&#160; 
 A travs del del API pblica para crear donaciones , se recibirn los siguientes parmetros (ajustar documentacin del API ),&#160; 
 gestion_exitosa 
 fecha_inicial 
 fecha_final 
&#160; 
 para consuLtar los anuncios con gestin exitosa, aportando su cdigo, documento soporte (de tenerlo), su peso y su costo (despus del proceso de verificacin detallada) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;eatc-state=received,pre-certified,certified&amp;_cmp=eatc-code,eatc-total_weight_kg,eatc-total_cost,eatc-doc,eatc-state 
&#160; 
 El sistema responder con el array que devuelve la anterior consulta 
&#160; 
 Consulta de anuncios con no gestin exitosa 
 A travs del del API pblica para crear donaciones , se recibirn los siguientes parmetros (ajustar documentacin del API ),&#160; 
 gestion_no_exitosa 
 fecha_inicial 
 fecha_final 
&#160; 
 para consultar los anuncios con gestin exitosa, aportando su cdigo, documento soporte (de tenerlo), su peso y su costo (despus del proceso de verificacin detallada) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;eatc-state=cancelled,not_delivered&amp;_cmp=eatc-code,eatc-doc,eatc-state 
&#160; 
 El sistema responder con el array que devuelve la anterior consulta y le adicionar a la respuesta el resultado de la siguiente consulta, colocando en&#160; eatc-state=deleted 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_deleted_dona_header?eatc-publication_date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;_cmp=eatc-code,eatc-doc 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESO DE ENTREGA INFORMACIN DE ANUNCIOS CON GESTIN EXITOSA O NO EXITOSA