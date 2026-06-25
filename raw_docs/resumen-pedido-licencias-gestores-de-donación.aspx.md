# resumen-pedido-licencias-gestores-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El siguiente wireframe, se dise para un ambiente web, por lo tanto se deber adaptar para su correcta visualizacin en la APP, y las caractersticas puntuales de las licencias para gestores de donaciones (por ejemplo, en ellas no es necesario anotar el nmero de puntos de donacin porque no aplica). 

 Label Ttulo de la Vista&#58; &quot;Actualiza tu plan&quot; 
 class=lbl_actualiza_plan ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualiza_plan )&#160;&#160; 
&#160; 
 Label Descripcin de la Vista&#58; 
 class=lbl_actualiza_plan_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualiza_plan_desc )&#160; 
&#160; 
 Confirma los siguientes datos para la actualizacin de tu plan. 

 Card&#58; Tu plan actual 

 Label Ttulo de la Card&#58; &quot;Tu plan actual&quot; 
 class=lbl_tu_plan_actual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_tu_plan_actual )&#160;&#160; 
&#160; 
 El sistema debe realizar la siguiente consulta para establecer los valores relativos a la actual licencia de la cuenta. 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;&amp;cua_type_period= lbl_mensual &amp; eatc_doma = _default &amp; eatc_doma_license = &#123;&#123;eatc_donation_managers. eatc_license &#125;&#125; &amp; _cmp= name_lbl,description_lbl,default_price,default_price_currency,cua_type_period 
&#160; 
 Si la consulta no trae ningn resultado, se deber realizar la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;&amp;cua_type_period= lbl_mensual &amp; eatc_doma = _default &amp; eatc_doma_license = free&amp; _cmp= name_lbl,description_lbl,default_price_currency,default_price,cua_type_period 
&#160; 
 Y tambin recuperar las variables que a continuacin se relacionan&#58; 
&#160; 
 &#123;&#123;nombre_de_la_organizacin&#125;&#125;&#58; 
 &#123;&#123;eatc_donation_managers . organizacin &#125;&#125; 
&#160; 
 &#123;&#123;eatc_license_actual&#125;&#125;&#160; 
 El sistema deber guardar en una variable el tipo de licencia actual &#123;&#123;eatc_donation_managers. eatc_license &#125;&#125; (antes de la actualizacin) para posibles reversiones de registros. Si la consulta no trae registros se colocar por defecto &quot; free&quot; 
&#160; 
 &#123;&#123;nombre_del_plan_actual&#125;&#125;&#160; 
 &#123;&#123;eatc_doma_licenses_prices . name_lbl &#125;&#125; 
&#160; 
 &#123;&#123;descripcion_del_plan_actual&#125;&#125;&#160; 
 &#123;&#123;eatc_doma_licenses_prices . description_lbl &#125;&#125; 
&#160; 
 &#123;&#123;moneda&#125;&#125; &#123;&#123;precio_actual&#125;&#125; mensual por sucursal=&gt; (Inicialmente las licencias sern mensuales, pero posteriormente se podrn generar otros periodos 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
&#160; 
 &#123;&#123;eatc_doma_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;eatc_doma_licenses_prices . default_price &#125;&#125; &#123;&#123;eatc_doma_licenses_prices . cua_type_period &#125;&#125; &#160; class= lbl_mensual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mensual ) class= lbl_por_sucursal ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_por_sucursal )&#160; 

 Card&#58; Nuevo plan 

 Label Ttulo de la Card&#58; &quot;Nuevo plan&quot; 
 class=lbl_nuevo_plan (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_nuevo_plan )&#160;&#160;&#160; 
