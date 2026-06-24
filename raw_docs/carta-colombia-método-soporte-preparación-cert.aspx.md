# carta-colombia-método-soporte-preparación-cert.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Método se Soporte Carta Colombia 
 Diagrama de flujo 

 Al seleccionar este método, el sistema desplegará los siguientes módulos funcionales 

 Método de soporte: carta_colombia: Selector de NITs (para cuenta con múltiples donantes) 
 Método de soporte: carta_colombia: sumatorias para el listado de anuncios soportados 
 Método de soporte: carta_colombia: listado de anuncios soportados 
 Método de soporte: carta_colombia: consulta de detalles consolidados 
 Método de soporte: carta_colombia: aprobación de carta soporte mediante firma 

 Diagrama de flujo 
 Método de soporte: carta_colombia 

 ","cachedEmbedCode":" ","shouldScaleWidth":true,"tempState":{},"thumbnailUrl":"https://lucid.app/documents/thumb/6a308c53-0381-4644-86e3-0312e2d79e2f/0/Some(443324)/NULL/1024","cachedEmbedCodeThumbnail":"https://lucid.app/documents/thumb/6a308c53-0381-4644-86e3-0312e2d79e2f/0/Some(443324)/NULL/1024","title":"Panorama general Certificación donación: carta_colombia: Lucidchart"},"containsDynamicDataSource":false}">

 Si el usuario seleccionó o dejó el selector en la posición del método " carta_colombia " 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ? eatc_dona_certification_support =carta_colombia   

 El sistema obtiene los siguientes datos, que a continuación se detallan de acuerdo a la (por el momento) única opción para este método.  El desarrollo por tanto deberá contemplar la implementación de un caso (el primero) dentro de posibles futuros casos diferentes, que tendrá una opción  de tratamiento (la primera) a partir de los siguientes datos, pero posteriormente la funcionalidad se podrá abrir a nuevas opciones (y combinaciones de opciones) a partir de los datos que se obtienen del método de soporte ( eatc_dona_certification_supports ): 

 _id : "1", 
 eatc_cua_master : "abaco", 
 eatc_dona_certification_support : "carta_colombia", 
 eatc_label : "class=”lbl_carta”", 
 eatc_support_generation_method : "automatico", 
 eatc_support_generation_method_desc_label : "class=”lbl_anuncios_cuyo_soporte_se_genera_automaticament”", 
 eatc_support_generation_frecuency : "mensual", 
 eatc_max_generation_day : "last", 
 eatc_file_extension_to_upload : "", 
 eatc_file_extension_to_validate : "", 
 eatc_months_back_to_support : "1", 
 eatc_montly_cut : "corte", 
 default : "si", 
 eatc_support_generation_method_accept_label : "class=”lbl_aceptacion_metodo_carta_colombia”" 

 Método de soporte: carta_colombia: Selector de NITs (para cuenta con múltiples donantes) 
 label: class=" lbl_selecciona_nit "  

 Si la cuenta respectiva ( _DOM. cua_user ) posee el dato eatc_cua. multiple_donors = si El sistema debe realizar un " select distinct " del dato eatc_dona_headers. eatc-donor_code , de los anuncios del mes en curso y los debe traer a un selector. El usuario deberá escoger un "NIT" y dicho filtro se aplicará al listado de anuncios soportados (es decir que solamente se mostrarán los datos correspondientes al NIT seleccionado) 

 Método de soporte: carta_colombia: sumatorias para el listado de anuncios soportados 
 Se debe presentar totales similares a los que se presentan en la funcionalidad Informe de detalle de anuncios en el BO adicionando solamente el número de anuncios certificables (que es la sumatoria de los anuncios eatc_dona_headers que responden a la consulta que trae los anuncios certificables del mes en curso para construir el listado abajo descrito).  Los labels para estos totales son: 

 Título de los totales: class=" lbl_totales_sumatoria " 
 Kilogramos aprovechados: class=" lbl_kg_aprovechados " 
 Kilogramos no aprovechados: class=" lbl_kg_no_aprovechados " 
 Unidades aprovechadas: class=" lbl_unidades_aprovechadas " 
 Unidades no aprovechadas: class=" lbl_unidades_no_aprovechadas " 
 Total anuncios certificables: class=" lbl_donaciones_certificables " 

 Método de soporte: carta_colombia: listado de anuncios soportados 
 Tal como lo establece el label respectivo eatc_support_generation_method_desc_label ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_anuncios_cuyo_soporte_se_genera_automaticament ) label que se debe mostrar al principio del listado, el sistema despliega un listado de los detalles de los anuncios que son susceptibles de ser soportados por la carta automática que se genera a final de mes (teniendo en cuenta los parámetros eatc_months_back_to_support , eatc_montly_cut , que quieren decir que se tomarán los anuncios del mes en curso para construir la información que se muestra en el listado) .  Dicho listado muestra, para los anuncios que no han sido previamente soportados (es decir, aquellos que cumplen con los parámetros eatc_months_back_to_support , eatc_montly_cut y no se encuentran registrados en la tabla eatc_certification_supports_details : se buscan mandando los códigos del encabezado de donación al parámetro eatc_dona_header_code {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_certification_supports_details? eatc_dona_header_code={{ eatc_dona_headers .eatc-code}} . Los anuncios que se encuentren previamente soportados, deben mostrarse en una tabla cuyo título es class=" lbl_previamente_soportados " abajo de la que se describe a continuación,  con las mismas características, adicionando dos columnas al inicio: una columna cuyo título es class=" lbl_soporte "   y que muestra la información del campo eatc_certification_supports_details. eatc_certification_support_code otra columna cuyo título es class=" lbl_tipo_soporte "   y que muestra la información del campo eatc_certification_supports_details. eatc_dona_certification_support )  los siguientes datos (se comporta de manera muy similar al listado desarrollado para la funcionalidad de Informe de detalle de anuncios en el BO , tanto para el listado, como para los totales, por lo tanto se puede utilizar dicha funcionalidad para reciclar código) , en donde se muestra información del detalle de cada donación acompañada de cierta información de encabezado: 

 ***NUEVO: se excluyen del listado aquellos anuncios de donación que pertenezcan a puntos de donación relacionados en la tabla eatc_doma_certification *** 
 Se ha creado una nueva tabla: {{URL_datagov}}//api/eatcloud/eatc_doma_certification?eatc_cua_user=_* en donde se relacionarán puntos de donación que serán certificados por otras organizaciones (otros beneficiarios). 
 Por lo tanto el sistema deberá consultar los puntos de donación que se encuentren en dicha tabla 
 {{URL_datagov}}//api/eatcloud/ eatc_doma_certification ?eatc_cua_master={{ _DOM. cua_master }} &eatc_cua_user={{ _DOM. cua_user }}&_cmp= eatc_pod_id 
Si la respuesta de la anterior consulta es _ all , querrá decir que todos los puntos, que quiere decir también, todas las donaciones de este donante, no serán certificadas por ABACO.   Si la respuesta arroja códigos de puntos {{array _pod_id}} , Las donaciones de dichos puntos no apaecerán en el listado de anuncios certificables, sino en un listado aparte denominado “Certificados por organizaciones diferentes a ABACO”, incorporando la misma información del listado original (abajo descrito) adicionando una columna que diga “Entidad que certifica” y mostrando para esos anuncios la información que se encuentra en 
 {{URL_datagov}}//api/eatcloud/ eatc_doma_certification ?eatc_cua_master={{ _DOM. cua_master }} &eatc_cua_user={{ _DOM. cua_user }}& eatc_pod_id= {{ eatc_dona_headers. eatc-pod_id }}&_cmp= eatc_certifying_doma_name 
 Los labels que se colocan a continuación servirán como títulos de las respectivas columnas que muestra el informe. La tabla de datos, debe permitir ocultar columnas y demás funcionalidades para ordenar la información por columnas. 

 Código del anuncio 
label: class=" lbl_codigo_anuncio " 
 La información se toma de: eatc_dona_headers .eatc-code 

 Fecha 
label: class=" lbl_fecha_publicacion " 
 La información se toma de: eatc_dona_headers .eatc-publication_date 

 Fecha y hora 
label: class=" lbl_hora_publicacion " 
 La información se toma de: eatc_dona_headers .eatc-publication_datetime 

 Mes 
label: class=" lbl_mes " 
 La información se toma de: eatc_dona_headers .eatc-publication_date (trayendo el mes) 

 Mes recepción (NO ESTABA EN EL INFORME QUE SIRVE COMO BASE) 
label: class=" lbl_mes_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime (trayendo el mes) 

 Estado 
label: class=" lbl_estado " 
 La información se toma de: eatc_dona_headers .eatc-state 

 Código Punto de donación 
label: class=" lbl_codigo_punto_donacion " 
 La información se toma de: eatc_dona .eatc-pod_id 

 Punto de donación 
 label: class=" lbl_pod " 
 La información se toma de: eatc_dona_headers .eatc-pod_name 

 Dirección punto de donación (OJO ID) 
label: id=" lbl_direccion_punto_donacion " 
 La información se toma de: eatc_dona_headers .eatc-pod_address 

 Ciudad 
label: class=" lbl_ciudad " 
 La información se toma de: eatc_dona_headers .eatc-city 

 Código del producto 
label: class=" lbl_codigo_producto " 
 La información se toma de: eatc_dona .eatc-odd_id 

 Nombre del producto 
label: class=" lbl_nombre_producto " 
 La información se toma de: eatc_dona .eatc-odd_name 

 Clasificación del producto 
label: class=" lbl_tipologia_a_producto " 
 La información se toma de: eatc_dona .eatc-odd_typology_a 

 KG Originales 
label: class=" kg_originales " 
 La información se toma de: la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) 

 KG aprovechados 
label: class=" lbl_kg_aprovechados " 
 La información se toma de: eatc_dona .eatc-odd_total_weight_kg 

 KG no aprovechados 
label: class=" lbl_kg_no_aprovechados " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg 

 Unidades aprovechadas 
label: class=" lbl_unidades_aprovechadas " 
 La información se toma de: eatc_dona .eatc-odd_quantity 

 Unidades no aprovechadas 
label: class=" lbl_unidades_no_aprovechadas " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity 

 Causal de Baja 
label: class=" lbl_causal_baja " 
 La información se toma de: eatc_dona .eatc-return_cause 

 Costo total definitivo 
label: class=" kg_costo_total_definitivo " 
 La información se toma de: eatc_dona .eatc-odd_total_cost 

 Costo no aprovechados 
