# mis-donaciones-eatc_dona_mine.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Filtro por defecto 

 Esta vista debe mostrar siempre los anuncios de donacin adjudicados al gestor de donacin al cual pertenece el usuario que est consultando y cuyo estado sea &quot;awarded&quot; y&#160; &quot;scheduled&quot;. 
&#160; 
 Consulta de organizacin &#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_users?numero_cedula=&#123;&#123;numero_cedula&#125;&#125; 
&#160; 
 Consulta de anuncios&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donation_manager_code=&#123;&#123; organizacin &#125;&#125;&amp;eatc_state=awarded,scheduled,delivered&amp;_compress 

 Consulta de anuncios 
 el sistema toma el parmetro &quot; organizacion &quot; del usuario respectivo&#58; 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
&#160; 
 El usuario Juan Carlos Buitrago, cuyo &quot;numero_cedula&quot;= 8161174 , tiene como organizacin el dato&#58; 900326456-1 
&#160; 
 Ambiente productivo&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174 &#160; 
&#160; 
 Trama comprimida&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?numero_cedula=8161174&amp;_compress &#160; 

 Con este parmetro&#160; y los cdigos almacenados en el array se va al API de encabezados de anuncio de donacin&#160; ( eatc_dona_headers ) y en el parmetro &quot; eatc-donation_manager_code &quot;, se enva el dato obtenido previamente (organizacion). 
&#160; 
 Ejemplo _DOM.cua_master=abaco&#58; 
 El usuario Juan Carlos Buitrago, cuya organizacin es&#58; 90326456-1, se realiza la siguiente consulta&#58; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=900326456-1 &#160;&#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=900326456-1&amp;_compress &#160; 
&#160; 
 Se muestran por defecto en esta vista 
 Luego en la vista se filtran los anuncios de donacin cuyo estado sea &quot;awarded&quot; y&#160; &quot;scheduled&quot;&#160; y &quot; delivered &quot; (para los anuncios cuyo estado sea &quot;delivered&quot; se debe colocar un anuncio visible, similar al que se coloca para &quot;programar&quot; que indique que se deben &quot;verificar&quot;, como estrategia para incentivar la aplicacin de este proceso, que en los primeros das del piloto se observ poco aplicado por los usuarios) para su presentacin por defecto.&#160; Los dems anuncios se podrn mostrar accediendo a travs de la funcionalidad de filtros.&#160; Es decir, que al entrar a &quot;mis donaciones&quot;, el sistema debe mostrar con prelacin aquellos anuncios que requieren acciones urgentes por parte del gestor, como son&#58; la programacin (estado &quot;awarded&quot;) y la recogida (estado &quot;scheduled&quot;). 

&#160; 
 ****NUEVO**** VISUALIZACIN DE ANUNCIOS PARA APPs MAESTRAS (ABACO, NODRIZZA) 
 La app deber validar, si el usuario pertenece a ABACO o a Nodrizza ( tipo_organizacion= Nodrizza,ABACO&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?tipo_organizacion=Nodrizza,ABACO ), y a partir de esta validacin, en la nube de donaciones le debe mostrar todas las donaciones as no estn adjudicadas a la organizacin a la cual pertenece en los datos ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donation_manager_code=_* ) .&#160; La idea es que usuarios de cuentas maestras puedan ver el movimiento de donaciones independiente a que hagan match o no, y tambin puedan ver anuncios que estn en diversos estados diversos a anunciados,&#160; Para esto la card tambin deber mostrar el estado de la donacin y a quin fue adjudicada (en una card similar a la que se presenta en &quot; mis donaciones &quot;) 
&#160; 
 Ejemplo&#58; 
&#160; 
 Si Ivn Daro Restrepo ha ingresado, el da 22 de noviembre de 2019. en la App, dado que su Tipo de Organizacin es Nodrizza 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_users?_id=33 
&#160; 
 El sistema le deber desplegar los anuncios, desplegados para el da en curso&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-state=announced,awarded,scheduled,delivered,recived,pre-certified,certified&amp;eatc-publication_date=2019-11-22 
