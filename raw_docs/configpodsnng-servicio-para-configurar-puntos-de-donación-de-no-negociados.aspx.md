# configpodsnng-servicio-para-configurar-puntos-de-donación-de-no-negociados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 

 El presente servicio se especifica para entregar una herramienta segura, que le permita a los puntos de donacin (validando correctamente sus credenciales de manera), y si las condiciones de la donacin as lo permiten, liberar las donaciones que por algn motivo no fueron recogidas y aun se pueden aprovechar o fueron canceladas por el sistema pero an son aptas para el consumo humano.  Se debe implementar como un servicio pblico, cuyos endpoints, parmetros de invocacin y respuestas, se detallan en el siguiente documento   

 Documentacin de API pblica para la configuracin de puntos de donacin de no negociados 

 Para evitar duplicidad en la documentacin, la implementacin del servicio deber basarse en dicha documentacin (si se deben hacer cambios se debe intervenir dicha documentacin), y a continuacin se explica lo que el servicio debe realizar con la informacin recibida. 

 LOG DEL SERVICIO 

 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 

 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta: 
  op:false 

 1. VALIDACIN DE DATOS COMPLETOS 

 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de . Parmetros del body de la peticin y objetos dentro de _data   de la especificacin de la API Pblica . Si lo son, seguir adelante con el prximo paso.  Si no lo son deber entregar una respuesta de error: 
 incomplete_data 

 2. VALIDACIN DE LOS DATOS DE LOS ORGENES Y DONANTES DE NO NEGOCIADOS. 

 Con los datos que llegan en los parmetros: 
 eatc_cua_donor_nng 
 cua_master 
 _data 
 eatc_cua_origin_nng 

 El sistema deber consultar corresponden a la misma cuenta maestra y si estan configurados como orgenes y donantes de no negociados: 

 Consulta para determinar que el donante de no negociados est configurado cmo tal 
 Cuando la donacin que se va a consultar fue enviada con el parmetro eatc_dona_state= cancelled entonces el sistema realiza la siguiente consulta 
 {{ URL_datagov }}/api/eatcloud/eatc_cua?name={{ eatc_donor_nng }}& eatc_nng_donor = y 

 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail {{ eatc_donor_nng }} no_nng_donor 

 Y el sistema no realizar las configuraciones (se para el proceso) 

 Consulta para determinar que el origen de no negociados est configurado cmo tal 
 Cuando la donacin que se va a consultar fue enviada con el parmetro eatc_dona_state= cancelled entonces el sistema realiza la siguiente consulta 
 {{ URL_datagov }}/api/eatcloud/eatc_cua?name={{ eatc_cua_origin_nng }}& eatc_nng_origin = y 

 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail {{ eatc_cua_origin_nng }} no_nng_origin 

 El sistema no realizar las consultas ni las configuraciones correspondientes a la {{ eatc_cua_origin_nng }} con la anterior consulta fallida, pero podr realizar las consultas y configuraciones de otras {{ eatc_cua_origin_nng }} que si estn configuradas como orgenes de no negociados. 

 Consulta para determinar que los donantes y los orgenes pertenecen a la misma cua_master 
 El sistema deber validar si la cuenta donante de no negociados ( eatc_donor_nng ) y la(s) cuenta(s) orgen de no negociados ( eatc_cua_origin_nng ), pertenezcan a la misma cuenta maestra, realizando la siguiente consulta 
 {{ URL_datagov }}/api/eatcloud/eatc_cua?name={{ eatc_cua_origin_nng }}&cua_master={{ cua_master }} 

 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta: 
 fail: {{ eatc_cua_origin_nng }} origin_nng_in_other_cua_master 

 El sistema no realizar las configuraciones correspondientes a la  {{ eatc_cua_origin_nng }} con la consulta fallida, pero podr realizar las configuraciones de otras {{ eatc_cua_origin_nng }} que si correspondan a la misma cuenta maestra del donante de no negociados. 

 3. VALIDACIN DEL(DE LOS) ESTADO(S) DEL(DE LOS) PUNTO(S) 

 Con el(los) dato(s) que llega(n) en los parmetros: 
 cua_master 
 eatc_cua_origin_nng 
 eatc_pods_nng 

 El sistema deber realizar la siguiente validacin del(de los) punto(s) de donacin 
 {{ URL_donantes }}/api/allpods/eatc_pods? eatc_active =y& eatc-cua_master= {{ cua_master }}& eatc-cua ={{ eatc_cua_origin_nng }}& eatc-id ={{ eatc_pods_nng }}&_cmp=_id 

 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta ( validacin de datos de la donacin ): 
 fail {{ eatc_cua_origin_nng }} {{ eatc_pods_nng }} 

 Si la consulta arroja respuesta una respuesta vlida el sistema sigue  adelante con las configuraciones 

 4. CONFIGURACIN DE LA CUENTA ORIGEN NO NEGOCIADOS CON LA OPCIN DE MLTIPLES NITS 

 El sistema deber configurar a la cuenta Origen con mltiples NITs y adems de esto deber establecer la persistencia de los mltiples NITs con el valor por defecto con los datos del NIT del Origen de No Negociados y con un registro con el NIT del Donante de No Negociado, identificando su respectiva cua_user. 

 Consulta NIT Origen de No Negociados 
 El sistema deber realizar la siguiente consulta para determinar el NIT  

 {{ URL_datagov }}/crypt/eatcloud/ getcrypt?table= eatc_customers_cua &fieldname= eatc_cua& fieldvalue= {{ eatc_cua_origin_nng }}& fielddecrypt = eatc_customer_fiscal_id 

 El sistema lleva el valor del dato obtenido en eatc_customers_cua . eatc_customer_fiscal_id a la variable {{ eatc_cua_origin_nng_fiscal_id }} y con ella realiza la consulta de la Razn Social del Origen de No Negociados. 

 {{ URL_datagov }}/crypt/eatcloud/ getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id& fieldvalue= {{ eatc_cua_origin_nng_fiscal_id }}& fielddecrypt = eatc_fiscal_name 

 El sistema lleva el valor del dato obtenido en eatc_customers . eatc_fiscal_name a la variable {{ eatc_cua_origin_nng_fiscal_name }} para futuros registros. 

 Consulta NIT Donante de No Negociados 
 {{ URL_datagov }}/crypt/eatcloud/ getcrypt?table= eatc_customers_cua &fieldname= eatc_cua& fieldvalue= {{ eatc_cua_donor_nng }}& fielddecrypt = eatc_customer_fiscal_id 

 El sistema lleva el valor del dato obtenido en eatc_customers_cua . eatc_customer_fiscal_id a la variable {{ eatc_cua_donor_nng_fiscal_id }} y con ella realiza la consulta de la Razn Social del Origen de No Negociados. 

 {{ URL_datagov }}/crypt/eatcloud/ getcrypt?table= eatc_customers &fieldname= eatc_fiscal_id& fieldvalue= {{ eatc_cua_donor_nng_fiscal_id }}& fielddecrypt = eatc_fiscal_name 

 El sistema lleva el valor del dato obtenido en eatc_customers . eatc_fiscal_name a la variable {{ eatc_cua_donor_nng_fiscal_name }} para futuros registros. 

 Configuraciones segn estado de la configuracin de " eatc_cua .multiple_donors" del origen de no negociados 
 El sistema realiza la siguiente consulta: 

 {{ URL_datagov }}/api/eatcloud/eatc_cua?name={{ eatc_cua_origin_nng }}&_cmp=multiple_donors 

 La cuenta Origen NNG tiene previamente la configuracin de mltiples donors ( eatc_cua .multiple_donors=si) 
 El sistema deber revisar si la tabla " eatc_multiple_donors_info " tiene configurados los campos eatc_cua_user y eatc_default   si no los tiene configurados debe proceder a crearlos con el siguiente llamado. 
 {{ URL_donantes }} /optb/{{ eatc_cua_origin_nng }}/newcampo?_tabla= eatc_multiple_donors_info &new_field=eatc_cua_user,eatc_default 

 El sistema deber revisar si la tabla configurado como eatc_default=y el NIT del Origen de No Negociados con esta consulta.  
 {{ URL_donantes }} /api/{{ eatc_cua_origin_nng }}/ eatc_multiple_donors_info ?eatc_donor_code= {{ eatc_cua_origin_nng_fiscal_id }} 

  En caso de  existir el NIT registrado pero no tener esta configuracin deber proceder a realizarla con el siguiente llamado 
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=updete& eatc_default= y &WHERE eatc_donor_code= {{ eatc_cua_origin_nng_fiscal_id }} 

 En caso de no tener el NIT registrado  
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=insert& eatc_default= y & eatc_donor_code= {{ eatc_cua_origin_nng_fiscal_id }}& eatc_donor_fiscal_name = {{ eatc_cua_origin_nng_fiscal_name }} 

 El sistema deber revisar si la tabla configurado el NIT del donante de no negociados configurado en la tabla, haciendo este llamado. 
 {{ URL_donantes }} /api/{{ eatc_cua_origin_nng }}/ eatc_multiple_donors_info ?eatc_donor_code= {{ eatc_cua_donor_nng_fiscal_id }} 

 En caso de tener dicho NIT (el del donnante de no negociados) en la tabla debera realizar el siguiente llamdo para actualizar toda la informacin correspondiente 
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=updete& eatc_cua_user={{ eatc_donor_nng }}&WHERE eatc_donor_code= {{ eatc_cua_donor_nng_fiscal_id }} 

  En caso de NO tener dicho NIT  (el del donnante de no negociados) en la tabla debera realizar el siguiente llamdo para realizar el registro 
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=insert& eatc_cua_user={{ eatc_cua_donor_nng }}& eatc_donor_code= {{ eatc_cua_donor_nng_fiscal_id }}& eatc_donor_fiscal_name = {{ eatc_cua_donor_nng_fiscal_name }} 

 La cuenta Origen NNG NO tiene previamente la configuracin de mltiples NITs 
 El sistema deber crear la persistencia de Multiples NITs 
 {{ URL_donantes }} /casebd/ {{ eatc_cua_origin_nng }} / eatc_multiple_donors_info /object_store 

 El sistema deber configurar la persistencia de Multiples NITs con el siguiente llamado 
 {{ URL_donantes }} /optb/{{ eatc_cua_origin_nng }}/newcampo?_tabla= eatc_multiple_donors_info &new_field= eatc_donor_code , eatc_donor_fiscal_name, eatc_cua_user,eatc_default 

 Nota: se debe configurar como clave primaria el parmetro " eatc_donor_code " 

 El sistema deber  realizar el registro del NIT del Origen de No Negociados como Default. 
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=insert& eatc_default= y & eatc_donor_code= {{ eatc_cua_origin_nng_fiscal_id }}& eatc_donor_fiscal_name = {{ eatc_cua_origin_nng_fiscal_name }} 

 El sistema deber  realizar el registro del NIT del Donante de no negociados. 
 {{ URL_donantes }} /crd/{{ eatc_cua_origin_nng }}/?_tabla= eatc_multiple_donors_info &_operacion=insert& eatc_cua_user={{ eatc_cua_donor_nng }}& eatc_donor_code= {{ eatc_cua_donor_nng_fiscal_id }}& eatc_donor_fiscal_name = {{ eatc_cua_donor_nng_fiscal_name }} 

 El sistema deber realizar la configuracin de mltiples NITs de la respectiva cuenta. 
 {{ URL_datagov }}/crd/eatcloud/?_tabla=eatc_cua&_cmp=multiple_donors=si&WHEREname={{ eatc_cua_origin_nng }} 

 4. CONFIGURACIN DE PUNTOS DE DONACIN DE NO NEGOCIADOS 

 El sistema deber configurar la informacin de los puntos de donacin informados en el llamado al servicio, para luego configurarlos como nuevos registros en la nueva tabla de puntos de donacin de no negociados.  

 Consulta puntos de donacin (en allpods) 
 De los puntos de donacin que se informan en el llamado se deben consultar todos sus datos, con este llamado 
 {{ URL_donantes }}/api/allpods/eatc_pods? eatc_active =y& eatc-cua_master= {{ cua_master }}& eatc-cua ={{ eatc_cua_origin_nng }}& eatc-id ={{ eatc_pods_nng }} 

 Se toman todos los parmetros y sus respectivos valores de la respuesta (a excepcin de _id ) y se guardan en la variable {{parametros_creacion_pod_cua_origin_nng}} 

 Registro del punto de donacin segn el llamado 
 Con los parmetros anteriormente guardados se procede a realizar el siguiente registro 
 {{ URL_donantes }}/crd/allpods/?_tabla=eatc_pods_cua_donor_nng&_operacion=insert& {{parametros_creacion_pod_cua_origin_nng}} & eatc_cua_donor_nng= {{eatc_cua_donor_nng}}   

 5. CONFIGURACIN DE MULTIPLES PUNTOS EN EL DONANTE DE NO NEGOCIADOS 

 Verificacin de la creacin de parmetro requerido para el registro del punto de donacin en eatc_pods del donante de no negociados 
 El sistema deber revisar si la tabla " eatc_pods " de la respectiva cuenta donante de no negociados, tiene configurado el campo eatc_cua_origin. Si no lo tiene configurado debe proceder a crearlo con el siguiente llamado. 
 {{ URL_donantes }} /optb/{{ eatc_cua_donor_nng }}/newcampo?_tabla= eatc_pods &new_field= eatc_cua_origin 

 Consulta puntos de donacin (en la cuenta del origen de no negociados) 
 De los puntos de donacin que se informan en el llamado se deben consultar todos sus datos en el objectstore propio de la cuenta origen de no negociados, con este llamado 
 {{ URL_donantes }}/api/ {{ eatc_cua_origin_nng }} /eatc_pods? eatc-id ={{ eatc_pods_nng }} 

 Creacin puntos de donacin (en la cuenta donante de no negociados) 
 Contando con los datos obtenidos anteriormente y guardados en en la variable {{parametros_creacion_pod_cua_origin_nng}} , el sistema procede a realizar el siguiente registro: 
 {{ URL_donantes }}/crd/{{ eatc_cua_donor_nng }}/?_tabla=eatc_pods&_operacion=insert& {{parametros_creacion_pod_cua_origin_nng}} & eatc_cua_origin = {{ eatc_cua_origin_nng }} 

 6. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 

 Si las actualizaciones de informacin realizadas por el servicio se realizan de manera adecuada, entonces entregar la respuesta: 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONFIGPODSNNG: SERVICIO PARA CONFIGURAR PUNTOS DE DONACIN DE NO NEGACIADOS