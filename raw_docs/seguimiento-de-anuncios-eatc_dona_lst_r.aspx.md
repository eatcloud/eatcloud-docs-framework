# seguimiento-de-anuncios-eatc_dona_lst_r.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Filtro por defecto de la lista 
 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o programado , es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 
&#160; 
 Consulta de anuncios 
&#160; 
 el sistema toma el parmetro &quot; eatc-id &quot; del punto de donacin ( eatc_pods ) respectivo&#58; 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot; = 31 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31&amp;_compress &#160; 

 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31 &#160;&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31&amp;_compress &#160;&#160; 
&#160; 
 Con este parmetro se va al API de encabezados de anuncio de donacin ( eatc_dona_headers ) y en el parmetro &quot; eatc-pod_id &quot;, se enva el dato obtenido previamente (organizacion). 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id (teniendo en cuenta los estados (eatc-state=announced,awarded,scheduled) a fin de no sobrecargar la consulta&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id= 31&amp;eatc-state=announced,awarded,scheduled &#160;&#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id= 31&amp;eatc-state=announced,awarded,scheduled&amp;_compress &#160; 
&#160; 
 Filtros 
&#160; 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin condiferentes estados a los del filtro por defecto 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 ( eatc-pod_id ) , desea consultar los anuncios certificados (eatc-state=certified)&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id = 31 &amp;eatc-state=certified 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id = 31 &amp;eatc-state=certified&amp;_compress &#160;&#160;&#160; 
&#160; 
 Card del anuncio de donacin 
&#160; 
 El informe debe ser construido en tiempo real para mostrar la fotografa (o estado actual) de los anuncios en el momento que se carga el informe. Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
 Cada anuncio de donacin ( eatc_dona_headers ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 
&#160; 
 Fecha y hora del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre&#58; eatc_dona_headers .eatc-donation_manager_name 
 Direccin&#58; eatc_dona_headers .eatc-donation_manager_address 
 Telfono&#58; eatc_dona_headers .eatc-donation_manager_address 
 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga &quot;PENDIENTE DE ADJUDICACIN&quot; 
&#160; 
 Total de kilos que contiene el anuncio 
 eatc_dona_headers .eatc-total_weight_kg 
&#160; 
 Estado del anuncio ( eatc_dona_states ) 
&#160; 
 Vale la pena anotar que los estados son acumulativos, respecto al orden, es decir, que un anuncio &quot;entregado&quot; fue previamente &quot;programado&quot;, &quot;adjudicado&quot; y &quot;anunciado&quot;, por lo tanto los estados anteriores al actual deben aparecer marcados en la card. 
&#160; 
 Botn + 
&#160; 
 Este botn dar la entrada a la funcionalidad &quot; dashboard de anuncio de donacin (eatc_dona_dsh) &quot;, pasando el identificador del encabezado ( eatc-id ). 
&#160; 
 RADIO BUTONS DE ESTADO 
&#160; 
 Muestran el estado , en el que se encuentra el anuncio, sabiendo que segn el &quot;order&quot; de dichos estados, se muestran de manera acumulativa. 
&#160; 
 Ejemplo&#58; 
 un anuncio cuyo estado sea &quot;scheduled&quot; (programado) y que tiene el valor &quot;order&quot; =3, tambin debe tener marcados los radio buton , &quot;awared&quot; (adjudicado, con &quot;order&quot;=2) y &quot;announced&quot; (anuncidado con &quot;order&quot;=1) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-anuncios-eatc_dona_lst_r%2F2489217077-4-seguimiento-anuncios--eatc_dona_lst_r-.png&ow=1280&oh=1792, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-anuncios-eatc_dona_lst_r%2F2489217077-4-seguimiento-anuncios--eatc_dona_lst_r-.png&ow=1280&oh=1792 
 EATCLOUD DONANTES DESKTOP 

 86.0000000000000 

 SEGUIMIENTO DE ANUNCIOS (EATC_DONA_LST_R)