# resumen-pedido-licencias-analytics.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante para el desarrollo 
 El siguiente wireframe, fue desarrollado inicialmente para confirmacin de pedido de licencias rescate, pero basndonos en el diseo (que no est corregido en este aspecto) se resaltarn en AZUL , nuevos llamados a API y consideraciones para adaptar el desarrollo realizado inicialmente para las licencias rescate, pero para las licencias analytics.&#160; Adems presenta el diseo para una pgina que tambin servir para la realizacin del proceso de check-out, pero que en una primera fase, servir para confirmar un pedido, realizando la integracin con el ERP de Alegra para generar una factura. 

 Label Ttulo de la Vista&#58; &quot; Actualiza tu licencia Analytics &quot; 
 class= lbl_actualiza_analytics ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualiza_analytics )&#160;&#160; 
&#160; 
 Label Descripcin de la Vista&#58; 
 class=lbl_actualiza_plan_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualiza_plan_desc ) 
&#160; 
 Confirma los siguientes datos para la actualizacin de tu plan. 

 Card&#58; Tu plan actual 

 Label Ttulo de la Vista&#58; &quot;Tu plan actual&quot; 
 class=lbl_tu_plan_actual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_tu_plan_actual )&#160;&#160; 
&#160; 
 El sistema debe definir cul es la licencia analytics que le aplica al cliente, mediante la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;eatc_cua. name &#125;&#125;&amp;_distinct= eatc_data_analytics_code 
&#160; 
 Si el sistema no arroja una respuesta vlida, el valor a tomar ser &quot; analytics_free &quot;.&#160; 
&#160; 
 El sistema debe realizar la siguiente consulta para establecer los valores relativos a la actual licencia de la cuenta. 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp; analytics_licence_code =&#123;&#123;eatc_data_analytics_cua. eatc_data_analytics_code &#125;&#125; 
&#160; 
 Y tambin recuperar las variables que a continuacin se relacionan&#58; 
&#160; 
 &#123;&#123;nombre_de_la_empresa&#125;&#125;&#58; 
 &#123;&#123; eatc_customer. eatc_fiscal_name &#125;&#125; 
&#160; 
 &#123;&#123; analytics_actual &#125;&#125;&#160; 
 El sistema deber guardar en una variable el tipo de licencia actual &#123;&#123; eatc_data_analytics_cua. eatc_data_analytics_code &#125;&#125; o en su defecto &quot; analytics_free &quot; (antes de la actualizacin) para posibles reversiones de registros. 
&#160; 
 &#123;&#123; nombre_del_plan_analytics_actual &#125;&#125; - &#123;&#123;pods_activos&#125;&#125; puntos de donacin 
&#160; 
 Con el dato obtenido (o con el valor por defecto &quot; analytics_free &quot;), se realiza la siguiente consulta&#58;&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_licences? eatc_code=&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125; &amp; _distinct =eatc_label 

&#160; 
 &#123;&#123; eatc_data_analytics_licences . eatc_label &#125;&#125; - &#123;&#123; pods_activos &#125;&#125; class=lbl_pods ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_pods ) 
&#160; 
 &#123;&#123;moneda&#125;&#125; &#123;&#123;precio_analytics_actual&#125;&#125; por punto de donacin 
&#160; 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;eatc_licenses_prices . default_price &#125;&#125; class= lbl_por_pod ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_por_pod )&#160; 
&#160; 
 Total&#58; &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio_analytics_actual&#125;&#125; 
&#160; 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 class= lbl_total ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_valor_unitario )&#58; &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio_analytics_actual&#125;&#125;&#160; 
&#160; 
 Nota &#58; este dato no se encuentra en el diseo, pero se considera necesario para los clculos que se realizarn para la card Facturacin. 

 Card&#58; Nuevo plan 

 Label Ttulo de la Card&#58; &quot;Nuevo plan&quot; 
 class=lbl_nuevo_plan ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_nuevo_plan )&#160;&#160;&#160; 
&#160; 
 Con la informacin del plan al cual se quiere acceder y que se seleccion en la vista anterior ( &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; ) sistema debe realizar la siguiente consulta para establecer los valores relativos a la actual licencia de la cuenta. 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp; analytics_licence_code = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Y tambin recuperar las variables que a continuacin se relacionan&#58; 
&#160; 
 &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125; 
 &#123;&#123;eatc_licenses_prices . name &#125;&#125; &#160; 
 (&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp; analytics_licence_code = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; &amp;_distinct= name ) 
&#160; 
 Nota &#58; en el diseo aparece como un selector, pero no es necesario que lo sea, simplemente puede ser el nombre de la licencia seleccionada en la pantalla anterior. 

