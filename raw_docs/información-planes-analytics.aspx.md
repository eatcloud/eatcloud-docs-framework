# información-planes-analytics.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante sobre la implementacin&#58;&#160; 
 Esta implementacin se puede basar en la realizada para mostrar informacin de las licencias rescate, dada que muchas de las consultas sern totalmente similares y por lo tanto se pueden reutilizar.&#160; Existen otras consultas que varan, dado que requieren datos diferentes a los expresados en Analytics, estas consultan se resaltarn en AZUL en la siguiente documentacin, para su fcil ubicacin.&#160; Esta definicin, reemplaza a la que se realiz inicialmente en lo que se denomin &quot; Landing Analytics &quot;. 

 W IREFRAME PROPUESTO 

 I NFORMACIN SOBRE PERIODICIDAD DEL COBRO 
 El sistema desplegar un selector nico con la siguiente informacin 

 Determinacin del valor por defecto 
 El sistema deber realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct=type_period 
&#160; 
 Si la anterior consulta no arroja datos, entonces se aplica el valor por defecto abajo definido 
&#160; 
 Valores del selector&#58; 
 Anual (ahorras un 15%) =&gt; Valor por defecto 
 class= lbl_anual_ahoras_15pc ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_anual_ahoras_15pc )&#160;&#160; 
&#160; 
 Mensual 
 class= lbl_mensual ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_mensual ) 
&#160; 
 El usuario podr elegir cualquiera de los dos periodos de la licencia de rescate.&#160;&#160; 
&#160; 
 Registro del label de periodicidad seleccionado en eatc_cua .type_period&#58; 
 Una vez haga su primera eleccin (si la consulta para la determinacin del valor por defecto no tuvo resultado) o si cambia de valor, el sistema deber realizar el siguiente registro&#58; 

&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla= eatc_cua &amp;_operacion=update&amp;type_period=&#123;&#123; lbl_anual_ahoras_15pc/lbl_mensual &#125;&#125;&amp;WHEREname=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 Leyenda debajo del selector (no est en el diseo)&#58; 
 class= lbl_periodicidad_global ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_periodicidad_global )&#160;&#160; 
&#160; 
 &quot;Esta periodicidad tambin afecta la periodicidad de facturacin de tus licencias rescate.&quot; 

 C ARDS VERTICALES CON INFORMACIN SOBRE LOS PLANES RESCATE 
 Se presentarn las cards (en formato vertical)&#160; de los diferentes planes de rescate que posean registros en la estructura de detalle de licencias y que corresponden a la siguiente consulta&#58; 

&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_type=a &amp; _distinct =eatc_licence_code 
&#160; 
 Ambiente de pruebas&#58; https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_type=a &amp; _distinct =eatc_licence_code &#160;&#160; 
 Ambiente de produccin&#58; https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_type=a &amp; _distinct =eatc_licence_code &#160; &#160; 

 NOTA con respecto al anterior diseo&#58; 
 No se presenta la&#160; card de la licencia &quot;analytics_free&quot;, la cual tambin se debe tener en cuenta, con un funcionamiento similar a la card del plan &quot; free &quot; en la pgina de informacin de licencias rescate. 
&#160; 
 Las cards dispondrn la informacin de la siguiente manera&#58; 
