# QR-WEB--Nuestro-impacto-en-números.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Solo para cuentas_usuario y pods_typolgy_a que tengan registro en la persistencia del cabezote principal, funcionará esta sección, de tal manera que una cua_user que por ejemplo no tenga un registro de cabezote, tampoco se le generará la información de nuestro impacto en números (esto con el ánimo de controlar las cua_user que tienen acceso a esta funcionalidad 

Título&#58; &#160;Nuestro impacto en números. 
Centrado, tal cómo se ve en el diseño 
&#160; 
Selector de fechas (no está en el diseño) 
Abajo del título debe existir un selector de fechas inicial y final que se muestre al interior de una leyenda &quot;del &#123;&#123;fecha_inicial&#125;&#125; al &#123;&#123;fecha_final&#125;&#125; 
&#160; 
 &#123;&#123;fecha_inicial&#125;&#125; 

 Valor por defecto &#58; primer día del año en curso 

 Formato de input &#58; date picker 

 Formato de la fecha &#58; AAAA-MM-DD 
 &#123;&#123;fecha_inicial&#125;&#125; 

 Valor por defecto &#58; fecha del día anterior al actual 

 Formato de input &#58; date picker 

 Formato de la fecha &#58; AAAA-MM-DD 
&#160; 
Consultas para construir los indicadores&#58; 
Tomando los parámetros que llegan por la URL&#160; 

 &#123;&#123;cua_master&#125;&#125; 

 &#123;&#123;cua_user&#125;&#125; 

 &#123;&#123;pod_typology_a&#125;&#125; (que puede llegar o no en la URL. &#160;Cuando no llega en las consultas se obvia el parámetro eatc-pod_typology_a ) 
&#160; 
Y las fechas del selector de fechas anteriormente descrito 

 &#123;&#123;fecha_inicial&#125;&#125; 

 &#123;&#123;fecha_final&#125;&#125; 
&#160; 
El sistema deberá realizar las siguientes consultas para obtener los datos que se utilizarán para obtener y calcular los indicadores que inicialmente se definieron&#58; 
&#160; 
Consulta para obtener los Kilogramos donados 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;KG_donados&#125;&#125; =&#123;&#123;url_entorno_donantes&#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_headers?eatc-donor= &#123;&#123;cua_user&#125;&#125; &amp;eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125; &amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-pod_typology_a= &#123;&#123;pod_typology_a&#125;&#125; &amp;_sum= eatc-total_weight_kg&#160; 
&#160; 
Consulta para obtener las organizaciones beneficiadas 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;org_beneficiadas&#125;&#125; =&#123;&#123;url_entorno_donantes&#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_headers?eatc-donor= &#123; &#123;cua_user&#125;&#125; &amp;eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125; &amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-pod_typology_a= &#123;&#123;pod_typology_a&#125;&#125; &amp;_distinct= eatc-donation_manager_name 
 El cont de la respuesta corresponderá al número de las organizaciones atendidas. 
&#160; 

Construcción de indicadores 

[Icono] 
 &#123;&#123;KG_donados&#125;&#125; 
Kilogramos donados 
Alimentos que han llegado a quienes más lo necesitan. (en un tooltip colocar&#58; kilogramos totales de donaciones en estado “entregado”, “recibido”, “pre-certificado” y “certificado” (no está en el diseño) ) 
&#160; 
&#160; 

[Icono] 
 &#123;&#123;KG_donados&#125;&#125;*636,9825361 
Huella hídrica (litros) * difiere del diseño 
Agua ahorrada gracias a la reducción de desperdicios (en un tooltip colocar&#58; Estimación realizada a partir de los kilogramos totales de donaciones en estado “entregado”, “recibido”, “pre-certificado” y “certificado” (no está en el diseño) ) 
&#160; 
&#160; 

[Icono] 
 &#123;&#123;KG_donados&#125;&#125;*2,435793924 
CO2 mitigado (kg) 
Emisiones evitadas al reducir desperdicios alimentarios ( en un tooltip colocar&#58; Estimación realizada a partir de los kilogramos totales de donaciones en estado “entregado”, “recibido”, “pre-certificado” y “certificado” (no está en el diseño) ) 
&#160; 
&#160; 

[Icono] 
 &#123;&#123;org_beneficiadas&#125;&#125; 
Organizaciones beneficiadas 
Aliados que nos ayudan a multiplicar nuestro impacto &#160;( en un tooltip colocar&#58; organizaciones que gestionaron en el periodo de tiempo donaciones en estado “entregado”, “recibido”, “pre-certificado” y “certificado” (no está en el diseño) ) 
&#160; 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=edfa0253b6f1409fa91008498864b825&ext=png&ow=434&oh=306, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=edfa0253b6f1409fa91008498864b825&ext=png&ow=434&oh=306 

 1038.00000000000 
 58322fd5-8bf8-4be0-a574-f65829c778bf 
 1!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 77672aec-d3c6-45b8-a9c6-06a86b6a93c4 
 2025-08-01T04:44:57.7064232Z 

 {"SessionId":"69698749-7729-45e5-a9f0-727df06432e5","SequenceId":7254,"FluidContainerCustomId":"6bf555ed-bc85-45fc-9b5b-d31ad34d41c9","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 QR WEB: Nuestro impacto en números