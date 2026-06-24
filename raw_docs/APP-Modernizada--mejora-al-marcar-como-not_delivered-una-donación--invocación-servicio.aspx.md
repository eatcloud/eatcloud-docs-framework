# APP-Modernizada--mejora-al-marcar-como-not_delivered-una-donación--invocación-servicio.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 En la actualidad, para donaciones en estado “scheduled” se despliega el siguiente botón: 

Tengo problemas con la entrega (con una lógica que se detalla aquí ) 

Al invocar dicha funcionalidad, el sistema realiza varias acciones, a saber: 

Despliegue de instrucciones ante una no entrega: según parámetro de configuración diferenciado por cua_user: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#instrucciones-ante-una-no-entrega-despliegue   

Despliegue de datos de comunicación con Soporte Técnico: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#datos-para-comunicaci%C3%B3n-con-soporte   

Llamado al API pública para notificación de una no entrega: aunque esto se hace hasta el final (después que se acciona la funcionalidad que a continuación se relata: Registro de no entrega), se documenta aquí, porque esto debe seguir funcionando igual: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#***nuevo-llamado-al-api-p%C3%BAblica-para-enviar-un-mensaje-de-notificaci%C3%B3n-ante-una-no-entrega***   

Despliegue de la funcionalidad: Registro de no entrega : https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#***nuevo-habilitar-funcionalidad-de-registro-de-no-entrega*** que a su vez tiene estos componentes: 

Despliegue de formulario con motivo de no entrega: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#motivo-de-no-entrega   

Este formulario tiene como principal funcionalidad, establecer “cuando una donación fue mal entregada ( wrongly_delivered )” y en ese caso tratar de obtener información para que los datos de entrega correspondan a la realidad.  Es por eso que cuando una donación es marcada con motivo “ wrongly_delivered ”, se realiza lo siguiente:  

1 - Despliegue de formulario para capturar datos de quién recibió la donación y cuándo lo hizo. 
2 - Registro en el log “ eatc_checkin_and_deliver_issues ”: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#registro-en-eatc_checkin_and_deliver_issues-cuando-la-causa-es-wrongly_delivered 
 3 - Cambio de los datos de la donación para incorporar la nueva información de entrega de la misma: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#actualizaci%C3%B3n-de-informaci%C3%B3n-de-encabezados-de-donaci%C3%B3n-cuando-la-causa-es-wrongly_delivered-***revisar-dinamismo-a-partir-de-_d   
 4 - Registro en el historial de estados: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#registro-de-informaci%C3%B3n-en-la-tabla-de-historial-de-los-estados-de-los-anuncios-de-donaciones-(eatc_dona_header_state_history)-c-1   

 Hasta aquí debe permanecer todo igual.  Ahora bien, cuando la causa es diferente a “ wrongly_delivered ”, entonces el sistema deberá realizar lo siguiente ( se anota en rojo lo que hacía antes , para diferenciarlo de este nuevo planteamiento): 

 1 - NO se despliega formulario para captura de información adicional sobre quién y cuándo pudo recibir la donación (sigue tal como estaba) 
 2 - Registro en el log “ eatc_checkin_and_deliver_issues ”: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx#registro-en-eatc_checkin_and_deliver_issues-cuando-la-causa-es-diferente-a-wrongly_delivered   
 3 - ***NUEVO: invocación del servicio “ cnebdona ”: 
 Anteriormente, en este punto directamente se afectaban los datos de la donación y del historial de cambio de estado de las donaciones .  Esto se va a reemplazar por la invocación del API Pública para cancelación, no entrega y borrado de donaciones cuya documentación se encuentra aquí .  Los parámetros de invocación del servicio serán: 

 Endpoints 
 URL ambiente de pruebas: https://devdonantes.eatcloud.info/cnebdona 

 URL ambiente productivo: https://donantes.eatcloud.info/cnebdona 

 Credenciales de acceso 
 Usuario : el mismo usuario con el que se accede a la APP beneficiarios 
 Password : el mismo password con el que se accede a la APP beneficiarios 

 Parámetros de invocación del servicio 

 _plataform = app   ***constante 
 _cuamaster= {{_DOM. cua_master }} 
 _cuauser   = {{eatc_dona_headers. eatc_cua_origin }}    ***cuenta origen de la donación que se está marcando como not_delivered 
 _doma= {{eatc_dona_headers. eatc-donation_manager_code }}    ***identificador_unico_registro del beneficiario que está marcando como not_delivered 
 _operation= not_delivered ***constante 
 eatc-code = {{eatc_dona_headers. eatc-code }}    ***código de la donación que se está marcando como not_delivered 
 eatc-state2 = not_delivered_registered_by_doma   ***constante 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 3bd8abfd-6e3c-4142-afff-60752d6f8dc7 
 3!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 ff203e71-28bd-4b1f-a9dd-ab53b14506a4 
 2025-09-19T04:36:55.3711445Z 

 {"SessionId":"b2f1e899-a419-416b-9eab-d0971cbd79b9","SequenceId":14,"FluidContainerCustomId":"b8700fed-40f2-44bf-83ee-1d5296b9de95","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 APP Modernizada: mejora al marcar como not_delivered una donación: invocación servicio "cnebdona"