&#160; 
 Con la informacin del plan al cual se quiere acceder y que se seleccion en la vista anterior ( &#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125; ) sistema debe realizar la siguiente consulta para establecer los valores relativos a la actual licencia de la cuenta. 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;&amp;cua_type_period= lbl_mensual &amp; eatc_doma = _default &amp; eatc_doma_license = &#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125; &amp; _cmp= name_lbl,description_lbl,default_price,default_price_currency,cua_type_period 
&#160; 
 Y tambin recuperar las variables que a continuacin se relacionan&#58; 
&#160; 
 &#123;&#123;nombre_del_nuevo_plan&#125;&#125; 
 &#123;&#123;eatc_doma_licenses_prices . name_lbl &#125;&#125; 
&#160; 
 Nota &#58; en el diseo aparece como un selector, pero no es necesario que lo sea, simplemente puede ser el nombre de la licencia seleccionada en la pantalla anterior. 

&#160; 
 Valor&#58; &#123;&#123;moneda&#125;&#125; &#123;&#123;precio&#125;&#125; mensual (por sucursal) 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
&#160; 
 class= lbl_valor ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_valor )&#160; &#123;&#123;eatc_doma_licenses_prices . cua_type_period &#125;&#125; &#160; &#123;&#123;eatc_doma_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;eatc_doma_licenses_prices . default_price &#125;&#125; class= lbl_mensual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mensual ) ( class= lbl_por_sucursal ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_por_sucursal )) 

 Colapsible&#58; &quot;Observaciones de la facturacin&quot; 

 Label Ttulo del colapsible&#58; &quot;Observaciones sobre la facturacin&quot; 
 class=lbl_obs_facturacion (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_obs_facturacion )&#160;&#160;&#160;&#160; 
&#160; 
 El sistema debe mostrar las siguientes observaciones como un listado con vietas, que por defecto est colapsado y si el usuario lo desea consultar lo podr descolapsar. 
&#160; 
 class=lbl_obs_facturacion_doma_1 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_obs_facturacion_doma_1 )&#160;&#160;&#160;&#160; 
&#160; 
 class=lbl_obs_facturacion_doma_2 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_obs_facturacion_doma_2 )&#160;&#160;&#160;&#160; 
&#160; 
 class=lbl_obs_facturacion_doma_3 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_obs_facturacion_doma_3 )&#160; &#160;&#160; 

 Card&#58; Facturacin hasta 
 Partiendo del supuesto, que la fecha de facturacin siempre es el inicio del mes, y por lo tanto, si una persona hace un ajuste en el precio de la licencia, en una fecha diferente a la del primero del mes, entonces el sistema ya habr generado una factura para dicho mes por el valor anterior de la factura y por lo tanto la facturacin corresponder al ajuste del precio por lo que resta del mes, para obtener el valor de la nueva licencia. 

 Label Ttulo de la Card&#58; &quot;Facturacin hasta&quot; 
 class=lbl_facturacion_hasta (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_facturacion_hasta )&#160;&#160;&#160;&#160; 

&#160; 
 Selector de periodo de facturacin 
 En el selector debern aparecer los meses posteriores (mes y ao) incluyendo el mes en curso , o el ltimo da de los meses posteriores, incluyendo el mes en curso (se deja a criterio del desarrollador).&#160; En principio se podrn mostrar hasta 12 meses posteriores. 
&#160; 
 El valor por defecto del selector deber ser el mes actual o el ltimo da del mes actual, pero el usuario podr seleccionar cualquier otro mes o da que requiera. 
&#160; 
 Segn la seleccin que realice el usuario, el sistema deber guardar el ltimo da del mes seleccionado, en formato AAAA-MM-DD, en una variable&#58; 
 &#123;&#123;eatc_license_valid_until&#125;&#125; 

 Determinacin del &#123;&#123;valor_a_facturar&#125;&#125; 
 A partir de la seleccin anterior y la determinacin de la fecha de validez de la licencia, el sistema deber realizar un clculo del valor del licenciamiento correspondiente al mes en curso 
&#160; 
 Valor a facturar (pagar) por lo que resta del mes en curso 
&#160; 
 &#123;&#123;diferencia_precios_licencias&#125;&#125; = &#123;&#123;precio&#125;&#125; - &#123;&#123;precio_actual&#125;&#125; 