&#160; 
 ***NUEVO&#58; Donaciones que se le despliegan al usuario tipo &quot;transportador&quot; *** 
 En &quot; Mis donaciones &quot;, solo se le mostrarn al usuario tipo &quot; transportador &quot; las donaciones que estn en estado &quot; scheduled &quot; y que han sido adjudicadas a l.&#160; Para determinar dichas donaciones, el sistema deber realizar esta consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donation_manager_code=&#123;&#123; organizacin &#125;&#125;&amp;eatc-picker_id=&#123;&#123;eatc_users . correo_electronico &#125;&#125;&amp;picker_license_plate= &#123;&#123;eatc_users . numero_cedula &#125;&#125; &amp;eatc_state=scheduled&amp;_compress 
&#160; 
 Cabe anotar que aunque es confuso que en el eatc-picker_id se enva el correo electrnico y en el parmetro picker_license_plate se enva el nmero de cdula, se dise as, para tener el mnimo de friccin a la hora de desplegar este modelo funcional (hacer caso omiso a la confusin de trminos dado que es deliverada). 
&#160; 
 Que tambin puede interpretarse a partir de los datos de login en la APP como 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donation_manager_code=&#123;&#123; organizacin &#125;&#125;&amp;eatc-picker_id= &#123;&#123;usuario&#125;&#125; &amp;picker_license_plate= &#123;&#123;password&#125;&#125; &amp;eatc_state=scheduled&amp;_compress 
&#160; 
 Filtros&#58; 
 Mediante los filtros definidos que corresponden a los diferentes estados , se podrn consultar ms anuncios de donacin adjudicados al gestor de donaciones al cual pertenece el usuario, definiendo a que filtro estado corresponde. 
&#160; 
 ***NUEVO*** 
&#160; 
 Se debe incorporar en el filtro los anuncios cuyo estado sea &quot;cancelado&quot;. 

 CARD de encabezado de anuncio de donacin&#58; informacin 

 Consulta de informacin ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id=&#123;&#123;eatc-id&#125;&#125; 
&#160; 
 Esta card mostrar para todos los anuncios la siguiente informacin&#58; 
&#160; 
 Fecha y hora de programacin del anuncio&#58;&#160; 
 Anuncios con estado (eatc-state) &quot;scheduled&quot; (para anuncios con estado (eatc-state) &quot;awarded&quot; aparecer un botn &quot; programar &quot; que abajo se describe) 
 Corresponde al campo &quot; eatc-programed_picking_datetime &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
&#160; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 5252095 , corresponde al dato &quot; 2019-09-19 01&#58;37&#58;54 &quot; que est contenido en el campo &quot; eatc-programed_picking_datetime &quot; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=5252095 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=5252095&amp;_compress &#160; 
&#160; 
 Faltan ##min&#58; anuncios con estado &quot;awared&quot; 
 Tomando el dato de &quot; eatc-adjudication_datetime &quot;, se le suman 1 horas y la informacin corresponde a la resta de esa hora con respecto a la fecha y hora actual. Se debe indicar que &quot;Faltan ## min para programar la recogida&quot; . 
&#160; 
 Faltan ##hrs ##min&#58; anuncios con estado &quot;scheduled&quot; 
 Tomando el dato de &quot; eatc-programed_picking_datetime &quot;, es el tiempo que resta a partir de la fecha y hora actual, para que se llegue a la fecha y hora programada. 
&#160; 
 Nombre del punto de donacin&#58; 
 Corresponde al campo &quot; eatc_pod_name &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
&#160; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 5252095 , corresponde al dato &quot; CARULLA PALMAS &quot; que est contenido en el campo &quot; eatc_pod_name &quot; 
 &#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095 &#160; &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095&amp;_compress &#160; 
&#160; 
 Direccin&#58; 
 Corresponde al campo &quot; eatc-pod_address &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
&#160; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 5252095 , corresponde al dato &quot; Av. Palac #99-33, Medelln, Antioquia &quot; que est contenido en el campo &quot; eatc-pod_address &quot; (datos cargados a fecha 18 de septiembre). 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095 &#160; 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095&amp;_compress &#160; 
&#160; 
 #### kg&#58; 
 Corresponde al campo &quot; eatc-total_weight_kg &quot;, de eatc_dona_headers 
