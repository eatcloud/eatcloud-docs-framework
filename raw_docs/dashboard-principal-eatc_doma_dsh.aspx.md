# dashboard-principal-eatc_doma_dsh.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Botones de accin 

 D ASHBOARD QUE PRESENTA MENSAJES IMPORTANTES Y LOS PRINCIPALES KPIS 

 Card: mensajes de la comunidad 
 Se enriquece la informacin que se carga para la mensajera del dashboard (doma_dashboard) con el nimo de poderle incorporar de manera dinmica ms elementos y para sentar las bases para un sistema de comunicacin con donantes ms dinmico y completo. 

 En primera instancia se abre la puerta para que no solamente se presente un solo mensaje, sino que se puedan presentar varios mensajes en una especie de rotador de mensajes y que permita incorporar caractersticas como imagen, y un botn de "Ver ms", ms administrable (con posibilidades de cambiar la leyenda y un cono en el botn). 

 Tambin se abre la posibilidad para incorporar otros tipos de mensajes que podrn verse por ejemplo en "la nube de donaciones (eatcloud)" cuando ocurra un evento en particular (por ejemplo, que no hallan donaciones disponibles o: "dona_not_available". 

 Las mejoras en este sentido tambin abren las posibilidades para incorporar mensajes que solo se vean en un pas en particular (empezando por Colombia: co), y tambin de programar fechas de inicio y fin de las publicaciones (algo que se podr implementar a futuro). 

 Consulta de los anuncios disponibles para el dashboard de gestor de donaciones (doma_dashboard) ***Revisar dinamismo a partir de _DOM.cua_master y _DOM.cua_master_country*** 
 La App debe consultar en primera instancia el tomar el dato _DOM. cua_master_country (que se obtuvo en los procesos de autenticacin ): 
 https://beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_cua=abaco 

 Como el llamado devuelve esta informacin: 
 { 
 ts : "200430155656", 
 op : true, 
 cont : 1, 
 res :  
 [ 
 { 
 _id : "1", 
 eatc_cua : "abaco", 
 eatc_country : "co" 
 } 
 ], 
 mem : 0.39, 
 time : "00:00:00" 
 } 

 Se toma como eatc_country a " co " y se procede a llamar el mensaje que para el pas est dispuesto para desplegarse en el dashboard ( doma_dashboard ) 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_messages? eatc_message_type=doma_dashboard & eatc_country= {{_DOM. cua_master_country }}&eatc_doma_code=_*  

 Por ejemplo para el ambiente de pruebas y _DOM. cua_master=abaco la consulta sera: 
 https://devbeneficiarios.eatcloud.info/api/abaco/eatc_doma_messages? eatc_message_type=doma_dashboard & eatc_country= co&eatc_doma_code=_* 

 El API devuelve la siguiente respuesta: 
 { 
 _id : "1", 
 code : "1", 
 date : "2020-04-29", 
 title : "ESTAMOS TRABAJANDO PARA TENER MS DONANTES!", 
 message : ""En EatCloud hacemos grandes esfuerzos para incrementar nuestra red de donantes y queremos contar con tu colaboracin. Haz clic en el botn ""+"" y aydanos a difundir el mensaje"", 
 url : " https://www.instagram.com/tv/B_ivcGaj0N8/?igshid=jz9zl3klnkuf ", 
 eatc_doma_code : "_all", 
 order : "1", 
 eatc_message_type : "doma_dashboard", 
 display_conditions : "always", 
 display_time_sec : "fix", 
 url_button_legend : "Ver ms", 
 url_button_icon : "", 
 image_url : "", 
 eatc_country : "co", 
 published_since : "2020-04-29", 
 published_until : "" 
 } 

 A continuacin se dan lineamientos generales para disponer el mensaje de acuerdo a la informacin que trae el API: 
 eatc_message_type, eatc_country,eatc_doma_code 

 Posteriormente se podr realizar un llamado para el gestor de donacin especfico, a fin de mostrar mensajes solo para ellos. 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_doma_messages?eatc_doma_code={{eatc_users. organizacion }}  

 _id, code, date: 

 Son datos informativos que permiten diferenciar el mensaje.  Por el momento no se muestran en la interfaz del usuario. 

 title 
 Sirve para pintar el ttulo del mensaje. 

   message 
 Sirve para pintar el cuerpo del mensaje. 

 url 
 URL que se abrir al presionar el botn respectivo (que en la primera versin fue un "+" en un crculo, pero que en versiones posteriores evolucionar a un botn con un letrero y posiblemente un cono (ambos administrables) en su interior. 

 url_button_legend : ejemplo: "Ver ms". 

 Corresponde a la leyenda del botn que abre la URL.  Si por ejemplo en este campo se configura en vez de un letrero el parmetro " _message ", esto quiere decir que el mismo mensaje ser el botn para abrir la URL respectiva y no habr un botn adicional (es decir el botn adicional se debe ocultar). 

 url_button_icon : "", 

 En futuras versiones se podr incorporar un pequeo cono para el botn el cual se podr desplegar desde una URL particular, con el nimo de hacerlo administrable. 

 image_url 

 En futuras versiones se podr incorporar una imagen al mensaje.  Esta imagen se obtendr de la URL registrada en este campo. 

 order 

 En futuras versiones en este espacio se podrn mostrar varios mensajes en forma de "sliders".  Este campo servir para establecer el orden en que se muestran estos mensajes. 

 display_conditions : ejemplo: "always" 

 En futuras versiones, se podrn establecer condiciones de visualizacin de los mensajes (esto funciona ms en el nuevo espacio que se abrir en la nube de donaciones ).  Como en este caso el parmetro indica "always", esto indica que siempre se visualiza el mensaje en este punto. 

 display_time_sec : "fix", 

 En futuras versiones, se podrn establecer el tiempo en segundos de la visualizacin de un mensaje (antes de pasar a otro) o antes de por ejemplo abrir otra funcionalidad (lo que funciona ms para la nube de donaciones ).  Como en este caso se informa que el mensaje estar fijo ("fix") esto querr decir que el mensaje no rotar, ni tendr un tiempo de visualizacin. 

 published_since, published_until : 
 En futuras versiones, se podr establecer tiempos de inicio y fin de la publicacin para establecer cuando se comienza a mostrar y cuando se termina de mostrar un mensaje. 

 Card Tus mtricas: 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el mes en curso 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el ao en curso 

 #KPI de impacto social 
 kg = eatc_dona_headers .eatc-total_weight_kg 

 Indicadores Clave: 

 Impacto social: muestra el total de kilogramos donados por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 

 #KPI de impacto social 
 kg = eatc_dona_headers .eatc-total_weight_kg 

 Impacto econmico: muestra el total de dinero ahorrado por cuenta de las donaciones  por parte del punto de donacin ( eatc_pods ), es decir la sumatoria de todos los ahorros y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 

 #KPI de impacto econmico 
 logistics_cost_savings = eatc_dona_headers .eatc-total_weight_kg * [] //Ahorro Almacenamiento: por KG semana: Fro =$394; Seco = $289 
 transport_cost_savings =  eatc_dona_headers .eatc-total_weight_kg * 79 //Ahorro Transporte: por KG =$79 
 waste_management_savings =  eatc_dona_headers .eatc-total_weight_kg * 1105//Ahorro Gestin de residuos: por KG =$1105 

 #KPI de ahorro tributario: 
 income_tax_savings = eatc_dona_headers .eatc-total_cost * 1,25//Beneficio en renta: por cada peso donado se retornan: $1,25 
 vat_savings = eatc_dona_headers .eatc-total_cost * 0,19//Beneficio IVA: por cada peso donado se retornan: =$0,19 

 Impacto ambiental: muestra el total de las emisiones de C02 ahorradas por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ). 

 #KPI de impacto ambiental 
 CO2_tons = eatc_dona_header.eatc-total_weight_kg * [] 

 Tablero de liderazgo 
 El dashboard presentar un "Tablero de Liderazgo" en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso 

 ***NUEVO: FORMULARIO NET PROMOTER SCORE **** 

 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio: 

 {{URL_entorno_datagov}}/int/eatcloud/int_nps_eatcloud?eatc_cua={{_DOM. cua_user }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= app_beneficiarios &eatc_enviroment={{ eatc_enviroment }} 

 Los parmetros para realizar la consulta son los siguientes: 

 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 

 eatc_user_code 
 Corresponde al parmetro "identificador_unico_registro" del gestor del donaciones que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/eatc_donation_managers?_id={{_id}} 

 eatc_plataform 
 app_beneficiarios (constante para este llamado) 

 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser: pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser: prod 

 Si el servicio responde de manera negativa, no se despliega el formulario. 

 Si el servicio responde de manera afirmativa se desplegar el formulario respectivo. 

 Despliegue del formulario 
 El formulario se deber desplegar segn su definicin y los mecanismos de integracin que se provean para este fin.  Se debe mirar si se despliega como un modal (que tendr dos formularios sucesivos adentro), en la parte superior de la pantalla o en la parte inferior de la  
 pantalla. 

 Registro del NPS ( nps_main_question ) 

 Edicin  del NPS ( nps_secondary_question ) 

 Llamado para el registro del NPS ( nps_main_question ) ***NUEVO*** adicin de parmetros de clasificacin (se resaltan en rojo) 

 Se deber realizar el siguiente llamado para realizar el registro del NPS 

 https://datagov.eatcloud.info/crd/eatcloud/?_tabla=int_nps_eatcloud&eatc_cua={{ eatc_donation_managers .organizacin }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= app_beneficiarios &eatc_enviroment={{ eatc_enviroment }}&nps={{ entero_de_0_a_10 }} & eatc_vertical ={{ eatc_donation_managers .tipo_organizacion }}& eatc_cua_size ={{ eatc_donation_managers .eatc_doma_typology_b }}& eatc_licence_type ={{ eatc_donation_managers . eatc_licence_type }} &_operacion= insert 

 Los parmetros para realizar la consulta son los siguientes: 

 eatc_donation_managers.organizacin 
 Corresponde al nombre ( eatc_donation_managers .organizacin ) del gestor de donaciones  

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/ eatc_donation_managers?_id={{eatc_donation_managers._id}} 

 eatc_user_code 
 Corresponde al parmetro "eatc_users. correo_electronico " del usuario del gestor del donaciones que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/ eatc_users ? organizacion ={{ eatc_donation_managers .identificador_unico_registro }} 

 eatc_plataform 
 app_beneficiarios (constante para este llamado) 

 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser: pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser: prod 

 entero_de_0_a_10 
 input del formulario respectivo 

 eatc_vertical 
 Corresponde al parmetro eatc_donation_managers .tipo_organizacion del beneficario ({{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers ?_id={{_id}} 

 eatc_cua_size 
 Corresponde al parmetro eatc_donation_managers .eatc_doma_typology_b del beneficiario ({{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers ?_id={{_id}} 

 eatc_licence_type 
 Corresponde al parmetro eatc_donation_managers . eatc_licence_type del beneficiario ({{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers ?_id={{_id}} (es un campo que aun no existe por lo tanto se enva inicialmente en blanco, pero se debe crear el nuevo campo en las tablas de eatc_donation_managers) 

 Llamado para la edicin  del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 

 https://datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id={{_id}}&lang={{ iso2_idioma }}&plataforma= app_beneficiarios &nps_secundary_answer={{ text_input }}&_operacion= update 

 Este llamado se debe realizar cuando se oprime el botn cuyo label es " nps_submit_btn " . 
 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .  Si no se encuentra registrado por defecto se enviar " en ") 

 eatc_plataform 
 app_beneficiarios (constante para este llamado) 

 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal-eatc_doma_dsh%2F2416948924-4-dashboard-de-beneficiario--eatc_doma_dsh-.png&ow=750&oh=1992, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal-eatc_doma_dsh%2F2416948924-4-dashboard-de-beneficiario--eatc_doma_dsh-.png&ow=750&oh=1992 
 EatCloud Beneficiarios 

 514.000000000000 

 DASHBOARD PRINCIPAL: EATC_DOMA_DSH