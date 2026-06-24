# creación-de-certificado-de-donación-crea_cert.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 LLAMADO AL SERVICIO 
 El servicio ser invocado de la siguiente manera  

 {{URL_entorno_donante}}/ crea_cert /{{_DOM. cua_master }}/ eatc_dona_certification_support= {{carta_colombia,factura_electronica_colombia}} & eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 MTODO DE SOPORTE: CARTA_COLOMBIA 
 Dada la informacin asociada al mtodo particular ( https://datagov.eatcloud.info/api/eatcloud/eatc_dona_certification_supports?eatc_cua_master=abaco&eatc_dona_certification_support=carta_colombia ) en sus parmetros eatc_dona_certification_supports . eatc_certification_trigger_type: "a_demanda" y eatc_dona_certification_supports . eatc_certification_trigger: "firma_carta_soporte"   disparador de la creacin de este certificado, es la firma del soporte (que se documenta aqu ). 

 MTODO DE SOPORTE: FACTURA ELECTRNICA COLOMBIA 
 Dada la informacin asociada al mtodo particular ( https://datagov.eatcloud.info/api/eatcloud/eatc_dona_certification_supports?eatc_cua_master=abaco&eatc_dona_certification_support=factura_electronica_colombia ) en sus parmetros eatc_dona_certification_supports . eatc_certification_trigger_type: "automatico" y eatc_dona_certification_supports . eatc_certification_trigger: "ltimo minuto del da registrado en eatc_dona_certification_supports . eatc_max_generation_day "   disparador de la creacin de este certificado, debe programarse para que se active automticamente en el ltimo minuto del da del mes que se obtiene en el parmetro eatc_dona_certification_supports. eatc_max_generation_day 

 Consultas necesarias para realizar el llamado: 

 El sistema deber determinar qu soportes se generaron para legalizar las donaciones recibidas el mes anterior.  Para ello realiza la siguiente consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/eatc_certification_supports_details?eatc_dona_certification_support=factura_electronica_colombia& eatc_receipt_year_month={{AAAA-MM}} 

 Siendo el parmetro eatc_receipt_year_month={{AAAA-MM}} el Mes inmediatamente anterior  

 Ejemplo: consulta para generar certificados el da 6 de mayo de 2021 en ambiente productivo ( _DOM. cua_master= abaco ) 

 https://donantes.eatcloud.info/api/abaco/eatc_certification_supports_details?eatc_dona_certification_support=factura_electronica_colombia& eatc_receipt_year_month=2021-04 

 El sistema deber realizar tantos llamados al servicio de creacin de certificados, como datos existan en el parmetro eatc_certification_supports_details . eatc_donor_code de la anterior consulta. Para cada grupo de soportes correspondientes a un mismo NIT ( eatc_certification_supports_details . eatc_donor_code )  

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/eatc_certification_supports_details?eatc_dona_certification_support=factura_electronica_colombia& eatc_receipt_year_month={{AAAA-MM}}&eatc_donor_code={{NIT_DONANTE}} 

 el sistema deber enviar los diferentes cdigos de facturas asociadas ( eatc_certification_supports_details. eatc_certification_support_code presentes en la anterior consulta), al llamado para la creacin del certificado: 

 {{URL_entorno_donante}}/ crea_cert /{{_DOM. cua_master }}/ eatc_dona_certification_support= factura_electronica_colombia & eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deber entregar una respuesta donde exprese que el certificado de donacin con cdigo {{ eatc_dona_certifications. eatc_code}} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un cdigo de error y reversar los registros que pudieron haberse creado de manera parcial, con el nimo que se pueda reintentar la operacin hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE CERTIFICADO DE DONACIN (CREA_CERT)