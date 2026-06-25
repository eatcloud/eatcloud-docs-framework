# nuevo-dashboard-de-anuncio-de-donación-eatc_dona_dsh.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta vista se cambiará la disposición de elementos como botones, y se eliminarán algunos gráficos (por ejemplo el MAPA y una imagen en el encabezado) para obtener una vista de datos más limpia como lo sugiere la siguiente imagen&#58; 

 Toda la programación de la vista se debe mantener (labels, ids de funcionalidades, llamados a API) pero se realizarán cambios estéticos, que se relacionan a continuación&#58; 

 Detalle de anuncio de donación&#58; encabezado 
 Se quitan del encabezado el mapa , la imagen que contiene datos del punto de donación y también el botón de consulta de horarios de atención (ya que redunda con la funcionalidad de horarios de atención a la cual se accede desde el menú lateral) 

 class=&quot; lbl_detalle_anuncio &quot; + eatc_dona_headers. eatc-code (tal como funcionaba anteriormente) 

 Primera franja de botones. 

 Se ubicarán los mismos botones (que se manejaban anteriormente en un formato vertical), en una disposición horizontal (que deberá fluir a varias hileras de botones (si el ancho de la pantalla no da para ubicarlos en una sola hilera) o hasta una disposición vertical para pantallas pequeñas) a excepción de ls boton &quot; Calificar al beneficiario &quot; ( que se moverá para ubicarlo después del nombre del beneficiario) y &quot; Eliminar anuncio &quot; (que se moverá para la parte inferior, después del listado de los componentes del anuncio). El funcionamiento de los botones será idéntico al que se tiene programado actualmente (labels, ids de funcionalidades, condiciones para el despliegue) 

 Datos del beneficiario y botón &quot;Califica al beneficiario&quot; 

 Se mostrará la información del beneficiario de la siguiente manera incluyendo el botón de &quot;Calificar Beneficiario&quot; 

 Datos del beneficiario&#58; (class=&quot; lbl_datos_beneficiario &quot;) 
