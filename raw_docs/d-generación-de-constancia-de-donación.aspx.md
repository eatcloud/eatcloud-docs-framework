# d-generación-de-constancia-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Introduccin&#58; 
 Esta funcionalidad constar de un informe de anuncios de donacin &quot;recibidos&quot; (es decir, aquellos que ya han pasado por el proceso de verificacin por parte del &quot;gestor de donaciones&quot; y le permitir al usuario seleccionar a demanda que anuncio o conjunto de anuncios desea &quot;pre-cerficicar&quot;, para que el sistema genere un informe o constancia de donacin donde incluya la informacin general de dichos anuncios y sus respectivos detalles. 
&#160; 
 Informacin que trae la lista de anuncios que pueden ser seleccionados para &quot;pre-certificarse&quot; 
 La funcionalidad presenta una lista de anuncios de donacin cuyo ( eatc_dona_states ), es &quot;received&quot; o entregado , es decir, en la lista se deben mostrar los anuncios que ya han sido verificados por parte del gestor de donaciones. 
&#160; 
 Consulta de anuncios ***DINAMIZAR CON CONSULTA DE CUENTA MAESTRA*** 
 el sistema toma el parmetro&#160; &quot;_DOM.cua_user&quot; que se entrega por la URL del ingreso al BO&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/BO/&#123;&#123;_DOM.cua_user&#125;&#125; 
&#160; 
 El sistema debe tomar la cuenta maestra de la cuenta respectiva para realizar la consulta de los anuncios que le corresponden&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; =&gt; eatc_cua_master 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= received 

&#160; 
 Ejemplo xito en ambiente de pruebas&#58; 
 En el BO del Exito ( https&#58;//devdonantes.eatcloud.info/bo/exito ) se consulta la cuenta para establecer la cuenta maestra 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito eatc_cua_master=abaco 
&#160; 
 Entonces la consulta para traer los anuncios es&#58; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-donor=exito&amp;eatc-state= received &#160; 

 Ttulo de la funcionalidad&#58; Constancia de donacin 
 class=&quot; lbl_constancia_donacin &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_constancia_donacion ) 
&#160; 
 Descripcin de la funcionalidad 
 class=&quot; lbl_constancia_donacion _desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_constancia_donacin_desc ) 
&#160; 
 &quot;Con esta funcionalidad podrs generar una carta de constancia de la realizacin de tus donaciones, efectivamente recibidas por los beneficiarios.&#160; Si generas una constancia no podrs generar un certificado de las donaciones seleccionadas.&quot; 
&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 
&#160; 
 ***NUEVO&#58; PESTAAS PARA LA GENERACIN DE CONSTANCIA*** 
&#160; 
 NUEVO (no est en la implementacin actual)&#58; texto explicativo de las pestaas 
 class=&quot; lbl_explicacion_pestanas_constancia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_explicacion_pestanas_constancia )&#160; 
&#160; 
 Dirgete primero a la pestaa para seleccionar los anuncios a los cuales le vas a expedir constancia.&#160; Una vez seleccionados dichos anuncios, dirgete a la pestaa para generar la constancia. 
&#160; 
 Paso1&#58; Seleccionar anuncios para constancia (primera pestaa) 
 class=&quot; lbl_p1_seleccionar_anuncios_constancia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_p1_seleccionar_anuncios_constancia )&#160; 
&#160; 
 Seleccionar todo 
 class=&quot; lbl_seleccionar_todo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_seleccionar_todo )&#160; 
&#160; 
 En esta pestaa se presentan las cards de los anuncios de donacin , cuyos labels se documentan ms adelante 
&#160; 
 Paso2&#58; Generar constancia (segunda pestaa) 
 class=&quot; lbl_p2_generar_constancia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_p2_generar_constancia )&#160; 
&#160; 
 Vista previa 
 class=&quot; lbl_vista_previa &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_vista_previa )&#160; 
