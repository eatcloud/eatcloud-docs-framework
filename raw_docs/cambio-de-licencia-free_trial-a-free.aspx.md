# cambio-de-licencia-free_trial-a-free.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Corrida del proceso: 
 Es un proceso que debe correrse todos los das en la noche y el cronjob se debe  

 Consulta de vigencia de la licencia free_trial:  
 El sistema, mediante la siguiente consulta se obtiene el dato eatc_days 
 https://datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code= free_trial   

 El dato obtenido (a 2 de diciembre de 2020: 15 ) es el periodo de tiempo que hay que evaluar desde la creacin de la cuenta, para establecer si la licencia cambia de " free_trial " a " free ", para hacer dicha evaluacin el sistema realiza la siguiente consulta 

 Consulta de cuentas:  
 El sistema debe consultar aquellos clientes cuyo tipo de licencia sea "free_trial" 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua?type=free_trial 

 Sobre las cuentas que arroje la consulta, el sistema debe  

 Comparaciones (para cambiar el tipo de licencia):  
 Posteriormente debe comparar el campo " creation_datetime ", con la fecha y hora actual.  Si la diferencia en das entre la fecha y hora actual y la fecha de creacin de la cuenta es superior a eatc_types_of_licenses. eatc_days se deben ejecutar las siguientes acciones:  

 Accin 1: Actualizacin de la informacin de la cuenta 
 Al liberar el  anuncio de donacin se debe actualizar la siguiente informacin: 
 type : debe cambiar a " free ". 

 Actualizacin del tipo "free" :  
 https://datagov.eatcloud.info/crd/eatcloud /?_tabla= eatc_cua &_operacion=update & type = free &WHERE eatc_cua ={{eatc_cua. name }} 

 Accin 2: registro en el historial de tipos de licencia por cuenta. 
 Se debe registrar el estado "announced" procurando incorporar la informacin del adjudicatario al cual se le elimin la adjudicacin, en el campo ( eatc-log )  
 eatc_cua ={{eatc_cua. name }} 
 type = free 
 eatc_datetime ={{timestamp en formato AAAA-MM-DD HH:MM:SS}} 
 eatc_log ="EatCloud cambi el tipo de licencia de la cuenta porque despus de {{eatc_types_of_licenses. eatc_days }} das no se ha adquirido una licencia "hero"." 

 Utilizando el API el registro sera algo como lo siguiente 

 Registro del tipo "free" :  
 https://datagov.eatcloud.info/crd/eatcloud /?_tabla= eatc_cua_type_history &_operacion=insert& eatc_cua ={{eatc_cua. name }}& type = free & eatc_datetime ={{timestamp en formato AAAA-MM-DD HH:MM:SS}}& eatc_log ="EatCloud cambi el tipo de licencia de la cuenta porque despus de {{eatc_types_of_licenses. eatc_days }} das no se ha adquirido una licencia "hero"." 

 Accin 2:  Llamado al servicio de creacin de configuracin de funcionalidades en AllPods (para cambiar a la configuracin de la cuenta free) 

 El sistema debe realizar tambin el siguiente llamado al servicio desarrollado para este fin (dado que el mismo implementa el borrado previo de los registros creados para la cuenta en cuestin). 

 {{URL_entorno_donantes}}/casebd/allpods/pods_default_features?eatc-cua={{ _DOM .cua_user }}&plan= free 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CAMBIO DE LICENCIA "FREE_TRIAL" A "FREE"