&#160; 
 TIPO DE LICENCIA (ANTES&#58; NOMBRE DE LA LICENCIA) 
 Mostrar el label que se obtiene de la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_licences? eatc_code=&#123;&#123;eatc_details_of_licenses .eatc_licence_code &#125;&#125; &amp; _distinct =eatc_label 
&#160; 
 Ejemplo &#58;&#160; ambiente de pruebas , eatc_details_of_licenses .eatc_licence_code= sostenibilidad 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_data_analytics_licences? eatc_code=sostenibilidad &amp; _distinct =eatc_label &#160; &#160; &#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 eatc_name_lbl &#58; &quot;lbl_sostenibilidad&quot; 
&#160; 
 El label que se coloca como nombre de la tarjeta ser&#58; lbl_sostenibilidad 

&#160; 
 ***PRECIO DE LA LICENCIA*** 
 Consulta de los valores que determinan el precio de la licencia 
 En el esquema de precios que se implement en EatCloud, se deben realizar las siguientes consultas para determinar el precio de la licencia&#58; 
&#160; 
 Periodo de la licencia &#123;&#123;eatc_cua .type_period &#125;&#125; 
 Valor que se obtuvo del selector ubicado ms arriba . 

&#160; 
 Pas desde el cul se consulta&#160; &#123;&#123;eatc_cua . eatc_country &#125;&#125; 
 El sistema debe obtener el pas de la cuenta, para realizar consultas que ms abajo se detallan. 

&#160; 
 Cantidad de puntos activos &#123;&#123; pods_activos &#125;&#125; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_cont 
&#160; 
 El nmero que arroja el conteo se deber guardar para establecer si para el nmero de puntos activos de la cuenta aplica un precio de lista o si se debe realizar una venta consultiva . 
&#160; 
 Ejemplo &#58; entorno de pruebas , _DOM. cua_user &#58; colombia 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc_active=y&amp;eatc-cua= colombia &amp;_cont 
&#160; 
 Dado que la respuesta es&#58; count &#58; &quot;82&quot; entonces se establece que la cantidad de puntos activos para la cuenta es &quot;82&quot; 
&#160; 
 KG gestionados en el ltimo mes &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; 
 El sistema debe establecer los KG que el donate (eatc_cua) ha gestionado efectivamente en el ltimo mes. Para ello el sistema realiza la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ? eatc-publication_date[0] =&#123;&#123;fecha_hace_un_mes (mismo da del mes anterior) en formato&#58; AAAA-MM-DD&#125;&#125;&amp; eatc-publication_date[1] =&#123;&#123;fecha_actual_en_formato&#58; AAAA-MM-DD&#125;&#125;&amp;eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc-state= received,pre-certified,certified &amp;_distinct= eatc-total_weight_kg 
&#160; 
 Y debe realizar la sumatoria de valores que se obtienen en el parmetro eatc-total_weight_kg , para as obtener el total de KG gestionados en el ltimo mes ( &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; ) por parte del donante.&#160; Con este dato se deber establecer y este volumen se encuentra dentro de los lmites para establecer un precio de lista o si por el contrario se debe realizar una venta consultiva. 
&#160; 
 ***NUEVO&#58; Si la consulta no trae resultados&#58; *** 
&#160; 
 Se debe establecer&#58; &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; = 0 (y no se despliega mensaje de error). 

&#160; 
 Ejemplo &#58; entorno de pruebas , _DOM. cua_user &#58; colombia, fecha actual&#58; 2021-05-12 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]= 2021-04-12 &amp;eatc-publication_date[1]= 2021-05-12 &amp;eatc-donor= colombia &amp;eatc-state=received,pre-certified,certified&amp;_distinct=eatc-total_weight_kg &#160; 
&#160; 
 Dado que la respuesta es&#58; 
 res &#58;&#160; 
 [ 
 &#123; 
 eatc-total_weight_kg &#58; &quot;18.49&quot; 
 &#125;, 
 &#123; 
 eatc-total_weight_kg &#58; &quot;14.88&quot; 
 &#125; 
 ], 
&#160; 
 Entonces el sistema establece que &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; = 18.49 + 14.88 = 33,37 
&#160; 
 ***NUEVO&#58; Vertical &#123;&#123;eatc_cua .vertical &#125;&#125; *** 
 El sistema debe obtener la vertical de la cuenta, para realizar consultas que ms abajo se detallan. 
&#160; 
 ***NUEVO&#58; Tamao de la cuenta &#123;&#123;eatc_cua .eatc_cua_size &#125;&#125; *** 
 El sistema debe obtener el tamao de la cuenta, para realizar consultas que ms abajo se detallan. 

&#160; 
 Consulta a la estructura eatc_licenses_prices ***NUEVO&#58; incorporacin de dos parmetros adicionales de consulta *** 
 El sistema deber realizar las siguientes consultas (una por cada card)&#58; 
&#160; 
 Eficiencia&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;eatc_cua_size_code=&#123;&#123;eatc_cua. eatc_cua_size &#125;&#125;&amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= eficiencia &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Si la anterior consulta no trae resultados entonces se realiza esta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= eficiencia &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 y si la anterior consulta no trae resultados entonces se realiza esta (la que estaba como nica consulta anteriormente) &#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp;analytics_licence_code= eficiencia &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
&#160; 
 Sostenibilidad&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;eatc_cua_size_code=&#123;&#123;eatc_cua. eatc_cua_size &#125;&#125;&amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= sostenibilidad &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Si la anterior consulta no trae resultados entonces se realiza esta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= sostenibilidad &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 y si la anterior consulta no trae resultados entonces se realiza esta (la que estaba como nica consulta anteriormente) &#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp;analytics_licence_code= sostenibilidad &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Ahorro&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;eatc_cua_size_code=&#123;&#123;eatc_cua. eatc_cua_size &#125;&#125;&amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= ahorro &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Si la anterior consulta no trae resultados entonces se realiza esta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= ahorro &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 y si la anterior consulta no trae resultados entonces se realiza esta (la que estaba como nica consulta anteriormente) &#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp;analytics_licence_code= ahorro &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 360&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;eatc_cua_size_code=&#123;&#123;eatc_cua. eatc_cua_size &#125;&#125;&amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= 360 &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Si la anterior consulta no trae resultados entonces se realiza esta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125; &amp;vertical=&#123;&#123;eatc_cua. vertical &#125;&#125; &amp;analytics_licence_code= 360 &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 y si la anterior consulta no trae resultados entonces se realiza esta (la que estaba como nica consulta anteriormente) &#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_licenses_prices ?country=&#123;&#123;eatc_cua. eatc_country &#125;&#125;&amp;cua_type_period=&#123;&#123;eatc_cua. type_period &#125;&#125;&amp;analytics_licence_code= 360 &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency 
&#160; 
 Si el sistema obtiene una respuesta vlida, sigue adelante con las dems validaciones.&#160; Si no la obtiene, entonces procede pintar en la interfaz, el Botn&#58; Consulte su precio con un asesor , que se especifica ms adelante. 

&#160; 
 Ejemplo 1&#58; ambiente de pruebas, country= es type_period&#58; anual ( lbl_anual_ahoras_15pc ) vertical&#58; retail eatc_cua_size_code&#58; little_retail 
&#160; 
 EFICIENCIA 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;eatc_cua_size_code= little_retail &amp;vertical= retail &amp;analytics_licence_code= eficiencia &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160;&#160; &#160; &#160; 
&#160; 
 Como la consulta no trae resultados se procede a realizar la siguiente&#58; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;vertical= retail &amp;analytics_licence_code= eficiencia &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160; 
&#160; 
 Como la consulta trae resultados, se podrn realizar validaciones para mostrar un precio. 
&#160; 
 SOSTENIBILIDAD 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;eatc_cua_size_code= little_retail &amp;vertical= retail &amp;analytics_licence_code= sostenibilidad &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160;&#160; &#160; &#160; 
&#160; 
 Como la consulta no trae resultados se procede a realizar la siguiente&#58; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;vertical= retail &amp;analytics_licence_code= sostenibilidad &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160;&#160; 
&#160; 
 Como la consulta trae resultados, se podrn realizar validaciones para mostrar un precio. 
&#160; 
 AHORRO 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;eatc_cua_size_code= little_retail &amp;vertical= retail &amp;analytics_licence_code= ahorro &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160; &#160;&#160; &#160; &#160; 
&#160; 
 Como la consulta no trae resultados se procede a realizar la siguiente&#58; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;vertical= retail &amp;analytics_licence_code= ahorro &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160;&#160; 
&#160; 
 Como la consulta trae resultados, se podrn realizar validaciones para mostrar un precio. 
&#160; 
 360 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;eatc_cua_size_code= little_retail &amp;vertical= retail &amp;analytics_licence_code= 360 &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160; &#160;&#160; &#160; &#160; 
&#160; 
 Como la consulta no trae resultados se procede a realizar la siguiente&#58; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country=es&amp;cua_type_period= lbl_anual_ahoras_15pc &amp;vertical= retail &amp;analytics_licence_code= 360 &amp;_cmp= name_lbl,description_lbl,cua_pods_inf_limit,cua_pods_sup_limit,cua_mensual_kg_inf_limit,cua_mensual_kg_sup_limit,default_price , default_price_currency &#160;&#160;&#160; 
&#160; 
&#160; 
 Como en los tres casos se obtiene respuesta se pasa a las Validaciones de &#123;&#123; pods_activos &#125;&#125; y &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; 

&#160; 
 Ejemplo 2&#58; ambiente de pruebas, country= ar type_period&#58; mensual ( lbl_mensual ) 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country= ar &amp;cua_type_period= lbl_mensual &amp;analytics_licence_code= eficiencia &#160; 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country= ar &amp;cua_type_period= lbl_mensual &amp;analytics_licence_code= sostenibilidad &#160; 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country= ar &amp;cua_type_period= lbl_mensual &amp;analytics_licence_code= ahorro &#160; 
&#160; 
 https&#58;// dev .datagov.eatcloud.info/api/eatcloud/ eatc_licenses_prices ?country= ar &amp;cua_type_period= lbl_mensual &amp;analytics_licence_code= 360 &#160;&#160; 
&#160; 
&#160; 
 Como en los tres casos no se obtiene respuesta el sistema deber mostrar en vez de un precio, el botn&#58; Consulte su precio con un asesor 

&#160; 
 Validaciones de &#123;&#123;pods_activos&#125;&#125; y &#123;&#123;kg_gestionados_ultimo_mes&#125;&#125; ***NUEVO&#58; variacin en la validacin de peso, para poder incorporar valores de kg gestionados en cero y que funcione *** 
 Con los datos de cada uno de los tipos de licencias que se obtienen de la anterior consulta, el sistema debe establecer lo siguiente&#58; 
&#160; 
 cua_pods_inf_limit &lt; &#123;&#123; pods_activos &#125;&#125; =&lt; cua_pods_sup_limit 
&#160; 
 Si los puntos de donacin activos se encuentran dentro de estos lmites, se proceder con la consulta del precio de lista para mostrarlo en la interfaz.&#160; Si el nmero de puntos activos no se encuentra dentro de los lmites establecidos, se procede a mostrar el Botn&#58; Consulte su precio con un asesor , que se especifica ms abajo. 
&#160; 
 cua_mensual_kg_inf_limit =&lt; &#123;&#123; kg_gestionados_ultimo_mes &#125;&#125; &lt; cua_mensual_kg_sup_limit 
&#160; 
 Si los kilogramos gestionados en el ltimo mes se encuentran dentro de estos lmites, se proceder con la consulta del precio de lista para mostrarlo en la interfaz.&#160; Si los kilogramos gestionados en el ltimo mes no se encuentran dentro de los lmites establecidos, se procede a mostrar el Botn&#58; Consulte su precio con un asesor , que se especifica ms abajo. 
&#160; 
 ***NUEVO&#58; validaciones para establecer si la organizacin &#123;&#123;no_posee_precio_de_lista&#125;&#125; y ello determinar el label del anterior botn &quot;comprar&quot; y su comportamiento 
 Si la cuenta no pasa una de las dos anteriores validaciones (prueba lgica &quot;o&quot;) se puede establecer que la organizacin &#123;&#123; no_posee_precio_de_lista &#125;&#125; .&#160; Esta condicin ser tomada en cuenta para la conformacin de los botones &quot; Comprar &quot; que se documentan ms abajo y tambin la presentacin o no de precio en la interfaz. 

&#160; 
 DEPRECADO&#58; Consulta de precio en ERP (consulta principal)&#58; &#123;&#123;precio&#125;&#125; 
 Documentacin Alegra&#58; https&#58;//developer.alegra.com/docs/consultar-un-producto-o-servicio &#160; 
&#160; 
 Con el dato obtenido en &#123;&#123;eatc_licenses_prices .erp_product_id &#125;&#125; se procede a realizar la siguiente consulta 
 cURL 
 curl -v -H &quot;Accept&#58; application/json&quot; -H &quot;Content-type&#58; application/json&quot; -X GET https&#58;//api.alegra.com/api/v1/items/&#123;&#123;eatc_licenses_prices .erp_product_id &#125;&#125;?fields=price -u 'diana.alvarez@eatcloud&#58; 6505f78dbfb7dfb38bfe ' 
&#160; 
 se toma el valor que llega en el parmetro 
 &quot;price&quot;&#58; [ &#123; &quot;price&quot;&#58; &quot;price.valor&quot;&#125; ] 
&#160; 
 Para con l pintar el valor que se mostrar en la interfaz.&#160; En caso que la anterior consulta no arroje resultados por algn motivo, se deber recurrir a la consulta de respaldo para presentar el precio de cada licencia 
&#160; 
 Consulta de precio en caso que no responda la consulta al ERP (consulta de respaldo)&#58; &#123;&#123;precio&#125;&#125; 
 Con el dato obtenido en &#123;&#123;eatc_licenses_prices . default_price &#125;&#125; se pinta el precio en la interfaz (a manera de respaldo o error handler de la consulta al ERP) 

&#160; 
 Despliegue del precio consultado en la interfaz 
 En la interfaz se deber presentar el precio consultado (que resulta ser un precio unitario), segido por el label class= lbl_por_pod ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_por_pod ) &#160; y seguido por la multiplicacin del precio unitario por los puntos de donacin activos y el label class= lbl_en_total ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel=lbl_en_total ) de la siguiente manera&#58; 

 Botn&#58; Consulte su precio con un asesor 
 Cuando por el nmero de puntos de donacin o los kg gestionados por el donante en el ltimo mes, le corresponde una venta consultiva, el sistema deber desplegar un botn de la siguiente manera 
