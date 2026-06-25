# traducción-de-labels.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disear un servicio, que permita la traduccin uno a uno de los labels o la traduccin en bloque de los labels.&#160; El servicio recibir el label o etiqueta (o una consulta general de labels) y definiendo un idioma origen (que inicialmente debe ser &quot;es&quot; o &quot;en&quot;) y un idioma destino (el ISO2 del idioma), obtenga la traduccin del copy respectivo (utilizando un API de traduccin) y se registren los datos asociados a dicho copy traducido en el lenguaje establecido. 

 Llamado al servicio 
 El llamado al servicio se propone sea el siguiente&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ translate /eatcloud? eatc_label =&#123;&#123; eatc_labels. eatc_labels &#125;&#125;&amp; from = &#123;&#123; eatc_config_labels . lang &#125;&#125;&amp; to =&#123;&#123; eatc_languages. iso2 &#125;&#125; 

 Parmetros del llamado al servicio 

 eatc_label 
 Servir para obtener el valor del respectivo copy del label en el lenguaje origen (from), para enviarlo en con el API de traduccin como el texto a traducir.&#160; Se pretende que en algn momento se pueda realizar un proceso bulk para traducir todos los labels, enviando el valor&#160; _* como indicacin de esta traduccin en bloque. 

 from 
 Lenguaje origen desde el cual se pretende traducir.&#160; Debe ser un leguaje previamente registrado en EatCloud, por lo tanto el sistema deber verificar que dicho cdigo ISO 2 est presente en el sistema realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ api /eatcloud/ eatc_config_labels ? idlabel = &#123;&#123; eatc_label &#125;&#125; &amp; _distinct =lang 
&#160; 
 Si el idioma no est en esta en esa consulta, entonces el servicio debe contestar&#58; 
&#160; 
 class= lbl_idioma_origen_no_disponible &quot;Copy en idioma origen no disponible&quot; 

 to 
 Lenguaje destino al cual se debe traducir el copy.&#160; Debe ser un lenguaje previamente registrado en EatCloud, por lo tanto el sistema deber realizar que dicho cdigo ISO 2 est presente en el maestro de lenguajes de EatCloud realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ api /eatcloud/ eatc_languages?_id= _ *&amp;_distinct= iso2 
&#160; 
 Si el idioma destino no est en esta en esa consulta, entonces el servicio debe contestar&#58; 
&#160; 
 class= lbl_idioma_destino_no_disponible &quot;Idioma destino no registrado como idioma oficial en EatCloud. Por favor regstrelo y proceda de nuevo&quot; 

 Llamado API externa de traduccin 
&#160; 
 Por lo general las APIs de traduccin, de una u otra manera, reciben tres parmetros&#58; 
&#160; 
 texto_a_traducir (se explicar ms adelante) 
 idioma_origen &#58; corresponde al dato enviado en el parmetro &quot; from &quot; 
 idioma_destino &#58; corresponde al dato enviado en el parmetro &quot; to &quot; 
&#160; 
 La idea es encontrar un servicio que nos permita realizar un buen volumen de llamadas para efectuar traducciones, de manera gratuita, o por un cobro muy reducido. 
&#160; 
 Inicialmente se encontraron estas dos posibles opciones&#58; 
&#160; 
 Libretranslate&#58; https&#58;//libretranslate.com/ &#160; 
 Yandex Translate&#58; https&#58;//cloud.yandex.com/en/docs/translate/ &#160; 

&#160; 
 Se pueden explorar otras opciones, que permitan un buen funcionamiento del servicio de traduccin. 

 texto_a_traducir &#58; a partir del parmetro eatc_label 
 Dado que un label, por personalizaciones asociadas al pas, o la cuenta, puede tener varios copies diferentes, con el dato recibido por el llamado al servicio, el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ api /eatcloud/ eatc_config_labels ? idlabel = &#123;&#123; eatc_label &#125;&#125; &amp;lang= &#123;&#123; from &#125;&#125;&amp;_distinct= copy 
&#160; 
 Para hacer tantos llamados al API de traduccin como copies diferentes existan para el label en cuestin. 
&#160; 
 El sistema deber guardar el texto_a_traducir y su respectiva traduccin (respuesta del API de traduccin), para posteriormente con esos datos realizar los registros necesarios en eatc_config_labels con las traducciones recibidas. 

 Registro de las traducciones ( traduccion ) en eatc_config_labels 
 Con las duplas&#58; texto_a_traducir , traduccin que se obtienen en el llamado al API de traduccin, el sistema debe realizar la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ api /eatcloud/ eatc_config_labels ? idlabel = &#123;&#123; eatc_label &#125;&#125;&amp; copy = &#123;&#123; texto_a_traducir &#125;&#125; &amp;lang= &#123;&#123; from &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 TRADUCCIN DE LABELS