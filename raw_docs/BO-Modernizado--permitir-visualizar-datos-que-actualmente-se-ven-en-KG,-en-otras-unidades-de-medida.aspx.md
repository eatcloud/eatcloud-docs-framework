# BO-Modernizado--permitir-visualizar-datos-que-actualmente-se-ven-en-KG,-en-otras-unidades-de-medida.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 El cliente Alquería, ha solicitado la posibilidad de poder visualizar KPIs, relacionados a información que se ve en Kilogramos (KG), en otra unidad de medida (para su caso: litros).  Es por eso que en su BO, deberá existir una posibilidad de configurar la unidad de medida en la cuál quiere ver sus datos, y a partir de esa selección, el sistema deberá transformar en la UI, los datos que están guardados en KG en la nueva unidad de medida, y para ello utilizará el factor de conversión de la unidad de medida seleccionada a KG. 

 Selector de unidad de medida 
Se dispondrá de un selector estándar de unidades de medida para visualizar sus KPIs referentes a unidades de peso, que se podrá obtener a partir de la siguiente consulta. 
{{URL_datagov}}/api/eatcloud/weight_measurement_units?_id=_*&_cmp=weight_measurement_unit 
Los valores que arroja la consulta deben ser tratados como “labels” para su respectiva internacionalización 

Ejemplo: ambiente productivo: 
 https://datagov.eatcloud.info/api/eatcloud/weight_measurement_units?_id=_*&_cmp=weight_measurement_unit   

El usuario podrá seleccionar la unidad de medida que desee utilizar en la visualización de informes.  Esta selección podrá cambiarse en cualquier momento, ingresando al respectivo configurador. 

Visualización de información de KPIs asociados a “peso” en la nueva unidad. 
Una vez se selecciona la unidad de peso el sistema deberá obtener el factor de conversión de la unidad seleccionada a KG. 
 {{URL_datagov}} /api/eatcloud/weight_measurement_units?weight_measurement_unit= {{unidad_seleccionada}} &_cmp= conversion_factor_to_kg 
Con este valor obtendrá el factor de conversión de KG a la unidad de medida seleccionada, de la siguiente manera: 
 conversion_factor_kg_to_new_mesurement_unit = 1/conversion_factor_to_kg 

Ejemplo: ambiente productivo: 
El usuario seleccionó como unidad de medida “ onzas ”: 

El sistema realiza la siguiente consulta. 
 https://datagov.eatcloud.info /api/eatcloud/weight_measurement_units?weight_measurement_unit= onzas &_cmp= conversion_factor_to_kg   
El sistema arroja como resultado “ 0,028349523 ”, por lo tanto el factor de conversión de KG a onzas será: 
1/ 0,028349523 = 35,27 (aprox) 
 Por lo tanto todo valor que en la UI tenga su expresión en KG, deberá ser multiplicado por 35,27 (aprox) para desplegar su equivalencia en onzas. 

Cambio de etiqueta “KG” o “Kilos”, por la nueva unidad de medida. 
En la interfaz de usuario, al seleccionar una nueva unidad de medida, y presentar los valores relativos a peso en KG en la nueva unidad, se deberán variar las etiquetas que originalmente están en “Kilogramos” por la nueva unidad de medida seleccionada (para el ejemplo anterior: en vez de hablar de KG se hablará de Onzas ). 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 282c0404-8186-42b5-af29-7a5e18228954 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 4f40ed2d-30c9-489f-9077-7dee78f73f6f 
 2025-06-04T04:17:42.3175804Z 

 {"SessionId":"d5f97482-5aeb-4ae6-9383-b2e15b416ac5","SequenceId":4447,"FluidContainerCustomId":"a52b8796-0c5a-4df3-9d11-268bd825423a","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 BO Modernizado: permitir visualizar datos que actualmente se ven en KG, en otras unidades de medida