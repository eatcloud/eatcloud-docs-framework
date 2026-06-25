# verificación-detallada-anuncio-de-donación-eatc_dona_ver.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Corresponde a una verificación de todas las referencias del anuncio de donación. Se efectúa en el punto de entrega (fundación o banco) solo para anuncios de donación con estado &quot;entregados&quot; y para ello se toman los detalles de la donación (eatc_dona) y se realiza un inventario ciego de los mismos . Si hay inconsistencia entre las cantidades consignadas en el anuncio y la donación recibida (inventario ciego) el sistema debe disponer de formularios de captura para capturar y documentar las inconsistencias y&#160; generar una alarma a la instancia responsable. Cuando se termina el proceso de revisión el anuncio de donación (eatc_dona_headers) cambia a estado &quot;recibido&quot; y se actualiza la información respectiva&#160; 

 Encabezado del listado de eatc-odd_id 
 El listado de eatc-odd_id debe tener el siguiente encabezado&#58;&#160; 
&#160; 
 Verificar contenido de la donación&#160; 
&#160; 
 Por favor verifica al desempacar tu donación que esté completa, en buen estado y apta para el consumo humano. 
&#160; 
 Consulta para traer los datos 
 Para consultar los detalles a verificar se debe realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code = &#123;&#123;eatc-code&#125;&#125; 
&#160; 
 ***NUEVO&#58; consulta del estado del ítem (según nuevo proceso de chequeo ) para validaciones en el formulario *** 
 Nota para el presente ajuste &#58; El funcionamiento del formulario como se tiene implementado, debe mantenerse, incluyendo los registros en las diversas estructuras de datos. 
&#160; 
 Se debe realizar la siguiente consulta para determinar el eatc-odd_state de cada ítem a verificar y realizar validaciones posteriores.&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code = &#123;&#123;eatc-code&#125;&#125;&amp;_cmd= eatc-odd_state, eatc-odd_id,eatc-odd_original_quantity,eatc-odd_quantity 

 Si para un ítem la respuesta de la consulta&#160; el parámetro eatc_dona. eatc-odd_state es 
&#160; 
 Vacía, nula o cero 
 rechazado 
&#160; 
 Quiere decir que la donación fue chequeada adecuadamente, o fue chequeada con una versión anterior al nuevo proceso de chequeo , y por lo tanto el formulario debe funcionar tal cual funciona hasta ahora . 
&#160; 
 Si para un ítem la respuesta de la consulta es&#58; 
 rechazo_parcial 
&#160; 
 Entonces la App debe realizar las siguientes acciones y validaciones en el formulario de verificación detallada&#58; 

&#160; 
 ***NUEVO &#58; acciones y validaciones ante un rechazo_parcial ( eatc-odd_state= rechazo_parcial ) *** 
 El formulario en la casilla de cantidades no debe traer el dato de las cantidades anunciadas, sino que debe dejar vacío el campo de captura. 
 El sistema debe validar que la cantidad en el campo de captura sea menor a la cantidad del anuncio. 
 Si el usuario en el campo de captura (que influye en eatc_dona. eatc-odd_quantity ) incorpora un valor igual o mayor a la cantidad anunciada originalmente ( eatc_dona. eatc-odd_original_quantity ) entonces deberá desplegar una ventana de confirmación de las siguientes características&#58; 

&#160; 
 label&#58; class=&quot;lbl_rechazo_parcial_chk_no_tenido_en_cuenta_verf&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_rechazo_parcial_chk_no_tenido_en_cuenta_verf )&#160; 
&#160; 
 &quot;La cantidad registrada no corresponde al rechazo parcial informado en el proceso de chequeo. Deseas que dicha cantidad sea&#58;&quot; 
&#160; 
 Botones de confirmación o corrección&#58; 
 Corregida&quot; label&#58; class=&quot;lbl_corregida&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_corregida )&#160; =&gt; Lógica semáforo Verde 
&#160; 
 Al seleccionar esta opción se debe limpiar el formulario en donde se ingresa la cantidad del Ítem, para que el usuario ingrese una nueva cantidad (que debe ser menor a eatc_dona. eatc-odd_original_quantity ) 

&#160; 
 &quot;Confirmada&quot; label&#58; class=&quot;lbl_confirmada&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_confirmada ) =&gt; Lógica semáforo Roja 
&#160; 
 Al accionar este botón el registro de la cantidad prosigue con la cantidad digitada en el formulario 

&#160; 
 Si para un ítem la respuesta de la consulta es&#58; 
 rechazo_total 
&#160; 
 Entonces la App debe realizar las siguientes acciones y validaciones en el formulario de verificación detallada&#58; 
&#160; 
 ***NUEVO &#58; acciones y validaciones ante un rechazo_total ( eatc-odd_state= rechazo_total ) *** 
 El formulario en la casilla de cantidades debe colocarse el valor &quot;0&quot; (promoviendo la captura de los causales de rechazo para todas las cantidades anuniadas). 
 El sistema debe validar que la cantidad en el campo de captura sea igual a &quot;0&quot;. 
 Si el usuario en el campo de captura (que influye en eatc_dona. eatc-odd_quantity ) incorpora un valor diferente a cero (0) entonces deberá desplegar una ventana de confirmación de las siguientes características&#58; 

&#160; 
 label&#58; class=&quot;lbl_rechazo_total_chk_no_tenido_en_cuenta_verf&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_rechazo_total_chk_no_tenido_en_cuenta_verf )&#160;&#160; 
&#160; 
 &quot;La cantidad registrada no corresponde al rechazo total informado en el proceso de chequeo. Deseas que dicha cantidad sea&#58;&quot; 
&#160; 
 Botones de confirmación o corrección&#58; 
 Corregida&quot; label&#58; class=&quot;lbl_corregida&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_corregida )&#160; =&gt; Lógica semáforo Verde 
&#160; 
 Al seleccionar esta opción se debe colocar &quot;0&quot; en el formulario y promover la captura del de los causales de rechazo por la totalidad de las unidades anunciadas. 

&#160; 
 &quot;Confirmada&quot; label&#58; class=&quot;lbl_confirmada&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_confirmada ) =&gt; Lógica semáforo Roja 
&#160; 
 Al accionar este botón el registro de la cantidad prosigue con la cantidad digitada en el formulario 
&#160; 
 ***NUEVO&#58; Selector del tipo de verificación *** 
 El sistema deberá desplegar un selector único que contiene las siguientes opciones&#58; 
&#160; 

 Verificación por cantidades 
 label&#58; class= &quot;lbl_verificacion_cantidades&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_verificacion_cantidades )&#160; 
&#160; 
 Selección por defecto (si se cambia al otro valor del selector, se debe cambiar también a ese valor por defecto).&#160; Da ingreso al formulario de verificación por cantidades , o formulario tradicional de verificación (el que se implementó originalmente y que debe preservarse). 

&#160; 

 Verificación por pesos&quot;&#160; 
 label&#58; class= &quot;lbl_verificacion_pesos&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_verificacion_pesos )&#160; 
&#160; 
 Da ingreso al nuevo formulario de verificación por pesos .&#160; Si se selecciona esta opción, deberá quedar como valor por defecto para que cuando se vuelva a entrar a la funcionalidad se despliegue este nuevo formulario 

&#160; 
 F ORMULARIO DE VERIFICACIÓN POR CANTIDADES (VERIFICACIÓN TRADICIONAL) 
 El sistema arroja un listado completo de referencias (eatc-odd_id) contenido en el detalle del anuncio de donación (eatc-dona) mostrando para cada una de las referencias, su nombre ( eatc-odd_name ) y su código ( eatc-odd_id ). &#160; Se debe excluir del listado aquellas referencias que tengan estado ( eatc-odd_state) &quot;rechazado&quot;. 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente productivo&#58; 
