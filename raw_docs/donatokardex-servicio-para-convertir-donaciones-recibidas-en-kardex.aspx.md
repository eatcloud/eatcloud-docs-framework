# donatokardex-servicio-para-convertir-donaciones-recibidas-en-kardex.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
 El presente servicio se especifica para transformar donaciones recibidas, en registros de inventario o Kardex, que serán la base de la generación de &quot;Redistribuciones de donaciones&quot; (validando condiciones que deben cumplirse para realizar dicha redistribución), y si las condiciones de la donación así lo permiten, convertir una donación correctamente recibida por un beneficiario, en un registro de inventario que alimentará las redistribuciones que se realizarán.&#160; Se debe implementar como un servicio público, cuyos endpoints, parámetros de invocación y respuestas, se detallan en el siguiente documento&#160;&#160; 
&#160; 
 Documentación de API pública para la creación de registro de Kardex&#160; 
&#160; 
 Para evitar duplicidad en la documentación, la implementación del servicio deberá basarse en dicha documentación (si se deben hacer cambios se debe intervenir dicha documentación), y a continuación se explica lo que el servicio debe realizar con la información recibida. 

 LOG DEL SERVICIO 
 El sistema deberá guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqué de un llamado no exitoso (datos incompletos, fallo de ejecución, fallos validación entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIÓN DEL SERVICIO 
 Si existe un fallo de ejecución en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;“op”&#58;”false” 

 1. VALIDACIÓN DE DATOS COMPLETOS 
 El servicio debe validar que los datos de invocación sean completos, según la definición de . Parámetros del body de la petición &#160; de la especificación de la API Pública . Vale la pena anotar, que si bien los datos eatc_odd_id &#160; y eatc_odd_quantity Son opcionales, no se podrán recibir peticiones que contengan eatc_odd_quantity sin contener eatc_odd_id (lo contrario si puede suceder, peticiones que contengan eatc_odd_id y no contengan eatc_odd_quantity ).&#160; Si los datos están completos se seguirá adelante con el próximo paso.&#160; Si no lo son deberá entregar una respuesta de error&#58; 
 incomplete_data 

 2. CONSULTA DE DATOS DE LA DONACIÓN PARA ESTABLECER SI ES VÁLIDA PARA CONVERTIR EN REGISTRO DE KARDEX Y PARA VALIDACIONES POSTERIORES 
&#160; 
 Con el dato que llega en los parámetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 El sistema deberá validar que el estado de la donación sea el correcto (garantizando que halla sido verificada por el beneficiario o gestor de donaciones para establecer las unidades aptas para el consumo humano&#58; eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified ) y que la donación no haya sido previamente distribuída ( eatc_distribution = ! y ), realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp;eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc_state2= ! distributed &amp;_cmp= eatc-donation_manager_code,eatc_closer_expiration_date,eatc-state, eatc_state2 
&#160; 
 El servicio guarda los valores obtenidos de la consulta para posteriores registros ( eatc_dona_headers. eatc-donation_manager_code, eatc_dona_headers. eatc_closer_expiration_date, eatc_dona_headers. eatc-state ) 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 fail 
 err_msg&#58; invalid dona 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema sigue con la siguiente validación. 

&#160; 
 Ejemplo 1&#58; entorno de producción, cua_master &quot; abaco &quot;, eatc_dona_header _code &#58; &quot; 00002007214302 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00002007214302&amp;eatc-receipt_datetime=!0000-00-00%2000&#58;00&#58;00&amp;eatc-state=delivered,received&amp;eatc_state2= ! distributed&amp;_cmp= eatc-donation_manager_code,eatc_closer_expiration_date,eatc-state, eatc_state2 &#160; &#160; &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante, guardando los valores recibidos para futuras acciones 

&#160; 
 Ejemplo 2&#58; entorno de producción, cua_master &quot; abaco &quot;, eatc_dona_header _code &#58; &quot; exito00007 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=exito00007&amp;eatc-receipt_datetime=!0000-00-00%2000&#58;00&#58;00&amp;eatc-state=delivered,received&amp; eatc_state2= ! distributed &amp;_cmp= eatc-donation_manager_code,eatc_closer_expiration_date,eatc-state, eatc_state2 &#160; &#160; 
&#160; 
 Dado que no se obtiene una respuesta válida entonces el sistema despliega la respuesta&#58; 
 &#160; 
 fail 
 err_msg&#58; invalid dona 
&#160; 
&#160; 
 3. VALIDACIÓN DEL ESTADO, CONDICIÓN Y CONFIGURACIÓN COMO DONANTE (PARA ADMON DEL HUB DE DISTRIBUCIÓN) DEL GESTOR DE DONACIONES 
&#160; 
 3.1. Estado y condición del gestor de donaciones 
El gestor de donaciones que opera el hub, debe estar activo y configurado como hub de distribución, por lo tanto el sistema debe realizar la siguiente validación. 
&#160; 
 Con el dato que llega en los parámetros de la anterior consulta&#58; 
 eatc_dona_headers. eatc-donation_manager_code 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-state= activo &amp;eatc_dist_hub= y 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
&#160; 
 fail 
 err_msg&#58; invalid doma 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación. 

&#160; 
 Ejemplo 1&#58; entorno de producción, eatc_dona_headers. eatc-donation_manager_code &#58; &quot; 811018073 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev beneficiarios .eatcloud.info/api/abaco/eatc_donation_managers? identificador_unico_registro =811018073&amp;eatc-state=activo&amp;eatc_dist_hub=y &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 

&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_headers. eatc-donation_manager_code &#58; &quot; 811000384 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev beneficiarios .eatcloud.info/api/abaco/eatc_donation_managers? identificador_unico_registro =811000384&amp;eatc-state=activo&amp;eatc_dist_hub=y &#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 fail 
 err_msg&#58; invalid doma 

&#160; 
 3.2. Validación de la configuración del gestor de donaciones como donante (para administración del hub de distribución) 
El gestor de un hub de donación debe tener un onboarding en la plataforma como donante, dado que administrará distribuciones desde los hubs, que para efecto de la plataforma son “puntos de donación”. &#160;Por lo tanto deberá hacer las siguientes comprobaciones&#58; 
&#160; 
 Con el dato que llega en los parámetros de la anterior consulta&#58; 
&#160; 
 eatc_dona_headers. eatc-donation_manager_code 
&#160; 
 El sistema deberá validar que el gestor de donaciones esté configurado también como &quot;donante&quot;, de tal manera que pueda gestionar las distribuciones desde la WAPP, realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;fielddecrypt=eatc_cua 
&#160; 
 El sistema guarda el valor (desencriptado) obtenido en &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; (que corresponde al nombre de la cua_user que ha sido asignado al gestor de donaciones que administra un hub de distribución). 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
&#160; 
 fail 
 err_msg&#58; invalid doma configuration for hub admin 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación. 

&#160; 
 Ejemplo 1&#58; entorno productivo, eatc_dona_headers. eatc-donation_manager_code &#58; &quot; 900082682 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=900082682&amp;fielddecrypt=eatc_cua &#160; &#160; 
&#160; 
 El sistema guarda el valor &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125;= fubam para utilizarlo más adelante en el proceso (dado que el registro de kardex debe indicar que el mismo “pertence” al “gestor del hub” y por eso este parámetro se utiliza para eso) 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante . 

&#160; 
 Ejemplo 2&#58; entorno productivo, eatc_dona_headers. eatc-donation_manager_code &#58; &quot; 811000387 &quot; 
&#160; 
 EEl sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=811000387&amp;fielddecrypt=eatc_cua &#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 fail 
 err_msg&#58; invalid doma configuration for distribution hub admin 

 4. VALIDACIÓN DE FECHAS DE VENCIMIENTO PARA DETERMINAR SI UNA DONACIÓN SE PUEDE REDISTRIBUIR ( IMPLEMENTACIÓN EN SEGUNDA ETAPA ) 
 Nota importante para este desarrollo &#58; en una segunda etapa se analizarán posibles restricciones ante registros válidos en fecha de vencimiento más próxima.&#160; Por el momento en la implementación inicial no se deberán implementar estas validaciones. 

 5. FLUJO DE PROCESO DE TRANSFORMACIÓN DE DONACIONES EN REGISTRO DE KARDEX 
&#160; 
 5.1. Consulta de datos de la donación a registrar en el kardex 
 Se realizan dos consultas diferenciadas, ya que si no llegan datos en el llamado al API de , se entiende que todos los detalles de la donación, serán convertidos en registros del kardex, a no ser de que hallan sido previamente distribuidos.&#160; Si por el contrario llegan datos en eatc_odd_id, solamente se distribuirán elementos específicos dentro de la donación y por lo tanto la consulta varía (en especificidad). 
&#160; 
 5.1.1. Cuando no llegan datos en eatc_odd_id y eatc_odd_quantity 
 Dado que el envío de los datos eatc_odd_id y eatc_odd_quantity son opcionales en el llamado al API Pública respectiva , podrá darse el siguiente caso&#58; 
&#160; 
 Con los datos que llegan en los parámetros&#58; 
 cua_master 
 eatc_dona_header_code 
&#160; 
 Y si no llegan datos en&#160; 
 eatc_odd_id &#160; 
 eatc_odd_quantity 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code =&#123;&#123; eatc_dona_header_code &#125;&#125;&amp; eatc_state2= ! distributed &amp;_cmp= eatc-dona_header_code,eatc-doc,eatc-odd_id,eatc-odd_code,eatc-odd_name, eatc-odd_quantity,eatc_odd_available_quantity ,eatc-odd_unit_weight_kg,eatc-odd_unit_cost,eatc-VAT_percentage,origin_odds_typology_a,origin_odds_typology_b,origin_odds_typology_c,eatc-odd_typology_a,eatc-odd_typology_b,eatc-odd_typology_c,eatc-odd_external_code,eatc-pod_id,eatc_donor,eatc-provider_id,eatc-return_cause_code,eatc-return_cause,eatc-contains_alergens,eatc-closer_expiration_date,eatc_lote, eatc_state2 
&#160; 
 Con los datos recibidos se procede a realizar (por cada producto contenido en el anuncio) el respectivo registro en el kardex. 

&#160; 
 5.1.2. Cuando no llegan datos en eatc_odd_quantity o llegan datos completos en la llamada al API 
 Dado que el envío de los datos eatc_odd_id y eatc_odd_quantity son opcionales en el llamado al API Pública respectiva , podrá darse el siguiente caso&#58; 
&#160; 
 Con los datos que llegan en los parámetros&#58; 
 cua_master 
 eatc_dona_header_code 
 eatc_odd_id 
&#160; 
 Y si no llegan datos en&#160; 
 eatc_odd_quantity 
&#160; 
 O llegan los parámetros completos 
 cua_master 
 eatc_dona_header_code 
 eatc_odd_id &#160; 
 eatc_odd_quantity 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code =&#123;&#123; eatc_dona_header_code &#125;&#125; &amp; eatc-odd_id = &#123;&#123; eatc_odd_id &#125;&#125;&amp; eatc_state2= ! distributed &amp;_cmp= eatc-dona_header_code,eatc-doc,eatc-odd_id,eatc-odd_code,eatc-odd_name, eatc-odd_quantity,eatc_odd_available_quantity ,eatc-odd_unit_weight_kg,eatc-odd_unit_cost,eatc-VAT_percentage,origin_odds_typology_a,origin_odds_typology_b,origin_odds_typology_c,eatc-odd_typology_a,eatc-odd_typology_b,eatc-odd_typology_c,eatc-odd_external_code,eatc-pod_id,eatc_donor,eatc-provider_id,eatc-return_cause_code,eatc-return_cause,eatc-contains_alergens,eatc-closer_expiration_date,eatc_lote, eatc_state2 
&#160; 
 Con los datos recibidos se procede a realizar el registro de inventario, bien sea si no se especificaron cantidades , o si se se especificaron cantidades en el llamado al API pública. 

&#160; 
 5.2. REGISTRO DE INVENTARIO 
&#160; 
 Para registrar el inventario se utilizan dos tipos de llamados diferentes, diferenciados principalmente por la cantidad que se lleva al registro del kardex ().&#160; En el primer caso, cuando en el llamado del API pública no se envía el parámetro correspondiente a la cantidad del artículo a distribuir (), la c 
&#160; 
 5.2.1. Determinación del stock previo y de acuerdo a registros previos en el kardex (stock actual más reciente) ***NUEVO&#58; se separan kardex por cua_user correspondiente al gestor de hubs *** 
 El sistema, con los datos &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; (obtenido en el proceso de validación del gestor de donaciones como donante ), &#123;&#123;eatc_dona .eatc_donor &#125;&#125; y &#123;&#123;eatc_dona .eatc-odd_id &#125;&#125; realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; / eatc_kardex ?eatc_donor= &#123;&#123;eatc_dona .eatc_donor &#125;&#125; &amp;eatc_odd_id= &#123;&#123;eatc_dona .eatc-odd_id &#125;&#125; &amp;_cmp= eatc_date_time, eatc_act_stock 
 En vez de tener un kardex por cuenta maestra (como estaba anteriormente y se muestra a continuación), se tienen kardex por cua_user correspondiente al gestor de donaciones que administra el hub ( &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; ), esto con el objetivo de poder controlar el inventario para cada administrador del hub y no tener un kardex global que pueda mezclar inventarios de varios gestores de donaciones administradores de hubs 
&#160; 
 Anteriormente&#58;&#160; 

 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master&#125;&#125;/ eatc_kardex ?eatc_donor=&#123;&#123;eatc_dona .eatc_donor &#125;&#125;&amp;eatc_odd_id=&#123;&#123;eatc_dona .eatc-odd_id &#125;&#125;&amp;_cmp= eatc_date_time,eatc_act_stock 
&#160; 
 Si no se obtiene respuesta, entonces se tomará que&#160; 
 eatc_prev_stock_value = 0 
&#160; 
 Si ese obtiene una respuesta única entonces 
 eatc_prev_stock_value =&#123;&#123; eatc_kardex . eatc_act_stock &#125;&#125; 
&#160; 
 Si se obtienen varias respuestas , el sistema deberá determinar el registro más reciente (según el valor recibido en &#123;&#123; eatc_kardex . eatc_date_time &#125;&#125; y ese será el valor que tomará el sistema para el registro 
 eatc_prev_stock_value =&#123;&#123; eatc_kardex . eatc_act_stock &#125;&#125; más_reciente 

&#160; 
 5.2. 2. Registro de inventario cuando no se especifican productos ni cantidades o&#160; no se especifican cantidades 
 Nota al desarrollador&#58; encerrados en tres asteríscos ( *** ) y de color café (ejempo&#58; ***comentario*** ) se entregan explicaciones para entender la variable, constante o fórmula que se lleva al valor del registro. 
&#160; 
 Determinación del valor a llevar en la cantidad ( eatc_odd_quantity ) 
&#160; 
 Si en la respuesta del llamado para traer los datos del detalle de la donación encontramos que&#58; 
 eatc_dona.eatc_state2=partially_distributed 
&#160; 
 Entonces el sistema definirá que&#160; 
 eatc_odd_quantity_value = &#123;&#123;eatc_dona . eatc_odd_available_quantity &#125;&#125; 

&#160; 
 En caso contrario, si en el valor del parámetro en cuestión, no hay un registro, no existe el campo, está nulo o vacío, o en cero y es diferente a partiallly_distributed (y por también a distributed). 
 eatc_dona.eatc_state2= _nin_ partially_distributed,distributed 
&#160; 
 Entonces el sistema definirá que&#160; 
 eatc_odd_quantity_value = &#123;&#123;eatc_dona .eatc-odd_quantity &#125;&#125; 

&#160; 
 Parámetros de invocación del CRD &#123;&#123;param_ins_kardex&#125;&#125; 
 eatc_date_time= &#123;&#123; datetime_stamp &#125;&#125; ***en formato AAAA-MM-DD HH&#58;MM&#58;SS con la fecha y hora de la invocación del CRD *** 
 eatc_date= &#123;&#123; date_stamp &#125;&#125; ***en formato AAAA-MM-DD con la fecha de la invocación del CRD *** 
 eatc_transaction_type = input ***Constante &quot; input&quot; que queiere decir que el registro es una entrada de inventario *** 
 eatc_cua_origen= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; **Valor que se obtiene en la validación de configuración* ** 
 eatc_donor = &#123;&#123;eatc_dona .eatc_donor &#125;&#125; 
 eatc_dona_header_code= &#123;&#123;eatc_dona .eatc-dona_header_code &#125;&#125; 
 eatc_doc= &#123;&#123;eatc_dona .eatc-doc &#125;&#125; 
 eatc_odd_id= &#123;&#123;eatc_dona .eatc-odd_id &#125;&#125; 
 eatc_odd_code= &#123;&#123;eatc_dona .eatc-odd_code &#125;&#125; 
 eatc_odd_name= &#123;&#123;eatc_dona .eatc-odd_name &#125;&#125; 
 eatc_odd_quantity= &#123;&#123; eatc_odd_quantity_value &#125;&#125; ***Establecido en el paso previo *** 
 eatc_prev_stock= &#123;&#123; eatc_prev_stock_value &#125;&#125; ***Consultado en paso previo *** 
 eatc_act_stock= &#123;&#123; &#123;&#123; eatc_prev_stock_value &#125;&#125; + &#123;&#123; eatc_odd_quantity_value &#125;&#125; &#125;&#125; ***Al stock previo se le suman las cantidades a distribuir*** 
 eatc_odd_unit_weight_kg= &#123;&#123;eatc_dona .eatc-odd_unit_weight_kg &#125;&#125; 
 eatc_odd_unit_cost= &#123;&#123;eatc_dona .eatc-odd_unit_cost &#125;&#125; 
 eatc_VAT_percentage= &#123;&#123;eatc_dona .eatc-VAT_percentage &#125;&#125; 
 origin_odds_typology_a= &#123;&#123;eatc_dona .origin_odds_typology_a &#125;&#125; 
 origin_odds_typology_b= &#123;&#123;eatc_dona .origin_odds_typology_b &#125;&#125; 
 origin_odds_typology_c= &#123;&#123;eatc_dona .origin_odds_typology_c &#125;&#125; 
 eatc_odd_typology_a= &#123;&#123;eatc_dona .eatc-odd_typology_a &#125;&#125; 
 eatc_odd_typology_b= &#123;&#123;eatc_dona .eatc-odd_typology_b &#125;&#125; 
 eatc_odd_typology_c= &#123;&#123;eatc_dona .eatc-odd_typology_c &#125;&#125; 
 eatc_odd_external_code= &#123;&#123;eatc_dona .eatc-odd_external_code &#125;&#125; 
 eatc_pod_id= &#123;&#123;eatc_dona .eatc-pod_id &#125;&#125; 
 eatc_provider_id= &#123;&#123;eatc_dona .eatc-provider_id &#125;&#125; 
 eatc_return_cause_code= &#123;&#123;eatc_dona .eatc-return_cause_code &#125;&#125; 
 eatc_return_cause= &#123;&#123;eatc_dona .eatc-return_cause &#125;&#125; 
 eatc_contains_alergens= &#123;&#123;eatc_dona .eatc-contains_alergens &#125;&#125; 
 eatc_closer_expiration_date= &#123;&#123;eatc_dona .eatc-closer_expiration_date &#125;&#125; 
 eatc_lote= &#123;&#123;eatc_dona .eatc_lote &#125;&#125; 
 eatc_user =&#123;&#123;eatc_user&#125;&#125; *** parámetro de invocación del servicio mediante el API pública*** 
 , 
&#160; 
 5.2.3. Cuando llegan todos los valores de la invocación del API 
&#160; 
 Parámetros de invocación del CRD &#123;&#123;param_ins_kardex&#125;&#125; 
 eatc_date_time= &#123;&#123; datetime_stamp en formato AAAA-MM-DD HH&#58;MM&#58;SS con la fecha y hora de la invocación del CRD &#125;&#125; 
 eatc_date= &#123;&#123; date_stamp en formato AAAA-MM-DD con la fecha de la invocación del CRD &#125;&#125; 
 eatc_transaction_type = input ***Constante &quot; input&quot; que queiere decir que el registro es una entrada de inventario *** 
 eatc_cua_origen= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; **Valor que se obtiene en la validación de configuración* ** 
 eatc_donor = &#123;&#123;eatc_dona .eatc_donor &#125;&#125; 
 eatc_dona_header_code= &#123;&#123;eatc_dona .eatc-dona_header_code &#125;&#125; 
 eatc_doc= &#123;&#123;eatc_dona .eatc-doc &#125;&#125; 
 eatc_odd_id= &#123;&#123;eatc_dona .eatc-odd_id &#125;&#125; 
 eatc_odd_code= &#123;&#123;eatc_dona .eatc-odd_code &#125;&#125; 
 eatc_odd_name= &#123;&#123;eatc_dona .eatc-odd_name &#125;&#125; 
 eatc_odd_quantity = &#123;&#123;eatc_odd_quantity&#125;&#125;&#160; ***Valor que llega en el llamado al API pública, validando que el dato que llega&#123;&#123;eatc_odd_quantity&#125;&#125; sea menor o igual el registro obtenido en &#123;&#123;eatc_dona .eatc-odd_quantity &#125;&#125; o en &#123;&#123;eatc_dona . eatc_odd_available_quantity &#125;&#125;, según sea el caso ( eatc_dona. eatc_state2 =partially_distributed o eatc_dona. eatc_state2 = _nin_ partially_distributed,distributed respectivamente) , Si en la invocación del servicio llega un valor mayor, entonces se llevará al registro &#123;&#123;eatc_dona .eatc-odd_quantity &#125;&#125; o &#123;&#123;eatc_dona . eatc_odd_available_quantity &#125;&#125; según sea el caso*** 
 eatc_prev_stock= &#123;&#123; eatc_prev_stock_value &#125;&#125; ***Consultado en el paso previo *** 
 eatc_act_stock= &#123;&#123; &#123;&#123; eatc_prev_stock_value + &#123;&#123;eatc_dona .eatc-odd_quantity &#125;&#125; &#125;&#125; ***Al stock previo se le suman las cantidades a distribuir*** 
 eatc_odd_unit_weight_kg= &#123;&#123;eatc_dona .eatc-odd_unit_weight_kg &#125;&#125; 
 eatc_odd_unit_cost= &#123;&#123;eatc_dona .eatc-odd_unit_cost &#125;&#125; 
 eatc_VAT_percentage= &#123;&#123;eatc_dona .eatc-VAT_percentage &#125;&#125; 
 origin_odds_typology_a= &#123;&#123;eatc_dona .origin_odds_typology_a &#125;&#125; 
 origin_odds_typology_b= &#123;&#123;eatc_dona .origin_odds_typology_b &#125;&#125; 
 origin_odds_typology_c= &#123;&#123;eatc_dona .origin_odds_typology_c &#125;&#125; 
 eatc_odd_typology_a= &#123;&#123;eatc_dona .eatc-odd_typology_a &#125;&#125; 
 eatc_odd_typology_b= &#123;&#123;eatc_dona .eatc-odd_typology_b &#125;&#125; 
 eatc_odd_typology_c= &#123;&#123;eatc_dona .eatc-odd_typology_c &#125;&#125; 
 eatc_odd_external_code= &#123;&#123;eatc_dona .eatc-odd_external_code &#125;&#125; 
 eatc_pod_id= &#123;&#123;eatc_dona .eatc-pod_id &#125;&#125; 
 eatc_provider_id= &#123;&#123;eatc_dona .eatc-provider_id &#125;&#125; 
 eatc_return_cause_code= &#123;&#123;eatc_dona .eatc-return_cause_code &#125;&#125; 
 eatc_return_cause= &#123;&#123;eatc_dona .eatc-return_cause &#125;&#125; 
 eatc_contains_alergens= &#123;&#123;eatc_dona .eatc-contains_alergens &#125;&#125; 
 eatc_closer_expiration_date= &#123;&#123;eatc_dona .eatc-closer_expiration_date &#125;&#125; 
 eatc_lote= &#123;&#123;eatc_dona .eatc_lote &#125;&#125; 
 eatc_user =&#123;&#123;eatc_user&#125;&#125; *** parámetro de invocación del servicio mediante el API pública*** 
 , 
&#160; 
 5.3. Escritura con el CRD ***NUEVO&#58; se separan kardex por cua_user correspondiente al gestor de hubs *** 
 Con los parámetros obtenidos se realiza la siguiente escritura&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; /?_tabla= eatc_kardex &amp;_operacion=insert&amp; &#123;&#123;param_ins_kardex&#125;&#125; 
 En vez de tener un kardex por cuenta maestra (como estaba anteriormente y se muestra a continuación), se tienen kardex por cua_user correspondiente al gestor de donaciones que administra el hub ( &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; ), esto con el objetivo de poder controlar el inventario para cada administrador del hub y no tener un kardex global que pueda mezclar inventarios de varios gestores de donaciones administradores de hubs 
&#160; 
 Anteriormente&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master&#125;&#125;/?_tabla= eatc_kardex &amp;_operacion=insert&amp; &#123;&#123;param_ins_kardex&#125;&#125; 

&#160; 
&#160; 
 6. ACTUALIZACIÓN DE DATOS DE LA DONACIÓN DISTRIBUÍDA 
&#160; 
 Actualización de eatc_estado2 en datos del encabezado 
&#160; 
 Cuando se realizó una distribución total (Registro de inventario cuando no se especifican productos ni cantidades ) 
 Dado que al no especificar productos ni cantidades en el llamado al API pública, se entiende que todo el anuncio fue distribuído, entonces se procede a realizar el siguiente llamado para marcarlo como tal ( eatc_state2= distributed ) 
&#160; 
 Update eatc_dona_headers con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_headers &amp;_operacion= update &amp; eatc_state2= distributed &amp;WHEREeatc-code= &#123;&#123; eatc_dona_header_code &#125;&#125; ** 
&#160; 
 ** eatc_dona_header_code&#58; Parámetro de invocación del servicio donatokardex a través del API pública 
&#160; 
 Cuando se realizó una distribución parcial (Registro de inventario cuando se especifican productos ó&#160; productos y cantidades ) 
&#160; 
 Cuando se especifican productos de una donación en el llamado al servicio, se establece que la donación fue parcialmente distribuída, y por lo tanto se realiza el registro respectivo ( eatc_state2=partially_ distributed ) 
&#160; 
 Update eatc_dona_headers con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_headers &amp;_operacion= update &amp; eatc_state2=partially_ distributed &amp;WHEREeatc-code= &#123;&#123; eatc_dona_header_code &#125;&#125; ** 
&#160; 
 ** Parámetro de invocación del servicio donatokardex a través del API pública 

&#160; 
 Actualización de eatc_estado2 en datos del detalle de donaciones ( eatc_dona ) 
 Cuando se realizó una distribución total (Registro de inventario cuando no se especifican productos ni cantidades ) 
&#160; 
 Dado que todos los productos de la donación en cuestión, al no especificarse ni productos ni cantidades, quedan totalmente distribuídos, la actualización se puede hacer por el parámetro eatc-dona_header_code (WHEREeatc-dona_header_code= &#123;&#123; eatc_dona_header_code &#125;&#125; ***Parámetro de invocación del servicio donatokardex a través del API pública*** ) 
&#160; 
 Update eatc_dona con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona &amp;_operacion= update &amp; eatc_state2= distributed &amp;WHEREeatc-dona_header_code= &#123;&#123; eatc_dona_header_code &#125;&#125; &#160; 

&#160; 
 Cuando se realizó una distribución parcial (Registro de inventario cuando se especifican productos , sin cantidades ) 
 Dado que los cuando se especifican productos&#160; quiere decir que solamente productos específicos de una donación son distribuidos y al no especificar cantidades, se establece que estos productos específicos serán distribuidos en su totalidad. Y dado que para definir esos productos específicos dentro de una donación, no se podrá utilizar solamente el código de encabezado de donación ( &#123;&#123; eatc_dona_header_code &#125;&#125; ***Parámetro de invocación del servicio donatokardex a través del API pública*** ), se deberá utilizar el servicio UPDATEPLUS , que permite enviar varios parámetros para realizar un query cruzado y así establecer una actualización particular, por la dupla &#123;&#123; eatc_dona_header_code &#125;&#125;,&#123;&#123; eatc_odd_id &#125;&#125; ambos parámetros presentes en la invocación del servicio a través del API pública . 

&#160; 
 Update eatc_dona con el servicio UPDATEPLUS 
&#160; 
 Endpoint&#58; &#123;&#123; URL_donantes &#125;&#125;crd/&#123;&#123; cua_master &#125;&#125; 
 Método&#58; POST 
&#160; 
 Parámetros en el body&#58;&#160; 
&#160; 
 &#123; 
 &#160;&#160;&#160; &quot;_tabla&quot;&#58; &quot;eatc_dona&quot;, 
 &#160;&#160;&#160; &quot;_operacion&quot;&#58; &quot;updateplus&quot;, 
 &#160;&#160;&#160; &quot;WHERE&quot;&#58; &quot;eatc-dona_header_code,eatc-odd_id&quot;, 
 &#160;&#160;&#160; &quot;_data&quot;&#58;[ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc_state2&quot;&#58; &quot; distributed &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc-dona_header_code&quot;&#58; &quot; &#123;&#123;eatc_dona_header_code&#125;&#125; &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc-odd_id&quot;&#58; &quot; &#123;&#123;eatc_odd_id&#125;&#125; &quot; 
 &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#125; 
 &#160;&#160;&#160;&#160;] 
 &#125; 

&#160; 
 Cuando se realizó una distribución parcial (Registro de inventario cuando se especifican productos , y cantidades ) 
 Dado que los cuando se especifican productos&#160; y cantidades quiere decir que solamente una porción de los productos productos específicos de una donación son distribuidos , y dado que para definir esos productos específicos dentro de una donación, no se podrá utilizar solamente el código de encabezado de donación ( &#123;&#123; eatc_dona_header_code &#125;&#125; ***Parámetro de invocación del servicio donatokardex a través del API pública*** ), se deberá utilizar el servicio UPDATEPLUS , que permite enviar varios parámetros para realizar un query cruzado y así establecer una actualización particular, por la dupla &#123;&#123; eatc_dona_header_code &#125;&#125;,&#123;&#123; eatc_odd_id &#125;&#125; ambos parámetros presentes en la invocación del servicio a través del API pública .&#160; 
&#160; 
 En este caso también deberá establecerse el valor de la cantidad disponible para el producto, después de la distribución, restando al valor disponible actual, la cantidad que se recibe por el llamado al API pública ( &#123;&#123; eatc_odd_quantity &#125;&#125; ), y esto se realiza de la siguiente manera&#58; 
&#160; 
 Si no existe registro en eatc_odd_available_quantity 
 eatc_odd_available_quantity_value = &#123;&#123;eatc_dona .eatc-odd_quantity &#125;&#125; - &#123;&#123; eatc_odd_quantity &#125;&#125; 
 Si existe registro en eatc_odd_available_quantity 
 eatc_odd_available_quantity_value = &#123;&#123;eatc_dona .eatc_odd_available_quantity &#125;&#125; - &#123;&#123; eatc_odd_quantity &#125;&#125; 
&#160; 
 Teniendo estos valores entonces se procede a realizar la actualización de información 
 Update eatc_dona con el servicio UPDATEPLUS 
&#160; 
 Endpoint&#58; &#123;&#123; URL_donantes &#125;&#125;crd/&#123;&#123; cua_master &#125;&#125; 
 Método&#58; POST 
&#160; 
 Parámetros en el body&#58;&#160; 
&#160; 
 &#123; 
 &#160;&#160;&#160; &quot;_tabla&quot;&#58; &quot;eatc_dona&quot;, 
 &#160;&#160;&#160; &quot;_operacion&quot;&#58; &quot;updateplus&quot;, 
 &#160;&#160;&#160; &quot;WHERE&quot;&#58; &quot;eatc-dona_header_code,eatc-odd_id&quot;, 
 &#160;&#160;&#160; &quot;_data&quot;&#58;[ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc_state2&quot;&#58; &quot; partially_ distributed &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; &quot;eatc_odd_available_quantity&quot;&#58; &quot;&#123;&#123; eatc_odd_available_quantity_value &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc-dona_header_code&quot;&#58; &quot; &#123;&#123;eatc_dona_header_code&#125;&#125; &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;eatc-odd_id&quot;&#58; &quot; &#123;&#123;eatc_odd_id&#125;&#125; &quot; 
 &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#125; 
 &#160;&#160;&#160;&#160;] 
 &#125; 

&#160; 
 Escritura en el historial de estados de la donación que fue distribuida. 
 &#123;&#123; parámetros_insert_CRD &#125;&#125; 
 eatc_dona_header_code=&#123;&#123; eatc_dona_header_code &#125;&#125; ***parámetro de invocación del servicio*** 
 eatc-state = &#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; 
 eatc-date_time =&#123;&#123; timestamp &#125;&#125; &#160; *** Fecha y hora en la cual se cambia el estado de la donación (es decir la fecha y la hora en que corre el presente proceso)*** 
 eatc-log = &#123;&#123; eatc_dona_headers. eatc-state2 &#125;&#125; ***después de la actualización de los datos del encabezado de donación *** 
 eatc_doma_id = &#123;&#123; eatc_dona_headers. eatc-donation_manager_code &#125;&#125; 
 Otros parámetros utilizados en el llamado&#58; 
 cua_master = &#123;&#123; cua_master &#125;&#125; ***parámetro de invocación del servicio*** 

&#160; 
 Inserción en eatc_dona_header_state_history con el CRD 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla= eatc_dona_header_state_history &amp;_operacion= insert &amp; &#123;&#123; parámetros_insert_CRD &#125;&#125; 

 7. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
 Si las actualizaciones de información realizadas por el servicio se realizan de manera adecuada, entonces entregará la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 DONATOKARDEX: SERVICIO PARA CONVERTIR DONACIONES RECIBIDAS EN REGISTROS DE KARDEX