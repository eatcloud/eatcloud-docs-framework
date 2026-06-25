# deprecada-de-generación-de-la-donación-en-especie.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En esta funcionalidad se le informar ael usuario podr escoger, entre una serie de opciones definidas por baco, los alimentos que pueden ser donados en la Alimentatn. El usuario registrar los kilogramos a donar de cada producto.&#160; Esta informacin se deber almacenar en una estructura de datos eatc_dona_alimentaton, especificando el donante (eatc_donor&#58; informacin que se toma del registro del usuario en la plataforma es decir de la informacin que se guarda en eatc_volunteers) y el punto de donacin (eatc_pod&#58; que corresponde al punto de donacin que el usuario selecciona para realizar la donacin), junto con el detalle de la donacin (los productos y los kilogramos donados). 

 Consulta de categoras&#58; 
 El sistema cosulta el API de eatc_odds_alimentaton (Objetos de donacin para la Alimentatn), para determinar que categoras estn disponibles 
&#160; 
 Ejemplo&#58; 
 para consultar el API se utiliza la siguiente sentencia 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria= _* 
&#160; 
 Las categoras que se muestran en el selector corresponden a un &quot; select distinct &quot; del parmetro &quot; categoria &quot; que arroja la anterior consulta. 
&#160; 
 El usuario podr seleccionar una de las categoras disponibles a fin de establecer que productos pueden ser donados. 

&#160; 
 Consulta de productos susceptibles de ser donados 
 Teniendo la &quot; categoria &quot; seleccionada, se utiliza el API para traer los productos que se listan en la vista. 
&#160; 
 Ejemplo&#58; 
 El usuario selecciona la categoras &quot; no perecederos &quot;, la consulta que se debe realizar para listar los productos es la siguiente&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_odds_alimentaton?categoria=no perecederos 
&#160; 
 Listado de productos&#58; 
 En el listado de productos se coloca la informacin correspondiente al parmetro &quot;alimentos&quot; que trae la anterior consulta y la cantidad donada por defecto ser &quot;0 Kg&quot; 
&#160; 
 A manera de carrito de compras, al frente del nombre de cada producto se coloca un registro para aumentar desde &quot;0 Kg&quot; en adelante, la cantidad a ser donada . 
&#160; 
 Los botones de &quot;-&quot; y &quot;+&quot; servirn para ir agregando de a un kilogramo donado, al formulario.&#160; Tambin se debe habilitar la posibilidad de ingresar el dato directamente con el teclado numrico (es decir sin utilizar los botones de ms y menos). 

&#160; 
 Botn &quot;Donar&quot;&#58; 
 Al presionar dicho botn se debe generar un objeto que debe transmitirse utilizando el api respectiva, al esquema de persistencia en la nube.&#160;&#160; 
 Ejemplo [PENDIENTE ENTREGA DE API PARA ESCRITURA]&#58; 
 El se debe hacer un llamado al API, para publicar el alimento donado a saber 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_alimentaton? 
&#160; 
 Si el usuario no est registrado, debe enviarlo a la funcionalidad de registro de usuario . 

 La App deber almacenar la informacin de la siguiente manera&#58; 
 eatc-dona_header_code = Cdigo de la cabecera del anuncio de donacin.&#160; Cdigo nico que genera la App (por lo tanto debe incorporar alguna informacin del donante) 
 eatc-date_time = Fecha y hora del anuncio de donacin (en formato&#58; AAAAMMDDHHMMSS).&#160; Se toma con la fecha y hora del dispositivo. 
 eatc-pod_id = Identificador nico del punto de donacin.&#160; Se toma desde la funcionalidad &quot; Dashboard principal - eleccin del punto de donacin &quot; 
 eatc-odd_id = Identificador nico del producto o artculo donado puede corresponder al mismo dato del parmetro &quot;alimentos&quot; , que se utiliz para construir el listado de productos (se toma el mismo nombre porque no se entregaron identificadores nicos para este maestro). 
 eatc-odd_name = Nombre o descripcin del producto a susceptible de donacin; corresponde al mismo dato del parmetro &quot;alimentos&quot; , que se utiliz para construir el listado de productos . 
 eatc-odd_quantity = Cantidad del producto o artculo donado; corresponde al dato de la cantidad a ser donada. 
 eatc-odd_total_cost = Se enva el dato vaco. 
 eatc-odd_code = Se enva el dato vaco . 
 eatc-odd_code_type = Se enva el dato vaco . 
 eatc_donor_code = Identificador o cdigo del donante (el mismo que se muestra en la vista&#58; men de usuario ) 
 eatc_donor = nombre del donante 
 eatc-odd_typology_a = Primera tipologa del artculo o producto donado, corresponde al dato de &quot;categora&quot; que se utiliz para construir el listado de productos 
 eatc-odd_typology_b = Se enva el dato vaco . 
 eatc-odd_typology_c = Se enva el dato vaco . 
 eatc-odd_unit_cost = Se enva el dato vaco . 
 eatc-odd_total_weight_kg = /Cantidad del producto o artculo donado; corresponde al dato de la cantidad a ser donada. 
 eatc-odd_total_height_cm = Se enva el dato vaco . 
 eatc-odd_total_width_cm = Se enva el dato vaco . 
 eatc-odd_total_length_cm = Se enva el dato vaco . 
 eatc-odd_total_volume_cm3 = Se enva el dato vaco . 
 eatc-odd_state = Se enva el dato vaco . 
 eatc-odd_rejection_cause = Se enva el dato vaco . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=0ed6957343a44ac0bfa048199cf7e151&ext=png&ow=750&oh=2074, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=0ed6957343a44ac0bfa048199cf7e151&ext=png&ow=750&oh=2074 
 App usuario final - Alimentatn 

 757.000000000000 

 DEPRECADA: GENERACIN DE LA DONACIN EN ESPECIE