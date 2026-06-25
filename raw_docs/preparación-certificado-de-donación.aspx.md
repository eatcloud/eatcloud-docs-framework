# preparación-certificado-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 preparacin certificado de donacin 
 A esta funcionalidad se accede a travs del men documentado aqu y submen documentado aqu y comprende los siguientes apartados&#58; 
 Diagrama de flujo 
 Selector (nico) de mtodo de soporte del certificado 

 DIAGRAMA DE FLUJO 
 Selector nico de mtodo de soporte de certificado 

 Selector (nico) de mtodo de soporte del certificado&#58; 
 Construccin del selector nico&#58; 
 El sistema, partiendo de la cuenta maestra ( eatc_cua. eatc_cua_master &#160;&#160; o _DOM. cua_master ) de la cuenta en cuestin,&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Debe construir un selector nico de mtodos de soporte para el precertificado a partir de una consulta a la persistencia de los mtodos de soporte de la certificacin ( eatc_dona_certification_supports ) para la cuenta maestra en especfico a partir de la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct= eatc_dona_certification_support 
&#160; 
 El valor de las opciones del selector nico ser el que se obtiene del parmetro que trae la anterior consulta&#58; 
 eatc_dona_certification_supports. eatc_dona_certification_support 
&#160; 
 El label de dichas opciones ser el que se obtiene del parmetro de la misma consulta (y debe funcionar a partir de las funciones de personalizacin e internacionalizacin implementadas) 
 eatc_dona_certification_supports. eatc_label 
&#160; 
 ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct= eatc_label) 
&#160; 
 Debajo de cada opcin seleccionada, debe aparecer una especie de cuadro de informacin que le diga al usuario que consulta la interfaz, lo que implica la misma de cara a la funcionalidad que se desplegar.&#160; Ese label es el que se obtiene del parmetro&#160; 
 eatc_dona_certification_supports. eatc_support_generation_method_desc_label 
&#160; 
 ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct= eatc_support_generation_method_desc_label) 

&#160; 
 Valor por defecto del selector nico&#58; 
 El valor por defecto seleccionado en este selector debe ser el valor consignado en eatc_cua. eatc_default_certification_support &#160; de la cuenta respectiva 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 Valor por defecto si la cuenta no cuenta con un registro en eatc_default_certification_support 
 Si la cuenta no tiene un dato registrado en el parmetro&#58; eatc_cua. eatc_default_certification_support el sistema deber mostrar como valor por defecto seleccionado el que corresponda a esta consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;default= si &amp;_distinct= eatc_dona_certification_support 
&#160; 
 Ejemplo&#58; ambiente productivo, _DOM .cua_master=abaco 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master= abaco &amp;default= si &amp;_distinct= eatc_dona_certification_support &#160;&#160; 
&#160; 
 Como la respuesta del sistema es&#58; 
&#160; 
 eatc_dona_certification_support &#58; &quot;carta_colombia&quot; 
&#160; 
&#160; 
 El soporte por defecto ser &quot; carta_colombia &quot; 

&#160; 
 La interfaz, deber presentar a continuacin la leyenda (label) que se obtiene del parmetro&#58; 
 eatc_dona_certification_supports. eatc_support_generation_method_accept_label 
&#160; 
 Acompaado del botn cuyo label es &quot; lbl_aceptar &quot;. 
&#160; 
 Al presionar el botn aceptar, el sistema deber realizar el siguiente registro para la cuenta en cuestin&#58; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_cua &amp;_operacion=update&amp; eatc_default_certification_support= &#123;&#123;eatc_dona_certification_supports. eatc_dona_certification_support &#125;&#125;&amp;WHEREname=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 Cambio en el valor del selector por parte del usuario&#58; 
 Si el usuario cambia el selector a un valor diferente al registrado en&#160; eatc_cua. eatc_default_certification_support el sistema deber realizar lo siguiente 
&#160; 
 ***NUEVO&#58; Validacin si se cumplen las condiciones para aplicar el mtodo *** 
 Core de la funcionalidad (para una implementacin rpida en primera instancia)&#58; 
&#160; 
 Para el mtodo de soporte &quot; factura_electronica_colombia &quot;, se deber validar si la cuenta particular toma sus donaciones a partir de un maestro de artculos, con la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;eatc_odds_app=eatc_odds&amp;_cont 
&#160; 
 Si la respuesta es&#160; 
 &quot;count&quot; &#58;&#160; &quot;1&quot; 
