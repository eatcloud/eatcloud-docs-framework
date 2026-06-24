# configuración-de-horarios-de-atención.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Vista de tabla editable 
 Al ingresar a esta funcionalidad la plataforma generará una vista tipo tabla realizando la consulta respectiva de acuerdo al identificador único del punto de donación (eatc_pods) 
 Ejemplo consulta: 

 El punto de donación "nzzn1" de la cuenta "colombia" desea entrar a la funcionalidad, cuando lo hace, se despliega una tabla con la siguiente información: 

 Implementación inicial: 
Ambiente de pruebas: https://devdonantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id=nzzn1 

Ambiente productivo: https://devdonantes.eatcloud.info/api/exito/eatc_attention_schedule?eatc-pod_id=nzzn1 

 ***Verificar que se esté guardando la información en este nuevo object store (en simultáneo con el legacy) y dinamizar con respecto a _DOM.cua_user*** 
 Implementación definitiva: 

 {{URL_entorno_donantes}}/api/ {{_DOM.cua_user}} /eatc_attention_schedule?eatc-pod_id={{eatc-pod_id}} 

 Ejemplo: cuenta colombia: 
Ambiente de pruebas: https://devdonantes.eatcloud.info/api/colombia/eatc_attention_schedule?eatc-pod_id=nzzn1   
Ambiente productivo: https://devdonantes.eatcloud.info/api/colombia/eatc_attention_schedule?eatc-pod_id=nzzn1   

 Tabla de horarios de atención: 
 Para el anterior ejemplo se debe presentar una tabla con la siguiente estructura: 

Tabla_edicion_horarios_de_atencion 

 Edición de registros 
 Esta tabla muestra datos no editables, solo cuando se oprime el símbolo de editar (que se convertirá en un chulo para oprimir cuando , se permitirá editar lo siguiente: 
 Hora de inicio : va desde las 00:00:00, hasta las 23:00:00 
 Hora fin : va desde la hora de inicio más una hora, hasta las 23:59:00 

 Cuando se termina de editar, se hace clic en el botón que se convierte en un chulo, y haciendo esto, se hace el llamado al respectivo CRD para realizar el update del registro: 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada:  

 {{URL_entorno_donantes}}/crd/ {{_DOM.cua_user}} /?_tabla=eatc_attention _schedule &_operacion=update&{{parametros}}&WHERE_id={{_id}} 

 Ejemplo: cuenta maestra "abaco", ambiente productivo 

 Se edita el la hora de inicio y fin del día lunes, cambiándola por 10:00:00 y 18:00:00 por lo tanto los parámetros serán los siguientes: 

 [Parámetros]: eatc-final_hour = 10:00:00& eatc-start_hour = 18:00:00 

 Y el llamado al CRD: 

 Fase inicial: en la estructura legacy 
 Se deberá utilizar la estructura que se utiliza en este momento para hacer el registro respectivo: https://donantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=update&[parametros]&WHERE_id=[_id] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=update&[parametros]&WHERE_id=[_id] ) 

 Fase definitiva: en la estructura definitiva 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada: https://donantes.eatcloud.info/crd/[user_CUA=colombia]/?_tabla=eatc_attention _schedule &_operacion=update&[parametros]&WHERE_id=[_id] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=update&[parametros]&WHERE_id=[_id] ), 
 y el registro editado se vuelve a colocar como no editable.  

 Borrado de registro 
 Cuando se hace clic en el botón respectivo, se hace el siguiente llamado al CRD 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada:  

 {{URL_entorno_donantes}}/crd/ {{_DOM.cua_user}} /?_tabla=eatc_attention _schedule &_operacion=delete&WHERE_id={{_id}} 

 Fase inicial: en la estructura legacy 
 Se deberá utilizar la estructura que se utiliza en este momento para hacer el registro respectivo: https://donantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=delete&WHERE_id=[_id] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=delete&WHERE_id=[_id] ) 

 Fase definitiva: en la estructura definitiva 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada   
 : https://donantes.eatcloud.info/crd/[user_CUA=colombia]/?_tabla=eatc_attention _schedule &_operacion=delete&WHERE_id=[_id] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=delete&WHERE_id=[_id ] ), 

 Nuevo registro 
 Cuando se oprime el botón "Nuevo registro" se despliega un formulario como el siguiente: 

Nuevo registro horario de atención 

 El formulario deberá implementar lo siguiente: 
 Día : el dropdown solo mostrará los días de la semana que no están registrados en el respectivo registro de horario, con el motivo de evitar duplicar registros por día (dado el actual estado de implementación) 
 Hora de inicio : va desde las 00:00:00, hasta las 23:00:00 
 Hora fin : va desde la hora de inicio más una hora, hasta las 23:59:00 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada:  

 {{URL_entorno_donantes}}/crd/ {{_DOM.cua_user}} /?_tabla=eatc_attention _schedule &_operacion=insert&{{parametros}} 

 Ejemplo: 
 Se crea un registro para el día sábado con hora de inicio 10:00:00 y fin 14:00:00 por lo tanto los parámetros serán los siguientes: 

 {{Parámetros}}: eatc-day =DO& eatc-final_hour = 10:00:00& eatc-start_hour = 18:00:00& eatc-pod_id = nzzn1 

 Y el llamado al CRD: 
 Fase inicial: en la estructura legacy: 
 Se deberá utilizar la estructura que se utiliza en este momento para hacer el registro respectivo: https://donantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=insert&[parametros] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=insert&[parametros ] ), 
 Fase definitiva: en la estructura definitiva 
 Esto se realizará cuando la tarea: https://app.asana.com/0/698639369029630/1164232107266018 esté completada   
 : https://donantes.eatcloud.info/crd/[user_CUA=colombia]/?_tabla=eatc_attention _schedule &_operacion=insert&[parametros] (ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_attention _schedule &_operacion=insert&[parametros ] ), 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx 

 CONFIGURACIÓN DE HORARIOS DE ATENCIÓN