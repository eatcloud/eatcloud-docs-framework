# información-planes-doma.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 S E BASA EN IMPLEMENTACIN PARA DATAGOV CUENTAS (WIREFRAME PROPUESTO SIMILAR A LA IMPLEMENTACIN ANTERIOR) 
 La implementacin debe poderse ver bien en la pantalla de un telfono mvil.&#160; Cmo la idea inicial es implementar esta funcionalidad mediante una pgina web (por velocidad), entonces esta pgina deber recibir como parmetros el identificador nico del gestor de donacin ( &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; ), la cuenta maestra ( &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; ) (preferiblemente como datos en la cabecera, es decir, no enviarlos como parmetros en la URL y deber implementar tambin credenciales de autenticacin, de tal manera que solo puedan acceder a la misma usuarios vlidos de la APP, tal como se controla en el proceso de autenticacin de la APP ).&#160; Tambin podr tomarse la decisin de implementar esta primera parte del Checkout en la misma APP, la segunda parte de la misma (detalle del plan) en la misma APP, y simplemente el pago por WOMPY por fuera de la APP (widget en una pgina web). 
 Por todo lo anterior, el wireframe de la funcionalidad, ser muy similar al siguiente, pero en una primera etapa solo tendr un solo selector superior (mensual) y 3 cards (dado que solamente sern las licencias free, hroe y superhroe. 

 I NFORMACIN SOBRE PERIODICIDAD DEL COBRO 
 El sistema desplegar un selector nico con la siguiente informacin 

 Valor del selector&#58; 
 En una primera etapa solo se mostrar el valor &quot;Mensual&quot; (pero no se descarta que a futuro se muestre tambin el valor anual). 
&#160; 
 (NO VA EN UNA PRIMERA ETAPA) Anual (ahorras un 15%) =&gt; Valor por defecto 
 class= lbl_anual_ahoras_15pc (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_anual_ahoras_15pc )&#160;&#160; 
&#160; 
 Mensual 
 class= lbl_mensual ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_mensual )&#160; 

 C ARDS VERTICALES CON INFORMACIN SOBRE LOS PLANES PARA LOS GESTORES DE DONACIN 
 Se presentarn las cards (en formato vertical)&#160; de los diferentes planes de rescate que posean registros en la estructura de detalle de licencias y que corresponden a la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_doma_licenses? eatc_licence_code =_*&amp; _distinct =eatc_licence_code 
&#160; 
 Ambiente de pruebas&#58; https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_details_of_doma_licenses? eatc_licence_code =_*&amp; _distinct =eatc_licence_code &#160;&#160; 
 Ambiente de produccin&#58; https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_details_of_doma_licenses? eatc_licence_code =_*&amp; _distinct =eatc_licence_code &#160;&#160; 

 I NDICACIN DEL PLAN ACTUAL 
 El sistema debe determinar la actual licencia de la cuenta realizando la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/ &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; / eatc_donation_managers ?identificador_unico_registro= &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; &amp;_distinct = eatc_license 
&#160; 
 Para sealar dicha card (puede ser encerrndola en una card ms grande, cambindole el color, o resaltndola de alguna manera) e indicando lo siguiente.&#160; Si el gestor no tiene dato registrado en eatc_license , deber aparecer como su licencia actual la &quot; free &quot; 
&#160; 
 Tu plan actual 
 class= lbl_tu_plan_actual ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_plan_actual )&#160; 

&#160; 
 Cards de licencias inferiores, se muestran de manera informativa pero con botones deshabilitados. 
 Las cards con licencias inferiores a la que tiene registrada el respectivo gestor de donaciones en &#123;&#123;eatc_donation_managers. eatc_licenses &#125;&#125; , deben aparecer activas, con botones accionables.&#160; Las cards de licencias inferiores deben aparecer inactivas (simplemente informativas).&#160; 
 Las cards dispondrn la informacin de la siguiente manera&#58; 
&#160; 
 Nombre de la licencia&#58; 
 Mostrar el label que se obtiene de la siguiente consulta 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_types_of_doma_licenses? eatc_code=&#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125; &amp; _distinct =eatc_name_lbl 
&#160; 
 Ejemplo &#58;&#160; ambiente de pruebas , eatc_details_of_licenses .eatc_licence_code= free 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_types_of_doma_licenses? eatc_code= free&amp; _distinct =eatc_name_lbl &#160;&#160; &#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
&#160; 
 eatc_name_lbl &#58; &quot;lbl_free&quot; 
&#160; 
 El label que se coloca como nombre de la tarjeta ser&#58; lbl_free 

