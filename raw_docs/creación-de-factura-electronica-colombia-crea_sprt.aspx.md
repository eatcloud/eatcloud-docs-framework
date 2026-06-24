# creación-de-factura-electronica-colombia-crea_sprt.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 DEPRECADO: 
 El soporte no se crear mediante llamado a un servicio, sino mediante el llamado directo al CRD desde las funciones de validacin de la factura electrnica.  Se deja la siguiente documentacin por si en el futuro se requiere la creacin de un servicio para esta labor. 

 Llamado al servicio 
 El servicio ser invocado de la siguiente manera  
 {{URL_entorno_donante}}/ crea_sprt /{{_DOM. cua_master }}/ eatc_dona_certification_support= factura_electronica_colombia& eatc_certification_support_code= {{eatc_certification_support_code}}& eatc_support_file ={{localizador_recurso / url_descarga_fe}}& eatc_dona_headers ={{array_codigos_eatc_dona_headers}}& ... 

 ... Si el desarrollador decide mandar los parmetros para la creacin de los registros definitivos eatc_certification_supports_headers y eatc_certification_products_details se deber documentar su inclusin en el llamado al servicio respectivo 

 Mtodo de soporte: factura_electronica_colombia: 
  Cuando en la invocacin del servicio en el parmetro eatc_dona_certification_support se recibe el dato factura_electronica_colombia ) el sistema debe proceder con la creacin de la siguiente manera. 

 Consultas necesarias para registrar la factura_electronica_colombia 
 (***Pendiente definicin desarrollador***) Consulta de datos provisionales de encabezado de soporte 
 El desarrollador tambin deber evaluar si es ms conveniente crear esta tabla en la cuenta maestra (decisin que se deber informar para ajustar la documentacin de creacin de cuenta maestra ), caso en el cual la consulta sera as 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_provisional_certification_supports_headers ?eatc_certification_support_code={{eatc_certification_support_code}} 
 O si es ms conveniente crear esta tabla en la cuenta usuario (decisin que se deber informar para ajustar la documentacin y los procesos  de creacin de cuenta usuario ), caso en el cual el llamado sera: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_user }}/ eatc_provisional_certification_supports_headers ?eatc_certification_support_code={{eatc_certification_support_code}} 
 Con la anterior consulta (o con los parmetros que se pasan en el llamado al servicio segn decisin del desarrollador), se proceden a realizar los registros en eatc_certification_supports_headers , cmo se detalla ms adelante. 

 (***Pendiente definicin desarrollador***) Consulta de datos provisionales de detalle de productos 
 El desarrollador tambin deber evaluar si es ms conveniente crear esta tabla en la cuenta maestra (decisin que se deber informar para ajustar la documentacin de creacin de cuenta maestra ), caso en el cual la consulta sera as 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_provisional_certification_products_details ?eatc_certification_support_code={{eatc_certification_support_code}} 
 O si es ms conveniente crear esta tabla en la cuenta usuario (decisin que se deber informar para ajustar la documentacin y los procesos  de creacin de cuenta usuario ), caso en el cual el llamado sera: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_user }}/ eatc_provisional_certification_products_details ?eatc_certification_support_code={{eatc_certification_support_code}} 
 Con la anterior consulta (o con los parmetros que se pasan en el llamado al servicio segn decisin del desarrollador), se proceden a realizar los registros en eatc_certification_products_details , cmo se detalla ms adelante. 

 Mtodo de soporte: factura_electronica_colombia: registro de datos a partir de la factura subida 
 El sistema segn lo establecido en los parmetros del mtodo de soporte: eatc_support_generation_method (automatico); eatc_support_generation_frecuency (mensual); eatc_max_generation_day (last), generar de manera automtica una o varias cartas de soporte (una por NIT: eatc_dona_headers. eatc-donor_code ) el ltimo da del mes (a ltima hora), y guardar dichas cartas en la persistencia eatc_certification_supports_headers y la relacin entre los soportes y los anuncios (aquellos que cumplen con los criterios para ser certificados ) en eatc_certification_supports_details de la siguiente manera: 

 parametros_creacin_encabezado_soporte 

 eatc_certification_support_code: 
 Corresponde al nmero de la factura electrnica, que llegar en el parmetro de encabezado (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_certification_support_code={{ }} 

 eatc_datetime: 
 Fecha y hora de generacin del soporte en formato AAAA-MM-DD HH:MM:SS (timestamp de cuando se llama el servicio). 

 eatc_date: 
 Fecha de generacin del soporte en formato AAAA-MM-DD (corresponde a la fecha en la cual se llama el servicio). 

 eatc_month: 
 Mes del soporte ( enero,febrero,,diciembre ). Corresponde al mes registrado en el dato eatc_dona_headers .eatc-receipt_datetime de los eatc_dona_headers ={{array_codigos_eatc_dona_headers}} contenidos en el llamado al servicio 

 eatc_year: 
 Ao del soporte (en formato AAAA ). Corresponde al ao registrado en el dato eatc_dona_headers .eatc-receipt_datetime de los eatc_dona_headers ={{array_codigos_eatc_dona_headers}} contenidos en el llamado al servicio 

 eatc_dona_certification_support: 
 Tipo de soporte de certificacin expedido  (en este caso sera siempre: factura_electronica_colombia ) 

 eatc_donor_code: 
 Corresponde al NIT de quien expide la factura, que llegar en el parmetro de encabezado (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_donor_code={{ }} 

 eatc_donor_fiscal_name: 
 Corresponde a la razn social, que llegar en el parmetro de encabezado (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_donor_fiscal_name={{ }} 

 eatc_value: 
 Corresponde a la sumatoria de los valores que llegarn en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_value={{ }} 

 eatc_cua: 
 Corresponde a la cuenta desde la cual se crea el soporte, que llegar en el parmetro de encabezado (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_cua={{_DOM.cua_user}} 

 eatc_support_file 
 Corresponde al dato " url_descarga_fe (segn lo estipulado en la documentacin respectiva ) " 

 El XML subido ( eatc_support_file ={{localizador_recurso}} ) se relaciona para poder ser recuperado desde las diferentes plataformas. 

 NOTA IMPORTANTE: se debe evaluar si se permite subir el ZIP de la factura electrnica, que contiene el XML y tambin el PDF, este ltimo importante para procesos de revisin humana de la informacin. Por lo tanto el localizador podra estar asociado a una carpeta que se cree en el servidor (idelamente con un hash o algo que dificulte su ubicacin por quienes no tienen acceso a la plataforma) y que all se contengan los recursos subidos: XML y PDF. 

 Creacin registro de encabezado del soporte  
 El sistema debe generar el registro utilizando el CRD correspondiente 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_supports_headers &_operacion= insert & {{parametros_creacin_encabezado_soporte}} 

 parametros_creacin_detalle_soporte 
 Con un registro para cada anuncio que es soportado por la factura_electronica_colombia , se consigna la siguiente informacin en la tabla respectiva, a partir de los datos recibidos en eatc_dona_headers ={{array_codigos_eatc_dona_headers}} 

 eatc_dona_header_code: 
 Cdigo del anuncio de donacin soportado ( eatc_dona_headers. eatc-code ).  Si en eatc_dona_headers ={{array_codigos_eatc_dona_headers}} llegan varios cdigos, entonces se crea un registro por cdigo con los siguientes datos: 

 eatc_publication_datetime: 
 Fecha y hora de publicacin del anuncio ( eatc_dona_headers. eatc-publication_datetime )", 

 eatc_value: 
 Valor del anuncio certificable antes de IVA (se toma de: eatc_dona_headers. eatc-total_cost ). 

 eatc_receipt_datetime: 
 Fecha de recepcin del anuncio ( eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM-DD HH:MM:SS 

 eatc_receipt_year_month: 
 Ao y mes de recepcin del anuncio (tomado de eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM 

 eatc_doc: 
 Documento soporte de la donacin ( eatc_dona_headers. eatc-doc ). 

 eatc_donation_manager: 
 Gestor de donaciones al que se le entreg la donacin ( eatc_dona_headers .eatc-donation_manager_code ). 

 eatc_doma_affiliated_organization: 
 Nombre de la organizacin a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el cdigo del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }} 

 Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca ese dato en el registro.  Si viene un NIT, se repite la consulta anteriormente realizada: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{ organizacion_vinculada }} 

 Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dgito de Verificacin.  Si despus de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 eatc_doma_affiliated_organization_id: 
 Identificador nico de la organizacin a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el cdigo del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers .eatc-donation_manager_code }} 

 Se toma el dato " organizacion_vinculada ".  Si en dicho dato viene el " abaco ", se coloca el dato que llega en el campo identificador_unico_registro de la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?identificador= abaco 

 Y se lleva al registro el dato consignado en " organizacin " (NOTA IMPORTANTE: si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dgito de Verificacin.  Si despus de esta segunda consulta no se traen datos, se debe llevar al registro " abaco ") 

 eatc_certification_support_code: 
 Cdigo del soporte para la certificacin que se toma del cdigo respectivo que se genera con el llamado al servicio: 
 eatc_certification_support_code={{ eatc_certification_support_code }} 

 Que tambin corresponde al dato guardado en el proceso anterior en: 
   eatc_certification_supports_headers. eatc_certification_support_code ) 

 eatc_dona_certification_support: 
 Tipo de soporte de certificacin expedido (en este caso siempre ser factura_electronica_colombia ). 

 eatc_donor_code: 
 Documento de identidad del donante ( eatc_certification_supports_headers . eatc_donor_code ). 

 eatc_donor_fiscal_name: 
 Razn social del donante ( eatc_certification_supports_headers . eatc_donor_fiscal_name ). 

 Creacin registro de detalle del soporte 
 El sistema debe generar el registro utilizando el CRD correspondiente 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_supports_details &_operacion= insert & {{parametros_creacin_detalle_soporte}} 

 parametros_creacion_detalle_productos 
 eatc_certification_support_code 
 Cdigo del soporte para la certificacin que se toma del cdigo respectivo que se genera con el llamado al servicio: 
 eatc_certification_support_code={{ eatc_certification_support_code }} 
 Que tambin corresponde al dato guardado en el proceso anterior en: 
   eatc_certification_supports_headers. eatc_certification_support_code 

 eatc_product_code 
 Corresponde al cdigo del producto que llega en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_product_code={{ }} 
 O al valor que llega el parmetro de detalle (si el desarrollador determin utilizar una persistencia provisional) 
 eatc_certification_products_details. eatc_product_code 

 eatc_product_name 
 Corresponde al cdigo del producto que llega en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_product_name={{ }} 
 O al valor que llega el parmetro de detalle (si el desarrollador determin utilizar una persistencia provisional) 
 eatc_certification_products_details. eatc_product_name 

 eatc_product_quantity 
 Corresponde al cdigo del producto que llega en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_product_quantity={{ }} 
 O al valor que llega el parmetro de detalle (si el desarrollador determin utilizar una persistencia provisional) 
 eatc_certification_products_details. eatc_product_quantity 

 eatc_unt_value 
 Corresponde al cdigo del producto que llega en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_unt_value={{ }} 

 O al valor que llega el parmetro de detalle (si el desarrollador determin utilizar una persistencia provisional) 
 eatc_certification_products_details. eatc_unt_value 

 eatc_total_value 
 Corresponde al cdigo del producto que llega en el parmetro de detalle (si el desarrollador determin entregarlo en el llamado al servicio): 
 eatc_total_value={{ }} 

 O al valor que llega el parmetro de detalle (si el desarrollador determin utilizar una persistencia provisional) 
 eatc_certification_products_details. eatc_total_value 

 Creacin registro de detalle del soporte 
 El sistema debe generar el registro utilizando el CRD correspondiente 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_products_details &_operacion= insert & {{parametros_creacin_detalle_productos}} 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deber entregar una respuesta donde exprese que el certificado de donacin con cdigo {{ eatc_certification_supports_headers. eatc_certification_support_code }} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un cdigo de error y reversar los registros que pudieron haberse creado de manera parcial, con el nimo que se pueda reintentar la operacin hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREACIN DE SOPORTE FACTURA ELECTRNICA CPLOMBIA (CREA_SPRT)