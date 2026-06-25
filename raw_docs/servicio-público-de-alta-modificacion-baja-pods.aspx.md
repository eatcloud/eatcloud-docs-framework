# servicio-público-de-alta-modificacion-baja-pods.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar el API pblica de creacin de Puntos de Donacin.&#160; La siguiente documentacin es indicativa de los temas que se deben tener en cuenta para este desarrollo, y se debe tomar como una gua (no como una camisa de fuerza). 

 Validacin de existencia de cuenta maestra y la cuenta usuario&#58; 
&#160; 
 El sistema valida si existe la cuenta maestra y la cuenta usuario con la cual se invoc el servicio. Si no existen el servicio retornar un mensaje de error 
&#160; 
 cua_master does not exist 
 cua_user does not exist 

 CREACIN DE UN PUNTO DE DONACIN (POD) 
&#160; 
 Se basa en la documentacin del API pblica respectiva 
&#160; 
 Validacin de tope de puntos de donacin por cuenta 
&#160; 
 Antes de operar el servicio, el sistema deber realizar la siguiente consulta, teniendo en cuenta los datos alojados en la informacin de la cuenta y que se consultan mediante este llamado 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123; cua_user &#125;&#125;&amp;_distinct=type 
&#160; 
 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_types_of_licenses? eatc_code =&#123;&#123;eatc_cua. type &#125;&#125;&amp;_distinct= eatc_pods_limit 
&#160; 
 Si esta ltima consulta no trae ningn valor, se utilizar esta consulta por defecto&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_types_of_licenses? eatc_code =free&amp;_distinct= eatc_pods_limit 
&#160; 
 El sistema debe evaluar si el nmero que se obtiene en el parmetro eatc_types_of_licenses. eatc_pods_limit es mayor al valor del count de la siguiente consulta. 

&#160; 
 &#160;Consulta del nmero de puntos de donacin ***ACTIVOS*** por la cuenta 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont 
&#160; 
 Si es mayor &#160; ( eatc_types_of_licenses. eatc_pods_limit &gt; eatc_pods. eatc_active =y ) el servicio permitir el registro 
&#160; 
 Si es menor o igual ( eatc_types_of_licenses. eatc_pods_limit = &lt; eatc_pods. eatc_active =y )&#160; debe desplegar un mensaje de error&#58; 
&#160; 
 The maximum number of PODs per license has been reached. 
&#160; 
 y adems se debe proceder con el registro del respectivo evento de upgrade&#58;&#160; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin ( eatc_upgrade_events )*** 
&#160; 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_pods_limit 
 eatc_user = anonymous_web_user 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
&#160; 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = eatc_pods_limit 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = eatc_pods_limit &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free &#160; 
&#160; 
&#160; 
 Validacin de unicidad de identificador nico del punto de donacin&#58; 
&#160; 
 Se deber validar que la combinacin entre&#160; el input que se est realizando ( eatc-pod_id ) y la cuenta usuario ( cua_user ), sea nica en el objectstore allpods de la siguiente manera 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/ allpods /eatc_pods?eatc-id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;eatc-cua=&#123;&#123; cua_user &#125;&#125;&amp;_cmp=eatc-id,eatc-name 
&#160; 
 Si la anterior consulta trae un resultado, quiere decir que el id que se est ingresando ya est utilizado por lo tanto el sistema debe desplegar un mensaje de error 
&#160; 
 &quot;The identifier entered (eatc-pod_id) is already being used by another donation point in your organization.&quot; 
&#160; 
 &#123;&#123;parametros&#125;&#125; 
 eatc-name =&gt; eatc_pods. eatc-name =&gt; El sistema valida que el dato exista 
 eatc-responsable =&gt; eatc_pods. eatc-responsable =&gt; El sistema valida que el dato exista 
 eatc-phone =&gt; eatc_pods. eatc-phone =&gt; El sistema valida que el dato exista 
 eatc-email =&gt; eatc_pods. eatc-email =&gt; El sistema valida que el dato exista y que sea un email en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 email (eatc-email) in incorrect format 
&#160; 
 eatc-lat =&gt; eatc_pods. eatc-lat =&gt; El sistema valida que el dato exista y que sea una coordenada decimal en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 Latitude (eatc-lat) in incorrect format (not a decimal coordinate with dot separator) 
