# creación-de-carta-soporte-crea_spr.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 LLAMADO AL SERVICIO 
 El servicio será invocado de la siguiente manera  
 {{URL_entorno_donante}}/ crea_sprt /{{_DOM. cua_master }}/ eatc_dona_certification_support= carta_colombia 

 Y debe llamarse automáticamente según lo establecido en https://datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ? eatc_dona_certification_support =carta_colombia en el parámetro: eatc_max_generation_day=last (lo cual quiere decir que se debe generar en el último minuto del último día de cada mes. 

 MÉTODO DE SOPORTE: CARTA_COLOMBIA: 
  Cuando en la invocación del servicio en el parámetro eatc_dona_certification_support se recibe el dato carta_colombia ) el sistema debe proceder con la creación de la siguiente manera. 

 Consultas necesarias para generar la carta soporte 

 Consulta sobre las cuentas a las cuales se les debe correr el proceso de manera automática 
 Se debe consultar las cuentas cuyo método de generación de soporte corresponde a " carta_colombia " mediante la siguiente consulta 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_default_certification_support=carta_colombia 

 Consulta sobre las características del método de soporte 
 Con el dato que llega en el parámetro eatc_certification_support , el sistema procede a realizar las siguientes consultas: 

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

 A continuación se detallan los datos que al ser leídos de esta persistencia tienen injerencia en el despliegue de la funcionalidad: 

 eatc_support_generation_method: "automatico" 
 Esto quiere decir que la generación del soporte para el proceso de precertificación la realizará el sistema de manera automática, de acuerdo a como se detallan en otros parámetros que se mencionarán más adelante. Por lo tanto lo que se despliega en la funcionalidad tendrá carácter informativo y no operativo (por lo menos en una primera versión) 

 eatc_support_generation_frecuency: "mensual" 
 Lo anterior quiere decir que el soporte " carta_colombia " se generará con una periodicidad mensual. 

 eatc_max_generation_day: "last" 
 Esto indica que el proceso de generación del soporte " carta_colombia " debe realizarse el último día del mes. 

 eatc_months_back_to_support: "1" 
 Este parámetro indica que los anuncios aptos para certificarse (que principalmente cumplen dos condiciones: tienen estado recibido (received) (Es decir que por ejemplo para ambiente de pruebas responden a esta consulta: https://devdonantes.eatcloud.info/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state=received ) y no se les ha expedido constancia de donación (no poseen un registro de fecha válido en eatc_constancy_datetime o no poseen un registro válido en  eatc_constancy_consecutive )) serán los de un mes atrás.  Este dato, combinado con el siguiente, determina el método de consulta para traer los anuncios que serán soportados por la carta automática. 

 eatc_montly_cut: "corte" 
 Esto quiere decir que el conteo del mes para atrás, se hace a corte mensual, es decir que el sistema debe evaluar el dato que llega en el parámetro eatc_dona_headers. eatc-receipt_datetime   para establecer si el mes en el que se recibió el anuncio corresponde al mes en curso (para la implementación del informe de detalle de anuncios, se utilizó una función que establece el mes del anuncio , y esta se puede utilizar para realizar esta validación), desde el primer día del mes hasta el último. 

 Consulta para establecer si se realiza un solo soporte o varios 
 Se debe establecer de las diferentes cuentas cuyo método de soporte para certificado es " carta_colombia " , cuales de ellas tienen el parámetro multiple_donors =si . Para estas cuentas, se debe hacer un recorrido por los diferentes eatc_dona_headers. eatc-donor_code de los anuncios aptos para ser certificados con el ánimo de desarrollar una carta por eatc_dona_headers. eatc-donor_code según el proceso que se documenta a continuación.  Si la cuenta tiene el parámetro multiple_donors =no entonces se elaborará una sola carta para soportar todos los anuncios aptos del periodo. 

 Solo se soportan donaciones que no han sido previamente soportadas: 
 Es decir, aquellos que cumplen con los parámetros eatc_months_back_to_support , eatc_montly_cut y no se encuentran registrados en la tabla eatc_certification_supports_details : Para determinar lo anterior se buscan los anuncios que cumplen los anteriores criterios, mandando los códigos del encabezado de donación al parámetro eatc_dona_header_code 

   {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_certification_supports_details? eatc_dona_header_code={{ eatc_dona_headers .eatc-code}} 

 Si el anuncio ya está registrado en la tabla de detalle de soportes, entonces no queda dentro de los soportados por la carta automática, y no debe tenerse en cuenta para la generación de los procesos y registros que se detallan a continuación 

 Método de soporte: carta_colombia: generación de carta soporte (proceso automático) 
 El sistema según lo establecido en los parámetros del método de soporte: eatc_support_generation_method (automatico); eatc_support_generation_frecuency (mensual); eatc_max_generation_day (last), generará de manera automática una o varias cartas de soporte (una por NIT: eatc_dona_headers. eatc-donor_code ) el último día del mes (a última hora), y guardará dichas cartas en la persistencia eatc_certification_supports_headers y la relación entre los soportes y los anuncios (aquellos que cumplen con los criterios para ser certificados ) en eatc_certification_supports_details de la siguiente manera: 

 ***NUEVO: no se tomarán en cuenta donaciones cuya cuenta o pod aparezcan en la tabla “eatc_doma_certification” *** 
Se aplicará lo establecido aquí , para no tomar en cuenta estos anuncios para crear la carta soporte. 

{{parametros_creación_encabezado_soporte}} 
 eatc_certification_support_code: 
 Código único generado por el sistema para identificar el soporte que se está creando. El sistema debe validar la unicidad de este código (por ejemplo colocándolo como clave primaria en la base de datos). 

 eatc_datetime: 
 Fecha y hora de generación del soporte en formato AAAA-MM-DD HH:MM:SS (debería corresponder en este caso al último segundo del último día del mes AAAA-MM-DD 23:59:59 ). 

 eatc_date: 
 Fecha de generación del soporte en formato AAAA-MM-DD (corresponde en este caso al último día del mes). 

 eatc_month: 
 Mes de generación del soporte ( enero,febrero,…,diciembre ). 

 eatc_year: 
 Año de generación del soporte (en formato AAAA ). 

 eatc_dona_certification_support: 
 Tipo de soporte de certificación expedido  (en este caso sería siempre: carta_colombia ) 

 eatc_donor_code: 
 El dato que se toma eatc_dona_headers. eatc-donor_code (todos los anuncios que se soportan con una carta deberán tener este dato idéntico). 

 eatc_donor_fiscal_name: 
 El dato que se toma eatc_dona_headers. eatc_donor_fiscal_name (todos los anuncios que se soportan con una carta deberán tener este dato idéntico). 

 eatc_value: 
 Sumatoria de los datos: eatc_dona_headers. eatc-total_cost de las donaciones certificables en el periodo definido. 

 eatc_cua: 
 Cuenta desde la que se generan los soportes.  Corresponde a _DOM. cua_user y también al dato eatc_dona_headers. eatc_donor 

 ***NUEVO : eatc_donee_code *** 
 Se coloca la constante: " 900326456 " 

 ***NUEVO : eatc_donee_fiscal_name *** 
 Se coloca la constante: " ASOCIACIÓN DE BANCOS DE ALIMENTOS DE COLOMBIA " 

 Creación registro de encabezado del soporte  
 El sistema debe generar el registro utilizando el CRD correspondiente 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_supports_headers &_operacion= insert & {{parametros_creación_encabezado_soporte} 

 {{parametros_creación_detalle_soporte}} 
 Con un registro para cada anuncio que es soportado por la carta_colombia , se consigna la siguiente información en la tabla respectiva 

 eatc_certification_support_code: 
 Código del soporte para la certificación (se toma de eatc_certification_supports_headers. eatc_certification_support_code ) 

 eatc_dona_certification_support: 
 Tipo de soporte de certificación expedido (en este caso siempre será carta_colombia ). 

 eatc_dona_header_code: 
 Código del anuncio de donación soportado ( eatc_dona_headers. eatc-code ) 

 eatc_publication_datetime: 
 Fecha y hora de publicación del anuncio ( eatc_dona_headers. eatc-publication_datetime )", 

 eatc_value: 
 Valor del anuncio certificable antes de IVA (se toma de: eatc_dona_headers. eatc-total_cost ). 

 eatc_receipt_datetime: 
 Fecha de recepción del anuncio ( eatc_dona_headers. eatc-receipt_datetime ). 

 eatc_doc: 
 Documento soporte de la donación ( eatc_dona_headers. eatc-doc ). 

 eatc_donor_code: 
 Documento de identidad del donante ( eatc_dona_headers. eatc-donor_code ). 

 eatc_donor_fiscal_name: 
 Razón social del donante ( eatc_dona_headers. eatc_donor_fiscal_name ). 

 eatc_donation_manager: 
 Gestor de donaciones al que se le entregó la donación ( eatc_dona_headers .eatc-donation_manager_code ). 

 eatc_doma_affiliated_organization: 
 Nombre de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }} 

 Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca ese dato en el registro.  Si viene un NIT, se repite la consulta anteriormente realizada: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{ organizacion_vinculada }} 

 Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.  Si después de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 eatc_doma_affiliated_organization_id: 
 Identificador único de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }} 

 Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca el dato que llega en el campo identificador_unico_registro de la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador= abaco 

 Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.  Si después de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 Creación registro de detalle del soporte 
 El sistema debe generar el registro utilizando el CRD correspondiente 

 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_supports_details &_operacion= insert & {{parametros_creación_detalle_soporte}} 

 Creación de la carta soporte 
 El sistema, con los datos consignados en eatc_certification_supports_headers y eatc_certification_supports_details debe generar una carta (en formato descargable) que se construye de la siguiente manera: 

 {{ eatc_certification_supports_headers. eatc_certification_support_code }} 

 Bogotá { { eatc_certification_supports_headers. eatc_date }} 
 ***MEJORA: Colocar la fecha de la carta como día/mes/año *** 

 Señor: 

 Juan Carlos Buitrago 

 Asociación de Bancos de Alimentos de Colombia ABACO 

 NIT: 900.326.456-1 

 Ciudad 

 Respetados Señores 

 Confirmamos que los productos entregados en donación por parte de la compañía  

