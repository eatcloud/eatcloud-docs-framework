# Cambio-de-estado-de-gestores-de-donaciones-de--inscritas--a--rechazadas-.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 JUSTIFICACIÓN DE LA NO DOCUMENTACIÓN COMO SERVICIO PÚBLICO 

 Este servicio no será invocado por ninguna plataforma, sino por un cronjob o similar, con el ánimo de evaluar en un día determinado si existen organizaciones en estado “inscritas” que puedan ser pasadas a estado “rechazadas”, por este motivo no se considera necesario (en primera instancia) documentar el servicio como uno público.  De todas maneras se recomienda incorporarle mecanismos de seguridad para que la invocación sea segura. 

 CRONJOB (o similar) para invocación del servicio: 
 Todos los días en horario nocturno, se deberá programar un Job, que por cuenta maestra dada de alta en el sistema 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua_master?_id=_*&_cmp= eatc_cua 
 Para cada cuenta maestra el sistema deberá realizar el siguiente llamado, para determinar los gestores de donación activos y pasivos, sobre los cuales opera el proceso  

 {{URL_entorno_beneficiarios}}/api/{{eatc_cua_master. eatc_cua }}/eatc_donation_managers?eatc_state= inscrito &_cmp= identificador_unico_registro 
Por cada identificador de beneficiario el sistema realizará un llamado (se deberá revisar si se pueden generar varios hilos de procesamiento paralelo, con el ánimo de poder generar datos de manera más rápida) 
 ENDPOINT PROPUESTO: 
 {{URL_entorno_datagov}}/ rejecteddoma 

 Se puede variar a elección del desarrollador si esto facilita la implementación. 

 Se propone incorporarle seguridad para su invocación (mediante envío de parámetros de autenticación en el encabezado). 

 PARÁMETROS QUE RECIBE EL SERVICIO: 
 eatc_date: 
 Fecha en formato AAAA-MM-DD a partir de la cual se quiere determinar que gestores de donaciones son rechazados => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra para la cual se invoca el servicio (eatc_cua_master. eatc_cua ) => parámetro de carácter obligatorio 

 identificador_unico_registro: 
 Identificador o código único de cada beneficiario al cual se le va a definir el estado  (eatc_donation_managers. identificador_unico_registro ) => parámetro de carácter obligatorio 

 CONSULTAS Y OPERACIONES QUE REALIZA EL SERVICIO PARA SU OPERACIÓN: 
Las siguientes consultas se deben realizar en el orden que el desarrollador considere más óptimo para el proceso, y por lo tanto el orden en que se presentan no es indicativo del orden en el algoritmo programado. 

 El sistema busca la carpeta en donde se suben los documentos legales solicitados en el onboarding 
 NUEVO: es importante consultar la carpeta como debe estar correctamente definida, y también, a manera de error handler, dado el bug recientemente detectado, que determinó que para las sucursales, se repetía el código de la sucursal en la carpeta, en las carpetas que puedan tener doble código de surcursal (con el ánimo de que el proceso funcione adecuadamente, aun si hay datos en carpetas mal configuradas) 
 El sistema busca en las carpetas los documentos legales solicitados en el oboarding 
 El sistema determina si en la carpeta (o las carpetas) existen los documentos legales que se exigen en el proceso de onboarding.  
 Si no existen dichos documentos en las carpetas 

 El sistema debe proceder a marcar como “rechazado” a la organización que estaba en estado “inscrito”: 

 {{URL_entorno_beneficiarios}}/crd/{{ eatc_cua_master }}/?_tabla=eatc_donation_managers&_operacion=update&eatc_state= rechazado &WHERE identificador_unico_registro ={{ identificador_unico_registro }} 

Escritura en el historial de cambio de estados del gestor de donaciones *** 
 El sistema deberá realizar la siguiente actualización de datos 

 {{ URL_entorno_datagov }}/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &_operacion= insert &eatc_code={{ eatc_code }}&eatc_date={{ eatc_date }}&eatc_datetime={{ eatc_datetime }}&eatc_cua_master={{_DOM. cua_master }}&eatc_doma_code = {{eatc_donation_managers .identificador_unico_registro }}&eatc_bo_user=eatcloud&eatc_doma_prev_state= inscrito &eatc_doma_new_state= rechazado &eatc_cause_code=automatic_process&eatc_notes= el gestor de donaciones fue rechazado por no haber adjuntado los documentos legales solicitados para su ingreso 

 Si existen dichos documentos en las carpetas 

 El sistema no realiza ninguna acción sobre el gestor de donaciones. 

 ENVÍO DE MENSAJE A GRUPO DE TELEGRAM CON INFORMACIÓN DEL Beneficiario rechazado 

Se debe enviar un mensaje con los datos básicos del gestor de donación rechazado (Nombre, identificador, teléfono, ciudad, provincia, dirección) anotando que fue un rechazo automático por no haberse encontrado documentos legales solicitados. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 Cambio de estado de gestores de donaciones de "inscritos" a "rechazados"