&#160; 
 El para el anuncio cuyo &quot; eatc-code &quot; = 40716 ( anuncio cuyo &quot; eatc-id &quot; = 7608059 ) (Carulla Palmas&#58; user &#58; 339; password &#58; (4) 6050294) 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716&amp;_compress &#160; 
&#160; 
 El sistema debe generar un listado de 15 productos, ya que el API trae 16 productos pero uno de ellos tiene estado ( eatc-odd_state) &quot; rechazado&quot; 
&#160; 
 Se debe implementar un buscador de productos (por nombre) para filtrar los elementos del listado. 
&#160; 
 Al frente de cada referencia haber un formulario de captura de unidades presentes en el anuncio (OJO QUE DIFIERE DE LO PRESENTADO EN EL DISEÑO&#58; DICHO DISEÑO SUGIERE QUE SE CAPTURAN KILOGRAMOS Y NO UNIDADES,&#160; Y EL SISTEMA SIEMPRE DEBE CAPTURAR UNIDADES ).&#160;&#160; 
&#160; 
 El sistema debe validar en el acto si las cantidades digitadas corresponden a las cantidades consignadas en el anuncio ( eatc-odd_quantity ).&#160; Si existen diferencias el sistema debe permitir la captura de los motivos de rechazo pudiendo digitar varias unidades por motivo (OJO QUE DIFIERE DEL DISEÑO) y agregar varios motivos. 

&#160; 
 Leyenda al lado del input de cantidades&#58; 
 Para no dar lugar a equívocos, y otorgar total claridad al usuario de las unidades que debe digitar, en ves de &quot;Unid&quot; (a secas, como está en este momento), colocar &quot;Unidades efectivamente recibidas (aptas para el consumo humano)&quot;.&#160; Aunque es muy largo, por problemas detectados en el proceso, se estima conveniente la aclaración. 

&#160; 
 Registro de causales o motivos de rechazo por verificación con cantidades diferentes 
 Si la cantidad digitada por el usuario es menor al dato que tiene el anuncio de donación ( eatc-dona.eatc-odd_quantity ) el sistema debe abrir un formulario realizando los siguientes procesos&#58; 
&#160; 
 Consulta de los causales ***NUEVO &#58; cambio en la consulta para obtener el selector (para registro de sobrantes ) *** 
 Anteriormente se tenían solamente causales de rechazo en el maestro, pero a partir del momento también se registrarán causales de “sobrantes” y se empezará a registrar los sobrantes en la tabla eatc_odd_rejection_registry dada una mejora solicitada por BAMX (en donde se deben notificar tanto sobrantes como faltantes). 
&#160; 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_odd_rejection_causes? rejection_cause = y 
&#160; 
 (Anteriormente&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=_* 
 &#160; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_odd_rejection_cause&amp;code=_todos ) 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_odd_rejection_causes. eatc_label &quot; para construir el selector internacionalizado y de acuerdo a la opción seleccionada se toman los datos &quot; eatc_odd_rejection_causes. nombre &quot; y &quot; eatc_odd_rejection_causes. code &quot; para llevarlos al registro del causal de rechazo&#58; 
&#160; 
 Consulta para determinar si la causal requiere evidencia. ***NUEVO&#58; registro de evidencia *** 
 El sistema deber realizar la siguiente consulta, para determinar si la causal requiere evidencia, el sistema deberá tener en consideración los siguientes parámetros&#58; 
&#160; 
Tipología b del gestor de donaciones &#123;&#123;doma_tipology_b&#125;&#125; 
Tipo de rechazo &#58; parcial (partial) o total (total) &#123;&#123;partial_or_total&#125;&#125; 
&#160; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_odd_rejection_causes ? eatc_label =&#123;&#123; eatc_odd_rejection_causes. eatc_label &#125;&#125;&amp; doma_tipology_b= &#123;&#123;doma_tipology_b&#125;&#125; &amp; rejection_type= &#123;&#123;partial_or_total&#125;&#125; &amp;_cmp= requires_evidence 
Si la consulta no arroja resultados entonces deberá realizar la siguiente consulta (doma_tipology_b= _default ) 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_odd_rejection_causes ? eatc_label =&#123;&#123; eatc_odd_rejection_causes. eatc_label &#125;&#125;&amp; doma_tipology_b= _default &amp; rejection_type= &#123;&#123;partial_or_total&#125;&#125; &amp;_cmp= requires_evidence 
&#160; 
 Si la causal requiere evidencia ( eatc_odd_rejection_causes. requires_evidence = yes ), se debe permitir tomar una foto &#160;( ***NUEVO&#58; no debe permitir seleccionar un archivo *** ) para registrarla como evidencia en el sistema (el sistema validará que el usuario tome la foto cuando se requiere, para completar el proceso de verificación&#58; evidencia obligatoria). 
&#160; 
 Si la causal NO requiere evidencia ( eatc_odd_rejection_causes. requires_evidence = no ), se debe permitir tomar una foto ( ***NUEVO&#58; no debe permitir seleccionar un archivo *** ) para registrarla como evidencia en el sistema, pero dicha acción será opcional. 
&#160; 
 El sistema debe subir el recurso al servidor y guardar registro de la URL &#123;&#123;URL_evidencia&#125;&#125; en donde se puede obtener el recurso en la estructura definida para tal fin (&#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_odd_rejection_registry &#160; campo “ evidence ”) y el anuncio de donación ( eatc_dona campo&#58; “ eatc-odd_rejection_cause ”). 
&#160; 
 Escritura en eatc_odd_rejection_registry con la API ***NUEVO&#58; se registrarán también “sobrantes”. &#160;Se llevará al registro el dato eatc_donor *** 
 Anteriormente solamente se registraban rechazos, pero a partir del momento también se registrarán en la tabla “sobrantes”, unidades que llegan de más y cuyo sobrante se registra en la verificación. 
&#160; 
Cuando se registran faltantes 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla= eatc_odd_rejection_registry &amp;_operacion= insert &amp;date_time= &#123;&#123;DATETIME&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_dona_headers . eatc-donation_manager_code &#125;&#125; &amp;eatc-donation_manager_user_doc_id= &#123;&#123; eatc_dona_headers . eatc-donation_manager_user_doc_id &#125;&#125; &amp;eatc_donor_code= &#123;&#123; eatc_dona_headers . eatc-donor_code &#125;&#125; &amp; eatc_donor =&#123;&#123; eatc_dona_headers . eatc-donor &#125;&#125; &amp;eatc-dona_header_code= &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; &amp;eatc-pod_id= &#123;&#123; eatc_dona_headers . eatc-pod_id &#125;&#125; &amp;eatc-odd_id= &#123;&#123; eatc_dona . eatc-odd_id &#125;&#125; &amp;verification_type= ver &amp;eatc-odd_rejection_cause= &#123;&#123; eatc_odd_rejection_causes .nombre&#125;&#125; &amp;eatc-odd_rejection_cause_id= &#123;&#123; eatc_odd_rejection_causes .code&#125;&#125; &amp;quantity= &#123;&#123;UNIDADES_rechazadas&#125;&#125; &amp;evidence= &#123;&#123;URL_evidencia&#125;&#125; 
Cuando se registra un sobrante entonces el registro será&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla= eatc_odd_rejection_registry &amp;_operacion= insert &amp;date_time= &#123;&#123;DATETIME&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_dona_headers . eatc-donation_manager_code &#125;&#125; &amp;eatc-donation_manager_user_doc_id= &#123;&#123; eatc_dona_headers . eatc-donation_manager_user_doc_id &#125;&#125; &amp;eatc_donor_code= &#123;&#123; eatc_dona_headers . eatc-donor_code &#125;&#125; &amp; eatc_donor =&#123;&#123; eatc_dona_headers . eatc-donor &#125;&#125; &amp;eatc-dona_header_code= &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; &amp;eatc-pod_id= &#123;&#123; eatc_dona_headers . eatc-pod_id &#125;&#125; &amp;eatc-odd_id= &#123;&#123; eatc_dona . eatc-odd_id &#125;&#125; &amp;verification_type= ver &amp;eatc-odd_rejection_cause= sobrante &amp;eatc-odd_rejection_cause_id= 3 &amp;quantity= &#123;&#123;UNIDADES_sobrantes&#125;&#125; &amp;evidence= &#123;&#123;URL_evidencia&#125;&#125; 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente pruebas&#58; 
&#160; 
 Para el anuncio de donación cuyo _id = 77 (y cuyo detalle eatc_dona se consulta aquí ) , El usuario El usuario Juan Carlos Buitrago (numero_cedula = 8161174 ; que tiene como organización el dato&#58; 900326456-1 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456-1 ) realiza la verificación del anuncio de donación. A las 18&#58;00&#58;00 del día 2019-09-26 definiendo mediante los formularios de captura de la App, establece que el artículo &quot;PASTEL DE QUESO&quot; ( eatc-odd_id &#58; &quot;0935419&quot;) tiene un inventario de 2 unidad.&#160; El sistema inmediatamente, al detectar un una diferencia (de 2 unidades) con las cantidades del aununcio ( eatc-odd_quantity &#58; &quot;2&quot;) abre un&#160; selector de motivo (con los datos que se encuentran en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_odd_rejection_causes&amp;eatc_language=es ) 
&#160; 
 El usuario selecciona el motivo &quot;No encontrada&quot; y al frente digita la cantidad 1, el sistema al detectar que aun falta 1 unidad para completar la diferencia de 2 entre el inventario y las cantidades del aununcio, abre otro selector de motivo (con el motivo anteriormente seleccionado) deshabilitado y al frente una casilla para digitar cantidades.&#160; El usuario selecciona el motivo &quot;no apta para el consumo humano&quot; digita 1 y el sistema habilita la cámara para adjuntar evidencia dado que este motivo de rechazo requiere evidencia ( requires_evidence &#58; &quot;yes&quot; ).&#160; El sistema también al validar que las las cantidades digitadas en ambos motivos suman 2 unidades y esta cifra es igual a la diferencia entre el inventario y eatc-dona.eatc-odd_quantity 
&#160; 
 Dado que se tienen los siguientes datos&#58; 
 date_time&#58; 2019-09-26 18&#58;00&#58;00 
 eatc-donation_manager_code= 900326456-1 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_user_doc_id= 8161174 (que corresponde a numero_cedula ) 
 eatc_donor_code= 890.900.608-9 (que corresponde a eatc_dona. eatc_donor_code) 
 eatc-dona_header_code= 00001912100729 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-pod_id= 729 (que corresponde a eatc_dona. eatc-pod_id) 
 eatc-odd_id= 0935419 (que corresponde a eatc_dona. eatc-odd_id) 
 eatc-odd_quantity= 0 (corresponde a la cantidad de unidades que se reciben) 
 verification_type= ver (que corresponde a verificación. Sería una constante en todo registro de esta funcionalidad ) 
 eatc-odd_rejection_cause= no se encuentra (que corresponde a https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=1 ) ; No apta para el consumo humano (que corresponde a https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=2 ) 
 eatc-odd_rejection_cause_id=1,2 
 quantity = 1 y 1 
 evidence = corresponde a la URL del recurso (fotografía) de evidencia que se guarda en el servidor 
&#160; 
 Utilizando el API se realizan los siguientes registros&#58; 
&#160; 
 Unidades que no se encontraron 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_odd_rejection_registry&amp;_operacion=insert&amp;date_time= 2019-09-26%2018&#58;00&#58;00&amp; eatc-donation_manager_code= 900326456-1 &amp;eatc-donation_manager_user_doc_id= 8161174 &amp;eatc_donor_code= 890.900.608-9 &amp;eatc-dona_header_code= 00001912100729 &amp;eatc-pod_id= 729 &amp;eatc-odd_id= 0935419 &amp;verification_type= ver &amp;eatc-odd_rejection_cause= No%20encontrada&amp; eatc-odd_rejection_cause_id=1 &amp;quantity=1&amp;evidence=NA &#160;&#160;&#160; 
&#160; 
 Unidades no apta para el consumo humano 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_odd_rejection_registry&amp;_operacion=insert&amp;date_time= 2019-09-26%2018&#58;00&#58;00&amp; eatc-donation_manager_code= 900326456-1 &amp;eatc-donation_manager_user_doc_id= 8161174 &amp;eatc_donor_code= 890.900.608-9 &amp;eatc-dona_header_code= 00001912100729 &amp;eatc-pod_id= 729 &amp;eatc-odd_id= 0935419 &amp;verification_type= ver &amp;eatc-odd_rejection_cause= No%20apta%20para%20el%20consumo%20humano&amp; eatc-odd_rejection_cause_id=1 &amp;quantity=1&amp;evidence=url &#160;&#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtengan respuestas de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; 4, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logran obtener estas respuestas, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aquí&#58;&#160; 
 https&#58;//dedonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code= 00001912100729 &amp;eatc-odd_id= 0935419 &#160; o en&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =110,111 &#160; 

&#160; 
 Actualización en eatc_dona con la API &#160; ***NUEVO&#58; se registrarán también “sobrantes” *** 
 Anteriormente solamente se registraban rechazos, pero a partir del momento también se registrarán en la tabla “sobrantes”, unidades que llegan de más y cuyo sobrante se registra en la verificación. 
 Dados los anteriores registros, se determina el _id del registro de detalle de anuncio de donación (eatc_dona)&#58; 
&#160; 
 Dado que se tienen los siguientes datos&#58; 
&#160; 
 eatc-dona_header_code= 00001912100729 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-odd_id= 0935419 (que corresponde a eatc_dona. eatc-odd_id) 
 eatc-odd_quantity= 2 (corresponde a la cantidad de unidades que se reciben) 
&#160; 
 Se puede determinar el _id&#58; &quot;4064&quot; con la siguiente consulta al API&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code =00001912100729&amp; eatc-odd_id= 0935419 &#160;&#160; 
&#160; 
 Con este dato se lleva la relación del anterior registro (URL JSON) al campo &quot; odd_rejection_cause &quot;&#160; 
&#160; 
 odd_rejection_cause= https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =110,111 
 eatc-odd_state= rechazadas 2 unidades, certificables 0 unidades (que corresponde a la sumatoria de las cantidades digitadas para los motivos establecidos) 
&#160; 
Actualización con la API &#160; ***NUEVO&#58; se registrarán también “sobrantes” *** 
 Anteriormente solamente se registraban rechazos, pero a partir del momento también se registrarán en la tabla “sobrantes”, unidades que llegan de más y cuyo sobrante se registra en la verificación. 
&#160; 
 Cuando existen faltantes el sistema realiza la siguiente escritura 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause=&#123;&#123;URL&#125;&#125;&amp;eatc-odd_state= rechazadas &#123;&#123;UNIDADES_rechazadas&#125;&#125; unidades, certificables &#123;&#123;UNIDADES_aceptadas&#125;&#125; unidades&amp;eatc-odd_quantity= &#123;&#123;UNIDADES_aceptadas&#125;&#125; &amp;WHERE_id=&#123;&#123;VALOR&#125;&#125; 
 Cuando existen sobrantes el sistema realiza la siguiente escritura 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause=&#123;&#123;URL&#125;&#125;&amp;eatc-odd_state= Sobrantes &#123;&#123;UNIDADES_sobrantes&#125;&#125; unidades &amp;eatc-odd_quantity= &#123;&#123;UNIDADES_aceptadas&#125;&#125; &amp;WHERE_id=&#123;&#123;VALOR&#125;&#125; 

&#160; 
 Ejemplo, _DOM. cua_master, ambiente productivo&#58; 
&#160; 
 Como el registro completo de las causas de rechazo se puede consultar aquí&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =110,111 
&#160; 
 Utilizando el API se realiza la siguiente actualización&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause= https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =110,111&amp; eatc-odd_quantity=0 &amp; eatc-odd_state= rechazadas%202%20und%20y%20certificables%200%20und &amp;WHERE_id= 4064 &#160; &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Nota importante&#58; Si se envían los parámetros por método GET (URL), no se puede enviar una URL que contenga &quot;&amp;&quot; dado que el sistema la toma como otro atributo a actualizar.&#160; Por eso se debe mandar como parámetro (en este caso &quot; eatc-odd_rejection_cause &quot;) una URL, no se debe mandar una que contenga &amp;.&#160; Utilizando el método POST (con el tester por ejemplo), si se podría enviar una URL con &quot;&amp;&quot; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aquí&#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=00001912100729&amp;eatc-odd_id=0935419 

&#160; 
 Actualización de datos enriquecidos&#58; 
 Se proponen mejoras porque han habido casos como este https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=00002007090581&amp;_id=45708 que a 29 de julio de 2020 poseía esta información (se programaron rutinas para solucionar esta problemática por lo tanto es posible que posteriormente a la fecha establecida los datos se visualicen bien)&#58; 
&#160; 
 eatc-odd_total_weight_kg &#58; &quot;4.54&quot;&#160; 
 eatc-odd_quantity &#58; &quot;0&quot;, 
 eatc-odd_unit_weight_kg &#58; &quot;4.54&quot; 
 eatc-odd_total_cost &#58; &quot;0&quot; 
&#160; 
 Con lo cual se observa un error en el registro de los kg totales ( eatc-odd_total_weight_kg ) dado que si la cantidad final ( eatc-odd_quantity ) es igual a 0 , el dato de los KG totales también debería ser también igual a 0 .&#160; Por lo tanto se propone simplificar la fórmula en aras de evitar posibles errores. 
&#160; 
 Dado que las cantidades certificables variariaron, se deben actualizar los datos correspondientes a&#58; 
&#160; 
 [MEJORA] eatc-odd_total_weight_kg &#58; eatc-odd_total_weight_kg =eatc-odd_quantity*eatc-odd_unit_weight_kg &#160; 
 (ANTES&#58; se puede determinar, aplicando regla de 3, cuando pesarían las unidades que finalmente se certifican ( eatc-odd_quantity= 100)&#58; si eatc-odd_quantity=200 unidades tienen un eatc-odd_total_weight_kg=200, que peso tendrán 100 unidades (la sencilla respuesta en este caso es 100, pero la idea es poder sacar ese dato con regla de tres para no tener que realizar consultas externas)). 
 [MEJORA] eatc-odd_total_cost &#58;&#160; eatc-odd_total_cost =eatc-odd_quantity*eatc-unit_cost&#160; 
 (ANTES&#58;se puede determinar, aplicando regla de 3, cuando valdrían las unidades que finalmente se certifican ( eatc-odd_quantity= 100)&#58; si eatc-odd_quantity=200 unidades tienen un eatc-odd_total_cost= 212745 , que costo tendrán 100 unidades (la sencilla respuesta en este caso es 212745/2=106372,5, pero la idea es poder sacar ese dato con regla de tres para no tener que realizar consultas externas.&#160; También se podría obtener el dato multiplicando eatc-odd_quantity&#160; por 1063.72 (en este caso 100 x 1063.72 = 106372). 
&#160; 
 Actualización con la API 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_total_weight_kg= &#123;&#123;NUEVO PESO CALCULADO&#125;&#125; &amp;eatc-odd_total_cost= &#123;&#123;NUEVO COSTO CALCULADO&#125;&#125; &amp;WHERE_id=&#123;&#123;VALOR&#125;&#125; 

&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente productivo&#58; 
&#160; 
 Dado que para el ejemplo anterior&#58;&#160; 
&#160; 
 eatc-odd_total_weight_kg =100 
 eatc-odd_total_cost =106372 
&#160; 
 Utilizando el API se realiza la siguiente actualización&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona&amp;_operacion=update&amp; eatc-odd_total_weight_kg =100&amp; eatc-odd_total_cost= 106372&amp; WHERE_id = 1229 &#160;&#160;&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Nota importante&#58; Si se envían los parámetros por método GET (URL), no se puede enviar una URL que contenga &quot;&amp;&quot; dado que el sistema la toma como otro atributo a actualizar.&#160; Por eso se debe mandar como parámetro (en este caso &quot; eatc-odd_rejection_cause &quot;) una URL, no se debe mandar una que contenga &amp;.&#160; Utilizando el método POST (con el tester por ejemplo), si se podría enviar una URL con &quot;&amp;&quot; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aquí&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=40716&amp;eatc-odd_id= 1005163 &#160; 
&#160; 
 NOTA DE UNIFICACIÓN&#58; 
 Dado que la actualización de información y los nuevos cálculos de información enriquecida se pueden hacer en un mismo proceso, podría realizarse el siguiente llamado unificado al API, para unificar ambas cosas&#58; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause= https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry? _id =3,4&amp; eatc-odd_quantity=100 &amp; eatc-odd_state= rechazadas%20100%20und%20y%20certificables%20100%20und &amp; eatc-odd_total_weight_kg =100&amp; eatc-odd_total_cost= 106372&amp; WHERE_id = 1229 &#160;&#160; 
&#160; 
 DEPRECADO&#58;&#160; llamado al servicio de integración blockchain 
 Adicional a los llamados para cambiar las cantidades recibidas de un ítem del anuncio de donación (actualización de la cantidad del ítem), el sistema deberá realizar DESPUÉS (dado que primero debe haberse actualizado eatc_dona ) el siguiente llamado a un nuevo servicio de integración con blockchain, con el ánimo de actualizar la información del respectivo item en la cadena de bloques&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125;&amp;eatc_odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_servicio=frmProductoDonacionEditar 
&#160; 
 En caso que la cantidad recibida sea 0 (es decir, el beneficiario reporta que no recibió el producto donado), se deberá realizar el siguiente llamado&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125;&amp;eatc_odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_servicio=frmProductoDonacionEliminar 

 &#160; 
 DEPRECADO&#58; A CTUALIZACIÓN DE LA INFORMACIÓN DEL ENCABEZADO DE DONACIÓN ( EATC_DONA_HEADERS ) =&gt; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/APP-Modernizada--marcado-como--reciept--para-donaciones-con-verificaci%C3%B3n-detallada.aspx &#160; 
 La cuenta tiene el parámetro multiple_donors = si 
&#160; 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = si , entonces se procede con la actualización del estado de la donación a a &quot;received&quot; (recibido) (Tal como funcionaba antes)&#58; Al terminar el proceso de verificación,&#160; un anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 

 eatc-state&#58; debe cambiar de &quot;delivered&quot; (entregado) a &quot;received&quot; (recibido) 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
 ***NUEVO&#58; registro de “eatc_state3” 

 eatc_state3&#58; “Recibido” 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received &amp; eatc-receipt_datetime =&#123;&#123; DATETIME&#125;&#125;&amp; eatc_state3= Recibido &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donación cuyo eatc-code = 40716 (y cuyo detalle eatc_dona se consulta aquí ) , se termina el proceso de&#160; verificación a las 2019-09-26 19&#58;00&#58;00 
&#160; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received &amp; eatc-receipt_datetime = 2019-09-26%2019&#58;00&#58;00&amp; WHEREeatc-code= 40716 &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aquí&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 &#160; 

 &#160; 
 La cuenta tiene el parámetro multiple_donors = no 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125; 
&#160; 
 Tiene el parámetro multiple_donors = no , entonces para realizar el cambio de estado a &quot;recibido&quot; se debe verificar si existe un registro válido en &quot; eatc_code_verification_datetime &quot; (fecha válida).&#160; En ese caso se realiza la siguiente actualización. 
&#160; 

 eatc-state&#58; debe cambiar de &quot;delivered&quot; (entregado) a &quot;received&quot; (recibido) 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received&amp; eatc_state3 = Recibido &amp; eatc-receipt_datetime =&#123;&#123;timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 

 &#160; 
 Si no existe una fecha válida en &quot; eatc_code_verification_datetime &quot; ( es decir [&quot;eatc_code_verification_datetime&quot;] == &quot;0000-00-00 00&#58;00&#58;00&quot;), el sistema realizará un estampe en la fecha de recepción, pero no cambiará el estado de la donación. 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
 ***NUEVO&#58; registro de “eatc_state3” 

 eatc_state3&#58; “Por validar” 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-receipt_datetime =&#123;&#123;timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc_state3= Por%20validar &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 
&#160; 

 &#160; 
 El beneficiario tiene el campo eatc_donation_managers.eatc_sdm = y 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_donations_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= eatc_sdm 
&#160; 
 Si el sistema arroja una respuesta inválida (ejemplo&#58; err_msg &#58; &quot;Unknown column 'eatc_sdm' in 'field list'&quot;), vacía, nula, o igual a &quot;n&quot; entonces el sistema funcionará como lo viene haciendo, en cuanto al registro de las fecha de recepción ( eatc_dona_headers. eatc-receipt_datetime ). 

 &#160; 
 Si el sistema arroja como respuesta un &quot;y&quot; , entonces se propone el siguiente nuevo funcionamiento&#58; 
&#160; 
 Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd =y) &#58; se registra también la fecha y hora de salida a la recolección*** 
&#160; 
 El sistema deberá evaluar si en las fechas&#58; 
&#160; 

 ***NUEVO&#58; eatc_dona_headers. eatc-picker_start_datetime *** 

 eatc_dona_headers. eatc-picking_checkin_datetime 

 eatc_dona_headers. eatc-picking_checkout_datetime 
&#160; 
 En cuyo caso deberá incorporar en dichas fechas la misma fecha que se guardará como eatc_dona_headers. eatc-receipt_datetime (si existen registros válidas en alguna de las fechas, se dejan dichas fechas válidas como registro). 
&#160; 
 Registro del estado de la donación cuando el beneficiario tiene el campo eatc_donation_managers.eatc_sdm = y 
&#160; 
 La cuenta tiene el parámetro multiple_donors = si 
&#160; 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = si , entonces se procede con la actualización del estado de la donación a &quot;received&quot; (recibido) (Tal como funcionaba antes)&#58; Al terminar el proceso de verificación,&#160; un anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 

 eatc-state&#58; debe cambiar de &quot;scheduled&quot; (programado) a &quot;received&quot; (recibido) &#160; 
 ***NUEVO&#58; registro de “eatc_state3” 

 eatc_state3&#58; “Recibido” 
&#160; 
 La cuenta tiene el parámetro multiple_donors = no 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = no , entonces se debe evaluar la información del parámetro eatc_dona_headers. eatc_code_verification_datetime &#58;&#160; 
&#160; 
 Si no tiene una fecha y hora válida (es decir el registro es igual a &quot;0000-00-00 00&#58;00&#58;00&quot;), 

 eatc_dona_headers. eatc-state &#58; debe cambiar de &quot;scheduled&quot; (programado) (o a futuro de &quot; annouced &quot;) a &quot; delivered &quot; (despachado)&#160; 
 ***NUEVO&#58; registro de “eatc_state3” 

 eatc_state3&#58; “Por validar” 
&#160; 
 Si tiene una fecha y hora válida (es decir el registro es diferente a &quot;0000-00-00 00&#58;00&#58;00&quot;), 

 eatc_dona_headers. eatc-state &#58; debe cambiar de &quot;scheduled&quot; (programado)&#160; (o a futuro de &quot; annouced &quot;) a &quot; received &quot; (recibido) &#160; 

 eatc_dona_headers. eatc_state3 &#58; debe cambiar de “Recibido” 

 ***NUEVO&#58; Formulario de verificación por PESOs (Nuevo tipo de verificación) *** 
 Con esta funcionalidad, se pretende dar al usuario la posibilidad de, en vez de registrar cantidades en el proceso de verificación ( eatc-odd_quantity ), se registre el peso total por artículo (item) verificado ( eatc-odd_total_weight_kg ). A partir de dicho dato y teniendo como dato fijo &quot;el peso unitario&quot; ( eatc-odd_unit_weight_kg ), el sistema debe calcular las unidades correspondientes ( eatc-odd_quantity&#58; utilizando una regla de tres) para llevarlas al registro del detalle de la donación (junto con el nuevo peso total). 
&#160; 
 Consulta para traer los datos para la verificación 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ?eatc-dona_header_code=&#123;&#123; eatc-code &#125;&#125;&amp;eatc-odd_state= ! rechazado&amp;_cmp=eatc-odd_name,eatc-odd_id,eatc-odd_state,eatc-odd_unit_weight_kg,eatc-odd_total_weight_kg 
&#160; 
 El sistema arroja un listado completo de referencias (eatc-odd_id) contenido en el detalle del anuncio de donación (eatc-dona) mostrando para cada una de las referencias, su nombre ( eatc-odd_name ) y su código ( eatc-odd_id ). &#160; Se debe excluir del listado aquellas referencias que tengan estado ( eatc-odd_state) &quot;rechazado&quot;. 
&#160; 
 Ejemplo, _DOM. cua_master=abaco, ambiente productivo&#58; 
&#160; 
 El para el anuncio cuyo &quot; eatc-code &quot; = 00001911240031 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=00001911240031&amp;eatc-odd_state=!rechazado&amp;_cmp=eatc-odd_name,eatc-odd_id,eatc-odd_state,eatc-odd_unit_weight_kg,eatc-odd_total_weight_kg&#160;&#160; 
&#160; 
 El sistema debe generar un listado de 10 productos 
&#160; 
 Se debe implementar un buscador de productos (por nombre) para filtrar los elementos del listado. 

 Campos de captura para la verificación por peso 
 Basados en la implementación de verificación por cantidades (como se muestra en la siguiente imagen), se debe, por cada item de la donación, desplegar un formulario de captura con la siguiente información 

 Nombre del producto (informativo, sin label) 
&#160; 
 Se muestra el dato contenido en&#58; 
 eatc_dona. eatc-odd_name 
&#160; 
 Código del producto&#160; (informativo, sin label) 
&#160; 
 Se muestra el dato contenido en&#58; 
 eatc_dona. eatc-odd_id 

&#160; 
 ***NUEVO &#58; Peso reportado en KG *** 
 label&#58; class= &quot;lbl_peso_reportado_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_peso_reportado_kg ) 

&#160; 
 Tipo de campo de captura&#58;&#160; 
 Campo para ingreso números flotantes. 

&#160; 
 Valor por defecto que muestra el campo&#58; 
 eatc_dona. eatc-odd_total_weight_kg 
&#160; 
 Label después del campo de captura&#160; 
 ( en la imagen ejemplo &quot; Unidades &quot;)&#58;&#160; 
&#160; 
 KG 
&#160; 
 label&#58; class= &quot;lbl_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_kg )&#160; 

 Label en la parte inferior del campo de captura&#160; 
 ( en la imagen ejemplo &quot; Unidades efectivamente recibidas (aptas para el consumo humano &quot;)&#58;&#160; 
&#160; 
 KG efectivamente recibidos (aptos para el consumo humano) 
&#160; 
 label&#58; class= &quot;lbl_kg_efectivamente_recibidos&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_kg_efectivamente_recibidos ) 

&#160; 
 El valor digitado se lleva a la variable&#58; 
 &#123;&#123;KG_efectivamente_recibidos&#125;&#125; 

&#160; 
 Validaciones con respecto al peso reportado en KG 
 El sistema deberá comparar el valor ingresado vs el valor registrado en eatc_dona. eatc-odd_total_weight_kg 
&#160; 
 Si el valor reportado es menor 
 (es decir hay menos KG aptos para el consumo humano que los KG originales del producto), se deberá desplegar un formulario similar al desarrollado para la verificación por cantidades que permita registrar la causal de los KG no aptos, como se detalla más adelante .&#160; La diferencia será que el label de Alerta (que en el ejemplo gráfico es &quot; Faltan X Unds &quot;) será&#58; 
&#160; 
 &quot;Faltan&quot; &quot;X&quot; &quot;KG&quot; 
&#160; 
 Concatenación de los labels&#58; 
&#160; 
 label&#58; class= &quot;lbl_faltan&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_faltan )&#160;&#160; 
&#160; 
 X &#58; KG faltantes&#58; que serían iguales a&#58;&#160; 
&#160; 
 eatc_dona. eatc-odd_total_weight_kg - KG digitados (los KG totales menos lo KG digitados) 
&#160; 
 label&#58; class= &quot;lbl_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_kg )&#160; 

&#160; 
 Si el valor reportado es mayor 
 (es decir hay más KG aptos para el consumo humano que los KG originales del producto), se deberá desplegar la alerta correspondiente de sobrante.&#160; La diferencia será que el label de Alerta (que en el ejemplo gráfico es &quot; Sobran X Unds &quot;) será&#58; 
&#160; 
 &quot;Sobran&quot; &quot;X&quot; &quot;KG&quot; 
&#160; 
 Concatenación de los labels&#58; 
&#160; 
 label&#58; class= &quot;lbl_sobran&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_sobran )&#160; 
&#160; 
 X &#58; KG sobrantes&#58; que serían iguales a&#58;&#160; 
&#160; 
 (eatc_dona. eatc-odd_total_weight_kg - KG digitados)* (-1) (los KG totales menos lo KG digitados multiplicados por menos uno) 
&#160; 
 label&#58; class= &quot;lbl_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_kg )&#160; 

&#160; 
 Registro de causales o motivos de rechazo por verificación con kilogramos diferentes 
 Si la cantidad digitada por el usuario es menor al dato que tiene el anuncio de donación ( eatc-dona.eatc-odd_quantity ) el sistema debe abrir un formulario realizando los siguientes procesos&#58; 
&#160; 
 Consulta de los causales ***NUEVO &#58; cambio en la consulta para obtener el selector (para registro de sobrantes ) *** 
 Anteriormente se tenían solamente causales de rechazo en el maestro, pero a partir del momento también se registrarán causales de “sobrantes” y se empezará a registrar los sobrantes en la tabla eatc_odd_rejection_registry dada una mejora solicitada por BAMX (en donde se deben notificar tanto sobrantes como faltantes). 
&#160; 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 &#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_odd_rejection_causes? rejection_cause = y 
&#160; 
 (Anteriormente&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_odd_rejection_causes?_id=_* 
 &#160; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_odd_rejection_cause&amp;code=_todos ) 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_odd_rejection_causes. eatc_label &quot; para construir el selector internacionalizado y de acuerdo a la opción seleccionada se toman los datos &quot; eatc_odd_rejection_causes. nombre &quot; y &quot; eatc_odd_rejection_causes. code &quot; para llevarlos al registro del causal de rechazo&#58; 
 Consulta para determinar si la causal requiere evidencia. ***NUEVO &#58; registro de evidencia *** 
 El sistema deber realizar la siguiente consulta, para determinar si la causal requiere evidencia 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/ eatc_odd_rejection_causes ? eatc_label =&#123;&#123; eatc_odd_rejection_causes.eatc_label &#125;&#125;&amp;_cmp= requires_evidence 
&#160; 
 Si la causal requiere evidencia ( eatc_odd_rejection_causes. requires_evidence = yes ), se debe permitir tomar una foto o seleccionar un archivo para registrarla como evidencia en el sistema (el sistema validará que el usuario tome la foto cuando se requiere, para completar el proceso de verificación&#58; evidencia obligatoria). 
&#160; 
 Si la causal NO requiere evidencia ( eatc_odd_rejection_causes. requires_evidence = no ), se debe permitir tomar una foto o seleccionar un archivo para registrarla como evidencia en el sistema, pero dicha acción será opcional. 
&#160; 
 El sistema debe subir el recurso al servidor y guardar registro de la URL en donde se puede obtener el recurso en la estructura definida para tal fin (&#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_odd_rejection_registry &#160; campo “ evidence ”) y el anuncio de donación ( eatc_dona campo&#58; “ eatc-odd_rejection_cause ”). 
&#160; 
 ***NUEVO &#58; Captura de KG rechazados *** (en vez de unidades rechazadas) 
&#160; 
 Tipo de campo de captura&#58;&#160; 
 Campo para ingreso números flotantes. 
&#160; 
 Valor por defecto que muestra el campo&#58; 
 &#123;&#123;eatc_dona. eatc-odd_total_weight_kg &#125;&#125; - &#123;&#123;KG_efectivamente_recibidos&#125;&#125; 
&#160; 
 El valor digitado se lleva a la variable&#58; 
 &#123;&#123;KG_rechazados_por_causal&#125;&#125; 
&#160; 
 Cálculo de cantidades rechazadas por motivo de rechazo&#58; 
 &#123;&#123; CANTIDAD_RECHAZADA_por_motivo_de_rechazo &#125;&#125; = &#123;&#123;KG_rechazados_por_causal&#125;&#125; / &#123;&#123;eatc_dona. eatc-odd_unit_weight_kg &#125;&#125; 
&#160; 
 Escritura en eatc_odd_rejection_registry con la API ***NUEVO&#58; &#160;se registrarán también “sobrantes”. Se llevará al registro el dato eatc_donor *** 
 Anteriormente solamente se registraban rechazos, pero a partir del momento también se registrarán en la tabla “sobrantes”, unidades que llegan de más y cuyo sobrante se registra en la verificación. 
&#160; 
Cuando se registran faltantes 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla= eatc_odd_rejection_registry &amp;_operacion= insert &amp;date_time= &#123;&#123;DATETIME&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_dona_headers . eatc-donation_manager_code &#125;&#125; &amp;eatc-donation_manager_user_doc_id= &#123;&#123; eatc_dona_headers . eatc-donation_manager_user_doc_id &#125;&#125; &amp;eatc_donor_code= &#123;&#123; eatc_dona_headers . eatc-donor_code &#125;&#125; &amp; eatc_donor =&#123;&#123; eatc_dona_headers . eatc-donor &#125;&#125; &amp;eatc-dona_header_code= &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; &amp;eatc-pod_id= &#123;&#123; eatc_dona_headers . eatc-pod_id &#125;&#125; &amp;eatc-odd_id= &#123;&#123; eatc_dona . eatc-odd_id &#125;&#125; &amp;verification_type= ver &amp;eatc-odd_rejection_cause= &#123;&#123; eatc_odd_rejection_causes .nombre&#125;&#125; &amp;eatc-odd_rejection_cause_id= &#123;&#123; eatc_odd_rejection_causes .code&#125;&#125; &amp;quantity= &#123;&#123;UNIDADES_rechazadas&#125;&#125; &amp;evidence= &#123;&#123;URL_evidencia&#125;&#125; 
Cuando se registra un sobrante entonces el registro será&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla= eatc_odd_rejection_registry &amp;_operacion= insert &amp;date_time= &#123;&#123;DATETIME&#125;&#125; &amp;eatc-donation_manager_code= &#123;&#123; eatc_dona_headers . eatc-donation_manager_code &#125;&#125; &amp;eatc-donation_manager_user_doc_id= &#123;&#123; eatc_dona_headers . eatc-donation_manager_user_doc_id &#125;&#125; &amp;eatc_donor_code= &#123;&#123; eatc_dona_headers . eatc-donor_code &#125;&#125; &amp; eatc_donor =&#123;&#123; eatc_dona_headers . eatc-donor &#125;&#125; &amp;eatc-dona_header_code= &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; &amp;eatc-pod_id= &#123;&#123; eatc_dona_headers . eatc-pod_id &#125;&#125; &amp;eatc-odd_id= &#123;&#123; eatc_dona . eatc-odd_id &#125;&#125; &amp;verification_type= ver &amp;eatc-odd_rejection_cause= sobrante &amp;eatc-odd_rejection_cause_id= 3 &amp;quantity= &#123;&#123;UNIDADES_sobrantes&#125;&#125; &amp;evidence= &#123;&#123;URL_evidencia&#125;&#125; 

&#160; 
 Sumatoria de faltantes y sobrantes 
 Debe funcionar sumando los KG reportados como faltantes en los diferentes items y los KG reportados como sobrantes en los diferentes items.&#160; Los labels son similares a excepción del que va después de las respectivas sumatorias, el cual deberá ser&#58;&#160; 
&#160; 
 ***NUEVO &#58; KG *** (en vez de &quot; Unids &quot;) 
&#160; 
 label&#58; class= &quot;lbl_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_kg )&#160; 

&#160; 
 ***NUEVO &#58; Cálculo de unidades a partir de los pesos reportados *** 
 Partiendo de la base que el peso unitario debe ser constante, entonces, para aportar el dato eatc_dona. eatc-odd_quantity el sistema deberá realizar el siguiente cálculo 
&#160; 
 &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125; = &#123;&#123;KG_efectivamente_recibidos&#125;&#125; / &#123;&#123;eatc_dona. eatc-odd_unit_weight_kg &#125;&#125; 

&#160; 
 Otros cálculos a partir de las unidades calculadas y definiciones ***NUEVO&#58; definición de sobrante para registro del mismo *** 
 Definición del estado &#123;&#123;estado_definido&#125;&#125; 
&#160; 
 Según el registro de rechazos se define el estado de cada item de la siguiente manera&#58; 
&#160; 
 Si todos los KG fueron rechazados (es decir se definieron como &quot;0&quot; los KG aptos para el consumo humano)&#58;&#160; 
 &#123;&#123;estado_definido&#125;&#125;&#160; = rechazado 
 Si todos los KG fueron aceptados (es decir no hubo rechazos o hubo sobrantes)&#58;&#160; 
 &#123;&#123;estado_definido&#125;&#125;&#160; = &#160; certificable 
 Si hubo un rechazo parcial&#58; se informan las cantidades rechazadas y las cantidades aceptadas 
 &#123;&#123;estado_definido&#125;&#125;&#160; =&#160; rechazadas &#123;&#123;sumatoria &#123;&#123; CANTIDAD_RECHAZADA_por_motivo_de_rechazo &#125;&#125; &#125;&#125; und y certificables &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125; und 
 ***NUEVO &#58; Si hubo un sobrante&#58; se informan las cantidades sobrantes 
 &#123;&#123;estado_definido&#125;&#125;&#160; =&#160; sobrantes &#123;&#123;sumatoria &#123;&#123; CANTIDAD_sobrante &#125;&#125; &#125;&#125; und&#160; 
&#160; 
 Actualización de costo total &#123;&#123;costo_total_actualizado&#125;&#125; 
 Para determinar el el costo total actualizado se realiza el siguiente cálculo&#58; 
 &#123;&#123; costo_total_actualizado &#125;&#125; = &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125; * &#123;&#123;eatc_dona. eatc-odd_unit_weight_kg &#125;&#125; 

&#160; 
 Actualización en eatc_dona con la API ***NUEVO&#58; se registrarán también “sobrantes” *** 
 Anteriormente solamente se registraban rechazos, pero a partir del momento también se registrarán en la tabla “sobrantes”, unidades que llegan de más y cuyo sobrante se registra en la verificación. 
&#160; 
 Cuando existen faltantes el sistema realiza la siguiente escritura 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause=&#123;&#123;URL&#125;&#125;&amp;eatc-odd_state= rechazadas &#123;&#123;UNIDADES_rechazadas&#125;&#125; unidades, certificables &#123;&#123;UNIDADES_aceptadas&#125;&#125; &#160;unidades&amp;eatc-odd_quantity= &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125; &amp;WHERE_id=&#123;&#123;VALOR&#125;&#125; 
 Cuando existen&#160; sobrantes&#160; el sistema realiza la siguiente escritura 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona&amp;_operacion=update&amp;eatc-odd_rejection_cause=&#123;&#123;URL&#125;&#125;&amp;eatc-odd_state= Sobrantes &#123;&#123;UNIDADES_sobrantes&#125;&#125; unidades &amp;eatc-odd_quantity= &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125; &amp;WHERE_id=&#123;&#123;VALOR&#125;&#125; 

 Anteriormente&#58;&#160; 
 Actualización con la API 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona&amp;_operacion=update&amp; eatc-odd_rejection_cause =&#123;&#123;URL&#125;&#125;&amp; eatc-odd_state= &#123;&#123;estado_definido&#125;&#125;&amp; eatc-odd_quantity= &#123;&#123; CANTIDAD_ACEPTADA &#125;&#125;&amp; eatc-odd_total_weight_kg = &#123;&#123;KG_efectivamente_recibidos&#125;&#125; &amp; eatc-odd_total_cost= &#123;&#123; costo_total_actualizado &#125;&#125;&amp; WHERE_id =&#123;&#123;VALOR&#125;&#125; 
&#160; 
 Deprecado&#58;&#160; llamado al servicio de integración blockchain 
 Adicional a los llamados para cambiar las cantidades recibidas de un ítem del anuncio de donación (actualización de la cantidad del ítem), el sistema deberá realizar DESPUÉS (dado que primero debe haberse actualizado eatc_dona ) el siguiente llamado a un nuevo servicio de integración con blockchain, con el ánimo de actualizar la información del respectivo item en la cadena de bloques&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125;&amp;eatc_odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_operacion=update&amp;_servicio=frmProductoDonacion 
&#160; 
 En caso que la cantidad recibida sea 0 (es decir, el beneficiario reporta que no recibió el producto donado), se deberá realizar el siguiente llamado&#58; 
&#160; 
 Endpoint&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona. eatc-dona_header_code &#125;&#125;&amp;eatc_odd_id=&#123;&#123;eatc_dona. eatc-odd_id &#125;&#125;&amp;_operacion=delete&amp;_servicio=frmProductoDonacion 
&#160; 
 DEPRECADO&#58; Actualización de la información del encabezado de donación ( eatc_dona_headers ) =&gt; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/APP-Modernizada--marcado-como--reciept--para-donaciones-con-verificaci%C3%B3n-detallada.aspx &#160; 
 Llamado al servicio para recalcular pesos y costos del encabezado de donación 
&#160; 
 Se deberá llamar al servicio que a partir de los nuevos datos del detalle de donación, recalcula los pesos y los costos del encabezado del anuncio de donación. 
&#160; 
 -------De aquí en adelante todo funciona similar a como funciona para la verificación tradicional en unidades------- 
 La cuenta tiene el parámetro multiple_donors = si 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125; 
&#160; 
 Tiene el parámetro multiple_donors = si , entonces se procede con la actualización del estado de la donación a &quot;received&quot; (recibido) (Tal como funcionaba antes)&#58; Al terminar el proceso de verificación,&#160; un anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 

 eatc-state&#58; debe cambiar de &quot;delivered&quot; (entregado) a &quot;received&quot; (recibido) 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
 ***NUEVO&#58;registro de “eatc_state3” 

 eatc_state3&#58; “Recibido” 
&#160; 
 Escritura con la API&#58;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received &amp; eatc-receipt_datetime =&#123;&#123; DATETIME&#125;&#125; &amp; eatc_state3= Recibido &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 
&#160; 
 Ejemplo&#58; 
&#160; 
 Para el anuncio de donación cuyo eatc-code = 40716 (y cuyo detalle eatc_dona se consulta aquí ) , se termina el proceso de&#160; verificación a las 2019-09-26 19&#58;00&#58;00 
&#160; 
&#160; 
 Utilizando el API se realiza el siguiente registro&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received &amp; eatc-receipt_datetime = 2019-09-26%2019&#58;00&#58;00&amp; WHEREeatc-code= 40716 &#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aquí&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= 40716 &#160; 

 &#160; 
 La cuenta tiene el parámetro multiple_donors = no 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = no , entonces para realizar el cambio de estado a &quot;recibido&quot; se debe verificar si existe un registro válido en &quot; eatc_code_verification_datetime &quot; (fecha válida).&#160; En ese caso se realiza la siguiente actualización. 
&#160; 

 eatc-state&#58; debe cambiar de &quot;delivered&quot; (entregado) a &quot;received&quot; (recibido) 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-state= received &amp; eatc_state3= Recibido &amp; eatc-receipt_datetime =&#123;&#123;timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 
&#160; 
&#160; 
 Si no existe una fecha válida en &quot; eatc_code_verification_datetime &quot; ( es decir [&quot;eatc_code_verification_datetime&quot;] == &quot;0000-00-00 00&#58;00&#58;00&quot;) , el sistema realizará un estampe en la fecha de recepción, pero no cambiará el estado de la donación. 

 eatc-receipt_datetime&#58; El sistema debe tomar la fecha y hora en la cual se termina el proceso de verificación. 
 ***NUEVO&#58;registro de “eatc_state3” 

 eatc_state3&#58; “Por validar” 
&#160; 
 Escritura con la API&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125; /?_tabla=eatc_dona_headers&amp;_operacion=update&amp; eatc-receipt_datetime =&#123;&#123;timestamp en formato AAAA-MM-DD HH&#58;MM&#58;SS&#125;&#125; &amp; eatc_state3= Por%20validar &amp; WHEREeatc-code=&#123;&#123; VALOR&#125;&#125; 
&#160; 

 &#160; 
 El beneficiario tiene el campo eatc_donation_managers.eatc_sdm = y 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_donations_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= eatc_sdm 
&#160; 
 Si el sistema arroja una respuesta inválida (ejemplo&#58; err_msg &#58; &quot;Unknown column 'eatc_sdm' in 'field list'&quot;), vacía, nula, o igual a &quot;n&quot; entonces el sistema funcionará como lo viene haciendo, en cuanto al registro de las fecha de recepción ( eatc_dona_headers. eatc-receipt_datetime ). 
&#160; 
 Si el sistema arroja como respuesta un &quot;y&quot; , entonces se propone el siguiente nuevo funcionamiento&#58; 
&#160; 
 Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd =y) &#58; se registra también la fecha y hora de salida a la recolección*** 
&#160; 
 El sistema deberá evaluar si en las fechas&#58; 
&#160; 

 ***NUEVO&#58; eatc_dona_headers. eatc-picker_start_datetime *** 

 eatc_dona_headers. eatc-picking_checkin_datetime 

 eatc_dona_headers. eatc-picking_checkout_datetime 

 &#160; 
 Registro del estado de la donación cuando el beneficiario tiene el campo eatc_donation_managers.eatc_sdm = y 
&#160; 
 La cuenta tiene el parámetro multiple_donors = si 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = si , entonces se procede con la actualización del estado de la donación a &quot;received&quot; (recibido) (Tal como funcionaba antes)&#58; Al terminar el proceso de verificación,&#160; un anuncio de donación se debe actualizar la siguiente información&#58; 
&#160; 

 eatc-state&#58; debe cambiar de &quot;scheduled&quot; (programado) a &quot;received&quot; (recibido) &#160; 
&#160; 
 ***NUEVO&#58;registro de “eatc_state3” 
 eatc_state3&#58; “Recibido” 
&#160; 
 La cuenta tiene el parámetro multiple_donors = no 
 Si la cuenta respectiva&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;_cmp=multiple_donors &#160; 
&#160; 
 Tiene el parámetro multiple_donors = no , entonces se debe evaluar la información del parámetro eatc_dona_headers. eatc_code_verification_datetime &#58;&#160; 
&#160; 
 Si no tiene una fecha y hora válida (es decir el registro es igual a &quot;0000-00-00 00&#58;00&#58;00&quot;), 

 eatc_dona_headers. eatc-state &#58; debe cambiar de &quot;scheduled&quot; (programado) (o a futuro de &quot; annouced &quot;) a &quot; delivered &quot; (despachado)&#160; 
 ***NUEVO&#58; registro de “eatc_state3” 

 eatc_state3&#58; “Por validar” 
&#160; 
 Si tiene una fecha y hora válida (es decir el registro es diferente a &quot;0000-00-00 00&#58;00&#58;00&quot;), 

 eatc_dona_headers. eatc-state &#58; debe cambiar de &quot;scheduled&quot; (programado)&#160; (o a futuro de &quot; annouced &quot;) a &quot; received &quot; (recibido) &#160; 

 eatc_dona_headers. eatc_state3 &#58; debe cambiar de “Recibido” 

 En cuyo caso deberá incorporar en dichas fechas la misma fecha que se guardará como eatc_dona_headers. eatc-receipt_datetime (si existen registros válidas en alguna de las fechas, se dejan dichas fechas válidas como registro). 

 DEPRECADO&#58; LLAMADO AL SERVICIO DE INTEGRACIÓN CON BLOCKCHAIN 
&#160; 
 Endpoint (según documentación ([POST] servicio&#58; frmRecibir (Enviar donación) )&#58; sujeto a revisión) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/int/eatcloud/int_blockchain?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_servicio=frmRecibir 
&#160; 
 Parámetros para el llamado al servicio&#58; 
&#160; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación recientemente creado&#58; eatc_dona_heaaders. eatc-code =&gt; parámetro de carácter obligatorio 
&#160; 
 eatc_cua_master&#58; 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) =&gt; parámetro de carácter obligatorio 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fverificaci%C3%B3n-detallada-anuncio-de-donaci%C3%B3n-eatc_dona_ver%2F1127086716-vericacion_app.jpg&ow=720&oh=1280, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fverificaci%C3%B3n-detallada-anuncio-de-donaci%C3%B3n-eatc_dona_ver%2F1127086716-vericacion_app.jpg&ow=720&oh=1280 

 User Administrator 
 568.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"Off"},{"Name":"AIGeneratedDescription","Version":"Off"}] 
 38856975-4d08-4692-b0e3-b36087bedd8f 
 4!1!3 
 https://centralus0-0.pushfp.svc.ms/fluid 
 b2f99724-721c-4c9d-a230-cebd2e3f0054 
 2026-02-13T04:17:50.5288715Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"60d72d49-a2c4-47be-a3a7-1828a58a4491","SequenceId":137,"FluidContainerCustomId":"073cf4b6-699b-459a-8b7a-795d0ce03edd","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 VERIFICACIÓN DETALLADA ANUNCIO DE DONACIÓN (EATC_DONA_VER)