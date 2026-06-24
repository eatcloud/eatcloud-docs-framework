# crea_cert-factura_electronica_colombia.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 LLAMADO AL SERVICIO 

 El servicio ser invocado de la siguiente manera  
 {{URL_entorno_donante}}/ crea_cert /{{_DOM. cua_master }}/ eatc_dona_certification_support= factura_electronica_colombia & eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 CONSULTAS NECESARIAS PARA GENERAR EL CERTIFICADO 
 Con los datos que llegan en el parmetro eatc_certification_support_code , el sistema procede a realizar las siguientes consultas: 

 Consulta del encabezado del soporte 
 Para este mtodo de soporte en particular, solo debe llegar un valor en el parmetro eatc_certification_support_code . Con ese valor se realiza la siguiente consulta 

 {{URL_entorno_donante}}/ api /{{_DOM. cua_master }}/ eatc_certification_supports_headers? eatc_certification_support_code ={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }}{{ eatc_certification_support_code }} 

 Consulta de los detalles del soporte 
 Para este mtodo de soporte en particular, solo debe llegar un valor en el parmetro eatc_certification_support_code . Con ese valor se realiza la siguiente consulta 
 {{URL_entorno_donante}}/ api /{{_DOM. cua_master }}/ eatc_certification_supports_details? eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 ***Nuevo: Enriquecimiento de datos de eatc_certification_supports_details *** 
 Para cada registro de detalle de soporte de certificado, se debern incorporar los siguientes datos: 

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

 *** 
 Consulta de los detalles de producto 
 Para este mtodo de soporte en particular, solo debe llegar un valor en el parmetro eatc_certification_products_details . Con ese valor se realiza la siguiente consulta 

 {{URL_entorno_donante}}/ api /{{_DOM. cua_master }}/ eatc_certification_products_details? eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 Con los datos que traen las anteriores consultas se realizan los siguientes registros en la estructura de persistencia del certificado eatc_dona_certifications y se crea el certificado como tal (documento fsico descargable). 

 Parmetros de creacin del certificado de donacin (en eatc_dona_certifications)  a partir del soporte factura_electronica_colombia 
 A continuacin se presentan los parmetros con los cuales se crea el registro en la persistencia eatc_dona_certifications a partir de los datos obtenidos en la consulta del encabezado del soporte . 

 parametros_creacion_certificado 

 eatc_code:  
 Cdigo nico generado por el sistema para identificar el certificado que se est creando. Debe contener el prefijo EC- seguido por un consecutivo de seis cifras generado por el sistema y por ltimo el sufijo -{{ao en formato AAAA}} (dicho ao se toma del dato eatc_certification_supports_headers . eatc_year de las facturas a partir de las cuales se genera el certificado).  El sistema debe validar la unicidad de este cdigo en el registro (puede utilizarse como clave primaria). 

 eatc_datetime:  
 Fecha y hora de generacin del certificado en formato AAAA-MM-DD HH:MM:SS (que debe corresponder aproximadamente a la fecha y de llamado automtico al servicio : eatc_dona_certification_supports . eatc_max_generation_day " disparador de la creacin de este certificado, debe programarse para que se active automticamente en el ltimo minuto del da del mes que se obtiene en el parmetro ). 

 eatc_date:  
 Fecha de generacin del certificado en formato AAAA-MM-DD . (dicho ao se toma del dato eatc_certification_supports_headers . eatc_date ). 

 eatc_month:  
 mes de generacin del soporte ( enero,febrero,,diciembre ). (dicho ao se toma del dato eatc_certification_supports_headers . eatc_month ) 

 eatc_year:  
 Ao de generacin del soporte (en formato AAAA ). (dicho ao se toma del dato eatc_certification_supports_headers . eatc_year ) 

 eatc_dona_certification_support: 
 Tipo de soporte de certificacin expedido  (en este caso sera siempre: factura_electronica_colombia ) 

 eatc_donor_code:  
 El dato que se toma eatc_certification_supports_headers . eatc_donor_code . (Debe ser nico por certificado) 

 eatc_donor_fiscal_name:  
 El dato que se toma eatc_certification_supports_headers . eatc_donor_fiscal_name . (Debe ser nico por certificado) 

 eatc_value:  
 Sumatoria de los datos: eatc_certification_supports_headers . eatc_value . 

 eatc_cua:  
 Cuenta desde la que se generan los soportes.  se toma de eatc_certification_supports_headers. eatc_cua . (Debe ser nico por certificado) 

 Creacin del registro a partir del CRD 
 El sistema debe generar el registro utilizando el CRD correspondiente de la siguiente manera: 
 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_certifications &_operacion= insert &{{ parametros_creacion_certificado }} 

 Parmetros de creacin de la relacin "certificado - soportes" 
 Una vez creado el certificado, se debe guardar en la persistencia " eatc_certifications_supports " su relacin con el soporte correspondiente (en el caso del soporte " factura_electronica_colombia " es una relacin uno a muchos: un certificado puede contener varias facturas), de la siguiente manera 
 parametros_certificado_soporte 

 eatc_certification_code:  
 Corresponde al cdigo del certificado de donacin que se acaba de crear eatc_dona_certifications. eatc_code 

 eatc_certification_support_code:  
 Corresponde al cdigo o los cdigos  de los soportes con el cual se invoc el servicio:  
 eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 La combinacin de ambos parmetros debe ser nica, por lo tanto debe programarse una clave compuesta con los mismos en la respectiva persistencia 

 Creacin del registro a partir del CRD 
 El sistema debe generar el registro utilizando el CRD correspondiente de la siguiente manera 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certifications_supports &_operacion= insert &{{ parametros_certificado_soporte }} 

 Actualizacin de datos del encabezado del soporte 
 Con el cdigo del certificado recin creado, se actualiza la informacin del encabezado de soporte de la siguiente manera 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_supports_headers &_operacion= update &eatc_certification_code={{ eatc_dona_certifications. eatc_code }}& WHERE eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 Actualizacin de datos de los detalles de producto 
 Con el cdigo del certificado recin creado, se actualiza la informacin de los detalles de producto a certificar de la siguiente manera 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_certification_products_details &_operacion= update &eatc_certification_code={{ eatc_dona_certifications. eatc_code }}& WHERE eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 Actualizacin de datos de los anuncios de donacin 
 Con el cdigo del certificado recin creado, se actualiza la informacin los encabezados de anuncios de donacin de la siguiente  de la siguiente manera: 

 Como primera medida, se traen los cdigos de los anuncios de donacin ( eatc_certification_supports_details . eatc_dona_header_code ) cuyos soportes han sido cobijados por el certificado que se cre recientemente con la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_details? 
 eatc_certification_support_code={{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},{{ eatc_certification_support_code }},...,{{ eatc_certification_support_code }} 

 Con el array de datos ( array_eatc_dona_header_code ) obtenidos del parmetro eatc_certification_supports_details . eatc_dona_header_code que se obtienen de la anterior consulta, se debe proceder a actualizar la informacin de los respectivos anuncios de donacin, marcndolos con el estado de " pre-certified ", guardando el cdigo del certificado ( eatc_certificate_code ) y estampando la fecha y hora de precertificacin ( eatc-pre_certification_datetime ).  Para realizar dicha actualizacin  se realiza la siguiente llamada al CRD. 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_headers &_operacion= update &eatc_certificate_code={{ eatc_dona_certifications. eatc_code }}&eatc-state= pre-certified &eatc-pre_certification_datetime={{ eatc_dona_certifications. eatc_datetime }}& WHERE eatc-code = {{ array_eatc_dona_header_code }} 

 ***NUEVO: LLAMADO AL SERVICIO DE INTEGRACIN BLOCKCHAIN *** 
 Endpoint (segn documentacin ([POST] servicio: frmPreCertificado (Traza) ): sujeto a revisin) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmPreCertificado 

 Parmetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Cdigo del anuncio de donacin recientemente creado: eatc_dona_heaaders. eatc-code => parmetro de carcter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parmetro de carcter obligatorio 

 Creacin del certificado 
 El sistema, con los datos consignados en eatc_dona_certifications y obtenidos de  eatc_certification_supports_details y eatc_certification_products_details (principal diferencia con el certificado a partir de carta, ya que este certificado debe contener un listado de los productos certificados y que fueron cobijados por los respectivos soportes) debe generar un certificado (en formato descargable preferiblemente PDF) que se construye de la siguiente manera (el formato que se propone debe poderse editar con posterioridad) 

 [Documento con marca de agua] " Pre-certificado no vlido para efectos tributarios ".  
 [Encabezado: Logo de baco Centrado ] 

 CERTIFICADO DE DONACIN No. {{ eatc_dona_certifications. eatc_code }} 

 EL SUSCRITO REVISOR FISCAL  

 CERTIFICA QUE: 

 La entidad ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA - ABACO con NIT 900.326.456-1 es una persona jurdica de derecho privado sin nimo de lucro, constituida por acta de asociados el da 26 de octubre de 2009, inscrita en la cmara de comercio el da 1 de diciembre de 2009 bajo el No. 00164449 del libro I de las entidades Sin nimo de Lucro y registro de inscripcin No. S0035850 del 1 de diciembre de 2009. 

 Que la ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIA-ABACO tiene como objetivo representar a sus Asociados y generar alianzas estratgicas con el sector pblico y privado a fin de mejorar la distribucin de alimentos, bienes y servicios en bsqueda de auxiliar la poblacin vulnerable, a travs de las instituciones vinculadas a los Asociados. 

 Que estas actividades no generan excedentes, dividendos, utilidades , ni beneficio econmico a sus asociados, o fundadores; la Asociacin revierte sus excedentes en el mismo objeto social y su fondo patrimonial en caso de liquidacin pasar a otra entidad que cumpla fines similares. 

 Que la ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIAABACO est sometida a la vigilancia de la Alcalda Mayor de Bogot D.C. 

 Que de acuerdo con lo estipulado en el artculo 19 del Estatuto Tributario la ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIA-ABACO, se encuentra sometida al Rgimen Tributario Especial y cumple con lo estipulado en el artculo 125-1, 125-2 y 125-3 del Estatuto Tributario para efectos de la deduccin de la renta por donaciones estipulada en el artculo 126-2. 

 Que la ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIA-ABACO ha presentado su declaracin de renta en la administracin de impuestos nacionales en forma oportuna e ininterrumpida.  

 Que todos los ingresos por donaciones en dinero son depositados en establecimientos financieros autorizados que para el efecto tiene la ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIA-ABACO. 

 La ASOCIACIN DE BANCOS DE ALIMENTOS DE COLOMBIA-ABACO ha recibido de la empresa Empresa {{ eatc_dona_certifications. eatc_donor_fiscal_name }} con NIT {{ eatc_dona_certifications. eatc_code }} donaciones en especie de productos varios relacionados, facturas {{ARRAY de nmeros de facturas: eatc_certification_supports_headers. eatc_certification_support_code } } . donaciones en especie de varios productos relacionados a continuacin:  
 Relacin de productos 
 No. Factura    |    Fecha Factura    |    Nombre del Articulo    |    Valor SIN IVA 
 {{eatc_certification_products_details. eatc_certification_support_code }}| {{eatc_certification_products_details. eatc_certification_support_date }}| 
 {{eatc_certification_products_details. eatc_product_name }}|  
 {{eatc_certification_products_details. eatc_total_value }}| 

 Esta donacin en especie tiene valor de {{ eatc_dona_certifications. eatc_value }}. Estos productos fueron entregados a: [ARRAY DE {{eatc_certification_supports_details. eatc_doma_affiliated_organization }} ({{eatc_certification_supports_details. eatc_doma_affiliated_organization_id }})] , en el mes de  {{ eatc_dona_certifications. eatc_month }} de Ao {{ eatc_dona_certifications. eatc_year }} 

 El producto de la donacin ser utilizado en el territorio nacional con destino al cubrimiento de las necesidades de la poblacin en general, buscando de esta manera defender, proteger y promocionar los derechos humanos. 

 Que acorde al artculo 424, numeral 9 del Estatuto Tributario los alimentos de consumo humano donados a favor de los Bancos de Alimentos legalmente constituidos, se encuentran excluidos del IVA con el previo cumplimiento de los requisitos establecidos en el Decreto 1794 de 2013, artculo 4. 

 Se expide el presente certificado en la ciudad de Bogot D.C., el da {{ eatc_dona_certifications. eatc_signature_datetime }} 

 Espacio firma electrnica 

 Nombre representante legal 
 Representante Legal ABACO 

 Espacio firma electrnica 

 Nombre revisor fiscal 
 Revisor fiscal ABACO 
 Tarjeta Profesional No. _________________________ 
 Designado por: _________________________ 

 Elabor: EatCloud System 
 Aprob: {{}} 
 Revis: {{}} 

 [Pie de pgina: Datos de baco ] 

 Calle 19 A # 32 50 Barrio Cundinamarca                                                                                                                             administracion@abaco.org.co 
 Telfono: +57 (1) 402 93 05 Celular: + 57 313 245 79 78                                                                                                                      www.abaco.org.co 
 Bogot, D.C. - Colombia 

 Nota con respecto a la relacin de productos: 
 La idea es crear una tabla que se llene con el resultado de la consulta de detalles de productos 

 Nota con respecto a la relacin de bancos de alimentos 
 Al expresar en la documentacin lo siguiente 
 ARRAY DE {{eatc_certification_supports_details. eatc_doma_affiliated_organization }} ({{eatc_certification_supports_details. eatc_doma_affiliated_organization_id }}) 

 Se quiere indicar que se debe realizar un listado separado por comas, en donde est primero el nombre del banco y luego entre parntesis su respectivo NIT (ejemplo: Banco de Alimentos 1 (NIT Banco de alimentos 1), Banco de Alimentos 2 (NIT Banco de alimentos 2), ..., Banco de Alimentos n (NIT Banco de Alimentos n ) 

 Para eso se debe hacer un select distinct, de los respectivos datos, obtenidos en los parmetros indicados, en la consulta de los detalles del soporte . 

 Nota con respecto a la firma del documento  
 datos abajo de " Se expide el presente certificado en la ciudad de Bogot D.C., el da {{ eatc_dona_certifications. eatc_signature_datetime }} ": 

 Inicialmente el documento no contar con la informacin necesaria para realizar la firma del documento. Cuando se completa el proceso de aprobacin del documento, ser cuando se registran las firmas y se llevan al documento descargable . 

 Nota con respecto los datos de encabezado y pie de pgina 
 En una primera versin estos datos irn quemados, pero posteriormente se evaluar si es necesario obtenerlos de alguna persistencia con el nimo de dinamizarlos.  

 Nota con respecto marca de agua 
 En cuando se crea el certificado que aun no est aprobado, se debe colocar una marca de agua: Pre-certificado no vlido para efectos tributarios.  Esta marca de agua se deber quitar cuando se apruebe el documento .  

 Actualizacin del registro del certificado con el documento generado 
 Una vez generado el certificado en formato descargable, el sistema lo debe guardar, de manera que sea accesible al usuario final (que lo pueda descargar) y deber incorporar la informacin necesaria para hacerla en el campo 

 eatc_certificate_file 

 El sistema, cuando cree la carta sin firmas, deber realizar la actualizacin de la informacin del soporte con el siguiente llamado 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_certifications &_operacion= update &eatc_certificate_file ={{ eatc_certificate_file }}&WHEREeatc_code={{ eatc_dona_certifications. eatc_code}} 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deber entregar una respuesta donde exprese que el certificado de donacin con cdigo {{ eatc_dona_certifications. eatc_code}} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un cdigo de error y reversar los registros que pudieron haberse creado de manera parcial, con el nimo que se pueda reintentar la operacin hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CREA_CERT: FACTURA_ELECTRONICA_COLOMBIA