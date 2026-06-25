# net-promoter-score.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Componente que se debe desarrollar, de tal manera que sea fcilmente embebible en las diferentes plataformas (donantes, webapp, beneficiarios, App, datagov_cuentas). 
&#160; 
 Esta herramienta de evaluacin de las diversas plataformas, se constituye en una pregunta de tipo calificacin (de 0 a 10) acompaada de una pregunta adicional opcional.&#160; A continuacin se dan varios ejemplos de su diseo 

 Llamado de la funcionalidad 
 La funcionalidad se deber llamarse como servicio, desde las diferentes plataformas, especificando que plataforma , qu cuenta y que usuario lo hace de la siguiente manera&#58; 
&#160; 
 La URL que se propone para este es&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;eatc_cua. name &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform=&#123;&#123; eatc_plataform &#125;&#125;&amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 A partir de este llamado el sistema debe realizar las siguientes operaciones&#58; 

 Despliegue de la funcionalidad 
 La funcionalidad se deber desplegar con una periodicidad definida en la siguiente configuracin&#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_nps_parameters?eatc_key=nps_frecuency_in_days 
&#160; 
 eatc_value 
 El sistema deber establecer si el usuario particular (de la cuenta particular), no tenga un registro de NPS en el repositorio correspondiente ( eatc_nps_registry ) en el tiempo que se establece en el parmetro consultado ( eatc_value ). La consulta se realiza de la siguiente manera (con los parmetros recibidos desde el llamado a servicio de integracin)&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_nps_registry?eatc_cua=&#123;&#123;eatc_cua. name &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform=&#123;&#123; eatc_plataform &#125;&#125;&amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 El sistema debe tomar el registro ms reciente (segn el parmetro eatc_date y compararlo con la fecha actual.&#160; Si la diferencia en das de la fecha actual con la fecha del ltimo registro, es menor a eatc_nps_parameters . eatc_value entonces el servicio no debe enviar una respuesta negativa, que le indicar a cada una de las plataformas, que no debe desplegar la funcionalidad.&#160; Si la diferencia entre la fechas evaluadas es mayor a eatc_nps_parameters . eatc_value , el sistema debe enviarle una respuesta afirmativa a la plataforma que le indique que debe desplegar el formulario con las etiquetas definidas ms arriba. 
&#160; 
 Se debe evaluar si como mecanismo de integracin, la respuesta del servicio puede ser el cdigo que cada plataforma debe embeber para desplegar el formulario (que idealmente debe desplegarse en la parte superior de la pantalla).&#160; El desarrollador deber evaluar si esto es factible o si en cada plataforma se debe &quot;disear&quot; el formulario respectivo para desplegarlo. 

 Etiquetas de la funcionalidad 
 Los textos que se utilizarn en esta funcionalidad se debern reemplazar por labels, con el nimo de obtener una funcionalidad internacionalizada de base, y se debern configurar de la siguiente manera&#58; 

 Pregunta principal&#58; 
 nps_main_question ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_main_question ) 
&#160; 
 Lmite inferior&#58; 
 nps_lower_limit_label ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_lower_limit_label ) 
&#160; 
 Lmite superior&#58; 
 nps_upper_limit_label ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_upper_limit_label ) 
&#160; 
 Pregunta secundaria&#58; 
 nps_secundary_question ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_secundary_question ) 
&#160; 
 Envo del formulario&#58; 
 nps_submit_btn ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_submit_btn ) 