&#160; 
 ***AJUSTE&#58; Actualmente tienes &#123;&#123;pods_activos&#125;&#125; &#160; Puntos de donacin activos *** 
 class=lbl_actualmente_tienes (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualmente_tienes ) &#123;&#123; pods_activos &#125;&#125; class= lbl_pods_activos ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_pods_activos )&#160; 
&#160; 
 Deprecado&#58; Nota &#58; en el diseo aparecen botones para adicionar o quitar puntos de donacin, que en primera instancia no deben ser implemenados, solamente se presenta el valor de puntos activos para la respectiva cuenta, tal como se obtuvo en la pantalla anterior . 

&#160; 
 Valor unitario (por punto de donacin)&#58; &#123;&#123;moneda&#125;&#125; &#123;&#123;precio&#125;&#125; &#160; 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 class= lbl_valor_unitario ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_valor_unitario )&#160; ( class= lbl_por_pod ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_por_pod )) &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;precio&#125;&#125; &#160; 
&#160; 
 Nota &#58; el precio ( &#123;&#123;precio&#125;&#125; ) se coloca a partir de la informacin obtenida en la pantalla anterior. 

&#160; 
 Total&#58; &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio&#125;&#125; 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 class= lbl_total ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_valor_unitario )&#58; &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio&#125;&#125; &#160; 
&#160; 
 Nota &#58; se muestra el valor de la multiplicacin del nmero de puntos de donacin activos por el precio, obtenido en la pantalla anterior ( similar a como se muestra en dicha pantalla el total ). 

 Card&#58; Facturacin 
 Partiendo del supuesto, que la fecha de facturacin siempre es el inicio del mes, y por lo tanto, si una persona hace un ajuste en el precio de la licencia, en una fecha diferente a la del primero del mes, entonces el sistema ya habr generado una factura para dicho mes por el valor anterior de la factura y por lo tanto la facturacin corresponder al ajuste del precio por lo que resta del mes, para obtener el valor de la nueva licencia. 

 Label Ttulo de la Vista&#58; &quot;Facturacin&quot; 
 class=lbl_facturacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_facturacion )&#160;&#160;&#160;&#160; 

&#160; 
 Selector de periodo de facturacin 
 Los valores y el funcionamiento de este selector es similar al implementado en la pgina de informacin de licencias (simplemente se cambia el tipo de selector de un radio button a un dropdown de seleccin nica. El valor que se muestra en primera instancia es el correspondiente al eatc_cua. type_period 

&#160; 
 Ahorro anual &#123;&#123;moneda&#125;&#125; &#123;&#123;valor_ahorro&#125;&#125; &#160; 
 Slo aparece si en el selector anterior se selecciona o est seleccionado el &quot; Plan anual &quot; 
 class=lbl_ahorro_anual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_ahorro_anual ) &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;valor_ahorro&#125;&#125;&#160; 
&#160; 
 Para calcular el &#123;&#123;valor_ahorro&#125;&#125;&#160; se realiza la siguiente operacin&#58; 
&#160; 
 &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio&#125;&#125; * 0,15 

 Determinacin del &#123;&#123;valor_a_facturar&#125;&#125; si existe una factura analytics pagada para el periodo actual de facturacin 
 El sistema deber determinar, consultando las facturas del cliente (con los mismos procesos que se implementaron para la funcionalidad &quot; Tu plan y facturacin &quot;), si existe una factura, aceptada (pagada) por el cliente, para el periodo actual, entonces se deben realizar los siguientes clculos para determinar el valor a facturar. 
&#160; 
 Para determinar el valor a facturar se deber establecer la diferencia entre el valor de la licencia a la cual se quiere actualizar la cuenta y su licencia anterior (o actual) y multiplicar dicho valor por la prorrata de das que faltan para el fin del periodo de facturacin ( eatc_cua. type_period ), que si es mensual correspondrn a los das que restan para terminar el mes, sobre el total de los das del mes.&#160; Si es anual correspondern a los das que faltan para terminar el ao facturable sobre el total de das del ao facturable. 
&#160; 
 &#123;&#123;diferencia_precios_licencias&#125;&#125; = ( &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio&#125;&#125; ) - ( &#123;&#123;pods_activos&#125;&#125; * &#123;&#123; precio_analtytics_actual &#125;&#125; ) 
&#160; 
 &#123;&#123;prorrata_periodo_restante&#125;&#125; = &#123;&#123;dias_que_faltan_para_fin_del_periodo&#125;&#125; / &#123;&#123;dias_totales_del_periodo&#125;&#125; 
&#160; 
 &#123;&#123;valor_a_facturar&#125;&#125; = &#123;&#123;diferencia_precios_licencias&#125;&#125; * &#123;&#123;prorrata_periodo_restante&#125;&#125; 

