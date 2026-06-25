# timeouts.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La presente documentación se realiza para analizar todos planteamientos sobre los timeouts realizados a lo largo de los requisitos. 

 dona_global_scheduling_timeout 
&#160; 
 Utilidad&#58; 
 Sirve para limitar el tiempo entre la publicación de un anuncio y la fecha y hora de recogida que se programa. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 96 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_global_scheduling_timeout )&#160; 
 BAMX &#58; 96 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_global_scheduling_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Programar recogida de anuncio de donación 
 Reprogramar recogida de anuncio de donación 
 Check-in express (mejora para establecer un tiempo máximo, o límite superior&#160; para realizar el check-in extemporáneo) =&gt; Pendiente de implementación 
 Registro / modificación de información de incidencia =&gt; Pendiente de implementación 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 dona_particular_scheduling_timeout 
&#160; 
 Utilidad&#58; 
 Sirve para establecer el tiempo máximo entre la adjudicación del anuncio y su programación. Si una donación, después de ser adjudicada, no se programa en este lapso de tiempo, la misma será liberada automáticamente por el sistema. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_particular_scheduling_timeout )&#160;&#160; 
 BAMX &#58; 2 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_particular_scheduling_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Liberación de anuncios de donación 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=dona_particular_scheduling_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 non_award_alert 
&#160; 
 Utilidad&#58; 
 Sirve para generar alertas cuando un anuncio no ha sido adjudicado después de un tiempo específico, contado a partir de la publicación del anuncio. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 3 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_*&amp;eatc-timeout_name=non_award_alert ) =&gt; Se crea este valor automáticamente cuando se crea una cuenta.&#160;&#160; 
 BAMX &#58; 3 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=non_award_alert )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso Casedb para creación de cuentas 
 Proceso Mensajería de alerta para anuncios no adjudicados 
 Cargadores Proceso manual de consulta de existencia de registro para creación de cuenta 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=non_award_alert &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 non_picking_alert 
&#160; 
 Utilidad&#58; 
 Sirve para generar alertas cuando un anuncio no ha sido recogido después de un lapso de tiempo contado a partir de su fecha y hora de recogida programada. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=non_picking_alert )&#160; 
 BAMX &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=non_picking_alert )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso Mensajería de alerta para anuncios que no han sido recogidos 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=non_picking_alert &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 checkin_timeout 
&#160; 
 Utilidad&#58; 
 Sirve para determinar el tiempo máximo después de la fecha y hora de recogida programada, para registrar la fecha y hora de check-in, utilizando la fecha y hora actual del dispositivo ( ***FUNCIONALIDAD PENDIENTE DE IMPLEMENTACIÓN*** &#58;&#160; a partir de lapso de tiempo se podrá registrar una fecha y hora diferente a la fecha y hora del dispositivo ). 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=checkin_timeout )&#160;&#160; 
 BAMX &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=checkin_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Check-in express =&gt; Pendiente de implementación 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=checkin_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 checkout_timeout 
&#160; 
 Utilidad&#58; 
 Sirve establecer un tiempo máximo entre el check-in y el check-out y permitir generar alertas. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 4 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=checkout_timeout )&#160;&#160;&#160; 
 BAMX &#58; 4 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=checkout_timeout )&#160;&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Registro de hora de salida =&gt; Pendiente de implementación de mejoras relacionadas 
 Mensajería para promover el registro de la hora de salida 
 Mensajes emergentes si el check-out no se hace según lo establecido en las reglas de timeouts 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=checkout_timeout&#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 verification_timeout 
&#160; 
 Utilidad&#58; 
 Sirve establecer un tiempo máximo entre el check-out y la verificación detallada de la donación para generación de alertas. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 2 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=verification_timeout )&#160;&#160;&#160;&#160; 
 BAMX &#58; 2 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=verification_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Mensajería para promover la verificación de anuncios 

&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=verification_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 dona_cancellation_timeout 
&#160; 
 Utilidad&#58; 
 Sirve para establecer el tiempo máximo entre la generación de un anuncio y su cancelación automática por parte del sistema. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 48 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_cancellation_timeout )&#160; 
 BAMX &#58; 48 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_cancellation_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso Escritura del dato eatc_cancellation_datetime en el encabezado de anuncio de donación 
 Creación manual de anuncios de donación&#58; Validación de horario de atención disponible antes del rango de cancelación del anuncio 
 Proceso Cancelación de anuncios de donación 
