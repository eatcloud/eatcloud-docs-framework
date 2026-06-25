# nube-de-donaciones-eatc_dona_cloud.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Informe que permite consultar los anuncios de donación disponibles (según criterios de ubicación, afinidad poblacional y capacidades) 

 Filtro por defecto 

 Esta vista debe mostrar siempre los anuncios de &quot;todos los donantes disponibles en la plataforma&quot;, cuyo estado sea &quot; announced &quot; (anunciado o publicado), ordenados mostrando primero los más antiguos.&#160;&#160; 
&#160; 
 Consulta de anuncios que realizan match 
&#160; 
 A partir de mejoras que se han realizado al match y a los procesos de consulta se plantean las siguientes mejoras en el proceso de consulta de los anuncios que hacen match, buscando optimizar las consultas. El proceso anterior primero consultaba los anuncios y luego consultaba el match para establecer cuál de los anuncios consultados estaban en el match, el decir, se traían muchos datos, para luego quedar con unos pocos.&#160; La primera optimización de ese proceso fue precisamente traer datos filtrados por geografía (y por eso se presentaron problemas con el match multipunto), para luego ir al match.&#160; La idea con esta mejora es cambiar estos múltiples llamados por uno solo y consolidar un proceso de servidor con un llamado optimizado y así lograr mejorar el desempeño del sistema. 
&#160; 
 Nuevo llamado para consultar la nube de donaciones 
&#160; 
 El sistema deberá realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/matchquery/&#123;&#123;_DOM.cua_master&#125;&#125;/&#123;&#123;eatc_donation_managers.identificador_unico_registro&#125;&#125; ?_compress 

&#160; 
 Ejemplo&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/matchquery/abaco/811018073?_compress 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/matchquery/abaco/811018073 
&#160; 
 Con este llamado, el servidor realizará un proceso para realizar las múltiples consultas que hacía la App y también los procesos de filtro, para obtener los anuncios de la nube, y directamente los recibirá listos desde el servidor (sin tener que hacer procesos y llamados adicionales). 

&#160; 
 SI LA CONSULTA DEL MATCHQUERY NO TRAE INFORMACIÓN 
 Si la anterior consulta no trae información, el sistema debe mostrar el siguiente mensaje 
&#160; 
 Título&#58;&#160; Sin donaciones disponibles &#58; class=&quot; lbl_sin_donaciones_disponibles &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_sin_donaciones_disponibles ) 
 Cuerpo del mensaje &#58;&#160; class=&quot; lbl_sin_donaciones_disponibles_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_sin_donaciones_disponibles_desc ) No tenemos en este momento donaciones disponibles para ti en tu zona. Por favor mantente pendiente de la nube de donaciones, que tan pronto tengamos disponibilidad la podrás consultar y asignártela. 
 Botón &#58; &quot; Regresar &quot;&#58; class=&quot; lbl_regresar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_regresar )&#160; debe retornar al dashboard principal de la APP (en donde se muestran los mensajes) 

 DEPRECADO&#58; 
&#160; 
 MEJORA&#58; consulta georeferenciada para obtener un subconjunto más pequeño de donaciones ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 Para traer estos anuncios, se utilizará el servicio &quot; getpuntos &quot;, enviando en parámetro &quot; fieldvalue &quot;, el dato que se obtiene en el campo &quot; coordenadas &quot; del gestor de donación respectivo ( eatc_donation_managers.coordenadas ). 
&#160; 
 Documentación general del proceso 
 Documentación particular (revisar el ejemplo 2 de dicha documentación, que fue realizado para este caso específico) 
&#160; 
 Anuncios que han realizado match ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 Como primer paso, se consultan los anuncios de donación cuyo estado sea &quot;announced&quot;&#58; 
 #Anuncios de donación ( eatc_dona_headers ) estado &quot; announced &quot; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state=announced&#160; 
&#160; 
 Trama comprimida&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-state=announced&amp;_compress&#160;&#160; 
&#160; 
 El sistema toma los códigos de encabezados obtenidos ( eatc-code )y los almacena en un array (valores separados por comas) . 
&#160; 
 Luego el sistema toma el parámetro &quot; organizacion &quot; del usuario respectivo&#58; 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
 El usuario Juan Carlos Buitrago, cuyo &quot;numero_cedula&quot;= 8161174 , tiene como organización el dato&#58; 90326456-1 
&#160; 
 Ambiente productivo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174&amp;_compress &#160; 