&#160; 
&#123;&#123;eatc_dona_headers. eatc-donation_manager_name &#125;&#125; (nombre del beneficiario) 
 (Botón) class=&quot; lbl_califica_al_beneficiario &quot; (Califica al beneficiario 
 Dirección ( class=&quot; lbl_direccion &quot;) &#58; &#123;&#123;eatc_dona_headers. eatc-donation_manager_address &#125;&#125; 
 Teléfono ( class=&quot; lbl_telefono &quot;) &#58; &#123;&#123;eatc_dona_headers. eatc-donation_manager_phone &#125;&#125; 
 Puntos ( class=&quot; lbl_puntos &quot;) &#58; &#123;&#123;eatc_dona_headers. eatc-donation_manager_score &#125;&#125; 

 Datos de recogida 

 Se mostrará de los datos de recogida como se establece a continuación 

 Recogerá la donación (class=&quot; lbl_card_recoge &quot;) 
&#160; 
&#123;&#123;eatc_dona_headers.eatc- picker_name &#125;&#125; (nombre del recolector) 
 Documento de identidad ( class=&quot; lbl_doc_id &quot; ) &#58; &#123;&#123;eatc_dona_headers. eatc-picker_doc_id &#125;&#125; 
 Placa vehículo ( class=&quot; lbl_card_placa_vehiculo &quot; ) &#58; &#123;&#123;eatc_dona_headers. eatc-picker_license_plate &#125;&#125; 

 ***NUEVO &#58; Teléfono recolector ( class=&quot; lbl_tel_recolector &quot; ) &#58; &#123;&#123;eatc_dona_headers. eatc-picker_phone &#125;&#125; *** 
 Fecha programada de recogida (class=&quot; lbl_fecha_programada_de_recogida 
&#123;&#123;eatc_dona_headers. eatc-programed_picking_datetime &quot; &#125;&#125; (Fecha y hora programada de recogida) 

 ***NUEVO&#58; Recolectores adicionales *** 
 Consulta para traer los datos y mostrar el label y la información adicional 
 El sistema realizará la siguiente consulta para establecer si existen registrados recolectores adicionales y si el sistema responde con una respuesta válida, se presentará la etiqueta y la información registrada&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_dona_multiple_pickers ?eatc_dona_header_code= &#123;&#123; eatc-id &#125;&#125; 
 Si el llamado obtiene una respuesta válida, el sistema desplegará la etiqueta y los datos registrados (las etiquetas pueden ser las mismas utilizadas para mostrar los datos del único recolector que hasta la fecha se registraba) 
 Label&#58;&#160; class= lbl_recolectores_adicionales 
&#160; 
 &#123;&#123;eatc_dona_multiple_pickers . eatc-picker_name &#125;&#125; (nombre del recolector) 
 Documento de identidad ( class=&quot; lbl_doc_id &quot; ) &#58; &#123;&#123;eatc_dona_multiple_pickers . eatc-picker_doc_id &#125;&#125; 
 Placa vehículo ( class=&quot; lbl_card_placa_vehiculo &quot; ) &#58; &#123;&#123;eatc_dona_multiple_pickers . eatc-picker_license_plate &#125;&#125; 
 Teléfono recolector ( class=&quot; lbl_tel_recolector &quot; ) &#58; &#123;&#123; eatc_dona_multiple_pickers . eatc-picker_phone &#125;&#125; &#160; 
 Fecha programada de recogida (class=&quot; lbl_fecha_programada_de_recogida &quot;)&#58; &#123;&#123;eatc_dona_multiple_pickers. eatc-programed_picking_datetime &#125;&#125; 
&#160; 
&#160; 
 ***NUEVO&#58; Botón&#58; Ver adjuntos *** 
Label&#58; class= lbl_ver_adjuntos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=wapp&amp;idlabel= lbl_ver_adjuntos ) 
 Condición para el despliegue del botón&#58; el botón se desplegará si al hacer la siguiente consulta, el sistema trae una información válida&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/ eatcloud / eatc_dona_attachments ?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp=eatc_doc_name,eatc_doc_url 
Al presionar el botón, el sistema tendrá dos comportamientos, de acuerdo a si la donación tiene varios o un solo adjunto&#58; 
 Varios adjuntos&#58; el sistema presentará un listado de los documentos adjuntos a la donación, según la anterior consulta (desplegando el nombre y haciendo que el mismo lleve a la respectiva URL). &#160;Cuando el usuario haga clic en un nombre, la WAPP deberá poder mostrar / descargar la imagen o documento que esté relacionado a la donación particular, según sea el caso 
 Un solo adjunto&#58; el sistema directamente al accionar el botón, deberá poder mostrar / descargar la imagen o documento que está relacionado a la donación en cuestión. 
&#160; 

 Contenido de la donación (nuevo funcionamiento de las funciones de edición y borrado) 

 Se realizará una disposición de los datos del detalle de la donación, en una tabla (con encabezados en las columnas para facilitar su lectura) y también se dispondrán los botones de editar (Adicionar un producto) y Eliminar la donación&#160; de manera diferente (Se mantendrán las cualidades de edición tal como están implementadas REVISANDO estados de la donación para el despliegue de los respectivos botones (sólo se podrán eliminar donaciones no adjudicadas y editar donaciones no despachadas), que se especifican a continuación) 

 Contenido del anuncio de donación&#58; (class=&quot; lbl_contenido_anuncio &quot;) 
 (Botón) class=&quot; lbl_editar_anuncio &quot; (Editar anuncio de donación) 
&#160; 
 Funcionamiento del botón &quot;Editar anuncio de donación&quot;&#58; ahora se podrán editar anuncios con estados &quot;delivered&quot;, &quot;received&quot;, y &quot;cancelled&quot; 
 Este botón sólo podrá aparecer para anuncios cuyo estado sea &quot;announced&quot; (anunciado) , &quot;awarded&quot; (adjudicado) ,&#160; &quot;scheduled&quot; (programado) , &quot;delivered&quot; (despachado), &quot;received&quot; (recibido) y &quot;cancelled&quot; (cancelado) y para donaciones creadas a través de EatCloud, por lo tanto la herramienta debe (en primera instancia) evaluar si el eatc-code está conformado solo por caracteres numéricos, y en este caso ocultar el botón. Si el eatc-code sigue los estándares de codificación que tiene la plataforma (y que incluye caracteres alfanuméricos), se debe presentar el botón. 
&#160; 
 &#160;Cuando se oprima el botón la acción deberá realizar dos cosas&#58; 
 Se deberá desplegar el botón &quot; Adicionar un producto &quot; (class=&quot;lbl_adicionar_producto&quot;) 
 Se deberán habilitar los íconos de edición (en la versión actual&#58; un lápiz en un círculo rojo) para los respectivos items de la lista de productos del anuncio. 
 Al terminar la edición (que edita los detalles directamente), se debe hacer el llamado al servicio bajo demanda para la regeneración del encabezado del anuncio (a partir de los datos editados) 
 Cuando se edite un anuncio (después de llamar al servicio para generación del encabezado) con estado &quot;delivered&quot; (despachado) o &quot;received&quot; (recibido) se debe invocar el servicio recalkpi&#58; Servicio para el recálculo de los KPIs de una donación 

&#160; 
 ***NUEVO &#58; funcionamiento del botón &quot;Adicionar item&quot; *** 
 Adicional a los llamados para adicionar un nuevo ítem del anuncio de donación (creación&#160; del ítem en eatc_dona, actualización de encabezado de anuncio de donación en eatc_dona_headers y llamado a la función recalkpi para anuncios con estado &quot;delivered&quot; (despachado) o &quot;received&quot; ), el sistema deberá realizar DESPUÉS (dado que primero debe haberse actualizado eatc_dona ) el siguiente llamado a un nuevo servicio de integración con blockchain, con el ánimo de actualizar la información del respectivo item en la cadena de bloques&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code= &#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125; &amp;eatc _ odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_servicio= frmProductoDonacion 

&#160; 
 ***NUEVO &#58; funcionamiento del botón &quot;Editar ítem (detalle) de la donación&quot; *** 
 Adicional a los llamados para editar un ítem del anuncio de donación (actualización de la cantidad&#160; del ítem, actualización de encabezado de anuncio de donación y llamado a la función recalkpi para anuncios con estado &quot;delivered&quot; (despachado) o &quot;received&quot; ), el sistema deberá realizar DESPUÉS (dado que primero debe haberse actualizado eatc_dona ) el siguiente llamado a un nuevo servicio de integración con blockchain, con el ánimo de actualizar la información del respectivo item en la cadena de bloques&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code= &#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125; &amp;eatc _ odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_servicio= frmProductoDonacionEditar 

&#160; 
 ***NUEVO &#58; funcionamiento del botón &quot;Eliminar ítem (detalle) de la donación (o colocar cantidad en cero)&quot; *** 
 Adicional a los llamados para borrar un ítem del anuncio de donación (borrado de ítem, actualización de encabezado de anuncio de donación y llamado a la función recalkpi para anuncios con estado &quot;delivered&quot; (despachado) o &quot;received&quot; ), el sistema deberá realizar DESPUÉS (dado que primero debe haberse actualizado eatc_dona ) el siguiente llamado a un nuevo servicio de integración con blockchain, con el ánimo de actualizar la información del respectivo item en la cadena de bloques&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code= &#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125; &amp;eatc _ odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_operacion=delete&amp;_servicio= frmProductoDonacionEliminar 
&#160; 
 Tabla de productos donados 
 Anteriormente no se poseían títulos en las columnas y en el nuevo diseño se deben incorporar de la siguiente manera 
 Producto class=&quot; lbl_producto &quot; 
&#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; (nombre del producto) 
 Código del producto ( class=&quot; lbl_codigo_producto &quot; ) &#58; &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; 
 Cantidad class=&quot; lbl_peso_kg &quot; 
&#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; + &quot; Unidades&quot; ( class=&quot; lbl_unidades &quot; ) 
 Peso (KG) class=&quot; lbl_peso_kg &quot; 
 Peso unitario ( class=&quot; lbl_peso_unitario &quot; )&#58; &#123;&#123;eatc_dona. eatc-odd_unit_weight_kg &#125;&#125; &#160; +&#160; &quot;KG x UND&quot; ( class=&quot; lbl_kg_x_und &quot; ) 
 Peso total ( class=&quot; lbl_peso_total &quot; )&#58; &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; &#160; +&#160; &quot;KG&quot; ( class=&quot; lbl_kg_x_und &quot; ) 
 Costo ($) class=&quot; lbl_costo &quot; 
 Costo unitario ( class=&quot; lbl_costo_unitario &quot; ) &#58; &quot;$&quot; ( class=&quot; lbl_signo_moneda &quot; ) + &#123;&#123;eatc_dona. eatc-unit_cost &#125;&#125; &#160; +&#160; &quot;x UND&quot; ( class=&quot; lbl_x_und &quot; ) 
 Costo total ( class=&quot; lbl_costo_total &quot; )&#58; &quot;$&quot; ( class=&quot; lbl_signo_moneda &quot; ) + &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; &#160; 

&#160; 
 Totales class=&quot; lbl_totales &quot; 
Sumatoria(&#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125;) + &quot; Unidades&quot; ( class=&quot; lbl_unidades &quot; ) 
Sumatoria(&#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125;) &#160; +&#160; &quot;KG&quot; ( class=&quot; lbl_kg_x_und &quot; ) 
 &quot;$&quot; ( class=&quot; lbl_signo_moneda &quot; ) +&#160; Sumatoria(&#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; &#160; ) 
&#160; 
 Costo total ( class=&quot; lbl_costo_total &quot; )&#58; &quot;$&quot; ( class=&quot; lbl_signo_moneda &quot; ) + &#123;&#123;eatc_dona. eatc-odd_total_cost &#125;&#125; &#160;&#160; 

&#160; 
 ***NUEVO &#58; funcionamiento del botón &quot;Eliminar anuncio de donación&quot; (ahora solo aparecerá para anuncios de tres estados en particular excluyendo algunos que se permitían anteriormente y no se podrá mostrar cuando eatc-donor es diferente a eatc_cua_origin, es decir, para donaciones de no negociados)*** 
 (Botón) class=&quot; lbl_eliminar_anuncio &quot; (Eliminar anuncio de donación) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_eliminar_anuncio )&#160; 
&#160; 
 El botón aparece cuando el anuncio tenga los estados&#58; 
 announced 
 awarded 
 cancelled 
&#160; 
 Y a aquellos anuncios en donde el eatc_dona_headers. eatc-donor es igual a eatc_dona_headers. eatc_cua_origin (si los datos en estos dos campos son diferentes, es decir, es una donación de no negociados, el botón de borrar la donación no podrá mostrarse) 
&#160; 
 DEPRECADO (anteriormente también se desplegaba para estos estados, y ahora no se permitirá)&#58; 
 scheduled 
 delivered 
 received 
 not_delivered 

&#160; 
 Al oprimir el botón deberá aparecer un modal de la siguiente manera&#58; 
&#160; 
 Leyenda principal&#58; 
&#160; 
 class=&quot; lbl_confirmar_eliminar_anuncio &quot; (¿Estás seguro(a) que deseas eliminar el anuncio de donación?) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_eliminar_anuncio )&#160; 
&#160; 
 Botón&#58; No&#58; regresar 
&#160; 
 class=&quot; lbl_no_regresar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_no_regresar )&#160; 
 Al oprimir el botón se vuelve al dashboard de la donación sin realizar ninguna acción adicional. 
&#160; 
 Botón&#58; Si&#58; borrarlo 
&#160; 
 class=&quot; lbl_si_borrarlo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_si_borrarlo ) 
&#160; 
 Al oprimir el botón se realiza la invocación al API Pública para el borrado de donaciones de la siguiente manera. 
&#160; 
 Parámetros de autenticación&#58; 
&#160; 
 Usuario&#58; &#123;&#123;usuario&#125;&#125; =&gt; &#123;&#123;eatc_pods. login &#125;&#125; 
 Password&#58; &#123;&#123;password&#125;&#125;&#160; =&gt; &#123;&#123;eatc_pods. password &#125;&#125; 
&#160; 
 Método de autenticación&#58; 
&#160; 
 Basic Auth 
&#160; 
 Llamado al servicio&#58; 
 &#123; 
 &quot; _platform &quot;&#58; “wapp”, 
 &quot; _cuamaster &quot;&#58; “&#123;&#123;_DOM. cua_master &#125;&#125;”, 
 &quot; _cuauser &quot;&#58; “&#123;&#123;_DOM. cua_user &#125;&#125;”, 
 &quot; _operation &quot;&#58; “deleted”, 
 &quot; eatc-code&quot;&#58;&quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot;, 
 &quot; user &quot;&#58; “ &#123;&#123;eatc_pods. login &#125;&#125; ” 
 &#125; 

&#160; 
 ***NUEVO&#58; COMENTAR (OCULTAR) EL&#160; botón &quot;Cancelar anuncio&quot; *** 
 (Botón) class=&quot; lbl_cancelar_anuncio &quot; (Cancelar anuncio de donación) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_cancelar_anuncio )&#160;&#160; 
&#160; 
 El botón aparece cuando el anuncio tenga los estados&#58; 
&#160; 
 announced 
 awarded 
 scheduled 
 delivered 
 received 
 not_delivered 
&#160; 
 Al oprimir el botón deberá aparecer un modal de la siguiente manera&#58; 
&#160; 
 Leyenda principal&#58; 
&#160; 
 class=&quot; lbl_confirmar_cancelar_anuncio &quot; (¿Estás seguro(a) que deseas cancelar el anuncio de donación?) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel=lbl_eliminar_anuncio )&#160; 
&#160; 
 Botón&#58; No&#58; regresar 
&#160; 
 class=&quot; lbl_no_regresar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_no_regresar )&#160; 
