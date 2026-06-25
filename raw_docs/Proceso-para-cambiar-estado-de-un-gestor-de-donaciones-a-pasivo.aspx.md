# Proceso-para-cambiar-estado-de-un-gestor-de-donaciones-a-pasivo.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 JUSTIFICACIÓN DE LA NO DOCUMENTACIÓN COMO SERVICIO PÚBLICO 
&#160; 
 Este servicio no será invocado por ninguna plataforma, sino por un cronjob o similar, con el ánimo de evaluar en un día determinado si existen organizaciones que se pueden determinar como (pasivas), por este motivo no se considera necesario (en primera instancia) documentar el servicio como uno público.&#160; De todas maneras se recomienda incorporarle mecanismos de seguridad para que la invocación sea segura. 

 CRONJOB (o similar) para invocación del servicio&#58; 
 Todos los días en horario nocturno, se deberá programar un Job, que por cuenta maestra dada de alta en el sistema 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?_id=_*&amp;_cmp= eatc_cua,eatc_pasive_doma_days 
 Para cada cuenta maestra el sistema deberá realizar el siguiente llamado, para determinar los gestores de donación activos y pasivos, sobre los cuales opera el proceso&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_donation_managers?eatc_state= activo,pasivo &amp;_cmp= identificador_unico_registro 
Por cada identificador de beneficiario el sistema realizará un llamado (se deberá revisar si se pueden generar varios hilos de procesamiento paralelo, con el ánimo de poder generar datos de manera más rápida) 
 ENDPOINT PROPUESTO&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/ pasivedoma 
&#160; 
 Se puede variar a elección del desarrollador si esto facilita la implementación. 
&#160; 
 Se propone incorporarle seguridad para su invocación (mediante envío de parámetros de autenticación en el encabezado). 

&#160; 
 PARÁMETROS QUE RECIBE EL SERVICIO&#58; 
 eatc_date&#58; 
 Fecha en formato AAAA-MM-DD a partir de la cual se quiere determinar que gestores de donaciones son pasivos =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra para la cual se invoca el servicio (eatc_cua_master. eatc_cua ) =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_pasive_doma_days&#58; 
 Número de días que por cuenta maestra sirven para definir que un gestor de donaciones es pasivo &#160;(eatc_cua_master. eatc_pasive_days ) =&gt; parámetro de carácter obligatorio 
&#160; 
 identificador_unico_registro&#58; 
 Identificador o código único de cada beneficiario al cual se le va a definir el estado &#160;(eatc_donation_managers. identificador_unico_registro ) =&gt; parámetro de carácter obligatorio 
&#160; 
&#160; 

 CONSULTAS Y OPERACIONES QUE REALIZA EL SERVICIO PARA SU OPERACIÓN&#58; 
Las siguientes consultas se deben realizar en el orden que el desarrollador considere más óptimo para el proceso, y por lo tanto el orden en que se presentan no es indicativo del orden en el algoritmo programado. 
&#160; 
Se considera que una organización es pasiva, cuando a partir de la fecha indicada en la invocación del servicio ( eatc_date ) &#160;contando hacia atrás el periodo de días o eatc_pasive_days (indicado también en la invocación del servicio), una organización cuyo estado es “activo”, no posee gestión de donaciones registrada en el sistema. &#160; 
&#160; 
 ***NUEVO &#58; no se marcarán com “pasivas” aquellas organizaciones cuya diferencia entre eatc_donation_managers.fecha1 y la fecha actual, no ha superado el tiempo definido en eatc_pasive_days *** 
 NUEVO&#58; el proceso como se definió inicialmente solamente operará para aquellas organizaciones, que han sido creadas y que al comparar la fecha de creación con la fecha actual, ya se ha superado el tiempo indicado en eatc_pasive_days , esto con el fin que las organizaciones nuevas, no queden automáticamente como “pasivas” dado que aun no han tenido un tiempo prudencial para gestionar donaciones (dicho tiempo prudencial será igual al definido en el parámetro eatc_pasive_days ) 
&#160; 
 El sistema no le cambiará el estado a &#160;pasivo a las organizaciones cuyo periodo de tiempo de haber sido creadas en la plataforma no supera al tiempo definido en eatc_pasive_days , por lo tanto a las organizaciones que cumplan con esta condición 
&#160; 
 &#123;&#123; eatc_pasive_days &#125;&#125; &gt; &#123;&#123;fecha_actual&#125;&#125; - &#123;&#123;eatc_donation_managers. fecha1 &#125;&#125;&#160; 
No podrán ser marcadas como pasivas, y deben ser excluidas del proceso que a continuación se especifica (y que ya fue implementado) 
 Determinación de fecha inicial de consulta (eatc-publication_date[0]) para la consulta de actividad de los gestores de donaciones)&#58; 
 Con los datos recibidos el los parámetros de invocación del servicio&#58; 
