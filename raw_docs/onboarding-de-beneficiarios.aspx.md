# onboarding-de-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar el registro de beneficiarios  en la plataforma a partir de un registro en la misma (dada de alta por parte del usuario final, a diferencia de lo que se manej asta marzo de 2020, en donde esto se realizaba a travs de carga de datos).  Esto se debe implementar en una pgina web responsiva que pueda ser invocada desde la App Beneficiarios. Vale la pena anotar que parte de la estructura de los beneficiarios se hered del sistema insights que se cre para baco, por lo tanto hay que revisar si se pueden reutilizar componentes ya desarrollados en dicha plataforma (y tambin reutilizar lo implementado en el Registro Simple de Puntos de Donacin ) 

 Registro a cuenta usuario especfica. 
 El registro de punto de donacin se debe generar para una cuenta usuario especfica la cual se debe generar a partir de la URL respectiva  

 URL segn cuenta maestra 
 {{URL_entorno_beneficiarios}}/registro/{{_DOM.cua_master}} 

 Ejemplo (ambiente productivo): 
 Si se van a registrar puntos de donacin para la cuenta " abaco ", se debera realizar mediante el vnculo https://beneficiarios.eatcloud.info/abaco/registro   (en pruebas: https://devbeneficiarios.eatcloud.info/abaco/registro ).  

 Validacin de la existencia de la cuenta maestra 
 La app deber validar que la cuenta maestra, en este caso "abaco" est registrada en datagov, es decir, que la siguiente consulta: ***NUEVO*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco (anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=abaco) traiga una resultado vlido. 

 ***NUEVO : CAPTURA PREVIA DEL DOCUMENTO DE IDENTIFICACIN TRIBUTARIA PARA ESTABLECER SI EL DONANTE SE INSCRIBE POR PRIMERA VEZ O EST INSCRIBIENDO UNA SUCURSAL *** 
 Campos para el registro 
 Los campos para el registro debern ser los siguientes https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_campos   y https://beneficiarios.eatcloud.info/api/abaco/eatc_users?_campos , 

 Validacin de existencia de identificador_unico_registro: de acuerdo a los datos registrados en la respectiva cuenta maestra 
 Este campo de captura debe colocarse de primero en el formulario de registro, y  como campo nico de captura (a diferencia de la implementacin inicial, que era un campo integrado al resto del formulario): 

 Documento de identificacin fiscal: 
 Label: class= lbl_identificacion_tributaria_doma 
 Ayuda: class=lbl_sin_giones_ni_dv [concat] class=lbl_long_minima_campo [concat] {{eatc_cua_master- eatc_doma_id_min_digit_val }} [concat] class=lbl_caracteres 
 Tipo de campo de captura: text_input 
 Tipo de dato: {{eatc_cua_master. eatc_doma_id_datatype }} 
 Validaciones:  Aplica las validaciones de nmero de dgitos , tipo de dato que ms adelante se detallan 

 Con los datos ingresados en el campo de captura el sistema realiza la siguente consulta (con el nimo de verificar si ya existe un registro de la organizacin en el sistema 
 {{URL_entorno_beneficiarios}}/api/ {{cua_master}}/ eatc_donation_managers?identificador_unico_registro={{input}} 

 O si tiene registro de surcursales 
 {{URL_entorno_beneficiarios}}/api/ {{cua_master}}/ eatc_donation_managers?identificador_unico_registro={{input}} _lk 

 Si la anterior consulta no trae resultados, entonces el sistema permite proceder con el registro, tal cual se realizaba en la primera versin del formulario, es decir, desplegando todos los campos de captura. 

 Si la(s) consulta(s) traen una respuesta vlida, entonces el sistema deber desplegar el siguiente cuadro de dilogo 
class= lbl_doma_previamente_registrado 

 "Tu organizacin ya est registrada en EatCloud.  Deseas crear una sucursal? 

 Y desplega, los botones 
class= lbl_no => No est creado el label en la plataforma ONB_beneficiarios => Crearlo 

class= lbl_si => No est creado el label en la plataforma ONB_beneficiarios => Crearlo 

 El usuario selecciona la opcin "No" 
 El sistema realiza la siguiente consulta 
 {{URL_entorno_beneficiarios}}/api/ {{cua_master}}/ eatc_donation_managers?identificador_unico_registro={{input}} _lk &_cmp= organizacin,identificador_unico_registro,eatc_state,fecha2,causal_inactivo  

 Si la respuesta arroja un solo resultado 

 El sistema despliega la siguiente informacin: 
 (class= lbl_tu_organizacion ) Tu organizacin {{eatc_donation_managers. organizacin }}, (class= lbl_registrada_con_estado )se encuentra registrada en EatCloud y tiene un estado {{eatc_donation_managers. eatc_state }} (class= lbl_desde )desde {{eatc_donation_managers. fecha2 }} 

 Si la organizacin tiene un estado diferente a " activo e inactivo " el mensaje se complementa con la siguiente informacin: 
 (class= lbl_la_causa ) la causa de tu estado es {{eatc_donation_managers. causal_inactivo }} 

 PARA POSTERIOR IMPLEMENTACIN 
 (class= lbl_consultar_mas_info )Deseas consultar ms informacin? 
 class= lbl_no => No est creado el label en la plataforma ONB_beneficiarios => Crearlo 
 Si el usuario  selecciona esta opcin, el sistema cierra el modal y sale. 
 class= lbl_si => No est creado el label en la plataforma ONB_beneficiarios => Crearlo 
 Si el usuario  selecciona esta opcin, el sistema realiza la siguiente consulta: 

 Si la organizacin tiene estado " activo " el mensaje se complementa con la siguiente informacin: 
 (class= lbl_ya_puedes_usar_app ) Ya puedes disfrutar de los beneficios de hacer parte de la comunidad de rescate alimentario EatCloud, entrando a nuestra app, disponible en https://play.google.com/store/search?q=eatcloud&c=apps >aqu 

 Si la organizacin tiene estado " inactivo " el mensaje se complementa con la siguiente informacin: 

 El sistema realiza la siguiente consulta: 
 {{URL_entorno_beneficiarios.}}/api/{{_DOM.cua_master}}/eatc_donation_managers?beneficiary_ecosystem_leader=y&_cmp= organizacin 

 Y con la informacin recibida arma el siguiente mensaje 
 (class= lbl_aun_no_haz_sido_activado )Aun no has sido activado por nuestro lder de ecosistema social {{eatc_donation_managers. organizacin }}.  Continuamente trabajamos para traer ms donantes a la plataforma y con ello poder activar a ms organizaciones como la tuya. 

 Si la respuesta arroja varios resultados 

 El sistema despliega la siguiente informacin: 
 (class= lbl_tu_organizacion_registra_sucursales ) Tu organizacin registra varias sucursales a saber: 

 El sistema crea una tabla con las siguientes columnas 
 (class= lbl_nombre ) Nombre => {{eatc_donation_managers. organizacin }} 
 (class= lbl_estado ) Estado => {{eatc_donation_managers. eatc_state }} 
 (class= lbl_desde ) Desde {{eatc_donation_managers. fecha2 }} 
 (class= lbl_causal_inactivo ) Causal de inactividad => {{eatc_donation_managers. causal_inactivo }} 

 Si la organizacin tiene sucursales en estado " activo "  al final se adiciona el siguiente mensaje 
 (class= lbl_suc_activas_pueden_usar_app ) Tus sucursales activas ya pueden disfrutar de los beneficios de hacer parte de la comunidad de rescate alimentario EatCloud, entrando a nuestra app, disponible en https://play.google.com/store/search?q=eatcloud&c=apps >aqu 

 Si la organizacin tiene sucursales en estado " inactivo "  al final se adiciona el siguiente mensaje 

 El sistema realiza la siguiente consulta: 
 {{URL_entorno_beneficiarios.}}/api/{{_DOM.cua_master}}/eatc_donation_managers?beneficiary_ecosystem_leader=y&_cmp= organizacin 

 Y con la informacin recibida arma el siguiente mensaje 
 (class= lbl_suc_inactivas )Aun tienes sucursales que no han sido activadas por nuestro lder de ecosistema social {{eatc_donation_managers. organizacin }}.  Continuamente trabajamos para traer ms donantes a la plataforma y con ello poder activar a ms organizaciones como la tuya. 

 El usuario selecciona la opcin "Si" (desea crear una sucursal) 
 El sistema trae la informacin que es comn a las sucursales de una misma organizacin y la precarga en el formulario 

 Para la informacin que cambia de sucursal a sucursal, se habilitan los campos de captura, tal cual se habilitaron en el formulario original, a saber: 
 Sufijo de la sucursal 
 Datos de ubicacin: coordendas, departamento, ciudad, direccin, telfonos 
 Datos de jornadas de atencin 
 Datos de capacidad 
 Datos de usuario y contrasea 

 Validacin de nmero de dgitos del identificador_unico_registro (consultando datos de cuenta maestra en datagov) 
 Adicional a las anteriores validaciones implementadas para el identificador_unico_registro se deber implementar una para que en la cuenta maestra respectiva se valide el nmero de dgitos (mnimo y mximo) que contiene dicho indentificador (con el nimo de obtener calidad de datos). 

 Para ello se deber consultar datos de configuracin de la cuenta maestra respectiva y a partir de dicha consulta realizar la validacin respectiva. La consulta es la siguiente: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua={{CUA_master}}&_cmp= eatc_doma_id_min_digit_val,eatc_doma_id_max_digit_val 

  Antes: {{URL_entorno_beneficiarios}}/api/data/eatc_cua_master?eatc_cua={{CUA_master}} 

 Esta consulta trae los datos: 

 eatc_doma_id_min_digit_val: que corresponder al nmero mnimo de dgitos que debe contener el identificador_unico_registro que se ingresa en el formulario. Si el identificador ingresado por el usuario tiene menos dgitos que los indicados en este dato, no se permitir realizar el registro. 

 eatc_doma_id_max_digit_val: que corresponder al nmero mximo de dgitos que debe contener el identificador_unico_registro que se ingresa en el formulario. Si el identificador ingresado por el usuario tiene ms dgitos que los indicados en este dato, no se permitir realizar el registro. 

 Ejemplo: 
 Para la CUA_master: abaco, en entorno productivo se debe realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco   

 Como la misma trae los siguientes valores: 

 eatc_doma_id_min_digit_val: "9". 
 eatc_doma_id_max_digit_val: "9". 

 Esto quiere decir que en campo de captura respectivo no pueden identificadores con menos de 9 y ms de 9 dgitos (es decir solo se aceptan identificadores de 9 dgitos). 

 Validacin de tipo de dato (consultando datos de cuenta maestra en datagov) 
 Adicional a las anteriores validaciones implementadas para el identificador_unico_registro se deber implementar una para que en la cuenta maestra respectiva se valide el tipo de dato del registro que contiene dicho indentificador (con el nimo de obtener calidad de datos). 

 Para ello se deber consultar datos de configuracin de la cuenta maestra respectiva y a partir de dicha consulta realizar la validacin respectiva. La consulta es la siguiente: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua={{CUA_master}}&_cmp= eatc_doma_id_datatype 

 Registro de eatc_cua_master 

 Al efectuar el registro del beneficiario, el dato que se digit en la URL para acceder al registro de usuario 
 {{URL_entorno_beneficiarios}}/ {{cua_master}} /registro 

 Se deber llevar al campo 
  eatc_donation_managers. eatc_cua_master 

 Al realizar el registro del beneficiario 

ONB_beneficiarios 

 Botn "Registrar gestor de donaciones" 
 Validacin de coordenada: apuntando a maestro de municipalidades en datagov 
 Dada la circunstancia que nos estn ingresando coordenadas al sistema que no corresponden a las direcciones, municipios y departamentos registrados, se hace necesario establecer un mecanismo de validacin que ayude a garantizar en alguna medida calidad con los datos de georeferenciacin desde la fuente. 

 La validacin operara de la siguiente manera: 

 Se toman las coordenadas registradas en el formulario: coordenadas y se guardan en variables ( lat1,lon1 ) 
 Con el dato ciudad (centro poblado) y sus respectivos cdigos se consulta la coordenada asociada a este punto 
 https://datagov.eatcloud.info/api/{{eatc_cua_master. eatc-country }}/eatc_municipalities?eatc-city={{ciudad_seleccionada}} 

 Si la consulta arroja varios resultados, se debe refinar con el siguiente llamado: 
 https://datagov.eatcloud.info/api/{{eatc_cua_master. eatc-country }}/eatc_municipalities?eatc-city={{ciudad_seleccionada}}&eatc-populated_center_type=CABECERA%20MUNICIPAL 

 Ejemplo: 
 Para una seleccin de la cabecera municipal de Medelln, la consulta sera as: 

 https://datagov.eatcloud.info/api/co/eatc_municipalities?eatc-city=MEDELLIN   

 Como la bsqueda da respuesta mltiple, entonces se refina con el siguiente llamado: 

 https://datagov.eatcloud.info/api/co/eatc_municipalities?eatc-city=MEDELLIN&eatc-populated_center_type=CABECERA%20MUNICIPAL   

 de esta consulta se toman los datos eatc-lat y eatc- y se guardan en variables ( lat2,lon2 ). 

 Con el siguiente script se calcula la distancia entre estas dos coordenadas: 

 function getKilometros(lat1,lon1,lat2,lon2){ 
  rad = function(x) {return x*Math.PI/180;} 
    //var R = 6378.137; //Radio de la tierra en km 
    var R = 63781; //Radio de la tierra en km 
    var dLat = rad( lat2 - lat1 ); 
    var dLong = rad( lon2 - lon1 ); 
    var a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(dLong/2) * Math.sin(dLong/2); 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; 
   return d.toFixed(3); //Retorna tres decimales 
  } 

 Si la distancia es mayor a 50 KM para ciudades principales y 20 KM para ciudades pequeas (o en general 50 KM), se debe mostrar el siguiente anuncio: 

 La coordenada registrada parece estar muy distante del municipio seleccionado.  Le solicitamos el favor revise el "pin" en el mapa e intente nuevamente realizar el registro. 

 Y no debe permitir realizar el registro. Si la distancia es menor a la estipulada, se debe dejar pasar. 

 Validacin dinmica del tipo de dato del identificador_unico_registro 
 Dado que los formatos de los identificadores nicos de registro (o nmeros de identificacin tributaria) varan de pas a pas, no es posible que la validacin de que el dato sea solamente numrico (sin puntos, guiones ni dgito de verificacin) funcione para todas las cuentas maestras, entonces se establecen (inicialmente) adicional a la validacin del nmero de dgitos del dato (a partir del dato eatc_cua_master. eatc_doma_id_min_digit_val   y eatc_cua_master. eatc_doma_id_max_digit_val ) se validar si el campo recibe solamente datos numricos (integer), o recibe datos alfanumricos (string).  Para determinar cul de las dos validaciones se debe realizar en el respectivo campo de captura, el sistema debe realizar la siguiente consulta: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua_master?eatc_cua={{eatc_cua. eatc_cua_master }}&_distinct= eatc_doma_id_datatype 
 Para determinar si el campo recibe solamente nmeros, o recibe nmeros y letras. 

 Ejemplo 1 : ambiente de pruebas DOM. cua_master = abaco : 

 El sistema por lo tanto debe realizar la siguiente consulta:  
   https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua= abaco &_distinct= eatc_doma_id_datatype     

 Como la respuesta que se recibe es: eatc_doma_id_datatype : "integer" entonces el sistema en el campo de captura solo debe recibir datos numricos (tal como funciona ahora) 

 Ejemplo 2 : ambiente de pruebas DOM. cua_master = mexico : 

 El sistema por lo tanto debe realizar la siguiente consulta:  
   https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua= mexico &_distinct= eatc_doma_id_datatype       

 Como la respuesta que se recibe es: eatc_doma_id_datatype : "string" entonces el sistema en el campo de captura permitir recibir datos alfanumricos (a diferencia de como funciona ahora, dado que solamente recibe campos numricos) 

 Para ms adelante se debe revisar cmo registrar en el maestro de cuentas maestras, este tipo de validaciones que para el caso de mxico son las que aplican: 

 Registro Federal de Contribuyentes 

 Es el RFC de las personas morales (empresas) est integrado por 3 letras, 6 nmeros y 3 caracteres alfanumricos ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&pais=MX&idlabel=lbl_numero_identificacion_tributaria_desc ). Se organizan de la siguiente forma: 

 Los tres caracteres iniciales corresponden a las iniciales de la persona moral. 
 Los seis caracteres que le siguen corresponden a la fecha de fundacin de la organizacin en el siguiente orden: dos dgitos para indicar el ao, dos para el mes y dos para el da. 
 Los ltimos tres caracteres corresponde a la homoclave asignada por el SAT (Sistema de Administracin Tributaria). 

 Registro por defecto automtico del dato "capacidad_recogida" 
 Se va a suprimir del formulario la captura del dato de " capacidad_recogida " ( Capacidad de Recogida por Donacin en Kilogramos ).  En reemplazo se deber tomar automticamente el dato del parmetro " limite_superior_kg " que arroja la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 

 (Ejemplo DOM. cua_master =abaco : https://beneficiarios.eatcloud.info/api/abaco/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 ) 

 Registro por defecto automtico del dato "capacidad_gestin" 
 Se va a suprimir del formulario la captura del dato de " capacidad_gestion " ( Capacidad de Total de Gestin de Donaciones en Kilogramos por da ). En reemplazo se deber tomar automticamente el dato del parmetro " limite_superior_kg " que arroja la siguiente consulta:  
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 

 (Ejemplo _ DOM. cua_master =abaco : https://beneficiarios.eatcloud.info/api/abaco/eatc_max_kg_x_doma_typology_b?eatc_doma_typology_b=3 ) 

 Selector de "Provincias, departamentos, estados" y luego de "Ciudades" genrico segn el pas de la cuenta y validando informacin de los selectores con la coordenada previamente seleccionada ****NUEVO: dinamizando el radio de consulta segn cuenta maestra**** 

 Para poder popular el  
 1. Determinacin del pas de la cuenta maestra, para a partir del mismo consultar los datos maestos de municipalidades: 

 A partir de la consulta genrica: 
 {{URL_entorno_datagov}} /api/eatcloud/eatc_cua_master?eatc_cua={{_DOM.cua_master}} 

 El sistema toma los siguientes datos  
eatc_cua_master. eatc-country 
eatc_cua_master. eatc_geo_query_radius_km 

 Para realizar la siguiente consulta. 

 Ejemplo Argentina ambiente de pruebas: 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=argentina ( 
eatc_cua_master. eatc-country = ar 
eatc_cua_master. eatc_geo_query_radius_km =  (vaco) 

 Ejemplo Mxico ambiente de pruebas 
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=mexico   
eatc_cua_master. eatc-country = mx 
eatc_cua_master. eatc_geo_query_radius_km = 25 

 2. Determinacin de la provincia (eatc-province) segn el maestro eatc_municipalities respectivo y sus coordenadas 

 Con los datos recolectados se realiza la siguiente consulta: 
 {{URL_entorno_datagov}} /get/{{eatc_cua_master. eatc-country }}/getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue ={{latitud_seleccionada_mapa}},{{longitud_seleccionada_mapa}}& showfield = eatc-province & km ={{ eatc_cua_master. eatc_geo_query_radius_km }} 

 Si la consulta del dato {{ eatc_cua_master. eatc_geo_query_radius_km }} arroja un dato vacio, nulo, o en cero, el valor por defecto sera " 15 "  

 Ejemplo Argentina ambiente de pruebas: 
 https://dev.datagov.eatcloud.info/get/ar/getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue =-34.6156624,-58.50351& showfield = eatc-province & km = 15 

 Ejemplo Mxico ambiente de pruebas 
 https://dev.datagov.eatcloud.info/get/mx/getpuntos?table=eatc_municipalities&fieldname=eatc-lat,eatc-lon&fieldvalue=19.4410303,-99.2000994&showfield=eatc-province&km= 25   

 El sistema debe tomar el dato eatc_municipalies. eatc-province ( haciendo un distinct sobre las respuestas obtenidas ) para incorporarlo al selector. 

 3. Determinacin de la ciudad segn el maestro eatc_municipalities y la seleccin previa de departamento 

 A partir de la seleccin anterior se debe realizar la siguiente consulta 
 {{URL_entorno_datagov}} /get/{{eatc_cua_master. eatc-country }}/getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue ={{latitud_seleccionada_mapa}},{{longitud_seleccionada_mapa}}& showfield = eatc-city & km ={{ eatc_cua_master. eatc_geo_query_radius_km }} 
 &filterfield_1= eatc-province &filtervalue_1= {{ eatc-province_seleccionada }} 

 Si la consulta del dato {{ eatc_cua_master. eatc_geo_query_radius_km }} arroja un dato vacio, nulo, o en cero, el valor por defecto sera " 15 "  

 El sistema debe tomar el dato eatc_municipalies. eatc-city ( haciendo un distinct sobre las respuestas obtenidas ) para incorporarlo al selector. 

 Ejemplo (ambiente de pruebas) 

 Suponiendo que para la cuenta maestra abaco , un usuario cuya latitud ( eatc-lat ) es: 6.2045697, y longitud ( eatc-lon ) es: -75.60157 (previamente seleccionadas en el mapa), entonces el sistema deber como primera medida realizar la siguiente consulta: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=abaco   

 la cual determina que eatc_cua_master. eatc-country es "co" y " eatc_cua_master. eatc_geo_query_radius_km" es 15 

 Por lo tanto el sistema realiza la siguiente consulta para determinar los datos del selector de departamentos: 

 https://datagov.eatcloud.info/get/ co /getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue =6.2045697,-75.60157& showfield = eatc-province & km = 15   

 Como el sistema arroja la siguiente informacin: 
 eatc-province : "ANTIOQUIA" (93 veces) 

 El sistema debe colocar en el selector de "Provincia, departamento, estado" "ANTIOQUIA" (una sola vez, porque hace distinct sobre el dato eatc-province ) 

 Posteriormente, cuando el usuario seleccione el departamento (si es uno solo se puede realizar una seleccin automtica) con este dato se procede a generar la informacin para el selector de ciudad:  

 https://datagov.eatcloud.info/get/ co /getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue =6.2045697,-75.60157& showfield = eatc-city & km =1 5 &filterfield_1= eatc-province &filtervalue_1= ANTIOQUIA     

 Como el sistema arroja la siguiente informacin: 

 eatc-city : "MEDELLIN" (26 veces), "ENVIGADO" (23 vez), e "ITAGUI" (7 veces), LA ESTRELLA (10), EL RETIRO (3),SABANETA (9) 

 El sistema debe colocar en el selector de "Ciudad" "MEDELLIN,ENVIGADO,ITAGUI,LA ESTRELLA,EL RETIRO,SABANETA" (una sola vez cada ciudad, porque hace distinct sobre el dato eatc-city ) 

 Ejemplo argentina en pruebas (con datos de ejemplo anterior) 

 Como el sistema no arroja datos en la consulta de {{ eatc_cua_master. eatc_geo_query_radius_km }} entonces se coloca el valor por defecto de 15 KM 
 https://dev.datagov.eatcloud.info/get/ ar /getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue =-34.6156624,-58.50351& showfield = eatc-city & km = 15 &filterfield_1= eatc-province &filtervalue_1= Buenos%20Aires       

 Ejemplo: Mxico en pruebas (con datos de ejemplo anterior) 

 Como el sistema arroja en la consulta de {{ eatc_cua_master. eatc_geo_query_radius_km }} el dato " 25 " entonces se realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/get/ mx /getpuntos? table =eatc_municipalities& fieldname =eatc-lat,eatc-lon& fieldvalue =19.4410303,-99.2000994& showfield = eatc-city & km = 25 &filterfield_1= eatc-province &filtervalue_1= Ciudad%20de%20Mxico   

 ***NUEVO: CAPTURA DE NMERO DE PERSONAS POR GRUPO ETAREO QUE SE ATIENDEN *** 
 NOTA PARA EL DESARROLLO:  a partir de la seleccin de los grupos etreos que atiende cada organizacin (que viene funcionando)  

 El sistema desplegar campos de captura por cada grupo etario seleccionado ( {{eatc_age_groups. age_group_label }} ), para establecer de manera obligatoria el nmero de personas que atiende cada organizacin por grupo etreo 

 Esta informacin se guardar en una nueva persistencia eatc_number_of_people_by_age_groups ( pendiente por crear ) , que contendr la siguiente informacin ( crear esta persistencia en el entorno datagov y la cuenta eatcloud ) 

 eatc_cua_master :  cuenta maestra a la cual pertenece el gestor de donaciones 
 eatc_doma_id : identificador nico del gestor de donaciones 
 eatc_country: pas del gestor de donaciones 
 eatc_province: provincia, departamento, estado del gestor de donaciones 
 eatc_region: regin del gestor de donaciones (aun est pendiente por implementacin general, pero tenerla en cuenta 
 eatc_city: Ciudad del gestor de donaciones 
 age_group_label : label del grupo etario seleccionado 
 number_of_people : nmero de personas atendido en el grupo etario particualr  

 Nmero de personas atendidas por grupo etario 
 class= lbl_num_pers_gr_etario 

 Ingresa el nmero de personas por cada grupo etario que atiendes en tu organizacin ( class= lbl_num_pers_gr_etario_desc ) 

 Tantos campos de captura de enteros como selecciones de grupos etarios realizados 
 Label : class={{eatc_age_groups. age_group_label }} 
 Ayuda (?) :  " Por favor ingresa el nmero de {{eatc_age_groups. age_group_label }} que atiende tu organizacin " 
 Tipo de campo de captura : input de nmeros enteros 
 Tipo de dato : integer 
 Valor por defecto : ninguno 
 Validaciones : obligatoriedad 
 Se guarda en : eatc_number_of_people_by_age_groups. number_of_people => PERSISTENCIA NUEVA A CREAR   

 El llamado para la creacin de cada captura individual sera as: 
 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla= eatc_number_of_people_by_age_groups &_operacion=insert &eatc_cua_master={{_DOM. cua_master }}&eatc_doma_id={{input_ identificador_unico_registro}}& age_group_label= {{eatc_age_groups. age_group_label }}&number_of_people={{ input }}   

 ***NUEVO: CAPTURA DE FECHAS DE DOCUMENTOS LEGALES *** 
 NOTA PARA EL DESARROLLO:  Esta captura SOLO se efectuar en la cua_master=abaco (las dems cuentas maestras no tendrn por el momento este tipo de captura ).  Se habilitarn campos de captura , para varias fechas asociadas a los documentos legales (en Colombia: RUT y CDC),  

 Una vez se hallan validado las fechas como correctas, y estn todas diligenciadas, el sistema desplegar la funcionalidad para subir los documentos legales (RUT, CDC) tal como se ha desplegado hasta el momento en el formulario 

 Descripcin detallada de campos de captura de fechas de documentos legales 
 A continuacin se describe detalladamente los campos de fechas asociados a los documentos legales 

 Fecha de impresin del rut 
 Label : class= lbl_doc_legal_1_fecha_impresion 
 Ayuda (?) :  class= lbl_doc_legal_1_fecha_impresion_desc "Por favor ingresa la fecha de impresin del Registro nico Tributario" 
 Tipo de campo de captura : date picker 
 Tipo de dato : date 
 Valor por defecto : ninguno 
 Validaciones : obligatoriedad 
 Se guarda en : eatc_donation_managers . doc_legal_1_fecha_impresion => CAMPO NUEVO A CREAR   

 Fecha de registro CDC 
 Label : class= lbl_doc_legal_2_fecha_registro 
 Ayuda (?) :  class= lbl_doc_legal_2_fecha_registro_desc   "Indique la fecha de inscripcin de la organizacin en la Cmara de Comercio." 
 Tipo de campo de captura : date picker 
 Tipo de dato : date 
 Valor por defecto : ninguno 
 Validaciones : Obligatoriedad. Adems el sistema debe validar que al ingresar la fecha el lapso entre esa fecha y la actual no sea inferior a 1 ao.  Si se da esa condicin se debe desplegar el siguiente label: class= lbl_doc_legal_2_fecha_registro_no_valida "La fecha de registro en la Cmara de Comercio debe ser mayor a 1 ao" (y no debe permitir seguir con el registro) 
 Se guarda en : eatc_donation_managers . doc_legal_2_fecha_registro => CAMPO NUEVO A CREAR   

 Fecha de expedicin CDC 
 Label : class = lbl_doc_legal_2_fecha_expedicion 
 Ayuda (?) :  class = lbl_doc_legal_2_fecha_expedicion_desc     "Coloca la fecha en que fue expedido el certificado de Cmara de Comercio que adjuntas" 
 Tipo de campo de captura : date picker 
 Tipo de dato : date 
 Valor por defecto : ninguno 
 Validaciones : Obligatoriedad. Adems el sistema debe validar que al ingresar la fecha el lapso entre esa fecha y la actual no sea superior 90 das.  Si se da esa condicin se debe desplegar el siguiente label: class= lbl_doc_legal_2_fecha_expedicion_no_valida "La fecha de expedicin del certificado de CDC debe ser menor a 90 das" (y no debe permitir seguir con el registro) 
 Se guarda en : eatc_donation_managers . doc_legal_2_fecha_expedicion => CAMPO NUEVO A CREAR   

 Cuando se validan la obligatoriedad y validez de las fechas, se despliega el file picker  
 Esto aplica solamente para el formulario cuya eatc_cua_master= abaco .  Para el resto de formularios, los anteriores campos de captura no aplican y el file picker siempre estar desplegado 

 ***NUEVO : Generacin del eatc_state de acuerdo a parmetro en cuenta maestra *** 
 Para guardar el estado del beneficiario, (que antes era un dato quemado en el cdigo y siempre llevaba eatc_state=inactivo) , el sistema realizar la siguiente consulta, para determinar que estado debe colocar a la hora de crear el registro de un beneficiario 

 {{URL_datagov}} /api/eatcloud/eatc_cua_master?eatc_cua= {{cua_master}}&_cmp= eatc_doma_creation_state 

 El valor que se recibe ser el que se lleve al parmetro eatc_state de la tabla eatc_donation_managers a la hora de crear el nuevo registro de gestor de donaciones 

 eatc_donation_managers. eatc_state= eatc_cua_master. eatc_doma_creation_state {{cua_master}}   
 Realizacin del registro en la base de datos de beneficiarios 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado para la incorporacin de la informacin (Mtodo POST  
 {{URL_entorno_beneficiarios}}/crd/{{cua_master}}/?_tabla= eatc_donation_managers &_operacion=insert&{{parametros}}  

 Confirmacin de registro realizado: mejora mensaje al finalizar el registro 
 Hasta el da de hoy, al realizar un registro de beneficiario sale el siguiente mensaje: 

 Se deber configurar dicho mensaje con los siguientes labels: 

 Gracias por registrarte! 
 Label : class=" lbl_agradecimiento_rgistro " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_agradecimiento_rgistro   

 Bienvenido a EatCloud 
 Label : class=" lbl_bienvenido_a_eatcloud " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_bienvenido_a_eatcloud    

 Nuestro Equipo validar la informacin para seguir con tu inscripcin. Una vez verifiquemos que los documentos e informacin estn en orden, podrs continuar con el proceso de activacin. 
 Label : class=" lbl_bienvenido_a_eatcloud_2 " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_bienvenido_a_eatcloud_2   

 ***NUEVO: No olvides realizar tu test de conocimiento (requisito para el proceso de aprobacin) *** . 
 Label : class=" lbl_test_conocimiento " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_test_conocimiento 

 y a continuacin debe desplegarse la siguiente URL con vnculo activo: https://forms.gle/vzYXunCNwf4zDhz26   

 Botn: Entendido (debe tener el mismo funcionamiento que el botn actual) 
 Label : class=" lbl_entendido " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_entendido     

 Deprecado 
 El formulario se debe confirmar la creacin correcta del punto de donacin y desplegar el siguiente mensaje: 
 "Gestor de donaciones correctamente registrado". 
 Y desplegar el siguiente html (el que est contenido en la siguiente tarea del Asana) 
 https://app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

 Envo de correo electrnico al realizar la inscripcin 
 En la actualidad el sistema est enviando el siguiente correo: 

 Bienvenido: Organizacin 2 Castelln 

 Gracias por inscribirte a nuestra red de Gestores de Donaciones EatCloud, de la mano de organizaciones como la tuya, estamos llegando a muchas personas que requieren nuestra ayuda, entregndoles alimentos y disminuyendo as la brecha de inseguridad alimentaria. 
 En este momento empiezas el proceso de aprobacin como Gestor de Donaciones. Para poder activarte en EatCloud nuestro equipo est verificando los siguientes documentos subidos por nuestro formulario de registro 
 1. RUT 
 2. Certificado de Cmara de Comercio (Vigencia anterior a 90 das) 
 Si te inscribiste y eres persona natural, desafortunadamente no puedes continuar con el proceso, dado que los gestores de donacin slo pueden ser Personas Jurdicas legalmente constituidas, con renovacin vigente. 
 Cordialmente, 

 Equipo de Inscripciones EatCloud. 

 Se deber programar que el correo se genere con los siguientes labels, para que funcione de manera adecuada en diferentes geografas 

 Bienvenido a EatCloud 
 Label : class=" lbl_bienvenido_a_eatcloud " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_bienvenido_a_eatcloud    

 Nombre de la organizacin 
 {{eatc_donation_managers. organizacin }} 

 Agradecimiento: 
 Gracias por inscribirte a nuestra red de Gestores de Donaciones (entidades beneficiarias). De la mano de organizaciones como la tuya, estamos llegando a muchas personas que requieren nuestra ayuda, entregndoles alimentos y disminuyendo as la brecha de inseguridad alimentaria. 

 Label : class=" lbl_agradecimiento_rg_email " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_agradecimiento_rg_email   

 Proceso aprobacin: 
 En este momento empiezas el proceso de aprobacin como Gestor de Donaciones idneo de nuestra red. Para poder activarte en EatCloud nuestro equipo est verificando los documentos que subiste a nuestro formulario de registro mediante las siguientes acciones: 

 Label : class=" lbl_proceso_aprobacion " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_proceso_aprobacion  

 Documento legal 1: 
 Label : class=" lbl_doc_legal_1_desc " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_doc_legal_1_desc    

 Documento legal 2: 
 Label : class=" lbl_doc_legal_2_desc " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_doc_legal_2_desc   

 Aviso actores vlidos: 
 Si te inscribiste y eres persona natural, desafortunadamente no puedes continuar con el proceso, dado que los gestores de donacin slo pueden ser Personas Jurdicas legalmente constituidas, con renovacin vigente. 

 Label : class=" lbl_aviso_actores_validos " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_aviso_actores_validos    

 Aviso niveles de servicio en aprobacin de gestores de donaciones: 
 Se disear un mensaje para establecer niveles de servicio.  Por ese motivo se debe dejar programado el label as no se tenga el mensaje an 

 Label : class=" lbl_aviso_niveles_servicio_aprov_doma " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_aviso_niveles_servicio_aprov_doma  

 Aviso puntos de contacto: 
 Se disear un mensaje para establecer puntos de contacto.  Por ese motivo se debe dejar programado el label as no se tenga el mensaje an 

 Label : class=" lbl_aviso_puntos_contacto_aprov_doma " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_aviso_puntos_contacto_aprov_doma  

 ***NUEVO: No olvides realizar tu test de conocimiento (requisito para el proceso de aprobacin) *** . 
 Label : class=" lbl_test_conocimiento " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_test_conocimiento 

 y a continuacin debe desplegarse la siguiente URL con vnculo activo: https://forms.gle/vzYXunCNwf4zDhz26   

 Cordialmente 
 Label : class=" lbl_cordialmente " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_cordialmente   

 Equipo de activaciones EatCloud 
 Label : class=" lbl_equipo_activaciones_eatcloud " https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=ONB_beneficiarios&idlabel= lbl_equipo_activaciones_eatcloud   

 Envo de correo electrnico al aprobar el usuario (en BO) 
 Se deber enviar un correo electrnico al gestor de donaciones (al correo registrado en eatc_donation_managers ( correo_electronico ) y eatc_users ( correo_electronico )) que contenga la informacin del html contenido en la siguiente tarea del Asana 
 https://app.asana.com/0/698639369029630/1168757312797114?lg=1584380071980 

 ***NUEVO: Envo de correo electrnico al gestor del ecosistema social ante la inscripcin de una nueva organizacin *** 

 Determinacin del correo electrnico al cul se enva: 
 El sistema realiza la siguiente consulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_cua_master?eatc_cua={{_DOM. cua_master }}&_cmp= eatc_pod_creation_notification_emails 

 Con la respuesta, el sistema construye un {{ array_destinatarios }} a los cuales enviar el siguiente correo electrnico.  Si la consulta no arroja resultados el correo no se enva. 

 from : noreply@eatcloud.com 
 to : {{ array_destinatarios }}  
 Asunto : Nuevo Gestor de Donaciones Inscrito 
 Cuerpo : 
 Se ha inscrito en EatCloud la organizacin: {{eatc_donation_managers. organizacin }} con id {{eatc_donation_managers. identificador_unico_registro }}. 

 Por favor revisa el BO del lder del ecosistema social ( https://beneficiarios.eatcloud.info/_nbob/#!/start )  con el nimo de realizar el proceso de verificacin y aprobacin de la organizacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fonboarding-de-beneficiarios%2F3384108518-imagen_onb_beneficiarios_2022-03-08.jpeg&ow=1280&oh=719, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fonboarding-de-beneficiarios%2F3384108518-imagen_onb_beneficiarios_2022-03-08.jpeg&ow=1280&oh=719 

 User Administrator 
 501.000000000000 

 ONBOARDING DE BENEFICIARIOS