&#160; 
 eatc-lon &#160; =&gt; eatc_pods. eatc-lon =&gt; El sistema valida que el dato exista y que sea una coordenada decimal en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 Longitude (eatc-lon) in incorrect format (not a decimal coordinate with dot separator) 
&#160; 
 eatc-a d dress &#160; =&gt; eatc_pods. eatc-adress&#160; =&gt; El sistema valida que el dato exista 
 Pas&#58;&#160; &#160; 
&#160; 
 A partir de la consulta genrica&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua&#125;&#125; 
&#160; 
 El sistema toma el dato eatc_cua. eatc-country &#160; para incorporarlo en este parmetro ( eatc-pods. eatc-country ) 
&#160; 
 eatc-province &#160; =&gt; eatc_pods. eatc-province&#160; =&gt; El sistema valida que el dato exista 
 eatc-city =&gt; eatc_pods. eatc-city =&gt; El sistema valida que el dato exista 
 eatc_postal_code =&gt; eatc_pods. eatc_postal_code =&gt; El sistema valida que el dato exista 
 eatc-pods_typolgy_a =&gt; eatc_pods. eatc-pods_typolgy_a 
 eatc-pods_typolgy_b =&gt; eatc_pods. eatc-pods_typolgy_b 
 eatc-pods_typolgy_c =&gt; eatc_pods. eatc-pods_typolgy_c 
 login =&gt; eatc_pods. login&#160; =&gt; El sistema valida que el dato exista 
 password =&gt; eatc_pods. password =&gt; El sistema valida que el dato exista 
 Datestamp =&gt;eatc_pods. eatc-production_date 
 Timestamp =&gt;/allpods/eatc_pods. eatc-update 
&#160; 
 Si alguno de los datos obligatorios (segn la documentacin del API pblica respectiva ) no se encuentra en el llamado, el servicio debe contestar con el mensaje 
 retry&#58; incomplete data 
&#160; 
 Registro del nuevo POD 
 Realizacin del registro en la base de datos de donantes 
&#160; 
 Una vez validados los datos, se realiza el respectivo registro 
 Mtodo POST&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla= eatc_pods &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
 Llamado al servicio de hasheo de contraseas 
 Realizado el anterior registro se procede a invocar el servicio para hashear contraseas 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /casebd/ &#123;&#123;cua_user&#125;&#125; /hpass 

&#160; 
 Realizacin del registro en allpods 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado &#160; para la incorporacin de la informacin&#160; 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/allpodss/?_tabla= eatc_pods &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
&#160; 
 Llamado al servicio de creacin de configuracin de funcionalidades en AllPods (llamado con plan= free ) 
 Dado que en el nuevo esquema de licenciamiento se elimina el tipo de licencia free_trial y se deja solamente la &quot;free&quot;, se debe revisar el llamado que anteriormente se haca con plan= free_trial y hacerlo con plan= free 
&#160; 
 Al presionar este botn el formulario debe realizar tambin el siguiente llamado al servicio desarrollado para este fin 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/allpods/pods_default_features?eatc-cua=&#123;&#123; _DOM .cua_user &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;plan= free 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la creacin correcta del punto de donacin y desplegar el siguiente mensaje&#58; 
&#160; 
 Confirmacin de datos completos 
 Una vez enviado el registro y que el CRD responda adecuadamente, se debe realizar la siguiente consulta&#58; 
 https&#58;//donantes.eatcloud.info/api/[cua_user]/eatc_pods? eatc-id=[eatc-id ] 
&#160; 
 Si la consulta no trae informacin o al evaluar los resultados, faltan campos obligatorios, el sistema debe proceder a borrar el registro creado de manera incompleta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_user &#125;&#125;/?_tabla=eatc_pods&amp;_operacion=delete&amp;WHERE eatc-id=&#123;&#123;eatc_pods.eatc-id&#125;&#125; 
&#160; 
 Y se le debe informar al usuario que debe intentar de nuevo la creacin del registro con el mensaje 
 retry&#58; incomplete data 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de xito 
 Success 
&#160; 
 Creacin de traza de auditora 
 El servicio deber crear un log para determinar desde dnde se llam el servicio, el usuario que lo hizo y la fecha y hora. 

 ACTUALIZACIN DE UN PUNTO DE DONACIN (POD) 
&#160; 
 Se basa en la documentacin del API pblica respectiva 