&#160; 
 Generar directamente 
 class=&quot; lbl_generar_directamente &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_generar_directamente )&#160;&#160; 
&#160; 
 Con estos botones se da paso a lo documentado ms adelante con respecto a la generacin de la constancia de donacin y su visualizacin 
&#160; 
 CARD DEL ANUNCIO DE DONACIN 
 Es un informe muy similar al &quot; informe operativo de donaciones &quot; (se debe procurar reutilizar la mayor cantidad de cdigo posible). El informe debe ser construido en tiempo real para mostrar la fotografa (o estado actual) de los anuncios en el momento que se carga el informe. Se debe pensar en refrescar de manera automtica esta carga cada cierto tiempo.&#160; 
 Cada anuncio de donacin ( eatc_dona_headers ) se presenta en una tarjeta que contiene la siguiente informacin&#58; 

 ENCABEZADO&#58; 
 Cdigo del anuncio&#58; 
 clase=&quot; lbl_codigo_anuncio &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_codigo_anuncio )&#160; 

&#160; 
 &#160; eatc_dona_headers .eatc-code 

&#160; 
 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre&#58; 
 clase=&quot; lbl_nombre_doma &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_nombre_doma )&#160; 

&#160; 
 eatc_dona_headers .eatc-donation_manager_name 

&#160; 
 Direccin&#58;&#160; 
 clase=&quot; lbl_direccion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_direccion )&#160; 

&#160; 
 eatc_dona_headers .eatc-donation_manager_address 

&#160; 
 Telfono&#58;&#160; 
 clase=&quot; lbl_telefono &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_telefono )&#160; 

&#160; 
 eatc_dona_headers .eatc-donation_manager_phone 

&#160; 
 Ver mapa&#58;&#160; ***PENDIENTE*** 
 clase=&quot; lbl_ver_mapa &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ver_mapa )&#160; 

&#160; 
 consulta de las coordenadas del anuncio eatc_dona_headers .eatc-lat, eatc_dona_headers .eatc-long 
&#160; 
 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga&#58; 
&#160; 
 &quot;PENDIENTE DE ADJUDICACIN&quot;&#160; 
 clase=&quot; lbl_pendiente_adjudicacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_pendiente_adjudicacion )&#160; 

&#160; 
 DETALLE ANUNCIO&#58; 
 Peso total&#160; 
 clase=&quot; lbl_peso_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_peso_total ) 

&#160; 
 eatc_dona_headers .eatc-total_weight_kg 

&#160; 
 Valor total =&gt; Valor al costo 
 clase=&quot; lbl_valor_al_costo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_valor_al_costo )&#160; 

&#160; 
 eatc_dona_headers .eatc-total_cost 

&#160; 
 TRACKING&#58; 
 Hora publicacin 
 clase=&quot; lbl_hora_publicacin &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hora_publicacin )&#160; 

&#160; 
 eatc_dona_headers .eatc-publication_datetime 

&#160; 
 Hora adjudicacin 
 clase=&quot; lbl_hora_adjudicacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hora_adjudicacion )&#160; 

&#160; 
 eatc_dona_headers .eatc-adjudication_datetime 

&#160; 
 Hora de entrega programada 
 clase=&quot; lbl_hora_entrega_programada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_hora_entrega_programada )&#160; 

&#160; 
 eatc_dona_headers .eatc-programed_picking_datetime 

&#160; 
 Hora de entrega real llegada 
 clase=&quot; lbl_hora_entrega_real_llegada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hora_entrega_real_llegada ) 

&#160; 
 eatc_dona_headers .eatc-picking_checkin_datetime 

&#160; 
 Hora de entrega real salida 
 clase=&quot; lbl_hora_entrega_real_salida &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hora_entrega_real_salida )&#160; 

&#160; 
 eatc_dona_headers .eatc-picking_checkout_datetime 

