# nuevo-dashboard-principal-eatc_doma_dsh.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 D ASHBOARD QUE PRESENTA MENSAJES IMPORTANTES Y LOS PRINCIPALES KPIS 

 Quitar leyenda&#58; &quot;Tu puntaje EatCloud&quot; del principio de la pantalla 

&#160; 
 ***NUEVO*** Validacin del estado del beneficiario para entrar al dashboard. 

&#160; 
 La aplicacin, cada vez que se ingrese al dashboard principal de la aplicacin, deber validar los datos que se validan en el login (usuario y password) y tambin deber validar si la organizacin a la cual pertenece el usuario, est activa o no ( eatc_state ), para dejarla continuar, o en caso contrario, para forzar la salida de la aplicacin y retornar a la pantalla de login. 
&#160; 
 Para hacer la validacin el sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123;identificador_unico_registro&#125;&#125;&amp;eatc_state=activo&amp;_cont 
&#160; 
 Si la consulta trae una respuesta vlida ( count mayor que cero ), entonces el usuario puede seguir en el dashboard, de lo contrario, debe forzarse la salida de la app y retorno a la pantalla de login. 

&#160; 
 Ejemplo 1&#58; Ambiente de pruebas 
 Un usuario de la organizacin con identificador_unico_registro=901163191, intenta entrar al dashboard.&#160; Al hacerlo el sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=901163191&amp;eatc_state=activo&amp;_cont &#160; 
&#160; 
 Como el sistema arroja esta respuesta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;210713150125&quot; , 
 op &#58; true , 
 cont &#58; 1 , 
 res &#58;&#160; 
 [ 
 &#123; 
 count &#58; &quot;0&quot; 
 &#125; 
 ], 
 mem &#58; 0.43 , 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 ( count &#58; &quot;0&quot; ) Entonces la aplicacin se cierra y retorna al login . 

&#160; 
 Ejemplo 2&#58; Ambiente de pruebas 
 Un usuario de la organizacin con identificador_unico_registro= 890103741 , intenta entrar al dashboard.&#160; Al hacerlo el sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=890103741&amp;eatc_state=activo&amp;_cont &#160;&#160; 
&#160; 
 Como el sistema arroja esta respuesta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;210713150125&quot; , 
 op &#58; true , 
 cont &#58; 1 , 
 res &#58;&#160; 
 [ 
 &#123; 
 count &#58; &quot;1&quot; 
 &#125; 
 ], 
 mem &#58; 0.43 , 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 ( count &#58; &quot;1&quot; ) Entonces la aplicacin le permite al usuario seguir en el dashboard. 

&#160; 
 Mensajes de la comunidad =&gt; Mejoramiento para que pueda mostrar varios mensajes (a manera de carrusel), mensajes direccionados a cuentas en particular y mensajes que puedan incorporar imagen y video 
 Se enriquece la informacin que se carga para la mensajera del dashboard ( doma_dashboard ) con el nimo de poderle incorporar de manera dinmica ms elementos y para sentar las bases para un sistema de comunicacin con beneficiarios ms dinmico y completo. 
&#160; 
 En primera instancia se abre la puerta para que no solamente se presente un solo mensaje, sino que se puedan presentar varios mensajes en una especie de rotador de mensajes y que permita incorporar caractersticas como imagen, y un botn de &quot;Ver ms&quot;, ms administrable (con posibilidades de cambiar la leyenda y un cono en el botn). 
