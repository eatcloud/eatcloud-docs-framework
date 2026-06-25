# donantes-autenticacion-segura-eat_pods_aut_r.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 Se realizar autenticacin por punto de donacin ( eatc_pods ), es decir cada punto de donacin se autentica con los datos que reposan en el maestro respectivo 

 Metodologa de autenticacin 
 API de consulta&#58; ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?_campos 
&#160; 
 API de consulta&#58; ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?_campos 
&#160; 
 Usuarios (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=_* 
&#160; 
 Usuarios (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=_* 

&#160; 

 El usuario digita en el campo &quot;nombre de usuario&quot; su &quot;eatc-id&quot; (que corresponde al &quot;id&quot; del punto de donacin) y en el campo &quot;contrasea&quot; su &quot;eatc-phone&quot; (que corresponde al &quot;telfono&quot; del punto de donacin) . Con estos datos debe utilizar el API respectiva y realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/[cua]/eatc_pods?eatc-id=[valor]&amp;eatc-phone=[valor] 
 Ejemplo&#58; 
 Para el punto de donacin &quot;EXITO SAN ANTONIO&quot;, cuyo &quot;eatc-id&quot; = 39 y eatc-phone= (4) 6050372 , la consulta sera para una autenticacin correcta&#58; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=39&amp;eatc-phone=(4)%206050372 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39&amp;eatc-phone=(4) 6050372 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-autenticacion-segura-eat_pods_aut_r%2F194411%2520Login%2520%28eatc_pods_aut_r%29.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-autenticacion-segura-eat_pods_aut_r%2F194411%2520Login%2520%28eatc_pods_aut_r%29.png 
 EatCloud Donantes Desktop 

 51.0000000000000 

 AUTENTICACIN SEGURA: EATC_PODS_AUT