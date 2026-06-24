# constancia-de-entrega.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONSTANCIA DE ENTREGA ","showTimeToRead":false,"encodedImage":"BBR:HGxufQ~qj[fQ"},"containsDynamicDataSource":false}">

 Esta funcionalidad al activarla, desplegará un PDF descargable que servirá como constancia de entrega de la donación.  Dicho PDF funcionará de la siguiente manera 

 Al accionarse el botón para cada donación el sistema realiza el siguiente llamado 
 {{URL_donantes}} /api/ {{_DOM.cua_master}} / eatc_dona_headers? eatc-code={{codigo_donacion}} &_cmp = eatc-code,eatc_cua_master,eatc_donor,eatc-pod_id,eatc_code_verification_datetime,eatc-donation_manager_typology_b,eatc_dona_units,eatc-original_weight_kg,eatc-total_weight_kg,eatc-warning,eatc-donation_manager_code,eatc-donation_manager_name,eatc-donation_manager_user_doc_id,eatc-picker_name,eatc-picker_doc_id,eatc-picker_license_plate 

 Con la información obtenida se realizan las siguientes consultas: 
 {{ URL_beneficiarios }}/api/{{eatc_dona_headers. eatc_cua_master }}/ eatc_donation_managers ?beneficiary_ecosystem_leader=y&_cmp= identificador,identificador_unico_registro,unidad_territorial,correo_electonico,web 

 eatc_donation_managers. beneficiary_ecosystem_leader  
 eatc_donation_managers. beneficiary_ecosystem_leader = y (abaco) 
 eatc_donation_managers. web 
 eatc_donation_managers. web = https://abaco.org.co (abaco) 

 {{ URL_datagov }}/api/eatcloud/ eatc_cua ?name=eatc_dona_headers .eatc_donor &_cmp= logo_proof_of_delivery,contract_supervisor 

 eatc_cua. logo_proof_of_delivery => Campo pendiente de creación en ambiente productivo (ya se creó en pruebas) 
 eatc_cua. logo_proof_of_delivery = ....... (exito) => registro pendiente Productivo: URL que permita descargar el recurso que abajo se adjunta (ejemplo: https://eatcloudcorp.sharepoint.com/:i:/r/sites/EatCloud2/Documentos%20compartidos/Logo_constancia.jpg?csf=1&web=1&e=K1rDM8 )  
 eatc_cua. contract_supervisor => Campo pendiente de creación en ambiente productivo (ya se creó en pruebas) 
 eatc_cua. contract_supervisor = Fundación Éxito (exito) => registro pendiente en prodcuctivo 

 NOTA : con el servicio {{URL_datagov}}/optb/eatcloud/newfield    
     "_data" :[ 
         { 
             "table" : "eatc_cua" , 
             "name" : "logo_proof_of_delivery" , 
             "tipo" : "VARCHAR" , 
             "length" : "140" 
         } 
     ] 

 La creación del campo funcionó en ambiente de pruebas, pero no en productivo (salió este error): 
 "ts" : "240118153416" , 
     "op" : false , 
     "err_msg" : { 
         "USER" : "datagoveatcloud" , 
         "HOME" : "/home/datagoveatcloud" , 
         "SCRIPT_NAME" : "/_process/drop/_drop.php" , 
         "REQUEST_URI" : "//optb/eatcloud/newfield" , 
         "QUERY_STRING" : "_cua=eatcloud&_case=newfield" , 
         "REQUEST_METHOD" : "POST" , 
         "SERVER_PROTOCOL" : "HTTP/1.1" , 
         "GATEWAY_INTERFACE" : "CGI/1.1" , 
         "REDIRECT_QUERY_STRING" : "_cua=eatcloud&_case=newfield" , 
         "REDIRECT_URL" : "/optb/eatcloud/newfield" , 
         "REMOTE_PORT" : "49862" , 
         "SCRIPT_FILENAME" : "/home/datagoveatcloud/public_html/_process/drop/_drop.php" , 
         "SERVER_ADMIN" : "webmaster@datagov.eatcloud.info" , 
         "CONTEXT_DOCUMENT_ROOT" : "/home/datagoveatcloud/public_html" , 
         "CONTEXT_PREFIX" : "" , 
         "REQUEST_SCHEME" : "https" , 
         "DOCUMENT_ROOT" : "/home/datagoveatcloud/public_html" , 
         "REMOTE_ADDR" : "206.84.80.235" , 
         "SERVER_PORT" : "443" , 
         "SERVER_ADDR" : "132.148.165.25" , 
         "SERVER_NAME" : "datagov.eatcloud.info" , 
         "SERVER_SOFTWARE" : "Apache" , 
         "SERVER_SIGNATURE" : "" , 
         "PATH" : "/usr/local/jdk/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/X11R6/bin:/usr/local/bin:/usr/X11R6/bin:/root/bin:/opt/bin" , 
         "HTTP_COOKIE" : "PHPSESSID=cb38482e7bd180585742ae7f3bee2844" , 
         "HTTP_POSTMAN_TOKEN" : "403794eb-f03e-4826-a8e7-294071036e3c" , 
         "HTTP_ACCEPT" : "*/*" , 
         "HTTP_USER_AGENT" : "PostmanRuntime/7.36.1" , 
         "CONTENT_TYPE" : "application/json" , 
         "CONTENT_LENGTH" : "186" , 
         "HTTP_X_REAL_IP" : "206.84.80.235" , 
         "HTTP_X_FORWARDED_SERVER" : "datagov.eatcloud.info" , 
         "HTTP_X_FORWARDED_PROTO" : "https" , 
         "HTTP_X_FORWARDED_PORT" : "443" , 
         "HTTP_X_FORWARDED_HOST" : "datagov.eatcloud.info" , 
         "HTTP_X_FORWARDED_FOR" : "206.84.80.235" , 
         "HTTP_HOST" : "datagov.eatcloud.info" , 
         "proxy-nokeepalive" : "1" , 
         "HTTPS" : "on" , 
         "UNIQUE_ID" : "ZamLSLxeOhvBH2YTAwB7UwAAARU" , 
         "REDIRECT_STATUS" : "200" , 
         "REDIRECT_HTTPS" : "on" , 
         "REDIRECT_isproxyrequest" : "1" , 
         "REDIRECT_UNIQUE_ID" : "ZamLSLxeOhvBH2YTAwB7UwAAARU" , 
         "FCGI_ROLE" : "RESPONDER" , 
         "PHP_SELF" : "/_process/drop/_drop.php" , 
         "REQUEST_TIME_FLOAT" : 1705610056.093471050262451171875 , 
         "REQUEST_TIME" : 1705610056 , 
         "argv" : [ 
             "_cua=eatcloud&_case=newfield" 
         ], 
         "argc" : 1 
     }, 
     "err_num" : "" 
 } 

 {{ URL_beneficiarios }}/api/{{eatc_dona_headers. eatc_cua_master }}/ eatc_donation_managers ? identificador_unico_registro={{ eatc_dona_headers. eatc-donation_manager_code}}&_cmp=representante_legal   

 MODELO APORTADO POR EL SOLICITANTE 

