# new-liberación-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La presente implementación implica el despliegue un selector de causal de liberación, y con esta información y con cierta información de la donación en cuestión, se hace el llamado al servicio de liberación de donaciones . 

 Validación de condiciones para el despliegue de la funcionalidad NO SE HAN IMPLEMENTADO (QUEDAN EN STANBY) 
 Al igual que el botón de despliega la funcionalidad, se deben realizar las siguientes consultas y validaciones para desplegar la funcionalidad (se referencia a documentación previamente desarrollada mediante los vínculos y así evitar duplicidad en la documentación)&#58; 
 Consulta para donaciones con eatc-state= scheduled =&gt; Validación de fechas para donaciones con eatc-state= scheduled &#58; 
 Consulta para donaciones con eatc-state= cancelled =&gt; Validación de fechas para donaciones con eatc-state= cancelled &#58;&#160; 
&#160; 
 ***Nuevo*** DONACIÓN Con estado &quot; SCHEDULED &quot;&#58; Determinación si la fecha actual es anterior a la fecha de recogida programada más un TIMEOUT, para mostrar o no el BOTÓN &quot; Liberar donación &quot; 
Despliegue del botón a partir del timeout “ dona_libdona_from_scheduled ” 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable a la&#160; &#123;&#123;cua_user&#125;&#125; &#160;respectiva 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua= &#123;&#123;cua_user&#125;&#125; &amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
Si no hay respuesta, entonces se deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
 En caso de no tener una respuesta del servicio, entonces dejar como valor por defecto 1 hora (quemado en el código) 
&#160; 
 Ejemplo cuenta maestra abaco en ambiente de pruebas &#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_libdona_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
 res &#58; 
 [ 
 &#123; 
 eatc-timeout_description &#58; &quot;Tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada&quot; , 
 eatc-timeout_in_minutes &#58; &quot;30&quot; , 
 eatc-timeout_in_hours &#58; &quot;0,5&quot; , 
 eatc-timeout_from &#58; &quot;eatc-programed_picking_datetime&quot; 
 &#125; 
 ], 
 Si la consulta no arroja respuesta, se tomará como valor por defecto&#58; 
 eatc-timeout_in_minutes &#58; &quot;30&quot; , 
 eatc-timeout_in_hours &#58; &quot;0,5&quot; , 
&#160; 
 Es decir que este timeout indica un tiempo mínimo que se debe esperar antes de poder liberar la donación contado a partir de la fecha de recogida programada. 
&#160; 
 El sistema deberá determinar, a la hora consultar la donación y que la misma aparezca en el listado de donaciones , ese tiempo mínimo ha transcurrido o no. 

&#160; 
 El tiempo mínimo no ha transcurrido&#58; 
 Esto quiere decir que la fecha y hora actual es anterior (está en el pasado) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;fecha_hora_actual&#125;&#125; &lt; &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; 
&#160; 
 Si el tiempo mínimo no ha transcurrido, NO SE PODRÁ MOSTRAR EL BOTÓN &quot; Liberar donación &quot; en la WAPP, y por lo tanto el anuncio no se podrá liberar. 

&#160; 
 El tiempo mínimo ya se cumplió&#58; 
 Esto quiere decir que la fecha y hora actual es posterior (está en el futuro) a la fecha y hora resultante de la sumatoria de la fecha de recogida programada y el timeout 
&#160; 
 &#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &#125;&#125; + &#123;&#123; eatc-timeout_in_hours/eatc-timeout_in_minutes &#125;&#125; &lt; &#123;&#123;fecha_hora_actual&#125;&#125; 
&#160; 
 Si el tiempo mínimo ya transcurrió, entonces se deberá Mostrar el botón &quot; Liberar donación &quot; y al accionarse, seguir el proceso&#58; &quot; Selección de causales de liberación &quot;.&#160; El funcionamiento será similar ( con una pequeña variante en la consulta de los causales ) a la implementación actual. En el siguiente vínculo se detalla el funcionamiento . 

&#160; 
 BOTÓN&#58; EDITAR DONACIÓN 
 Label 
 class=&quot; lbl_editar_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_editar_donacion )&#160;&#160; 
&#160; 
 Este botón deberá dar acceso a la funcionalidad de &quot; Edición de donación &quot; (en el caso de donaciones canceladas, se debe modificar la regla que aplica para permitir la edición de la donación, de tal manera que permita la edición de donaciones canceladas). 

