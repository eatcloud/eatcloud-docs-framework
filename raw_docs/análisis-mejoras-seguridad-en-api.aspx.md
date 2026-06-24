# análisis-mejoras-seguridad-en-api.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En una primera etapa de la implementacin de un esquema de seguridad, se implementaron servicios para evitar que la informacin de los anuncios de donacin fuera consultada por organizaciones no habilitadas en la plataforma, y que la adjudicacin tuviera que hacerse a organizaciones habilitadas correctamente en la plataforma.  En ese primer bloque de trabajo se realizaron las siguientes implementaciones: 

 Implementacin del servicio matchquery : para consultar el match, que incorpora validacin del estado de la organizacin para poder consultar el match 
 API: Prohibicin de consulta del match de manera directa : se prohibi consultar el match en el API envindo como parmetro el identificador nico de una organizacin. 
 API: Prohibicin de consulta de anuncios a organizaciones inactivas : se prohibi consultar las donaciones a organizaciones inactivas. 
 Validacin del estado de la organizacin al ingreso de la plataforma : para no permitir el ingreso de organizaciones inactivas. 
 Validacin del estado de la organizacin en el dashboard principal : para sacar de la App a organizaciones inactivas. 
 Implementacin del servicio awardona : para adjudicarse una donacin, y que no permite la adjudicacin a organizaciones que no estn "activas" en la plataforma. 
 CRD: prohibicin de cambio de estado: para que no se pueda operar el cambio de estado para adjudicar una donacin por fuera del proceso awardona. 

 Posterior a esta implementacin se realiz un segundo bloque de mejoras, que realiz las siguientes tareas: 

 Creacin de un servicio pblico para autenticacin de usuarios de la APP : al cual se ingresa entregando por encabezado un usuario y una contrasea y que implica el manejo de contraseas hasheadas => DOCUMENTAR EL SERVICIO 
 Autenticacin desde la APP utilizando el nuevo servicio : para garantizar que siempre se haga a travs del servicio pblico => DOCUMENTAR AJUSTE 
 Ocultamiento de la estructura sobre la cual se haca la validacin de credenciales : para garantizar que posibles versiones viejas queden inservibles y se tenga que actualizar para poder ingresar a la plataforma. 

 Como tercer bloque de mejoras de seguridad se implementar lo siguiente: 
 Creacin de servicio para consulta de recolectores : con este servicio pblico (protegido por contrasea y password) se implementaron tres estructuras que pueden mejorar las prestaciones de seguridad en la APP, para restringir recolectores y restringir dispositivos. 
 Lista negra de dispositivos: en donde se podrn guardar IMEIs a los cuales se les prohbe el ingreso a la plataforma. 
 Lista negra de recolectores y placas: contra la cual se podrn validar placas y documentos de identidad de recolectores restringidos y al detectar un posible intento de registro, poder enviar el IMEI del dispositivo a la lista negra. 
 Registro de conductores autorizados : para poder tener un mejor control y conocimiento de dichos recolectores o transportadores de donaciones. 
 Creacin de servicio para la programacin de donaciones : con este servicio pblico (protegido por contrasea y password), se genera una manera ms segura de programacin de donaciones.  Con esta implementacin se implement tambin la siguiente mejora 
 Mejora en la estructura de registro de historial de estado : lo cual podr traer como consecuencia tener mayor informacin de quien programa una donacin y en casos eventuales, restringir el dispositivo. 
 Ajustes en la APP para mejorar la validacin de datos del recolector y utilizar los nuevos servicios : con el nimo de tener en la APP los mecanismos de verificacin de informacin. Con esta implementacin se realizar tambin lo siguiente: 
 Prohibicin del cambio de estado a programado : para versiones viejas de la APP no puedan servir sin estos ajustes en cuanto a la programacin. 

 A partir de los anteriores ajustes se establecen las siguientes posibles acciones para seguir afianzando la seguridad del sistema: 
 Validacin de IMEI en: 
 Ingreso de la plataforma 
 Dashboard principal 
 matchquery 
 awardona 

 Implementacin de servicios pblicos de autenticacin 
 Para la Nueva WAPP 
 Para el Nuevo BO datagov cuentas 
 Para el Nuevo BO beneficiarios cua_master 
 Para la plataforma BO datagov EatCloud 

 Generacin de API pblica de consulta de donaciones (eatc_dona_headers eatc_dona) (con ocultamiento de APIs).  Este ajuste implica cambios a travs de: 
 APP Beneficiarios 
 Nueva WAPP donantes 
 Nuevo BO Beneficiarios cua_master 
 Nuevo BO Beneficiarios bancos 
 Nuevo BO Beneficiarios Instituciones 

 => Se debe hacer anlisis para documentar los puntos exactos para realizar los cambios. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ANLISIS MEJORAS SEGURIDAD EN API