label: class=" kg_costo_no_aprovechados " (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las " Unidades no aprovechadas "  por el costo unitario ( eatc_dona .eatc-unit_cost ) 

 Porcentaje IVA 
label: class=" lbl_porcentaje_iva " 
 La información se toma de: eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
label: class=" lbl_valor_iva " 
 La información se toma de: eatc_dona .eatc-total_VAT 

 Beneficiario 
label: class=" lbl_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Beneficiario dirección 
label: class=" lbl_direccion_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_adress 

 Beneficiario teléfono 
label: class=" lbl_telefono " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_phone 

 Hora de adjudicación 
label: class=" lbl_hora_adjudicacion " 
 La información se toma de: eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega programada 
label: class=" lbl_hora_entrega_programada " 
 La información se toma de: eatc_dona_headers .eatc-programed_picking_datetime 

 Hora de entrega real: llegada 
label: class=" lbl_hora_entrega_real_llegada " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real: salida 
label: class=" lbl_hora_entrega_real_salida " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkout_datetime 

 Fecha recepción 
label: class=" lbl_hora_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime 

 Documento soporte 
label: class=" lbl_documento_soporte " 
 La información se toma de: eatc_dona_headers .eatc-doc 

 Alerta 
label: class=" lbl_alerta " 
 La información se toma de: eatc_dona_headers .eatc-warnin 

 Método de soporte: carta_colombia: consulta de detalles consolidados 
 El sistema deberá proporcionar un botón con el siguiente label 
 label: class=" lbl_consulta_detalles_consolidados "  

 Y que pueda mostrar la siguiente descripción (puede ser como un tooltip): 
 label: class="lbl_consulta_detalles_consolidados_desc"  

 Que debe generar un informe descargable en formato .csv que consolide por código de producto, cantidades, kilogramos, y valores (en una tabla con los siguientes encabezados) y que corresponda en sus sumatorias de valores a las sumatorias del listado de anuncios soportados , dado que estos informes deben 100% consistentes) 

 Código del producto 
label: class=" lbl_codigo_producto " 
 La información se toma de: eatc_dona .eatc-odd_id (no se podrán repetir códigos de producto dentro del informe ya que se consolidan por esta variable) 

 Nombre del producto 
label: class=" lbl_nombre_producto " 
 La información se toma de: eatc_dona .eatc-odd_name (no se podrán repetir nombres de producto dentro del informe ya que al consolidarse por ID, a cada ID diferente le debe corresponder un nombre) 

 Clasificación del producto 
label: class=" lbl_tipologia_a_producto " 
 La información se toma de: eatc_dona .eatc-odd_typology_a 

 KG Originales 
label: class=" kg_originales " 
 La información se toma de: la multiplicación de las unidades originales por el peso unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) consolidado por eatc_dona .eatc-odd_id 

 KG aprovechados 
label: class=" lbl_kg_aprovechados " 
 La información se toma de: eatc_dona .eatc-odd_total_weight_kg consolidado por eatc_dona .eatc-odd_id 

 KG no aprovechados 
label: class=" lbl_kg_no_aprovechados " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg consolidado por eatc_dona .eatc-odd_id 

 Unidades aprovechadas 
label: class=" lbl_unidades_aprovechadas " 
 La información se toma de: eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 

 Unidades no aprovechadas 
label: class=" lbl_unidades_no_aprovechadas " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 

 Costo total definitivo 
label: class=" kg_costo_total_definitivo " 
 La información se toma de: eatc_dona .eatc-odd_total_cost consolidado por eatc_dona .eatc-odd_id 

 Costo no aprovechados 
label: class=" kg_costo_no_aprovechados " (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las " Unidades no aprovechadas "  por el costo unitario ( eatc_dona .eatc-unit_cost ) consolidado por eatc_dona .eatc-odd_id 

 Porcentaje IVA 
label: class=" lbl_porcentaje_iva " 
 La información se toma de: eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
label: class=" lbl_valor_iva " 
 La información se toma de: eatc_dona .eatc-total_VAT consolidado por eatc_dona .eatc-odd_id 

 MÉTODO DE SOPORTE: CARTA_COLOMBIA: APROBACIÓN DE CARTA SOPORTE MEDIANTE FIRMA 
 Listado de soportes ***NUEVO: Selector de documentos firmados y no firmados***** 
 A este listado, que contendrá los botones de acción para aprobar firmando las cartas soportes, se accede por el submenú documentado aquí : 

 El sistema presentará un selector con los siguientes valores:  

 Soportes sin firma (valor por defecto) 
 Label : class=" lbl_soportes_sin_firma " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_soportes_sin_firma ) 
 Consulta para el despliegue del listado : El listado presentará en primera medida, los soportes que no han sido firmados, es decir, los que responden a esta consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ?eatc_dona_certification_support= carta_colombia &eatc_cua={{_DOM. cua_user }}&eatc_signature_datetime= 0000-00-00%2000:00:00 
 Ordenamiento del listado : primero los más ANTIGUOS, y luego los más nuevos. 
 Si la consulta no trae resultados: se despliega el siguiente label:  
 class=" lbl_sin_soportes_no_firmados " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_sin_soportes_no_firmados )  
 "No tienes soportes pendientes de firma. Puedes consultar todos tus soportes" 

 Todos los soportes 
 Label : class=" lbl_todos_los_soportes " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_todos_los_soportes ) 
 Consulta para el despliegue del listado : El listado presentará en primera medida, los soportes que no han sido firmados, es decir, los que responden a esta consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ?eatc_dona_certification_support= carta_colombia &eatc_cua={{_DOM. cua_user }} 
 Ordenamiento del listado : primero los más NUEVOS, y luego los más antiguos. 
 Si la consulta no trae resultados: se despliega el siguiente label:  
 class=" lbl_sin_soportes " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&idlabel= lbl_sin_soportes )  
 "No tienes soportes disponibles." 

 Listado de soportes  
 De acuerdo a las anteriores selecciones, se mostrará la información que traigan las respectivas consultas en una tabla (paginada con un máximo de 20 soportes por página) de la siguiente manera: 

 Código: (label class=" lbl_codigo " ) muestra la información contenida en eatc_certification_supports_headers. eatc_certification_support_code 
 Fecha y hora: (label class=" lbl_fecha_hora " ) muestra la información contenida en eatc_certification_supports_headers. eatc_datetime 
 Soporte: (label class=" lbl_soporte " ) muestra la información contenida en eatc_certification_supports_headers. eatc_dona_certification_support 
 Identificación tributaria donante: (label class=" lbl_id_donante " ) muestra la información contenida en eatc_certification_supports_headers. eatc_donor_code 
 Razón Social: (label class=" lbl_razon_social " ) muestra la información contenida en eatc_certification_supports_headers. eatc_donor_fiscal_name 
 Valor total: (label class=" lbl_valor_total " ) muestra la información contenida en eatc_certification_supports_headers. eatc_value 
 Fecha y hora de aprobación (label class=" lbl_fecha_hora_aprobacion " ) muestra la información contenida en eatc_certification_supports_headers. eatc_signature_datetime . Si para un registro en particular no existe una fecha y hora válida registrada, en vez de mostrarla se deberá mostrar un botón " Aprobar " (label class=" lbl_aprobar " ) que dará ingreso a la siguiente funcionalidad. 
 Documento soporte (label class=" lbl_documento_soporte " ) si existe un registro válido en  eatc_certification_supports_headers. eatc_signature_datetime se debe presentar el botón " Descargar borrador " ( class=" lbl_descargar_borrador " ) y existe una fecha válida se debe presentar el boton "Descargar soporte" ( class=" lbl_descargar_soporte " )  ambos botones deben servir para descargar la carta soporte a partir de la información consignada en: eatc_certification_supports_headers. eatc_support_file 

 Aprobación de documento soporte (firma de la carta soporte) 
 Si el usuario le da clic al botón " Aprobar " (label class=" lbl_aprobar " ), el sistema debe desplegar un formulario para incorporar datos de firma que se guardarán encriptados y en la persistencia eatc_certification_supports_headers y que servirán para aprobar la carta soporte 
 Descripción aprobación "(Se coloca arriba del siguiente formulario ( class=" lbl_aprobar_carta_soporte_desc " ) 

