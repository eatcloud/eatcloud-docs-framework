# incorporación-eatc_cua_master-en-allpods-eatc_pods.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Tomando los datos del eatc_pods y eatc_cua realizar una rutina peridica que revise si hay un registro vlido en&#160; 
 https&#58;//donantes.eatcloud.info/api/ all pods/eatc_pods? _id =_* &amp;_distinct= eatc_cua_master 
&#160; 
 Nota&#58; 
 &#160;El campo no est creado en la tabla allpods/eatc_pods. eatc_cua_master por lo tanto se debe crear en ambos ambientes. 

&#160; 
 Si no tiene un dato vlido para un eatc_pods- _id en particular, el sistema debe realizar una rutina peridica que incorpore las siguientes tareas&#58; 
&#160; 
 1. Determinacin del cuenta del punto de donacin, para a partir del mismo consultar su cuenta maestra&#58; 
 Se toma el dato allpods /eatc_pods. eatc_cua (que corresponde a la cuenta usuario (o &#123;&#123;_DOM. cua_user &#125;&#125; ) de cada punto en allpods ) para con dicho dato consultar la cuenta maestra respectiva en el maestro eatcloud/eatc_cua 
&#160; 
 La consulta debe ser similar a la siguiente&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123; allpods /eatc_pods. eatc_cua &#125;&#125;&amp;_distinct= eatc_cua_master 
&#160; 
 Con el dato obtenido se realiza el siguiente proceso 
&#160; 
 2. Escritura del dato de cuenta maestra obtenido en la estructura allpods/eatc_pods 
 Con el dato obtenido en la consulta anterior&#160; (en adelante eatc_cua. eatc_cua_master ) 
&#160; 
 El sistema debe tomar llamar al servicio para incertarlo en el respectivo registro. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/allpods/?_tabla=eatc_pods&amp;_operacion=update&amp; eatc_cua_master =&#123;&#123; eatc_cua. eatc_cua_master &#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_pods._id&#125;&#125; 

&#160; 
 3. incorporacin del dato eatc_pods. eatc_cua_master en el proceso que lleva datos de &#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods a allpods/eatc_pods 
&#160; 
 Se deber intervenir el proceso que escribe en allpods /eatc_pods a partir de un registro en &#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods &#160; para que desde la fuente incorpore el nuevo dato eatc_pods. eatc_cua_master 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 INCORPORACIN EATC_CUA_MASTER EN ALLPODS / EATC_PODS