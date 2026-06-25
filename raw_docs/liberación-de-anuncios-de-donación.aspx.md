# liberación-de-anuncios-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Liberacin de anuncios por no programar recogida despus de una hora de aceptar el anuncio ***IMPLEMENTAR dinamismo para mltiples cuentas usuario *** . 
&#160; 
 El sistema debe liberar anuncios de donacin que hallan sido adjudicados, pero que el adjudicatario no haya programado su recogida despus del tiempo determinado en la persistencia eatc_timeout_rules de haber aceptado el anuncio. 
&#160; 
 El proceso de liberacin de anuncios debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_* 
&#160; 
 Este ajuste aplica tanto para los procesos activados por tareas programadas como los que son activados mediante servicios web (en caso de existir). 
&#160; 
 NUEVO Proceso por cuenta usuario 
&#160; 
 Para obtener el tiempo a partir del cual se debe liberar un anuncio no programado se debe realizar la siguiente manera 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules? cua=&#123;&#123; _DOM. cua_user&#125;&#125; &amp; eatc-timeout_name=dona_particular_scheduling_timeout &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 
&#160; 
 Si la anterior consulta no da resultado entonces el sistema responde debe volver a intentar con la consulta por _default 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_timeout_rules? cua=_default &amp; eatc-timeout_name=dona_particular_scheduling_timeout &amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from 

&#160; 
 Un ejemplo del caso particular esta regla de timeout se consulta de la siguiente manera&#58;&#160; 
&#160; 
 Ejemplo 1&#58; eatc_cua_master. eatc_cua=abaco, _DOM. cua_user=exito ambiente de productivo&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules? cua=exito&amp; eatc-timeout_name=dona_particular_scheduling_timeout&amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from &#160; &#160;&#160; 
 &#160; 
 Como la respuesta es&#58;&#160; 
 &#123; 
 ts &#58; &quot;230420150417&quot; , 
 op &#58; true , 
 cont &#58; 0 , 
 err_msg &#58; &quot;No se produjeron resultados&quot; , 
 err_num &#58; &quot;&quot; , 
 mem &#58; 0.41 , 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; &#160; 
&#160; 
 Entonces se procede a realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules? cua=_default&amp; eatc-timeout_name=dona_particular_scheduling_timeout&amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from &#160; &#160;&#160;&#160; 
&#160; 
 Dado que la respuesta es&#58;&#160; 
&#160; 
 &#123; 
 eatc-timeout_in_minutes &#58; &quot;60&quot;, 
 eatc-timeout_from &#58; &quot;eatc-adjudication_datetime&quot;, 
 &#125; 
&#160; 
 El sistema no debe liberar la donacin despus de ( eatc-timeout_in_minutes ) 60 minutos contados a partir del ( eatc-timeout_from ) eatc-adjudication_datetime , si no se ha programado la recogida. 
&#160; 
&#160; 
 Ejemplo 2&#58; eatc_cua_master. eatc_cua=abaco, _DOM. cua_user=terpel ambiente de productivo&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_timeout_rules? cua=terpel&amp; eatc-timeout_name=dona_particular_scheduling_timeout&amp;_cmp= eatc-timeout_in_minutes,eatc-timeout_from &#160; &#160;&#160;&#160; 
 &#160; 
 Dado que la respuesta es&#58;&#160; 
&#160; 
 &#123; 
 eatc-timeout_in_minutes &#58; &quot;10&quot;, 
 eatc-timeout_from &#58; &quot;eatc-adjudication_datetime&quot;, 
 &#125; 
&#160; 
 El sistema no debe liberar la donacin despus de ( eatc-timeout_in_minutes ) 10 minutos contados a partir del ( eatc-timeout_from ) eatc-adjudication_datetime , si no se ha programado la recogida. 
&#160; 
 Consulta de anuncios ***DINAMIZAR para mltiples cuentas maestras***&#58;&#160; 
 El sistema debe consultar aquellos anuncios con estado ( eatc-state )&#160; &quot;awarded&quot; (adjudicados) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125;/eatc_dona_headers?eatc-state=awarded&#160;&#160;&#160; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=awarded &#160;&#160;&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=awarded&amp;_compress &#160; 
