# nueva-creación-de-auncios-de-donación-eatc_dona_upl.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La presente implementación es totalmente basada en la implementación actual de creación de anuncio de donación .&#160; Absolutamente todo el funcionamiento de debe corresponder a lo ya implementado (incluyendo por ejemplo, el despliegue de la funcionalidad, la validación de horarios, la selección de punto de donación para cuentas con edit_coordinates = si , temas que en el diseño mejorado no están presentes).&#160; Por lo tanto esta mejora se debe entender como simplemente un cambio en la visualización del proceso de agregar productos a la donación, y generarla. 

 Diseño 
 http&#58;//repograf.eatcloud.info/crt_dona.html 

 CREAR ANUNCIO DE DONACIÓN 
 Label 
 class=&quot;lbl_crear_anuncios&quot; 

 ***NUEVO&#58; VALIDACIÓN DE ESTADO DEL POD EN ALLPOD PARA EL DESPLIEGUE DE LA FUNCIONALIDAD*** 
 El sistema deberá realizar la siguiente validación del punto de donación, antes de desplegarle la funcionalidad de captura de anuncios de donación&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125; 
&#160; 
 Si el servicio responde con una respuesta no válida o no responde entonces el sistema deberá mostrar el siguiente pop-up y no permitir la toma de anuncios. 
&#160; 
 &quot;x&quot; para cerrar el pop-up 
 Debe redireccionar al Dashboard general de la Web App . 
&#160; 
 Labels Pop-up de anuncio de punto de donación inactivo 
 En la siguiente documentación, cuando se coloca la notación (concat) quiere decir que se están uniendo o concatenando labels, o en algunos casos muy específicos, caracteres (como por ejemplo en el cuerpo del pop-up al establecer (concat)&#160; ( (concat) , quiere decir que entre las dos variables (identificadas con doble corchete) se concatena un carácter de apertura de paréntesis) 
&#160; 
 lo sentimos!... &#58;( 
 class= lbl_lo_sentimos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_lo_sentimos )&#160; 
&#160; 
 Este punto de donación está inactivo.&#160; Comunícate con el administrador del sistema EatCloud para su acivación a través del entorno administrativo 
 class= lbl_pod_inactivo (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_pod_inactivo ) 
&#160; 
 Si el punto de donación está activo (el llamado al API responde adecuadamente), entonces el sistema podrá seguir adelante con las demás validaciones. 
&#160; 
 Ejemplo 1&#58; entorno de pruebas, cuenta &quot;exito&quot; punto de donación (eatc-id) &quot;39&quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=exito&amp;eatc-id=39 &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 
&#160; 
&#160; 
 Ejemplo 2&#58; entorno de pruebas, cuenta &quot;exito&quot; punto de donación (eatc-id) &quot;646&quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=exito&amp;eatc-id= 646 &#160; &#160; 
&#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces se despliega un pop-up con la siguiente información que no lo deja seguir con la toma del anuncio de la donación&#58; 

&#160; 
 lo sentimos!... &#58;( 
 Este punto de donación está inactivo.&#160; Comunícate con el administrador del sistema EatCloud para su activación a través del entorno administrativo 

&#160; 
 Validación de tope de anuncios por punto de donación por mes 
 Antes de desplegar el formulario, el sistema deberá realizar la siguiente consulta, teniendo en cuenta los datos alojados en la información de la cuenta y que se consultan mediante este llamado 
&#160; 
 VALIDACIÓN PREVIA AL DESPLIEGUE DEL FORMULARIO DE CAPTURA DE DONACIONES 
 El esquema de licenciamiento definido, establece unos límites de donaciones a realizarse por mes y punto de donación, de acuerdo al tipo de la licencia que posee la cuenta.&#160; Es por eso que antes de desplegar el formulario de captura, se deberá realizar las siguientes validaciones&#58; 
&#160; 
 Validación de tope de anuncios por punto de donación por mes ***NUEVO &#58; no se tienen en cuenta los anuncios cancelados*** 
 Antes de desplegar el formulario, el sistema deberá realizar la siguiente consulta, teniendo en cuenta los datos alojados en la información de la cuenta y que se consultan mediante este llamado 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125;&amp;_distinct=type&#160; 
