# beneficiarios-dashboard-de-anuncio-de-donación-eatc_dona_dsh.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 DASHBOARD DE ANUNCIO DE DONACIÓN (EATC_DONA_DSH) ","showTimeToRead":false,"encodedImage":"BBR:HGxufQ~qj[fQ"},"containsDynamicDataSource":false}">

 Nota implementación mejoramiento:  
 Se identificarán mejoras prioritarias y mejoras en el dashboard de la donación principalmente en los botones de acción.  Se sugiere empezar con la implementación prioritaria, y una vez se tenga dicha implementación, seguir con los ajustes de más baja prioridad. 

 D ETALLE DE ANUNCIO DE DONACIÓN: ENCABEZADO 

 Consulta de anuncios ***MEJORA NO prioritaria: optimización llamado *** 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &_cmp= eatc-code,eatc-pod_name,eatc-pod_address,eatc-pod_phone,eatc-pod_score,eatc-warning, 

 El sistema toma el parámetro " eatc-id " del encabezado de anuncio de donación ( eatc_dona_headers ) seleccionado desde el listado donde se invoca esta vista ( nube de donaciones: botón me interesa y mis donaciones: botón “+” ) y con él se invoca el respectivo API 

 Ejemplo _DOM. cua_master=abaco: 
 El para el anuncio cuyo " eatc-id " = 672726ec-1c55-11ea-b250-0018515a556c 

 Ambiente pruebas: https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=672726ec-1c55-11ea-b250-0018515a556c&_cmp=eatc-code,eatc-pod_name,eatc-pod_address,eatc-pod_phone,eatc-pod_score,eatc-warning 

 Información a desplegar 
 Con la respuesta del API se toma la siguiente información del gestor de donaciones al que se le adjudicó el anuncio: 

 Donación: eatc-code (para el ejemplo: 00001912100729 ) 
 Punto de donación: eatc-pod_name (para el ejemplo: CARULLA LAURELES ) 
 Dirección : eatc-pod_address (para el ejemplo: Transversal 39 B Circular 73 B 22 ) 
 Telefono : eatc-pod_phone (para el ejemplo: (4) 6051129 ) 

 ***MEJORA NO prioritaria: desplegar el label "Score", si el valor del mismo es diferente de 0 *** 

 Si esta consulta 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-pod_score =0&_cont 

 Arroja un resultado válido, entonces no se muestra el label "Score".  Si la consulta no arroja un resultado (es decir que hay un valor diferente de cero en el score) se presenta el label y el valor 

 Score : eatc-pod_score (para el ejemplo: dado que el valor es "0" no se debe mostrar el label "Score" (PENDIENTE DE IMPLEMENTAR) ) 

 Visualización de horarios de atención registrados en el dashboard del anuncio de donación 
 Se solicita como mejora, el poder visualizar los horarios de atención registrados (del donante que hizo la donación)  en el dashboard del anuncio de donación (debe ser una visualización muy similar a la que se implementó en la funcionalidad configuración horarios de atención , que sea meramente informativa y que no ocupe tanto espacio de pantalla).  Es ideal que esto se pueda ver antes de hacer la programación del anuncio, como una ayuda previa al gestor de donaciones para realizar dicha programación 

 Mensaje de ALERTA 

 En un lugar muy visible (y en un fondo que lo haga aún más visible, puede ser Rojo) del dashboard de donación, se debe colocar un mensaje "ALERTA", si y solo si en el campo eatc-warning posee información, diferente a 0 o vacía (y no es nulo) y que muestre el contenido del campo eatc-warning del anuncio respectivo. 

 ***Nuevo: Requisitos para retirar la donación *** 
 Similar al mensaje de alerta original (anterior) en cuanto a diseño y se debe ubicar debajo del anterior, pero apuntando a una información nueva de la siguiente manera: 

 Validación para mostrar el cuadro de información (y evitar problemas por faltantes en estructuras de datos): 

  Se deberá validar que para la estructura eatc_dona_headers de la respectiva cuenta maestra, exista el campo " eatc_dona_headers. eatc_logistical_requirements ". Tambien se deberá validar que en dicho campo existe información válida (que no sea nula o vacía).   Si el campo no existe, o si el campo no tiene información, el recuadro con informacion no se despliega (incluyendo su titulo). 

 Título: 
   class="lbl_rq_retirar_donacion" ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&idlabel=lbl_rq_retirar_donacion )  

 Se muestran el dato contenido en:  
 eatc_dona_headers. eatc_logistical_requirements 

 Listado de documentos soporte eatc-doc 

 Arriba del listado de ítems, si y solo si en el campo eatc-doc de el eatc_dona respectivo existen registros válidos, diferente a 0 o vacío (y no es nulo), se debe mostrar el array de dichos eatc_dona.eatc-doc (se debe hacer un distinct para no repetir eatc-doc ), antecedido por la siguiente leyenda: 
 El presente anuncio contiene los siguientes documentos soporte: 

 Recoge esta donación ***Nuevo: incorporación del código de recogida *** 
 Se realiza la siguiente consulta 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-picker_name=_novacio 

 Si la consulta no es exitosa, entonces se deben ocultar los datos de programación (todo el div) y se debe colocar un punto rojo al lado del menú superior de 3 puntos que indique al usuario que debe programar la recogida. 

 Si la consulta es exitosa, entonces se procede con la consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &_cmp= eatc-picker_name,eatc-picker_doc_id,eatc-picker_license_plate,eatc-programed_picking_datetime, eatc-verification_code 

 Se presenta la siguiente información: 

 Recoge esta donación 
 Nombre : eatc-picker_name 
 Documento de identidad (): eatc-picker_doc_id 
 Placa vehículo () : eatc-picker_license_plate 
 Fecha y hora de recogida : eatc-programed_picking_datetime 
 Código de recogida (label (class) lbl_codigo_recogida ) : eatc-verification_code 

 ***NUEVO: Recolectores adicionales *** 

 Consulta para traer los datos y mostrar el label y la información adicional 
 El sistema realizará la siguiente consulta para establecer si existen registrados recolectores adicionales y si el sistema responde con una respuesta válida, se presentará la etiqueta y la información registrada: 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_dona_multiple_pickers ?eatc_dona_header_code= {{ eatc-id }} 

 Si el llamado obtiene una respuesta válida, el sistema desplegará la etiqueta y los datos registrados en un colapisible (las etiquetas pueden ser las mismas utilizadas para mostrar los datos del único recolector que hasta la fecha se registraba) 

 Label:  class= lbl_recolectores_adicionales 
 Nombre : {{eatc_dona_multiple_pickers . eatc-picker_name }} 
 Documento de identidad: {{eatc_dona_multiple_pickers . eatc-picker_doc_id }} 
 Placa vehículo : {{eatc_dona_multiple_pickers . eatc-picker_license_plate }} 
 Fecha y hora de recogida : {{eatc_dona_multiple_pickers. eatc-programed_picking_datetime }} 

 B OTONES DE ACCIÓN 

 ***MEJORA: Al presionar los tres puntos, se deben refrescar las consultas para determinar las condiciones de presentación u ocultamiento de botones en adelante descritos *** 

 Se observa que para que se refresquen en algunos casos las condiciones necesarias para mostrar u ocultar los botones que en adelante se detallan, es necesario salirse del dashboard del anuncio de donación respectivo, para volver a entrar a él y en ese momento se refrescan las condiciones.  Se sugiere que las condiciones que se están tomando al entrar al dashboard, se refresquen cada vez que se oprima el menú superior (tres puntos) para que de esta manera no halla que salir del dashboard de donación y volver a entrar para ver los botones que se requieren para acciones subsiguientes. 

 Botón: acepta esta donación 

 Condición para mostrar el botón: 
 Solo se solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea estado " announced" (anunciado) . 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state=announced 

 ***MEJORA NO prioritaria: Condición para ocultar el botón: *** 

 Solo se solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea estado " announced" (anunciado) . 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state= ! announced 

 Botón: no estoy interesado ***NUEVO: también opera para anuncios "programados" y "anunciados" con el dato eatc_dona_headers. eatc_not_interested_btn = y *** 

 Se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea estado " announced" (anunciado) .  

 ó (prueba lógica ó, si se cumple una de las condiciones solamente se muestra el botón) 

 Se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea estado "scheduled (programado)" y en el campo eatc_dona_headers. eatc_not_interested_btn tenga el valor " y " 

 ó (prueba lógica ó, si se cumple una de las condiciones solamente se muestra el botón) 

 Se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea estado "awarded (adjudicado)" y en el campo eatc_dona_headers. eatc_not_interested_btn tenga el valor " y " 

 El botón da acceso a la funcionalidad " Cancelación de anuncio de donación ". 

 Botón: programar recogida 

 Condición para mostrar el botón: 
 Solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea "awarded" (adjudicado) . 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state=awarded 

 ***MEJORA NO prioritaria: Condición para ocultar el botón: *** 
 El botón no se muestra para anuncios cuyo estado  sea diferente a "awarded" (adjudicado) . 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state= ! awarded 

 El botón da acceso a la funcionalidad " Programar recogida ". 

 ***NUEVO: Botón: recolector adicional *** (class=lbl_recolector_adicional) 

 Nota para el desarrollo: 
 Este botón permitirá un nuevo acceso a la funcionalidad de "Programar recogida", que tradicionalmente permitía un solo registro asociado a la donación.  A partir de la implementación de la mejora, de permitír a partir del proceso de PROGRAMDONA , permitir múltiples recolectores,  se habilitará, para anuncios grandes, que requieren varios vehículos,  se les registren varios recolectores.  Por eso, este botón, se habilitará para donaciones programadas  y que sobrepasen las 4 toneladas y se deshabilitará cuando la donación sea entregada 

 Condición para mostrar el botón: 
 Solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea "scheduled (programado)" y su peso original ( eatc-original_weight_kg) supere las 4 toneladas. 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state=scheduled& eatc-original_weight_kg =_>4000 

 Condición para ocultar el botón: 
 El botón no se muestra para anuncios cuyo estado  sea diferente a "scheduled (programado)". 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state=_nin_scheduled 

 El botón da acceso a la funcionalidad " Programar recogida ". 

 ***NUEVO: volver a habilitar : Botón: reprograma recogida *** 
 Solo se solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea "scheduled" (programado) y [NUEVO] no tengan un dato registrado en " eatc-picking_checkin_datetime " 

 El botón da acceso a la funcionalidad " Reprogramar recogida ". 

 Botón: abortar recogida de donación ***MEJORA NO prioritaria: revisar funcionamiento botón *** 
 Nota para el desarrollador: En las últimas versiones no se ha visto funcionando este botón, se debe revisar si hay alguna anotación en el código que indique por qué salió de funcionamiento y comunicar los hallazgos antes de proceder a activar el botón 

 Condición para mostrar el botón: 

 Solo se solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea "awarded" (adjudicado) . 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state=awarded 

 ***MEJORA NO prioritaria: Condición para ocultar el botón: *** 
 El botón no se muestra para anuncios cuyo estado  sea diferente a "awarded" (adjudicado) . 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state= ! awarded 

 El botón da acceso a la funcionalidad " Abortar anuncio de donación ". 

 Botón: recoge esta donación 

 Condición para mostrar el botón: ***MEJORA: validación de registro en eatc-picker_start_datetime *** 

 Solo se solo se habilita para anuncios de donación cuyo estado ( eatc_dona_states ) sea "scheduled" (programado)   y no tengan un dato registrado en " eatc- eatc-picker_start_datetime "  y  no tengan un dato registrado en " eatc-picking_checkin_datetime " 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-state =scheduled& eatc-picker_start_datetime= 0000-00-00 %20 00:00:00& eatc-picking_checkin_datetime= 0000-00-00 %20 00:00:00 

 ***MEJORA: Condición para ocultar el botón: implementación operación lógica _novacio (se deberá validar con Jesús si esta operación lógica opera también con fechas vacías 0000-00-00 00:00:00) *** 

 El botón no se muestra si el estado de la donación es diferente a " scheduled " y si hay una fecha y hora válida en los parámetros " eatc-picker_start_datetime " y " eatc-picking_checkin_datetime= "  

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }}&eatc-state= ! scheduled& eatc-picker_start_datetime= _NOVACIO &eatc-picking_checkin_datetime= _NOVACIO 

 El botón da acceso a la funcionalidad " Recoger anuncio de donación ". 

 Botón: ver código de recogida 

 Condición para mostrar el botón: 
 Sólo se solo se habilita para anuncios de donación que previamente se les halla presionado el botón " recoge esta donación " o que ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picker_start_datetime" y que no haya dato registrado en "eatc-code_verification_datetime" 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-state =scheduled & eatc-picking_checkin_datetime = _novacio &eatc-code_verification_datetime =0000-00-00 %20 00:00:00 

 ***MEJORA: Condición para ocultar el botón: *** 
 El botón se oculta si el estado de la donación es diferente a  scheduled 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-state= !scheduled 

 El botón da acceso a la funcionalidad " Código para recogida ". 

 Botón: "Llegué al punto de donación" ***MEJORA: validación condicionada según el valor del campo eatc_donation_managers .eatc_sdm: cuando hay un dato en eatc_donation_managers .eatc_sdm no se muestra el botón*** 

 El sistema realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro={{eatc_donations_managers. identificador_unico_registro }}&_cmp= eatc_sdm 

 Si el sistema arroja una respuesta inválida (ejemplo: err_msg : "Unknown column 'eatc_sdm' in 'field list'" ), vacía, nula, o igual a " n " entonces el sistema funcionará como lo viene haciendo: 

 Funcionamiento tradicional (funciona como funcionaba anteriormente): 
 Condición para mostrar el botón: 
 Sólo se solo se habilita para anuncios de donación que previamente se les haya presionado el botón " recoge esta donación " o que  en el encabezado del anuncio de donación ( eatc_dona_headers ) tengan registrado un dato en el campo "eatc-picker_start_datetime" y que el estado del anuncio no sea cancelado (cancelled) y que no haya dato registrado en "eatc-picking_checkin_datetime" 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-picker_start_datetime= _NOVACIO & eatc-picking_checkin_datetime= 0000-00-00 %20 00:00:00 &eatc-state= !cancelled 

 Si el sistema arroja como respuesta un "y" , entonces se propone el siguiente nuevo funcionamiento: 

 Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd = y ) ***MEJORA: no se mostrará el botón*** : 
 No se mostrará el botón 

 El botón da acceso a la funcionalidad " Check-in express: Llegué al punto de donación ". 

 ***NUEVO: Botón: (Fotografía) "Salida Almacén - Factura Aliado" *** 

 Icono: cámara fotográfica 

 label: class= lbl_salida_almacen ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_salida_almacen ) =  Salida Almacen - Factura Aliado   

 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} = mexico, {{eatc_photos. eatc_label }} = lbl_salida_almacen  y {{eatc_dona_headers. eatc-code }} 

 Para desplegar el botón se deberán cumplir las siguientes condiciones (todas: prueba lógica "y") 
 Anuncio con fecha válida en eatc-picking_checkin_datetime: 
 Sólo se solo se habilita para anuncios de donación en donde se halla establecido que el recolector del anuncio ha llegado al punto de donación a recoger la donación es decir que en  ( eatc_dona_headers ) tengan registrado un dato válido en "eatc-picking_checkin_datetime" (diferente a 0000-00-00 00:00:00 , es decir !0000-00-00 %20 00:00:00 ) y que el estado del anuncio no sea cancelado ( ! cancelled) 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-picking_checkin_datetime= !0000-00-00 %20 00:00:00 &eatc-state= !cancelled 

 Para la cuenta maestra en cuestión, existe una configuración para toma de fotografías y no se han tomado un máximo de 2 fotografías para el label " lbl_salida_almacen " 

 El sistema realiza la siguiente cosulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_label= lbl_salida_almacen 

 Si la consulta arroja una respuesta válida, entonces el sistema realiza la siguiente: 
 {{ URL_datagov }}/api/eatcloud/eatc_photo_registry?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona_headers. eatc-code }}&eatc_label= lbl_salida_almacen &_cont 

 Si la respuesta es menor que  "dos" (2) (es decir, no se han tomado un máximo de dos fotografías para este label) entonces se deberá desplegar el botón con las siguientes características 

 Icono: cámara fotográfica 

 label : class=lbl_salida_almacen ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_salida_almacen ) =  Salida Almacen - Factura Aliado  

 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} , {{eatc_photos. eatc_label }} = lbl_salida_almacen y {{eatc_dona_headers. eatc-code }} 

 ***NUEVO: Botón: (Fotografía) "Recibo interno de recepción" *** 

 Icono: cámara fotográfica 

 label: class= lbl_recibo_interno_rec ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_recibo_interno_rec ) =  Salida Almacen - Factura Aliado   

 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} = mexico, {{eatc_photos. eatc_label }} = lbl_recibo_interno_rec   y {{eatc_dona_headers. eatc-code }} 

 Para desplegar el botón se deberán cumplir las siguientes condiciones (todas: prueba lógica "y") 
 Anuncio con fecha válida en eatc-picking_checkin_datetime: 
 Sólo se solo se habilita para anuncios de donación en donde se halla establecido que el recolector del anuncio ha llegado al punto de donación a recoger la donación es decir que en  ( eatc_dona_headers ) tengan registrado un dato válido en "eatc-picking_checkin_datetime" (diferente a 0000-00-00 00:00:00 , es decir !0000-00-00 %20 00:00:00 ) y que el estado del anuncio no sea cancelado ( ! cancelled) 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-picking_checkin_datetime= !0000-00-00 %20 00:00:00 &eatc-state= !cancelled 

 Para la cuenta maestra en cuestión, existe una configuración para toma de fotografías y no se han tomado un máximo de 2 fotografías para el label " lbl_recibo_interno_rec  " 
 El sistema realiza la siguiente cosulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_label= lbl_recibo_interno_rec   

 Si la consulta arroja una respuesta válida, entonces el sistema realiza la siguiente: 
 {{ URL_datagov }}/api/eatcloud/eatc_photo_registry?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona_headers. eatc-code }}&eatc_label= lbl_recibo_interno_rec &_cont 

 Si la respuesta es menor que  "dos" (2) (es decir, no se han tomado un máximo de dos fotografías para este label) entonces se deberá desplegar el botón con las siguientes características 

 Icono: cámara fotográfica 

 label : class=lbl_salida_almacen ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_recibo_interno_rec )  =  Recibo interno de recepción 

 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} , {{eatc_photos. eatc_label }} = lbl_recibo_interno_rec   y  {{eatc_dona_headers. eatc-code }} 

 Botón: "Problemas con la entrega" 
 [TIENE LA MISMA REGLA DE HABILITACIÓN DEL BOTÓN: VER CÓDIGO DE RECOGIDA]  

 Condición para mostrar el botón: 
 Sólo se solo se habilita para anuncios de donación que previamente se les halla presionado el botón " recoge esta donación " o que ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picker_start_datetime" y que el estado del anuncio no sea cancelado (cancelled) y que no haya dato registrado en "eatc-code_verification_datetime" 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-state =scheduled &eatc-picking_checkin_datetime= _novacio &eatc-code_verification_datetime =0000-00-00 %20 00:00:00 

 ***MEJORA: Condición para ocultar el botón: *** 
 El botón se oculta si el estado de la donación es diferente a  scheduled 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-state= !scheduled 

 El botón da acceso a la funcionalidad " Tengo problemas para que me entreguen ". 

 Nota importante: se debe disponer el botón de tal manera que en celulares de pantalla pequeña se pueda ver toda la leyenda y la misma no esté cortada. 

 Botón: firmar documento soporte: 
 Sólo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime"   y que no exista una fecha válida registrada en el campo " eatc_rec_doc_signature_datetime ".  Además se debe validar que el donante ( eatc_donor ), tenga en la información de su cuenta ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{$eatc-donor}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=$eatc-donor ) el parámetro " eatc_rec_doc_signature " marcado con "y" (se deben cumplir las tres condiciones para que aparezca el botón). 

 El botón da acceso a la funcionalidad " Firmar documento soporte ". 

 Botón: Pre-verificar donación: 
 Sólo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime"   y que no exista una fecha válida registrada en el campo " eatc_rec_odds_pre_verification_datetime ".  Además se debe validar que el donante ( eatc_donor ), tenga en la información de su cuenta ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{$eatc-donor}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=$eatc-donor ) el parámetro " eatc_rec_odds_pre_verification " marcado con "y" (se deben cumplir las tres condiciones para que aparezca el botón). 

 El botón da acceso a la funcionalidad " Pre-verficar donación ". 

 Botón: "No validaron código de recogida" 
 Para desplegar este botón se deben aplicar dos reglas (ambas validaciones deben cumplirse): la primera es: 

 Si evaluando la información del donante del anuncio respectivo en la configuración de cuentas ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{$eatc-donor}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=$eatc-donor ), se establece que la cuenta no está habilitada para editar coordenadas edit_coordinates=no ) se cumple la primera condición para habilitar esta funcionalidad. 

 Ejemplo : 
 Para la cuenta "exito" se evalúa su respectiva configuración con el siguiente llamado:  

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia     
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=colombia) 

 Al comprobar que el parámetro " edit_coordinate " tiene como valor " no " se cumple la primera condición para habilitar la funcionalidad para la cuenta en cuestión. 

 La segunda regla es: 

  Sólo se solo se habilita para anuncios con registro de una hora válida en " eatc-picking_checkout_datetime " y que no tenga un registro válido en " eatc_code_verification_datetime " 

 El botón da acceso a la funcionalidad " No me validaron el código de recogida ". 

 B OTÓN: REGISTRAR SALIDA PUNTO DONACIÓN (PARA HACER MANDATORIO OTROS DOS BOTONES)   
 ***MEJORA: validación condicionada según el valor del campo eatc_donation_managers .eatc_sdm: cuando hay un dato en eatc_donation_managers .eatc_sdm no se muestra el botón*** 

 Label : class= lbl_registrar_salida_pod 

 El sistema realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro={{eatc_donations_managers. identificador_unico_registro }}&_cmp= eatc_sdm 

 Si el sistema arroja una respuesta inválida (ejemplo: err_msg : "Unknown column 'eatc_sdm' in 'field list'" ), vacía, nula, o igual a " n " entonces el sistema funcionará como lo viene haciendo: 

 Funcionamiento tradicional (funciona como funcionaba anteriormente): 
 Para habilitar el botón se deben evaluar si ya hay un registro de fecha y hora de check-in y que no haya un registro de fecha y hora de check-out (operador lógico "y" es decir que se deben cumplir las dos validaciones para mostrar el botón 

 Primera validación: que haya un registro válido en eatc_dona_headers. eatc-picking_checkin_datetime   

 Segunda validación: que NO exista un registro valido en eatc_dona_headers .eatc-picking_checkout_datetime para el anuncio en cuestión. 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-picking_checkin_datetime= _NOVACIO &eatc-picking_checkout_datetime= 0000-00-00 %20 00:00:00 &eatc-state= !cancelled 

 Si el sistema arroja como respuesta un "y" , entonces se propone el siguiente nuevo funcionamiento: 

 Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd = y ) ***MEJORA: no se mostrará el botón*** : 
 No se mostrará el botón 

 Implementación para hacer mandatorio la operación afirmativa del botón "firmar documento soporte" 
 Adicional a las anteriores validaciones, si el donante ( eatc_donor ), tiene en la información de su cuenta ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{$eatc-donor}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=$eatc-donor )) el parámetro " eatc_rec_doc_signature " marcado con "y" , se debe validar que el dato de " eatc_dona_header " " eatc_rec_doc_signature_datetime " tenga una fecha válida registrada (diferente a vacía, nula, o 0000-00-00 00:00:00), En caso de no ser así, debe informarlo al usuario para que realice la firma del documento soporte ( operación afirmativa del respectivo botón, que es la operación que estampa una fecha válida en el campo eatc_rec_doc_signature_datetime ). 

 Implementación para hacer mandatorio la operación afirmativa del botón "Pre-verificar donación" 
 Adicional a las anteriores validaciones, si el donante ( eatc_donor ), tiene en la información de su cuenta ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{$eatc-donor}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=$eatc-donor )) el parámetro " eatc_rec_odds_pre_verification " marcado con "y" , se debe validar que el dato de " eatc_dona_header " " eatc_rec_odds_pre_verification_datetime " tenga una fecha válida registrada (diferente a vacía, nula, o 0000-00-00 00:00:00). En caso de no ser así, debe informarlo al usuario para que realice la pre-verificación respectiva ( operación afirmativa del respectivo botón, que es la operación que estampa una fecha válida en el campo eatc_rec_odds_pre_verification_datetime ). 

 ***NUEVO: validación toma de fotografías, antes de desplegar el acceso a la funcionalidad *** 

 Para realizar esta validación el sistema requiere en este punto los siguientes datos: 

 Cuenta maestra: {{_DOM. cua_master }} 
 Código del anuncio de donación: {{eatc_dona_headers. eatc-code }} 
 Label del presente botón: {{ button_label }} = lbl_registrar_salida_pod 

 Con el label del botón, y una vez el usuario lo presione, el sistema deberá realizar la siguiente consulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_mandatory= y &eatc_validation_point={{ button_label }} 

 Que para el caso específico de este botón sería: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_mandatory= y &eatc_validation_point= lbl_registrar_salida_pod 

 Si la consulta NO arroja una respuesta válida , entonces el botón dará acceso a la funcionalidad " entrega de donación: hora de salida " 

 Si la consulta arroja una respuesta válida, entonces el sistema realiza, con uno de los datos obtenidos en la anterior consulta ( {{eatc_photos. eatc_label }} ), la siguiente: 
 {{ URL_datagov }}/api/eatcloud/eatc_photo_registry?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona_headers. eatc-code }}&eatc_label={{ eatc_photos. eatc_label }}&_cont 

 Si la respuesta es igual a cero (0) entonces deberá desplegar un cuadro de diálogo de la siguiente manera 

 ( label = {{eatc_photos. eatc_validation_message }} ) 

 Y con un botón que tenga las siguientes características 
 Icono: cámara fotográfica 
 label: {{eatc_photos. eatc_label }} 
 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} , {{eatc_photos. eatc_label }} y {{eatc_dona_headers. eatc-code }} 

 Si la respuesta es diferente de cero (0) (es decir, existe una fotografia con el label específico, para la donación en cuestión), entonces el sistema dirige a la funcionalidad " entrega de donación: hora de salida " ( sin desplegar la ventana de diálogo y el botón que direige la funcionalidad de toma de fotografías). 

 El botón da acceso a la funcionalidad " entrega de donación: hora de salida ". 

 Ejemplo 1: ambiente de pruebas, cua_master=abaco,  
 Cuenta maestra: abaco 
 Código del anuncio de donación: 000007777 
 Label del presente botón: {{ button_label }} = lbl_registrar_salida_pod 

 El sistema realiza la siguiente la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_cua_master=abaco&eatc_mandatory= y &eatc_validation_point= lbl_registrar_salida_pod   

 Como el sistema no arroja una consulta válida, entonces el botón dirige directamente a la funcionalidad " entrega de donación: hora de salida ". 

 Ejemplo 2: ambiente de pruebas, cua_master=mexico,  
 Cuenta maestra: mexico 
 Código del anuncio de donación: 000007777 
 Label del presente botón: {{ button_label }} = lbl_registrar_salida_pod 

 El sistema realiza la siguiente la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_cua_master=mexico&eatc_mandatory= y &eatc_validation_point= lbl_registrar_salida_pod    

 Como la consulta arroja una respuesta válida, entonces el sistema realiza, con uno de los datos obtenidos en la anterior consulta ({{eatc_photos. eatc_label }}= lbl_salida_almacen ), la siguiente: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photo_registry?eatc_cua_master=mexico&eatc_dona_header_code=000007777&eatc_label=lbl_salida_almacen&_cont   

 Como la respuesta es igual a cero (0) entonces el sistema despliega un cuadro de diálogo de la siguiente manera 
 ( label = {{eatc_photos. eatc_validation_message }}= lbl_salida_almacen_vm  https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_salida_almacen_vm ) 

 "Antes de salir del punto de donación debes tomar una fotografía del documento de salida del almacén o la factura del aliado " 

 Y con un botón que tenga las siguientes características 
 Icono: cámara fotográfica 
 label: class={{eatc_photos. eatc_label }}= lbl_salida_almacen ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_salida_almacen ) =  Salida Almacen - Factura Aliado   
 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} = mexico, {{eatc_photos. eatc_label }} = lbl_salida_almacen  y {{eatc_dona_headers. eatc-code }} = 000007777 

 Botón: califica al donante: 
 Condición para mostrar el botón: ***MEJORA: implementación operación lógica _novacio (se deberá validar con Jesús si esta operación lógica opera también con fechas vacías 0000-00-00 00:00:00) *** 

 Solo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime" . Una vez se acciona y se genera la calificación el botón debe desaparecer. 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-picking_checkin_datetime= _novacio 

 ***MEJORA: Condición para ocultar el botón: *** 
 El botón se oculta si no existe un registro válido en el dato "eatc-picking_checkin_datetime" 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-picking_checkin_datetime= 0000-00-00 %20 00:00:00 
 El botón da acceso a la funcionalidad " Calificación punto de donación ". 

 Botón: Chequear donación recogida 
 Condición para mostrar el botón: ***MEJORA: implementación operación lógica _novacio (se deberá validar con Jesús si esta operación lógica opera también con fechas vacías 0000-00-00 00:00:00). Incorpora validación de no haber una verificación detallada previa (eatc-receipt_datetime) *** 
 Solo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime" .   y Que no tengan un registro válido en el campo "eatc-check_datetime" 

 Lo que se quiere decir con esto es que si existe un registro en eatc-receipt_datetime, 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} &eatc-picking_checkin_datetime= _novacio &eatc-check_datetime=0000-00-00 %20 00:00:00 

 ***MEJORA: Condición para ocultar el botón: *** 
 El botón no puede aparecer si existe un dato registrado en " eatc-receipt_datetime " (una fecha válida) aun así la condición de que opere para mostrar el botón sea válida.  En otras palabras si no existe una fecha válida de chequeo ( eatc-check_datetime ) y existe una fecha válida de recepción ( eatc-receipt_datetime ), el botón se deberá ocultar 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-id= {{ eatc-id }} & eatc-receipt_datetime = _novacio 

 El botón da acceso a la funcionalidad " Chequeo de donación ". 

 Botón: verifica tu donación ***NUEVO: validación condicionada según el valor del campo eatc_donation_managers .eatc_sdm*** 

 Label : class= lbl_verificar_donacion 

 El sistema realiza la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro={{eatc_donations_managers. identificador_unico_registro }}&_cmp= eatc_sdm 

 Si el sistema arroja una respuesta inválida (ejemplo: err_msg : "Unknown column 'eatc_sdm' in 'field list'" ), vacía, nula, o igual a " n " entonces el sistema funcionará como lo viene haciendo: 

 Funcionamiento tradicional (funciona como funcionaba anteriormente): 
 Solo se solo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado una fecha válida en el campo  "eatc-picking_checkout_datetime"   y que NO tengan una fecha válida registrada en " eatc-receipt_datetime "  (anteriormente era solamente en eatc-picking_checkout_datetime ) 

 (****NUEVO******: Se quita esta validación:   (nueva validación) cuyo estado "eatc-state" sea "delivered" , y se deja solamente la condición de una fecha válida en el campo " eatc-receipt_datetime " y en  "eatc-picking_checkout_datetime" ) 

 Si el sistema arroja como respuesta un "y", entonces se propone el siguiente nuevo funcionamiento: 

 Nuevo Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd = y ) : 

 Se habilita para anuncios de donación ( eatc_dona_headers ) que NO tengan una fecha válida registrada en " eatc-receipt_datetime " . 

 NUEVO : Para establecer si se cumple esta condición, con el dato del código de la donación se envía a la siguiente consulta, con el dato de fecha de recepción "vacia" (0000-00-00 00:00:00)  

 {{ URL_entorno_donantes }}/api/{{ _DOM.cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&eatc-receipt_datetime=0000-00-00%2000:00:00&_cmp=eatc-receipt_datetime 

  si el servicio responde con la fecha vacía, quiere decir que el botón de verificación debe aparecer (dado que corrobora que no tiene una fecha válida en la fecha de recepción de la donación) 

 (Inicialmente solamente se habilitará para el Banco de Alimentos de Cali: ) 

 ***NUEVO: validación toma de fotografías, antes de desplegar el acceso a la funcionalidad *** 

 Para realizar esta validación el sistema requiere en este punto los siguientes datos: 

 Cuenta maestra: {{_DOM. cua_master }} 
 Código del anuncio de donación: {{eatc_dona_headers. eatc-code }} 
 Label del presente botón: {{ button_label }} = lbl_verificar_donacion  

 Con el label del botón, y una vez el usuario lo presione, el sistema deberá realizar la siguiente consulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_mandatory= y &eatc_validation_point={{ button_label }} 

 Que para el caso específico de este botón sería: 
 {{ URL_datagov }}/api/eatcloud/eatc_photos?eatc_cua_master={{_DOM. cua_master }}&eatc_mandatory= y &eatc_validation_point= lbl_verificar_donacion 

 Si la consulta NO arroja una respuesta válida , entonces el botón dará acceso a la funcionalidad " Verificación detallada de anuncio de donación ". 

 Si la consulta arroja una respuesta válida, entonces el sistema realiza, con uno de los datos obtenidos en la anterior consulta ( {{eatc_photos. eatc_label }} ), la siguiente: 

 {{ URL_datagov }}/api/eatcloud/eatc_photo_registry?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona_headers. eatc-code }}&eatc_label={{ eatc_photos. eatc_label }}&_cont 

 Si la respuesta es igual a cero (0) entonces deberá desplegar un cuadro de diálogo de la siguiente manera 

 ( label = {{eatc_photos. eatc_validation_message }} ) 

 Y con un botón que tenga las siguientes características 
 Icono: cámara fotográfica 
 label: {{eatc_photos. eatc_label }} 
 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} , {{eatc_photos. eatc_label }} y {{eatc_dona_headers. eatc-code }} 

 Si la respuesta es diferente de cero (0) (es decir, existe una fotografia con el label específico, para la donación en cuestión), entonces el sistema dirige a la funcionalidad " Verificación detallada de anuncio de donación " ( sin desplegar la ventana de diálogo y el botón que direige la funcionalidad de toma de fotografías). 

 El botón da acceso a la funcionalidad "" Verificación detallada de anuncio de donación ". 

 Ejemplo 1: ambiente de pruebas, cua_master=abaco,  
 Cuenta maestra: abaco 
 Código del anuncio de donación: 000007777 
 Label del presente botón: {{ button_label }} = lbl_verificar_donacion  

 El sistema realiza la siguiente la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_cua_master=abaco&eatc_mandatory= y &eatc_validation_point=lbl_verificar_donacion   

 Como el sistema no arroja una consulta válida, entonces el botón dirige directamente a la funcionalidad " Verificación detallada de anuncio de donación ". 

 Ejemplo 2: ambiente de pruebas, cua_master=mexico,  
 Cuenta maestra: mexico 
 Código del anuncio de donación: 000007777 
 Label del presente botón: {{ button_label }} = lbl_verificar_donacion 

 El sistema realiza la siguiente la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_cua_master=mexico&eatc_mandatory= y &eatc_validation_point=lbl_verificar_donacion   

 Como la consulta arroja una respuesta válida, entonces el sistema realiza, con uno de los datos obtenidos en la anterior consulta ({{eatc_photos. eatc_label }}= " lbl_recibo_interno_rec " , ), la siguiente: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_photo_registry?eatc_cua_master=mexico&eatc_dona_header_code=000007777&eatc_label=lbl_recibo_interno_rec&_cont   

 Como la respuesta es igual a cero (0) entonces el sistema despliega un cuadro de diálogo de la siguiente manera 
 ( label = {{eatc_photos. eatc_validation_message }}= lbl_recibo_interno_rec https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_recibo_interno_rec_vm )  

 "Antes hacer la verificación detallada, debes tomar una fotografía del documento de recibo interno de la institución gestora de donaciones (Banco de Alimentos, Fundación)" 

 Y con un botón que tenga las siguientes características 

 Icono: cámara fotográfica 
 label: class={{eatc_photos. eatc_label }}= lbl_recibo_interno_rec ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_recibo_interno_rec )  =  Recibo interno de recepción   
 Dirige a: funcionalidad de toma de fotografías (envíandole los parámetros: {{_DOM. cua_master }} = mexico, {{eatc_photos. eatc_label }} = lbl_recibo_interno_rec y {{eatc_dona_headers. eatc-code }} = 000007777 

 [***NUEVO***]Botón: PQRs 
 Solo se solo se habilita para anuncios de donación ( eatc_dona_headers ) que tengan registrado un dato en el campo “eatc-picking_checkout_datetime” . 

 El botón da acceso a la funcionalidad " Peticiones, quejas y reclamos ". 

 Contenido del anuncio 

 Este apartado muestra el detalle de anuncio de donación (eatc_dona) mediante una consulta al API se debe traer información de los productos donados que componen el anuncio y listarlos dentro de un colapsible de la siguiente manera: 

 Consulta de detalles de anuncio de donación (eatc_dona) 

 Consulta de información 

 El sistema toma el parámetro " eatc-code " del encabezado de anuncio de donación ( eatc_dona_headers ) y con él se invoca el API de detalles de anuncio de donación ( eatc_dona ) , enviando ese valor en el parámetro eatc-dona_header_code 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona? eatc-dona_header_code ={{ eatc-code }} 

 Ejemplo _DOM. cua_master=abaco: 
 El para el anuncio cuyo " eatc-code " = 40716 ( anuncio cuyo " eatc-id " = 7608059 ) (Carulla Palmas: user : 339; password : (4) 6050294) 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716   
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716&_compress   

 Con la respuesta del API se toma la siguiente información del gestor de donaciones al que se le adjudicó el anuncio: 

 Item: eatc-odd_name 
 Fecha y hora : eatc-date_time 
 Texto secundario : eatc-odd_typology_a 
 Peso en KG : eatc-odd_total_weight_kg 
 Contiene alérgenos : eatc-contains_alergens 
 Fecha de expiración más próxima: eatc-closer_expiration_date 

 ***NUEVO: Botón: Ver adjuntos*** 
Label: class= lbl_ver_adjuntos ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel= lbl_ver_adjuntos ) 
 Condición para el despliegue del botón: el botón se desplegará si al hacer la siguiente consulta, el sistema trae una información válida: 

 {{ URL_entorno_datagov }}/api/ eatcloud / eatc_dona_attachments ?eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_cmp=eatc_doc_name,eatc_doc_url 