&#160; 
 Determinacin del &#123;&#123;valor_a_facturar&#125;&#125; si no existe una factura aceptada / pagada para el periodo actual de facturacin 
 Si el sistema determina que no hay una factura expedida para el periodo actual (con los mismos procesos que se implementaron para la funcionalidad &quot; Tu plan y facturacin &quot;) lo cual deber ocurrir en particular el primer da del mes (dado que se ha determinado que ese es el da en el cual se expedirn las facturas mensuales), entonces se proceder a determinar el valor a facturar de la siguiente manera&#58; 
&#160; 
 &#123;&#123;valor_a_facturar&#125;&#125; = &#123;&#123;pods_activos&#125;&#125; * &#123;&#123;precio&#125;&#125; 

&#160; 
 A pagar &#123;&#123;moneda&#125;&#125; &#123;&#123;valor_a_facturar&#125;&#125; + impuestos 
 class=lbl_a_pagar ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_a_pagar ) &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;valor_a_facturar&#125;&#125; class=lbl_mas_impuestos ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_mas_impuestos )&#160;&#160; 

&#160; 
 ***NUEVO &#58; Periodo de facturacin *** 
 class= lbl_bill_period ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_bill_period )&#160;&#160;&#160; 
&#160; 
 &#123;&#123;fecha_actual&#125;&#125;&#160; - &#123;&#123;ltimo_dia_periodo_facturable&#125;&#125;&#160; 
&#160; 
 El sistema debe informar la fecha actual y la fecha correspondiente al ltimo da del periodo facturable.&#160; Para los planes mensuales este ltimo da facturable corresponder al ltimo da del mes, y para los planes anuales corresponder al ltimo da del ao que se factura. 

&#160; 
 Con esta actualizacin tu cuenta EatCloud pasar a tener la licencia analytics &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125;&#160; con &#123;&#123;pods_activos&#125;&#125; Puntos de donacin activos *** 
 class= lbl_con_esta_actualizacion_analytics ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_con_esta_actualizacion_analytics ) &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125; class=lbl_con ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_con )&#160; &#123;&#123; pods_activos &#125;&#125; class= lbl_pods_activos ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_pods_activos ) 

 DEPRECADO class=lbl_a_pagar_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_a_pagar ) 
&#160; 
 El valor facturado corresponde al valor del nuevo plan de seleccionado, siempre y cuando no haya una factura aceptada / pagada por el mismo periodo para el plan actual. En caso que dicha factura exista, corresponde entonces a la prorrata de los das restantes del periodo facturado de las diferencias entre el precio actual y nuevo precio de la licencia adquirida. 
&#160; 
 ***AJUSTE&#58;&#160; Botn&#58; &quot;Actualizar Plan&quot; (antes Botn&#58; &quot;Aceptar&quot;) *** 
 class=lbl_actualizar_plan ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizar_plan )&#160; 
&#160; 
 Al oprimir este botn se desplegar una ventana modal de confirmacin de la siguiente manera 

 Ventana modal de confirmacin de pedido / facturacin 
 El wirefame de la ventana es el siguiente&#58; 

 Leyenda principal del modal 
 class= lbl_confirmacion_pedido_analytics ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_confirmacion_pedido_analytics )&#160;&#160; 
&#160; 
 Recuerda que al actualizar tu plan, cambiarn los valores facturables por concepto de licencia analytics, del precio de la licencia anterior, al precio de la nueva licencia por punto de donacin. 
&#160; 
 Botn&#58; &quot;No, cancelar&quot; 
 class=lbl_no_cancelar ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_no_cancelar ) 
&#160; 
 Al accionar este botn, se cierra el modal y se retorna a la pantalla anterior. 
&#160; 
 Botn&#58; &quot;Si, estoy de acuerdo&quot; 
 class=lbl_si_de_acuerdo ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_si_de_acuerdo ) 
&#160; 
 Al accionar este botn, se realizan varias acciones&#58; 
 Envo de datos para integracin de con pasarela de pago y realizacin del pago (pendiente) 
 Actualizacin de los valores de la cuenta a partir de la confirmacin de la actualizacin 
 Se genera una factura electrnica mediante integracin con el sistema ERP Alegra 
 Se direcciona a una pantalla de xito de la transaccin 

 E NVO DE DATOS PARA INTEGRACIN CON PASARELA DE PAGO Y REALIZACIN DEL PAGO 
 ***Pendiente&#58; se implementar en una segunda etapa*** 
 En este punto, el sistema deber enviar los datos del producto a facturar&#58; (De ser necesario&#58; eatc_licenses_prices. name (eatc_licenses_prices. name_lbl ), eatc_licenses_prices. description (eatc_licenses_prices. description_lbl ) ) y su respectivo &#123;&#123;valor_a_facturar&#125;&#125; a la pasarela de pagos, para la realizacin del pago .&#160; Con el pago confirmado, se realizan los dems procesos, de acuerdo a las indicaciones respectivas.&#160; En una primera etapa, no se tendr en cuenta este proceso, y simplemente se comenzar con el siguiente. 

 A CTUALIZACIN DE LOS DATOS DE LA CUENTA A PARTIR DE LA ACTUALIZACIN DE LICENCIA 
 Llamado al CRD para la actualizacin de los datos de la cuenta 
 Con los datos de la nueva licencia adquirida se procede a realizar la siguiente actualizacin de informacin de la cuenta del cliente&#58; 
