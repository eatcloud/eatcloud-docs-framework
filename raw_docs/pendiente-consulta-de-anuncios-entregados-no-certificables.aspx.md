# pendiente-consulta-de-anuncios-entregados-no-certificables.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 C ONSULTA DE ANUNCIOS ENTREGADOS NO CERTIFICABLES &#58; 
&#160; 
 Botn del men lateral 
 El sistema deber presentar un botn con el siguiente label (en el men lateral) 
 label&#58; class=&quot;lbl_donaciones_no_certificables&quot;&#160; 
&#160; 
 Y que pueda mostrar la siguiente descripcin (puede ser como un tooltip)&#58; 
 label&#58; class=&quot;lbl_donaciones_no_certificables_tooltip&quot;&#160; 
&#160; 
 El sistema presentar un botn, a partir del cual se generar un listado de los anuncios cuyo estado es &quot;delivered&quot; y que estn pendientes de verificacin.&#160; La funcionalidad tambin presentar la posibilidad de sealar los anuncios con problemas y enviar un mensaje a soporte tcnico y a las fundaciones para solicitar que sean verificados. 
&#160; 
 El botn deber persentar un globo de advertencia si la siguiente consulta trae datos (ideal que en el mismo aparezca el valor del cont respectivo) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state=delivered&amp; eatc-receipt_datetime = 0000-00-00%2000&#58;00&#58;00&amp;_compress 
&#160; 
 Funcionalidad de visualizacin de anuncios pendientes por gestin 
 Al presionar el botn de men, se debe entrar a una funcionalidad, cuyo ttulo es&#58; 
 label&#58; class=&quot;lbl_titulo_donaciones_no_certificables&quot;&#160; 
&#160; 
 Y abajo de dicho ttulo colocar la siguiente descripcin&#58; 
 label&#58; class=&quot;lbl_donaciones_no_certificables_desc&quot;&#160; 
&#160; 
 Consulta para traer las donaciones pendientes de gestin 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state=delivered&amp; eatc-receipt_datetime = 0000-00-00%2000&#58;00&#58;00&amp;_compress 
&#160; 
 A continuacin se presenta una lista que contiene la siguiente informacin de los anuncios que trae la anterior consulta, ordenando primero aquellos cuya fecha y hora de publicacin ( eatc_dona_headers .eatc-publication_datetime ) sea la ms antigua&#58; 
&#160; 
 Cdigo del anuncio 
label&#58; class=&quot; lbl_codigo_anuncio &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Fecha y hora 
label&#58; class=&quot; lbl_hora_publicacion &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Estado 
label&#58; class=&quot; lbl_estado &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-state 
&#160; 
 Cdigo Punto de donacin 
label&#58; class=&quot; lbl_codigo_punto_donacion &quot;&#160; 
 La informacin se toma de&#58; eatc_dona .eatc-pod_id 
&#160; 
 Punto de donacin 
label&#58; class=&quot; lbl_pod &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Direccin punto de donacin (OJO ID) 
label&#58; id=&quot; lbl_direccion_punto_donacion &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-pod_address 
&#160; 
 Ciudad 
label&#58; class=&quot; lbl_ciudad &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-city 
&#160; 
 KG Originales 
label&#58; class=&quot; kg_originales &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers . eatc-original_weight_kg ) 
&#160; 
 Costo original 
label&#58; class=&quot; kg_costo_original &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers . eatc-original_cost 
&#160; 
 Porcentaje IVA 
label&#58; class=&quot; lbl_porcentaje_iva &quot;&#160; 
 La informacin se toma de&#58; eatc_dona .eatc-VAT_percentage 
&#160; 
 Tarifa IVA 
label&#58; class=&quot; lbl_valor_iva &quot;&#160; 
 La informacin se toma de&#58; eatc_dona .eatc-total_VAT 
&#160; 
 Beneficiario 
label&#58; class=&quot; lbl_beneficiario &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Beneficiario direccin 
label&#58; class=&quot; lbl_direccion_beneficiario &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-donation_manager_adress 
&#160; 
 Beneficiario telfono 
