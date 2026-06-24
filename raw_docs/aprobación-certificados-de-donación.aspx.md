# aprobación-certificados-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 APROBACIÓN DE CERTIFICADOS 

 Label del título: "Aprobación de certificados de donación" 
 class=" lbl_aprobacion_certificados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_aprobacion_certificados )  

 Label de la descripción: 
 class=" lbl_aprobacion_certificados_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_aprobacion_certificados_desc )  

 "Aquí podrás consultar los certificados de donación que requieren de revisión y aprobación por parte de usuarios de la presente plataforma" 

 Listado de de certificados pendientes de aprobación 
 A este listado, que contendrá los botones de acción para aprobar los certificados, presentará en primera medida, que no han sido aprobados, es decir, los que responden a esta consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/ eatc_dona_certifications ?eatc_certification_datetime =0000-00-00%2000:00:00&_compress 
 mostrando primero los más antiguos, y luego los más nuevos, en una tabla que contiene las siguientes columnas 

 ****NUEVO: Casilla de selección para seleccionar o deseleccionar todos (o algunos) precertificados para acciones bulk (aprovación bulk o desaprovación bulk) **** 
 Para los precertificados a los cuales se les construye los botones de aprobación y desaprobación , se les debe desplegar una casilla de selección, con la opción de "seleccionar todos" y que permita realizar acciones bulk de aprobación y desaprobación de los precertificados, que deben funcionar de la misma manera a como funcionan las acciones aprobar y desaprobar de manera individual (pero operando sobre un grupo de pre-certificados) 

 Código:  
 Label : class=" lbl_codigo " 
 Muestra la información contenida en eatc_dona_certifications . eatc_code 

 Fecha y hora:  
 Label : class=" lbl_fecha_hora " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_datetime   

 Identificación tributaria donante:  
 Label : class=" lbl_id_donante " 
 Muestra la información contenida en eatc_dona_certifications . eatc_donor_code 

 ***NUEVO: cua_master: abaco: si el NIT no tiene dígito de verificación, calcularlo y colocarlo *** 
Si el eatc_donor_code, para la cuenta ABACO, no tiene dígito de verificación, el sistema deberá calcularlo (https://codepen.io/gabrielizalo/pen/bJwXaq) y colocarlo en el informe 
 Razón Social:  
 Label : class=" lbl_razon_social " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_donor_fiscal_name 

 Valor total: ***NUEVO: el valor que aparezca con el signo de $ (formato valor) *** 
 Label : class=" lbl_valor_total " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_value 

 Documento(s) soporte  
 Label : class=" lbl_documentos_soporte_tabla " ) 
 Con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certifications_supports ?eatc_certification_code={{eatc_dona_certifications . eatc_code }} se deben obtener los códigos de los soportes ( eatc_certifications_supports .eatc_certification_support_code ), y con ellos se realiza una lista de soportes (con sus códigos) y con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_certification_support_code ={{eatc_certifications_supports .eatc_certification_support_code }} , para traer la información que permite descargar el soporte ( eatc_certification_support_code.eatc_support_file ) se deben activar vínculos en cada uno de esos códigos para descargar el respectivo soporte. 

 ***NUEVO: Detalles *** 
 Nota: esta sección no se documentó inicialmente pero aparece en el desarrollo (como se muestra a continuación).  Esta documentación solamente se levanta para establecer una mejora definida que implica mostrar en dicho listado la fecha y hora de las respectivas aprobaciones) 

 ***NUEVO: Fecha y hora de aprobación*** 