&#160; 
 ***PRECIO DE LA LICENCIA*** 
 Consulta de los valores que determinan el precio de la licencia 
 En una primera implementacin el valor de la licencia se obtiene consultando los siguientes valores (posteriormente se podrn adicionar ms parmetros de consulta). 
&#160; 
 Cuenta maestra &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; 
&#160; 
 Periodo de la licencia&#58; en una primera instancia, ser una constante&#58; &#160; lbl_mensual 
 Valor que se obtuvo del selector ubicado ms arriba . 

&#160; 
 Consulta a la estructura eatc_licenses_prices 
 El sistema deber realizar las siguientes consultas en una primera instancia (una por cada card)&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master = &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; &amp;cua_type_period= lbl_mensual &amp; doma_license = free&amp;_cmp= default_price,default_price_currency 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master = &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; &amp;cua_type_period= lbl_mensual &amp; doma_license = hero&amp;_cmp= default_price,default_price_currency 
&#160; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master = &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; &amp;cua_type_period= lbl_mensual &amp; doma_license = superhero&amp;_cmp= default_price,default_price_currency 
&#160; 
 Si el sistema obtiene una respuesta vlida, sigue adelante con las dems validaciones.&#160; Si no la obtiene, entonces procede pintar en la interfaz, el Botn&#58; Consulte su precio con un asesor , que se especifica ms adelante. 

&#160; 
 Ejemplo 1&#58; ambiente de pruebas, eatc_cua_master = abaco type_period&#58; lbl_mensual 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =abaco&amp;cua_type_period= lbl_mensual &amp; doma_license = free&amp;_cmp=default_price,default_price_currency &#160; &#160; 
 &#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =abaco&amp;cua_type_period= lbl_mensual &amp; doma_license = hero&amp;_cmp=default_price,default_price_currency &#160; 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_doma_licenses_prices ? eatc_cua_master =abaco&amp;cua_type_period= lbl_mensual &amp; doma_license = free&amp;_cmp=default_price,default_price_currency &#160; 

&#160; 
 Despliegue del precio consultado en la interfaz 
 En la interfaz se deber presentar el precio consultado (que resulta ser un precio unitario), segido por el label class= lbl_mensual_por_sucursal &#58; 
&#160; 
 class= lbl_mensual_por_sucursal (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=app_beneficiarios&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_mensual_por_sucursal )&#160; 

 (En una primera instancia no ir, pero puede habilitarse a futuro) Botn&#58; Consulte su precio con un asesor 
 Cuando por el nmero de puntos de donacin o los kg gestionados por el donante en el ltimo mes, le corresponde una venta consultiva, el sistema deber desplegar un botn de la siguiente manera 
&#160; 
 label&#58; class=lbl_precio_consultivo 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_precio_consultivo &#160; 
&#160; 
 Captura de la licencia a la cual se le quiere consultar el precio 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_cua_master 
 eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform =datagov_cuentas 
 eatc_upgrade_event =&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125;_consulta_precio 
 eatc_user =&#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct =email 
 eatc_actual_rescue_plan =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Registro del lead en el CRM 
 El sistema deber realizar un registro de Lead en el CRM de la empresa (Freshworks), de acuerdo a la documentacin del API de la herramienta y a las siguientes indicaciones. 

 NO VA (POR CUESTIONES DE ESPACIO Y VISUALIZCIN) PRIMER BOTN &quot;COMPRAR&quot;&#58; 
&#160; 
 En una primera instancia no va&#58; comportamiento diferenciado si la cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; 
 Segn lo establecido en la documentacin de validaciones (arriba descrita), el sistema tendr dos comportamientos diferentes, dependiendo si la cuenta&#58; 
&#160; 
 Posee un precio de lista y es un plan superior al plan actual del cliente 
 &#123;&#123;no_posee_precio_de_lista&#125;&#125; o es un plan anterior al plan actual del cliente 
&#160; 
 para principalmente desplegar el label del botn y posteriormente hacia donde redirecciona y por lo tanto que integraciones se realizan a partir del inters en la transaccin.&#160; Antes de detallar esta diferenciacin, de manera estndar para todos los casos (tengan o no precios de upgrade) se deber realizar la captura del evento de upgrade respectivo, como se define a continuacin&#58; 