&#160; 
 &#123;&#123;prorrata_periodo_restante&#125;&#125; = &#123;&#123;dias_que_faltan_para_fin_del_periodo(mes)&#125;&#125; / &#123;&#123;dias_totales_del_periodo(mes)&#125;&#125; 
&#160; 
 &#123;&#123;valor_a_facturar_mes_en_curso&#125;&#125; = &#123;&#123;diferencia_precios_licencias&#125;&#125; * &#123;&#123;prorrata_periodo_restante&#125;&#125; 

&#160; 
 Valor a facturar (pagar) por meses adicionales 
&#160; 
 Si el usuario seleccion como periodo a pagar meses ms adelante que el fin del mes en curso, entonces el sistema deber determinar el nmero de meses adicionales que el usuario seleccion y con ello determinar el valor de la licencia por esos meses&#58; 
&#160; 
 &#123;&#123;valor_a_facturar_meses_adicionales&#125;&#125; = &#123;&#123;meses_adicionales&#125;&#125; * &#123;&#123;precio&#125;&#125; 
&#160; 
 Ambos valores debern mostrarse (de ser necesario) como parte de una sumatoria que generar un gran total.&#160; Para identificar cada valor se debern utilizar los siguientes labels&#58; 
&#160; 
 Valor por lo que resta del mes&#58; class=lbl_valor_por_lo_que_resta_del_mes &#160; 
 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_valor_por_lo_que_resta_del_mes ) class=lbl_signo_moneda ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_signo_moneda )&#160; &#123;&#123;valor_a_facturar_mes_en_curso&#125;&#125; 
&#160; 
 Valor por mese(s) adicional(es) class=lbl_valor_por_meses_adicionales &#160; 
 (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_valor_por_meses_adicionales ) ( &#123;&#123;meses_adicionales&#125;&#125; )&#58; class=lbl_signo_moneda ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_signo_moneda ) &#123;&#123;valor_a_facturar_meses_adicionales&#125;&#125; 

&#160; 
 A pagar &#123;&#123;moneda&#125;&#125; &#123;&#123;valor_a_facturar&#125;&#125; El sistema deber sumar el valor a facturar por el mes en curso ms el valor a facturar por meses adicionales&#58;&#160; 
 &#123;&#123;valor_a_facturar&#125;&#125; = &#123;&#123;valor_a_facturar_mes_en_curso&#125;&#125; + &#123;&#123;valor_a_facturar_meses_adicionales&#125;&#125; 
&#160; 
 El sistema deber presentar dicha sumatoria as&#58;&#160; 
 class=lbl_a_pagar ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficarios&amp;idlabel= lbl_a_pagar )&#160; &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;valor_a_facturar&#125;&#125;&#160; &#160; 

&#160; 
 Periodo de facturacin 
 class= lbl_bill_period (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_bill_period )&#160;&#160;&#160; 
 &#123;&#123;fecha_actual&#125;&#125;&#160; - &#123;&#123;ltimo_dia_periodo_facturable&#125;&#125;&#160; 
&#160; 
 El sistema debe informar la fecha actual y la fecha correspondiente al ltimo da del periodo facturable, segn la seleccin que se realiz en el primer selector de la presente card.&#160;&#160; 
&#160; 
 Con esta actualizacin tu cuenta EatCloud pasar a tener licencia &#123;&#123;nombre_del_nuevo_plan&#125;&#125;&#160;&#160; 
 class=lbl_con_esta_actualizacion ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_con_esta_actualizacion ) &#123;&#123;nombre_del_nuevo_plan&#125;&#125;&#160; 

&#160; 
 ***AJUSTE&#58;&#160; Botn&#58; &quot;Actualizar Plan&quot; (antes Botn&#58; &quot;Aceptar&quot;) *** 
 class=lbl_actualizar_plan ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualizar_plan )&#160;&#160; 
