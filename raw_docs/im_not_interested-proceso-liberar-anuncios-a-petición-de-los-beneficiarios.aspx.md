# im_not_interested-proceso-liberar-anuncios-a-petición-de-los-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 PROCESO BORRAR MATCH, GENERAR REGISTRO DE EXCLUSIN DE MATCH, BORRAR DATOS DE ASIGNACIN Y GENERAR NUEVO MATCH 

 Se implementar un servicio que tenga la siguiente estructura&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/ notinterested /&#123;&#123; _DOM. cua_master &#125;&#125;? eatc_country = &#123;&#123; eatc_cua_master . eatc_country &#125;&#125;&amp; eatc_city = &#123;&#123;&#123; eatc_dona_headers. eatc-city &#125;&#125;&amp; eatc_doma = &#123;&#123; eatc_donation_managers. organizacin &#125;&#125;&amp; eatc_doma_code = &#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp; eatc_user = &#123;&#123; eatc_users . correo_electronico &#125;&#125;&amp; eatc_platform = app_beneficiarios &amp;eatc_dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc_cua = &#123;&#123; eatc_dona_headers. eatc_cua_origin &#125;&#125;&amp;eatc_state=&#123;&#123; eatc_dona_headers. eatc-state &#125;&#125;&amp; eatc_match_registry_id= &#123;&#123; eatc_match_registry. _id &#125;&#125; 
&#160; 
 EJEMPLO (ambiente de pruebas)&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/ im_not_interested /abaco/? eatc_country = CO &amp; eatc_city = CALI &amp; eatc_doma = FUNDACION%20ARQUIDIOCESANA%20BANCO%20DE%20ALIMENTOS%20DE%20CALI &amp; eatc_doma_code = 805025018 &amp; eatc_user = astridgiraldo@bancalimentos.org &amp; eatc_platform = app_beneficiarios &amp; eatc_dona_header_code = 00002108194223 &amp;&amp; eatc_cua = exito &amp; eatc_state = announced &amp; eatc_match_registry_id= 2 

 Registro en eatc_match_rejection_registry *** 
 Con los datos de la donacin seleccionada , del gestor de donaciones y del usuario de la App , se realiza el siguiente registro&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; eatc_cua_master . eatc_country &#125;&#125; 
 eatc_city = &#123;&#123;&#123; eatc_dona_headers. eatc-city &#125;&#125; 
 eatc_cua_master = &#123;&#123; _DOM. cua_master &#125;&#125; 
 eatc_doma = &#123;&#123; eatc_donation_managers. organizacin &#125;&#125; 
 eatc_doma_code = &#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125; 
 eatc_dona_header_code = &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
 eatc_cua = &#123;&#123; eatc_dona_headers. eatc_cua_origin &#125;&#125; 
 eatc_platform = app_beneficiarios 
 eatc_reject_cause = no_me_interesa 
 eatc_user = &#123;&#123; eatc_users . correo_electronico &#125;&#125; 
 eatc_state =&#123;&#123; eatc_dona_headers. eatc-state &#125;&#125; 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_match_rejection_registry&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

 Borrado de match 
&#160; 
 El sistema debe borrar el registro de match, que se utiliza para definir los anuncios que se muestran en la nube de donaciones con el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_match_registry &amp;_operacion=DELETE&amp;WHERE_id=&#123;&#123; eatc_match_registry. _id &#125;&#125; 

&#160; 
 Borrado de datos de adjudicacin / programacin ( eatc_state= awarded o eatc_state= programed) 
&#160; 
 Cuando el estado de la donacin sea &quot;awarded&quot; (adjudicada) o &quot;programmed&quot; (programada), adicional a los registros anteriores, el sistema deber borrar los datos de adjudicacin y programacin (segn sea el caso) y pasar de nuevo la donacin a estado &quot;announced&quot;. 
 El dato que debe editar es&#58; 
&#160; 
 eatc-state&#58; &quot; announced &quot; 
&#160; 
 Los datos que debe borrar (dejar vacos) son&#58; 
 &quot;eatc-adjudication_datetime&quot; &#58; &quot;0000-00-00 00&#58;00&#58;00&quot; 
 &quot;eatc-donation_manager_user_doc_id&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_code&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_name&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_address&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_phone&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_typology_a&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_typology_b&quot; &#58; &quot;&quot; 
 &quot;eatc-donation_manager_typology_c&quot; &#58; &quot;&quot; 
 &quot;eatc-scheduling_datetime&quot; &#58; &quot;0000-00-00 00&#58;00&#58;00&quot; 
 &quot;eatc-programed_picking_datetime&quot; &#58; &quot;0000-00-00 00&#58;00&#58;00&quot; 
 &quot;eatc-picker_name&quot; &#58; &quot;&quot; 
 &quot;eatc-picker_doc_id&quot; &#58; &quot;&quot; 
 &quot;eatc-picker_license_plate&quot; &#58; &quot;&quot; 
 ***NUEVO&#58; &quot;eatc-picker_phone&quot; &#58; &quot;&quot; *** 
