# splash-screen-y-bienvenida-sale.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 &#160; (splscr, eatc_sale_bienv1 (eatc_alim_bienv1), eatc_sale_bienv2 (eatc_alim_bienv2)) 

 Splash Screen 
 Diseño&#58; 
 https&#58;//zeroheight.com/6217d62d5/p/24da03-splash-screen-mobile/b/64c81a 

 Descripción&#58; 
 Muestra la imagen del splash screen. 
&#160; 
 Al ingresar la App debe solicitar el permiso de acceder a la ubicación del dispositivo, con el ánimo de poder obtener en este punto el país (código de dos caracteres) desde el cual se ingresa, lo cual se utilizará para la consulta de los mensajes de onboarding. 

 Onboarding&#58; 
 Diseño&#58; 
 https&#58;//zeroheight.com/6217d62d5/p/02efcc-bienvenida-al-usuario/b/926928 
&#160; 
 Descripción técnica&#58; 
 El onboarding, compuesto por tres mensajes que se dispondrán en secuencia, se deberá presentar la primera vez que el usuario ingresa a la app.&#160; Por lo tanto cuando se realice este ingreso por primera vez, la app deberá guardar una variable de control que permita establecer si el usuario está ingresando por primera vez (cuando esa variable no exista) y en consecuencia se muestre el onboarding, o si no es la primera vez que ingresa (first_admision) (cuando la variable está almacenada) y por lo tanto no se le despliega el onboarding. 
&#160; 
 El título, la imagen y el texto de estos mensajes se cargarán de manera dinámica desde la siguiente persistencia&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=[actual_contry]&#160; 
&#160; 
 Para el caso inicial de Colombia (co) , la consulta sería la siguiente 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co &#160;&#160; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co &#160; 

 Onboarding 1 
 Teniendo en cuenta la información que arroja la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=[actual_contry]&amp; order=1&#160; 
&#160; 
 Para el caso inicial de Colombia (co) , la consulta sería la siguiente 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=1 &#160; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=1 &#160; 
&#160; 
 De la siguiente manera&#58; 
&#160; 
 Imagen superior&#58; se debe traer de la URL registrada en el campo image_url 
 Título del mensaje&#58;&#160; según el dato que trae el parámetro&#58; title 
 Cuerpo del mensaje&#58;&#160; según el dato que trae el parámetro&#58; message 
&#160; 
 La demás información por el momento no se utilizará en esta implementación, pero a futuro podrán hacerse mejoras que manejen dichos datos. 

 Onboarding 2 
 Teniendo en cuenta la información que arroja la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=[actual_contry]&amp; order=2 
&#160; 
 Para el caso inicial de Colombia (co) , la consulta sería la siguiente 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=2 &#160; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=2 &#160; 
&#160; 
 Aplican las mismas consideraciones de visualización para el onboarding anterior 

 Onboarding 3 
 Teniendo en cuenta la información que arroja la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=[actual_contry]&amp; order=3 
&#160; 
 Para el caso inicial de Colombia (co) , la consulta sería la siguiente 
&#160; 
 Ambiente de pruebas&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=3 &#160; 
&#160; 
 Ambiente productivo&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/eatcloud/eatc_sale_messages?eatc_message_type=sale_onboarding&amp;eatc_country=co&amp; order=3 &#160; 
&#160; 
 Aplican las mismas consideraciones de visualización para el onboarding anterior 

 Botones de acción 
 En la parte inferior de los mensajes de onboarding se presentan dos botones. Uno de ellos (anterior) envía al mensaje previo. 
&#160; 
 Ingresa&#58; 
 Si se está ingresando por primera vez, el sistema debe ir a la funcionalidad &quot; Activación de permisos &quot; y luego a &quot; Mapa Nube de Alimentos &quot; corriendo también los procesos de Consulta de datos de ubicación y configuración y Obtención de código del usuario . 
&#160; 
 Si no se está ingresando por primera vez, el sistema debe ir a la funcionalidad &quot; Mapa Nube de Alimentos &quot; corriendo también los procesos de Consulta de datos de ubicación y configuración y Obtención de código del usuario . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsplash-screen-y-bienvenida-sale%2F1351870913-EmbeddedImage--80-.jpg&ow=1280&oh=666, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fsplash-screen-y-bienvenida-sale%2F1351870913-EmbeddedImage--80-.jpg&ow=1280&oh=666 
 App usuario final - Sale 

 778.000000000000 

 BIENVENIDA: SPLASH SCREEN Y ONBOARDING