# Error-Handler.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Lineamientos principales&#58; 
&#160; 
Se debe desarrollar este servicio en modernización (utilizando node.js y sus frameworks, o procedimientos almacenados de base de datos), y procurando mucha eficiencia y performance en el desarrollo 

 Objetivo&#58; 
Desarrollar un servicio que corra de manera periódica en horario nocturno y que sirva para la información de las cuentas orígenes a la tabla “eatc_pod_tag_registry” a partir de la información del respectivo anuncio de donación referenciado por el eatc-id en cada registro de tag de calificación 
&#160; 
&#160; 
 Datos que debe recibir el servicio 
 cua_master 
 cua_user 
 _id 
&#160; 
 Consultas para correr el servicio y actualizar los datos&#58; 
Con la información de invocación del servicio, se realizan las siguientes operaciones 
Consulta de información del producto para actualizar en la donación 
El sistema realiza esta consulta&#58; 
 &#123;&#123;url_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_pod_tag_registry?_id= &#123;&#123;_id&#125;&#125; &amp;eatc_cua_origin=_vacio&amp;_cmp=eatc-dona_id 
Si no se reciben datos, o la respuesta es incorrecta, entonces, el servicio para y no sigue adelante con la actualización. Con el dato recibido en eatc_pod_tag_registry . eatc-dona_id el sistema realizará la siguiente consulta. 
&#160; 
 &#123;&#123;url_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_headers?eatc-id=&#123;&#123;eatc_pod_tag_registry . eatc-dona_id &#125;&#125;&amp;_cmp= eatc_cua_origin 
Con el dato recibido en eatc_dona_headers . eatc_cua_origin el sistema realiza la siguiente actualización de información en la tabla eatc_pod_tag_registry 
&#160; 
Actualización de información de la cuenta origen en el registro de tags de calificación 
El sistema realiza la siguiente actualización&#58; 
&#160; 
 &#123;&#123;url_donantes&#125;&#125; /crd/ &#123;&#123;cua_master&#125;&#125; /?_tabla=eatc_pod_tag_registry&amp;_operacion=update&amp; eatc_cua_origin =&#123;&#123;eatc_dona_headers . eatc_cua_origin &#125;&#125;&amp;WHERE_id= &#123;&#123;_id&#125;&#125; 
Una vez se realice la actualización, el servicio deberá contestar con un mensaje de éxito. 
&#160; 
Automatización del servicio&#58; 
El sistema deberá correr un proceso periódico en horario nocturno 
&#160; 
 Datos que debe recibir el servicio (para automatizar)&#58; 
Se propone que el servicio reciba como datos de entrada&#58; 

 cua_master 

 cua_user 

 fecha 
&#160; 
 Consultas para correr el servicio de automatización&#58; 
Con los datos entregados al invocar el servicio, se deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123;url_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_pod_tag_registry? date_time=&#123;&#123; fecha &#125;&#125; _lk &amp;eatc_cua_origin=_vacio &amp;_cmp= _id 
&#160; 
El servicio traerá un array de eatc_pod_tag_registry . _id , que debe colocarse en una cola de procesamiento, para con ese dato y los recibidos en 

 cua_master 

 cua_user 
&#160; 
Realizar el llamado del servicio y paulatinamente ir realizando, de manera asincrónica, la actualización de la información (o mirar si se pueden realizar llamados en paralelo del servicio para actualizar varios eatc_pod_tag_registry. eatc_cua_origin al tiempo y obtener mejor performance. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 Error Handler eatc_cua_origin en eatc_pod_tag_registry a partir de información registrada en eatc_dona_headers