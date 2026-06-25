# informe-de-excepciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Este informe presenta consulta de las novedades de los anuncios de donacin, para un rango de fechas especfico (el valor por defecto del rango de fechas al presentar el informe debe ser el da actual) y funcionalidades propias de &quot;data-tables&quot; (exportacin a excel, csv, filtros, ordenamientos, etc), para el punto de donacin respectivo. 
&#160; 
 Este informe debe ser accedido desde un botn en el men lateral izquierdo (abajo del vnculo al informe operativo de donaciones y encima del botn salir) 

 ***Revisar dinamismo a partir de _DOM.cua_master de la consulta para generar el informe*** 
 Se debe generar mediante una consulta al registro de novedades ( eatc_odd_rejection_registry ) el punto de donacin en particular. 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_master&#125;&#125; /eatc_odd_rejection_registry?eatc-pod_id=&#123;&#123;eatc-pod_id&#125;&#125; 

&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; ambiente productivo 
&#160; 
 Para el punto de donacin xito de San Antonio cuyo cdigo es 39 ( eatc-pod_id), el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
 NOTA &#58; tener en cuenta la variable DOM en la implementacin para la primera parte de los llamados a las APIs 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-pod_id=39 &#160; 
&#160; 
 Si la consulta por algn motivo no arroja resultados, se debe informar de esto mediante un mensaje que salga en la pantalla 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finforme-de-excepciones%2F3915983518-EmbeddedImage--1-.png&ow=1024&oh=768, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finforme-de-excepciones%2F3915983518-EmbeddedImage--1-.png&ow=1024&oh=768 

 112.000000000000 

 INFORME DE EXCEPCIONES (WEB APP DONANTES)