# warning-automático.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema generar una alerta para anuncios generados desde ciertos puntos especficos, con informacin importante para la entrega de la donacin 
 Mecnica de la implementacin&#58; 
 El desarrollador debe definir la mecnica de implementacin idnea para esta nueva funcionalidad , que puede ser de dos maneras&#58; 
&#160; 
 Integrada con el proceso de Creacin de Encabezado de Anuncios de Donacin (tanto para anuncios por interfaz como servicio para creacin de estos encabezados a partir de la WAPP de donantes). 
 Proceso activado por cronjob para incorporar peridicamente dicho warning a los anuncios (el cronjob debe estar programado en una frecuencia muy corta para poder garantizar que rpidamente el warning se despliegue en el anuncio, puede ser en periodos de 5 minutos como mximo) 
&#160; 
 Generacin del warning automtico&#58; 
 El sistema debe evaluar por cada eatc_pod , si el mismo tiene un waring automtico programado, de la siguiente manera&#58; Cada anuncio, posee un eatc_pod_id y un eatc_donor, con estos datos se debe realizar una consulta de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_donor&#125;&#125;/eatc_pods_with_aut_warning?eatc-pod_id=&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125; 
&#160; 
 La consulta puede arrojar (en principio) un warning automtico (a futuro) o varios warnigs automticos, que debern llevarse al campo eatc-warning del encabezado de anuncio (conviviendo con la funcionalidad de warning por problemas en la entrega , de tal menera que si se generan dos o ms warnings, se deben mostrar ambos, es decir que la funcionalidad debe adicionar los textos del warning ms nuevo al warning ya existente) 
&#160; 
 Ejemplo 1 en entorno de pruebas 
 Para el anuncio cuyo cdigo es&#58; makroST0220200310082817270 y por lo tanto su eatc-pod_id es &quot; ST02 &quot; y su eatc_donor es &quot; makro &quot;, el sistema hace la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/makro/eatc_pods_with_aut_warning?eatc-pod_id= ST02 
&#160; 
 Como la consulta no arroja resultados, no se genera ningn warning. 
&#160; 
 Ejemplo 2 en entorno de pruebas 
 Para el anuncio cuyo cdigo es&#58; 00002009100022 y por lo tanto su eatc-pod_id es &quot; 22 &quot; y su eatc_donor es &quot; exito &quot;, el sistema hace la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods_with_aut_warning?eatc-pod_id= 22 
&#160; 
 Como el sistema arroja esta respuesta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;201008133148&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 res &#58;&#160; 
 [ 
 &#123; 
 _id &#58; &quot;2&quot;, 
 eatc-pod_id &#58; &quot;22&quot;, 
 eatc-pod_name &#58; &quot;CEDI ENVIGADO&quot;, 
 eatc-warning_code &#58; &quot;1&quot; 
 &#125; 
 ], 
 mem &#58; 0.39, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Esto quiere decir que a este anuncio se le debe incorporar un warning automtico como se indica a continuacin, tomando el eatc-warning_code (que para el ejemplo es &quot; 1 &quot;). 

&#160; 
 Incorporacin del warning automtico al la informacin de encabezado de donacin ***DINAMIZAR&#160; para mltiples cuentas maestras 
 Con el eatc-warning_code &#160; que se obtiene de la anterior consulta y el dato previamente obtenido de eatc_donor , se procede a realizar la consulta de la alerta a llevar a la informacin del encabezado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_donor &#125;&#125;/eatc_aut_warning?eatc-warning_code=&#123;&#123; eatc-warning_code &#125;&#125; 
&#160; 
 Tanto el ttulo como el cuerpo del mensaje se debern incorporar al anuncio en cuestin.&#160; La implementacin deber considerar un mecanismo para ir controlando sobre que encabezados de anuncios de donacin ya se hizo la operacin de generacin de warning automtico para no considerarlos en corridas sucesivas del proceso (dado el caso que esa sea la definicin de mtodo de implementacin ). 
&#160; 
 Para escribir el dato del warning se deber utilizar el servicio CRD respectivo, teniendo en cuenta la incorporacin en el mismo de cualquier Waring realizado con anterioridad (es decir la escritura no debe ser una mera edicin, sino que debe contener cualquier warning previo digitado por el usuario. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacin=update&amp;eatc-warning=&#123;&#123;[eatc_aut_warning.eatc-title]&#58; [eatc_aut_warning.eatc-warning] - [eatc_dona_headers.eatc-warning(anterior)&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc_dona_headers.eatc-code&#125;&#125; 

&#160; 
 Ejemplo ambiente de pruebas&#58; siguiendo con el ejemplo anterior &#58; 
&#160; 
 como eatc-warning_code es &quot; 1 &quot; y eatc_donor es &quot; exito &quot; la consulta que debe hacer el sistema para establecer el contenido de la alerta es&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ exito /eatc_aut_warning?eatc-warning_code= 1 &#160; 
&#160; 
&#160; 
 Dado que el anuncio en cuestin ( https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00002009100022 ) no posee una alerta previa (antes de realizar el presente ejemplo), el sistema debe escribir lo siguiente en el campo eatc-warning del encabezado de anuncio 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-warning=Atencin&#58;%20lea%20esto%20con%20detenimiento&#58;%20Si%20desean%20recoger%20este%20anuncio%20TODO%20el%20personal%20de%20recogida%20(incluyendo%20conductor)%20debe%20presentar%20EPS,%20ARL%20y%20Botas%20al%20ingresar%20a%20las%20instalaciones%20del%20punto%20de%20donacin.%20Verifica%20antes%20de%20salir%20el%20cumplimiento%20de%20estos%20requisitos&amp;WHEREeatc-code=00002009100022 &#160;&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 WARNING AUTOMTICO