&#160; 
 Con la consulta se obtiene el dato eatc_cua. type y con ese dato se realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_types_of_licenses? eatc_code =&#123;&#123;eatc_cua. type &#125;&#125; 
&#160; 
 Si esta última consulta no trae ningún valor, se utilizará esta consulta por defecto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =free 
&#160; 
 El sistema debe evaluar si el número que se obtiene en el parámetro eatc_types_of_licenses. eatc_dona_x_pod_mes_limit es mayor al valor del count de la consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. eatc_cua_master &#125;&#125;/eatc_dona_headers?eatc-pod_id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;eatc-publication_date[0]=&#123;&#123;fecha_primer_dia_mes_actual&#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123;fecha_actual&#125;&#125;&amp;eatc-estate= ! cancelled &amp;_cont 

&#160; 
 Nota para el desarrollo&#58; se implementa el llamado con el prefijo&#160; &quot; ! &quot; tal como se indica en la documentación al respecto , para consultar los datos diferentes al dato que se envía en el parámetro de consulta, en esta caso, anuncios con estado cancelado . Lo anterior quiere decir que en el conteo de las donaciones límite por licencia no se tomarán en cuenta las donaciones canceladas. 

&#160; 
 Si es mayor lo dejará pasar al formulario. 
&#160; 
 Si es menor o igual no lo debe dejar tomar el anuncio, debe realizar un registro de datos en la estructura eatc_upgrade_events que se detalla más adelante y debe mostrar un Pop-up informándole al usuario que ha sobrepasado el límite de anuncios de su plan ( dicho pop-up se detalla más adelante ) 

&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; (en el registro se separan por &quot; &amp; &quot;) 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = wapp 
 eatc_upgrade_event = eatc_dona_x_pod_mes_limit 
 eatc_user = &#123;&#123;eatc_pods. eatc-id &#125;&#125; 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parámetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot;axionlog&quot;, en el punto de donación con eatc-id &quot; rjWVOF2Uyw2YrpVUU2DvC &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= axionlog &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= axionlog &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = axionlog 
 eatc_platform = wapp 
 eatc_upgrade_event = eatc_dona_x_pod_mes_limit 
 eatc_user = rjWVOF2Uyw2YrpVUU2DvC 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= axionlog &amp;_distinct =type = free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creación de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =axionlog&amp; eatc_platform =wapp&amp; eatc_upgrade_event =eatc_dona_x_pod_mes_limit&amp; eatc_user =rjWVOF2Uyw2YrpVUU2DvC&amp; eatc_actual_rescue_plan =free &#160; 

&#160; 
 Wireframe Pop-up de anuncio de límite de anuncios mensuales por punto sobrepasados 

 &quot;x&quot; para cerrar el pop-up 
 Debe redireccionar al Dashboard general de la Web App . 
&#160; 
 Labels Pop-up de anuncio de límite de anuncios mensuales por punto sobrepasados 
 En la siguiente documentación, cuando se coloca la notación (concat) quiere decir que se están uniendo o concatenando labels, o en algunos casos muy específicos, caracteres (como por ejemplo en el cuerpo del pop-up al establecer (concat)&#160; ( (concat) , quiere decir que entre las dos variables (identificadas con doble corchete) se concatena un caracter de apertura de paréntesis) 
&#160; 
 lo sentimos!... &#58;( 
 class= lbl_lo_sentimos ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_lo_sentimos )&#160; 
&#160; 
 Has superado el límite de donaciones por punto de donación mensuales de tu plan rescate (concat)&#160; &#123;&#123;Plan_de_rescate&#125;&#125; (concat)&#160; ( (concat) &#123;&#123;numero_anuncios_por_pod_mes&#125;&#125; (concat) anuncios de donación). 
 class= lbl_has_superado_limite_dona ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_has_superado_limite_dona ) 
 &#160;&#160; 
 &#123;&#123;Plan_de_rescate&#125;&#125; (en el ejemplo&#58; &quot;Free&quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot;axionlog&quot; 
 El sistema debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name=axionlog&amp;_distinct =type &#160; 