&#160; 
 Al oprimir este botn se desplegar una ventana modal de confirmacin de la siguiente manera 

 E NVO DE DATOS PARA INTEGRACIN CON PASARELA DE PAGO Y REALIZACIN DEL PAGO 
 En este punto, el sistema deber enviar los datos del producto a facturar&#58; (De ser necesario&#58; eatc_licenses_prices. name (eatc_licenses_prices. name_lbl ), eatc_licenses_prices. description (eatc_licenses_prices. description_lbl ) ) y su respectivo &#123;&#123;valor_a_facturar&#125;&#125; a la pasarela de pagos, para la realizacin del pago .&#160; Con el pago confirmado, se realizan los dems procesos, de acuerdo a las indicaciones respectivas.&#160; En una primera etapa, no se tendr en cuenta este proceso, y simplemente se comenzar con el siguiente. 

 A CTUALIZACIN DE LOS DATOS DEL GESTOR DE DONACIONES A PARTIR DE LA ACTUALIZACIN DE LICENCIA 
&#160; 
 Llamado al servicio &quot; updatedomalic &quot; 
 Segn la documentacin, del servicio en cuestin , al recibir la confirmacin del pago se deber enviar la informacin de la cuenta maestra, el gestor de donaciones, la nueva licencia adquirida y la fecha de validez de la licencia, seleccionada ( &#123;&#123;eatc_license_valid_until&#125;&#125; ) 

&#160; 
 Mensajes para informar sobre el proceso 
 Los siguientes mensajes se debern ir desplegando al usuario a medida que progresa el proceso de edicin de datos, para mantenerlo informado del progreso y resultado del proceso (puede ser mediante toast por ejemplo) 
&#160; 
 Mensaje que se despliega mientras el proceso se est ejecutando&#58; &quot; Actualizando datos de la institucin beneficiaria &quot; 
 class=lbl_actualizando_doma ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualizando_doma )&#160;&#160;&#160; 
&#160; 
 Mensaje que se despliega ante una falla de ejecucin del proceso&#58; &quot; Reintentando &quot; 
 Si el servicio responde con el mensaje&#58; 
 op&#58;false 
 o 
 incomplete_data 
&#160; 
 El sistema deber desplegar el siguiente mensaje&#58; 
 class=lbl_reintentando ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_reintentando )&#160;&#160; 
&#160; 
 Y deber reintentar de nuevo, verificando que se enven los datos completos.&#160; Despus de tres reintentos fallidos, se deber desplegar el mensaje&#58; 
&#160; 
 Mensaje actualizacin fallida (definitiva&#58; despus de tres reintentos)&#58; &quot;No pudimos editar los datos de tu organizacin. Comuncate con nuestra mesa de ayuda&quot; 
 class=lbl_actualizando_doma_falla2 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualizando_doma_falla2 )&#160;&#160; 
&#160; 
 El sistema deber generar automticamente un correo electrnico, con los datos de la transaccin generada (y que se detalla ms adelante ) al correo de soporte@eatcloud.com 

&#160; 
 Mensaje actualizacin fallida, por gestor inactivo&#58; &quot;Por favor actvate para poder actualizar tus datos. Comuncate con nuestra mesa de ayuda&quot; 
 Si el servicio responde con el mensaje&#58; 
 fail_not_active_doma 
&#160; 
 El sistema deber desplegar el siguiente mensaje&#58; 
 class=lbl_ fail_not_active_doma ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_ fail_not_active_doma )&#160;&#160; 
&#160; 
 El sistema deber generar automticamente un correo electrnico, con los datos de la transaccin generada (y que se detalla ms adelante ) al correo de soporte@eatcloud.com 

&#160; 
 Mensaje actualizacin fallida, por pago no validado&#58; &quot;No pudimos validar tu pago. Comuncate con nuestra mesa de ayuda&quot; 
 Si el servicio responde con el mensaje&#58; 
 fail_not_valid_payment 
&#160; 
 El sistema deber desplegar el siguiente mensaje&#58; 
 class=lbl_ fail_not_valid_payment ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_ fail_not_valid_payment )&#160;&#160; 