&#160; 

&#160; 
 ***NUEVO &#58; RECLASIFICACIN DE DONACIN (PARA DONACIONES QUE TIENEN RESTRICCIONES CON RESPECTO A LOS BANCOS DE ALIMENTOS ) *** 
&#160; 
 Se ha establecido una categorizacin especial de donaciones, para que cuando un banco rechase una donacin con la funcin &quot;im_not_interested&quot;, el sistema realice las siguientes validaciones y operaciones para aumentarle las posibilidades de gestin a la donacin y evitar que al rechazar donaciones priorizadas o exclusivas para los bancos, las mismas queden en el aire&#58; 
&#160; 
 Verificacin de estado (para evitar colisiones) 
 El sistema deber verificar que el anuncio&#160; contine en estado &quot; announced &quot;, despus de realizado el anterior proceso, con el nimo de evitar que la operacin se realize, despus que otra organizacin realice adjudicacin del mismo. 
&#160; 
 Validaciones para la cuenta maestra ABACO 
 Verificacin que en el registro del match, no exista otro banco de alimentos =&gt; ABACO 
 &#160;El sistema deber verificar que el anuncio&#160; no tenga en su registro de match, otro banco de alimentos, caso en el cual no se deber reclasificar la donacin, dado que aun tendrn prelacin los dems bancos registrados en el match. 
&#160; 
 La verificacin se realizar con una consulta como la siguiente&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/abaco/ eatc_match_registry ?eatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;tipologia_b=1&amp;_cont 
&#160; 
 Si el conteo es mayor o igual a 1, quiere decir que existen otros bancos de alimentos con prelacin para adjudicarse el anuncio,&#160; entonces el sistema no realiza la reclasificacin de la donacin.&#160; Si el conteo es igual a cero, entonces el sistema realiza la siguiente validacin para establecer si la regla que le aplica a la donacin, tiene exclusividad o no para bancos de donacin. 

&#160; 
 Verificacin que la regla de match no sea exclusiva para bancos&#160; =&gt; ABACO 
 &#160;El sistema deber verificar que la regla de match que se le aplic a la donacin no sea una regla que tenga exclusividad para bancos de alimentos. 
&#160; 
 La verificacin se realizar con una consulta como la siguiente&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/abaco/ eatc_dona_headers ?eatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp= eatc_match_asignation_rule&#160; 
&#160; 
 Con el valor obtenido, deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_match_asignation_rules?eatc_match_asignation_rule= &#123;&#123; eatc_dona_headers. eatc_match_asignation_rule &#125;&#125; &amp;eatc_exclusive=n &amp;_cont 
&#160; 
 Si el conteo es igual a 0, quiere decir que la regla que le aplica al anuncio tiene exclusividad para bancos, caso en el cual no se puede reclasificar la donacin.&#160; 
&#160; 
 En este caso el sistema deber generar una alerta al correo operaciones@eatcloud.com con el asunto&#58; 
 &quot;Donacin exclusiva rechazada&quot; 
