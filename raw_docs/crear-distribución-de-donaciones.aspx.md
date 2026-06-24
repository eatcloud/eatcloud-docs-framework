# crear-distribución-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo:  esta funcionalidad permitirá seleccionar a partir del Kardex que se crea mediante el servicio " donatokardex " productos a redistribuir desde puntos de distribución (configurados para el beneficiario en un onboarding especial tipo " donante ") a otras organizaciones sociales que estarán en la zona de influencia de dichos puntos.  Para realizar dicho registro, utilizará el API pública para crear donaciones a partir del kardex .  Al generar dichas distribuciones, en últimas se generarán donaciones en estado "adjudicadas", que podrán gestionarse por la app de beneficiarios, y también por la WEBAPP del punto de distribución (punto de donación adscrito al beneficiario).  Estas donaciones también tendrán como característica, que no generarán KPIs , dado que los mismos se generarán a partir de las donaciones que fueron marcadas para ser distribuídas. 

 VALIDACIONES PREVIAS ANTES DE DESPLEGAR LA FUNCIONALIDAD 

 Validación del estado y la condición del gestor de donaciones como hub de distribución. 
 El sistema realiza la siguiente consulta, utilizando el " identificador_unico_registro " del beneificario que está logueado en la plataforma {{eatc_donation_managers. identificador_unico_registro }} 

 {{ URL_entorno_beneficiarios }}/api/{{ cua_master }}/eatc_donation_managers? identificador_unico_registro ={{eatc_donation_managers. identificador_unico_registro }}&eatc-state= activo &eatc_dist_hub= y&_cmp= eatc-state,eatc_dist_hub 

 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta: 

 class= lbl_doma_no_valido ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_doma_no_valido )    "El gestor de donaciones, no está configurado para operar un hub de distribución. ( error_code: doma_config)" 

 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación. 

 Ejemplo 1: entorno de pruebas, cua_master " abaco ", eatc_dona_distributor : " 811018073 " 

 El sistema realiza la siguiente consulta: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811018073&eatc-state=activo&eatc_dist_hub=y&_cmp=identificador_unico_registro     

 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 

 Ejemplo 2: entorno de pruebas, cua_master " abaco ", eatc_dona_distributor : " 811000384 " 

 El sistema realiza la siguiente consulta: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811000384&eatc-state=activo&eatc_dist_hub=y&_cmp=identificador_unico_registro       

 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta: 

 "El gestor de donaciones, no está configurado para operar un hub de distribución. ( error_code: doma_config)" 

 Validación de la configuración del gestor de donaciones como donante para gestionar las distribuciones. 
 El sistema realiza la siguiente consulta, utilizando el " identificador_unico_registro " del beneificario que está logueado en la plataforma {{eatc_donation_managers. identificador_unico_registro }} 

 {{ URL_entorno_datagov }}/crypt/eatcloud/getcrypt?table=eatc_customers_cua&fieldname=eatc_customer_fiscal_id&fieldvalue={{eatc_donation_managers. identificador_unico_registro }}&fielddecrypt=eatc_cua   

 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta: 

 class= lbl_doma_no_configurado ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_doma_no_configurado ) "El gestor de donaciones, no está configurado para entregar donaciones como hub de distribución. ( error_code: doma_cua_config)" 

 Si la consulta arroja respuesta una respuesta válida el sistema, guarda el dato {{eatc_customers_cua. eatc_cua }}  (que corresponde al nombre de la cua_user que ha sido asignado al gestor de donaciones que administra un hub de distribución) y despliega la funcionalidad que se define a continuación . 

 Ejemplo 1: entorno productivo, eatc_dona_distributor : " 900082682 " 

 El sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&fieldname=eatc_customer_fiscal_id&fieldvalue=900082682&fielddecrypt=eatc_cua     

 El sistema guarda el valor {{eatc_customers_cua. eatc_cua }}= fubam para utilizarlo más adelante en el proceso 

 Dada la respuesta válida que trae el servicio entonces el sistema despliega la funcionalidad .  

 Ejemplo 2: entorno productivo, eatc_dona_distributor : " 811000387 " 

 EEl sistema realiza la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&fieldname=eatc_customer_fiscal_id&fieldvalue=811000387&fielddecrypt=eatc_cua      

 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta: 

 "El gestor de donaciones, no está configurado para entregar donaciones como hub de distribución. ( error_code: doma_cua_config)" 

 SELECTOR DE PUNTO DE DISTRIBUCIÓN DESDE EL CÚAL SE ENTREGARÁ LA DONACIÓN: 

 La funcionalidad deberá mostrar un selector para elegir el punto de distribución (punto de donación) desde donde saldrá la donación: 

 Label (place holder): class= lbl_selecciona_pod ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_selecciona_pod ) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Tipo de campo de captura: Selector único 
 El selector se arma con la información tomada de:  
 El sistema realiza la siguiente consulta 
 {{url_donantes}} /api/ {{eatc_customers_cua. eatc_cua }} /eatc_pods?eatc-id= _* &_cmp= eatc-id, eatc-name,eatc-city, eatc-responsable,eatc-lat,eatc-lon 
 En el selector se debe presentar una concatenación del campo eatc-name y eatc-city, así: {{eatc-name}} - {{eatc-city}} - {{eatc-responsable}} 
 Valor por defecto: ninguno (vacío) 

 El código correspondiente al valor seleccionado por el usuario ( eatc_pods. eatc-id ) se guardará en la variable: {{ eatc_pod_id }} 

 SELECTOR DE BENEFICIARIO PARA LA DISTRIBUCIÓN: 
 El sistema deberá desplegar un campo de captura numérico, que refiera los KM a la redonda del punto de donación, a partir de este dato, se genera un listado de gestores de donación en el área de influencia del hub de distribución, y a partir de dicha información se construirán filtros adicionales para establecer criterios que permitan traer los datos de un gestor de donaciones que recibirá la distribución de la donación.  La funcionalidad principal será entonces la generación de un selector de gestores de donaciones, el cuál se podrá filtrar por diferentes criterios que se especifican a continuación: 

 KM: 
 Label (place holder): class= lbl_km ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_km ) 
 Tipo de dato: integer 
 Obligatoriedad : si 
 Validación : obligatoriedad, valor numérico 
 Tipo de campo de captura: campo de numérico 
 Valor por defecto: 7 

 El usuario podrá variar el valor de los KM, el dato lo llevará a la variable {{ KM }} , con este valor, y valores obtenidos en consultas previas (como es el caso de {{ eatc_pods. eatc-lat }} , {{ eatc_pods. eatc-lon }} , en la consulta anterior) el sistema realizará la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/get/abaco/getpuntos? table = eatc_donation_managers & fieldname = coordenadas & fieldvalue = {{ eatc_pods. eatc-lat }} , {{ eatc_pods. eatc-lon }} & showfield = identificador_unico_registro,organizacin,municipio,eatc_comuna_localidad & km = {{ KM }} &filterfield_1= eatc-state &filtervalue_1= activo, pasivo 

 Con la información obtenida el sistema genera los siguientes filtros:  

 Ciudad: 
 Label (place holder): class= lbl_ciudad ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_ciudad ) 
 Tipo de dato: string 
 Obligatoriedad : no 
 Validación : ninguna 
 Tipo de campo de captura: Selector único 
 El selector se arma con la información tomada de:  los datos de la consulta anterior que se retornan en: eatc_donation_managers . municipio 
 Valor por defecto: ninguno 

 El usuario podrá variar seleccionar una ciudad (que se llevará a la variable {{ ciudad }} y a partir de dicha selección y de valores previamente obtenidos o configurados  el sistema realizará la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/get/abaco/getpuntos? table = eatc_donation_managers & fieldname = coordenadas & fieldvalue = {{ eatc_pods. eatc-lat }} , {{ eatc_pods. eatc-lon }} & showfield = identificador_unico_registro,organizacin,municipio,eatc_comuna_localidad & km = {{ KM }} &filterfield_1= eatc-state &filtervalue_1= activo, pasivo &filterfield_2= municipio &filtervalue_2= {{ ciudad }} 

 Con la información obtenida el sistema genera el siguiente filtro:  

 Localidad / Comuna: 
 Label (place holder): class= lbl_localidad_comuna ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_localidad_comuna ) 
 Tipo de dato: string 
 Obligatoriedad : no 
 Validación : ninguna 
 Tipo de campo de captura: Selector único 
 El selector se arma con la información tomada de:  los datos de la consulta anterior que se retornan en: eatc_donation_managers . eatc_comuna_localidad 
 Valor por defecto: ninguno 

 El usuario podrá variar seleccionar una ciudad (que se llevará a la variable {{ comuna_localidad }} y a partir de dicha selección y de valores previamente obtenidos o configurados  el sistema realizará la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/get/abaco/getpuntos? table = eatc_donation_managers & fieldname = coordenadas & fieldvalue = {{ eatc_pods. eatc-lat }} , {{ eatc_pods. eatc-lon }} & showfield = identificador_unico_registro,organizacin,municipio,eatc_comuna_localidad & km = {{ KM }} &filterfield_1= eatc-state &filtervalue_1= activo, pasivo &filterfield_2= municipio &filtervalue_2= {{ ciudad }}& &filterfield_3= eatc_comuna_localidad &filtervalue_3= {{ comuna_localidad }} 

 Receptor de la distribución: 
 Label (place holder): class= lbl_receptor_dist ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_receptor_dist ) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validación : Obligatoriedad 
 Tipo de campo de captura: Selector único 
 El selector se arma con la información tomada de:  los datos de la consulta anterior que se retornan en: eatc_donation_managers . organizacin 
 Valor por defecto: ninguno 

 El usuario tendrá que seleccionar un gestor de donaciones que recibirá la distribución y al hacerlo, llevará el valor eatc_donation_managers . identificador_unico_registro correspondiente a la selección, a la variable: {{ eatc_donation_manager_code }} 

 AGREGAR PRODUCTOS A LA DISTRIBUCIÓN: 
 La funcionalidad deberá presentar un campo de captura para establecer los días del último movimiento de inventario y a partir de ese dato, obtener los productos que tienen existencia 

 Días para el último movimiento: ***NUEVO:  se separan kardex por cua_user correspondiente al gestor de hubs *** 

 Label (place holder): class= lbl_dias_ult_mov ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_dias_ult_mov ) 
 Tipo de dato: integer 
 Obligatoriedad : si 
 Validación : obligatoriedad, valor numérico, valor máximo: 30 días. 
 Tipo de campo de captura: campo de numérico 
 Valor por defecto: 7 

 El usuario podrá variar el valor de los días del último movimiento de inventario y lo llevará a la variable {{ dias }} , con este valor,  calculará la fecha inicial de la consulta 
 {{ fecha_inicial }} = {{fecha_actual}} - {{ dias }} 

 Con estos datos y el dato   {{eatc_customers_cua. eatc_cua }}  (obtenido en el proceso de  validación del gestor de donaciones como donante ),  {{eatc_dona .eatc_donor }} el sistema realiza la siguiente consulta: 

 {{ URL_entorno_donantes }}/api/ {{ eatc_customers_cua .eatc_cua}} / eatc_kardex ? eatc_cua_origen= {{eatc_customers_cua. eatc_cua }} & eatc_date[0]={{ fecha_inicial }}&eatc_date[1]={{ fecha_actual }} & eatc_actual_stock=_>0 &_cmp= _id,eatc_odd_id,eatc_odd_name, eatc_donor,eatc_odd_unit_weight_kg.eatc_closer_expiration_date,eatc_return_cause,eatc_date_time,eatc_actual_stock 

 En vez de tener un kardex por cuenta maestra (como estaba anteriormente y se muestra a continuación), se tienen kardex por cua_user correspondiente al gestor de donaciones que administra el hub ( {{eatc_customers_cua. eatc_cua }} ), esto con el objetivo de poder controlar el inventario para cada administrador del hub y no tener un kardex global que pueda mezclar inventarios de varios gestores de donaciones administradores de hubs 

 Anteriormente: 

 {{ URL_entorno_donantes }}/api/{{ cua_master }}/ eatc_kardex ? eatc_cua_origen= {{eatc_customers_cua. eatc_cua }} &eatc_date[0]={{ fecha_inicial }}&eatc_date[1]={{ fecha_actual }}& eatc_actual_stock=_>0 &_cmp= _id,eatc_odd_id,eatc_odd_name,eatc_donor,eatc_odd_unit_weight_kg.eatc_closer_expiration_date,eatc_return_cause,eatc_date_time,eatc_actual_stock 

 El sistema agrupará por eatc_odd_id y determinará para cada arreglo de datos, si el registro más reciente (según  eatc_date_time ), posee stock ( eatc_act_stock mayor que cero) con esos registros  más recientes con existencias, armará una tabla de datos que tendrá un campo para agregar cantidades y que presentará la siguiente información: 

 Tabla de información de productos, para agregar cantidades: 
 Esta tabla paginada, deberá tener la oporunidad de filtrar por columnas, buscar registros y ordenar por columnas, y presentará la siguiente información: 

 ID 
 label: class= lbl_id ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_id ) 
 Presenta la información contenida en: {{eatc_kardex. eatc_odd_id }}    

 Nombre 
 label: class= lbl_nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_nombre ) : 
 Presenta la información contenida en: {{eatc_kardex. eatc_odd_name }}     

 Donante 
 label: class= lbl_donante ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_donante ) 
 Presenta la información contenida en: {{eatc_kardex. eatc_donor }}     

 Peso unitario en KG 
 label: class= lbl_peso_unitario_kg ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_peso_unitario_kg ) 
 Presenta la información contenida en: {{eatc_kardex. eatc_odd_unit_weight_kg }}     

 Fecha de vencimiento 
 label: class= lbl_fecha_vencimiento ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_fecha_vencimiento ) 
 Presenta la información contenida en: {{eatc_kardex. act }}   

 Cantidades en inventario 
 label: class= lbl_cant_inv ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cant_inv ) 
 Presenta la información contenida en: {{eatc_kardex. eatc_act_stock }}     

 Cantidad a distribuir (Columna con campos de texto para ingresar cantidades) 
 label: class= lbl_cant_dist ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_cant_dist ) 
 Tipo de dato: integer 
 Obligatoriedad : no (se pueden dejar casillas vacías, lo cuál indicará que de ese producto no se realizará distribución 
 Validación : el valor debe ser menor al que para el respectivo registro retorna {{eatc_kardex. eatc_act_stock }} , campo numérico 
 Tipo de campo de captura: campo de numérico 
 Valor por defecto: ninguno (vacio) 
 El valor ingresado por el usuario se llevará a la variable para cada producto {{ eatc_odd_dist_quantity }} 

 Documento soporte: 
 El sistema desplegará un campo de captura para el documento soporte 
 Label (place holder): class= lbl_documento_soporte ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_documento_soporte ) 
 Tipo de dato: string 
 Obligatoriedad : no (campo de captura opcional) 
 Validación : ninguna 
 Tipo de campo de captura: alfanumérico 
 Valor por defecto: ninguno 
 El valor ingresado por el usuario se llevará a la variable para cada producto {{ eatc_doc }} 

 Cuando el usuario termine de ingresar los datos, podrá oprimir el siguiente botón que será el encargado de armar los objetos para invocar el API correspondiente para crear una donación a partir del kardex . 

 CREAR DISTRIBUCIÓN 
 label: class= lbl_crear_dist ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_crear_dist )  

 Array de objetos: productos a ser distribuidos 
 Al oprimir el botón el sistema realizará un array de objetos de aquellos productos que el usuario determinó con cantidades a distribuir, de la siguiente manera: 

 eatc_pod_id = {{ eatc_pod_id }}    *** obtenido en el selector de puntos de distribución .  Se agrega a cada objeto de producto*** 
 eatc_donor ={{eatc_kardex. eatc_donor }} *** obtenido en la tabla para agregar productos a la distribución *** 
 eatc_odd_id ={{eatc_kardex. eatc_odd_id }} *** obtenido en la tabla para agregar productos a la distribución *** 
 eatc_odd_dist_quantity = {{ eatc_odd_dist_quantity }} *** obtenido en la tabla para agregar productos a la distribución *** 

 Este array de objetos los colocará dentro del parámetro _data de la invocación del API para la creacion de donaciones a partir del kardex , y generará el siguiente arreglo de datos para invocar el API : 

 Encabezado del llamado: 
 _operation = create_donation_from_kardex   *** constante *** 
 eatc_dona_distributor = {{eatc_donation_managers. identificador_unico_registro }} *** Identificador único de registro del beneficiario que utiliza la plataforma*** 
 eatc_donation_manager_code = {{ eatc_donation_manager_code }} *** obtenido en el selector de gestor de donaciones que recibe la distribución*** 
 eatc_doc = {{ eatc_doc }} *** OPCIONAL: obtenido en la captura de documento soporte *** 
 _data : *** array de objetos construídos con la captura anterior.*** 

 Mensaje al usuario ante una creación exitosa: 
 label: class= lbl_crear_dist_exito ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&idlabel= lbl_crear_dist_exito )  
 "Distribución creada exitosamente" 

 Mensaje al usuario ante un problema: 
 Se le retorna el mensaje de error que entrega la API 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 CREAR DISTRIBUCIÓN DE DONACIONES