&#160; 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Si el usuario acciona dicho botn, el sistema realizar lo siguiente 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country &#58; &quot;&#123;&#123;eatc_cua_master( eatc_cua =&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;). eatc_country &#125;&#125;&quot;, 
 eatc_cua_master &#58; &quot;&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;&quot;, 
 eatc_cua &#58; &quot;&quot; =&gt; *** No se enva registro *** 
 eatc_doma &#58; &quot;&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&quot;, =&gt; *** Campo nuevo , se debe adicionar a la tabla*** 
 eatc_platform &#58; &quot;app_beneficiarios&quot;, 
 eatc_upgrade_event =&#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125;_comprar_1 
 eatc_user =&#123;&#123;usuario de la APP&#125;&#125; 
 eatc_actual_rescue_plan =&#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125;/ eatc_donation_managers ?identificador_unico_registro=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;_distinct = eatc_license 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 La cuenta posee un precio de lista y el plan a adquirir es superior al plan actual de la cuenta 
 En una primera instancia, dado el evento de upgrade, solo se podrn mostrar botones de compra de las licencias superiores a la actual para el respectivo gestor de donaciones (dado que son esas licencias las que le dan la capacidad de gestin necesaria, y por la cual llegaron a este punto). 
 Label&#58; &quot; Comprar &quot;&#58; class= lbl_comprar ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_comprar )&#160;&#160;&#160; 
&#160; 
 Redireccin a la pgina resumen de pedido 
 El sistema dirigir al usuario a la pgina de &quot; Resumen de pedido &quot;. 

&#160; 
 En una primera instancia no va&#58; La cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; o el plan a adquirir es inferior al plan actual de la cuenta 
&#160; 
 Label&#58; &quot; Contactar a ventas &quot;&#58; class= lbl_contactar_a_ventas ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contactar_a_ventas )&#160;&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina &quot;Contacto con ventas&quot; 
 El sistema dirigir al usuario a la pgina de &quot; Contacto con ventas &quot;. 

&#160; 
 D ETALLES DE LA LICENCIA &#58; 
 Mostrarn los labels que se obtienen de la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_doma_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =n &amp; _cmp = eatc_order ,eatc_detail_description_lbl 
&#160; 
 En el orden que se obtiene en el parmetro eatc_details_of_doma_licenses. eatc_order 
&#160; 
 Ejemplo &#58;&#160; ambiente de pruebas , eatc_details_of_doma_licen ses .eatc_licence_code=free 
&#160; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_details_of_doma_licenses? eatc_licence_code= free &amp;eatc_implemented=y&amp;eatc_additional_info=n &amp; _cmp = eatc_order ,eatc_detail_description_lbl &#160; 
&#160; 
 &#123; &#160;&#160;&#160;&#160;&#160; 
 eatc_order&#58; &quot;1&quot;, 
 eatc_detail_description_lbl&#58; &quot;lbl_hasta_25_kg&quot; 
 &#125;, 
 &#123; 
 eatc_order&#58; 2, 
 eatc_detail_description_lbl&#58; &quot;lbl_notificaciones_cercania&quot; 
 &#125;, 
 &#123; 
 eatc_order&#58; &quot;3&quot;, 
 eatc_detail_description_lbl&#58; &quot;lbl_soporte_fb&quot; 
 &#125;, 
 &#123; 
 eatc_order&#58; &quot;4&quot;, 
 eatc_detail_description_lbl&#58; &quot;lbl_soporte_ws&quot; 
 &#125;, 
 &#123; 
 eatc_order&#58; &quot;5&quot;, 
 eatc_detail_description_lbl&#58; &quot;lbl_soporte_wa&quot; 
 &#125; 
&#160; 
 Se disponen dichos labels en el orden que dicta la respuesta en el parmetro &quot;eatc_order&quot; 

&#160; 
 En una primera instancia no va&#58; Botn&#58; &quot;ver ms detalles&quot; (no est en el diseo) 
&#160; 
 Despliegue del botn 
 El botn se mostrar si la siguiente consulta trae resultados 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =y &amp; _distinct =eatc_detail_description_lbl 
&#160; 
 Nota&#58; por el momento no hay datos registrados con esta caracterstica 
&#160; 
 Label del botn&#58; 
 class= lbl_ver_mas_detalles (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_ver_mas_detalles )&#160;&#160;&#160; 
&#160; 
 Si el usuario acciona dicho botn, el sistema realizar lo siguiente 
&#160; 
 Registro del evento de upgrade 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_cua_master 
 eatc_cua =&#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform =datagov_cuentas 
 eatc_upgrade_event =&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125;_ver_mas 
 eatc_user =&#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct =email 
 eatc_actual_rescue_plan =&#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; haciendo clic en el primer botn comprar en la card de la licencia &quot; esencial &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime =2021-09-11 14&#58;43&#58;00 
 eatc_date =2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master =abaco 
 eatc_cua = abaco 
 eatc_platform =datagov_cuentas 
 eatc_upgrade_event =esencial_ver_mas 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email =jdr@nodrizza.com 
 eatc_actual_rescue_plan = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =type =free 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event =esencial_ver_mas&amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_rescue_plan =free 
