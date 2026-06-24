# configuración-donantes-no-negociados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 PROTOTIPO UI 

 CONFIGURACIN DONANTES DE NO NEGOCIADOS 
 class=lbl_config_donantes_no_negociados (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_donantes_no_negociados)  

 Descripcin: 
 class=lbl_config_donantes_no_negociados_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_donantes_no_negociados_desc)  

 Con esta funcionalidad podrs determinar cuentas que realizarn donaciones desde puntos de donacin de terceros (no negociados). 

 CASO DE USO 

 Actores: 
 Usuario EatCloud, sistema datagov_eatcloud. 

 Precondiciones: 
  Deben existir en el sistema cuentas usuario (cua_user) previamente registradas con licencia rescate impacto.  Debe existir un usuario vlido del BO datagov_eatcloud ( https://datagov.eatcloud.info/bo/eatcloud ) logueado en el sistema, ( crear el campo " eatc_cua. eatc_nng_donor " ). 

 Flujo Principal (Secuencia Normal de Eventos): 

 Paso 1: 
 El usuario ingresa al men de "Configuracin de donantes" del grupo de elementos de men "No negociados" 

 Paso 2:   (precondicin: crear el campo " eatc_cua. eatc_nng_donor " ): 
 El sistema le despliega un selector mltiple de cuentas de usuario (cua_user) que tienen licencia impacto (y que no tienen configurado como "y" el campo eatc_cua. eatc_nng_donor ). 

 Selector mltiple de cuentas:  
 Placeholder : class=lbl_selecciona_cuentas (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_cuentas) "Selecciona la(s) cuenta(s) que deseas configurar" 
 Llamado para construccin del selector : {{URL_datagov}}/api/eatcloud/eatc_cua?type=impacto&eatc_nng_donor=!y&_cmp=name,eatc_cua_master ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-7a216299-169e-491c-8e43-6d4c953d72c8 )   

 Paso 3:  
 El usuario selecciona una o varias cuentas usuario desplegadas 

 Paso 4.1:  
 Cuando el usuario realiza su primera seleccin, el sistema muestra el botn "Configurar donante de no negociados" 

 Botn:  
 class=lbl_configurar_donante_no_negociados (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configurar_origen_no_negociados) "Configurar donante no negociados" 

 Paso 4.2:  
 El usuario oprime el botn Configurar donante de no negociados 

 Paso 5  (precondicin: crear el campo " eatc_cua. eatc_nng_donor " ): 
  El sistema coloca en el campo eatc_cua. eatc_nng_donor un y de las cuentas seleccionadas 

 Llamado ejemplo para la creacin del registro : {{URL_datagov}}/crd/eatcloud/?_tabla=eatc_cua&_operacion=update&eatc_nng_donor=y&WHEREname={{cua_user}}   ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-e454ae2d-1888-4438-96a9-a056fad88026 )   

 Paso 6:  
 El sistema guarda un log del usuario que hizo el(los) cambio(s) y la fecha y hora en que se hicieron. 

 Paso 7:  
 El sistema verifica que la configuracin haya quedado correctamente realizada y posteriormente despliega un mensaje de xito La configuracin fue correctamente realizada 

 Mensaje:  
 class=lbl_configuracion_exitosa (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configuracion_exitosa) "La configuracin fue correctamente realizada" 

 Paso 8  (Que por lo menos exista una eatc_cua. eatc_nng_donor =y): 
  El sistema despliega una lista donde relaciona las cuentas que han sido configuradas como orgenes de no negociados 

 Llamado ejemplo para la creacin del la tabla : {{URL_datagov}}/api/eatcloud/eatc_cua?eatc_nng_donor=y&_cmp=name,eatc_cua_master,eatc_nng_donor ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-16f0364c-fee1-408b-aa10-b133aa132464 )   

 Primera columna: cua_user: coloca informacin contenida en eatc_cua. name 
 Segunda columna: cua_master: coloca informacin contenida en eatc_cua. eatc_cua_master 
 Tercera columna: eatc_mmg_donor: coloca informacin contenida en eatc_cua. eatc_nng_donor 

 Paso 9 (Que por lo menos exista una eatc_cua. eatc_nng_donor =y): 
 El sistema despliega una casilla de seleccin por cada registro, con la oportunidad de seleccionarlos todos y posee un botn "Borrar" que permitir realizar una accin bulk de borrado del registro eatc_cua. eatc_nng_donor 

 Botn:  
 class=lbl_borrar ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_borrar ) "Borrar" 

 Paso 10 (Que por lo menos exista una eatc_cua. eatc_nng_donor =y): 
 El usuario podr seleccionar uno o varios registros, para luego oprimir el botn "Borrar" 

 Paso 11: 
 El sistema borrar el dato que se encuentra en el campo eatc_cua. eatc_nng_origin  

 Llamado ejemplo para el borrado del registro : {{URL_datagov}}/crd/eatcloud/?_tabla=eatc_cua&_operacion=update&eatc_nng_donor=&WHEREname={{cua_user}} ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-65c80a50-9051-4073-8f53-b01d24839784 )   

 y una vez que lo realize de manera adecuada (guardando un log de la operacin), desplegar un mensaje de xito. 

 class=lbl_configuracion_exitosa ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configuracion_exitosa ) "La configuracin fue correctamente realizada" 

 Flujos Alternativos (Rutas alternativas al Flujo Principal): 
 Un usuario podr entrar a la vista solamente a crear o a borrar registros (no es necesario que realice todo el flujo especificado para la operacin de un caso de uso exitoso) 

 Postcondiciones: 
  Cuenta usuario con el campo eatc_cua. eatc_nng_donor : y . Log del cambio guardado. 

 Reglas de Negocio:   
 Solo podrn configurarse como origen de no negociado, cuentas con licencia rescate impacto 

 Requisitos Especiales:  
 No aplica 

 Prioridad:  
 Alta 

 Frecuencia de Uso:  
 Cada vez que se desee configurar un donante de no negociados (espordico) 

 Notas y Problemas:  
 Se debe crear el campo eatc_cua. eatc_nng_donor como boleano (se brindan las siguientes URLs para facilitar la creacin, pero no se han accionado). 

 Creacin entorno de pruebas: 
 https://dev.datagov.eatcloud.info/optb/eatcloud/newcampo?_tabla=eatc_cua&new_field= eatc_nng_donor 

 Creacin entorno produccin: 
 https://datagov.eatcloud.info/optb/eatcloud/newcampo?_tabla= eatc_cua &new_field= eatc_nng_donor 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-donantes-no-negociados%2F3798941514-config_donantes_nng_1.jpg&ow=1136&oh=579, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-donantes-no-negociados%2F3798941514-config_donantes_nng_1.jpg&ow=1136&oh=579 

 872.000000000000 

 CONFIGURACIN DONANTES NO NEGOCIADOS