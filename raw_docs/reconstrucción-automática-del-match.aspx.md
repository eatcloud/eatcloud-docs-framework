# reconstrucción-automática-del-match.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Este servicio debe correr todas las horas a travs de un cronjob. 
&#160; 
 El servicio deber establecer los anuncios en estado anunciado, que han sido creados durante la tima hora, evaluando los encabezados de donacin 
 &#123;&#123;url_entorno_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_dona_headers?eatc-publication_datetime[0]=&#123;&#123;fecha_actual_AAA-MM-DD&#125;&#125;&amp;atc-publication_datetime[1]=&#123;&#123;fecha_actual_AAA-MM-DD&#125;&#125;&amp;eatc-state=announced&amp;_cmp=eatc-code,eatc-publication_datetime,eatc-pod_id 
&#160; 
 Nota &#58; verificar si por ejemplo con el dato &quot; eatc_dona_headers. eatc_dona_classification_datetime &quot;, tambin se puede evaluar la circunstancia de tener algn problema en el match. 
&#160; 
 Con el array de cdigos del punto de donacin ( eatc-pod_id ) el sistema debe proceder a buscar si existen registros para asignacin / programacin directa 
 &#123;&#123;url_entorno_datagov&#125;&#125;/api/eatcloud/eatc_direct_dona?eatc-pod_id=&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125; 
&#160; 
 Si tiene asignacin directa, se debe revisar que no haya sido rechazada por el beneficiario.&#160; Si ya fue rechazada, se procede al siguiente paso. 
&#160; 
 Si existen registros el sistema debe proceder con la asignacin directa. 
&#160; 
 Si no existen registros, el sistema debe evalar para cada uno de los anuncios ( eatc-code ) si existen datos en el registro de match, para cada uno de los anuncios generados en la ltima hora 
 &#123;&#123;url_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_match_registry?eatc-header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si se encuentra algn anuncio sin registro de match, el sistema deber proceder a invocar para dicho anuncio el servicio para reconstruccin del match&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/clsfmatch&#160; 
&#160; 
 Datos del body 
 &#123; 
 &#160;&#160;&#160;&#160;&quot;cua_master&quot;&#58; &quot;&#123;&#123;cua_master&#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&quot;eatc_dona_header_code&quot;&#58; &quot;&#123;&#123;eatc-dona_header_code&#125;&#125;&quot; 
 &#125; 
&#160; 
 Para regenerar el match de aquellos anuncios sin match en la ltima hora. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 RECONSTRUCCIN AUTOMTICA DEL MATCH