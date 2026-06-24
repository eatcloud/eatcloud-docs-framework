# d-generación-de-certificado-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 [DEPRECADO] Nota importante para el desarrollo 
 Esta funcionalidad deber estar disponible en dos entornos aplicativos: BO Donantes y BO baco.  Dado que en un cercano futuro se pretende migrar el BO a Datagov Cuentas, entonces el desarrollador debe plantearse cmo ser la mejor manera para abordar el desarrollo sin generar muchos reprocesos (una opcin puede ser en primera instancia hacer una implementacin sobre datagov cuentas y luego a partir de la misma la implementacin en el BO de Abaco).  Aunque se documenta la funcionalidad como parte del BO de Donantes, se deja igualmente documentados los accesos en el men lateral de Datagov Cuentas, para realizar la incorporacin a dicha plataforma. 

 Generalidades de la funcionalidad 

 El presente proceso tendr dos etapas: 

 Preparacin del certificado: 
 Implica, configurar un mtodo de soporte especfico, que servir para cada cuenta usuario (cliente) en un territorio particular (cua_master), y que tendr una dinmica propia, establecida en una persistencia ( https://datagov.eatcloud.info/api/eatcloud/eatc_dona_certification_supports?eatc_cua_master=_* ) de la siguiente manera: 

 Mtodo de generacin (eatc_support_generation_method) : podr ser "automatico", o subido por el usuario "upload". 
 Frecuencia de generacin (eatc_support_generation_frecuency) : establece cada cuanto se genera el soporte por ejemplo "mensual" o "a_demanda", 
 Da mximo de generacin del soporte (eatc_max_generation_day) : Establece el da hasta en el cual se genera el soporte automtico (por ejemplo: "last" para indicar que es el ltimo da del mes) o el da hasta el cul se puede subir un soporte tipo "upload" (por ejemplo "6" para indicar que se pueden subir soportes de un mes anterior hasta el "sexto da" del mes posterior. 
 Extensin vlida del archivo a subir (eatc_file_extension_to_upload) : Para los soportes tipo "upload" establece las extensiones de archivos vlidas a subir, por ejemplo "zip". 
 Extensin vlida del archivo a validar (eatc_file_extension_to_validate : Para los soportes tipo "upload" establece las extensiones de archivos que se utilizarn para hacer validaciones, como por ejemplo "xml" (para el caso de la factura electrnica colombia) 
 Meses atrs que soporta (eatc_months_back_to_support) : Establece los meses atrs que soporta el documento, como por ejemplo "1". 
 Corte mensual (eatc_montly_cut) : establece hasta que fecha puede soportar, por ejemplo "corte" para indicar que empieza en el corte del mes. 
 Mtodo por (default) : Indica con un "si", si es el mtodo por defecto a seleccionar para la cuenta usuario. 
 Etiqueta de aceptacin del mtodo de soporte (eatc_support_generation_method_accept_label) : Es un texto (label) que se configura en el sistema para indicarle al usuario las implicaciones de aceptar el mtodo particular, por ejemplo para el mtodo "carta_colombia" se estableci este label  " lbl_aceptacion_metodo_carta_colombia ". 
 Tipo de disparador del proceso de certificacin (eatc_certification_trigger_type) : establece cmo se genera la accin que da como resultado la generacin del "Precertificado", por ejemplo, la generacin del precertificado del mtodo "carta_colombia" es "a_demanda", por lo que se explica a continuacin. 
 Disparador del proceso de certificacin (eatc_certification_trigger) : indica el proceso que dispara el flujo de aprobacin del certificado a partir de la generacin de un precertificado, por ejemplo, para el mtodo "carta_colombia" ser la "firma_carta_soporte". 
 Query para establecer si es un mtodo vlido para la cuenta OPCIONAL (eatc_valid_method_if_query) : Establece un query de validacin para establecer si la cuenta con los datos mnimos para hacer la validacin del soporte establecida. Por ejemplo se estableci que para el mtodo factura_electronica_colombia, la cuenta deber tener configurado un maestro de artculos, y para validar eso se establece este query " {{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&eatc_odds_app=eatc_odds&_cont ". 
 Respuesta vlida del query (eatc_valid_method_if_response) : Establece cmo debe responder el anterior query para establecer que el mtodo de soporte es vlido para la cuenta en particular.  Para el ejemplo anterior la respuesta vlida es: " count=1 ". 
 Etiqueta de respuesta ante un mtodo de soporte no vlido para la cuenta (eatc_invalid_method_resp) : Establece un mensaje que se desplegar por interfaz para informarle al usuario que el mtodo de soporte seleccionado no es vlido, siguiendo con el ejemplo anterior este label ser " lbl_para_fe_col_eatc_odds " 

 Inicialmente se establecieron para la cuenta maestra "abaco", dos mtodos de soporte: 
 Carta => la genera automticamente el sistema 
 Factura => la sube el usuario 

 Cada cuenta usuario ( cua_user ) guarda en sus datos, un parmetro que identifica el soporte por defecto, pero este se podr cambiar en cualquier momento. 

 Este proceso operar slo sobre anuncios que cumplan con estas condiciones: 
  Anuncios cuyo estado sea "received"( eatc_dona_headers. eatc-state= received )  
 Anuncios que no tengan una constancia expedida (es decir, que no tengan una fecha vlida registrada en el campo eatc_dona_headers. eatc_constancy_datetime ) 
 Anuncios del mes en curso ( eatc_dona_headers. eatc-publication_date igual al mes en curso, o si el da del mes est entre los cinco primeros das del mismo ( eatc_dona_headers. eatc-publication_date de AAAA-MM-01 a AAAA-MM-05), pueden seleccionarse anuncios del mes anterior). 

 El usuario podr seleccionar los anuncios sobre los cuales se generan los certificados (siempre y cuando cumplan las anteriores condiciones) 

 Cuando se elija el modo de soporte "Carta", el sistema la generar automticamente a partir de los datos de los anuncios, y esta carta se anexar como dato soporte de manera automtica para generar el precertificado. 

 Cuando se escoja el modo factura, se deber subir el .zip de la factura electrnica, que contiene el XML.  A partir de los datos del XML se debern realizar validaciones para que los items y las cantidades correspondan a la factura y que tambin que dicha factura cumpla con requisitos necesarios (como por ejemplo que est realizada a nombre de Abaco con sus datos correctos y con las fechas correctas). 

 Una vez se prepare el certificado, se generar, segn las dinmicas que se establezcan para la generacin de los soportes, un pre-certificado, este pasar por un flujo de aprobacin, en el cual diversos actores darn un visto bueno, para la generacin del certificado a partir del precertificado. 

 En las siguientes pginas se documentarn los pasos del proceso a saber: 

 Preparacin certificado de donacin 

 PENDIENTE: Consulta de anuncios certificados no certificables 

 Consulta de certificados de donacin 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Donantes 

 GENERACIN DE CERTIFICADO DE DONACIN