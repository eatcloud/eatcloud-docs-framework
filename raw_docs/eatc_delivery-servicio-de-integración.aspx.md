# eatc_delivery-servicio-de-integración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se debe disponibilizar un servicio web que se invoque de la siguiente manera, el cual leer datos del encabezado de anuncio de donacin y a partir de los mismos crear registros en las plataformas demos o apps para interactuar con la app de delivery. 
&#160; 
 La URL que se propone para este es&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/int/&#123;&#123;_DOM.cua_master&#125;&#125;/int_eatc_delivery?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_operacion= insert 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/int/&#123;&#123;_DOM.cua_master&#125;&#125;/int_eatc_delivery?eatc_dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_operacion= update 
&#160; 
 A partir de este llamado el sistema debe realizar las siguientes operaciones&#58; 
&#160; 
 Determinacin URL_delivery&#58; 
 A partir de la URL del servicio y de acuerdo al entorno en el que se est trabajando el sistema hace la siguiente asignacin&#58; 
&#160; 
 Si URL_entorno_donantes corresponde al entorno de pruebas , entonces URL_delivery= https&#58;//demos.nzzn.co 
&#160; 
 Si URL_entorno_donantes corresponde al entorno de produccin , entonces URL_delivery= https&#58;//apps.nzzn.co 

 Lectura de los datos del encabezado del anuncio de donacin (que son la fuente de datos) 
 El sistema deber realizar la siguiente lectura 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Para obtener estos datos especficos&#58; 
&#160; 
eatc_dona_headers. eatc-code 
eatc_dona_headers. eatc-pod_name 
eatc_dona_headers. eatc-pod_address 
eatc_dona_headers. eatc-picker_doc_id 
eatc_dona_headers. eatc-picker_name 
eatc_dona_headers. eatc-picker_license_plate 
eatc_dona_headers. eatc-verification_code 
eatc_dona_headers. eatc-total_weight_kg 
eatc_dona_headers. eatc-programed_picking_datetime 
&#160; 
 Que sern los datos con los cuales se realizarn las escrituras en las tablas de delivery 

 Escritura en la tablas de demos y apps 
 Evaluar si se extienden los servicios CRD a las plataformas DEMOS y APPS para realizar esta escritura 
 Se debe evaluar si como estrategia de implementacin, se extienden el servicio CRD a las plataformas DEMOS y APPS para realizar esta escritura 

&#160; 
 Validacin de la existencia del usuario (usuarios)&#58; 
 Para realizar dicha escritura se deben tomar los siguientes parmetros a partir de la consulta del respectivo anuncio&#58; 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/api/delivery/ usuarios ? m2z_id =&#123;&#123;eatc_dona_headers. eatc-picker_doc_id &#125;&#125; 
&#160; 
 Si no existe el usuario, se procede a realizar el registro en usuario&#58; 
 Para realizar dicha escritura se deben tomar los siguientes parmetros a partir de la consulta del respectivo anuncio&#58; 
&#160; 
 &#123;&#123;parametros_creacion_usuario&#125;&#125; 
 m2z_id = eatc_dona_headers. eatc-picker_doc_id 
 m2z_password = eatc_dona_headers. eatc-picker_license_plate 
 m2z_nombre = eatc_dona_headers. eatc-picker_name 
 vehiculo = eatc_dona_headers. eatc-picker_license_plate 
&#160; 
 Escritura (si se extiende CRD)&#58; 
 En caso de no extender el servicio CRD se debe tomar como referencia para la escritura 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/crd/ delivery /?_tabla= usuarios &amp;_operacion= insert &amp;&#123;&#123; parametros_creacion_usuario &#125;&#125; 
&#160; 
 Luego de registrar el usuario o si el usuario existe se debe proceder a realizar lo siguientes registros&#58; 
&#160; 
 Escritura en la tabla clientes (mt_clientes)&#58; 
 Para realizar dicha escritura se deben tomar los siguientes parmetros a partir de la consulta del respectivo anuncio&#58; 
&#160; 
 &#123;&#123;parametros_creacion_cliente&#125;&#125; (_operacion=insert) 
 m2z_usuario = eatc_dona_headers. eatc-picker_doc_id 
 direccion = eatc_dona_headers. eatc-pod_address 
 m2z_id = eatc_dona_headers. eatc-code 
 m2z_nombre = eatc_dona_headers. eatc-pod_name 
 codigo = eatc_dona_headers. eatc-verification_code 
 peso = eatc_dona_headers. eatc-total_weight_kg 
&#160; 
 Escritura (si se extiende CRD)&#58; 
 En caso de no extender el servicio CRD se debe tomar como referencia para la escritura 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/crd/ delivery /?_tabla=mt_clientes&amp;_operacion=insert&amp;&#123;&#123; parametros_creacion_cliente &#125;&#125; 
&#160; 
 &#123;&#123;parametros_edicion_cliente&#125;&#125; (_operacion=update) 
 m2z_usuario = eatc_dona_headers. eatc-picker_doc_id 
 m2z_id = eatc_dona_headers. eatc-code 
&#160; 
 Edicin (si se extiende CRD)&#58; 
 En caso de no extender el servicio CRD se debe tomar como referencia para la escritura 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/crd/ delivery /?_tabla=mt_clientes&amp;_operacion=update&amp;&#123;&#123; parametros_edicion_cliente &#125;&#125;&amp;WHERE m2z_id =&#123;&#123;eatc_dona_headers. eatc-code&#125;&#125; 
&#160; 
 Escritura en la tabla agenda (mt_ruteros_agenda)&#58; 
 Para realizar dicha escritura se deben tomar los siguientes parmetros a partir de la consulta del respectivo anuncio&#58; 
&#160; 
 &#123;&#123;parametros_creacion_rutero&#125;&#125; (_operacion=insert) 
 m2z_usuario = eatc_dona_headers. eatc-picker_doc_id 
 m2z_id = eatc_dona_headers. eatc-code 
 m2z_fecha_hora = eatc_dona_headers. eatc-programed_picking_datetime 
&#160; 
 Escritura (si se extiende CRD)&#58; 
 En caso de no extender el servicio CRD se debe tomar como referencia para la escritura 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/crd/ delivery /?_tabla= mt_ruteros_agenda &amp;_operacion=insert&amp;&#123;&#123; parametros_creacion_rutero &#125;&#125; 
&#160; 
 &#123;&#123;parametros_edicion_rutero&#125;&#125; (_operacion=update) 
 m2z_usuario = eatc_dona_headers. eatc-picker_doc_id 
 m2z_fecha_hora = eatc_dona_headers. eatc-programed_picking_datetime 
 m2z_id = eatc_dona_headers. eatc-code 
&#160; 
 Edicin (si se extiende CRD)&#58; 
 En caso de no extender el servicio CRD se debe tomar como referencia para la escritura 
&#160; 
 &#123;&#123; URL_delivery &#125;&#125;/crd/ delivery /?_tabla= mt_ruteros_agenda &amp;_operacion=update&amp;&#123;&#123; parametros_edicion_rutero &#125;&#125;&amp;WHERE m2z_id =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIO DE INTEGRACIN CON EATC_DELIVERY