&#160; 
 eatc_date 
 eatc_pasive_doma_days 
&#160; 
El sistema deberá calcular la fecha incial de consulta, de la siguiente manera&#58; 
&#160; 
 &#123;&#123; fecha_inicial_consulta &#125;&#125; = &#123;&#123;eatc_date&#125;&#125; - &#123;&#123;eatc_pasive_doma_days&#125;&#125;&#160; 
&#160; 
Ejemplo ambiente de pruebas&#58; eatc_date=2024-07-01 y eatc_pasive_doma_days=90 &#58; 
El sistema realiza la siguiente operación para calcular la fecha incial de consulta 
 &#123;&#123; fecha_inicial_consulta &#125;&#125; = 2024-07-01 - 90 días = 2024-04-01 (aprox)&#160; 
&#160; 
 Consulta de las donaciones gestionadas para determinar si el gestor de donaciones es activo o inactivo 
 Con los datos obtenidos en la anterior operación&#160; 
 fecha_inicial_consulta 
 y los datos recibidos en la invocación del servicio 
 eatc_date 
 eatc_cua_master 
 identificador_unico_registro 
&#160; 
El sistema realiza la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc_cua_master &#125;&#125;/eatc_dona_headers? eatc-donation_manager_code =&#123;&#123; identificador_unico_registro &#125;&#125;&amp; eatc-publication_date [0]= &#123;&#123; fecha_inicial_consulta &#125;&#125; &amp; eatc-publication_date [1]= &#123;&#123; eatc_date &#125;&#125; &amp;_cont 
 Si la respuesta es cero , entonces se debe marcar al beneficiario con el estado pasivo 
&#160; 
 Cuando no se encuentran anuncios gestionados en el periodo determinado por la anterior consulta, entonces el sistema debe actualizar el estado del beneficiario a “pasivo” con el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123; eatc_cua_master &#125;&#125;/?_tabla=eatc_donation_managers&amp;_operacion=update&amp;eatc_state= pasivo &amp;WHERE identificador_unico_registro =&#123;&#123; identificador_unico_registro &#125;&#125; 
 ***NUEVO &#58; escritura en el historial de cambio de estados del gestor de donaciones *** 
 El sistema deberá realizar la siguiente actualización de datos 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; eatc_code &#125;&#125;&amp;eatc_date=&#123;&#123; eatc_date &#125;&#125;&amp;eatc_datetime=&#123;&#123; eatc_datetime &#125;&#125;&amp;eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user=eatcloud&amp;eatc_doma_prev_state= activo &amp;eatc_doma_new_state= pasivo &amp;eatc_cause_code=automatic_process&amp;eatc_notes=el gestor de donaciones fue inactivado porque no ha gestionado donaciones en los últimos &#123;&#123; eatc_pasive_days &#125;&#125; 
&#160; 
 Si la respuesta es mayor que cero, entonces se debe marcar al beneficiario con el estado activo 
&#160; 
 Cuando se encuentran anuncios gestionados en el periodo determinado por la anterior consulta, entonces el sistema debe actualizar el estado del beneficiario a “activo” con el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123; eatc_cua_master &#125;&#125;/?_tabla=eatc_donation_managers&amp;_operacion=update&amp;eatc_state= activo &amp;WHERE identificador_unico_registro =&#123;&#123; identificador_unico_registro &#125;&#125; 
&#160; 
 ***NUEVO &#58; escritura en el historial de cambio de estados del gestor de donaciones *** 
 El sistema deberá realizar la siguiente actualización de datos 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud / ?_tabla= eatc_doma_state_change_history &amp;_operacion= insert &amp;eatc_code=&#123;&#123; eatc_code &#125;&#125;&amp;eatc_date=&#123;&#123; eatc_date &#125;&#125;&amp;eatc_datetime=&#123;&#123; eatc_datetime &#125;&#125;&amp;eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_doma_code = &#123;&#123;eatc_donation_managers .identificador_unico_registro &#125;&#125;&amp;eatc_bo_user=eatcloud&amp;eatc_doma_prev_state= pasivo &amp;eatc_doma_new_state= activo &amp;eatc_cause_code= automatic_process &amp;eatc_notes= el gestor de donaciones fue activado porque ha gestionado donaciones en los últimos &#123;&#123; eatc_pasive_days &#125;&#125; 
&#160; 
&#160; 

 ENVÍO DE MENSAJE A GRUPO DE TELEGRAM CON INFORMACIÓN DEL Beneficiario inactivo 
&#160; 
Se debe enviar un mensaje con los datos básicos del gestor de donación inactivo (Nombre, identificador, teléfono, ciudad, provincia, dirección) de los gestores de donación que pasan a estado “pasivo” 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 Proceso para cambiar estado de un gestor de donaciones a "pasivo" o a "activo"