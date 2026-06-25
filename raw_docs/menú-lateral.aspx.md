# menú-lateral.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En la parte izquierda de la pantalla debe existir un menú que se colapse hacia el lado derecho, y que contiene lo siguientes items, que dan acceso a las funcionalidades (que se vinculan desde sus nombres) de la presente plataforma datagov/bo. Cuando el elemento del menú posea una alerta (como se describirá abajo) al posar el mouse sobre la misma, se deberá desplegar un tootip de alerta, que abajo se detalla para cada caso en dónde puede aplicar. 

 Título de la plataforma e identificación básica del usuario = DEPRECADO 

 EatCloud 
 Al colapsar el menú, se debe reemplazar la plalabra EatCloud, por el Ícono en fondo blanco (tal como está funcionando en este momento)Ícono, Nombre del usuario y Nombre de la empresa 
 Se desplegará un Ícono o logo de la cuenta (que en una etapa posterior se solicitará como dato adicional para la configuración de la cuenta) y los datos del nombre del usuario que se encuentra autenticado en la plataforma y el nombre de la compañía.&#160; Cuando se colapse el menú, solamente se mostrará el logo o ícono. 
 Icono 
 Cuando no existe un ícono por defecto, al hacerle clic sobre la imagen, se debe abrir un formulario que permita subir una imagen a la plataforma. 
 Que tenga los siguientes datos&#58; Que tenga los siguientes datos&#58; 
 Título del formulario &#58; &quot;Sube el logotipo de tu organización&quot; class=&quot; lbl_sube_logo &quot; 
 Descripción del formulario &#58; &quot;Aquí podrás subir un logotipo de tu organización (en formato .png, .jpg, .jpeg, .gif de no más de 2 megas de peso), que ayudará a personalizar tu presencia en la plataforma EatCloud&quot; class=&quot; lbl_sube_logo_desc &quot; 
 Selector de archivos &#58; placeholder &quot;Selecciona el archivo a subir&quot; class=&quot; lbl_selecciona_archivo &quot; 
 Casilla de verificación uso logotipo (por defecto chuliada) &#58; &quot;Al seleccionar esta casilla autorizas a EatCloud a utilizar tu logotipo en su plataforma y aplicaciones relacionadas y también en su presencia web.&#160; Asegúrate de contar con los privilegios necesarios para realizar esta autorización antes de subir tu logotipo&quot; class=&quot; lbl_sube_logo_terminos &quot; 
 Botón &quot;Subir logotipo&quot; (solo debe aparecer si la anterior casilla está &quot;chuliada&quot;.&#160; Si por algún motivo el usuario cambia su valor por defecto (de chuliada a no chuliada) el botón debe desaparecer y por lo tanto no se podrá subir un logotipo&#58;&#160; class=&quot; lbl_subir_logotipo &quot; 
 Validaciones para la subida del logo &#58; se deben validar los formatos gráficos establecidos .png, .jpg, .jpeg, .gif y el peso del archivo (2 megas), si el archivo no cumple con las validaciones se deben mostrar los siguientes mensajes según sea el caso 
 &quot;El formato del archivo no es válido.&#160; Por favor inténtalo de nuevo&quot; class=&quot; lbl_formato_no_valido &quot; 
 &quot;El peso del archivo sobrepasa el límite establecido. Por favor inténtalo de nuevo&quot; class=&quot; lbl_tamano_no_valido &quot; 
 El recurso subido se debe nombrar como está nombrada la cuenta respectiva (eatc_cua.name) y llevarlo a una carpeta en tamaño ícono y en tamaño normal, para desde ahí tenerlo disponible para los efectos requeridos. 
&#160; 
 Nombre de usuario 
 Muestra la información contenida aquí 
 bo_usuarios. nombre_usuario 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;CUA&#125;&#125;/bo_users?/bo_usuarios? nombre_usuario =_*&#160; 
&#160; 
 Al hacerle clic a dicho nombre debe abrirse la sección &quot; Configura tu&#160;usuario &quot; 
 Nombre de la empresa 
&#160; 
 El nombre del donante se toma de&#58; 
&#160; 
 Con el dato _DOM. cua_user se realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue=&#123;&#123;_DOM. cua_user &#125;&#125;&#160; 
&#160; 
 Con la respuesta obtenida se toma el _id para realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua,eatc_customer_fiscal_id &amp;&amp;filterfield_1=_id&amp;filtervalue_1=&#123;&#123; eatc_customers_cua._id &#125;&#125; 
&#160; 
 Con esto se obtiene el valor desencriptado de eatc_customers_cua.eatc_customer_fiscal_id &#160; y con él se realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/decrypt?table= eatc_customers &amp;fieldname= eatc_fiscal_name &amp;&amp;filterfield_1= eatc_fiscal_id &amp;filtervalue_1=&#123;&#123; eatc_customers_cua.eatc_customer_fiscal_id &#125;&#125;&#160; 
&#160; 
 Al hacerle clic al nombre de la empresa debe abrirse la sección &quot; Configura tu&#160; empresa &quot;. 

 Elementos del menú con alertas y contadores 
 Los siguientes elementos del menú deben incorporar alertas visibles, o contadores para indicarle al usuario que debe realizar acciones de configuración y de alguna manera reforzar las configuraciones que se están promoviendo desde el onboarding, y servir de alguna manera como manejador de errores ante posibles flujos truncados de onbording por parte de los usuarios. 

 ****NUEVA DISPOSICIÓN ELEMENTOS DEL MENÚ**** 
 Dashboad principal =&gt; NO VA&#160; 
 (ANTERIORMENTE&#58; Dashboard principal &#58;&#160; 
 label&#58; lb_btn_dsh_datagov_cua&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_dsh_datagov_cua 
 tooltip alerta&#58;&#160; lb_btn_dsh_datagov_cua_tooltip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_dsh_datagov_cua_tooltip ) 
&#160; 
 1. Primeros pasos&#58; ELEMENTO DE MENÚ&#160; DE PRIMERA JERARQUÍA 
 label&#58; class=&quot;lb_menu_primeros_pasos&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_menu_primeros_pasos &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Primeros pasos 
 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 
 Este elemento de menú en la actualidad está incorporado en una agrupación de menús llamada &quot;Primeros Pasos&quot;.&#160; Debe pasar a ser parte de la agrupación &quot;Configuración&quot;.&#160; La idea es que la funcionalidad que abre este elemento del menú, sea la que se muestre por defecto, hasta que se hayan terminado de realizar dichos pasos de la configuración (hasta que todos estén chuleados). 
&#160; 
 Alerta de menú Primeros pasos 
 Debe aparecer una alerta en el menú, si alguno de los primeros pasos no han sido completados (es decir, si todas las etapas de los primeros pasos no están chuliadas. Por ejemplo, en el siguiente ejemplo, en el menú debería aparecer una alerta, dado que todos los primeros pasos no están completados 

 1.1. Adiciona tu primer punto de donación&#58; elemento de menú (dentro del grupo &quot;PRIMEROS PASOS&quot;) 
 label&#58; class=&quot; lbl_agregar_punto_donacion &#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_agregar_punto_donacion &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Agrega nuevo punto de donación &#58;&#160; 
&#160; 
 Alerta de menú &quot;Aun no tienes puntos de donación activos. ¡Adiciona tu primer punto de donación!&quot; 
 La alerta se debe desplegar si no existen registros de puntos de donación de donación creados / activos, lo cual se determina con la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125; 
 tooltip alerta&#58; class=lb_sin_pods_tooltip&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_sin_pods_tooltip 
&#160; 
 1.2. Realiza tu donación&#58; elemento de menú (dentro del grupo &quot;PRIMEROS PASOS&quot;) 
 label&#58; id=&quot;lb_btn_dona_datagov_cua&#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_dona_datagov_cua 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Realiza tu donación &#58;&#160; 
&#160; 
 Alerta de menú &quot;Realiza tu donación&quot; 
 La alerta se debe desplegar si no existen registros de anuncios de donación creados, lo cual se determina con la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125; 
 tooltip alerta&#58; lb_btn_dona_datagov_cua_tooltip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma=datagov_cuentas&amp; idlabel= lb_btn_dona_datagov_cua_tooltip &#160; 
&#160; 
 1.3. Crea usuarios administradores&#58; elemento de menú (dentro del grupo &quot;PRIMEROS PASOS&quot;) 
 label&#58; id=&quot; lb_cnf_bo_user_datagov_cua &#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_cnf_bo_user_datagov_cua &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Agrega usuarios de dashboard administrativo &#58;&#160; 

&#160; 
 1.4. Consulta tus resultados&#58; elemento de menú 
 label&#58; id=&quot;lb_btn_consulta_datagov_cua&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_consulta_datagov_cua 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Informes de donación 
&#160; 
 Alerta de menú &quot;Consulta tus resultados&quot; 
 La alerta se debe desplegar si no existen registros de ingreso al BO para ninguno de los usuarios registrados, es decir que cuando se hace la siguiente consulta 
 NOTA CONSTRUIR LA CONSULTA A PARTIR DE LA ESTRUCTURA DE DATOS QUE GUARDA LA INFO DE INGRESOS AL BO&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/_____ 
&#160; 
 En todos los parámetros ingresos que devuelve la consulta, no se registran ingresos 
 tooltip alerta&#58; lb_btn_consulta_datagov_cua_tootip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma=datagov_cuentas&amp; idlabel= lb_btn_consulta_datagov_cua_tootip &#160; 

 2. INICIO&#58; ELEMENTO de menú DE PRIMERA JERARQUÍA ***NUEVO*** =&gt; INFORME SIN GRÁFICA 
 label&#58; class=&quot;lbl_inicio&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_inicio 
 Ícono&#58; 
 Abre la funcionalidad&#58; ***NUEVO*** Inicio - Consulta de indicadores básicos &#160; (Se le remueven las gráficas a&#58; https&#58;//dev.datagov.eatcloud.info/_dgbo/#!/dashboard https&#58;//datagov.eatcloud.info/_dgbo/#!/dashboard ) 
&#160; 
 3. Configuración&#58; Agrupación de elementos del menú 
 label&#58; class=&quot;lb_agr_menu_cnf&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lb_agr_menu_cnf &#160; 
 Ícono&#58; El que está funcionando actualmente (piñón) 
 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 
&#160; 
 Este grupo de menús contiene los siguientes elementos de menú 
&#160; 
 3.2. Configura tu cuenta de usuario&#58; elemento de menú 
 label&#58; class=&quot;lb_btn_cnf_user_datagov_cua&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lb_btn_cnf_user_datagov_cua &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Configura tu cuenta de usuario 
&#160; 
 Alerta de menú &quot;Configura tu cuenta de usuario&quot; 
 La alerta se debe presentar, cuando al realizar la consulta de los datos del usuario respectivo (el que está logueado en la plataforma) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/bo_usuarios?id=&#123;&#123;bo_usuarios. id &#125;&#125; 
&#160; 
 Existe información incompleta, como por ejemplo el nombre de pila del usuario&#58; 
 bo_usuarios. nombre_usuario 
&#160; 
 o los datos de su perfilamiento&#58; 
 bo_usuarios. eatc_user_profile 
 tooltip alerta&#58; id=&quot; lb_btn_cnf_user_datagov_cua_tooltip &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lb_btn_cnf_user_datagov_cua_tooltip &#160; 
&#160; 
 3.3. Configura tu empresa&#58; elemento de menú 
 label&#58; class=&quot; lb_btn_cnf_emp_datagov_cua &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lb_btn_cnf_emp_datagov_cua &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Configura tu empresa 
&#160; 
 Alerta de menú &quot;Configura tu empresa&quot; 
 La alerta se debe desplegar, si no existen datos de asociación entre cuenta y cliente, lo cual se determina con la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue=&#123;&#123;eatc_cua. name &#125;&#125; 
&#160; 
 El tooltip de la alerta invita a completar los datos del cliente. 
 Ejemplo 1&#58; la consulta no trae datos&#58; eatc_cua. name=cualquiercosa 
&#160; 
 La consulta entonces sería&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table= eatc_customers_cua &amp;fieldname= eatc_cua &amp;fieldvalue= cualquiercosa &#160;&#160; 
&#160; 
 El sistema trae la siguiente respuesta que indica que no hay datos registrados&#58; 
 &#123; 
 0 &#58; &quot;no se realizó ninguna operación&quot;, 
 ts &#58; &quot;201125130416&quot;, 
 op &#58; false, 
 mem &#58; 0.39, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 tooltip alerta&#58; lb_btn_cnf_emp_datagov_cua_tooltip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_emp_datagov_cua_tooltip 

&#160; 
 3.4. Agrega usuarios administradores&#58; elemento de menú 
 label&#58; class=&quot; lb_btn_cnf_bo_user_datagov_cua &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_bo_user_datagov_cua 

 Abre la funcionalidad&#58; Agrega usuarios administradores 
&#160; 
 Alerta de menú &quot;Agrega usuarios administradores&quot; 
 La alerta se debe desplegar si no existen registros de usuarios tipo U, en el maestro de usuarios del BO, lo cual se determina con la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/bo_usuarios?tipousuario=U 
 tooltip alerta&#58; lb_btn_cnf_bo_user_datagov_cua https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_bo_user_datagov_cua_tootip 

&#160; 
 3.5. Tu plan y facturación&#58; elemento de menú (dentro del grupo &quot;Configuración&quot;) 
 label&#58; class=&quot; lbl_tu_plan_y_facturacion &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_tu_plan_y_facturacion &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Configura tu plan y facturación 
 PENDIENTE DEFINICIÓN DE ALERTA DE TOOLTIP 
 tooltip alerta&#58; lb_btn_cnf_pl_fc_datagov_cua_tooltip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_pl_fc_datagov_cua_tooltip 
&#160; 
 3.6. Mapeo de datos&#58; elemento de menú =&gt; PENDIENTE 
 label&#58; class=&quot; lbl_mapeo_datos&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_mapeo_datos &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Mapeo de datos (para cargas mediante archivo plano) 
&#160; 
 Alerta de menú &quot;Mapeo de datos&quot; 
 La alerta se debe desplegar si no existen registros de mapa o de equivalencia para el mapa, lo cual se averigua a partir de la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_map?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct=eatc_equivalent 
&#160; 
 Si la consulta no trae resultados, o trae un resultado vacío, entonces se debe colocar el globo de alerta y desplegar el tooltip correspondiente 
&#160; 
 tooltip alerta&#58; class=lb_btn_cnf_data_map_tooltip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lb_btn_cnf_data_map_tooltip &#160; (Aun no has configurado ningún mapa de datos para la subida de información a partir de archivos planos) 

&#160; 
 3.7. Carga de datos&#58; elemento de menú =&gt; PENDIENTE 
 label&#58; class=&quot; lbl_carga_datos&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_carga_datos &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Carga de datos (mediante archivo plano) 
&#160; 
 3.8. ***NUEVO&#58; Bloqueo de beneficiaros&#58; elemento de menú (dentro del grupo &quot;Configuración&quot;) 
 label&#58; lbl_bloqueo_doma ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_bloqueo_doma ) 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Bloqueo de gestores de donación por cuenta 
&#160; 
 3.9. ***NUEVO*** Configura productos&#58; elemento de menú =&gt; PENDIENTE 
 Solo le aparece a cuentas que en la configuración de la cuenta tenga configurado que en la WebApp los artículos se cargan desde un maestro de artículos ( eatc_odds ), es decir que respondan con una respuesta válida a la siguiente consulta 
 &#123;&#123;URL_entorno_donantes&#125;&#125; /api/eatcloud/ eatc_cua ?name= &#123;&#123;_DOM. cua_users &#125;&#125; &amp;eatc_odds_app= eatc_odds 
&#160; 
 Ejemplo 1&#58; ambiente de pruebas, cuenta alquería&#58; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=alqueria&amp;eatc_odds_app=eatc_odds 
 Como se despliega una respuesta válida, el elemento de menú se le despliega a la cuenta particular. 
&#160; 
 Ejemplo 2&#58; ambiente de pruebas, cuenta exito&#58; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;eatc_odds_app=eatc_odds &#160; 
 Como NO se despliega una respuesta válida, el elemento de menú no se le muestra a la cuenta particular. 

&#160; 
 label&#58; class=&quot; lbl_configura_productos&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_configura_productos 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Configura productos 

&#160; 
 3.10. ***NUEVO***Correos para reporte anuncios&#58; elemento de menú =&gt; PENDIENTE 
 Debe tener identificador de funcionalidad (para poderlo restringir por tipo de licencia y vertical) y debe ser visible solamente a usuarios administradores (tipo=A) 
 label&#58; class=&quot; lbl_menu_correos_para_reporte_anuncios &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_correos_para_reporte_anuncios &#160;&#160; 
 Abre la funcionalidad&#58; Correos para reporte anuncios 

&#160; 
 3.11. ***NUEVO***Configura tus funcionalidades&#58; elemento de menú =&gt; PENDIENTE 
 Debe tener identificador de funcionalidad (para poderlo restringir por tipo de licencia y vertical) y debe ser visible solamente a usuarios administradores (tipo=A) 
 label&#58; class=&quot; lb_btn_cnf_fun_datagov_cua&#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_fun_datagov_cua &#160; 
 Abre la funcionalidad&#58; Configura tus funcionalidades &#58; 
 label&#58; lb_btn_cnf_fun_datagov_cua&#58;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_cnf_fun_datagov_cua 

&#160; 
 4. AGREGA Puntos de donación&#58; elemento de menú De primera categoría 
 label&#58; id=&quot;lb_btn_cnf_pods_datagov_cua&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_cnf_pods_datagov_cua 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Agrega puntos de donación &#58; 
 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 
 Alerta de menú &quot;Puntos de donación&quot; 
 La alerta se debe desplegar si no existen registros de puntos de donación para la cuenta en cuestión, lo cual se averigua a partir de la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. name &#125;&#125;/eatc_pods?_id=_* 
 tooltip alerta&#58; id= lb_btn_cnf_pods_datagov_cua_tooltip&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lb_btn_cnf_pods_datagov_cua_tooltip 
&#160; 
 4a. ***Nuevo&#58; Descarga tus puntos de donación *** 
 label&#58; class=&quot;lbl_descarga_pods&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_cnf_pods_datagov_cua 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Descarga tus puntos de donación &#58; 
 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 

&#160; 
 5. INFORME DE DONACIONES&#58; ELEMENTO DE MENÚ ***NUEVO***=&gt; CON GRÁFICA 
 label&#58; class=&quot;lb_informe_donaciones&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_informe_donaciones &#160; &#160; 
 Ícono&#58; 
 Abre la funcionalidad&#58; ***NUEVO*** Informe de donaciones &#58; ( https&#58;//dev.datagov.eatcloud.info/_dgbo/#!/dashboard https&#58;//datagov.eatcloud.info/_dgbo/#!/dashboard ) 

&#160; 
 5a. ***NUEVO&#58; INFORME DE PESO EXCESIVO *** 
 Label &#58; class=&quot;lbl_info_peso_excesivo&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_peso_excesivo )&#160;&#160; 
&#160; 
 El botón del menú lateral, deberá presentar una alerta (puede ser un signo de admiración en un globo rojo), cuando la s&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; eatc_cua_origin =&#123;&#123;_DOM .cua_user &#125;&#125; &amp; eatc_excessive_weight= y &amp;_cont 
&#160; 
 Siendo 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;&#58; tres días antes del día actual 
 &#123;&#123; fecha_final_periodo &#125;&#125;&#58; dia actual 
&#160; 
 Si la consulta en el parámetro &quot; count &quot; entrega un valor diferente a cero, se despliega la alerta.&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra la alerta. 
 El elemento de menú da ingreso al Informe de Peso Excesivo 

&#160; 
 Ejemplo 1&#58; ambiente productivo, _DOM .cua_master &quot;abaco&quot;, _DOM .cua_user &quot;exito&quot; , mayo 31 de 2022 
 El sistema evalúa la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2022-05-28&amp;eatc-publication_date[1]=2022-05-31&amp; eatc_cua_origin = exito &amp;eatc_excessive_weight= y &amp;_cont &#160;&#160; &#160; 
&#160; 
&#160; 
 Como la consulta entrega count &#58; &quot;3&quot; , entonces se despliega la alerta en el botón del menú lateral. 
&#160; 
 5B. ***NUEVO&#58; CANCELADOS A REVISAR *** 
 Label &#58; class=&quot;lbl_cancelados_a_revisar&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_cancelados_a_revisar )&#160;&#160;&#160; 
&#160; 
 El botón del menú lateral, deberá presentar una alerta (puede ser un signo de admiración en un globo rojo), cuando la respuesta de la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; eatc_cua_origin =&#123;&#123;_DOM .cua_user &#125;&#125; &amp; eatc-original_weight_kg = _&gt;_ 50 &amp; eatc-state = cancelled &amp;_cont 
&#160; 
 Siendo 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;&#58; siete días antes del día actual 
 &#123;&#123; fecha_final_periodo &#125;&#125;&#58; dia actual 
&#160; 
 En el parámetro &quot; count &quot; entrega un valor diferente a cero (se despliega la alerta).&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra la alerta. 
&#160; 
 El elemento de menú da ingreso al Informe de Revisión de Cancelados 
&#160; 
 5C. ***NUEVO&#58; ANUNCIOS ELIMINADOS *** 
 Label &#58; class=&quot;lbl_anuncios_eliminados&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_anuncios_eliminados )&#160;&#160;&#160;&#160; 
 El botón del menú lateral, deberá presentar una alerta (puede ser un signo de admiración en un globo rojo), cuando la respuesta de la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_deleted_dona_header ?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; eatc-donor =&#123;&#123;_DOM .cua_user &#125;&#125; &amp;_cont 
&#160; 
 Siendo 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;&#58; siete días antes del día actual 
 &#123;&#123; fecha_final_periodo &#125;&#125;&#58; dia actual 
 En el parámetro &quot; count &quot; entrega un valor diferente a cero (se despliega la alerta).&#160; En caso contrario ( count &#58; &quot;0&quot; ) no se muestra la alerta. 
 El elemento de menú da ingreso al Informe de Donaciones Eliminadas 
&#160; 
&#160; 
 5D. ***NUEVO&#58; PROGRAMADOS Y DESPACHADOS *** 
 Label &#58; class=&quot;lbl_programados_despachados&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_programados_despachados ) &#160;&#160;&#160;&#160; 
&#160; 
 El elemento de menú da ingreso al Informe de anuncios programados y despachados 
&#160; 
 6. *NUEVO*CONSTANCIA DE DONACIÓN&#58; Agrupación de elementos del menú 
 ID funcionalidad&#58; constancia_donacion (falta crearse) (oculta todo el menú y sus respectivos submenús) 
 label&#58; id=&quot; lbl_constancia_donacion &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_constancia_donacion &#160;&#160; 
 Ícono&#58;&#160; PENDIENTE 

 ***NUEVO Condición para viualizar la agrupación de elementos de menú y todos sus elementos&#58; *** 
&#160; 
 El sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua_master? eatc_cua =&#123;&#123;_DOM. cua_master &#125;&#125;&amp;eatc_proof_of_donation=y 
&#160; 
 Si se obtiene una respuesta satisfactoria, el grupo de elementos de menú (y todos sus elementos) se visualizarán.&#160; De lo contrario no se visualizarán (es decir cuando en el parámetro&#58;&#160; eatc_cua_master. eatc_proof_of_donation de la respectiva cuenta maestra &#123;&#123;_DOM. cua_master &#125;&#125; se tiene un valor igual a &quot;n&quot;, vacío, o nulo no se visualiza el grupo de elementos de menú y sus respectivos menús asociados )&#160; 
&#160; 
 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 

&#160; 
 6.1. Creación de constancia&#58; elemento de menú 
 label&#58; class=&quot; lbl_menu_creacion_constancia &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_creacion_constancia 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Generación de constancia de donación 
&#160; 
 6.2. Listado de constancias&#58; elemento de menú 
 label&#58; class=&quot; lbl_menu_listado_constancias &quot; 
https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_listado_constancias 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Listado de constancias 

&#160; 
 7. *NUEVO*Certificados de donación&#58; Agrupación de elementos del menú 
 ID funcionalidad&#58; certificados_donacion (falta crearse) (oculta todo el menú y sus respectivos submenús) 
 label&#58; id=&quot; lbl_menu_certificados &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_certificados &#160; 

 Ícono&#58;&#160; PENDIENTE 
&#160; 
 Alerta de menú &quot;Certificados de donación&quot; 
 Cuando alguno de sus dos submenús genera una alerta, en la agrupación de menús también se debe mostrar una alerta. 
 tooltip alerta&#58; lb_menu_certificados_tootip &#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lb_menu_certificados_tootip &#160; 

 EL GRUPO Y TODOS SUS ELEMENTOS SOLO LE DEBEN APARERECER A USUARIOS TIPO= A (A LOS USUARIOS TIPO= U SE LES DEBE OCULTAR) 
&#160; 
 Submenús que se despliegan a partir del menú principal 
&#160; 
 7.1. Preparación certificado&#58; elemento de menú 
 ***NUEVO &#58; Consulta para establecer si se muestra o no este elemento de menú *** 
 El sistema deberá realizar la siguiente consulta para establecer si muestra o no este elemento de menú, debido que inicialmente habrán cuentas maestras cuyos certificados se generarán directamente y por lo tanto no requieren de preparación&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud// eatc_direct_certificates ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Si la consulta no arroja resultados, entonces no se muestra el elemento del menú 
&#160; 
 Si la consulta arroja un resultado válido entonces se muestra el elemento del menú&#58; 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master=esp 
&#160; 
 El sistema realiza la consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud// eatc_direct_certificates ?eatc_cua_master=esp 
&#160; 
 Dado que el sistema arroja un resultado válido entonces no se muestra el botón del menú lateral. 
&#160; 
 label&#58; class=&quot; lbl_menu_creacion_soporte &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_menu_creacion_soporte &#160; 
 Ícono&#58;&#160; PENDIENTE 

 Abre la funcionalidad&#58; Preparación certificado de donación 
&#160; 
 Alerta de menú &quot;Preparación certificado&quot; 
 La alerta se debe desplegar si no existe un registro de método de soporte por defecto para la certificación de donaciones ( eatc_default_certification_support ) para la cuenta específica 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; 
 tooltip alerta&#58; class=&quot; lbl_menu_creacion_precertificado _tootip&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_creacion_precertificado _tootip &#160; 
&#160; 
 7.2. Listado de soportes&#58; elemento de menú 
 ***NUEVO &#58; Consulta para establecer si se muestra o no este elemento de menú *** 
 El sistema deberá realizar la siguiente consulta para establecer si muestra o no este elemento de menú, debido que inicialmente habrán cuentas maestras cuyos certificados se generarán directamente y por lo tanto no requieren de preparación y no poseen soportes&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud// eatc_direct_certificates ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Si la consulta no arroja resultados, entonces no se muestra el elemento del menú 
&#160; 
 Si la consulta arroja un resultado válido entonces se muestra el elemento del menú&#58; 
&#160; 
 label&#58; class=&quot; lbl_menu_listado_soportes &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_listado_soportes 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Listado de soportes ( método carta colombia , método factura electrónica colombia) 
 Alerta de menú &quot;Listado de soportes&quot; 
 La alerta se debe desplegar si existen documentos soporte tipo &quot; carta_colombia &quot; que no tienen un valor válido de &quot;fecha y hora de firma&quot; para la cuenta en cuestión, es decir si la siguiente consulta arroja resultados 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_certification_supports_headers ?eatc_dona_certification_support= carta_colombia &amp;eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_signature_datetime= 0000-00-00%2000&#58;00&#58;00 
 tooltip alerta&#58; class=&quot;lb_menu_listado_soportes_tootip&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_menu_listado_soportes_tootip &#160; &#160; 
&#160; 
 7.3a. Listado de pre-certificados&#58; elemento de menú 
 ***NUEVO &#58; Consulta para establecer si se muestra o no este elemento de menú *** 
 El sistema deberá realizar la siguiente consulta para establecer si muestra o no este elemento de menú, debido que inicialmente habrán cuentas maestras cuyos certificados se generarán directamente y por lo tanto no requieren de preparación&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud// eatc_direct_certificates ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Si la consulta no arroja resultados, entonces no se muestra el elemento del menú 
&#160; 
 Si la consulta arroja un resultado válido entonces se muestra el elemento del menú&#58; 
 label&#58; class=&quot; lbl_menu_listado_precertificado &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_menu_listado_precertificado &#160; &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Listado de pre-certificados 

&#160; 
 7.3. Consulta de certificados&#58; elemento de menú 
 label&#58; class=&quot; lbl_menu_consulta_certificados&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_menu_consulta_certificados &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Consulta de certificados de donación 
&#160; 
 7.4. Donaciones no certificables&#58; elemento de menú 
 label&#58; class=&quot; lbl_donaciones_no_certificables &quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_donaciones_no_certificables &#160; &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; Consulta de anuncios entregados no certificables 

 8. DATA ANALYTICS&#58; ELEMENTO DE MENÚ 

 A diferencia de los demás componentes del menú lateral, este componente tendrá una especie de botón muy distintivo y llamativo, con un diseño similar al que se muestra a continuación.&#160; Si la empresa (cuenta usuario) posee una licencia de Data Analytics, entonces abrirá una sección donde podrá revisar informes avanzados en la plataforma.&#160; Si no posee una licencia, entonces abrirá una landing page que informará de manera general cómo funciona esta importante sección y lo invitará a adquirir la licencia respectiva 

 label&#58; class=&quot;lb_btn_data_analytics&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lb_btn_data_analytics &#160; 
 Ícono&#58;&#160; PENDIENTE 
 Abre la funcionalidad&#58; El sistema debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; 
 Si hay un registro válido para la respectiva cuenta en eatc_data_analytics_cua &#58; Data Analytics 
 Ejemplo&#58; _DOM. cua_user= exito Entorno de pruebas 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=exito 
 Si no hay un registro válido para la respectiva cuenta en eatc_data_analytics_cua &#58; Data Analytics Landing 
 Ejemplo&#58; _DOM. cua_user= aco Entorno de pruebas 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=aco 
&#160; 
 Alerta de menú &quot;Data Analytics&quot; 
 La alerta se debe desplegar si no existen registros para la cuenta respectiva (&#123;&#123;_DOM. cua_user &#125;&#125;) en el&#160; &quot; eatc_data_analytics_cua&quot; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; 
 tooltip alerta&#58; lb_btn_data_analytics_tootip&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma=datagov_cuentas&amp; idlabel= lb_btn_data_analytics_tootip 

&#160; 
 Elementos del menú Analytics&#58; 
 Eficiencia 
 Sostenibilidad 
 Ahorro 
 Detalles de anuncios 
 [DEPRECADO] &#58; Programados y despachados ( debe salir del menú analytics para desplegarlo a todos los donantes ) 
 Cancelados 

 ***NUEVO&#58; Informe avanzado de cancelados ***&#160; 
 label&#58; class=&quot;lbl_info_avanzado_cancelados&quot; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel= lbl_info_avanzado_cancelados 
 Abre la funcionalidad&#58; Informe avanzado de Cancelados 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmen%C3%BA-lateral%2F2009355257-data_analytics_btn.jpg&ow=219&oh=68, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fmen%C3%BA-lateral%2F2009355257-data_analytics_btn.jpg&ow=219&oh=68 
 Nuevo BO (datagov_cuentas) 

 292.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 974ff08a-7455-4229-8ac3-1ee24339a181 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 c1d33a6f-0416-4efc-adfd-ac6df581ffaf 
 2025-04-16T00:02:18.2071247Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"514a9b08-9d68-46c7-a4e4-a6eb8e0d7539","SequenceId":530,"FluidContainerCustomId":"69ffd818-0e92-476b-b2d6-fd09117ac014","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 MENÚ LATERAL