# BO-donantes--informes-de-data-analítica--incorporar-filtro-por-eatc_do.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Contexto general: 
Se nos ha solicitado que en los informes del datagov_cuentas en lo concerniente a Analytics, se incorpore un nuevo filtro, que permita ver información por “NIT” de donante.  Por lo tanto en los diversos informes y presentación de estadísticas, se deberá incorporar (para las cuentas que tengan el parámetro “ eatc_cua. multiple_donors ” con el dato “si”, para el caso de legacy y su respectiva concordancia en modernización), un selector que se alimente de su selector de NITs. 
{{URL_donantes}}/ap/{{cua_user}}/eatc_multiple_donors_info?_id=_*  

 ( para legacy y su estructura equivalente en modernización ) 

La información deberá filtrarse por este nuevo parámetro, enviándolo como dato al parámetro 

  eatc_dona_headers. eatc-donor_code para el caso de informes que tengan que ver con datos de donaciones,  

 eatc_dona. eatc_donor_code para el caso de informes de detalles, y  

 eatc_dona_kpi. eatc_donor_code para los informes relativos a KPIs. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 d5748b85-20e2-4526-801d-6c0e798de89e 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 8926a7a2-e7b9-4c45-b5a6-cd05a2ad408f 
 2025-04-26T05:37:32.5121334Z 

 {"SessionId":"ce002e36-8d98-4d5c-b4d9-c643795aac68","SequenceId":2473,"FluidContainerCustomId":"674f5a62-9ad8-4c1a-8338-906ca6efd99b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 BO donantes: informes de data analítica: incorporar filtro por eatc-donor_code