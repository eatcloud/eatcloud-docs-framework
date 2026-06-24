# BO-Beneficiarios-(perfil-líder-de-ecosistema--ABACO)--Reporte-de-generación-de-certificado-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación:  
Originalmente se solicitó este reporte para el BO Gobierno, pero  eso nos traería complicaciones, dado que a ese BO tienen acceso personas por fuera de ABACO que no deben tener relación con la funcionalidad de creación de certificados de donación. 

Por este motivo, esta funcionalidad es un buen pretexto para comenzar con el desarrollo modernizado del BO Beneficiarios, y en concreto del perfil de ABACO.  Por lo tanto este perfil de líder de ecosistema social, también deberá tener acceso a todos los informes que en este momento están en el BO de territorio circunscritos a Colombia y permitir también el ingreso a esta nueva funcionalidad 

 Titulo de la vista: Reporte de generación de certificados de donación. 
 Descripción del informe 
Informe que permite visualizar por donante que pre-certificados ha realizado y cuantos ABACO les ha certificado 

 Filtro de cua_user 
Selector múltiple de cuentas usuario (con opción de seleccionar todas), que mostrará aquellas cuentas que se les ha generado certificados. 
 Filtro de fechas 
El sistema presentará campos de captura para obtener la fecha inicial y final 
 Fecha inicial 
Tipo: date 
Input: {{fecha_inicial}} 
Validación: campo requerido.  Debe ser inferior a la fecha final 
 Fecha final 
Tipo: date 
Input: {{fecha_final}} 
Validación: campo requerido.  Debe ser superior a la fecha final 
 Filtro de cua_user 
Selector múltiple de cuentas usuario, que mostrará aquellas cuentas que se les ha generado certificados en el periodo consultado 

 Filtro por estado de aprobación (label:  class="lbl_filtro_aprobacion) 
 Aplica sobre los valores contenidos en  eatc_dona_certifications . eatc_certification_datetime . Los selectores para el filtro serán : 

 Pendientes de aprobación (label:  class=" lbl_pendientes_aprobacion " ) : al presionarlo, traerá los certificados que no contengan una fecha válida en  eatc_dona_certifications . eatc_certification_datetime  (para el periodo de tiempo seleccionado en el filtro por fecha) 

 Aprobados (label:  class=" lbl_aprobados " ) : al presionarlo, traerá los certificados que tienen una fecha válida en  eatc_dona_certifications . eatc_certification_datetime   (para el periodo de tiempo seleccionado en el fltro por fecha) 

 Todos   (label:  class=" lbl_todos " ) : Será el valor por defecto y trae todos los certificados, mostrando primero los pendientes de aprobación con fecha más antigua. 
 Botón consultar Consultar 
 Al oprimir el botón el sistema consultará los datos para armar el informe. 

 Estructura del informe: similar al que se construyó para datagov_cuentas. 
El informe será en estructura y datos, similar al que se implementó para datagov_cuentas, y que se puede consultar aquí . 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 67117dca-e103-4fb8-9e70-2c178b96da8e 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 4c6c815f-3778-43de-b4fa-772a137b022b 
 2025-08-01T06:45:01.5460160Z 

 {"SessionId":"fac65d57-7f2e-4182-b4ce-2cd295119fd4","SequenceId":96,"FluidContainerCustomId":"cb9278d2-15e4-46d4-8a10-fb5841cc7964","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"Off"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 BO Beneficiarios (perfil líder de ecosistema: ABACO): Reporte de generación de certificado de donación