&#160; 
 El sistema deber generar automticamente un correo electrnico, con los datos de la transaccin generada (y que se detalla ms adelante) al correo de soporte@eatcloud.com 

&#160; 
 Mensaje actualizacin exitosa&#58; &quot;Datos de la institucin beneficiaria exitosamente editados&quot; 
 class=lbl_actualizando_doma_exito ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualizando_doma_exito )&#160;&#160; 

 ENVO DE CORREO&#58; ANTE FALLA O TRANSACCIN EXITOSA&#58; 
 Encabezado falla&#58; 
 Se enviar un correo a &quot; soporte@eatcloud.com &quot; con el mensaje de error con el cual respondi el servicio, como ttulo del correo 
&#160; 
 Encabezado transaccin exitosa&#58; 
 Se enviar un correo a &quot; diana.alvarez@eatcloud.com &quot; con el ttulo &quot;Facturar a organizacin beneficiaria&quot; 
&#160; 
 Cuerpo del mensaje&#58; 
 En el cuerpo del mensaje se deber incluir el siguiente vnculo&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/&#123;&#123; _DOM.cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123; eatc_donation_managers. identificador_unico_registro&#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,unidad_territorial,municipio,departamento,telefono1,correo_electronico,eatc_state,eatc_license,eatc_license_valid_until 
&#160; 
 Y tambin los siguientes datos&#58; 
&#160; 
 Valor pagado&#58;&#160; 
 &#160; &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;valor_a_facturar&#125;&#125;&#160; &#160; 
&#160; 
 Periodo de facturacin 
&#160; 
 &#123;&#123;fecha_actual&#125;&#125;&#160; - &#123;&#123;ltimo_dia_periodo_facturable&#125;&#125;&#160; 
&#160; 
 &#123;&#123;nombre_del_nuevo_plan&#125;&#125;&#160;&#160; 