{{ eatc_certification_supports_headers. eatc_donor_fiscal_name }} , identificada con NIT: {{ eatc_certification_supports_headers. eatc_donor_code }} , entregados en el mes {{ eatc_certification_supports_headers. eatc_month }} de {{ eatc_certification_supports_headers. eatc_year }} , por un valor ${{ eatc_certification_supports_headers. eatc_value }} , son valorizados a costo acorde a su valor en libros, antes de IVA según el artículo 125-2 estatuto tributario.  
 ***MEJORA: Colocar después del valor en números ({{ eatc_certification_supports_headers. eatc_value }}), el valor en letras (utilizando endpoint que desarrolló Carlos Villa para traer el valor en letras de un número) *** 

 ***AJUSTE: Relación de facturas, o documentos soportes  (Anteriormente: Relación de anuncios) *** (Verificar que en la fecha y hora de publicación se esté llevando la eatc_publication_datetime (que corresponde al dato eatc-publication_datetime de la respectiva donación) 

 Fecha y hora publicación    |    Código del anuncio    |    Valor en libros (antes de IVA)    |    Fecha y hora de recepción 
 {{eatc_certification_supports_details. eatc_publication_datetime }}| {{eatc_certification_supports_details. eatc_dona_header_code }}| 
 {{eatc_certification_supports_details. eatc_value }}|  
 {{eatc_certification_supports_details. eatc_receipt_datetime }}| 

 ***MEJORA: Colocar una fila al final con el total de las donaciones *** 

 Cordialmente 

 {{ eatc_certification_supports_headers. eatc_signature }} 

 {{ eatc_certification_supports_headers. eatc_name }} 
 Cédula de ciudadanía: {{ eatc_certification_supports_headers. eatc_doc_id }} 
 {{ eatc_certification_supports_headers. eatc_position }} 
 T.P.: {{ eatc_certification_supports_headers. eatc_professional_card }} 

 Elaboró: EatCloud System 
 Aprobó: {{ eatc_certification_supports_headers. eatc_name }},{{ eatc_certification_supports_headers. eatc_position }} 

 Nota con respecto a la relación de anuncios: 
 La idea es crear una tabla que se llene con la relación de los anuncios soportados por la carta 

 Nota con respecto a la firma del documento (datos abajo de "Cordialmente"): 
 Inicialmente el documento no contará con la información necesaria para realizar la firma del documento.  En la funcionalidad "Aprobación de carta soporte mediante firma", el usuario deberá aportar la información para generar la firma completa del documento. 

 Creación del documento descargable: 
 Una vez generado el documento, el sistema lo debe guardar, de manera que sea accesible al usuario final (que lo pueda descargar) y deberá incorporar la información necesaria para hacerla en el campo 
 eatc_support_file 

 El sistema, cuando cree la carta sin firmas, deberá realizar la actualización de la información del soporte con el siguiente llamado 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_supports_headers &_operacion= update &eatc_support_file ={{ eatc_support_file }}&WHEREeatc_certification_support_code={{ eatc_certification_supports_headers . eatc_certification_support_code}} 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deberá entregar una respuesta donde exprese que el certificado de donación con código {{ eatc_certification_supports_headers. eatc_certification_support_code }} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un código de error y reversar los registros que pudieron haberse creado de manera parcial, con el ánimo que se pueda reintentar la operación hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 464f930a-1383-4ca4-bee2-5d8d5c05671b 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 58758245-7a4c-4a6f-b9c1-bfd07572ada1 
 2025-05-30T05:03:13.0419436Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"01c1c80e-d34d-4ff4-ad4b-5f43aa1f2a39","SequenceId":447,"FluidContainerCustomId":"496d7b02-82fa-49df-9990-b133e9313d04","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 CREACIÓN DE CARTA SOPORTE (CREA_SPRT)