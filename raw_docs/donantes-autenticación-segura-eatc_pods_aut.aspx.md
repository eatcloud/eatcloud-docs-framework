# donantes-autenticación-segura-eatc_pods_aut.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 Se realizar autenticacin por punto de donacin ( eatc_pods ), es decir cada punto de donacin se autentica con los datos que reposan en el maestro respectivo 

 Metodologa de autenticacin 
 API de consulta&#58; ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?_campos 
 API de consulta&#58; ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?_campos 
 Usuarios (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=_* 
 Usuarios&#160; (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=_* 

&#160; 
 El usuario digita en el campo &quot;nombre de usuario&quot; su &quot;eatc-id&quot; (que corresponde al &quot;id&quot; del punto de donacin)&#160; y en el campo &quot;contrasea&quot; su &quot;eatc-phone&quot; (que corresponde al &quot;telfono&quot; del punto de donacin) . Con estos datos debe utilizar el API respectiva y realizar la siguiente consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/[cua]/eatc_pods?eatc-id=[valor]&amp;eatc-phone=[valor] 

 Ejemplo&#58; 
 Para el punto de donacin &quot;EXITO SAN ANTONIO&quot;, cuyo &quot;eatc-id&quot; = 39 y eatc-phone= (4) 6050372 , la consulta sera para una autenticacin correcta&#58; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=39&amp;eatc-phone=(4)%206050372 
&#160; 
 trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=39&amp;eatc-phone=(4)%206050372&amp;_compress &#160; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39&amp;eatc-phone=(4) 6050372 
&#160; 
 trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39&amp;eatc-phone=(4) 6050372&amp;_compress &#160; 

 Registro de fecha y hora de login 
 Cuando se realiza el login del usuario el sistema realiza un registro de la fecha y hora del login en formato AAAA-MM-DD%20HH&#58;MM&#58;SS en el object store eatc_pods_login_history de la cuenta respectiva (timestamp). En dicho repositorio se guarda el eatc_pods. _id &#160; en el campo eatc-pod_id de eatc_pods_login_history (se deja a eleccin del desarrollador si se lleva en ltimas el _id (como se dise originalmente el objectstore para que fuera muy semntico)&#160; o si se prefiere llevar el eatc-id ). 
&#160; 
 El llamado de creacin sera el siguiente&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;CUA_user&#125;&#125;/?_tabla=eatc_pods_login_history&amp;_operacion=insert&amp;eatc-pod_id=[_id]&amp;eatc-login_datetime=[AAAA-MM-DD%20HH&#58;MM&#58;SS] 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-autenticaci%C3%B3n-segura-eatc_pods_aut%2F595002%20login%20%28eatc_pods_aut%29_.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonantes-autenticaci%C3%B3n-segura-eatc_pods_aut%2F595002%20login%20%28eatc_pods_aut%29_.png 
 EatCloud Donantes 

 46.0000000000000 

 AUTENTICACIN SEGURA: EATC_PODS_AUT