&#160; 
 Ejemplo _DOM. cua_master=abaco&#58; 
&#160; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 5252095 , corresponde al dato &quot; 392 &quot; que est contenido en el campo &quot; eatc-total_weight_kg &quot; 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095&amp;_compress &#160; 
 &#160; 
&#160; 
 RADIO BUTONS DE ESTADO 
 Muestran el estado , en el que se encuentra el anuncio, sabiendo que segn el &quot;order&quot; de dichos estados, se muestran de manera acumulativa. 
&#160; 
 Ejemplo&#58; 
 un anuncio cuyo estado sea &quot;scheduled&quot; (programado) y que&#160; tiene el valor &quot;order&quot; =3, tambin debe tener marcados los radio buton , &quot;awared&quot; (adjudicado, con &quot;order&quot;=2) y &quot;announced&quot; (anuncidado con &quot;order&quot;=1) 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin ( eatc_dona_headers ), cuyo identificador es (eatc-id) = 5252095 , dado que tiene un estado &quot;&quot;scheduled&quot; (programado) &quot; deberan aparecer marcados los estados&#58; &quot; Anunciado &quot;, &quot; Adjudicado &quot; y &quot; Programado &quot;. 
&#160; 
 Ambiente de productivo&#58; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095 
 Trama comprimida&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id= 5252095&amp;_compress &#160; 

 Donante&#58; 
 Corresponde al campo &quot; eatc_donor &quot;, de eatc_dona_headers 
&#160; 
 Si el donante es diferente a la cuenta que maneja el DOM de la APP, se debe pintar la card del anuncio con un color diferente que permita diferenciarla de las dems donaciones. 
&#160; 
 ***NUEVA*** Punto de recogida 
 Si el registro de match para el anuncio particular tiene un dato vlido (diferente a 0, nulo o vaco) en el campo del registro de match&#58; eatc_match_registry . eatc_pick_up_point_name entonces se despliega un tag vistoso en la card del anuncio de la siguiente manera&#58; 
&#160; 
 label &#58; class=&quot; lbl_punto_de_recogida &quot; 
 La informacin se toma de&#58; eatc_match_registry . eatc_pick_up_point_name 
&#160; 
 Si el registro de match tiene un dato no vlido (cero, nulo o vaco) en eatc_match_registry . eatc_pick_up_point_name entonces no se muestra el tag en la card del anunico. 
&#160; 
 ***NUEVA*** Contiene Alrgenos 
 Si el campo eatc-contains_alergens del encabezado de nuncio de donacin es igual a &quot;si&quot; (o &quot;s&quot; o &quot;yes&quot; o &quot;y&quot;) se debe agregar un tag o etiqueta que diga &quot;Contiene Alrgenos&quot;.&#160; Si este parmetro no existe, viene vaco, nulo o con el valor &quot;no&quot; (o &quot;n&quot;), no se debe mostrar ninguna etiqueta a este respecto. 
&#160; 
 ***NUEVA*** Fecha ms prxima de expiracin 
 Se debe colocar una etiqueta o tag que diga &quot;fecha de expiracin ms prxima&#58; [eatc_dona_header. eatc-closer_expiration_date] . &quot; Si este parmetro no existe, viene vaco, nulo o con el valor &quot;0000-00-00&quot;, no se debe mostrar esta etiqueta o tag. 
&#160; 
 CARD DE ENCABEZADO DE ANUNCIO DE DONACIN&#58; BOTONES DE ACCIN 
 La card posee los siguientes anuncios distintivos y el siguiente botn&#58; 
&#160; 
 Aviso en fondo naranja&#58; Programar recogida! ( ***NUEVO&#58; direcciona a la funcionalidad respectiva*** ) 
 Cuando un anuncio est en estado&#160; &quot;awared&quot;, se despliega este anuncio distintivo en color rojo llamativo. Al presionar este anuncio (analizar si se le cambia el estilo para que parezca un botn ) se debe ingresar a la funcionalidad &quot; Programar Recogida &quot; de la misma manera como se hace desde el respectivo botn ( Botn&#58; programa recogida ) en el dashboard de anuncio de donacin 
