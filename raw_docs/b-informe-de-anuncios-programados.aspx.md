# b-informe-de-anuncios-programados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Dado que con la ltima versin de indicadores generales, estamos eNcontrando que gran cantidad de anuncios  (358 a julio 3 de 2020) se estn quedando en estado "scheduled" sin poder determinar si a donacin fue entregada o no.  Esto nos lleva a la necesidad de generar una herramienta para implementar un proceso que nos ayude a darle cierre a estos anuncios y de esta manera poder obtener indicadores de mejor calidad en la plataforma.  Esta herramienta tambin nos podr servir para analizar los anuncios despachados (delivered) que no completan el proceso para quedar como recibidos (recieved) y que tambin es importante promover se complete el proceso 

 Selector de tipo de anuncio: 
 El informe deber mostrar un selector para establecer el estado:  

 Programados ( scheduled ) 
 Despachados ( delivered ) 

 Ranking de eatc_donation_managers por cantidad de anuncios en este estado 
 Se deber generar una tabla que muestre los Gestores de Donaciones con ms cantidad de anuncios en este estado y que muestre la siguiente informacin: 

 Gestor de donaciones 
 Orden: 1ra columna 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Nmero de anuncios (se ordena por esta columna el listado mostrando de mayor a menor cantidad de anuncios)***DINAMIZAR a partir de _DOM.cua_master 
 Orden: 2da columna 
 La informacin se toma del: count de las siguientes consultas segn sea el caso 
 {{URL_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state= scheduled &eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&_compress 

 {{URL_donantes}}api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state= delivered &eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code&_compress 

 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin. 

 (***NUEVO***) "Delivered": Nmero de anuncios pendientes de validacin del cdigo de recogida (donante) 
 Label: class="lbl_pendientes_validacion_codigo_recogida" 
 Orden: 2.1 columna 
 La informacin se toma del: count de la siguiente consulta segn sea el caso 
 {{URL_donantes}}api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state= delivered &eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code& eatc_code_verification_datetime =0000-00-00%2000:00:00&_compress 

 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin. 

 (***NUEVO***) "Delivered": Nmero de anuncios pendientes de verificacin del anuncio (beneficiario) 
 Label: class="lbl_pendientes_verificacion_donacion" 
 Orden: 2.2 columna 
 La informacin se toma del: count de la siguiente consulta segn sea el caso 
 {{URL_donantes}}api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state= delivered &eatc-donation_manager_code=eatc_dona_headers .eatc-donation_manager_code& eatc-receipt_datetime =0000-00-00%2000:00:00&_compress 

 Este nmero debe contener un vnculo al detalle de los anuncios con ese estado para el Gestor en cuestin, 

 Telfono(s) 
 Orden: 3ra columna 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_phone ( poder poner todos los telfonos que estn registrados en el maestro eatc_donation_managers para el gestor en cuestin (telefono1, telefono2, telefono3)) 

 Tipo 
 Orden: 4ta columna 
 La informacin se toma de:  eatc_dona_headers .eatc-donation_manager_typology_a 

 Estado 
 Orden: 5ta columna 
 La informacin se toma de:  eatc_donation_managers.eatc-state 

 Detalle de anuncios en este estado 
 Accedido desde el nmero de anuncios del informe anterior, se debe generar una lista con los anuncios con este estado.  La lista debe contener la siguiente informacin y permitir la siguiente edicin de informacin: 

 Buscador: 
 Esta vista debe tener un buscador que permita ubicar de la manera ms amplia posible un anuncio en el listado. 

 Fecha publicacin 
 Orden: 1ra columna 
 La informacin se toma de: eatc_dona_headers .eatc-publication_date 

 Cdigo 
 Orden: 2da columna 
 La informacin se toma del: eatc_dona_headers .eatc-code 

 Donante 
 Orden: 3ra columna 
 La informacin se toma de: eatc_dona_headers .eatc-donor 

 Punto de donacin 
 Orden: 4ta columna 
 La informacin se toma de: eatc_dona_headers .eatc-pod_name 

 Fecha de programacin 
 Orden: 5ta columna 
 La informacin se toma de: eatc_dona_headers .eatc-scheduling_datetime 

 Fecha de programada 
 Orden: 6ta columna 
 La informacin se toma de: eatc_dona_headers .eatc-programed_picking_datetime 

 KG 
 Orden: 7ma columna 
 La informacin se toma de: eatc_dona_headers .eatc-total_weight_kg 

 Estado 
 Orden: 8va columna 
 La informacin se toma de: eatc_dona_headers .eatc-state 

 Al hacerle clic se debe abrir una ventana que permita editar el estado y colocar una observacin. 

 Selector de estado 
 Los estados que podrn ser seleccionados de las siguientes opciones: 

 Anuncios con estado programado ( scheduled ) 
 Despachado ( delivered ) 
 Recibido ( received ) 
 Cancelado ( cancelled ) 
 No entregado ( not_delivered ) 
 [NUEVO] Anunciado ( announced ) 

 Anuncios con estado despachado ( delivered ) 
 Recibido ( received ) 
 Cancelado ( cancelled ) 
 No entregado ( not_delivered ) 

 Cuando se cambie el estado se debe realizar un update a la tabla de eatc_dona_headers con el nuevo estado 
 {{URL_entorno_donantes}}/crd/ {{_DOM. cua_master }} /?_tabla= eatc_dona_headers &_operacion=update & eatc-state ={{nuevo_estado_editado}}& WHERE_eatc-code ={{eatc_dona_headers .eatc-code }} 

 Y realizar un registro de los causales del cambio para poder hacer otros cambios en la informacin del anuncio y registro o modificacin en el registro de issues ( eatc_checkin_and_deliver_issues ) 

 [***NUEVO***] R EGISTRO / MODIFICACIN DE INFORMACIN DE LA INCIDENCIA: 
 El sistema debe validar si para el anuncio en cuestin existe o no un registro de issue previo abierto ( eatc_checkin_and_deliver_issues) , procediendo de acuerdo a dicha circunstancia. 

 Tomando el dato eatc_dona_headers. eatc-code del anuncio que se est consultando, se debe realizar la siguiente consulta: 

 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-issue_cause_code =donation_unknow,eatcloud_unkonw,responsible_not_found,wrongly_delivered,no_validation_process,dona_announced,extemporaneous_code_verification,other& resolved =no 

 E L ANUNCIO NO TIENE UN REGISTRO PREVIO DE ISSUE 
 El sistema debe presentar un formulario de captura de informacin con el nimo de generar un registro en  eatc_checkin_and_deliver_issues que a su vez contenga toda la informacin para ajustar la informacin en " eatc_dona_headers ".  En dicho formulario de captura se recolectan los siguientes datos. 

 Caso 1: anuncio programado que pasa a despachado: 
 Cuando se pasa de estado programado ( scheduled ) a estado despachado ( delivered ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 
 El sistema despliega un formulario que contiene las siguientes opciones: 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico (debe mostrar en el selector la informacin contenida en el parmetro " eatc-type_name " seguida de un guin y la informacin contenida en el parmetro " eatc-issue_cause ", para llevar al registro la informacin contenida en " eatc-issue_cause_code ") 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state=delivered  

 ms el motivo " other ": 

 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state=delivered ms el motivo "other" https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin: obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 A qu organizacin se la entregaron?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code= wrongly_delivered 
 Tipo de dato : sting compuesto (el auto selector muestra el  dato organizacin y obtiene con l tambin el dato identificador_unico_registro 
 Tipo de input de datos: texto predictivo 
 De donde toma los datos para realizar el texto predictivo :  
 {{URL_entorno_beneficiarios}}/api/{{CUA_master}}/eatc_donation_managers? eatc_state = activo 
 Valor por defecto : vaco 
 Obligatoriedad : si 
 Validacin : que los datos guardados correspondan a unos que hallan sido trados en la consulta de datos para la funcin de autocompletar 
 Se guarda en (si hay un registro vlido):  
Registro de problemas de checkin y despacho: identificador_unico_registro se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_code y organizacin se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_name. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 
 Actualizacin de datos del encabezado de anuncio de donacin: con los datos capturados se realiza el proceso de actualizacin de datos del encabezado que se detalla ms adelante cuando la causa es  wrongly_delivered y cuando es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable (en caso de que exista dicha informacin) 
 De dnde toman los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cuando la causa es  wrongly_delivered y cuando es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 Cuando se hace el cambio de estado se deben actualizar las fechas y horas (de manera obligatoria) correspondientes de la siguiente manera (el sistema presentar un datetime picker para que el usuario realice estos registros: 

 Fecha y hora de llegada al punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la hora registrada en eatc_dona_headers .eatc-programed_picking_datetime 
 Validaciones :  
 La fecha y hora no puede ser menor a eatc_dona_headers .eatc-adjudication_datetime   
 La fecha no puede ser mayor a la que se origina de sumarle el dona_global_scheduling_timeout respectivo a la eatc_dona_headers .eatc-adjudication_datetime   (que se obtiene con la consulta {{URL_entorno_donantes}}/api/ {{CUA_master}} /eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout siendo en este caso el CUA_master la cuenta del BO es decir "abaco" 
 Se guarda en : eatc_dona_headers .eatc-picking_checkin_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es  wrongly_delivered y cuando es diferente a wrongly_delivered y dona_announced . 
 Fecha y hora de salida del punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms 15 minutos. 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms tres horas. 
 Se guarda en : eatc_dona_headers .eatc-picking_checkout_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es  wrongly_delivered y cuando es diferente a wrongly_delivered y dona_announced . 

 Caso 2: anuncio programado que pasa a recibido 
 Cuando se pasa de estado programado ( scheduled ) a estado recibido ( received ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: [a julio de 2020] dropdown nico con el dato "other" seleccionado (dado que a la fecha no existen registro en el maestro de issue cuyo estado inicial sea programado y final recibido 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state= received (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas: 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state= received y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : [a julio de 2020] other 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es diferente a wrongly_delivered . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas: 
 Fecha y hora de llegada al punto de donacin:  
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la hora registrada en eatc_dona_headers .eatc-programed_picking_datetime 
 Validaciones :  
 La fecha y hora no puede ser menor a eatc_dona_headers .eatc-adjudication_datetime   
 La fecha no puede ser mayor a la que se origina de sumarle el dona_global_scheduling_timeout respectivo a la eatc_dona_headers .eatc-adjudication_datetime   (que se obtiene con la consulta {{URL_entorno_donantes}}/api/ {{CUA_master}} /eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout siendo en este caso el CUA_master la cuenta del BO es decir "abaco" 
 Se guarda en : eatc_dona_headers .eatc-picking_checkin_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 
 Fecha y hora de salida del punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms 15 minutos. 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms tres horas. 
 Se guarda en : eatc_dona_headers .eatc-picking_checkout_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Fecha y hora de recepcin final de la donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkout_datetime ) ms 1 hora 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms cuatro horas. 
 Se guarda en : eatc_dona_headers .eatc-receipt_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Caso 3: anuncio despachado que pasa a entregado: 
 Cuando se pasa de estado despachado ( delivered ) a estado recibido ( received ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: [a julio de 2020] dropdown nico con el dato "other" seleccionado (dado que a la fecha no existen registro en el maestro de issue cuyo estado inicial sea programado y final recibido 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=delivered&eatc-final_state= received (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas: 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=delivered&eatc-final_state= received y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : [a julio de 2020] " other " 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 Fecha y hora de recepcin final de la donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto: el sistema debe sugerir o poner por defecto la fecha y hora de salida del punto de donacin ( eatc_dona_headers .eatc-picking_checkout_datetime ) ms 1 hora 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms cuatro horas. 
 Se guarda en : eatc_dona_headers .eatc-receipt_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Caso 4: anuncio (programado o despachado) que pasa a "no entregado": 
 Cuando se pasa a estado no entregado ( not_delivered ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico (debe mostrar en el selector la informacin contenida en el parmetro " eatc-type_name " seguida de un guin y la informacin contenida en el parmetro " eatc-issue_cause ", para llevar al registro la informacin contenida en " eatc-issue_cause_code ") 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=not_delivered 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=not_delivered y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other 
 Valor por defecto : vaco 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code=other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Caso 5: anuncio (programado o despachado) que pasa a "cancelado": 
 Cuando pasa a estado cancelado ( cancelled ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: [a julio de 2020] dropdown nico con el dato " other " seleccionado (dado que a la fecha no existen registro en el maestro de issue cuyo estado inicial sea programado y final recibido 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=cancelled (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=cancelled ms el motivo " other " https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : [a julio de 2020] other 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es diferente a wrongly_delivered . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cuando la causa es  wrongly_delivered y cuando es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Caso 6: anuncio programado que pasa a "anunciado": 
 Cuando pasa de estado programado ( scheduled ) a estado anunciado ( announced ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el dato " dona_announced " preseleccionado 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=announced 
 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=announced ms el motivo " other " https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : dona_announced 
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es  dona_announced. 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es  dona_announced. 

 Observaciones: 
 Tipo de dato : sting  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toman los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es  dona_announced. 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Actualizacin de informacin cuando la causa es diferente a wrongly_delivered y dona_announced 
 Cuando el causa del issue es diferente a " wrongly_delivered " y  "d ona_announced ", se procede a realizar el registro del Issue en " eatc_checkin_and_deliver_issues ", el cambio de estado en el encabezado de anuncio de donacin y el respectivo registro en el historial de estado. 

 Registro en eatc_checkin_and_deliver_issues cuando la causa es diferente a wrongly_delivered y dona_announced: 
 Se hace el registro de un issue, por la no entrega de la donacin de la siguiente manera: 

 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: se deja vaco.  
 eatc-final_doma_name: se deja vaco. 
 eatc-dona_initial_state : se toma del estado inicial del anuncio eatc-dona_initial_state . 
 eatc-verification_code: se toma de la informacin del anuncio respectivo eatc_dona_headers. eatc-verification_code 
 eatc-token : por el momento se deja vaco. En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : se toma el estado final del anuncio eatc-dona_final_state 
 eatc-issue_cause_code : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause_code 
 eatc-issue_cause : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved : se coloca en este punto: si 
 Escritura con la API (METODO POST):  

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=insert& eatc-date ={{fecha actual en formato AAAA-MM-DD}} & eatc-datetime ={{fecha actual en formato AAAA-MM-DD HH:MM:SS}}& eatc-donor_code ={{eatc_dona_headers. eatc-donor_code }}& eatc-donor ={{eatc_dona_headers. eatc-donor }}& eatc-pod_id ={{ eatc_dona_headers. eatc-pod_id }}& eatc-pod_name ={{eatc_dona_headers. eatc-pod_name }}& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-donation_manager_code ={{eatc_dona_headers. eatc-donation_manager_code }}& eatc-donation_manager_name ={{eatc_dona_headers. eatc-donation_manager_name }}& eatc-final_doma_code =""& eatc-final_doma_name =""& eatc-dona_initial_state ={{ eatc-dona_initial_state }}& eatc-verification_code ={{eatc_dona_headers. eatc-verification_code }}& eatc-token =""& eatc-dona_final_state ={{ eatc-dona_final_state }}& eatc-issue_cause_code ={{ eatc-issue_cause_code }}& eatc-issue_cause ={{ eatc-issue_cause }}& eatc-log =bo_automated_issue_registration& resolved =si 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es diferente a wrongly_delivered y dona_announced: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en , eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 Parmetros_a_actualizar 
 eatc-state: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-dona_final_state 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state ={{eatc_checkin_and_deliver_issues. eatc-dona_final_state }} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es diferente a wrongly_delivered y dona_announced: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime), el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , y las observaciones capturadas en la presente funcionalidad para llevar la concatenacin de dicha informacin al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state ={{eatc_checkin_and_deliver_issues. eatc-dona_final_state }}& eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log ={{eatc_checkin_and_deliver_issues. eatc-issue_cause_code }}:{{eatc_checkin_and_deliver_issues. eatc-issue_cause }}-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 Actualizacin de informacin cuando la causa es wrongly_delivered 
 Cuando la causa del issue es  " wrongly_delivered ", se procede a realizar el respectivo registro del Issue en " eatc_checkin_and_deliver_issues " a realizar el cambio de estado en el encabezado de anuncio de donacin con el correspondiente registro en el historial de estados en el historial de estado.  

 Registro en eatc_checkin_and_deliver_issues cuando la causa es wrongly_delivered: 
 Se hace el registro de un issue, por la no entrega de la donacin de la siguiente manera: 

 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: dato identificador_unico_registro de la respectiva funcionalidad de captura A qu organizacin se la entregaron ? 
 eatc-final_doma_name: dato organizacin de la respectiva funcionalidad de captura A qu organizacin se la entregaron ? 
 eatc-dona_initial_state : " scheduled " 
 eatc-verification_code: se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token : por el momento se deja vaco. En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : " delivered ".  
 eatc-issue_cause_code : se coloca  wrongly_delivered 
 eatc-issue_cause : se coloca Entregaron a otra fundacin 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved :  se coloca " si ".  
 Escritura con la API (METODO POST):   

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=insert& eatc-date ={{fecha actual en formato AAAA-MM-DD}} & eatc-datetime ={{fecha actual en formato AAAA-MM-DD HH:MM:SS}}& eatc-donor_code ={{eatc_dona_headers. eatc-donor_code }}& eatc-donor ={{eatc_dona_headers. eatc-donor }}& eatc-pod_id ={{ eatc_dona_headers. eatc-pod_id }}& eatc-pod_name ={{eatc_dona_headers. eatc-pod_name }}& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-donation_manager_code ={{eatc_dona_headers. eatc-donation_manager_code }}& eatc-donation_manager_name ={{eatc_dona_headers. eatc-donation_manager_name }}& eatc-final_doma_code ={{ eatc-final_doma_code }}& eatc-final_doma_name ={{ eatc-final_doma_name }}& eatc-dona_initial_state = scheduled & eatc-verification_code ={{eatc_dona_headers. eatc-verification_code }}& eatc-token =""& eatc-dona_final_state = delivered & eatc-issue_cause_code = wrongly_delivered & eatc-issue_cause =Entregaron%20a%20otra fundacin& eatc-log =bo_automated_issue_registration& resolved = si 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es wrongly_delivered: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en , eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 Parmetros_a_actualizar 
 eatc-state: delivered 
 eatc-verification_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-verification_codeeatc-verification_code 
 eatc-adjudication_datetime: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-datetime 
 eatc-donation_manager_user_doc_id:   se deja = "0" 
 eatc-donation_manager_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-final_doma_code 
 eatc-donation_manager_name:   se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-final_doma_name 
 eatc-donation_manager_address: si el dato que se incorpor en el anterior campo es diferente de "0" o "vaco" se utiliza para ir al maestro de gestores de donacin (enviando ese dato al parmetro " identificador_unico_registro ") para traer el dato " unidad_territorial ".  La consulta que se hace es la siguiente 
 {{URL_entorno_beneficiarios}}/api/{{CUA_master}}/eatc_donation_managers?identificador_unico_registro= eatc-donation_manager_code 
 eatc-donation_manager_phone: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " telefono1 ".  
 eatc-donation_manager_typology_a: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " organizacion_vinculada ".  
 eatc-donation_manager_typology_b: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " eatc_doma_typology_b ".  
 eatc-donation_manager_typology_c: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " tipo_organizacion ".  
 eatc-scheduling_datetime: se deja = "0" 
 eatc-programed_picking_datetime: se toma el dato provisto en el selector correspondiente de Fechas y horas de la presente funcionalidad. 
 eatc-picker_name: se deja = "0" 
 eatc-picker_doc_id: se deja = "0" 
 eatc-picker_license_plate: se deja = "0" 
 eatc-picker_start_datetime: se deja = "0" 
 eatc-picker_lat: se deja = "0" 
 eatc-picker_lon: se deja = "0" 
 eatc-picking_checkin_datetime: se toma el dato provisto en el selector correspondiente de Fechas y horas de la presente funcionalidad. 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& {{Parmetros_a_actualizar}} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es wrongly_delivered: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime)el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , y las observaciones capturadas en la presente funcionalidad para llevar la concatenacin de dicha informacin al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state = delivered & eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log = wrongly_delivered :Entregaron%20a%20otra fundacin-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 Actualizacin de informacin cuando la causa es dona_announced 
 Cuando el causa la causa del issue es " dona_announced" , se procede a realizar el registro del Issue en " eatc_checkin_and_deliver_issues " y el cambio de estado en el encabezado de anuncio de donacin a " announced ", el respectivo registro en el historial de estado. 

 Registro en eatc_checkin_and_deliver_issues cuando la causa es dona_announced: 
 Se hace el registro de un issue, por la no entrega de la donacin de la siguiente manera: 

 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: se deja vaco.  
 eatc-final_doma_name: se deja vaco. 
 eatc-dona_initial_state : se toma de la informacin del anuncio y su estado eatc_dona_headers. eatc-state y debe ser: scheduled . 
 eatc-verification_code: se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token : por el momento se deja vaco. En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : se registra el estado final que se registrar en eatc_dona_headers. eatc-state y es " announced ". 
 eatc-issue_cause_code : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause_code   
 eatc-issue_cause : se toma de a partir de la informacin del selector respectivo de la funcionalidad   eatc-issue_cause 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved : se coloca en este punto: si 

 Escritura con la API (METODO POST):  

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=insert& eatc-date ={{fecha actual en formato AAAA-MM-DD}} & eatc-datetime ={{fecha actual en formato AAAA-MM-DD HH:MM:SS}}& eatc-donor_code ={{eatc_dona_headers. eatc-donor_code }}& eatc-donor ={{eatc_dona_headers. eatc-donor }}& eatc-pod_id ={{ eatc_dona_headers. eatc-pod_id }}& eatc-pod_name ={{eatc_dona_headers. eatc-pod_name }}& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-donation_manager_code ={{eatc_dona_headers. eatc-donation_manager_code }}& eatc-donation_manager_name ={{eatc_dona_headers. eatc-donation_manager_name }}& eatc-final_doma_code =""& eatc-final_doma_name =""& eatc-dona_initial_state = scheduled & eatc-verification_code ={{eatc_dona_headers. eatc-verification_code }}& eatc-token =""& eatc-dona_final_state = announced & eatc-issue_cause_code ={{ eatc-issue_cause_code }}& eatc-issue_cause ={{ eatc-issue_cause }}& eatc-log =bo_automated_issue_registration& resolved =si 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es dona_announced: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en , eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 Parmetros_a_actualizar 
 eatc-state: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-dona_final_state 
 eatc-verification_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-verification_codeeatc-verification_code 
 eatc-adjudication_datetime: se coloca: 0000-00-00 00:00:00 
 eatc-donation_manager_user_doc_id: se coloca: " 0 " 
 eatc-donation_manager_code: se coloca: " 0 " 
 eatc-donation_manager_name:   se coloca: " 0 " 
 eatc-donation_manager_address: se coloca: " 0 " 
 eatc-donation_manager_phone: se coloca: " 0 " 
 eatc-donation_manager_typology_a: se coloca: " 0 "  
 eatc-donation_manager_typology_b: se coloca: " 0 "  
 eatc-donation_manager_typology_c: se coloca: " 0 "  
 eatc-scheduling_datetime: se coloca: " 0 " 
 eatc-programed_picking_datetime: se coloca: 0000-00-00 00:00:00 
 eatc-picker_name: se coloca: " 0 "  
 eatc-picker_doc_id: se coloca: " 0 "  
 eatc-picker_license_plate: se coloca: " 0 "  
 eatc-picker_start_datetime: se coloca: " 0 "  
 eatc-picker_lat: se coloca: " 0 "  
 eatc-picker_lon: se coloca: " 0 "  
 eatc-picking_checkin_datetime: se coloca: 0000-00-00 00:00:00 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& {{Parmetros_a_actualizar}} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es diferente a wrongly_delivered: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime) y el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , para llevarlo al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state = announced & eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log ={{eatc_checkin_and_deliver_issues. eatc-issue_cause_code }}:{{eatc_checkin_and_deliver_issues. eatc-issue_cause }}-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 E L ANUNCIO TIENE UN REGISTRO PREVIO DE ISSUE 
 El sistema debe presentar un formulario de captura de informacin con el nimo de confirmar o actualizar el registro en  eatc_checkin_and_deliver_issues que a su vez contenga toda la informacin para ajustar la informacin en " eatc_dona_headers ".  En dicho formulario de captura se recolectan los siguientes datos.  Esta funcionalidad es muy similar a  la anterior, con la diferencia bsica que toma la informacin del registro previo de eatc_checkin_and_deliver_issues para colocar el valor por defecto de algunos de los formularios de captura y en vez de realizar una insercin de registro en dicho maestro, lo actualiza, de ser necesario. 

 Para deterinar si el anuncio en cuestin tiene un issue asociado, se debe tomar el eatc_dona_headers .eatc-code y realizar la siguiente consulta: 

 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 Caso 1: anuncio programado que pasa a despachado (con registro previo en eatc_checkin_and_deliver_issues): 
 Cuando se pasa de estado programado ( scheduled ) a estado despachado ( delivered ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 El sistema despliega un formulario que contiene las siguientes opciones: 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. 
 La informacin del dropdown se toma de (maestro): 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state=delivered  

 ms el motivo " other ": 

 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state=delivered ms el motivo "other" https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Si hubo un cambio en el motivo, se actualiza el registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin: obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 A qu organizacin se la entregaron?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code= wrongly_delivered 
 Tipo de dato : sting compuesto (el auto selector muestra el  dato organizacin y obtiene con l tambin el dato identificador_unico_registro 
 Tipo de input de datos: texto predictivo 
 De donde toma los datos para realizar el texto predictivo :  
 {{URL_entorno_beneficiarios}}/api/{{CUA_master}}/eatc_donation_managers? eatc_state = activo 
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-final_doma_code 
 eatc-final_doma_name 
 Obligatoriedad : si 
 Validacin : que los datos guardados correspondan a unos que hallan sido trados en la consulta de datos para la funcin de autocompletar 
 Se guarda en (si hay un registro vlido):  
Si hubo un cambio en el dato previamente registrado, se actualiza el registro de problemas de checkin y despacho: identificador_unico_registro se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_code y organizacin se guarda en eatc_checkin_and_deliver_issues .eatc-final_doma_name. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 
 Actualizacin de datos del encabezado de anuncio de donacin: con los datos capturados se realiza el proceso de actualizacin de datos del encabezado que se detalla ms adelante cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable (en caso de que exista dicha informacin) 
 De dnde toman los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 Cuando se hace el cambio de estado se deben actualizar las fechas y horas (de manera obligatoria) correspondientes de la siguiente manera (el sistema presentar un datetime picker para que el usuario realice estos registros: 

 Fecha y hora de llegada al punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la hora registrada en eatc_dona_headers .eatc-programed_picking_datetime 
 Validaciones :  
 La fecha y hora no puede ser menor a eatc_dona_headers .eatc-adjudication_datetime   
 La fecha no puede ser mayor a la que se origina de sumarle el dona_global_scheduling_timeout respectivo a la eatc_dona_headers .eatc-adjudication_datetime   (que se obtiene con la consulta {{URL_entorno_donantes}}/api/ {{CUA_master}} /eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout siendo en este caso el CUA_master la cuenta del BO es decir "abaco" 
 Se guarda en : eatc_dona_headers .eatc-picking_checkin_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 
 Fecha y hora de salida del punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms 15 minutos. 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms tres horas. 
 Se guarda en : eatc_dona_headers .eatc-picking_checkout_datetime . Se detalla ms adelante el proceso de registro en el object store cuando la causa es  wrongly_delivered y cundo es diferente a wrongly_delivered y dona_announced . 

 Caso 2: anuncio programado que pasa a recibido (con registro previo en eatc_checkin_and_deliver_issues) 
 Cuando se pasa de estado programado ( scheduled ) a estado recibido ( received ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state= received (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas: 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=scheduled&eatc-final_state= received y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Si hubo un cambio en el dato previamente registrado, se actualiza el registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra cmo se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado: se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cuando la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas: 
 Fecha y hora de llegada al punto de donacin:  
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la hora registrada en eatc_dona_headers .eatc-programed_picking_datetime 
 Validaciones :  
 La fecha y hora no puede ser menor a eatc_dona_headers .eatc-adjudication_datetime   
 La fecha no puede ser mayor a la que se origina de sumarle el dona_global_scheduling_timeout respectivo a la eatc_dona_headers .eatc-adjudication_datetime   (que se obtiene con la consulta {{URL_entorno_donantes}}/api/ {{CUA_master}} /eatc_timeout_rules?eatc-timeout_name=dona_global_scheduling_timeout siendo en este caso el CUA_master la cuenta del BO es decir "abaco" 
 Se guarda en : eatc_dona_headers .eatc-picking_checkin_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fecha y hora de salida del punto de donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms 15 minutos. 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms tres horas. 
 Se guarda en : eatc_dona_headers .eatc-picking_checkout_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 
 Fecha y hora de recepcin final de la donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto : el sistema debe sugerir o poner por defecto la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkout_datetime ) ms 1 hora 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms cuatro horas. 
 Se guarda en : eatc_dona_headers .eatc-receipt_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Caso 3: anuncio despachado que pasa a entregado (con registro previo en eatc_checkin_and_deliver_issues): 
 Cuando se pasa de estado despachado ( delivered ) a estado recibido ( received ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. 
 La informacin del dropdown se toma de : 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=delivered&eatc-final_state= received (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas: 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-initial_state=delivered&eatc-final_state= received y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 Fecha y hora de recepcin final de la donacin:   
 Tipo de dato : datetime en formato AAAA-MM-DD HH:MM:SS 
 Tipo de input de datos:   datetime picker 
 Obligatorio : si 
 Valor por defecto: el sistema debe sugerir o poner por defecto la fecha y hora de salida del punto de donacin ( eatc_dona_headers .eatc-picking_checkout_datetime ) ms 1 hora 
 Validaciones :  
 La fecha y hora no puede ser menor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) 
 La fecha no puede ser mayor a la fecha y hora registrada en el registro anterior ( eatc_dona_headers .eatc-picking_checkin_datetime ) ms cuatro horas. 
 Se guarda en : eatc_dona_headers .eatc-receipt_datetime . Se detalla ms adelante el proceso de registro en el object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Caso 4: anuncio (programado o despachado) que pasa a "no entregado" (con registro previo en eatc_checkin_and_deliver_issues): 
 Cuando se pasa a estado no entregado ( not_delivered ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. (debe mostrar en el selector la informacin contenida en el parmetro " eatc-type_name " seguida de un guin y la informacin contenida en el parmetro " eatc-issue_cause ", para llevar al registro la informacin contenida en " eatc-issue_cause_code ") 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=not_delivered 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=not_delivered y el motivo " other ": https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other 
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code=other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Caso 5: anuncio (programado o despachado) que pasa a "cancelado" (con registro previo en eatc_checkin_and_deliver_issues): 
 Cuando pasa a estado cancelado ( cancelled ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. 
 La informacin del dropdown se toma de : 
 {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=cancelled (consulta a julio de 2020 vaca) 

 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 
 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=cancelled ms el motivo " other " https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es diferente a wrongly_delivered y dona_announced . 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toma los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en :  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelantecundo la causa es diferente a wrongly_delivered y dona_announced . 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Caso 6: anuncio programado que pasa a "anunciado" (con registro previo en eatc_checkin_and_deliver_issues): 
 Cuando pasa de estado programado ( scheduled ) a estado anunciado ( announced ). Ambos registros (estado inicial: eatc-dona_initial_state y estado final: eatc-dona_final_state ) se deben guardar en una variable para ser registrados en " eatc_checkin_and_deliver_issues " 

 Motivo de la incidencia: 
 Tipo de dato : string 
 Tipo de input de datos: dropdown nico con el valor por defecto seleccionado. 
 La informacin del dropdown se toma de: 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=announced 
 ms el motivo " other ": {{URL_entorno_donantes}}/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other  

 Ejemplo: 
 Para el punto el entorno de pruebas 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si&eatc-final_state=announced ms el motivo " other " https://devdonantes.eatcloud.info/api/eatcloud/eatc_issue_master?eatc-dona_header_manual_state_change=si& eatc-issue_cause_code=other   
 Valor por defecto : se toma el valor registrado en los campos correspondientes del eatc_checkin_and_deliver_issues 
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 eatc-issue_cause_code 
 eatc-issue_cause 
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause_code y eatc_checkin_and_deliver_issues .eatc-issue_cause (esta segunda captura se lleva en todos los casos a excepcin del eatc_not_deliver_causes .eatc-issue_cause_code =other en donde se despliega un campo de captura para obtener la descripcin de la causal ).  Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es  dona_announced. 

 Cul?: 
 [Despliegue condicionado] 
 Despliegue condicionado : se despliega si en el selector anterior se realiz la siguiente eleccin: eatc_not_deliver_causes .eatc-issue_cause_code =other 
 Tipo de dato : string 
 Tipo de input de datos: text area 
 Valor por defecto : vaco 
 Obligatoriedad : si (si se despliega) 
 Validacin : obligatoriedad 
 Se guarda en :  
Registro de problemas de checkin y despacho: eatc_checkin_and_deliver_issues .eatc-issue_cause. Ms adelante se muestra como se hace el registro completo del issue en este object store cundo la causa es  dona_announced. 

 Observaciones: 
 Tipo de dato : string  
 Tipo de input de datos: text area con informacin pre-llenada editable 
 De dnde toman los datos para realizar pre-llenar el rea de texto editable :  
 Se toma la informacin que se obtiene del anterior selector Motivo de la incidencia (eatc-issue_cause_code) con el se realiza la siguiente consulta 

 {{URL_entorno_donantes}}/api/eatcloud//eatc_issue_master?eatc-issue_cause_code={{Motivo de la incidencia.eatc-issue_cause_code}} 

 Para traer la informacin del campo o parmetro " eatc-action " 
 Valor por defecto : El valor que se obtiene de la anterior consulta en el parmetro eatc-action 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en:  
 Historial de estados de anuncio de donacin ( eatc_dona_header_state_history ), campo eatc-log : con los datos capturados se realiza el proceso de actualizacin de datos del historial de estados  que se detalla ms adelante cundo la causa es  dona_announced. 

 Fechas y horas 
 No se despliegan datatime pickers para obtener fechas y horas adicionales. 

 Actualizacin de informacin cuando la causa es diferente a wrongly_delivered y dona_announced (cuando hay registro previo en eatc_checkin_and_deliver_issues) 
 Cuando el causa del issue es diferente a " wrongly_delivered " y  "d ona_announced ", se procede a realizar la actualizacin del Issue en " eatc_checkin_and_deliver_issues ", el cambio de estado en el encabezado de anuncio de donacin y el respectivo registro en el historial de estados. 

 Registro en eatc_checkin_and_deliver_issues cuando la causa es diferente a wrongly_delivered y dona_announced: 
 Con el _id del issue no resuelto correspondiente, que se obtiene con la consulta,  
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 se realiza el respectivo " update ", de aquellos parmetros que fueron modificados a saber (si no se modificaron solo se modifican los parmetros: resolved :" si " y eatc-log : " bo_automated_issue_registration " 

 {{parametros_modificados}} 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-dona_initial_state : se toma del estado inicial del anuncio eatc-dona_initial_state . 
 eatc-verification_code: se toma de la informacin del anuncio respectivo eatc_dona_headers. eatc-verification_code 
 eatc-dona_final_state : se toma el estado final del anuncio eatc-dona_final_state 
 eatc-issue_cause_code : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause_code 
 eatc-issue_cause : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved : se coloca en este punto: si 

 Escritura con la API (METODO POST):  

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=update& {{parametros_modificados}}WHERE_id=_id 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es diferente a wrongly_delivered y dona_announced: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 Parmetros_a_actualizar 
 eatc-state: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-dona_final_state 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& eatc-state ={{eatc_checkin_and_deliver_issues. eatc-dona_final_state }} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es diferente a wrongly_delivered y dona_announced: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime), el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , y las observaciones capturadas en la presente funcionalidad para llevar la concatenacin de dicha informacin al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state ={{eatc_checkin_and_deliver_issues. eatc-dona_final_state }}& eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log ={{eatc_checkin_and_deliver_issues. eatc-issue_cause_code }}:{{eatc_checkin_and_deliver_issues. eatc-issue_cause }}-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 Actualizacin de informacin cuando la causa es wrongly_delivered (cuando hay registro previo en eatc_checkin_and_deliver_issues) 
 Cuando el causal del issue es  " wrongly_delivered ",  se procede a realizar la actualizacin del Issue en " eatc_checkin_and_deliver_issues ", el cambio de estado en el encabezado de anuncio de donacin y el respectivo registro en el historial de estados. 

 Registro en eatc_checkin_and_deliver_issues cuando la causa es  wrongly_delivered: 
 Con el _id del issue no resuelto correspondiente, que se obtiene con la consulta,  
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 
 se realiza el respectivo "update", de aquellos parmetros que fueron modificados a saber (si no se modificaron solo se modifican los parmetros: resolved :" si " y eatc-log : " bo_automated_issue_registration " 

 {{parametros_modificados}} 
 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: dato identificador_unico_registro de la respectiva funcionalidad de captura A qu organizacin se la entregaron ? 
 eatc-final_doma_name: dato organizacin de la respectiva funcionalidad de captura A qu organizacin se la entregaron ? 
 eatc-dona_initial_state : " scheduled " 
 eatc-verification_code: se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token : por el momento se deja vaco. En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : " delivered ".  
 eatc-issue_cause_code : se coloca  wrongly_delivered 
 eatc-issue_cause : se coloca Entregaron a otra fundacin 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved :  se coloca " si ".  

 Escritura con la API (METODO POST):   

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=update& {{parametros_modificados}}WHERE_id=_id 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es wrongly_delivered: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 {{parametros_a_actualizar}} 
 eatc-state: delivered 
 eatc-verification_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-verification_codeeatc-verification_code 
 eatc-adjudication_datetime: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-datetime 
 eatc-donation_manager_user_doc_id:   se deja = "0" 
 eatc-donation_manager_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-final_doma_code 
 eatc-donation_manager_name:   se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-final_doma_name 
 eatc-donation_manager_address: si el dato que se incorpor en el anterior campo es diferente de "0" o "vaco" se utiliza para ir al maestro de gestores de donacin (enviando ese dato al parmetro " identificador_unico_registro ") para traer el dato " unidad_territorial ".  La consulta que se hace es la siguiente 
 {{URL_entorno_beneficiarios}}/api/{{CUA_master}}/eatc_donation_managers?identificador_unico_registro= eatc-donation_manager_code 
 eatc-donation_manager_phone: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " telefono1 ".  
 eatc-donation_manager_typology_a: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " organizacion_vinculada ".  
 eatc-donation_manager_typology_b: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " eatc_doma_typology_b ".  
 eatc-donation_manager_typology_c: utilizando la misma consulta anterior se coloca el dato recuperado en el parmetro " tipo_organizacion ".  
 eatc-scheduling_datetime: se deja = "0" 
 eatc-programed_picking_datetime: se toma el dato provisto en el selector correspondiente de Fechas y horas de la presente funcionalidad. 
 eatc-picker_name: se deja = "0" 
 eatc-picker_doc_id: se deja = "0" 
 eatc-picker_license_plate: se deja = "0" 
 eatc-picker_start_datetime: se deja = "0" 
 eatc-picker_lat: se deja = "0" 
 eatc-picker_lon: se deja = "0" 
 eatc-picking_checkin_datetime: se toma el dato provisto en el selector correspondiente de Fechas y horas de la presente funcionalidad. 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& {{parametros_a_actualizar}} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es wrongly_delivered: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime)el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , y las observaciones capturadas en la presente funcionalidad para llevar la concatenacin de dicha informacin al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state = delivered & eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log = wrongly_delivered :Entregaron%20a%20otra fundacin-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 Actualizacin de informacin cuando la causa es dona_announced (cuando hay registro previo en eatc_checkin_and_deliver_issues) 
 Cuando el causal de issue es  " dona_announced" , se procede a realizar la actualizacin del Issue en " eatc_checkin_and_deliver_issues ", el cambio de estado en el encabezado de anuncio de donacin y el respectivo registro en el historial de estados. 

 Registro en eatc_checkin_and_deliver_issues cuando la causa es dona_announced: 
 Con el _id del issue no resuelto correspondiente, que se obtiene con la consulta,  
 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ?eatc-dona_header={{eatc_dona_headers. eatc-code }}&resolved= no 

 se realiza el respectivo "update", de aquellos parmetros que fueron modificados a saber (si no se modificaron solo se modifican los parmetros: resolved :" si " y eatc-log : " bo_automated_issue_registration " 

 {{parametros_modificados}} 
 eatc-date : fecha actual en formato AAAA-MM-DD 
 eatc-datetime : fecha actual en formato AAAA-MM-DD HH:MM:SS 
 eatc-donor_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor_code 
 eatc-donor : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donor 
 eatc-pod_id : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_id 
 eatc-pod_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-city : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-city 
 eatc-dona_header_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-code 
 eatc-donation_manager_code : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_code 
 eatc-donation_manager_name : se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-donation_manager_name 
 eatc-final_doma_code: se deja vaco.  
 eatc-final_doma_name: se deja vaco. 
 eatc-dona_initial_state : se toma de la informacin del anuncio y su estado eatc_dona_headers. eatc-state y debe ser: scheduled . 
 eatc-verification_code: se toma de la informacin del anuncio respectivo y corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-token : por el momento se deja vaco. En un futuro ser la clave criptogrfica para decodificar el cdigo de verificacin (que se enviar encriptado). 
 eatc-dona_final_state : se registra el estado final que se registrar en eatc_dona_headers. eatc-state y es " announced ". 
 eatc-issue_cause_code : se toma de a partir de la informacin del selector respectivo de la funcionalidad eatc-issue_cause_code   
 eatc-issue_cause : se toma de a partir de la informacin del selector respectivo de la funcionalidad   eatc-issue_cause 
 eatc-log : se coloca lo siguiente (constante para la funcionalidad): bo_automated_issue_registration 
 resolved : se coloca en este punto: si 

 Escritura con la API (METODO POST):  

 {{URL_entorno_donantes}}/crd/eatcloud/?_tabla= eatc_checkin_and_deliver_issues &_operacion=update& {{parametros_modificados}}WHERE_id=_id 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114127", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Actualizacin de informacin de encabezados de donacin cuando la causa es dona_announced: 
 De acuerdo a la informacin suministrada por el usuario en el formulario de la presente funcionalidad y el registro realizado previamente en , eatc_checkin_and_deliver_issues, se construyen los siguientes datos para realizar la actualizacin de informacin del anuncio en el respectivo encabezado ( eatc_dona_headers ) 

 {{parametros_a_actualizar}} 
 eatc-state: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-dona_final_state 
 eatc-verification_code: se toma la informacin del anterior registro de issue as eatc_checkin_and_deliver_issues. eatc-verification_codeeatc-verification_code 
 eatc-adjudication_datetime: se coloca: 0000-00-00 00:00:00 
 eatc-donation_manager_user_doc_id: se coloca: " 0 " 
 eatc-donation_manager_code: se coloca: " 0 " 
 eatc-donation_manager_name:   se coloca: " 0 " 
 eatc-donation_manager_address: se coloca: " 0 " 
 eatc-donation_manager_phone: se coloca: " 0 " 
 eatc-donation_manager_typology_a: se coloca: " 0 "  
 eatc-donation_manager_typology_b: se coloca: " 0 "  
 eatc-donation_manager_typology_c: se coloca: " 0 "  
 eatc-scheduling_datetime: se coloca: " 0 " 
 eatc-programed_picking_datetime: se coloca: 0000-00-00 00:00:00 
 eatc-picker_name: se coloca: " 0 "  
 eatc-picker_doc_id: se coloca: " 0 "  
 eatc-picker_license_plate: se coloca: " 0 "  
 eatc-picker_start_datetime: se coloca: " 0 "  
 eatc-picker_lat: se coloca: " 0 "  
 eatc-picker_lon: se coloca: " 0 "  
 eatc-picking_checkin_datetime: se coloca: 0000-00-00 00:00:00 

 Escritura con la API:  
 {{URL_entorno_donantes}}/crd/{{CUA_master}}/?_tabla=eatc_dona_headers&_operacion=update& {{parametros_a_actualizar}} 

 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190924114847", 
 op : true, 
 cont : 1, 
 mem : 0.74, 
 time : "00:00:00" 
 } 

 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) cuando la causa es diferente a wrongly_delivered: 
 Para el registro del estado en " eatc_checkin_and_deliver_issues. eatc-dona_final_state " se toma la fecha fecha y hora actual (current_datetime) y el causal seleccionado como motivo de la no entrega (y registrado en eatc_checkin_and_deliver_issues) , para llevarlo al respectivo log, realizando el siguiente llamado al CRD 

 {{URL_entorno}}/crd/{{CUA_master}}/?_tabla= eatc_dona_header_state_history &_operacion=insert& eatc-dona_header_code ={{eatc_dona_headers. eatc-code }}& eatc-state = announced & eatc-date_time ={{current_datetime en formato AAAA-MM-DD HH:MM:SS}}& eatc-log ={{eatc_checkin_and_deliver_issues. eatc-issue_cause_code }}:{{eatc_checkin_and_deliver_issues. eatc-issue_cause }}-{{ observaciones }} 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : "00:00:15" 
 } 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 User Administrator 

 INFORME DE ANUNCIOS PROGRAMADOS - DESPACHADOS