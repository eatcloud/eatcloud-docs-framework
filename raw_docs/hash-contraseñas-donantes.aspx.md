# hash-contraseñas-donantes.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando se creen eatc_pods de manera manual, se deber correr sobre el objectstore particular el siguiente query a fin de hashear las contraseas (a partir del 2020-04-16 en horas de la noche) 

 UPDATE eatc_pods SET `password`= SHA2(`password`, 384) WHERE LENGTH(`password`) &lt; 96; 

 Script&#58; 
 https&#58;//paiza.io/projects/DhCGotqtnBULqaQCxusdiA &#160; 
&#160; 
 Proceso por URL 
&#160; 
 Se disponen de las siguientes URLs para realizar el proceso&#58; 
&#160; 
https&#58;//donantes.eatcloud.info/hpass/&#123;&#123; cua &#125;&#125; 
https&#58;//devdonantes.eatcloud.info/hpass/&#123;&#123; cua &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 HASH CONTRASEA DONANTES