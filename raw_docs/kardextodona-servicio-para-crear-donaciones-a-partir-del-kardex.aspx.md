# kardextodona-servicio-para-crear-donaciones-a-partir-del-kardex.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para, a partir de los datos del punto de donación, del beneficiario final y de registros de inventario (kardex), se genere una donación &quot;Asignada&quot; (awarded) y también se realicen los consiguientes controles en el kardex para generar la respectiva &quot;salida&quot; de inventario a partir de esta distribución.&#160; Se debe implementar como un servicio público, cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento&#160;&#160; 
&#160; 
 Documentación de API pública para la creación de donaciones a partir de registros de&#160; Kardex&#160; 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 
&#160; 
&#160; 
 LOG DEL SERVICIO 
 El sistema deberá guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqué de un llamado no exitoso (datos incompletos, fallo de ejecución, fallos validación entre otros) 

&#160; 
&#160; 
 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;“op”&#58;”false” 
&#160; 
&#160; 
 1. VALIDACIÓN DE DATOS COMPLETOS 
&#160; 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación de la API Pública .&#160; Si los datos están completos se seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 
&#160; 
 2. VALIDACIÓN DEL ESTADO, CONDICIÓN Y CONFIGURACIÓN COMO DONANTE (PARA ADMON DEL HUB DE DISTRIBUCIÓN) DEL GESTOR DE DONACIONES 
&#160; 
 2.1. Estado y condición del gestor de donaciones 
 Con el dato que llega en los parámetros de invocación del API pública &#58; 
 eatc_dona_distributor 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123; eatc_dona_distributor &#125;&#125;&amp;eatc-state= activo &amp;eatc_dist_hub= y&amp;_cmp= identificador_unico_registro 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
 err_msg&#58; invalid doma 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación. 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_distributor &#58; &quot; 811018073 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811018073&amp;eatc-state=activo&amp;eatc_dist_hub=y&amp;_cmp=identificador_unico_registro &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 

&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_distributor &#58; &quot; 811000384 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811000384&amp;eatc-state=activo&amp;eatc_dist_hub=y&amp;_cmp=identificador_unico_registro &#160;&#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 fail 
 err_msg&#58; invalid doma 

&#160; 
 2.2. Validación de la configuración del gestor de donaciones como donante (para administración del hub de distribución) 
&#160; 
 Con el dato que llega en los parámetros de la anterior consulta&#58; 
 eatc_dona_distributor 
&#160; 
 El sistema deberá validar que el gestor de donaciones esté configurado también como &quot;donante&quot;, de tal manera que pueda gestionar las distribuciones desde la WAPP, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=&#123;&#123; eatc_dona_distributor &#125;&#125;&amp;fielddecrypt=eatc_cua 
&#160; 
 El sistema guarda el valor (desencriptado) obtenido en &#160; &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &#160;(que corresponde al nombre de la cua_user que ha sido asignado al gestor de donaciones que administra un hub de distribución) , para futuras operaciones. 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
 err_msg&#58; invalid doma configuration for hub admin 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación.&#160; 

&#160; 
 Ejemplo 1&#58; entorno productivo, eatc_dona_distributor &#58; &quot; 900082682 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=900082682&amp;fielddecrypt=eatc_cua &#160; &#160; 
&#160; 
 El sistema guarda el valor &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125;= fubam para utilizarlo más adelante en el proceso 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante .&#160; 

&#160; 
 Ejemplo 2&#58; entorno productivo, eatc_dona_distributor &#58; &quot; 811000387 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=811000387&amp;fielddecrypt=eatc_cua &#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 fail 
 err_msg&#58; invalid doma configuration for distribution hub admin 
&#160; 
&#160; 
 3. CONSULTA DE DATOS DEL KARDEX PARA ESTABLECER SI EL PRODUCTO A DONAR EXISTE Y TIENE EXISTENCIAS ***NUEVO&#58; &#160;se separan kardex por cua_user correspondiente al gestor de hubs *** 
&#160; 
 Con los datos que llegan en el encabezado 
 eatc_dona_distributor &#160; 
&#160; 
 y los diferentes parámetros de los Objetos dentro _data &#58; 
 eatc_donor &#160; 
 eatc_odd_id 
 eatc_odd_dist_quantity 
&#160; 
 Y con el dato&#160; &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &#160;(obtenido en el proceso de&#160; validación del gestor de donaciones como donante ), 
