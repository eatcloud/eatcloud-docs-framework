# correo-automático-anuncios-pendientes-de-gestión.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Con el nimo de informar de manera automatizada a los bancos de alimentos, sobre los anuncios que requieren de su gestin, se generar los das martes, un correo electrnico a diferentes actores de la plataforma que contenga informacin para promover acciones con respecto a las donaciones que estn pendientes de gestin por parte de las organizaciones, de la siguiente manera 

 Cada 15 das se genera mail al banco de alimentos (usuario de la plataforma + director del banco de alimentos) 
 Cada 20 das  se genera mail al banco de alimentos (usuario de la plataforma + director del banco de alimentos), con copia a ABACO ingrid + norma + juan carlos  ***NUEVO: Marcela Rodriguez (marcela.rodriguez@eatcloud.com)  *** 

 Determinacin de los anuncios que generan correos  
 El sistema debe determinar, qu anuncios estn pendientes de gestin por parte de los bancos de alimentos, realizando la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00& eatc-donation_manager_typology_b=1&_distinct= eatc-donation_manager_code 

 De con los datos que arroja la anterior consulta, se debe realizar un select distinct sobre el campo " eatc-donation_manager_code " para determinar a los bancos de alimentos que se les enviar un correo particularizado ( array_bancos_alimentos) 

 Ejemplo: entorno de pruebas, cuenta maestra abaco: 
 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00& eatc-donation_manager_typology_b=1&_distinct= eatc-donation_manager_code    

 Determinacin de los correos a los cuales se les debe enviar el informe: 
 Correos gestor de donaciones (siempre) 
 Con cada uno de los datos del array_bancos_alimentos obtenido de la consulta anterior, se deben realizar las siguientes  
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers?identificador_unico_registro={{eatc_dona_headers. eatc-donation_manager_code }} 

 Se toma el dato contenido en eatc_donation_managers. correo_electronico para dirigirle el email.  Adicionamente se realiza la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users?organizacion={{eatc_dona_headers. eatc-donation_manager_code }} 

 Se toma(n) el(los) dato(s) contenido(s) en eatc_users. correo_electronico para dirigirle(s) el email.   

 Correos cuenta maestra (martes cada 20 das) 
 Para determinar los correos que se envan a los funcionarios de la cuenta maestra, se realiza la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/bo_usuarios?eatc_approval_role=logistica_abaco,representante_legal,planeacion_abaco&_distinct=email 

 Se toman los datos contenidos en bo_usuarios. email para dirigirles el email.   

 Ejemplo: entorno de pruebas, cuenta maestra abaco: 
 https://devbeneficiarios.eatcloud.info/api/abaco/bo_usuarios?eatc_approval_role=logistica_abaco,representante_legal,planeacion_abaco&_distinct=email   

 CONSULTA PARA EXTRAER LOS DATOS PARA ENVIAR EL INFORME: 

 NOTA IMPORTANTE: todos los labels de los cuales se habla abajo, estn registrados para la plataforma BO Donantes y en algunos casos Datagov Cuentas.  De acuerdo a las determinaciones tomadas por el desarrollador para la ubicacin del desarrollo (que se sugiere se ubique en datagov en la cuenta eatcloud para que tenga caracter general), se debern ajustar las etiquetas (e se debern tomar las que estn registradas en BO Donantes) 

 Con cada uno de los datos del array_bancos_alimentos obtenido de la consulta de anuncios realizada anteriormente, se realiza la siguiente consulta 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/eatc_dona_headers?eatc-donation_manager_code={{eatc_dona_headers. eatc-donation_manager_code }}&eatc-state=awarded,scheduled,delivered& eatc-receipt_datetime = 0000-00-00%2000:00:00& eatc-donation_manager_typology_b=1 

 Y se debe pintar un informe que contenga la siguiente informacin: 

 Informacin de encabezado 
 Se muestra una vez al inicio del informe. 

 Beneficiario 
 label: class=" lbl_beneficiario " 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Beneficiario direccin 
 label: class=" lbl_direccion_beneficiario " 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_adress 

 Cantidad de anuncios pendientes por verificar 
 label: class=" lbl_cantidad_anuncios_verificar " 
 La informacin se toma del cont que la anterior consulta. 

 Tabla de anuncios pendientes 
 Introduccin: 
 Antes de la tabla se deber incorporar el siguiente label 
 label: class=" lbl_gestionar_verificar_anuncios " 

 Tabla: 
 Se ordenar mostrando primero los ms antiguos segn su fecha y hora de publicacin, hasta mostrar por ltimo el ms reciente. Los siguientes datos se mostrarn en una tabla que contendr las siguientes columnas 

 Cdigo del anuncio 
 label: class=" lbl_codigo_anuncio " 
 La informacin se toma de: eatc_dona_headers .eatc-code 

 Fecha 
 label: class=" lbl_fecha_publicacion " 
 La informacin se toma de: eatc_dona_headers .eatc-publication_date 

 Fecha y hora 
 label: class=" lbl_hora_publicacion " 
 La informacin se toma de: eatc_dona_headers .eatc-publication_datetime 

 Estado 
 label: class=" lbl_estado " 
 La informacin se toma de: eatc_dona_headers .eatc-state 

 Punto de donacin 
 label: class=" lbl_pod " 
 La informacin se toma de: eatc_dona_headers .eatc-pod_name 

 Direccin punto de donacin (OJO ID) 
 label: id=" lbl_direccion_punto_donacion " 
 La informacin se toma de: eatc_dona_headers .eatc-pod_address 

 Ciudad 
 label: class=" lbl_ciudad " 
 La informacin se toma de: eatc_dona_headers .eatc-city 

 Hora de adjudicacin 
 label: class=" lbl_hora_adjudicacion " 
 La informacin se toma de: eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega programada 
 label: class=" lbl_hora_entrega_programada " 
 La informacin se toma de: eatc_dona_headers .eatc-programed_picking_datetime 

 Hora de entrega real: llegada 
 label: class=" lbl_hora_entrega_real_llegada " 
 La informacin se toma de: eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real: salida 
 label: class=" lbl_hora_entrega_real_salida " 
 La informacin se toma de: eatc_dona_headers .eatc-picking_checkout_datetime 

 Fecha recepcin 
 label: class=" lbl_hora_recepcion " 
 La informacin se toma de: eatc_dona_headers .eatc-receipt_datetime 

 Alerta 
 label: class=" lbl_alerta " 
 La informacin se toma de: eatc_dona_headers .eatc-warning 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CORREO AUTOMTICO ANUNCIOS PENDIENTES DE GESTIN