Modelo Constancia 

 Modelo Constancia.xlsx 

 DISEÑO DEL INFORME 

 Logo del informe (parte superior izquierda) 
 Se aporta a continuación un recurso que deberá cargarse a la plataforma y relacionarse (URL recurso) en el campo eatc_cua. logo_proof_of_delivery (campo nuevo que se debe crear) 

 Datos Legales EatCloud (segunda columna parte superior) 
 Label:  
 class= lbl_datos_legales_eatcloud 

 A continuación se presentan los respectivos labels y valores que la sección en cuestión 

 Nit: 
 class= lbl_nit 
 901391724 

 Dirección: 
 class= lbl_direccion 
 Calle 6Sur No. 70-215 interior 806 

 Correo: 
 class= lbl_correo 

 soporte@eatcloud.com 
 DEPRECADO: operaciones@eatcloud.com 

 Web: 
 class= lbl_web 

 https://eatcloud.com   

 Datos Legales ABACO (tercera columna parte superior) 
 Label:  
 class= lbl_datos_legales + {{ eatc_donation_managers .identificador}}   

 A continuación se presentan los respectivos labels y valores que la sección en cuestión 

 Nit: 
 class= lbl_nit 

 Valor: 
 {{ eatc_donation_managers . identificador_unico_registro }}   

 Dirección: 
 class= lbl_direccion 

 Valor: 
 {{ eatc_donation_managers . unidad_territorial }}   
 Correo: 
 class= lbl_correo 

 Valor: 
 {{ eatc_donation_managers .correo_electonico}} 

 Web: 
 class= lbl_web 

 Valor: 
 {{ eatc_donation_managers . web }} => Campo pendiente de creación en la tabla eatc_donation_managers 

 A CONTINUACIÓN, PARA NO DUPLICAR LA INFORMACIÓN QUE YA CONSTA EN EL G-DOC, SE DOCUMENTARÁ SOLAMENTE AQUELLOS PUNTOS QUE REQUIERES  
 Destinación 
 Label:  
 class= lbl_destinacion 
 Según los datos que se obtienen {{eatc_dona_headers. eatc-donation_manager_typology_b }} se despliegan los siguientes labels así: 

 {{eatc_dona_headers. eatc-donation_manager_typology_b }}=1 
 class= lbl_donacion_bdea "Donación Bancos de Alimentos" 

 {{eatc_dona_headers. eatc-donation_manager_typology_b }}=!1 (diferente de 1) 
 class= lbl_donacion_inst_funda "Donación institución / fundación " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconstancia-de-entrega%2F3625009424-Logo_constancia.jpg&ow=1280&oh=720, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconstancia-de-entrega%2F3625009424-Logo_constancia.jpg&ow=1280&oh=720 

 239.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 b42d9b3a-3bf8-4ffd-976e-d6401a3c1328 
 4!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 f4cccd0c-c09d-471c-9158-c33493f2d275 
 2025-11-28T04:43:49.3435255Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"c6437895-ff48-4f2b-94c2-94c13ccc9af2","SequenceId":91,"FluidContainerCustomId":"2d04b1da-2f4f-4909-988d-10fcc230e3db","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 CONSTANCIA DE ENTREGA