&#160; 
 label&#58; class=lbl_precio_consultivo 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_precio_consultivo &#160; 
&#160; 
 Captura de la licencia a la cual se le quiere consultar el precio 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;_consulta_precio 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; (si el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Redireccin a la pgina &quot;Contacto con ventas&quot; 
 El sistema deber direccionar a la pgina &quot; Contacto con Ventas &quot; para que a partir de la misma se realice una consulta de precios. 

 P RIMER BOTN &quot;COMPRAR&quot;&#58; 
 *** NUEVO &#58; comportamiento diferenciado si la cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; 
 Segn lo establecido en la documentacin de validaciones (arriba descrita), el sistema tendr dos comportamientos diferentes, dependiendo si la cuenta&#58; 
&#160; 
 Posee un precio de lista y es un plan superior al plan actual del cliente 
 &#123;&#123;no_posee_precio_de_lista&#125;&#125; o es un plan anterior al plan actual del cliente 
&#160; 
 para principalmente desplegar el label del botn y posteriormente hacia donde redirecciona y por lo tanto que integraciones se realizan a partir del inters en la transaccin.&#160; Antes de detallar esta diferenciacin, de manera estndar para todos los casos (tengan o no precios de upgrade) se deber realizar la captura del evento de upgrade respectivo, como se define a continuacin&#58; 
&#160; 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Si el usuario acciona dicho botn, el sistema realizar lo siguiente 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;_comprar_1 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; (si el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; haciendo clic en el primer botn comprar en la card de la licencia &quot; sostenibilidad &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = sostenibilidad_comprar_1 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua= abaco= analytics_free (como el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = sostenibilidad_comprar_1 &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_analytics_plan = analytics_free 

&#160; 
 La cuenta posee un precio de lista y el plan a adquirir es superior al plan actual de la cuenta 
 Label&#58; &quot; Comprar &quot;&#58; class= lbl_comprar ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_comprar )&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina resumen de pedido 
 El sistema dirigir al usuario a la pgina de &quot; Resumen de pedido Analytics &quot;. 

&#160; 
 La cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; o el plan a adquirir es inferior al plan actual de la cuenta 
 Label&#58; &quot; Contactar a ventas &quot;&#58; class= lbl_contactar_a_ventas ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contactar_a_ventas )&#160;&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina &quot;Contacto con ventas Analytics&quot; 
 El sistema dirigir al usuario a la pgina de &quot; Contacto con ventas analytics &quot;. 

&#160; 
 ***NUEVO*** NOMBRE DE LA LICENCIA&#58; 
 Mostrar el label&#58; 
 eatc_licenses_prices. name_lbl 
&#160; 
 Que se obtiene en las consultas para definir un precio de lista .&#160; Si las consultas no traen informacin, este label simplemente no se muestra ( NO se debe desplegar ningn mensaje de error). 
&#160; 
 ***NUEVO*** D ESCRIPCIN DE LA LICENCIA&#58; 
 Mostrar el label&#58; 
 eatc_licenses_prices. description_lbl 
&#160; 
 Que se obtiene en las consultas para definir un precio de lista .&#160; Si las consultas no traen informacin, este label simplemente no se muestra ( NO se debe desplegar ningn mensaje de error). 
&#160; 
 DETALLES DE LA LICENCIA&#58; ***SIEMPRE SE DEBEN MOSTRAR AS NO HALLA PRECIO DE LISTA DEFINIDO*** 
 Mostrarn los labels que se obtienen de la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =n &amp; _distinct =eatc_detail_description_lbl 
&#160; 
 En el orden que se obtiene en el parmetro eatc_details_of_analytics_licenses. eatc_order 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;&amp;eatc_implemented=y&amp;eatc_additional_info=n 
&#160; 
 **NUEVO&#58; se resaltarn en negrilla los detalles que tengan el dato&#160; eatc_details_of_analytics_licenses .subtitle&#58; &quot;y&quot; ** 
&#160; 
 Cuando uno de los detalles que arroje la consulta tiene en el parmetro &quot; eatc_details_of_analytics_licenses. subtitle &quot; el valor &quot; y &quot; , entonces se deber resaltar en negrilla (como una especie de subttulo)&#160; el respectivo texto (que se despliega a partir del label). 

&#160; 
 Ejemplo &#58;&#160; ambiente de pruebas , eatc_details_of_analytics_licenses .eatc_licence_code=360 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code= 360 &amp;eatc_implemented=y&amp;eatc_additional_info=n &amp; _distinct =eatc_detail_description_lbl &#160; &#160; &#160;&#160; 
&#160; 
 Dado que se obtiene la siguiente respuesta&#58; 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_43_indicadores&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_eficiencia&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_sostenibilidad&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_ahorro&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_reportes_descargables&quot; 
 &#125; 
&#160; 
 Se disponen dichos labels en el orden que dicta la consulta 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=360&amp;eatc_implemented=y&amp;eatc_additional_info=n &#160; &#160; 
&#160; 
 Dado que para los siguientes labels, el parmetro eatc_details_of_analytics_licenses. subtitle &#160; tiene el dato &quot; y &quot; estos se deben presentar resaltados en negrilla (como una especie de subttulos) 
&#160; 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_43_indicadores&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_eficiencia&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_sostenibilidad&quot; 
 &#125;, 
 &#123; 
 eatc_detail_description_lbl &#58; &quot;lbl_indicadores_ahorro&quot; 
 &#125;, 
&#160; 
&#160; 
 Botn&#58; &quot;Ver ms detalles&quot; (no est en el diseo) 
&#160; 
 Despliegue del botn 
 El botn se mostrar si la siguiente consulta trae resultados 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =y &amp; _distinct =eatc_detail_description_lbl 
&#160; 
 Nota&#58; por el momento no hay datos registrados con esta caracterstica 
&#160; 
 Label del botn&#58; 
 class= lbl_ver_mas_detalles ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_ver_mas_detalles )&#160;&#160;&#160;&#160; 