&#160; 
 Si la cuenta tena una licencia analytics previa 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_data_analytics_cua &amp;_operacion= _update &amp; eatc_data_analytics_code =&#123;&#123;Cdigo de la nueva licencia adquirida&#58; eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp;WHERE eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Si la cuenta&#160; NO tena una licencia analytics previa 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_data_analytics_cua &amp;_operacion= _insert &amp; eatc_data_analytics_code =&#123;&#123;Cdigo de la nueva licencia adquirida&#58; eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp; eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Si se hizo un cambio en el periodo de facturacin, tambin se deber realizar la siguiente actualizacin&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_cua &amp;_operacion= _update &amp;type_period=&#123;&#123; lbl_anual_ahoras_15pc/lbl_mensual &#125;&#125;&amp;WHEREname=&#123;&#123;_DOM.cua_user&#125;&#125; 
&#160; 
 Mensajes para informar sobre el proceso 
 Los siguientes mensajes se debern ir desplegando al usuario a medida que progresa el proceso de edicin de datos, para mantenerlo informado del progreso y resultado del proceso (puede ser mediante toast por ejemplo) 
&#160; 
 Mensaje que se despliega mientras el proceso se est ejecutando&#58; &quot;Actualizando datos en la cuenta de la empresa&quot; 
 class=lbl_actualizando_cua ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizando_cua )&#160;&#160; 
&#160; 
 Mensaje actualizacin fallida, reintento&#58; &quot;Error al actualizar datos de la cuenta, reintentando...&quot; 
 class=lbl_actualizando_cua_reintento ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizando_cua_reintento )&#160; 
&#160; 
 Mensaje actualizacin exitosa&#58; &quot;Datos de la cuenta exitosamente editados&quot; 
 class=lbl_actualizando_cua_exito ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizando_cua_exito )&#160; 
&#160; 
 Mensaje actualizacin fallida (definitiva&#58; despus de tres reintentos)&#58; &quot;No pudimos editar los datos de tu cuenta&quot; 
 class=lbl_actualizando_cua_falla ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizando_cua_falla )&#160; 
&#160; 
 Se debe evaluar la posibilidad de que ante un fallo en la actualizacin (despus de tres reintentos), se enve un correo (a danielcardenas@eatcloud.com Asunto&#58; actualizar manualmente datos de la cuenta) que contenga la URL de actualizacin ( &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/?_tabla= eatc_cua &amp;_operacion= _update &amp;type=&#123;&#123;Cdigo de la nueva licencia adquirida&#58; eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp;type_period=&#123;&#123; lbl_anual_ahoras_15pc/lbl_mensual &#125;&#125;&amp;WHEREname=&#123;&#123;_DOM. cua_user &#125;&#125; ) para realizar&#160; el proceso manual por parte de la mesa de servicio. 

 I NTEGRACIN CON FACTURACIN ELECTRNICA DEL ERP 
 Verificacin de la existencia o no del cliente en el ERP 
 El sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers&amp;fieldname=eatc_fiscal_id&amp;fieldvalue=&#123;&#123; eatc_fiscal_id &#125;&#125;&amp;fielddecrypt=eatc_fiscal_id,eatc_fiscal_name 
&#160; 
 Para determinar si existe un registro vlido en el parmetro eatc_customers. erp_id (lo cual es un indicativo de que el cliente no ha sido creado en el ERP).&#160; De no existir un registro vlido en dicho campo el sistema deber realizar el siguiente llamado (para crear primero el cliente en el ERP y luego generar la factura correspondiente)&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/ierp/eatcloud?fiscalid=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; 
&#160; 
 Mensajes para informar sobre el proceso de creacin del cliente en el ERP 
 Los siguientes mensajes se debern ir desplegando al usuario a medida que progresa el proceso de edicin de datos, para mantenerlo informado del progreso y resultado del proceso (puede ser mediante toast por ejemplo) 
&#160; 
 Mensaje que se despliega mientras el proceso se est ejecutando&#58; &quot;Creando cliente en el ERP&quot; 
 class=lbl_creando_cliente_erp ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_cliente_erp )&#160;&#160; 
