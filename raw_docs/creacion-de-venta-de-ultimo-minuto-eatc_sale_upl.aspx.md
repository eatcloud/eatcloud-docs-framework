# creacion-de-venta-de-ultimo-minuto-eatc_sale_upl.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Esta funcionalidad se basa en la ya desarrollada "Creacin de anuncio de donacin", pero apunta a estructuras de datos diferentes y tiene algunas capturas de datos diferentes.  Para sealar estas diferencias se utilizar la notacin [***] para indicar que hay un cambio con respecto a la funcionalidad base y [+++] cuando hay algo diferente a la funcionalidad base. 

 CREACIN DE LA OFERTA 
 [***NUEVO****] Seleccin de tiempo de vida de la oferta (antes de la validacin de existencia de horario de venta). 
 El sistema, antes de validar la existencia de un horario de venta, deber preguntar cual es el tiempo de vida de la oferta ( eatc-offer_lifetime ) de una manera muy ilustrativa y didctica, que sirva para explicar al usuario nuestro modelo de negocio y trabajo. El dato obtenido de esta seleccin, servir para la validacin de existencia de horario de venta, y posteriormente se llevar a las estructura eatc_sale , dado que a partir de su informacin el sistema realizar operaciones de transformacin de ofertas en anuncios de donacin y tambin posteriormente acciones de informativas a usuarios que a partir de estas ofertas realizan un pedido. 

 El sistema deber desplegar el siguiente mensaje:  

 Por favor selecciona el tiempo de vida de tu oferta 

 A continuacin se debe desplegar un selector nico (similar al selector que se coloc para tipificar si la venta de ltimo minuto es de un producto nuevo, uno existente o unto tipo box) que debe se debe construir a partir de la informacin de la siguiente consulta:  
 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout 

 En el selector se deber mostrar la siguiente informacin (similar al selector que se coloc para tipificar si la venta de ltimo minuto es de un producto nuevo, uno existente o unto tipo box), a partir de los datos de la consulta: 

                                      Oferta de ltimo minuto de vida {{eatc-offer_lifetime}} 
                                                     {{eatc-timeout_in_hours}} horas de tiempo de vida 
                                                     {{ eatc-timeout_description }} 

 Cuando se selecciona una opcin, se deber guardar la informacin del parmetro eatc_sale_timeout_rules. eatc-offer_lifetime , el cual se deber guardar para luego ser incorporado en el parmetro eatc_sale. eatc-offer_lifetime y tambin se debern guardar los parmetros  eatc_sale_timeout_rules. eatc-timeout_in_minutes y eatc_sale_timeout_rules. eatc-timeout_in_hours para realizar la validacin de horario de venta. 
 Ejemplo (ambiente de pruebas): 
 Con los datos cargados a 21 de septiembre de 2020, los selectores deben construirse con la informacin que arroja la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout   

 Y por lo tanto el selector nico deber contener la siguiente informacin: 

 Se guarda el dato de las horas de tiempo de vida para llevarlo posteriormente a eatc_sale.eatc-offer_lifetime 
 Si por ejemplo el usuario selecciona la primera opcin, entonces el dato " corta " (eatc_sale_timeout_rules. eatc-offer_lifetime ) ser guardado para ser llevado posteriormente a los datos de la oferta en el parmetro: eatc_sale. eatc-offer_lifetime la informacin correspondiente a eatc_sale_timeout_rules. eatc-timeout_in_hours es decir: 

 eatc_sale. eatc-offer_lifetime = 10 

 [***MODIFICADO***] Validacin de existencia de horario de venta. 
 A partir de la informacin seleccionada en el anterior selector , el sistema deber validar si existe un horario de venta disponible segn el tiempo de vida de la oferta ( eatc_sale_timeout_rules. eatc-timeout_in_minutes y eatc_sale_timeout_rules. eatc-timeout_in_hours )  similar a la validacin de horarios de atencin pero apuntando a un nuevo object store: 

 [***] 

 {{URL_entorno}} /api/ {{cua_user}} /eatc_sale_schedule?eatc-pod_id= {{eatc-pod_id}} 

 Pruebas : https://devdonantes.eatcloud.info/api/ {{cua_user}} /eatc_sale_schedule?eatc-pod_id= {{eatc-pod_id}} 

 Productivo : https://donantes.eatcloud.info/api/ {{cua_user}} /eatc_sale_schedule?eatc-pod_id= {{eatc-pod_id}} 

 Si existe un registro asociado al punto, se pasa a la siguiente validacin: Horario de venta disponible antes del rango de transformacin de la oferta en anuncio . 

 Si no existe un registro asociado al punto. 

 Ejemplo: un punto de donacin, cuyo eatc-pod_id es 777, realiza la consulta (en ambiente de pruebas):  
 [***] 
 https://devdonantes.eatcloud.info/api/exito/eatc_sale_schedule?eatc-pod_id=777 el resultado de la misma es: 
{ 
 ts : "200504094733", 
 op : true, 
 cont : 0, 
 err_msg : "No se produjeron resultados", 
 err_num : "", 
 mem : 0.39, 
 time : "00:00:00" 
} 

 Por lo tanto se debe  desplegar el siguiente mensaje: 

 El punto de donacin no tiene horarios de [***] venta asociados, por favor ingresa a la funcionalidad [***] " horarios de venta " para configurarlos 

 El sistema debe proporcionar un vnculo para ingresar a la funcionalidad [***] horarios de venta , y no debe permitir al usuario hacer un registro de anuncio de donacin, hasta que el punto de donacin no tenga horarios de atencin registrados y que cumpla con la siguiente validacin. 

 Validacin de horario de venta disponible antes del rango de transformacin de la venta en anuncio 
 Si existe un registro de horario de venta, el sistema debe validar que dicho horario empieza antes de que culmine el tiempo que se tiene establecido para transformar la oferta en un anuncio de donacin 
   [***]   

 {{URL_entorno_donantes}}/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout 

 Ambiente de pruebas: https://devdonantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout       

 Ambiente de productivo: https://donantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout     

 Si el inicio de por lo menos uno de los horarios de atencin registrados, no se encuentra antes del tiempo establecido en el Timeout, el sistema debe mostrar el siguiente anuncio: 

 El punto de donacin no tiene un horario de venta disponible antes del tiempo estipulado de {{eatc_sale_timeout_rules. eatc-timeout_in_hours que se obtuvo a partir del selector de tiempo de vida de la oferta }} horas para la realizacin de la venta de ltimo minuto. Por favor ingresa a la funcionalidad [***] horarios de venta para configurar un horario adecuado para una venta realizada en este momento. [***] Recuerde que en dicho horario se debe estar en disposicin de atender a quienes acrediten la compra de los productos a travs de EatCloud. 

 Este mensaje  debe impedir realizar el anuncio de donacin (es decir es un mensaje restrictivo como el anterior), y debe proporcionar un vnculo a la funcionalidad de [***] horarios de venta para hacer la configuracin.  

 [***] NO VA: Validacin de existencia de horarios de atencin por defecto 

 [***] Selector de ubicacin 
 Lo primero que se realizar antes de realizar una venta ser la visualizacin, y edicin de los datos correspondientes al punto de donacin, que funcionar de manera similar a como se implement en la funcionalidad de generacin de anuncio de donacin.  Esta funcionalidad Tiene un diseo diferente [***] al de edicin de la ubicacin actual y  debe permitir, cuando la cuenta as lo tenga configurado, editar coordenadas de puntos de donacin y generar nuevas coordenadas de punto.  En otras palabras, si evaluando la informacin de la cuenta respectiva (cua_user) ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua]), se establece que la cuenta est habilitada para editar coordenadas edit_coordinates=si ), deber aparecer el vnculo "Cambiar direccin" que dar entrada a la funcionalidad respectiva. 

 Informacin cuando no se edita el punto de donacin 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id): 

 Informacin tcnica del parmetro: eatc_pods.eatc-id y eatc_sale.eatc-pod_id   
 La informacin se toma de: 

 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: 39 

 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_id={{input}} 

 Nombre del punto de venta (se toma de eatc_pods.eatc-name): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-name 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: EXITO SAN ANTONIO 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_name={{input}} 
  Este dato se debe mostrar (pintar) en la interfaz de la APP y [+++] y se lleva tambin al object store de eatc_sale 

 Latitud del punto de venta (se toma de eatc_pods.eatc-lat): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat   
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-lat 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: 6.24683 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lat={{input}} 
   [+++] Este dato se lleva  al object store de eatc_sale 

 Longitud del punto de venta (se toma de eatc_pods.eatc-lat): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-lon 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: -75.566905 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lon={{input}} 
   [+++] Este dato se lleva  al object store de eatc_sale 

 Direccin del punto de venta (se toma de eatc_pods.eatc-adress): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se llevaba al object store de las donaciones pero ahora si se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-adress 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: Cl. 48 #46-115, Medelln, Antioquia 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_address={{input}} 
  Este dato se debe mostrar (pintar) en la interfaz de la APP y [+++] y se lleva tambin al object store de eatc_sale 

 Ciudad del punto de venta (se toma de eatc_pods.eatc-city): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-city 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: MEDELLIN 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_city={{input} 
   [+++] Este dato se debe mostrar (pintar) en la interfaz de la APP y se lleva tambin al object store de eatc_sale 

 Departamento / provincia / estado del punto de venta (se toma de eatc_pods.eatc-province): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-province y eatc_sale.eatc-pod_province [PENDIENTE DOCUMENTACIN] 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-province 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: ANTIOQUIA 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_province={{input} 

 Pas del punto de venta (se toma de eatc_pods.eatc-country): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} eatc-country 

 Ejemplo: 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   
 Es decir al {{input}} se lleva el valor: CO 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_country={{input}} 

 [+++] Nombre del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
  no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura con respecto a este dato ya que el mismo se toma desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito 
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= exito )   

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
  tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor   a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor : " Juan David Correa Toro ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si (si la cuenta maneja mltiples donantes) 
 Validacin : obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   

 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= exito ) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user }}) ) tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code : " 71745712 ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 Parmetros para editar informacin del punto de donacin (y guardarla en la persistencia eatc_pods), cuando se edita el nombre del donante y su identificacin para cuentas que manejen mltiples donantes 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos: 
 {{Parametros edicin en eatc_pods }}: eatc-donor ={{Nombre del donate}}& eatc-donor_code ={{Nit o identificacin del donate}} 
 [***] Cuando se termina de editar esta informacin 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods&_operacion=update&{{ Parametros edicin en eatc_pods}} &WHEREeatc-id={{ eatc_pods.eatc-id}} 

 Edicin de coordenadas del punto de donacin: 
 Despliegue de la funcionalidad 
 Si evaluando la informacin de la cuenta respectiva (cua_user) ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user }} (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}), se establece que la cuenta est habilitada para editar coordenadas edit_coordinates=si ), al lado de la direccin se debe desplegar un botn que permita editar/seleccionar una direccin para efectuar la donacin. 
 Ejemplo : 
 Para la cuenta "colombia" se evala su respectiva configuracin con el siguiente llamado:  

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=colombia) 

 Al comprobar que el parmetro " edit_coordinate " tiene como valor "si" se debe habilitar la funcionalidad para la cuenta en cuestin. 
 Edicin de coordenadas: 
 Al darle clic al botn, la plataforma debe evaluar si en la persistencia " eatc_pods_coordinates (NOTA PARA JDC: falta documentacin mtodo, parmetros) " para el "eatc_pod" respectivo existe informacin ( eatc_pods.eatc-id ), para mostrar las diversas direcciones guardadas en un selector (se muestra en el selector la direccin y su nombre, permitiendo traer las coordenadas respectivas, informacin que se terminar llevando a la informacin del respectivo eatc_pod).   
 Ejemplo : 
 Para el punto de donacin "nzzn1" de la cuenta "colombia" se tiene la siguiente informacin: 

 Ambiente de prueba: https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1 
 Ambiente productivo: https://donantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1   

 Por lo tanto se debe poder seleccionar una de las direcciones registradas (en etapas posteriores se debe poder operar este selector como un buscador) para desplegar la latitud y longitud determinada. 
 Tambin debe presentar la opcin de adicionar una nueva direccin, y para hacerlo se debe desplegar un mapa que coloque por defecto a eatc_lat y eatc_lon del eatc_pod respectivo (se debe reciclar lo implementado aqu: https://devdonantes.eatcloud.info/registro/colombia   para mayor informacin comunicarse con Ivn Daro Restrepo). La nica diferencia con las imgenes abajo dispuestas, es que debe existir un campo de captura adicional con la etiqueta " Nombre del punto de donacin " inmediatamente abajo de la direccin y que corresponde a la informacin que se encuentra en eatc_pods.eatc-name (en caso de que no halla un registro en eatc_pods_coordinates ) o eatc_pods_coordinates .eatc-name cuando se ha realizado una seleccin de las coordenadas registradas o en (ser un campo editable tipo text_field que reciba informacin tipo string) 

 [***] Visualizacin del mapa: primero mostrar el mapa y luego la direccin 
 A diferencia del diseo original del mapa en donde sala primero la direccin y luego el mapa (que modificaba la direccin), se debe poner primero el mapa y luego la direccin (como est actualmente en las funcionalidades de registro): 

 Al mover el PIN en el mapa se podr ir variando las coordenadas y la direccin (tal como lo hace la actual implementacin ejemplo https://devdonantes.eatcloud.info/regpdona/ ) . 
 Siempre se permitir editar la direccin que aparece a partir del la seleccin del PIN. Ciudad y Pas no permitirn ser editados, solo sern editables a partir de la seleccin el pin en el mapa. 

 Edicin de coordenadas del punto de donacin: se selecciona un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id): 
 Informacin tcnica del parmetro: eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de: 
 El proceso de login . 
 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_id={{input}} 

 Nombre del punto de venta (se toma de eatc_pods_coordinates y se lleva a eatc_pods.eatc-name y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Selector (nico): formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}} eatc-name 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector: 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH   

 Es decir, el selector debe tener los valores: oficina y casa. El valor que sea seleccionado se llevar al {{input}} respectivo y se guardar su _id para las posteriores consultas 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-name={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_name={{input}} 
 Latitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lat y se lleva a eatc_pods.eatc-lat y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-lat 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: 6.252699799631093 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lat={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lat={{input}} 

 Longitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lon y se lleva a eatc_pods.eatc-lon y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon   
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-lon 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: -75.59463315188623 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lon={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lon={{input}} 

 Direccin del punto de venta (se toma de eatc_pods_coordinates.eatc-adress y se lleva a eatc_pods.eatc-name y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-adress 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-adress={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_adress={{input}} 

 Ciudad del punto de venta (se toma de eatc_pods_coordinates.eatc-city y se lleva a eatc_pods.eatc-city y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-city 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-city={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_city={{input}} 

 Departamento del punto de venta (se toma el dato eatc_pods_coordinates.eatc-city y luego se lleva a eatc_pods.eatc-province y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province .  [pendiente documentacin] 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-province 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: ANTIOQUIA (pendiente de implementar el dato en el repositorio) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-province={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_province={{input}} 

 Pas del punto de venta (se toma de eatc_pods_coordinates.eatc-country y se lleva a eatc_pods.eatc-country y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-country 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: CO 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-country={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_country={{input}} 

 [+++] Nombre del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user }} (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}))   no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro    
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia     
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor : " Juan David Correa Toro ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si (si la cuenta maneja mltiples donantes) 
 Validacin : obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
 tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code : " 71745712 ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 Observaciones para la recogida (se toma de eatc_pods_coordinates.eatc-warning y se lleva a eatc_sale): 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato: string 
 Obligatoriedad : no 
 Validacin : ninguna 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-warning 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Primera observacin de prueba 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-warning={{input}} 

 Parmetros para editar informacin de coordenadas (y guardarla en la persistencia eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos: 

 {{Parametros edicin en eatc_pods }}: eatc-name ={{eatc-name}}& eatc-adress ={{Direccion}}& eatc-city ={{Ciudad}}& eatc-province ={{Departamento}}& eatc-adress ={{Direccion}}& eatc-lat ={{eatc-lat}}& eatc-lon ={{eatc-lon}}& eatc-name ={{eatc-name}}& eatc-country ={{pas}} eatc-donor ={{Nombre del donate}}& eatc-donor_code ={{Nit o identificacin del donate}} 

 [***] Cuando se termina de editar los datos de las coordenadas (seleccionando una opcin diferente a la almacenada en eatc_pods) 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods&_operacion=update&{{ Parametros edicin en eatc_pods}} &WHEREeatc-id={{ eatc_pods.eatc-id}} 

 Edicin de coordenadas del punto de donacin: se editan los datos un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id): 
 Informacin tcnica del parmetro: eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de: 
 El proceso de login . 

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_id={{input}} 

 Nombre del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-name luego a eatc_pods.eatc-name y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Selector (nico): formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}} eatc-name 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector: 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH   

 Es decir, el selector debe tener los valores: oficina y casa. El valor que sea seleccionado se llevar al {{input}} respectivo y se guardar su _id para las posteriores consultas 

 El usuario podr cambiar la informacin del dato seleccionado en el anterior selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-name={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-name={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_name={{input}} 

 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-lat 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: 6.252699799631093 

 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-lat={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lat={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lat={{input}} 

 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-lon 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: -75.59463315188623 

 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-lon={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lon={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lon={{input}} 

 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-adress 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 

 El usuario podr cambiar la informacin del dato seleccionado y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-adress={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-adress={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_adress={{input}} 

 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 

 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-city 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Medelln 

 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-city={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-city={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_city={{input}} 

 Departamento / provincia / estado del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-province luego a eatc_pods.eatc-province y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 

 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province , [pendiente documentacin] 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 

 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-province 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: ANTIQUIA (Pendiente de implementacin en datos) 

 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-province={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-province={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_province={{input}} 

 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 

 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 

 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-country 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: CO 

 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa. En una primera etapa solo se aceptarn ventas de Colombia, pero a futuro se debern incorporar nuevos pases) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-country={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-country={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_country={{input}} 

 [+++] Nombre del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
  tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor : " Juan David Correa Toro ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 

 Informacin tcnica del parmetro: eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si (si la cuenta maneja mltiples donantes) 
 Validacin : obligatoriedad (si la cuenta maneja mltiples donantes) 

 La informacin se toma de: 

 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
  no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code : " 71745712 ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-warning luego a eatc_sale.eatc-warning): 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato: string 
 Obligatoriedad : no 
 Validacin : ninguna 
 La informacin se toma de: 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta ):   

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-id={{current:eatc_pods.eatc-id}}&_id={{_id tomado de la seleccin anterior}} eatc-warning 

 Ejemplo: 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin " oficina " (_id= 17 ): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &_id =17    

 Por lo tanto el valor que se llevar al {{input}} respectivo es: Primera observacin de prueba 

 El usuario podr cambiar la informacin del dato que se despliega a partir del selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo y luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-warning={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-warning={{input}} 

 Parmetros para editar informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos: 

 {{Parametros edicin en eatc_pods_coordinates }} : eatc-city ={{Ciudad}}& eatc-province ={{Departamento}}& eatc-adress ={{Direccion}}& eatc-lat ={{eatc-lat}}& eatc-lon ={{eatc-lon}}& eatc-name ={{eatc-name}}& eatc-country ={{CO}}& eatc-warning= {{ OBSERVACIONES_PARA_LA_RECOGIDA }} 

 [***] Cuando se  terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates: 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods_coordinates&_operacion=update&{{ Parametros edicin en eatc_pods_coordinates}} &WHER_id={{ eatc_pods_coordinates._id}} 

 {{Parametros edicin en eatc_pods }}: eatc-name ={{eatc-name}}& eatc-adress ={{Direccion}}& eatc-city ={{Ciudad}}& eatc-province ={{Departamento}}& eatc-adress ={{Direccion}}& eatc-lat ={{eatc-lat}}& eatc-lon ={{eatc-lon}}& eatc-name ={{eatc-name}}& eatc-country ={{pas}} eatc-donor ={{Nombre del donate}}& eatc-donor_code ={{Nit o identificacin del donate}} 

 [***] Cuando se  terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods: 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods&_operacion=update&{{ Parametros edicin en eatc_pods}} &WHEREeatc-id={{ eatc_pods.eatc-id}} 

 Creacin de coordenadas del punto de donacin: se crea un nuevo punto en eatc_pods_coordinates 

 Identificador del punto de venta (se toma de eatc_pods.eatc-id): 
 Informacin tcnica del parmetro: eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de: 
 El proceso de login . 

 {{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-id={{current:eatc_pods.eatc-id}} 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_id={{input}} 

 Nombre del punto de venta (se despliega un campo de captura y luego se lleva eatc_pods_coordinates.eatc-name, a eatc_pods.eatc-name y a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-name={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-name={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_name={{input}} 

 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-lat={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lat={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lat={{input}} 

 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) : 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-lon={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-lon={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_lon={{input}} 

 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN), con posibilidad de editar la direccin que sugiere el mapa 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-adress={{input}} 
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-adress={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_adress={{input}} 

 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-city={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-city={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_city={{input}} 

 Departamento / provincia / estado del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-province luego a eatc_pods.eatc-province y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province [pendiente documentacin] 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-province={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-province={{input}} 

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_province={{input}} 

 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale): 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Campo de captura Tipo : Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-country={{input}}   
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-country={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-pod_country={{input}} 

 [+++] Nombre del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user }}) ) tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor : " Juan David Correa Toro ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes): 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro: eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si (si la cuenta maneja mltiples donantes) 
 Validacin : obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de: 
 CASO 1: 

 S i la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) 

 Como el resultado del parmetro multiple_donors es " no ", entonces no se debe mostrar ningn campo de captura. 

 Ejemplo 2: 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=makro) 

 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 

 CASO 2: 

 Si la cuenta respectiva en datagov ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) ) 
 tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code : " 71745712 ", esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 

 Ejemplo 2: 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro " si ") cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta "nombre del donante" de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods?eatc-donor={{input}} => cuando se edita o se crea esta informacin.  Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc- luego a eatc_sale): 
 Informacin tcnica del parmetro: eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato: string 
 Obligatoriedad : no 
 Validacin : ninguna 
 La informacin se toma de: 
 Campo de captura Tipo : Pregunta abierta ( Textarea ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 Se guarda en [+++] :  
{{URL_entorno}}/api/{{cua_user}}/eatc_pods_coordinates?eatc-warning={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-warning={{input}} 

 Parmetros para crear informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos: 

 {{Parametros creacin en eatc_pods_coordinates }} : eatc-city ={{Ciudad}}& eatc-province ={{Departamento}}& eatc-adress ={{Direccion}}& eatc-lat ={{eatc-lat}}& eatc-lon ={{eatc-lon}}& eatc-name ={{eatc-name}}& eatc-country ={{CO}}& eatc-warning= {{ OBSERVACIONES_PARA_LA_RECOGIDA }} 

 [***] Cuando se  terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates: 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods_coordinates&_operacion= insert &{{ Parametros edicin en eatc_pods_coordinates}} 

 {{Parametros edicin en eatc_pods }}: eatc-name ={{eatc-name}}& eatc-adress ={{Direccion}}& eatc-city ={{Ciudad}}& eatc-province ={{Departamento}}& eatc-adress ={{Direccion}}& eatc-lat ={{eatc-lat}}& eatc-lon ={{eatc-lon}}& eatc-name ={{eatc-name}}& eatc-country ={{pas}}& eatc-donor ={{Nombre del donate}}& eatc-donor_code ={{Nit o identificacin del donate}} 

 [***] Cuando se  terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods: 
 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_pods&_operacion=update&{{ Parametros edicin en eatc_pods}} &WHEREeatc-id={{ eatc_pods.eatc-id}} 

 Datos que se digitan en el encabezado (una sola vez por anuncio) 
 Documento soporte:  
 Campo de texto abierto que se despliega si se cumple la siguiente condicin: que en parmetro eatc_dona_upl tenga como valor "yes" **NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] ). En caso que el parmetro tenga como valor "no" no se debe desplegar campo de captura y se toma este dato como vaco (para posteriormente llevarlo al registro . 
 Informacin tcnica del parmetro:  eatc_sale.eatc-doc 
 Descripcin ( tooltip ) : Ingrese por favor un documento de soporte 
 Tipo : Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 Tipo de dato: string 
 Obligatoriedad : no 
 Regla obligatoriedad : no aplica 
 Validacin : ninguna 
 Se guarda en :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-doc={{input}} 
 Mtodo para guardar especfico (para efectos indicativos, no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-doc={{input}} 

 Encabezado: Datos generados por la APP: 
 Los datos de encabezado se toman y se muestran al iniciar la transaccin y se agregan a cada registro de detalle (eatc_dona).  Dichos datos son 
 Cdigo de la venta 
 [***] Debe funcionar exactamente igual como est funcionando el cdigo del anuncio de donacin y ser llamado de igual manera para facilitar la implementacin)   ( eatc-dona_header_code que corresponde a un identificador nico para la venta que se realizar).  Idealmente este cdigo deber contener el nombre de la cuenta [CUA], el cdigo del punto de donacin (eatc-pod_id) y una cadena (que puede ser el estampe de tiempo con milisegundos (AAAAMMDDHHMMSSMM). La nica diferencia es que esta informacin se lleva al object store eatc_sale 
 Informacin tcnica del parmetro:  eatc_sale.eatc-dona_header_code 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Lo genera el sistema de la misma manera como genera el cdigo para los anuncios de donacin. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-dona_header_code={{input}} 

 [****AJUSTE EN TIPO DE DATO****] Fecha actual: eatc-date_time 
 [***] Debe funcionar exactamente igual como est funcionando en anuncios de donacin, con la diferencia que se lleva al object store eatc_sale 
 Informacin tcnica del parmetro:  eatc_sale.eatc-date_time 
 Tipo de dato: datetieme (en formato AAAA-MM-DD HH:MM:SS) 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Lo genera el sistema a partir del current datetime. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-date_time={{input}} 

 Fecha actual: eatc-date_time_2 
 [***] Debe funcionar exactamente igual como est funcionando en anuncios de donacin, con la diferencia que se lleva al object store eatc_sale 
 Informacin tcnica del parmetro:  eatc_sale.eatc-date_time_2 
 Tipo de dato: date 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 Lo genera el sistema a partir del current date. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  

{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-date_time_2={{input}} 

 [NUEVO] eatc_cua_origin 
 Informacin tcnica del parmetro:  eatc_sale.eatc_cua_origin 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
   $DOM.cua_user //Cuenta desde la cual se genera el anuncio de donacin que corresponde a la cua_user de la WebApp. 

 [+++] Nit del donante (se toman de eatc_cua en datagov a excepcin de las cuentas mltiples como "colombia") ***NUEVO: SE TOMA LA INFORMACIN DE DATAGOV*** 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro:  eatc_sale.eatc_donor_code 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 

 La informacin se toma de: 

 CASO 1: multiple_donors=no: 
 S i la cuenta respectiva en datagov  
 ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{_DOM.cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) )  

 no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 

 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 Ejemplo 1: 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta: 

 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=exito) ) 

 Como el resultado del parmetro multiple_donors es " no ", entonces la informacin se toma de la siguiente consulta  

 ****NUEVO: CONSULTAS PARA OBTENER EL NIT DE DATAGOV****:  
 Primera consulta para obtener la relacin entre la cuenta y los datos del cliente 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue={{_DOM.cua_user}} 

  Con la respuesta obtenida se toma el _id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &fieldname= eatc_cua,eatc_customer_fiscal_id &&filterfield_1=_id&filtervalue_1={{ eatc_customers_cua._id }}  

 Con esto se obtiene el valor desencriptado de eatc_customer_fiscal_id   que es el que se guarda en eatc_sale. eatc_donor_code y tambin se utiliza para obtener el nombre del donante ms adelante 
 (ANTERIORMENTE: se toma de eatc_cua . customer__eatc_clientes__partyidentification https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua] ) 

 Ejemplo: CONSULTAS PARA OBTENER EL NIT DE DATAGOV:  
 Ejemplo _DOM. cua_user = exito 

 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname= eatc_cua &fieldvalue=exito    

 Dado que la respuesta es: 

 { 
 _id : "8", 
 eatc_country : "co", 
 ... 
 } 

  Con la respuesta obtenida se toma el _id=8 para realizar la siguiente consulta: 

 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &fieldname= eatc_cua,eatc_customer_fiscal_id &&filterfield_1=_id&filtervalue_1=8   

 Como eatc_customer_fiscal_id : " 890900608 ", el dato se lleva a eatc_sale. eatc_donor_code y se guarda para la prxima consulta 

 CASO 2: multiple_donors=si: 
 Si la cuenta respectiva en datagov 
 ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/ eatc_cua?name={{ _DOM. cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) )  
 tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer el dato guardado en eatc_pods. eatc-donor 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_pods?eatc-id={{eatc_pods. eatc_id }} 

 Ejemplo 1 (entorno de pruebas): 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code : " 71745712 ", esta informacin se lleva al registro 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor_code={{input}} 

 [+++] Nombre del donante (se toman de eatc_cua en datagov) *** NUEVO: consulta a datagov***** 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).  Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro:  eatc_sale.eatc-donor 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 

 La informacin se toma de: 

 CASO 1: multiple_donors=no: 
 S i la cuenta respectiva en datagov  
 ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{_DOM.cua_user}} 
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user}}) )  
 no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es " no " 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 

 ****NUEVO: CONSULTAS PARA OBTENER EL LA RAZN SOCIAL DE DATAGOV****:  
 Se toma el dato obtenido para eatc_customers_cua. eatc_customer_fiscal_id en la anterior consulta y se realiza esta 
 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id &fieldvalue={{eatc_customers_cua. eatc_customer_fiscal_id }} 
 Con el resultado de la consulta se toma el dato _id para realizar la siguiente consulta y obtener el eatc_fiscal_name 
 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &fieldname= eatc_fiscal_name &&filterfield_1= _id &filtervalue_1={{eatc_customers_cua. _id }} 
 Con esto se obtiene el valor desencriptado de eatc_fiscal_name   que es el que se guarda en eatc_sale. eatc_donor   

 (ANTERIORMENTE: se toma de eatc_cua . customer__eatc_clientes__partyidentification https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= [cua] ) 

 Ejemplo: CONSULTAS PARA OBTENER LA RAZN SOCIAL DE DATAGOV:  
 Ejemplo (retomando el ejemplo anterior ) 

 Como el dato que se obtuvo fue: eatc_customer_fiscal_id : " 890900608 " 

 Entonces se realiza la siguiente consulta: 

 https://datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id &fieldvalue= 890900608   

 Como la respuesta obtenida es 

 { 
 _id : "2", 
 eatc_country : "co", 
 eatc_fiscal_id : "bGlzbGJKSVMydE8xT3ZQa3ByZit3Zz09", 
 eatc_fiscal_name : "Sm95T1M5Z2hqYmlUb0JyM281YXpMSFBkOFFxdE05YnErTnIyUU1rNDRRQT0=", 
 ....."" 
 } 
 Con el resultado de la consulta se toma el dato _id para realizar la siguiente consulta y obtener el eatc_fiscal_name 

 https://datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &fieldname= eatc_fiscal_name &&filterfield_1= _id &filtervalue_1=2   

 dado que eatc_fiscal_name : "Almacenes xito S.A.", entonces el dato que se lleva al registro ( eatc_donor ) es " Almacenes xito S.A. ".   Este dato se debe mostrar (pintar) en la interfaz de la APP y se guarda para el registro. 
 . 

 CASO 2: multiple_donors=si: 
 Si la cuenta respectiva en datagov  

 ( ***NUEVO***   https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{cua_user}}   
( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name={{cua_user }}) ) 

 tiene registrado en el parmetro multiple_donors el valor " si ", el sistema debe traer el dato guardado en eatc_pods. eatc-donor 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_user }}/eatc_pods?eatc-id={{eatc_pods. eatc_id }} 

 Ejemplo 1: 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta: 

 ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia   
 ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name= colombia) 

 Como el resultado del parmetro multiple_donors es " si ", se debe proceder a realizar la siguiente consulta (ambiente de pruebas): 

 https://devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH   

 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor : " Juan David Correa Toro ", este es el valor que se lleva al registro 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-donor={{input}} 

 [+++] selector de tipo de venta:  

 En esta nuevo enfoque funcional se podrn seleccionar tres tipos de venta:  
 Producto Nuevo : genera todos los datos del producto y lo registra en dos object store: eatc_sale_prd_mstr y eatc_sale 
 Producto Existente : consulta los datos de eatc_sale_prd_mstr 
 Producto Box : consulta los datos de eatc_sale_prd_mstr para traer solamente aquellos cuya eatc-odd_typology_a= box 

 Tipo de venta: producto nuevo: 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto nuevo para la venta, y se establece su registro en los object stores correspondientes: eatc_sale_prd_mstr y eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Nombre del producto o artculo: 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr. eatc-odd_name y eatc_sale. eatc-odd_name 
 Orden en el formulario : 1 
 Descripcin ( tooltip ) : Ingresa por favor el nombre del producto o artculo a vender. 
 Tipo : Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-odd_name={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_name={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-odd_name={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_name={{input}} 

 Identificador del producto: 
 Funciona de manera similar a como lo hace en la creacin de anuncios de donacin, sugiriendo un identificador a partir del nombre del artculo que el usuario puede editar 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_id y eatc_sale.eatc-odd_id 
 Orden en el formulario : 2 
 Descripcin ( tooltip ) : Ingresa un identificador nico para el producto o artculo 
 Tipo : Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad, unicidad (no debe haber un eatc-odd_id similar en eatc_sale_prd_mstr) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-odd_id={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_id={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-odd_id={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_id={{input}}  

 Fotografa / Imagen del producto: 
 [+++] Nueva funcionalidad.  Se debe indagar con Ivn Daro Restrepo para reciclar cdigo que se desarroll para la funcionalidad de registro de gestor de donaciones (para la subida de RUT y Certificado de Cmara de Comercio).  Se debe concretar con Luis Carlos Correa la relacin de aspecto con la cual se debe subir la imagen 

 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_image y eatc_sale.eatc-odd_image 
 Orden en el formulario : 3 
 Descripcin ( tooltip ) : Sube una imagen o fotografa del producto 
 Tipo : subida (desde el dispositivo: File Input ) de imagen o toma de imagen con cmara del equipo. 
 Tipo de dato: string (se debe establecer con Ivn Daro Restrepo que informacin se lleva al registro: una URL absoluta, o URL relativa o simplemente el nombre del la fotografa subida (que debera nombrarse con el eatc-odd_id) 
 Obligatoriedad : si 
 Validacin : obligatoriedad, tamao: se debe limitar el tamao de las imgenes a un peso razonable para su manipulacin web (por ejemplo 2 Megas), para evitar sobrecarga del servidor y consultas muy pesadas en la App. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-odd_image={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_image={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-odd_image={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_image={{input}}  

 Descripcin: 
 [+++] Nueva funcionalidad. 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_description y eatc_sale.eatc-odd_description 
 Orden en el formulario : 4 
 Descripcin ( tooltip ) : Ingresa una descripcin del producto o artculo 
 Tipo : Pregunta abierta ( rea de texto ) ( informacin tcnica sobre el tipo de pregunta : PAT ) 
 Tipo de dato: string  
 Obligatoriedad : si 
 Validacin : obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-odd_description={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_description={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-odd_description={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_description={{input}} 

 Peso unitario del producto en KG (si necesita ingresar en gramos utilice decimales): 
 [***] Similar a la captura del peso unitario pero guardando en object stores diferentes 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_unit_weight_kg y eatc_sale.eatc-odd_unit_weight_kg 
 Orden en el formulario : 5 
 Descripcin ( tooltip ) : Ingresa el peso unitario del producto o artculo en Kilogramos.  Si requieres ingresarlo en gramos, utiliza nmeros decimales) 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : si 
 Validacin : obligatoriedad, diferente de cero, pesos excesivos (se pregunta por confirmacin si el peso unitario es superior a 20 KG) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-odd_unit_weight_kg={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-odd_unit_weight_kg={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_unit_weight_kg={{input}} 

 Porcentaje de impuesto al valor agregado aplicable al producto 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc_VAT_percentage y eatc_sale.eatc_VAT_percentage 
 Orden en el formulario : 6 
 Descripcin ( tooltip ) : Ingresa el impuesto al valor agregado aplicable al producto 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : no 
 Validacin : ninguna. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc_VAT_percentage={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc_VAT_percentage={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc_VAT_percentage={{input}} 

{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc_VAT_percentage={{input}} 

 Porcentaje de otros impuestos aplicables al producto 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-other_taxes_percentage y eatc_sale.eatc-other_taxes_percentage 
 Orden en el formulario : 7 
 Descripcin ( tooltip ) : Ingresa el porcentaje de otros impuestos aplicables al producto, como por ejemplo IMPOCONSUMO 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : no 
 Validacin : ninguna. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-other_taxes_percentage={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-other_taxes_percentage={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-other_taxes_percentage={{input}} 

{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-other_taxes_percentage={{input}} 

 Contiene alrgenos? 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-contains_alergens y eatc_sale.eatc-contains_alergens 
 Orden en el formulario : 8 
 Descripcin ( tooltip ) : Ingresa si el producto o artculo contiene substancias que pueden resultar alrgicas para ciertas personas. 
 Tipo : Seleccin nica (SI / NO) ( Select ) ( informacin tcnica sobre el tipo de pregunta : SLU ) 
 Tipo de dato: boleano  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr?eatc-contains_alergens={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-contains_alergens={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc-contains_alergens={{input}} 

{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-contains_alergens={{input}} 

 Fecha de caducidad de los artculos 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes: Para cada registro se debe de manera opcional , seleccionar la fecha ms prxima de vencimiento.  Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parmetro (eatc_sale. eatc-closer_expiration_date ) ser: 0000-00-00 . Si el usuario desea registrar una fecha, deber ingresar a un " date picker " o " selector de fechas " que presenta por defecto, como sugerencia de "fecha ms prxima de vencimiento" la sumatoria de la fecha actual ms el nmero que se encuentra en el parmetro  eatc_cua. days_before_expiration ( **NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] )) .  Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vaco o nulo, el valor por defecto que debe tomarse es "5", para realizar la sumatoria y asi sugerir la fecha .  El usuario podr modificar esa fecha sugerida, y el sistema no le permitir ingresar fechas anteriores al da actual ms 1 da. (solo se podrn ingresar fechas posteriores). El dato resultante (tipo fecha con formato AAAA-MM-DD) se deber guardar en el parmetro eatc_sale. eatc-closer_expiration_date 
 Informacin tcnica del parmetro: eatc_sale.eatc-closer_expiration_date 
 Orden en el formulario : 9 
 Descripcin ( tooltip ) : selecciona la fecha ms prxima de expiracin de los productos ofertados. 
 Tipo : Date Picker 
 Tipo de dato: date  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-closer_expiration_date ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-closer_expiration_date ={{input}} 

 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_min_sale_unit_price 
 Orden en el formulario : 10 
 Descripcin ( tooltip ) : Ingresa el precio de venta al pblico (incluyendo tarifas e impuestos) para promover la venta de ltimo minuto 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : si 
 Validacin : Obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  

{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_min_sale_unit_price ={{input}} 

 Porcentaje de descuento para venta de ltimo minuto (sirve para incentivar la compra) 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_max_discount 
 Orden en el formulario : 11 
 Descripcin ( tooltip ) : Ingresa el porcentaje descuento sobre el precio de venta al pblico real, que representa el precio de venta al pblico de ltimo minuto. El poder visualizar estos descuentos ayuda a estimular la compra. 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: integer  
 Obligatoriedad : no (en un futuro puede cambiar) 
 Validacin : no aplica (en un futuro puede cambiar) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_max_discount ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  

{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_max_discount ={{input}} 

 [Clculo oculto] Precio de venta al publico unitario (PVP: se calcula si se obtuvieron los dos datos anteriores) 
 [+++] Nuevo campo que se calcula a partir de las dos capturas anteriores 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_unit_price 
 Tipo de dato: float  
 Obligatoriedad : no (en un futuro puede cambiar) 
 Validacin : no aplica (en un futuro puede cambiar) 
 Cmo se calcula: 
 eatc-odd_unit_price - eatc-odd_max_discount *eatc-odd_unit_price = eatc-odd_min_sale_unit_price 

 eatc-odd_unit_price= eatc-odd_min_sale_unit_price /( 1-eatc-odd_max_discount ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_unit_price ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  

{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_unit_price ={{input}} 

 Cantidad de productos disponibles para la venta (la venta se realizar por unidades) 
 [***] Similar a la captura para anuncios de donacin (eatc-odd_original_quantity y eatc-odd_quantity) pero guardando en un object store diferente 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_original_quantity y eatc_sale.eatc-odd_quantity 
 Orden en el formulario : 12 
 Descripcin ( tooltip ) : Ingresa las cantidades del producto o artculo disponible para la venta. Recuerda que los artculos se vendern por separado. 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: integer  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. Mayor o igual que uno. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_original_quantity ={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_quantity ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert& eatc-odd_original_quantity ={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale_prd_mstr&_operacin=insert& eatc-odd_quantity ={{input}}  

 [Campo oculto] Estado del producto para la venta (eatc_state=sale) 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_state 
 Tipo de dato: string  
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Dado que el producto se oferta, se registra en el parmetro eatc_state el valor {{input}} "sale" 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_state =sale 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_state =sale 

 Cdigo del registro 
 Informacin tcnica del parmetro:  eatc_sale.eatc-code [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 La informacin se toma de: 
 la concatenacin de los datos " Identificador del producto " (eatc_sale. eatc-odd_id ) y " Cdigo de la venta " (eatc_sale. eatc-dona_header_code )  
 Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-code={{input}} 

 *****NUEVO****** [Campo oculto] tiempo de vida de la oferta  
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-offer_lifetime [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato: integer  
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Dado que se gener al seleccionar al principio de la creacin de la oferta su tiempo de vida til 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-offer_lifetime ={{eatc_sale_timeout_rules. eatc-timeout_in_hours }} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-offer_lifetime ={{eatc_sale_timeout_rules. eatc-timeout_in_hours }} 

 *****NUEVO****** [Campo oculto] fecha y hora de finalizacin de tiempo de vida de la oferta 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-offer_lifetime_until [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato: datetime  (AAAA-MM-DD HH:MM:SS) 
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Se le suma al dato eatc_sale. eatc-date_time las horas registradas en el dato anterior (tiempo de vida de la oferta) eatc_sale. eatc-offer_lifetime 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-offer_lifetime_until ={{eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours }} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-offer_lifetime_until ={{eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours }} 

 Venta producto nuevo: botn: "Agregar Producto": Parmetros para crear informacin de en eatc_sale_prd_mstr y en eatc_sale 
 [***] En trminos generales funciona de manera similar al proceso para agregar producto en la creacin de anuncios de donacin (incluyendo la aparicin en el listado, la validacin de que no se repita ni en el listado ni en lo que se registra, etc.) pero con dos diferencias: el object store en el cual se registra (que ahora ser eatc_sale de la cuenta "eatcloud") y que no se requerir llamar a un webservice adicional al final de la creacin para crear un "encabezado" (en proceso que esta funcionalidad solo crear detalles). 

 Al oprimir el botn agregar productos se realizan las siguientes operaciones de insercin en eatc_sale_prd_mstr y en eatc_sale: 
 {{Parametros creacin en eatc_sale_prd_mstr }} : eatc-odd_name ={{Nombre del producto}}& eatc-odd_id ={{input}}& eatc-odd_image ={{input}}& eatc-odd_description ={{input}}& eatc-odd_unit_weight_kg ={{input}}& eatc_VAT_percentage ={{input}}& eatc-other_taxes_percentage ={{input}}& eatc-contains_alergens ={{input}} 
 [***] Cuando se  terminan de crear los datos de los productos se realiza el siguiente llamado al CRD: 

 Mtodo POST https://devdonantes.eatcloud.info/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacion= insert & {{Parametros creacin en eatc_sale_prd_mstr }} 

 {{Parmetros creacin en eatc_sale }}: & eatc-pod_name ={{eatc-name}}&& eatc-pod_id ={{eatc-name}}& eatc-pod_lat ={{eatc-lat}}& eatc-pod_lon ={{eatc-lon}}& eatc-pod_adress ={{Direccion}}& eatc-pod_city ={{Ciudad}}& eatc-pod_country ={{CO}}& eatc-warning= {{ OBSERVACIONES_PARA_LA_RECOGIDA }}& eatc-doc ={{input}}& eatc-dona_header_code ={{input}}& eatc-date_time ={{input}}& eatc-date_time_2 ={{input}}& eatc-donor_code ={{input}}& eatc-donor ={{input}}& eatc-odd_name ={{Nombre del producto}}& eatc-odd_id ={{input}}& eatc-odd_image ={{input}}& eatc-odd_description ={{input}}& eatc-odd_unit_weight_kg ={{input}}& eatc_VAT_percentage ={{input}}& eatc-other_taxes_percentage ={{input}}& eatc-contains_alergens ={{input}}& eatc-closer_expiration_date ={{input}}& eatc-odd_min_sale_unit_price ={{input}}& eatc-odd_max_discount ={{input}}& eatc-odd_unit_price ={{input}}& eatc-odd_original_quantity ={{input}}& eatc-odd_quantity ={{input}}& eatc-odd_state =sale& eatc-code ={{input}}& eatc-offer_lifetime ={{input}}& eatc-offer_lifetime_until ={{input}} 

 [***] Se guarda la informacin en el object store eatc_sale de la cuenta eatcloud: 

 Mtodo POST https://devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&_operacion=insert& {{Parmetros creacin en eatc_sale }} 

 Tipo de venta: producto existente: 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto para la venta a partir de la seleccin de un producto ya existente en el maestro eatc_sale_prd_mstr, y se establece su registro en el object store correspondiente: eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Buscador de productos por nombre o por cdigo: 
 [***] Tal como funciona la para la creacin de anuncios de donacin, se debe desplegar un selector nico para establecer que tipo de bsqueda se realiza: si es por nombre (eatc-odd_name) o si es por codigo (eatc-odd_id). Dicha bsqueda se debe hacer contra el object store eatc_sale_prd_mstr (siendo esta la unica diferencia) 
 Segn sea el caso se utilizarn las siguientes consultas para popular los selectores: 
 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_name =_* 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id =_* 

 Ejemplo: cuenta "colombia", ambiente de pruebas: 

 https://devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_name =_* 

 https://devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_id =_* 

 Bsqueda por nombre del producto o artculo {{eatc_sale_prd_mstr.eatc-odd_name}}: 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr. eatc-odd_name y eatc_sale. eatc-odd_name 
 Descripcin ( tooltip ) : Ingresa por favor el nombre del producto o artculo a buscar. 
 Tipo : Texto predictivo con autocompletar 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_name={{eatc_sale_prd_mstr.eatc-odd_name}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_name={{eatc_sale_prd_mstr.eatc-odd_name}}  

 Bsqueda por identificador del producto {{eatc_sale_prd_mstr.eatc-odd_id}}: 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_id y eatc_sale.eatc-odd_id   
 Descripcin ( tooltip ) : Ingresa un identificador nico para el producto o artculo a buscar. 
 Tipo : Texto predictivo con autocompletar 
 Tipo de dato: string 
 Obligatoriedad : si 
 Validacin : obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_id={{eatc_sale_prd_mstr.eatc-odd_id}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_id={{eatc_sale_prd_mstr.eatc-odd_id}} 
 Tal como funciona la para la creacin de anuncios de donacin, se muestra el dato complementario segn sea el caso (nombre o identificador) y con el identificador respectivo se traen los datos que se pueden llamar recursivamente del object store eatc_sale_prd_mstr 

 Fotografa / Imagen del producto {{eatc_sale_prd_mstr.eatc-odd_image}}: 
 [+++] Nueva funcionalidad.  Se debe mostrar la imagen del producto que se est buscando. 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_image y eatc_sale.eatc-odd_image 
 Orden en el formulario : 3 
 Descripcin: no aplica 
 Tipo : imagen 
 Tipo de dato: string (se debe establecer con Ivn Daro Restrepo cmo se consultar este recurso para traerlo a la interfaz de la APP) 
 Obligatoriedad : si 
 Validacin : obligatoriedad, 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc-odd_image 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_image={{ eatc_sale_prd_mstr. eatc-odd_image}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_image={{ eatc_sale_prd_mstr. eatc-odd_image}} 

 Descripcin {{eatc_sale_prd_mstr.eatc-odd_description}}: 
 [+++] Nueva funcionalidad. Se debe mostrar la descripcin del producto o artculo 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_description y eatc_sale.eatc-odd_description   
 Orden en el formulario : 4 
 Descripcin ( tooltip ) : no aplica 
 Tipo :  texto 
 Tipo de dato: string  
 Obligatoriedad : si 
 Validacin : obligatoriedad. 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc-odd_description 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_description={{ eatc_sale_prd_mstr. eatc-odd_description}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_description={{ eatc_sale_prd_mstr. eatc-odd_description}} 

 Peso unitario del producto en KG {{eatc_sale_prd_mstr.eatc-odd_unit_weight_kg}}: 
 [***] Similar a la implementacin de creacin de anuncio de donacion pero solo traera informacin desde el repositorio eatc_sale_prd_mstr 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-odd_unit_weight_kg y eatc_sale.eatc-odd_unit_weight_kg 
 Orden en el formulario : 5 
 Descripcin ( tooltip ) : no aplica 
 Tipo : Texto 
 Tipo de dato: float  
 Obligatoriedad : si 
 Validacin : obligatoriedad, diferente de cero, pesos excesivos (se pregunta por confirmacin si el peso unitario es superior a 20 KG) 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc-odd_unit_weight_kg 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg={{ eatc_sale_prd_mstr. eatc-odd_unit_weight_kg}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-odd_unit_weight_kg={{ eatc_sale_prd_mstr. eatc-odd_unit_weight_kg}} 

 Porcentaje de impuesto al valor agregado aplicable al producto {{eatc_sale_prd_mstr.eatc_VAT_percentage}}: 
 [***] Similar 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc_VAT_percentage y eatc_sale.eatc_VAT_percentage 
 Orden en el formulario : 6 
 Descripcin ( tooltip ) : no aplica 
 Tipo : Texto 
 Tipo de dato: float  
 Obligatoriedad : no 
 Validacin : ninguna. 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc_VAT_percentage 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc_VAT_percentage={{ eatc_sale_prd_mstr. eatc_VAT_percentage}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert&eatc_VAT_percentage={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc_VAT_percentage={{ eatc_sale_prd_mstr. eatc_VAT_percentage}} 

 Porcentaje de otros impuestos aplicables al producto {{eatc_sale_prd_mstr.eatc-other_taxes_percentage}}: 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-other_taxes_percentage y eatc_sale.eatc-other_taxes_percentage 
 Orden en el formulario : 7 
 Descripcin ( tooltip ) : Ingresa el porcentaje de otros impuestos aplicables al producto, como por ejemplo IMPOCONSUMO 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : no 
 Validacin : ninguna. 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc-other_taxes_percentage 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-other_taxes_percentage={{ eatc_sale_prd_mstr. eatc-other_taxes_percentage}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-other_taxes_percentage={{ eatc_sale_prd_mstr. eatc-other_taxes_percentage}} 

 Contiene alrgenos? {{eatc_sale_prd_mstr.eatc-contains_alergens}}: 
 [+++] En este caso se traer desde el maestro eatc_sale_prd_mstr 
 Informacin tcnica del parmetro: eatc_sale_prd_mstr.eatc-contains_alergens y eatc_sale.eatc-contains_alergens 
 Orden en el formulario : 8 
 Descripcin ( tooltip ) : no aplica. 
 Tipo : Texto 
 Tipo de dato: boleano  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. 
 La informacin se toma de: 
 Consulta a partir de lo que trae el selector inicial: formado con la siguiente consulta de valores: 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_id ={{current:eatc_sale_prd_mstr. eatc-odd_id }} eatc-contains_alergens 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale?eatc-contains_alergens={{ eatc_sale_prd_mstr. eatc-contains_alergens}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert&eatc-contains_alergens={{ eatc_sale_prd_mstr. eatc-contains_alergens}} 

 Nota : De aqu en adelante funciona se manera similar al formulario de captura de informacin para productos nuevos: 

 Fecha de caducidad de los artculos 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes: Para cada registro se debe de manera opcional , seleccionar la fecha ms prxima de vencimiento.  Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parmetro (eatc_sale. eatc-closer_expiration_date ) ser: 0000-00-00 . Si el usuario desea registrar una fecha, deber ingresar a un " date picker " o " selector de fechas " que presenta por defecto, como sugerencia de "fecha ms prxima de vencimiento" la sumatoria de la fecha actual ms el nmero que se encuentra en el parmetro  eatc_cua. days_before_expiration ( **NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= {{cua_user}} ( anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=[cua] )) .  Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vaco o nulo, el valor por defecto que debe tomarse es "5", para realizar la sumatoria y asi sugerir la fecha .  El usuario podr modificar esa fecha sugerida, y el sistema no le permitir ingresar fechas anteriores al da actual ms 1 da. (solo se podrn ingresar fechas posteriores). El dato resultante (tipo fecha con formato AAAA-MM-DD) se deber guardar en el parmetro eatc_sale. eatc-closer_expiration_date 
 Informacin tcnica del parmetro: eatc_sale.eatc-closer_expiration_date 
 Orden en el formulario : 9 
 Descripcin ( tooltip ) : selecciona la fecha ms prxima de expiracin de los productos ofertados. 
 Tipo : Date Picker 
 Tipo de dato: date  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-closer_expiration_date ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-closer_expiration_date ={{input}} 

 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_min_sale_unit_price 
 Orden en el formulario : 10 
 Descripcin ( tooltip ) : Ingresa el precio de venta al pblico (incluyendo tarifas e impuestos) para promover la venta de ltimo minuto 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: float  
 Obligatoriedad : si 
 Validacin : Obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_min_sale_unit_price ={{input}} 

 Porcentaje de descuento para venta de ltimo minuto (sirve para incentivar la compra) 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_max_discount 
 Orden en el formulario : 11 
 Descripcin ( tooltip ) : Ingresa el porcentaje descuento sobre el precio de venta al pblico real, que representa el precio de venta al pblico de ltimo minuto. El poder visualizar estos descuentos ayuda a estimular la compra. 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: integer  
 Obligatoriedad : no (en un futuro puede cambiar) 
 Validacin : no aplica (en un futuro puede cambiar) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_max_discount ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_max_discount ={{input}} 

 [Clculo oculto] Precio de venta al publico (PVP: se calcula si se obtuvieron los dos datos anteriores) 
 [+++] Nuevo campo que se calcula a partir de las dos capturas anteriores 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_unit_price 
 Tipo de dato: float  
 Obligatoriedad : no (en un futuro puede cambiar) 
 Validacin : no aplica (en un futuro puede cambiar) 
 Cmo se calcula: 
 eatc-odd_unit_price - eatc-odd_max_discount *eatc-odd_unit_price = eatc-odd_min_sale_unit_price 

 eatc-odd_unit_price= eatc-odd_min_sale_unit_price /( 1-eatc-odd_max_discount ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_unit_price ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_unit_price ={{input}} 

 Cantidad de productos disponibles para la venta (la venta se realizar por unidades) 
 [***] Similar a la captura para anuncios de donacin (eatc-odd_original_quantity y eatc-odd_quantity) pero guardando en un object store diferente 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_original_quantity y eatc_sale.eatc-odd_quantity 
 Orden en el formulario : 12 
 Descripcin ( tooltip ) : Ingresa las cantidades del producto o artculo disponible para la venta. Recuerda que los artculos se vendern por separado. 
 Tipo : Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta : PAN ) 
 Tipo de dato: integer  
 Obligatoriedad : si 
 Validacin : Obligatoriedad. Mayor o igual que uno. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_original_quantity ={{input}} 
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_quantity ={{input}} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/{{cua_user}}/?_tabla=eatc_sale_prd_mstr&_operacin=insert& eatc-odd_original_quantity ={{input}} 
{{URL_entorno}}/api/eatcloud/?_tabla=eatc_sale_prd_mstr&_operacin=insert& eatc-odd_quantity ={{input}}  

 [Campo oculto] Estado del producto para la venta (eatc_state=sale) 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-odd_state 
 Tipo de dato: string  
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Dado que el producto se oferta, se registra en el parmetro eatc_state el valor {{input}} "sale" 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_state =sale 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-odd_state =sale 

 *****NUEVO****** [Campo oculto] tiempo de vida de la oferta  
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-offer_lifetime [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato: integer  
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Dado que se gener al seleccionar al principio de la creacin de la oferta su tiempo de vida til 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-offer_lifetime ={{eatc_sale_timeout_rules. eatc-timeout_in_hours }} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-offer_lifetime ={{eatc_sale_timeout_rules. eatc-timeout_in_hours }} 

 *****NUEVO****** [Campo oculto] fecha y hora de finalizacin de tiempo de vida de la oferta 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro:  eatc_sale.eatc-offer_lifetime_until [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato: datetime  (AAAA-MM-DD HH:MM:SS) 
 Obligatoriedad : si 
 Validacin : de obligatoriedad 
 Cmo se registra: 
 Se le suma al dato eatc_sale. eatc-date_time las horas registradas en el dato anterior (tiempo de vida de la oferta) eatc_sale. eatc-offer_lifetime 
 [+++] Se guarda en (para efectos indicativos, no prcticos) :  
{{URL_entorno}}/api/eatcloud/eatc_sale? eatc-offer_lifetime_until ={{eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours }} 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) :  
{{URL_entorno}}/crd/eatcloud/?_tabla=eatc_sale&_operacin=insert& eatc-offer_lifetime_until ={{eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours }} 

 Venta producto existente: Botn: "Agregar Producto": Parmetros para crear en eatc_sale 
 [***] En trminos generales funciona de manera similar al proceso para agregar producto en la creacin de anuncios de donacin (incluyendo la aparicin en el listado, la validacin de que no se repita ni en el listado ni en lo que se registra, etc.) pero con dos diferencias: el object store en el cual se registra (que ahora ser eatc_sale de la cuenta "eatcloud") y que no se requerir llamar a un webservice adicional al final de la creacin para crear un "encabezado" (en proceso que esta funcionalidad solo crear detalles). 

 {{Parmetros creacin en eatc_sale }}: & eatc-pod_name ={{eatc-name}}&& eatc-pod_id ={{eatc-name}}& eatc-pod_lat ={{eatc-lat}}& eatc-pod_lon ={{eatc-lon}}& eatc-pod_adress ={{Direccion}}& eatc-pod_city ={{Ciudad}}& eatc-pod_country ={{CO}}& eatc-warning= {{ OBSERVACIONES_PARA_LA_RECOGIDA }}& eatc-doc ={{input}}& eatc-dona_header_code ={{input}}& eatc-date_time ={{input}}& eatc-date_time_2 ={{input}}& eatc-donor_code ={{input}}& eatc-donor ={{input}}& eatc-odd_name ={{Nombre del producto}}& eatc-odd_id ={{input}}& eatc-odd_image ={{input}}& eatc-odd_description ={{input}}& eatc-odd_unit_weight_kg ={{input}}& eatc_VAT_percentage ={{input}}& eatc-other_taxes_percentage ={{input}}& eatc-contains_alergens ={{input}}& eatc-closer_expiration_date ={{input}}& eatc-odd_min_sale_unit_price ={{input}}& eatc-odd_max_discount ={{input}}& eatc-odd_unit_price ={{input}}& eatc-odd_original_quantity ={{input}}& eatc-odd_quantity ={{input}}& eatc-odd_state =sale& eatc-offer_lifetime ={{input}}& eatc-offer_lifetime_until ={{input}} 

 [***] Se guarda la informacin en el object store eatc_sale de la cuenta eatcloud: 
 Mtodo POST https://devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&_operacion=insert& {{Parmetros creacin en eatc_sale }} 

 Tipo de venta: producto box: 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto para la venta a partir de la seleccin de un producto ya existente en el maestro eatc_sale_prd_mstr, y se establece su registro en el object store correspondiente: eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Funcionalidad similar a la anterior ( tipo de venta: producto existente ) 
 [***] Totalmente similar al anterior, con la nica diferencia que en el selector solo aparecern productos cuya eatc-odd_typology_a es igual a " box " (siendo esta la nica diferencia) 
 Segn sea el caso se utilizarn las siguientes consultas para popular los selectores: 
 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_typology_a =box 

 {{URL_entorno}}/api/{{cua_user}}/eatc_sale_prd_mstr? eatc-odd_typology_a =box 

 Ejemplo: cuenta "colombia", ambiente de pruebas: 

 https://devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_typology_a =box   

 https://devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_typology_a =box   

 Listado de productos agregados 
 A medida que se van agregando productos debe generarse un listado con los que han sido agregados.  Este listado debe mostrar la siguiente informacin: 

 Tumbnail Fotografa / Imagen del producto {{eatc_sale_prd_mstr.eatc-odd_image}}: 
 {{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_image={{ eatc_sale_prd_mstr. eatc-odd_image}} 

 Nombre del producto o artculo {{eatc_sale_prd_mstr.eatc-odd_name}}: 
 {{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_name={{eatc_sale_prd_mstr.eatc-odd_name}} 

 Peso unitario del producto en KG {{eatc_sale_prd_mstr.eatc-odd_unit_weight_kg}}: 
 {{URL_entorno}}/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg={{ eatc_sale_prd_mstr. eatc-odd_unit_weight_kg}} 

 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 {{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price ={{output}} 

 Cantidad de productos disponibles para la venta 
 {{URL_entorno}}/api/eatcloud/eatc_sale? eatc-odd_original_quantity ={{input}} 

 Borrar 
 Para cada registro debe colocarse la opcin de "borrar" con el nimo de eliminar el registro particular 

 Editar 
 Para cada registro debe colocarse la opcin de "editar" que debe recargar en el formulario de captura originar los datos del registro en cuestin para modificarlos. 

 BOTN "TERMINAR DE AGREGAR PRODUCTOS" 
 Dado que esta funcionalidad no genera encabezados, al presionar este botn, funcionar de manera muy similar a como lo hace el botn "anunciar donacin" de la funcionalidad de "creacin de anuncios de donacin" simple y llanamente, este botn no llamar ningn proceso para la creacin de encabezados (que de hecho para este mdulo funcional no existirn como tal). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreacion-de-venta-de-ultimo-minuto-eatc_sale_upl%2F2472305312-EmbeddedImage--25-.jpg&ow=1134&oh=784, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreacion-de-venta-de-ultimo-minuto-eatc_sale_upl%2F2472305312-EmbeddedImage--25-.jpg&ow=1134&oh=784 

 129.000000000000 

 CREACIN DE OFERTA DE LTIMO MINUTO (EATC_SALE_UPL)