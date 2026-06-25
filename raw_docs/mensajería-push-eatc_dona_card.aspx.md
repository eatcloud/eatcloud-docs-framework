# mensajería-push-eatc_dona_card.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La mensajera Push debe mostrar siempre los anuncios de&#160; donacin de&quot;todos los donantes disponibles en la plataforma&quot; que se van generando, es decir cuyo estado sea &quot; announced &quot; (anunciado o publicado), ordenados mostrando primero los ms antiguos. 
&#160; 
 Para realizar esta consulta, se realizar un proceso en dos fases (a medida que avance el piloto y el proyecto). 

 Consulta de anuncios ***Revisar dinamismo a partir de _DOM.cua_master*** 
 El primer paso de la consulta es determinar los anuncios cuyo estado es &quot; announced &quot; 
&#160; 
 Para ello el usuario mediante el sistema (que utiliza el API respectiva&#58; eatc_dona_headers ), debe generar mensajes push para los anuncios de donacin cuyo estado sea announced . 
&#160; 
 #Anuncios de donacin ( eatc_dona_headers ) estado &quot; announced &quot; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state=announced 
&#160; 
 Anuncios que han realizado match&#160; 
 Con la consulta de los anuncios con estado &quot; announced &quot;, se procede a realizar la consulta de los que han realizado match con la organizacin respectiva. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_match_registry?eatc-donation_manager_code=90326456-1&amp;eatc-dona_header_code=&#123;&#123;array_codigos&#125;&#125; 
&#160; 
 El sistema toma los cdigos de encabezados obtenidos ( eatc-code )y los almacena en un array (valores separados por comas) . 
&#160; 
 Luego el sistema toma el parmetro &quot; organizacion &quot; del usuario respectivo&#58; 
&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente productivo&#58; 
&#160; 
 El usuario Juan Carlos Buitrago, cuyo &quot;numero_cedula&quot;= 8161174 , tiene como organizacin el dato&#58; 90326456-1 
&#160; 
 Ambiente productivo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174 &#160; 
&#160; 
 Con este parmetro y los cdigos almacenados en el array se va al API de match (eatc_match_registry) y en el parmetro &quot; eatc-donation_manager_code &quot;, se enva el dato obtenido previamente (organizacion) y en el &quot; eatc-dona_header_code &quot; se enva el array obtenido. 
&#160; 
 Ejemplo&#58; 
 El usuario Juan Carlos Buitrago, cuya organizacin es&#58; 90326456-1, se realiza la siguiente consulta&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?eatc-donation_manager_code=90326456-1&amp;eatc-dona_header_code=[array] &#160; 

 CARD de encabezado de anuncio de donacin&#58; informacin 
&#160; 
 Consulta de informacin del anuncio ***REVISAR dinamismo con respecto a _DOM.cua_master*** 
 Para consultar la informacin de los anuncios para mostrar la informacin en la card, es la siguiente&#58; 
&#160; 
 &#123;&#123;URL_ambiente_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id=&#123;&#123;valor&#125;&#125; 
&#160; 
 Esta card mostrar la siguiente informacin&#58; 
&#160; 
 Fecha y hora de publicacin del anuncio&#58; 
 Corresponde al campo &quot; eatc-publication_datetime &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = [valor], corresponde al dato &quot;&quot; que est contenido en el campo &quot; eatc-publication_datetime &quot; 
&#160; 
 Ambiente de prueba&#58; 
 https&#58;//donantes.eatcloud.info/api/devexito/eatc_dona_headers?eatc-id=[valor] &#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_headers?eatc-id=[valor] &#160; 
 &#160; 
 Faltan ##hrs ##min&#58; 
 Tomando el dato de &quot; eatc-publication_datetime &quot;, se le suman 24 horas y la informacin corresponde a la resta de esa hora con respecto a la fecha y hora actual. 
&#160; 
 #### kg&#58; 
 Corresponde al campo &quot; eatc-total_weight_kg &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = [valor], corresponde al dato &quot;&quot; que est contenido en el campo &quot; eatc-total_weight_kg &quot; 
&#160; 
 Ambiente de prueba&#58; 
 https&#58;//donantes.eatcloud.info/api/devexito/eatc_dona_headers?eatc-id=[valor] &#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_headers?eatc-id=[valor] &#160; 
&#160; 
 Nombre del punto de donacin&#58; 
 Corresponde al campo &quot; eatc_pod_name &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = [valor], corresponde al dato &quot;&quot; que est contenido en el campo &quot; eatc_pod_name &quot; 
&#160; 
 Ambiente de prueba&#58; 
 https&#58;//donantes.eatcloud.info/api/devexito/eatc_dona_headers?eatc-id=[valor] &#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_headers?eatc-id=[valor] &#160; 
&#160; 
 Direccin&#58; 
 Corresponde al campo &quot; eatc-pod_address &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = [valor], corresponde al dato &quot;&quot; que est contenido en el campo &quot; eatc-pod_address &quot; 
&#160; 
 Ambiente de prueba&#58; 
 https&#58;//donantes.eatcloud.info/api/devexito/eatc_dona_headers?eatc-id=[valor] &#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_headers?eatc-id=[valor] &#160; 
 &#160; 
&#160; 
 CARD de encabezado de anuncio de donacin&#58; vnculo de accin 
&#160; 
 La card posee el siguiente vnculo&#58; 
 Me interesa&#58;&#160; 
 Que conecta con la funcionalidad &quot; dashboard de anuncio de donacin &quot;, pasando el parmetro &quot; eatc-id &quot; de eatc_dona_headers 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmensajer%C3%ADa-push-eatc_dona_card%2F1556006080-7-PUSH--eatc_dona_card-.png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmensajer%C3%ADa-push-eatc_dona_card%2F1556006080-7-PUSH--eatc_dona_card-.png&ow=750&oh=1334 
 EatCloud Beneficiarios 

 520.000000000000 

 MENSAJERA PUSH: (EATC_DONA_CARD)