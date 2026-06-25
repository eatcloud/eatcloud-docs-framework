# toma-de-fotografías.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
La idea con esta implementación, es establecer la toma de fotografías inicialmente en puntos fijos de la APP, es decir, un puntos que estarán configurados en los menús de la APP y que se desplegarán en puntos específicos, según lo establece el parámetro eatc_photos. eatc_validation_point , es decir, en la APP se definen puntos en la lógica correspondientes inicialmente a los dos puntos que por el momento se han definido como puntos de toma de fotografía, a saber&#58; 
&#160; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_photos?_id=_*&amp;_cmp=eatc_validation_point 
Y que para el caso de producción serán&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_photos?_id=_*&amp;_cmp=eatc_validation_point &#160; 
&#160; 

lbl_registrar_salida_pod 

lbl_verificar_donacion 

 ***NUEVA&#58; lbl_not_delivered&#58; fotografía en la funcionalidad de “ registro de no entrega ” *** 
&#160; 
Entonces, en esos puntos, el sistema deberá desplegar botones de toma de fotografía, que accedan a esa función y que a continuación se describe, como se construyen a partir de la información que se encuentra en la estructura de datos eatc_photos. 
&#160; 
Antes de seguir, se anota que en el futuro se desplegará una nueva funcionalidad para tomar fotos, pero esta será utilizada para “escanear” documentos y extraer información de ellos con inteligencia artificial. &#160;Por lo tanto en ese nuevo punto se deberá definir el botón respectivo, y deberá funcionar de manera similar a como se explicará a continuación, pero en este caso se integrará con el servicio de IA que se está desarrollando para analizar la Fotografía y extraerle la información. &#160; Por lo tanto esta definición deberá entenderse, como una para desplegar el botón de tomar fotografía, otorgarle un label característico y generar mensajes de confirmación específicos. &#160;Por eso en adelante se explicará el funcionamiento de cada punto en donde se configurará el botón y cómo deberá entenderse su funcionamiento&#58; 
&#160; 
Toma de fotografía al registrar la salida del punto de donación (lbl_registrar_salida_pod) 
El sistema, deberá tener un botón, ubicado en este punto del proceso, cuando para una donación específica se registra la salida del punto de donación, el cual para activarse (es decir, para estar disponible para el usuario) tendrá que hacerse mediante estas consultas, diseñadas para que la funcionalidad dependa inicialmente de la cuenta maestra y de la cuenta usuario. 
&#160; 
El sistema, para la donación en cuestión deberá realizar la siguiente consulta&#58;&#160; 
 &#123;&#123; URL_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp= eatc-code, eatc_cua_master , eatc-donor , eatc-donation_manager_code 
&#160; 
Con los datos obtenidos, y sabiendo que la ubicación programada en la app es “ el registro de salida del punto de donación ” o “ lbl_registrar_salida_pod ”, entonces el sistema deberá realizar la siguiente consulta&#58; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master=&#123;&#123; eatc_dona_headers. eatc_cua_master &#125;&#125; &amp;eatc_cua=&#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125; 
Si no obtiene respuesta, entonces realiza esta consulta&#58; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master=&#123;&#123; eatc_dona_headers. eatc_cua_master &#125;&#125; &amp;eatc_cua=_* 
Si no obtiene resultado, entonces la funcionalidad (el botón para tomar la fotografía) no se despliega. &#160;En caso contrario el sistema deberá entender lo siguiente&#58; 
&#160; 
El label del botón para tomar la fotografía será 
 &#123;&#123;eatc_photos. eatc_label &#125;&#125; 
&#160; 
La validación de obligatoriedad de toma de la foto será 
 &#123;&#123;eatc_photos. eatc_mandatory &#125;&#125;&#58; cuando reciba “y”, la foto será obligatoria, y en su defecto no. 
&#160; 
El mensaje de validación de obligatoriedad de toma de la foto será (que se despliega si no se toma la foto en el punto definido y no permitirá seguir adelante) 
 &#123;&#123;eatc_photos. eatc_validation_message &#125;&#125; 