&#160; 
 Comparaciones&#58;&#160; 
 Posteriormente debe comparar el campo &quot; eatc-adjudication_datetime &quot;, con la fecha y hora actual.&#160; Si la diferencia entre la fecha y hora actual y la fecha de adjudicacin es superior a una hora y no hay informacin registrada (o est en cero o que no tenga una fecha de programacin vlida) en el campo &quot; eatc-programed_picking_datetime &quot; (o tambin en este &quot; eatc-scheduling_datetime &quot;) , debe ejecutar las siguientes acciones&#58;&#160; 

&#160; 
 Accin 1&#58; Actualizacin de la informacin del encabezado de donacin ( eatc_dona_headers ) 
 Al liberar el&#160; anuncio de donacin se debe actualizar la siguiente informacin&#58; 
&#160; 
 eatc-state&#58; debe cambiar de &quot;awarded&quot; a &quot;announced&quot;. 
 eatc-adjudication_datetime&#58; &#160; se debe borrar 
 eatc-donation_manager_user_doc_id&#58; se debe borrar 
 eatc-donation_manager_code&#58; se debe borrar pero guardarlo en una variable temporal para el prximo registro 
 eatc-donation_manager_name&#58; se debe borrar pero guardarlo en una variable temporal para el prximo registro 
 eatc-donation_manager_address&#58; se debe borrar 
 eatc-donation_manager_phone &#58; se debe borrar 
 eatc-donation_manager_typology_a&#58; se debe borrar 
 eatc-donation_manager_typology_b&#58; se debe borrar 
 eatc-donation_manager_typology_c&#58; se debe borrar 
&#160; 
 Accin 2&#58; registro en el historial de los estados de los anuncios de donaciones ( eatc_dona_header_state_history ) ***DINAMIZAR para mltiples cuentas maestras*** 
 Se debe registrar el estado &quot;announced&quot; procurando incorporar la informacin del adjudicatario al cual se le elimin la adjudicacin, en el campo ( eatc-log )&#160; 
&#160; 
 eatc-dona_header_code =[ eatc_dona_headers .eatc-code] 
 eatc-state = annouced 
 eatc-date_time =[datetime] 
 eatc-log =&quot;EatCloud anul la adjudicacin al usuario $[eatc-donation_manager_code] $[eatc-donation_manager_name] por demora en la programacin&#160; de recogida&quot; 
&#160; 
 Utilizando el API el registro sera algo como lo siguiente 
&#160; 
 Registro del estado &quot;annouced&quot; &#58;&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_cua &#125;&#125; /?_tabla= eatc_dona_header_state_histor y &amp;_operacion=insert&amp; eatc-dona_header_code =&#123;&#123;eatc-code&#125;&#125;&amp; eatc-state = annouced &amp; eatc-date_time =&#123;&#123;datetime&#125;&#125;&amp; eatc-log =&quot;EatCloud se le liber al usuario &#123;&#123;eatc-donation_manager_code&#125;&#125; &#123;&#123;eatc-donation_manager_name&#125;&#125; por demora en la programacin&#160; de recogida&quot; 

 ***NUEVO &#58;&#160; Llamado al servicio para la regeneracin del match *** 
 Con los parmetros &#123;&#123; cua_master&#125;&#125; y &#123;&#123; eatc_dona_header_code&#125;&#125; recibido en la invocacin del servicio, y una vez realizados los anteriores registros, se procede a realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_dona_headers?eatc-code= &#123;&#123; eatc_dona_header_code&#125;&#125; &amp;_cmp= . eatc_match_asignation_rule ,eatc-lat,eatc-lon, eatc-total_weight_kg 
&#160; 
 Con los datos obtenidos en la anterior consulta y con los datos que llegan en el llamado del presente servicio , se procede a realizar el llamado al servicio para el registro del match correspondiente. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 LIBERACIN DE ANUNCIOS DE DONACIN