# new-creación-de-venta-de-último-minuto-eatc_sale_upl.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Esta funcionalidad se basa en la ya desarrollada &quot;Creacin de anuncio de donacin&quot;, pero apunta a estructuras de datos diferentes y tiene algunas capturas de datos diferentes.&#160; Para sealar estas diferencias se utilizar la notacin [***] para indicar que hay un cambio con respecto a la funcionalidad base y [+++] cuando hay algo diferente a la funcionalidad base. 

 CREACIN DE LA OFERTA 
 [***NUEVO****] Seleccin de tiempo de vida de la oferta (antes de la validacin de existencia de horario de venta). 
 El sistema, antes de validar la existencia de un horario de venta, deber preguntar cual es el tiempo de vida de la oferta ( eatc-offer_lifetime ) de una manera muy ilustrativa y didctica, que sirva para explicar al usuario nuestro modelo de negocio y trabajo. El dato obtenido de esta seleccin, servir para la validacin de existencia de horario de venta, y posteriormente se llevar a las estructura eatc_sale , dado que a partir de su informacin el sistema realizar operaciones de transformacin de ofertas en anuncios de donacin y tambin posteriormente acciones de informativas a usuarios que a partir de estas ofertas realizan un pedido. 
&#160; 
 El sistema deber desplegar el siguiente mensaje&#58;&#160; 
 Por favor selecciona el tiempo de vida de tu oferta 
&#160; 
 A continuacin se debe desplegar un selector nico (similar al selector que se coloc para tipificar si la venta de ltimo minuto es de un producto nuevo, uno existente o unto tipo box) que debe se debe construir a partir de la informacin de la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout 
&#160; 
 En el selector se deber mostrar la siguiente informacin (similar al selector que se coloc para tipificar si la venta de ltimo minuto es de un producto nuevo, uno existente o unto tipo box), a partir de los datos de la consulta&#58; 

&#160; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Oferta de ltimo minuto de vida &#123;&#123;eatc-offer_lifetime&#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#123;&#123;eatc-timeout_in_hours&#125;&#125; horas de tiempo de vida 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123;&#123; eatc-timeout_description &#125;&#125; 

&#160; 
 Cuando se selecciona una opcin, se deber guardar la informacin del parmetro eatc_sale_timeout_rules. eatc-offer_lifetime , el cual se deber guardar para luego ser incorporado en el parmetro eatc_sale. eatc-offer_lifetime y tambin se debern guardar los parmetros&#160; eatc_sale_timeout_rules. eatc-timeout_in_minutes y eatc_sale_timeout_rules. eatc-timeout_in_hours para realizar la validacin de horario de venta. 
 Ejemplo (ambiente de pruebas)&#58; 
 Con los datos cargados a 21 de septiembre de 2020, los selectores deben construirse con la informacin que arroja la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout &#160; 
&#160; 
 Y por lo tanto el selector nico deber contener la siguiente informacin&#58; 

 Se guarda el dato de las horas de tiempo de vida para llevarlo posteriormente a eatc_sale.eatc-offer_lifetime 
 Si por ejemplo el usuario selecciona la primera opcin, entonces el dato &quot; corta &quot; (eatc_sale_timeout_rules. eatc-offer_lifetime ) ser guardado para ser llevado posteriormente a los datos de la oferta en el parmetro&#58; eatc_sale. eatc-offer_lifetime la informacin correspondiente a eatc_sale_timeout_rules. eatc-timeout_in_hours es decir&#58; 
&#160; 
 eatc_sale. eatc-offer_lifetime = 10 

 [***MODIFICADO***] Validacin de existencia de horario de venta. 
 A partir de la informacin seleccionada en el anterior selector , el sistema deber validar si existe un horario de venta disponible segn el tiempo de vida de la oferta ( eatc_sale_timeout_rules. eatc-timeout_in_minutes y eatc_sale_timeout_rules. eatc-timeout_in_hours )&#160; similar a la validacin de horarios de atencin pero apuntando a un nuevo object store&#58; 
&#160; 
 [***] 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125; /api/ &#123;&#123;cua_user&#125;&#125; /eatc_sale_schedule?eatc-pod_id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Pruebas &#58; https&#58;//devdonantes.eatcloud.info/api/ &#123;&#123;cua_user&#125;&#125; /eatc_sale_schedule?eatc-pod_id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Productivo &#58; https&#58;//donantes.eatcloud.info/api/ &#123;&#123;cua_user&#125;&#125; /eatc_sale_schedule?eatc-pod_id= &#123;&#123;eatc-pod_id&#125;&#125; 
&#160; 
 Si existe un registro asociado al punto, se pasa a la siguiente validacin&#58; Horario de venta disponible antes del rango de transformacin de la oferta en anuncio . 
&#160; 
 Si no existe un registro asociado al punto. 
&#160; 
 Ejemplo&#58; un punto de donacin, cuyo eatc-pod_id es 777, realiza la consulta (en ambiente de pruebas)&#58;&#160; 
 [***] 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_sale_schedule?eatc-pod_id=777 el resultado de la misma es&#58; 
&#123; 
 ts &#58; &quot;200504094733&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.39, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
&#125; 
&#160; 
 Por lo tanto se debe&#160; desplegar el siguiente mensaje&#58; 
&#160; 
 El punto de donacin no tiene horarios de [***] venta asociados, por favor ingresa a la funcionalidad [***] &quot; horarios de venta &quot; para configurarlos 
&#160; 
 El sistema debe proporcionar un vnculo para ingresar a la funcionalidad [***] horarios de venta , y no debe permitir al usuario hacer un registro de anuncio de donacin, hasta que el punto de donacin no tenga horarios de atencin registrados y que cumpla con la siguiente validacin. 
&#160; 
 Validacin de horario de venta disponible antes del rango de transformacin de la venta en anuncio 
 Si existe un registro de horario de venta, el sistema debe validar que dicho horario empieza antes de que culmine el tiempo que se tiene establecido para transformar la oferta en un anuncio de donacin 
 &#160; [***] &#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout 
&#160; 
&#160; 
 Ambiente de pruebas&#58; https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout &#160;&#160;&#160;&#160;&#160; 
&#160; 
 Ambiente de productivo&#58; https&#58;//donantes.eatcloud.info/api/eatcloud/eatc_sale_timeout_rules?eatc-timeout_name=sale_timeout &#160;&#160;&#160; 
&#160; 
 Si el inicio de por lo menos uno de los horarios de atencin registrados, no se encuentra antes del tiempo establecido en el Timeout, el sistema debe mostrar el siguiente anuncio&#58; 
&#160; 
 El punto de donacin no tiene un horario de venta disponible antes del tiempo estipulado de &#123;&#123;eatc_sale_timeout_rules. eatc-timeout_in_hours que se obtuvo a partir del selector de tiempo de vida de la oferta &#125;&#125; horas para la realizacin de la venta de ltimo minuto. Por favor ingresa a la funcionalidad [***] horarios de venta para configurar un horario adecuado para una venta realizada en este momento. [***] Recuerde que en dicho horario se debe estar en disposicin de atender a quienes acrediten la compra de los productos a travs de EatCloud. 
&#160; 
 Este mensaje&#160; debe impedir realizar el anuncio de donacin (es decir es un mensaje restrictivo como el anterior), y debe proporcionar un vnculo a la funcionalidad de [***] horarios de venta para hacer la configuracin.&#160; 