&#160; 
 &#123;&#123;IDENTIFICADOR_TRANSACCION_PASARELA_PAGO&#125;&#125; 

 (CONTINUAR MS ABAJO &#58; PANTALLA DE XITO DE LA TRANSACCIN )&#58; 
 PENDIENTE DE DOCUMENTAR&#58; Integracin con Facturacin electrnica del ERP 
&#160; 
 Autenticacin&#58; https&#58;//siigoapi.docs.apiary.io/#reference/autenticacion/generar-token/generar-token &#160; 
&#160; 
 Consultar cliente&#58; https&#58;//siigoapi.docs.apiary.io/#reference/clientes/consultar-cliente/consultar-cliente 
&#160; 
 Crear cliente&#58; https&#58;//siigoapi.docs.apiary.io/#reference/clientes/crear-cliente/crear-cliente 
&#160; 
 Crear factura&#58; https&#58;//siigoapi.docs.apiary.io/#reference/facturas-de-venta/crear-factura/crear-factura &#160; 
&#160; 
 Verificacin de la existencia o no del cliente en el ERP 
&#160; 
 El sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers&amp;fieldname=eatc_fiscal_id&amp;fieldvalue=&#123;&#123; eatc_fiscal_id &#125;&#125;&amp;fielddecrypt=eatc_fiscal_id,eatc_fiscal_name 
&#160; 
 Para determinar si existe un registro vlido en el parmetro eatc_customers. erp_id (lo cual es un indicativo de que el cliente no ha sido creado en el ERP).&#160; De no existir un registro vlido en dicho campo el sistema deber realizar el siguiente llamado (para crear primero el cliente en el ERP y luego generar la factura correspondiente)&#58; 
&#160; 
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
 &#123;&#123; _DOM .cua_user&#125;&#125; 

&#160; 
 Cantidad de puntos activos &#123;&#123; pods_activos &#125;&#125; 
 Que fueron obtenidos para las validaciones necesarias para consultar el precio de lista en la pgina de informacin de licencias (como se document anteriormente ). 

&#160; 
 &#123;&#123;nombre_del_plan_actual&#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Tu plan actual &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;nombre_del_nuevo_plan&#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;precio_actual&#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Tu plan actual &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;precio&#125;&#125; 
 Que fu obtenidopara la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;prorrata_periodo_restante&#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Facturacin &quot;&#160; (como se document ms arriba ). 

&#160; 
 &#123;&#123;precio_unitario_prorrateado&#125;&#125; 
 Es igual al precio menos el precio actual por la prorrata del periodo restante 
 &#123;&#123; precio_unitario_prorrateado &#125;&#125; = (&#123;&#123;precio&#125;&#125; - &#123;&#123;precio_actual&#125;&#125; ) * &#123;&#123; prorrata_periodo_restante &#125;&#125; 

&#160; 
 &#123;&#123;valor_a_facturar&#125;&#125; 
 Que fueron obtenidos para la construccin de la card &quot; Facturacin &quot;&#160; (como se document ms arriba ). 

&#160; 
 Consulta a la estructura eatc_licenses_prices 
 Con la consulta realizada a la respectiva estructura con el fin de mostrar el precio (en la pgina de&#160; informacin de los planes ), se toman los datos&#58;&#160; 
&#160; 
 eatc_licenses_prices. description ( eatc_licenses_prices. description_lbl) 
 eatc_licenses_prices. erp_product_id 
 eatc_licenses_prices. default_price_currency 

&#160; 
 Nota sobre el parmetro eatc_licenses_prices. description &#58; en una primera fase de implementacin se deber llevar el dato que est en este campo, pero en fases posteriores se deber llevar el resultado de la consulta del label que est registrado en el campo eatc_licenses_prices. description_lbl 
&#160; 
 Otros datos necesarios para integrarse con la cotizacin del ERP&#58; 
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
 &#123;&#123;URL_entorno_datagov&#125;&#125; /crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue=&#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125;&amp;fielddecrypt= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address 
&#160; 
 Y con el llamado se obtienen los siguientes datos&#160; desencriptados para realizar posteriormente el llamado al API para la creacin de la cotizacin 
&#160; 
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
 https&#58;//dev.datagov.eatcloud.info/crypt/ eatcloud /getcrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_id &amp;fieldvalue= 860004922 &amp;fielddecrypt= eatc_fiscal_id,eatc_fiscal_name,eatc_email,eatc_phone,eatc_address &#160;&#160; 
&#160; 
 Y con l obtiene los datos requeridos para el proceso. 

&#160; 
 Registro de la factura electrnica en el ERP&#58; 
 Documentacin&#58; https&#58;//developer.alegra.com/docs/crear-factura-de-venta &#160; 
&#160; 
 Para realizar el registro de la cotizacin segn la documentacin del ERP, se deber construir el siguiente JSON, para posteriormente enviarlo a travs de un llamado cURL que se especifica ms adelante&#58; 
&#160; 
 &#123;&#123;JSON_CURL&#125;&#125; 
 &#123; 
 &#160;&#160;&quot;date&quot; &#58; &quot;&#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125;&quot;, 
 &#160;&#160;&quot;dueDate&quot; &#58; &quot;&#123;&#123;timestamp en formato AAAA-MM-DD&#125;&#125;&quot;, 
 &#160;&#160;&quot;observations&quot; &#58; &quot;Cuenta&#58; &#123;&#123; _DOM .cua_user&#125;&#125; - Razn social&#58; &#123;&#123;eatc_customer. eatc_fiscal_name &#125;&#125; - NIT&#58; &#123;&#123;eatc_customers_cua. eatc_customer_fiscal_id &#125;&#125; - Email contacto&#58; &#123;&#123;eatc_customer. eatc_email &#125;&#125; - Telfono&#58; &#123;&#123;eatc_customer. eatc_phone &#125;&#125; - Ciudad&#58; &#123;&#123;eatc_customer. eatc_city &#125;&#125; - Pas&#58; &#123;&#123;eatc_customer. eatc_country &#125;&#125;&quot; - Actualizacin licencia rescate de&#58; &#123;&#123;nombre_del_plan_actual&#125;&#125; a &#123;&#123;nombre_del_nuevo_plan&#125;&#125;&quot;, 
 &#160;&#160;&quot;anotation&quot; &#58; &quot;Nota &#58; Favor consignar a la cuenta Cuenta de Ahorros Bancolombia 36000000518 a nombre de EatCloud SAS BIC. Tendrs 48 horas para realizar el pago o tu actualizacin de licencia ser reversada.&quot;, 
 &#160;&#160;&quot;termsConditions&quot; &#58; &quot;Esta factura se asimila en todos sus efectos a una letra de cambio de conformidad con el Art. 774 del cdigo de comercio. Autorizo que en caso de incumplimiento de esta obligacin sea reportado a las centrales de riesgo, se cobraran intereses por mora. Servicios excluidos de IVA Art 476ET N 21&quot;, 
 &#160;&#160;&quot;status&quot; &#58; &quot;open&quot;, 
 &#160;&#160;&quot;client&quot;&#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot;&#58; &#123;&#123;eatc_customer. erp_id&#125;&#125; 
 &#160;&#160;&#160;&#160;&#125;, 
 &quot;numberTemplate&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&quot;id&quot; &#58; 1 
 &#160;&#160;&#125;, 
 &#160;&#160;&quot;seller&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot; &#58; &quot;1&quot; 
 &#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&quot;currency&quot; &#58; &#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;code&quot; &#58; &quot;&#123;&#123;eatc_licenses_prices. default_price_currency &#125;&#125;&quot; , 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;exchangeRate&quot; &#58; 1 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125;, 
 &#160;&#160;&#160;&#160;&quot;items&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot;&#58; &#123;&#123;eatc_licenses_prices. erp_product_id &#125;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;description&quot;&#58; &quot;&#123;&#123;eatc_licenses_prices. description &#125;&#125;&quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;discount&quot; &#58; 0, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;tax&quot; &#58; [ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;id&quot; &#58; =&gt; Este dato no se enva porque este tipo de servicios estn excentos de IVA 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;], 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;price&quot; &#58; &#123;&#123; precio_unitario_prorrateado &#125;&#125;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;quantity&quot; &#58; &#123;&#123; pods_activos &#125;&#125; 
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
 class=lbl_actualizacion_licencia_exitosa ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_actualizacion_licencia_exitosa )&#160; 
&#160; 
 &#123;&#123;nombre_del_nuevo_plan&#125;&#125; 
 Que fu obtenido para la construccin de la card &quot; Nuevo plan &quot;&#160; (como se document ms arriba). 

 &#123;&#123;moneda&#125;&#125; &#123;&#123;precio&#125;&#125; mensual 
 Con los valores obtenidos se concatena la siguiente informacin&#58; 
 &#123;&#123;eatc_licenses_prices . default_price_currency &#125;&#125; &#123;&#123;precio&#125;&#125; &#123;&#123;eatc_licenses_prices . cua_type_period &#125;&#125; ( class= lbl_mensual ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_mensual ))&#160; &#160; 
&#160; 
 Vlida hasta 
 class=lbl_valida_hasta ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_valida_hasta )&#160; 
&#160; 
 &#123;&#123;eatc_donation_managers. eatc_license_valid_until &#125;&#125; 
&#160; 
 Botn finalizar 
 class=lbl_finalizar ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_finalizar )&#160;&#160; 
&#160; 
 Redireccin a la nube de donaciones 
 El sistema deber redireccionar al hacer clic en el botn finalizar a la nube de donaciones 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresumen-pedido-licencias-gestores-de-donaci%C3%B3n%2F2986593311-resumen_pedido_2_enc--2-.jpg&ow=1127&oh=189, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fresumen-pedido-licencias-gestores-de-donaci%C3%B3n%2F2986593311-resumen_pedido_2_enc--2-.jpg&ow=1127&oh=189 
 EatCloud Beneficiarios 

 575.000000000000 

 RESUMEN DE PEDIDO LICENCIAS GESTORES DE DONACIONES