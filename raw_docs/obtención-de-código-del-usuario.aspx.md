# obtención-de-código-del-usuario.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La aplicacin, deber obtener un identificador o cdigo para el usuario que la est accediendo (en principio de manera anmima) y que la pueda servir para enlazar las transacciones que este usuario (annimo en principio) realice, de tal manera que antes de solicitarle datos del registro, se pueda por ejemplo adicionar productos a un carro de compras, y luego obtener los dems datos del usuario, necesarios para cerrar la compra.&#160; Esta operacin se puede realizar de varias maneras, y por lo tanto se debe establecer cual es la mejor y ms conveniente en trminos de desarrollo y de integridad de datos.&#160; A continuacin se presentan varias opciones. 
&#160; 
 OBTENCIN DEL CDIGO DEL USUARIO 
 Obtencin del IMEI o el UUID del telfono 
 Esta informacin se puede obtener a travs de algn mtodo tcnico y no ser necesaria mucha interaccin con el usuario.&#160; Un buen ejemplo al respecto se puede tomar del onboarding de la aplicacin TikTok, que es reconocido en publicaciones como estas&#58; 
&#160; 
 https&#58;//pando.com/2020/06/12/rise-tiktok-and-understanding-its-parent-company-bytedance/ 
 https&#58;//www.zackhargett.com/tiktok/ 
&#160; 
 Como una prctica destacada de esta App y que genera poca friccin para enganchar al usuario&#58; 

 Nmero de telfono con validacin a travs de mensaje 
 Esta manera de identificar al usuario, tambin est muy difundida y se utiliza en apps como WhatsApp. Ella requiere interaccin con el usuario y envo de un cdigo de verificacin, por lo que se considera ms complicada de implementar que el anterior mtodo 

 Correo electrnico con validacin a travs de mensaje de e-mail 
 Esta manera de identificar al usuario, tambin es muy difundida como la anterior. Igualmente requiere interaccin con el usuario y envo de un correo electrnico, sumado que por lo general utilizar un cdigo que contenga una arroba puede ser problemtico para algunos sistemas, este mtodo se considera ms complicado que los dos anteriores y menos recomendado. 

 ALMACENAMIENTO DEL CDIGO DEL USUARIO 
 El cdigo obtenido por alguno de los mtodos anteriormente descritos, y con los datos de ubicacin obtenidos en la Consulta constante de datos de ubicacin (CIUDAD, DEPARTAMENTO y PAIS (cdigo de dos letras)), se procede a almacenar los datos del usuario de la siguiente manera&#58; 
&#160; 
 Primero se debe consultar si el usuario no existe, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_users? eatc-code =&#123;&#123;cdigo_obtenido&#125;&#125; 
&#160; 
 Si no se obtienen datos de la consulta se procede a crear el usuario utilizando el siguiente servicio. 
&#160; 
 &#123;&#123;Parmetros creacin en eatc_sale_users &#125;&#125;&#58; eatc-code =&#123;&#123;cdigo_obtenido&#125;&#125;&amp; eatc-creation_date =&#123;&#123;fecha actual en formato AAAA-MM-DD&#125;&#125;&amp; eatc-creation_datetime =&#123;&#123;fecha y hora actual en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125;&amp; eatc-state =anonimo&amp; eatc-token =&#123;&#123;token generado por el sistema y que servir para encriptar infrmacin personal&#125;&#125;&amp; eatc-city= &#123;&#123;CIUDAD desde la que ingresa el usuario&#125;&#125;&amp; eatc-province= &#123;&#123;PROVINCIA, departamento o estado desde el que ingresa el usuario&#125;&#125;&amp; eatc-country =&#123;&#123;Pas cdigo de dos letras&#125;&#125; 
&#160; 
 [***] Se guarda la informacin en el object store eatc_sale_users de la cuenta eatcloud&#58; 
&#160; 
 Mtodo POST&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_users&amp;_operacion=insert&amp; &#123;&#123;Parmetros creacin en eatc_sale_users &#125;&#125; 
&#160; 
 El eatc-user_code (el cdigo del usuario obtenido por la metodologa elegida para ello) tambin se debe guardar en una variable del dispositivo para tenerla disponible para otros procesos 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fobtenci%C3%B3n-de-c%C3%B3digo-del-usuario%2F3625634177-EmbeddedImage--83-.jpg&ow=1280&oh=574, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fobtenci%C3%B3n-de-c%C3%B3digo-del-usuario%2F3625634177-EmbeddedImage--83-.jpg&ow=1280&oh=574 
 App usuario final - Sale 

 782.000000000000 

 OBTENCIN DEL CDIGO DEL USUARIO