# servicios-de-casos-sobre-la-base-de-datos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se han disponibilizado servicios web, que permiten programar procesos sobre la base de datos (querys, escritura de datos, borrados especiales, etc.), los cuales servirn para realizar operaciones necesarias de configuracin de manera rpida y sencilla, evitando posibles errores por manipulacin humana de los procesos. 
&#160; 
 Cuando se necesita un proceso especial o caso de base de datos, se programa dicho servicio (por dentro&#160; se hace el query necesario para tal fin) y el mismo se podr operar entregando ciertos parmetros por URL [CUA sobre la cual se aplica el proceso y nombre del caso]&#160; de la siguiente manera 
&#160; 
 Esto funciona por ejemplo para el caso de ayer sobre el hash de la contrasea, que de hecho se puede hacer desde este proceso y borrar el otro (opcional), se usa de la siguiente forma&#58; 
&#160; 
 [URL_entorno]/casebd/[CUA]/[nombre_caso] 
&#160; 
 A continuacin los casos implementados hasta el momento&#58; 

 hashpass&#58; hasheo de passwords de donantes&#58; 
&#160; 
 Para qu sirve&#58; 
 Para hashear los passwords de los donantes (eatc_pods) en una cuenta especfica. 
&#160; 
 Cundo se debe accionar&#58; 
 Cuando se suben manualmente a la plataforma puntos de donacin, dado que el actual mecanismo de autenticacin requiere de un password hasheado. 
&#160; 
 URL del servicio&#58; 
 https&#58;//donantes.eatcloud.info/casebd/[CUA]/hpass 

 non_award_alert&#58; incorporacin de timeout non_award_alert a eatc_timeout_rules para una cuenta particular&#58; 
 Para qu sirve&#58; 
 Para programar una regla de timeout necesaria para la activacin de las alertas de no adjudicacin de anuncios, para una cuenta especfica (dada que la insercin en la tabla eatc_timeout_rules requiere de establecer la cuenta sobre la cual funciona). 
&#160; 
 Cundo se debe accionar&#58; 
 Cuando se crea una nueva cuenta. 
&#160; 
 URL del servicio&#58; 
 https&#58;//donantes.eatcloud.info/casebd/[CUA]/non_award_alert 

 [NUEVO] Creacin de Object Store 
 Para qu sirve&#58; 
 Para crear un objects stores segn lo que sobre la configuracin del mismo se guarda en la respectiva documentacin de parmetros (https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=&#123;&#123;object_store&#125;&#125;). Al definir la el object_store a crear, el sistema deber consultar sus parmetros con el nimo de crear en la base de datos respectiva (de la cuenta invocada) una tabla que contenga los campos (parmetros) establecidos. Si los parmetros respectivos no existen, no se podr crear el object_store establecido.&#160; Si la cuenta no existe, tampoco se permitir crear el object_store 
&#160; 
 Cundo se debe accionar&#58; 
 Cuando se crea una nueva cuenta. 
&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/casebd/&#123;&#123;CUA&#125;&#125;/&#123;&#123;object_store&#125;&#125;/object_store 
&#160; 
&#160; 
 Ejemplo 
&#160; 
 Se desea crear el object_store&#58; eatc_sale_schedule para la cuenta colombia en ambiente de pruebas, por lo tanto se hace el siguiente llamado 
&#160; 
 https&#58;//devdonantes.eatcloud.info/casedb/colombia/eatc_sale_schedule/object_store 
&#160; 
 El sistema debe consultar la configuracin de los parmetros, para crear la tabla en la base de datos de la cuenta &quot;colombia&quot; 
&#160; 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=eatc_sale_schedule &#160; 

 [NUEVO] Carga de productos genricos para la venta 
 Para qu sirve&#58; 
 Para crear un objects stores por cuenta que incluyan los productos genricos a ser vendidos y que estn dispuestos como primera data maestra para la funcionalidad de Creacin de venta de ltimo minuto . 
&#160; 
 Los productos susceptibles a ser vendidos son estos (formato .csv)&#58; 

 eatc-odd_id;eatc-odd_code;eatc-odd_code_type;eatc-odd_name;eatc_odd_description;eatc_odd_image;eatc-odd_unit_weight_kg;eatc_VAT_percentage;eatc-contains_alergens 
 1;box_1;;Caja sorpesa de 1 KG;Caja con productos sorpresa con un peso de 1 KG;image_url;1;; 
 2;box_2;;Caja sorpesa de 2 KG;Caja con productos sorpresa con un peso de 2 KG;image_url;2;; 
 5;box_5;;Caja sorpesa de 5 KG;Caja con productos sorpresa con un peso de 2 KG;image_url;5;; 
 10;box_10;;Caja sorpesa de 10 KG;Caja con productos sorpresa con un peso de 10 KG;image_url;10;; 
&#160; 
 Cundo se debe accionar&#58; 
 Cuando se crea una nueva cuenta. 
&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/casebd/&#123;&#123;CUA&#125;&#125;/upl_eatc_sale_prd_mstr 
&#160; 
&#160; 
 El servicio debe funcionar como la accin que se realiza para cargar este archivo con este servicio&#58;&#160; 
&#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/mstr/&#123;&#123;CUA&#125;&#125;/eatc_sale_prd_mstr 

 [NUEVO] CONFIGURACIN POR DEFECTO DE FUNCIONALIDADES PARA VISUALIZACIN DE PODS 
 Para qu sirve&#58; 
 Para crear registros&#160; 
&#160; 
 Cundo se debe accionar&#58; 
 Cuando se crea un nuevo punto de donacin . 
 Cuando a una cuenta&#160; 
&#160; 
 URL del servicio para configurar por punto de donacin&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/allpods/pods_default_features?eatc-cua=&#123;&#123; eatc-cua &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125;&amp;plan=&#123;&#123; tipo_de_licencia &#125;&#125; 
&#160; 
 Consulta que se debe realizar para realizar obtener los datos para realizar el registro&#58; 
 El sistema debe realizar la siguiente consulta, para establecer la vertical de la cuenta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc-cua &#125;&#125; 
&#160; 
 Con el dato obtenido y los datos anteriormente entregados en la invocacin del servicio, se traen las funcionalidades que deben ser registradas para el punto de donacin (mltiples funcionalidades a ser asignadas a un punto) 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?plataforma= webapp &amp;plan=&#123;&#123; tipo_de_licencia &#125;&#125;&amp;ambiente= produ &amp;vertical=&#123;&#123; vertical &#125;&#125; 
&#160; 
 Con esta consulta se obtienen los datos para la posterior escritura en el maestro de configuracin en allpods&#58; 
eatc_config_funcionalidades. idfuncionalidad 
eatc_config_funcionalidades. funcionalidad 
eatc_config_funcionalidades. descripcion 
&#160; 
 Escritura en el maestro de configuracin de funcionalidades en allpods 
 Con las funcionalidades que se obtienen en la anterior consulta, se realizan las mltiples escrituras en el maestro de configuracin que se guarda en la cuenta allpods .&#160; 
&#160; 
 Si existen registros previos para el punto en cuestin, se deber realizar como primera medida el borrado de los registros&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/allpods/?_tabla=eatc_config_funcionalidades&amp;_operacion=delete&amp; WHEREpod_id =&#123;&#123; eatc-pod_id &#125;&#125; 
&#160; 
 Luego se debe realizar la siguiente consulta para obtener el nombre de del punto de donacin eatc-name 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc-cua &#125;&#125;/eatc_pods?eatc-id=&#123;&#123; eatc-pod_id &#125;&#125; 
&#160; 
 Con los datos obtenidos se generan los parmetros de escritura en el respectivo maestro de configuracin eatc_config_funcionalidades en la cuenta allpods (mltiples funcionalidades a ser asignadas a un punto). 
&#160; 
 &#123;&#123;parametros_creacion_registros&#125;&#125; 
 idfuncionalidad = &#123;&#123;eatc_config_funcionalidades. idfuncionalidad &#125;&#125; 
 funcionalidad = &#123;&#123;eatc_config_funcionalidades. funcionalidad &#125;&#125; 
 descripcion = &#123;&#123;eatc_config_funcionalidades. descripcion &#125;&#125; 
 pod_id = eatc-pod_id (se toma del llamado del servicio) 
 pod_name = eatc-name (se toma de la consulta que se hace con el dato eatc-pod_id &#160; que se incluye en el llamado del servicio) 
 cua= eatc-cua (se toma del llamado del servicio) 
 lastupdate= timestamp 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/allpods/?_tabla=eatc_config_funcionalidades&amp;_operacion=insert&amp; &#123;&#123;parametros_creacion_registros&#125;&#125; 
&#160; 
 URL del servicio para configurar por cuenta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/allpods/pods_default_features?eatc-cua=&#123;&#123; eatc-cua &#125;&#125;&amp;plan=&#123;&#123; tipo_de_licencia &#125;&#125; 
&#160; 
 Consulta que se debe realizar para realizar obtener los datos para realizar el registro&#58; 
 El sistema debe realizar la siguiente consulta, para establecer la vertical de la cuenta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; eatc-cua &#125;&#125; 
&#160; 
 Con el dato obtenido y los datos anteriormente entregados en la invocacin del servicio, se traen las funcionalidades que deben ser registradas para los diversos puntos de donacin de la cuenta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?plataforma= webapp &amp;plan=&#123;&#123; tipo_de_licencia &#125;&#125;&amp;ambiente= produ &amp;vertical=&#123;&#123; vertical &#125;&#125; 
&#160; 
 Con esta consulta se obtienen los datos para la posterior escritura en el maestro de configuracin en allpods&#58; 
eatc_config_funcionalidades. idfuncionalidad 
eatc_config_funcionalidades. funcionalidad 
eatc_config_funcionalidades. descripcion 
&#160; 
 Consulta que se debe realizar para obtener los puntos de donacin de la cuenta&#58; 
 El sistema realiza la siguiente&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123; eatc-cua &#125;&#125;/eatc_pods?eatc-id=_* 
&#160; 
 Con esta consulta se obtienen los puntos de donacin a los cuales se les deben registrar las mltiples funcionalidades producto de la primera consulta&#58; 
eatc_pods. eatc-pod_id 
eatc_pods. eatc-name 
&#160; 
 Escritura en el maestro de configuracin de funcionalidades en allpods 
 Con las funcionalidades que se obtienen en la&#160; consulta respectiva, se realizan las mltiples escrituras en el maestro de configuracin para cada uno de los mltiples puntos de donacin de la cuenta, las cuales se guardan en la cuenta allpods .&#160; 
&#160; 
 Si existen registros previos para la cuenta respectiva, se deber realizar como primera medida el borrado de los registros&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/allpods/?_tabla=eatc_config_funcionalidades&amp;_operacion=delete&amp; WHEREcua =&#123;&#123; eatc-cua &#125;&#125; 

&#160; 
 &#123;&#123;parametros_creacion_registros&#125;&#125; 
&#160; 
 idfuncionalidad = &#123;&#123;eatc_config_funcionalidades. idfuncionalidad &#125;&#125; 
 funcionalidad = &#123;&#123;eatc_config_funcionalidades. funcionalidad &#125;&#125; 
 descripcion = &#123;&#123;eatc_config_funcionalidades. descripcion &#125;&#125; 
 pod_id = &#123;&#123; eatc-pod_id &#125;&#125; (se toma de la consulta de los puntos por cuenta) 
 pod_name = &#123;&#123; eatc-name &#125;&#125; (se toma de la consulta de los puntos por cuenta) 
 cua= eatc-cua (se toma del llamado del servicio) 
 lastupdate= timestamp 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/allpods/?_tabla=eatc_config_funcionalidades&amp;_operacion=insert&amp; &#123;&#123;parametros_creacion_registros&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE CASOS SOBRE LA BASE DE DATOS - CASEDB