&#160; 
 quiere decir que el mtodo es vlido (es decir que la cuenta tiene configurada la realizacin de donaciones ( eatc_odds_app ) a partir de un maestro de producto ( eatc_odds ), y por lo tanto puede aceptar el mtodo de factura electrnica colombia y seguir con el proceso de registro como se indica ms adelante . 
&#160; 
 En caso que la respuesta sea&#58; 
 &#160;&quot;count&quot; &#58;&#160; &quot;0&quot; 
&#160; 
 Entonces el sistema debe desplegar el label&#58;&#160; 
 class=&quot;lbl_para_fe_col_eatc_odds&quot; 
&#160; 
 Cuya configuracin para el idioma espaol es&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp; lang =es&amp;idlabel=lbl_para_fe_col_eatc_odds 
&#160; 
 O sea&#58; 
 &quot;Para acceder al mtodo de soporte &quot;Factura electrnica Colombia&quot;, tus donaciones debern configurarse a travs de un maestro de productos que deber ser configurado en la plataforma. Si deseas utilizar este mtodo debes comunicarte con nuestra mesa de ayuda para establecer dicha configuracin.&quot; 
&#160; 
 [Aceptar (class=lbl_aceptar)] 
&#160; 
 Terminando la accin sin haber seleccionado el nuevo mtodo 

&#160; 
 Implementacin avanzada (con querys de validacin en persistencia&#58; para una segunda etapa)&#58; 
 El sistema deber recuperar, a partir del valor seleccionado en el selector ( eatc_dona_certification_supports. eatc_dona_certification_support ), el query&#160; 

&#160; 
 ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp; eatc_dona_certification_support=&#123;&#123; eatc_dona_certification_supports. eatc_dona_certification_support &#125;&#125; &amp;_distinct= eatc_valid_method_if_query ) 
&#160; 
 y la respuesta&#160; 
 ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp; eatc_dona_certification_support=&#123;&#123; eatc_dona_certification_supports. eatc_dona_certification_support &#125;&#125; &amp;_distinct= eatc_valid_method_if_response ) 
&#160; 
 para definir si el mtodo es vlido (segn las condiciones de configuracin de la cuenta).&#160; En caso que el mtodo no sea vlido, deber presentar la respectiva respuesta&#58; 
 ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp; eatc_dona_certification_support=&#123;&#123; eatc_dona_certification_supports. eatc_dona_certification_support &#125;&#125; &amp;_distinct= eatc_invalid_method_resp ) 
&#160; 
 y no permitir el cambio de mtodo (Mostrar el botn con &quot; lbl_aceptar &quot; que permite terminar la accin sin haber seleccionado un nuevo mtodo). 

&#160; 
 Ejemplo 1&#58; ambiente de pruebas, _DOM .cua_master=abaco, _DOM .cua_user=exito, mtodo de soporte seleccionado&#58; ( eatc_dona_certification_supports. eatc_dona_certification_support )&#58; factura_electronica_colombia &#160; 
&#160; 
 El sistema mediante la siguiente consulta, establece el query de validacin de aplicabilidad del mtodo segn las condiciones de configuracin de la cuenta usuario 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master= abaco &amp;eatc_dona_certification_support=factura_electronica_colombia&amp;_distinct= eatc_valid_method_if_query &#160; 
&#160; 
 Como el servicio responde&#58; 
&#160; 
 eatc_valid_method_if_query &#58; &quot;&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;eatc_odds_app=eatc_odds&amp;_cont 
&#160; 
 El sistema deber realizarlo de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_cua?name= exito &amp;eatc_odds_app=eatc_odds&amp;_cont &#160; 
&#160; 
 Como el sistema responde&#58; 
&#160; 
 count &#58; &quot;0&quot; 
&#160; 
 y la respuesta al query de validacin para el mtodo particular es la que se obtiene de la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=abaco&amp;eatc_dona_certification_support=factura_electronica_colombia&amp;_distinct= eatc_valid_method_if_response &#160; 
&#160; 
 Que en particular es&#58; 
&#160; 
 eatc_valid_method_if_response &#58; &quot;count=1&quot; 
&#160; 
 Entonces el sistema determina que el mtodo &quot; factura_electronica_colombia &quot; no es vlido dadas las condiciones de configuracin de la cuenta usuario y por lo tanto debe mostrarle el siguiente label&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=abaco&amp;eatc_dona_certification_support=factura_electronica_colombia&amp;_distinct= eatc_invalid_method_resp 
&#160; 
 Es decir&#58; 
&#160; 
 eatc_invalid_method_resp &#58; &quot;lbl_para_fe_col_eatc_odds&quot; 

&#160; 
&#160; 
 Cuya configuracin para el idioma espaol es&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp; lang =es&amp;idlabel=lbl_para_fe_col_eatc_odds 
&#160; 
&#160; 
 O sea&#58; 
&#160; 
 &quot;Para acceder al mtodo de soporte &quot;Factura electrnica Colombia&quot;, tus donaciones debern configurarse a travs de un maestro de productos que deber ser configurado en la plataforma. Si deseas utilizar este mtodo debes comunicarte con nuestra mesa de ayuda para establecer dicha configuracin.&quot; 
&#160; 
 [Aceptar] 
&#160; 
 Terminando la accin sin haber seleccionado el nuevo mtodo 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, _DOM .cua_master=abaco, _DOM .cua_user=alqueria, mtodo de soporte seleccionado&#58; ( eatc_dona_certification_supports. eatc_dona_certification_support )&#58; factura_electronica_colombia &#160; 
&#160; 
 El sistema mediante la siguiente consulta, establece el query de validacin de aplicabilidad del mtodo segn las condiciones de configuracin de la cuenta usuario 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master= abaco &amp;eatc_dona_certification_support=factura_electronica_colombia&amp;_distinct= eatc_valid_method_if_query &#160;&#160; 
&#160; 
 Como el servicio responde&#58; 
&#160; 
 eatc_valid_method_if_query &#58; &quot;&#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM.cua_user&#125;&#125;&amp;eatc_odds_app=eatc_odds&amp;_cont 
&#160; 
 El sistema deber realizarlo de la siguiente manera 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_cua?name= alqueria &amp;eatc_odds_app=eatc_odds&amp;_cont &#160; &#160; 
&#160; 
 Como el sistema responde&#58; 
&#160; 
 count &#58; &quot;1&quot; 
&#160; 
 y la respuesta al query de validacin para el mtodo particular es la que se obtiene de la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=abaco&amp;eatc_dona_certification_support=factura_electronica_colombia&amp;_distinct= eatc_valid_method_if_response &#160; 
&#160; 
 Que en particular es&#58; 
&#160; 
 eatc_valid_method_if_response &#58; &quot;count=1&quot; 
&#160; 
 Entonces el sistema determina que el mtodo &quot; factura_electronica_colombia &quot; es vlido dadas las condiciones de configuracin de la cuenta usuario y por lo tanto permite terminar el proceso de seleccin cmo se indica ms adelante. 

&#160; 
 Ejemplo 3&#58; ambiente de pruebas, _DOM .cua_master=abaco, _DOM .cua_user=alqueria, mtodo de soporte seleccionado&#58; ( eatc_dona_certification_supports. eatc_dona_certification_support )&#58; carta_colombia &#160; 
&#160; 
 El sistema mediante la siguiente consulta, establece el query de validacin de aplicabilidad del mtodo segn las condiciones de configuracin de la cuenta usuario 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master= abaco &amp;eatc_dona_certification_support=carta_colombia&amp;_distinct= eatc_valid_method_if_query &#160;&#160;&#160; 
&#160; 
 Como el servicio responde&#58; 
&#160; 
 eatc_valid_method_if_query &#58; &quot;&quot; 
&#160; 
 Lo cual indica que no posee un query de validacin, y por lo tanto el mtodo el vlido, entonces se le permite al usuario terminar el proceso de seleccin cmo se indica a continuacin. 

&#160; 
 Despliegue del label de aceptacin de mtodo ante una validacin exitosa 
 Una vez validado el mtodo (como vlido ante las condiciones de configuracin de la respectiva cuenta), el sistema deber mostrar en su interfaz, la leyenda (label) que se obtiene del parmetro&#58; 
 eatc_dona_certification_supports. eatc_support_generation_method_accept_label 
&#160; 
 Acompaado del botn cuyo label es &quot; lbl_aceptar &quot;. 
&#160; 
 Al presionar el botn aceptar, el sistema deber realizar el siguiente registro para la cuenta en cuestin&#58; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_cua &amp;_operacion=update&amp; eatc_default_certification_support= &#123;&#123;eatc_dona_certification_supports. eatc_dona_certification_support &#125;&#125;&amp;WHEREname=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 EJEMPLO&#58; Cuenta &quot;EXITO&quot; 
&#160; 
 Dado que la cuenta maestra del &quot; exito &quot; es &quot; abaco &quot; (segn lo que arroja el parmetro eatc_cua_master de la consulta https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name=exito ), entonces el sistema debe construir un selector nico que contenga los siguientes valores (que se obtienen de la siguiente consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_certification_supports?eatc_cua_master=abaco ) 
 carta_colombia (el label de esta opcin se construye con class=&quot; lbl_carta &quot; ) 
 factura_electronica_colombia (el label de esta opcin se construye con class=&quot; lbl_factura_electronica_colombiana &quot; ) 
&#160; 
 Como la cuenta exito no tiene ningn valor en el parmetro &quot; eatc_default_certification_support &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name=exito ), la opcin seleccionada ser ( https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ?eatc_cua_master=abaco&amp;default= si ) 
 carta_colombia (el label de esta opcin se construye con class=&quot; lbl_carta &quot; ) 
&#160; 
 Debajo de esta opcin se presenta el label&#58; 
 lbl_anuncios_cuyo_soporte_se_genera_automaticament ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_anuncios_cuyo_soporte_se_genera_automaticament ) y tambin dado que no tena registro a continuacin debe registrar mostrar este label. 
 lbl_aceptacion_metodo_carta_colombia ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_aceptacion_metodo_carta_colombia ) acompaado del botn aceptar ( class=&quot; lbl_aceptar &quot; ).&#160;&#160; 
&#160; 
 Si el usuario lo presiona (sin cambiar la opcin), el sistema realizar el siguiente llamado para actualizar los datos de la cuenta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla= eatc_cua &amp;_operacion=update&amp; eatc_default_certification_support= carta_colombia&amp;WHEREname=exito (si se realizan pruebas con este llamado se solicita devolverlo a su estado original &quot;vaco&quot; una vez se terminen las comprobaciones) 

 Mtodo de soporte&#58; carta_colombia 
&#160; 
 Mtodo de soporte&#58; factura_electronica_colombia 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Datagov_cuentas 

 PREPARACIN CERTIFICADO DE DONACIN