label&#58; class=&quot; lbl_telefono &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-donation_manager_phone 
&#160; 
 Hora de adjudicacin 
label&#58; class=&quot; lbl_hora_adjudicacion &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Hora de entrega real&#58; llegada 
label&#58; class=&quot; lbl_hora_entrega_real_llegada &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Hora de entrega real&#58; salida 
label&#58; class=&quot; lbl_hora_entrega_real_salida &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Fecha recepcin 
label&#58; class=&quot; lbl_hora_recepcion &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-receipt_datetime (debe estar en ceros, dado que es una condicin que se tiene en cuenta en la consulta para traer los datos) 
&#160; 
 Documento soporte 
label&#58; class=&quot; lbl_documento_soporte &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-doc 
&#160; 
 Alerta 
label&#58; class=&quot; lbl_alerta &quot;&#160; 
 La informacin se toma de&#58; eatc_dona_headers .eatc-warning 

&#160; 
 Botn&#58; Enviar solicitudes de gestin&#58; 
 En la parte superior del listado debe colocarse un botn con la siguiente leyenda 
 label&#58; class=&quot; lbl_enviar_mensajes_solicitando_gestion &quot;&#160; 
&#160; 
 Al presionar el botn, se deber desplegar un modal o una pgina en donde aparezca lo siguiente&#58; 
&#160; 
 Ttulo 
 label&#58; class=&quot; lbl_titulo_enviar_mensajes_solicitando_gestion &quot;&#160; 
&#160; 
 El ttulo del modal o de la pgina ser 
&#160; 
 &quot; Enviar mensajes solicitando de gestin &quot; 
&#160; 
 Descripcin 
 label&#58; class=&quot; lbl_enviar_mensajes_solicitando_gestion_desc &quot;&#160; 
&#160; 
 Abajo del ttulo se colocar la siguiente leyenda. 
&#160; 
 &quot; Con esta funcionalidad, podrs generar mensajes automticos a todas las organizaciones que tienen gestiones pendientes para poder otorgarles a las donaciones que se les han entregado el estatus de &quot;recibidas&quot;, necesario para poder ser certificables.&quot; 
&#160; 
 Remitente 
 label&#58; class=&quot;lbl_remitente&quot;&#160; 
&#160; 
 A manera de un mensaje, se colocar&#58; &quot; Remitente&#58; &#123;&#123;nombre_donante&#125;&#125; &quot; 
&#160; 
 El nombre del donante se toma de&#58; &#160; 
&#160; 
 Con el dato _DOM. cua_user se realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Con la respuesta obtenida se toma el _id para realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua,eatc_customer_fiscal_id &amp;&amp;filterfield_1=_id&amp;filtervalue_1=&#123;&#123; eatc_customers_cua._id &#125;&#125; 
&#160; 
 Con esto se obtiene el valor desencriptado de eatc_customers_cua. eatc_customer_fiscal_id &#160; y con l se realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_name &amp;&amp;filterfield_1= eatc_fiscal_id &amp;filtervalue_1=&#123;&#123; eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; 
&#160; 
 El valor que se obtiene de esta ltima consulta ser el remitente se guarda en la variable &#123;&#123; remitente &#125;&#125; 
&#160; 
 Mensaje por defecto 
 En un campo de captura de texto, debajo del nombre del remitente, de manera predeterminada (a manera de una especie de &quot;place holder&quot; o valor por defecto), debe aparecer el siguiente mensaje, que el usuario podr editar a su antojo&#58; 
 label&#58; class=&quot;lbl_mensaje_solicitando_gestion&quot;&#160; 
&#160; 
 &quot; Les solicitamos amablemente la gestin de los anuncios pendientes (por programar, recoger o verificar) que hemos entregado a su organizacin. Dicha gestin es fundamental para la emisin del respectivo certificado y por lo tanto importante para nosotros.&#160; De antemano muchas gracias por la atencin recibida &quot; 
