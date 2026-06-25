# descarga-tus-puntos-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descarga de un archivo csv con los puntos de donacin de la cuenta respectiva 

 Funcionalidad disponible solo para usuarios superadmin 
 Solo los usuarios con perfil de superadmin ( tipo= A ) 
&#160; 
 Label Botn Men&#58; 
 lbl_descarga_pods (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_descarga_pods )&#160; 
&#160; 
 Label Ttulo de la Vista&#58; 
 lbl_descarga_pods (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_descarga_pods )&#160; 
&#160; 
 Label Descripcin de la Vista&#58; 
 lbl_descarga_pods_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_descarga_pods_desc ) 
&#160; 
 Con esta funcionalidad podrs descargar un archivo plano con la informacin relevante te tus puntos de donacin.&#160; La misma no contendr los passwords, dado que nosotros no almacenamos dicha informacin. 
&#160; 
 Label Botn de descarga&#58; 
 lbl_btn_descarga_pods ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_btn_descarga_pods )&#160; 
&#160; 
 Al accionar el botn de descarga, el sistema deber realizar una accin similar a la que se realiza mediante la siguiente URL 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?_id=_*&amp;_csv 
&#160; 
 Con dos ajustes importantes&#58; 

&#160; 

 El archivo no contendr la informacin de los passwords 
 Se podr , bien sea eliminar esa columna en la descarga o simplemente dejarla pero sin informacin. 

&#160; 

 El archivo contendr la informacin de la columna &quot; eatc_active &quot; que el respectivo punto de donacin tiene en allpods 
 Se deber incorporar en la descarga, para cada punto de donacin, la informacin que contine para dicho punto, la columna &quot;&quot; que contiene la tabla &quot;&quot;,&#160; para indicarle al usuario si el punto est activo o inactivo 

 Cuando no hay registros en el respectivo repositorio de puntos de donacin 
 El sistema debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?_id=_* 
&#160; 
 Si la misma no trae datos se debe mostrar el siguiente anuncio 
 lbl_descarga_pods_sin_datos ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_descarga_pods_sin_datos )&#160; 
&#160; 
 No tienes puntos de donacin registrados en nuestro sistema 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Cuentas datagov 

 DESCARGA TUS PUNTOS DE DONACIN