&#160; 
 Hora de recepcin 
 clase=&quot; lbl_hora_recepcion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hora_recepcion )&#160; 

&#160; 
 eatc_dona_headers .eatc-receipt_datetime 
&#160; 
 ESTADO ( eatc_dona_states ) 
 clase=&quot; lbl_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_estado )&#160; 

&#160; 
 Slo se muestran anuncios con estado &quot;delivered&quot; o &quot;entregados&quot;&#160; 
&#160; 
 Botn + *** PENDIENTE*** 
 Este botn dar la entrada a la funcionalidad &quot; dashboard de anuncio de donacin (eatc_dona_dsh) &quot;, pasando el identificador del encabezado ( eatc-id ). 

&#160; 
 Botn&#58; Consulta de novedades *** PENDIENTE*** 
 clase=&quot; lbl_consulta_novedades &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consulta_novedades) 

&#160; 
 Con este botn se debe generar una consulta al registro de novedades ( eatc_odd_rejection_registry ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la informacin que trae la consulta. 
 Ejemplo&#58; 
 Para el anuncio cuyo cdigo de encabezado ( eatc-dona_header_code) es 40716, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code=40716 
&#160; 
 CHECKBOX PARA SELECCIONAR ANUNCIOS A EXPEDRSELES CONSTANCIA 
 Cada anuncio debe tener un botn que permita seleccionarlo para ser generarle la constancia.&#160; El usuario puede seleccionar uno, varios o todos los anuncios presentes en la lista (debe haber una funcionalidad rpida para seleccionarlos todos&quot; 
 clase=&quot; lbl_seleccionar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_seleccionar )&#160; 

&#160; 
 BOTN&#58; &quot;Generar constancia de donacin&quot; ***NUEVO&#58; configuracin de labels**** 
 Una vez que se halla seleccionado por lo menos un anuncio de donacin a &quot;pre-certificar&quot;, se debe mostrar el botn &quot;generar constancia de donacin&quot;.&#160; Al oprimirlo, el sistema debe cambiar el estado de todos los anuncios seleccionados a &quot;pre-certified&quot; o &quot;pre-certificado&quot; y generar un informe, que debe ser susceptible de ser impreso o enviado a una direccin de correo electrnico con la siguiente informacin, construida a partir de la informacin de los anuncios seleccionados&#58; 

&#160; 

 Municipio&#58;&#160; 
 clase=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ciudad )&#160; 
&#160; 
 Siempre ser &quot; Bogot &quot; (obligatorio) 

&#160; 

 Fecha de expedicin de la constancia&#58;&#160; 
 clase=&quot; lbl_fecha_expedicion_constancia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_expedicion_constancia )&#160; 
&#160; 
 &#160;&#123;Da&#125; del &#123;Mes&#125; de &#123;Ao&#125; que corresponde a la fecha actual, es decir la fecha en la que se oprimi el botn para generar la constancia Ej&#58; 01 de Enero de 2019 (obligatorio). 

&#160; 

 Consecutivo&#58;&#160; 
 clase=&quot; lbl_consecutivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consecutivo ) 
&#160; 
 Todos las constancias de donacin debe emitirse con un nmero de consecutivo, con prefijo EC-Cons, iniciando desde el Nmero 1 (obligatorio) 

&#160; 

 Ao&#58;&#160; 
 clase=&quot; lbl_year &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_year )&#160; 
&#160; 
 en formato (yyyy), corresponde al ao en curso (obligatorio) 

&#160; 

 Mes de entrega de la donacin&#58; &#160; 
 clase=&quot; lbl_mes_entrega_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_mes_entrega_donacion ) 
&#160; 
 Mes de la entrega de la donacin&#160; Ej&#58; &quot;Enero&quot;.&#160; Debe corresponder al mes o los meses que se encuentran registrados en la fecha eatc_dona_headers .eatc-receipt_datetime &#160; (obligatorio) 