&#160; 
 Si el usuario acciona dicho botn, el sistema realizar lo siguiente 
&#160; 
 Registro del evento de upgrade 
&#160; 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;_ver_mas 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; (si el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; haciendo clic en el primer botn comprar en la card de la licencia &quot; 360 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = 360_ver_mas 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua= abaco = analytics_free (como el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = 360_ver_mas &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_analytics_plan = analytics_free 
&#160; 
 Visualizacin de labels con informacin adicional 
 El sistema desplegar los labels que se obtienen de la siguiente consulta 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;&amp; eatc_implemented =y&amp; eatc_additional_info =y &amp; _distinct =eatc_detail_description_lbl 
&#160; 
 Nota&#58; por el momento no hay datos registrados con esta caracterstica 
&#160; 
 En el orden que se obtiene en el parmetro eatc_details_of_analytics_licenses. eatc_order 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_details_of_analytics_licenses? eatc_licence_code=&#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;&amp;eatc_implemented=y&amp;eatc_additional_info=y 

&#160; 
 S EGUNDO BOTN &quot;COMPRAR&quot;&#58; 
&#160; 
 *** NUEVO &#58; comportamiento diferenciado si la cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; 
 Segn lo establecido en la documentacin de validaciones (arriba descrita), el sistema tendr dos comportamientos diferentes, dependiendo si la cuenta&#58; 