&#160; 
 Y en el cuerpo debe enviarse la fecha y hora del rechazo , el donante, el nmero de la donacin la fecha y hora de publicacin de la donacin, los KG Originales, la regla de clasificacin de match aplicable y el banco que la rechaz en ltima instancia (con los datos principales del Banco&#58; el telfono 1 y el responsable) . 
&#160; 
 (De debe revisar tambin el envo de esta informacin a un grupo de Telegram exclusivo para esta alerta&#58; &quot;Donaciones exclusivas rechazadas&quot; que nos permita a futuro incorporar por ejemplo personal de ABACO en la recepcin de esta alerta.) 
&#160; 
 Si el conteo es mayor o igual a 1, quiere decir que la regla no tiene exclusividad, y por lo tanto se podr evaluar la siguiente caracterstica para establecer si se procede con la reclasificacin del anuncio. 
&#160; 
 Verificacin que en el registro del match, no existan otros beneficiarios. &#160; =&gt; ABACO 
 El sistema deber verificar que el anuncio&#160; no tenga en su registro de match, otras organizaciones. 
&#160; 
 La verificacin se realizar con una consulta como la siguiente&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/abaco/ eatc_match_registry ?eatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;tipologia_b=!1&amp;_cont 
&#160; 
 Si el conteo es igual a 0, quiere decir que el anuncio no tiene otras organizaciones registradas en el match, caso en el cual se deber proceder con la reclasificacin de la donacin para aumentarle las opciones de gestin.&#160; Si el conteo es menor que tres (es decir que hay solamente 3 organizaciones en el match) entonces tambin se deber proceder a realizar la reclasificacin.&#160; 
&#160; 
 Si hay un conteo mayor de 3 entonces el sistema deber evaluar si la fecha y hora de visualizacin del match 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/abaco/ eatc_match_registry ?eatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;tipologia_b=!1&amp;_distinct=matching_since 
&#160; 
 Es posterior a la fecha y hora actual, caso en el cual deber proceder a establecer la fecha y hora actual como la fecha / hora de visualizacin del match 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/_tabla= eatc_match_registry &amp;_operacion=updete&amp;matching_since=&#123;&#123;fecha_hora_actual&#125;&#125;&amp;WHEREeatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 

&#160; 
 Validaciones para dems cuentas&#160; maestras (en principio &quot;mexico&quot;) 
 El sistema deber evaluar si la fecha y hora de visualizacin del match 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/abaco/ eatc_match_registry ?eatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;tipologia_b=1&amp;_distinct=matching_since 
&#160; 
 Es posterior a la fecha y hora actual, caso en el cual deber proceder a establecer la fecha y hora actual como la fecha / hora de visualizacin del match 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/_tabla= eatc_match_registry &amp;_operacion=updete&amp;matching_since=&#123;&#123;fecha_hora_actual&#125;&#125;&amp;WHEREeatc-dona_header_code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 

&#160; 
 Reclasificacin de la donacin&#160; 
 Una vez pasadas las validaciones anteriores cuando corresponda (en el caso de ABACO&#58;&#160; determinar que en el match solamente estaba registrado el banco que rechaz la donacin y la regla de asignacin no era exclusiva.&#160; Se entiende que para las dems cuentas maestras, simplemente se valida que las reglas de asignacin apliquen a Bancos de Alimentos y el sistema entra a este lugar), el sistema deber reclasificar la donacin con el siguiente llamado, para aumentar las opciones de gestin (esta clasificacin no est registrada en los querys de clasificacin dado que solamente se clasificar as a partir de este proceso). 
&#160; 
 ***NUEVO&#58; verificacin de si la donacin ha tenido el nmero mximo de rechazos segn lo estipulado en la configuracin respectiva *** =&gt; Inicialmente Piloto Nestl 
 Para el piloto de Nestl se ha definido un nmero mximo de rechazos por parte de los bancos que participarn del mismo a partir de los cuales un anuncio se tendr que reclasificar de una manera que haga que el match sea visible a todos los dems bancos (sin importar los turnos PACADI establecidos).&#160; Para ello se deber establecer cuantos rechazos por parte de los bancos adscritos al piloto ha tenido el anuncio, y si dicha cantidad es igual o superior al parmetro de nmero de rechazos mximos establecido para la regla de clasificacin del anuncio en particular, entonces el anuncio debera ser reclasificado, de tal manera que al operar el match, sea visible a todos los bancos. 
&#160; 
 El sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master=&#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_origin_match_asignation_rule = &#123;&#123; eatc_dona_headers. eatc_match_asignation_rule &#125;&#125;&amp;_cmp= eatc_max_rejection , eatc_destiny_match_asignation_rule, eatc_destiny_match_asignation_rule_by_rejetions 
&#160; 
 Si la anterior consulta trae una respuesta vlida (un nmero entero), luego el sistema deber evaluar cuantos rechazos por parte de los bancos que se inscriben en el piloto con Nestl ha recibido, para ello deber realizar la siguiente consulta 
 &#123;&#123; array_id_auditados_nestle &#125;&#125;=&#123;&#123;url_entorno_beneficiarios&#125;&#125;/api/mexico/eatc_donation_managers? eatc_audited_by_nestle =y&amp;_cmp=identificador_unico_registro&#160; 
&#160; 
 Con el array obtenido deber realizar luego la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_match_rejection_registry?eatc_doma_code= &#123;&#123; array_id_auditados_nestle &#125;&#125;&amp;eatc_dona_header_code= &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;_count 
&#160; 
 Si el conteo recibido es igual o superior al valor registrado en &#123;&#123; eatc_dona_reclassification_rules. eatc_max_rejection &#125;&#125; , entonces el sistema deber realizar la siguiente escritura&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers ?&amp;_operacion=update&amp; eatc_match_asignation_rule= &#123;&#123; eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule _by_rejetions &#125;&#125;&amp;WHEREeatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si el nmero de rechazos para la donacin en cuestin, es menor al nmero mximo de rechazos establecidos, entonces podr pasar al proceso de reclasificaccin en adelante detallado. 
&#160; 
 Definicin de la regla de reclasificacin aplicable 
 El sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master=&#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_origin_match_asignation_rule = &#123;&#123; eatc_dona_headers. eatc_match_asignation_rule &#125;&#125;&amp;_cmp= eatc_destiny_match_asignation_rule 
&#160; 
 Si la consulta no trae resultados entonces deber realizarse la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master=&#123;&#123; _DOM. cua_master &#125;&#125;&amp; eatc_origin_match_asignation_rule = _default &amp;_cmp= eatc_destiny_match_asignation_rule 
&#160; 
 Y si no trae respuesta entonces se realizar la consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master= _default &amp; eatc_origin_match_asignation_rule = _default &amp;_cmp= eatc_destiny_match_asignation_rule 
&#160; 
 Con el parmetro que se recibe en la consulta &#123;&#123; eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125; 
&#160; 
 El sistema realiza el siguiente registro&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers ?&amp;_operacion=update&amp; eatc_match_asignation_rule= &#123;&#123; eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125;&amp;WHEREeatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Y por lo tanto aplicarn las reglas de registro&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_match_asignation_rules?eatc_match_asignation_rule=&#123;&#123; eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125; 
&#160; 
 y ampliacin 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule=&#123;&#123; eatc_dona_reclassification_rules. eatc_destiny_match_asignation_rule &#125;&#125;&#160; 
&#160; 
 correspondientes a la nueva clasificacin, que dado que acto seguido se deber regenerar el match , empezarn a aplicarse a la nueva donacin para ampliar sus posibilidades de gestin. 

&#160; 
 Ejemplo &#58; ambiente de produccin donacin en la cuenta maestra &quot; abaco &quot; y clasificada como &quot; abaco_def_0_to_99_kg &quot; 
 El sistema realiza la siguiente consulta para determinar la regla de reclasificacin aplicable 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master= abaco &amp;eatc_origin_match_asignation_rule= abaco_def_0_to_99_kg &amp;_cmp=eatc_destiny_match_asignation_rule &#160; 
&#160; 
 Como la consulta no trae resultados, entonces procede con la siguiente 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_dona_reclassification_rules ?eatc_cua_master= abaco &amp;eatc_origin_match_asignation_rule= _default &amp;_cmp=eatc_destiny_match_asignation_rule &#160; 
&#160; 
 Dado que la respuesta es &quot; reclass_by_ImNotInt &quot;, el sistema procede a reclasificar la donacin de la siguiente manera 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_dona_headers ?&amp;_operacion=update&amp; eatc_match_asignation_rule= reclass_by_ImNotInt &amp;WHEREeatc-code=&#123;&#123; eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Para la anterior regla operan las siguientes reglas de asignacin 
 datagov.eatcloud.info/api/eatcloud/eatc_match_asignation_rules?eatc_match_asignation_rule=reclass_by_ImNotInt &#160; 
&#160; 
 Y las siguientes reglas de ampliacin 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule=reclass_by_ImNotInt &#160; 

&#160; 
 Generar Nuevo Match&#160; ***NUEVO &#58; para estado announced tambin se regenera el match ( eatc_state= announced o eatc_state= awarded o eatc_state= programed) *** 
 Cuando los anuncios estn en estado announced , awarded o programed, se debe generar nuevo match (incorporar nuevas funciones de match) 
&#160; 
 Borrar del match los beneficiarios que ya han rechazado el anuncio en cuestin&#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_match_rejection_registry? eatc_dona_header_code= &#123;&#123; eatc_dona_headers. eatc-code &#125;&#125;&amp;_cmp=eatc_doma_code 
&#160; 
 Con el array de cdigos se procede a borrar los match que se regeneraron para beneficiarios que se haban rechazado 
 &#123;&#123;URL_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM.cua_master/?_tabla=eatc_match_registry&amp;_operacion=deleteeatc-dona_header_code=&#123;&#123;eatc-dona_header_code&#125;&#125;&amp;_cmp=_id,eatc-pod_name,eatc-donation_manager_code,organizacin,matching_since,eatc_match_asignation_rule,eatc_match_asignation_rule_code&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 IM_NOT_INTERESTED