Al presionar el botón, el sistema tendrá dos comportamientos, de acuerdo a si la donación tiene varios o un solo adjunto: 
 Varios adjuntos: el sistema presentará un listado de los documentos adjuntos a la donación, según la anterior consulta (desplegando el nombre y haciendo que el mismo lleve a la respectiva URL).  Cuando el usuario haga clic en un nombre, la APP deberá poder mostrar / descargar la imagen o documento que esté relacionado a la donación particular, según sea el caso 
 Un solo adjunto: el sistema directamente al accionar el botón, deberá poder mostrar / descargar la imagen o documento que está relacionado a la donación en cuestión. 

 Mapa del anuncio de donación: seguimiento 
 El mapa muestra la coordenada del anuncio pintada en el mapa ( eatc_lat, eatc_lon ). 

 En términos generales deberá funcionar así: 

 publicado y adjudicado, muestra las coordenadas del almacén;  
 en el estado adjudicado, también el seguimiento (geobeneficiario) que hace la App del beneficiario u Operador logístico,  
 en estado entregado la coordenada del almacén y el seguimiento de la App del beneficiario (geobeneficiario) y el operador logístico, 
 en recibido, verificado y certificado la coordenada del beneficiario. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbeneficiarios-dashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F1456382672-2022-04-13-10.38.08.jpg&ow=575&oh=1280, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbeneficiarios-dashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F1456382672-2022-04-13-10.38.08.jpg&ow=575&oh=1280 
 EatCloud Beneficiarios 

 532.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 313353e5-fd8f-4dd8-9d37-708780324f6c 
 3!1!2 
 https://centralus0-0.pushfp.svc.ms/fluid 
 cea6b70a-9464-4aa1-a65f-1c67ef1bc25b 
 2026-06-17T23:47:02.7301365Z 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-17T15:47:18.1816879Z"}] 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"30a004c5-9919-4590-9124-189295fded9e","SequenceId":9,"FluidContainerCustomId":"d9625c03-d57f-4a44-978b-4b2457b0ccce","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 DASHBOARD DE ANUNCIO DE DONACIÓN (EATC_DONA_DSH)