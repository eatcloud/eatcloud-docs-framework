# correo-donantes-gestión-donaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Los donantes podrn configurar en su plataforma BO (tipo de usuario A) correos electrnicos a los cuales se les enva un informe con los anuncios de donacin en un determinado estado, en dos cortes diarios: finalizando la maana (11:50) y finalizando la tarde (17:50).  Si el desarrollador estima que el proceso para enviar estos correos en los horarios determinados puede comprometer la salud del servidor, se le encarga determinar dos horarios alternativos similares seleccionados teniendo en mente evitar posibles sobrecargas. 

 Se debern configurar dos procesos que se corran en los horarios establecidos y que leyendo la informacin de configuracin respectiva, generen los correos que han sido solicitados por los donantes. 

 Determinacin de los correos a los cuales se les enviar informacin en cada uno de los cortes 

 El sistema debe determinar, para cada uno de los cortes, que correos s: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_state_change_emails?eatc_send_time={{eatc_send_time}} 

 De con los datos que arroja la anterior consulta, se debe realizar un select distinct sobre el campo " eatc_email " para determinar los correos electrnicos a los cuales hay que enviar informacin en el corte particular 

 Ejemplo: ambiente de pruebas 
 El sistema debe determinar a qu correos electrnicos les debe enviar informacin en el corte  
 de final de la maana, por lo tanto realiza la siguiente consulta: 

 https://dev.datagov.eatcloud.info/api/eatcloud/eatc_state_change_emails?eatc_send_time=11:50:00 

 elect distinct sobre el campo " eatc_email " se determina que deber enviar correos electrnicos a jdr@eatcloud.com y jdc@eatcloud.com   

 CONSULTA PARA EXTRAER LOS DATOS PARA ENVIAR EL INFORME: 

 NOTA IMPORTANTE: todos los labels de los cuales se habla abajo, estn registrados para la plataforma BO Donantes y en algunos casos Datagov Cuentas.  De acuerdo a las determinaciones tomadas por el desarrollador para la ubicacin del desarrollo (que se sugiere se ubique en datagov en la cuenta eatcloud para que tenga caracter general), se debern ajustar las etiquetas (e se debern tomar las que estn registradas en BO Donantes) 

 Con cada uno de los correos electrnicos obtenidos en la anterior consulta, se establece a que cuenta maestra ( eatc_state_change_emails. eatc_cua_master ) y la cuenta usuario ( eatc_state_change_emails. eatc_cua_user ) a la cual pertenecen pertenecen y los estados (que pueden ser un array: eatc_state_change_emails. eatc_state ) sobre los cuales se debe generar informacin: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_state_change_emails? eatc_email ={{ eatc_email }} 

 Tomando estos datos, se determinan los anuncios sobre los cuales se enviar el informe. 

 {{URL_entorno_donantes}}/api/{{ eatc_state_change_emails. eatc_cua_master }}/eatc_dona_headers?eatc-donor={{ eatc_state_change_emails. eatc_cua_user }}&eatc-state={{array: eatc_state_change_emails. eatc_state }} 

 Para aquellos anuncios cuyo estado sea " recieved " se deben filtrar aquellos cuya " eatc-receipt_datetime ", se encuentre dentro de la ltima semana 
 Para aquellos anuncios cuyo estado sea " pre-certified " se deben filtrar aquellos cuya " eatc-pre_certification_datetime ", se encuentre dentro de la ltima semana 
 Para aquellos anuncios cuyo estado sea " certified " se deben filtrar aquellos cuya " eatc-certification_datetime ", se encuentre dentro de la ltima semana 

 Y se debe pintar un informe que contenga la siguiente informacin: 

 Informacin de encabezado 
 Se muestra una vez al inicio del informe. 

 Fecha y hora de generacin del informe 
 label: class=" lbl_fecha_hora_generacion_informe " 
 La informacin se toma de: un timestamp de la fecha y hora de la generacin del presente informe 

 Donante 
 label: class=" lbl_donante " 
 La informacin se toma de: eatc_dona_headers .eatc-donor 

 Tabla de anuncios 

 Introduccin: 
 Antes de la tabla se deber incorporar el siguiente label 
 label: class=" lbl_gestionar_verificar_anuncios " 

 Tabla: 
 Se ordenar mostrando primero los ms antiguos segn su fecha y hora de publicacin, hasta mostrar por ltimo el ms reciente. Los siguientes datos se mostrarn en una tabla que contendr las siguientes columnas 

 Cdigo del anuncio 
 label: class=" lbl_codigo_anuncio " 
 La informacin se toma de: eatc_dona_headers .eatc-code 

 Identificacin del donante 
 label: class=" lbl_id_donante " 
 La informacin se toma de: eatc_dona_headers .eatc-donor_code 

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

 Beneficiario 
 label: class=" lbl_beneficiario " 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_name 

 Beneficiario direccin 
 label: class=" lbl_direccion_beneficiario " 
 La informacin se toma de: eatc_dona_headers .eatc-donation_manager_adress 

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

 CORREO PARA DONANTES SOBRE LA GESTIN DE DONACIONES