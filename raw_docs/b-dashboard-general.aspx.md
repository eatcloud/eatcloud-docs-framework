# b-dashboard-general.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 I NDICADORES CLAVE: 
 Mediante cuatro pestaas presenta los principales indicadores por tipo de indicador, y el botn (+) que da acceso a la funcionalidad: detalle de KPI . El valor por defecto ser el mes en curso, pero se podrn ingresar fecha inicial y fecha final para ajustar los clculos presentados en el dashboard. Las pestaas son las siguientes: 

 I NDICADORES PRINCIPALES PRIORITARIOS: 
 Impacto Social 
 Muestra el total de Kilogramos recibidos por los eatc_donation_managers  (segn el cua_user de la URL de ingreso, que en este momento siempre ser ABACO, pero en el futuro pueden haber nuevas cuentas de beneficiarios) 

 KPI KG ENTREGADOS (antes de realizar esto debe realizarse esta tarea: https://app.asana.com/0/698639369029630/1171297969708779 dado que solo se est generando los KPIs del Exito y se necesitan activar todas las dems cuentas) 
 Para realizar el clculo se debe invocar el API :   

 Por almacn o grupo de almacenes: ejemplo: https://donantes.eatcloud.info/api/[cua]/eatc_dona_kpi?kpi=kg (para el caso de abaco la consulta es: https://donantes.eatcloud.info/api/abaco/eatc_dona_kpi?kpi=kg   

 Se toma el dato " value " y realiza una sumatoria 

 KPI RACIONES: 
 Indicadores de proceso : 
 Muestra el total anuncios gestionados por el o los puntos de donacin ( eatc_pods : segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_process_kpi ) 

 KPI Nmero Total de Anuncios 
 Para realizar el clculo se debe invocar el API:  
 Total: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=_*&_compress   

 Se toma el dato " cont " que entrega el API y se pinta en la tarjeta. En adelante se toma el Numero Total de Anuncios para el clculo de otros indicadores 

 KPI KG MOVIDOS 
 Sumatoria del parmetro eatc-total_weight_kg de los registros de la siguiente consulta 
 Total: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=_*&_compress   

 En adelante se toman los KG Movidos para el clculo de otros indicadores. 

 APROVECHAMIENTO EN NMERO DE ANUNCIOS: 
 KPI Nmero de anuncios entregados sobre Nmero Total de Anuncios 
 Como numerador se toma el siguiente dato " cont ". de la siguiente consulta 
 Anuncios entregados: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=delivered, received,pre-certified,certified&_compress   

 El denominador ser  el Numero Total de Anuncios 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Nmero de anuncios entregados sobre Nmero Total de Anuncios ltimo mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Nmero de anuncios entregados sobre Nmero Total de Anuncios ltima semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 APROVECHAMIENTO EN KG: 
 KPI Porcentaje de KG entregados sobre KG Movidos 
 Como numerador se toma la s umatoria del parmetro eatc-total_weight_kg de los registros de la siguiente consulta: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=delivered, received,pre-certified,certified 

 El denominador sern  los KG Movidos 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Porcentaje de KG entregados sobre KG Movidos ltimo mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Porcentaje de KG entregados sobre KG Movidos ltima semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 NO ENTREGA EN NMERO DE ANUNCIOS: 
 KPI Porcentaje de anuncios no entregados sobre el nmero total de anuncios 
 Como numerador se toma el siguiente dato " cont ". de la siguiente consulta 
 Anuncios entregados: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=not_delivered &_compress   

 El denominador ser  el Numero Total de Anuncios 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Porcentaje de anuncios no entregados sobre el nmero total de anuncios ltimo Mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Porcentaje de anuncios no entregados sobre el nmero total de anuncios ltima Semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 NO ENTREGA EN KG: 
 KPI Porcentaje de KG no entregados sobre KG Gestionados Total 
 Como numerador se toma la s umatoria del parmetro eatc-total_weight_kg de los registros de la siguiente consulta: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=not_delivered 

 El denominador sern  los KG Movidos 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Porcentaje de KG no entregados sobre KG Gestionados ltimo mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Porcentaje de KG no entregados sobre KG Gestionados ltima semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 CANCELADOS EN NMERO DE ANUNCIOS: 
 KPI Porcentaje de anuncios cancelados sobre el nmero total de anuncios 
 Como numerador se toma el siguiente dato " cont ". de la siguiente consulta 
 Anuncios entregados: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=cancelled &_compress   

 El denominador ser  el Numero Total de Anuncios 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Porcentaje de anuncios cancelados sobre el nmero total de anuncios ltimo Mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Porcentaje de anuncios cancelados sobre el nmero total de anuncios ltima Semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 CANCELADOS EN KG: 
 KPI Porcentaje de KG no entregados sobre KG Gestionados Total 
 Como numerador se toma la s umatoria del parmetro eatc-total_weight_kg de los registros de la siguiente consulta: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers? eatc-state=cancelled   

 El denominador sern  los KG Movidos 

 El dato se muestra como porcentaje (multiplicado por 100) 

 KPI Porcentaje de KG no entregados sobre KG Gestionados ltimo mes 
 Corresponde al mismo indicador, pero tomando solo los anuncios del ltimo mes 

 KPI Porcentaje de KG no entregados sobre KG Gestionados ltima semana 
 Corresponde al mismo indicador, pero tomando solo los anuncios de la ltima semana 

 GESTORES DE DONACIONES: 
 NMERO DE GESTORES REGISTRADOS: 
 Se toma el dato " cont ". de la siguiente consulta: https://beneficiarios.eatcloud.info/api/[cua_user]/eatc_donation_managers?_id=_*&_compress 

 Es decir que para el BO de abaco ( https://beneficiarios.eatcloud.info/bo/abaco ) la consulta es: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=_*&_compress    

 Abajo de este indicador, debe haber un botn de "descargar registros" que permita descargar todos los Gestores de Donaciones de la CUA respectiva (en este caso ABACO: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?_id=_ * ) 

 ACTIVOS: 
 Nmero de gestores de donaciones activos 
 Se toma el dato " cont ". de la siguiente consulta: https://beneficiarios.eatcloud.info/api/[cua_user]/eatc_donation_managers?eatc_state=activo&_compress 

 Es decir que para el BO de abaco ( https://beneficiarios.eatcloud.info/bo/abaco ) la consulta es: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?eatc_state=activo&_compress   

 Gestores activos como porcentaje de activos con respecto al total 
 Como numerador se toma el siguiente Nmero de gestores de donaciones activos 

 El denominador ser  el NUMERO DE GESTORES REGISTRADOS 

 El dato se muestra como porcentaje (multiplicado por 100) 

 INACTIVOS: 
 Nmero de gestores de donaciones inactivos 
 Se toma el dato " cont ". de la siguiente consulta: https://beneficiarios.eatcloud.info/api/[cua_user]/eatc_donation_managers?eatc_state=inactivo&_compress 

 Es decir que para el BO de abaco ( https://beneficiarios.eatcloud.info/bo/abaco ) la consulta es: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?eatc_state=inactivo&_compress   

 Gestores inactivos como porcentaje del total 
 Como numerador se toma el siguiente Nmero de gestores de donaciones inactivos 

 El denominador ser  el NUMERO DE GESTORES REGISTRADOS 

 El dato se muestra como porcentaje (multiplicado por 100) 

 SUSPENDIDOS: 
 Nmero de gestores de donaciones suspendidos  
 Se toma el dato " cont ". de la siguiente consulta: https://beneficiarios.eatcloud.info/api/[cua_user]/eatc_donation_managers?eatc_state=suspendido,persona_natural&_compress 

 Es decir que para el BO de abaco ( https://beneficiarios.eatcloud.info/bo/abaco ) la consulta es: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?eatc_state=suspendido,persona_natural&_compress     

 Gestores suspendidos como porcentaje del total 
 Como numerador se toma el siguiente Nmero de gestores de donaciones suspendidos 

 El denominador ser  el NUMERO DE GESTORES REGISTRADOS 

 El dato se muestra como porcentaje (multiplicado por 100) 

 BENEFICIARIOS FINALES: 
 Count de la siguiente consulta: https://beneficiarios.eatcloud.info/api/[cua_user]/eatc_final_beneficiaries_lt?_id=_*&_compress 

 Es decir que para el BO de abaco ( https://beneficiarios.eatcloud.info/bo/abaco ) la consulta es: https://beneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?_id=_*&_compress   

 Abajo de este indicador, debe haber un botn de "descargar registros" que permita descargar todos los beneficiarios de la CUA respectiva (en este caso ABACO: https://beneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?_id=_* ) 

 PUNTOS DE DONACIN: 
 Count de la siguiente consulta: https://donantes.eatcloud.info/api/allpods/eatc_pods?eatc-country=CO&_compress 

 Abajo de este indicador, debe haber un botn de "descargar registros" que permita descargar todos los beneficiarios https://donantes.eatcloud.info/api/allpods/eatc_pods?eatc-country=CO   

 Otros indicadores de impacto: 
 Impacto econmico : 
 Muestra el total de ahorros generados por el o los puntos de donacin ( eatc_pods : segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI  ( eatc_pods_economic_impact_kpi ) 

 KPI total ahorros 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]:   
   https://donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Economic%20impact&eatc-pod_id=_* 

 Se toma el dato " value " y realiza una sumatoria 

 Impacto ambiental :  
 Muestra el total de toneladas de CO2  ahorradas por el o los puntos de donacin ( eatc_pods : segn perfil del usuario) o sus diferentes tipologas y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_enviromental_impact_kpi ) 

 KPI toneladas de CO2 [PENDIENTE POR REVISAR] 
 Para realizar el clculo se debe invocar el API [REVISAR CUANDO SE TENGAN LOS OBJECT STORES DE CONSOLIDACIONES]:   
 https://donantes.eatcloud.info/api/abaco/eatc_dona_kpi?eatc-kpi_type=Environmental%20impact&eatc-pod_id=_*    

 Se toma el dato " value " y realiza una sumatoria 

 Crecimiento del nmero de donaciones en el tiempo 
 Grfico de lnea de tiempo en donde se muestre el crecimiento del nmero de donaciones gestionadas y entregadas acumuladas en el tiempo 

 Crecimiento de KG entregados en el tiempo 
 Grfico de lnea de tiempo en donde se muestre el crecimiento los KG Movidos y entregados acumulados en el tiempo 

 T ABLERO DE LIDERAZGO 
 El dashboard presentar un "Tablero de Liderazgo" en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso. 

 ***NUEVO: FORMULARIO NET PROMOTER SCORE **** 
 Llamado del servicio 
 Se deber integrar la funcionalidad de NPS , en el dashboard principal del BO. Por lo tanto se debern realizar los siguientes llamados para desplegar y posteriormente realizar los registros del servicio: 

 https://datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua={{_DOM. cua_user }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= beneficiarios &eatc_enviroment={{ eatc_enviroment }} 

 Los parmetros para realizar la consulta son los siguientes: 

 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario (generalmente se guarda en _DOM. cua_user ) 

 eatc_user_code 
 Corresponde al parmetro "usuario" del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/bo_usuarios?id={{id}} 

 eatc_plataform 
 beneficiarios (constante para este llamado) 

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

 https://datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_cua={{_DOM. cua_user }}&eatc_user_code={{ eatc_user_code }}&eatc_plataform= beneficiarios &eatc_enviroment={{ eatc_enviroment }}&nps={{ entero_de_0_a_10 }}&_operacion= insert 

 Los parmetros para realizar la consulta son los siguientes: 

 _DOM.cua_user 
 Corresponde al nombre de la cuenta de usuario desde la cual se dispone el BO 

 eatc_user_code 
 Corresponde al parmetro "usuario" del usuario que se encuentra logueado en la plataforma y que podra consultarse con la siguiente consulta: 

 {{URL_entorno_beneficiarios}}/api/{{_DOM.cua_master}}/bo_usuarios?id={{id}} 

 eatc_plataform 
 beneficiarios (constante para este llamado) 

 eatc_enviroment 
 Si se trabaja en ambiente de pruebas el valor enviado ser: pruebas 
 Si se trabaja en ambiente productivo el valor enviado ser: prod 

 entero_de_0_a_10 
 input del formulario respectivo 

 Llamado para la edicin  del NPS ( nps_secondary_question ) 
 Para hacer el registro se deber disponer un servicio que reciba los siguientes parmetros 

 https://datagov.eatcloud.info/int/eatcloud/int_nps_eatcloud?eatc_nps_registry_id={{_id}}&lang={{ iso2_idioma }}&plataforma= beneficiarios &nps_secundary_answer={{ text_input }}&_operacion= update 

 Este llamado se debe realizar cuando se oprime el botn cuyo label es " nps_submit_btn " . 

 lang 
 lenguaje de la plataforma (iso2) debe estar registrado en esta tabla https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* .  Si no se encuentra registrado por defecto se enviar " en ") 

 eatc_plataform 
 beneficiarios (constante para este llamado) 

 nps_secundary_answer 
 Tex input del formulario respectivo 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-dashboard-general%2F1530596569-EmbeddedImage--72-.jpg&ow=1280&oh=262, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-dashboard-general%2F1530596569-EmbeddedImage--72-.jpg&ow=1280&oh=262 

 585.000000000000 

 DASHBOARD GENERAL (BO BENEFICIARIOS)