&#160; 
 Posee un precio de lista y es un plan superior al actual 
 &#123;&#123;no_posee_precio_de_lista&#125;&#125; o es un plan inferior al actual 
&#160; 
 para principalmente desplegar el label del botn y posteriormente hacia donde redirecciona y por lo tanto que integraciones se realizan a partir del inters en la transaccin.&#160; Antes de detallar esta diferenciacin, de manera estndar para todos los casos (tengan o no precios de upgrade) se deber realizar la captura del evento de upgrade respectivo, como se define a continuacin&#58; 
&#160; 
 Captura de la licencia a la cual se quiere acceder por el botn de comprar 
 El sistema debe tomar el cdigo de la licencia que se intenta comprar 
 &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125; 
&#160; 
 Registro del evento de upgrade en la estructura de datos reservada para tal fin 
 El evento de upgrade debe ser capturado por la plataforma para ser guardado en la estructura que se destina para tal fin ( eatc_upgrade_events alojada en el entorno datagov de la cuenta eatcloud) de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parametros_registro&#125;&#125; 
&#160; 
 eatc_datetime = &#123;&#123;timestamp_en_formato AAAA-MM-DD HH&#58;MM&#58;SS &#125;&#125; 
 eatc_date = &#123;&#123;datestamp_en_formato AAAA-MM-DD &#125;&#125; 
 eatc_country = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =eatc_country 
 eatc_cua_master = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct = eatc_cua_master 
 eatc_cua = &#123;&#123;_DOM. cua_user &#125;&#125; 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = &#123;&#123;eatc_details_of_analytics_licenses .eatc_licence_code &#125;&#125;_comprar_2 
 eatc_user = &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_user &#125;&#125;/ bo_usuarios? nombre_usuario = &#123;&#123; bo_usuarios. nombre_usuario &#125;&#125;&amp;_distinct = email 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125; (si el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
 Llamado al api con los &#123;&#123;parametros_registro&#125;&#125; (en el llamado los parmetros se separan por &quot; &amp; &quot;) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; &#123;&#123;parametros_registro&#125;&#125; 