&#160; 
 Al oprimir el botón se vuelve al dashboard de la donación sin realizar ninguna acción adicional. 
&#160; 
 Botón&#58; Si&#58; cancelarlo 
&#160; 
 class=&quot; lbl_si_cancelarlo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_si_cancelarlo )&#160; 
&#160; 
 Al oprimir el botón se realiza la invocación al API Pública para cancelar donaciones de la siguiente manera. 
&#160; 
 Parámetros de autenticación&#58; 
 Usuario&#58; &#123;&#123;usuario&#125;&#125; =&gt; &#123;&#123;eatc_pods. login &#125;&#125; 
 Password&#58;&#123;&#123;password&#125;&#125;&#160; =&gt; &#123;&#123;eatc_pods. password &#125;&#125; 
&#160; 
 Método de autenticación&#58; 
 Basic Auth 
&#160; 
 Llamado al servicio&#58; 
 &#123; 
 &quot; _platform &quot;&#58;“wapp”, 
 &quot; _cuamaster &quot;&#58;“&#123;&#123;_DOM. cua_master &#125;&#125;”, 
 &quot; _cuauser &quot;&#58;“&#123;&#123;_DOM. cua_user &#125;&#125;”, 
 &quot; _operation &quot;&#58;“cancel”, 
 &quot; eatc-code&quot;&#58;&quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot;, 
 &quot; eatc_state_2&quot;&#58;&quot; manual_cancellation_wapp &quot; =&gt; implementar y dejar comentado hasta que esta tarea esté lista&#58; https&#58;//app.asana.com/0/1193204835809005/1203083257349090 &#160; 
 &#125; 

