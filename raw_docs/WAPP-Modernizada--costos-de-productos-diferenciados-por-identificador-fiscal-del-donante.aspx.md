# WAPP-Modernizada--costos-de-productos-diferenciados-por-identificador-fiscal-del-donante.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, en la WAPP para donantes particulares (habilitados por el parámetro de configuración “ multiple_donors ”), se permiten tomar donaciones que salen a nombre de diferentes razones sociales. &#160;Uno de nuestros clientes ( donkin donuts ) solicitó poder tener costos diferenciados por “identificador fiscal” o razón social de las cuales hace donaciones. &#160;Por eso se debe crear un nuevo parámetro de configuración para el maestro de productos “odds”&#58; &quot; donor_fiscal_id &quot; cuyo valor por defecto será “NULL” o “vacío” (según el estándar de desarrollo implementado en Modernización). &#160;Cuando un donante decida dar un “costo diferenciado por razón social”, deberá registrar en ese campo el respectivo “identificador fiscal” o nit (que corresponde a la tabla de configuración respectiva). 
 Validación del parámetro de configuración para desplegar el costo diferenciado 
 Cuando el donante está configurado como “”, entonces la WAPP le permite escoger dicha razón social en un selector al inicio de la creación de donaciones. &#160;Al hacer esto, el sistema deberá guardar el respectivo “identificador fiscal” de la razón social seleccionada, y a la hora de mostrar los “costos de un artículo seleccionado”, primero deberá ir a la tabla de “odds” y buscar por el tradicional “código del producto” (tal como se busca ahora) y el nuevo dato de “ donor_fiscal_id ”. &#160;Si la consulta no arroja resultados, deberá consultar de la misma manera que se hace hasta ahora, arrojando el precio y los datos del respectivo producto. &#160;Si hay un match para dicho producto, con un precio diferenciado por “ donor_fiscal_id ”, entonces deberá traer el costo diferenciado para registrarlo en la donación. 
&#160; 
 Incorporación del nuevo parámetro en la creación por archivo plano de donaciones. 
Cuando una cuenta tenga la opción de “ multiple_donors ” habilitada, a la hora de crear anuncios por archivo plano, deberá habilitarse la opción “no obligatoria” para mapear el nit o “ donor_fiscal_id” ( identificación tributaria del donante) y poder cargar esa información por archivo plano. &#160;Esta opción deberá habilitarse validando contra el maestro respectivo (en donde están lo que anteriormente se conocía como ”multiple_nits&quot;), para evitar el registro de datos erróneos. &#160;El sistema deberá permitir el envío de este campo “Vacío” y la funcionalidad deberá permitir el registro de valores “vacíos” o “nulos” en el respectivo maestro (cuando a partir de la información de crean registros de productos en el maestro “odds”), sin ningún inconveniente. 
&#160; 
 Incorporación del nuevo parámetro en la creación manual de productos. 
Cuando una cuenta tenga la opción de “ multiple_donors ” habilitada, a la hora de crear productos, deberá habilitarse un campo opcional para colocar el nit o “ donor_fiscal_id” ( identificación tributaria del donante). &#160;Esta opción deberá habilitarse con un selector, que funcione de la misma manera que funciona el selector en la WAPP, cuando el donante tiene esta condición, es decir, que le permita escoger del maestro respectivo (en donde están lo que anteriormente se conocía como ”multiple_nits&quot;), para registrar el dato. &#160;El valor por defecto del campo debe ser “Vacío” y la funcionalidad deberá permitir el registro de valores “vacíos” o “nulos” en el respectivo maestro, sin ningún inconveniente. 
&#160; 
 Incorporación del nuevo parámetro en la creación por archivo plano de productos. 
Cuando una cuenta tenga la opción de “ multiple_donors ” habilitada, a la hora de crear productos por archivo plano, deberá habilitarse la opción “no obligatoria” para mapear el nit o “ donor_fiscal_id” ( identificación tributaria del donante) y poder cargar esa información por archivo plano. &#160;Esta opción deberá habilitarse validando contra el maestro respectivo (en donde están lo que anteriormente se conocía como ”multiple_nits&quot;), para evitar el registro de datos erróneos. &#160;El sistema deberá permitir el envío de este campo “Vacío” y la funcionalidad deberá permitir el registro de valores “vacíos” o “nulos” en el respectivo maestro, sin ningún inconveniente. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 72e9828e-1a23-4551-ab3b-6d73577eaa4b 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 4b83d00b-49ea-473c-91c0-0821e5fdb7bc 
 2025-04-28T23:09:58.3023080Z 

 {"SessionId":"e8ad5a4a-c893-4df0-b6ae-f239f782b2e8","SequenceId":6563,"FluidContainerCustomId":"6ae62dab-6a86-4fa5-9b64-a295bbdef01d","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: costos de productos diferenciados por identificador fiscal del donante