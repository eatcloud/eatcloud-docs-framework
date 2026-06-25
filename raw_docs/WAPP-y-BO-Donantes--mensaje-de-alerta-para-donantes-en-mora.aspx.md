# WAPP-y-BO-Donantes--mensaje-de-alerta-para-donantes-en-mora.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 Se deberá implementar un mensaje, en la parte superior de la interfaz gráfica de la WAPP y el BO Donantes en donde se informe del estado pendiente de facturación. 
&#160; 
 Dicha implementación se guiará por este diseño&#58; https&#58;//www.figma.com/design/fz65QCafGLQOjca5ShRzTc/Nubola-Design-System?node-id=2606-2245&amp;t=13f4kboyf4CbsvAh-0 &#160; 
&#160; 
Y las siguientes consultas para determinar, cuándo se despliega el mensaje. &#160; 
&#160; 
 Nota importante&#58; Cabe destacar que se crearon dos estructuras de datos Legacy para esto, y que también hay una automatización diseñada para ingresar la información a la estructura que sirve para determinar a cuál cua_user se le debe mostrar el mensaje . &#160;Por lo tanto no se recomienda “modernizar” dichas estructuras y de ser absolutamente necesario, se debe conservar la misma estructura presente en legacy y avisar a Juan Correa para ajustar las automatizaciones creadas. 
 Consulta para establecer a cual cua_user se le despliega el mensaje 
El sistema deberá realizar esta consulta para determinar si la cua_user en cuestión (bien sea de los diversos usuarios de la WAPP, o de su respectivo BO), se le debe desplegar un mensaje&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ customer_warning_cua ?cua= &#123;&#123;cua_user&#125;&#125; &amp;estado= vigente &amp;_cmp= categoria 
&#160; 
Si la consulta no trae resultados, entonces no se despliega el mensaje. 
&#160; 
Si la consulta arroja un resultado entonces, a partir de la respuesta recibida en la anterior consulta, el sistema realiza la siguiente consulta&#58; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/ customer_warning_messages?categoria=&#123;&#123; customer_warning_cua. categoria&#125;&#125; &amp;_cmp= mensaje,color 
&#160; 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 14984050-c3b3-4ff1-900d-3369c9f385c9 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 41e58ff1-ca6c-42ca-b336-cce949f04b84 
 2026-01-07T06:24:30.5473516Z 

 {"SessionId":"1e076dcd-bb76-44ac-92ce-71d929fb3a37","SequenceId":3528,"FluidContainerCustomId":"45f17ec9-c9ff-4e86-a221-e46f8c34e44d","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP y BO Donantes: mensaje de alerta para donantes en mora