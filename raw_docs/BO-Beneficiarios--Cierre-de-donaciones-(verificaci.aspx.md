# BO-Beneficiarios--Cierre-de-donaciones-(verificaci.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación:  
Se ha solicitado que se habilite en el BO para el perfil de beneficiarios, la posibilidad de cerrar donaciones, es decir, que puedan realizar verificación detallada de las mismas con acciones bulk (para poder hacer acciones de verificación por lote).  Esta implementación corresponde a la misma que se está realizando en la APP modernizada.  Por ese motivo el desarrollo debe basarse en ese desarrollo (de ser posible debe ser la misma funcionalidad), y operará para cada beneficiario que ingrese al sistema, de la misma manera como operaría en la APP. 

 Titulo de la vista: Cierre de donaciones - Verificación detallada. 
 Descripción 
Funcionalidad que permitirá realizar la verificación detallada de las donaciones con posibilidad de acciones en lote, es decir por grupo de donaciones. 

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
 Botón consultar Consultar 
 Al oprimir el botón el sistema consultará los datos para desplegar la funcionalidad. 

 Estructura de la funcionalidad: similar a la implementación en la APP Modern 
La funcionalidad debe ser similar a la implementación de la funcionalidad de verificación detallada de la donación como se puede   consultar aquí . 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/media.akamai.odsp.cdn.office.net/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/media.akamai.odsp.cdn.office.net/_layouts/15/images/sitepagethumbnail.png 

 24961db6-20a0-4e37-b477-792c69a60b5b 
 1!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 d6852647-87a8-4dea-952d-5f8b2c0e331f 
 2025-08-02T05:36:23.2821852Z 

 {"SessionId":"2bb87803-cbd9-440c-8cbf-529bb5aefacf","SequenceId":15,"FluidContainerCustomId":"e878cfa9-4388-49d7-9888-1fb88e2d595c","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 BO Beneficiarios: Cierre de donaciones (verificación detallada con funciones bulk)