# BO-donantes--Creación-manual-de-maestro-de-Artículos--Categoría-de-artículos-obligatoria.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 BO donantes: Creación manual de maestro de Artículos: Categoría de artículos obligatoria "},"containsDynamicDataSource":false}">

Resumen: 
 En la actualidad, existe una funcionalidad de creación de artículos para el maestro de artículos (odds).  La misma se debe refinar, para posibilitar la clasificación por parte del usuario, del producto, en las categorías significativas definidas por ABACO y por BAMX. 

 Para lograr eso, se deber incorporar, a partir del dato captura, información en los campos odds_typology_a y odds_typology_b. 

Captura del campo “Selecciona categoría de producto” (captura obligatoria) 
Según lo propuesto en el diseño: https://www.figma.com/design/fz65QCafGLQOjca5ShRzTc/Nubola-Design-System?node-id=1343-4030&t=i0PJufXsrqhLOiEv-0   

Tipo de campo de captura: 
Selector único en lista desplegable, con buscador de valores. 
Valor por defecto: 
El sistema deberá sugerir un valor, a partir de enviarle el nombre del producto, previamente digitado más arriba en el formulario, al siguiente endpoint: 
 Método:  POST 
 Endpoint:   http://20.83.146.184/api/v1/webhooks/Iiet185CbmyZNu77QrT9E/sync   
 Json body: 
{
 "data": {
   "rows": [
     {
       "ambiente": "prd",    ***prd o dev, según sea el ambiente*** 
       "odd_name": " {{odd_name}} ",  ***obligatorio*** 
       "cua_master": " {{cua_master}} ",  ***obligatorio*** 
       "odd_category": " {{odd_origin_typology_a}} "  ***opcional: lo más seguro es que no se envíe*** 
     }
   ]
 }
} 
El sistema deberá responder con un mensaje como este: 
{
 "ok": true,
 "data": {
   "ambiente": "prd",
   "odd_name": " {{odd_name}} ",
   "cua_master": " {{cua_master}} ",
   "eatc_odd_typology_a": " {{eatc-odd_typology_a}} ",   ***food / other*** 
   "eatc_odd_typology_b": " {{eatc-odd_typology_b}} ",   ***es el dato que se colocará como categoría de productos sugerida en                                                                                               el selector*** 
   "origin_odds_typology_a": " {{odd_origin_typology_a}} "  ***por lo general llegará vacía*** 
 },
 "message": " {{tipo_clasificacion}} "  ***se utiliza más adelante para actualizar el maestro de productos, se ser necesario*** ,
 "classified": true,
 "already_classified": true
} 

Si el servicio no responde, entonces el valor por defecto será la selección vacía, con el ánimo de que el usuario tenga que realizar una búsqueda o una selección 

Valores para construir el selector: 
El selector se deberá construir a partir de los siguientes valores:  
Si la cuenta maestra es “ mexico ” se realiza la siguiente consulta 
{{URL_datagov}}/api/eatcloud/ odds_categories ?cua_master= mexico &_cmp=etiqueta,tipo 
 Ejemplo , ambiente de pruebas: https://dev.datagov.eatcloud.info/api/eatcloud/odds_categories?cua_master=mexico&_cmp=etiqueta,tipo   
Para las demás cuentas maestras (hasta que se haga una nueva determinación al respecto), las clasificaciones serán 
{{URL_datagov}}/api/eatcloud/ odds_categories ?cua_master= ! mexico&_cmp=etiqueta,tipo 
 Ejemplo , ambiente de pruebas: https://dev.datagov.eatcloud.info/api/eatcloud/odds_categories?cua_master= ! mexico&_cmp=etiqueta, tipo   

El selector deberá presentar en su respectiva “etiqueta”, el valor que devuelve el campo “etiqueta” (este valor se deberá internacionalizar según el idioma de la plataforma). 
Una vez el usuario seleccione la “ {{etiqueta}} ” que considere (o si deja el valor por defecto seleccionado), el sistema deberá hacer la siguiente escritura en el maestro de ODDs (la escritura siguiente es meramente ilustrativa, y muestra los parámetros que están incluidos en esta porción de la funcionalidad y que deberán ser incorporados a la hora de crear todos los parámetros en el respectivo maestro de artículos modernizado ( odds )), teniendo en cuenta el respectivo {{tipo}} asociado a la misma: 

Si el usuario no cambia el valor por defecto sugerido:  
{
 "classification_type": " {{tipo_clasificacion}} ",   
 "eatc_odd_typology_a": " {{eatc-odd_typology_a}} ",
 "eatc_odd_typology_b": " {{eatc-odd_typology_b}} ",
 "classification_percentage": "100"
} 
Si el usuario no cambia el valor de la etiqueta, por uno de su elección, entonces la escritura será:  
{
 "classification_type": “ user_classification ” 
 "eatc_odd_typology_a": " {{tipo}} ",
 "eatc_odd_typology_b": " {{etiqueta}} ",
 "classification_percentage": "100"
} 

Validaciones: 
La captura de este campo será obligatoria y por lo tanto el sistema deberá validar que existan valores en el mismo y que correspondan a los seleccionados por el usuario. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=e178761d3e21477ab6ad39e3e4c91644&ext=png&ow=810&oh=341, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=e178761d3e21477ab6ad39e3e4c91644&ext=png&ow=810&oh=341 

 62785cf3-ff68-4560-9364-6332f9c9a156 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 c99fa560-a9c8-4e79-b282-6e172808c4f9 
 2025-12-24T00:36:26.0675137Z 

 {"SessionId":"236b3d41-ea7f-4830-acfe-651156b834d9","SequenceId":562,"FluidContainerCustomId":"988e63c7-08fa-4083-82b5-4eeb9ff0e5c7","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1177.00000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 BO donantes: Creación manual de maestro de Artículos: Categoría de artículos obligatoria