&#160; 
 Dada la respuesta que trae el servicio&#58; type &#58; &quot;free&quot; , entonces ese es el valor (free) que se despliega en el pop-up 

&#160; 
 &#123;&#123;numero_anuncios_por_pod_mes&#125;&#125; en el ejemplo &quot; 3 &quot; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_types_of_licenses?eatc_code=&#123;&#123;eatc_cua. type &#125;&#125;&amp;_distinct = eatc_dona_x_pod_mes_limit 
&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot;axionlog&quot; 
 Como con la consulta anterior se obtubo que&#160; eatc_cua. type &#58; &quot;free&quot; , entonces el sistema debe realizar la siguiente consulta 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses?eatc_code=free&amp;_distinct =eatc_dona_x_pod_mes_limit 
&#160; 
 Dada la respuesta que trae el servicio&#58; eatc_dona_x_pod_mes_limit &#58; &quot;3&quot; , entonces ese es el valor (3) que se despliega en el pop-up 
&#160; 
 anuncios de donación. 
 &#160;class= lbl_anuncios_donacion_parentesis ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_anuncios_donacion_parentesis )&#160;&#160; 
&#160; 
 Contacta al administrador de tu cuenta EatCloud para actualizar el plan. 
 class= lbl_cont_admin_act_plan ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_cont_admin_act_plan )&#160; 

 Ejemplo 1&#58; Ambiente productivo, fecha&#58; 2021-07-27, cuenta exito, eatc_pods. eatc-id=39 
 El eatc_pod cuyo eatc-id es 39 perteneciente a la cuenta &quot; exito &quot; desea crear un anuncio de donación el día 27 de julio de 2021, por lo tanto el sistema debe realizar las siguientes consultas y validaciones&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 type&#58; &quot; impacto &quot; 
