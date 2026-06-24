# configuración-orígenes-no-negociados.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 PROTOTIPO UI 

 CONFIGURACIÓN ORÍGENES NO NEGOCIADOS 
 class=lbl_config_origenes_no_negociados https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_origenes_no_negociados )  

 Descripción: 
 class=lbl_config_origenes_no_negociados_desc ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_config_origenes_no_negociados_desc )  

 Con esta funcionalidad podrás determinar cuentas desde las cuales se originan donaciones de no negociados, es decir, donaciones que tienen un donante diferente al donante al cual pertenecen los puntos de donación desde el cuál se realiza la donación. 

 CASO DE USO 

 Actores: 
 Usuario EatCloud, sistema datagov_eatcloud. 

 Precondiciones: 
  Deben existir en el sistema cuentas usuario (cua_user) previamente registradas con licencia rescate “impacto” y en la vertical “retail”.  Debe existir un usuario válido del BO datagov_eatcloud ( https://datagov.eatcloud.info/bo/eatcloud ) logueado en el sistema,  ( crear el campo eatc_nng_origin ). 

 Flujo Principal (Secuencia Normal de Eventos): 

 Paso 1: 
 El usuario ingresa al menú de configuración de orígenes de no negociados 

 Paso 2:  (precondición: crear el campo eatc_nng_origin ): 
 El sistema le despliega un selector múltiple de cuentas de usuario (cua_user) que tienen licencia “impacto” y vertical “retail” (y que no tienen configurado como " y " el campo eatc_cua.eatc_nng_origin ). 

 Selector múltiple de cuentas:  
 Placeholder : class=lbl_selecciona_cuentas ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_cuentas ) "Selecciona la(s) cuenta(s) que deseas configurar" 
 Llamado para construcción del selector : {{URL_datagov}}/api/eatcloud/eatc_cua?vertical=retail&type=impacto&eatc_nng_origin=!y&_cmp=name,eatc_cua_master ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-7c181f50-25bc-4401-b156-6e20ea1584cd )  

 Paso 3:  
 El usuario selecciona una o varias cuentas usuario desplegadas 

 Paso 4.1:  
 Cuando el usuario realiza su primera selección, el sistema muestra el botón "Configurar origen de no negociados" 

 Botón:  
 class=lbl_configurar_origen_no_negociados ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configurar_origen_no_negociados ) "Configurar origen no negociados" 

 Paso 4.2:  
 El usuario oprime el botón “Configurar origen de no negociados” 

 Paso 5  (precondición: crear el campo eatc_nng_origin ): 
  El sistema coloca en el campo eatc_cua. eatc_nng_origin un “y” de las cuentas seleccionadas 

 Llamado ejemplo para la creación del registro : {{URL_datagov}}/crd/eatcloud/?_tabla=eatc_cua&_operacion=update&eatc_nng_origin=y&WHEREname={{cua_user}}   ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-5951138a-b954-4239-b245-87de16b2a635 )  

 Paso 6:  
 El sistema guarda un log del usuario que hizo el(los) cambio(s) y la fecha y hora en que se hicieron. 

 Paso 7:  
 El sistema verifica que la configuración haya quedado correctamente realizada y posteriormente despliega un mensaje de éxito “La configuración fue correctamente realizada” 

 Mensaje:  
 class=lbl_configuracion_exitosa ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configuracion_exitosa ) "La configuración fue correctamente realizada" 

 Paso 8  (Que por lo menos exista una eatc_cua. eatc_nng_origin =y): 
  El sistema despliega una lista donde relaciona las cuentas que han sido configuradas como orígenes de no negociados 
 Llamado ejemplo para la creación del la tabla : {{URL_datagov}}/api/eatcloud/eatc_cua?eatc_nng_origin=y&_cmp=name,eatc_cua_master,eatc_nng_origin ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-314145e6-e27c-45d5-9bdb-7810a3412731 )  
 Primera columna: cua_user: coloca información contenida en eatc_cua. name 
 Segunda columna: cua_master: coloca información contenida en eatc_cua. eatc_cua_master 
 Tercera columna: eatc_mmg_origin: coloca información contenida en eatc_cua. eatc_nng_origin 

 Paso 9 (Que por lo menos exista una eatc_cua. eatc_nng_origin =y): 
  El sistema despliega una casilla de selección por cada registro, con la oportunidad de seleccionarlos todos y posee un botón "Borrar" que permitirá realizar una acción bulk de borrado del registro eatc_cua. eatc_nng_origin 

 Botón:  
 class=lbl_borrar ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_borrar ) "Borrar" 

 Paso 10 (Que por lo menos exista una eatc_cua. eatc_nng_origin =y): 
 El usuario podrá seleccionar uno o varios registros, para luego oprimir el botón "Borrar" 

 Paso 11: 
 El sistema borrará el dato que se encuentra en el campo eatc_cua. eatc_nng_origin  

 Llamado ejemplo para el borrado del registro : {{URL_datagov}}/crd/eatcloud/?_tabla=eatc_cua&_operacion=update&eatc_nng_origin=&WHEREname={{cua_user}} ( https://crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/request/11174160-eaa734ee-720a-439f-b85e-88ce8ff623e4 )   

 y una vez que lo realize de manera adecuada (guardando un log de la operación), desplegará un mensaje de éxito. 

 class=lbl_configuracion_exitosa ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_configuracion_exitosa ) "La configuración fue correctamente realizada 

 Flujos Alternativos (Rutas alternativas al Flujo Principal): 
 Un usuario podrá entrar a la vista solamente a crear o a borrar registros (no es necesario que realice todo el flujo especificado para la operación de un caso de uso exitoso) 

 Postcondiciones: 
  Cuenta usuario con el campo “eatc_cua. eatc_nng_origin ” : “ y ” . Log del cambio guardado. 

 Reglas de Negocio:   
 Solo podrán configurarse como origen de no negociado, cuentas de la vertical “retail” y con licencia rescate “impacto” 

 Requisitos Especiales:  
 No aplica 

 Prioridad:  
 Alta 

 Frecuencia de Uso:  
 Cada vez que se desee configurar un origen de no negociados (esporádico) 

 Notas y Problemas:  
 Se debe crear el campo eatc_cua.eatc_nng_origin como boleano (se brindan las siguientes URLs para facilitar la creación, pero no se han accionado). 

 Creación entorno de pruebas: 
 https://dev.datagov.eatcloud.info/optb/eatcloud/newcampo?_tabla=eatc_cua&new_field= eatc_nng_origin 

 Creación entorno producción: 
 https://datagov.eatcloud.info/optb/eatcloud/newcampo?_tabla= eatc_cua &new_field= eatc_nng_origin 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-or%C3%ADgenes-no-negociados%2F2852123763-config_origenes_nng_1.jpg&ow=1139&oh=563, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fconfiguraci%C3%B3n-or%C3%ADgenes-no-negociados%2F2852123763-config_origenes_nng_1.jpg&ow=1139&oh=563 

 868.000000000000 

 CONFIGURACIÓN ORÍGENES NO NEGOCIADOS