&#160; 
 Mensaje creacin fallida, reintento&#58; &quot;Error al crear el cliente en el ERP, reintentando...&quot; 
 class=lbl_creando_cliente_erp_reintento ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_cliente_erp_reintento )&#160; 
&#160; 
 Mensaje creacin exitosa&#58; &quot;Cliente creado exitosamente&quot; 
 class=lbl_creando_cliente_erp_exito ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_cliente_erp_exito )&#160; 
&#160; 
 Mensaje creacin fallida (definitiva&#58; despus de tres reintentos)&#58; &quot;No pudimos crear el cliente en el ERP&quot; 
 class=lbl_creando_cliente_erp_falla ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_cliente_erp_falla )&#160; 
&#160; 
 Se debe evaluar la posibilidad de que ante un fallo en la actualizacin (despus de tres reintentos), se enve un correo (a danielcardenas@eatcloud.com &#58; Asunto&#58; crear manualmente un cliente en el ERP) que contenga la URL de creacin ( &#123;&#123; URL_entorno_datagov &#125;&#125;/ierp/eatcloud?fiscalid=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; ) para realizar&#160; el proceso manual por parte de la mesa de servicio. 
&#160; 
 Una vez se haya creado el cliente en el ERP, o si en la evaluacin anterior se determina que existe un dato vlido en eatc_customers. erp_id &#160; (lo que es indicativo de que el cliente ya ha sido creado en el ERP), se procede, con los datos obtenidos con anterioridad en el flujo de proceso y otros datos que se detallan ms adelante, a saber&#58; 
&#160; 
 Datos obtenidos con anterioridad en el flujo de proceso&#58; 
 Estos datos se obtuvieron en la presente funcionalidad o en funcionalidades anteriores que trajeron a esta, como es el caso de la pgina que presenta la informacin de los planes y cuyo botn &quot;Comprar&quot; nos trae a esta funcionalidad o pantalla.&#160; 
&#160; 
 &#123;&#123; _DOM .cua_user&#125;&#125; 

&#160; 
 Cantidad de puntos activos &#123;&#123; pods_activos &#125;&#125; 
 Que fueron obtenidos para las validaciones necesarias para consultar el precio de lista en la pgina de informacin de licencias (como se document anteriormente ). 

&#160; 
 &#123;&#123; nombre_del_plan_analytics_actual &#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Tu plan actual &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123; precio_analytics_actual &#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Tu plan actual &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;precio&#125;&#125; 
 Que fu obtenidopara la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123; prorrata_periodo_restante &#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Facturacin &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123; precio_unitario_prorrateado &#125;&#125; 
 Es igual al precio menos el precio actual por la prorrata del periodo restante 
 &#123;&#123; precio_unitario_prorrateado &#125;&#125; = ( &#123;&#123;precio&#125;&#125; - &#123;&#123;precio_actual&#125;&#125; ) * &#123;&#123; prorrata_periodo_restante &#125;&#125; 

&#160; 
 &#123;&#123;valor_a_facturar&#125;&#125; 
 Que fueron obtenidos para la construccin de la card &quot; Facturacin &quot;&#160; (como se document ms arriba ). 

&#160; 
 Consulta a la estructura eatc_licenses_prices 
 Con la consulta realizada a la respectiva estructura con el fin de mostrar el precio (en la pgina de&#160; informacin de los planes ), se toman los datos&#58;&#160; 
 eatc_licenses_prices. description ( eatc_licenses_prices. description_lbl) 
 eatc_licenses_prices. erp_product_id 
 eatc_licenses_prices. default_price_currency 

&#160; 
 Nota sobre el parmetro eatc_licenses_prices. description &#58; en una primera fase de implementacin se deber llevar el dato que est en este campo, pero en fases posteriores se deber llevar el resultado de la consulta del label que est registrado en el campo eatc_licenses_prices. description_lbl 
&#160; 
 Otros datos necesarios para integrarse con la facturacin electrnica del ERP&#58; 
 Nota para la implementacin&#58; la obtencin de los datos adicionales, idealmente se debe implementar, consultando variables ya obtenidas previamente en otras funcionalidades y las que queden haciendo falta, se deben implementar cuando se ingresa a la funcionalidad (para evitar que cuando se opriman los botones, por ejemplo &quot;Comprar&quot; que deben detonar el registro de la cotizacin en el ERP, el procesamiento no sea muy pesado, y halla una buena experiencia de usuario). 
&#160; 
 Determinacin &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; del cliente&#58;&#160; 
 Nota para la implementacin&#58; en la funcionalidad &quot; Configura tu empresa &#58; https&#58;//dev.datagov.eatcloud.info/_dgbo/#!/cnfempresa &quot;, se debieron implementar consultas similares, por lo tanto se recomienda revisar el cdigo para obtener la variable ya consultada (que es lo ideal) o para realizar la consulta respectiva como se establece a continuacin 
&#160; 
 El sistema, con el dato&#58; &#123;&#123;_DOM. cua_user &#125;&#125; debe proceder a realizar la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname= eatc_cua &amp;fieldvalue=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;fielddecrypt= eatc_customer_fiscal_id 
&#160; 
 Se guarda el dato obtenido para realizar la consulta de los datos del cliente que se especifica ms adelante. 

&#160; 
 Ejemplo&#58; ambiente de pruebas, &#123;&#123;_DOM. cua_user &#125;&#125;= alqueria 
&#160; 
 El sistema deber realizar el siguiente llamado&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info//crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname= eatc_cua &amp;fieldvalue= alqueria &amp;fielddecrypt= eatc_customer_fiscal_id &#160; 
 &#160; 
&#160; 
 Por lo tanto &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; = 860004922 
&#160; 
 Lectura de los datos del cliente 
 Nota para la implementacin&#58; en la funcionalidad &quot; Configura tu empresa &#58; https&#58;//dev.datagov.eatcloud.info/_dgbo/#!/cnfempresa &quot;, se debieron implementar consultas similares, por lo tanto se recomienda revisar el cdigo para obtener la variable ya consultada (que es lo ideal) o para realizar la consulta respectiva como se establece a continuacin 
&#160; 
 El sistema deber realizar la siguiente lectura a partir de los datos obtenidos anteriormente&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; &amp;fielddecrypt= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address 
&#160; 
 Y con el llamado se obtienen los siguientes datos&#160; desencriptados para realizar posteriormente el llamado al API para la creacin de la cotizacin 
 eatc_customer. eatc_fiscal_name 
 eatc_customer. eatc_fiscal_id 
 eatc_customer. eatc_email 
 eatc_customer. eatc_phone 
 eatc_customer. eatc_address 
 eatc_customer. eatc_city 
 eatc_customer. eatc_country 
 eatc_customer. erp_id 

&#160; 
 Ejemplo&#58; ambiente de pruebas, &#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125;= 860004922 
&#160; 
 El sistema deber realizar el siguiente llamado&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= 860004922 &amp;fielddecrypt= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &#160; &#160; &#160; 
&#160; 
 Y con l obtiene los datos requeridos para el proceso. 

&#160; 
 Registro de la factura electrnica en el ERP&#58; 
 Documentacin&#58; https&#58;//developer.alegra.com/docs/crear-cotizaci%C3%B3n &#160; 
&#160; 
 Para realizar el registro de la cotizacin segn la documentacin del ERP, se deber construir el siguiente JSON, para posteriormente enviarlo a travs de un llamado cURL que se especifica ms adelante&#58; 
&#160; 
 &#123;&#123;JSON_CURL&#125;&#125; 
 &#123; 
 &#160;&#160;&quot;date&quot; &#58; &quot;&#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125;&quot; , 
 &#160; &quot;dueDate&quot; &#58; &quot;&#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125;&quot; , =&gt; REVISAR 
 &#160; &quot;observations&quot; &#58; &quot;Cuenta&#58; &#123;&#123; _DOM .cua_user&#125;&#125; - Razn social&#58; &#123;&#123; eatc_customer. eatc_fiscal_name &#125;&#125; - NIT&#58; &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; - Email contacto&#58; &#123;&#123;eatc_customer. eatc_email &#125;&#125; - Telfono&#58; &#123;&#123;eatc_customer. eatc_phone &#125;&#125; - Ciudad&#58; &#123;&#123;eatc_customer. eatc_city &#125;&#125; - Pas&#58; &#123;&#123;eatc_customer. eatc_country &#125;&#125; &quot; - Actualizacin licencia rescate de&#58; &#123;&#123;nombre_del_plan_actual&#125;&#125; a &#123;&#123;nombre_del_nuevo_plan&#125;&#125; &quot; , 
 &#160; &quot;anotation&quot; &#58; &quot;Nota &#58; Favor consignar a la cuenta Cuenta de Ahorros Bancolombia 36000000518&quot; ,&#160; =&gt; REVISAR 
 &#160; &quot;termsConditions&quot; &#58; &quot;Tendrs 48 horas para realizar pago o tu actualizacin de licencia ser reversada.&quot; , =&gt; REVISAR 
 &#160; &quot;status&quot; &#58; &quot;draft&quot; , =&gt; REVISAR 
 &#160; &quot;client&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;id&quot; &#58; &#123;&#123;eatc_customer. erp_id&#125;&#125; 
 &#160;&#160;&#160;&#160;&#125;, 
 &quot;numberTemplate&quot; &#58; &#123; 
 &#160;&#160;&#160; &quot;id&quot; &#58; 1 , 
 &#160;&#160;&#125;, 
 &#160; &quot;seller&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;id&quot; &#58; &quot;1&quot; =&gt; REVISAR 
 &#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160; &quot;currency&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;code&quot; &#58; &quot; &#123;&#123;eatc_licenses_prices. default_price_currency &#125;&#125; &quot; , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;exchangeRate&quot; &#58; 1 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160; &quot;items&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;id&quot; &#58; &#123;&#123;eatc_licenses_prices. erp_product_id &#125;&#125; , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;description&quot; &#58; &quot; &#123;&#123;eatc_licenses_prices. description &#125;&#125; &quot; , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;discount&quot; &#58; 0 , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;tax&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;id&quot; &#58; =&gt; PENDIENTE DEFINICIN 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;], 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;price&quot; &#58; &#123;&#123; precio_unitario_prorrateado &#125;&#125; , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &quot;quantity&quot; &#58; &#123;&#123; pods_activos &#125;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;], 
 &quot;payments&quot; &#58; [ =&gt; ESTE OBJETO SE UTILIZAR CUANDO SE REALICE EL PAGO ELECTRNICO, POR EL MOMENTO NO SE ENVA 
 &#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;date&quot;&#58; &quot;&#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;account&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot;&#58; 2 
 &#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;amount&quot; &#58; &#123;&#123;valor_a_facturar&#125;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;paymentMethod&quot; &#58; &quot;cash&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;retentions&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot;&#58; 1, =&gt; PENDIENTE DEFINICIN 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;amount&quot; &#58; 50 =&gt; PENDIENTE DEFINICIN 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;], 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;currency&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;code&quot; &#58; &quot;&#123;&#123;eatc_licenses_prices. default_price_currency &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;exchangeRate&quot; &#58; 1 
 &#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#125; 
 ], 
 &#125; 

 cURL&#58; 
 curl -v -H &quot;Accept&#58; application/json&quot; -H &quot;Content-type&#58; application/json&quot; -X https&#58;//api.alegra.com/api/v1/estimates/ -u 'diana.alvarez@eatcloud&#58; 6505f78dbfb7dfb38bfe ' -d ' &#123;&#123;JSON_CURL&#125;&#125; ' 
&#160; 
 Mensajes para informar sobre el proceso de creacin de la factura 
 Los siguientes mensajes se debern ir desplegando al usuario a medida que progresa el proceso de creacin de la factura, para mantenerlo informado del progreso y resultado del proceso (puede ser mediante toast por ejemplo) 
&#160; 
 Mensaje que se despliega mientras el proceso se est ejecutando&#58; &quot;Creando factura electrnica el ERP&quot; 
 class=lbl_creando_factura ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_factura )&#160; 
