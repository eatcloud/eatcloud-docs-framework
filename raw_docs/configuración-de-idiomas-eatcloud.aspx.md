# configuración-de-idiomas-eatcloud.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Para dar de alta una cuenta maestra, y poder tener los fundamentos bsicos para internacionalizar la plataforma, se deber crear, en un proceso muy sencillo, el idioma como dato maestro general: 

 https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* 

 Creacin del idioma 
 Para la creacin del idioma se tendr un mecanismo muy simple y es un campo de Bsqueda / Seleccin del pas a crear, y que operar con los datos que se alojan en este maestro: 

 https://datagov.eatcloud.info/api/eatcloud/languages?_id=_* 

 El buscador debe operar con texto predictivo sobre la informacin los campos: 

 languages .native_name 
 languages .name 

 Nuevo validacin si el idioma existe en eatc_languages 
 Una vez realizada la seleccin en el selector, el sistema deber realizar la siguiente consulta 

 {{URL_entorno_datagov}}/api/eatcloud/eatc_languages?iso2={{ languages .iso2 }}&_cont 

 Si la respuesta es: count : "1" , quiere decir que el idioma ya est creado y por lo tanto no debe permitir crearlo, sacando el siguiente mensaje: 

 El idioma ya ha sido creado previamente en la plataforma 

 Y no lo deja salir adelante.   

 Si la respuesta es: count : "0" , querr decir que el idioma no existe y le permitir seguir adelante 

 Ejemplo, ambiente de pruebas, espaol (iso2=es) 

 El sistema realizar la siguiente consulta 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_languages?iso2=es&_cont   

 Como la respuesta es: count : "1" entonces el sistema no le permite realizar la creacin mostrndole el siguiente mensaje 

 El idioma ya ha sido creado previamente en la plataforma 

 Cuando el usuario seleccione uno de los nombres de idiomas en la lista (y el mismo no haya sido previamente creado), el sistema deber realizar el siguiente registro: 

 {{parametros_registro_idioma}} 
 iso2 = languages .iso2 
 iso3 = languages .iso3 
 name = languages .name 
 native_name = languages .native_name 

 POR EL MOMENTO NO VA: creation_datetime =timestamp de fecha y hora de creacin. 

 Llamado CRD para creacin del idioma 
 https://datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_languages&_operacion=insert& {{parametros_registro_idioma}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONFIGURACIN DE IDIOMAS EATCLOUD