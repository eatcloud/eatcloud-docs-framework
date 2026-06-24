# crea_cert-esp.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL 
 La creacin de certificados de donacin en espaa, tendr la siguientes caractersticas que contrastan con la creacin de certificados en la cuenta maestra abaco 

 Una donacin genera un certificado 
 Los certificados no tienen soporte diferente a la donacin misma 
 Es un proceso que se realizar peridicamente consultando los anuncios de donacin con estado "recibido" 
 El anuncio pasar de estado "recibido" a "certificado" sin tener que pasar por el estado "pre-certificado" 
 En trminos generales es un proceso mucho ms simple que el implementado en Colombia, dado que no requiere la creacin de soportes, no requiere aprobacin y el documento del certificado como tal lo generar nuestro partner espaol y nos lo entregar como respuesta al la invocacin del servicio "frmCertificacion" 

 NOTA PARA EL DESARROLLO: 
 La presente documentacin se basa en la documentacin del servicio crea_cert: factura_electronica_colombia, por lo tanto es posible que partes del cdigo de dicho servicio se puedan reutilizar. 

 LLAMADO AL SERVICIO 

 Se deber programar un cronjob que peridicamente (inicialmente puede ser cada 10 minutos) realice la siguiente consulta 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_dona_headers? eatc-receipt_datetime[0]= {{fecha_dia_anterior}}& eatc-receipt_datetime[1]= {{fecha_actual}}&eatc-state= received&_cmp=eatc-code 

 Con el array de cdigos de anuncios de donacin, se procede a realizar llamados individuales al siguiente endpoint (se debe evaluar la posiblidad de hacer llamados bulk, teniendo en cuenta que por cada anuncio se deber generar un certificado de donacin ). 

 END POINT 
 El servicio ser invocado de la siguiente manera  
 {{URL_entorno_donante}}/ crea_cert /esp/ eatc_dona_certification_support= eatc_dona_header & eatc_certification_support_code={{ eatc_dona_headers. eatc-code}} 

 Al realizar el llamado, el sistema realiza las siguientes acciones 

 Actualizacin de datos de los anuncios de donacin 
 El sistema genera el cdigo del certificado de la siguiente manera: 

 eatc_code:  
 Cdigo nico generado por el sistema para identificar el certificado que se est creando. Debe contener el prefijo CERT- seguido por el cdigo del anuncio de donacin {{ eatc_dona_headers. eatc-code}} . 

 Para realizar dicha actualizacin  se realiza la siguiente llamada al CRD. 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_headers &_operacion= update &eatc_certificate_code={{ eatc_code }}&eatc-state= certified &eatc-certification_datetime={{ datetimestamp }}& WHERE eatc-code ={{ eatc_dona_headers. eatc-code}} 

 LLAMADO AL SERVICIO DE CREACIN DE CERTIFICADO BLOCKCHAIN 
 Se deber llamar ese servicio 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master=esp&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmCertificacion 

 LLAMADO AL SERVICIO DE GENREACIN DE CERTIFICADO 
 Se deber llamar ese servicio, dado que el mismo responder con una URI (URL) que servir para la construccin del certificado en la interfaz de consulta de los mismos (Datagov_cuentas) y que se llevar a la estructura de almacenamiento de certificados, para su posterior consulta: 

 Se deja a discrecin del desarrollador, generar un servicio de integracin de este estilo: 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master=esp&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= generarcertificado 

 Como se expresa en la documentacin respectiva: [ GET ] servicio: generarcertificado (generacion certificado) , o en este punto realizar el llamado directo al servicio como se expresa la documentacin respectiva: 

 /activiti-app/services/eatcloud/generarcertificado/{donationId}/{token} 

 La URI recibida, se deber almacenar en la variable eatc_certificate_file , para su posterior registro. 

 NOTA IMPORTANTE: Otro tema a validar tcnicamente es si vale la pena guardar en persistencia la respuesta del servicio o si por el contrario solamente se deja en el botn "descargar certificado" de la funcionalidad de Consulta de certificados que ms abajo se relaciona. 

 CONSULTAS NECESARIAS PARA GENERAR EL CERTIFICADO 
 Nota para el desarrollo: la siguiente especificacin se realiz con el objetivo de generar los datos mnimos necesarios para que la funcionalidad de consulta de certificados de datagov_cuentas , funcione sin inconvenientes (se entiende que la tabla de la imagen abajo adjunta se construye con los datos consignados en eatc_dona_certifications) .  Por ese motivo, despus de realizar esta implementacin, se deber revisar si dicho informe (Consulta de certificados) funciona sin inconvenientes en un datagov de una cuenta espaola, o ser necesario ajustar algo (lo que se considera que puede generar ajuste el botn de descargar el certificado, dado que para este caso en particular se deber generar a partir de la URI con la que contesta el servicio frmCertificacion) 

 El sistema deber realizar la siguiente consulta, para establecer los datos para la generacin del certificado 

 {{URL_entorno_donante}}/ api /esp/ eatc_dona_headers= eatc- code={{ eatc_dona_headers. eatc-code}}&_cmp=eatc-code, eatc-donor_code,eatc_donor_fiscal_name,eatc-total_cost,eatc_donor, eatc-donation_manager_code,eatc-donation_manager_name 

 Parmetros de creacin del certificado de donacin (en eatc_dona_certifications)  a partir de la consulta de los datos de encabezado de donacin. 
 A continuacin se presentan los parmetros con los cuales se crea el registro en la persistencia eatc_dona_certifications a partir de los datos obtenidos en la anterior consulta de parmetros del eatc_dona_headers. 
 parametros_creacion_certificado 

 eatc_code:  
 Cdigo nico generado por el sistema para identificar el certificado que se est creando. Debe contener el prefijo CERT- seguido por el cdigo del anuncio de donacin {{ eatc_dona_headers. eatc-code}} . 

 eatc_datetime:  
 (Datetimestamp) Fecha y hora de generacin del certificado en formato AAAA-MM-DD HH:MM:SS   

 eatc_dona_certification_support: 
 Tipo de soporte de certificacin expedido  (en este caso sera siempre: eatc_dona_header ) 

 eatc_donor_code: 
 El dato que se se recibe en eatc_dona_headers. eatc-donor_code   

 eatc_donor_fiscal_name: 
 El dato que se se recibe en eatc_dona_headers. eatc_donor_fiscal_name 

 eatc_value: 
 El valor que se obtiene de: eatc_dona_headers. eatc-total_cost   

 eatc_cua: 
 Cuenta desde la que se generan los soportes.  Corresponde a _DOM. cua_user y tambin al dato eatc_dona_headers. eatc_donor 

 eatc_donee_code *** 
 El valor que se obtiene de: eatc_dona_headers . eatc-donation_manager_code 

 eatc_donee_fiscal_name 
 El valor que se obtiene de: eatc_dona_headers . eatc-donation_manager_name 

 eatc_certificate_file 
 Corresponde a la URI con la cual responde el servicio blockchain frmCertificacin y que se guard en la variable: 
 eatc_certificate_file 

 Creacin del registro a partir del CRD 
 El sistema debe generar el registro utilizando el CRD correspondiente de la siguiente manera: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_certifications &_operacion= insert &{{ parametros_creacion_certificado } 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deber entregar una respuesta donde exprese que el certificado de donacin con cdigo {{ eatc_dona_certifications. eatc_code}} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un cdigo de error y reversar los registros que pudieron haberse creado de manera parcial, con el nimo que se pueda reintentar la operacin hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcrea_cert-esp%2F2178438260-2022-10-04-18.44.07.jpg&ow=1280&oh=449, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcrea_cert-esp%2F2178438260-2022-10-04-18.44.07.jpg&ow=1280&oh=449 

 960.000000000000 

 CREA_CERT: CUA_MASTER: ESP