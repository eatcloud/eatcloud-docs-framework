# nuevo-dashboard-principal-eatc_pods_dsh.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseño 
 http&#58;//repograf.eatcloud.info/home.html# &#160; 

 Mensaje parte superior del dashboard (se debe mostrar después de un login exitoso) 
 *** Ver documentación *** 

&#160; 
 ***NUEVO&#58;&#160; M ensajes de interés [PENDIENTE REFINAR]*** 
&#160; 
 &#160;Se enriquece la información que se carga para la mensajería del dashboard (doma_dashboard) con el ánimo de poderle incorporar de manera dinámica más elementos y para sentar las bases para un sistema de comunicación con beneficiarios más dinámico y completo. 
&#160; 
 En primera instancia se abre la puerta para que no solamente se presente un solo mensaje, sino que se puedan presentar varios mensajes en una especie de rotador de mensajes y que permita incorporar características como imagen, y un botón de &quot;Ver más&quot;, más administrable (con posibilidades de cambiar la leyenda y un ícono en el botón). 
&#160; 
 También se abre la posibilidad para incorporar otros tipos de mensajes que podrán verse por ejemplo en &quot;la nube de donaciones (eatcloud)&quot; cuando ocurra un evento en particular (por ejemplo, que no hallan donaciones disponibles o&#58; &quot;dona_not_available&quot;. 
&#160; 
 Las mejoras en este sentido también abren las posibilidades para incorporar mensajes que solo se vean en un país en particular (empezando por Colombia&#58; co), y también de programar fechas de inicio y fin de las publicaciones. 
&#160; 
 Consulta de los anuncios disponibles para el dashboard de gestor de donaciones (doma_dashboard) ***Revisar dinamismo a partir de _DOM.cua_master y _DOM.cua_master_country*** 
&#160; 
 La App debe consultar en primera instancia el tomar el dato _DOM. cua_master_country (que se obtuvo en los procesos de autenticación )&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_cua=abaco 
&#160; 
 Como el llamado devuelve esta información&#58; 
 &#123; 
 ts&#58; &quot;200430155656&quot;, 
 op&#58; true, 
 cont&#58; 1, 
 res&#58; 
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
 Se toma como eatc_country a &quot; co &quot; y se procede a llamar el mensaje que para el país está dispuesto para desplegarse en el dashboard ( doma_dashboard ) 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_doma_messages? eatc_message_type=doma_dashboard &amp; eatc_country= &#123;&#123;_DOM. cua_master_country &#125;&#125;&amp;eatc_doma_code=_all 
&#160; 
 Por ejemplo para el ambiente de pruebas y _DOM. cua_master=abaco la consulta sería&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_doma_messages? eatc_message_type=doma_dashboard &amp; eatc_country= co&amp;eatc_doma_code=_all 
&#160; 
 El API devuelve la siguiente respuesta&#58; 
 &#123; 
 _id &#58; &quot;1&quot; , 
 code &#58; &quot;1&quot; , 
 date &#58; &quot;2021-04-22&quot; , 
 title &#58; &quot;ACTUALIZACIÓN IMPORTANTE&#58; Versión de la App 1.40.41&quot; , 
 message &#58; &quot;Por el crecimiento en la actividad de nuestra plataforma fue necesario realizar un importante ajuste, que tiene como objetivo agilizar las consultas de las donaciones. De igual manera se mejoraron los procesos que garantizan su correcta gestión. Te invitamos a estar pendiente de la disponibilidad de la nueva versión haciendo clic en el &quot;Más&quot;. A continuación debes realizar los siguientes pasos&#58; 1- Reiniciar el dispositivo. 2- Confirmar que la versión 1.40.41 es la que quedó actualizada en tu dispositivo. NOTA IMPORTANTE&#58; como la nueva versión incluye un ajuste los procesos de gestión, se visualizarán donaciones que no quedaron verificadas. Por favor realiza el proceso indicado, para que las donaciones tengan el cierre necesario. De antemano muchas gracias.&quot; , 
 url &#58; &quot; https&#58;//play.google.com/store/apps/details?id=co.nzzn.eatcloud.beneficiarios &quot; , 
 eatc_doma_code &#58; &quot;_all&quot; , 
 order &#58; &quot;1&quot; , 
 eatc_message_type &#58; &quot;doma_dashboard&quot; , 
 display_conditions &#58; &quot;always&quot; , 
 display_time_sec &#58; &quot;fix&quot; , 
 url_button_legend &#58; &quot;Ver más&quot; , 
 url_button_icon &#58; &quot;&quot; , 
 image_url &#58; &quot;&quot; , 
 eatc_country &#58; &quot;co&quot; , 
 published_since &#58; &quot;2021-04-22&quot; , 
 published_until &#58; &quot;&quot; , 
 display_query &#58; &quot;&quot; , 
 display_query_response &#58; &quot;&quot; 
 &#125; 
&#160; 
 A continuación se dan lineamientos generales para disponer el mensaje de acuerdo a la información que trae el API&#58; 
 eatc_message_type, eatc_country, eatc_doma_code 
&#160; 
 Posteriormente se podrá realizar un llamado para el gestor de donación específico, a fin de mostrar mensajes solo para ellos. 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_doma_messages?eatc_doma_code=&#123;&#123;eatc_users. organizacion &#125;&#125; 
&#160; 
 _id, code, date&#58; 
&#160; 
 Son datos informativos que permiten diferenciar el mensaje.&#160; Por el momento no se muestran en la interfaz del usuario. 
&#160; 
 Card de mensaje (diseño&#58; card ; carrusel ) 
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
 URL que se abrirá al presionar el botón respectivo (que en la primera versión fue un &quot;+&quot; en un círculo , pero que en la versión mejorada evolucionará a un botón con un letrero y un ícono (ambos administrables) en su interior. 
&#160; 
 url_button_legend &#58; en el ejemplo&#58; &quot;Ver más&quot; . 
&#160; 
 Corresponde a la leyenda del botón que abre la URL.&#160; Si por ejemplo en este campo se configura en vez de un letrero el parámetro &quot; _message &quot;, esto quiere decir que el mismo mensaje será el botón para abrir la URL respectiva y no habrá un botón adicional (es decir el botón adicional se debe ocultar). 
&#160; 
 url_button_icon &#58; &quot;&quot;, 
&#160; 
 Se podrá incorporar un pequeño ícono para el botón el cual se podrá desplegar desde una URL particular (URL del recurso gráfico), con el ánimo de hacerlo administrable. 
&#160; 
 image_url 
 En la versión mejorada se podrá incorporar una imagen al mensaje.&#160; Esta imagen se obtendrá de la URL registrada en este campo. 
&#160; 
 order 
&#160; 
 En la versión mejorada en este espacio que ocupa la actual card única del mensaje a los beneficiarios, se podrán mostrar varios mensajes en forma de &quot;sliders&quot;, o “carrusel” .&#160; Este campo servirá para establecer el orden en que se muestran estos mensajes. 
&#160; 
 display_conditions &#58; ejemplo&#58; &quot;always&quot; 
&#160; 
 En futuras versiones, se podrán establecer condiciones de visualización de los mensajes (esto funciona más en el nuevo espacio que se abrirá en la nube de donaciones ).&#160; Como en este caso el parámetro indica &quot; always &quot;, esto indica que siempre se visualiza el mensaje en este punto. 
&#160; 
 display_time_sec &#58; &quot;fix&quot;, 
&#160; 
 En futuras versiones, se podrán establecer el tiempo en segundos de la visualización de un mensaje (antes de pasar a otro) o antes de por ejemplo abrir otra funcionalidad (lo que funciona más para la nube de donaciones ).&#160; Como en este caso se informa que el mensaje estará fijo (&quot;fix&quot;) esto querrá decir que el mensaje no rotará, ni tendrá un tiempo de visualización. Si en este campo se determina un tiempo en segundos, se debe utilizar el dato obtenido para setear la propiedad del carrusel, que permite un paso dinámico de una card de mensaje a otra. 
&#160; 
 published_since, published_until &#58; 
&#160; 
 Se podrá establecer tiempos de inicio y fin de la publicación para establecer cuando se comienza a mostrar y cuando se termina de mostrar un mensaje. 
 Si en un periodo de tiempo no existen mensajes configurados, todo el carrusel debe ocultarse para mostrar en primera instancia las cards de las métricas aplicadas a cada beneficiario. 

&#160; 
 Etiquetas encabezado 

 Tablero 
 class=&quot;lbl_tablero&quot; 
&#160; 
 ***NUEVO&#58; Horarios de atención 
 class=&quot;lbl_horarios_atencion&quot; 
&#160; 
 Después del Título &quot;Tablero&quot;, y antes de los botones &quot;Crear anuncios de Donación&quot; y &quot;Ver entregas de donaciones&quot;, se deberá colocar una tabla (no editable) con los horarios de atención, tal como se ve en la funcionalidad &quot; Horarios de atención &quot; ( https&#58;//devdonantes.eatcloud.info/webapp/index.html#!/config_horario_atencion ), que presente los horarios de atención del punto de donación respectivo, trayendo los datos de la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;_DOM.cua_user&#125;&#125; /eatc_attention_schedule?eatc-pod_id=&#123;&#123;eatc-pod_id&#125;&#125; &#160; 
&#160; 
 La tabla deberá ser más compacta que la que presenta la funcionalidad de configuración (sin los botones de acción que permiten configurar),&#160; 

 y con un botón que permita ir a la respectiva funcionalidad de configuración de horarios de atención&#58; https&#58;//devdonantes.eatcloud.info/webapp/index.html#!/config_horario_atencion mediante un botón con el label &quot;class= lbl_configurar_horarios_atencion &quot; 
&#160; 
 *** 
&#160; 
 Crear anuncio de donación 
 class=&quot;lbl_crear_anuncios&quot; 
 En una primera versión, se utilizará la misma funcionalidad que hasta el momento ha funcionado .&#160; En una segunda etapa se desplegará una funcionalidad mejorada . 
&#160; 
 Ver listado de donaciones 
 class=&quot;lbl_ver_dona_list&quot; 
&#160; 
 Dará acceso a la nueva funcionalidad de Listado de donaciones . 

&#160; 
 Donaciones próximas a entregar 
 class=&quot;lbl_donaciones_entregar&quot; 

&#160; 
 Cards de donaciones próximas a entregar (anuncios pendientes de verificación)&#160; 
 Esta funcionalidad se constituirá en una alerta flotante con posición destacada y&#160; siempre visible a primera vista en el dashboard, que dará muy fácil acceso al proceso de verificación de código de recogida (que se ha identificado como un proceso problemático y por lo tanto se propone esta facilidad buscando que el mismo sea de más fácil operación. Puede ser similar a la card de anuncio de donación que se implementa en la funcionalidad &quot; seguimiento de anuncio de donación &quot; con algunos ajustes que se documentan más abajo) &#160; cada vez que una de las donaciones cambie su estado de &quot;adjudicado&quot; a &quot;programado&quot;. 
&#160; 
&#160; 
 CONSULTA PARA OBTENER LA INFORMACIÓN NECESARIA ***NUEVO&#58; CONSULTA DIFERENCIAL SEGÚN EL DATO REGISTRADO EN EATC_PODS. CENTRALIZED_MANAGEMENT_POD *** 
 El sistema realizará la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/eatc_pods?eatc-id=&#123;&#123;eatc_pods. eatc-id &#125;&#125;&amp;_cmp=centralized_management_pod 
&#160; 
 De acuerdo a la respuesta obtenida en el llamado se construye el llamado para traer los anuncios en el listado&#58; 
&#160; 
 Si la respuesta es &quot;n&quot; o &quot;vacía&quot; (la consulta no trae respuesta) 
 El sistema deberá operar como lo ha venido haciendo , es decir deberá realizar la siguiente consulta 
&#160; 
 el sistema toma el parámetro &quot; eatc-id &quot; del punto de donación ( eatc_pods ) respectivo y su _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-pod_id=&#123;&#123;eatc_pods.eatc-id&#125;&#125; &amp;eatc_cua_origin=&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 
&#160; 
 Con la información obtenida, el sistema debe mostrar aquellos anuncios cuya fecha de publicación ( eatc_dona_headers. eatc-publication_date ) esté dentro del último mes. 
&#160; 
 Si la respuesta es &quot; y &quot; 
 El sistema deberá traer todas las donaciones, cuyo donante es el dueño del punto, es decir, este punto se convertirá en un punto de gestión centralizada para todas las donaciones de esa cua_user 
&#160; 
 el sistema toma el parámetro _DOM.cua_user 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_headers?eatc-donor =&#123;&#123; _DOM .cua_user &#125;&#125; &amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 
&#160; 
 Con la información obtenida, el sistema debe mostrar aquellos anuncios cuya fecha de publicación ( eatc_dona_headers. eatc-publication_date ) esté dentro del último mes.&#160; 
&#160; 
 NOTA PARA EL DESARROLLADOR &#58; Se deberá implementar paginación en esta consulta dado que puede traer gran cantidad de registros. 
 Ejemplo&#58;&#160; ambiente de pruebas, cua_user= postobon , eatc_pods.eatc-id= P2130234402 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/postobon/eatc_pods?eatc-id= P2130234402 &amp;_cmp=centralized_management_pod &#160;&#160; 
 Dado que la consulta trae &quot; y &quot; como respuesta, entonces el sistema realiza esta consulta para traer las donaciones&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=postobon&amp;eatc-state=scheduled,delivered,received&amp; eatc_code_verification_datetime= 0000-00-00&amp;2000&#58;00&#58;00 &#160; 
&#160; 
 Etiqueta si no hay donaciones pendientes para entregar&#58; 
 Si la anterior consulta no trae resultados, se debe mostrar una letrero vistoso con el siguiente label&#58; 
 class=&quot;lbl_sin_dona_pendientes_entrega&quot; 

 Etiquetas card de anuncios próximos a entregarse 

 Mitad izquierda de la card 
 Fecha del anuncio&#58; 
 class=&quot;lbl_fecha_anuncio&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers .eatc-publication_date 
&#160; 
 Hora&#58; 
 class=&quot;lbl_hora&quot; 
&#160; 
 La información se toma de (haciendo un split para mostrar la porción que contiene la hora) 
 eatc_dona_headers .eatc-publication_dateme 
&#160; 
 Nombre del beneficiario ( eatc_donation_manager ) al cual se le adjudicó el anuncio y programó su recogida 
 La información se toma de&#58; 
 eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Dirección (no está en el diseño)&#58;&#160; 
 class=&quot;lbl_direccion_doma&quot; 
&#160; 
 La información se toma de&#58; 
 eatc_dona_headers .eatc-donation_manager_address 
&#160; 
 Teléfono (no está en el diseño)&#58;&#160; 
 class=&quot;lbl_telefono_doma&quot; 
&#160; 
 La información se toma de&#58; 
 eatc_dona_headers .eatc- donation_manager_phone 
&#160; 
 Tag&#58; ¡Verifica de inmediato! (no está en el diseño) 
 (Se debe mostrar si existe un registro válido en e atc_dona_headers .eatc- picking_checkout_datetime ) 
&#160; 
 Debe ser vistoso, puede ser acompañado de un icono de signo de admiración en un círculo rojo 

 class=&quot;lbl_verificar_inmediatamente&quot; 

 Mitad derecha de la card 
 Datos de recogida 
 class=&quot;lbl_datos_recogida&quot; 
&#160; 
 Fecha y hora programada de recogida (no está en el diseño) 
 class=&quot;lbl_fecha_hora_recogida_programada&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Recoge (En el diseño está como &quot;Nombre&quot;) 
 class=&quot;lbl_recolector&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers . eatc-picker_name 
&#160; 
 Identificación (En el diseño está como &quot;Teléfono&quot;) 
 class=&quot;lbl_doc_id_recolector&quot; 
 La información se toma de&#160; 
 eatc_dona_headers . eatc-picker_doc_id 
&#160; 
 Placa 
 class=&quot;lbl_placa_recolector&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers . eatc-picker_license_plate 
&#160; 
 Llegó al punto de donación a las (no está en el diseño)&#58;&#160; 
 (información que solo se debe mostrar si existe un registro válido en e atc_dona_headers .eatc-picking_checkin_datetime ) 
 class=&quot;lbl_fecha_hora_llegada&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Salió del punto de donación a las&#58;&#160; 
 (información que solo se debe mostrar si existe un registro válido en e atc_dona_headers .eatc- picking_checkout_datetime ) 
 class=&quot;lbl_fecha_hora_salida&quot; 
&#160; 
 La información se toma de&#160; 
 eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Botón&#58; Verificar código&#58; 
 class=&quot; btn_init_verf_codrecg &quot; 
&#160; 
 Da ingreso a la funcionalidad de &quot; Verificación de código de recogida &quot; (que permanece igual en funcionamiento a como se ha implementado anteriormente) 
&#160; 
 Botón&#58; Detalle donación (en el diseño está como &quot;Detalle anuncio&quot;)&#58; 
 class=&quot; lbl_detalle_donacion &quot; 
&#160; 
 Da ingreso al dahsboard del anuncio de donación (que permanece igual en funcionamiento a como se ha implementado anteriormente) 

 ***NUEVO&#58; formulario Net Promoter Score**** 
&#160; 
 Llamado del servicio 
 Se deberá integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se deberán realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio&#58; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= webapp &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125; 
&#160; 
 Los parámetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 
&#160; 
 eatc_user_code 
 Corresponde al parámetro &quot;eatc-id&quot; del punto de donación que se encuentra logueado en la plataforma y que podría consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 eatc_plataform 
 webapp (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado será&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado será&#58; prod 
&#160; 
 Si el servicio responde de manera negativa, no se despliega el formulario. 
&#160; 
 Si el servicio responde de manera afirmativa se desplegará el formulario respectivo. 
&#160; 
 Despliegue del formulario 
 El formulario se deberá desplegar según su definición y los mecanismos de integración que se provean para este fin.&#160; Se debe mirar si se despliega como un modal (que tendrá dos formularios sucesivos adentro), en la parte superior de la pantalla o en la parte inferior de la&#160; 
 pantalla. 
 Registro del NPS ( nps_main_question ) 

 Edición&#160; del NPS ( nps_secondary_question ) 

 Llamado para el registro del NPS ( nps_main_question ) 
 Se deberá realizar el siguiente llamado para realizar el registro del NPS 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_user_code=&#123;&#123; eatc_user_code &#125;&#125;&amp;eatc_plataform= webapp &amp;eatc_enviroment=&#123;&#123; eatc_enviroment &#125;&#125;&amp;nps=&#123;&#123; entero_de_0_a_10 &#125;&#125;&amp;_operacion= insert 
&#160; 
 Los parámetros para realizar la consulta son los siguientes&#58; 
&#160; 
 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
&#160; 
 eatc_user_code 
 Corresponde al parámetro &quot;eatc-id&quot; del punto de donación que se encuentra logueado en la plataforma y que podría consultarse con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM.cua_user&#125;&#125;/eatc_pods?_id=&#123;&#123;_id&#125;&#125; 
&#160; 
 eatc_plataform 
 webapp (constante para este llamado) 
&#160; 
 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado será&#58; pruebas 
 Si se trabaja en ambiente productivo el valor enviado será&#58; prod 
&#160; 
 entero_de_0_a_10 
 input del formulario respectivo 
&#160; 
 Llamado para la edición&#160; del NPS ( nps_secondary_question ) 
 Para hacer el registro se deberá disponer un servicio que reciba los siguientes parámetros 
&#160; 
 https&#58;//datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id=&#123;&#123;_id&#125;&#125;&amp;lang=&#123;&#123; iso2_idioma &#125;&#125;&amp;plataforma= webapp &amp;nps_secundary_answer=&#123;&#123; text_input &#125;&#125;&amp;_operacion= update 
&#160; 
 Este llamado se debe realizar cuando se oprime el botón cuyo label es &quot; nps_submit_btn &quot; . 
&#160; 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .&#160; Si no se encuentra registrado por defecto se enviará &quot; en &quot;) 
&#160; 
 eatc_plataform 
 webapp (constante para este llamado) 
&#160; 
 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-principal-eatc_pods_dsh%2F3772707025-enc_dsh.jpg&ow=1280&oh=261, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnuevo-dashboard-principal-eatc_pods_dsh%2F3772707025-enc_dsh.jpg&ow=1280&oh=261 
 EATCLOUD DONANTES 

 170.000000000000 

 NUEVO DASHBOARD PRINCIPAL: EATC_PODS_DSH