&#160; 
 DONACIONES CANCELADAS&#58; SELECCIONA UN CAUSAL DE LIBERACIÓN 
 Label del título 
 class=&quot; lbl_selecciona_causal_liberación &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_selecciona_causal_liberación )&#160;&#160; 
&#160; 
 Selector único 
 Valor por defecto 
 Vacío (ninguno seleccionado) 
 Valores del selector 
 El sistema, tomando el estado de la donación ( eatc_dona_headers. eatc-state ), realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_release_causes?eatc_cua_master= _default &amp;eatc_cua_user= _default &amp;eatc_dona_state= cancelled &amp;_cmp=eatc_name,eatc_cause_label 
 En principio se realiza el llamado con para cua_master y eatc_cua_user = _default (se deja la puerta para que posteriormente se pueda dinamizar por eatc_cua_master y eatc_cua_user ). 
 Se coloca como &quot; class &quot; (para la internacionalización de las etiquetas de las opciones) el valor contenido en eatc_dona_ralease_causes. eatc_cause_label y el valor entre los tags eatc_dona_ralease_causes. eatc_name 

&#160; 
 Ejemplo&#58; ambiente de producción, cua_master&#58; abaco , eatc-state= cancelled 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_release_causes?eatc_cua_master=_default&amp;eatc_cua_user=_default&amp;eatc_dona_state=cancelled&amp;_cmp=eatc_name,eatc_cause_label &#160; 
&#160; 
 Por lo tanto las opciones que se desplegarán son&#58; 
 Toda la mercancía apta para el consumo humano ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_toda_dona_ok )&#160;&#160; 
 La mayor parte de la mercancía apta para el consumo humano ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_casi_toda_dona_ok )&#160; 
&#160; 
 Valores a guardar a partir de la selección para posterior llamado al servicio 
 A partir de la selección del usuario el sistema guardará el valor contenido en eatc_dona_release_causes. eatc_cause_label como valor para hacer el posterior llamado al servicio de liberación. 

&#160; 
 Botón &quot;Confirmar liberación&quot; 
 class=&quot; lbl_confirmar_liberacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirmar_liberacion )&#160;&#160; 
 Al oprimir el botón, y con la información del Punto de donación, la donación y la causal de liberación el sistema deberá llamar al servicio de liberación de anuncios tal cual se especifica en la documentación del servicio público (se incorporan parámetros de autenticación en la cabecera del llamado). 

&#160; 
 DONACIONES PROGRAMADAS&#58; LA FECHA Y HORA DE RECOGIDA PROGRAMADA MÁS UN TIMEOUT ESTÁ EN EL PASADO&#58;&#160; 
 Selecciona un causal de liberación ( ***NUEVO &#58; Parámetro adicional de búsqueda de causales *** ) 
 Nota para el desarrollo&#58; la implementación de esta funcionalidad es totalmente idéntica a la ya implementada, simplemente se enviará un parámetro adicional en la búsqueda de causales para traer causales específicas que aplican cuando se libera la donación y ya ha pasado la fecha y hora programada de recogida. 
&#160; 
 Label del título 
 class=&quot; lbl_selecciona_causal_liberación &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_selecciona_causal_liberación )&#160;&#160; 
&#160; 
 Selector único 
 Valor por defecto 
 Vacío (ninguno seleccionado) 
&#160; 
 Valores del selector 
 El sistema, tomando el estado de la donación ( eatc_dona_headers. eatc-state ), realiza la siguiente consulta (Se incorpora un nuevo parámetro de consulta&#58; before_eatc_programed_picking_datetime= n )&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_release_causes?eatc_cua_master= _default &amp;eatc_cua_user= _default &amp;eatc_dona_state= scheduled &amp; before_eatc_programed_picking_datetime= n &amp;_cmp=eatc_name,eatc_cause_label 
&#160; 
 En principio se realiza el llamado con para cua_master y eatc_cua_user = _default (se deja la puerta para que posteriormente se pueda dinamizar por eatc_cua_master y eatc_cua_user ). 
&#160; 
 Se coloca como &quot; class &quot; (para la internacionalización de las etiquetas de las opciones) el valor contenido en eatc_dona_ralease_causes. eatc_cause_label y el valor entre los tags eatc_dona_ralease_causes. eatc_name 
&#160; 
 Ejemplo&#58; ambiente de pruebas, cua_master&#58; abaco , eatc-state= scheduled 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_dona_release_causes?eatc_cua_master=_default&amp;eatc_cua_user=_default&amp;eatc_dona_state= scheduled&amp;before_eatc_programed_picking_datetime=n &amp;_cmp=eatc_name,eatc_cause_label &#160; 
&#160; 
 Por lo tanto las opciones que se desplegarán son&#58; 
 El beneficiario no se presentó ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_doma_no_se_presento )&#160;&#160; 
 El beneficiario no fue admitido ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_doma_no_admitido )&#160; 
