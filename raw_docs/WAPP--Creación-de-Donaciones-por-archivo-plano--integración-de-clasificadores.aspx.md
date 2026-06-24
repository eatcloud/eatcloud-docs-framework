# WAPP--Creación-de-Donaciones-por-archivo-plano--integración-de-clasificadores.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, existe una funcionalidad de creación de donaciones mediante archivo plano.  La misma se debe refinar, para posibilitar la integración con los clasificadores de artículos que se están desarrollando. 

 Para lograr eso, se deber incorporar la captura del dato “Tipología origen a”, y posteriormente crear un servicio, que en una cola, permita realizar la clasificación de los artículos que se cargan por el archivo plano. 

 Captura del campo “ origin_odds_typology_a ” 
En el mapeo del archivo origen, se deberá exigir de manera obligatoria la entrega de una clasificación o tipología propia de la compañía para este artículo.  Se deberá explicar al usuario en su experiencia, que esta información es necesaria para clasificar el producto en categorías que son necesarias para la operación del sistema.  El sistema deberá validar que los datos de la columna respectiva estén presentes a la hora de cargar el archivo plano. 

 Integración servicios de clasificación 
 Una vez creados los productos en la base de datos, deberá operar sobre ellos un proceso que genere una cola de clasificación y que deberá invocar diversos servicios de clasificación en la secuencia que se explica a continuación:  

 Inclusión del producto en el maestro modernizado (odds) 
Como primera medida se deben llevar los datos del producto al maestro de productos modernizado.  Una vez se complete este registro de manera exitosa, se procede a realizar la invocación del clasificador unificado (en la anterior especificación había 4 llamados endpoints diferentes, que se convirtieron en uno, pero su condición de operación es que el producto esté registrado en el maestro. 

El nombre del producto no debe contener comas, dobles espacios al medio, debe estar “Trimiado” (sin espacios al inicio y al final) para ser registrado en el maestro y que el clasificador funcione adecuadamente. 

Invocación del clasificador: 
El sistema realizará el siguiente llamado para invocar el clasificador 
 Método:  POST 
 Endpoint:   http://20.83.146.184/api/v1/webhooks/h3XsPnbataR114sxkvGDF    (si este no funciona, se puede utilizar este como redundancia: http://20.83.146.184/api/v1/webhooks/p8lkMtp8lc7E7Jq20CToo ) 
 Json body: 
{
 "data": {
   "rows": [
     {
       "ambiente": "prd",    *** prd o dev , según sea el ambiente*** 
       "odd_name": " {{odd_name}} ",  ***obligatorio*** 
       "cua_master": " {{cua_master}} ",  ***obligatorio*** 
       "odd_category": " {{odd_origin_typology_a}} "  ***opcional*** 
     }
   ]
 }
} 
 DEPRECADO 
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
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
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
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
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
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
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
 y posteriormente al registro del eatc_dona específico 
 eatc_dona. eatc-odd_typology_a = {{ typology_a }} 
 eatc_dona. eatc-odd_typology_b = {{ typology_b }} 
 Para porcentajes de probabilidad por debajo de 90%, se deberá generar una alerta, a un grupo de Telegram o Teams, en donde se informe, fuera de la respuesta que arroja el clasificador (y que se expuso más arriba), los datos de la cuenta maestra, cuenta usuario, nombre, código y tipología a del articulo 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 7cc01c12-04b9-4ef5-bdd3-1935c06d92ca 
 4!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 dea62bee-56a6-4c20-a8f4-d319d1b8ebe7 
 2025-11-07T05:24:46.8436339Z 

 {"SessionId":"e6606e96-9b37-4755-9893-d24c8bef6c00","SequenceId":72,"FluidContainerCustomId":"9f43fcc3-20bc-430b-ad06-0cd7a75429ca","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 WAPP: Creación de Donaciones por archivo plano: integración de clasificadores