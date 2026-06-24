# BO-donantes--Creación-de-Artículos-por-archivo-plano--integración-de-clasificadores.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, existe una funcionalidad de creación de artículos para el maestro de artículos (odds) mediante archivo plano.  La misma se debe refinar, para posibilitar la integración con los clasificadores de artículos que se están desarrollando. 

 Para lograr eso, se deber incorporar la captura del dato “Tipología origen a”, y posteriormente crear un servicio, que en una cola, permita realizar la clasificación de los artículos que se cargan por el archivo plano. 

 Si esta funcionalidad está disponible en la WAPP, habilitarla igualmente para dicho perfil. 
 Captura del campo “ origin_odds_typology_a ” 
En el mapeo del archivo origen, se deberá exigir de manera obligatoria la entrega de una clasificación o tipología propia de la compañía para este artículo.  Se deberá explicar al usuario en su experiencia, que esta información es necesaria para clasificar el producto en categorías que son necesarias para la operación del sistema.  El sistema deberá validar que los datos de la columna respectiva estén presentes a la hora de cargar el archivo plano. 

 Integración servicios de clasificación 
 Una vez creados los productos en la base de datos, deberá operar sobre ellos un proceso que genere una cola de clasificación y que deberá invocar diversos servicios de clasificación en la secuencia que se explica a continuación:  
 Invocación del primer clasificador 
 El sistema procederá a realizar el siguiente llamado, con la información del “nombre del producto” ( {{ eatc-odd_name }} ) digitado por el usuario y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class1/categorize?cua_master= {{_DOM. cua_master }} &odd_name= {{ eatc-odd_name }} 
Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 } 
Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
En caso de no obtener respuesta deberá invocar el segundo clasificador. 

 Invocación del segundo clasificador 
 Si no obtuvo una clasificación con el primer clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class2/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 } 
Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
En caso de no obtener respuesta deberá invocar el tercer clasificador. 

 Invocación del tercer clasificador 
 Si no obtuvo una clasificación con el segundo clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class3/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
Si el sistema responde adecuadamente con las tipologías a y b 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}" 
 } 
Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
En caso de no obtener respuesta deberá invocar el cuarto clasificador. 

 Invocación del cuarto clasificador 
 Si no obtuvo una clasificación con el tercer clasificador, sistema procederá a realizar el siguiente llamado, con la información de la tipología origen del producto digitada por el usuario ( {{ origin_odds_typology_a }} )  y la cuenta maestra a la cuál pertenece ( {{_DOM. cua_master }} ): 
 {{ URL_entorno_datagov }}/eatc_class4/categorize?cua_master= {{_DOM. cua_master }} &typology= {{ origin_odds_typology_a }} 
Si se llega a este punto se deberá utilizar la información generada por el clasificador 
 { 
   "eatc-odd_typology_b": "{{ typology_b }}", 
   "eatc-odd_typology_a": "{{ typology_a }}", 
   "probabilidad": {{ porcentaje_probabilidad }}, 
   "modelo_usado": {{ modelo }} 

 } 

Entonces el sistema deberá a proceder a llevar estas tipologías al maestro de productos ( eatc_odds u odds ),  
 eatc_odds. eatc-odd_typology_a = {{ typology_a }} 
 eatc_odds. eatc-odd_typology_b = {{ typology_b }} 
Para porcentajes de probabilidad por debajo de 90%, se deberá generar una alerta, a un grupo de Telegram o Teams, en donde se informe, fuera de la respuesta que arroja el clasificador (y que se expuso más arriba), los datos de la cuenta maestra, cuenta usuario, nombre, código y tipología a del articulo 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 32b13d0e-f82d-493a-ab41-e5e83c5f372c 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 cf0d368d-8632-42dc-84df-2ef4dd88d079 
 2025-05-30T04:50:12.5013728Z 

 {"SessionId":"69a92147-2c38-4f90-b427-69f0b1023d04","SequenceId":257,"FluidContainerCustomId":"85700341-6869-42bc-8aa2-91ff3194b16a","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 

 BO donantes: Creación de Artículos por archivo plano: integración de clasificadores