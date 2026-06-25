# WAPP-Modernizada--restricción-de-captura-de-fecha-de-vencimiento-a-partir-de-nuevo-parámetro-de-POD.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, para el funcionamiento de la WAP, se tiene un parámetro&#58; &#160;“ expiration_date_mandatory ”, que indica si la captura de la fecha de vencimiento es obligatoria o no . &#160;Por solicitud de ísimo, se requiere, que fuera de la condición de obligatoriedad, se configure la plataforma de tal manera que no permita tomar como fecha de vencimiento, la fecha actual. &#160;Por este motivo, se solicita adicionar un parámetro de configuración para los PODs (en modernización), que indique el número de días a partir del día actual, en los cuales no se pueda tomar la fecha de vencimiento. &#160;Este parámetro debe ser numérico y deberá indicar el número de días, contados a partir de la fecha actual, en los que el “date picker” estará deshabilitado. &#160; Por ejemplo, para el caso específico de isimo, se deberá configurar este parámetro nuevo en 1, de tal manera, que la funcionalidad de datepicker, entienda que la primera fecha habilitada para capturar la fecha de vencimiento, será el día actual + un día, y por lo tanto no permitirá capturar como fecha de vencimiento la del día actual. &#160;Cuando no existan datos, estén en cero o &#160;en nulo en este campo, entonces el sistema entenderá que podrá tomar como fecha de vencimiento la del día actual y por lo tanto habilitará dicha fecha en el datepicker respectivo. 
Parametro de configuración en PODs modernizado 
 Crear un nuevo parámetro de configuración (que puede llamarse&#58; “days_after_today_for_expiration_datepicker”) de caracter numérico (entero), en donde se pueda configurar un número de días, contados a partir del día actual, en los que se deshabilitarán las fechas para la toma de fecha de vencimiento. &#160;Inicialmente se debe configurar con el valor “1” para todos los pods de ISIMO. 
&#160; 
Funcionamiento del datepicker de fecha más próxima de vencimiento, a partir de la lectura del nuevo parámetro 
 Cuando un usuario de un POD esté en la aplicación tomando una donación, el sistema leerá el número que trae ese parámetro, y lo utilizará para deshabilitar en el datepicker, las fechas contadas a partir del día actual, como fechas válidas para dicha captura. 
 Por ejemplo, para el caso que inspiró esta solicitud, al tener todos los pods de isimo, el dato en 1, entonces el sistema contará 1 día a partir del actual y por lo tanto la primera fecha válidad para generar la captura de la fecha de vencimiento, será la de mañana. 
Como ejemplo adicional, en un segundo caso hipotético, si el pod tiene configurado el parámetro en 2, entonces el datepicker de la fecha de vencimiento no está activado, ni con la fecha de hoy, ni con la fecha de mañana, siendo la de pasado mañana la primera fecha válida para ser escogida como fecha de vencimiento. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 6930c0f6-5da2-42ff-bd6e-23fcf39e0172 
 4!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 669b78cc-de8a-4408-8115-de0107cb47d5 
 2026-01-30T03:16:40.5014574Z 

 {"SessionId":"5d94c160-6e6a-42a7-a968-a1427653a250","SequenceId":6475,"FluidContainerCustomId":"27d77d4a-a4ab-4487-8154-2e6fd849b047","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción de captura de fecha de vencimiento a partir de nuevo parámetro de POD