&#160; 
 Por lo tanto se debe proceder en primera instancia con esta consulta (para establecer el límite de anuncios por punto de donación al mes para la cuenta en cuestión&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =impacto &#160; 
&#160; 
 Como se obtiene en el parámetro eatc_dona_x_pod_mes_limit &#58; &quot;100000000&quot;&#160; y este es mayor al valor del count de la consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=39&amp;eatc-publication_date[0]=2021-07-01&amp;eatc-publication_date[1]=2021-07-27&amp;_cont &#160; 
&#160; 
 El sistema le desplegará el formulario de creación de anuncios de donación. 
&#160; 
&#160; 
 Ejemplo 2&#58; Ambiente de pruebas, fecha y hora&#58; 2019-11-11 11&#58;11&#58;11 , cuenta colombia , eatc_pods. eatc-id= nzzn1 
 El eatc_pod cuyo eatc-id es nzzn1 perteneciente a la cuenta &quot; colombia &quot; desea crear un anuncio de donación el día 27 de noviembre de 2019, por lo tanto el sistema debe realizar las siguientes consultas y validaciones&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160; 
 type&#58; &quot; free &quot; 
&#160; 
 Por lo tanto se debe proceder en primera instancia con esta consulta (para establecer el límite de anuncios por punto de donación al mes para la cuenta en cuestión&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses? eatc_code =free &#160;&#160; 
&#160; 
 Como se obtiene en el parámetro eatc_dona_x_pod_mes_limit &#58; &quot;3&quot;&#160; y este es mayor al valor del count de la consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=nzzn1&amp;eatc-publication_date[0]=2019-11-01&amp;eatc-publication_date[1]=2020-11-11&amp;_cont &#160; 
&#160; 
 El sistema no desplegará el formulario de creación de la donación realizar y realizará el siguiente registro en la estructura de eventos de upgrade 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime = 2019-11-11 %20 11&#58;11&#58;11 &amp; eatc_date = 2019-11-11 &amp; eatc_country= co &amp; eatc_cua_master = abaco &amp; eatc_cua = colombia &amp; eatc_platform =wapp&amp; eatc_upgrade_event =eatc_dona_x_pod_mes_limit&amp; eatc_user = nzzn1 &amp; eatc_actual_rescue_plan = free&#160; 
&#160; 
 Hecho el registro el sistema presenta el siguiente mensaje 
&#160; 
 Lo sentimos!... &#58;( 
 Has superado el límite de donaciones por punto de donación mensuales de tu plan rescate free&#160; ( 3 anuncios de donación). 
 Contacta al administrador de tu cuenta EatCloud para actualizar el plan. 

&#160; 
 EDICIÓN DE COORDENADAS DEL PUNTO DE DONACIÓN 
 Debe funcionar como está implementado en la actualidad 
 Y debe desplegarse después del título de la funcionalidad y antes de las pestañas de proceso 

 PESTAÑAS DE PROCESO 

 Label 
 class=&quot; lbl_agrega_productos &quot;&#160; 
 class=&quot; lbl_confirma_donacion &quot;&#160; 
&#160; 
 Descripción básica de su funcionamiento 
 Estas son pestañas que deben ubicar al usuario en la parte del proceso en la cual se encuentra.&#160; Por lo tanto su valor por defecto (es decir, debe aparecer como una pestaña activa por defecto, con un color distintivo que así lo indique) es &quot;PASO 1&#58; AGREGA TUS PRODUCTOS&quot; y solo podrá pasar al PASO 2 cuando tenga por lo menos un producto agregado. 

 Agregar productos para donación 
 Label 
 class=&quot; lbl_agregar_productos_donacion &quot; 
&#160; 
 Botones Agregar y Cargar productos 

 En una primera implementación estos botones no van, dado que se entiende que servirán cuando se implemente una funcionalidad de carga de productos en lote, pero como por el momento no se tiene esa funcionalidad, no son necesarios, dado que lo que se despliega de manera automática es el formulario de captura de datos (sin necesidad de pasar a otra funcionalidad de subida de productos). 
&#160; 
 Formulario de captura de información 
 Su funcionamiento es similar al implementado en la funcionalidad actual , con la mejora que cada campo de captura incorporará un &quot; tooltip &quot; (signo de interrogación encerrado en un círculo azul en el diseño encima de cada campo de captura) para entregarle al usuario mayor información sobre la captura que va a realizar (Todo el demás funcionamiento es similar, incluyendo la marcación de campos obligatorios).&#160; A continuación se presenta la documentación de los labels de place holder y tooltip requeridos 
&#160; 
 Nombre del producto 
 Place holder&#58; class=&quot;lbl_nombre_producto&quot; 
 Tooltip&#58; class=&quot;lbl_nombre_producto_desc&quot; 
 Obligatorio 

&#160; 
 Código del producto 
 Place holder&#58; class=&quot;lbl_codigo_producto&quot; 
 Tooltip&#58; class=&quot;lbl_codigo_producto_desc&quot; 
 Obligatorio 

&#160; 
 Cantidad 
 Place holder&#58; class=&quot;lbl_cantidad&quot; 
 Tooltip&#58; class=&quot;lbl_cantidad_desc&quot; 
 Obligatorio 

&#160; 
 Peso unitario en kilogramos 
 Place holder&#58; class=&quot;lbl_peso_unitario_kg&quot; 
 Tooltip&#58; class=&quot;lbl_peso_unitario_kg_desc&quot; 
 Obligatorio 

&#160; 
 Costo unitario 
 Place holder&#58; class=&quot;lbl_costo_unitario&quot; 
 Tooltip&#58; class=&quot;lbl_costo_unitario_desc&quot; 
 Obligatorio 

&#160; 
 Porcentaje de IVA ***NUEVO &#58; permitir incorporarle al input dos decimales *** 
 Place holder&#58; class=&quot;lbl_porcentaje_iva&quot; 
&#160; 
 Tooltip&#58; class=&quot;lbl_porcentaje_iva_desc&quot; 
&#160; 
 Tipo de dato&#58; float (2), por defecto integer ( por defecto se debe comportar como un entero, tal como lo hace hoy, pero debe permitir introducir dos decimales ) 
 Obligatorio 
&#160; 
 Valor por defecto&#58;&#160; para obtener el valor por defecto que se coloca en el campo, el sistema debe realizar la siguiente consulta&#58; 
 &#160; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;eatc_cua. eatc_cua_master &#125;&#125;&amp;_distinct= eatc_default_VAT 
&#160; 
 Solo se dinamiza la obtención de este valor por defecto, pero el funcionamiento de captura del campo seguirá igual a como funciona actualmente. 
&#160; 

 Ejemplo&#58; entorno de pruebas, cuenta maestra&#58; abaco 
&#160; 
 El sistema debe realizar entonces la siguiente consulta&#58;&#160; https&#58;//dev.datagov.eatcloud.info//api/eatcloud/eatc_cua_master?eatc_cua=abaco&amp;_distinct= eatc_default_VAT &#160; 
 Como se obtiene la siguiente respuesta&#58; eatc_default_VAT &#58; &quot;19&quot; , el valor por defecto que se coloca en el campo es &quot;19&quot; . El usuario podrá variar dicho valor (tal como funciona actualmente) 

&#160; 
 Causal de baja 
 Place holder&#58; class=&quot;lbl_causal_baja&quot; 
 Tooltip&#58; class=&quot;lbl_causal_baja_desc&quot; 
 Obligatorio 

&#160; 
 Los siguientes campos de captura no están en el diseño.&#160; Dado que son opcionales se debe hacerle entender al usuario de manera clara esta condición de captura. 
&#160; 
 Contiene alérgenos 
 Place holder&#58; class=&quot;lbl_contiene_alergenos&quot; 
 Tooltip&#58; class=&quot;lbl_contiene_alergenos_desc&quot; 
 Opcional 

&#160; 
 Fecha más próxima de vencimiento 
 Place holder&#58; class=&quot;lbl_fecha_proxima_vencimiento&quot; 
 Tooltip&#58; class=&quot;lbl_fecha_proxima_vencimiento_desc&quot; 
 Opcional 

&#160; 
 ***NUEVO&#58; Lote *** 
 Place holder&#58; class=&quot;lbl_lote&quot; 
 Tooltip&#58; class=&quot;lbl_lote_desc&quot; 
 Tipo de campo de captura&#58; text_input 
 Tipo de dato&#58; string (alfanumérico) 
 Validación&#58; ninguna (campo opcional ) 
 Se escribe en&#58; eatc_dona. eatc_lote 

&#160; 
 Botones de acción del formulario 

 Cancelar 
class=&quot;lbl_cancelar&quot; 
&#160; 
 Este botón borra la información del formulario y retorna al ancla que se debe ubicar al principio del mismo 
&#160; 
 Agregar 
class=&quot;lbl_agregar&quot; 
&#160; 
 Este botón hace el registro en el detalle de anuncio de donación (eatc_dona) y retorna al ancla que se debe ubicar al principio del mismo 

 Resumen Donación 
&#160; 
 Label 
 class=&quot; lbl_resumen_donacion &quot; 
&#160; 
 Card &quot;No has agregado ningún producto a tu donación&quot; 
 class=&quot; lbl_no_has_agregado_productos &quot; 

 Descripción básica de su funcionamiento 
 Esta card, como su nombre lo indica, aparece cuando no hay productos agregados al anuncio de donación y desaparece cuando se agrega el primero, para dar lugar al listado de productos de la donación que se describe a continuación. 
&#160; 
 Listado de productos 

 Esta es una de las partes más importantes del nuevo diseño, ya que en vistas tipo escritorio, muestra el listado al lado del formulario (no abajo como está en este momento). 
&#160; 
 Los siguientes son los labels de las columnas que se presentan en el diseño 
&#160; 
 Producto 
 class=&quot;lbl_producto&quot; 
&#160; 
 Cantidad 
 class=&quot; lbl_cantidad &quot; 
&#160; 
 Peso total 
 class=&quot; lbl_peso_total &quot; 
&#160; 
 Costo total 
 class=&quot; lbl_costo_total &quot; 

 Botón &quot;Terminar donación&quot; 
 class=&quot; lbl_costo_total &quot; 
&#160; 
 Este botón da paso a &quot;PASO &quot;&#58; CONFIRMA DONACIÓN&quot; que debe presentarse en una pestaña aparte (diferente a la actual en donde se presenta el formulario y el listado resumen. A diferencia de la implementación actual, este botón no genera aun el encabezado de donación, el cual debe generarse una vez se confirme la donación. A continuación se detallan los labels de este segundo paso 

 Campos que&#160; se agregan al encabezado de donación&#58; 

 Documento soporte 
 Place holder&#58; class=&quot; lbl_digitar_documento_soporte &quot; 
 Tooltip&#58; class=&quot; lbl_digitar_documento_soporte_desc &quot; 
 Tipo de campo de captura&#58; text_input 
 Tipo de dato&#58; string (alfanumérico) 
 Validación&#58; ninguna (campo opcional ) 
 Se escribe en&#58; eatc_dona_headers. eatc-doc 

&#160; 
 Observación punto de donación 
 Place holder&#58; class=&quot; lbl_observacion_pod &quot; 
 Tooltip&#58; class=&quot; lbl_observacion_pod _desc&quot; 
 Tipo de campo de captura&#58; text_input 
 Tipo de dato&#58; string (alfanumérico) 
 Validación&#58; ninguna (campo opcional ) 
 Se escribe en&#58; eatc_dona_headers. eatc-warning &#160; 

&#160; 
 ***NUEVO&#58; Requisitos para retirar la donación *** 
 Validación para mostrar el campo de captura (y evitar problemas por faltantes en estructuras de datos)&#58; se deberá validar que para la estructura eatc_dona_headers de la respectiva cuenta maestra, exista el campo &quot; eatc_dona_headers. eatc_logistical_requirements &quot;.&#160; Si el campo existe, se despliega el campo de captura.&#160; Si no existe no se despliega el campo de captura 
&#160; 
 Place holder&#58; class=&quot;lbl_rq_retirar_donacion&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_rq_retirar_donacion )&#160; 
&#160; 
 Tooltip&#58; class=&quot;lbl_rq_retirar_donacion_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;idlabel=lbl_rq_retirar_donacion_desc )&#160; 
&#160; 
 Tipo de campo de captura&#58; text_input 
&#160; 
 Tipo de dato&#58; string (alfanumérico) 
&#160; 
 Validación&#58; ninguna (campo opcional ) 
&#160; 
 Se escribe en&#58; eatc_dona_headers. eatc_logistical_requirements 

 PASO 2&#58; CONFIRMA LA DONACIÓN 
 Título &#58; class=&quot; lbl_confirma_donacion &quot;&#160; 
 Descripción &#58; class=&quot; lbl_confirma_donacion_desc &quot;&#160; 

 Producto 
 class=&quot;lbl_producto&quot; 
&#160; 
 Cantidad 
 class=&quot; lbl_cantidad &quot; 
&#160; 
 Peso total 
 class=&quot; lbl_peso_total &quot; 
&#160; 
 Costo total 
 class=&quot; lbl_costo_total &quot; 
&#160; 
 Total 
 class=&quot; lbl_total &quot; 

 Botón &quot;Confirmar donación&quot; 
 class=&quot; lbl_confirmar_donacion &quot; 
&#160; 
 Este botón invoca el servicio para crear el encabezado de la donación.&#160; Si se obtiene una respuesta satisfactoria de dicho servicio, entonces se debe mostrar una pantalla de confirmación que se describe a continuación. 

 Tu anuncio de donación ha sido creado 

 Tu anuncio de donación ha sido creado 
 class=&quot; lbl_anuncio_creado &quot; 
&#160; 
 Muchísimas gracias. En breve encontraremos un beneficiario 
 class=&quot; lbl_anuncio_creado_desc &quot; 
&#160; 
 Botón finalizar 
 class=&quot; lbl_finalizar &quot; 
 Este botón retorna al dashboard principal . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnueva-creaci%C3%B3n-de-auncios-de-donaci%C3%B3n-eatc_dona_upl%2F3611950363-pop-up_limite_dona_sobrepasado.jpg&ow=575&oh=218, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnueva-creaci%C3%B3n-de-auncios-de-donaci%C3%B3n-eatc_dona_upl%2F3611950363-pop-up_limite_dona_sobrepasado.jpg&ow=575&oh=218 

 176.000000000000 

 CREACIÓN DE ANUNCIO DE DONACIÓN (EATC_DONA_UPL)