&#160; 
 Ejemplo&#58; entorno de pruebas, cuenta &quot; abaco &quot;, bo_usuarios. nombre_usuario &quot; abaco &quot;, el &quot; 2021-09-11 14&#58;43&#58;00 &quot; haciendo clic en el primer botn comprar en la card de la licencia &quot; 360 &quot; 
&#160; 
 El sistema toma los siguientes datos 
 eatc_datetime = 2021-09-11 14&#58;43&#58;00 
 eatc_date = 2021-09-11 
 eatc_country = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_country = co 
 eatc_cua_master = https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_cua ?name= abaco &amp;_distinct =eatc_cua_master = abaco 
 eatc_cua = abaco 
 eatc_platform = datagov_cuentas 
 eatc_upgrade_event = 360_comprar_2 
 eatc_user = https&#58;//devdonantes.eatcloud.info//api/ abaco / bo_usuarios? nombre_usuario = abaco&amp;_distinct =email = jdr@nodrizza.com 
 eatc_actual_analytics_plan = &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_analytics_cua ?eatc_cua= abaco = analytics_free (como el servicio no entrega una respuesta se colocar el valor &quot; analytics_free &quot;) 

&#160; 
&#160; 
 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https&#58;//dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_upgrade_events&amp;_operacion=insert&amp; eatc_datetime =2021-09-11%2014&#58;43&#58;00&amp; eatc_date =2021-09-11&amp; eatc_country= co&amp; eatc_cua_master =abaco&amp; eatc_cua =abaco&amp; eatc_platform =datagov_cuentas&amp; eatc_upgrade_event = 360_comprar_2 &amp; eatc_user =jdr@nodrizza.com&amp; eatc_actual_analytics_plan = analytics_free 