&#160; 
 ***NUEVO &#58; botón &quot;No Entregado&quot; *** 
 (Botón) class=&quot; lbl_no_entregado &quot; (Cancelar anuncio de donación) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_no_entregado )&#160; 

&#160; El botón aparece cuando el anuncio el estado&#58; 
 scheduled 
&#160; 
 Adicional a esto el sistema deberá realizar la las siguientes validaciones para mostrar el botón&#58; 
Consulta de la fecha y hora programada de recolección (y que no tenga fechas de check-in y check-out registradas&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123; eatc_dona_header_code &#125;&#125; &amp;eatc-picking_checkin_datetime=0000-00-00%2000&#58;00&#58;00&amp;eatc-picking_checkout_datetime=0000-00-00%2000&#58;00&#58;00 &amp;eatc-state= scheduled &amp;_cmp= e eatc-programed_picking_datetime 
&#160; 
 El sistema deberá realizar la siguiente consulta de timeout, para determinar el valor por defecto del timeout aplicable 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_timeout_rules?eatc-timeout_name= dona_release_from_scheduled 
 &amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from 
&#160; 
 Ejemplo cuenta maestra&#160;abaco&#160;en ambiente de&#160;pruebas&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=dona_release_from_scheduled&amp;cua=_default&amp;_cmp=eatc-timeout_description,eatc-timeout_in_minutes,eatc-timeout_in_hours,eatc-timeout_from &#160; 
&#160; 
 res &#58; 
 [ 
 &#123; 
 eatc-timeout_description &#58;&#160; &quot;Tiempo mínimo para liberar una donación a partir de la fecha de la fecha y hora de recogida programada&quot; , 
 eatc-timeout_in_minutes &#58;&#160; &quot;30&quot; , 
 eatc-timeout_in_hours &#58;&#160; &quot;0,5&quot; , 
 eatc-timeout_from &#58;&#160; &quot;eatc-programed_picking_datetime&quot; 
 &#125; 
 ], 
&#160; 
 Si la consulta no arroja respuesta, se tomará como valor por defecto&#58; 
 eatc-timeout_in_minutes &#58;&#160; &quot;30&quot; , 
 eatc-timeout_in_hours &#58;&#160; &quot;0,5&quot; , 
&#160; 
 Es decir que este timeout indica un tiempo mínimo que se debe esperar antes de mostrar el botón de &quot;No Entregado&quot;. &#160; Por lo tanto el sistema debe evaluar si la fecha y hora actual es posterior a la fecha y hora programada de recolección más el timeout, para poder mostrar el botón (funcionamiento similar al botón de liberar donación en este aspecto). 
&#160; 
 DEPRECADO&#58; El botón aparece cuando el anuncio tenga los estados&#58; 
 announced 
 awarded 
 scheduled 
 delivered 
 received 
 cancelled 
&#160; 
 Al oprimir el botón deberá aparecer un modal de la siguiente manera&#58; 
&#160; 
 Leyenda principal&#58; 
&#160; 
 class=&quot; lbl_confirmar_no_entregado &quot; (¿Estás seguro(a) que deseas marcar como no entregado el anuncio de donación?) ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_confirmar_no_entregado )&#160; 
