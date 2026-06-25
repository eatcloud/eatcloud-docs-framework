# slides-introductorios-eatcloud-donantes.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Cuando se identifica que un usuario est entrando por primera vez a la plataforma, se deber desplegar unos slides introductorios que le muestren al usuario como realizar las principales tareas en la APP (informacin similar a la que se muestra aqu&#58; https&#58;//www.eatcloud.com/donantes-inscritos/ ) de una manera rpida y fcil de entender y aplicar. 

 Identificacin del usuario que entra por primera vez&#58; 
 Para establecer si un usuario ha entrado o no por primera vez, se realiza una consulta al API de la siguiente manera&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; cua_user &#125;&#125;/eatc_pods_login_history?eatc-pod_id=&#123;&#123; eatc_pods._id &#125;&#125;&amp;_compress 
&#160; 
 Si la respuesta tiene cont&#58; 0&#160; y err_msg&#58; como por ejemplo&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;200420154710&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.29, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Esto quiere decir que el punto de donacin no ha ingresado a la plataforma, por lo tanto se le debe desplegar los Slides introductorios. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SLIDES INTRODUCTORIOS EATCLOUD DONANTES