&#160; 

 Ao de entrega donacin&#58;&#160; 
 clase=&quot; lbl_year_entrega_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_year_entrega_donacion )&#160; 
&#160; 
 en formato (yyyy). Debe corresponder al ao o los aos que se encuentran registrados en la fecha eatc_dona_headers .eatc-receipt_datetime (obligatorio). 

&#160; 

 &#160;Donante&#58;&#160; 
 clase=&quot; lbl_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_donante )&#160; 
&#160; 
 Razn social del donante, corresponde al dato eatc_dona_headers .eatc-donor (obligatorio) 

&#160; 

 &#160;Nmero de identificacin del donante&#58;&#160; 
 clase=&quot; lbl_doc_id_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_id_donante )&#160; 
&#160; 
 Identificador nico del donante (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, sin el dgito de verificacin (obligatorio). 

&#160; 

 DV&#58; &#160;&#160; 
 clase=&quot; lbl_dv &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_dv )&#160; 
&#160; 
 Dgito de verificacin del (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, despus del &quot;-&quot;, o dgito de verificacin (obligatorio) 

&#160; 

 Kilos&#58;&#160; 
 clase=&quot; lbl_kg &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg )&#160;&#160; 
&#160; 
 Cantidad de kilos reportados como recibidos acorde a la donacin anunciada y entregada .&#160; Corresponde a la sumatoria del campo eatc_dona_headers .eatc-total_weight_kg de todos los anuncios de donacin seleccionados (obligatorio) 

&#160; 

 Categora&#58;&#160; 
 clase=&quot; lbl_categoria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_categoria )&#160; 
&#160; 
 Categora del producto entregado en donacin anunciada y entregada.&#160; Corresponde a un array del distinct de categoras presentes en los detalles de todos los anuncios de donacin seleccionados para certificar eatc_dona. eatc-odd_typology_a (obligatorio) 

&#160; 

 De acuerdo a los anuncios de donacin cuyos cdigos son&#58; 
 clase=&quot; lbl_de_acuerdo_a_dona &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_de_acuerdo_a_dona) 
&#160; 
 nmero de documento asociado a la entrega del producto, puede ser 1 documento o varios documentos. Corresponde al array de eatc_dona_headers .eatc-code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio) 

 ANTERIORMENTE&#58; Documento soporte de entrega de donacin&#58;&#160; clase=&quot; lbl_doc_soporte_entrega_dona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_soporte_entrega_dona ) 
&#160; 

 Organizacin(es) beneficiada(s)&#58; 
 clase=&quot; lbl_org_beneficiada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_org_beneficiada )&#160; 
&#160; 
 Nombre del gestor de donacin o los gestores de donaciones a los cuales se les adjudicaron los anuncios, puede ser 1 o varias organizaciones.&#160; Corresponde al array de datos de eatc- eatc_dona_headers . donation_manager_name de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.&#160; DE SER NECESARIO EL BANCO HABRA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIN EN https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA y con ese dato obtener con la misma API el nombre de dicho banco) 

&#160; 

 NIT Beneficiarios&#58;&#160; 
 clase=&quot; lbl_doc_id_beneficiarios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_id_beneficiarios )&#160; 
&#160; 
 Identificador de los gestores de donaciones (NIT), puede ser 1 o varios (obligatorio). Corresponde al array de datos de eatc_dona_headers . donation_manager_code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.&#160; DE SER NECESARIO EL BANCO HABRA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIN EN https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA) 

&#160; 

 Representante legal ABACO&#58;&#160; 
 clase=&quot; lbl_representate_legal_abaco &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_representate_legal_abaco )&#160; 
&#160; 
 siempre ser el de ABACO. Corresponde al dato &quot;representante_legal&quot; de la siguiente consulta&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador=ABACO (obligatorio) 

&#160; 

 Cargo&#58;&#160; 
 clase=&quot; lbl_cargo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cargo ) 