&#160; 
 Botón&#58; No&#58; regresar 
&#160; 
 class=&quot; lbl_no_regresar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_no_regresar )&#160; 
&#160; 
 Al oprimir el botón se vuelve al dashboard de la donación sin realizar ninguna acción adicional. 
&#160; 
 Botón&#58; Si 
&#160; 
 class=&quot; lbl_si &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_si )&#160; 
&#160; 
 ***NUEVO&#58; Selector de tipo de no entrega *** 
 Si es oprime el botón &quot; Si &quot;, el sistema deberá habilitar un selector con la siguiente leyenda 
 class= lbl_seleccionar_tipo_no_entrega &quot;Selecciona el tipo de no entrega efectuada&quot; 
&#160; 
 El sistema deberá desplegar un selector único con dos opciones&#58; 
 class= lbl_parcial &#58; Parcial 
 class= lbl_total &#58; Total 
&#160; 
 Si el usuario selecciona el causal &quot; Parcial &quot;, el sistema debe desplegar un cuadro de diálogo con la siguiente leyenda&#58; 
 class= lbl_editar_donacion_desc &quot;Por favor edita la donación para establecer eliminar de la misma los productos que no fueron entregados&quot; y desplegarle el botón &quot; lbl_editar_donacion &quot; que lo debe situar en la funcionalidad de edición de donación. 
