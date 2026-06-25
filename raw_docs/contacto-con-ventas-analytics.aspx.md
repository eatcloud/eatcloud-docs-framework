# contacto-con-ventas-analytics.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante para el desarrollo 
 El siguiente wireframe, fue desarrollado inicialmente para confirmacin de pedido de licencias rescate, pero basndonos en el diseo (que no est corregido en este aspecto) se resaltarn en AZUL , nuevos llamados a API y consideraciones para adaptar el desarrollo realizado inicialmente para las licencias rescate, pero para las licencias analytics. 

 En esta pantalla se presentar un resumen de la informacin del cliente, su plan actual, sus particularidades (principalmente que no le permiten acceder a un precio de lista) y el nuevo plan al que se quiere acceder.  Posteriormente con estos datos, se crear un "Deal" en el CRM, para que con esta herramienta se genere la interaccin comercial necesaria.  La informacin necesaria para pintar las diferentes cards, se ha detallado cmo se obtiene en las funcionalidades " Informacin planes " y " Resumen pedido " y por lo tanto en esta funcionalidad no se vuelve a detallar, solamente de define como han sido llamadas las variables en las anteriores funcionalidades. 

 El wireframe propuesto es: 

 C ONTATAR A VENTAS 
 class= lbl_contactar_a_ventas ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_contactar_a_ventas ) 

 Tus datos 
 class= lbl_tus_datos ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_tus_datos )  
 eatc_customer. eatc_fiscal_name 
 eatc_customer. eatc_fiscal_id 
 eatc_customer. eatc_email 
 eatc_customer. eatc_phone 
 eatc_customer. eatc_city 
 eatc_customer. eatc_country 
 eatc_customer. crm_id 

 Tus plan actual 
 class= lbl_tu_plan_actual ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_tu_plan_actual )  

 {{ nombre_del_plan_analytics_actual }} 

 Puntos de donacin 
 class= lbl_pods ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_pods )  

 {{ pods_activos }}   

 KG Gestionados en el ltimo mes: 
 class= lbl_kg_gestionados_ultimo_mes ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_kg_gestionados_ultimo_mes )   

 {{ kg_gestionados_ultimo_mes }} 

 Deseo pasarme a: 
 class= lbl_deseo_pasarme_a ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_deseo_pasarme_a )   

 {{ nombre_del_nuevo_plan_analytics }} => Selector 

 En una primera etapa se debe implementar solamente el nombre del plan seleccionado anteriormente (en la vista de informacin de plan) y luego se implementar un selector para poder cambiar aqu ese plan. 

 Observaciones adicionales: 
 class= lbl_obs_adicionales ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_obs_adicionales )  

 Cuadro de texto (opcional) 

 Lo que se ingrese de manera opcional se debe llevar a la variable  

 {{obs_adionales}} 

 Botn:  Enviar 
 class= lbl_enviar ( https://dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&lang=_*&pais=_*&idlabel= lbl_enviar )  

 Al accionar este botn se dispara la integracin con el Deal en el CRM (documentacin: https://developers.freshworks.com/crm/api/#create_deal ) 

 Validacin previa de la existencia de la cuenta (cliente) en el CRM 
 Antes de realizar la creacin del " Deal ", se debe proceder a utilizar el siguiente llamado CURL para verificar que la cuenta (cliente) exista en el CRM: 

 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json " -X GET " https://eatcloud-team.myfreshworks.com/crm/sales /api/sales_accounts/{{eatc_customer. crm_id }} " 

 Si el cliente  (cuenta) no existe en el CRM, se debe proceder a realizar el respectivo llamado al servicio de integracin ( verificarlo por favor con Jess )  
 token= REDACTED 

 Llamado al API del CRM para la creacin del "deal" 
 Si el cliente existe en el CRM, se deben enviar al API de integracin con el CRM los siguientes datos, segn la documentacin ( https://developers.freshworks.com/crm/api/#deals )  deben tener una estructura como la siguiente (se realizar referencia a las variables consultadas anteriormente): 

 nombre_deal 
 Ser igual a la concatenacin de lo siguiente: 
 {{eatc_customer. eatc_fiscal_name }} : actualizacin licencia analytics de {{nombre_del_plan_analytics_actual}} a {{nombre_del_nuevo_plan_analytics}} 

 amount 
 Ser igual a la multiplicacin del nmero de pods activos por el precio de lista de la licencia escogida ,es decir el precio que se obtiene tras hacer la siguiente consulta: 
 {{precio}} = {{precio}} ={{ URL_entorno_datagov }}/api/eatcloud/ eatc_licenses_prices ?country= co &cua_type_period={{eatc_cua. type_period }}& analytics_licence_code ={{eatc_details_of_analytics_licenses. eatc_licence_code }}&_distinct= default_price 

 amount = {{pods_activos}}* {{precio}} ( decimal (15,2) ) 

 Sobre el objeto "custom_field" 
 En la siguiente documentacin si incluye el objeto "custom_field", a saber 
 "custom_field":{"cf_puntos_conectados":[[ pods_activos ]], "cf_responsable":" Isis y Simn ","cf_vertical":[[eatc_cua .vertical ]], "cf_licencias_rescate":[[ nombre_del_nuevo_plan ]],"cf_observaciones":[[ obs_adionales ]]} 

 El mismo se construye con datos de la cuenta (por ejemplo: eatc_cua. vertical ) e informacin se se construye para llegar a esta funcionalidad o mediante la misma funcionalidad (como por ejemplo: nombre_del_nuevo_plan y obs_adionales ). Si el llamado al API no funciona con ese objeto se debe dejar planteado para futuras revisiones (dado que los campos "custom" requieren de una configuracin previa en el CRM, que ya se realiz pero no se ha probado). 

 cURL 
 curl -H "Authorization: Token token= REDACTED " -H "Content-Type: application/json" -d '{"deal":{"name":" nombre_deal ", "amount": amount , "sales_account_id": [[eatc_customer. crm_id ]] , "created_at": [[ datetime_stamp ]]   
 "custom_field":{"cf_puntos_conectados":[[ pods_activos ]], "cf_responsable":" Isis y Simn ","cf_vertical":[[eatc_cua .vertical ]], "cf_licencias_rescate":[[ nombre_del_nuevo_plan ]],"cf_observaciones":[[ obs_adionales ]]} }}' -X POST "https:// https://eatcloud-team.myfreshworks.com /crm/sales/api/deals" 

 Nota para la implementacin: el llamado cURL no estaba presente en la documentacin , as que el mismo se document abstrayendo de otro llamado similar.  Por ese motivo se deber probar si el llamado funciona y de no funcionar revisar con llamados cURL documentados en otras partes de la API. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcontacto-con-ventas-analytics%2F551949355-contactar_a_ventas--1-.jpg&ow=500&oh=620, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcontacto-con-ventas-analytics%2F551949355-contactar_a_ventas--1-.jpg&ow=500&oh=620 

 495.000000000000 

 CONTACTO CON VENTAS ANALYTICS