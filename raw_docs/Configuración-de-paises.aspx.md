# Configuración-de-paises.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

Para configurar paises y cua_masters debemos añadir primero el país en la tabla countries, importante que la columna “code” sea el ISO 3166-1 alfa-2, que es el código de 2 letras de cada país.

Una vez añadido en countries, debemos añadir la cua en la tabla cua_masters, ingresando en “code_country” el mismo ingresado en la columna “code” de la tabla countries. El sistema solo detectará aquellas "cua_masters" cuyo status es True o 1. 

Con esta configuración el país estará disponible en el onboarding de beneficiarios y en el registro de puntos de donación. 

En adición a eso para un correcto funcionamiento y una buena experiencia de usuario es necesario proveer los labels de internacionalización necesarios para un correcto funcionamiento, como base se adjuntan los labels de Colombia: 

 xxxxxxxxxx 

 "co" : { 
         "lbl_identificacion_tributaria_doma" : "Nit de la organización" , 
         "lbl_fecha_registro_doc_legal_2" : "Fecha de registro en la Cámara de Comercio" , 
         "lbl_fecha_impresion_doc_legal_1" : "Fecha de impresión del RUT (Registró Único Tributario)" , 
         "lbl_ingresa_fecha_impresion_doc_legal_1" : "Ingresa la fecha de impresión del RUT (Registró Único Tributario)" , 
         "lbl_adjunta_doc_legal_1" : "Adjunta el RUT (Registró Único Tributario)" , 
         "lbl_adjunta_doc_legal_2" : "Adjunta el Certificado de Cámara de Comercio" , 
         "lbl_kilos_recoge_organizacion" : "¿Cuántos Kilos puede recoger la organización?" , 
         "lbl_departamento" : "Departamento" , 
         "lbl_indica_nit" : "Indica tu NIT" , 
         "lbl_escribe_nit" : "Escribe tu NIT" , 
         "todos_departamentos" : "Todos los departamentos" 
   } 

 "},"searchablePlainTexts":{"code":""co": {
 "lbl_identificacion_tributaria_doma": "Nit de la organización",
 "lbl_fecha_registro_doc_legal_2": "Fecha de registro en la Cámara de Comercio",
 "lbl_fecha_impresion_doc_legal_1": "Fecha de impresión del RUT (Registró Único Tributario)",
 "lbl_ingresa_fecha_impresion_doc_legal_1": "Ingresa la fecha de impresión del RUT (Registró Único Tributario)",
 "lbl_adjunta_doc_legal_1": "Adjunta el RUT (Registró Único Tributario)",
 "lbl_adjunta_doc_legal_2": "Adjunta el Certificado de Cámara de Comercio",
 "lbl_kilos_recoge_organizacion": "¿Cuántos Kilos puede recoger la organización?",
 "lbl_departamento": "Departamento",
 "lbl_indica_nit": "Indica tu NIT",
 "lbl_escribe_nit": "Escribe tu NIT",
 "todos_departamentos": "Todos los departamentos"
 }"},"imageSources":{},"links":{}},"dataVersion":"2.0","properties":{"language":"TypeScript","lineNumbers":false,"lineWrapping":true,"theme":"Base16Light"},"containsDynamicDataSource":false}">

 xxxxxxxxxx 

 "co" : { 
         "lbl_identificacion_tributaria_doma" : "Nit de la organización" , 
         "lbl_fecha_registro_doc_legal_2" : "Fecha de registro en la Cámara de Comercio" , 
         "lbl_fecha_impresion_doc_legal_1" : "Fecha de impresión del RUT (Registró Único Tributario)" , 
         "lbl_ingresa_fecha_impresion_doc_legal_1" : "Ingresa la fecha de impresión del RUT (Registró Único Tributario)" , 
         "lbl_adjunta_doc_legal_1" : "Adjunta el RUT (Registró Único Tributario)" , 
         "lbl_adjunta_doc_legal_2" : "Adjunta el Certificado de Cámara de Comercio" , 
         "lbl_kilos_recoge_organizacion" : "¿Cuántos Kilos puede recoger la organización?" , 
         "lbl_departamento" : "Departamento" , 
         "lbl_indica_nit" : "Indica tu NIT" , 
         "lbl_escribe_nit" : "Escribe tu NIT" , 
         "todos_departamentos" : "Todos los departamentos" 
   } 

"co": {
 "lbl_identificacion_tributaria_doma": "Nit de la organización",
 "lbl_fecha_registro_doc_legal_2": "Fecha de registro en la Cámara de Comercio",
 "lbl_fecha_impresion_doc_legal_1": "Fecha de impresión del RUT (Registró Único Tributario)",
 "lbl_ingresa_fecha_impresion_doc_legal_1": "Ingresa la fecha de impresión del RUT (Registró Único Tributario)",
 "lbl_adjunta_doc_legal_1": "Adjunta el RUT (Registró Único Tributario)",
 "lbl_adjunta_doc_legal_2": "Adjunta el Certificado de Cámara de Comercio",
 "lbl_kilos_recoge_organizacion": "¿Cuántos Kilos puede recoger la organización?",
 "lbl_departamento": "Departamento",
 "lbl_indica_nit": "Indica tu NIT",
 "lbl_escribe_nit": "Escribe tu NIT",
 "todos_departamentos": "Todos los departamentos"
 } 

También es importante al momento de llenar el registro en la tabla cua_masters, llenar la columna “unique_identifier” como un JSON con la siguiente información (se toma como ejemplo el caso de Colombia - Abaco):  

 "{\\"type\\":\\"alphanumeric\\", \\"maxLength\\":\\"9\\", \\"verificationDigit\\":\\"required\\", \\"minLength\\":\\"9\\"}" 

 "},"searchablePlainTexts":{"code":""{\\"type\\":\\"alphanumeric\\", \\"maxLength\\":\\"9\\", \\"verificationDigit\\":\\"required\\", \\"minLength\\":\\"9\\"}""},"imageSources":{},"links":{}},"dataVersion":"2.0","properties":{"language":"JavaScript","lineNumbers":false,"lineWrapping":true,"theme":"Base16Light"},"containsDynamicDataSource":false}">

 "{"type":"alphanumeric", "maxLength":"9", "verificationDigit":"required", "minLength":"9"}" 

"{"type":"alphanumeric", "maxLength":"9", "verificationDigit":"required", "minLength":"9"}" 

Dónde “type” puede ser “alphanumeric” o “numeric” y “verificationDigit” puede ser “required” o “not_required”. 

 [{"UserId":17,"DisplayName":"Carlos Villa","LoginName":"carlos.villa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 {"SessionId":"a9c8d46e-10c5-4b90-bde3-4e70cea57d1a","SequenceId":1620,"FluidContainerCustomId":"eb45936c-1aae-45e4-8bae-b237c6f8115a","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 7df2a727-450a-41f0-a204-34a8d1a3236e 
 1!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 38ec5364-60b5-40e2-bea2-9b0544ad6436 
 2025-06-19T20:57:07.2344093Z 
 17;#i:0#.f|membership|carlos.villa@eatcloud.com 
 Carlos Villa 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 

 Configuración de paises y cua_masters