&#160; 
 Si el usuario selecciona el causal &quot; Total &quot; entones el sistema funciona como de costumbre y se realizan las siguientes acciones&#58; se realiza la invocación al API Pública para no entrega de una donación de la siguiente manera. 
&#160; 
 Parámetros de autenticación&#58; 
 Usuario&#58; &#123;&#123;usuario&#125;&#125; =&gt; &#123;&#123;eatc_pods. login &#125;&#125; 
 Password&#58; &#123;&#123;password&#125;&#125;&#160; =&gt; &#123;&#123;eatc_pods. password &#125;&#125; 
&#160; 
 Método de autenticación&#58; 
 Basic Auth 
&#160; 
 Llamado al servicio&#58; 
 &#123; 
 &quot; _platform &quot;&#58; “wapp”, 
 &quot; _cuamaster &quot;&#58; “&#123;&#123;_DOM. cua_master &#125;&#125;”, 
 &quot; _cuauser &quot;&#58; “&#123;&#123;_DOM. cua_user &#125;&#125;”, 
 &quot; _operation &quot;&#58; “not_delivered”, 
 &quot; eatc-code&quot;&#58;&quot; &#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; &quot;, 
 &quot; eatc_state_2&quot;&#58;&quot; manual_not_delivered_wapp &quot; =&gt; implementar y dejar comentado hasta que esta tarea esté lista&#58; https&#58;//app.asana.com/0/1193204835809005/1203083257349090 &#160; 

