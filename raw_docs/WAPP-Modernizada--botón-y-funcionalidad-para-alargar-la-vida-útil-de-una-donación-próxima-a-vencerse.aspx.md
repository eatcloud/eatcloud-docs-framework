# WAPP-Modernizada--botón-y-funcionalidad-para-alargar-la-vida-útil-de-una-donación-próxima-a-vencerse.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 Se ha solicitado una funcionalidad que le permita alargar la vida útil a una donación y para ello se ha documentado un servicio ( API Pública ) que permitirá realizar dicha operación. 
&#160; 
 Esta funcionalidad se desplegará solamente para aquellas donaciones en estado “announced” que están próximas a cancelarse (a dos horas o menos), y capturará información en días de alargue, que deberá transformar a horas para invocar el servicio &#160;( API Pública )&#160;que se desarrollará para tal fin. 
&#160; 
 Por lo tanto a continuación se documentan las condiciones para desplegar el botón (que debería estar presente tanto en la card de la donación en los diferentes listados de la WAPP, como en el dashboard o detalle de la donación), y cómo operaría la funcionalidad para invocar el servicio. 
 Condiciones para desplegar el botón “Alargar vida útil a la donación” 
Se deberán cumplir dos condiciones para desplegar el botón “Alargar vida útil a la donación”, tanto en la card de la misma en diversos listados de la WAPP, como al interior de la misma (cuando se ingresa para ver sus detalles). 

Solo se desplegará en donaciones en estado “Anunciado” (eatc-state=announced). 

Solo se desplegará máximo dos horas antes de la fecha de cancelación de la donación&#58; &#160;para hacer esto el sistema deberá tomar la fecha y hora actual y realizar la siguiente comparación con respecto a la fecha y hora de cancelación de la donación (eatc_dona_headers. eatc-cancellation_datetime ). 
 (&#123;&#123; eatc_dona_headers. eatc-cancellation_datetime &#125;&#125; -&#160; 2 horas ) =&lt; &#123;&#123;fecha_hora_actual&#125;&#125; =&lt; &#123;&#123; eatc_dona_headers. eatc-cancellation_datetime &#125;&#125;&#160; 
Si la fecha y hora actual no está en ese rango de tiempo el botón no se puede desplegar. 
 Funcionalidad “Alargar la vida útil de la donación” (que se desplegará al presionar el botón) 
El sistema deberá desplegar un formulario en donde existan los siguientes campos de captura. 
Selector de días de alargue de la donación 
Su valor por defecto será 1 día, y deberá mostrar las opciones de 1, 5, 10 y &#160;14 días. &#160;Será un campo de captura obligatorio. &#160;El dato que se tome deberá multiplicarse por 24 para invocar el servicio, ya que el mismo recibe valores en horas. 
&#160; 
Causa por la cual se libera 
Inicialmente se propone un campo de captura de línea de texto, que pueda ser llenado libremente. &#160;En una segunda etapa se podrá construir un maestro para llenar este selector. &#160;Inicialmente &#160;será un campo opcional (con miras a volverlo obligatorio) 
&#160; 
&#160; 
 Invocación API pública “Alargar la vida útil de la donación” 
 Con los datos obtenidos en la funcionalidad anterior, y otros datos propios del POD y de la donación (como su código) se debe invocar el API, enviando los parámetros que constan en su documentación ( Parámetros del body de la petición ). 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 1101.00000000000 
 50898fc2-ef4f-4813-9925-f7f01f226f78 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 c799892e-307e-485d-984b-ca41b97bbbb3 
 2025-09-05T05:49:17.3098103Z 

 {"SessionId":"1ae3b2aa-d0c7-4584-9c1d-abbcaae6ef9a","SequenceId":6215,"FluidContainerCustomId":"d21f335b-4e81-4245-85e4-f750686569af","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: botón y funcionalidad para alargar la vida útil de una donación próxima a vencerse