&#160; 
 Siempre se escribe&#58; Director Ejecutivo (obligatorio) 

&#160; 

 Elabor certificado&#58;&#160; 
 clase=&quot; lbl_elaboro_certificado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_elaboro_certificado )&#160; 
&#160; 
 Debe parametrizarse por ahora las siguientes iniciales&#58; N.J.H.H. Si N.J.H.H. (obligatorio) 

&#160; 

 Aprob certificado&#58;&#160; 
 clase=&quot; lbl_aprobo_certificado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_aprobo_certificado )&#160; 
&#160; 
 Debe parametrizarse por ahora las siguientes iniciales&#58; I.V.B.P. Si I.V.B.P. (obligatorio) 

&#160; 

 Revis certificado&#58;&#160; 
 clase=&quot; lbl_reviso_certificado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_reviso_certificado )&#160; 
&#160; 
 Debe parametrizarse por ahora las siguientes iniciales&#58; M.M.P. Si M.M.P. (obligatorio) 

 ***NUEVO***Datos que se llevan al encabezado del anuncio de donacin 
 Cuando se genera la constancia se deben llevar los siguientes datos al registro de los encabezados que &#58; 
eatc_dona_headers . eatc_constancy_datetime &#58; corresponde al timestamp de cuando se realiz la constancia en formato AAAA-MM-DD HH&#58;MM&#58;SS 
eatc_dona_headers . eatc_constancy_consecutive &#58; corresponde al consecutivo de la constancia que se gener 
&#160; 
 NOTA IMPORTANTE&#58; 
&#160; 
 Anteriormente el proceso de generacin de constancia llevaba el dato &quot;precertified&quot; a eatc_dona_headers . eatc_state . Esta especificacin implica precisamente reemplazar dicho registro, por lo tanto al crearse la constancia ya NO se debe cambiar el estado de la donacin . 

 Descarga de detalles de anuncios de donacin con constancia 
 Se debe permitir descargar un archivo en Excel o .csv que contenga los detalles de los anuncios certificados y que tenga la siguiente estructura&#58; 

 Ttulo&#58; Listado de constancias 
 clase=&quot; lbl_listado_constancias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_listado_constancias )&#160; 
&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 

 Listado 

 Operaciones&#58; 
 clase=&quot; lbl_operaciones &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_operaciones )&#160; 

&#160; 

 Municipio&#58;&#160; 
 clase=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_ciudad )&#160; 
&#160; 
 Siempre ser &quot; Bogot &quot; (obligatorio) 

&#160; 

 Fecha de expedicin de la constancia&#58;&#160; 
 clase=&quot; lbl_fecha_expedicion_constancia &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_expedicion_constancia )&#160; 
 &#160; 
 &#123;Da&#125; del &#123;Mes&#125; de &#123;Ao&#125; que corresponde a la fecha actual, es decir la fecha en la que se oprimi el botn para generar la constancia Ej&#58; 01 de Enero de 2019 (obligatorio). 

&#160; 

 Consecutivo&#58;&#160; 
 clase=&quot; lbl_consecutivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consecutivo ) 
&#160; 
 Todos las constancias de donacin debe emitirse con un nmero de consecutivo, con prefijo EC-Cons, iniciando desde el Nmero 1 (obligatorio) 

&#160; 

 Ao&#58;&#160; 
 clase=&quot; lbl_year &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_year )&#160; 
&#160; 
 en formato (yyyy), corresponde al ao en curso (obligatorio) 

&#160; 

 Mes de entrega de la donacin&#58; &#160; 
 clase=&quot; lbl_mes_entrega_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_mes_entrega_donacion ) 
&#160; 
 Mes de la entrega de la donacin&#160; Ej&#58; &quot;Enero&quot;.&#160; Debe corresponder al mes o los meses que se encuentran registrados en la fecha eatc_dona_headers .eatc-receipt_datetime &#160; (obligatorio) 

