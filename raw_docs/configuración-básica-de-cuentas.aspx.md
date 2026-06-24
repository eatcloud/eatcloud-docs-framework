# configuración-básica-de-cuentas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Una vez se han creados los registros de usuario super admin, de cuenta y los datos y tablas automticas que se despliegan en la funcionalidad de " Onboarding de cuentas ", se hace un ingreso automtico a la plataforma de cuentas en data gov (sin pasar por el login ). Esta configuracin bsica abrir inicialmente tres pantallas de captura de datos (que pueden ser popup windows) y que cumplen las siguientes funciones (la ltima tiene relacin directa con una funcionalidad de esta plataforma, por lo tanto su implementacin es complementaria): 
 Darle la bienvenida al usuario y terminar de perfilarlo, 
 Terminar de perfilar a la cuenta con su tamao 
 Capturar los datos bsicos del cliente   => Configura tu empresa 

 Una vez capturada toda la informacin del cliente y el usuario, se procede a realizar integraciones con el ERP y el CRM .  Por ltimo se mostrarn tres pasos importantes (con una barra de progreso de los mismos) que estarn dispuestos para invitar al usuario a realizar por primera vez estas configuraciones.  Cada una de estas capturas tiene correspondencia con una funcionalidad de esta plataforma  
 La creacin de puntos de donacin  => Agrega puntos de donacin 
 Hacer la primera donacin => Realiza una donacin 
 Crear usuarios de BO => Agrega usuarios de consulta 
 Consultar el BO por primera vez =>  Consulta tus resultados 

 BIENVENIDA Y PERFILAMIENTO DEL USUARIO SUPERADMIN 

 Nota importante de implementacin (implementar internacionalizando y poniendo a funcionar el administrador de funcionalidades):  
 en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Botones para la seleccin de la funcin del usuario: *** NUEVO : el label para internacionalizacin se toma del dato: eatc_superadmin_profile .eatc_name *** 
 El sistema desplegar una serie de botones (nube de botones) en dnde se mostrarn los diferentes perfiles que le aplican al superadministrador. El usuario deber elegir uno de los perfiles y dicho dato se llevar a la persistencia en donde se guardan los datos del superadministrado (se entiende que es bo_usuarios ). 
 Informacin tcnica del parmetro: bo_usuarios. eatc_user_profile   
 Tipo de dato: string 
 Tipo de input: nube de botones: selector nico 
 La informacin del selector se toma de class={{ eatc_verticals_mt .eatc_name }} (se deber configurar para que los valores que se obtienen de la siguiente consulta, sean tratados como labels) 

 Consulta de perfiles: 
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_verticals_mt?eatc_onboarding=1 &_distinct= eatc_name 

 Ejemplo en ambiente productivo: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_superadmin_profile?_id=_*&_distinct= eatc_name   

 Dado que la respuesta del servicio es: 
 res :  
 [ 
 { 
 eatc_name : "CEO" 
 }, 
 { 
 eatc_name : "director_marketing" 
 }, 
 { 
 eatc_name : "director_logistica" 
 }, 
 { 
 eatc_name : "director_ventas" 
 }, 
 { 
 eatc_name : "director_sostenibilidad" 
 }, 
 { 
 eatc_name : "director_operaciones" 
 }, 
 { 
 eatc_name : "profesional_ambiental" 
 }, 
 { 
 eatc_name : "profesional_rse" 
 }, 
 { 
 eatc_name : "profesional_logistica" 
 }, 
 { 
 eatc_name : "director_compras" 
 } 
 ], 

 Entonces los selectores se deben popular con los siguientes labels: 
 class=" CEO ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=CEO 
 class=" director_marketing ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=director_marketing   
 class=" director_logistica ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=retaildirector_logistica   
 class=" director_ventas ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=director_ventas   
 class=" director_sostenibilidad ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=director_sostenibilidad   
 class=" director_operaciones ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=director_operaciones   
 class=" profesional_ambiental ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=profesional_ambiental   
 class=" profesional_rse ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=profesional_rse   
 class=" profesional_logistica ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=profesional_logistica   
 class=" director_compras ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=director_compras   

 DEPRECADO: 
 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 

 ***NUEVO: Paso 2: consulta de los perfiles disponibles para este onboarding: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_superadmin_profile?_id=_* 

 El sistema toma el array de valores del parmetro eatc_superadmin_profile. _id para realizar la siguiente consulta 

 ***NUEVO: Paso 3: consulta de los perfiles 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_superadmin_profile &eatc_language={{codigo_dos_digitos_idioma}}& eatc_data_id={{array( eatc_superadmin_profile . _id)}} 

 Ejemplo: idioma espaol a 24 de noviembre de 2020: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_superadmin_profile &eatc_language=es& eatc_data_id=1,2,3,4,5,6,7,8,9,10   

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto (ingls=en idioma por defecto): 

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_superadmin_profile &eatc_language= en &eatc_data_id= {{array( eatc_superadmin_profile . _id)}} 

 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en los botones 

 Ejemplo: idioma espaol a 24 de noviembre de 2020: 
 Se mostraran los botones con los siguientes labels 
 Socio / CEO / Propietario 
 Direccin de marketing 
 Direccin de logstica 
 Direccin de ventas 
 Direccin de sostenibilidad 
 Direccin de operaciones 
 Profesional ambiental 
 Profesional de RSE 
 Profesional de logstica 
 Direccin de compras 
 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id ={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro el valor eatc_superadmin_profile. eatc_name 

 Ejemplo, continuando con el anterior 
 Si el usuario selecciona " Profesional de RSE " entonces eatc_internationalize_dt. eatc_data_id=8 por lo tanto al hacer la siguiente consulta: https://datagov.eatcloud.info/api/eatcloud/ eatc_superadmin_profile ?_id=8   al registro se llevara el valor "eatc_superadmin_profile. eatc_name " = "profesional_rse" 

 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda con :  
https://datagov.eatcloud.info/crd/eatcloud/?tabla=bo_usuarios&_operacion=update& eatc_user_profile ={{ eatc_superadmin_profile. eatc_name }}&WHEREid={{bo_usuarios. id }} 

 Al realizar la seleccin el sistema lo debe pasar a la siguiente pantalla del flujo de onboarding. 

 Tamao de la cuenta 

 Primera sesin del usuario superadmin paso D 
 Nota importante de implementacin: en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Botones para la seleccin del tamao de la cuenta: *** NUEVO : el label para internacionalizacin se toma del dato: eatc_cua_size_mt .eatc_code y eatc_cua_size_mt .eatc_description *** 

 El sistema desplegar una serie de botones (nube de botones) en dnde se mostrarn los diferentes tamaos de cuenta con su descripcin, segn la respectiva vertical (este rasgo difiere un poco de lo establecido en el diseo de pantalla arriba expuesto dado que los botones no muestran la descripcin y tampoco estn filtrados por vertical) que le aplican a la cuenta que se cre en los pasos previos. El usuario deber elegir uno de los tamaos y esta informacin se adjuntar en la informacin de la respectiva cuenta 

 Informacin tcnica del parmetro: eatc_cua. eatc_cua_size   
 Tipo de dato: string 
 Tipo de input: nube de botones: selector nico 
 La informacin del selector se toma de class={{ eatc_cua_size_mt . eatc_code }} concatenado con {{ eatc_cua_size_mt . eatc_description_lbl }} (se deber configurar para que los valores que se obtienen de la siguiente consulta, sean tratados como labels) 

 Consulta de tamaos segn la vertical: 
 {{ URL_entorno_datagov }} /api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= {{ eatc_cua.vertical }}&eatc_onboarding=1 &_distinct= eatc_code 

 {{ URL_entorno_datagov }} /api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= {{ eatc_cua.vertical }}&eatc_onboarding=1 &_distinct= eatc_description_lbl 

 Ejemplo en ambiente productivo, para la vertical "retail": 
 https://datagov.eatcloud.info//api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= retail&eatc_onboarding=1&_distinct= eatc_code 

 Dado que la respuesta del servicio es: 
 res :  
 [ 
 { 
 eatc_code : "little_retail" 
 }, 
 { 
 eatc_code : "medium_retail" 
 }, 
 { 
 eatc_code : "big_retail" 
 } 

 ], 

 https://datagov.eatcloud.info//api/eatcloud/ eatc_cua_size_mt? eatc_vertical_code= retail&eatc_onboarding=1&_distinct= eatc_description_lbl   

 Dado que la respuesta del servicio es: 
 res :  
 [ 
 { 
 eatc_description_lbl : "little_retail_desc" 
 }, 
 { 
 eatc_description_lbl : "medium_retail_desc" 
 }, 
 { 
 eatc_description_lbl : "big_retail_desc" 
 } 

 ], 

 Entonces los selectores se deben popular con los siguientes labels: 
 class=" little_retail " - class=" little_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=little_retail  - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=little_retail_desc   
 class=" medium_retail " - class=" medium_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=medium_retail    - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=medium_retail_desc    
 class=" big_retail " - class=" big_retail_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=big_retail    - https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=big_retail_desc    

 DEPRECADO: 
 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 

 ***NUEVO: Paso 2: consulta de los tamaos para la vertical de la cuenta respectiva (con su respectiva descripcin):  
 En el proceso de creacin de la cuenta se estableci la vertical de la misma . Con este dato se debe realizar la consulta al maestro de tamaos para traer los tamaos y sus descripciones, que le aplican a la cuenta particular. 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_size_mt?eatc_vertical_code={{eatc_cua. vertical }} 
 El sistema toma el array de valores del parmetro eatc_cua_size_mt . _id para realizar la siguiente consulta 

 ***NUEVO: Paso 3: consulta de los tamaos en datos internacionalizados 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language={{codigo_dos_digitos_idioma}}&eatc_mt= eatc_cua_size_mt & eatc_data_id={{array( eatc_cua_size_mt . _id)}} 
 Ejemplo: idioma espaol para la vertical "retail" a 24 de noviembre de 2020: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_size_mt?eatc_vertical_code=retail   
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_language=es&eatc_mt=eatc_cua_size_mt&eatc_data_id=1,2,3 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto (ingls=en idioma por defecto): 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt= eatc_cua_size_mt &eatc_language= en &eatc_data_id= {{array( eatc_cua_size_mt. _id)}} 
 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en los botones: {{eatc_name}}: {{eatc_description}} 
 Ejemplo: idioma espaol a 24 de noviembre de 2020, vertical retail: 
 Se mostraran los botones con los siguientes labels 
 Pequea cadena: Cadena de retail de 1 a 10 tiendas 
 Mediana cadena: Cadena de retail de 11 a 100 tiendas 
 Gran cadena: Cadena de retail de ms de 100 tiendas 
 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_size_mt?_id={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro el valor eatc_cua_size_mt. eatc_code 

 Ejemplo, continuando con el anterior 
 Si el usuario selecciona " Gran cadena " entonces eatc_internationalize_dt. eatc_data_id= 3 por lo tanto al hacer la siguiente consulta: https://datagov.eatcloud.info/api/eatcloud/eatc_cua_size_mt?_id=3   al registro se llevara el valor " eatc_cua. eatc_cua_size " = " big_retail " 

 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_cua_size ={{ eatc_cua_size_mt. eatc_code }} 
 Se guarda con :  
https://datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_cua&_operacion=update& eatc_cua_size ={{ eatc_cua_size_mt. eatc_code }}&WHEREname={{_DOM. cua_user }} 

 Al realizar la seleccin el sistema lo debe pasar a la siguiente pantalla del flujo de onboarding. 

 Captura de datos bsicos del cliente 
 Primera sesin del usuario superadmin paso E 
 Nota importante de implementacin (implementar internacionalizando): 
   en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Tener en cuenta esta funcionalidad al realizar la implementacin (con el nimo de reutilizar) 
 En el BO de cuentas en Datagov existir la funcionalidad: configura tu empresa .  Al realizar esta implementacin de debe realizar pensando cmo reutilizar el cdigo en la implementacin de la otra funcionalidad, con el nimo de tener una implementacin eficiente (esto puede implicar segn criterio del programador, implementar primero la funcionalidad del BO de cuentas, que la del Onboarding, por ejemplo). 

 Consulta previa antes de realizar el registro ***NUEVO: simplificacin consultas con " fielddecrypt" de la funcin "getcrypt" y label cuando hay registros*** 

 El sistema debe realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue={{eatc_cua. name }}&fielddecrypt= eatc_cua,eatc_customer_fiscal_id 

 Con el nimo de establecer si ya existe un registro previo de cliente para la cuenta registrada. 

 Si la consulta no trae datos, se procede a desplegar el formulario de captura de datos del cliente .  

 Si la consulta trae datos, se debe tomar el dato recibido en eatc_customer_fiscal_id   y realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/crypt/eatcloud/getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id &fieldvalue={{ eatc_customer_fiscal_id }}&fielddecrypt=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email, eatc_number_of_employees 

 CON LA CONSULTA SE OBTIENEN LOS DATOS desencriptados DEL CLIENTE Y SE PROCEDE A  mostrarlos en el formulario como prellenados avisndole al usuario que ya existe un registro de cliente asociado a la cuenta, dndole la oportunidad de editar o cambiar el registro del cliente. 

 El aviso se realiza colocando el siguiente label: 
 class=lbl_cuenta_con_cliente_asociado ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_cuenta_con_cliente_asociado ) 

 "La cuenta ya cuenta con un registro de cliente asociado.  Por favor revise o edite los datos del registro existente que le presentamos a continuacin" 

 Ejemplo 1 entorno de pruebas: la consulta no trae datos: eatc_cua. name=cualquiercosa2 

 La consulta entonces sera: 
 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue= cualquiercosa2 &fielddecrypt= eatc_cua,eatc_customer_fiscal_id   

 El sistema trae la siguiente respuesta que indica que no hay datos registrados: 
 { 
 ts : "210722164651" , 
 op : true , 
 cont : 0 , 
 err_msg : "No se produjeron resultados" , 
 err_num : "" , 
 mem : 0.41 , 
 time : "00:00:00" 
 } 

 En este caso (la consulta  no trae datos) entonces el sistema le despliega al usuario el  formulario de captura para obtener los datos del cliente . 
 Ejemplo 2 entorno de pruebas: la consulta trae datos: eatc_cua. name=exito 

 La consulta entonces sera: 

 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue= exito &fielddecrypt= eatc_cua,eatc_customer_fiscal_id   
 Con esto se obtiene el valor desencriptado de eatc_customer_fiscal_id y con l se procede a realizar la siguiente consulta 
 https://dev.datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id &fieldvalue=890900608&fielddecrypt=eatc_fiscal_id,eatc_fiscal_name,eatc_address,eatc_phone,eatc_email, eatc_number_of_employees   
 El sistema despliega el siguiente aviso: 

 " La cuenta ya cuenta con un registro de cliente asociado.  Por favor revise o edite los datos del registro existente que le presentamos a continuacin " 

 Y con los datos obtenidos se popula el siguiente formulario permitiendo la edicin de los mismos, con las respectivas validaciones. 

 FORMULARIO DE CAPTURA DE DATOS DEL CLIENTE 
 Los siguientes datos se guardan encriptados (utilizando los servicios de encripcin de la plataforma) 

 Con el nimo de proteger la informacin privada y confidencial que se recolecta de los clientes. 

 Pas (captura oculta): 
 Informacin tcnica del parmetro: eatc_customer. eatc_country 
 Tipo de dato: string 
 Tipo de input: oculto 
 La informacin del selector se toma de: eatc_cua. eatc_country 
 Obligatoriedad : si 
 Se guarda en (para efectos indicativos, no prcticos) :  
 https://datagov.eatcloud.info/api/eatcloud/eatc_customer?eatc_country={{ eatc_cua. eatc_country } 

 Identificacin tributaria / fiscal ( ***NUEVO: cambiar label para que se muestre nombre internacionalizado, place holder informativo del formato y validacin de formato ** ) 
 class=" lbl_identificacion_tributaria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_identificacion_tributaria     

 Por ejemplo en Espaa se debe mostrar este label https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&pais=es&idlabel=lbl_identificacion_tributaria   

 ***NUEVO: Placeholder con informacin del formato  
 Se puede colocar abajo del campo, como se hace actualmente en el formulario de registro de gestores de donacin: ejemplo: campo "Cdigo de identificacin fiscal": https://devbeneficiarios.eatcloud.info/_registro/index.html?esp 
 class=" lbl_numero_identificacion_tributaria_desc ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=lbl_numero_identificacion_tributaria_desc       
 Por ejemplo en Espaa se debe mostrar este label https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&pais=es&idlabel=lbl_numero_identificacion_tributaria_desc     
 Informacin tcnica del parmetro: eatc_customer. eatc_fiscal_id 
 Tipo de dato: string 
 Tipo de input: number input. (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad, unicidad por pas (en un mismo pas eatc_customer. eatc_country , no deben existir dos identificaciones fiscales iguales (si se requiere, se debe validar la unicidad en el registro sin incorporar el pas).   

 ***NUEVO: Validacin de nmero de dgitos del eatc_fiscal_id   y el tipo de dato*** 
 Adicional a las anteriores validaciones implementadas para el eatc_fiscal_id se deber implementar una para que en la cuenta maestra respectiva se valide el nmero de dgitos (mnimo y mximo) que contiene dicho indentificador (con el nimo de obtener calidad de datos). 

 Para ello se deber consultar datos de configuracin de la cuenta maestra respectiva y a partir de dicha consulta realizar la validacin respectiva. La consulta es la siguiente: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua={{CUA_master}} 

 Esta consulta trae los datos: 

 eatc_doma_id_min_digit_val: que corresponder al nmero mnimo de dgitos que debe contener el eatc_fiscal_id que se ingresa en el formulario. Si el identificador ingresado por el usuario tiene menos dgitos que los indicados en este dato, no se permitir realizar el registro. 

 eatc_doma_id_max_digit_val: que corresponder al nmero mximo de dgitos que debe contener el eatc_fiscal_id que se ingresa en el formulario. Si el identificador ingresado por el usuario tiene ms dgitos que los indicados en este dato, no se permitir realizar el registro. 

 eatc_doma_id_datatype: que corresponder al tipo dato del eatc_fiscal_id que se ingresa en el formulario. Si el identificador ingresado por el usuario tiene un tipo de dato diferente, no se permitir realizar el registro. 

 Ejemplo: 
 Para la CUA_master: abaco, en entorno productivo se debe realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco   

 Como la misma trae los siguientes valores: 

 eatc_doma_id_min_digit_val: "9". 
 eatc_doma_id_max_digit_val: "9" 
 eatc_doma_id_datatype " integer " . 

 Esto quiere decir que en campo de captura respectivo no pueden identificadores con menos de 9 y ms de 9 dgitos (es decir solo se aceptan identificadores de 9 dgitos) y debe ser numrico. 

 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_fiscal_id ={{ input }} 

 Razn social 
 Informacin tcnica del parmetro: eatc_customer. eatc_fiscal_name 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_fiscal_name ={{ input}} 

 Direccin 
 Informacin tcnica del parmetro: eatc_customer. eatc_address 
 Tipo de dato: string 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_address ={{ input }} 

 Ciudad (no est en el diseo) 
 Informacin tcnica del parmetro: eatc_customer. eatc_city 
 Tipo de dato: string 
 Tipo de input: Selector nico con texto predictivo 
 De dnde se toman los datos del selector: 
 A partir de la seleccin anterior se debe realizar la siguiente consulta 
 https://datagov.eatcloud.info/api/{{eatc_cua. eatc_country }}/eatc_municipalities?_id=_* 

 El sistema debe colocar en el selector una sola vez cada ciudad - provincia , por lo tanto se debe hacer distinct sobre el dato eatc-city - eatc-province (estos datos son los que se muestran en el selector / teclado predictivo) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda  en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_city ={{ input }} 
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_province ={{ input }} 

 Telfono 
 Informacin tcnica del parmetro: eatc_customer. eatc_phone 
 Tipo de dato: string 
 Tipo de input: phone input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_phone ={{ input }} 

 E-mail notificaciones (en vez de usuario responsable) 
 Informacin tcnica del parmetro: eatc_customer. eatc_email 
 Tipo de dato: email 
 Tipo de input: text input (se guarda encriptado) 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad, email 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_email ={{ input }} 

 Nmero de empleados 
 Informacin tcnica del parmetro: eatc_customer. eatc_number_of_employees   
 Tipo de dato: string 
 Tipo de input: selector nico (se guarda encriptado) 
 Opciones del selector :  
 1 - 3 
 4 - 20 
 21 - 100 
 101 - 500 
 501 - 1500 
 1501 - 5000 
 Ms de 5000 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 Se guarda ENCRIPTADO en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? eatc_number_of_employees ={{ input }}} 

 Fecha y hora de creacin (captura oculta de timestamp): 
 Informacin tcnica del parmetro: eatc_customer. creation_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp (oculto) 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? creation_datetime ={{ current_datetime }} 

 Fecha y hora de ltima modificacin (captura oculta de timestamp): 
 Informacin tcnica del parmetro: eatc_customer. last_modification_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp (oculto) 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? last_modification_datetime ={{ current_datetime }} 

 Fecha de ltima modificacin (captura oculta de datestamp): 
 Informacin tcnica del parmetro: eatc_customer. last_modification_date 
 Tipo de dato: date 
 Tipo de input: datestamp (oculto) 
 Valor por defecto: fecha actual 
 Obligatoriedad : si 
 Validacin : obligatoriedad  
 Se guarda en (para efectos indicativos, no prcticos) :  
datagov.eatcloud.info/api/eatcloud/eatc_customer? last_modification_date ={{ current_date }} 

 Guardado de la relacin eatc_customer con eatc_cua (captura oculta) 
 La relacin entre el cliente y la cuenta se guardar en una tabla a parte ( eatc_customer_cua ), con el nimo de otorgar flexibilidad. En principio solo podr existir un registro por eatc_cua   

 Para crear el registro se utiliza el siguiente servicio: 
 https://datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_customer_cua &_operacion=insert& eatc_country= {{eatc_cua. eatc_country }} &eatc_customer_fiscal_id= {{eatc_customer. eatc_fiscal_id }}& eatc_cua ={{eatc_cua. name }} 

 Como el dato se debe guardar encriptado, se procede a realizar el siguiente llamado para encriptar: 
 https://datagov.eatcloud.info/crypt/eatcloud/encrypt?table=eatc_customers_cua&fieldname=eatc_customer_fiscal_id,eatc_cua 

 Integracin con ERP  
 Se proceder a realizar el llamado al servicio de integracin respectivo : 
 https://datagov.eatcloud.info/int/eatcloud/int_erp_alegra?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 Integracin con CRM  
 Se proceder a realizar el llamado al servicio de integracin respectivo : 
 https://datagov.eatcloud.info/int/eatcloud/int_crm_freshworks?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 Integracin con RDStation (marketing automation platform) 
 Se proceder a realizar el llamado al servicio de integracin respectivo : 
 https://datagov.eatcloud.info/int/eatcloud/int_mat_rdstation?eatc_customer={{eatc_customers. eatc_fiscal_id }}&_operacion= insert 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-b%C3%A1sica-de-cuentas%2F3933051897-EmbeddedImage--51-.jpg&ow=1280&oh=824, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-b%C3%A1sica-de-cuentas%2F3933051897-EmbeddedImage--51-.jpg&ow=1280&oh=824 

 286.000000000000 

 CONFIGURACIN BSICA DE CLIENTE Y CUENTA