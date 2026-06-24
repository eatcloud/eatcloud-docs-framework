# configuración-puntos-de-donación-no-negociados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 PROTOTIPO UI 

 CONFIGURACIN PUNTOS DE DONACIN NO NEGOCIADOS 
 class=lbl_config_pods_no_negociados https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_pods_no_negociados )  

 Descripcin: 
 class=lbl_config_pods_no_negociados_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_pods_no_negociados_desc )   

 Con esta funcionalidad podrs determinar, para los donantes de no negociados, los puntos desde los cuales se despacha su mercanca donada. 

 CASO DE USO 

 Actores: 
 Usuario EatCloud, sistema datagov_eatcloud, servicio de creacin de puntos de donacin no negociados. 

 Precondiciones: 
 Deben existir en el sistema cuentas usuario ( cua_user ) previamente configuradas como origen de no negociados y donantes de no negociados.  Debe existir un usuario vlido del BO datagov_eatcloud ( https://datagov.eatcloud.info/bo/eatcloud ) logueado en el sistema. 

 Flujo Principal (Secuencia Normal de Eventos): 

 Paso 1: 
 El usuario ingresa al men de configuracin de puntos de donacin de no negociados. 

 Paso 2: 
 El sistema le despliega un selector nico de cuentas de usuario (cua_user) que son donantes de no negociados ( eatc_cua. eatc_nng_donor =y ) 

 Selector nico de cuentas:  
 Placeholder : class=lbl_selecciona_cuenta ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_donante_nng ) "Selecciona el donante de no negociados que  deseas configurar" 
 Llamado para construccin del selector : {{URL_datagov}}/api/eatcloud/eatc_cua? eatc_nng_donor =y&_cmp=name,eatc_cua_master ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-ff539db1-85dd-452a-8c47-71ddf5ab6d06 )  
 El sistema guarda el valor eatc_cua. eatc_cua_master {{cua_master}} para la creacin del prximo selector. 

 Paso 3: 
 El usuario selecciona una cuenta usuario ( cua_user ) donante de no negociados. 

 El sistema guarda el valor (o los valores) seleccionado(s) por el usuario, correspondientes a eatc_cua. eatc_cua_master en la variable {{cua_master}} para la creacin del prximo selector. 

 Paso 4: 
 El sistema despliega un selector mltiple de cuentas de usuario ( cua_user ) con orgenes de no negociados ( eatc_cua. eatc_nng_origin = y ) 

 Selector mltiple de cuentas:  

 Placeholder : class=lbl_selecciona_cua_origen_nng ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_cua_origen_nng ) Selecciona la(s) cuenta(s) origen de no negociados a asociar 

 Llamado para construccin del selector : {{URL_datagov}}/api/eatcloud/eatc_cua? eatc_nng_origin =y&eatc_cua_master= {{cua_master}} &_cmp=name,eatc_cua_master ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-247567b8-55b8-416e-a84e-882a0242b7ed ) 

 Paso 5: 
 El usuario selecciona una o varias cuentas usuario origen de no negociados. 

 El sistema guarda el valor (o los valores) seleccionado(s) por el usuario, correspondientes a eatc_cua. name en la variable {{cua_user}} para futuras selecciones. 

 Paso 6: 
 El sistema despliega un selector mltiple de ciudades 

 Selector mltiple de ciudades:  

 Placeholder : class=lbl_selecciona_ciudades ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_ciudades ) Selecciona la(s) ciudad(es) 

 Llamado para construccin del selector: {{URL_donantes}} /api/ allpods /eatc_pods?eatc-cua= {{cua_user}} &_distinct= eatc-city   ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-247567b8-55b8-416e-a84e-882a0242b7ed )  

 Paso 7: 
 El usuario selecciona una o varias ciudades. 

 El sistema guarda el valor (o los valores) seleccionado(s) por el usuario, correspondientes a eatc_pods. eatc-city en la variable {{eatc-city}} para futuras selecciones. 

 Paso 8: 
 El sistema despliega una lista de los puntos de donacin activos que cumplen con los anteriores criterios de filtro (con informacin, de su cdigo, nombre, ciudad, tipologas a y b, y estado de actividad).  La lista tiene un buscador que permite filtrar aun ms los resultados.  La lista tiene casillas de seleccin mltiple, que permiten al usuario seleccionar varios de los puntos de donacin que aparecen.  Tambin posee una casilla para seleccionar todos los puntos que aparecen en la lista.  

 Listado de puntos de donacin:  
 Llamado para construccin de la lista: {{URL_donantes} }/api/allpods/eatc_pods?eatc-cua= {{cua_user}} &eatc-city= {{eatc-city}} &eatc_active=y&_cmp=eatc-id,eatc-name,eatc-cua_master,eatc-cua,eatc-city,eatc-adress,eatc-typology_a,eatc-typology_b,eatc_active   ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-700a1bf9-178a-4684-a548-9ac415fb9679 )  
 Primera columna: pod_id : coloca informacin contenida en eatc_pods. eatc-id 
 Segunda  columna: pod_name : coloca informacin contenida en eatc_pods. eatc-name 
 Tercera columna: cua_master : coloca informacin contenida en eatc_pods. eatc-cua_master 
 Cuarta columna: cua_user : coloca informacin contenida en eatc_pods. eatc-cua 
 Quinta columna: Ciudad: coloca informacin contenida en eatc_pods. eatc-city 
 Sexta coluna: Direccin: coloca informacin contenida en eatc_pods. eatc-adress 
 Septima columna: Tip A: coloca informacin contenida en eatc_pods. eatc-typology_a 
 Octava colummna: Tip B: coloca informacin contenida en eatc_pods. eatc-typology_a 

 Otro label de la interfaz:  
 Placeholder Buscador : class=lbl_buscar ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_buscar )  " Buscar " 

 Paso 9: 
 El usuario podr seleccionar uno o varios puntos de donacin de no negociados. 

 El sistema guarda el valor (o los valores) seleccionado(s) por el usuario, correspondientes a eatc_pods. eatc-city en la variable {{eatc_pods_nng}} para futuras acciones. 

 Paso 10: 
 Al realizar una seleccin, el sistema despliega el botn " Asociar Punto NNG . 

 Botn: Asociar Punto NNG : class=lbl_asociar_punto_nng ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_asociar_punto_nng ) " Asociar punto NNG " 

 Paso 11: 
 El usuario oprime el botn Asociar Punto de NNG y al hacerlo obtiene informacin del la cuenta donante de no negociados y los respectivos puntos seleccionados. 

 El sistema guarda el valor (o los valores) seleccionado(s) por el usuario, correspondientes a eatc_pods. eatc-id en la variable {{eatc_pods_nng}} y sus respectivos eatc_pods. eatc-cua en la variable {{eatc_cua_origin_nng}} para futuras acciones. 

 Paso 12: 
 Con esta informacin el sistema invoca ( documentacin API Pblica ) al servicio configpodsnng : Servicio para configurar puntos de donacin de no negociados . 

 Paso 13: 
 Ante una respuesta de "success" el servicio muestra el mensaje al usuario:  

 class=lbl_configuracion_exitosa ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configuracion_exitosa ) "La configuracin fue correctamente realizada" 

 Flujos Alternativos (Rutas alternativas al Flujo Principal): 
 No aplica 

 Postcondiciones: 

 En cuenta de usuario origen de no negociados: 

 Configuracin de cuenta en (eatcloud/eatc_cua) como multiple_donors=si   
 Creacin (de ser necesario) del object store " eatc_multiple_donors_info " 
 Creacin (de ser necesario) de los campos " eatc_cua_user", "eatc_default " en el objectstore " eatc_multiple_donors_info " 
 Configuracin  (de ser necesario) del valor por defecto en los datos de multiples NIT (con los datos del propio origen de no negociados). 

 Configuracin del NIT del donante como un dato en la persistencia " eatc_multiple_donors_info ". 

 En Allpods 

 Configuracin de los puntos de donacin de No Negociados en eatc_pods_cua_donor_nng 

 En la cuenta donante de no negociados 

 Creacin (de ser necesario) del campo " eatc_cua_origin", en el objectstore " eatc_pods " 
 En la respectiva persistencia de puntos de de donacin ( eatc_pods ) se registran los puntos de donacin de no negociados. 

 Reglas de Negocio:   
 Solo podrn configurarse como origen de no negociado, cuentas con licencia rescate impacto y puntos de donacin activos. 

 Requisitos Especiales:  
 No aplica 

 Prioridad:  
 Alta 

 Frecuencia de Uso:  
 Cada vez que se desee configurar un donante de no negociados (espordico) 

 Notas y Problemas:  
 Para implementar el caso de uso se deber crear un API pblica y un Servicio de configuracin de puntos.  Se deber evaluar cmo implementar dicho servicio para manejar el registro bulk de puntos, ya que en la documentacin se presentan guas como ejemplo pero para la creacin de un punto de donacin a la vez. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-puntos-de-donaci%C3%B3n-no-negociados%2F1081753211-config_puntos_nng_1.jpg&ow=1103&oh=550, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-puntos-de-donaci%C3%B3n-no-negociados%2F1081753211-config_puntos_nng_1.jpg&ow=1103&oh=550 

 876.000000000000 

 CONFIGURACIN PUNTOS DE DONACIN NO NEGOCIADOS