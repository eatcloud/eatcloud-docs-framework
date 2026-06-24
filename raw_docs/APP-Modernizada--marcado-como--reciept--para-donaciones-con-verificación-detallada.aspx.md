# APP-Modernizada--marcado-como--reciept--para-donaciones-con-verificación-detallada.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 APP Modernizada: marcado como "received" para donaciones con verificación detallada. "},"containsDynamicDataSource":false}">

Resumen:  
En este momento hay confusión con el proceso de “ marcado como recibida ” de las donaciones a partir del proceso de verificación detallada (dado que en legacy se estaban manejando dos condiciones para requerir o no la verificación del código de recogidan (una para el donante y otra para el beneficiario) para marcar las donaciones como “ recibidas ”).  Con el ánimo de obtener claridad al respecto, para garantizar una adecuada gestión de las mismas, se simplifica la documentación y se toman algunas medidas para clarificar muy bien el manejo del estado recibido.   NOTA Importante: esto funciona de manera similar para la verificación detallada por unidades y por pesos . 

Creación de un nuevo parámetro de configuración para las cua_user (en modernización) 
Se creará un nuevo parámetro de configuración en la “ cua_user ” “ received_without_code_verification ” (que inicialmente debe quedar en “ TRUE ” para estas cuentas modernizadas (las que hayan migrado: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si&_cmp=name)   

Edición de “eatc-receipt_datetime” 
Se debe tener en cuenta que este nombre, por como se desarrolló la plataforma, ya no es semántico, es decir, que puede inducir a confusiones.  Por lo tanto en adelante (aun el campo no esté declarado de esta manera) debería entenderse como eatc_detail_verification_datetime , es decir la fecha y hora de la verificación detallada.  Por ese motivo, cuando se realiza la verificación detallada, siempre se deberá estampar una fecha en “ eatc-receipt_datetime (que más bien se debería entender como eatc_detail_verification_datetime )” 
 {{url_donantes}}/crd/{{cua_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-receipt_datetime= {{datetime_stamp}} &WHEREeatc-code={{eatc_dona_headers. eatc-code }} 

Evaluaciones para marcar la donación como recibida. 
El sistema debe establecer que cuenta es el eatc-donor de la donación que se está verificando 

{{url_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= eatc-donor 

Para luego con ese dato ir al maestro de cua_users modernizado y evaluar lo siguiente: 

 received_without_code_verification =true 
En ese caso, dado que se indica que la cuenta usuario en cuestión puede recibir sin verificación del código de recogida , entonces siempre marcará la donación ( eatc-state ) con estado “recibida” ( received ) y el estado 3 ( eatc_state3 ) con “ Recibido ( receipt_without_code_verification_true ) ” para tener una indicación más específica de porqué la donación quedó como recibida sin la verificación del código de recogida (se agrega  ( receipt_without_code_verification_true ) . 
 {{url_donantes}}/crd/{{cua_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= received & eatc_state3= Recibido ( receipt_without_code_verification_true ) &WHEREeatc-code={{eatc_dona_headers. eatc-code }} 

 received_without_code_verification =false (vacío, o nulo) 
Si la cua_user evaluada tiene este (nuevo) parámetro en false , lo tiene vacío o nulo , entonces el sistema deberá validar dato eatc_code_verification_datetime :  

{{url_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= eatc_code_verification_datetime 

 eatc_code_verification_datetime con fecha válida 
Si en dicho dato existe una fecha válida (diferente a 0000-00-00 00:00:00) lo cuál quiere decir que a la donación el punto de donación ya le evaluó el código de recogida , entonces se cumplen las dos condiciones para dar por recibida la donación , por lo tanto la donación deberá cambiar su estado ( eatc-state ) a “recibida” ( received ) y el estado 3 ( eatc_state3 ) con “ Recibido ( receipt_without_code_verification_false ) ” (se agrega  ( receipt_without_code_verification_false ) para obtener más claridad desde el subestado) 
 {{url_donantes}}/crd/{{cua_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= received & eatc_state3= Recibido ( receipt_without_code_verification_false ) &WHEREeatc-code={{eatc_dona_headers. eatc-code }} 

 eatc_code_verification_datetime sin fecha válida 
Si en dicho dato no existe una fecha válida (es decir que es igual a 0000-00-00 00:00:00) lo cuál quiere decir que a la donación no se le ha validado su código de recogida por parte del pod , y por eso NO se cumplen las dos condiciones para dar por recibida la donación. Por lo tanto no se cambia el estado ( eatc-state ) de la donación (debería quedar en estado “ delivered ”) y el estado 3 ( eatc_state3 ) se marca con  “ Por validar ( receipt_without_code_verification_false ) ” (se agrega  ( receipt_without_code_verification_false ) para obtener más claridad desde el subestado) 
 {{url_donantes}}/crd/{{cua_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state= delivered & eatc_state3= Recibido ( receipt_without_code_verification_false ) &WHEREeatc-code={{eatc_dona_headers. eatc-code }} 

Edición de “eatc-picker_start_datetime”, “eatc-picking_checkin_datetime” y “eatc-picking_checkout_datetime” 
Para estampar estas fechas es que se requiere evaluar si el gestor de donaciones tiene o no habilitada la gestión simplificada de donaciones, consultando el parámetro “ sdm ” ( s implified d onation m anagement ). 

Evaluaciones para variar las fechas 
El sistema debe establecer el gestor de donaciones en cuestión: 

{{url_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= eatc-donation_manager_code 

Para luego con ese dato ir al maestro de donation_managers modernizado ( code ) y evaluar lo siguiente: 

 sdm =true 
En ese caso, dado que se indica que el beneficiario tiene gestión simplificada, entonces el sistema estampa la misma fecha y hora de la verificación detallada ( eatc-receipt_datetime ), como la fecha y hora de salida del recolector ( eatc-picker_start_datetime ), la fecha y hora de llegada al punto de donación ( eatc-picking_checkin_datetime ) y de salida ( eatc-picking_checkout_datetime ) del mismo. 
 {{url_donantes}}/crd/{{cua_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-picker_start_datetime = {{datetime_stamp}} & eatc-picking_checkin_datetime = {{datetime_stamp}} & eatc-picking_checkout_datetime = {{datetime_stamp}} &WHEREeatc-code={{eatc_dona_headers. eatc-code }} 
 sdm =false (vacío, o nulo) 
Si el beneficiario evaluado tiene este parámetro en false , lo tiene vacío o nulo , quiere decir que el mismo no tiene gestión simplificada de la donación y por lo tanto no debe modificar ninguna otra fecha (solamente el término del proceso de verificación detallada modificará la fecha “ eatc-receipt_datetime (que más bien se debería entender como eatc_detail_verification_datetime ) " como se estableció más arriba en esta documentación. (en otras palabras, no se realiza ninguna actualización adicional de datos del encabezado de donación) 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://media.akamai.odsp.cdn.office.net/_layouts/15/images/sitepagethumbnail.png, https://media.akamai.odsp.cdn.office.net/_layouts/15/images/sitepagethumbnail.png 

 86f67a7b-8644-4b76-9e8a-9991c6ba0363 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 b2187f56-a512-4e51-ae86-ea1e4c16fdd8 
 2026-02-14T03:33:19.6582172Z 

 {"SessionId":"94e2eabe-7642-4cc3-89f4-ab0e53ad3cbd","SequenceId":2128,"FluidContainerCustomId":"df3cb4b8-3349-4a05-915c-1e6fb0e11938","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"Off"},{"Name":"AIGeneratedDescription","Version":"Off"}] 

 APP Modernizada: marcado como "received" para donaciones con verificación detallada.