&#160; 
 La cuenta posee un precio de lista y el plan a adquirir es superior al plan actual de la cuenta 
 Label&#58; &quot; Comprar &quot;&#58; class= lbl_comprar ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_comprar )&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina resumen de pedido analytics 
 El sistema dirigir al usuario a la pgina de &quot; Resumen de pedido analytics &quot;. 

&#160; 
 La cuenta &#123;&#123;no_posee_precio_de_lista&#125;&#125; o el plan a adquirir es inferior al plan actual de la cuenta 
 Label&#58; &quot; Contactar a ventas &quot;&#58; class= lbl_contactar_a_ventas ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contactar_a_ventas )&#160;&#160;&#160;&#160; 
&#160; 
 ***NUEVO***&#58; Redireccin a la pgina &quot;Contacto con ventas analytics&quot; 
 El sistema dirigir al usuario a la pgina de &quot; Contacto con ventas analytics &quot;. 

&#160; 
 INDICACIN DEL PLAN ACTUAL (NO EST EN EL DISEO) 
 El sistema debe determinar la actual licencia de la cuenta realizando la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_cua ?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct =type 
&#160; 
 Para sealar dicha card (puede ser encerrndola en una card ms grande, cambindole el color, o resaltndola de alguna manera) e indicando lo siguiente 
