# Onboarding-PODs--activación-por-periodo-de-tiempo.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripción general 
Al crear el PODs, en el proceso de onboarding, debe existir una parametrización, que le permita al donante establecer un rango de fechas en el cuál el POD va a tener activo el servicio. Es decir, el formulario de onboarding, deberá tener una captura de información opcional de fecha inicial y fecha final de activación. Cuando un POD tenga esta información registrada, el sistema lo activará entre esas dos fechas y lo desactivará si la fecha está por fuera de las mismas. &#160;De igual manera se deberá llevar un registro de quién cambió dichas fechas y cómo se cambiaron, de tal manera que en el maestro de pods se encuentren las vigentes, pero en un registro a parte se puedan guardar cada vez que se cambiaron dichas fechas. 
&#160; 
En todos los casos este periodo de inactivación (el que esté por fuera de las fechas de inicio y fin de actividad), permitirá que el usuario acceda al pod, pero que no pueda utilizar la plataforma para realizar donaciones. 
&#160; 
 Ajuste del formulario público y formulario de edición de pods&#58; 
Se deberá incluir una pregunta ¿Desea activar el punto de donación por fechas? cuyo valor por defecto sea “no”. En caso de que el usuario seleccione la opción “si”, el formulario deberá permitirle desplegar un par de date pickers de la siguiente manera 
 Fecha inicial&#58; 
Valor por defecto el día actual, podrá moverse hacia el futuro (no hacia el pasado) y debe ser obligatoria 
 Fecha final&#58; 
Valor por defecto una semana después de la fecha seleccionada en el selector inicial. &#160;Debe permitir mover hacia el futuro, y hasta dos días después de la fecha inicial. Captura obligatoria. 
&#160; 
 NOTA IMPORTANTE&#58; este mismo ajuste se deberá habilitar para los perfiles de EatCloud que administran PODs, de tal manera que usuarios EatCloud puedan hacer dicha configuración. 
&#160; 
 Ajuste al maestro de pods&#58; 
Adicional a estos nuevos campos, se deberá poder guardar el usuario que hizo el cambio en las fechas y cuándo las cambió. 
&#160; 
 Persistencia para guardar datos de auditoría de estos cambios 
Se deberá crear una tabla adicional en donde se guarde la fecha del cambio, el usuario que haga un cambio y cuales fueron las fechas que cambio (fechas inicial y final configuradas). &#160;Esto a efectos de auditoría. 
&#160; 
 Ajuste al listado de pods en el BO donantes&#58; 
En el listado de pods del donante, cuando un pod tenga registros en la fecha de inicio y fin de activación, y la fecha actual esté por fuera de ese rango, el sistema deberá indicar que el POD está inactivo (y deberá proveer una herramienta para activarlo, bien sea borrando dichas fechas o variándolas). 
&#160; 
 Ajuste&#160;a la WAPP 
Para los PODs que tengan registros de fecha de inicio y fin de activación, deberá permitírseles el ingreso a los usuarios, pero si se ingresa en una fecha que no esté dentro del rango de actividad, deberá mostrarle un letrero vistoso que indique que el POD está inactivo, y no se le deberá permitir utilizar las funcionalidades de creación de donaciones (y otras transacciones) y gestión de las mismas. &#160;Se deberá permitir que el POD genere una solicitud de activación que llegue a la mesa de servicio (soporte@eatcloud.com). 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 3c0b165a-fc19-4429-8bb3-c1aa2e2d4bb3 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 8482a295-39bb-4134-a1cb-6e954b90f02a 
 2025-08-27T04:27:14.5840103Z 

 {"SessionId":"518981a0-0e92-4fcc-aca9-3e255a915665","SequenceId":7980,"FluidContainerCustomId":"3152d2a6-a565-4230-8a78-be2b57b757b9","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Onboarding PODs: activación por periodo de tiempo