&#160; 
 De manera ideal el formulario deber presentarse en dos partes, la primera para enviar el NPS (al marcar una opcin de puntaje del 0 al 10 se debe proceder a guardar el registro respectivo y a pasar a la segunda parte del formulario) y la segunda para la pregunta secundaria (que el usuario la podr responder de manera opcional, llenando el cuadro de texto y oprimiendo el submit o simplemente descartarla cerrando esta parte del formulario. 

 FORMULARIO NPS_MAIN_QUESTION 
 Este formulario deber permitir la captura de un entero de 0 a 10 (de manera obligatoria), y a partir de dicha seleccin realizar la calificacin cualitativa del NPS y enviar los parmetros bsicos para la creacin del registro, obteniendo el ID del mismo.&#160; Con este ID se pasa a la segunda parte del formulario. Estas acciones se debern realizar cuando se oprime el nmero respectivo y se deber pasar a la segunda parte del formulario. 

 Llamado al servicio de creacin del registro&#58; 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;eatc_cua. name &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform=&#123;&#123; eatc_plataform &#125;&#125;&amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125;&amp;_operacion= insert 
&#160; 
 Con estos parmetros se construyen los siguientes parmetros para la creacin del registro&#58; 
&#160; 
 &#123;&#123;parametros_creacion_registro_nps&#125;&#125; 
&#160; 
 eatc_datetime 
 timestamp de la fecha y hora actual 
&#160; 
 eatc_date 
 datestamp de la fecha actual 
&#160; 
 eatc_plataform 
 Plataforma desde la cual se realiza el registro (donantes, webapp,beneficiacios, App, datagov_cuentas)&quot;, 
&#160; 
 eatc_enviroment 
 eatc_enviroment (se toma del llamado al servicio de insercin) 
&#160; 
 eatc_cua 
 eatc_cua (se toma del llamado al servicio de insercin) 
&#160; 
 Con el valor eatc_cua que se obtiene del llamado al servicio se procede a realizar la siguiente consulta&#58;&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= eatc_cua y con los datos recibidos se realizarn los siguientes registros&#58; 
&#160; 
 eatc_vertical 
 eatc_vertical (que trae la consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= eatc_cua) 
&#160; 
 eatc_cua_size 
 eatc_cua_size&#160; (que trae la consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= eatc_cua) 
&#160; 
 eatc_licence_type 
 type&#160; (que trae la consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= eatc_cua) 
 eatc_user_code 
 eatc_user_code (se toma del llamado al servicio de insercin) 
&#160; 
 nps 
 Valor de la calificacin otorgada para el NPS en el formulario de calificacin (un entero de 0 a 10) 
&#160; 
 nps_qualification 
 A partir del valor de la calificacin otorgada para el NPS en el formulario de calificacin (un entero de 0 a 10) se hace el registro de la siguiente manera&#58; 
&#160; 
 Si la calificacin fue de 0 a 6&#58; detractor 
 Si la calificacin fue de 7 a 8&#58; pasivo 
 .Si la calificacin fue de 9 a 10&#58; promotor 

&#160; 
 Creacin del registro en la tabla eatc_nps_registry 
 Se realiza la respectiva insercin con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_nps_registry &amp;_operacion=insert&amp;&#123;&#123;parametros_creacion_registro_nps&#125;&#125; 
&#160; 
 Se debe obtener el _id del registro realizado, con el nimo de pasarlo al segundo formulario para hacer la actualizacin respectiva. 

 FORMULARIO NPS_SECUNDARY_QUESTION 
 Este formulario deber permitir de manera opcional realizar el registro de la pregunta secundaria formulada, y con esta informacin hacer la edicin del registro de NPS respectivo 

 Llamado al servicio de creacin del registro&#58; 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma=&#123;&#123; plataforma &#125;&#125;&amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
&#160; 
 Este llamado se debe realizar cuando se oprime el botn cuyo label es &quot; nps_submit_btn &quot; . 
&#160; 
 &#123;&#123;parametros_creacion_registro_nps&#125;&#125; 
&#160; 
 nps_secundary_question 
 Con los parmetros recibidos en el llamado el sistema debe hacer la siguiente consulta para obtener la respectiva pregunta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= nps_secundary_question &amp;lang= lang &amp;plataforma= plataforma &#160; 
&#160; 
 Se toma el valor que devuelve el parmetro copy&#160; 
&#160; 
 nps_secundary_answer 
 nps_secundary_answer (Respuesta a la pregunta opcional que se hace en conjunto con el NPS) 
&#160; 
 Actulizacin del registro en la tabla eatc_nps_registry 
 Se realiza la respectiva insercin con el siguiente llamado&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_nps_registry &amp;_operacion=update&amp;&#123;&#123;parametros_creacion_registro_nps&#125;&#125;&amp;WHERE_id= eatc_nps_registry_id 
&#160; 
 Botn salir (X en la parte superior izquierda del formulario) 
 Al oprimir la X en la parte superior del formulario, se cierra el mismo sin realizar registro. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnet-promoter-score%2F3358362503-EmbeddedImage---2024-07-30T163958.996.jpg&ow=1184&oh=690, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnet-promoter-score%2F3358362503-EmbeddedImage---2024-07-30T163958.996.jpg&ow=1184&oh=690 

 893.000000000000 

 NET PROMOTER SCORE