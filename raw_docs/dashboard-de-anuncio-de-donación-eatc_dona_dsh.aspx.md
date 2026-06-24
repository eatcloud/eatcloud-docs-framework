# dashboard-de-anuncio-de-donación-eatc_dona_dsh.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta vista se mostrarn los detalles del beneficiario al cual fue asignada la donacin (con su scoring) y de la programacin de su recogida.  

 Detalle de anuncio de donacin: encabezado 
 Este apartado solo se habilita para anuncios de donacin cuyo estado eatc_dona_states ) sea  "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado),  "received" (recibido),  "pre-certified" (pre-certificado) y "certified" (certificado) . Los anuncios con estado " announced" (anunciado) , NO muestran esta informacin. 

 Consulta de anuncios ***Revisar dinamismo a partir de _DOM.cua_master*** 
 El sistema toma el parmetro " eatc-id " del encabezado de anuncio de donacin ( eatc_dona_headers ) seleccionado  desde el listado donde se invoca esta vista ( seguimiento de anuncios de donacin: botn + )  y con l se invoca el respectivo API 

 {{URL_entorno_donantes}}/api/ {{_DOM-cua.master}} /eatc_dona_headers?eatc-id={{{eatc-id}} 

 Ejemplo: 
 El para el anuncio cuyo " eatc-id " = 8687012  

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012    

 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&_compress   

 Con la respuesta del API se toma la siguiente informacin del gestor de donaciones al que se le adjudic el anuncio: 
 Foto (PENDIENTE POR DEFINIR) 
 Nombre: eatc-donation_manager_name 
 Direccin : eatc-donation_manager_address 
 Telfono : eatc-donation_manager_phone 
 Score : eatc-donation_manager_score 
 Nombre de quien recoge: eatc-picker_name 
 Documento de identidad de quien recoge: eatc-picker_doc_id 
 Placa de quien recoge: eatc-picker_license_plate 

 Dado que los datos pueden ser muchos se pueden presentar en un colapsible (por ejemplo colapsar los datos de quien recoge). 

 Mensaje de ALERTA 
 En un lugar muy visible (y en un fondo que lo haga an ms visible, puede ser Rojo) del dashboard de donacin, se debe colocar un mensaje "ALERTA", si y solo si en el campo eatc-warning posee informacin, diferente a 0 o vaca (y no es nulo) y que muestre el contenido del campo eatc-warning del anuncio respectivo. 

 Listado de documentos soporte eatc-doc 
 Arriba del listado de tems, si y solo si en el campo eatc-doc de el eatc_dona respectivo existen registros vlidos, diferente a 0 o vaco (y no es nulo), se debe mostrar el array de dichos eatc_dona.eatc-doc (se debe hacer un distinct para no repetir eatc-doc ), antecedido por la siguiente leyenda: 

 El presente anuncio contiene los siguientes documentos soporte: 

 [NUEVO]: Botn "eliminar anuncio" ***Revisar dinamismo a partir de _DOM.cua_master*** 

 Este apartado solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea  "announced" (anunciado) ,  Es decir, para los anuncios cuyo estado sea diferente a anunciado ( "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado),  "received" (recibido),  "pre-certified" (pre-certificado) y "certified" (certificado) y "cancelled" (cancelado) ) no se les mostrar este botn. 

 Solo se debe desplegar para donaciones creadas a travs de la plataforma. 

 El xito nos solicit que esto solo se le despliegue a donaciones creadas a travs de EatCloud, por lo tanto la herramienta debe (en primera instancia) evaluar si el eatc-code est conformado solo por caracteres numricos, y en este caso ocultar el botn.  Si el eatc-code sigue los estndares de codificacin que tiene la plataforma (y que incluye caracteres alfanumricos), se debe presentar el botn. 

 Eliminar anuncio 
 Al oprimir este botn, Deber salir una alerta que le informe al usuario lo siguiente: 

 Con esta accin borrars por completo el anuncio de donacin y su informacin de detalle. Deseas eliminar el anuncio? 

 Si                  No 

 Si se oprime la opcin "Si" el sistema deber hacer lo siguiente: 

 Validacin del estado "announced": 

 En ese momento se debe validar que el anuncio siga teniendo el estado "anunciado" para poder proceder con las siguientes acciones: 

 Borrado del encabezado 

 {{URL_entorno}}/crd/ {{_DOM.cua_master}}/ ?_tabla=eatc_dona_headers&_operacion=delete&WHEREeatc-code=[eatc_dona_headers.eatc-code] 

 Borrado del detalle 
 {{URL_entorno}}/crd/ {{_DOM.cua_master}} /?_tabla=eatc_dona&_operacion=delete&WHEREeatc-dona_header_code=[eatc_dona_headers.eatc-code] 
 Si se oprime la opcin "No" lo devuelve al dashboard del anuncio. 

 Registro de informacin en la tabla de historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) ***Revisar dinamismo a partir de _DOM.cua_master*** 

 Se registrar el borrado del anuncio " deleted " tomando la fecha en la que se se presion el botn  y en log ( eatc-log ) se colocan los datos de quien realiz el borrado (el eatc-pod_id )  

 {{URL_entorno_donantes}}/crd/ {{DOM.cua_master}} /?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code ={{codigo}}& eatc-state = {{estado}} & eatc-date_time ={{AAAA-MM-DD%20HH:MM:SS}}& eatc-log = eatc-pod_id :{{pod_id}} 

 Ejemplo: cuenta maestra "abaco" ambiente productivo 

 Para el anuncio de donacin cuyo eatc-code = 40717 que fue borrado, a las "2019-11-01 11:11:11" por el eatc-pod_id : "339" 

 Utilizando el API se realiza el siguiente registro: 

 Registro del estado "deleted" :  
 https://donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_header_state_histor y &_operacion=insert& eatc-dona_header_code =40717& eatc-state = deleted & eatc-date_time =2019-11-01%2012:11:11& eatc-log = eatc-pod_id :339 

 Para consultar los estados registrados: https://donantes.eatcloud.info/api/abaco/eatc_dona_header_state_history?eatc-dona_header_code=40717 

 La app debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo: 
 { 
 ts : "190925174723", 
 op : true, 
 cont : 1, 
 last : "7", 
 mem : 0.72, 
 time : 00:00:15 
 } 

 Botn "digitar documento soporte" 
 Este apartado solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea  "announced" (anunciado) ,  "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado),  "received" (recibido),  "pre-certified" (pre-certificado) y "certified" (certificado) . A los anuncios cuyo estado sea diferente a los anteriores (a 30 de julio de 2020: "cancelled" (cancelado) y "not_delivered" (no entregado) pero puede variar en el futuro, por lo tanto es til programar la regla lgica con "direrente a") no se les mostrar este botn. 

 Este botn dar ingreso a la funcionalidad: Registro de documento soporte 

 Botones de accin 
 Este apartado solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea  "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado),  "received" (recibido),  "pre-certified" (pre-certificado) y "certified" (certificado) . Los anuncios con estado " announced" (anunciado) , y "cancelled" (cancelado) NO muestran estos botones. 

 [NUEVO]  Botn: (Antes: registro de llegada de beneficiario) Verificacin de cdigo de recogida 
 Slo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea  "awarded" (adjudicado) , "scheduled" (programado) y ****NUEVO**** "delivered" (despachado) y que no tengan un registro vlido en el campo " eatc_code_verification_datetime ". 

 El botn da acceso a la funcionalidad " Verificacin de cdigo de recogida ". 

 Si para el anuncio en cuestin existe un registro de "issue" no resuelto, se debe colocar al lado del botn una notacin de "urgencia".  Para hacer esa consulta se realiza el siguiente llamado al API respectiva: 

 {{URL_entorno_donantes}}/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code={{eatc_dona_headers. eatc-code }}&resolved=no&_compress 

 Si el sistema provee una respuesta a esta consulta (count diferente de cero) se debe mostrar la notacin de urgencia al lado del botn. 

 [***NUEVO: CLASS de funcionalidad: para ocultarlo a la cuenta exito***] Botn: registro de salida de beneficiario: 
 Clase de funcionalidad " btn_registro_salida_beneficiario " (incorporar al cdigo) 

 Slo se habilita para anuncios de donacin ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime"   y que no tenga un registro vlido en el campo " eatc-picking_checkout_datetime " 

 El botn da acceso a la funcionalidad " entrega de donacin: hora de salida ". 

 Botn: califica al beneficiario (OJO QUE DIFIERE A LO PROPUESTO EN EL MOCKUP): 
 Slo se habilita para anuncios de donacin ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkout_datetime" .  Una vez se acciona y se genera la calificacin el botn debe desaparecer . 
 El botn da acceso a la funcionalidad " entrega de donacin: calificacin beneficiario ". 

 Contenido del anuncio 
 Este apartado muestra el detalle de anuncio de donacin (eatc_dona) mediante una consulta al API se debe traer informacin de los productos donados que componen el anuncio y listarlos dentro de un colapsible de la siguiente manera: 

 Consulta de detalles de anuncio de donacin (eatc_dona) *** Revisar dinamismo a partir de _DOM.cua_master*** 

 El sistema toma el parmetro " eatc-code " del encabezado de anuncio de donacin ( eatc_dona_headers )   y con l se invoca el API de detalles de anuncio de donacin ( eatc_dona ) , enviando ese valor en el parmetro eatc-dona_header_code 

 {{URL_entorno_donantes}}/api/ {{_DOM.cua_master}} /eatc_dona? eatc-dona_header_code = {{ eatc-code}} 

 Ejemplo: 
 El para el anuncio cuyo " eatc-code " = 40716 ( anuncio cuyo " eatc-id " = 7608059 ) (Carulla Palmas: user : 339; password : (4) 6050294) 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716 

 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716&_compress   

 Con la respuesta del API se toma la siguiente informacin del gestor de donaciones al que se le adjudic el anuncio: 
 Item: eatc-odd_name 
 Fecha y hora : eatc-date_time 
 Texto secundario : eatc-odd_typology_a 
 Peso en KG : eatc-odd_total_weight_kg 

 Mapa del anuncio de donacin: seguimiento 
 El mapa muestra la coordenada del anuncio pintada en el mapa (eatc_lat, eatc_lon). 

 En trminos generales deber funcionar as: 
 publicado y adjudicado, muestra las coordenadas del almacn;  
 en el estado adjudicado, tambin el seguimiento (geobeneficiario) que hace la App del beneficiario u Operador logstico,  
 en estado entregado la coordenada del almacn y el seguimiento de la App del beneficiario (geobeneficiario) y el operador logstico, 
 en recibido, verificado y certificado la coordenada del beneficiario. 

 Mensajes emergentes si el check out no se hace segn lo establecido en eatc_timeout_rules despus del check in ***Dinamizar a partir de _DOM.cua_master*** 

 Si no existe registro en el campo eatc-picking_checkout_datetime (o es igual a un registro 0000-00-00 00:00:00) sistema debe peridicamente (puede ser cada 5 minutos) comparar la fecha y hora actual, con la fecha y hora del check in ( eatc-picking_checkin_datetime ), si la diferencia entre esas horas es igual o superior a lo consultado en el esquema de persistencia eatc_timeout_rules respectivo... 

 {{URL_entorno_donantes}}/api/ {{_DOM.cua_master}} /eatc_timeout_rules?eatc-timeout_name=checkout_timeout    

 Ejemplo cuenta maestra "abaco" ambiente de pruebas: 
 https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=checkout_timeout     
 Dado que la respuesta (a 4 de diciembre de 2019) es: 
 { 
 _id : "4", 
 eatc-code : "4", 
 cua : "exito", 
 eatc-timeout_name : "checkout_timeout", 
 eatc-timeout_description : "Tiempo entre el check-in y el check-out (para generacin de alertas)", 
 eatc-timeout_in_minutes : "20", 
 eatc-timeout_in_hours : "0,33", 
 eatc-timeout_from : "eatc-picking_checkin_datetime" 
 } 
 El sistema no debe comparar la hora actual con ( eatc-timeout_from ) eatc-picking_checkin_datetime y si han pasado ( eatc-timeout_in_minutes ) 0,33 horas o ( eatc-timeout_in_hours ) 20 minutos se debe generar el anuncio visible. 

  ... Se debe desplegar un mensaje visible con la siguiente leyenda:   
 Han pasado ms de [eatc_timeout_rules. eatc-timeout_in_minutes https://devdonantes.eatcloud.info/api/abaco/eatc_timeout_rules?eatc-timeout_name=checkout_timeout ] minutos desde el registro de la hora de llegada del beneficiario El beneficiario ya sali de las instalaciones?  

 y debe presentar dos opciones: 

 NO: 

 El sistema no realiza ninguna accin, solo deja de mostrar el letrero, el cual volver a aparecer cuando vuelva a correr el proceso. 

 SI 

 El sistema debe realizar las mismas acciones que realiza en la funcionalidad " Registro de salida de beneficiario " 

 No permitir salir del dashboard hasta no haber registrado la salida del beneficiario 
 Si se intenta salir del dashboard se debe verificar que no exista eatc-picking_checkout_datetime (o es igual a un registro 0000-00-00 00:00:00).  En caso que este dato no se encuentre se debe mostrar el siguiente letrero   
 Est pendiente registrar la hora de salida del beneficiario, por favor regstrala para poder salir del dashboard 

 ***NUEVO: Botn "Editar anuncio"*** 
 Este apartado solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea  "announced" (anunciado) ,  "awarded" (adjudicado) , "scheduled" (programado) . 

 Solo se debe desplegar para donaciones creadas a travs de la plataforma. 
 Esta funcionalidad solo se le despliega a donaciones creadas a travs de EatCloud, por lo tanto la herramienta debe (en primera instancia) evaluar si el eatc-code est conformado solo por caracteres numricos, y en este caso ocultar el botn. Si el eatc-code sigue los estndares de codificacin que tiene la plataforma (y que incluye caracteres alfanumricos), se debe presentar el botn. 
 Esta validacin ya se implement para el botn " Eliminar anuncio " y por lo tanto se puede reciclar el cdigo. 

 Botones e inputs que se habilitan al presionar el botn "Editar anuncio". 
 Al Oprimir el botn de Editar Anuncio, deber ocurrir lo siguiente: 

 A cada lnea del anuncio (tem) se le debe desplegar un botn para borrarla (cono "bote de basura" al lado de la lnea) 
 Al presionar el botn se deber borrar el registro respectivo en eatc_dona ,  
 {{URL_entorno_donantes}}/crd/ {{_DOM.cua_master}} /?_tabla=eatc_dona&_operacion=delete&WHERE _id = {{ _id} 

 A cada lnea del anuncio (tem) se le debe poder cambiar la cantidad (la cantidad debe aparecer en un input numrico editable) 

 El sistema debe habilitar un input numrico en cada cantidad, cuyo valor por defecto sea el registrado en eatc_dona.eatc-odd_original_quantity (que para este tipo de anuncios es igual a atc-odd_quantity ) y que permita al usuario variar dicha cantidad .   

 El sistema tambin debe realizar los clculos respectivos del costo total y el valor total de la lnea del anuncio: 
 Peso total de la mercanca donada: eatc-odd_total_weight_kg: corresponde a la multiplicacin de las unidades digitadas por eatc-odd_unit_weight_kg ( eatc-odd_quantity* eatc-odd_unit_weight_kg) es decir ( {{input}}* eatc-odd_unit_weight_kg). En Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_weight_kg . 
 Costo total de la mercanca donada: eatc-odd_total_cost: corresponde a la multiplicacin de las unidades digitadas por eatc-odd_unit_cost ( eatc-odd_quantity*eatc-odd_unit_cost ) es decir ( {{input}}*eatc-odd_unit_cost ). En Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_cost . 

 Al hacerlo el sistema debe realizar la siguiente operacin de update 
 {{URL_entorno_donantes}}/crd/ {{_DOM.cua_master}} /?_tabla=eatc_dona&_operacion=update&eatc-odd_original_quantity={{ input }}&eatc-odd_quantity={{ input }}& eatc-odd_total_weight_kg={{(input) *( eatc_dona. eatc-odd_unit_weight_kg)}} & eatc-odd_total_cost={{(input) *( eatc_dona. eatc-odd_unit_cost )}} &WHERE _id = {{ _id} 

 Para realizar este input se deben implementar tambin las dos validaciones que se implementan al crear un anuncio de donacin y agregarle la cantidad (que ya estn implementadas en la funcionalidad de agregar un anuncio de donacin y por lo tanto su cdigo se podr reciclar) : 
 Validacin de peso total (eatc-odd_total_weight_kg) cuando el resultado es cero (no se deben permitir que los pesos estn en cero) 
 Validacin de peso total (eatc-odd_total_weight_kg) cuando el resultado es un peso muy elevado 

 Debe aparecer un botn para agregar un nuevo tem (o lnea) al anuncio de donacin. 
 El botn " Agregar nuevo tem " permitir desplegar una funcionalidad que funcione igual a la ya implementada cuando se estn creando los detalles del anuncio de donacin , y por lo tanto su cdigo se deber reutilizar. 

 Debe aparecer un botn para terminar de editar la donacin 
 Al oprimir este botn ( Terminar edicin del anuncio ), si no hubieron cambios en los datos del anuncio que se est editando, no se realiza ninguna funcin de llamado de servicio, pero si se han realizado cambios o ediciones se debe llamar al servicio respectivo para la "regeneracin" del encabezado del anuncio con los nuevos datos ,. 

 Al presionarse este botn (en cualquiera de los casos), tambin se ocultan las funcionalidades / botones que se han descrito arriba ( borrado de lnea (item) , edicin de cantidades , Agregar nuevo tem y este mismo botn, dejando solamente el botn de " Editar anuncio "). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F65577.2%2520detalle%2520anuncio%2520%28eatc_dona_dsh%29.png&ow=375&oh=1636, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-anuncio-de-donaci%C3%B3n-eatc_dona_dsh%2F65577.2%2520detalle%2520anuncio%2520%28eatc_dona_dsh%29.png&ow=375&oh=1636 
 EATCLOUD DONANATES 

 88.0000000000000 

 DASHBOARD DE ANUNCIO DE DONACIN (EATC_DONA_DSH)