&#160; 
 Condicin para mostrar el aviso ***Revisar funcionamiento*** &#58; 
 Solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea &quot;awarded&quot; (adjudicado) . 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id= &#123;&#123; eatc-id &#125;&#125;&amp;eatc-state=awarded 
&#160; 
 ***MEJORA&#58; Condicin para ocultar el aviso&#58; *** 
 El botn no se muestra para anuncios cuyo estado&#160; sea diferente a &quot;awarded&quot; (adjudicado) . 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id= &#123;&#123; eatc-id &#125;&#125;&amp;eatc-state= ! awarded 
&#160; 
 El botn da acceso a la funcionalidad &quot; Programar recogida &quot;. 

&#160; 
 Aviso en fondo naranja&#58; Recoger! ( ***NUEVO&#58; direcciona a la funcionalidad respectiva*** ) 
 Cuando un anuncio est en estado&#160; &quot;scheduled&quot; y [NUEVO] no existe registro en la fecha y hora de check-in &quot; eatc-picking_checkin_datetime &quot;, se despliega este anuncio distintivo en color rojo llamativo. Al presionar este anuncio (analizar si se le cambia el estilo para que parezca un botn ) se debe ingresar a la funcionalidad &quot; Recoger anuncio &quot; de la misma manera como se hace desde el respectivo botn ( Botn&#58; recoge esta donacin ) en el dashboard de anuncio de donacin 
&#160; 
 Condicin para mostrar el aviso&#58; ***MEJORA&#58; validacin de registro en eatc-picker_start_datetime *** 
 Solo se solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea &quot;scheduled&quot; (programado) &#160; y no tengan un dato registrado en &quot; eatc- eatc-picker_start_datetime &quot;&#160; y&#160; no tengan un dato registrado en &quot; eatc-picking_checkin_datetime &quot; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id= &#123;&#123; eatc-id &#125;&#125; &amp;eatc-state =scheduled&amp; eatc-picker_start_datetime= 0000-00-00 %20 00&#58;00&#58;00&amp; eatc-picking_checkin_datetime= 0000-00-00 %20 00&#58;00&#58;00 
&#160; 
 ***MEJORA&#58; Condicin para ocultar el aviso&#58; implementacin operacin lgica _novacio (se deber validar con Jess si esta operacin lgica opera tambin con fechas vacas 0000-00-00 00&#58;00&#58;00) *** 
 El botn no se muestra si el estado de la donacin es diferente a &quot; scheduled &quot; y si hay una fecha y hora vlida en los parmetros &quot; eatc-picker_start_datetime &quot; y &quot; eatc-picking_checkin_datetime= &quot;&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id= &#123;&#123; eatc-id &#125;&#125;&amp;eatc-state= ! scheduled&amp; eatc-picker_start_datetime= _NOVACIO &amp;eatc-picking_checkin_datetime= _NOVACIO 
&#160; 
 El botn da acceso a la funcionalidad &quot; Recoger anuncio de donacin &quot;. 
&#160; 
 Aviso en fondo naranja&#58; Registra salida! ( ***NUEVO&#58; direcciona a la funcionalidad respectiva*** ) ***MEJORA&#58; validacin condicionada segn el valor del campo eatc_donation_managers .eatc_sdm&#58; cuando hay un dato en eatc_donation_managers .eatc_sdm no se muestra el aviso*** 
 Label &#58; class=&quot; lbl_registra_salida_pod &quot; 
