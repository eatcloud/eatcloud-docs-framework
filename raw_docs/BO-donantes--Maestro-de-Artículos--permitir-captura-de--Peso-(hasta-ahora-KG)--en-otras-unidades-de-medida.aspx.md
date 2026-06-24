# BO-donantes--Maestro-de-Artículos--permitir-captura-de--Peso-(hasta-ahora-KG)--en-otras-unidades-de-medida.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, cuando se crea un producto en el maestro de productos a través del formulario de creación respectivo el usuario debe ingresar los KG o el Peso unitario del producto, la única unidad de medida permitida hasta el momento. 

 Se ha aprobado una mejora que implicará la posibilidad, para cuentas especificadas, poder tomar el “Peso de cada ítem del maestro” en unidades de medida diferentes a KG.  Si bien se permitirá la captura en estas unidades diferenciadas, se guardará una tabla con los factores de conversión de cada una de las unidades de medida a KG, porque el sistema deberá poder seguir guardando la información en KG (a pesar que se capturen en otras unidades de medida) 
 Cuentas a las cuales se le despliega la funcionalidad 
Deberán poseer puntos debidamente configurados como poseedores de la funcionalidad o tener la configuración a nivel de cuenta de despliegue de dicha funcionalidad. 

 Selector de unidad de medida 
Se dispondrá de un selector estándar de unidades de medida, que se podrá obtener a partir de la siguiente consulta. 
{{URL_datagov}}/api/eatcloud/ weight_measurement_units ?_id=_*&_cmp=weight_measurement_unit 
Los valores que arroja la consulta deben ser tratados como “labels” para su respectiva internacionalización. 

Ejemplo: ambiente productivo: 
 https://datagov.eatcloud.info/api/eatcloud/weight_measurement_units?_id=_*&_cmp=weight_measurement_unit   

El usuario podrá seleccionar la unidad de medida que desee utilizar para posteriormente ingresar la cantidad del “Peso” a ingresar. 

El sistema deberá proveer una opción para guardar dicha unidad de peso, como la que se utilice por defecto para la captura del mismo, otorgando también al usuario la manera de variar dicha selección por defecto. 

 Conversión de cantidad capturada a KG según factor de conversión 
Una vez se selecciona la unidad de peso y  se ingresa el valor en el campo de captura, el sistema deberá determinar el factor de conversión con la siguiente consulta. 
 {{URL_datagov}} /api/eatcloud/weight_measurement_units?weight_measurement_unit= {{unidad_seleccionada}} &_cmp= conversion_factor_to_kg 
El valor ingresado en el campo de captura deberá multiplicarse por el factor de conversión, para guardar el peso en KG en la información de la donación. 

Ejemplo: ambiente productivo: 
El usuario seleccionó como unidad de medida “ onzas ” y entró el valor “ 77 ” 

El sistema realiza la siguiente consulta. 
 https://datagov.eatcloud.info /api/eatcloud/weight_measurement_units?weight_measurement_unit= onzas &_cmp= conversion_factor_to_kg   
El sistema arroja como resultado “ 0,028349523 ”, por lo tanto el valor que guarda en la base de datos será: 
77 x 0,028349523 = 2,182913271 

 Persistencia de la unidad de peso en la creación del producto 
 El sistema deberá guardar en un campo en el maestro de artículos la unidad con la cual se creó el producto.  Esto no quiere decir que el peso unitario no se guarde en KG (idea principal de implementación), pero si la posibilidad a futuro, aplicando el factor de conversión inverso, de mostrar los pesos del producto en diversos informes en la unidad de medida en la cual se creó. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ca9435e2-a690-446d-b217-8f3800c0884e 
 1!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 81f485e9-b61a-4032-a581-6e6ef21b5886 
 2025-04-12T07:29:48.1063791Z 

 {"SessionId":"54ece4a0-b4d4-4e84-b4f3-555558509a67","SequenceId":567,"FluidContainerCustomId":"33191e58-a472-4343-9c5e-2054b3b1fbdd","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"Off"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 

 BO donantes: Maestro de Artículos: permitir captura de "Peso (hasta ahora KG)" en otras unidades de medida