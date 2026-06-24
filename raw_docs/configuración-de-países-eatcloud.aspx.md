# configuración-de-países-eatcloud.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Para dar de alta una cuenta maestra, y poder poner a funcionar un nuevo pas dentro de la infraestructura EatCloud, es necesario realizar una configuracin de pas, que como primera medida registra el pas en la estructura: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_countries?_id=_* 

 https://datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_*   https://dev.datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_*    

 y posteriormente configura los maestros geogrficos necesarios para la configuracin de puntos de donacin, gestores de donacin y otras configuraciones que se requieren para el funcionamiento de la plataforma.  Con respecto a este  segundo aspecto, la implementacin debe ser similar a la que se utiliza para la carga de maestros estandarizados en la App Movilizza, en donde, a partir de un cargador de un archivo plano (csv) y la determinacin de los campos estndar, que para el caso particular de la estructura eatc_municipalities, que es dnde se guardar la divisin poltica del nuevo pas, se realiza un mapeo de datos, y luego se carga la informacin a una base de datos por pas que se alojar en datagov  

 {{URL_entorno_datagov}}/api/{{eatc_countries.iso2}}/eatc_municipalities?_id=_* 

 https://datagov.eatcloud.info/api/{{eatc_countries.iso2}}/eatc_municipalities?_id=_*https://dev.datagov.eatcloud.info/api/{{eatc_countries.iso2}}/eatc_municipalities?_id=_* 

 Creacin del pas 
 Para la creacin del pas se tendr un mecanismo muy simple y es un campo de Bsqueda / Seleccin del pas a crear, y que operar con los datos que se alojan en este maestro: 

 {{URL_entorno_datagov}}/api/eatcloud/countries?_id=_* 

 https://datagov.eatcloud.info/api/eatcloud/countries?_id=_* https://dev.datagov.eatcloud.info/api/eatcloud/countries?_id=_*   

 El buscador debe operar con texto predictivo sobre la informacin del campo: 
 countries .nombre 

 ****Nuevo validacin si el pas existe en eatc_countries **** 
 Una vez realizada la seleccin en el selector, el sistema deber realizar la siguiente consulta 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_countries?iso2={{ countries .iso2 }}&_cont 

 Si la respuesta es: count : "1" , quiere decir que el pas ya est creado y por lo tanto no debe permitir crearlo, sacando el siguiente mensaje: 

 El pas ya ha sido creado previamente en la plataforma 

 Y no lo deja salir adelante.   

 Si la respuesta es: count : "0" , querr decir que el pas no existe y le permitir seguir adelante 

 Ejemplo, ambiente de pruebas, Colombia (iso2=co) 

 El sistema realizar la siguiente consulta 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2=co&_cont   

 Como la respuesta es: count : "1" entonces el sistema no le permite realizar la creacin mostrndole el siguiente mensaje 
 El pas ya ha sido creado previamente en la plataforma 

 Cuando el usuario seleccione uno de los nombres de pases en la lista el sistema deber realizar el siguiente registro: 

 {{parametros_registro_pas}} 

 nombre = countries .nombre 
 name = countries .name 
 nom = countries .nom 
 iso2 = countries .iso2 
 iso3 = countries .iso3 
 phone_code = countries .phone_code 
 fecha_creacion =timestamp de fecha de creacin. 

 Llamado CRD para creacin del pas 
 {{URL_entorno_datagov}}/crd/eatcloud/?_tabla=eatc_countries&_operacion=insert& {{parametros_registro_pas}} 

 https://datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_countries&_operacion=insert& {{parametros_registro_pas}} 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_countries&_operacion=insert& {{parametros_registro_pas}}  

 Carga de datos geogrficos 
 Una vez creado el registro del pas, el sistema debe presentar un cargador de archivo indicando que el usuario debe cargar la divisin poltica (municipalidades) georeferenciada  (en coordenadas decimales con separador de decimales "punto") del pas acabado de crear en un archivo csv separado por punto y coma, cuya primera lnea corresponda a la declaracin de campos. 

 Lectura del vector de encabezado 
 El sistema debe leer el "vector de encabezados"  para realizar el mapeo a los siguientes campos estndar: 

 {{URL_entorno_datagov}}/api/co/eatc_municipalities?_campos 

 https://datagov.eatcloud.info/api/co/eatc_municipalities?_campos   
 https://dev.datagov.eatcloud.info/api/co/eatc_municipalities?_campos   

 ANTERIORMENTE: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&metodo=eatc_municipalities 

 Desplegando su descripcion e indicando cuales de estos campos son obligatorios: 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_municipalities 

 https://datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_municipalities   
 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_municipalities   

 ANTERIORMENTE: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&metodo=eatc_municipalities& obligatorio=si   

 Validacin de mapeo para campos obligatorios 
 El sistema debe validar que todos los campos " obligatorios " sean mapeados (al eatc_parameter respectivo para su creacin en el respectivo maestro: los eatc_parameter sern el nombre estndar que se utilicen en el maestro eatc_municipalities del pas respectivo en la plataforma datagov ), antes de cargar la informacin. 

 Validacin de separador "punto" en coordenadas decimales 
 Adicional a esta validacin el sistema debe validar que los datos que vienen en los datos que se mapeen hacia " eatc-lat " y " eatc-lon " tengan como separador de decimales el "punto ( . )".  En caso de tener "coma" como separador, el sistema de manera ideal, al cargar los datos los debe reemplazar 

 Carga de datos a base de datos del pas 
 Cuando las validaciones de mapeo de datos obligatorios y separador "punto" en coordenadas decimales estn realizadas, el sistema debe tomar los datos del archivo y subirlos a la base de datos del pas respectivo.  Para ejemplarizar como sera el proceso, debe ser uno homlogo al que se realizara con el siguiente llamado: 

 {{URL_entorno_datagov}}/ mstr /{{eatc_countries. iso2 }}/eatc_municipalities (se ha reemplazado " mstr " por una clave secreta por temas de seguridad) 

 https://datagov.eatcloud.info/ mstr /{{eatc_countries. iso2 }}/eatc_municipalities   
 https://dev.datagov.eatcloud.info/ mstr /{{eatc_countries. iso2 }}/eatc_municipalities   

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONFIGURACIN DE PASES EATCLOUD