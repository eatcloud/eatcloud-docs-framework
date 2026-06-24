# aprobación-de-certificado-de-donación-crea_cert.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Este proceso realiza varias tareas finales que dan como resultado un certificado aprobado oficial. 

 LLAMADO AL SERVICIO 

 El servicio ser invocado de la siguiente manera  
 {{URL_entorno_donante}}/ aprv_cert /{{_DOM. cua_master }}/ eatc_dona_certification_code= {{ eatc_dona_certification_code }} 

 REGISTRO Y ACTUALIZACIN DE DATOS 

 Registro de la aprobacin 

 El sistema debe proceder a realizar el siguiente registro de la aprobacin: 

 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_certification_approval_registry &_operacion= insert &eatc_certification_code={{eatc_dona_certifications. eatc_code }}&eatc_approval_datetime={{ timestamp_formato AAAA:MM:DD HH:MM:SS }}&eatc_approval_code= representante_legal &eatc_approval_type= final &eatc_approval_role= representante_legal &eatc_bo_user={{bo_usuarios. usuario }} 

 Actualizacin de datos del certificado 

 Cuando se aprueba el certificado se debe actualizar la la siguiente informacin en la persistencia en donde se registra dicho certificado eatc_dona_certifications (utilizando el cdigo que se enva en el llamado al servicio: eatc_dona_certification_code= {{ eatc_dona_certification_code }} ) 
 parametros_actualizacion_certificado 

 eatc_certification_datetime 
 Timestamp con fecha y hora actual (en formato AAAA-MM-DD HH:MM:SS) que se obtiene del parmetro eatc_certification_approval_registry. eatc_approval_datetime , de la bsqueda:  
 {{URL_entorno_donants}}/api/{{_DOM. cua_master }}/ eatc_certification_approval_registry ?eatc_certification_code={{ eatc_dona_certification_code }} &eatc_approval_type= final 

 eatc_bo_user:  
 Se obtiene del parmetro eatc_certification_approval_registry. eatc_bo_user , de la bsqueda:  
 {{URL_entorno_donants}}/api/{{_DOM. cua_master }}/ eatc_certification_approval_registry ?eatc_certification_code={{ eatc_dona_certification_code }} &eatc_approval_type= final 

 eatc_certificate_token 
 Token criptogrfico con la informacin del json del certificado o del archivo del certificado (puede ser un hash de la informacin, que de alguna manera se deber incorporar en el documento descargable para su autenticacin). 

 eatc_verification_code 
 Cdigo de 6 cifras (pueden ser alfanumricas), muy similar al cdigo de verificacin que se genera para cada anuncio de donacin y que servir para verificar la autenticidad del certificado de donacin.  Idealmente se debe guardar encriptado en la base de datos , para que la comparacin se tenga que hacer utilizando tambin las funciones de encriptacin. 

 Se realiza el respectivo llamado al CRD para actualizar el registro del certificado 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_certifications &_operacion= update & {{parametros_actualizacion_certificado}}& WHEREeatc_code ={{ eatc_dona_certification_code }} 

 FIRMAS CERTIFICADOS 
 Dado que el certificado posee dos firmas (Revisor Fiscal y Representante Legal), cuando se aprueba el certificado, se le deben registrar dichas firma en la persistencia establecida para ello: eatc_dona_certifications_sgs   registrando dos firmas por certificado: 

 Firma certificado: revisora fiscal 
 parametros_firma_certificado_revisor_fiscal 

 eatc_code 
 Corresponde al cdigo del certificado que se est firmando: eatc_dona_certification_code= {{ eatc_dona_certification_code }}   

 NOTA : a diferencia de muchos parmetros subsiguientes de la firma, este dato se debe guardar desencriptado en el repositorio eatc_dona_certifications_sgs dado que se utiliza como criterio de filtro para ubicar las firmas en el certificado 

 eatc_signature_datetime:  
 Corresponde al timestamp en formato AAAA-MM-DD HH:MM:SS en el cual se firma el certificado. 

 eatc_signature_location_identifier 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_signature_location_identifier el dato que se obtiene del parmetro bo_usuarios. eatc_signature_location_identifier en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_signature_location_identifier &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 
 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   

 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 NOTA: a diferencia de muchos parmetros subsiguientes de la firma, este dato se debe guardar desencriptado en el repositorio eatc_dona_certifications_sgs dado que se utiliza como criterio de filtro para ubicar las firmas en el certificado 

 eatc_signature 
 La siguiente firma deber guardarse encriptado (bien sea el recurso o la ubicacin del recurso, en este segundo caso el recurso se deber guardar en una carpeta protegida) en el parmetro: bo_usuarios. sgcrt del repositorio de usuarios del BO respectivo: 

 https://devbeneficiarios.eatcloud.info/crd/abaco/?_tabla=bo_usuarios&_operacion=update&WHEREeatc_approval_role=revisoria_fiscal  

 (el registro est pendiente de creacin) 
 https://beneficiarios.eatcloud.info/crd/abaco/?_tabla=bo_usuarios&_operacion=update&WHEREeatc_approval_role=revisoria_fiscal  

 (el registro est pendiente de creacin) 

 Una vez guardado el recurso, se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_signature el dato que se obtiene del parmetro bo_usuarios. sgcrt en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= sgcrt &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_name 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_name el dato que se obtiene del parmetro bo_usuarios. eatc_name en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_name &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_doc_id 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_doc_id el dato que se obtiene del parmetro bo_usuarios. eatc_doc_id en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_doc_id &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_position 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_position el dato que se obtiene del parmetro bo_usuarios. eatc_position en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_position &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_tax_review_firm 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_tax_review_firm el dato que se obtiene del parmetro bo_usuarios. eatc_tax_review_firm en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_tax_review_firm &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_professional_card 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_professional_card el dato que se obtiene del parmetro bo_usuarios. eatc_professional_card en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_professional_card &filterfield_1=eatc_approval_role&filtervalue_1= revisoria_fiscal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= revisoria_fiscal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 LLAMADO PARA LA CREACIN DEL REGISTRO 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_certifications_sgs &_operacion= insert & {{parametros_firma_certificado_revisor_fiscal}} 

 LLAMADO PARA LA ENCRIPTACIN DEL REGISTRO 
 {{URL_entorno_donantes}}/crypt/{{_DOM.cua_master}}/ encrypt ?table= eatc_dona_certifications_sgs &fieldname=eatc_name,eatc_doc_id,eatc_position,eatc_tax_review_firm,eatc_professional_card 

 Firma certificado: representante legal 
 parametros_firma_certificado_representante_legal 

 eatc_signature_datetime:  
 Corresponde al timestamp en formato AAAA-MM-DD HH:MM:SS en el cual se firma el certificado. 

 eatc_signature_location_identifier 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_signature_location_identifier el dato que se obtiene del parmetro bo_usuarios. eatc_signature_location_identifier en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_signature_location_identifier &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 NOTA: a diferencia de muchos parmetros subsiguientes de la firma: Este dato se debe guardar desencriptado en el repositorio eatc_dona_certifications_sgs dado que se utiliza como criterio de filtro para ubicar las firmas en el certificado 

 eatc_signature 
 La siguiente firma deber guardarse encriptado (bien sea el recurso o la ubicacin del recurso, en este segundo caso el recurso se deber guardar en una carpeta protegida) en el parmetro: bo_usuarios. sgcrt del repositorio de usuarios del BO respectivo: 

 https://devbeneficiarios.eatcloud.info/crd/abaco/?_tabla=bo_usuarios&_operacion=update&WHEREeatc_approval_role= representante_legal   
 (el registro est pendiente de creacin) 

 Una vez guardado el recurso, se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_signature el dato que se obtiene del parmetro bo_usuarios. sgcrt en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= sgcrt &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_name 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_name el dato que se obtiene del parmetro bo_usuarios. eatc_name en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_name &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_doc_id 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_doc_id el dato que se obtiene del parmetro bo_usuarios. eatc_doc_id en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_doc_id &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_position 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_position el dato que se obtiene del parmetro bo_usuarios. eatc_position en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_position &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_tax_review_firm 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_tax_review_firm el dato que se obtiene del parmetro bo_usuarios. eatc_tax_review_firm en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_tax_review_firm &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 eatc_professional_card 
 Se deber llevar al parmetro eatc_dona_certifications_sgs .eatc_professional_card el dato que se obtiene del parmetro bo_usuarios. eatc_professional_card en la consulta: 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=bo_usuarios&fieldname= eatc_professional_card &filterfield_1=eatc_approval_role&filtervalue_1= representante_legal 

 Que es el valor desencriptado del parmetro que se obtiene de: 

 {{URL_entorno_beneficiarios}}/api/abaco/bo_usuarios?eatc_approval_role= representante_legal   
 NOTA: el registro que funcionar con la anterior consulta an no ha sido creado 

 Este dato se debe guardar encriptado en el repositorio eatc_dona_certifications_sgs 

 LLAMADO PARA LA CREACIN DEL REGISTRO 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_certifications_sgs &_operacion= insert & {{parametros_firma_certificado_representante_legal}} 

 LLAMADO PARA LA ENCRIPTACIN DEL REGISTRO 
 {{URL_entorno_donantes}}/crypt/{{_DOM.cua_master}}/ encrypt ?table= eatc_dona_certifications_sgs &fieldname=eatc_name,eatc_doc_id,eatc_position,eatc_tax_review_firm,eatc_professional_card 

 Actualizacin del archivo del certificado (con firmas, para dejarlo en firme) 
 Con la informacin de las firmas, se procede a quitarle la marca de agua al certificado, y a colocarle las respectivas firmas para dejarlo con validez legal. 

 [Encabezado: Logo de baco Centrado ] 

 CERTIFICADO DE DONACIN No. {{ eatc_dona_certifications. eatc_code }} 

 Cdigo de verificacin: {{ eatc_dona_certifications. eatc_verification_code }} 

 EL SUSCRITO REVISOR FISCAL  

 CERTIFICA QUE: 

 [***Cuerpo del certificado como se expidi segn el tipo de soporte: carta_colombia o factura_electronica_colombia ***] 

 Se expide el presente certificado en la ciudad de Bogot D.C., el da {{ eatc_dona_certifications. eatc_signature_datetime }} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_signature &filterfield_1= eatc_signature_location_identifier &filtervalue_1= representante_legal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_name &filterfield_1= eatc_signature_location_identifier &filtervalue_1= representante_legal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_position &filterfield_1= eatc_signature_location_identifier &filtervalue_1= representante_legal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table=eatc_dona_certifications_sgs&fieldname= eatc_signature &filterfield_1= eatc_signature_location_identifier &filtervalue_1= revisoria_fiscal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_name &filterfield_1= eatc_signature_location_identifier &filtervalue_1= revisoria_fiscal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_position &filterfield_1= eatc_signature_location_identifier &filtervalue_1= revisoria_fiscal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 

 Tarjeta Profesional No. {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_professional_card &filterfield_1= eatc_signature_location_identifier &filtervalue_1= revisoria_fiscal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}} 
 Designado por {{URL_entorno_beneficiarios}}/crypt/ abaco /decrypt?table= eatc_dona_certifications_sgs &fieldname= eatc_tax_review_firm &filterfield_1= eatc_signature_location_identifier &filtervalue_1= revisoria_fiscal &filterfield_2= eatc_code &filtervalue_2= {{eatc_dona_certification_code}}   {{eatc_dona_certifications. }} 

 Elabor: EatCloud System 
 Revis y aprob: [ARRAY {{eatc_certification_approval_registry. eatc_approval_role }}{{eatc_certification_approval_registry. eatc_approval_datetime }} ({{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_certification_approval_registry? eatc_certification_code= eatc_dona_certifications)] 

 [Pie de pgina: Datos de baco ] 

 Calle 19 A # 32 50 Barrio Cundinamarca                                                                                                                           administracion@abaco.org.co 

 Telfono: +57 (1) 402 93 05 Celular: + 57 313 245 79 78                                                                                                                    www.abaco.org.co 

 Bogot, D.C. - Colombia 

 Actualizacin del registro del certificado con el documento generado 
 Una vez generado el certificado en formato descargable, el sistema lo debe guardar, de manera que sea accesible al usuario final (que lo pueda descargar) y deber incorporar la informacin necesaria para hacerla en el campo 

 eatc_certificate_file 

 El sistema, cuando cree la carta sin firmas, deber realizar la actualizacin de la informacin del soporte con el siguiente llamado 
 {{URL_entorno_donantes}}/crd/{{_DOM.cua_master}}/?_tabla= eatc_dona_certifications &_operacion= update &eatc_certificate_file ={{ eatc_certificate_file }}& WHEREeatc_code ={{ eatc_dona_certification_code }} 

 Actualizacin de datos de los anuncios de donacin 
 Con el cdigo del certificado recin aprobado, se actualiza la informacin los encabezados de anuncios de donacin de la siguiente  de la siguiente manera: 

 Como primera medida, se traen los cdigos de los anuncios de donacin ( eatc_certification_supports_details . eatc_dona_header_code ) cuyos soportes han sido cobijados por el certificado que se cre recientemente con la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_details?eatc_certification_support_code = {{ eatc_certification_supports_headers. eatc_certification_support_code}} 

 Con el array de datos ( array_eatc_dona_header_code ) obtenidos del parmetro eatc_certification_supports_details . eatc_dona_header_code que se obtienen de la anterior consulta, se debe proceder a actualizar la informacin de los respectivos anuncios de donacin, marcndolos con el estado de " certified " y estampando la fecha y hora de precertificacin ( eatc-certification_datetime ).  Para realizar dicha actualizacin  se realiza la siguiente llamada al CRD. 

 {{URL_entorno_donantes}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_dona_headers &_operacion= update &eatc_certificate_code={{ eatc_dona_certifications. eatc_code }}&eatc-state= certified &eatc-certification_datetime={{ eatc_dona_certifications. eatc_certification_datetime }}& WHERE eatc-code = {{ array_eatc_dona_header_code }} 

 ***NUEVO: LLAMADO AL SERVICIO DE INTEGRACIN BLOCKCHAIN *** 
 Endpoint (segn documentacin ([POST] servicio: frmCertificacion (Certificado) ): sujeto a revisin) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmCertificacion 

 Parmetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Cdigo del anuncio de donacin recientemente creado: eatc_dona_heaaders. eatc-code => parmetro de carcter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parmetro de carcter obligatorio 

 Respuesta exitosa del servicio 
 Cuando el servicio corra todos sus procesos, deber entregar una respuesta donde exprese que el certificado de donacin con cdigo {{ eatc_dona_certifications. eatc_code}} ha sido creado exitosamente 

 Respuesta no exitosa del servicio 
 Si cualquiera de los procesos falla, se debe devolver un cdigo de error y reversar los registros que pudieron haberse creado de manera parcial, con el nimo que se pueda reintentar la operacin hasta obtener una respuesta exitosa. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faprobaci%C3%B3n-de-certificado-de-donaci%C3%B3n-crea_cert%2F2805935087-EmbeddedImage--18-.png&ow=333&oh=254, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Faprobaci%C3%B3n-de-certificado-de-donaci%C3%B3n-crea_cert%2F2805935087-EmbeddedImage--18-.png&ow=333&oh=254 

 962.000000000000 

 APROBACIN DE CERTIFICADO DE DONACIN (APRV_CERT)