&#160; 
 Cuando un anuncio tiene un registro vlido en la fecha y hora de llegada ( eatc_dona_headers. eatc-picking_checkin_datetime diferente a 0000-00-00 00&#58;00&#58;00 ) y (preba lgica &quot;y&quot;) no tiene un registro vlido de fecha y hora de salida eatc_dona_headers. eatc-picking_checkout_datetime siempre y cuando ya se haya superado el timeout respectivo ( y como se establece aqu) , se despliega este anuncio distintivo en color rojo llamativo.&#160; Al presionar este anuncio (analizar si se le cambia el estilo para que parezca un botn ) se debe ingresar a la funcionalidad &quot; Entrega de donacin&#58; registrar hora de salida &quot; de la misma manera como se hace desde el respectivo botn ( Botn&#58; registro de salida de beneficiario ) en el dashboard de anuncio de donacin 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_donations_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= eatc_sdm 
&#160; 
 Si el sistema arroja una respuesta invlida (ejemplo&#58; err_msg &#58; &quot;Unknown column 'eatc_sdm' in 'field list'&quot; ), vaca, nula, o igual a &quot; n &quot; entonces el sistema funcionar como lo viene haciendo&#58; 
&#160; 
 Funcionamiento tradicional (funciona como funcionaba anteriormente)&#58; 
 Para habilitar el aviso se deben evaluar si ya hay un registro de fecha y hora de check-in y que no haya un registro de fecha y hora de check-out (operador lgico &quot;y&quot; es decir que se deben cumplir las dos validaciones para mostrar el botn 
&#160; 
 Primera validacin&#58; que haya un registro vlido en eatc_dona_headers. eatc-picking_checkin_datetime &#160; 
&#160; 
 Segunda validacin&#58; que NO exista un registro valido en eatc_dona_headers .eatc-picking_checkout_datetime para el anuncio en cuestin. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-id= &#123;&#123; eatc-id &#125;&#125; &amp;eatc-picking_checkin_datetime= _NOVACIO &amp;eatc-picking_checkout_datetime= 0000-00-00 %20 00&#58;00&#58;00 &amp;eatc-state= !cancelled 
 Si el sistema arroja como respuesta un &quot;y&quot; , entonces se propone el siguiente nuevo funcionamiento&#58; 
&#160; 
 Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd = y ) ***MEJORA&#58; no se mostrar el botn*** &#58; 
 No se mostrar el aviso 

&#160; 
 Aviso en fondo naranja&#58; Verificar! ( ***NUEVO&#58; direcciona a la funcionalidad respectiva*** ) ***NUEVO&#58; validacin condicionada segn el valor del campo eatc_donation_managers .eatc_sdm*** 
&#160; 
 Label &#58; class=&quot; lbl_verificar &quot; 
&#160; 
 Cuando un anuncio tiene estado (eatc-state) &quot;delivered&quot; y (prueba lgica &quot;Y&quot;&#58; deben cumplirse ambas condiciones)&#160; NO tiene un registro vlido en la fecha y hora de recepcin &quot; eatc-receipt_datetime &quot; (es decir que dicho registro est en 0000-00-00 00&#58;00&#58;00 ) , se despliega este anuncio distintivo en color rojo llamativo. Al presionar este anuncio (analizar si se le cambia el estilo para que parezca un botn ) se debe ingresar a la funcionalidad &quot; Verificacin detallada de anuncio de donacin &quot; de la misma manera como se hace desde el respectivo botn ( Botn&#58; verifica tu donacin ) en el dashboard de anuncio de donacin 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donations_managers?/eatc_donation_managers?identificador_unico_registro=&#123;&#123;eatc_donations_managers. identificador_unico_registro &#125;&#125;&amp;_cmp= eatc_sdm 
&#160; 
 Si el sistema arroja una respuesta invlida (ejemplo&#58; err_msg &#58; &quot;Unknown column 'eatc_sdm' in 'field list'&quot; ), vaca, nula, o igual a &quot; n &quot; entonces el sistema funcionar como lo viene haciendo&#58; 
&#160; 
 Funcionamiento tradicional (funciona como funcionaba anteriormente)&#58; 
 Solo se solo se habilita para anuncios de donacin ( eatc_dona_headers ) que tengan registrado una fecha vlida en el campo&#160; &quot;eatc-picking_checkout_datetime&quot; &#160; y que NO tengan una fecha vlida registrada en &quot; eatc-receipt_datetime &quot;&#160; (anteriormente era solamente en eatc-picking_checkout_datetime ) 
&#160; 
 (****NUEVO******&#58; Se quita esta validacin&#58; &#160; (nueva validacin) cuyo estado &quot;eatc-state&quot; sea &quot;delivered&quot; , y se deja solamente la condicin de una fecha vlida en el campo &quot; eatc-receipt_datetime &quot; y en&#160; &quot;eatc-picking_checkout_datetime&quot; ) 

&#160; 
 Si el sistema arroja como respuesta un &quot;y&quot;, entonces se propone el siguiente nuevo funcionamiento&#58; 
&#160; 
 Nuevo Funcionamiento (para organizaciones con eatc_donations_managers. eatc_smd = y ) &#58; 
 Se habilita para anuncios de donacin ( eatc_dona_headers ) que NO tengan una fecha vlida registrada en &quot; eatc-receipt_datetime &quot; . 
 (Inicialmente solamente se habilitar para el Banco de Alimentos de Cali&#58; ) 
&#160; 
 El botn da acceso a la funcionalidad &quot; Verificacin detallada de anuncio de donacin &quot;. 

&#160; 
 Botn&#58; &quot;Ver ms&quot; 
 Que conecta con la funcionalidad &quot; dashboard de anuncio de donacin &quot;, pasando el parmetro &quot; eatc-id &quot; de eatc_dona_headers 

 ****NUEVO**** Mensajes de solicitud de gestin a gestores 
 Al inicio de la pantalla se debern mostrar aquellos mensajes dirigidos al beneficiario particular y que tengan como tipo &quot; mis_donaciones &quot;.&#160; Adicionalmente para cada mensaje trado se deber evaluar su respectivo &quot; display_query &quot; y &quot; display_query_response &quot; para establecer si el mismo se muestra o no. 
&#160; 
 Consulta de menajes (eatc_doma_messages) para la seccin de mis_donaciones 
 El siguiente proceso se realiza cada vez que se ingresa a &quot;Mis Donaciones&quot; 
&#160; 
 Para establecer cules mensajes se deben mostrar se realiza la siguiente consulta&#58; 
 &#123;&#123; URL_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_doma_messages ?eatc_message_type= mis_donaciones &amp;display_conditions= hasta_gestion_anuncios 
&#160; 
 Para cada uno de los anuncios que devuelve la consulta, se toma el dato incorporado en el parmetro eatc_doma_messages. display_query y se establece si la respuesta que se obtiene corresponde a lo que se establece en el parmetro eatc_doma_messages. display_query_response . Si la respuesta obtenida, corresponde a lo establecido en el parmetro eatc_doma_messages. display_query_response , se muestra el mensaje.&#160; En caso contrario, se procede a realizar para el mensaje particular, la siguiente actualizacin de informacin&#58; 
&#160; 
 &#123;&#123; URL_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_doma_messages &amp;_operacion= insert &amp;display_conditions= gestionado &amp;WHERE_id=&#123;&#123; eatc_doma_messages. _id &#125;&#125; 
 Y el mismo no se mostrar 
&#160; 
 Se muestra en la pgina Mis donaciones el ttulo del mensaje y al oprimir el mismo, se podr ir a ver el cuerpo del mensaje 
&#160; 
 En la pantalla de mis donaciones, se muestra en una tarjeta muy vistosa (que puede tener por ejemplo un signo de interrogacin encerrado en un crculo rojo) el ttulo del mensaje, que viene en el parmetro&#58; eatc_doma_messages. title . Se se oprime la delgada card con el ttulo, se deber poder ver el cuerpo del mensaje que est el parmetro&#58; eatc_doma_messages. message .&#160; Tambin se deber ver el contenido que se obtiene de eatc_doma_messages. url (en principio no vendr informacin en dicho campo, pero en un futuro podr incorporarse).&#160; El usuario tendr oportunidad de cerrar el mensaje (puede ser con una &quot;X&quot; en la parte superior de la visualizacin) y retornar a &quot;Mis donaciones&quot;.&#160; Cada vez que se ingrese de nuevo a mis donaciones se deber actualizar la consulta para traer los mensajes y correr el proceso que se deriva de dicho query 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmis-donaciones-eatc_dona_mine%2F2980015013-mis_donaciones.jpg&ow=575&oh=1280, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmis-donaciones-eatc_dona_mine%2F2980015013-mis_donaciones.jpg&ow=575&oh=1280 
 EatCloud Beneficiarios 

 528.000000000000 

 MIS DONACIONES: EATC_DONA_MINE