&#160; 
 [***] NO VA&#58; Validacin de existencia de horarios de atencin por defecto 

 [***] Selector de ubicacin 
 Lo primero que se realizar antes de realizar una venta ser la visualizacin, y edicin de los datos correspondientes al punto de donacin, que funcionar de manera similar a como se implement en la funcionalidad de generacin de anuncio de donacin.&#160; Esta funcionalidad Tiene un diseo diferente [***] al de edicin de la ubicacin actual y&#160; debe permitir, cuando la cuenta as lo tenga configurado, editar coordenadas de puntos de donacin y generar nuevas coordenadas de punto.&#160; En otras palabras, si evaluando la informacin de la cuenta respectiva (cua_user) ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= [cua]), se establece que la cuenta est habilitada para editar coordenadas edit_coordinates=si ), deber aparecer el vnculo &quot;Cambiar direccin&quot; que dar entrada a la funcionalidad respectiva. 

 Informacin cuando no se edita el punto de donacin 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id &#160; 
 La informacin se toma de&#58; 
&#160; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; 39 
&#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se toma de eatc_pods.eatc-name)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-name 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; EXITO SAN ANTONIO 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 
 &#160;Este dato se debe mostrar (pintar) en la interfaz de la APP y [+++] y se lleva tambin al object store de eatc_sale 

&#160; 
 Latitud del punto de venta (se toma de eatc_pods.eatc-lat)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat &#160; 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-lat 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; 6.24683 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 
 &#160; [+++] Este dato se lleva&#160; al object store de eatc_sale 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods.eatc-lat)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-lon 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; -75.566905 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 
 &#160; [+++] Este dato se lleva&#160; al object store de eatc_sale 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods.eatc-adress)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se llevaba al object store de las donaciones pero ahora si se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-adress 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; Cl. 48 #46-115, Medelln, Antioquia 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_address=&#123;&#123;input&#125;&#125; 
 &#160;Este dato se debe mostrar (pintar) en la interfaz de la APP y [+++] y se lleva tambin al object store de eatc_sale 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods.eatc-city)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-city 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; MEDELLIN 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125; 
 &#160; [+++] Este dato se debe mostrar (pintar) en la interfaz de la APP y se lleva tambin al object store de eatc_sale 

&#160; 
 Departamento / provincia / estado del punto de venta (se toma de eatc_pods.eatc-province)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-province y eatc_sale.eatc-pod_province [PENDIENTE DOCUMENTACIN] 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-province 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; ANTIOQUIA 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_province=&#123;&#123;input&#125; 

&#160; 
 Pas del punto de venta (se toma de eatc_pods.eatc-country)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-country 
&#160; 
 Ejemplo&#58; 
 Para el xito de San Antonio, esta ser la informacin que se toma 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 &#160; 
 Es decir al &#123;&#123;input&#125;&#125; se lleva el valor&#58; CO 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 &#160;no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura con respecto a este dato ya que el mismo se toma desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= exito ) &#160; 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 &#160;tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor &#160; a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= exito ) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para editar informacin del punto de donacin (y guardarla en la persistencia eatc_pods), cuando se edita el nombre del donante y su identificacin para cuentas que manejen mltiples donantes 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
 [***] Cuando se termina de editar esta informacin 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

&#160; 
 Edicin de coordenadas del punto de donacin&#58; 
 Despliegue de la funcionalidad 
 Si evaluando la informacin de la cuenta respectiva (cua_user) ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user &#125;&#125; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;), se establece que la cuenta est habilitada para editar coordenadas edit_coordinates=si ), al lado de la direccin se debe desplegar un botn que permita editar/seleccionar una direccin para efectuar la donacin. 
 Ejemplo &#58; 
 Para la cuenta &quot;colombia&quot; se evala su respectiva configuracin con el siguiente llamado&#58;&#160; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Al comprobar que el parmetro &quot; edit_coordinate &quot; tiene como valor &quot;si&quot; se debe habilitar la funcionalidad para la cuenta en cuestin. 