&#160; 
 Mediante el botón respectivo, el sistema despliega la funcionalidad que permite seleccionar una foto de la galería o abrir la cámara para tomar una fotografía. 
&#160; 
 El usuario podrá seleccionar o tomar una fotografía, acto seguido el sistema invocará el servicio para subir fotografías al sistema, y una vez esté en la nube, capturará la ruta en la cual quedó almacenada en el servidor &#123;&#123; ruta_foto &#125;&#125; y el código con el cual se identifica la fotografía &#123;&#123; codigo_foto &#125;&#125; 
 &#123;&#123; URL_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_photo_registry&amp;_operacion= insert &amp;eatc_code= &#123;&#123; codigo_foto &#125;&#125; &amp;eatc_cua_master=&#123;&#123;eatc_dona_headers. eatc_cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc_doma_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;eatc_label= lbl_registrar_salida_pod &amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_photo= &#123;&#123; ruta_foto &#125;&#125; &#160; 
&#160; 
 Ejemplo 1 &#58; anuncio “ iconnaad4a6bfad62eb53425894a928f2b56320250110145341 ” cua_master “ mexico ” en ambiente “ dev ” 
El sistema, para la donación en cuestión deberá realizar la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/mexico/eatc_dona_headers?eatc-code=iconnaad4a6bfad62eb53425894a928f2b56320250110145341&amp;_cmp=eatc-code,eatc_cua_master,eatc-donor,eatc-donation_manager_code&#160; 
Dado que la respuesta es&#58; 
&#123; 
 eatc-code &#58; &quot;iconnaad4a6bfad62eb53425894a928f2b56320250110145341&quot;, 
 eatc_cua_master &#58; &quot;mexico&quot;, 
 eatc-donor &#58; &quot;iconn&quot;, 
 eatc-donation_manager_code &#58; &quot;FSA001009R70&quot; 
&#125; 
El sistema deberá realizar la siguiente consulta (sabiendo que está en el punto específico de la APP&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master= mexico &amp;eatc_cua= iconn &#160;&#160; 
Como no obtiene respuesta, entonces realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master= mexico &amp;eatc_cua=_* &#160; 
Y dado que obtiene esta respuesta&#58; 
&#123; 
 _id &#58; &quot;1&quot;, 
 eatc_cua_master &#58; &quot;mexico&quot;, 
 eatc_cua &#58; &quot;_*&quot;, 
 eatc_label &#58; &quot;lbl_salida_almacen&quot;, 
 eatc_mandatory &#58; &quot;y&quot;, 
 eatc_validation_point &#58; &quot;lbl_registrar_salida_pod&quot;, 
 eatc_validation_message &#58; &quot;lbl_salida_almacen_vm&quot; 
&#125; 
&#160; 
Entonces despliega un botón&#58; 
&#160; 
Cuyo label es 
 lbl_salida_almacen ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_salida_almacen ) 
 “ Salida Almacen - Factura Aliado ” 
&#160; 
Cuya obligatoriedad de validación o toma de fotografía es 
 “y”, es decir es una toma de fotografía obligatoria 
&#160; 
Y cuyo mensaje de validación de obligatoriedad es 
 lbl_salida_almacen_vm ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_salida_almacen_vm )&#160; 
 “ Antes de salir del punto de donación debes tomar una fotografía del documento de salida del almacen ” 
&#160; 
Al tomar la fotografía el sistema deberá realizar el siguiente registro 
&#160; 
 https&#58;//dev.datagov .eatcloud.info/crd/eatcloud/?_tabla=eatc_photo_registry&amp;_operacion= insert &amp;eatc_code= &#123;&#123; codigo_foto &#125;&#125; &amp;eatc_cua_master= mexico &amp;eatc_cua= iconn &amp;eatc_doma_code= FSA001009R70 &amp;eatc_dona_header_code=iconnaad4a6bfad62eb53425894a928f2b56320250110145341&amp;eatc_label= lbl_salida_almacen &amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_photo= &#123;&#123; ruta_foto &#125;&#125; &#160; 
