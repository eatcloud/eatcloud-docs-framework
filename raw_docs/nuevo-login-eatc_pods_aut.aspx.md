# nuevo-login-eatc_pods_aut.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo&#58;&#160; 
 http&#58;//repograf.eatcloud.info/login.html &#160; 

 Etiquetas&#58; 
&#160; 
 Inicio de sesin de punto de donacin 
 class=&quot;lbl_inicio_sesion_pod&quot; 
&#160; 
 Nombre de usuario o email 
 class=&quot;lbl_nombre_usuario&quot; 
&#160; 
 Contrasea 
 class=&quot;lbl_password&quot; 
&#160; 
 Olvidaste tu contrasea? 
 class=&quot; lbl_recuperar_pasword &quot; 
&#160; 
 Iniciar sesin 
 id=&quot; login_btn &quot; 

 Descripcin general 

 El funcionamiento del login ser similar al implementado hasta el momento, con una mejora de usabilidad&#58; 
&#160; 
 URL nica de login 
 La idea con esta implementacin es que todos los usuarios de EatCloud, siempre tengan una sola puerta de entrada a la plataforma y que se asocien los datos de login a una cuenta maestra y cuenta usuario, para as poder validarlos con el object_store respectivo. 
&#160; 
 Se deber implementar la URL nica de login&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/pod/login 
&#160; 
 En dnde la primera vez que se ingrese , una vez se tomen los datos de usuario y contrasea (guardndolos en variables temporales &#123;&#123;usuario&#125;&#125; y &#123;&#123;password&#125;&#125; ) se realicen dos procesos de obtencin de datos&#58; 
&#160; 
 Obtencin de la cuenta maestra 
 De manera similar a como se implement la obtencin de la cuenta maestra en la App Beneficiarios , el sistema a partir de la ubicacin del browser, establecer la cuenta maestra a la que se pertenece quien est intentando ingresar (para guardarla en una variable global asociada a los datos de login previamente capturadas y que pueda recuperarse cuando el usuario entre por segunda vez).&#160; La cuenta maestra obtenida se almacena en una variable global&#160; 
 &#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Se debe evaluar la creacin de una persistencia general (puede ser en datagov.eatcloud.info/api/eatcloud/eatc_login_cua por ejemplo o utilizar la ya creada&#58; https&#58;//donantes.eatcloud.info/api/ all pods/eatc_pods?_id=_* ) para guardar la cuenta maestra ( &#123;&#123;_DOM. cua_master &#125;&#125; ) asociada a los datos de logueo previamente obtenidos ( &#123;&#123;usuario&#125;&#125; y &#123;&#123;password&#125;&#125; ) 
&#160; 
 Obtencin de la cuenta usuario 
 Tambin la primera vez que se ingrese se deber preguntar la cuenta usuario a la que pertenece el punto de donacin que est ingresando puede de la siguiente manera&#58; 
&#160; 
 Digita por favor el nombre de tu cuenta 
 class=&quot;lbl_digitar_cua_user&quot; 
&#160; 
 Descripcin 
 class=&quot;lbl_digitar_cua_user_desc&quot; 
&#160; 
 Debajo del anterior label, se coloca la siguiente descripcin 
 &quot; El nombre de tu cuenta est compuesto por una palabra o abreviatura, que en el momento del registro se utiliz para identificar de manera nica a la empresa o institucin donante que acoge diferentes puntos de donacin (ejemplo&#58; &quot;exito&quot;, &quot;alqueria&quot;, &quot;aco&quot;, etc.) &quot; 
&#160; 
 Campo de texto para ingreso del nombre de la cuenta usuario&#160; 
 El sistema proveer un campo de texto en donde el usuario podr ingresar un nombre de cuenta. El sistema deber validar que el &#123;&#123;input&#125;&#125; del campo de texto, sea una cuenta vlida, mediante la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;input&#125;&#125; 
&#160; 
 Si la cuenta no es vlida se debe presentar la siguiente label&#58; 
 class=&quot;lbl_cua_invalida&quot; 
 &quot; El nombre de la cuenta ingresado es incorrecto, por favor intenta de nuevo &quot; 
&#160; 
 Si la cuenta es correcta se deber colocar un mensaje de confirmacin (compuesto de una etiqueta, una variable y luego otra etiqueta) de la siguiente manera&#58; 
&#160; 
 Primera etiqueta&#58; 
 class=&quot;lbl_estas_tratando_de_ingresar&quot; 
 &quot; Ests tratando de ingresar a la cuenta &quot; 
&#160; 
 Variable 
 &#123;&#123;eatc_cua. name &#125;&#125; 
&#160; 
 Segunda etiqueta&#58; 
 class=&quot;lbl_estas_seguro_cua&quot; 
 &quot; ests seguro &quot; 
&#160; 
 Botn&#58; NO 
 class=&quot;lbl_no&quot; 
&#160; 
 Al oprimirlo, el sistema vuelve a desplegar el campo de captura del nombre de la cuenta usuario . 
&#160; 
 Botn&#58; SI 
 class=&quot;lbl_si&quot; 
&#160; 
 La cuenta usuario obtenida se almacena en una variable global&#160; 
 &#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Se debe evaluar la creacin de una persistencia general (puede ser en datagov.eatcloud.info/api/eatcloud/eatc_login_cua por ejemplo) para guardar la cuenta maestra ( &#123;&#123;_DOM. cua_user &#125;&#125; ) asociada a los datos de logueo previamente obtenidos ( &#123;&#123;usuario&#125;&#125; y &#123;&#123;password&#125;&#125; ) 

&#160; 
 La segunda vez que el mismo usuario ingrese, se deben recuperar los datos previamente ingresados y una vez el usuario ingrese a&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/pod/login 
&#160; 
 El sistema debe redireccionar al login respectivo (cmo ha funcionado hasta ahora) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/apl/ &#123;&#123;_DOM. cua_master &#125;&#125;/&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 La metodologa de autenticacin a partir de este punto ser similar a la desarrollada para la primera versin de la WAPP donantes. 

 Metodologa de autenticacin 
 API de consulta&#58; ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?_campos 
 API de consulta&#58; ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?_campos 
 Usuarios (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=_* 
 Usuarios&#160; (eatc_pods) disponibles ambiente de pruebas&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=_* 

&#160; 
 El usuario digita en el campo &quot;nombre de usuario&quot; su &quot;eatc-id&quot; (que corresponde al &quot;id&quot; del punto de donacin)&#160; y en el campo &quot;contrasea&quot; su &quot;eatc-phone&quot; (que corresponde al &quot;telfono&quot; del punto de donacin) . Con estos datos debe utilizar el API respectiva y realizar la siguiente consulta&#58; 
&#160; 
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
 https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;CUA_user&#125;&#125;/?_tabla=eatc_pods_login_history&amp;_operacion=insert&amp;eatc-pod_id=[_id]&amp;eatc-login_datetime=[AAAA-MM-DD%20HH&#58;MM&#58;SS] 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EATCLOUD DONANTES 

 NUEVO: LOGIN (EATC_PODS_AUT)