La tabla de detalle deberá complementarse mostrando la información que aparece en la siguiente consulta: 
 {{ URL_entorno_donantes }}/ api /{{ _DOM. cua_master}}/ api /eatc_certification_approval_registry? eatc_certification_code ={{ eatc_dona_certifications .eatc_code}} &_cmp= eatc_approval_datetime   

 Descargar archivo 
 Label : class=" lbl_descargar_archivo " ) 
 Como no  existe un registro válido en  eatc_dona_certifications . eatc_certification_datetime se debe presentar el botón " Descargar borrador " ( class=" lbl_descargar_borrador " ) (en el listado de consultar certificados podrá existir uno con una fecha válida en eatc_dona_certifications . eatc_certification_datetime s e deberá presentar entonces el boton "Descargar soporte" ( class=" lbl_descargar_certificado " ) El botón servirá para descargar el borrador del certificado a partir de la información consignada en: eatc_dona_certifications . eatc_certificate_file 

 Fecha y hora de aprobación: 
 Label : class=" lbl_fecha_hora_aprobacion " ). 
 Muestra la información contenida en eatc_dona_certifications . eatc_certification_datetime . Como no existe una fecha y hora válida registrada, en vez de mostrarla, se deberá mostrar dos cosas, según sea el caso y el rol del usuario: 

 Uno o varios label indicando que el certificado ha sido aprobado por una o diferentes áreas de la empresa; 
 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Con los datos obtenidos en el parámetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parámetro eatc_certification_approval_flow. eatc_approval_by_label . Cada etiqueta debe tener un vínculo que muestre la siguiente información del registro de aprobación 
 ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} )  

 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la información contenida en el parámetro eatc_certification_approval_registry. eatc_approval_datetime 

 Usuario ( class=" lbl_usuario_solo " ): que muestra la información contenida en el parámetro eatc_certification_approval_registry. eatc_bo_user 

 Uno o varios tags con vínculo mostrando las desaprobaciones: indicando que el certificado ha sido desaprobado por una o varias áreas del ente certificador; 

 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Si la consulta no trae información no mostrará nada 

 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente: 

 Con los datos obtenidos en el parámetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parámetro eatc_certification_approval_flow. eatc_disapproval_by_label . Cada etiqueta debe tener un vínculo que muestre la siguiente información del registro de desaprobación ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} )  

 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_approval_datetime 
 Usuario ( class=" lbl_usuario_solo " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_bo_user 

 Explicación: ( class=" lbl_explicacion " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_disapproval_note 

 Un botón para la acción " Aprobar ", según las indicaciones que se entregan en  la siguiente funcionalidad. o en su defecto un mensaje "Pendiente de aprobación" ( class=" lbl_pendiente_aprobacion " ) 

 Aprobación del certificado 

 Definición del rol de aprobación del usuario del sistema (BO beneficiarios) 
 Cada usuario tiene en sus datos registrados, un rol de aprobación ( bo_usuarios. eatc_approval_role ), por eso se debe traer ese dato con la siguiente consulta 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/bo_usuarios? nombre_usuario ={{nombre_usuario}} 

 Con el dato recuperado en bo_usuarios. eatc_approval_role se procede a realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role={{bo_usuarios. eatc_approval_role }} 

 Con los datos  que trae la siguiente consulta, se realizan las labores para determinar si existe los prerequisitos necesarios para realizar la aprobación por parte del rol y toda la información para establecer los botones de acción, las revisiones necesarias y las acciones de aprobación o desaprobación que surgen de la labor. 

 Consulta inicial para mostrar un botón para realizar acciones de aprobación / desaprobación 
 Si el dato del parámetro que se obtiene en eatc_certification_approval_flow. eatc_approval_method es "manual" entonces se pasa a las siguientes evaluaciones para establecer si se muestra el botón de acción "aprobar" 

 Ejemplo (ambiente de pruebas), _DOM .cua_master= abaco, nombre_usuario =logistica : 

 El usuario "abaco" está logeado en el sistema.  Dado que sus datos son: 

 https://devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios? nombre_usuario =logistica 

 y que bo_usuarios. eatc_approval_role = logistica_abaco, entonces el sistema debe realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco 

 Dado que eatc_certification_approval_flow. eatc_approval_method es "manual", entonces el sistema prosigue con las posteriores evaluaciones 

 Evaluación del primer prerrequisito para mostrar el botón de la acción "aprobar" 
 Con el (los) dato(s) que se recuperan de la consulta anterior, en los parámetros: eatc_certification_approval_flow. eatc_precedent_query y el tipo de respuesta que se está esperando según lo registrado en el parámetro eatc_certification_approval_flow. eatc_precedent_query_response se realiza la siguiente consulta y se evalúa su respuesta. 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_certification_approval_registry{{ eatc_certification_approval_flow. eatc_precedent_query}} 

 Si la respuesta es como se espera (según lo establecido en eatc_certification_approval_flow. eatc_precedent_query_response ) se debe revisar el dato que se obtiene en eatc_certification_approval_flow.eatc_querys_operator si no se obtiene dato, o se cumplen las siguientes condiciones, quiere decir que solamente con el primer Query, y su respuesta esperada, se cumple el prerrequisito para la aprobación. 

 Las condiciones que se deben cumplir, así se tenga un dato en el operador y que indica que solo con la primera evaluación vasta son las siguientes: 

 El operador es " y " y la evaluación del primer query no fue exitosa (la prueba lógica de ambos querys  se puede descartar solo con el resultado de la evaluación del primer query) 
 El operador es " o " y la evaluación del primer query  fue exitosa (la prueba lógica de ambos querys puede darse como exitosa solo con el resultado de la evaluación del primero) 

 Ejemplo (ambiente de pruebas), _DOM .cua_master= abaco, nombre_usuario =abaco, eatc_dona_certifications. eatc_code EC-00001-2021 (código que no existe, pero para efectos de esta prueba sirve como ejemplo: 

 Prosiguiendo con el ejemplo anterior y dada la consulta 

 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco&_distinct=eatc_precedent_query 

 se obtienen los siguientes datos: 

 eatc_certification_approval_flow. eatc_precedent_query= ?eatc_code={{eatc_dona_certifications.eatc_code}}&eatc_approval_code=logistica 

 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco&_distinct=eatc_precedent_query_response 

 eatc_certification_approval_flow. eatc_precedent_query_response=invalid 

 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco&_distinct= eatc_querys_operator 

 Como el dato eatc_certification_approval_flow .eatc_querys_operator = sin datos 

 Entonces el sistema debe evaluar la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_certification_approval_registry ?eatc_code={{eatc_dona_certifications.eatc_code}}&eatc_approval_code=logistica 

 Y dado que eatc_dona_certifications.eatc_code= EC-00001-2021  entonces la consulta debe ser: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_certification_approval_registry ?eatc_code= EC-00001-2021 &eatc_approval_code=logistica 

 Como la respuesta es:  

 { 
 ts : "210222093736", 
 op : true, 
 cont : 0, 
 err_msg : "No se produjeron resultados", 
 err_num : "", 
 mem : 0.39, 
 time : "00:00:00" 
 } 

 Es decir una respuesta inválida , y el valor de  
 eatc_certification_approval_flow. eatc_precedent_query_response= invalid , quiere decir que la condición para mostrar el botón se cumple hasta este momento. 

 Como el parámetro eatc_certification_approval_flow .eatc_querys_operator no trae dato, esto quiere decir que no es necesario evaluar el segundo prerrequisito, y se debe pasar a construir el botón de acción "aprobar" como se indica más adelante . 

 Evaluación del segundo prerrequisito para mostrar el botón de la acción "aprobar" 
 Si se obtiene en eatc_certification_approval_flow .eatc_querys_operator un dato, quiere decir que es necesario, en algunos casos) evaluar el eatc_certification_approval_flow .eatc_precedent_query_b   para establecer si se cumplen las condiciones para la aparición del botón de acción.  Los casos son los siguientes: 

 El operador es " y " y la evaluación del primer query fue exitosa 
 El operador es " o " y la evaluación del primer query no fue exitosa 

 En estos dos casos se procede a realizar  la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_certification_approval_registry{{ eatc_certification_approval_flow. eatc_precedent_query_b}} 

 y de acuerdo al dato eatc_certification_approval_flow. eatc_precedent_query_b_response se evalua la respuesta (para establecer si la prueba es exitosa o no exitosa). Con el resultado del segundo término y el operador lógico se establece si el botón de acción "aprobar" se muestra o no, de la siguiente manera. 

 El operador es " y " la evaluación del primer query fue exitosa y la evaluación del segundo query también: se muestra el botón de acción " aprobar ". 
 El operador es " o ", la evaluación del primer query no fue exitosa y y la evaluación del segundo query fue exitosa: se muestra el botón de acción " aprobar " 

 Construcción del botón de acción 
 El botón se construye con el label ( class ) que se aporta en el parámetro eatc_certification_approval_flow .eatc_approval_btn_label . (para el ejemplo anterior del usuario " abaco ", el label del botón deberá ser class=" lbl_aprobacion_logistica " (en español: "Aprobación logística") 

 Construcción de las visualizaciones para realizar la aprobación: descripción 
 Al oprimir el botón de acción aprobación, el sistema debe mostrar la siguiente información (puede ser en un modal): 
 Descripción de la aprobación: se muestra el label (class) que se obtiene del dato eatc_certification_approval_flow .eatc_approval_desc_label (para el ejemplo anterior del usuario " abaco ", el label  ser class=" lbl_aprobacion_logistica_desc " (en español: "Aprobación logística") . 

 Construcción de las visualizaciones para realizar la aprobación: query 
 Con el dato del rol del aprobador ( eatc_certification_approval_flow. eatc_approval_role ), se debe realizar la siguiente consulta, para establecer el query o los querys que se le mostrarán para la realización de su aprobación (en el orden que lo expresan los datos registrados). 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cert_aprv_vis_querys?eatc_approval_role={{eatc_certification_approval_flow. eatc_approval_role }} 

 Con los datos obtenidos se arma la descripción del query: 
eatc_cert_aprv_vis_querys. eatc_label 

 Y el query cómo tal 
 {{eatc_cert_aprv_vis_querys. eatc_enviroment }}/api/{{eatc_cert_aprv_vis_querys. eatc_cua }}/{{eatc_cert_aprv_vis_querys. eatc_object_store }}{{eatc_cert_aprv_vis_querys. eatc_query }} 

 Que traerá los datos que se mostrarán como parámetros a continuación. 
 Ejemplo (ambiente de pruebas), _DOM .cua_master= abaco, nombre_usuario =abaco, eatc_dona_certifications. eatc_code EC-00001-2021 

 Dado que eatc_certification_approval_flow. eatc_approval_role = logistica_abaco, entonces el sistema realiza la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cert_aprv_vis_querys?eatc_approval_role=logistica_abaco 

 Dado que: 

 eatc_cert_aprv_vis_querys. eatc_label ="class=”lbl_comprobacion_anuncios_recibidos” 
 eatc_cert_aprv_vis_querys. eatc_enviroment = {{URL_entorno_donantes}} 
 eatc_cert_aprv_vis_querys. eatc_cua = _DOM. cua_master 
 eatc_cert_aprv_vis_querys. eatc_object_store = eatc_dona_headers 
 eatc_cert_aprv_vis_querys. eatc_query = ?eatc_certificate_code={{eatc_dona_certifications.eatc_code}} 

 Entonces el sistema debe colocar el label: lbl_comprobacion_anuncios_recibidos 

 Realizar la siguiente consulta: 

 {{eatc_cert_aprv_vis_querys. eatc_enviroment }}/api/{{eatc_cert_aprv_vis_querys. eatc_cua }}/{{eatc_cert_aprv_vis_querys. eatc_object_store }}{{eatc_cert_aprv_vis_querys. eatc_query }} 

 es decir: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc_certificate_code={{eatc_dona_certifications.eatc_code}}  

 Qué se traduce en: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc_certificate_code= EC-00001-2021 (PENDIENTE de realización de ejemplo de certificado para que la consulta traiga datos) 

 Y es la consulta que proporcionará los datos para la construcción de los detalles junto con el dato de: 

 eatc_cert_aprv_vis_querys. eatc_code = anuncios_recibidos 
 eatc_cert_aprv_vis_querys. eatc_query_vis = table 

 Construcción de las visualizaciones para realizar la aprobación: detalle (parámetros) 
 Con los códigos de los querys obtenidos en la anterior consulta se debe proceder a presentar los datos obtenidos, para que el aprobador realice su comprobación.  Para determinar qué parámetro se muestra en la visualización (según el tipo de visualización del query: eatc_cert_aprv_vis_querys. eatc_query_vis = table )  y con qué etiqueta, se realiza la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cert_aprv_vis_parameters? eatc_code ={{eatc_cert_aprv_vis_querys. eatc_code }} 

 Y con los datos obtenidos se realiza la visualización de los datos. 

 Continuando con el ejemplo anterior (ambiente de pruebas), _DOM .cua_master= abaco, nombre_usuario =abaco, eatc_dona_certifications. eatc_code EC-00001-2021 

 Dado que eatc_cert_aprv_vis_querys. eatc_code = anuncios_recibidos , el sistema realiza la siguiente consulta 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cert_aprv_vis_parameters? eatc_code = anuncios_recibidos 

 Dado que: eatc_cert_aprv_vis_querys. eatc_query_vis = table 

 El sistema debe construir una tabla con las siguientes columnas: 

 1. ( eatc_cert_aprv_vis_parameters .e atc_order : 1) Código del anuncio :  (label: eatc_cert_aprv_vis_parameters . eatc_label : "class=” lbl_codigo_anuncio ”): toma la información de: eatc_cert_aprv_vis_parameters . eatc_parameter : "eatc-code" es decir de "{{eatc_cert_aprv_vis_querys. eatc_object_store }}. eatc-code " o "eatc_dona_headers. eatc-code " 

 2. ( eatc_cert_aprv_vis_parameters .e atc_order : 2) Estado :  (label: eatc_cert_aprv_vis_parameters . eatc_label : "class=” lbl_estado ”): toma la información de: eatc_cert_aprv_vis_parameters . eatc_parameter : "eatc-state" es decir de "{{eatc_cert_aprv_vis_querys. eatc_object_store }}. eatc-state " o "eatc_dona_headers. eatc-state " 

 3. ( eatc_cert_aprv_vis_parameters .e atc_order : 3) Donante :  (label: eatc_cert_aprv_vis_parameters . eatc_label : "class=” lbl_donante ”): toma la información de: eatc_cert_aprv_vis_parameters . eatc_parameter : "eatc_donor_fiscal_name" es decir de "{{eatc_cert_aprv_vis_querys. eatc_object_store }}. eatc_donor_fiscal_name " o "eatc_dona_headers. eatc_donor_fiscal_name " 

 4. ( eatc_cert_aprv_vis_parameters .e atc_order : 4) Fecha y hora recibido :  (label: eatc_cert_aprv_vis_parameters . eatc_label : "class=” lbl_fecha_hora_recibido ”): toma la información de: eatc_cert_aprv_vis_parameters . eatc_parameter : "eatc-receipt_datetime" es decir de "{{eatc_cert_aprv_vis_querys. eatc_object_store }}. eatc-receipt_datetime " o "eatc_dona_headers. eatc-receipt_datetime 

 5. ( eatc_cert_aprv_vis_parameters .e atc_order : 5) Código certificado :  (label: eatc_cert_aprv_vis_parameters . eatc_label : "class=” lbl_codigo_certificado ”): toma la información de: eatc_cert_aprv_vis_parameters . eatc_parameter : "eatc_certificate_code" es decir de "{{eatc_cert_aprv_vis_querys. eatc_certificate_code }}. eatc-receipt_datetime " o "eatc_dona_headers. eatc_certificate_code 

 Disparador de aprobación 
 Debajo de las visualizaciones se debe colocar de nuevo el botón de aprobar ( eatc_certification_approval_flow .eatc_approval_btn_label . (para el ejemplo anterior del usuario " abaco ", el label del botón deberá ser class=" lbl_aprobacion_logistica " (en español: "Aprobación logística") ), pero en este caso el mismo disparará la aprobación según el dato que se obtiene en el parámetro: eatc_certification_approval_flow. eatc_approval_trigger 

 Para el caso del ejemplo que hemos venido tratando ( https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco ) sería 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_approval_registry &_operacion= insert &eatc_certification_code ={{ eatc_dona_certifications . eatc_code}}& eatc_approval_datetime ={{ timestamp_formato AAAA:MM:DD HH:MM:SS}}& eatc_approval_code =logistica &eatc_approval_type =intermedia& eatc_approval_role =logistica_abaco &eatc_bo_user ={{ bo_usuarios .usuario}} 

 Formulario de desaprobación 
 Al lado del botón de aprobación, se debe presentar un botón de desaprobación ( class=" lbl_desaprobar " (en español: "Aprobación logística") ), que dará entrada a un formulario de desaprobación muy simple que contiene: 

 Motivo de la desaprobación (label: class=" lbl_motivo_desaprobacion ") 
 Descripción: (label: class=" lbl_motivo_desaprobacion_desc ") 
 Cuadro de texto obligatorio. 
 El valor consignado se guarda en la variable ( eatc_disapproval_note ) que se utilizará en el registro de desaprobación. 

 Disparador de aprobación 
 Al confirmar el envío del anterior formulario se debe disparar la desaprobación según lo indica el dato: eatc_certification_approval_flow. eatc_disapproval_trigger 

 Para el caso del ejemplo que hemos venido tratando ( https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_role=logistica_abaco ) sería 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_disapproval_registry &_operacion= insert &eatc_certification_code ={{ eatc_dona_certifications . eatc_code}}& eatc_disapproval_datetime ={{ timestamp_formato AAAA:MM:DD HH:MM:SS}}& eatc_approval_code =logistica& eatc_disapproval_role =logistica_abaco &eatc_bo_user ={{ bo_usuarios .usuario}}& eatc_disapproval_note ={{eatc_disapproval_note}}&eatc_query_a={{ {{eatc_cert_aprv_vis_querys. eatc_enviroment }}/api/{{eatc_cert_aprv_vis_querys. eatc_cua }}/{{eatc_cert_aprv_vis_querys. eatc_object_store }}{{eatc_cert_aprv_vis_querys. eatc_query }} }} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faprobaci%C3%B3n-certificados-de-donaci%C3%B3n%2F1761196393-detalle_ap_cert.png&ow=2560&oh=1600, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faprobaci%C3%B3n-certificados-de-donaci%C3%B3n%2F1761196393-detalle_ap_cert.png&ow=2560&oh=1600 
 Nuevo BO CUA MASTER Beneficiarios 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"Off"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 35d25fe2-f103-4602-b737-09730320fe2b 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 8afded79-46cf-4c3a-b47d-c14af7fcc74a 
 2025-04-15T00:51:48.8489902Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"1bf7ac59-7e03-4ea2-a748-cbef8365a6a9","SequenceId":757,"FluidContainerCustomId":"e83a99b1-bbb6-40d8-a50a-71e8f5431586","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 989.000000000000 

 APROBACIÓN (CERTIFICADOS DE DONACIÓN)