&#160; 
 Con este parámetro&#160; y los códigos almacenados en el array se va al API de match (eatc_match_registry) y en el parámetro &quot; eatc-donation_manager_code &quot;, se envía el dato obtenido previamente (organizacion) y en el&#160; &quot; eatc-dona_header_code &quot; se envía el array obtenido. 
&#160; 
 Ejemplo&#58; 
 El usuario Juan Carlos Buitrago, cuya organización es&#58; 90326456-1, se realiza la siguiente consulta&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?eatc-donation_manager_code=90326456-1&amp;eatc-dona_header_code=[array] &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?eatc-donation_manager_code=90326456-1&amp;eatc-dona_header_code=[array]&amp;_compress &#160; 

 [NUEVO&#58; por definir] Mensaje resumido 
 ... 
 [DEPRECADO] VISUALIZACIÓN DE ANUNCIOS GENERADOS ASÍ YA ESTÉN ASIGNADOS A OTRAS ORGANIZACIONES&#58; 
 El sistema deberá mostrar, abajo de los anuncios de donación, que se encuentran en el match y que tienen estado &quot;announced&quot;, aquellos anuncios de donación, que también están en el match , que fueron realizados el día en curso ( eatc-publication_date =[current-date] ) y ya han sido adjudicados, programados, entregados, recibidos, certificados y pre-certificados ( eatc-state =awarded,scheduled,delivered,recived,pre-certified,certified ).&#160; Estos anuncios solo deben presentarse a manera informativa, mostrando también la organización a la cual han sido asignados, su estado (es decir en una card más similar a la que se utiliza en la funcionalidad &quot; mis donaciones &quot;) y no deben permitir consultar los detalles de los mismos.&#160; También puede ser adecuado mostrarlos en un color que los haga aparecer &quot;desactivados para toda acción&quot;. 
&#160; 
 Ejemplo&#58; 
 para el día 23-11-2019, se deben presentar los siguientes anuncios (siempre y cuando estén en el match)&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=awarded,scheduled,delivered,recived,pre-certified,certified&amp;eatc-publication_date=2019-11-2 

 ***NUEVO&#58; Ordenamiento por peso *** 
 El sistema debe tener un botón que permita ordenar el listado de donaciones por peso, de la más pesada a la más liviana (Que es el modo operativo del filtro por defecto) y viceversa (es decir de la donación más liviana a la más pesada). 
&#160; 
 class=lbl_ordenar_listado&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_ordenar_listado 
 class=lbl_por_peso&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_por_peso 
 class= lbl_mas_pesadas_primero (valor por defecto del filtro)&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mas_pesadas_primero 
 class= lbl_mas_livianas_primero&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mas_livianas_primero 
 ***NUEVO&#58; Ordenamiento por distancia *** 
 El sistema debe tener un botón que permita ordenar el listado de donaciones por distancia, de la más cercana (la coordenada más próxima a la ubicación actual del teléfono y este será el modo operativo del filtro por defecto) y viceversa (es decir de la donación más lejana a la más cercana). 
&#160; 
 class=lbl_ordenar_listado&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_ordenar_listado 
 class=lbl_por_distancia&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_por_distancia 
 class=lbl_mas_cercanas_primero (valor por defecto del filtro)&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mas_cercanas_primero &#160; 
 class= lbl_mas_lejanas_primero&#58; datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_mas_lejanas_primero 
 ***NUEVO&#58; filtro por rango de pesos *** 
 En la parte superior de la nube, colocar un nuevo botón&#58; 
&#160; 
 Filtro por peso (funcionalidad que no se le presenta al perfil &quot;transportador&quot;) 
 label&#58; class=lbl_filtro_por_peso&#160; 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_filtro_por_peso &#160; 
&#160; 
 Al presionar el botón el sistema debe presentar una funcionalidad de captura de rangos de peso de la siguiente manera&#58; 
&#160; 
 Deseo ver anuncios cuyo peso en KG se encuentre en el siguiente rango&#58; 
 label&#58; class=lbl_filtro_por_peso_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_filtro_por_peso_desc &#160; 
&#160; 
 Desde 
 label&#58; class=lbl_desde 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_desde &#160; 
 Tipo de campo&#58; input numérico 
 Valor por defecto&#58; 0 
 Validaciones &#58; 
 Debe ser menor que el valor hasta (que se captura en el siguiente input)&#58; &#160; mensaje ante validación no exitosa &#58; class= lbl_desde_menor_hasta &#58; &quot;El valor debe ser menor al valor definido como el rango superior del filtro&quot; (y no debe permitir ingresar el valor) 
 El valor debe ser mayor que cero&#58; no se debe permitir la captura de valores negativos. 
&#160; 
 Hasta 
 label&#58; class=lbl_hasta 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_hasta &#160; 
 Tipo de campo&#58; input numérico 
 Valor por defecto&#58; el que se obtiene con la siguientes consultas (el menor valor de los arrojados por la consulta)&#58; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123;identificador_unico_registro&#125;&#125;&amp;_cmp= capacidad_recogida,capacidad_gestion 
 Ejemplo &#58; ambiente de pruebas para la organización cuyo &quot;identificador_unico_registro es &quot; 900326456 &quot;, el sistema hace la siguiente consulta y&#160; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=900326456&amp;_cmp=capacidad_recogida,capacidad_gestion y por lo tanto el valor por defecto será &quot; 1000000 &quot; 
 Validaciones &#58; 
 Debe ser menor que el valor obtenido en la consulta anterior (que corresponde a la capacidad máxima de gestión / recogida)&#58; mensaje ante validación no exitosa &#58; class= lbl_supera_capacidad_gest_rec &#58; &quot;El valor debe ser menor a las capacidades de recolección / gestión de la organización&quot; (y debe cambiar el valor al valor por defecto, sin dejar ingresar el valor que el usuario definió y está por fuera de dicho rango) 
 Debe ser mayor que el valor hasta (que se captura en el siguiente input)&#58; &#160; mensaje ante validación no exitosa &#58; class= lbl_hasta_mayor_desde &#58; &quot;El valor debe ser mayor al valor definido como el rango inferior del filtro&quot; (y no debe permitir ingresar el valor) 
&#160; 
 Botón&#58; Filtrar nube 
 label&#58; class=lbl_filtrar_nube 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_filtrar_nube &#160; 
&#160; 
 Aparecerá tan pronto el usuario haya seleccionado valores válidos para el filtro.&#160; Cuando se realice esta acción, el sistema deberá mostrar la información del filtro que se aplica en la parte superior de la nube de la siguiente manera 
&#160; 
 &quot;Desde (class=lbl_desde) &#123;&#123;concat&#125;&#125; &#123;&#123;input_desde&#125;&#125;, hasta (class=lbl_hasta) &#123;&#123;concat&#125;&#125; &#123;&#123;input_hasta&#125;&#125; KG (class=lbl_kg) 
&#160; 
 Ejemplo &#58; para una organización que seleccionó como valor desde&#58; 100 y hasta 1000 en la presente funcionalidad, el sistema debe mostar en la parte superior la información del filtro, con la posibilidad de quitarlo (mediante la X en la pastilla que indica el valor del filtro). 

 El sistema solamente presentará en la nube los anuncios que cumplan con ese criterio de filtro en la nube de donaciones, y guardará los valores del filtro, para nuevos ingresos a la nube de donaciones, hasta que el usuario edite o borre el filtro.&#160; Cuando el usuario vuelva a presionar la funcionaliad para configurar el filtro, los valores por defecto que mostrará serán los que configuró previamente. 

&#160; 
 CARD de encabezado de anuncio de donación&#58; información 
&#160; 
 Consulta de información del anuncio para mostrar información en la card ***REVISAR dinamismo a partir de _DOM.cua_master*** 
&#160; 
 El sistema realiza esta consulta para obtener la información de cada anuncio disponible&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id=&#123;&#123;_id&#125;&#125;&#160; 
&#160; 
 Esta card mostrará para todos los anuncios la siguiente información&#58; 
&#160; 
 Fecha y hora de publicación del anuncio&#58; 
 Corresponde al campo &quot; eatc-publication_datetime &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donación ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 8687012 , corresponde al dato &quot; 2019-09-18 15&#58;37&#58;54 &quot; que está contenido en el campo &quot; eatc-publication_datetime &quot; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 

&#160; 
 Faltan ##hrs ##min&#58; 
 Tomando el dato de &quot; eatc-publication_datetime &quot;, se le suman 24 horas y la información corresponde a la resta de esa hora con respecto a la fecha y hora actual. 

&#160; 
 #### kg&#58; 
 Corresponde al campo &quot; eatc-total_weight_kg &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donación ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 8687012 , corresponde al dato &quot; 1000 &quot; que está contenido en el campo &quot; eatc-total_weight_kg &quot; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress &#160; 
&#160; 
 ***NUEVO&#58; Costo de la donación *** 
 Para donantes ( eatc_cua ) con licencia impactoplus (type), con valor &quot; y &quot; en el parametro eatc_show_cost_of_dona y con un número válido en el parámetro eatc_show_cost_if_dona_weigth_is_less_than_kg , el sistema permitirá mostrar el costo de la donación (encerrada en un paréntesis al lado de los KG precedida de la etiqueta de signo de moneda), si el peso de la donación es menor o igual al valor que se tiene registrado en el parámetro eatc_show_cost_if_dona_weigth_is_less_than_kg. 

 P resentación del número de referencias y el número de unidades 

 Botón &quot;Eliminar&quot; (anteriormente &quot;x&quot; en el extremo superior derecho&#160; de la card) &#58; con comprobación antes de realizar la acción 
&#160; 
 Botón&#58; parte superior derecha de la card (donde anteriormente estaba una &quot;X&quot;) 
 Label &#58; class=&quot; lbl_eliminar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_eliminar )&#160; 
&#160; 
 =&gt; Al oprimir el botón el sistema presenta el siguiente cuadro de diálogo 
&#160; 
 ***NUEVO&#58; cuadro de diálogo para corroborar acción 
 Cuando se oprime el anterior botón, el sistema mostrará un cuadro de Diálogo de comprobación de la acción de la siguiente manera&#58; 
 Label &#58; class=&quot; lbl_eliminar_dona_nube_comprobacion &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_eliminar_dona_nube_comprobacion )&#160; 
&#160; 
 &quot;Estás seguro que deseas eliminar esta donación de la nube de donaciones (a partir de esta acción no la podrás volver a consultar)&quot; 
&#160; 
 Botón&#58; &quot;No&quot; (seleccionado por defecto) 
 Label &#58; class=&quot; lbl_no &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_no )&#160; 
&#160; 
 =&gt; Cierra el cuadro de diálogo y retorna a la nube sin realizar ninguna acción. 
&#160; 
 Botón&#58; &quot;Si&quot; 
 Label &#58; class=&quot; lbl_si &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_si )&#160; 
&#160; 
 =&gt; Elimina la donación de la nube de donaciones ( función que se hacía antes oprimiendo la &quot;X&quot; ) 
&#160; 
 ## referencias &#58; *** 
 El sistema deberá mostrar (debajo de los KG del anuncio y en estilo de letra de fácil legibilidad) el número de referencias (referencias de productos) contenidas en el anuncio,&#160; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;_distinct=eatc-odd_id&amp;_cont 
&#160; 
 Se toma el resultado obtenido en &quot; count &quot; y lo presenta como el ## y luego el label&#58; 
 Label &#58; class=&quot; lbl_referencias &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_referencias )&#160; 
&#160; 
 ***NUEVO&#58; ### unidades &#58; *** 
 El sistema deberá mostrar (debajo de los KG del anuncio y del número de referencias, y en estilo de letra de fácil legibilidad) el número de unidades (sumatoria de las cantidades de los productos donados) contenidas en el anuncio,&#160; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp;&amp;_cmp= eatc-odd_quantity 
&#160; 
 El sistema realiza una sumatoria de los valores obtenidos y la presenta como el ### y luego el label&#58; 
 Label &#58; class=&quot; lbl_unidades &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel= lbl_unidades )&#160; 
&#160; 
 ***NUEVO&#58; etiqueta “Comida Preparada”*** 
 El sistema deberá mostrar en la card del anuncio, una etiqueta llamativa que indique que el mismo contiene “Comida Preparada”,&#160; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code si el mismo fue marcado como tal, de la siguiente manera&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; eatc_prepared_food= y &amp;_cmp= eatc_prepared_food 
Si el sistema arroja una respuesta válida “y”, entonces se despliega en la card del anuncio en la nube el siguiente label o etiqueta 
&#160; 
 Label &#58; class=&quot; lbl_comida_preparada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;idlabel=lbl_comida_preparada ) =&gt; PENDIENTE DE CREACIÓN&#58; hacerlo directamente en modernización 
&#160; 
 Si el sistema NO arroja una respuesta válida, no se despliega la etiqueta en la card del anuncio. 
&#160; 
 Nombre del punto de donación&#58; 
 Corresponde al campo &quot; eatc_pod_name &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donación ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 8687012 , corresponde al dato &quot; EXITO COLOMBIA &quot; que está contenido en el campo &quot; eatc_pod_name &quot; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress 

&#160; 
 Dirección&#58; 
 Corresponde al campo &quot; eatc-pod_address &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donación ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 8687012 , corresponde al dato &quot; Transversal 39B, Medellín, Antioquia &quot; que está contenido en el campo &quot; eatc-pod_address &quot; (datos cargados al 18 de septiembre de 2019) 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;_compress 

&#160; 
 Donante&#58; 
 Corresponde al campo &quot; eatc_donor &quot;, de eatc_dona_headers 
&#160; 
 Si el donante es diferente a la cuenta que maneja el DOM de la APP, se debe pintar la card del anuncio con un color diferente que permita diferenciarla de las demás donaciones. 
&#160; 
 ***NUEVA*** Contiene Alérgenos 
 Etiqueta &#58; class=&quot;lbl_contiene_alergenos&quot; 
&#160; 
 Si el campo eatc-contains_alergens del encabezado de nuncio de donación es igual a &quot;si&quot; (o &quot;s&quot; o &quot;yes&quot; o &quot;y&quot;) se debe agregar un tag o etiqueta que diga &quot;Contiene Alérgenos&quot;.&#160; Si este parámetro no existe, viene vacío, nulo o con el valor &quot;no&quot; (o &quot;n&quot;), no se debe mostrar ninguna etiqueta a este respecto. 

&#160; 
 ***NUEVA*** Fecha más próxima de expiración 
 Etiqueta &#58; class=&quot; lbl_fecha_proxima_vencimiento &quot; 
&#160; 
 Se debe colocar una etiqueta o tag que diga &quot;fecha de expiración más próxima&#58; [eatc_dona_header. eatc-closer_expiration_date] . &quot; Si este parámetro no existe, viene vacío, nulo o con el valor &quot;0000-00-00&quot;, no se debe mostrar esta etiqueta o tag. 

&#160; 
 CARD de encabezado de anuncio de donación&#58; &quot;botones de acción&quot; 
 La card posee dos botones de acción a saber&#58; 
&#160; 
 Me interesa&#58;&#160; 
 Que conecta con la funcionalidad &quot; dashboard de anuncio de donación &quot;, pasando el parámetro &quot; eatc-id &quot; de eatc_dona_headers 
&#160; 
 Ver mapa 
 Que muestra el mapa que se encuentra en la funcionalidad &quot; dashboard de anuncio de donación &quot; 
&#160; 
 Ordenamientos avanzados (etapas posteriores) 
 La app debería poseer filtros avanzados en las nube de donaciones con los siguientes parámetros 
&#160; 
 Ordenar por fecha y hora (ascendente y descendente) 
 Según el campo eatc-publication_datetime 
&#160; 
 Ordenar por peso (ascendente y descendente) 
 Según el campo eatc-total_weight_kg 
&#160; 
 Ordenar por valor (ascendente y descendente) 
 Según el campo eatc-total_cost 
&#160; 
 Ordenar por distancia (primero los más cercanos tomando como referencia la coordenada actual) 
 Según los campos eatc-lat y eatc-long 

 Card&#58; mensajes en la nube de donaciones 
 Dada la necesidad de establecer espacios de comunicación, que se activen cuando los usuarios acceden a la nube de donaciones (y por ejemplo no ven anuncios disponibles para ellos), se activa un nuevo espacio de mensajes (mensajes tipo&#58; dona_cloud ), que será totalmente administrable. 
 En primera instancia se abre la puerta para que no solamente se presente un solo mensaje, sino que se puedan presentar varios mensajes en una especie de rotador de mensajes y que permita incorporar características como imagen, y un botón de &quot;Ver más&quot;, más administrable (con posibilidades de cambiar la leyenda y un ícono en el botón). 
&#160; 
 Consulta de los anuncios disponibles para la nube de donaciones (dona_cloud) ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Tomando el dato _DOM. cua_master_country se realiza la siguiente consulta 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_doma_messages? eatc_message_type=dona_cloud &amp; eatc_country=&#123;&#123; _DOM. cua_master_country&#125;&#125; &amp;eatc_doma_code=_* 
&#160; 
 El API devuelve la siguiente respuesta (ejemplo _DOM. cua_master= abaco ) 
 &#123; 
 _id &#58; &quot;2&quot;, 
 code &#58; &quot;2&quot;, 
 date &#58; &quot;2020-04-30&quot;, 
 title &#58; &quot;No existen donaciones disponibles en tu área&quot;, 
 message &#58; &quot;Estamos trabajando fuertemente para mejorar nuestra red de donantes. Por favor sigue pendiente de las notificaciones de la App&quot;, 
 url &#58; &quot; https&#58;//www.instagram.com/tv/B_ivcGaj0N8/?igshid=jz9zl3klnkuf &quot;, 
 eatc_doma_code &#58; &quot;_all&quot;, 
 order &#58; &quot;1&quot;, 
 eatc_message_type &#58; &quot;dona_cloud&quot;, 
 display_conditions &#58; &quot;dona_not_available&quot;, 
 display_time_sec &#58; &quot;14&quot;, 
 url_button_legend &#58; &quot;Ayúdanos a difundir&quot;, 
 url_button_icon &#58; &quot;&quot;, 
 image_url &#58; &quot;&quot;, 
 eatc_country &#58; &quot;co&quot;, 
 published_since &#58; &quot;2020-04-30&quot;, 
 published_until &#58; &quot;&quot; 
 &#125; 
&#160; 
 A continuación se dan lineamientos generales para disponer el mensaje de acuerdo a la información que trae el API&#58; 
 eatc_message_type, eatc_country,eatc_doma_code 
&#160; 
 Posteriormente se podrá realizar un llamado para el gestor de donación específico, a fin de mostrar mensajes solo para ellos. 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_messages?eatc_doma_code=[eatc_users.organizacion ]&#160; 

 _id, code, date&#58; 
&#160; 
 Son datos informativos que permiten diferenciar el mensaje.&#160; Por el momento no se muestran en la interfaz del usuario. 
&#160; 
 title 
&#160; 
 Sirve para pintar el título del mensaje. 
&#160; 
 message 
&#160; 
 Sirve para pintar el cuerpo del mensaje. 
&#160; 
 url 
&#160; 
 URL que se abrirá al presionar el botón respectivo (que en la primera versión fue un &quot;+&quot; en un círculo, pero que en versiones posteriores evolucionará a un botón con un letrero y posiblemente un ícono (ambos administrables) en su interior. 
&#160; 
 url_button_legend &#58; ejemplo&#58; &quot;Ayúdanos a difundir&quot;. 
&#160; 
 Corresponde a la leyenda del botón que abre la URL.&#160; Si por ejemplo en este campo se configura en vez de un letrero el parámetro &quot; _message &quot;, esto quiere decir que el mismo mensaje será el botón para abrir la URL respectiva y no habrá un botón adicional (es decir el botón adicional se debe ocultar). 
&#160; 
 url_button_icon &#58; &quot;&quot;, 
&#160; 
 En futuras versiones se podrá incorporar un pequeño ícono para el botón el cual se podrá desplegar desde una URL particular, con el ánimo de hacerlo administrable. 
&#160; 
 display_conditions &#58; ejemplo&#58; &quot;dona_not_available&quot; 
&#160; 
 La condición de visualización de este mensaje es que se debe desplegar cuando no hay donaciones disponibles para el usuario en cuestión. &#160; En futuras versiones también se podrán desplegar mensajes en este punto sin que se cumpla esa condicion (por ejemplo si en display_conditions se tiene como dato &quot;always&quot; se deberá desplegar el mensaje en la parte superior de la nube, en todo momento. 
&#160; 
 image_url 
&#160; 
 En futuras versiones se podrá incorporar una imagen al mensaje.&#160; Esta imagen se obtendrá de la URL registrada en este campo. 
&#160; 
 order 
&#160; 
 En futuras versiones en este espacio se podrán mostrar varios mensajes en forma de &quot;sliders&quot;.&#160; Este campo servirá para establecer el orden en que se muestran estos mensajes. 
&#160; 
 display_time_sec &#58; ejemplo &quot;14&quot;, 
&#160; 
 Como cuando no hay anuncios disponibles, la App saca al usuario hasta el dashboard principal, se establece este parámetro, para darle un tiempo de visualización al mensaje.&#160; Cuando se generen varios mensajes tipo &quot;rotador&quot; esto servirá para controlar el tiempo que se muestra un mensaje antes de pasar a otro. 
&#160; 
 published_since, published_until &#58; 
&#160; 
 En futuras versiones, se podrá establecer tiempos de inicio y fin de la publicación para establecer cuando se comienza a mostrar y cuando se termina de mostrar un mensaje. 

 Botones de acción (footer) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 524.000000000000 

 NUBE DE DONACIONES: EATC_DONA_CLOUD