&#160; 
 Tambin se abre la posibilidad para incorporar otros tipos de mensajes que podrn verse por ejemplo en &quot;la nube de donaciones (eatcloud)&quot; cuando ocurra un evento en particular (por ejemplo, que no hallan donaciones disponibles o&#58; &quot;dona_not_available&quot;. 
&#160; 
 Las mejoras en este sentido tambin abren las posibilidades para incorporar mensajes que solo se vean en un pas en particular (empezando por Colombia&#58; co), y tambin de programar fechas de inicio y fin de las publicaciones. 

 Consulta de los anuncios disponibles para el dashboard de gestor de donaciones (doma_dashboard) ***Revisar dinamismo a partir de _DOM.cua_master y _DOM.cua_master_country*** 
 La App debe consultar en primera instancia el tomar el dato _DOM. cua_master_country (que se obtuvo en los procesos de autenticacin )&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_cua=abaco 
&#160; 
 Como el llamado devuelve esta informacin&#58; 
 &#123; 
 ts&#58; &quot;200430155656&quot;, 
 op&#58; true, 
 cont&#58; 1, 
 res&#58;&#160; 
 [ 
 &#123; 
 _id&#58; &quot;1&quot;, 
 eatc_cua&#58; &quot;abaco&quot;, 
 eatc_country&#58; &quot; co &quot;, 
 eatc_doma_id_min_digit_val&#58; &quot;9&quot;, 
 eatc_doma_id_max_digit_val&#58; &quot;9&quot;, 
 eatc_doma_wa&#58; &quot;573052423193&quot;, 
 eatc_donors_wa&#58; &quot;573125333638&quot; 
 &#125; 
 ], 
 mem&#58; 0.39, 
 time&#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Se toma como eatc_country a &quot; co &quot; y se procede a llamar el mensaje que para el pas est dispuesto para desplegarse en el dashboard ( doma_dashboard ) 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_doma_messages? eatc_message_type=doma_dashboard &amp; eatc_country= &#123;&#123;_DOM. cua_master_country &#125;&#125;&amp;eatc_doma_code=_all&#160; 
&#160; 
 Por ejemplo para el ambiente de pruebas y _DOM. cua_master=abaco la consulta sera&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_doma_messages? eatc_message_type=doma_dashboard &amp; eatc_country= co&amp;eatc_doma_code=_all 
&#160; 
 El API devuelve la siguiente respuesta&#58; 
 &#123; 
 _id &#58; &quot;1&quot; , 
 code &#58; &quot;1&quot; , 
 date &#58; &quot;2021-04-22&quot; ,&#125; 
 title &#58; &quot;ACTUALIZACIN IMPORTANTE&#58; Versin de la App 1.40.41&quot; , 
 message &#58; &quot;Por el crecimiento en la actividad de nuestra plataforma fue necesario realizar un importante ajuste, que tiene como objetivo agilizar las consultas de las donaciones. De igual manera se mejoraron los procesos que garantizan su correcta gestin. Te invitamos a estar pendiente de la disponibilidad de la nueva versin haciendo clic en el &quot;Ms&quot;. A continuacin debes realizar los siguientes pasos&#58; 1- Reiniciar el dispositivo. 2- Confirmar que la versin 1.40.41 es la que qued actualizada en tu dispositivo. NOTA IMPORTANTE&#58; como la nueva versin incluye un ajuste los procesos de gestin, se visualizarn donaciones que no quedaron verificadas. Por favor realiza el proceso indicado, para que las donaciones tengan el cierre necesario. De antemano muchas gracias.&quot; , 
 url &#58; &quot; https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios &quot; , 
 eatc_doma_code &#58; &quot;_all&quot; , 
 order &#58; &quot;1&quot; , 
 eatc_message_type &#58; &quot;doma_dashboard&quot; , 
 display_conditions &#58; &quot;always&quot; , 
 display_time_sec &#58; &quot;fix&quot; , 
 url_button_legend &#58; &quot;Ver ms&quot; , 
 url_button_icon &#58; &quot;&quot; , 
 image_url &#58; &quot;&quot; , 
 eatc_country &#58; &quot;co&quot; , 
 published_since &#58; &quot;2021-04-22&quot; , 
 published_until &#58; &quot;&quot; , 
 display_query &#58; &quot;&quot; , 
 display_query_response &#58; &quot;&quot; 
 &#125; 
&#160; 
 A continuacin se dan lineamientos generales para disponer el mensaje de acuerdo a la informacin que trae el API&#58; 
 eatc_message_type, eatc_country, eatc_doma_code 
&#160; 
 Posteriormente se podr realizar un llamado para el gestor de donacin especfico, a fin de mostrar mensajes solo para ellos. 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_doma_messages?eatc_doma_code=&#123;&#123;eatc_users. organizacion &#125;&#125;&#160; 

&#160; 
 _id, code, date&#58; 
&#160; 
 Son datos informativos que permiten diferenciar el mensaje.&#160; Por el momento no se muestran en la interfaz del usuario. 
&#160; 
 Card de mensaje (diseo&#58; card ; carrusel ) 

&#160; title 
 Sirve para pintar el ttulo del mensaje. 
&#160; 
 &#160; message 
 Sirve para pintar el cuerpo del mensaje. 
&#160; 
 url 
 URL que se abrir al presionar el botn respectivo (que en la primera versin fue un &quot;+&quot; en un crculo , pero que en la versin mejorada evolucionar a un botn con un letrero y un cono (ambos administrables) en su interior. 
&#160; 
 url_button_legend &#58; en el ejemplo&#58; &quot;Ver ms&quot; . 
 Corresponde a la leyenda del botn que abre la URL.&#160; Si por ejemplo en este campo se configura en vez de un letrero el parmetro &quot; _message &quot;, esto quiere decir que el mismo mensaje ser el botn para abrir la URL respectiva y no habr un botn adicional (es decir el botn adicional se debe ocultar). 
&#160; 
 url_button_icon &#58; &quot;&quot;, 
 Se podr incorporar un pequeo cono para el botn el cual se podr desplegar desde una URL particular (URL del recurso grfico), con el nimo de hacerlo administrable. 
&#160; 
 image_url 
 En la versin mejorada se podr incorporar una imagen al mensaje.&#160; Esta imagen se obtendr de la URL registrada en este campo. 
&#160; 
 order 
 En la versin mejorada en este espacio que ocupa la actual card nica del mensaje a los beneficiarios, se podrn mostrar varios mensajes en forma de &quot;sliders&quot;, o carrusel .&#160; Este campo servir para establecer el orden en que se muestran estos mensajes. 
&#160; 
 display_conditions &#58; ejemplo&#58; &quot;always&quot; 
 En futuras versiones, se podrn establecer condiciones de visualizacin de los mensajes (esto funciona ms en el nuevo espacio que se abrir en la nube de donaciones ).&#160; Como en este caso el parmetro indica &quot; always &quot;, esto indica que siempre se visualiza el mensaje en este punto. 
&#160; 
 display_time_sec &#58; &quot;fix&quot;, 
 En futuras versiones, se podrn establecer el tiempo en segundos de la visualizacin de un mensaje (antes de pasar a otro) o antes de por ejemplo abrir otra funcionalidad (lo que funciona ms para la nube de donaciones ).&#160; Como en este caso se informa que el mensaje estar fijo (&quot;fix&quot;) esto querr decir que el mensaje no rotar, ni tendr un tiempo de visualizacin. Si en este campo se determina un tiempo en segundos, se debe utilizar el dato obtenido para setear la propiedad del carrusel, que permite un paso dinmico de una card de mensaje a otra. 

 published_since, published_until &#58; 
 Se podr establecer tiempos de inicio y fin de la publicacin para establecer cuando se comienza a mostrar y cuando se termina de mostrar un mensaje. 
&#160; 
 Si en un periodo de tiempo no existen mensajes configurados, todo el carrusel debe ocultarse para mostrar en primera instancia las cards de las mtricas aplicadas a cada beneficiario. 

 Tus mtricas&#58; 
 Label &#58; class=&quot;lbl_tus_metricas&quot; 
&#160; 
 En esta seccin del dashboard, se mostrar un filtro por fecha conformado por los siguientes valores&#58; 
 ltimo da &#58; class=&quot;lbl_ultimo_dia&quot; 
 ltimos tres das &#58; class=&quot;lbl_ultimos_tres_dias&quot; 
 ltima semana &#58; class=&quot;lbl_ultima_semana&quot; 
 ltimo mes &#58; class=&quot;lbl_ultimo_mes&quot; 
 ltimo trimestre &#58; class=&quot;lbl_ultimo_trimestre&quot; 
 ltimo semestre &#58; class=&quot;lbl_ultimo_semestre&quot; 
 ltimo ao &#58; class=&quot;lbl_ultimo_year&quot; 
 Desde el comienzo &#58; class=&quot;lbl_desde_el_comienzo&quot; 
&#160; 
 Y cuyo valor por defecto ser &quot; ltimos tres das &#58; class=&quot;lbl_ultimos_tres_dias &quot; y a partir del periodo de tiempo definido, se realizarn llamados a diversos APIs, para traer mtricas bsicas de la operacin del beneficiario. 
&#160; 
 Indicadores Clave&#58; 

 Impacto social&#58; muestra el total de kilogramos donados por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
&#160; 
 #KPI de impacto social 
 kg = eatc_dona_headers .eatc-total_weight_kg 
&#160; 

 Impacto econmico&#58; muestra el total de dinero ahorrado por cuenta de las donaciones&#160; por parte del punto de donacin ( eatc_pods ), es decir la sumatoria de todos los ahorros y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
&#160; 
 #KPI de impacto econmico 
 logistics_cost_savings = eatc_dona_headers .eatc-total_weight_kg * [] //Ahorro Almacenamiento&#58; por KG semana&#58; Fro =$394; Seco = $289 
 transport_cost_savings =&#160; eatc_dona_headers .eatc-total_weight_kg * 79 //Ahorro Transporte&#58; por KG =$79 
 waste_management_savings =&#160; eatc_dona_headers .eatc-total_weight_kg * 1105//Ahorro Gestin de residuos&#58; por KG =$1105 
&#160; 
 #KPI de ahorro tributario&#58; 
 income_tax_savings = eatc_dona_headers .eatc-total_cost * 1,25//Beneficio en renta&#58; por cada peso donado se retornan&#58; $1,25 
 vat_savings = eatc_dona_headers .eatc-total_cost * 0,19//Beneficio IVA&#58; por cada peso donado se retornan&#58; =$0,19 
&#160; 

 Impacto ambiental&#58; muestra el total de las emisiones de C02 ahorradas por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ). 
&#160; 
 #KPI de impacto ambiental 
 CO2_tons = eatc_dona_header.eatc-total_weight_kg * [] 

 Tablero de liderazgo&#58;&#160; Por el momento se inhabilita (dado que no es funcional) 
 El dashboard presentar un &quot;Tablero de Liderazgo&quot; en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso 

 *************Tus resultados************ 
 label &#58; class=&quot;lbl_tus_resultados&quot; 
&#160; 
 En esta seccin se presentarn resultados bsicos de la operacin de cada beneficiario (gestor de donaciones), con el diseo de card bsica de resultado&#58; 

 ***NUEVO&#58; FORMULARIO NET PROMOTER SCORE **** 
&#160; 
 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= app_beneficiarios &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;identificador_unico_registro&quot; del gestor del donaciones que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers?_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 eatc_plataform 
 app_beneficiarios (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
&#160; 
 Si el servicio responde de manera negativa, no se despliega el formulario. 
&#160; 
 Si el servicio responde de manera afirmativa se desplegar el formulario respectivo. 
&#160; 
 Despliegue del formulario 
 El formulario se deber desplegar segn su definicin y los mecanismos de integracin que se provean para este fin.&#160; Se debe mirar si se despliega como un modal (que tendr dos formularios sucesivos adentro), en la parte superior de la pantalla o en la parte inferior de la&#160; 
 pantalla. 
&#160; 
 Registro del NPS ( nps_main_question ) 

 Edicin&#160; del NPS ( nps_secondary_question ) 

 Llamado para el registro del NPS ( nps_main_question ) ***NUEVO*** adicin de parmetros de clasificacin (se resaltan en rojo) 
&#160; 
 Se deber realizar el siguiente llamado para realizar el registro del NPS 
&#160; 
 https&#58;//datagov.eatcloud.info/crd/eatcloud/?_tabla=int_nps_eatcloud&amp;eatc_cua=&#123;&#123; eatc_donation_managers .organizacin &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= app_beneficiarios &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125; &amp; eatc_vertical =&#123;&#123; eatc_donation_managers .tipo_organizacion &#125;&#125;&amp; eatc_cua_size =&#123;&#123; eatc_donation_managers .eatc_doma_typology_b &#125;&#125;&amp; eatc_licence_type =&#123;&#123; eatc_donation_managers . eatc_licence_type &#125;&#125; &amp;_operacion= insert 
&#160; 
 Los parmetros para realizar la consulta son los siguientes&#58; 
&#160; 
 eatc_donation_managers.organizacin 
 Corresponde al nombre ( eatc_donation_managers .organizacin ) del gestor de donaciones&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_donation_managers?_id=&#123;&#123;eatc_donation_managers._id&#125;&#125; 
&#160; 
 eatc_user_code 
 Corresponde al parmetro &quot;eatc_users. correo_electronico &quot; del usuario del gestor del donaciones que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/ eatc_users ? organizacion =&#123;&#123; eatc_donation_managers .identificador_unico_registro &#125;&#125; 
&#160; 
 eatc_plataform 
 app_beneficiarios (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser&#58; prod 
&#160; 
 entero_de_0_a_10 
 input del formulario respectivo 
&#160; 
 eatc_vertical 
 Corresponde al parmetro eatc_donation_managers .tipo_organizacion del beneficario (&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers ?_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 eatc_cua_size 
 Corresponde al parmetro eatc_donation_managers .eatc_doma_typology_b del beneficiario (&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers ?_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 eatc_licence_type 
 Corresponde al parmetro eatc_donation_managers . eatc_licence_type del beneficiario (&#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers ?_id=&#123;&#123;_id&#125;&#125; (es un campo que aun no existe por lo tanto se enva inicialmente en blanco, pero se debe crear el nuevo campo en las tablas de eatc_donation_managers) 
&#160; 
 Llamado para la edicin&#160; del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma= app_beneficiarios &amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
&#160; 
 Este llamado se debe realizar cuando se oprime el botn cuyo label es &quot; nps_submit_btn &quot; . 
&#160; 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .&#160; Si no se encuentra registrado por defecto se enviar &quot; en &quot;) 
&#160; 
 eatc_plataform 
 app_beneficiarios (constante para este llamado) 
&#160; 
 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-principal-eatc_doma_dsh%2F3029850618-EmbeddedImage--68-.jpg&ow=1280&oh=262, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-principal-eatc_doma_dsh%2F3029850618-EmbeddedImage--68-.jpg&ow=1280&oh=262 
 EatCloud APP Beneficiarios 

 511.000000000000 

 NUEVO DASHBOARD PRINCIPAL: EATC_DOMA_DSH