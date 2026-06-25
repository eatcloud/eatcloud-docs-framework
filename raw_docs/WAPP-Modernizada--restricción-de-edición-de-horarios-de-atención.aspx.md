# WAPP-Modernizada--restricción-de-edición-de-horarios-de-atención.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad, en la WAPP se habilita para todos los usuarios la funcionalidad de “editar los horarios de atención”. &#160;Se han reportado casos en donde los usuarios del POD están editando horarios tan sumamente estrechos, que no permiten la gestión de las donaciones y esto puede configurarse en una mala práctica. &#160;Por eso se debe crear un nuevo parámetro de configuración (boleano) por cuenta POD &quot; edit_attention_schedules &quot; (por defecto en opción TRUE) que cuando esté marcado como “n” o “FALSE” (según como sea el estándar de implementación en modernización), no permitirá el despliegue de la funcionalidad que permite editar los horarios de atención. &#160;Al crear el nuevo parámetro o campo se deberá llenar por defecto con el dato “y” o “TRUE” según como sea el estándr de implementación en modernización) y solamente marcar como “n” o “FALSE” el correspondiente al POD &#160;“CARULLA EXPRESS SIBERIA” (no sin antes revisar que los horarios de atención configurados para ese punto cumplan con los estándares habituales para la cua_user exito (los más comunes). 
 Validación del parámetro de configuración para restringir la funcionalidad 
 Antes de desplegar el botón o los botones que permiten “editar los horarios de atención” a lo largo de la WAPP modernizada, el sistema deberá validar el parámetro &quot; edit_attention_schedules &quot;. &#160;Si el mismo para la respectiva cuenta usuario se encuentra en “n” o “FALSE”, entonces la WAPP no le desplegará el botón que permite editar los horarios de atención. &#160;Por el contrario si el valor del parámetro se encuentra en “s” o “TRUE” entonces la WAPP permitirá el despliegue del botón y la funcionalidad. &#160;Esto no aplicará para la primera vez que se editen los horarios de atención, antes de hacer la primera donación, acción que debe ser obligatoria, pero para evitar malas prácticas de entrada, también se incorporará la siguiente restricción 
&#160; 
Nueva restricción para la configuración de horarios de atención 
 Para evitar de entrada malas prácticas, también se deberá contemplar que la funcionalidad inicial de configuración de horarios &#160;de atención y también en la de edición de los mismos (para usuarios con parámetro &quot; edit_attention_schedules &quot; en TRUE ) , el sistema no permitirá cerrar la funcionalidad ni realizar configuraciones si no ocurre lo siguiente&#58; 

 Que los horarios de atención por día sean de mínimo 2 horas&#58; si en el datepicker se intenta colocar un horario de menos de dos horas, se deberá indicar al usuario que el tiempo mínimo de atención por día es de 2 horas y no dejarlo continuar hasta que corrija. 

 Que como mínimo se tengan tres días de atención a la semana (de preferencia en días hábiles y espaciados uniformemente). &#160;Si el sistema, no detecta como mínimo este tipo de configuración, le debe indicar al usuario que como mínimo se deben configurar tres días de atención a la semana en días hábiles y espaciados de manera uniforme (de preferencia&#58; lunes, miércoles y viernes o a lo sumo&#58; martes, jueves y sábado) y no dejarlo terminar hasta que la configuración sea puesta de esta manera. 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 ec2d800a-426e-4c2c-9bd1-8754faf346a2 
 3!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 443a2f72-c536-4e44-a5ba-b2d1781214f3 
 2026-01-31T00:06:32.4063682Z 

 {"SessionId":"2472d004-1081-41aa-a7d7-2bfe60af9b94","SequenceId":4764,"FluidContainerCustomId":"146881e5-8728-4107-b837-2d89779bddb6","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: restricción de edición de horarios de atención