# APP-Modernizada--mejora-filtro-por-defecto-en-mis-elegidas-.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 APP Modernizada: mejora filtro por defecto en mis elegidas" "},"containsDynamicDataSource":false}">

Resumen: 
 En la actualidad, en los filtros por defecto de mis elegidas se están mostrando todas las donaciones con estado "awarded", "scheduled" y "delivered".  La mejora va a consistir que se muestren en primera instancia (tanto en la burbuja de mis elegidas, como en el listado por defecto cuando se abre "mis elegidas") solo las donaciones que están pendientes de gestión por parte del beneficiario, es decir, las "awarded", las "scheduled" y las "delivered" que tengan en el campo "eatc-receipt_datetime" no tengan una fecha válida (lo cual quiere decir que el no ha realizado la verificación detallada de la misma).   

Consulta para mostrar el número de la burbuja de mis elegidas 
El sistema deberá realizar la siguiente consulta 

{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{code}}&eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime=0000-00-00 00:00:00 &_cont 

Consulta para mostrar las donaciones pendientes de gestión en mis elegidas 
El sistema deberá realizar las siguientes consultas para mostrar primero las pendientes por programar, segundo las prendientes por recoger y tercero las pendientes por la verificación detallada de la donación 

Pendientes por programar: 

{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{code}}&eatc-state=awarded 
Pendientes por recoger: 

{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{code}}&eatc-state=scheduled 
Pendientes por verificación detallada: 

{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{code}}&eatc-state=delivered& eatc-receipt_datetime=0000-00-00 00:00:00 
Hasta aquí las donaciones que se deben mostrar en el filtro por defecto de mis elegidas (cuando se oprime el botón desde las diferentes vistas de la app) 

Nuevo filtro en mis elegidas => NO DEBEN APARECER EN LA VISTA POR DEFECTO DE MIS ELEGIDAS 
Se deberá crear un nuevo filtro en mis elegidas, que le permita visualizar al beneficiario las donaciones que él ya gestionó, pero que sigen en estado “delivered” por falta de gestión del donante.  Para mostrar estas donaciones deberá aplicar el siguiente filtro:  

{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-donation_manager_code={{code}}&eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime= ! 0000-00-00 00:00:00 &_cont 

 MUY IMPORTANTE : estas donaciones NO DEBEN APARECER en el Filtro por defecto de MIS ELEGIDAS . 

Filosóficamente es importante entender que la vista por defecto de mis elegidas debe estar optimizada para que los beneficiarios encuentren rápidamente las donaciones que tienen pendiente su gestión, es decir aquellas en estado awarded (les falta la programación de recogida), scheduled (les falta la recogida) y delivered con eatc-receipt_datetime=0000-00-00 00:00:00 (les falta la verificación detallada de la donación).  Las demás donaciones (incluidas las delivered con una fecha válida en eatc-receipt_datetime que es lo mismo que eatc-receipt_datetime = ! 0000-00-00 00:00:00), no les deben aparecer en la vista por defecto , pero podrían ser accesibles a través de filtros (como el que se describe en este punto) 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 d11576e7-8b09-429f-b4f6-fa995abda3e7 
 4!1!3 
 https://centralus0-0.pushfp.svc.ms/fluid 
 613b4f41-9247-4c77-9b0e-da8f6259308e 
 2026-03-11T00:53:51.1383216Z 

 {"SessionId":"af08b9d4-2754-4422-b3e7-f4b3dffedf2e","SequenceId":954,"FluidContainerCustomId":"d8748523-1cc5-4465-98e8-ccee3b41c679","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"Off"}] 

 APP Modernizada: mejora filtro por defecto en mis elegidas"