&#160; 
 Tu plan actual 
 class= lbl_tu_plan_actual ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_tu_plan_actual )&#160;&#160; 

 I NFORMACIN Y BOTN DE PIE DE PGINA 
 El sistema desplegar la siguiente informacin abajo de las cards con informacin de las licencias 

 Si tienes ms de 50 puntos de donacin, accede a nuestro plan preferencial 
 class= lbl_si_tienes_mas_de_50_pods ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_si_tienes_mas_de_50_pods )&#160; 
&#160; 
 NO VA&#58; Rescate Business (est en el diseo arriba) 
 class= lbl_rescate_business ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_rescate_business )&#160; 
&#160; 
 Botn&#58; Contactar a ventas 
 class= lbl_contar_a_ventas ( https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;lang=_*&amp;pais=_*&amp;idlabel= lbl_contar_a_ventas )&#160;&#160;&#160;&#160; 
&#160; 
 Redireccin a contacto a ventas (CRM) 
 https&#58;//eatcloud-team.myfreshworks.com/crm/sales/web_forms/8006fad31788cd6cd2288676bdfadde91a3f7a0c7c96484234ec70263f5d4bb6/form.html?1629993883234 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformaci%C3%B3n-planes-analytics%2F2074640493-info_lic_analytics.jpg&ow=525&oh=448, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finformaci%C3%B3n-planes-analytics%2F2074640493-info_lic_analytics.jpg&ow=525&oh=448 

 User Administrator 
 481.000000000000 

 INFORMACIN PLANES (ANALYTICS)