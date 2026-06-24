# blockchain-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos invocar servicios de integracin con blockhain. 

 La URL que se propone para este es: 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= {{servicio}} 

 A partir de este llamado el sistema debe realizar las siguientes operaciones: 

 Persistencia respuesta llamados 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_blockchain_headers?headercode={{eatc_dona_headers.eatc-code}} 

 Ejemplos 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_blockchain_headers?headercode=exito7320220915152504349   

 https://datagov.eatcloud.info/api/eatcloud/eatc_blockchain_headers?headercode={{eatc_dona_headers.eatc-code}}  

 {{URL_entorno_datagov}}/api/eatcloud/eatc_blockchain_dona?headercode={{eatc_dona_headers.eatc-code}} 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_blockchain_dona?headercode=exito7320220915152504349   

 https://datagov.eatcloud.info/api/eatcloud/eatc_blockchain_headers?headercode={{eatc_dona_headers.eatc-code }}  

 SERVICIOS PARA CREACIN DE BLOCKCHAIN 
 Los servicios estn publicados en el siguiente servidor: 

 http://ec2-52-47-199-128.eu-west-3.compute.amazonaws.com:8080/login 

 Las credenciales de acceso a los servicios: 
 usuario:  eatcloud 
 password: addapta 

 [POST]  /activiti-app/services/login/validate login 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_login_validate   

 NOTACIN GENERAL DE LOS LLAMADOS PARA LA CONSTRUCCIN DEL SERVICIO 
 Se utiliza la siguiente notacin para la construccin del servicio de integracin 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= {{servicio}} 

 Lectura de datos del anuncio de donacin: 
 Definicin de array de datos  que se envan como consulta al object store especfico 

