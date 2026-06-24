# autenticación-segura-eatc_doma_aut.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Seleccin automtica de cuenta maestra segn pas 
 El sistema debe, a partir de los servicios de localizacin que arrojan el pas en el cul se encuentra el dispositivo (cdigo de dos dgitos, cuyo maestro general se puede consultar aqu: iso2 ), determinar cul es la cuenta maestra que le corresponde, realizando la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country={{codigo_dos_digitos_pais}} 

 Si la consulta no arroja resultados, el sistema debe desplegar un mensaje: 
 "EatCloud no est disponible aun en tu pas.  Por favor conctate a nuestra pgina web ( https://eatcloud.com ) y redes sociales para informarte sobre nuestra cobertura" 

 Si la consulta entrega un resultado vlido, debe guardar el dato eatc_cua_master. eatc_cua , como _DOM. cua_master y el dato eatc_cua_master. eatc_country como _DOM. cua_master_country para futuras validaciones y consultas. 

 Ejemplo: 
 Un dispositivo utilizado en colombia ( co ) debe realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country=co 

 Por lo tanto el sistema guarda la siguiente informacin: 
 _DOM. cua_master=abaco 
 _DOM. cua_master_country=co 

 Chequeo de cuenta: 
 Una app de beneficiario debe tener una cuenta asociada (guardada en una variable o en un archivo de configuracin). 

 Con esta cuenta de usuario (en adelante"CUA"), se debe efectuar la siguiente validacin: 
 Se debe utilizar la siguiente API para el chequeo de cuenta https://beneficiarios.eatcloud.info/cuachk/[CUA]/   

 Ejemplo: 
 Para efecto del piloto todas las cuentas de los beneficiarios sern "abaco" por lo tanto la consulta que se debe realizar es: 
 https://beneficiarios.eatcloud.info/cuachk/abaco/   

 El API contesta con los datos bsicos de la cuenta a saber: 

 { 
 ts : "190912090528", 
 op : true, 
 cont : 1, 
 cua : "abaco", 
 objstr :  
 [ 
 "eatc_calification_tags", 
 "eatc_donation_managers", 
 "eatc_final_beneficiaries", 
 "eatc_odds_typolgy", 
 eatc_users 
 ], 
 mem : 0.68, 
 time : "00:00:00" 
 } 

 Lo que indica que es una cuenta vlida. 

 Si se hace una consulta con una cuenta no valida por ejemplo: https://beneficiarios.eatcloud.info/cuachk/abac/ 

 El API retorna: 
 { 
 ts : "190912090701", 
 op : false, 
 err_msg : "No existe informacin asociada a la cuenta de cliente (abac)", 
 err_num : "" 
 } 

 Metodologa de autenticacin 
 Con el dato _DOM.cua_master se debe proceder a realizar la autenticacin del usuario utilizando los siguientes llamados: 
   {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users?_campos  
   {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users?_id=_* 

 El usuario digita en el campo "nombre de usuario" su "correo_electronico"  y en el campo "contrasea" su "numero_cedula" . Con estos datos debe utilizar el API respectiva y realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users ?correo_electronico= {{valor}} &numero_cedula= {{valor}} 

 Ejemplo: _DOM.cua_master=abaco 
 El usuario Juan Carlos Buitrago, cuyo "correo_electronico" = direccion@abaco.org.co y "numero_cedula"= 8161174 , la consulta sera para una autenticacin correcta: 

 Ambiente productivo: https://beneficiarios.eatcloud.info/api/abaco/eatc_users?correo_electronico=direccion@abaco.org.co&numero_cedula=8161174 

 Consulta de reglas de timeouts  
 Al ingresar a la APP, el sistema debe realizar la siguiente consulta, para traer las reglas de timeouts: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_timeout_rules?_id=_*  

 El sistema deber guardar los datos en su persistencia local para operarlos con posterioridad. 

 Validacin del estado del beneficiario para entrar a la aplicacin ***NUEVO: permitir el ingreso de usuarios con estado pasivo *** 
 La aplicacin, cada vez que se desee ingresar a ella, deber validar si la organizacin a la cual pertenece el usuario, est activa o no ( eatc_state ), para dejarlo ingresar. 

 Para hacer la validacin el sistema deber realizar la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro={{identificador_unico_registro}}&eatc_state=activo, pasivo &_cont 

 Si la consulta trae una respuesta vlida ( count mayor que cero ), entonces el usuario puede ingresar a la App.  De lo contrario se debe mostrar el label 
 class= lbl_organizacion_inactiva . ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&idlabel=lbl_organizacion_inactiva ) 

 y no lo debe permitir entrar. 

 Ejemplo 1: Ambiente de pruebas 
 Un usuario de la organizacin con identificador_unico_registro=901163191, intenta hacer autenticarse en la plataforma. Al hacerlo el sistema realiza la siguiente consulta: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=901163191&eatc_state=activo&_cont   

 Como el sistema arroja esta respuesta: 

 { 
 ts : "210713150125" , 
 op : true , 
 cont : 1 , 
 res :  
 [ 
 { 
 count : "0" 
 } 
 ], 
 mem : 0.43 , 
 time : "00:00:00" 
 } 
 ( count : "0" ) Entonces la despliega el label class= lbl_organizacion_inactiva y no le permite ingresar. 

 Ejemplo 2: Ambiente de pruebas 
 Un usuario de la organizacin con identificador_unico_registro= 890103741 , intenta hacer autenticarse en la plataforma.  Al hacerlo el sistema realiza la siguiente consulta: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=890103741&eatc_state=activo&_cont    

 Como el sistema arroja esta respuesta: 

 { 
 ts : "210713150125" , 
 op : true , 
 cont : 1 , 
 res :  
 [ 
 { 
 count : 1 
 } 
 ], 
 mem : 0.43 , 
 time : "00:00:00" 
 } 
 ( count : "1" ) Entonces la aplicacin le permite al usuario seguir en el dashboard. 

 ***NUEVO: Validacin del tipo de usuario (transportador) para ocultarle funcionalidades *** 

 A nuevo tipo de usuario autenticado ( tipo_usuario =transportador ) no se le mostrar la nube de donaciones y se le restringirn funcionalidades en el dashboard de donacin (no podr realizar verificacin detallada de la donacin) 
 El sistema determinar si el usuario es de tipo transportador. 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users ?correo_electronico= {{usuario}} &numero_cedula= {{password}}& tipo_usuario =transportador &_cmp=tipo_usuario,correo_electronico,numero_cedula &_token=eb20a489e56e3294e66b2ffe4809ec40 

 En caso de tratarse un usuario de tipo " transportador ", el sistema deber restringirle el acceso a la nube, y por lo tanto deber mostrarle solamente estas funcionalidades (cuando ingresa a la aplicacin). 

 Ejemplo: ambiente de pruebas, cua_master= abaco , usuario= 5821495 , password= ASD123  

 https://devbeneficiarios.eatcloud.info/api/ abaco /eatc_users ?correo_electronico= 5821495 &numero_cedula= ASD123 & tipo_usuario =transportador &_cmp=tipo_usuario,correo_electronico,numero_cedula &_token=eb20a489e56e3294e66b2ffe4809ec40   

 Dado que el sistema trae una respuesta vlida, a este usuario se le restringen funcionalidades, como se detalla a continuacin. 

 Nota para el desarrollo: 
 Como se ver a continuacin se muestran dos perspectivas diferentes para el filtrado de las funcionalidades: funcionalidades a mostrar y funcionalidadades a ocultar.  Se solicita al desarrollador que aplique una u otra perspectiva procurando realizar el menor esfuerzo de desarrollo posible y me explico: por ejemplo para filtrar el men superior derecho (tres puntos) se puede utilizar la perspectiva de "ocultar" dado que solamente hay que ocultar un solo elemento de men a este tipo de usuario, mientras que para el filtro por estados, se puede utilizar la perspectiva de "mostrar", dado que solamente hay que mostrarle las donaciones en estado "programadas" mientras que el resto de estados hay que "ocultarlos" 

 Funcionalidades a mostrale al usuario tipo "transportador" 
 Dashboard principal de la app (con los respectivos mensajes de la APP) 
 Menu superior izquierdo (tres puntos) 
 Nombre de la organizacin 
 Nombre del usuario 
 Info. Organizacin 
 Tutoriales 
 Mesa de ayuda 
 Preguntas frecuentes 
 Reportar caso de soporte 
 Info App 
 Salir 
 Mis donaciones 
 Por gestionar 
 Filtro por estado: Solo se podrn mostrar donaciones "programadas" 
 Programadas ( solo se le podrn mostrar donaciones programadas y que estn asignadas al trasportador autenticado en la plataforma ) 
 Dashboard de donacin (adjudicada) 
 Men superior izquierdo donacin (tres puntos) 
 Ver cdigo de recogida 
 Llegu al punto de donacin 
 Chequear donacin recogida 
 Registrar salida punto donacin 
 Problemas con la entrega 
 Califica al donante 

 Funcionalidades a ocultarle al usuario tipo "transportador" 
 Nube de donaciones 
 Del men superior derecho (tres puntos), que se muestra, no se debern mostrar los siguientes submens 
 Crear Beneficiario Final 
 De Mis donaciones (que se muestra) no se deber mostrar 
 Ms donaciones 
 De "por gestionar"  que se muestra, no se deber mostrar 
 Fitro por estado  (se debe mostrar, pero de este filtro no se podrn mostrar las siguientes opciones:) 
 Anunciados 
 Adjudicados 
 Certificados 
 Despachados 
 Precertificados 
 Recibidos (verificados) 
 No entregados 
 Cancelados 
 Por verificar 
 No se podrn mostrar las donaciones que no estn  se le adjudicaron como recolector al usuario autenticado 
 Del men superior  del dashboard de donaciones (que se muestra) no se muestran los siguientes submens 
 No me interesa 
 Me interesa 
 Programar 
 Reprogramar 
 Recolector adicional 
 Verifica tu donacin 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 509.000000000000 

 AUTENTICACIN SEGURA: EATC_DOMA_AUT