&#160; 
 Visualizacin de labels con informacin adicional 
 El sistema desplegar los labels que se obtienen de la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =y &amp; _distinct =eatc_detail_description_lbl 
&#160; 
 Nota&#58; por el momento no hay datos registrados con esta caracterstica 
&#160; 
 En el orden que se obtiene en el parmetro eatc_details_of_licenses. eatc_order 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125;&amp;eatc_implemented=y&amp;eatc_additional_info=y 

&#160; 
 S EGUNDO BOTN &quot;COMPRAR&quot; &#58; 
 En una primera instancia no va&#58;&#160; comportamiento diferenciado si la cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; 
 Segn lo establecido en la documentacin de validaciones (arriba descrita), el sistema tendr dos comportamientos diferentes, dependiendo si la cuenta&#58; 
&#160; 
 Posee un precio de lista y es un plan superior al actual 
 &#123;&#123;no_posee_precio_de_lista&#125;&#125; o es un plan inferior al actual 
&#160; 
 para principalmente desplegar el label del botn y posteriormente hacia donde redirecciona y por lo tanto que integraciones se realizan a partir del inters en la transaccin.&#160; Antes de detallar esta diferenciacin, de manera estndar para todos los casos (tengan o no precios de upgrade) se deber realizar la captura del evento de upgrade respectivo, como se define a continuacin&#58; 
&#160; 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country &#58; &quot;&#123;&#123;eatc_cua_master( eatc_cua = &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; ). eatc_country &#125;&#125;&quot;, 
 eatc_cua_master &#58; &quot; &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; &quot;, 
 eatc_cua &#58; &quot;&quot; =&gt; *** No se enva registro *** 
 eatc_doma &#58; &quot; &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; &quot;, =&gt; *** Campo nuevo , se debe adicionar a la tabla *** 
 eatc_platform &#58; &quot; app_beneficiarios &quot;, 
 eatc_upgrade_event = &#123;&#123;eatc_details_of_doma_licenses .eatc_licence_code &#125;&#125;_comprar_1 
 eatc_user =&#123;&#123;usuario de la APP&#125;&#125; 
 eatc_actual_rescue_plan = &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/ &#123;&#123;eatc_donation_managers. eatc_cua_master &#125;&#125; / eatc_donation_managers ?identificador_unico_registro= &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; &amp;_distinct = eatc_license 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; &#160; 
&#160; 
 Redireccin a la pgina resumen de pedido 
 El sistema dirigir al usuario a la pgina de &quot; Resumen de pedido &quot;. 

&#160; 
 En una primera instancia no va&#58; La cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; o el plan a adquirir es inferior al plan actual de la cuenta 
 Label&#58; &quot; Contactar a ventas &quot;&#58; class= lbl_contactar_a_ventas ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contactar_a_ventas )&#160;&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina &quot;Contacto con ventas&quot; 
 El sistema dirigir al usuario a la pgina de &quot; Contacto con ventas &quot;. 

 EN UNA PRIMERA INSTANCIA NO VA&#58; INFORMACIN Y BOTN DE PIE DE PGINA 
 El sistema desplegar la siguiente informacin abajo de las cards con informacin de las licencias 

 Si tienes ms de 50 puntos de donacin, accede a nuestro plan preferencial 
 class= lbl_si_tienes_mas_de_50_pods ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_si_tienes_mas_de_50_pods )&#160; 
&#160; 
 Rescate Business 
 class= lbl_rescate_business ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_rescate_business )&#160; 
&#160; 
 Botn&#58; Contactar a ventas 
 class= lbl_contar_a_ventas (https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contar_a_ventas )&#160;&#160;&#160; 
&#160; 
 Redireccin a contacto a ventas (CRM) 
 https&#58;//eatcloud-team.myfreshworks.com/crm/sales/web_forms/8006fad31788cd6cd2288676bdfadde91a3f7a0c7c96484234ec70263f5d4bb6/form.html?1629993883234 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformaci%C3%B3n-planes-doma%2F941925128-info_planes_rescate--1-.jpg&ow=854&oh=892, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformaci%C3%B3n-planes-doma%2F941925128-info_planes_rescate--1-.jpg&ow=854&oh=892 
 EatCloud Beneficiarios 

 571.000000000000 

 INFORMACIN PLANES (GESTORES DE DONACIN)