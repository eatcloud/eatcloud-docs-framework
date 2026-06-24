# configuración-de-horarios-de-venta.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Funcionalidad extendida de Configuracin de horarios de atencin , dnde simplemente se cambia el object store en el cual se guardan los datos, pero que tiene estructura similar al utilizado en la anterior funcionalidad (de eatc_attention_schedule de pasa a eatc_sale_schedule ) 

 Vista de tabla editable 
 Al ingresar a esta funcionalidad la plataforma generar una vista tipo tabla realizando la consulta respectiva de acuerdo al identificador nico del punto de donacin (eatc_pods) 
 Ejemplo consulta: 

 El punto de donacin "nzzn1" de la cuenta "colombia" desea entrar a la funcionalidad, cuando lo hace, se despliega una tabla con la siguiente informacin: 

 {{URL_entorno}}/api/ {{_DOM.cua_user} }/eatc_sale_schedule?eatc_pod_id={{eatc_pod_id}} 

Ambiente de pruebas: https://devdonantes.eatcloud.info/api/colombia/eatc_sale_schedule?eatc-pod_id=nzzn1 
Ambiente productivo: https://devdonantes.eatcloud.info/api/colombia/eatc_sale_schedule?eatc-pod_id=nzzn1 

 Tabla de horarios de atencin: 
 Para el anterior ejemplo se debe presentar una tabla con la siguiente estructura: 

Tabla_edicion_horarios_de_atencion 

 Edicin de registros 
 Esta tabla muestra datos no editables, solo cuando se oprime el smbolo de editar (que se convertir en un chulo para oprimir cuando , se permitir editar lo siguiente: 
 Hora de inicio : va desde las 00:00:00, hasta las 23:00:00 
 Hora fin : va desde la hora de inicio ms una hora, hasta las 23:59:00 
 Cuando se termina de editar, se hace clic en el botn que se convierte en un chulo, y haciendo esto, se hace el llamado al respectivo CRD para realizar el update del registro 
 Ejemplo: 
 Se edita el la hora de inicio y fin del da lunes, cambindola por 10:00:00 y 18:00:00 por lo tanto los parmetros sern los siguientes: 

 {{Parmetros}}: eatc-final_hour = 10:00:00& eatc-start_hour = 18:00:00 

 Y el llamado al CRD: 

 {{URL_entorno}}/crd/ {{_DOM.cua_user}} /?_tabla= eatc_sale_schedule &_operacion=update&{{parametros}}&WHERE_id={{_id}} 

 Ejemplo: cuenta "colombia" 
 Ambiente productivo: 
 https://donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &_operacion=update&{{parametros}}&WHERE_id={{_id}} 
 Ambiente de pruebas: 
 https://devdonantes.eatcloud.info/crd/colombia]/?_tabla= eatc_sale_schedule &_operacion=update&{{parametros}}&WHERE_id={{_id}} 
 y el registro editado se vuelve a colocar como no editable.  

 Borrado de registro 
 Cuando se hace clic en el botn respectivo, se hace el siguiente llamado al CRD 
 {{URL_entorno}}/crd/ {{_DOM.cua_user}} /?_tabla= eatc_sale_schedule &_operacion=delete&WHERE_id={{_id}} 

 Ejemplo: cuenta "colombia" 
 Ambiente productivo: https://donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &_operacion=delete&WHERE_id={{_id}} 
 Ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla= eatc_sale_schedule &_operacion=delete&WHERE_id={{_id}} 

 Nuevo registro 
 Cuando se oprime el botn "Nuevo registro" se despliega un formulario como el siguiente: 

Nuevo registro horario de atencin 

 El formulario deber implementar lo siguiente: 
 Da : el dropdown solo mostrar los das de la semana que no estn registrados en el respectivo registro de horario, con el motivo de evitar duplicar registros por da (dado el actual estado de implementacin) 
 Hora de inicio : va desde las 00:00:00, hasta las 23:00:00 
 Hora fin : va desde la hora de inicio ms una hora, hasta las 23:59:00 
 Ejemplo: 
 Se crea un registro para el da sbado con hora de inicio 10:00:00 y fin 14:00:00 por lo tanto los parmetros sern los siguientes: 

 {{Parmetros}}: eatc-day =DO& eatc-final_hour = 10:00:00& eatc-start_hour = 18:00:00& eatc-pod_id = nzzn1 

 Y el llamado al CRD: 
 {{URL_entorno}}crd/ {{_DOM.cua_user}} /?_tabla= eatc_sale_schedule &_operacion=insert&{{parametros}} 

 Ejemplo: cuenta "colombia" 
 Ambiente productivo: https://donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &_operacion=insert&{{parametros}}  
 Ambiente de pruebas: https://devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_sale _schedule &_operacion=insert&{{parametros}} ), 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx 

 CONFIGURACIN DE HORARIOS DE VENTA