&#160; 
 Ejemplo 2 &#58; anuncio “ postobonp13521220250102093958420 ” cua_master “ abaco ” en ambiente “ dev ” 
El sistema, para la donación en cuestión deberá realizar la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= postobonp13521220250102093958420 &amp;_cmp=eatc-code,eatc_cua_master,eatc-donor,eatc-donation_manager_code &#160; 
Dado que la respuesta es&#58; 
&#123; 
 eatc-code &#58; &quot;postobonp13521220250102093958420&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 eatc-donor &#58; &quot;postobon&quot;, 
 eatc-donation_manager_code &#58; &quot;900082682&quot; 
&#125; 
El sistema deberá realizar la siguiente consulta (sabiendo que está en el punto específico de la APP&#58; lbl_registrar_salida_pod )&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master= abaco &amp;eatc_cua= postobon &#160; 
Como no obtiene respuesta, entonces realiza esta consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_validation_point= lbl_registrar_salida_pod &amp;eatc_cua_master= abaco &amp;eatc_cua= _* &#160; 
&#160; 
Dado que tampoco recibe respuesta, en esta donación específica no se despliega botón de toma de fotografía al salir del punto de donación. 
&#160; 
Toma de fotografía al verificar la donación (lbl_verificar_donacion) 
El sistema, deberá tener un botón, ubicado en este punto del proceso, cuando para una donación específica se hace la verificación detallada, el cual para activarse (es decir, para estar disponible para el usuario) tendrá que hacerse mediante estas consultas, diseñadas para que la funcionalidad dependa inicialmente de la cuenta maestra y de la cuenta usuario. 
&#160; 
El sistema, para la donación en cuestión deberá realizar la siguiente consulta&#58;&#160; 
 &#123;&#123; URL_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers? eatc-code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp= eatc-code, eatc_cua_master , eatc-donor , eatc-donation_manager_code 
&#160; 
Con los datos obtenidos, y sabiendo que la ubicación programada en la app es “ la verificación detallada de la donación &quot; o “ lbl_verificar_donacion ”, entonces el sistema deberá realizar la siguiente consulta&#58; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_photos?eatc_validation_point= lbl_verificar_donacion &amp;eatc_cua_master=&#123;&#123; eatc_dona_headers. eatc_cua_master &#125;&#125; &amp;eatc_cua=&#123;&#123; eatc_dona_headers. eatc-donor &#125;&#125; 
Si no obtiene respuesta, entonces realiza esta consulta&#58; 
&#123;&#123;URL_datagov&#125;&#125;/api/eatcloud/eatc_photos?eatc_validation_point= lbl_verificar_donacion &amp;eatc_cua_master=&#123;&#123; eatc_dona_headers. eatc_cua_master &#125;&#125; &amp;eatc_cua=_* 
Si no obtiene resultado, entonces la funcionalidad (el botón para tomar la fotografía) no se despliega. &#160;En caso contrario el sistema deberá entender lo siguiente&#58; 
&#160; 
El label del botón para tomar la fotografía será 
 &#123;&#123;eatc_photos. eatc_label &#125;&#125; 
&#160; 
La validación de obligatoriedad de toma de la foto será 
 &#123;&#123;eatc_photos. eatc_mandatory &#125;&#125;&#58; cuando reciba “y”, la foto será obligatoria, y en su defecto no. 
&#160; 
El mensaje de validación de obligatoriedad de toma de la foto será (que se despliega si no se toma la foto en el punto definido y no permitirá seguir adelante) 
 &#123;&#123;eatc_photos. eatc_validation_message &#125;&#125; 
&#160; 
 Mediante el botón respectivo, el sistema despliega la funcionalidad que permite seleccionar una foto de la galería o abrir la cámara para tomar una fotografía. 
&#160; 
 El usuario podrá seleccionar o tomar una fotografía, acto seguido el sistema invocará el servicio para subir fotografías al sistema, y una vez esté en la nube, capturará la ruta en la cual quedó almacenada en el servidor &#123;&#123; ruta_foto &#125;&#125; y el código con el cual se identifica la fotografía &#123;&#123; codigo_foto &#125;&#125; 
 &#123;&#123; URL_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_photo_registry&amp;_operacion= insert &amp;eatc_code= &#123;&#123; codigo_foto &#125;&#125; &amp;eatc_cua_master=&#123;&#123;eatc_dona_headers. eatc_cua_master &#125;&#125;&amp;eatc_cua=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc_doma_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;eatc_label= lbl_verificar_donacion &amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_photo= &#123;&#123; ruta_foto &#125;&#125; 
&#160; 
 Ejemplo 1 &#58; anuncio “ exito3520250219075007675 ” cua_master “ abaco ” en ambiente “ dev ” 
El sistema, para la donación en cuestión deberá realizar la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code= exito3520250219075007675 &amp;_cmp=eatc-code,eatc_cua_master,eatc-donor,eatc-donation_manager_code &#160; 
Dado que la respuesta es&#58; 
&#123; 
 eatc-code &#58; &quot;exito3520250219075007675&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 eatc-donor &#58; &quot;exito&quot;, 
 eatc-donation_manager_code &#58; &quot;811018073&quot; 
&#125; 
Con los datos obtenidos, y sabiendo que la ubicación programada en la app es “ la verificación detallada de la donación &quot; o “ lbl_verificar_donacion ”, entonces el sistema deberá realizar la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_photos?eatc_validation_point= lbl_verificar_donacion &amp;eatc_cua_master= abaco &amp;eatc_cua= exito &#160; 
Como obtiene la siguiente respuesta&#58; 
&#123; 
 _id &#58; &quot;3&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 eatc_cua &#58; &quot;exito&quot;, 
 eatc_label &#58; &quot;lbl_foto_donacion&quot;, 
 eatc_mandatory &#58; &quot;y&quot;, 
 eatc_validation_point &#58; &quot;lbl_verificar_donacion&quot;, 
 eatc_validation_message &#58; &quot;lbl_foto_donacion_vm&quot; 
&#125; 
Entonces despliega un botón&#58; 
&#160; 
Cuyo label es 
 lbl_foto_donacion ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_foto_donacion ) 
 “ Foto de la donación ” 