&#160; 
 Valores a guardar a partir de la selección para posterior llamado al servicio 
 A partir de la selección del usuario el sistema guardará el valor contenido en eatc_dona_release_causes. eatc_cause_label como valor para hacer el posterior llamado al servicio de liberación. 
&#160; 
 Botón &quot;Confirmar liberación&quot; 
 class=&quot; lbl_confirmar_liberacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirmar_liberacion )&#160;&#160; 
&#160; 
 Al oprimir el botón, y con la información del Punto de donación, la donación y la causal de liberación el sistema deberá llamar al servicio de liberación de anuncios tal cual se especifica en la documentación del servicio público (se incorporan parámetros de autenticación en la cabecera del llamado). 

&#160; 
 ***NUEVO&#58; DONACIONES PROGRAMADAS&#58; LA FECHA Y HORA DE RECOGIDA PROGRAMADA MÁS UN TIMEOUT, ESTÁS EN EL FUTURO*** 
&#160; 
 No se podrá efectuar la liberación de la donación, por lo tanto se debe volver al listado del anuncio, sin hacer ninguna acción sobre la donación. 
&#160; 
 DEPRECADO***NUEVO&#58; Funcionamiento con más alertas y validaciones***) 
 Nota para el desarrollo&#58; A diferencia de la implementación anterior, en este caso el sistema desplegará muchos más mensajes de alerta y confirmaciones, para lograr que el punto de donación solo utilice esta opción en casos bien justificados y con mucho conocimiento de causa. 
&#160; 
 Alerta al ingresar a la funcionalidad 
 Label del título&#58; Atención 
 class=&quot; lbl_atencion &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_atencion_libdona_before_ppdt )&#160;&#160; 
&#160; 
 Label del cuerpo&#58; Atención 
 class=&quot; lbl_atencion_libdona_before_ppdt &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_atencion_libdona_before_ppdt ) 
&#160; 
 &quot;¡Vas a liberar una donación antes de la fecha y hora programada para su entrega! Esto implica la posibilidad que un beneficiario se encuentre en camino para acá y pierda su venida. Por favor utiliza esta opción solo en casos extraordinarios que así lo ameriten. ¿Deseas Continuar? 
&#160; 
 Botón&#58; NO 
 class=&quot; lbl_no &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_no ) 
&#160; 
 Al presionar este botón la funcionalidad retorna al listado de donaciones (desde donde fue invocada la funcionalidad de liberación), y no realiza ninguna acción. 
&#160; 
 Botón&#58; SI 
 class=&quot; lbl_si &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_si ) 
&#160; 
 Al presionar este botón, se desplegará el selector único que se detalla a continuación. 
&#160; 
 Selector único 
 Valor por defecto 
 Vacío (ninguno seleccionado) 
&#160; 
 Valores del selector 
 El sistema, tomando el estado de la donación ( eatc_dona_headers. eatc-state ), realiza la siguiente consulta (Se incorpora un nuevo parámetro de consulta&#58; before_eatc_programed_picking_datetime=y )&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_release_causes?eatc_cua_master= _default &amp;eatc_cua_user= _default &amp;eatc_dona_state= scheduled&amp;before_eatc_programed_picking_datetime=y &amp;_cmp=eatc_name,eatc_cause_label 
&#160; 
 En principio se realiza el llamado con para cua_master y eatc_cua_user = _default (se deja la puerta para que posteriormente se pueda dinamizar por eatc_cua_master y eatc_cua_user ). 
&#160; 
 Se coloca como &quot; class &quot; (para la internacionalización de las etiquetas de las opciones) el valor contenido en eatc_dona_ralease_causes. eatc_cause_label y el valor entre los tags eatc_dona_ralease_causes. eatc_name 
&#160; 
 Ejemplo&#58; ambiente de pruebas, cua_master&#58; abaco , eatc-state= scheduled 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_dona_release_causes?eatc_cua_master=_default&amp;eatc_cua_user=_default&amp;eatc_dona_state= scheduled&amp;before_eatc_programed_picking_datetime=y &amp;_cmp=eatc_name,eatc_cause_label 
&#160; 
 Por lo tanto las opciones que se desplegarán son&#58; 
 El beneficiario ha incumplido antes ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_beneficiario_ha_incumplido )&#160;&#160; 
 l beneficiario no cumple con los requisitos para entregarle ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_beneficiario_sin_requisitos )&#160; 
 Preferimos no entregar más donaciones a ese beneficiario ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_bloqueo_pod_beneficiario )&#160; 

