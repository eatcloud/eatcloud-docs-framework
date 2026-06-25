# WAPP-Modernizada--permitir-captura-de--Peso-(hasta-ahora-KG)--en-otras-unidades-de-medida.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, cuando se crea una donación en la WAPP y la cuenta particular debe ingresar los KG o el Peso por la plataforma la WAPP, la única unidad de medida permitida, como su nombre lo indica es precisamente KG. 
&#160; 
 Se ha aprobado una mejora que implicará la posibilidad, para cuentas especificadas, poder tomar el “Peso de cada ítem del anuncio” en unidades de medida diferentes a KG. &#160;Si bien se permitirá la captura en estas unidades diferenciadas, se guardará una tabla con los factores de conversión de cada una de las unidades de medida a KG, porque el sistema deberá poder seguir guardando la información en KG (a pesar que se capturen en otras unidades de medida) 
 Puntos a los cuales se le despliega la funcionalidad 
Deberán ser puntos debidamente configurados como poseedores de la funcionalidad (se debe definir un parámetro de configuración para ello, que pueda actuar a nivel de punto de donación, pero también a nivel de cua_user, de tal manera que se pueda configurar también el despliegue para todos los puntos de donación de una cuenta, sin tener que hacer “n” registros de configuración&#58; uno por punto) 
&#160; 
 Selector de unidad de medida 
Se dispondrá de un selector estándar de unidades de medida, que se podrá obtener a partir de la siguiente consulta. 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/weight_measurement_units?_id=_*&amp;_cmp=weight_measurement_unit 
Los valores que arroja la consulta deben ser tratados como “labels” para su respectiva internacionalización 
&#160; 
Ejemplo&#58; ambiente productivo&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/weight_measurement_units?_id=_*&amp;_cmp=weight_measurement_unit &#160; 
&#160; 
El usuario podrá seleccionar la unidad de medida que desee utilizar para posteriormente ingresar la cantidad del “Peso” a ingresar. 
&#160; 
El sistema deberá proveer una opción para guardar dicha unidad de peso, como la que se utilice por defecto para la captura del mismo, otorgando también al usuario la manera de variar dicha selección por defecto. 
&#160; 
 Conversión de cantidad capturada a KG según factor de conversión 
Una vez se selecciona la unidad de peso y &#160;se ingresa el valor en el campo de captura, el sistema deberá determinar el factor de conversión con la siguiente consulta. 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/weight_measurement_units?weight_measurement_unit= &#123;&#123;unidad_seleccionada&#125;&#125; &amp;_cmp= conversion_factor_to_kg 
El valor ingresado en el campo de captura deberá multiplicarse por el factor de conversión, para guardar el peso en KG en la información de la donación. 
&#160; 
Ejemplo&#58; ambiente productivo&#58; 
El usuario seleccionó como unidad de medida “ onzas ” y entró el valor “ 77 ” 
&#160; 
El sistema realiza la siguiente consulta. 
 https&#58;//datagov.eatcloud.info /api/eatcloud/weight_measurement_units?weight_measurement_unit= onzas &amp;_cmp= conversion_factor_to_kg &#160; 
El sistema arroja como resultado “ 0,028349523 ”, por lo tanto el valor que guarda en la base de datos será&#58; 
77 x 0,028349523 = 2,182913271 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 f5243267-a32d-494f-91e2-0838198e1c03 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 eb95defc-a511-40fd-b432-3478ac076542 
 2025-04-12T06:42:44.0658040Z 

 {"SessionId":"59dd4453-f9b8-4787-8059-31f6ab740b25","SequenceId":3435,"FluidContainerCustomId":"844e6a24-d130-401d-97b2-ba542e7a6998","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: permitir captura de "Peso (hasta ahora KG)" en otras unidades de medida