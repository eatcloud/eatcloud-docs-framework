# autenticación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Primero, se consulta con el login el "email" ejemplo : https://devdonantes.eatcloud.info/api/pruebaesp2/bo_usuarios?email=_* 

 Luego en un tester de php, se obtiene el hash 

 http://phptester.net/ 

 echo hash("sha384", " punto1pruebaesp2@prueba.es "); 

 Con ese se obtiene el password: 

 43e843a52a2a548a17adea0a5a3370e04b4d620310f6f1be01a8eb4be9aa1132b25f4eda4e42d66518725afa424b88b6 

 En resumen, el usuario es el "email " y el password es el "hash del email" 

 solo hay una excepcin en produccin para la cuenta "platostradicionales" est quemado el usuario y pass 

 $usuario = "platos"; 

 $pass = "n123"; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 AUTENTICACIN