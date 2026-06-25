# new-configuración-de-horarios-de-venta.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Funcionalidad extendida de Configuracin de horarios de atencin , dnde simplemente se cambia el object store en el cual se guardan los datos, pero que tiene estructura similar al utilizado en la anterior funcionalidad (de eatc_attention_schedule de pasa a eatc_sale_schedule ) 
&#160; 
 Vista de tabla editable 
 Al ingresar a esta funcionalidad la plataforma generar una vista tipo tabla realizando la consulta respectiva de acuerdo al identificador nico del punto de donacin (eatc_pods) 
 Ejemplo consulta&#58; 
&#160; 
 El punto de donacin &quot;nzzn1&quot; de la cuenta &quot;colombia&quot; desea entrar a la funcionalidad, cuando lo hace, se despliega una tabla con la siguiente informacin&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/ &#123;&#123;_DOM.cua_user&#125; &#125;/eatc_sale_schedule?eatc_pod_id=&#123;&#123;eatc_pod_id&#125;&#125; 
&#160; 
Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_schedule?eatc-pod_id=nzzn1 
Ambiente productivo&#58; https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_schedule?eatc-pod_id=nzzn1 

&#160; 
 Tabla de horarios de atencin&#58; 
 Para el anterior ejemplo se debe presentar una tabla con la siguiente estructura&#58; 

Tabla_edicion_horarios_de_atencion 

 Edicin de registros 
 Esta tabla muestra datos no editables, solo cuando se oprime el smbolo de editar (que se convertir en un chulo para oprimir cuando , se permitir editar lo siguiente&#58; 
 Hora de inicio &#58; va desde las 00&#58;00&#58;00, hasta las 23&#58;00&#58;00 
 Hora fin &#58; va desde la hora de inicio ms una hora, hasta las 23&#58;59&#58;00 
&#160; 
 Cuando se termina de editar, se hace clic en el botn que se convierte en un chulo, y haciendo esto, se hace el llamado al respectivo CRD para realizar el update del registro 
&#160; 
 Ejemplo&#58; 
 Se edita el la hora de inicio y fin del da lunes, cambindola por 10&#58;00&#58;00 y 18&#58;00&#58;00 por lo tanto los parmetros sern los siguientes&#58; 
&#160; 
 &#123;&#123;Parmetros&#125;&#125;&#58; eatc-final_hour = 10&#58;00&#58;00&amp; eatc-start_hour = 18&#58;00&#58;00 
&#160; 
 Y el llamado al CRD&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/crd/ &#123;&#123;_DOM.cua_user&#125;&#125; /?_tabla= eatc_sale_schedule &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 Ejemplo&#58; cuenta &quot;colombia&quot; 
 Ambiente productivo&#58; 
 https&#58;//donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
 Ambiente de pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/crd/colombia]/?_tabla= eatc_sale_schedule &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 y el registro editado se vuelve a colocar como no editable.&#160; 
&#160; 
 Borrado de registro 
 Cuando se hace clic en el botn respectivo, se hace el siguiente llamado al CRD 
 &#123;&#123;URL_entorno&#125;&#125;/crd/ &#123;&#123;_DOM.cua_user&#125;&#125; /?_tabla= eatc_sale_schedule &amp;_operacion=delete&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 Ejemplo&#58; cuenta &quot;colombia&quot; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &amp;_operacion=delete&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/crd/exito/?_tabla= eatc_sale_schedule &amp;_operacion=delete&amp;WHERE_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 Nuevo registro 
 Cuando se oprime el botn &quot;Nuevo registro&quot; se despliega un formulario como el siguiente&#58; 

Nuevo registro horario de atencin 

 El formulario deber implementar lo siguiente&#58; 
 Da &#58; el dropdown solo mostrar los das de la semana que no estn registrados en el respectivo registro de horario, con el motivo de evitar duplicar registros por da (dado el actual estado de implementacin) 
 Hora de inicio &#58; va desde las 00&#58;00&#58;00, hasta las 23&#58;00&#58;00 
 Hora fin &#58; va desde la hora de inicio ms una hora, hasta las 23&#58;59&#58;00 
 Ejemplo&#58; 
 Se crea un registro para el da sbado con hora de inicio 10&#58;00&#58;00 y fin 14&#58;00&#58;00 por lo tanto los parmetros sern los siguientes&#58; 
&#160; 
 &#123;&#123;Parmetros&#125;&#125;&#58; eatc-day =DO&amp; eatc-final_hour = 10&#58;00&#58;00&amp; eatc-start_hour = 18&#58;00&#58;00&amp; eatc-pod_id = nzzn1 
&#160; 
 Y el llamado al CRD&#58; 
 &#123;&#123;URL_entorno&#125;&#125;crd/ &#123;&#123;_DOM.cua_user&#125;&#125; /?_tabla= eatc_sale_schedule &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
 Ejemplo&#58; cuenta &quot;colombia&quot; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/crd/colombia/?_tabla= eatc_sale_schedule &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125;&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_sale _schedule &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; ), 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FTabla_edicion_horarios_de_atencion.pptx 

 CONFIGURACIN DE HORARIOS DE VENTA