&#160; 
 Mensaje creacin fallida, reintento&#58; &quot;Error al crear la factura electrnica, reintentando...&quot; 
 class=lbl_creando_factura_reintento ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_factura_reintento )&#160; 
&#160; 
 Mensaje creacin exitosa&#58; &quot;Factura creada exitosamente&quot; 
 class=lbl_creando_factura_exito ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_factura_exito )&#160; 
&#160; 
 Mensaje creacin fallida (definitiva&#58; despus de tres reintentos)&#58; &quot;No pudimos crear la factura&quot; 
 class=lbl_creando_factura_falla ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_creando_factura_falla )&#160; 
&#160; 
 Se debe evaluar la posibilidad de que ante un fallo en la creacin de la factura (despus de tres reintentos), se enve un correo (a diana.alvarez@eatcloud.com &#58; Asunto&#58; Crear manualmente Factura en el ERP) que contenga la URL de creacin del cliente en el ERP ( &#123;&#123; URL_entorno_datagov &#125;&#125;/ierp/eatcloud?fiscalid=&#123;&#123;eatc_customers. eatc_fiscal_id &#125;&#125; ) y los datos del &#123;&#123; JSON_cURL &#125;&#125; para la creacin de la factura. 

 P ANTALLA DE XITO DE LA TRANSACCIN 
 Este es el wireframe de la pantalla de xito de la transaccin 

 La implementacin de este wireframe tendr dos etapas (en la imagen se muestra la etapa inicial&#58; cuando aun no se ha integrado el pago electrnico), que se comportar de la siguiente manera, teniendo en cuenta principalmente la informacin recolectada para la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 
&#160; 
 Ttulo&#58; La actualizacin de tu licencia ha sido exitosa! 
 class=lbl_actualizacion_licencia_exitosa (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_actualizacion_licencia_exitosa ) 
&#160; 
 &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125; 
&#160; 
 Que fu obtenido para la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 

 Tienes &#123;&#123;pods_activos&#125;&#125;&#160; puntos de donacin 
 class=lbl_tienes (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_tienes ) &#123;&#123; pods_activos &#125;&#125; class=lbl_pods ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_pods )&#160; 
&#160; 
 &#123;&#123;moneda&#125;&#125; &#123;&#123;precio&#125;&#125; por punto de donacin 
&#160; 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;precio&#125;&#125; ( class= lbl_por_pod ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_por_pod )) &#160; 
&#160; 
 Leyenda despus del precio 
 Etapa 1&#58; SIN implementacin de pago electrnico&#58; En tu correo electrnico &#123;&#123; eatc_customer. eatc_email &#125;&#125; recibirs tu factura electrnica para efectuar tu pago.&#160; Tendrs 48 horas para realizarlo, de lo contrario la actualizacin de tu licencia ser reversada. 
 class=lbl_en_tu_email (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_en_tu_email ) 
&#160; 
 &#123;&#123; eatc_customer. eatc_email &#125;&#125;&#160; 
&#160; 
 class=lbl_factura_y_terminos_pago (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_factura_y_terminos_pago ) 
&#160; 
 recibirs tu factura electrnica para efectuar tu pago. Tendrs 48 horas para realizarlo, de lo contrario la actualizacin de tu licencia ser reversada. 
&#160; 
 Etapa 2&#58; CON implementacin de pago electrnico PENDIENTE 
 class=lbl_ (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_ ) 
&#160; 
 ..... 

&#160; 
 Botn finalizar 
 class=lbl_finalizar (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_finalizar ) 
&#160; 
 Etapa 1&#58; SIN implementacin de pago electrnico&#58; Envo de correo para gestin de pago. 
 Para enviar el correo, el sistema deber consultar la URL de descarga de la ltima factura (la que se acab de crear&#58; &#123;&#123; URL_ultima_factura &#125;&#125; ) utilizando para ello las mismas funciones que se implementaron para consultar la informacin del historial de facturas en la pgina &quot; Tu plan y facturacin &quot; 
&#160; 
 Se debe enviar un correo&#160; a diana.alvarez@eatcloud.com &#58; con el siguiente Asunto&#58; Gestin de pago de la Factura. 
&#160; 
 Y que contenga en su cuerpo la siguiente informacin 
 Cuenta&#58; &#123;&#123; _DOM .cua_user&#125;&#125; - Razn social&#58; &#123;&#123; eatc_customer. eatc_fiscal_name &#125;&#125; - NIT&#58; &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; - Email contacto&#58; &#123;&#123;eatc_customer. eatc_email &#125;&#125; - Telfono&#58; &#123;&#123;eatc_customer. eatc_phone &#125;&#125; - Ciudad&#58; &#123;&#123;eatc_customer. eatc_city &#125;&#125; - Pas&#58; &#123;&#123;eatc_customer. eatc_country &#125;&#125; &quot; - Actualizacin licencia rescate de&#58; &#123;&#123; nombre_del_plan_analytics_actual &#125;&#125; a &#123;&#123; nombre_del_nuevo_plan_analytics &#125;&#125; &quot; 
&#160; 
 Revisar el pago de la ltima factura expedida al cliente&#58; &#123;&#123; URL_ultima_factura &#125;&#125; 
&#160; 
 Si en las prximas 48 horas contadas a partir de &#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125; , por favor proceder a devolver los cambios en el tipo de licencia presionando la siguiente URL&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_data_analytics_cua &amp;_operacion= _update &amp; eatc_data_analytics_code =&#123;&#123; analytics_actual &#125;&#125; &amp;WHERE eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Etapa 2&#58; CON implementacin de pago electrnico PENDIENTE 
 Dado que el pago se efectuar con pasarela de pagos, antes de expedir la factura, entonces el correo de gestin de cobro no ser necesario.&#160; En ambos casos (etapa 1, y etapa 2) al accionar el botn se redireccionar a la pgina&#58; 
&#160; 
 Redireccin a pgina&#58; &quot; Tu plan y facturacin &quot; 
 El sistema deber redireccionar al hacer clic en el botn finalizar a&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/_dgbo/#!/planfacturacion 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresumen-pedido-licencias-analytics%2F693364553-resumen_pedido_2_enc--1-.jpg&ow=1127&oh=189, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresumen-pedido-licencias-analytics%2F693364553-resumen_pedido_2_enc--1-.jpg&ow=1127&oh=189 

 487.000000000000 

 RESUMEN DE PEDIDO ANALYTICS