# informe-operativo-de-anuncios-de-donación-eatc_dona_lst2.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** Cambiar el nombre del informe y su botn de men por &quot;Informe histrico de donaciones&quot; 
&#160; 
 Filtro por defecto de la lista ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o programado , es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 
&#160; 
 Consulta eatc-id del pod&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc-id&#125;&#125; 
 Consulta de los anuncios&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id= &#123;&#123;eatc-id&#125;&#125; &amp;eatc-state=announced,awarded,scheduled&#160; 
 En su vista por defecto se debe ordenar el listado mostrando primero los ms recientes y luego los ms antiguos. 
&#160; 
 Consulta de anuncios 
 el sistema toma el parmetro &quot; eatc-id &quot; del punto de donacin ( eatc_pods ) respectivo&#58; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot; = 31 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31&amp;_compress &#160; 

 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31&amp;_compress &#160; 
 Con este parmetro se va al API de encabezados de anuncio de donacin ( eatc_dona_headers ) y en el parmetro &quot; eatc-pod_id &quot;, se enva el dato obtenido previamente (organizacion). 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id (teniendo en cuenta los estados (eatc-state=announced,awarded,scheduled) a fin de no sobrecargar la consulta&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=announced,awarded,scheduled &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=announced,awarded,scheduled&amp;_compress &#160; 
&#160; 
 Filtros ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin condiferentes estados a los del filtro por defecto 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers? eatc-pod_id =&#123;&#123; &#123;&#123;eatc-id&#125;&#125; &#125;&#125;&amp;eatc-state=&#123;&#123;filtro&#125;&#125; 
&#160; 
 ***NUEVO*** Mostrar los filtros que se estn aplicando sobre el listado 
 El sistema deber mostrar en la interfaz de usuario (vista del listado de anuncios) los filtros que se estn aplicando en el momento y que pueden ser variados con la presente funcionalidad 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 ( eatc-pod_id ) , desea consultar los anuncios certificados (eatc-state=certified)&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id =31&amp;eatc-state=certified &#160; 
&#160; 
 El sistema deber mostrar, despus de esta accin, que se est aplicando el anterior filtro al listado 
 Card del anuncio de donacin 
 El informe debe ser construido en tiempo real para mostrar la fotografa (o estado actual) de los anuncios en el momento que se carga el informe. Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
 Cada anuncio de donacin ( eatc_dona_headers ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 
&#160; 
 ENCABEZADO&#58; 
 Cdigo del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-code 
&#160; 
 Fecha y hora del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre&#58; eatc_dona_headers .eatc-donation_manager_name 
 Direccin&#58; eatc_dona_headers .eatc-donation_manager_address 
 Telfono&#58; eatc_dona_headers .eatc-donation_manager_address 
 Ver mapa&#58; consulta de las coordenadas del anuncio eatc_dona_headers .eatc-lat, eatc_dona_headers .eatc-long 
 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga &quot;PENDIENTE DE ADJUDICACIN&quot; 
&#160; 
 DETALLE ANUNCIO&#58; 
 Peso total (del anuncio) 
 eatc_dona_headers .eatc-total_weight_kg 
&#160; 
 Valor total (del anuncio) 
 eatc_dona_headers .eatc-total_cost 
&#160; 
 TRACKING&#58; 
 Hora publicacin 
 eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Hora adjudicacin 
 eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Hora de entrega programada 
 eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Hora de entrega real llegada 
 eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Hora de entrega real salida 
 eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Hora de recepcin 
 eatc_dona_headers .eatc-receipt_datetime 
&#160; 
 Hora de pre-certificacin 
 eatc_dona_headers .eatc-pre_certification_datetime 
&#160; 
 Hora de certificacin 
 eatc_dona_headers .eatc-certification_datetime 
&#160; 
 ESTADO ( eatc_dona_states ) 
 Vale la pena anotar que los estados son acumulativos, respecto al orden, es decir, que un anuncio &quot;entregado&quot; fue previamente &quot;programado&quot;, &quot;adjudicado&quot; y &quot;anunciado&quot;, por lo tanto los estados anteriores al actual deben aparecer marcados en la card. 
&#160; 
 ETIQUETAS DE ESTADO 
 Muestran el estado , en el que se encuentra el anuncio, sabiendo que segn el &quot;order&quot; de dichos estados, se muestran de manera acumulativa. 
 Ejemplo&#58; 
 un anuncio cuyo estado sea &quot;scheduled&quot; (programado) y que tiene el valor &quot;order&quot; =3, tambin debe tener marcados los radio buton , &quot;awared&quot; (adjudicado, con &quot;order&quot;=2) y &quot;announced&quot; (anuncidado con &quot;order&quot;=1) 
&#160; 
 Botn + 
 Este botn dar la entrada a la funcionalidad &quot; dashboard de anuncio de donacin (eatc_dona_dsh) &quot;, pasando el identificador del encabezado ( eatc-id ). 
&#160; 
 Botn&#58; consulta de novedades de anuncio de donacin ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Con este botn se debe generar una consulta al registro de novedades ( eatc_odd_rejection_registry ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_odd_rejection_registry?eatc-dona_header_code=&#123;&#123;eatc-dona_header_code&#125;&#125; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40716, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code=40716 
&#160; 
 Botn&#58; consulta de histrico de estados del anuncio de donacin ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Con este botn se debe generar una consulta al registro de de histrico de estados ( eatc_dona_header_state_history ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. Esta informacin debe estar ordenada ascendentemente por fecha ( eatc-date_time ) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_header_state_history?eatc-dona_header_code=&#123;&#123;eatc-dona_header_code&#125;&#125; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code ) es 40717, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 
&#160; 
 Botn&#58; consulta de histrico de coordenadas del anuncio de donacin ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Con este botn se debe generar una consulta al registro de de histrico de estados ( eatc_dona_header_geo_history ) para el anuncio particular en un mapa 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_header_geo_history?eatc-dona_header_code=&#123;&#123;eatc-dona_header_code&#125;&#125; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code ) es 40717, el sistema debe realizar la siguiente consulta para mostrar los puntos en el mapa 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_header_geo_history?eatc-dona_header_code=40717 &#160; 
&#160; 
 Botn&#58; generar certificado preliminar =&gt; QUITARLO (esto se har por una funcionalidad backoffice) 
&#160; 
 Botn&#58; generar constancia de donacin [PENDIENTE DOCUMENTAR] =&gt; QUITARLO (esto se har por una funcionalidad backoffice) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=8c222dc0bef341bd9bd10612de21f418&ext=png&ow=1280&oh=1792, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=8c222dc0bef341bd9bd10612de21f418&ext=png&ow=1280&oh=1792 
 EatCloud Donantes Desktop 

 110.000000000000 

 INFORME OPERATIVO DE ANUNCIOS DE DONACIN (EATC_DONA_LST2)