&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=dona_cancellation_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 dona_nng_cancellation_timeout 
&#160; 
 Utilidad&#58; 
 Sirve para establecer el tiempo máximo entre la generación de un anuncio y su cancelación para mercancía no negociada. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 96 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_nng_cancellation_timeout )&#160; 
 BAMX &#58; 96 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_nng_cancellation_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso Escritura del dato eatc_cancellation_datetime en el encabezado de anuncio de donación 
&#160; 
 Ideas de mejora&#58; 
 No se observa que el timeout tenga que estar solamente asociado a la cuenta maestra abaco, razón por la cual se puede analizar trasladar la estructura de timeouts a una cuenta general (como puede ser https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_timeout_rules?eatc-timeout_name=dona_nng_cancellation_timeout &#160; y documentar las tareas para la consulta a la estructura de datos nueva). 

 ***NUEVO&#58; dona_aut_closing_timeout *** 
&#160; 
 Utilidad&#58; 
 Sirve para establecer el tiempo máximo entre la fecha de recogida programada y el cierre automático de las donaciones. 
&#160; 
 Valores por defecto&#58; 
 ABACO &#58; 8 días, 192 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_aut_closing_timeout )&#160; 
 BAMX &#58; 8 días, 192 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_aut_closing_timeout )&#160; 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso Cierre automático de anuncios de donación 
&#160; 
 Ideas de mejora&#58; 
 En una segunda etapa, implementar un parámetro por kilometraje, que varíe de acuerdo a la distancia que debe recorrer el recolector para recoger la donación. 

 ***NUEVO&#58; dona_libdona_from_scheduled *** 
 Utilidad&#58; 
 Sirve para establecer el tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada . 
 Valores por defecto&#58; 
 ABACO &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_libdona_from_scheduled )&#160; 
 BAMX &#58; 1 hora ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_libdona_from_scheduled )&#160; 
 Funcionalidades en las que se emplea&#58; 
 Liberación de donaciones 
&#160; 

 ***NUEVO&#58; dona_not_delivered_from_scheduled *** 
 Utilidad&#58; 
 Sirve para establecer el tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada . 
 Valores por defecto&#58; 
 ABACO &#58; 2 horas ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_not_delivered_from_scheduled )&#160; 
 BAMX &#58; 2 horas ( https&#58;//donantes.eatcloud.info/api/mexico/eatc_timeout_rules?cua=_default&amp;eatc-timeout_name=dona_not_delivered_from_scheduled )&#160; 
 Funcionalidades en las que se emplea&#58; 
 WAPP&#58; Botón de marcar como no entregado 
&#160; 

 DEPRECADO&#58; eatc_doma_typolgy_b 
&#160; 
 Utilidad&#58; 
 Sirve para establecer procesos de match escalonado a partir de la tipología_b de los gestores de donación. 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Proceso de Match escalonado 
&#160; 
 Ideas de mejora&#58; 
 Cuando se documentó la aplicación de este&#160; timeout en el match escalonado, se estableció sensibilidad con respecto a las cuentas maestras, por este motivo, en la configuración de una cuenta maestra se deberá llevar el valor default definido y configurar allí los diversos timeouts. 

 sale_timeout (deprecado) 
&#160; 
 Utilidad&#58; 
 Tiempo máximo para vender un producto de último minuto 
&#160; 
 Funcionalidades en las que se emplea&#58; 
 Ninguna (se cambió por las reglas de timeout específicas para eatc_sale) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 ba363bc8-b8a0-48bf-b3b1-501dfa770ae2 
 4!1!3 
 https://centralus0-0.pushfp.svc.ms/fluid 
 33de31d2-ddc1-4aec-b231-d79ee9109bbd 
 2026-06-17T23:25:24.5195836Z 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-17T15:44:34.1645891Z"}] 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"3ab1a4e6-fc4a-47bc-9480-460025f60fdc","SequenceId":193,"FluidContainerCustomId":"3b464824-322c-4354-8a9c-7d18702a8050","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 TIMEOUTS