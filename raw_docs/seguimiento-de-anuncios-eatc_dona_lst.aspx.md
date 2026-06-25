# seguimiento-de-anuncios-eatc_dona_lst.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Filtro por defecto de la lista 

 Se debe permitir filtrar por los diferentes estados del anuncio de donacin ( eatc_dona_states ), teniendo al ingresar a la vista el filtro por defecto que presente anuncios de donacin con estado &quot;announced&quot; o &quot;anunciado&quot;, &quot;awarded&quot; o &quot;adjudicado&quot; y &quot;scheduled&quot; o &quot;programado&quot;, es decir, en la lista se deben mostrar los anuncios que aun estn en el almacn y estn pendientes de ser entregados. 
&#160; 
 En su vista por defecto se debe ordenar el listado mostrando primero los ms recientes y luego los ms antiguos. 
&#160; 
 Consulta de anuncios ***Revisar dinamismo a partir de _DOM.cua_master*** 
&#160; 
 el sistema toma el parmetro &quot; eatc-id &quot; del punto de donacin ( eatc_pods ) respectivo&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_pods?eatc-id=&#123;&#123;eatc-id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot; = 31 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31&amp;_compress &#160; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31&amp;_compress &#160;&#160; 
&#160; 
 Con este parmetro se va al API de encabezados de anuncio de donacin ( eatc_dona_headers ) y en el parmetro &quot; eatc-pod_id &quot;, se enva el dato obtenido previamente (organizacion). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_dona_headers?eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;eatc-state=announced,awarded,scheduled 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id (teniendo en cuenta los estados (eatc-state=announced,awarded,scheduled) a fin de no sobrecargar la consulta&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=announced,awarded,scheduled &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&amp;eatc-state=announced,awarded,scheduled&amp;_compress &#160; 

 Filtros [NUEVO estado &quot;cancelled&quot; para incorporar al filtro] 
 Los filtros deben realizar llamados al API, para traer anuncios de donacin condiferentes estados a los del filtro por defecto 
&#160; 
 Ejemplo&#58; 
 El usuario &quot;EXITO COLOMBIA&quot;, cuyo &quot; eatc-id &quot;&quot;= 31 ( eatc-pod_id ) , desea consultar los anuncios certificados (eatc-state=certified)&#58; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id =31&amp;eatc-state=certified &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id =31&amp;eatc-state=certified&amp;_compress &#160; 
&#160; 
 ****NUEVO**** 
 NOTA &#58; se debe incorporar un nuevo valor al filtro &quot;cancelados&quot; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-pod_id =31&amp;eatc-state=cancelled &#160; 
 ****NUEVO**** 

 Card del anuncio de donacin 

 El informe debe ser construido en tiempo real para mostrar la fotografa de los anuncios en el momento que se&#160; carga el informe.&#160; Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
&#160; 
 Cada anuncio de donacin ( eatc_dona_headers ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 
&#160; 
 Fecha y hora del anuncio&#58; 
 &#160; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Datos del gestor de donaciones ( eatc_donation_manager )&#160; al cual se le adjudic el anuncio 

 Nombre&#58; eatc_dona_headers .eatc-donation_manager_name 
 Direccin&#58; eatc_dona_headers .eatc-donation_manager_address 
 Telfono&#58; eatc_dona_headers .eatc-donation_manager_address 

 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga &quot;PENDIENTE DE ADJUDICACIN&quot; 

 Total de kilos que contiene el anuncio 

 eatc_dona_headers .eatc-total_weight_kg 

 Estado del anuncio ( eatc_dona_states ) 

 Vale la pena anotar que los estados son acumulativos, respecto al orden, es decir, que un anuncio &quot;entregado&quot; fue previamente &quot;programado&quot;, &quot;adjudicado&quot; y &quot;anunciado&quot;, por lo tanto los estados anteriores al actual deben aparecer marcados en la card. 
&#160; 
 ***NUEVO*** 
&#160; 
 El nico estado que no es acumulativo con los dems es el estado &quot; cancelado &quot;.&#160; Para mostrar las dems etiquetas de estado (para los dems estados acumulativas), cuando un anuncio ha sido cancelado (eatc-dona_state=cancelled), se debe mostrar la respectiva etiquera &quot;cancelado&quot; y las dems se colocarn consultando las respectivas fechas (se deben leer las siguientes fechas, y si existe una registrada, o una fecha vlida registrada, entonces se colocarn las siguientes etiquetas)&#58; 
 eatc-publication_datetime&#58; se coloca la etiqueta&#58; anunciado 
 eatc-adjudication_datetime&#58; se coloca la etiqueta&#58; adjudicado 
 eatc-scheduling_datetime&#58; se coloca la etiqueta&#58; programado 

 Botn + 

 Este botn dar la entrada a la funcionalidad &quot; dashboard de anuncio de donacin (eatc_dona_dsh) &quot; 

 RADIO BUTONS DE ESTADO 
 Muestran el estado , en el que se encuentra el anuncio, sabiendo que segn el &quot;order&quot; de dichos estados, se muestran de manera acumulativa. 
&#160; 
 Ejemplo&#58; 
 un anuncio cuyo estado sea &quot;scheduled&quot; (programado) y que tiene el valor &quot;order&quot; =3, tambin debe tener marcados los radio button , &quot;awared&quot; (adjudicado, con &quot;order&quot;=2) y &quot;announced&quot; (anunciado con &quot;order&quot;=1) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-anuncios-eatc_dona_lst%2F2057546684-6-seguimiento-anuncios--eatc_dona_lst-.png&ow=375&oh=2866, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fseguimiento-de-anuncios-eatc_dona_lst%2F2057546684-6-seguimiento-anuncios--eatc_dona_lst-.png&ow=375&oh=2866 
 EATCLOUD DONANTES 

 84.0000000000000 

 SEGUIMIENTO DE ANUNCIOS: (EATC_DONA_LST)