&#160; 

 &#160;Donante&#58;&#160; 
 clase=&quot; lbl_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_donante )&#160; 

&#160; 

 Nmero de identificacin del donante&#58;&#160; 
 clase=&quot; lbl_doc_id_donante &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_id_donante )&#160; 
&#160; 
 Identificador nico del donante (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, sin el dgito de verificacin (obligatorio). 

&#160; 

 DV&#58; &#160;&#160; 
 clase=&quot; lbl_dv &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_dv )&#160; 
&#160; 
 Dgito de verificacin del (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, despus del &quot;-&quot;, o dgito de verificacin (obligatorio) 

&#160; 

 Kilos&#58;&#160; 
 clase=&quot; lbl_kg &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_kg )&#160;&#160; 
&#160; 
 Cantidad de kilos reportados como recibidos acorde a la donacin anunciada y entregada .&#160; Corresponde a la sumatoria del campo eatc_dona_headers .eatc-total_weight_kg de todos los anuncios de donacin seleccionados (obligatorio) 

&#160; 

 Productos&#58;&#160; 
 clase=&quot; lbl_productos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_productos )&#160; 
&#160; 
 Cantidad de kilos reportados como recibidos acorde a la donacin anunciada y entregada .&#160; Corresponde a la sumatoria del campo eatc_dona_headers .eatc-total_weight_kg de todos los anuncios de donacin seleccionados (obligatorio) 

&#160; 

 Categora&#58;&#160; 
 clase=&quot; lbl_categoria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_categoria )&#160; 
 Categora del producto entregado en donacin anunciada y entregada.&#160; Corresponde a un array del distinct de categoras presentes en los detalles de todos los anuncios de donacin seleccionados para certificar eatc_dona. eatc-odd_typology_a (obligatorio) 

&#160; 

 Documento soporte de entrega de donacin&#58;&#160; 
 clase=&quot; lbl_doc_soporte_entrega_dona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_soporte_entrega_dona )&#160; 
&#160; 
 nmero de documento asociado a la entrega del producto, puede ser 1 documento o varios documentos. Corresponde al array de eatc_dona_headers .eatc-code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio) 
&#160; 

 Organizacin(es) beneficiada(s)&#58; 
 clase=&quot; lbl_org_beneficiada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_org_beneficiada )&#160; 
&#160; 
 Nombre del gestor de donacin o los gestores de donaciones a los cuales se les adjudicaron los anuncios, puede ser 1 o varias organizaciones.&#160; Corresponde al array de datos de eatc- eatc_dona_headers . donation_manager_name de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.&#160; DE SER NECESARIO EL BANCO HABRA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIN EN https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA y con ese dato obtener con la misma API el nombre de dicho banco) 

&#160; 

 NIT Beneficiarios&#58;&#160; 
 clase=&quot; lbl_doc_id_beneficiarios &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_doc_id_beneficiarios )&#160; 
&#160; 
 Identificador de los gestores de donaciones (NIT), puede ser 1 o varios (obligatorio). Corresponde al array de datos de eatc_dona_headers . donation_manager_code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.&#160; DE SER NECESARIO EL BANCO HABRA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIN EN https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA) 

&#160; 

 Representante legal ABACO&#58;&#160; 
 clase=&quot; lbl_representate_legal_abaco &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_representate_legal_abaco )&#160; 
&#160; 
 siempre ser el de ABACO. Corresponde al dato &quot;representante_legal&quot; de la siguiente consulta&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador=ABACO (obligatorio) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fd-generaci%C3%B3n-de-constancia-de-donaci%C3%B3n%2F2155297035-constancia_donacion_form.jpg&ow=1280&oh=638, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fd-generaci%C3%B3n-de-constancia-de-donaci%C3%B3n%2F2155297035-constancia_donacion_form.jpg&ow=1280&oh=638 

 256.000000000000 

 GENERACIN DE CONSTANCIA DE DONACIN