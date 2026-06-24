# borrado-de-mensajes.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Este servicio debe correr todos los das a ltima hora (despus de las 11:45 PM), con el nimo de analizar los mensajes cuya fecha de caducidad es anterior o igual a la fecha actual, evaluando el siguiente campo: 

 {{url_entorno_beneficiario}}/api/{{cua_master}}/eatc_doma_messages?_id=_*&_cmp= published_until 

 Si en el campo " published_until " no hay datos (vaco, nulo, cero), entonces el mensaje no pasar por el proceso, es decir, este proceso solamente operar sobre los mensajes con una fecha vlida ( AAAA-MM-DD ) en el campo " published_until ". 

 Una vez se determinan dichos mensajes (fecha " published_until ", anterior o igual a la fecha actual), el servicio deber realizar una copia de los mismos a una estructura de datos, de similares caractersticas a la estructura en la cual se guardan los mensajes 

 {{url_entorno_beneficiario}}/api/{{cua_master}}/eatc_doma_messages?_campos 

 Pero destinada para almacenar mensajes borrados ( se debe crear esta nueva estructura de datos en las diferentes cuentas maestras ): 

 {{url_entorno_beneficiario}}/api/{{cua_master}}/eatc_doma_deleted_messages?_campos 

 Una vez realizada la copia el sistema debe proceder a borrar los mensajes con fecha de caducidad igual o anterior a la actual. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 BORRADO DE MENSAJES (SERVICIO NOCTURNO ACTIVADO POR CRONJOB)