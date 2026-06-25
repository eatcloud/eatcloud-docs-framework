# ENRIQUECIMIENTO-DE-eatc_dona_headers.eatc_state3.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En reiteradas ocasiones Abaco y los bancos de alimentos nos han solicitado que para las donaciones en estado “delivered”, se pueda establecer porqué no han pasado a estado “received”&#58; 

 Por falta de gestión del donante&#58; no ha validado el código de recolección, es decir&#58; no hay una fecha válida en el campo “ eatc_code_verification_datetime ” 

 Por falta de gestión del beneficiario&#58; no ha realizado la verificación detallada de la donación, es decir&#58; no hay una fecha válida en el campo “ eatc-receipt_datetime ” 
&#160; 
 Por este motivo se solicita generar un proceso de base de datos (trigger, procedimiento almacenado), que permita en el campo “eatc_state3”, colocar estos dos estados, más el estado combinado de falta de gestión y el estado con gestión completa, evaluando las siguientes condiciones&#58; 
&#160; 

 falta_gestion_donante &#58; eatc-state = delivered y eatc_code_verification_datetime= 0000-00-00 00&#58;00&#58;00 (independiente de lo demás) 

 falta_gestion_beneficiario &#58; eatc-state = delivered y eatc-receipt_datetime= 0000-00-00 00&#58;00&#58;00 (independiente de lo demás) 

 falta_gestion_donante_y_beneficiario &#58; eatc-state = delivered y eatc_code_verification_datetime= 0000-00-00 00&#58;00&#58;00 y eatc-receipt_datetime= 0000-00-00 00&#58;00&#58;00&#160; 

 gestion_recogida_completa &#58; eatc-state = recieved (que es lo mismo que&#58; eatc_code_verification_datetime diferente de 0000-00-00 00&#58;00&#58;00 y eatc-receipt_datetime diferente de&#160; 0000-00-00 00&#58;00&#58;00 ) 
&#160; 
 Condiciones para disparar la evaluación que cambia el dato del campo 

 Cambio de estado de “scheduled” a “ delivered ” (o simplemente cambio de estado a “ delivered ”) 

 Ingreso de una fecha válida (diferente a 0000-00-00 00&#58;00&#58;00) en el campo eatc_code_verification_datetime 

 Ingreso de una fecha válida (diferente a 0000-00-00 00&#58;00&#58;00) en el campo eatc-receipt_datetime 

 Cambio de estado de “delivered” a “ recieved ” (o simplemente cambio de estado a “ recieved ”) 
&#160; 
&#160; 
&#160; 
 Incorporación del dato eatc_dona_headers_state3 a los informes de encabezados y detalles de donantes y beneficiarios 
 Una vez realizada la programación del proceso de base de datos, se deberá incorporar el dato eatc_state_3 en los informes de detalle y encabezado de los BO de donantes y Beneficiarios (iniciando por estos últimos) 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 d3946fc2-576e-4f9c-a306-33eb26174f35 
 4!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 7db7f72f-8e67-4126-9aad-5af28bcaf196 
 2025-10-24T05:52:08.0360229Z 

 {"SessionId":"ea73081a-e6e8-4074-a42b-7c52b2052103","SequenceId":805,"FluidContainerCustomId":"209d4087-69cc-44e4-bc11-2b4ec62ad896","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 ENRIQUECIMIENTO DE eatc_dona_headers.eatc_state3