&#160; 
 El mensaje (por defecto o editado por el donante) se guarda en una variable &#123;&#123; mensaje_solicitud_gestion &#125;&#125; 
&#160; 
 eatc_message_type 
 El tipo de mensaje en este caso ser una constante y la misma es&#58; mis_donaciones 
&#160; 
 display_conditions 
 La condicin de despliegue del mensaje ser una constante y la misma es&#58; hasta_gestion_anuncios , y la misma quiere decir que el mensaje se mostrar hasta que se culminen de gestionar las donaciones que promovieron el mensaje.&#160; Para evaluar el cumplimiento de dicha condicin se utilizan los dos siguientes parmetros (nuevos)&#58; display_query y display_query_response 

&#160; 
 Botn&#58; &quot;Enviar&quot;&#58; 
 label&#58; class=&quot; lbl_enviar &quot;&#160; 
&#160; 
 Al presionar el botn, se deber&#160; hacer un distinct sobre el dato eatc_dona_headers . eatc-donation_manager_code de la consulta original y para cada gestor de donaciones (beneficiario) realizar la siguiente escritura de datos, tomando el timestamp con la fecha y hora en la cual se oprime el botn, el dato &#123;&#123;_DOM. cua_user &#125;&#125; y las siguientes condiciones de despliegue del mensaje &#58; 
&#160; 
 display_query 
 En este caso se enva la bsqueda que est dando como resultado el envo del mensaje (reemplazando los valores con los datos respectivos).&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-state=delivered&amp; eatc-receipt_datetime = 0000-00-00%2000&#58;00&#58;00 
&#160; 
 Nota para el desarrollador&#58; se deber evaluar si se enva este query o a partir del mismo se toman los datos que se obtienen del campo eatc_dona_headers. eatc-code y con el &#123;&#123;array_de_codigos&#125;&#125; obtenido se enva en el campo la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donation_manager_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;eatc-state=delivered&amp; eatc-receipt_datetime = 0000-00-00%2000&#58;00&#58;00 &amp;eatc-code= &#123;&#123;array_de_codigos&#125;&#125; 
&#160; 
 La url que se obtiene (con los valores respectivos) se guarda en la variable &#123;&#123; query_url &#125;&#125; 
&#160; 
 display_query_response 
 Dado que el mensaje se debe mostrar hasta qu no se gestionen las donaciones del donante remitente, el mensaje se deber mostrar hasta que la anterior consulta traiga resultados, es decir que en este caso, se registra en el campo la constante&#58; valid 

&#160; 
 &#123;&#123; URL_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_doma_messages &amp;_operacion= insert &amp;date=&#123;&#123; timestamp &#125;&#125;&amp;eatc_message_type= mis_donaciones &amp;title= Mensaje %20 importante %20 de %20&#123;&#123; remitente &#125;&#125; &amp;message=&#123;&#123; mensaje_solicitud_gestion &#125;&#125;&amp;eatc_doma_code=&#123;&#123;eatc_dona_headers. eatc-donation_manager_code &#125;&#125;&amp;display_conditions= hasta_gestion_anuncios &amp;display_time_sec=fix&amp;display_query= &#123;&#123; query_url &#125;&#125; &amp;display_query_response= valid 
&#160; 
 El mensaje ha sido enviado a&#58; 
 label&#58; class=&quot;lbl_mensaje_enviado_a&quot;&#160; 
&#160; 
 Una vez se realiza las escrituras de los mensajes, a manera de confirmacin, el sistema muestra un mensaje&#58; 
&#160; 
 Mensaje enviado a&#58; &#123;&#123;listado_nombres_beneficiarios&#125;&#125; 
&#160; 
 A continuacin se presenta un listado que resulta del sect_distinct realizado sobre el dato&#58; eatc_dona_headers .eatc-donation_manager_name de la consulta original . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PENDIENTE: CONSULTA DE ANUNCIOS ENTREGADOS NO CERTIFICABLES