ANTES DEL FORMULARIO  PARA LA FIRMA / APROBACIÓN ***NUEVO: permitir ingreso de valor con decimales *** : 
 El sistema debe mostrar el valor de la carta con el siguiente label: 
 class=" lbl_valor_antes_de_iva " 

 El valor que se muestra es: 
 eatc_certification_supports_headers. eatc_value 

 El usuario podrá editar esta información, ***NUEVO: y podrá ingresar valor con decimales (el sistema deberá controlar para que el separador de decimales sea el estándar necesario para el correcto almacenamiento de los datos) *** . De realizar la edición del valor, el sistema deberá realizar el correspondiente update, incluyendo el parámetro en la actualización de información al realizar la firma . 
 eatc_value={{INPUT}} 

 FORMULARIO PARA LA FIRMA / APROBACIÓN: 

 Nombre de quien firma la carta soporte (label: class= "lbl_firmante_carta_soporte" ) 
 Descripción: nombre de la persona que firma el documento soporte 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_name 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_name ={{ input }} 

 Documento de identidad (label: class=" lbl_doc_id " ) 
 Descripción: documento de identidad de quien firma la carta soporte (puede funcionar como tooltip con la siguiente etiqueta class=" lbl_doc_id_firmante_carta_soporte " ) 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_doc_id 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_doc_id ={{ input }} 

 Cargo del firmante (label: class=" lbl_cargo_firmante " ) 
 Descripción: Selecciona de una de los tres posibles cargos que pueden ser los firmantes de la carta soporte (puede funcionar como tooltip con la siguiente etiqueta class=" lbl_cargo_firmante_carta_soporte " ) 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_position 
 Tipo de dato: string 
 Tipo de input: Selector único de la siguiente lista: Contador, Revisor Fiscal, Representante Legal 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_position ={{ input }} 

 Tarjeta profesional (label: class= "lbl_tarjeta_profesional" ) 
 Descripción: Si seleccionaste el cargo de "Contador" o "Revisor fiscal", debes ingresar su respectiva tarjeta profesional (puede funcionar como tooltip con la siguiente etiqueta class=" lbl_tarjeta_profesional_desc " ) 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_professional_card 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : condicionada (si el anterior input eatc_certification_supports_headers. eatc_position es Contador, Revisor Fiscal entonces el dato es obligatorio .  Por el contrario si el anterior input es Representante Legal entonces el dato no es obligatorio 
 Validación : obligatoriedad condicionada 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_professional_card ={{ input }} 

 Firma (label: class= "lbl_firma" ) 
 Descripción: Sube la respectiva firma en formato gráfico (png, jpg, gif) de no más de 100 KB, para incorporar al documento (puede funcionar como tooltip con la siguiente etiqueta class=" lbl_firma_desc " ) 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_signature 
 Tipo de dato: archivo de imagen 
 Tipo de input: Upload de archivo de imagen (con límite de tamaño para no permitir la subida de archivos grandes) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad, tamaño (Máximo 100 KB) y extensión del archivo (solo permitir: png , jpg , gif ) 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_signature ={{ input }} 

 Botón para guardar los datos "Aprobar carta soporte" ( class=" lbl_aprobar_carta_soporte " ) 

 Cuando se oprime el botón, se realizan también las siguientes dos capturas automáticas: 

 Fecha y hora de la firma (Captura automática en segundo plano) 
 Descripción : Fecha y hora en el cual el usuario de la plataforma entrega los datos para la firma del soporte de la donación. 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_signature_datetime 
 Tipo de dato: datetime (en formato AAAA-MM-DD HH:MM:SS ) 
 Tipo de input: timestamp automático 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_signature_datetime ={{ timestamp}} 

 Usuario BO (Captura automática en segundo plano) 
 Descripción : Usuario del BO (plaraforma EatCloud) que realizó el proceso de firma 
 Información técnica del parámetro: eatc_certification_supports_headers . eatc_bo_user 
 Tipo de dato: string 
 Tipo de input: se toma automáticamente del dato del usuario del BO que realiza la operación de firma 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
{{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_bo_user ={{ input}} 

 PARÁMETROS PARA LA ACTUALIZACIÓN DEL REGISTRO (Con la firma del documento soporte): 
 parametros_firma : 
 eatc_name ={{input}}& eatc_doc_id ={{input}}& eatc_position ={{input}}& eatc_professional_card ={{input}}& eatc_signature ={{input}}& eatc_signature_datetime ={{timestamp}}& eatc_bo_user ={{input}} 

 LLAMADO A CRD PARA ACTUALIZACIÓN DEL REGISTRO (si NO se corrigió el valor de la carta): 
 {{ URL_entorno_donantes }}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_headers &_operacion= update &{{ parametros_firma }} &WHEREeatc_certification_support_code={{ eatc_certification_supports_headers . eatc_certification_support_code}} 

 LLAMADO A CRD PARA ACTUALIZACIÓN DEL REGISTRO (si  se corrigió el valor de la carta): 
 {{ URL_entorno_donantes }}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_headers &_operacion= update &{{ parametros_firma }}& eatc_value={{ INPUT }}&WHEREeatc_certification_support_code={{ eatc_certification_supports_headers . eatc_certification_support_code}} 

 LLAMADO A FUNCION DE ENCRIPTADO: 
 Parámetros de autenticación: consultar aquí . 
 {{ URL_entorno_donantes }}/crypt/{{_DOM. cua_master }}/encrypt?table= eatc_certification_supports_headers &fieldname= eatc_name , eatc_doc_id , eatc_professional_card , eatc_signature 

 LLAMADO A FUNCIÓN QUE CREA EL PRECERTIFICADO 
 Una vez se registran los datos encriptados de la firma, se realiza el llamado a la función que crea el precertificado de la siguiente manera: 
 {{URL_entorno_donantes}}/ cert_crea /{{_DOM. cua_master }}? _support_code = {{ eatc_certification_supports_headers. eatc_certification_support_code}} &tipo_soporte= carta_colombia 

 Si la función responde con un código de certificado , de la siguiente manera: 
 { 
 ts: "211111233942", 
 op: true, 
 res: [ 
 { 
 res_insert_enc: { 
 op: true, 
 cont: 1, 
 } 
 }, 
 { 
 res_upd_enc: { 
 op: true, 
 cont: 1, 
 } 
 }, 
 { 
 update_dona_headers: { 
 op: true, 
 cont: 2, 
 } 
 }, 
 ], 
 codesoprt: "55d20c5234e87b9891e514db938b24b4", 
 codecert: "EC-000036-2021", 
 mem: 0.42, 
 time: "00:00:01", 
 } 

 entonces el proceso termina.   

 Si se obtiene una respuesta con algún tipo de error , de la siguiente manera: 
 { 
 ts: "211112090129", 
 op: false, 
 err_msg: "Sin resultados", 
 err_num: "", 
 } 

  se debe reintentar hasta obtener un código de certificado. 

 M ÉTODO DE SOPORTE: FACTURA_ELECTRONICA_COLOMBIA 

 ","cachedEmbedCode":" ","shouldScaleWidth":true,"tempState":{},"thumbnailUrl":"https://lucid.app/documents/thumb/ac8fe440-a24c-4178-b10f-2ad83d345acd/0/Some(236162)/NULL/1024","cachedEmbedCodeThumbnail":"https://lucid.app/documents/thumb/ac8fe440-a24c-4178-b10f-2ad83d345acd/0/Some(236162)/NULL/1024","title":"Panorama general Certificación donación: factura_electronica_colombia: Lucidchart"},"containsDynamicDataSource":false}">

 Si el usuario seleccionó o dejó el selector en la posición del método " factura_electronica_colombia " 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ? eatc_dona_certification_support =factura_electronica_colombia    

 El sistema obtiene los siguientes datos, que a continuación se detallan de acuerdo a la por el momento única opción para este método.  El desarrollo por tanto deberá contemplar la implementación como un caso dentro de posibles futuros casos diferentes, que por el momento tendrá una opción a partir de los siguientes datos: 

 _id : "2", 
 eatc_cua_master : "abaco", 
 eatc_dona_certification_support : "factura_electronica_colombia", 
 eatc_label : "class=”lbl_factura_electronica_colombiana”", 
 eatc_support_generation_method : "upload", 
 eatc_support_generation_method_desc_label : "class=”lbl_selecciona_anuncios_a_soportar”", 
 eatc_support_generation_frecuency : "a_demanda", 
 eatc_max_generation_day : "6", 
 eatc_file_extension_to_upload : "xml", 
 eatc_file_extension_to_validate : "xml", 
 eatc_months_back_to_support : "1", 
 eatc_montly_cut : "corte", 
 default : "no", 
 eatc_support_generation_method_accept_label : "class=”lbl_aceptacion_metodo_factura_electronica_colombia”" 

 Método de soporte: factura_electronica_colombia: pregunta para determinar si se muestran los auncios del mes anterior o del mes actual 
 Dado que en los datos del método de soporte se encuentra esta información: 

 eatc_support_generation_method: "upload" 
 Esto quiere decir que la generación del soporte para el proceso de precertificación la realiza el usuario, subiendo el documento, el cual debe pasar por el proceso de validación respectivo 

 eatc_support_generation_frecuency: "a_demanda" 
 Lo anterior quiere decir que el soporte " factura_electronica_colombia " se generará a demanda del usuario (por eso se podrá subir cuando el usuario lo determine). 

 eatc_max_generation_day: "6" 
 El sistema debe preguntar hasta el día del mes que se indique en el parámetro eatc_max_generation_day (actualmente hasta el 6to día del mes), si se quieren ver los anuncios del mes anterior (que debe estar seleccionada por defecto) o del mes actual. 
 Label introductorio: class=" lbl_deseas_ver_donaciones_de " 
 Opción por defecto del selector : class=" lbl_mes_anterior " 
 Segunda opción: class=" lbl_mes_actual " 

 Según la selección que realice el usuario, se deberán traer (en los primeros días del mes) los anuncios cuya fecha de recepción ( eatc_dona_headers .eatc-receipt_datetime ) corresponda al mes anterior o al mes actual. 

 Los demás días del mes, no debe mostrar este selector y debe consultar los anuncios cuya fecha de recepción ( eatc_dona_headers .eatc-receipt_datetime ) correspondan al mes en curso (dado que se obtiene esta información del método de soporte: eatc_months_back_to_support : "1" ).   

 NOTA : si el dato del método eatc_months_back_to_support cambia a más meses, los labels del selector deben cambiar a: 
 Opción por defecto del selector : class=" lbl_periodo_anterior " >: {{ eatc_months_back_to_support }} meses. 
 Segunda opción: class=" lbl_periodo_actual " > 

 Y las consultan deberán traer los anuncios correspondientes a los periodos definidos por el dato eatc_months_back_to_support 

 eatc_months_back_to_support: "1" 
 Este parámetro indica que los anuncios aptos para soportarse por una factura (que principalmente cumplen dos condiciones: tienen estado recibido (received) (Es decir que por ejemplo para ambiente de pruebas responden a esta consulta: https://devdonantes.eatcloud.info/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state=received ) y no se les ha expedido constancia de donación (no poseen un registro de fecha válido en eatc_constancy_datetime o no poseen un registro válido en  eatc_constancy_consecutive )) serán los de un mes atrás.  Este dato, combinado con el siguiente, determina el método de consulta para traer los anuncios que serán soportados por la carta automática. 

 eatc_montly_cut: "corte" 
 Esto quiere decir que el conteo del mes para atrás, se hace a corte mensual, es decir que el sistema debe evaluar el dato que llega en el parámetro eatc_dona_headers. eatc-receipt_datetime   para establecer si el mes en el que se recibió el anuncio corresponde al mes en curso (para la implementación del informe de detalle de anuncios, se utilizó una función que establece el mes del anuncio , y esta se puede utilizar para realizar esta validación), desde el primer día del mes hasta el último. 

 Método de soporte: factura_electronica_colombia: Selector de NITs (para cuenta con múltiples donantes) 
 label: class=" lbl_selecciona_nit "  

 Si la cuenta respectiva ( _DOM. cua_user ) posee el dato eatc_cua. multiple_donors = si El sistema debe realizar un " select distinct " del dato eatc_dona_headers. eatc-donor_code , de los anuncios consultados según el criterio definido a partir del selector o consulta anterior (mes actual, mes en curso). El usuario deberá escoger un "NIT" y dicho filtro se aplicará al listado de anuncios soportados (es decir que solamente se mostrarán los datos correspondientes al NIT seleccionado). 

 Método de soporte: factura_electronica_colombia: sumatorias para el listado de anuncios soportados 
 Se debe presentar totales similares a los que se presentan en la funcionalidad Informe de detalle de anuncios en el BO adicionando solamente el número de anuncios certificables (que es la sumatoria de los anuncios eatc_dona_headers que responden los anuncios que se van seleccionando en el listado de anuncios a soportar con factura del que se habla más adelante : 
 Título de los totales: class=" lbl_totales_sumatoria " 
 Kilogramos aprovechados: class=" lbl_kg_aprovechados " 
 Kilogramos no aprovechados: class=" lbl_kg_no_aprovechados " 
 Unidades aprovechadas: class=" lbl_unidades_aprovechadas " 
 Unidades no aprovechadas: class=" lbl_unidades_no_aprovechadas " 
 Total anuncios certificables: class=" lbl_donaciones_certificables " 

 Método de soporte: factura_electronica_colombia: listado de anuncios soportados para seleccionar 
 Tal como lo establece el label respectivo eatc_support_generation_method_desc_label ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_anuncios_a_soportar ) label que se debe mostrar al principio del listado, el sistema despliega un listado de los detalles de los anuncios que son susceptibles de ser soportados por la factura electrónica, permitiendo su selección (mediante un checkbox al inicio de cada registro) .  Los anuncios que se deben mostrar en este listado, corresponde a los del mes en curso desde el primer día del mes ( eatc_dona_certification_supports . eatc_months_back_to_support : "1", y  eatc_dona_certification_supports . eatc_montly_cut : "corte" ). 

 Hasta el día 6 del mes siguiente ( eatc_dona_certification_supports . eatc_max_generation_day ) se podrán mostrar los anuncios del mes anterior (filtrados por el NIT seleccionado anteriormente). Dicho listado muestra los siguientes datos (se comporta de manera muy similar al listado desarrollado para la funcionalidad de Informe de detalle de anuncios en el BO , tanto para el listado, como para los totales, por lo tanto se puede utilizar dicha funcionalidad para reciclar código) , en donde se muestra información del detalle de cada donación acompañada de cierta información de encabezado: 

 Los labels que se colocan a continuación servirán como títulos de las respectivas columnas que muestra el informe. La tabla de datos, debe permitir ocultar columnas y demás funcionalidades para ordenar la información por columnas. 

 Seleccionar 
label: class=" lbl_seleccionar " 
 Checkbox que permite seleccionar el anuncio y a partir de dicha selección realizar las totalizaciones necesarias.  Como es un informe de detalle, al seleccionar un registro, se deben seleccionar automáticamente todos los que tengan su mismo eatc_dona_headers .eatc-code 
 Al seleccionar un anuncio se lleva su eatc_dona_headers .eatc-code al {{ array_codigos_eatc_dona_headers }} , cuando se desmarca se quita el eatc_dona_headers .eatc-code de dicho array. 

 Código del anuncio 
label: class=" lbl_codigo_anuncio " 
 La información se toma de: eatc_dona_headers .eatc-code 

 Fecha 
label: class=" lbl_fecha_publicacion " 
 La información se toma de: eatc_dona_headers .eatc-publication_date 

 Fecha y hora 
label: class=" lbl_hora_publicacion " 
 La información se toma de: eatc_dona_headers .eatc-publication_datetime 

 Mes 
label: class=" lbl_mes " 
 La información se toma de: eatc_dona_headers .eatc-publication_date (trayendo el mes) 

 Mes recepción (NO ESTABA EN EL INFORME QUE SIRVE COMO BASE) 
label: class=" lbl_mes_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime (trayendo el mes) 

 Estado 
label: class=" lbl_estado " 
 La información se toma de: eatc_dona_headers .eatc-state 

 Código Punto de donación 
label: class=" lbl_codigo_punto_donacion " 
 La información se toma de: eatc_dona .eatc-pod_id 

 Punto de donación 
label: class=" lbl_pod " 
 La información se toma de: eatc_dona_headers .eatc-pod_name 

 Dirección punto de donación (OJO ID) 
label: id=" lbl_direccion_punto_donacion " 
 La información se toma de: eatc_dona_headers .eatc-pod_address 

 Ciudad 
label: class=" lbl_ciudad " 
 La información se toma de: eatc_dona_headers .eatc-city 

 Código del producto 
label: class=" lbl_codigo_producto " 
 La información se toma de: eatc_dona .eatc-odd_id 

 Nombre del producto 
label: class=" lbl_nombre_producto " 
 La información se toma de: eatc_dona .eatc-odd_name 

 Clasificación del producto 
label: class=" lbl_tipologia_a_producto " 
 La información se toma de: eatc_dona .eatc-odd_typology_a 

 KG Originales 
label: class=" kg_originales " 
 La información se toma de: la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) 

 KG aprovechados 
label: class=" lbl_kg_aprovechados " 
 La información se toma de: eatc_dona .eatc-odd_total_weight_kg 

 KG no aprovechados 
label: class=" lbl_kg_no_aprovechados " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg 

 Unidades aprovechadas 
label: class=" lbl_unidades_aprovechadas " 
 La información se toma de: eatc_dona .eatc-odd_quantity 

 Unidades no aprovechadas 
label: class=" lbl_unidades_no_aprovechadas " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity 

 Causal de Baja 
label: class=" lbl_causal_baja " 
 La información se toma de: eatc_dona .eatc-return_cause 

 Costo total definitivo 
label: class=" kg_costo_total_definitivo " 
 La información se toma de: eatc_dona .eatc-odd_total_cost 

 Costo no aprovechados 
label: class=" kg_costo_no_aprovechados " (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las " Unidades no aprovechadas "  por el costo unitario ( eatc_dona .eatc-unit_cost ) 

 Porcentaje IVA 
label: class=" lbl_porcentaje_iva " 
 La información se toma de: eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
label: class=" lbl_valor_iva " 
 La información se toma de: eatc_dona .eatc-total_VAT 

 Beneficiario 
label: class=" lbl_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Beneficiario dirección 
label: class=" lbl_direccion_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_adress 

 Beneficiario teléfono 
label: class=" lbl_telefono " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_phone 

 Hora de adjudicación 
label: class=" lbl_hora_adjudicacion " 
 La información se toma de: eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega programada 
label: class=" lbl_hora_entrega_programada " 
 La información se toma de: eatc_dona_headers .eatc-programed_picking_datetime 

 Hora de entrega real: llegada 
label: class=" lbl_hora_entrega_real_llegada " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real: salida 
label: class=" lbl_hora_entrega_real_salida " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkout_datetime 

 Fecha recepción 
label: class=" lbl_hora_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime 

 Documento soporte 
label: class=" lbl_documento_soporte " 
 La información se toma de: eatc_dona_headers .eatc-doc 

 Alerta 
label: class=" lbl_alerta " 
 La información se toma de: eatc_dona_headers .eatc-warning 

 Método de soporte: factura_electronica_colombia: botón "Confirmar anuncios a soportar" 
 En una parte visible del listado, se debe colocar un botón con el label class=" lbl_confirmar_donaciones_soportar " . Al oprimir este botón el sistema realiza lo siguiente: 
 Genera un array con los eatc_dona_headers. eatc-code de las donaciones seleccionadas ( {{ array_codigos_eatc_dona_headers }} ) el cual se utilizará para hacer el llamado al servicio que crea el soporte. 
 Genera un consolidado de productos donados a certificar y 
 Proporcionar un formulario para subir la factura electrónica correspondiente a dichos anuncios 

 Consolidación de productos donados a certificar 
 El sistema deberá generar un listado (que se debe guardar en una persistencia temporal) que consolide los artículos a ser certificados.  

 El sistema deberá proporcionar también botón con el siguiente label 
 label: class=" lbl_consulta_detalles_consolidados "  

 Y que pueda mostrar la siguiente descripción (puede ser como un tooltip): 
 label: class=" lbl_consulta_detalles_consolidados_desc "  

 Que debe permitir descargar el listado consolidado en formato .csv  por código de producto, cantidades, kilogramos, y valores (en una tabla con los siguientes encabezados) y que corresponda en sus sumatorias de valores a las sumatorias del listado de anuncios soportados , dado que estos informes deben 100% consistentes) 

 Código del producto 
label: class=" lbl_codigo_producto " 
 La información se toma de: eatc_dona .eatc-odd_id (no se podrán repetir códigos de producto dentro del informe ya que se consolidan por esta variable) 

 Nombre del producto 
label: class=" lbl_nombre_producto " 
 La información se toma de: eatc_dona .eatc-odd_name (no se podrán repetir nombres de producto dentro del informe ya que al consolidarse por ID, a cada ID diferente le debe corresponder un nombre) 

 Clasificación del producto 
label: class=" lbl_tipologia_a_producto " 
 La información se toma de: eatc_dona .eatc-odd_typology_a 

 KG Originales 
label: class=" kg_originales " 
 La información se toma de: la multiplicación de las unidades originales por el peso unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) consolidado por eatc_dona .eatc-odd_id 

 KG aprovechados 
label: class=" lbl_kg_aprovechados " 
 La información se toma de: eatc_dona .eatc-odd_total_weight_kg consolidado por eatc_dona .eatc-odd_id 

 KG no aprovechados 
label: class=" lbl_kg_no_aprovechados " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg consolidado por eatc_dona .eatc-odd_id 

 Unidades aprovechadas 
label: class=" lbl_unidades_aprovechadas " 
 La información se toma de: eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 

 Unidades no aprovechadas 
label: class=" lbl_unidades_no_aprovechadas " 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de: eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 

 Costo total definitivo 
label: class=" kg_costo_total_definitivo " 
 La información se toma de: eatc_dona .eatc-odd_total_cost consolidado por eatc_dona .eatc-odd_id 

 Costo no aprovechados 
label: class=" kg_costo_no_aprovechados " (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las " Unidades no aprovechadas "  por el costo unitario ( eatc_dona .eatc-unit_cost ) consolidado por eatc_dona .eatc-odd_id 

 Porcentaje IVA 
label: class=" lbl_porcentaje_iva " 
 La información se toma de: eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
label: class=" lbl_valor_iva " 
 La información se toma de: eatc_dona .eatc-total_VAT consolidado por eatc_dona .eatc-odd_id 

 Guardado de datos consolidados en una persistencia 
 El desarrollador puede evaluar la generación de una persistencia (si es una tabla, deberá albergarse en la cuenta maestra correspondiente) para almacenar esta consolidación, ya que posteriormente algunos de sus datos se utilizarán para los procesos de validación de la factura electrónica . 

 Despliegue de formulario para subida de factura electrónica 
 Se debe desplegar un formulario con el siguiente label introductorio class=" lbl_subir_factura_desc " y que debe tener un campo para seleccionar un archivo XML y subirlo a la plataforma (Hasta el día 6 del mes siguiente se podrán subir facturas del mes anterior ( eatc_dona_certification_supports . eatc_max_generation_day )) 
 Place hoder : class=" lbl_factura_electronica_colombia " 
 Botón de subir: class=" lbl_subir_factura_electronica_colombia " 

 Al subir la factura, se debe desplegar el proceso de validación de datos de la misma, que se detalla a continuación. 

 NOTA IMPORTANTE: se debe evaluar si se permite subir el ZIP de la factura electrónica, que contiene el XML y también el PDF, este último importante para procesos de revisión humana de la información. Por lo tanto el localizador podría estar asociado a una carpeta que se cree en el servidor (idelamente con un hash o algo que dificulte su ubicación por quienes no tienen acceso a la plataforma) y que allí se contengan los recursos subidos: XML y PDF. 

 Método de soporte: factura_electronica_colombia: validación de datos de la factura 
 Para la factura electrónica colombiana se efectuarán las siguiente validaciones: 

 La fecha de la factura tiene que corresponder a la fecha de la factura del mes en que se recibieron las donaciones 
 TAG XML en donde se encuentra el dato:  
 cbc:IssueDate > 
 ó 
 cbc:IssueDate > 

 Búsqueda que debe hacerse con el dato extraído: 
 El mes de la factura, debe corresponder al dato que se presenta en el parámetro del listado de anuncios: Mes recepción (NO ESTABA EN EL INFORME QUE SIRVE COMO BASE) label: class=" lbl_mes_recepcion " La información se toma de: eatc_dona_headers .eatc-receipt_datetime (trayendo el mes) . 

 Label validación exitosa: 
 class="lbl_fecha_factura_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro eatc_datetime   para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 

 Label validación no exitosa: 
 class="lbl_fecha_factura_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

 La razón social de a quién se le expide la factura corresponde la razón social de Ábaco 
 TAG XML en donde se encuentra el dato:  
 cac:ReceiverParty > cbc:RegistrationName > 
 ó 
 cac:accountingcustomerparty > cbc:registrationname > 

 Comparación que debe hacerse con el dato extraído: 
 Debe ser igual a " ASOCIACIÓN DE BANCOS DE ALIMENTOS DE COLOMBIA " (la validación debe ser case insensitive y sin validación de caracteres acentuados, es decir que si se presenta todo mayúsculas, todo minúsculas o tipo título y con o sin tildes la validación puede pasar) 

 Label validación exitosa: 
 class="lbl_nombre_destinatario_factura_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos. 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro eatc_donee_fiscal_name   para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 

 Label validación no exitosa: 
 class="lbl_nombre_destinatario_factura_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

 El NIT de a quién se le expide la factura corresponde la NIT de Ábaco 
 TAG XML en donde se encuentra el dato:  
 cac:ReceiverParty > cbc:CompanyID > 
 ó 
 cac:accountingcustomerparty > cbc:companyid > 

 Comparación que debe hacerse con el dato extraído: 
 Debe ser igual a " 900326456 " 

 Label validación exitosa: 
 class="lbl_id_destinatario_factura_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro eatc_donee_code   para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 

 Label validación no exitosa: 
 class="lbl_id_destinatario_factura_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

 La razón social de quien expide la factura corresponde al eatc_donor_fiscal_name registrado en las donaciones 
 TAG XML en donde se encuentra el dato:  
 cbc:RegistrationName > 
 ó 
 cbc:registrationname > 

 Búsqueda que debe hacerse con el dato extraído: 
 De los anuncios seleccionados en el listado (que deben corresponder a un NIT en particular), el sistema debe comparar si el dato extraído del XML corresponde al dato contenido en eatc_dona_headers .eatc_donor_fiscal_name (que dado el selector de NIT debe ser igual para todos los anuncios seleccionados). 

 Label validación exitosa: 
 class=" lbl_nombre_emisor_factura_ok " 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro eatc_donor_fiscal_name   para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 

 Label validación no exitosa: 
 class=" lbl_nombre_emisor_factura_no_ok " 

 Cuando la validación no es exitosa se hace: 
 Debe salir un modal con: 
 Título : class=" lbl_nombre_emisor_factura_no_ok " 
 Descripción abajo del título class=" lbl_nombre_emisor_factura_no_ok_desc ": (primera versión en español): Tendrás las siguientes opciones para corregirlo: 
 Opción 1 (seleccionada por defecto): class=" lbl_corregir_factura " : si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario para subir una nueva factura se debe colocar el siguiente label: lbl_corregir_nombre_donante ((primera versión en español): Recuerda que debes expedir una factura cuyo emisor tenga el siguiente nombre (RegistrationName): ) seguido del dato que se obtiene de eatc_dona_headers .eatc_donor_fiscal_name 
 Opción 2 : class=" lbl_corregir_datos_donaciones :  al seleccionar esta opción debe aparecer un modal con la siguiente información: 
 Introducción :  class=" lbl_corregir_datos_donaciones_intro ": (primera versión en español): Al seleccionar esta opción el sistema tomará el dato contenido en la factura electrónica como el nombre del donante: 
 Nombre del donante en la factura : después del label anterior se debe mostrar de manera vistosa el dato contenido en el TAG XML correspondiente . 
 Conclusión : class=" lbl_corregir_datos_donaciones_conclu ": (primera versión en español): y  lo cambiará en los datos de donaciones e información maestra del donante en la plataforma, lo cual lo variará para las donaciones seleccionadas y para futuras donaciones.  Por favor verifica muy bien la información de la factura antes de realizar este cambio.  ¿Estás seguro de realizar esta actualización de datos? 
 Opción No (seleccionada por defecto): class=" lbl_no " : si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario se debe colocar el siguiente label: lbl_corregir_nombre_donante seguido del dato que se obtiene de eatc_dona_headers .eatc_donor_fiscal_name 
 Opción Si : class=" lbl_si " : ( Se debe considerar la construcción de un servicio para las siguientes actualizaciones, que debe guardar un log de cuando se realice un cambio, con fecha y hora de realización, usuario de bo que lo realiza, datos originales (por si hay que reversar el cambio) y factura electrónica a partir de la cual se realizó el cambio) el sistema debe corregir los datos contenidos en eatc_dona_headers .eatc_donor_fiscal_name de las donaciones seleccionadas. 
 Si la cuenta no tiene múltiples donors ( eatc_cua. multiple_donors = no ), se debe proceder a realizar el cambio del dato eatc_fiscal_name en la tabla de clientes. ( https://datagov.eatcloud.info/api/eatcloud/eatc_customers?_id=_* ) previa consulta de la relación de la cuenta particular con el cliente ( https://datagov.eatcloud.info/api/eatcloud/eatc_customers_cua?_id=_* ).  Se debe tener en cuenta que esta información está encriptada y se debe volver a guardar encriptada. 
 Si la cuenta tiene múltiples donors ( eatc_cua. multiple_donors = si ), no se actualiza ningún dato adicional. 

 El NIT de quien emite la factura corresponde al eatc_donor_code registrado en las donaciones 
 TAG XML en donde se encuentra el dato:  
 cac:SenderParty > cbc:CompanyID > 
 ó 
 cac:accountingsupplierparty > cbc:companyid > 

 Búsqueda que debe hacerse con el dato extraído: 
 De los anuncios seleccionados en el listado (que deben corresponder a un NIT en particular), el sistema debe comparar si el dato extraído del XML corresponde al dato contenido en eatc_dona_headers .eatc-donor_code (que dado el selector de NIT debe ser igual para todos los anuncios seleccionados). Esta comparación no debe incorporar código de verificación, ni ningún sufijo.  Si un dato viene con un sufijo y otro no, pero el número previo es igual, la validación debe darse por exitosa. 

 Label validación exitosa: 
 class="lbl_id_emisor_factura_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro eatc_donor_code   para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 

 Label validación no exitosa: 
 class="lbl_id_emisor_factura_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

 Debe salir un modal con: 
 Título : class=" lbl_id_emisor_factura_no_ok " 
 Descripción abajo del título class=" lbl_id_emisor_factura_no_ok_desc ": (primera versión en español): Tendrás las siguientes opciones para corregirla: 
 Opción 1 (seleccionada por defecto): class=" lbl_corregir_factura " : si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura .  Antes del formulario para la subida de una nueva factura se debe colocar el siguiente label: lbl_corregir_id_donante ((primera versión en español): Recuerda que debes expedir una factura cuyo emisor tenga el siguiente NIT (CompanyID): ) seguido del dato que se obtiene de eatc_dona_headers .eatc-donor_code 
 Opción 2 : class=" lbl_corregir_datos_donaciones :  al seleccionar esta opción debe aparecer un modal con la siguiente información: 
 Introducción :  class=" lbl_corregir_id_datos_donaciones_intro ": (primera versión en español): Al seleccionar esta opción el sistema tomará el dato contenido en la factura electrónica como el NIT del donante: 
 NIT del donante en la factura : después del label anterior se debe mostrar de manera vistosa el dato contenido en el TAG XML correspondiente . 
 Conclusión : class=" lbl_corregir_datos_donaciones_conclu ": (primera versión en español): y  lo cambiará en los datos de donaciones e información maestra del donante en la plataforma, lo cual lo variará para las donaciones seleccionadas y para futuras donaciones.  Por favor verifica muy bien la información de la factura antes de realizar este cambio.  ¿Estás seguro de realizar esta actualización de datos? 
 Opción No (seleccionada por defecto): class=" lbl_no " : si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario se debe colocar el siguiente label: lbl_corregir_id_donante ((primera versión en español): Recuerda que debes expedir una factura cuyo emisor tenga el siguiente NIT (CompanyID): )  seguido del dato que se obtiene de eatc_dona_headers .eatc-donor_code 
 Opción Si : class=" lbl_si " : ( Se debe considerar la construcción de un servicio para las siguientes actualizaciones, que debe guardar un log de cuando se realice un cambio, con fecha y hora de realización, usuario de bo que lo realiza, datos originales (por si hay que reversar el cambio) y factura electrónica a partir de la cual se realizó el cambio) el sistema debe corregir los datos contenidos en eatc_dona_headers .eatc-donor_codee de las donaciones seleccionadas. 
 Si la cuenta no tiene múltiples donors ( eatc_cua. multiple_donors = no ), se debe proceder a realizar el cambio del dato eatc_fiscal_id en la tabla de clientes. ( https://datagov.eatcloud.info/api/eatcloud/eatc_customers?_id=_* ) previa consulta de la relación de la cuenta particular con el cliente ( https://datagov.eatcloud.info/api/eatcloud/eatc_customers_cua?_id=_* ).  Se debe tener en cuenta que esta información está encriptada y se debe volver a guardar encriptada. 
 Si la cuenta tiene múltiples donors ( eatc_cua. multiple_donors = si ), no se actualiza ningún dato adicional. 

 Número de la factura no puede estar repetido 
 TAG XML en donde se encuentra el dato:  
 cbc:id> 
 ó 
 cbc:id> 

 Búsqueda que debe hacerse con el dato extraído: 
 Se debe realizar la siguiente búsqueda (con los datos, de la validación de NIT anterior): 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_certification_supports_headers? eatc_donor_code={{ eatc_donor_code_extraido_de_la_factura }}&eatc_certification_support_code={{ numero_de_factura_extraido_de_la_factura }} 

 Si la anterior consulta NO trae un resultado válido, entonces la validación se da como exitosa. 

 Label validación exitosa: 
 class="lbl_id_factura_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa se hace: 
 Se guarda el dato obtenido del XML en el parámetro eatc_certification_support_code   para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte. 

 Label validación no exitosa: 
 class="lbl_id_factura_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

 ***NUEVO: información de la factura electrónica que se guarda para el registro: URL de descarga: url_descarga_fe *** 
 El sistema debe tomar la información de la URL que comienza por " https://catalogo-vpfe.dian.gov.co/document/ShowDocumentToPublic/ " y que se encuentra en el tag: "stamp": {"barCodeContent":} y guardarlo en la variable url_descarga_fe 

 Registro de datos de cabecera de soporte (una vez se han validado los datos del encabezado de la factura) 

 Con los siguientes parámetros, que se obtienen la factura electrónica validada exitosamente: 
 parametros_creacion_eatc_certification_supports_headers 
 eatc_certification_support_code={{ }} 
 eatc_suppport_datetime={{ }} => falta por crear el campo 
 eatc_datetime={{Fecha y hora de generación del soporte (datetimestamp) en formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date={{Fecha de generación del soporte (datestamp) en formato AAAA-MM-DD }} 
 eatc_month={{Mes del soporte (enero,febrero,…,diciembre)}} 
 eatc_year={{Año del soporte (en formato AAAA )}} 
 eatc_dona_certification_support= factura_electronica_colombia (constante) 
 eatc_donor_code={{ }} 
 eatc_donor_fiscal_name={{ }} 
 eatc_value={{ }} 
 eatc_cua={{_DOM. cua_user }} 
 **NUEVO : eatc_support_file= url_descarga_fe (según lo estipulado en la documentación respectiva ) ** 
 eatc_donee_fiscal_name= eatc_donee_fiscal_name (Debe ser igual a " ASOCIACIÓN DE BANCOS DE ALIMENTOS DE COLOMBIA ") 
 eatc_donee_code= eatc_donee_code (Debe ser igual a " 900326456 ") 
 eatc_suppport_w_complete_validation= n (constante, dado que hasta este punto se ha validado el encabezado, pero no los detalles de la factura) => falta por crear el campo 

 El sistema hace el llamado al respectivo crd: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_headers &_operacion=insert&{{ parametros_creacion_eatc_certification_supports_headers }} => Tener en cuenta en creación de cuentas maestras 

 VALIDACIONES PARA LAS LÍNEAS DE LA FACTURA ( ) 
 En términos generales se debe realizar por cada línea un validación de su código y del nombre del producto en primera instancia. Si alguno de estos datos es incorrecto (y otro está correcto) debe dársele al usuario la oportunidad de actualizar el dato incorrecto en los registros de EatCloud para hacerlo compatible a la factura. Si ambos datos son incorrectos se debe parar la validación (con un mensaje), y volver al  formulario para subida de factura. Si uno de los dos datos  (código o descripción) es correcto (y se procede con la corrección del dato en los Registros de EatCloud, se debe proceder a validar la cantidad de producto en cada línea.  Si la cantidad de producto en el XML es inferior a la cantidad de producto consolidado ( unidades aprovechadas ) de los anuncios seleccionados, entonces la validación pasará (será exitosa) y se llevará la cantidad informada en la factura al registro de unidades de producto a certificar ( eatc_certification_products_details ). Si la cantidad en la factura es superior, a la cantidad consolidada para el ITEM, se debe solicitar la corrección de la factura con la cantidad que se tiene registrada en EatCloud. Si una línea de la factura no cumple con las validaciones, entonces la factura debe ser rechazada y se solicitará la subida de una nueva factura con los datos corregidos, o que el usuario realice una nueva selección de donaciones que estén acorde con la factura. 

 El código de los ítems de la factura debe corresponder al código de los items consolidados 
 TAG XML en donde se encuentra el dato:  

 ó 

 NOTA : en los ejemplos de facturas consultados, estos datos son iguales.  En caso que en una factura en particular sean diferentes, se deberá realizar la consulta con ambos y si uno de los dos pasa la verificación se entiende que la verificación es exitosa. 

 Búsqueda que debe hacerse con el dato extraído: 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML corresponde a un Código de producto ( eatc_dona .eatc-odd_id) que esté contenido en los anuncios seleccionados . 

 Label validación exitosa: 
 class="lbl_id_items_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
 Cuando la validación es exitosa se hace: 
 Se guarda el dato en el parámetro " eatc_product_code " para posteriormente, cuando las demás validaciones se completen, se lleve al registro de productos en el soporte ( eatc_certification_products_details ). 

 Label validación no exitosa: 
 class="lbl_id_item_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Se debe pasar a validar el nombre del item de la factura (validación siguiente).  Si dicha validación es exitosa (en conjunto con la validación de cantidad), se le debe preguntar al usuario ( class=" lbl_cambiar_codigo_item " ): ¿Deseas reemplazar el código registrado en las donaciones por el código que trae la factura que acabas de subir? y si el usuario define que si ( class=" lbl_si " ), entonces el sistema debe proceder a actualizar el eatc_dona .eatc-odd_id en las donaciones seleccionadas .  Si el usuario define que no ( class=" lbl_no " ) el sistema debe desplegar el siguiente mensaje: ( class=" lbl_id_item_no_ok_desc " ): Los códigos de los productos registrados en la factura deben corresponder con los códigos de los productos reportados en el anuncio, por favor corrige la factura y procede a subirla de nuevo ,  y se vuelve a mostrar el formulario de subida de factura . 

 La descripción de los ítems de la factura debe corresponder a la descripción de los ítems consolidados 
 TAG XML en donde se encuentra el dato:  
 cbc:description > 

 Búsqueda que debe hacerse con el dato extraído: 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML corresponde al nombre del producto ( eatc_dona .eatc-odd_name) que está contenido en los anuncios seleccionados . 

 Label validación exitosa: 
 class="lbl_nombre_item_ok" 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 

 Cuando la validación es exitosa (junto con la validación anterior) se hace: 
 Se guarda el dato en el parámetro " eatc_product_name " para posteriormente, cuando la tercera validación del ítem se complete ( validación de cantidades ), se lleve al registro de productos en el soporte ( eatc_certification_products_details ) 

 Cuando la validación es exitosa (y la anterior no lo fue) se hace: 
 Se procede como se indicó anteriormente . 

 Label validación no exitosa: 
 class="lbl_nombre_item_no_ok" 

 Cuando la validación no es exitosa (y la anterior si lo fue y la validación de cantidades también ) se hace: 
 Se le debe preguntar al usuario ( class=" lbl_cambiar_nombre_item " ): ¿Deseas reemplazar el nombre registrado en las donaciones por el nombre del producto que trae la factura que acabas de subir? y si el usuario define que si ( class=" lbl_si " ), entonces el sistema debe proceder a actualizar el eatc_dona .eatc-odd_name en las donaciones seleccionadas .  Si el usuario define que no ( class=" lbl_no " ) el sistema debe desplegar el siguiente mensaje: ( class=" lbl_nombre_item_no_ok_desc " ): El nombre del ítem en la factura debe corresponder al nombre del ítem registrado en las donaciones. Por favor corrige la factura y súbela de nuevo ,  y se vuelve a mostrar el formulario de subida de factura . 

 Cuando la validación no es exitosa (y la anterior tampoco lo fue) se hace: 
 Si la validación de código no es exitosa tampoco, entonces se para la validación, se muestra el label " lbl_nombre_item_no_ok_desc " y se vuelve a mostrar el formulario de subida de factura . 

 Las cantidades de los ítems de la factura deben ser menores o iguales a las cantidades de los ítems consolidados 
 TAG XML en donde se encuentra el dato:  

 Búsqueda que debe hacerse con el dato extraído: 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML corresponde a una cantidad igual o menor a la cantidad de Unidades aprovechadas ( eatc_dona .eatc-odd_quantity) de los anuncios seleccionados . 

 Label validación exitosa: 
 class="lbl_cantidad_item_ok" 

 Cuando la validación es exitosa se hace (junto con las dos anteriores o al menos una de las dos anteriores): 
 Se guarda el dato en el parámetro " eatc_product_quantity " para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ) 

 Label validación no exitosa: 
 class="lbl_cantidad_item_no_ok" 

 Cuando la validación no es exitosa se hace: 
 Cuando la cantidad de la factura es superior a la informada en los anuncios seleccionados, se para la validación, y se muestra el label " lbl_cantidad_item_no_ok_desc ": La cantidad del ítem informada en la factura no corresponde a la cantidad efectivamente verificada por el beneficiario, informada en las donaciones recibidas. Por favor cambie la selección de donaciones o corrija el dato en la factura y vuelva a subirla   y debajo debe mostrar dos opciones (botones): class=" lbl_cambiar_seleccion_donaciones " (que devuelve a la lista de anuncios para seleccionar ) y class=" lbl_corregir_factura " (que vuelve a mostrar el formulario de subida de factura ) 

 OTROS DATOS DE LAS LÍNEAS DE LA FACTURA ( ) que se llevan al registro si las anteriores validaciones son exitosas: 
 Lo siguientes datos deben obtenerse de la información de la factura para guardarse posteriormente en los registros correspondientes 

 Valor unitario del ítem antes de IVA 
 TAG XML en donde se encuentra el dato:  

 Se guarda en: 
 Se guarda el dato en el parámetro " eatc_unt_value " para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ) 

 Valor total del ítem antes de IVA 
 TAG XML en donde se encuentra el dato:  
 cbc:lineextensionamount > 
 ó 
 cbc:taxableamount > 

 NOTA : Este segundo tag no está presente en algunas facturas electrónicas 

 Se guarda en: 
 Se guarda el dato en el parámetro " eatc_total_value " para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ). 

 Registro de datos de detalle de productos (una vez se tiene la validación de los detalles de manera exitosa) 
 Tan pronto el sistema determina que los detalles de la factura han sido correctamente validados, con los datos obtenidos de dichos detalles de la factura se obtiene la siguiente información para el registro del cada producto incorporado en la factura: 

 parametros_creacion_eatc_certification_products_details 
 eatc_certification_support_code={{ }}= {{ eatc_certification_supports_headers. eatc_certification_support_code }} 
 eatc_product_code={{ ó }} 
 eatc_product_name={{ eatc_product_name }}={{ }} 
 eatc_product_quantity={{ }} 
 eatc_unt_value={{ eatc_unt_value }}={{ }} 
 eatc_total_value={{ eatc_total_value }}={{ }} 

 Los anteriores datos se extraen tantas veces como líneas de factura ( ) existan. 

 El sistema realiza el siguiente llamado para registrar los datos de los productos de la factura: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_products_details &_operacion= insert &{{ parametros_creacion_eatc_certification_products_details }} 

 Actualización de dato de encabezado de soporte (una vez se tiene la validación de los detalles de manera exitosa) 
 Tan pronto el sistema determina que los detalles de la factura han sido correctamente validados, el sistema deberá realizar la siguiente actualización para informar que la validación del soporte está completa, realizando el llamado al respectivo al crd: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_headers &_operacion= update &eatc_suppport_w_complete_validation= y &WHEREeatc_certification_support_code={{ eatc_certification_supports_headers. eatc_certification_support_code }} 
   => Tener en cuenta en creación de cuentas maestras / falta por crear el campo 

 Registro de datos de detalle de soporte (listado de anuncios de donación soportados: una vez se tiene la validación de los detalles de manera exitosa) 
 T an pronto el sistema determina que los detalles de la factura han sido correctamente validados, con los datos de cada anuncio que fuere previamente seleccionado   para ser soportado por la factura_electronica_colombia y a partir de ello, para realizar validar los datos de factura electrónica, se realiza el siguiente registro de datos: 
 parametros_creación_detalle_soportes 
 eatc_dona_header_code: 
 Código del anuncio de donación soportado ( eatc_dona_headers. eatc-code ). 

 eatc_publication_datetime: 
 Fecha y hora de publicación del anuncio ( eatc_dona_headers. eatc-publication_datetime )", 

 eatc_value: 
 Valor del anuncio certificable antes de IVA (se toma de: eatc_dona_headers. eatc-total_cost ). 

 eatc_receipt_datetime: 
 Fecha de recepción del anuncio ( eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM-DD HH:MM:SS 

 eatc_receipt_year_month: 
 Año y mes de recepción del anuncio (tomado de eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM 

 eatc_doc: 
 Documento soporte de la donación ( eatc_dona_headers. eatc-doc ). 

 eatc_donation_manager: 
 Gestor de donaciones al que se le entregó la donación ( eatc_dona_headers .eatc-donation_manager_code ). 

 eatc_doma_affiliated_organization: 
 ***NUEVO: se deja vacío *** 
 Dado que en un proceso de servidor que se generará al crear el certificado, se incorporará esta información. 

 DEPRECADO: 
 Nombre de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta:{{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }}Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca ese dato en el registro.  Si viene un NIT, se repite la consulta anteriormente realizada:{{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{ organizacion_vinculada }}Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.  Si después de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 eatc_doma_affiliated_organization_id: 

 ***NUEVO: se deja vacío *** 

 Dado que en un proceso de servidor que se generará al crear el certificado, se incorporará esta información. 

 DEPRECADO: 
 Identificador único de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta:{{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }}Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca el dato que llega en el campo identificador_unico_registro de la siguiente consulta:{{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador= abaco Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.  Si después de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 eatc_certification_support_code: 
 Código del soporte para la certificación que se toma del código respectivo que se genera con el llamado al servicio: 
 eatc_certification_support_code={{ eatc_certification_support_code }} 

 Que también corresponde al dato guardado en el proceso anterior en: 
  {{ eatc_certification_supports_headers. eatc_certification_support_code }} 

 eatc_dona_certification_support: 
 Tipo de soporte de certificación expedido (en este caso siempre será factura_electronica_colombia ). 

 eatc_donor_code: 
 Documento de identidad del donante ( eatc_certification_supports_headers . eatc_donor_code ). 
 eatc_donor_fiscal_name: 
 Razón social del donante ( eatc_certification_supports_headers . eatc_donor_fiscal_name ). 

 Creación registro de detalle del soporte 
 El sistema debe generar el registro utilizando el CRD correspondiente 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_details &_operacion= insert & {{parametros_creación_detalle_soporte}} 

 DEPRECADO ( dado que inicialmente los registros se realizarán directamente en el proceso de validación de factura electrónica y no mediante un servicio ) 
 Parámetros que se obtienen de la factura electrónica y que se deben enviar para su creación en el sistema 
 Este es el resumen de los parámetros que se envían (con indicación del último tag XML en donde se encuentra la información para efectos indicativos), a partir de los datos que se obtienen del XML de la factura Electrónica 
 parametros_creacion_eatc_certification_supports_headers 
 eatc_cua={{_DOM.cua_user}} 
 eatc_datetime={{ }} 
 eatc_donee_fiscal_name={{ }} 
 eatc_donee_code={{ }} 
 eatc_donor_fiscal_name={{ }} 
 eatc_donor_code={{ }} 
 eatc_certification_support_code={{ }} 
 **NUEVO: eatc_support_file= url_descarga_fe (según lo estipulado en la documentación respectiva ) ** 

 Los anteriores datos se extraen una vez por factura electrónica 
 parametros_creacion_eatc_certification_products_details 
 eatc_certification_support_code={{ }} 
 eatc_product_code={{ ó }} 
 eatc_product_name={{ }} 
 eatc_product_quantity={{ }} 
 eatc_unt_value={{ }} 
 eatc_total_value={{ }} 

 Los anteriores datos se extraen tantas veces como líneas de factura ( ) existan. 

 NOTA IMPORTANTE: El desarrollador debe definir si envía los anteriores parámetros en el llamado al servicio que crea la factura (comprimiéndolos de algún modo) o si procede a implementar en el servidor la obtención de estos parámetros a partir del XML (lo cual sería algo redundante con la implementación anterior) o si genera persistencias provisionales para guardarlos ( eatc_provisional_certification_supports_headers , eatc_provisional_certification_products_details ) que podrán ser consultada con el dato eatc_certification_support_code (que se manda en el llamado al servicio que crea la factura ) para realizar las escrituras en las tablas definitivas eatc_certification_supports_headers y  eatc_certification_products_details 

 Método de soporte: factura_electronica_colombia: llamado a servicio ante una validación totalmente exitosa 
 Si todas las validaciones practicadas a la factura fueron exitosas (o las correcciones de datos sugeridas fueron implementadas) entonces se pasa a realizar el siguiente llamado al servicio, con el ánimo de crear los registros de rigor a partir del documento soporte aportado 
 {{ URL_entorno_donante }}/ crea_sprt /{{_DOM. cua_master }}/ eatc_dona_certification_support= factura_electronica_colombia& eatc_certification_support_code= {{eatc_certification_support_code}}& eatc_support_file ={{localizador_recurso / url_descarga_fe }}& eatc_dona_headers ={{array_codigos_eatc_dona_headers}}& ... 

 ... Si el desarrollador decide mandar los parámetros ( parametros_creacion_eatc_certification_supports_headers / parametros_creacion_eatc_certification_products_details)  para la creación de los registros definitivos eatc_certification_supports_headers y eatc_certification_products_details se deberá documentar su inclusión en el llamado al servicio respectivo 

 El servicio deberá llamarse tantas veces sea necesario, hasta obtener una respuesta exitosa del mismo . 

 CONSULTA DE ANUNCIOS ENTREGADOS NO CERTIFICABLES 
 Botón del menú lateral 
 El sistema deberá presentar un botón con el siguiente label (en el menú lateral) 
 label: class="lbl_donaciones_no_certificables"  

 Y que pueda mostrar la siguiente descripción (puede ser como un tooltip): 
 label: class="lbl_donaciones_no_certificables_tooltip"  

 El sistema presentará un botón, a partir del cual se generará un listado de los anuncios cuyo estado es "delivered" y que están pendientes de verificación.  La funcionalidad también presentará la posibilidad de señalar los anuncios con problemas y enviar un mensaje a soporte técnico y a las fundaciones para solicitar que sean verificados. 

 El botón deberá persentar un globo de advertencia si la siguiente consulta trae datos (ideal que en el mismo aparezca el valor del cont respectivo) 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donor={{_DOM. cua_user }}&eatc-state=delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00&_compress 

 Funcionalidad de visualización de anuncios pendientes por gestión 
 Al presionar el botón de menú, se debe entrar a una funcionalidad, cuyo título es: 
 label: class="lbl_titulo_donaciones_no_certificables"  

 Y abajo de dicho título colocar la siguiente descripción: 
 label: class="lbl_donaciones_no_certificables_desc"  

 Consulta para traer las donaciones pendientes de gestión 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donor={{_DOM. cua_user }}&eatc-state=delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00&_compress 

 A continuación se presenta una lista que contiene la siguiente información de los anuncios que trae la anterior consulta, ordenando primero aquellos cuya fecha y hora de publicación ( eatc_dona_headers .eatc-publication_datetime ) sea la más antigua: 

 Código del anuncio 
label: class=" lbl_codigo_anuncio " 
 La información se toma de: eatc_dona_headers .eatc-code 

 Fecha y hora 
label: class=" lbl_hora_publicacion " 
 La información se toma de: eatc_dona_headers .eatc-publication_datetime 

 Estado 
label: class=" lbl_estado " 
 La información se toma de: eatc_dona_headers .eatc-state 

 Código Punto de donación 
label: class=" lbl_codigo_punto_donacion " 
 La información se toma de: eatc_dona .eatc-pod_id 

 Punto de donación 
label: class=" lbl_pod " 
 La información se toma de: eatc_dona_headers .eatc-pod_name 

 Dirección punto de donación (OJO ID) 
label: id=" lbl_direccion_punto_donacion " 
 La información se toma de: eatc_dona_headers .eatc-pod_address 

 Ciudad 
label: class=" lbl_ciudad " 
 La información se toma de: eatc_dona_headers .eatc-city 

 KG Originales 
label: class=" kg_originales " 
 La información se toma de: eatc_dona_headers . eatc-original_weight_kg ) 

 Costo original 
label: class=" kg_costo_original " 
 La información se toma de: eatc_dona_headers . eatc-original_cost 

 Porcentaje IVA 
label: class=" lbl_porcentaje_iva " 
 La información se toma de: eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
label: class=" lbl_valor_iva " 
 La información se toma de: eatc_dona .eatc-total_VAT 

 Beneficiario 
label: class=" lbl_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Beneficiario dirección 
label: class=" lbl_direccion_beneficiario " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_adress 

 Beneficiario teléfono 
label: class=" lbl_telefono " 
 La información se toma de: eatc_dona_headers .eatc-donation_manager_phone 

 Hora de adjudicación 
label: class=" lbl_hora_adjudicacion " 
 La información se toma de: eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega real: llegada 
label: class=" lbl_hora_entrega_real_llegada " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real: salida 
label: class=" lbl_hora_entrega_real_salida " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkout_datetime 

 Fecha recepción 
label: class=" lbl_hora_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime (debe estar en ceros, dado que es una condición que se tiene en cuenta en la consulta para traer los datos) 

 Documento soporte 
label: class=" lbl_documento_soporte " 
 La información se toma de: eatc_dona_headers .eatc-doc 

 Alerta 
label: class=" lbl_alerta " 
 La información se toma de: eatc_dona_headers .eatc-warning 

 Botón: Enviar solicitudes de gestión: 
 En la parte superior del listado debe colocarse un botón con la siguiente leyenda 
 label: class=" lbl_enviar_mensajes_solicitando_gestion "  

 Al presionar el botón, se deberá desplegar un modal o una página en donde aparezca lo siguiente: 

 Título 
 label: class=" lbl_titulo_enviar_mensajes_solicitando_gestion "  

 El título del modal o de la página será 

 " Enviar mensajes solicitando de gestión " 

 Descripción 
 label: class=" lbl_enviar_mensajes_solicitando_gestion_desc "  

 Abajo del título se colocará la siguiente leyenda. 

 " Con esta funcionalidad, podrás generar mensajes automáticos a todas las organizaciones que tienen gestiones pendientes para poder otorgarles a las donaciones que se les han entregado el estatus de "recibidas", necesario para poder ser certificables." 

 Remitente 
 label: class="lbl_remitente"  

 A manera de un mensaje, se colocará: " Remitente: {{nombre_donante}} " 

 El nombre del donante se toma de:   

 Con el dato _DOM. cua_user se realiza la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue={{_DOM. cua_user }} 

 Con la respuesta obtenida se toma el _id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &fieldname= eatc_cua,eatc_customer_fiscal_id &&filterfield_1=_id&filtervalue_1={{ eatc_customers_cua._id }} 

 Con esto se obtiene el valor desencriptado de eatc_customers_cua. eatc_customer_fiscal_id   y con él se realiza la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &fieldname= eatc_fiscal_name &&filterfield_1= eatc_fiscal_id &filtervalue_1={{ eatc_customers_cua. eatc_customer_fiscal_id }} 

 El valor que se obtiene de esta última consulta será el remitente se guarda en la variable {{ remitente }} 

 Mensaje por defecto 
 En un campo de captura de texto, debajo del nombre del remitente, de manera predeterminada (a manera de una especie de "place holder" o valor por defecto), debe aparecer el siguiente mensaje, que el usuario podrá editar a su antojo: 
 label: class="lbl_mensaje_solicitando_gestion"  

 " Les solicitamos amablemente la gestión de los anuncios pendientes (por programar, recoger o verificar) que hemos entregado a su organización. Dicha gestión es fundamental para la emisión del respectivo certificado y por lo tanto importante para nosotros.  De antemano muchas gracias por la atención recibida " 

 El mensaje (por defecto o editado por el donante) se guarda en una variable {{ mensaje_solicitud_gestion }} 

 eatc_message_type 
 El tipo de mensaje en este caso será una constante y la misma es: mis_donaciones 

 display_conditions 
 La condición de despliegue del mensaje será una constante y la misma es: hasta_gestion_anuncios , y la misma quiere decir que el mensaje se mostrará hasta que se culminen de gestionar las donaciones que promovieron el mensaje.  Para evaluar el cumplimiento de dicha condición se utilizan los dos siguientes parámetros (nuevos): display_query y display_query_response 

 Botón: "Enviar": 
 label: class=" lbl_enviar "  

 Al presionar el botón, se deberá  hacer un distinct sobre el dato eatc_dona_headers . eatc-donation_manager_code de la consulta original y para cada gestor de donaciones (beneficiario) realizar la siguiente escritura de datos, tomando el timestamp con la fecha y hora en la cual se oprime el botón, el dato {{_DOM. cua_user }} y las siguientes condiciones de despliegue del mensaje : 

 display_query 
 En este caso se envía la búsqueda que está dando como resultado el envío del mensaje (reemplazando los valores con los datos respectivos).  
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&eatc-state=delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00 

 Nota para el desarrollador: se deberá evaluar si se envía este query o a partir del mismo se toman los datos que se obtienen del campo eatc_dona_headers. eatc-code y con el {{array_de_codigos}} obtenido se envía en el campo la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&eatc-state=delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00 &eatc-code= {{array_de_codigos}} 

 La url que se obtiene (con los valores respectivos) se guarda en la variable {{ query_url }} 

 display_query_response 
 Dado que el mensaje se debe mostrar hasta qué no se gestionen las donaciones del donante remitente, el mensaje se deberá mostrar hasta que la anterior consulta traiga resultados, es decir que en este caso, se registra en el campo la constante: valid 

 {{ URL_beneficiarios }}/crd/{{_DOM. cua_master }}/?_tabla= eatc_doma_messages &_operacion= insert &date={{ timestamp }}&eatc_message_type= mis_donaciones &title= Mensaje %20 importante %20 de %20{{ remitente }} &message={{ mensaje_solicitud_gestion }}&eatc_doma_code={{eatc_dona_headers. eatc-donation_manager_code }}&display_conditions= hasta_gestion_anuncios &display_time_sec=fix&display_query= {{ query_url }} &display_query_response= valid 

 El mensaje ha sido enviado a: 
 label: class="lbl_mensaje_enviado_a"  

 Una vez se realiza las escrituras de los mensajes, a manera de confirmación, el sistema muestra un mensaje: 

 Mensaje enviado a: {{listado_nombres_beneficiarios}} 

 A continuación se presenta un listado que resulta del sect_distinct realizado sobre el dato: eatc_dona_headers .eatc-donation_manager_name de la consulta original . 

 CONSULTA DE CERTIFICADOS DE DONACIÓN 
 ID funcionalidad: consulta_certificados_donacion (falta crearse) 

 Label botón de menú izquierdo : class=" lbl_menu_consulta_certificados " 

 Label título de la funcionalidad: class=" lbl_consulta_certificados " 

 Label descripción de la funcionalidad: class=" lbl_consulta_certificados_desc " 

 Listado de de certificados pendientes de aprobación 
 A este listado, que contendrá una lista de los certificados que responden a esta consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_dona_certifications ?eatc_cua ={{ _DOM .cua_user}} 

 La lista deberá contener dos filtros 

 Filtro por fecha (label:  class="lbl_filtro_fecha) 
 Aplica sobre los valores contenidos en eatc_dona_certifications . eatc_datetime . Debe tener un selector de fecha inicial y fecha final, cuyos valores por defecto deben ser: 
 Fecha inicial (label: id=" lbl_fecha_inicial " ) : tres meses antes de la fecha actual 
 Fecha final (label: id=" lbl_fecha_final " ) : fecha actual 

 Filtro por estado de aprobación (label:  class="lbl_filtro_aprobacion) 
 Aplica sobre los valores contenidos en eatc_dona_certifications . eatc_certification_datetime . Los selectores para el filtro serán : 
 Pendientes de aprobación (label: class=" lbl_pendientes_aprobacion " ) : al presionarlo, traerá los certificados que no contengan una fecha válida en  eatc_dona_certifications . eatc_certification_datetime (para el periodo de tiempo seleccionado en el filtro por fecha) 
 Aprobados (label: class=" lbl_aprobados " ) : al presionarlo, traerá los certificados que tienen una fecha válida en  eatc_dona_certifications . eatc_certification_datetime (para el periodo de tiempo seleccionado en el fltro por fecha) 
 Todos (label: class=" lbl_todos " ) : Será el valor por defecto y trae todos los certificados, mostrando primero los pendientes de aprobación con fecha más antigua. 

 A partir de la selección que el usuario haga en los filtros, se deberá mostrar un listado de certificados que contiene las siguientes columnas: 

 Código:  
 Label : class=" lbl_codigo " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_code 

 Fecha y hora:  
 Label : class=" lbl_fecha_hora " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_datetime   

 Identificación tributaria donante:  
 Label : class=" lbl_id_donante " 
 Muestra la información contenida en eatc_dona_certifications . eatc_donor_code 

 Razón Social:  
 Label : class=" lbl_razon_social " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_donor_fiscal_name 

 Valor total:  
 Label : class=" lbl_valor_total " ) 
 Muestra la información contenida en eatc_dona_certifications . eatc_value 

 Documento(s) soporte: 
 Label : class=" lbl_docs_soporte " 
 Con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certifications_supports ?eatc_certification_code={{eatc_dona_certifications . eatc_code }} se deben obtener los códigos de los soportes ( eatc_certifications_supports .eatc_certification_support_code ), y con ellos se realiza una lista de soportes (con sus códigos) y con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_certification_support_code ={{eatc_certifications_supports .eatc_certification_support_code }} , para traer la información que permite descargar el soporte ( eatc_certification_support_code.eatc_support_file ) se deben activar vínculos en cada uno de esos códigos para descargar el respectivo soporte. 

 Descargar archivo 
 Label : class=" lbl_descargar_archivo " 
 Como no existe un registro válido en eatc_dona_certifications . eatc_certification_datetime se debe presentar el botón " Descargar borrador " ( class=" lbl_descargar_borrador " ) (en el listado de consultar certificados podrá existir uno con una fecha válida en eatc_dona_certifications . eatc_certification_datetime s e deberá presentar entonces el boton "Descargar soporte" ( class=" lbl_descargar_certificado " ) El botón servirá para descargar el borrador del certificado a partir de la información consignada en: eatc_dona_certifications . eatc_certificate_file 

 Fecha y hora de aprobación: 
 Label : class=" lbl_fecha_hora_aprobacion " ). 
 Muestra la información contenida en eatc_dona_certifications . eatc_certification_datetime . Cuando no existe una fecha y hora válida registrada, en vez de mostrarla, se deberá mostrar lo siguiente: 
 Uno o varios tags con vínculo mostrando las aprobaciones: indicando que el certificado ha sido aprobado por una o diferentes áreas del ente certificador; 

 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Si la consulta no trae información deberá mostrar el tag con la etiqueta class=" lbl_pendiente_aprobaciones " 

 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente: 

 Con los datos obtenidos en el parámetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parámetro eatc_certification_approval_flow. eatc_approval_by_label . Cada etiqueta debe tener un vínculo que muestre la siguiente información del registro de aprobación ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} )  
 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la información contenida en el parámetro eatc_certification_approval_registry. eatc_approval_datetime 
 Usuario ( class=" lbl_usuario_solo " ): que muestra la información contenida en el parámetro eatc_certification_approval_registry. eatc_bo_user 
 Un botón para la acción " Aprobar ", según las indicaciones que se entregan en la siguiente funcionalidad. o en su defecto un mensaje "Pendiente de aprobación" ( class=" lbl_pendiente_aprobacion " ) 

 Uno o varios tags con vínculo mostrando las desaprobaciones: indicando que el certificado ha sido desaprobado por una o varias áreas del ente certificador; 

 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Si la consulta no trae información no mostrará nada 

 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente: 

 Con los datos obtenidos en el parámetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parámetro eatc_certification_approval_flow. eatc_disapproval_by_label . Cada etiqueta debe tener un vínculo que muestre la siguiente información del registro de desaprobación ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code = 
{{eatc_dona_certifications . eatc_code }} )  
 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_approval_datetime 
 Usuario ( class=" lbl_usuario_solo " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_bo_user 
 Explicación: ( class=" lbl_explicacion " ): que muestra la información contenida en el parámetro eatc_certification_disapproval_registry. eatc_disapproval_note 
 Un botón para la acción " Aprobar ", según las indicaciones que se entregan en la siguiente funcionalidad. o en su defecto un mensaje "Pendiente de aprobación" ( class=" lbl_pendiente_aprobacion " ) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Datagov_Cuentas 

 MÉTODO DE SOPORTE CARTA COLOMBIA