&#160; 
 Edicin de coordenadas&#58; 
 Al darle clic al botn, la plataforma debe evaluar si en la persistencia &quot; eatc_pods_coordinates (NOTA PARA JDC&#58; falta documentacin mtodo, parmetros) &quot; para el &quot;eatc_pod&quot; respectivo existe informacin ( eatc_pods.eatc-id ), para mostrar las diversas direcciones guardadas en un selector (se muestra en el selector la direccin y su nombre, permitiendo traer las coordenadas respectivas, informacin que se terminar llevando a la informacin del respectivo eatc_pod).&#160;&#160; 
 Ejemplo &#58; 
 Para el punto de donacin &quot;nzzn1&quot; de la cuenta &quot;colombia&quot; se tiene la siguiente informacin&#58; 
&#160; 
 Ambiente de prueba&#58; https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1 &#160; 
&#160; 
 Por lo tanto se debe poder seleccionar una de las direcciones registradas (en etapas posteriores se debe poder operar este selector como un buscador) para desplegar la latitud y longitud determinada. 
&#160; 
 Tambin debe presentar la opcin de adicionar una nueva direccin, y para hacerlo se debe desplegar un mapa que coloque por defecto a eatc_lat y eatc_lon del eatc_pod respectivo (se debe reciclar lo implementado aqu&#58; https&#58;//devdonantes.eatcloud.info/registro/colombia &#160; para mayor informacin comunicarse con Ivn Daro Restrepo). La nica diferencia con las imgenes abajo dispuestas, es que debe existir un campo de captura adicional con la etiqueta &quot; Nombre del punto de donacin &quot; inmediatamente abajo de la direccin y que corresponde a la informacin que se encuentra en eatc_pods.eatc-name (en caso de que no halla un registro en eatc_pods_coordinates ) o eatc_pods_coordinates .eatc-name cuando se ha realizado una seleccin de las coordenadas registradas o en (ser un campo editable tipo text_field que reciba informacin tipo string) 
&#160; 
 [***] Visualizacin del mapa&#58; primero mostrar el mapa y luego la direccin 
 A diferencia del diseo original del mapa en donde sala primero la direccin y luego el mapa (que modificaba la direccin), se debe poner primero el mapa y luego la direccin (como est actualmente en las funcionalidades de registro)&#58; 

 Al mover el PIN en el mapa se podr ir variando las coordenadas y la direccin (tal como lo hace la actual implementacin ejemplo https&#58;//devdonantes.eatcloud.info/regpdona/ ) . 
 Siempre se permitir editar la direccin que aparece a partir del la seleccin del PIN. Ciudad y Pas no permitirn ser editados, solo sern editables a partir de la seleccin el pin en el mapa. 

 Edicin de coordenadas del punto de donacin&#58; se selecciona un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se toma de eatc_pods_coordinates y se lleva a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Selector (nico)&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-name 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Es decir, el selector debe tener los valores&#58; oficina y casa. El valor que sea seleccionado se llevar al &#123;&#123;input&#125;&#125; respectivo y se guardar su _id para las posteriores consultas 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lat y se lleva a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lat 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; 6.252699799631093 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lon y se lleva a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon &#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lon 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; -75.59463315188623 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates.eatc-adress y se lleva a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-adress 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates.eatc-city y se lleva a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-city 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 
&#160; 
 Departamento del punto de venta (se toma el dato eatc_pods_coordinates.eatc-city y luego se lleva a eatc_pods.eatc-province y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province .&#160; [pendiente documentacin] 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-province 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; ANTIOQUIA (pendiente de implementar el dato en el repositorio) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-province=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_province=&#123;&#123;input&#125;&#125; 
&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates.eatc-country y se lleva a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-country 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; CO 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user &#125;&#125; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;)) &#160; no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates.eatc-warning y se lleva a eatc_sale)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-warning 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Primera observacin de prueba 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para editar informacin de coordenadas (y guardarla en la persistencia eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 

 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-province =&#123;&#123;Departamento&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
&#160; 
 [***] Cuando se termina de editar los datos de las coordenadas (seleccionando una opcin diferente a la almacenada en eatc_pods) 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

 Edicin de coordenadas del punto de donacin&#58; se editan los datos un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
 El proceso de login . 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-name luego a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Selector (nico)&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-name 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Es decir, el selector debe tener los valores&#58; oficina y casa. El valor que sea seleccionado se llevar al &#123;&#123;input&#125;&#125; respectivo y se guardar su _id para las posteriores consultas 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado en el anterior selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 

&#160; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lat 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; 6.252699799631093 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lon 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; -75.59463315188623 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-adress 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
&#160; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-city 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Medelln 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-city=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 
&#160; 
 Departamento / provincia / estado del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-province luego a eatc_pods.eatc-province y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province , [pendiente documentacin] 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
&#160; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-province 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; ANTIQUIA (Pendiente de implementacin en datos) 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-province=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-province=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_province=&#123;&#123;input&#125;&#125; 
&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
&#160; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-country 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; CO 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa. En una primera etapa solo se aceptarn ventas de Colombia, pero a futuro se debern incorporar nuevos pases) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-country=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 &#160;tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 

 La informacin se toma de&#58; 
&#160; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 &#160;no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
 &#160; 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-warning luego a eatc_sale.eatc-warning)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-warning 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Primera observacin de prueba 
&#160; 
 El usuario podr cambiar la informacin del dato que se despliega a partir del selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo y luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-warning=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para editar informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
&#160; 

 &#123;&#123;Parametros edicin en eatc_pods_coordinates &#125;&#125; &#58; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-province =&#123;&#123;Departamento&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125; 
&#160; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods_coordinates&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods_coordinates&#125;&#125; &amp;WHER_id=&#123;&#123; eatc_pods_coordinates._id&#125;&#125; 

&#160; 

 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-province =&#123;&#123;Departamento&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
&#160; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

 Creacin de coordenadas del punto de donacin&#58; se crea un nuevo punto en eatc_pods_coordinates 
&#160; 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
 El proceso de login . 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se despliega un campo de captura y luego se lleva eatc_pods_coordinates.eatc-name, a eatc_pods.eatc-name y a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 
&#160; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN), con posibilidad de editar la direccin que sugiere el mapa 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-city=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 
&#160; 
 Departamento / provincia / estado del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-province luego a eatc_pods.eatc-province y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-province , eatc_pods.eatc-province y eatc_sale.eatc-pod_province [pendiente documentacin] 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-province=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-province=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_province=&#123;&#123;input&#125;&#125; 
&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-country=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
 &#160; 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) 
 tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc- luego a eatc_sale)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Pregunta abierta ( Textarea ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Se guarda en [+++] &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-warning=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para crear informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
&#160; 
 &#123;&#123;Parametros creacin en eatc_pods_coordinates &#125;&#125; &#58; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-province =&#123;&#123;Departamento&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125; 
&#160; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods_coordinates&amp;_operacion= insert &amp;&#123;&#123; Parametros edicin en eatc_pods_coordinates&#125;&#125; 
&#160; 

 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-province =&#123;&#123;Departamento&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125;&amp; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
&#160; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

 Datos que se digitan en el encabezado (una sola vez por anuncio) 
 Documento soporte&#58;&#160; 
 Campo de texto abierto que se despliega si se cumple la siguiente condicin&#58; que en parmetro eatc_dona_upl tenga como valor &quot;yes&quot; **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ). En caso que el parmetro tenga como valor &quot;no&quot; no se debe desplegar campo de captura y se toma este dato como vaco (para posteriormente llevarlo al registro . 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-doc 
 Descripcin ( tooltip ) &#58; Ingrese por favor un documento de soporte 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Regla obligatoriedad &#58; no aplica 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-doc=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos, no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-doc=&#123;&#123;input&#125;&#125; 

&#160; 
 Encabezado&#58; Datos generados por la APP&#58; 
 Los datos de encabezado se toman y se muestran al iniciar la transaccin y se agregan a cada registro de detalle (eatc_dona).&#160; Dichos datos son 
 Cdigo de la venta 
 [***] Debe funcionar exactamente igual como est funcionando el cdigo del anuncio de donacin y ser llamado de igual manera para facilitar la implementacin) &#160; ( eatc-dona_header_code que corresponde a un identificador nico para la venta que se realizar).&#160; Idealmente este cdigo deber contener el nombre de la cuenta [CUA], el cdigo del punto de donacin (eatc-pod_id) y una cadena (que puede ser el estampe de tiempo con milisegundos (AAAAMMDDHHMMSSMM). La nica diferencia es que esta informacin se lleva al object store eatc_sale 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-dona_header_code 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Lo genera el sistema de la misma manera como genera el cdigo para los anuncios de donacin. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-dona_header_code=&#123;&#123;input&#125;&#125; 

&#160; 
 [****AJUSTE EN TIPO DE DATO****] Fecha actual&#58; eatc-date_time 
 [***] Debe funcionar exactamente igual como est funcionando en anuncios de donacin, con la diferencia que se lleva al object store eatc_sale 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-date_time 
 Tipo de dato&#58; datetieme (en formato AAAA-MM-DD HH&#58;MM&#58;SS) 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Lo genera el sistema a partir del current datetime. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-date_time=&#123;&#123;input&#125;&#125; 
&#160; 
 Fecha actual&#58; eatc-date_time_2 
 [***] Debe funcionar exactamente igual como est funcionando en anuncios de donacin, con la diferencia que se lleva al object store eatc_sale 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-date_time_2 
 Tipo de dato&#58; date 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Lo genera el sistema a partir del current date. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-date_time_2=&#123;&#123;input&#125;&#125; 
&#160; 
 [NUEVO] eatc_cua_origin 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc_cua_origin 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 &#160; $DOM.cua_user //Cuenta desde la cual se genera el anuncio de donacin que corresponde a la cua_user de la WebApp. 

&#160; 
 [+++] Nit del donante (se toman de eatc_cua en datagov a excepcin de las cuentas mltiples como &quot;colombia&quot;) ***NUEVO&#58; SE TOMA LA INFORMACIN DE DATAGOV*** 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc_donor_code 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 

 La informacin se toma de&#58; 
&#160; 
 CASO 1&#58; multiple_donors=no&#58; 
 S i la cuenta respectiva en datagov&#160; 
 ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) )&#160; 
&#160; 
 no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) ) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces la informacin se toma de la siguiente consulta&#160; 
&#160; 
 ****NUEVO&#58; CONSULTAS PARA OBTENER EL NIT DE DATAGOV****&#58;&#160; 
 Primera consulta para obtener la relacin entre la cuenta y los datos del cliente 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue=&#123;&#123;_DOM.cua_user&#125;&#125; 
&#160; 
 &#160;Con la respuesta obtenida se toma el _id para realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua,eatc_customer_fiscal_id &amp;&amp;filterfield_1=_id&amp;filtervalue_1=&#123;&#123; eatc_customers_cua._id &#125;&#125;&#160; 
