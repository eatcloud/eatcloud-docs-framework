# factura-electrónica-colombia-método-de-soporte-prep-cert.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Método se Soporte Factura electrónica Colombia 
 Diagrama de flujo 
&#160; 
 Al seleccionar este método de soporte el sistema desplegará los siguientes módulos funcionales 
 Consulta de la configuración del método de soporte 
 Pregunta para determinar si se muestran los anuncios del mes anterior o del mes actual 
 Selector de NITs (para cuenta con múltiples donantes) 
 Sumatorias para el listado de anuncios soportados 
 Listado de anuncios soportados para seleccionar 
 Botón “Confirmar anuncios a soportar” 
 Consolidación de productos donados a certificar 
 Despliegue de formulario para subida de factura electrónica 
 Validación de datos de la factura 
 La fecha de la factura tiene que corresponder a la fecha de la factura del mes en que se recibieron las donaciones 
 La razón social de a quién se le expide la factura corresponde la razón social de Ábaco 
 El NIT de a quién se le expide la factura corresponde la NIT de Ábaco 
 La razón social de quien expide la factura corresponde al eatc_donor_fiscal_name registrado en las donaciones 
 El NIT de quien emite la factura corresponde al eatc_donor_code registrado en las donaciones 
 Número de la factura no puede estar repetido 
 Registro de datos de cabecera de soporte (una vez se han validado los datos del encabezado de la factura) 
 VALIDACIONES PARA LAS LÍNEAS DE LA FACTURA (&lt;cac&#58;invoiceline&gt;) 
 El código de los ítems de la factura debe corresponder al código de los items consolidados 
 La descripción de los ítems de la factura debe corresponder a la descripción de los ítems consolidados 
 Las cantidades de los ítems de la factura deben ser menores o iguales a las cantidades de los ítems consolidados 
 OTROS DATOS DE LAS LÍNEAS DE LA FACTURA (&lt;cac&#58;invoiceline&gt;) que se llevan al registro si las anteriores validaciones son exitosas&#58; 
 Valor unitario del ítem antes de IVA 
 Valor total del ítem antes de IVA 
 Registro de datos de detalle de productos (una vez se tiene la validación de los detalles de manera exitosa) 

 DIAGRAMA DE FLUJO &#58;&#160; 
 Método de soporte&#58; factura_electronica_colombia 

 Consulta de la configuración del método de soporte 
 Si el usuario seleccionó o dejó el selector en la posición del método &quot; factura_electronica_colombia &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_dona_certification_supports ? eatc_dona_certification_support =factura_electronica_colombia &#160;&#160; 
&#160; 
 El sistema obtiene los siguientes datos, que a continuación se detallan de acuerdo a la por el momento única opción para este método.&#160; El desarrollo por tanto deberá contemplar la implementación como un caso dentro de posibles futuros casos diferentes, que por el momento tendrá una opción a partir de los siguientes datos&#58; 
&#160; 
 _id &#58; &quot;2&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 eatc_dona_certification_support &#58; &quot;factura_electronica_colombia&quot;, 
 eatc_label &#58; &quot;class=”lbl_factura_electronica_colombiana”&quot;, 
 eatc_support_generation_method &#58; &quot;upload&quot;, 
 eatc_support_generation_method_desc_label &#58; &quot;class=”lbl_selecciona_anuncios_a_soportar”&quot;, 
 eatc_support_generation_frecuency &#58; &quot;a_demanda&quot;, 
 eatc_max_generation_day &#58; &quot;6&quot;, 
 eatc_file_extension_to_upload &#58; &quot;xml&quot;, 
 eatc_file_extension_to_validate &#58; &quot;xml&quot;, 
 eatc_months_back_to_support &#58; &quot;1&quot;, 
 eatc_montly_cut &#58; &quot;corte&quot;, 
 default &#58; &quot;no&quot;, 
 eatc_support_generation_method_accept_label &#58; &quot;class=”lbl_aceptacion_metodo_factura_electronica_colombia”&quot; 

 Pregunta para determinar si se muestran los anuncios del mes anterior o del mes actual 
 Dado que en los datos del método de soporte se encuentra esta información&#58; 
&#160; 
 eatc_support_generation_method&#58; &quot;upload&quot; 
 Esto quiere decir que la generación del soporte para el proceso de precertificación la realiza el usuario, subiendo el documento, el cual debe pasar por el proceso de validación respectivo 
&#160; 
 eatc_support_generation_frecuency&#58; &quot;a_demanda&quot; 
 Lo anterior quiere decir que el soporte &quot; factura_electronica_colombia &quot; se generará a demanda del usuario (por eso se podrá subir cuando el usuario lo determine). 
&#160; 
 eatc_max_generation_day&#58; &quot;6&quot; 
 El sistema debe preguntar hasta el día del mes que se indique en el parámetro eatc_max_generation_day (actualmente hasta el 6to día del mes), si se quieren ver los anuncios del mes anterior (que debe estar seleccionada por defecto) o del mes actual. 
&#160; 
 Label introductorio&#58; class=&quot; lbl_deseas_ver_donaciones_de &quot; 
 Opción por defecto del selector &#58; class=&quot; lbl_mes_anterior &quot; 
 Segunda opción&#58; class=&quot; lbl_mes_actual &quot; 
&#160; 
 Según la selección que realice el usuario, se deberán traer (en los primeros días del mes) los anuncios cuya fecha de recepción ( eatc_dona_headers .eatc-receipt_datetime ) corresponda al mes anterior o al mes actual. 
&#160; 
 Los demás días del mes, no debe mostrar este selector y debe consultar los anuncios cuya fecha de recepción ( eatc_dona_headers .eatc-receipt_datetime ) correspondan al mes en curso (dado que se obtiene esta información del método de soporte&#58; eatc_months_back_to_support &#58; &quot;1&quot; ).&#160;&#160; 
&#160; 
 NOTA &#58; si el dato del método eatc_months_back_to_support cambia a más meses, los labels del selector deben cambiar a&#58; 
 Opción por defecto del selector &#58; &lt; class=&quot; lbl_periodo_anterior &quot; &gt;&#58; &#123;&#123; eatc_months_back_to_support &#125;&#125; meses. 
 Segunda opción&#58; &lt; class=&quot; lbl_periodo_actual &quot; &gt; 
&#160; 
 Y las consultan deberán traer los anuncios correspondientes a los periodos definidos por el dato eatc_months_back_to_support 
&#160; 
 eatc_months_back_to_support&#58; &quot;1&quot; 
 Este parámetro indica que los anuncios aptos para soportarse por una factura (que principalmente cumplen dos condiciones&#58; tienen estado recibido (received) (Es decir que por ejemplo para ambiente de pruebas responden a esta consulta&#58; https&#58;//devdonantes.eatcloud.info/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state=received ) y no se les ha expedido constancia de donación (no poseen un registro de fecha válido en eatc_constancy_datetime o no poseen un registro válido en&#160; eatc_constancy_consecutive )) serán los de un mes atrás.&#160; Este dato, combinado con el siguiente, determina el método de consulta para traer los anuncios que serán soportados por la carta automática. 
&#160; 
 eatc_montly_cut&#58; &quot;corte&quot; 
 Esto quiere decir que el conteo del mes para atrás, se hace a corte mensual, es decir que el sistema debe evaluar el dato que llega en el parámetro eatc_dona_headers. eatc-receipt_datetime &#160; para establecer si el mes en el que se recibió el anuncio corresponde al mes en curso (para la implementación del informe de detalle de anuncios, se utilizó una función que establece el mes del anuncio , y esta se puede utilizar para realizar esta validación), desde el primer día del mes hasta el último. 
&#160; 
 Selector de NITs (para cuenta con múltiples donantes&#58;) 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;multiple_donors= si 

&#160; 
 label&#58; class=&quot; lbl_selecciona_nit &quot;&#160; 
&#160; 
 El sistema debe realizar un &quot; select distinct &quot; del dato eatc_dona_headers. eatc-donor_code , de los anuncios consultados según el criterio definido a partir del selector o consulta anterior ( lbl_mes_anterior , lbl_mes_actual ).&#160; 
&#160; 
 Mes anterior&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers? eatc-receipt_datetime[0]= &#123;&#123;fecha_primer_dia_mes_anterior&#125;&#125;&amp; eatc-receipt_datetime[1]= &#123;&#123;fecha_ultimo_dia_mes_anterior&#125;&#125;&amp;eatc-state= received &amp;_distinct= eatc-donor_code 
&#160; 
 Mes actual&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers? eatc-receipt_datetime[0]= &#123;&#123;fecha_primer_dia_mes_actual&#125;&#125;&amp; eatc-receipt_datetime[1]= &#123;&#123;fecha_actual&#125;&#125;&amp;eatc-state= received &amp;_distinct= eatc-donor_code 
&#160; 
 El usuario deberá escoger un &quot;NIT&quot; y dicho filtro se aplicará al listado de anuncios soportados (es decir que solamente se mostrarán los datos correspondientes al NIT seleccionado). 
&#160; 
 Sumatorias para el listado de anuncios soportados 
 Se debe presentar totales similares a los que se presentan en la funcionalidad Informe de detalle de anuncios en el BO adicionando solamente el número de anuncios certificables (que es la sumatoria de los anuncios eatc_dona_headers que responden los anuncios que se van seleccionando en el listado de anuncios a soportar con factura del que se habla más adelante &#58; 
&#160; 
 Título de los totales&#58; class=&quot; lbl_totales_sumatoria &quot; 
 Kilogramos aprovechados&#58; class=&quot; lbl_kg_aprovechados &quot; 
 Kilogramos no aprovechados&#58; class=&quot; lbl_kg_no_aprovechados &quot; 
 Unidades aprovechadas&#58; class=&quot; lbl_unidades_aprovechadas &quot; 
 Unidades no aprovechadas&#58; class=&quot; lbl_unidades_no_aprovechadas &quot; 
 Total anuncios certificables&#58; class=&quot; lbl_donaciones_certificables &quot; 
&#160; 
 Listado de anuncios soportados para seleccionar ***NUEVO&#58; sin incluir donaciones que ya tengan soporte generado *** 
 Tal como lo establece el label respectivo eatc_support_generation_method_desc_label ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel=lbl_selecciona_anuncios_a_soportar ) label que se debe mostrar al principio del listado, el sistema despliega un listado de los detalles de los anuncios que son susceptibles de ser soportados por la factura electrónica, permitiendo su selección (mediante un checkbox al inicio de cada registro) .&#160; Los anuncios que se deben mostrar en este listado, corresponde a los del mes en curso desde el primer día del mes ( eatc_dona_certification_supports . eatc_months_back_to_support &#58; &quot;1&quot;, y&#160; eatc_dona_certification_supports . eatc_montly_cut &#58; &quot;corte&quot; ) 
&#160; 
 Hasta el día 6 del mes siguiente ( eatc_dona_certification_supports . eatc_max_generation_day ) se podrán mostrar los anuncios del mes anterior (filtrados por el NIT seleccionado anteriormente). Dicho listado muestra los siguientes datos (se comporta de manera muy similar al listado desarrollado para la funcionalidad de Informe de detalle de anuncios en el BO , tanto para el listado, como para los totales, por lo tanto se puede utilizar dicha funcionalidad para reciclar código) , en donde se muestra información del detalle de cada donación acompañada de cierta información de encabezado 
&#160; 
 ***NUEVO&#58; En este listado no deben aparecer las donaciones que ya tienen un soporte generado.&#160; Revisando la documentación no se pudo establecer un registro que pueda relacionar las donaciones con los soportes, por eso fue necesario crear una nueva escritura tan pronto se validan los datos del encabezado del soporte , con el ánimo de poder tener dicha relación.&#160; A partir de dicha implementación, el sistema debe realizar la siguiente consulta, para el respectivo mes (cuando se habla de respectivo mes, se hace alución al selector de mes que se tiene al inicio de la funcionalidad&#58; si se selecciona el mes anterior, la fecha inicial será el primer día del mes anterior y la final el respectivo día.&#160; Si se selecciona el mes actual, la fecha inicial será el primer día del mes y la final el día actual)&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers_support ?eatc_dona_publication_date[0]=&#123;&#123;fecha_inicio_mes_respectivo&#125;&#125;&amp;eatc_dona_publication_date[0]=&#123;&#123;fecha_fin_mes_respectivo&#125;&#125;&amp;_cmp=eatc_dona_header_code 
&#160; 
 obteniendo el array de códigos de donaciones anterior, dicho array se debe enviar con el prefijo _nin_ al respectivo parámetro con el que se arma la consulta para traer la donación (bien sea si la misma se hace por dona_headers o por dona) 
&#160; 
 eatc_dona_headers? eatc-code = _nin_ &#123;&#123; array_codigos_donaciones_con_soportes &#125;&#125; 
 eatc_donas? eatc-dona_header_code = _nin_ &#123;&#123; array_codigos_donaciones_con_soportes &#125;&#125; 
 ***NUEVO&#58; &#160;se excluyen del listado aquellos anuncios de donación que pertenezcan a puntos de donación relacionados en la tabla&#160; eatc_doma_certification *** 
 Se ha creado una nueva tabla&#58; &#123;&#123;URL_datagov&#125;&#125;//api/eatcloud/eatc_doma_certification?eatc_cua_user=_* en donde se relacionarán puntos de donación que serán certificados por otras organizaciones (otros beneficiarios). 
 Por lo tanto el sistema deberá consultar los puntos de donación que se encuentren en dicha tabla 
 &#123;&#123;URL_datagov&#125;&#125;//api/eatcloud/ eatc_doma_certification ?eatc_cua_master=&#123;&#123; _DOM. cua_master &#125;&#125; &amp;eatc_cua_user=&#123;&#123; _DOM. cua_user &#125;&#125;&amp;_cmp= eatc_pod_id 
Si la respuesta de la anterior consulta es&#160; _ all , &#160;querrá decir que todos los puntos, que quiere decir también, todas las donaciones de este donante,&#160; no serán &#160;certificadas por ABACO. &#160; Si la respuesta arroja códigos de puntos &#160; &#123;&#123;array _pod_id&#125;&#125; , Las donaciones de dichos puntos no apaecerán en el listado de anuncios certificables, sino en un listado aparte denominado “Certificados por organizaciones diferentes a ABACO”, incorporando la misma información del listado original (abajo descrito) adicionando una columna que diga “Entidad que certifica” y mostrando para esos anuncios la información que se encuentra en 
 &#123;&#123;URL_datagov&#125;&#125;//api/eatcloud/ eatc_doma_certification ?eatc_cua_master=&#123;&#123; _DOM. cua_master &#125;&#125; &amp;eatc_cua_user=&#123;&#123; _DOM. cua_user &#125;&#125;&amp; eatc_pod_id= &#123;&#123; eatc_dona_headers. eatc-pod_id &#125;&#125;&amp;_cmp= eatc_certifying_doma_name 
Estos anuncios no serán seleccionables para adjuntárseles una factura (es decir estos anuncios quedan por fuera de las funcionalidades propias de la certificación por factura electrónica )
&#160; 
 *** 
 Los labels que se colocan a continuación servirán como títulos de las respectivas columnas que muestra el informe. La tabla de datos, debe permitir ocultar columnas y demás funcionalidades para ordenar la información por columnas. 
&#160; 
 Seleccionar 
label&#58; class=&quot; lbl_seleccionar &quot; 
 Checkbox que permite seleccionar el anuncio y a partir de dicha selección realizar las totalizaciones necesarias.&#160; Como es un informe de detalle, al seleccionar un registro, se deben seleccionar automáticamente todos los que tengan su mismo eatc_dona_headers .eatc-code 
 Al seleccionar un anuncio se lleva su eatc_dona_headers .eatc-code al &#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; , cuando se desmarca se quita el eatc_dona_headers .eatc-code de dicho array. 
&#160; 
 Código del anuncio 
label&#58; class=&quot; lbl_codigo_anuncio &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Fecha 
label&#58; class=&quot; lbl_fecha_publicacion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date 
&#160; 
 Fecha y hora 
label&#58; class=&quot; lbl_hora_publicacion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Mes 
label&#58; class=&quot; lbl_mes &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date (trayendo el mes) 
&#160; 
 Mes recepción (NO ESTABA EN EL INFORME QUE SIRVE COMO BASE) 
label&#58; class=&quot; lbl_mes_recepcion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime (trayendo el mes) 
&#160; 
 Estado 
label&#58; class=&quot; lbl_estado &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-state 
&#160; 
 Código Punto de donación 
label&#58; class=&quot; lbl_codigo_punto_donacion &quot; 
 La información se toma de&#58; eatc_dona .eatc-pod_id 
&#160; 
 Punto de donación 
label&#58; class=&quot; lbl_pod &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Dirección punto de donación (OJO ID) 
label&#58; id=&quot; lbl_direccion_punto_donacion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_address 
&#160; 
 Ciudad 
label&#58; class=&quot; lbl_ciudad &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-city 
&#160; 
 Código del producto 
label&#58; class=&quot; lbl_codigo_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_id 
&#160; 
 Nombre del producto 
label&#58; class=&quot; lbl_nombre_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_name 
&#160; 
 Clasificación del producto 
label&#58; class=&quot; lbl_tipologia_a_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_typology_a 
&#160; 
 KG Originales 
label&#58; class=&quot; kg_originales &quot; 
 La información se toma de&#58; la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) 
&#160; 
 KG aprovechados 
label&#58; class=&quot; lbl_kg_aprovechados &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_weight_kg 
&#160; 
 KG no aprovechados 
label&#58; class=&quot; lbl_kg_no_aprovechados &quot; 
 Tipo de dato&#58; float con dos posiciones decimales 
 La información se toma de&#58; ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg 
&#160; 
 Unidades aprovechadas 
label&#58; class=&quot; lbl_unidades_aprovechadas &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_quantity 
&#160; 
 Unidades no aprovechadas 
label&#58; class=&quot; lbl_unidades_no_aprovechadas &quot; 
 Tipo de dato&#58; float con dos posiciones decimales 
 La información se toma de&#58; eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity 
&#160; 
 Causal de Baja 
label&#58; class=&quot; lbl_causal_baja &quot; 
 La información se toma de&#58; eatc_dona .eatc-return_cause 
&#160; 
 Costo total definitivo 
label&#58; class=&quot; kg_costo_total_definitivo &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_cost 
&#160; 
 Costo no aprovechados 
label&#58; class=&quot; kg_costo_no_aprovechados &quot; (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las &quot; Unidades no aprovechadas &quot;&#160; por el costo unitario ( eatc_dona .eatc-unit_cost ) 
&#160; 
 Porcentaje IVA 
label&#58; class=&quot; lbl_porcentaje_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-VAT_percentage 
&#160; 
 Tarifa IVA 
label&#58; class=&quot; lbl_valor_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-total_VAT 
&#160; 
 Beneficiario 
label&#58; class=&quot; lbl_beneficiario &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Beneficiario dirección 
label&#58; class=&quot; lbl_direccion_beneficiario &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-donation_manager_adress 
&#160; 
 Beneficiario teléfono 
label&#58; class=&quot; lbl_telefono &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-donation_manager_phone 
&#160; 
 Hora de adjudicación 
label&#58; class=&quot; lbl_hora_adjudicacion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Hora de entrega programada 
label&#58; class=&quot; lbl_hora_entrega_programada &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Hora de entrega real&#58; llegada 
label&#58; class=&quot; lbl_hora_entrega_real_llegada &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Hora de entrega real&#58; salida 
label&#58; class=&quot; lbl_hora_entrega_real_salida &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Fecha recepción 
label&#58; class=&quot; lbl_hora_recepcion &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime 
&#160; 
 Documento soporte 
label&#58; class=&quot; lbl_documento_soporte &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-doc 
&#160; 
 Alerta 
label&#58; class=&quot; lbl_alerta &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-warning 

&#160; 
 Botón &quot;Confirmar anuncios a soportar&quot; 
 En una parte visible del listado, se debe colocar un botón con el label class=&quot; lbl_confirmar_donaciones_soportar &quot; . Al oprimir este botón el sistema realiza lo siguiente&#58; 
&#160; 
 Genera un array con los eatc_dona_headers. eatc-code de las donaciones seleccionadas ( &#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; ) el cual se utilizará para hacer el llamado al servicio que crea el soporte. 
 Genera un consolidado de productos donados a certificar y 
 Proporcionar un formulario para subir la factura electrónica correspondiente a dichos anuncios 

&#160; 
 Consolidación de productos donados a certificar 
 El sistema deberá generar un listado (que se debe guardar en una persistencia temporal) que consolide los artículos a ser certificados.&#160; 
&#160; 
 El sistema deberá proporcionar también botón con el siguiente label 
 label&#58; class=&quot; lbl_consulta_detalles_consolidados &quot;&#160; 
&#160; 
 Y que pueda mostrar la siguiente descripción (puede ser como un tooltip)&#58; 
 label&#58; class=&quot; lbl_consulta_detalles_consolidados_desc &quot;&#160; 
&#160; 
 Que debe permitir descargar el listado consolidado en formato .csv&#160; por código de producto, cantidades, kilogramos, y valores (en una tabla con los siguientes encabezados) y que corresponda en sus sumatorias de valores a las sumatorias del listado de anuncios soportados , dado que estos informes deben 100% consistentes) 
&#160; 
 Código del producto 
label&#58; class=&quot; lbl_codigo_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_id (no se podrán repetir códigos de producto dentro del informe ya que se consolidan por esta variable) 
&#160; 
 Nombre del producto 
label&#58; class=&quot; lbl_nombre_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_name (no se podrán repetir nombres de producto dentro del informe ya que al consolidarse por ID, a cada ID diferente le debe corresponder un nombre) 
&#160; 
 Clasificación del producto 
label&#58; class=&quot; lbl_tipologia_a_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_typology_a 
&#160; 
 KG Originales 
label&#58; class=&quot; kg_originales &quot; 
 La información se toma de&#58; la multiplicación de las unidades originales por el peso unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) consolidado por eatc_dona .eatc-odd_id 
&#160; 
 KG aprovechados 
label&#58; class=&quot; lbl_kg_aprovechados &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_weight_kg consolidado por eatc_dona .eatc-odd_id 
&#160; 
 KG no aprovechados 
label&#58; class=&quot; lbl_kg_no_aprovechados &quot; 
 Tipo de dato&#58; float con dos posiciones decimales 
 La información se toma de&#58; ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Unidades aprovechadas 
label&#58; class=&quot; lbl_unidades_aprovechadas &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Unidades no aprovechadas 
label&#58; class=&quot; lbl_unidades_no_aprovechadas &quot; 
 Tipo de dato&#58; float con dos posiciones decimales 
 La información se toma de&#58; eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Costo total definitivo 
label&#58; class=&quot; kg_costo_total_definitivo &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_cost consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Costo no aprovechados 
label&#58; class=&quot; kg_costo_no_aprovechados &quot; (ojo que la etiqueta tiene un error en su label por incorporar kg en vez de lbl, pero así quedó configurada) 
 La información se toma de multiplicar las &quot; Unidades no aprovechadas &quot;&#160; por el costo unitario ( eatc_dona .eatc-unit_cost ) consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Porcentaje IVA 
label&#58; class=&quot; lbl_porcentaje_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-VAT_percentage 
&#160; 
 Tarifa IVA 
label&#58; class=&quot; lbl_valor_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-total_VAT consolidado por eatc_dona .eatc-odd_id 
&#160; 
 Guardado de datos consolidados en una persistencia 
 El desarrollador puede evaluar la generación de una persistencia (si es una tabla, deberá albergarse en la cuenta maestra correspondiente) para almacenar esta consolidación, ya que posteriormente algunos de sus datos se utilizarán para los procesos de validación de la factura electrónica . 

&#160; 
 Despliegue de formulario para subida de factura electrónica 
 Se debe desplegar un formulario con el siguiente label introductorio class=&quot; lbl_subir_factura_desc &quot; y que debe tener un campo para seleccionar un archivo XML y subirlo a la plataforma (Hasta el día 6 del mes siguiente se podrán subir facturas del mes anterior ( eatc_dona_certification_supports . eatc_max_generation_day )) 
&#160; 
 Place hoder &#58; class=&quot; lbl_factura_electronica_colombia &quot; 
 Botón de subir&#58; class=&quot; lbl_subir_factura_electronica_colombia &quot; 
&#160; 
 Al subir la factura, se debe desplegar el proceso de validación de datos de la misma, que se detalla a continuación. 
&#160; 
 NOTA IMPORTANTE&#58; se debe evaluar si se permite subir el ZIP de la factura electrónica, que contiene el XML y también el PDF, este último importante para procesos de revisión humana de la información. Por lo tanto el localizador podría estar asociado a una carpeta que se cree en el servidor (idelamente con un hash o algo que dificulte su ubicación por quienes no tienen acceso a la plataforma) y que allí se contengan los recursos subidos&#58; XML y PDF. 

&#160; 
 V ALIDACIÓN DE DATOS DE LA FACTURA 
 Para la factura electrónica colombiana se efectuarán las siguiente validaciones&#58; 

&#160; 
 La fecha de la factura tiene que corresponder al mes en que se recibieron las donaciones 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt; cbc&#58;IssueDate &gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt; cbc&#58;IssueDate &gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; 
 El mes de la factura, debe corresponder al dato que se presenta en el parámetro del listado de anuncios&#58; Mes recepción (NO ESTABA EN EL INFORME QUE SIRVE COMO BASE) label&#58; class=&quot; lbl_mes_recepcion &quot; La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime (trayendo el mes) . 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_fecha_factura_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_fecha_factura_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro eatc_datetime &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_fecha_factura_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_fecha_factura_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

&#160; 
 La razón social de a quién se le expide la factura corresponde la razón social de Ábaco 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt; cac&#58;ReceiverParty &gt;&lt;cac&#58;PartyTaxScheme&gt;&lt; cbc&#58;RegistrationName &gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt; cac&#58;accountingcustomerparty &gt;&lt;cac&#58;party&gt;&lt;cac&#58;partylegalentity&gt;&lt; cbc&#58;registrationname &gt; 
&#160; 
 Comparación que debe hacerse con el dato extraído&#58; 
 Debe ser igual a &quot; ASOCIACIÓN DE BANCOS DE ALIMENTOS DE COLOMBIA &quot; (la validación debe ser case insensitive y sin validación de caracteres acentuados, es decir que si se presenta todo mayúsculas, todo minúsculas o tipo título y con o sin tildes la validación puede pasar) 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_nombre_destinatario_factura_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_destinatario_factura_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos. 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro eatc_donee_fiscal_name &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_nombre_destinatario_factura_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_destinatario_factura_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

&#160; 
 El NIT de a quién se le expide la factura corresponde la NIT de Ábaco 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt; cac&#58;ReceiverParty &gt;&lt;cac&#58;PartyTaxScheme&gt;&lt; cbc&#58;CompanyID &gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt; cac&#58;accountingcustomerparty &gt;&lt;cac&#58;party&gt;&lt;cac&#58;partylegalentity&gt;&lt; cbc&#58;companyid &gt; 
&#160; 
 Comparación que debe hacerse con el dato extraído&#58; 
 Debe ser igual a &quot; 900326456 &quot; 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_id_destinatario_factura_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_destinatario_factura_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro eatc_donee_code &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_id_destinatario_factura_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_destinatario_factura_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 

&#160; 
 La razón social de quien expide la factura corresponde al eatc_donor_fiscal_name registrado en las donaciones&#58; ***NUEVO&#58; escritura del nuevo nombre en la tabla eatc_multiple_donors_info *** 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt;cac&#58;SenderParty&gt;&lt;cac&#58;PartyTaxScheme&gt;&lt; cbc&#58;RegistrationName &gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;accountingsupplierparty&gt;&lt;cac&#58;party&gt;&lt;cac&#58;partylegalentity&gt;&lt; cbc&#58;registrationname &gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; ***NUEVO&#58; se guarda el valor actual de la razón social en una variable para posteriores acciones *** 
 De los anuncios seleccionados en el listado (que deben corresponder a un NIT en particular), el sistema debe comparar si el dato extraído del XML corresponde al dato contenido en eatc_dona_headers .eatc_donor_fiscal_name (que dado el selector de NIT debe ser igual para todos los anuncios seleccionados).&#160; NUEVO&#58;&#160; Se debe guardar el dato&#160; &#123;&#123;eatc_dona_headers .eatc_donor_fiscal_name &#125;&#125; en la variable &#123;&#123; actual_donor_fiscal_name &#125;&#125;&#160; 
&#160; 
 Label validación exitosa&#58; 
 class=&quot; lbl_nombre_emisor_factura_ok &quot;&#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_emisor_factura_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro eatc_donor_fiscal_name &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot; lbl_nombre_emisor_factura_no_ok &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_emisor_factura_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace ***NUEVO&#58; actualización datos en eatc_multiple_donors_info (Opción 2) *** &#58; 
&#160; 
 Debe salir un modal con&#58; 
&#160; 
 Título &#58; class=&quot; lbl_nombre_emisor_factura_no_ok &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_emisor_factura_no_ok 
 Descripción abajo del título class=&quot; lbl_nombre_emisor_factura_no_ok_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_emisor_factura_no_ok_desc &#160; (primera versión en español)&#58; Tendrás las siguientes opciones para corregirlo&#58; 
 Opción 1 (seleccionada por defecto)&#58; class=&quot; lbl_corregir_factura &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_factura &#58; si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario para subir una nueva factura se debe colocar el siguiente label&#58; lbl_corregir_nombre_donante ((primera versión en español)&#58; Recuerda que debes expedir una factura cuyo emisor tenga el siguiente nombre (RegistrationName)&#58; ) seguido del dato que se obtiene de eatc_dona_headers .eatc_donor_fiscal_name 
 Opción 2 &#58; class=&quot; lbl_corregir_datos_donaciones https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_datos_donaciones &#58;&#160; al seleccionar esta opción debe aparecer un modal con la siguiente información&#58; 
 Introducción &#58;&#160; class=&quot; lbl_corregir_datos_donaciones_intro &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_datos_donaciones_intro &#58; (primera versión en español)&#58; Al seleccionar esta opción el sistema tomará el dato contenido en la factura electrónica como el nombre del donante&#58; 
 Nombre del donante en la factura &#58; después del label anterior se debe mostrar de manera vistosa el dato contenido en el TAG XML correspondiente . 
 Conclusión &#58; class=&quot; lbl_corregir_datos_donaciones_conclu &quot;&#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_datos_donaciones_conclu &#58; (primera versión en español)&#58; y&#160; lo cambiará en los datos de donaciones e información maestra del donante en la plataforma, lo cual lo variará para las donaciones seleccionadas y para futuras donaciones.&#160; Por favor verifica muy bien la información de la factura antes de realizar este cambio.&#160; ¿Estás seguro de realizar esta actualización de datos? 
 Opción No (seleccionada por defecto)&#58; class=&quot; lbl_no &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_no &#58; si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario se debe colocar el siguiente label&#58; lbl_corregir_nombre_donante https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_nombre_donante &#160; seguido del dato que se obtiene de &#123;&#123;e atc_dona_headers .eatc_donor_fiscal_name &#125;&#125; 

 Opción Si &#58; class=&quot; lbl_si &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_si &#58; ( Se debe considerar la construcción de un servicio para las siguientes actualizaciones, que debe guardar un log de cuando se realice un cambio, con fecha y hora de realización, usuario de bo que lo realiza, datos originales (por si hay que reversar el cambio) y factura electrónica a partir de la cual se realizó el cambio) el sistema debe corregir los datos contenidos en &#123;&#123;eatc_dona_headers .eatc_donor_fiscal_name &#125;&#125; de las donaciones seleccionadas, incorporando en los mismos el dato que se saca del tag XML correspondiente ( &lt; cbc&#58;RegistrationName &gt; ). 
&#160; 
 El siguiente llamado es indicativo, dado que no se tiene claro si el CRD funciona con un array en el parámetro WHERE 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc_donor_fiscal_name=&#123;&#123;&lt; cbc&#58;RegistrationName &gt;&#125;&#125;&amp;WHERE_eatc-code=&#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; 
&#160; 
 Si la cuenta no tiene múltiples donors ( eatc_cua. multiple_donors = no ), se debe proceder a realizar el cambio del dato eatc_fiscal_name en la tabla de clientes. ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_customers?_id=_* ) previa consulta de la relación de la cuenta particular con el cliente ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_customers_cua?_id=_* ).&#160; Se debe tener en cuenta que esta información está encriptada y se debe volver a guardar encriptada. 

 Si la cuenta tiene múltiples donors ( eatc_cua. multiple_donors = si ), NUEVO&#58; el sistema deberá establecer el _id , del registro de la Razón Social actualmente registrada ( &#123;&#123; actual_donor_fiscal_name &#125;&#125; ) &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_multiple_donors_info?eatc_donor_fiscal_name=&#123;&#123; actual_donor_fiscal_name &#125;&#125;&amp;_cmp= _id 
&#160; 
 Para posteriormente, con el _id obtenido hacer el ajuste en el maestro de &quot; eatc_multiple_donors_info &quot; con la información del tag XML obtenido &#123;&#123;&lt; cbc&#58;RegistrationName &gt;&#125; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_user&#125;&#125;/?_tabla=eatc_multiple_donors_info&amp;_operacion=update&amp;eatc_donor_fiscal_name=&#123;&#123;&lt; cbc&#58;RegistrationName &gt;&#125;&#125;&amp;WHERE_id= _id 
&#160; 
 El NIT de quien emite la factura corresponde al eatc_donor_code registrado en las donaciones ***NUEVO&#58; se valida la parte numérica del NIT (sin el guión y el dígito de verificación) *** 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt; cac&#58;SenderParty &gt;&lt;cac&#58;PartyTaxScheme&gt;&lt; cbc&#58;CompanyID &gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt; cac&#58;accountingsupplierparty &gt;&lt;cac&#58;party&gt;&lt;cac&#58;partylegalentity&gt;&lt; cbc&#58;companyid &gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído ***NUEVO&#58; revisar validación sin sufijo (guión y dígito de verificación) y se guarda el valor actual de la razón social en una variable para posteriores acciones *** &#58; 
 De los anuncios seleccionados en el listado (que deben corresponder a un NIT en particular), el sistema debe comparar si el dato extraído del XML corresponde al dato contenido en eatc_dona_headers .eatc-donor_code NUEVO&#58; en su parte numérica, es decir, quitándole a ambos valores el guión y el dígito de verificación para realizar la comparación (que dado el selector de NIT debe ser igual para todos los anuncios seleccionados). Esta comparación no debe incorporar código de verificación, ni ningún sufijo (guion y dígito de verificación).&#160; Si un dato viene con un sufijo y otro no, pero el número previo es igual, la validación debe darse por exitosa. NUEVO&#58;&#160; Se debe guardar el dato&#160; &#123;&#123;eatc_dona_headers . eatc-donor_cod e &#125;&#125; en la variable &#123;&#123; actual_donor_fiscal_id &#125;&#125;&#160; 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_id_emisor_factura_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_emisor_factura_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro eatc_donor_code &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro del soporte ( eatc_certification_supports_headers ). 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_id_emisor_factura_no_ok&quot; 
&#160; 
 Cuando la validación no es exitosa se hace ***NUEVO&#58; actualización datos en eatc_multiple_donors_info (Opción 2) *** &#58; 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 
&#160; 
 Debe salir un modal con&#58; 
&#160; 
 Título &#58; class=&quot; lbl_id_emisor_factura_no_ok &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_emisor_factura_no_ok 
 Descripción abajo del título class=&quot; lbl_id_emisor_factura_no_ok_desc &quot;&#58; (primera versión en español)&#58; Tendrás las siguientes opciones para corregirla&#58; 
 Opción 1 (seleccionada por defecto)&#58; class=&quot; lbl_corregir_factura &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_emisor_factura_no_ok_desc &#58; si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura .&#160; Antes del formulario para la subida de una nueva factura se debe colocar el siguiente label&#58; lbl_corregir_id_donante https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_id_donante ((primera versión en español)&#58; Recuerda que debes expedir una factura cuyo emisor tenga el siguiente NIT (CompanyID)&#58; ) seguido del dato que se obtiene de eatc_dona_headers .eatc-donor_code 

 Opción 2 &#58; class=&quot; lbl_corregir_datos_donaciones https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_datos_donaciones &#58;&#160; al seleccionar esta opción debe aparecer un modal con la siguiente información&#58; 
&#160; 
 Introducción &#58;&#160; class=&quot; lbl_corregir_id_datos_donaciones_intro &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_id_datos_donaciones_intro &#58; (primera versión en español)&#58; Al seleccionar esta opción el sistema tomará el dato contenido en la factura electrónica como el NIT del donante&#58; 
 NIT del donante en la factura &#58; después del label anterior se debe mostrar de manera vistosa el dato contenido en el TAG XML correspondiente . 
 Conclusión &#58; class=&quot; lbl_corregir_datos_donaciones_conclu &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_datos_donaciones_conclu &#58; (primera versión en español)&#58; y&#160; lo cambiará en los datos de donaciones e información maestra del donante en la plataforma, lo cual lo variará para las donaciones seleccionadas y para futuras donaciones.&#160; Por favor verifica muy bien la información de la factura antes de realizar este cambio.&#160; ¿Estás seguro de realizar esta actualización de datos? 
 Opción No (seleccionada por defecto)&#58; class=&quot; lbl_no &quot; &#58; si el usuario selecciona esta opción, se para la validación y se vuelve a mostrar el formulario de subida de factura . Antes del formulario se debe colocar el siguiente label&#58; lbl_corregir_id_donante https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_id_donante &#160; ((primera versión en español)&#58; Recuerda que debes expedir una factura cuyo emisor tenga el siguiente NIT (CompanyID)&#58; )&#160; seguido del dato que se obtiene de &#123;&#123;eatc_dona_headers .eatc-donor_code &#125;&#125; 

 Opción Si &#58; class=&quot; lbl_si &quot; &#58; ( Se debe considerar la construcción de un servicio para las siguientes actualizaciones, que debe guardar un log de cuando se realice un cambio, con fecha y hora de realización, usuario de bo que lo realiza, datos originales (por si hay que reversar el cambio) y factura electrónica a partir de la cual se realizó el cambio) el sistema debe corregir los datos contenidos en eatc_dona_headers .eatc-donor_code de las donaciones seleccionadas.&#160; 
&#160; 
 El siguiente llamado es indicativo, dado que no se tiene claro si el CRD funciona con un array en el parámetro WHERE&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/ &#123;&#123;_DOM.cua_master&#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-donor_code=&#123;&#123;&lt; cbc&#58;CompanyID &gt;&#125;&#125;&amp;WHERE_eatc-code=&#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; 
&#160; 
 Si la cuenta no tiene múltiples donors ( eatc_cua. multiple_donors = no ), se debe proceder a realizar el cambio del dato eatc_fiscal_id en la tabla de clientes. ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_customers?_id=_* ) previa consulta de la relación de la cuenta particular con el cliente ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_customers_cua?_id=_* ).&#160; Se debe tener en cuenta que esta información está encriptada y se debe volver a guardar encriptada. 

 Si la cuenta tiene múltiples donors ( eatc_cua. multiple_donors = si ), no se actualiza ningún dato adicional. NUEVO&#58; el sistema deberá establecer el _id , del registro de la Razón Social actualmente registrada ( &#123;&#123; actual_donor_fiscal_id &#125;&#125; )&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_multiple_donors_info?eatc_donor_code=&#123;&#123; actual_donor_fiscal_id &#125;&#125;&amp;_cmp= _id 
&#160; 
 Para posteriormente, con el _id obtenido hacer el ajuste en el maestro de &quot; eatc_multiple_donors_info &quot; con la información del tag XML obtenido &#123;&#123;&lt; cbc&#58;CompanyID &gt;&#125;&#125; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM.cua_user&#125;&#125;/?_tabla=eatc_multiple_donors_info&amp;_operacion=update&amp;eatc_donor_code=&#123;&#123;&lt; cbc&#58;CompanyID &gt;&#125;&#125;&amp;WHERE_id= _id 
&#160; 
 Número de la factura no puede estar repetido 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt; cbc&#58;id&gt; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt; cbc&#58;id&gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; 
 Se debe realizar la siguiente búsqueda (con los datos, de la validación de NIT anterior)&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_certification_supports_headers? eatc_donor_code=&#123;&#123; eatc_donor_code_extraido_de_la_factura &#125;&#125;&amp;eatc_certification_support_code=&#123;&#123; numero_de_factura_extraido_de_la_factura &#125;&#125; 
 Si la anterior consulta NO trae un resultado válido, entonces la validación se da como exitosa. 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_id_factura_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_factura_ok &#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato obtenido del XML en el parámetro eatc_certification_support_code &#160; para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte. 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_id_factura_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_factura_no_ok 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Se para la validación y se vuelve a mostrar el formulario de subida de factura . 
&#160; 
 ***NUEVO&#58; información de la factura electrónica que se guarda para el registro&#58; URL de descarga&#58; url_descarga_fe *** 
 El sistema debe tomar la información de la URL que comienza por &quot; https&#58;//catalogo-vpfe.dian.gov.co/document/ShowDocumentToPublic/ &quot; y que se encuentra en el tag&#58; &quot;stamp&quot;&#58; &#123;&quot;barCodeContent&quot;&#58;&#125; y guardarlo en la variable url_descarga_fe 
&#160; 
 Registro de datos de cabecera de soporte (una vez se han validado los datos del encabezado de la factura) 
 Con los siguientes parámetros, que se obtienen la factura electrónica validada exitosamente&#58; 
&#160; 
 parametros_creacion_eatc_certification_supports_headers 
 eatc_certification_support_code=&#123;&#123;&lt;cbc&#58;id&gt;&#125;&#125; 
 eatc_suppport_datetime=&#123;&#123;&lt;cbc&#58;IssueDate&gt;&#125;&#125; =&gt; falta por crear el campo 
 eatc_datetime=&#123;&#123;Fecha y hora de generación del soporte (datetimestamp) en formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date=&#123;&#123;Fecha de generación del soporte (datestamp) en formato AAAA-MM-DD &#125;&#125; 
 eatc_month=&#123;&#123;Mes del soporte (enero,febrero,…,diciembre)&#125;&#125; 
 eatc_year=&#123;&#123;Año del soporte (en formato AAAA )&#125;&#125; 
 eatc_dona_certification_support= factura_electronica_colombia (constante) 
 eatc_donor_code=&#123;&#123;&lt;cbc&#58;CompanyID&gt;&#125;&#125; 
 eatc_donor_fiscal_name=&#123;&#123;&lt;cbc&#58;RegistrationName&gt;&#125;&#125; 
 eatc_value=&#123;&#123;&lt;cbc&#58;taxableamount&gt;&#125;&#125; 
 eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; 
 **NUEVO &#58; eatc_support_file= url_descarga_fe (según lo estipulado en la documentación respectiva ) ** 
 eatc_donee_fiscal_name= eatc_donee_fiscal_name (Debe ser igual a &quot; ASOCIACIÓN DE BANCOS DE ALIMENTOS DE COLOMBIA &quot;) 
 eatc_donee_code= eatc_donee_code (Debe ser igual a &quot; 900326456 &quot;) 
 eatc_suppport_w_complete_validation= n (constante, dado que hasta este punto se ha validado el encabezado, pero no los detalles de la factura) =&gt; falta por crear el campo 
&#160; 
 El sistema hace el llamado al respectivo crd&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_certification_supports_headers &amp;_operacion=insert&amp;&#123;&#123; parametros_creacion_eatc_certification_supports_headers &#125;&#125; =&gt; Tener en cuenta en creación de cuentas maestras 
&#160; 
 ***NUEVO&#58; Registro de relación entre los encabezados de donación y el respectivo soporte eatc_dona_headers_support ( Tabla pendiente por crear&#58; una vez se han validado los datos del encabezado de la factura) *** 
 El sistema deberá hacer el siguiente registro, para definir que donaciones no poseen soporte registrado y cuales si&#58; 
&#160; 
 eatc_dona_header_code&#58; &#123;&#123;eatc_dona_headers.eatc-code&#125;&#125; 
 eatc_dona_publication_date&#58; &#123;&#123;eatc_dona_headers.eatc-publication_date&#125;&#125; 
 eatc_certification_support_code=&#123;&#123;&lt;cbc&#58;id&gt;&#125;&#125; 
 eatc_suppport_datetime=&#123;&#123;&lt;cbc&#58;IssueDate&gt;&#125;&#125; 
 eatc_date=&#123;&#123;Fecha de generación del soporte (datestamp) en formato AAAA-MM-DD &#125;&#125; 
&#160; 
 El sistema hace el llamado al respectivo crd&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_dona_headers_support &amp;_operacion=insert&amp;&#123;&#123; parametros_creacion_eatc_dona_headers_supports &#125;&#125; =&gt; Tener en cuenta en creación de cuentas maestras 
&#160; 
 VALIDACIONES PARA LAS LÍNEAS DE LA FACTURA (&lt;cac&#58;invoiceline&gt;) 
 En términos generales se debe realizar por cada línea un validación de su código y del nombre del producto en primera instancia. Si alguno de estos datos es incorrecto (y otro está correcto) debe dársele al usuario la oportunidad de actualizar el dato incorrecto en los registros de EatCloud para hacerlo compatible a la factura. Si ambos datos son incorrectos se debe parar la validación (con un mensaje), y volver al&#160; formulario para subida de factura. Si uno de los dos datos&#160; (código o descripción) es correcto (y se procede con la corrección del dato en los Registros de EatCloud, se debe proceder a validar la cantidad de producto en cada línea.&#160; Si la cantidad de producto en el XML es inferior a la cantidad de producto consolidado ( unidades aprovechadas ) de los anuncios seleccionados, entonces la validación pasará (será exitosa) y se llevará la cantidad informada en la factura al registro de unidades de producto a certificar ( eatc_certification_products_details ). Si la cantidad en la factura es superior, a la cantidad consolidada para el ITEM, se debe solicitar la corrección de la factura con la cantidad que se tiene registrada en EatCloud. Si una línea de la factura no cumple con las validaciones, entonces la factura debe ser rechazada y se solicitará la subida de una nueva factura con los datos corregidos, o que el usuario realice una nueva selección de donaciones que estén acorde con la factura. 
&#160; 
 El código de los ítems de la factura debe corresponder al código de los items consolidados ***NUEVO&#58; diferentes tipos de validación a partir de lectura de un parámetro de configuración *** 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;item&gt; &lt;cac&#58;sellersitemidentification&gt; 
&#160; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;item&gt; &lt;cac&#58;standarditemidentification&gt; 
&#160; 
 NOTA &#58; en los ejemplos de facturas consultados, estos datos son iguales.&#160; En caso que en una factura en particular sean diferentes, se deberá realizar la consulta con ambos y si uno de los dos pasa la verificación se entiende que la verificación es exitosa. 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML ( &lt;cac&#58;standarditemidentification&gt; ) corresponde a un Código de producto ( eatc_dona .eatc-odd_id) que esté contenido en los anuncios seleccionados . 
&#160; 
 NUEVO&#58; tipos de validaciones diferentes a partir de lectura de parámetro de configuración 
 El sistema debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_validation ? eatc_cua_master =abaco&amp; eatc_process =factura_electronica_colombia&amp; eatc_object_store =eatc_dona&amp; eatc_parameter =eatc-odd_id&amp; eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cmp= eatc_validation_type 
&#160; 
 Si la respuesta es &quot;integer&quot; 
&#160; 
 Quiere decir que el sistema solamente debe validar la parte &quot;entera&quot; de los respectivos códigos, comparando solamente el número al interior de los mismos (sacando de la comparación las letras y los símbolos presentes 
&#160; 
 Ejemplo &#58; entorno de pruebas,&#160; _DOM. cua_user= alquería&#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_validation ? eatc_cua_master =abaco&amp; eatc_process =factura_electronica_colombia&amp; eatc_object_store =eatc_dona&amp; eatc_parameter =eatc-odd_id&amp; eatc_cua =alqueria&amp;_cmp= eatc_validation_type &#160; 
&#160; 
 Dado que la respuesta es &quot;integer&quot;, el sistema solo comparará la parte entera de ambos códigos (no tomando en cuenta en la comparación las letras, símbolos y caracteres especiales) 

&#160; 
 Si la respuesta es &quot;string&quot; o vacía 
&#160; 
 El sistema debe comparar ambos códigos como string, es decir incluyendo en la comparación todos las letras y los números presentes en ambos (comparación exacta). NOTA&#58; Es así como se implementó en principio la validación y debe ser su funcionamiento por defecto. 

&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_id_items_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_items_ok &#160; 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa se hace&#58; 
 Se guarda el dato en el parámetro &quot; eatc_product_code &quot; para posteriormente, cuando las demás validaciones se completen, se lleve al registro de productos en el soporte ( eatc_certification_products_details ). 

&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_id_item_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_item_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Se debe pasar a validar el nombre del item de la factura (validación siguiente).&#160; Si dicha validación es exitosa (en conjunto con la validación de cantidad), se le debe preguntar al usuario ( class=&quot; lbl_cambiar_codigo_item &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cambiar_codigo_item )&#58; ¿Deseas reemplazar el código registrado en las donaciones por el código que trae la factura que acabas de subir? y si el usuario define que si ( class=&quot; lbl_si &quot; ), entonces el sistema debe proceder a actualizar el eatc_dona .eatc-odd_id en las donaciones seleccionadas .&#160; Si el usuario define que no ( class=&quot; lbl_no &quot; ) el sistema debe desplegar el siguiente mensaje&#58; ( class=&quot; lbl_id_item_no_ok_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_id_item_no_ok_desc )&#58; Los códigos de los productos registrados en la factura deben corresponder con los códigos de los productos reportados en el anuncio, por favor corrige la factura y procede a subirla de nuevo ,&#160; y se vuelve a mostrar el formulario de subida de factura . 
&#160; 
 La descripción de los ítems de la factura debe corresponder a la descripción de los ítems consolidados 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;item&gt;&lt; cbc&#58;description &gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML corresponde al nombre del producto ( eatc_dona .eatc-odd_name) que está contenido en los anuncios seleccionados . 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_nombre_item_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_item_ok 
&#160; 
 Puede aparecer en un toast, mientras se hace el proceso, con un delay de unos tres segundos 
&#160; 
 Cuando la validación es exitosa (junto con la validación anterior) se hace&#58; 
 Se guarda el dato en el parámetro &quot; eatc_product_name &quot; para posteriormente, cuando la tercera validación del ítem se complete ( validación de cantidades ), se lleve al registro de productos en el soporte ( eatc_certification_products_details ) 
&#160; 
 Cuando la validación es exitosa (y la anterior no lo fue) se hace&#58; 
 Se procede como se indicó anteriormente . 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_nombre_item_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_item_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa (y la anterior si lo fue y la validación de cantidades también ) se hace&#58; 
 Se le debe preguntar al usuario ( class=&quot; lbl_cambiar_nombre_item &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cambiar_nombre_item )&#58; ¿Deseas reemplazar el nombre registrado en las donaciones por el nombre del producto que trae la factura que acabas de subir? y si el usuario define que si ( class=&quot; lbl_si &quot; ), entonces el sistema debe proceder a actualizar el eatc_dona .eatc-odd_name en las donaciones seleccionadas .&#160; Si el usuario define que no ( class=&quot; lbl_no &quot; ) el sistema debe desplegar el siguiente mensaje&#58; ( class=&quot; lbl_nombre_item_no_ok_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_item_no_ok_desc )&#58; El nombre del ítem en la factura debe corresponder al nombre del ítem registrado en las donaciones. Por favor corrige la factura y súbela de nuevo ,&#160; y se vuelve a mostrar el formulario de subida de factura . 
&#160; 
 Cuando la validación no es exitosa (y la anterior tampoco lo fue) se hace&#58; 
 Si la validación de código no es exitosa tampoco, entonces se para la validación, se muestra el label &quot; lbl_nombre_item_no_ok_desc https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_nombre_item_no_ok_desc &quot; y se vuelve a mostrar el formulario de subida de factura . 

&#160; 
 Las cantidades de los ítems de la factura deben ser menores o iguales a las cantidades de los ítems consolidados 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;&lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;price&gt; &lt;cbc&#58;basequantity&gt; 
&#160; 
 Búsqueda que debe hacerse con el dato extraído&#58; 
 De la consolidación por producto obtenida en el proceso correspondiente , se debe proceder a buscar si la información extraída del XML corresponde a una cantidad igual o menor a la cantidad de Unidades aprovechadas ( eatc_dona .eatc-odd_quantity) de los anuncios seleccionados . 
&#160; 
 Label validación exitosa&#58; 
 class=&quot;lbl_cantidad_item_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cantidad_item_ok &#160; 
&#160; 
 Cuando la validación es exitosa se hace (junto con las dos anteriores o al menos una de las dos anteriores)&#58; 
 Se guarda el dato en el parámetro &quot; eatc_product_quantity &quot; para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ) 
&#160; 
 Label validación no exitosa&#58; 
 class=&quot;lbl_cantidad_item_no_ok&quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cantidad_item_no_ok &#160; 
&#160; 
 Cuando la validación no es exitosa se hace&#58; 
 Cuando la cantidad de la factura es superior a la informada en los anuncios seleccionados, se para la validación, y se muestra el label &quot; lbl_cantidad_item_no_ok_desc &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cantidad_item_no_ok_desc &#58; La cantidad del ítem informada en la factura no corresponde a la cantidad efectivamente verificada por el beneficiario, informada en las donaciones recibidas. Por favor cambie la selección de donaciones o corrija el dato en la factura y vuelva a subirla &#160; y debajo debe mostrar dos opciones (botones)&#58; class=&quot; lbl_cambiar_seleccion_donaciones &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_cambiar_seleccion_donaciones &#160; (que devuelve a la lista de anuncios para seleccionar ) y class=&quot; lbl_corregir_factura &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_corregir_factura &#160; (que vuelve a mostrar el formulario de subida de factura ) 

&#160; 
 OTROS DATOS DE LAS LÍNEAS DE LA FACTURA (&lt;cac&#58;invoiceline&gt;) que se llevan al registro si las anteriores validaciones son exitosas&#58; 
 Lo siguientes datos deben obtenerse de la información de la factura para guardarse posteriormente en los registros correspondientes 
&#160; 
 Valor unitario del ítem antes de IVA 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;price&gt; &lt;cbc&#58;priceamount&gt; 
&#160; 
 Se guarda en&#58; 
 Se guarda el dato en el parámetro &quot; eatc_unt_value &quot; para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ) 
&#160; 
 Valor total del ítem antes de IVA 
&#160; 
 TAG XML en donde se encuentra el dato&#58;&#160; 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt; cbc&#58;lineextensionamount &gt; 
&#160; 
 ó 
 &lt;AttachedDocument&gt;&lt;cac&#58;Attachment&gt;&lt;cac&#58;ExternalReference&gt;&lt;cbc&#58;Description&gt;&lt;![CDATA[&lt;invoice&gt;&lt;cac&#58;invoiceline&gt;&lt;cac&#58;taxtotal&gt;&lt;cac&#58;taxsubtotal&gt;&lt; cbc&#58;taxableamount &gt; 
&#160; 
 NOTA &#58; Este segundo tag no está presente en algunas facturas electrónicas 
&#160; 
 Se guarda en&#58; 
 Se guarda el dato en el parámetro &quot; eatc_total_value &quot; para posteriormente, cuando las demás validaciones se completen, se lleve al registro de soporte ( eatc_certification_products_details ). 

&#160; 
 Registro de datos de detalle de productos (una vez se tiene la validación de los detalles de manera exitosa) 
 Tan pronto el sistema determina que los detalles de la factura han sido correctamente validados, con los datos obtenidos de dichos detalles de la factura se obtiene la siguiente información para el registro del cada producto incorporado en la factura&#58; 
&#160; 
 parametros_creacion_eatc_certification_products_details 
 eatc_certification_support_code=&#123;&#123;&lt;cbc&#58;id&gt;&#125;&#125;= &#123;&#123; eatc_certification_supports_headers. eatc_certification_support_code &#125;&#125; 
 eatc_product_code=&#123;&#123;&lt;cac&#58;sellersitemidentification&gt; ó &lt;cac&#58;standarditemidentification&gt;&#125;&#125; 
 eatc_product_name=&#123;&#123; eatc_product_name &#125;&#125;=&#123;&#123;&lt;cbc&#58;description&gt;&#125;&#125; 
 eatc_product_quantity=&#123;&#123;&lt;cbc&#58;basequantity&gt;&#125;&#125; 
 eatc_unt_value=&#123;&#123; eatc_unt_value &#125;&#125;=&#123;&#123;&lt;cbc&#58;lineextensionamount&gt;&#125;&#125; 
 eatc_total_value=&#123;&#123; eatc_total_value &#125;&#125;=&#123;&#123;&lt;cbc&#58;taxableamount&gt;&#125;&#125; 
&#160; 
 Los anteriores datos se extraen tantas veces como líneas de factura ( &lt;cac&#58;invoiceline&gt; ) existan. 
&#160; 
 El sistema realiza el siguiente llamado para registrar los datos de los productos de la factura&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_certification_products_details &amp;_operacion= insert &amp;&#123;&#123; parametros_creacion_eatc_certification_products_details &#125;&#125; 
&#160; 
 ***NUEVO&#58; Actualización de datos de detalle de productos en anuncios soportados a partir de los costos contenidos en la factura *** 
 A partir de los datos contenidos en la factura, con los cuales se registraron los detalles de los productos, el sistema deberá consultar los detalles de los anuncios seleccionados a soportar ( &#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; ) y sus respectivos detalles, para actualizarlos de acuerdo a los detalles e las facturas validadas 
&#160; 
 eatc_dona _operacion=upgrade 
 eatc_dona. eatc-odd_name = eatc_product_name=&#123;&#123; eatc_product_name &#125;&#125;=&#123;&#123;&lt;cbc&#58;description&gt;&#125;&#125; 
 eatc_dona. eatc-unit_cost = eatc_unt_value=&#123;&#123; eatc_unt_value &#125;&#125;=&#123;&#123;&lt;cbc&#58;lineextensionamount&gt;&#125;&#125; 
&#160; 
 Para cada línea o detalle de donación en donde hubo una variación del costo unitario, el sistema deberá calcular el costo total 
 eatc_dona. eatc-odd_total_cost = eatc_dona. eatc-odd_quantity * eatc_dona. eatc-unit_cost 
&#160; 
 ***NUEVO&#58; Actualización de datos de encabezado de donación en anuncios soportados a partir de los costos contenidos en la factura *** 
 Una vez actualizada la información, se deberá correr el proceso para actualizar los respectivos encabezados de donación ( &#123;&#123; array_codigos_eatc_dona_headers &#125;&#125; ) a partir de los detalles actualizados (con nuevos costos). 
&#160; 
 ***NUEVO&#58; Recálculo de KPIs *** 
 Una vez actualizada la información, se deberá llamar a la función Recalkpi , para recalcular los KPIs de las donaciones cuyos costos variaron a partir de costos subidos en las respectivas facturas electrónicas 

&#160; 
 Actualización de dato de encabezado de soporte (una vez se tiene la validación de los detalles de manera exitosa) 
 Tan pronto el sistema determina que los detalles de la factura han sido correctamente validados, el sistema deberá realizar la siguiente actualización para informar que la validación del soporte está completa, realizando el llamado al respectivo al crd&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_certification_supports_headers &amp;_operacion= update &amp;eatc_suppport_w_complete_validation= y &amp;WHEREeatc_certification_support_code=&#123;&#123; eatc_certification_supports_headers. eatc_certification_support_code &#125;&#125; 
 &#160; =&gt; Tener en cuenta en creación de cuentas maestras / falta por crear el campo 

&#160; 
 Registro de datos de detalle de soporte (listado de anuncios de donación soportados&#58; una vez se tiene la validación de los detalles de manera exitosa) 
 T an pronto el sistema determina que los detalles de la factura han sido correctamente validados, con los datos de cada anuncio que fuere previamente seleccionado &#160; para ser soportado por la factura_electronica_colombia y a partir de ello, para realizar validar los datos de factura electrónica, se realiza el siguiente registro de datos&#58; 
&#160; 
 parametros_creación_detalle_soportes 
&#160; 
 eatc_dona_header_code&#58; 
 Código del anuncio de donación soportado ( eatc_dona_headers. eatc-code ). 
&#160; 
 eatc_publication_datetime&#58; 
 Fecha y hora de publicación del anuncio ( eatc_dona_headers. eatc-publication_datetime )&quot;, 
&#160; 
 eatc_value&#58; 
 Valor del anuncio certificable antes de IVA (se toma de&#58; eatc_dona_headers. eatc-total_cost ). 
&#160; 
 eatc_receipt_datetime&#58; 
 Fecha de recepción del anuncio ( eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM-DD HH&#58;MM&#58;SS 
&#160; 
 eatc_receipt_year_month&#58; 
 Año y mes de recepción del anuncio (tomado de eatc_dona_headers. eatc-receipt_datetime ), en formato AAAA-MM 
&#160; 
 eatc_doc&#58; 
 Documento soporte de la donación ( eatc_dona_headers. eatc-doc ). 
&#160; 
 eatc_donation_manager&#58; 
 Gestor de donaciones al que se le entregó la donación ( eatc_dona_headers .eatc-donation_manager_code ). 
&#160; 
 eatc_doma_affiliated_organization&#58; 
&#160; 
 ***NUEVO&#58; se deja vacío *** 
 Dado que en un proceso de servidor que se generará al crear el certificado, se incorporará esta información. 

&#160; 
 DEPRECADO&#58; 
 Nombre de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta&#58;&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_dona_headers .eatc-donation_manager_code &#125;&#125;Se toma el dato &quot; organizacion_vinculada &quot;.&#160; Si en dicho dato viene el &quot; abaco &quot;, se coloca ese dato en el registro.&#160; Si viene un NIT, se repite la consulta anteriormente realizada&#58;&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123; organizacion_vinculada &#125;&#125;Y se lleva al registro el dato consignado en &quot; organizacin &quot; (NOTA IMPORTANTE&#58; si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.&#160; Si después de esta segunda consulta no se traen datos, se debe llevar al registro &quot; abaco &quot;) 
&#160; 
 eatc_doma_affiliated_organization_id&#58; 
&#160; 
 ***NUEVO&#58; se deja vacío *** 
&#160; 
 Dado que en un proceso de servidor que se generará al crear el certificado, se incorporará esta información. 

&#160; 
 DEPRECADO&#58; 
 Identificador único de la organización a la que se adscribe el gestor de donaciones (Banco de Alimentos). Con el código del gestor de donaciones ( eatc_dona_headers .eatc-donation_manager_code ) se realiza la siguiente consulta&#58;&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_dona_headers .eatc-donation_manager_code &#125;&#125;Se toma el dato &quot; organizacion_vinculada &quot;.&#160; Si en dicho dato viene el &quot; abaco &quot;, se coloca el dato que llega en el campo identificador_unico_registro de la siguiente consulta&#58;&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?identificador= abaco Y se lleva al registro el dato consignado en &quot; organizacin &quot; (NOTA IMPORTANTE&#58; si con el dato consignado en organizacion_vinculada no se obtiene una respuesta, la consulta se debe volver a realizar, quitando el Dígito de Verificación.&#160; Si después de esta segunda consulta no se traen datos, se debe llevar al registro &quot; abaco &quot;) 
&#160; 
 eatc_certification_support_code&#58; 
 Código del soporte para la certificación que se toma del código respectivo que se genera con el llamado al servicio&#58; 
 eatc_certification_support_code=&#123;&#123; eatc_certification_support_code &#125;&#125; 
&#160; 
 Que también corresponde al dato guardado en el proceso anterior en&#58; 
 &#160;&#123;&#123; eatc_certification_supports_headers. eatc_certification_support_code &#125;&#125; 
&#160; 
 eatc_dona_certification_support&#58; 
 Tipo de soporte de certificación expedido (en este caso siempre será factura_electronica_colombia ). 
&#160; 
 eatc_donor_code&#58; 
 Documento de identidad del donante ( eatc_certification_supports_headers . eatc_donor_code ). 
&#160; 
 eatc_donor_fiscal_name&#58; 
 Razón social del donante ( eatc_certification_supports_headers . eatc_donor_fiscal_name ). 

&#160; 
 Creación registro de detalle del soporte 
 El sistema debe generar el registro utilizando el CRD correspondiente 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_certification_supports_details &amp;_operacion= insert &amp; &#123;&#123;parametros_creación_detalle_soporte&#125;&#125; 

&#160; 
 DEPRECADO ( dado que inicialmente los registros se realizarán directamente en el proceso de validación de factura electrónica y no mediante un servicio ) 
&#160; 
 Parámetros que se obtienen de la factura electrónica y que se deben enviar para su creacion en el sistema 
&#160; 
 Este es el resumen de los parámetros que se envían (con indicación del último tag XML en donde se encuentra la información para efectos indicativos), a partir de los datos que se obtienen del XML de la factura Electrónica 
&#160; 
 parametros_creacion_eatc_certification_supports_headers 
 eatc_cua=&#123;&#123;_DOM.cua_user&#125;&#125; 
 eatc_datetime=&#123;&#123;&lt;cbc&#58;IssueDate&gt;&#125;&#125; 
 eatc_donee_fiscal_name=&#123;&#123;&lt;cbc&#58;RegistrationName&gt;&#125;&#125; 
 eatc_donee_code=&#123;&#123;&lt;cbc&#58;CompanyID&gt;&#125;&#125; 
 eatc_donor_fiscal_name=&#123;&#123;&lt;cbc&#58;RegistrationName&gt;&#125;&#125; 
 eatc_donor_code=&#123;&#123;&lt;cbc&#58;CompanyID&gt;&#125;&#125; 
 eatc_certification_support_code=&#123;&#123;&lt;cbc&#58;id&gt;&#125;&#125; 
 **NUEVO&#58; eatc_support_file= url_descarga_fe (según lo estipulado en la documentación respectiva ) ** 
&#160; 
 Los anteriores datos se extraen una vez por factura electrónica 
&#160; 
 parametros_creacion_eatc_certification_products_details 
 eatc_certification_support_code=&#123;&#123;&lt;cbc&#58;id&gt;&#125;&#125; 
 eatc_product_code=&#123;&#123;&lt;cac&#58;sellersitemidentification&gt; ó &#125;&#125; 
 eatc_product_name=&#123;&#123;&lt;cbc&#58;description&gt;&#125;&#125; 
 eatc_product_quantity=&#123;&#123;&lt;cbc&#58;basequantity&gt;&#125;&#125; 
 eatc_unt_value=&#123;&#123;&lt;cbc&#58;lineextensionamount&gt;&#125;&#125; 
 eatc_total_value=&#123;&#123;&lt;cbc&#58;taxableamount&gt;&#125;&#125; 
&#160; 
 Los anteriores datos se extraen tantas veces como líneas de factura ( &lt;cac&#58;invoiceline&gt; ) existan. 
&#160; 
 NOTA IMPORTANTE&#58; El desarrollador debe definir si envía los anteriores parámetros en el llamado al servicio que crea la factura (comprimiéndolos de algún modo) o si procede a implementar en el servidor la obtención de estos parámetros a partir del XML (lo cual sería algo redundante con la implementación anterior) o si genera persistencias provisionales para guardarlos ( eatc_provisional_certification_supports_headers , eatc_provisional_certification_products_details ) que podrán ser consultada con el dato eatc_certification_support_code (que se manda en el llamado al servicio que crea la factura ) para realizar las escrituras en las tablas definitivas eatc_certification_supports_headers y&#160; eatc_certification_products_details 

 &#160; 
 Método de soporte&#58; factura_electronica_colombia&#58; llamado a servicio ante una validación totalmente exitosa 
&#160; 
 Si todas las validaciones practicadas a la factura fueron exitosas (o las correcciones de datos sugeridas fueron implementadas) entonces se pasa a realizar el siguiente llamado al servicio, con el ánimo de crear los registros de rigor a partir del documento soporte aportado 
&#160; 
 &#123;&#123; URL_entorno_donante &#125;&#125;/ crea_sprt /&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_certification_support= factura_electronica_colombia&amp; eatc_certification_support_code= &#123;&#123;eatc_certification_support_code&#125;&#125;&amp; eatc_support_file =&#123;&#123;localizador_recurso / url_descarga_fe &#125;&#125;&amp; eatc_dona_headers =&#123;&#123;array_codigos_eatc_dona_headers&#125;&#125;&amp; ... 
&#160; 
 ... Si el desarrollador decide mandar los parámetros ( parametros_creacion_eatc_certification_supports_headers / parametros_creacion_eatc_certification_products_details)&#160; para la creación de los registros definitivos eatc_certification_supports_headers y eatc_certification_products_details se deberá documentar su inclusión en el llamado al servicio respectivo 
&#160; 
 El servicio deberá llamarse tantas veces sea necesario, hasta obtener una respuesta exitosa del mismo . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Datagov_Cuentas 

 MÉTODO DE SOPORTE FACTURA ELECTRÓNICA COLOMBIA