&#160; 
Cuya obligatoriedad de validación o toma de fotografía es 
 “y”, es decir es una toma de fotografía obligatoria 
&#160; 
Y cuyo mensaje de validación de obligatoriedad es 
 lbl_foto_donacion_vm ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_foto_donacion_vm )&#160; 
 “ Antes hacer la verificación detallada, debes tomar una fotografía de la donación ” 
&#160; 
Al tomar la fotografía el sistema deberá realizar el siguiente registro 
&#160; 
 https&#58;//dev.datagov .eatcloud.info/crd/eatcloud/?_tabla=eatc_photo_registry&amp;_operacion= insert &amp;eatc_code= &#123;&#123; codigo_foto &#125;&#125; &amp;eatc_cua_master= abaco &amp;eatc_cua= exito &amp;eatc_doma_code= 811018073 &amp;eatc_dona_header_code= exito3520250219075007675 &amp;eatc_label= lbl_verificar_donacion &amp;eatc_datetime=&#123;&#123; datetime_stamp &#125;&#125;&amp;eatc_date=&#123;&#123; date_stamp &#125;&#125;&amp;eatc_photo= &#123;&#123; ruta_foto &#125;&#125; 
&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 76dfe0bd-8225-4fca-a5a1-376dcbc28602 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 62f11fed-e560-43ed-a6ae-e0c46fc5e136 
 2025-10-15T04:35:22.2236824Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"e07d2174-037e-4fb0-972c-e9ad018d5dc8","SequenceId":229,"FluidContainerCustomId":"a3b2d159-497d-4be5-9536-79ba8a9e13d5","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 TOMA DE FOTOGRAFÍAS