&#160; 
 ***NUEVO&#58; funcionamiento del botón &quot;Editar anuncio de donación&quot; *** 
 Este botón sólo podrá aparecer para anuncios cuyo estado sea &quot;announced&quot; (anunciado) , &#160; &quot;awarded&quot;, &quot;scheduled&quot;, &quot;delivered&quot; y &quot;received&quot; ( cuando se invoque el servicio en estado &quot;delivered&quot; y &quot;received&quot; se deberá, después de corregir cantidades en el detalle y generar el nuevo encabezado, invocar el servicio &quot; recalkpi &quot;, para volver a generar los KPIs del anuncio ) y para donaciones creadas a través de EatCloud, por lo tanto la herramienta debe (en primera instancia) evaluar si el eatc-code está conformado solo por caracteres numéricos, y en este caso ocultar el botón. Si el eatc-code sigue los estándares de codificación que tiene la plataforma (y que incluye caracteres alfanuméricos), se debe presentar el botón. ( en la actualidad está programada dicha restricción en el botón, la cual se debe conservar ). 
&#160; 
 ***NUEVO&#58; Edición de anuncios&#58;&#160; Nuevos campos que se deberán editar en dona_headers *** 
 eatc_dona_references 
&#160; 
 Se deberá guardar el número de referencias del anuncio; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_distinct=eatc-odd_id&amp;_cont 
&#160; 
 Se toma el resultado obtenido en &quot; count &quot; y se lleva al parámetro en cuestión ( eatc_dona_references ) el CRD respectivo.. 
&#160; 
 eatc_dona_units 
 Se deberá guardar el número de unidades del anuncio; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;&amp;_cmp= eatc-odd_quantity 
&#160; 
 El sistema realiza una sumatoria de los valores obtenidos y se lleva al parámetro en cuestión ( eatc_dona_units) con el CRD respectivo.. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F2238166234-CONTENIDO-DE-LA-DONACION.png&ow=707&oh=387, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F2238166234-CONTENIDO-DE-LA-DONACION.png&ow=707&oh=387 
 EatCloud Donantes (NuevaWAPP) 

 216.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 7323bef8-652e-4312-9afb-2f1903a0903b 
 4!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 62ccd5f1-071d-4bd7-b549-0ce4ff767866 
 2025-12-19T06:03:51.7081886Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"0a93b07f-5fcb-4aa3-9876-267f5ed8d46a","SequenceId":2112,"FluidContainerCustomId":"e322c742-9bc9-4258-8287-546983304990","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 NUEVO DASHBORAD DE ANUNCIO DE DONACIÓN (EATC_DONA_DSH)