&#160; 
 Con esto se obtiene el valor desencriptado de eatc_customer_fiscal_id &#160; que es el que se guarda en eatc_sale. eatc_donor_code y tambin se utiliza para obtener el nombre del donante ms adelante 
 (ANTERIORMENTE&#58; se toma de eatc_cua . customer__eatc_clientes__partyidentification https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= [cua] ) 
&#160; 
 Ejemplo&#58; CONSULTAS PARA OBTENER EL NIT DE DATAGOV&#58;&#160; 
 Ejemplo _DOM. cua_user = exito 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue=exito &#160;&#160; 
&#160; 
 Dado que la respuesta es&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;8&quot;, 
 eatc_country &#58; &quot;co&quot;, 
 ... 
 &#125; 
&#160; 
 &#160;Con la respuesta obtenida se toma el _id=8 para realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua,eatc_customer_fiscal_id &amp;&amp;filterfield_1=_id&amp;filtervalue_1=8 &#160; 
&#160; 
 Como eatc_customer_fiscal_id &#58; &quot; 890900608 &quot;, el dato se lleva a eatc_sale. eatc_donor_code y se guarda para la prxima consulta 
&#160; 
 CASO 2&#58; multiple_donors=si&#58; 
 Si la cuenta respectiva en datagov 
 ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_cua?name=&#123;&#123; _DOM. cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) )&#160; 
 tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer el dato guardado en eatc_pods. eatc-donor 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc_id &#125;&#125; 

&#160; 
 Ejemplo 1 (entorno de pruebas)&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se lleva al registro 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor_code=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (se toman de eatc_cua en datagov) *** NUEVO&#58; consulta a datagov***** 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 

 La informacin se toma de&#58; 
&#160; 
 CASO 1&#58; multiple_donors=no&#58; 
 S i la cuenta respectiva en datagov&#160; 
 ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) )&#160; 
 no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 ****NUEVO&#58; CONSULTAS PARA OBTENER EL LA RAZN SOCIAL DE DATAGOV****&#58;&#160; 
 Se toma el dato obtenido para eatc_customers_cua. eatc_customer_fiscal_id en la anterior consulta y se realiza esta 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; 
 Con el resultado de la consulta se toma el dato _id para realizar la siguiente consulta y obtener el eatc_fiscal_name 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_name &amp;&amp;filterfield_1= _id &amp;filtervalue_1=&#123;&#123;eatc_customers_cua. _id &#125;&#125; 
 Con esto se obtiene el valor desencriptado de eatc_fiscal_name &#160; que es el que se guarda en eatc_sale. eatc_donor &#160; 

 (ANTERIORMENTE&#58; se toma de eatc_cua . customer__eatc_clientes__partyidentification https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= [cua] ) 
&#160; 
 Ejemplo&#58; CONSULTAS PARA OBTENER LA RAZN SOCIAL DE DATAGOV&#58;&#160; 
 Ejemplo (retomando el ejemplo anterior ) 
&#160; 
 Como el dato que se obtuvo fue&#58; eatc_customer_fiscal_id &#58; &quot; 890900608 &quot; 
&#160; 
 Entonces se realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= 890900608 &#160; 
&#160; 
 Como la respuesta obtenida es 
&#160; 
 &#123; 
 _id &#58; &quot;2&quot;, 
 eatc_country &#58; &quot;co&quot;, 
 eatc_fiscal_id &#58; &quot;bGlzbGJKSVMydE8xT3ZQa3ByZit3Zz09&quot;, 
 eatc_fiscal_name &#58; &quot;Sm95T1M5Z2hqYmlUb0JyM281YXpMSFBkOFFxdE05YnErTnIyUU1rNDRRQT0=&quot;, 
 .....&quot;&quot; 
 &#125; 
 Con el resultado de la consulta se toma el dato _id para realizar la siguiente consulta y obtener el eatc_fiscal_name 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_name &amp;&amp;filterfield_1= _id &amp;filtervalue_1=2 &#160; 
&#160; 
 dado que eatc_fiscal_name &#58; &quot;Almacenes xito S.A.&quot;, entonces el dato que se lleva al registro ( eatc_donor ) es &quot; Almacenes xito S.A. &quot;. &#160; Este dato se debe mostrar (pintar) en la interfaz de la APP y se guarda para el registro. 
 . 
&#160; 
&#160; 
 CASO 2&#58; multiple_donors=si&#58; 
 Si la cuenta respectiva en datagov&#160; 
&#160; 
 ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; &#160; 
( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) 
&#160; 
 tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer el dato guardado en eatc_pods. eatc-donor 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc_id &#125;&#125; 

&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, este es el valor que se lleva al registro 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

 [+++] selector de tipo de venta&#58;&#160; 

 En esta nuevo enfoque funcional se podrn seleccionar tres tipos de venta&#58;&#160; 
 Producto Nuevo &#58; genera todos los datos del producto y lo registra en dos object store&#58; eatc_sale_prd_mstr y eatc_sale 
 Producto Existente &#58; consulta los datos de eatc_sale_prd_mstr 
 Producto Box &#58; consulta los datos de eatc_sale_prd_mstr para traer solamente aquellos cuya eatc-odd_typology_a= box 

 Tipo de venta&#58; producto nuevo&#58; 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto nuevo para la venta, y se establece su registro en los object stores correspondientes&#58; eatc_sale_prd_mstr y eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Nombre del producto o artculo&#58; 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr. eatc-odd_name y eatc_sale. eatc-odd_name 
 Orden en el formulario &#58; 1 
 Descripcin ( tooltip ) &#58; Ingresa por favor el nombre del producto o artculo a vender. 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-odd_name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_name=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-odd_name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_name=&#123;&#123;input&#125;&#125; 

&#160; 
 Identificador del producto&#58; 
 Funciona de manera similar a como lo hace en la creacin de anuncios de donacin, sugiriendo un identificador a partir del nombre del artculo que el usuario puede editar 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_id y eatc_sale.eatc-odd_id 
 Orden en el formulario &#58; 2 
 Descripcin ( tooltip ) &#58; Ingresa un identificador nico para el producto o artculo 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad, unicidad (no debe haber un eatc-odd_id similar en eatc_sale_prd_mstr) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-odd_id=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_id=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-odd_id=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_id=&#123;&#123;input&#125;&#125;&#160; 

&#160; 
 Fotografa / Imagen del producto&#58; 
 [+++] Nueva funcionalidad.&#160; Se debe indagar con Ivn Daro Restrepo para reciclar cdigo que se desarroll para la funcionalidad de registro de gestor de donaciones (para la subida de RUT y Certificado de Cmara de Comercio).&#160; Se debe concretar con Luis Carlos Correa la relacin de aspecto con la cual se debe subir la imagen 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_image y eatc_sale.eatc-odd_image 
 Orden en el formulario &#58; 3 
 Descripcin ( tooltip ) &#58; Sube una imagen o fotografa del producto 
 Tipo &#58; subida (desde el dispositivo&#58; File Input ) de imagen o toma de imagen con cmara del equipo. 
 Tipo de dato&#58; string (se debe establecer con Ivn Daro Restrepo que informacin se lleva al registro&#58; una URL absoluta, o URL relativa o simplemente el nombre del la fotografa subida (que debera nombrarse con el eatc-odd_id) 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad, tamao&#58; se debe limitar el tamao de las imgenes a un peso razonable para su manipulacin web (por ejemplo 2 Megas), para evitar sobrecarga del servidor y consultas muy pesadas en la App. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-odd_image=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_image=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-odd_image=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_image=&#123;&#123;input&#125;&#125;&#160; 

&#160; 
 Descripcin&#58; 
 [+++] Nueva funcionalidad. 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_description y eatc_sale.eatc-odd_description 
 Orden en el formulario &#58; 4 
 Descripcin ( tooltip ) &#58; Ingresa una descripcin del producto o artculo 
 Tipo &#58; Pregunta abierta ( rea de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Tipo de dato&#58; string&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-odd_description=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_description=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-odd_description=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_description=&#123;&#123;input&#125;&#125; 

&#160; 
 Peso unitario del producto en KG (si necesita ingresar en gramos utilice decimales)&#58; 
 [***] Similar a la captura del peso unitario pero guardando en object stores diferentes 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_unit_weight_kg y eatc_sale.eatc-odd_unit_weight_kg 
 Orden en el formulario &#58; 5 
 Descripcin ( tooltip ) &#58; Ingresa el peso unitario del producto o artculo en Kilogramos.&#160; Si requieres ingresarlo en gramos, utiliza nmeros decimales) 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad, diferente de cero, pesos excesivos (se pregunta por confirmacin si el peso unitario es superior a 20 KG) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-odd_unit_weight_kg=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-odd_unit_weight_kg=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_unit_weight_kg=&#123;&#123;input&#125;&#125; 

&#160; 
 Porcentaje de impuesto al valor agregado aplicable al producto 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc_VAT_percentage y eatc_sale.eatc_VAT_percentage 
 Orden en el formulario &#58; 6 
 Descripcin ( tooltip ) &#58; Ingresa el impuesto al valor agregado aplicable al producto 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc_VAT_percentage=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc_VAT_percentage=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc_VAT_percentage=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc_VAT_percentage=&#123;&#123;input&#125;&#125; 
&#160; 
 Porcentaje de otros impuestos aplicables al producto 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-other_taxes_percentage y eatc_sale.eatc-other_taxes_percentage 
 Orden en el formulario &#58; 7 
 Descripcin ( tooltip ) &#58; Ingresa el porcentaje de otros impuestos aplicables al producto, como por ejemplo IMPOCONSUMO 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-other_taxes_percentage=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-other_taxes_percentage=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-other_taxes_percentage=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-other_taxes_percentage=&#123;&#123;input&#125;&#125; 
&#160; 
 Contiene alrgenos? 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-contains_alergens y eatc_sale.eatc-contains_alergens 
 Orden en el formulario &#58; 8 
 Descripcin ( tooltip ) &#58; Ingresa si el producto o artculo contiene substancias que pueden resultar alrgicas para ciertas personas. 
 Tipo &#58; Seleccin nica (SI / NO) ( Select ) ( informacin tcnica sobre el tipo de pregunta &#58; SLU ) 
 Tipo de dato&#58; boleano&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr?eatc-contains_alergens=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-contains_alergens=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc-contains_alergens=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-contains_alergens=&#123;&#123;input&#125;&#125; 
&#160; 
 Fecha de caducidad de los artculos 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes&#58; Para cada registro se debe de manera opcional , seleccionar la fecha ms prxima de vencimiento.&#160; Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parmetro (eatc_sale. eatc-closer_expiration_date ) ser&#58; 0000-00-00 . Si el usuario desea registrar una fecha, deber ingresar a un &quot; date picker &quot; o &quot; selector de fechas &quot; que presenta por defecto, como sugerencia de &quot;fecha ms prxima de vencimiento&quot; la sumatoria de la fecha actual ms el nmero que se encuentra en el parmetro&#160; eatc_cua. days_before_expiration ( **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] )) .&#160; Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vaco o nulo, el valor por defecto que debe tomarse es &quot;5&quot;, para realizar la sumatoria y asi sugerir la fecha .&#160; El usuario podr modificar esa fecha sugerida, y el sistema no le permitir ingresar fechas anteriores al da actual ms 1 da. (solo se podrn ingresar fechas posteriores). El dato resultante (tipo fecha con formato AAAA-MM-DD) se deber guardar en el parmetro eatc_sale. eatc-closer_expiration_date 
 Informacin tcnica del parmetro&#58; eatc_sale.eatc-closer_expiration_date 
 Orden en el formulario &#58; 9 
 Descripcin ( tooltip ) &#58; selecciona la fecha ms prxima de expiracin de los productos ofertados. 
 Tipo &#58; Date Picker 
 Tipo de dato&#58; date&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-closer_expiration_date =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-closer_expiration_date =&#123;&#123;input&#125;&#125; 

&#160; 
 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_min_sale_unit_price 
 Orden en el formulario &#58; 10 
 Descripcin ( tooltip ) &#58; Ingresa el precio de venta al pblico (incluyendo tarifas e impuestos) para promover la venta de ltimo minuto 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 

&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125; 
&#160; 
 Porcentaje de descuento para venta de ltimo minuto (sirve para incentivar la compra) 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_max_discount 
 Orden en el formulario &#58; 11 
 Descripcin ( tooltip ) &#58; Ingresa el porcentaje descuento sobre el precio de venta al pblico real, que representa el precio de venta al pblico de ltimo minuto. El poder visualizar estos descuentos ayuda a estimular la compra. 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; no (en un futuro puede cambiar) 
 Validacin &#58; no aplica (en un futuro puede cambiar) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_max_discount =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 

&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_max_discount =&#123;&#123;input&#125;&#125; 
&#160; 
 [Clculo oculto] Precio de venta al publico unitario (PVP&#58; se calcula si se obtuvieron los dos datos anteriores) 
 [+++] Nuevo campo que se calcula a partir de las dos capturas anteriores 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_unit_price 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no (en un futuro puede cambiar) 
 Validacin &#58; no aplica (en un futuro puede cambiar) 
 Cmo se calcula&#58; 
 eatc-odd_unit_price - eatc-odd_max_discount *eatc-odd_unit_price = eatc-odd_min_sale_unit_price 
&#160; 
 eatc-odd_unit_price= eatc-odd_min_sale_unit_price /( 1-eatc-odd_max_discount ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_unit_price =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 

&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_unit_price =&#123;&#123;input&#125;&#125; 
&#160; 
 Cantidad de productos disponibles para la venta (la venta se realizar por unidades) 
 [***] Similar a la captura para anuncios de donacin (eatc-odd_original_quantity y eatc-odd_quantity) pero guardando en un object store diferente 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_original_quantity y eatc_sale.eatc-odd_quantity 
 Orden en el formulario &#58; 12 
 Descripcin ( tooltip ) &#58; Ingresa las cantidades del producto o artculo disponible para la venta. Recuerda que los artculos se vendern por separado. 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. Mayor o igual que uno. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_original_quantity =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_quantity =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp; eatc-odd_original_quantity =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp; eatc-odd_quantity =&#123;&#123;input&#125;&#125;&#160; 

&#160; 
 [Campo oculto] Estado del producto para la venta (eatc_state=sale) 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_state 
 Tipo de dato&#58; string&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Dado que el producto se oferta, se registra en el parmetro eatc_state el valor &#123;&#123;input&#125;&#125; &quot;sale&quot; 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_state =sale 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_state =sale 

&#160; 
 Cdigo del registro 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-code [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 la concatenacin de los datos &quot; Identificador del producto &quot; (eatc_sale. eatc-odd_id ) y &quot; Cdigo de la venta &quot; (eatc_sale. eatc-dona_header_code )&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-code=&#123;&#123;input&#125;&#125; 

&#160; 
 *****NUEVO****** [Campo oculto] tiempo de vida de la oferta&#160; 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-offer_lifetime [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Dado que se gener al seleccionar al principio de la creacin de la oferta su tiempo de vida til 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-offer_lifetime =&#123;&#123;eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-offer_lifetime =&#123;&#123;eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 

&#160; 
 *****NUEVO****** [Campo oculto] fecha y hora de finalizacin de tiempo de vida de la oferta 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-offer_lifetime_until [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato&#58; datetime&#160; (AAAA-MM-DD HH&#58;MM&#58;SS) 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Se le suma al dato eatc_sale. eatc-date_time las horas registradas en el dato anterior (tiempo de vida de la oferta) eatc_sale. eatc-offer_lifetime 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-offer_lifetime_until =&#123;&#123;eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-offer_lifetime_until =&#123;&#123;eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 

&#160; 
 Venta producto nuevo&#58; botn&#58; &quot;Agregar Producto&quot;&#58; Parmetros para crear informacin de en eatc_sale_prd_mstr y en eatc_sale 
 [***] En trminos generales funciona de manera similar al proceso para agregar producto en la creacin de anuncios de donacin (incluyendo la aparicin en el listado, la validacin de que no se repita ni en el listado ni en lo que se registra, etc.) pero con dos diferencias&#58; el object store en el cual se registra (que ahora ser eatc_sale de la cuenta &quot;eatcloud&quot;) y que no se requerir llamar a un webservice adicional al final de la creacin para crear un &quot;encabezado&quot; (en proceso que esta funcionalidad solo crear detalles). 
&#160; 
 Al oprimir el botn agregar productos se realizan las siguientes operaciones de insercin en eatc_sale_prd_mstr y en eatc_sale&#58; 
 &#123;&#123;Parametros creacin en eatc_sale_prd_mstr &#125;&#125; &#58; eatc-odd_name =&#123;&#123;Nombre del producto&#125;&#125;&amp; eatc-odd_id =&#123;&#123;input&#125;&#125;&amp; eatc-odd_image =&#123;&#123;input&#125;&#125;&amp; eatc-odd_description =&#123;&#123;input&#125;&#125;&amp; eatc-odd_unit_weight_kg =&#123;&#123;input&#125;&#125;&amp; eatc_VAT_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-other_taxes_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-contains_alergens =&#123;&#123;input&#125;&#125; 
 [***] Cuando se&#160; terminan de crear los datos de los productos se realiza el siguiente llamado al CRD&#58; 
&#160; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacion= insert &amp; &#123;&#123;Parametros creacin en eatc_sale_prd_mstr &#125;&#125; 
&#160; 
 &#123;&#123;Parmetros creacin en eatc_sale &#125;&#125;&#58; &amp; eatc-pod_name =&#123;&#123;eatc-name&#125;&#125;&amp;&amp; eatc-pod_id =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-pod_lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-pod_lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-pod_adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-pod_city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-pod_country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125;&amp; eatc-doc =&#123;&#123;input&#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;input&#125;&#125;&amp; eatc-date_time =&#123;&#123;input&#125;&#125;&amp; eatc-date_time_2 =&#123;&#123;input&#125;&#125;&amp; eatc-donor_code =&#123;&#123;input&#125;&#125;&amp; eatc-donor =&#123;&#123;input&#125;&#125;&amp; eatc-odd_name =&#123;&#123;Nombre del producto&#125;&#125;&amp; eatc-odd_id =&#123;&#123;input&#125;&#125;&amp; eatc-odd_image =&#123;&#123;input&#125;&#125;&amp; eatc-odd_description =&#123;&#123;input&#125;&#125;&amp; eatc-odd_unit_weight_kg =&#123;&#123;input&#125;&#125;&amp; eatc_VAT_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-other_taxes_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-contains_alergens =&#123;&#123;input&#125;&#125;&amp; eatc-closer_expiration_date =&#123;&#123;input&#125;&#125;&amp; eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125;&amp; eatc-odd_max_discount =&#123;&#123;input&#125;&#125;&amp; eatc-odd_unit_price =&#123;&#123;input&#125;&#125;&amp; eatc-odd_original_quantity =&#123;&#123;input&#125;&#125;&amp; eatc-odd_quantity =&#123;&#123;input&#125;&#125;&amp; eatc-odd_state =sale&amp; eatc-code =&#123;&#123;input&#125;&#125;&amp; eatc-offer_lifetime =&#123;&#123;input&#125;&#125;&amp; eatc-offer_lifetime_until =&#123;&#123;input&#125;&#125; 

&#160; 
 [***] Se guarda la informacin en el object store eatc_sale de la cuenta eatcloud&#58; 
&#160; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&amp;_operacion=insert&amp; &#123;&#123;Parmetros creacin en eatc_sale &#125;&#125; 

 Tipo de venta&#58; producto existente&#58; 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto para la venta a partir de la seleccin de un producto ya existente en el maestro eatc_sale_prd_mstr, y se establece su registro en el object store correspondiente&#58; eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Buscador de productos por nombre o por cdigo&#58; 
 [***] Tal como funciona la para la creacin de anuncios de donacin, se debe desplegar un selector nico para establecer que tipo de bsqueda se realiza&#58; si es por nombre (eatc-odd_name) o si es por codigo (eatc-odd_id). Dicha bsqueda se debe hacer contra el object store eatc_sale_prd_mstr (siendo esta la unica diferencia) 
 Segn sea el caso se utilizarn las siguientes consultas para popular los selectores&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_name =_* 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =_* 
&#160; 
 Ejemplo&#58; cuenta &quot;colombia&quot;, ambiente de pruebas&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_name =_* 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_id =_* 
&#160; 

&#160; 
 Bsqueda por nombre del producto o artculo &#123;&#123;eatc_sale_prd_mstr.eatc-odd_name&#125;&#125;&#58; 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr. eatc-odd_name y eatc_sale. eatc-odd_name 
 Descripcin ( tooltip ) &#58; Ingresa por favor el nombre del producto o artculo a buscar. 
 Tipo &#58; Texto predictivo con autocompletar 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_name=&#123;&#123;eatc_sale_prd_mstr.eatc-odd_name&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_name=&#123;&#123;eatc_sale_prd_mstr.eatc-odd_name&#125;&#125;&#160; 

&#160; 
 Bsqueda por identificador del producto &#123;&#123;eatc_sale_prd_mstr.eatc-odd_id&#125;&#125;&#58; 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_id y eatc_sale.eatc-odd_id &#160; 
 Descripcin ( tooltip ) &#58; Ingresa un identificador nico para el producto o artculo a buscar. 
 Tipo &#58; Texto predictivo con autocompletar 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_id=&#123;&#123;eatc_sale_prd_mstr.eatc-odd_id&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_id=&#123;&#123;eatc_sale_prd_mstr.eatc-odd_id&#125;&#125; 
 Tal como funciona la para la creacin de anuncios de donacin, se muestra el dato complementario segn sea el caso (nombre o identificador) y con el identificador respectivo se traen los datos que se pueden llamar recursivamente del object store eatc_sale_prd_mstr 

&#160; 
 Fotografa / Imagen del producto &#123;&#123;eatc_sale_prd_mstr.eatc-odd_image&#125;&#125;&#58; 
 [+++] Nueva funcionalidad.&#160; Se debe mostrar la imagen del producto que se est buscando. 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_image y eatc_sale.eatc-odd_image 
 Orden en el formulario &#58; 3 
 Descripcin&#58; no aplica 
 Tipo &#58; imagen 
 Tipo de dato&#58; string (se debe establecer con Ivn Daro Restrepo cmo se consultar este recurso para traerlo a la interfaz de la APP) 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad, 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc-odd_image 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_image=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_image&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_image=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_image&#125;&#125; 

&#160; 
 Descripcin &#123;&#123;eatc_sale_prd_mstr.eatc-odd_description&#125;&#125;&#58; 
 [+++] Nueva funcionalidad. Se debe mostrar la descripcin del producto o artculo 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_description y eatc_sale.eatc-odd_description &#160; 
 Orden en el formulario &#58; 4 
 Descripcin ( tooltip ) &#58; no aplica 
 Tipo &#58;&#160; texto 
 Tipo de dato&#58; string&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad. 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc-odd_description 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_description=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_description&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_description=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_description&#125;&#125; 

&#160; 
 Peso unitario del producto en KG &#123;&#123;eatc_sale_prd_mstr.eatc-odd_unit_weight_kg&#125;&#125;&#58; 
 [***] Similar a la implementacin de creacin de anuncio de donacion pero solo traera informacin desde el repositorio eatc_sale_prd_mstr 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-odd_unit_weight_kg y eatc_sale.eatc-odd_unit_weight_kg 
 Orden en el formulario &#58; 5 
 Descripcin ( tooltip ) &#58; no aplica 
 Tipo &#58; Texto 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad, diferente de cero, pesos excesivos (se pregunta por confirmacin si el peso unitario es superior a 20 KG) 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc-odd_unit_weight_kg 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_unit_weight_kg&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-odd_unit_weight_kg=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_unit_weight_kg&#125;&#125; 

&#160; 
 Porcentaje de impuesto al valor agregado aplicable al producto &#123;&#123;eatc_sale_prd_mstr.eatc_VAT_percentage&#125;&#125;&#58; 
 [***] Similar 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc_VAT_percentage y eatc_sale.eatc_VAT_percentage 
 Orden en el formulario &#58; 6 
 Descripcin ( tooltip ) &#58; no aplica 
 Tipo &#58; Texto 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna. 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc_VAT_percentage 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc_VAT_percentage=&#123;&#123; eatc_sale_prd_mstr. eatc_VAT_percentage&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp;eatc_VAT_percentage=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc_VAT_percentage=&#123;&#123; eatc_sale_prd_mstr. eatc_VAT_percentage&#125;&#125; 

&#160; 
 Porcentaje de otros impuestos aplicables al producto &#123;&#123;eatc_sale_prd_mstr.eatc-other_taxes_percentage&#125;&#125;&#58; 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-other_taxes_percentage y eatc_sale.eatc-other_taxes_percentage 
 Orden en el formulario &#58; 7 
 Descripcin ( tooltip ) &#58; Ingresa el porcentaje de otros impuestos aplicables al producto, como por ejemplo IMPOCONSUMO 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna. 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc-other_taxes_percentage 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-other_taxes_percentage=&#123;&#123; eatc_sale_prd_mstr. eatc-other_taxes_percentage&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-other_taxes_percentage=&#123;&#123; eatc_sale_prd_mstr. eatc-other_taxes_percentage&#125;&#125; 

&#160; 
 Contiene alrgenos? &#123;&#123;eatc_sale_prd_mstr.eatc-contains_alergens&#125;&#125;&#58; 
 [+++] En este caso se traer desde el maestro eatc_sale_prd_mstr 
 Informacin tcnica del parmetro&#58; eatc_sale_prd_mstr.eatc-contains_alergens y eatc_sale.eatc-contains_alergens 
 Orden en el formulario &#58; 8 
 Descripcin ( tooltip ) &#58; no aplica. 
 Tipo &#58; Texto 
 Tipo de dato&#58; boleano&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. 
 La informacin se toma de&#58; 
 Consulta a partir de lo que trae el selector inicial&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_id =&#123;&#123;current&#58;eatc_sale_prd_mstr. eatc-odd_id &#125;&#125; eatc-contains_alergens 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-contains_alergens=&#123;&#123; eatc_sale_prd_mstr. eatc-contains_alergens&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp;eatc-contains_alergens=&#123;&#123; eatc_sale_prd_mstr. eatc-contains_alergens&#125;&#125; 

&#160; 
 Nota &#58; De aqu en adelante funciona se manera similar al formulario de captura de informacin para productos nuevos&#58; 

&#160; 
 Fecha de caducidad de los artculos 
 [***] Similar a la captura para anuncios de donacin pero guardando en object stores diferentes&#58; Para cada registro se debe de manera opcional , seleccionar la fecha ms prxima de vencimiento.&#160; Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parmetro (eatc_sale. eatc-closer_expiration_date ) ser&#58; 0000-00-00 . Si el usuario desea registrar una fecha, deber ingresar a un &quot; date picker &quot; o &quot; selector de fechas &quot; que presenta por defecto, como sugerencia de &quot;fecha ms prxima de vencimiento&quot; la sumatoria de la fecha actual ms el nmero que se encuentra en el parmetro&#160; eatc_cua. days_before_expiration ( **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] )) .&#160; Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vaco o nulo, el valor por defecto que debe tomarse es &quot;5&quot;, para realizar la sumatoria y asi sugerir la fecha .&#160; El usuario podr modificar esa fecha sugerida, y el sistema no le permitir ingresar fechas anteriores al da actual ms 1 da. (solo se podrn ingresar fechas posteriores). El dato resultante (tipo fecha con formato AAAA-MM-DD) se deber guardar en el parmetro eatc_sale. eatc-closer_expiration_date 
 Informacin tcnica del parmetro&#58; eatc_sale.eatc-closer_expiration_date 
 Orden en el formulario &#58; 9 
 Descripcin ( tooltip ) &#58; selecciona la fecha ms prxima de expiracin de los productos ofertados. 
 Tipo &#58; Date Picker 
 Tipo de dato&#58; date&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-closer_expiration_date =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-closer_expiration_date =&#123;&#123;input&#125;&#125; 

&#160; 
 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_min_sale_unit_price 
 Orden en el formulario &#58; 10 
 Descripcin ( tooltip ) &#58; Ingresa el precio de venta al pblico (incluyendo tarifas e impuestos) para promover la venta de ltimo minuto 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125; 

&#160; 
 Porcentaje de descuento para venta de ltimo minuto (sirve para incentivar la compra) 
 [+++] Nuevo campo de captura 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_max_discount 
 Orden en el formulario &#58; 11 
 Descripcin ( tooltip ) &#58; Ingresa el porcentaje descuento sobre el precio de venta al pblico real, que representa el precio de venta al pblico de ltimo minuto. El poder visualizar estos descuentos ayuda a estimular la compra. 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; no (en un futuro puede cambiar) 
 Validacin &#58; no aplica (en un futuro puede cambiar) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_max_discount =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_max_discount =&#123;&#123;input&#125;&#125; 

&#160; 
 [Clculo oculto] Precio de venta al publico (PVP&#58; se calcula si se obtuvieron los dos datos anteriores) 
 [+++] Nuevo campo que se calcula a partir de las dos capturas anteriores 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_unit_price 
 Tipo de dato&#58; float&#160; 
 Obligatoriedad &#58; no (en un futuro puede cambiar) 
 Validacin &#58; no aplica (en un futuro puede cambiar) 
 Cmo se calcula&#58; 
 eatc-odd_unit_price - eatc-odd_max_discount *eatc-odd_unit_price = eatc-odd_min_sale_unit_price 
&#160; 
 eatc-odd_unit_price= eatc-odd_min_sale_unit_price /( 1-eatc-odd_max_discount ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_unit_price =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_unit_price =&#123;&#123;input&#125;&#125; 

&#160; 
 Cantidad de productos disponibles para la venta (la venta se realizar por unidades) 
 [***] Similar a la captura para anuncios de donacin (eatc-odd_original_quantity y eatc-odd_quantity) pero guardando en un object store diferente 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_original_quantity y eatc_sale.eatc-odd_quantity 
 Orden en el formulario &#58; 12 
 Descripcin ( tooltip ) &#58; Ingresa las cantidades del producto o artculo disponible para la venta. Recuerda que los artculos se vendern por separado. 
 Tipo &#58; Pregunta abierta numrica ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAN ) 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; Obligatoriedad. Mayor o igual que uno. 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_original_quantity =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_quantity =&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp; eatc-odd_original_quantity =&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/?_tabla=eatc_sale_prd_mstr&amp;_operacin=insert&amp; eatc-odd_quantity =&#123;&#123;input&#125;&#125;&#160; 

&#160; 
 [Campo oculto] Estado del producto para la venta (eatc_state=sale) 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-odd_state 
 Tipo de dato&#58; string&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Dado que el producto se oferta, se registra en el parmetro eatc_state el valor &#123;&#123;input&#125;&#125; &quot;sale&quot; 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_state =sale 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-odd_state =sale 

&#160; 
 *****NUEVO****** [Campo oculto] tiempo de vida de la oferta&#160; 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-offer_lifetime [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato&#58; integer&#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Dado que se gener al seleccionar al principio de la creacin de la oferta su tiempo de vida til 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-offer_lifetime =&#123;&#123;eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-offer_lifetime =&#123;&#123;eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 

&#160; 
 *****NUEVO****** [Campo oculto] fecha y hora de finalizacin de tiempo de vida de la oferta 
 [+++] Nuevo campo 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-offer_lifetime_until [PENDIENTE DE DOCUMENTACIN] 
 Tipo de dato&#58; datetime&#160; (AAAA-MM-DD HH&#58;MM&#58;SS) 
 Obligatoriedad &#58; si 
 Validacin &#58; de obligatoriedad 
 Cmo se registra&#58; 
 Se le suma al dato eatc_sale. eatc-date_time las horas registradas en el dato anterior (tiempo de vida de la oferta) eatc_sale. eatc-offer_lifetime 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-offer_lifetime_until =&#123;&#123;eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacin=insert&amp; eatc-offer_lifetime_until =&#123;&#123;eatc_sale. eatc-offer_lifetime + eatc_sale_timeout_rules. eatc-timeout_in_hours &#125;&#125; 
&#160; 
 Venta producto existente&#58; Botn&#58; &quot;Agregar Producto&quot;&#58; Parmetros para crear en eatc_sale 
 [***] En trminos generales funciona de manera similar al proceso para agregar producto en la creacin de anuncios de donacin (incluyendo la aparicin en el listado, la validacin de que no se repita ni en el listado ni en lo que se registra, etc.) pero con dos diferencias&#58; el object store en el cual se registra (que ahora ser eatc_sale de la cuenta &quot;eatcloud&quot;) y que no se requerir llamar a un webservice adicional al final de la creacin para crear un &quot;encabezado&quot; (en proceso que esta funcionalidad solo crear detalles). 

&#160; 
 &#123;&#123;Parmetros creacin en eatc_sale &#125;&#125;&#58; &amp; eatc-pod_name =&#123;&#123;eatc-name&#125;&#125;&amp;&amp; eatc-pod_id =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-pod_lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-pod_lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-pod_adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-pod_city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-pod_country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125;&amp; eatc-doc =&#123;&#123;input&#125;&#125;&amp; eatc-dona_header_code =&#123;&#123;input&#125;&#125;&amp; eatc-date_time =&#123;&#123;input&#125;&#125;&amp; eatc-date_time_2 =&#123;&#123;input&#125;&#125;&amp; eatc-donor_code =&#123;&#123;input&#125;&#125;&amp; eatc-donor =&#123;&#123;input&#125;&#125;&amp; eatc-odd_name =&#123;&#123;Nombre del producto&#125;&#125;&amp; eatc-odd_id =&#123;&#123;input&#125;&#125;&amp; eatc-odd_image =&#123;&#123;input&#125;&#125;&amp; eatc-odd_description =&#123;&#123;input&#125;&#125;&amp; eatc-odd_unit_weight_kg =&#123;&#123;input&#125;&#125;&amp; eatc_VAT_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-other_taxes_percentage =&#123;&#123;input&#125;&#125;&amp; eatc-contains_alergens =&#123;&#123;input&#125;&#125;&amp; eatc-closer_expiration_date =&#123;&#123;input&#125;&#125;&amp; eatc-odd_min_sale_unit_price =&#123;&#123;input&#125;&#125;&amp; eatc-odd_max_discount =&#123;&#123;input&#125;&#125;&amp; eatc-odd_unit_price =&#123;&#123;input&#125;&#125;&amp; eatc-odd_original_quantity =&#123;&#123;input&#125;&#125;&amp; eatc-odd_quantity =&#123;&#123;input&#125;&#125;&amp; eatc-odd_state =sale&amp; eatc-offer_lifetime =&#123;&#123;input&#125;&#125;&amp; eatc-offer_lifetime_until =&#123;&#123;input&#125;&#125; 
&#160; 
 [***] Se guarda la informacin en el object store eatc_sale de la cuenta eatcloud&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale&amp;_operacion=insert&amp; &#123;&#123;Parmetros creacin en eatc_sale &#125;&#125; 

 Tipo de venta&#58; producto box&#58; 
 A continuacin se establecen los campos que debern tomarse para la creacin de un producto para la venta a partir de la seleccin de un producto ya existente en el maestro eatc_sale_prd_mstr, y se establece su registro en el object store correspondiente&#58; eatc_sale . 
 Se presenta a continuacin el diseo de la interfaz (el cual se entregar prximamente maquetado en html), y que ser la gua para la interfaz de usuario, teniendo en cuenta los aspectos tcnicos que se establecen ms adelante (como nombramiento y ordenamiento de las preguntas. Lo presentado en el diseo ser indicativo y se debe implementar los campos de seleccin y captura de acuerdo a lo que se expresa ms abajo en la documentacin). 

 Funcionalidad similar a la anterior ( tipo de venta&#58; producto existente ) 
 [***] Totalmente similar al anterior, con la nica diferencia que en el selector solo aparecern productos cuya eatc-odd_typology_a es igual a &quot; box &quot; (siendo esta la nica diferencia) 
 Segn sea el caso se utilizarn las siguientes consultas para popular los selectores&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_typology_a =box 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_sale_prd_mstr? eatc-odd_typology_a =box 
&#160; 
 Ejemplo&#58; cuenta &quot;colombia&quot;, ambiente de pruebas&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_typology_a =box &#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_sale_prd_mstr? eatc-odd_typology_a =box &#160; 
&#160; 

&#160; 
 Listado de productos agregados 
 A medida que se van agregando productos debe generarse un listado con los que han sido agregados.&#160; Este listado debe mostrar la siguiente informacin&#58; 
&#160; 
 Tumbnail Fotografa / Imagen del producto &#123;&#123;eatc_sale_prd_mstr.eatc-odd_image&#125;&#125;&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_image=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_image&#125;&#125; 
&#160; 
 Nombre del producto o artculo &#123;&#123;eatc_sale_prd_mstr.eatc-odd_name&#125;&#125;&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_name=&#123;&#123;eatc_sale_prd_mstr.eatc-odd_name&#125;&#125; 
&#160; 
 Peso unitario del producto en KG &#123;&#123;eatc_sale_prd_mstr.eatc-odd_unit_weight_kg&#125;&#125;&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_unit_weight_kg=&#123;&#123; eatc_sale_prd_mstr. eatc-odd_unit_weight_kg&#125;&#125; 
&#160; 
 Precio de venta al pblico para venta de ltimo minuto (incluye tarifas, impuestos y descuento de ltimo minuto). 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_min_sale_unit_price =&#123;&#123;output&#125;&#125; 
&#160; 
 Cantidad de productos disponibles para la venta 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale? eatc-odd_original_quantity =&#123;&#123;input&#125;&#125; 
&#160; 
 Borrar 
 Para cada registro debe colocarse la opcin de &quot;borrar&quot; con el nimo de eliminar el registro particular 
&#160; 
 Editar 
 Para cada registro debe colocarse la opcin de &quot;editar&quot; que debe recargar en el formulario de captura originar los datos del registro en cuestin para modificarlos. 
&#160; 
 BOTN &quot;TERMINAR DE AGREGAR PRODUCTOS&quot; 
 Dado que esta funcionalidad no genera encabezados, al presionar este botn, funcionar de manera muy similar a como lo hace el botn &quot;anunciar donacin&quot; de la funcionalidad de &quot;creacin de anuncios de donacin&quot; simple y llanamente, este botn no llamar ningn proceso para la creacin de encabezados (que de hecho para este mdulo funcional no existirn como tal). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreacion-de-venta-de-ultimo-minuto-eatc_sale_upl%2F90244EmbeddedImage%2520%283%29.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcreacion-de-venta-de-ultimo-minuto-eatc_sale_upl%2F90244EmbeddedImage%2520%283%29.png 
 NUEVA WAPP 

 CREACIN DE OFERTA DE LTIMO MINUTO (EATC_SALE_UPL)