&#160; 
 Valores a guardar a partir de la selección para posterior llamado al servicio 
 A partir de la selección del usuario el sistema guardará el valor contenido en eatc_dona_release_causes. eatc_cause_label como valor para hacer el posterior llamado al servicio de liberación. 
&#160; 
 Botón &quot;Confirmar liberación&quot; 
 class=&quot; lbl_confirmar_liberacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirmar_liberacion )&#160;&#160; 
&#160; 
 Al oprimir este botón se desplegará una segunda alerta de la siguiente manera&#58; 
&#160; 
 Alerta de confirmación 
 Label del título&#58; Atención 
 class=&quot; lbl_atencion &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_atencion_libdona_before_ppdt )&#160;&#160; 
&#160; 
 Label del cuerpo&#58; Atención 
 class=&quot; lbl_atencion_libdona_before_ppdt_2 &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_atencion_libdona_before_ppdt_2 ) 
&#160; 
 &quot;Te invitamos que solo utilices esta opción en casos muy extremos ya que con esta acción puedes estar haciéndole perder el tiempo a un gestor de donaciones que lo necesita para atender a su comunidad. ¿Deseas confirmar esta acción? 
&#160; 
 Botón&#58; NO 
 class=&quot; lbl_no &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_no ) 
&#160; 
 Al presionar este botón, la funcionalidad retorna al listado de donaciones (desde donde fue invocada la funcionalidad de liberación), y no realiza ninguna acción. 
&#160; 
 Botón&#58; SI 
 class=&quot; lbl_si &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_si ) 
&#160; 
 Al oprimir el botón, y con la información del Punto de donación, la donación y la causal de liberación el sistema deberá llamar al servicio de liberación de anuncios tal cual se especifica en la documentación del servicio público (se incorporan parámetros de autenticación en la cabecera del llamado). 

 Despliegue de información a partir de las respuestas del servicio&#58; 
 Respuesta exitosa&#58; 
 El sistema deberá responder con el siguiente mensaje para posteriormente sacar al usuario al listado de anuncios. 
 clase = lbl_liberacion_exitosa (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_liberacion_exitosa )&#160; 
&#160; 
 &quot;Haz liberado exitosamente la donación. La misma estará de nuevo disponible para su gestión por nuestra comunidad de rescate.&quot; 
&#160; 
 Respuesta no exitosa&#58; incomplete_data&#58; El sistema deberá validar de nuevo los datos necesarios en el llamado e intentarlo de nuevo. 
 Respuesta no exitosa&#58; “op”&#58;”false”&#58; El sistema deberá reintentar el llamado y desplegarle al usuario un solo toast (con control para que no se despliegue varias veces), con el siguiente label&#58; 
 clase = lbl_reintentando2 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_reintentando2 )&#160;&#160; 
&#160; 
 &quot;Reintentando, espera por favor unos segundos&quot; 
 Respuesta no exitosa&#58; fail&#58; El sistema deberá responder con el siguiente mensaje para posteriormente sacar al usuario de la funcionalidad de programación. 
 clase = lbl_problema_liberacion (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_problema_liberacion )&#160; 
&#160; 
 &quot;Ocurrió un problema. No fue posible liberar esta donación.&quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 65830c25-e7d8-4981-baa9-eb1eda3249ca 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 c0a1f36e-0e13-41ed-a589-87b1568a062a 
 2026-06-18T00:05:40.9651955Z 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-17T16:06:48.7011045Z"}] 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"78d46cca-702a-4dd7-85ec-fbe010d42831","SequenceId":66,"FluidContainerCustomId":"477c7526-278e-4264-b128-2c96463995a4","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 LIBERACIÓN DE DONACIONES