&#160; 
 &#123;&#123;parametros&#125;&#125; 
 eatc-name =&gt; eatc_pods. eatc-name&#160; 
 eatc-responsable =&gt; eatc_pods. eatc-responsable&#160; 
 eatc-phone =&gt; eatc_pods. eatc-phone&#160; 
 eatc-email =&gt; eatc_pods. eatc-email =&gt; En caso que llegue en el respectivo JSON, el sistema valida que sea un email en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 email (eatc-email) in incorrect format 
 eatc-lat =&gt; eatc_pods. eatc-lat =&gt; En caso que llegue en el respectivo JSON, el sistema valida que sea una coordenada decimal en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 Latitude (eatc-lat) in incorrect format (not a decimal coordinate with dot separator) 
&#160; 
 eatc-lon &#160; =&gt; eatc_pods. eatc-lon =&gt; En caso que llegue en el respectivo JSON, el sistema valida que sea una coordenada decimal en el formato adecuado.&#160; de no ser as responde con el siguiente mensaje&#58; 
 Longitude (eatc-lon) in incorrect format (not a decimal coordinate with dot separator) 
&#160; 
 eatc-a d dress &#160; =&gt; eatc_pods. eatc-adress&#160;&#160; 
 eatc-province &#160; =&gt; eatc_pods. eatc-province 
 eatc-city =&gt; eatc_pods. eatc-city 
 eatc_postal_code =&gt; eatc_pods. eatc_postal_code 
 eatc-pods_typolgy_a =&gt; eatc_pods. eatc-pods_typolgy_a 
 eatc-pods_typolgy_b =&gt; eatc_pods. eatc-pods_typolgy_b 
 eatc-pods_typolgy_c =&gt; eatc_pods. eatc-pods_typolgy_c 
 login =&gt; eatc_pods. login 
 password =&gt; eatc_pods. password 
 Timestamp =&gt;/allpods/eatc_pods. eatc-update 
&#160; 
 Si alguno de los datos obligatorios (segn la documentacin del API pblica respectiva ) no se encuentra en el llamado, el servicio debe contestar con el mensaje 
 retry&#58; incomplete data 
&#160; 
 Actualizacin del POD 
 Realizacin del update en la base de datos de donantes 
 Una vez validados los datos, se realiza el respectivo update 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla= eatc_pods &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHEREeatc-pod_id= eatc-pod_id 
&#160; 
 Llamado al servicio de hasheo de contraseas 
 Realizado el anterior registro se procede a invocar el servicio para hashear contraseas 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /casebd/ &#123;&#123;cua_user&#125;&#125; /hpass 

&#160; 
 Realizacin del registro en allpods 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado &#160; para la incorporacin de la informacin&#160; 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/allpodss/?_tabla= eatc_pods &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHEREeatc-pod_id= eatc-pod_id 
&#160; 
 Si la actualizacin&#160; fue exitosa se le debe mostrar al usuario el mensaje de xito 
 Success 
&#160; 
 Creacin de traza de auditora 
 El servicio deber crear un log para determinar desde dnde se llam el servicio, el usuario que lo hizo y la fecha y hora. 

 BORRADO DE UN PUNTO DE DONACIN (POD) 
&#160; 
 Se basa en la documentacin del API pblica respectiva 
&#160; 
 &#123;&#123;parametros&#125;&#125; 

&#160; 
 y =&gt;/allpods/eatc_pods. eatc_active 
&#160; 
 Si alguno de los datos obligatorios (segn la documentacin del API pblica respectiva ) no se encuentra en el llamado, el servicio debe contestar con el mensaje 
 retry&#58; incomplete data 
&#160; 
 Borrado del POD 
 Realizacin del registro en allpods 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado &#160; para la incorporacin de la informacin&#160; 
&#160; 
 Mtodo POST&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/allpods/?_tabla= eatc_pods &amp;_operacion=update&amp;&#123;&#123;parametros&#125;&#125;&amp;WHEREeatc-pod_id= eatc-pod_id 
&#160; 
 Si el registro fue exitoso se le debe mostrar al usuario el mensaje de xito 
 Success 
&#160; 
 Creacin de traza de auditora 
 El servicio deber crear un log para determinar desde dnde se llam el servicio, el usuario que lo hizo y la fecha y hora. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIO PBLICO DE ALTA - MODIFICACIN - BAJA DE PUNTOS DONACIN (EATC_PODS)