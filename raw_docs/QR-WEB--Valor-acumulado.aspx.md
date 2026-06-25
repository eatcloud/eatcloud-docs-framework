# QR-WEB--Valor-acumulado.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Solo para cuentas_usuario y pods_typolgy_a que tengan registro en la persistencia del cabezote principal, funcionará esta sección, de tal manera que una cua_user que por ejemplo no tenga un registro de cabezote, tampoco se le generará la información de Valor acumulado (esto con el ánimo de controlar las cua_user que tienen acceso a esta funcionalidad 

Título&#58; &#160;Valor aculumado. 
Centrado, tal cómo se ve en el diseño 
&#160; 
Selector de fechas (no está en el diseño, y no estará presente aquí, pero le aplica para cálculos) 
Le aplicarán los mismos selectores de fechas que aplican para la sección&#58; Nuestro Impacto en Números . 
&#160; 
Consultas para construir el indicador&#58; 
Tomando los parámetros que llegan por la URL&#160; 

 &#123;&#123;cua_master&#125;&#125; 

 &#123;&#123;cua_user&#125;&#125; 

 &#123;&#123;pod_typology_a&#125;&#125; (que puede llegar o no en la URL. &#160;Cuando no llega en las consultas se obvia el parámetro eatc-pod_typology_a ) 
&#160; 
Y las fechas del selector de fechas anteriormente descrito 

 &#123;&#123;fecha_inicial&#125;&#125; 

 &#123;&#123;fecha_final&#125;&#125; 
&#160; 
El sistema deberá realizar las siguientes consultas para obtener los datos que se utilizarán para obtener y calcular el indicador&#58; 
&#160; 
&#160; 
Consulta para obtener el costo de las donaciones 
El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;costo_donaciones&#125;&#125; = &#123;&#123;url_entorno_donantes&#125;&#125;/api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona_headers?eatc-donor= &#123; &#123;cua_user&#125;&#125; &amp;eatc-publication_date[0]= &#123;&#123;fecha_inicial&#125;&#125; &amp;eatc-publication_date[1]= &#123;&#123;fecha_final&#125;&#125; &amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-pod_typology_a= &#123;&#123;pod_typology_a&#125;&#125; &amp;_sum= eatc-total_cost 
Consulta para obtener el impacto económico de los programas 
El sistema realizará una consulta al repositorio de los programas de impacto social , con el ánimo de obtener la sumatoria de los valores de “ economic_impact ” 

Construcción de indicadores 

Valor acumulado 
Impacto económico de nuestras donaciones y programas sociales 
&#160; 
 &#123;&#123;costo_donaciones&#125;&#125; &#160;+ sumatoria economic_impact 
&#160; 
&#160; 
Valor económico generado a través de nuestras iniciativas sociales. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=a7d4f52e0c8c4c33ad9eaf1fc0132e19&ext=png&ow=1248&oh=400, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=a7d4f52e0c8c4c33ad9eaf1fc0132e19&ext=png&ow=1248&oh=400 

 1058.00000000000 
 1a771a28-a151-40e4-b2c3-b19be38df49c 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 136c788e-d18e-49ba-89a5-03f8464281f7 
 2025-08-01T04:34:29.6992155Z 

 {"SessionId":"c9d103ad-1658-4330-868b-bdd27938e041","SequenceId":1860,"FluidContainerCustomId":"b51a1a2d-6548-4042-b3f4-9bbedf672811","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 QR WEB: Valor acumulado