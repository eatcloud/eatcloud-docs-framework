# WAPP-Modernizada--restricción-de-registros-en-eatc_odds-a-partir-de-parámetro-de-configuración.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, cuando se crea una donación en la WAPP y el producto no está en el maestro, el sistema realiza un registro de producto que se está creando en eatc_odds. &#160;Uno de nuestros clientes (isimo) solicitó bloquear dicha funcionalidad, es decir, que no se puedan crear productos en el maestro y por lo tanto que solamente se permitan subir productos en donaciones que están presentes en el maestro. &#160;Por eso se creó un nuevo parámetro de configuración eatc_cua. create_odds_from_wapp_dona que cuando esté marcado como “n”, no permitirá incluir nuevos productos al maestros desde la creación de la donación y por ende también bloquear la creación de donaciones por productos fuera del maestro 
 Validación del parámetro de configuración para restringir la funcionalidad 
 Antes de desplegar el formulario, el sistema deberá realizar validar la cuenta en cuestión tiene restricciones al respecto, en caso de ternerlas (valor del parámetro =n) entonces no le permitirá crear donaciones con productos por fuera del maestro de productos y tampoco llevar nuevos productos al maestro. &#160;Por eso debe realizar la siguiente consulta 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/ eatc_cua? name= &#123;&#123; _DOM. cua_user&#125;&#125;&amp;_cmp= create_odds_from_wapp_dona 
&#160; 
 Si la respuesta es igual a “ n ”, entonces el sistema no le permitirá al usuario de la cuenta respectiva, crear donaciones con productos por fuera del maestro (y por ende realizar nuevos registros en el maestro eatc_odds, a partir de la creación de donaciones en la WAPP) 
&#160; 
 Si la respuesta es vacía , nula , cero , incorrecta o “ y ”, entonces el sistema funcionará cómo viene funcionando hasta el momento (con la posibilidad de adicionar nuevos productos desde la creación del anuncio en la WAPP y el registro de dichos productos en eatc_odds) 
&#160; 
 Ejemplo 1&#58; ambiente de producción eatc_cua “alqueria” 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_cua? name= alqueria&amp;_cmp= create_odds_from_wapp_dona &#160; 
Como a 24 de febrero de 2025, la respuesta es 
&#123; 
 ts &#58; &quot;250224174650&quot;, 
 op &#58; false, 
 err_msg &#58; &quot;Unknown column 'create_odds_from_wapp_dona' in 'field list'&quot;, 
 err_num &#58; 1054, 
 mem &#58; 0.41, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
&#125; 
(incorrecta), el sistema funcionará tal y como viene funcionando (permitiéndole adicionar nuevos productos desde la WAPP a la donación y al maestro de productos eatc_odds) 
&#160; 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas eatc_cua “axionlog” 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=axionlog&amp;_cmp=create_odds_from_wapp_dona&#160; 
Como a 24 de febrero de 2025, la respuesta es 
&#123; 
 create_odds_from_wapp_dona &#58; &quot;n&quot; 
&#125; 
El sistema restringirá la posibilidad de adicionar productos que no están en el maestro eatc_odds a la donación y por ende de realizar nuevos registros a eatc_odds 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"}] 
 0405a719-577b-4907-af4a-a7cc3e51f75d 
 1!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 f2af42f7-02e6-4cd3-bf49-096d476f009f 
 2025-04-28T22:50:17.9699673Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"3f7208b4-d3f0-4946-8a5f-bb6cfdc46a85","SequenceId":-1,"FluidContainerCustomId":"e3abb697-ef6d-44eb-a234-27bf8a5d5827","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción de registros en eatc_odds a partir de parámetro de configuración