&#160; 
 El sistema deberá validar que el artículo exista en el kardex y que tenga existencias suficientes para atender la donación establecida, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/ &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; / eatc_kardex ?eatc_cua_origin= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &amp;eatc_donor=&#123;&#123; eatc_donor &#125;&#125;&amp;eatc_odd_id=&#123;&#123; eatc_odd_id &#125;&#125;&amp; eatc_act_stock= _&gt;0 &amp;_cmp= _id,eatc_date_time , eatc_act_stock 
 En vez de tener un kardex por cuenta maestra (como estaba anteriormente y se muestra a continuación), se tienen kardex por cua_user correspondiente al gestor de donaciones que administra el hub ( &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; ), esto con el objetivo de poder controlar el inventario para cada administrador del hub y no tener un kardex global que pueda mezclar inventarios de varios gestores de donaciones administradores de hubs 
&#160; 
 Anteriormente&#58;&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_kardex ?eatc_cua_origin= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &amp;eatc_donor=&#123;&#123; eatc_donor &#125;&#125;&amp;eatc_odd_id=&#123;&#123; eatc_odd_id &#125;&#125;&amp; eatc_act_stock= _&gt;0&amp;_cmp= _id,eatc_date_time , eatc_act_stock 
&#160; 
 Si el servicio no encuentra resultados debe retornar un error 
 fail 
 err_msg&#58;&#160; eatc_donor&#58; &#123;&#123; eatc_donor &#125;&#125;, eatc_odd_id&#58; &#123;&#123; eatc_odd_id &#125;&#125;&#58; Product not in stock 
