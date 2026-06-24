# dashboard-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 https://datagov.eatcloud.info/bo/{{cua_user}} 

 Pendiente de definicin sobre este dashboard, pero se pretende que a futuro en l se muestren estadsticas de la operacin, de tal manera que esta plataforma en algn punto reemplace a la plataforma BO que reside en el entorno donantes. 
 Nota importante de implementacin: en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 ID Funcionalidad 
 dsh_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_funcionalidades?idfuncionalidad= dsh_datagov_cua ) 

 Label Botn Men: 
 lb_btn_dsh_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_dsh_datagov_cua ) 

 Label Ttulo de la Vista: 
 lb_dsh_datagov_cua (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_dsh_datagov_cua ) 

 Label Descripcin de la Vista: 
 lb_dsh_datagov_cua_desc (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_dsh_datagov_cua_desc ) 

 C ARRUSEL CON INFORMACIN IMPORTANTE 

 Descripcin tcnica: 
 El carrusel del presente onboarding, compuesto por los  mensajes que se dispongan en el respectivo object store y que se dispondrn en secuencia segn el orden registrado en dicho repositorio de informacin; se debern presentar la primera vez que el usuario ingresa a la app. Por lo tanto cuando se realice este ingreso por primera vez, la app deber guardar una variable de control que permita establecer si el usuario est ingresando por primera vez (cuando esa variable no exista) y en consecuencia se muestre el carrusel, o si no es la primera vez que ingresa (first_admision) (cuando la variable est almacenada) y por lo tanto no se le despliega el carrusel. 

 El ttulo, la imagen y el texto de estos mensajes se cargarn de manera dinmica desde la siguiente persistencia: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country={{actual_contry}} 

 Para el caso inicial de Colombia (co) , la consulta sera la siguiente 

 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country=co   

 Persistencia de la lectura de los mensajes 
 Tan pronto el usuario lea un mensaje, el sistema debe guardar un registro de dicha lectura (en una tabla almacenada en cada la base de datos de cada cuenta de usuario), de tal manera que el sistema pueda determinar si existen mensajes disponibles que no hallan sido leidos, y estos son los que debe priorizar en cuanto a visualizacin, sobre los que ya han sido ledos.  En ese orden de ideas el ordenamiento de los mensajes se debe dar por "no visualizados" => "orden entre los no visualizados" => "visualizados2 => "orden visualizados". 

 Onboarding 1 
 Teniendo en cuenta la informacin que arroja la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country={{actual_contry}}& order=1  

 Para el caso inicial de Colombia (co) , la consulta sera la siguiente 

 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country=co& order=1    

 De la siguiente manera: 
 Imagen superior: se debe traer de la URL registrada en el campo image_url 
 Ttulo del mensaje: segn el dato que trae el parmetro: title 
 Cuerpo del mensaje: segn el dato que trae el parmetro: message 

 La dems informacin por el momento no se utilizar en esta implementacin, pero a futuro podrn hacerse mejoras que manejen dichos datos. 

 Onboarding 2 
 Teniendo en cuenta la informacin que arroja la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country={{actual_contry}}& order=2 

 Para el caso inicial de Colombia (co) , la consulta sera la siguiente 

 https://datagov.eatcloud.info/api/eatcloud/eatc_messages?eatc_message_type= cua_onboarding &eatc_country=co& order=2     

 De la siguiente manera: 
 Imagen superior: se debe traer de la URL registrada en el campo image_url 
 Ttulo del mensaje: segn el dato que trae el parmetro: title 
 Cuerpo del mensaje: segn el dato que trae el parmetro: message 

 La dems informacin por el momento no se utilizar en esta implementacin, pero a futuro podrn hacerse mejoras que manejen dichos datos. 
 Y as sucesivamente de acuerdo a la cantidad de mensajes que se guarden en el repositorio (para efectos del ejemplo de la documentacin en el momento se manejan solo tres mensajes). 

 Cuando se termine esta secuencia de manera ideal se debe direccionar a la funcionalidad para agregar puntos de donacin en la plataforma de cuentas en datagov y tambin como se tienen todos los datos necesarios, se debern disparar procesos para enviar informacin al ERP y CRM y tambin para generar (en la medida de las posibilidades) de manera automtica los cronjobs que deben crearse una vez se cree cada cuenta. 

 ***NUEVO: FORMULARIO NET PROMOTER SCORE **** 
 Determinacin si la cuenta / app se le despliega o no el NPS 

 Antes de realizar el llamado al servicio se debe determinar si la plafaforma, para la cuenta especfica, tiene bloqueado o no la funcionalidad.  Para hacerlo se deber realizar el siguiente llamado 
 {{ URL_entorno_datagov }}/api/eatcloud/nps_block?eatc_cua={{_DOM. cua_user }}&eatc_plataform={{ eatc_platforms. eatc_code }}&eatc_enviroment={{ eatc_enviroment }} 

 Si el llamado trae un dato vlido, entonces no se despliega el llamado al servicio y por lo tanto no se despliega el formulario de NPS 
 Ejemplo: ambiente productivo, webapp, exito 

 El sistema debe realizar el siguiente llamado: 
 https://datagov.eatcloud.info/api/eatcloud/nps_block?eatc_cua=exito&eatc_plataform= webapp &eatc_enviroment=prod   

 Como el llamado muestra una respuesta vlida, entonces no se despliega el servicio 

 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio: 
 {{ URL_entorno_datagov }}/int/eatcloud/int_nps_eatcloud?eatc_cua={{_DOM. cua_user }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= datagov_cuentas &eatc_enviroment={{ eatc_enviroment }} 

 Los parmetros para realizar la consulta son los siguientes: 

 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 
 eatc_user_code 
 Corresponde al parmetro "usuario" del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_user}}/bo_usuarios?_id={{id}} 

 eatc_plataform 
 datagov_cuentas (constante para este llamado) 

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

 Llamado para el registro del NPS ( nps_main_question ) 
 Se deber realizar el siguiente llamado para realizar el registro del NPS 
 https://datagov.eatcloud.info/api/eatcloud/int_nps_eatcloud?eatc_cua={{_DOM. cua_user }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= datagov_cuentas &eatc_enviroment={{ eatc_enviroment }}&nps={{ entero_de_0_a_10 }}&_operacion= insert 

 Los parmetros para realizar la consulta son los siguientes: 

 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 

 eatc_user_code 
 Corresponde al parmetro "usuario" del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_user}}/bo_usuarios?id={{id}} 

 eatc_plataform 
 datagov_cuentas (constante para este llamado) 

 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser: pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser: prod 

 entero_de_0_a_10 
 input del formulario respectivo 

 Llamado para la edicin  del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 
 https://datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id={{_id}}&lang={{ iso2_idioma }}&plataforma= datagov_cuentas &nps_secundary_answer={{ text_input }}&_operacion= update 

 Este llamado se debe realizar cuando se oprime el botn cuyo label es " nps_submit_btn " . 

 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .  Si no se encuentra registrado por defecto se enviar " en ") 

 eatc_plataform 
 datagov_cuentas (constante para este llamado) 

 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-datagov%2F436117705-EmbeddedImage--64-.jpg&ow=1280&oh=744, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-datagov%2F436117705-EmbeddedImage--64-.jpg&ow=1280&oh=744 

 445.000000000000 

 DASHBOARD CUENTAS DATAGOV