{{ array_parametros }}= {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= {{servicio}} &_distinct= eatc_origin_parameter 

 Object store especfico 
 {{eatc_object_store}} = {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= {{servicio}} &_distinct= eatc_object_store 

 Clave para consulta en el object store especfico 
 {{eatc_object_store_key}} = {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= {{servicio}} &eatc_object_store= {{eatc_object_store}} &_distinct= eatc_object_store_key 

 Lectura de datos a enviar mediante el servicio 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ {{eatc_object_store}} ? {{eatc_object_store_key}} ={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 De manera particular segn object store: 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ eatc_dona_headers ?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ eatc_dona ?eatc-dona_header_code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Mapeo de datos para llamado al servicio.   
 Para establecer el mapeo de datos propio del servicio, se deber realizar el siguiente llamado 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= {{servicio}} &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 En donde se obtendr la siguiente informacin 

 eatc_origin_parameter: Establece como se llama el parmetro en el eatc_object_store de eatcloud. 
 eatc_origin_parameter_split: Para campos tipo datetime, establece despus de la notacin :split() que parte del dato (date / hour) se le debe pasar al parmetro destino a partir de una funcin de split. 
 eatc_origin_param_type: Establece el tipo de dato en el eatc_object_store . 
 blck_target_parameter : Establece el nombre del parmetro destino, con el cual se invoca el servicio externo . 
 blck_target_parameter_type : Establece el tipo de dato del parmetro destino, que se debe enviar al servicio externo . 

 A continuacin se realiza la documentacin especfica de cada uno de los servicios: 

 [PUT] servicio: frmDonacionExcedente   (Nueva donacin) 
  /activiti-app/services/interface/prcEatCloud/frmDonacionExcedente/{token}    

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/put_activiti_app_services_interface_prcEatCloud_frmDonacionExcedente__token_   

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmDonacionExcedente 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmDonacionExcedente &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDonacionExcedente&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDonacionExcedente&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmDonacionExcedente 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/put_activiti_app_services_interface_prcEatCloud_frmDonacionExcedente__token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmDonacionExcedente &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDonacionExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDonacionExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 [POST] servicio: frmAdjudicarDonacion (Adjudicar donacin) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmAdjudicarDonacion/Excedente/{origin_entity_value}/{token} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmAdjudicarDonacion_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmAdjudicarDonacion 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmAdjudicarDonacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAdjudicarDonacion&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAdjudicarDonacion&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmAdjudicarDonacion 

 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmAdjudicarDonacion_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmAdjudicarDonacion &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAdjudicarDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAdjudicarDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 ***NUEVO: consulta para obtener la informacin a enviar en el parmetro donor_direccion_fiscal *** 
 Con el dato {{eatc_dona_header. eatc-donor }} se realiza la siguiente consulta: 

 {{ URL_entorno_datagov }}/crypt/eatcloud/getcrypt?table= eatc_customers_cua &fieldname=eatc_cua&fieldvalue={{eatc_dona_header. eatc-donor }}&fielddecrypt=eatc_customer_fiscal_id,eatc_cua 

 Con el dato {{eatc_customers_cua. eatc_customer_fiscal_id }} se realiza la siguiente consulta: 

 {{ URL_entorno_datagov }}/crypt/eatcloud/getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id &fieldvalue= {{eatc_customers_cua. eatc_customer_fiscal_id }} &fielddecrypt= eatc_address 

 El dato {{eatc_customers. eatc_address }} se lleva al parmetro donor_direccion_fiscal   que se emplea en el llamado al servicio " frmAdjudicar " 

 [POST] servicio: frmAgendarDonacion (Programar donacin)  
 /activiti-app/services/interface/byorigin/prcEatCloud/frmAgendarDonacion/Excedente/{origin_entity_value}/{token}   

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmAgendarDonacion_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmAgendarDonacion 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmAgendarDonacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAgendarDonacion&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAgendarDonacion&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmAgendarDonacion 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmAgendarDonacion_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmAgendarDonacion &eatc_origin_parameter =_novacio &&_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAgendarDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmAgendarDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type    

 [POST] servicio: frmDespachar (Enviar donacin) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmDespachar/Excedente/{origin_entity_value}/{token} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmDespachar_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmDespachar 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmDespachar &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmDespachar 

 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmDespachar_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmDespachar &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 [POST] servicio: frmRecibir (Enviar donacin) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmRecibir/Excedente/{origin_entity_value}/{token} 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmRecibir_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmRecibir 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmRecibir &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmRecibir&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmRecibir&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmRecibir 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmRecibir_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmRecibir &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmDespachar& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 [POST] servicio: frmPreCertificado (Traza) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmPreCertificado/Excedente/{origin_entity_value}/{token} 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmPreCertificado_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmPreCertificado 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmPreCertificado &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmPreCertificado&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmPreCertificado&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 

 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmPreCertificado 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmPreCertificado_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmPreCertificado &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmPreCertificado& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmPreCertificado& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 [POST] servicio: frmCertificacion (Certificado) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmCertificacion/Excedente/{idExcedente}/{token} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmCertificacion_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmCertificacion 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmCertificacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCertificacion&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCertificacion&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmCertificacion 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmCertificacion_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmCertificacion &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type  

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCertificacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type    

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCertificacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type    

 [POST] servicio: frmCancelarExcedente (Cancelar) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmCancelarExcedente/Excedente/{idExcedente}/{token} 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmCancelarExcedente_Excedente__idExcedente___token_    

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmCancelarExcedente 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmCancelarExcedente &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCancelarExcedente&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCancelarExcedente&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmCancelarExcedente 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmCancelarExcedente_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmCancelarExcedente &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCancelarExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type     

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmCancelarExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type    

 [POST] servicio: frmNoEnviadoExcedente (Cancelar) 
 /activiti-app/services/interface/byorigin/prcEatCloud/frmNoEnviadoExcedente/Excedente/{idExcedente}/{token} 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmNoEnviadoExcedente_Excedente__idExcedente___token_   

 origin_entity_value * = {{eatc_dona_headers. eatc-code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmNoEnviadoExcedente 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmNoEnviadoExcedente &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmNoEnviadoExcedente&_distinct= eatc_origin_parameter 

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmNoEnviadoExcedente&_distinct= eatc_origin_parameter 

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmNoEnviadoExcedente 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_byorigin_prcEatCloud_frmNoEnviadoExcedente_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmNoEnviadoExcedente &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmNoEnviadoExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmNoEnviadoExcedente& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 [POST] servicio: frmBulkProductoDonacion (Nuevos Productos) 
 /activiti-app/services/fr4ll/frmBulkProductoDonacion/Excedente/{idExcedente}/{token} 
 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_fr4ll_frmBulkProductoDonacion_Excedente__idExcedente___token_   

 idExcedente * = {{eatc_dona_headers. eatc-code }} = {{eatc_dona. eatc-dona_header_code }} 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio= frmBulkProductoDonacion 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmBulkProductoDonacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmBulkProductoDonacion&_distinct= eatc_origin_parameter     

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmBulkProductoDonacion&_distinct= eatc_origin_parameter    

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ eatc_dona ?eatc-dona_header_code={{eatc_dona_headers. eatc-code }}&_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmBulkProductoDonacion 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_fr4ll_frmBulkProductoDonacion_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmBulkProductoDonacion &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmBulkProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type     

 Pruebas:   => FALTAN DATOS 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmBulkProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type    

 [ POST ] servicio: frmProductoDonacion (Creacin de productos de productos) 
 /activiti-app/services/interface/prcEatCloud/frmProductoDonacion/Excedente/{idExcedente}/{token} 

 idExcedente * = {{eatc_dona_headers. eatc-code }} = {{eatc_dona. eatc-dona_header_code }} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_prcEatCloud_frmProductoDonacion_Excedente__idExcedente___token_   

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona. eatc-dona_header_code }} &eatc _ odd_id={{eatc_dona. eatc-odd_id }}&_servicio= frmProductoDonacion 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmProductoDonacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion&_distinct= eatc_origin_parameter      

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion&_distinct= eatc_origin_parameter     

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ eatc_dona ?eatc-dona_header_code={{eatc_dona. eatc-dona_header_code }}& eatc - odd_id={{eatc_dona. eatc-odd_id }} &_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmProductoDonacion 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/post_activiti_app_services_interface_prcEatCloud_frmProductoDonacion_Excedente__idExcedente___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmProductoDonacion &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type      

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 [ PATCH ] servicio: frmProductoDonacion (Edicin de productos) 
 /activiti-app/services/interface/prcEatCloud/frmProductoDonacion/{idExcedente}/{idProducto}/{token} 

 idExcedente * = {{eatc_dona_headers. eatc-code }} = {{eatc_dona. eatc-dona_header_code }} 
 idProducto * =   {{eatc_dona. eatc-odd_id }} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/patch_activiti_app_services_interface_prcEatCloud_frmProductoDonacion_id__idProducto___token_   

 Para la actualizacin del producto se usar el mtodo tipo: PATCH 

 Con el siguiente Endpoint: 

 /activiti-app/services/interface/prcEatCloud/frmProductoDonacion/id/ /O6WFtdnQ8iVK7Mh2XeilTjY2C 

 y el mismo PAYLOAD que ponemos en el alta: frmBulkProductoDonacion (ejemplo): 
 { 
     "id" : "sergio1044" , 
     "costefinal" : "4.00" , 
     "cost_original" : "4.00" , 
     "original_quantity" : "4" , 
     "quantity" : "4" , 
     "name" : "sergio1044" , 
     "product_channel_typology_a" : "" , 
     "product_channel_typology_b" : "" , 
     "product_channel_typology_c" : "" , 
     "product_unit_weight" : "33" , 
     "weight_final" : "132.00000" , 
     "VAT" : "0.16" 
 } 

 La respuesta ser de este tipo: 
 { 
     "context" : { 
         "criticalError" : false , 
         "blockChainHash" : "f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb" , 
         "blockChainList" : null , 
         "criticalMessage" : "" , 
         "criticalType" : "" , 
         "mensajesError" : [], 
         "listaPermisos" : {}, 
         "entities" : {}, 
         "values" : { 
             "iddonacion" : { 
                 "value" : "sergio1003" , 
                 "valueName" : "sergio1003" , 
                 "id" : "iddonacion" , 
                 "fieldName" : "Id Donacin" , 
                 "type" : "origin" 
             }, 
             "weight_final" : { 
                 "value" : "1320" , 
                 "valueName" : "1.320,00" , 
                 "id" : "weight_final" , 
                 "fieldName" : "Peso total de la donacin" , 
                 "type" : "integer" 
             }, 
             "original_quantity" : { 
                 "value" : "40" , 
                 "valueName" : "40,00" , 
                 "id" : "original_quantity" , 
                 "fieldName" : "original_quantity" , 
                 "type" : "integer" 
             }, 
             "quantity" : { 
                 "value" : "40" , 
                 "valueName" : "40,00" , 
                 "id" : "quantity" , 
                 "fieldName" : "quantity" , 
                 "type" : "integer" 
             }, 
             "product_donor_typology_c" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_donor_typology_c" , 
                 "fieldName" : "tercera tipologa de donante" , 
                 "type" : "text" 
             }, 
             "product_channel_typology_c" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_channel_typology_c" , 
                 "fieldName" : "Tercera tipologa producto canal" , 
                 "type" : "text" 
             }, 
             "product_donor_typology_a" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_donor_typology_a" , 
                 "fieldName" : "primera tipologa donante" , 
                 "type" : "text" 
             }, 
             "product_channel_typology_b" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_channel_typology_b" , 
                 "fieldName" : "Segunda tipologa producto canal" , 
                 "type" : "text" 
             }, 
             "product_donor_typology_b" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_donor_typology_b" , 
                 "fieldName" : "Segunda tipologa donante" , 
                 "type" : "text" 
             }, 
             "product_channel_typology_a" : { 
                 "value" : null , 
                 "valueName" : "" , 
                 "id" : "product_channel_typology_a" , 
                 "fieldName" : "Primera tipologa producto canal" , 
                 "type" : "text" 
             }, 
             "vat" : { 
                 "value" : "0" , 
                 "valueName" : "0,00" , 
                 "id" : "vat" , 
                 "fieldName" : "VAT" , 
                 "type" : "integer" 
             }, 
             "product_unit_weight" : { 
                 "value" : "330" , 
                 "valueName" : "330,00" , 
                 "id" : "product_unit_weight" , 
                 "fieldName" : "Peso unitario del producto" , 
                 "type" : "integer" 
             }, 
             "costefinal" : { 
                 "value" : "40" , 
                 "valueName" : "40,00" , 
                 "id" : "costefinal" , 
                 "fieldName" : "Coste final" , 
                 "type" : "integer" 
             }, 
             "cost_original" : { 
                 "value" : "40" , 
                 "valueName" : "40,00" , 
                 "id" : "cost_original" , 
                 "fieldName" : "Coste original" , 
                 "type" : "integer" 
             }, 
             "blockchain" : { 
                 "value" : "f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb" , 
                 "valueName" : "f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb" , 
                 "id" : "blockchain" , 
                 "fieldName" : "blockchain" , 
                 "type" : "text" 
             }, 
             "name" : { 
                 "value" : "sergio1044" , 
                 "valueName" : "sergio1044" , 
                 "id" : "name" , 
                 "fieldName" : "name" , 
                 "type" : "text" 
             }, 
             "id" : { 
                 "value" : "sergio1044" , 
                 "valueName" : "sergio1044" , 
                 "id" : "id" , 
                 "fieldName" : "id" , 
                 "type" : "identificador" 
             } 
         }, 
         "funcionalidades" : { 
             "roles" : false , 
             "usuarios" : false , 
             "pacientes" : false , 
             "traza" : false , 
             "estadistica" : false , 
             "entidades" : false , 
             "calendario" : false , 
             "eficiencias" : false , 
             "organizaciones" : false , 
             "tablas" : false , 
             "coleccionesExternas" : false , 
             "gestorServicios" : false , 
             "plantillas" : false , 
             "trabajadores" : false , 
             "administrador" : false , 
             "menus" : false , 
             "exportforms" : false , 
             "importforms" : false , 
             "templatefields" : false 
         }, 
         "openThreads" : 206 , 
         "openConnections" : 15 
     } 
 }   

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona. eatc-dona_header_code }} &eatc _ odd_id={{eatc_dona. eatc-odd_id }}&_servicio= frmProductoDonacionEditar 

 Lectura de datos del anuncio de donacin 
 El sistema deber realizar la siguiente lectura para determinar los parmetros que debe consultar en la donacin  
 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmProductoDonacion &_distinct= eatc_origin_parameter 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion&_distinct= eatc_origin_parameter      

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion&_distinct= eatc_origin_parameter      

 Con la anterior consulta se obtiene {{ array_parametros }} que se deben consultar para obtener la informacin a llevar al servicio de integracin en el respectivo body 
 {{URL_entorno_donantes}} /api/{{_DOM. cua_master }}/ eatc_dona ?eatc-dona_header_code={{eatc_dona. eatc-dona_header_code }}& eatc - odd_id={{eatc_dona. eatc-odd_id }} &_cmp= {{ array_parametros }} 

 Llamado al servicio de integracin frmBulkProductoDonacion 
 Tal como se expresa en la respectiva documentacin, se deber realizar el llamado al servicio correspondiente: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/patch_activiti_app_services_interface_prcEatCloud_frmProductoDonacion_id__idProducto___token_   

 En la formacin del JSON particular para el envo de los datos, se debern enviar las respectivas equivalencias por parmetro eatcloud consultado ( eatc_origin_parameter ), segn lo que se informa en el campo respectivo {{eatc_blockchain_int_parameters. blck_target_parameter }} 

 {{URL_entorno_datagov}} /api/ eatcloud /eatc_blockchain_int_parameters?service= frmProductoDonacion &eatc_origin_parameter =_novacio &_cmp= eatc_origin_parameter,eatc_origin_parameter_split,eatc_origin_param_type, blck_target_parameter, blck_target_param_type 

 Produccin: 
 https://datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type      

 Pruebas: 
 https://dev.datagov.eatcloud.info/api/ eatcloud /eatc_blockchain_int_parameters?service=frmProductoDonacion& eatc_origin_parameter=_novacio &_cmp= eatc_origin_parameter,eatc_origin_param_type, blck_target_parameter, blck_target_param_type   

 [ DELETE ] servicio: frmProductoDonacion (Borrado de Productos) 
 /activiti-app/services/interface/prcEatCloud/frmProductoDonacion/{idExcedente}/ 

 idExcedente * = {{eatc_dona_headers. eatc-code }} = {{eatc_dona. eatc-dona_header_code }} 
 idProducto * =   {{eatc_dona. eatc-odd_id }} 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/delete_activiti_app_services_interface_prcEatCloud_frmProductoDonacion_id___idproducto___token_ 

 PayLoad 

 vaco 

 Respuesta 

 {     
 "context": { 
         "criticalError": false, 
         "blockChainHash": " f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb ", 
         "blockChainList": null, 
         "criticalMessage": "", 
         "criticalType": "", 
         "mensajesError": [], 
         "listaPermisos": {}, 
         "entities": {}, 
         "values": { 
             "iddonacion": { 
                 "value": "pruebaesp25qowevoygwivlz5qsq3kp20221003064532889", 
                 "valueName": "pruebaesp25qowevoygwivlz5qsq3kp20221003064532889", 
                 "id": "iddonacion", 
                 "fieldName": "Id Donacin", 
                 "type": "origin" 
             }, 
             "weight_final": { 
                 "value": "132.00000", 
                 "valueName": "132,00", 
                 "id": "weight_final", 
                 "fieldName": "Peso total de la donacin", 
                 "type": "integer" 
             }, 
             "original_quantity": { 
                 "value": "4", 
                 "valueName": "4,00", 
                 "id": "original_quantity", 
                 "fieldName": "original_quantity", 
                 "type": "integer" 
             }, 
             "quantity": { 
                 "value": "4", 
                 "valueName": "4,00", 
                 "id": "quantity", 
                 "fieldName": "quantity", 
                 "type": "integer" 
             }, 
             "product_donor_typology_c": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_donor_typology_c", 
                 "fieldName": "tercera tipologa de donante", 
                 "type": "text" 
             }, 
             "product_channel_typology_c": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_channel_typology_c", 
                 "fieldName": "Tercera tipologa producto canal", 
                 "type": "text" 
             }, 
             "product_donor_typology_a": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_donor_typology_a", 
                 "fieldName": "primera tipologa donante", 
                 "type": "text" 
             }, 
             "product_channel_typology_b": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_channel_typology_b", 
                 "fieldName": "Segunda tipologa producto canal", 
                 "type": "text" 
             }, 
             "product_donor_typology_b": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_donor_typology_b", 
                 "fieldName": "Segunda tipologa donante", 
                 "type": "text" 
             }, 
             "product_channel_typology_a": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "product_channel_typology_a", 
                 "fieldName": "Primera tipologa producto canal", 
                 "type": "text" 
             }, 
             "vat": { 
                 "value": null, 
                 "valueName": "", 
                 "id": "vat", 
                 "fieldName": "VAT", 
                 "type": "integer" 
             }, 
             "product_unit_weight": { 
                 "value": "33", 
                 "valueName": "33,00", 
                 "id": "product_unit_weight", 
                 "fieldName": "Peso unitario del producto", 
                 "type": "integer" 
             }, 
             "costefinal": { 
                 "value": "4.00", 
                 "valueName": "4,00", 
                 "id": "costefinal", 
                 "fieldName": "Coste final", 
                 "type": "integer" 
             }, 
             "cost_original": { 
                 "value": "4.00", 
                 "valueName": "4,00", 
                 "id": "cost_original", 
                 "fieldName": "Coste original", 
                 "type": "integer" 
             }, 
             "blockchain": { 
                 "value": "f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb", 
                 "valueName": "f56d0120639d2d0b1f01765c49d00661add45c323b8d248df9852daae69ce7fb", 
                 "id": "blockchain", 
                 "fieldName": "blockchain", 
                 "type": "text" 
             }, 
             "name": { 
                 "value": "sergio1003", 
                 "valueName": "sergio1003", 
                 "id": "name", 
                 "fieldName": "name", 
                 "type": "text" 
             }, 
             "id": { 
                 "value": "sergio1003", 
                 "valueName": "sergio1003", 
                 "id": "id", 
                 "fieldName": "id", 
                 "type": "identificador" 
             } 
         }, 
         "funcionalidades": { 
             "roles": false, 
             "usuarios": false, 
             "pacientes": false, 
             "traza": false, 
             "estadistica": false, 
             "entidades": false, 
             "calendario": false, 
             "eficiencias": false, 
             "organizaciones": false, 
             "tablas": false, 
             "coleccionesExternas": false, 
             "gestorServicios": false, 
             "plantillas": false, 
             "trabajadores": false, 
             "administrador": false, 
             "menus": false, 
             "exportforms": false, 
             "importforms": false, 
             "templatefields": false 
         }, 
         "openThreads": 0, 
         "openConnections": 0 
     } 
 } 

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona. eatc-dona_header_code }} &eatc _ odd_id={{eatc_dona. eatc-odd_id }}&_servicio= frmProductoDonacionEliminar 

 [ GET ] servicio: generarcertificado (generacion certificado) *** Nuevos parmetros y nombramiento de parmetros*** 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/get_activiti_app_services_eatcloud_generarcertificado__iddonacion___idEntidadsocial___emailEntidadsocial___token_   

   ***NUEVO: Se nombra la variable de manera diferente*** iddonacion   * = {{eatc_dona_headers. eatc-code }} = {{eatc_dona. eatc-dona_header_code }} 

   ***NUEVO parmetro*** idEntidadsocial (antes: donationId ) * = {{eatc_dona_headers. eatc-donation_manager_code }} 

   ***NUEVO parmetro*** emailEntidadsocial   * = {{ eatc_donation_managers . correo_electronico }} 

 Se tendra que realizar la siguiente consulta para obtener el valor a enviar en este parametro 

 {{ URL_entorno_beneficiarios }}/api/{{_DOM. cua_master }}/ eatc_donation_managers ? identificador_unico_registro = {{eatc_dona_headers. eatc-donation_manager_code }} &_cmp= correo_electronico 

 Documentacin: 
 http://eatcloud.swagger.nadiesinsuraciondiaria.es/#/EatCloud/get_activiti_app_services_eatcloud_generarcertificado__iddonacion___idEntidadsocial___emailEntidadsocial___token_   

 Endpoint 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code= {{eatc_dona. eatc-dona_header_code }} &_servicio= generarcertificado 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE INTEGRACIN CON BLOCKCHAIN