&#160; 
 Si la consulta arroja resultados, el sistema debe tomar el registro más reciente (según el dato obtenido en&#58; eatc_date_time ) y realizar la siguiente comparación (verificar si el último (más reciente) &quot; stock actual &quot; ( eatc_act_stock ), es mayor o igual a la cantidad a distribuir) 
 eatc_act_stock &gt;= eatc_odd_dist_quantity 
&#160; 
 Teniendo el registro más reciente una consulta al API que puede establecer dicha condición es&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/ &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; / eatc_kardex ?eatc_donor=&#123;&#123; eatc_donor &#125;&#125;&amp;eatc_odd_id=&#123;&#123; eatc_odd_id &#125;&#125;&amp; eatc_date_time= &#123;&#123; fecha_hora_mas_reciente &#125;&#125;&amp; eatc_act_stock= _&gt;_ &#123;&#123; eatc_odd_dist_quantity &#125;&#125;&amp;_cmp= _id,eatc_date_time , eatc_act_stock 
&#160; 
 Anteriormente&#58;&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_kardex ?eatc_cua_origin= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &amp;eatc_donor=&#123;&#123; eatc_donor &#125;&#125;&amp;eatc_odd_id=&#123;&#123; eatc_odd_id &#125;&#125;&amp; eatc_date_time= &#123;&#123; fecha_hora_mas_reciente &#125;&#125;&amp; eatc_act_stock= _&gt;_&#123;&#123; eatc_odd_dist_quantity &#125;&#125;&amp;_cmp= _id,eatc_date_time , eatc_act_stock 
&#160; 
 Al obtener el valor de eatc_act_stock más reciente, el sistema determina que&#58; 
 &#160; eatc_prev_stock_value =&#123;&#123; eatc_kardex . eatc_act_stock &#125;&#125; 

&#160; 
 En caso de que la consulta no arroje resultados, el sistema deberá responder con un mensaje de error&#58; 
 fail 
 err_msg&#58;&#160; eatc_donor&#58; &#123;&#123; eatc_donor &#125;&#125;, eatc_odd_id&#58; &#123;&#123; eatc_odd_id &#125;&#125;&#58; Insufficient stock 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación. 
&#160; 
 En caso de obtener un resultado válido, el sistema guarda el dato obtenido en&#160; eatc_kardex. _id es decir, que deberá obtener el _id del registro más reciente de kardex con el ánimo de realizar las siguientes consultas. 

 4. VALIDACIÓN DE FECHAS DE VENCIMIENTO PARA DETERMINAR SI UNA DONACIÓN SE PUEDE REDISTRIBUIR ( IMPLEMENTACIÓN EN SEGUNDA ETAPA ) 
 Nota importante para este desarrollo &#58; en una segunda etapa se analizarán posibles restricciones ante registros válidos en fecha de vencimiento más próxima.&#160; Por el momento en la implementación inicial no se deberán implementar estas validaciones. 

 5. FLUJO DE PROCESO DE CREACIÓN DE DONACIONES A PARTIR DE UN REGISTRO DE REGISTRO DE KARDEX 
&#160; 
 5.1. Consulta de datos del kardex para generar el anuncio de donación. 
 Con los datos que se obtubieron en anteriores consultas&#58; 
 eatc_kardex. _id 
&#160; 
 El sistema realizan ls siguientes consultas&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/ eatc_kardex ?_id=&#123;&#123; eatc_kardex. _id &#125;&#125; 
&#160; 
 Los valores recibidos se guardan para el posterior registro de baja del kardex. 
&#160; 
 5.2. Registro de detalles de donación&#160; 
 A partir de los parámetros de llamado a la presente API, a saber&#58; 
 eatc_dona_header_code &#160; 
 eatc_donation_manager_code 
 eatc_dona_distributor 
 eatc_doc &#160; 
&#160; 
 eatc_pod_id &#160; 
 eatc_donor &#160; 
 eatc_odd_id 
 eatc_odd_dist_quantity 
&#160; 
 Y de los datos que se han obtenido en consultas previas, se procede, para registrar el detalle de la donación a invocar el API Pública para la creación de donaciones , cuyos parámetros de invocación ( documentados aquí ) y se construirán de la siguiente manera&#58; 

&#160; 
 _operation = create_donation *** CONSTANTE&#58; parámetro de invocación de la actual servicio*** 
 eatc-dona_header_code = &#123;&#123;eatc_dona_header_code&#125;&#125; &#160; *** OPCIONAL&#58; parámetro de invocación de la actual servicio*** 
 eatc-donation_manager_code = &#123;&#123;eatc_donation_manager_code&#125;&#125;&#160; *** Parámetro de invocación de la actual servicio*** 
 eatc_dona_distributor =&#160; &#123;&#123; eatc_dona_distributor &#125;&#125; ***Parámetro de invocación de la actual servicio*** 
 eatc_doc = &#123;&#123;eatc_doc&#125;&#125;&#160; *** OPCIONAL&#58; parámetro de invoación de la actual servicio*** 
&#160; 
 _data *** Array de objetos&#58; se envía el siguiente array por cada uno de los productos que llegan en el llamado al presente servicio*** 
&#160; 
 eatc-pod_id =&#160; &#123;&#123;eatc_pod_id &#125;&#125; *** Parámetro de invocación de la actual servicio*** 
 eatc-odd_id =&#160; &#123;&#123;eatc_odd_id &#125;&#125; *** Parámetro de invocación de la actual servicio*** 
 eatc-odd_name =&#160; &#123;&#123; eatc_kardex. eatc_odd_name&#125;&#125; 
 eatc-odd_original_quantity &#160; =&#160; &#123;&#123; eatc_odd_dist_quantity &#125;&#125;&#160; *** Parámetro de invocación de la actual servicio*** 
 eatc-odd_unit_weight_kg &#160; =&#160; &#123;&#123; eatc_kardex. eatc_odd_unit_weight_kg&#125;&#125; 
 eatc-unit_cost &#160; =&#160; &#123;&#123; eatc_kardex. eatc_odd_unit_cost&#125;&#125; 
 eatc-VAT_percentage &#160; =&#160; &#123;&#123; eatc_kardex. eatc_vat_percentage&#125;&#125; 
 eatc-donor = &#123;&#123; eatc_donor &#125;&#125;&#160; *** Parámetro de invocación de la actual servicio*** 
&#160; 
 Una vez el servicio de creación de anuncios tenga una respuesta satisfactoria, se procederá a realizar el registro de salida de inventario 

&#160; 
 5.2. Registro de salida de inventario&#160; 
 Para registrar la salida de inventario, por cada producto que integró la donación (elemento del array de objetos dentro de _data ), se realiza el siguiente llamado 
&#160; 
 Parámetros de invocación del CRD &#123;&#123;param_ins_kardex&#125;&#125; 
 eatc_date_time= &#123;&#123; datetime_stamp en formato AAAA-MM-DD HH&#58;MM&#58;SS con la fecha y hora de la invocación del CRD &#125;&#125; 
 eatc_date= &#123;&#123; date_stamp en formato AAAA-MM-DD con la fecha de la invocación del CRD &#125;&#125; 
 eatc_transaction_type = output ***Constante &quot; output&quot; que queiere decir que el registro es una salida de inventario *** 
 eatc_cua_origen = &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; ***Valor que se obtiene en la validación de configuración *** 
 eatc_donor = &#123;&#123; eatc_kardex .eatc_donor &#125;&#125; ***Como el registro se hace por ítem del array este dato es único*** 
 eatc_dona_header_code= &#123;&#123;eatc_dona .eatc-dona_header_code &#125;&#125; ***Código de la donación creada en el paso anterior *** 
 eatc_doc = &#123;&#123;eatc_doc&#125;&#125;&#160; *** OPCIONAL&#58; parámetro de invocación del servicio KARDEXTODONA*** 
 eatc_odd_id = &#160; &#123;&#123;eatc_odd_id &#125;&#125;&#160; ***Parámetro de invocación del servicio KARDEXTODONA*** 
 eatc_odd_code = &#160; &#123;&#123;eatc_odd_id &#125;&#125;&#160; ***Parámetro de invocación del servicio KARDEXTODONA*** 
 eatc_odd_name = &#123;&#123; eatc_kardex. eatc_odd_name&#125;&#125; &#160; ***Dato consultado en paso previo *** 
 eatc_odd_quantity =&#160; &#123;&#123; eatc_odd_dist_quantity &#125;&#125;&#160; ***Parámetro de invocación del servicio KARDEXTODONA*** 
 eatc_prev_stock = &#123;&#123; eatc_prev_stock_value &#125;&#125; ***Consultado en paso previo *** 
 eatc_act_stock = &#123;&#123; &#123;&#123; eatc_prev_stock_value - &#123;&#123; eatc_odd_dist_quantity &#125;&#125;&#125;&#125; ***Al stock previo se le restan las cantidades que fueron distribuídas*** 
 eatc_odd_unit_weight_kg =&#160; &#123;&#123; eatc_kardex. eatc_odd_unit_weight_kg&#125;&#125; &#160; ***Dato consultado en paso previo *** 
 eatc_odd_unit_cost = &#123;&#123; eatc_kardex. eatc_odd_unit_cost&#125;&#125; ***Dato consultado en paso previo *** 
 eatc_VAT_percentage = &#123;&#123; eatc_kardex. eatc-VAT_percentage &#125;&#125; ***Dato consultado en paso previo *** 
 origin_odds_typology_a = &#123;&#123; eatc_kardex. origin_odds_typology_a &#125;&#125; ***Dato consultado en paso previo *** 
 origin_odds_typology_b = &#123;&#123; eatc_kardex. origin_odds_typology_b &#125;&#125; ***Dato consultado en paso previo *** 
 origin_odds_typology_c = &#123;&#123; eatc_kardex. origin_odds_typology_c &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_odd_typology_a = &#123;&#123; eatc_kardex. eatc-odd_typology_a &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_odd_typology_b = &#123;&#123; eatc_kardex .eatc-odd_typology_b &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_odd_typology_c = &#123;&#123; eatc_kardex .eatc-odd_typology_c &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_odd_external_code = &#123;&#123; eatc_kardex .eatc-odd_external_code &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_pod_id = &#123;&#123; eatc_kardex .eatc-pod_id &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_provider_id = &#123;&#123; eatc_kardex .eatc-provider_id &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_return_cause_code = &#123;&#123; eatc_kardex .eatc-return_cause_code &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_return_cause = &#123;&#123; eatc_kardex .eatc-return_cause &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_contains_alergens = &#123;&#123; eatc_kardex .eatc-contains_alergens &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_closer_expiration_date = &#123;&#123; eatc_kardex .eatc-closer_expiration_date &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_lote = &#123;&#123; eatc_kardex .eatc_lote &#125;&#125; ***Dato consultado en paso previo *** 
 eatc_user =&#123;&#123;eatc_user&#125;&#125; *** parámetro de invocación del servicio KARDEXTODONA mediante el API pública*** 
 , 
&#160; 
 5.3. Escritura con el CRD ***NUEVO&#58; &#160;se separan kardex por cua_user correspondiente al gestor de hubs *** 
 Con los parámetros obtenidos se realiza la siguiente escritura&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; /?_tabla= eatc_kardex &amp;_operacion=insert&amp; &#123;&#123;param_ins_kardex&#125;&#125; 
&#160; 
 Anteriormente&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master&#125;&#125;/?_tabla= eatc_kardex &amp;_operacion=insert&amp; &#123;&#123;param_ins_kardex&#125;&#125; 

 6. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 

 Si las actualizaciones de información realizadas por el servicio se realizan de manera adecuada, entonces entregará la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 KARDEXTODONA: SERVICIO PARA CREAR DONACIONES A PARTIR DE REGISTROS DE KARDEX