# proceso-de-cálculo-de-población-atendida.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El propsito de este proceso es generar un proceso que corra todos los primeros das del mes y que a partir de datos maestros que nos entrega ABACO en cuanto a la poblacin atendida por ciudad, primero determine, para cada cuenta usuario, las donaciones que fueron realizadas en dichas ciudades, y al establecerlo, realizar el clculo del potencial de personas atendidas segn la data maestra que nos suministra en primera instancia ABACO. 

 Proceso que corre el primer da del mes&#58; 
 Se deber programar una tarea programada, para que a primera hora del primer da del mes, se corra el proceso para calcular la poblacin atendida. 

 Determinacin de ciudades para realizar el clculo 
&#160; 
 El sistema deber determinar el array de ciudades para el clculo del indicador, realizando la siguiente consulta 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_poblacion_atendida ?_id=_*&amp;_cmp= ciudad 
&#160; 
 Con esta consulta se obtienen las ciudades &#123;&#123; array_ciudades &#125;&#125; que deben ser evaluadas en el mes anterior para realizar el clculo respectivo.&#160; 
&#160; 
 Ejemplo, Ambiente produccin , cua_master&#58; abaco , este es el &#123;&#123; array_ciudades &#125;&#125; 
 BOGOTA,MEDELLIN,CALI,RIOHACHA,BUCARAMANGA,SANTA MARTA,CUCUTA,MANIZALES,CARTAGO,NEIVA,CARTAGENA,VILLAVICENCIO,BARRANQUILLA 

&#160; 
 El sistema tambin deber tener en cuenta estos datos para posteriores clculos 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_poblacion_atendida ?_id=_*&amp;_cmp= ciudad,departamento,poblacion_atendida 

 Consulta de las donaciones para cada cuenta, para determinar qu ciudades se tomarn para realizar el clculo 
 Nota importante para el desarrollo&#58; la siguiente descripcin de consultas es ilustrativa, ya que no se puede establecer a ciencia cierta si es la secuencia ms ptima.&#160; A continuacin se destacan como subttulos, los aspectos que se deben tener en cuenta para realizar la consulta o las consultas para obtener la informacin 
&#160; 
 Determinacin de las cuentas a las cuales se les debe calcular el indicador 
 Con la siguiente consulta se obtienen las cuentas a las cuales se les debe calcular el indicador 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp=name 

&#160; 
 Ejemplo&#58; cua_master&#58; abaco , entorno de pruebas &#58; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_cua_master=abaco&amp;_cmp=name &#160;&#160; 

&#160; 
 Determinacin de los anuncios en las ciudades con informacin de cobertura y que han sido gestionados 
 El sistema deber determinar si en el mes anterior existen donaciones en las ciudades / departamentos informados, para cada donante activo en la plataforma y que han sido asignados y gestionados.&#160; Se propone realizar la siguiente consulta&#160; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?eatc-publication_date[0]=&#123;&#123; fecha_inicial_mes_anterior &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_mes_anterior &#125;&#125;&amp; eatc-donor =&#123;&#123; eatc_cua. name &#125;&#125;&amp; eatc-city =&#123;&#123;array_ciudades&#125;&#125;&amp; eatc-state =awarded,scheduled,delivered,received,pre-certified,certified &amp;_cmp= eatc-code,eatc-city,eatc-province 
&#160; 
 Con esta consulta se obtienen el array de cdigos&#160; de anuncios de donacin que pertenecen a estas ciudades &#123;&#123; array_codigos_todas_donaciones &#125;&#125;. 

&#160; 
 Ejemplo&#58; cua_master&#58; abaco , cua_user&#58; takami, entorno de produccin, Fecha de corrida del proceso&#58; 01/01/2022 &#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-12-01&amp;eatc-publication_date[1]=2021-12-31&amp;eatc-donor=takami&amp;eatc-city=BOGOTA_DC,MEDELLIN,CALI,RIOHACHA,BUCARAMANGA,SANTA%20MARTA,CUCUTA,MANIZALES,CARTAGO,NEIVA,CARTAGENA,VILLAVICENCIO,BARRANQUILLA&amp;eatc-state=awarded,scheduled,delivered,received,pre-certified,certified&amp;_cmp=eatc-code,eatc-city,eatc-province 

&#160; 
 Validacin de ciudades que pertenezcan a los departamentos indicados ( es la parte que se me dificulta expresar con consultas ) 
 El sistema debe tomar solamente los anuncios que corresponden a la ciudad / departamento adecuado (para evitar que se tomen en cuenta nombres de ciudades homnimas que pertenezcan a otros departamentos) para posteriormente establecer el distinct de ciudades respectivo de la siguiente manera&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?eatc-publication_date[0]=&#123;&#123; fecha_inicial_mes_anterior &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_mes_anterior &#125;&#125;&amp; eatc-donor =&#123;&#123; eatc_cua. name &#125;&#125;&amp; eatc-city =&#123;&#123;array_ciudades&#125;&#125;&amp; eatc-state =awarded,scheduled,delivered,received,pre-certified,certified &amp;_distinct= eatc-city 

&#160; 
 Ejemplo&#58; cua_master&#58; abaco , cua_user&#58; takami, entorno de produccin, Fecha de corrida del proceso&#58; 01/01/2022 &#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2021-12-01&amp;eatc-publication_date[1]=2021-12-31&amp;eatc-donor=takami&amp;eatc-city=BOGOTA_DC,MEDELLIN,CALI,RIOHACHA,BUCARAMANGA,SANTA%20MARTA,CUCUTA,MANIZALES,CARTAGO,NEIVA,CARTAGENA,VILLAVICENCIO,BARRANQUILLA&amp;eatc-state=awarded,scheduled,delivered,received,pre-certified,certified&amp;_distinct=eatc-city &#160; 
&#160; 
 Con los datos obtenidos en la anterior consulta se genera un &#123;&#123; array_ciudades_con_cobertura &#125;&#125; 
&#160; 
 Consulta calcular el dato de poblacin atendida 
 Con el anterior dato (ciudades con cobertura), el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_poblacion_atendida ?ciudad=&#123;&#123; array_ciudades_con_cobertura &#125;&#125;&amp;_cmp= poblacion_atendida 
&#160; 
 Para posteriormente realizar la sumatoria de los datos obtenidos en &quot; poblacion_atendida &quot; y con ello obtener el dato del KPI particular &#123;&#123; poblacion_atendida_mes_anterior &#125;&#125; 
&#160; 
 Continuando con el ejemplo anterior 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/ eatc_poblacion_atendida ?ciudad=BOGOTA_DC&amp;_cmp= poblacion_atendida &#160; 
&#160; 
 Como se obtiene la respuesta&#58; 
 res &#58; 
 [ 
 &#123; 
 poblacion_atendida &#58; &quot;171619&quot; 
 &#125; 
 ], 
&#160; 
 En este caso no se debe hacer sumatoria, por lo tanto 
&#160; 
 &#123;&#123; poblacion_atendida_mes_anterior &#125;&#125; = 171619 

 RESGISTRO DE POBLACIN ATENDIDA POR CUA_USER 
&#160; 
 Con los datos obtenidos anteriormente se procede a realizar el registro en la estructura definida para ese propsito 
&#160; 
 &#123;&#123;parametros_registro_poblacion_atendida_por_cua&#125;&#125; 
&#160; 
 eatc_fecha_generacion&#58;&#160; 
 En formato &quot;0000-00-00&quot; , corresponde a la fecha en la cual se corre el proceso para la obtencin de este KPI (que debe ser el primer da del mes). 
&#160; 
 eatc_fechahora_generacion &#58; En formato &quot;0000-00-00 00&#58;00&#58;00&quot; , corresponde a la fecha y hora en la cual se corre el proceso para la obtencin de este KPI (que debe ser el primer da del mes a primera hora) 
&#160; 
 eatc_mes_kpi &#58; &quot;Mes para el cul se calcula el KPI en formato AAAA-MM&quot; , que debe ser el mes inmediatamente anterior. 
&#160; 
 eatc_cua_user &#58; Corresponde al dato de la cuenta usuario para el cual se calcul el indicador&#58; &#123;&#123; eatc_cua. name &#125;&#125; , 
&#160; 
 poblacion_atendida &#58; &quot;Nmero de personas atendidas segn el clculo&quot;, que corresponde a &#123;&#123; poblacion_atendida_mes_anterior &#125;&#125; 

&#160; 
 Escritura CRD 
 Para escribir el dato se realiza la siguiente escritura&#58; 

&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_registro_poblacion_atendida_cua &amp;_operacion=insert&amp;&#123;&#123; parametros_registro_poblacion_atendida_por_cua &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESO DE CLCULO DE POBLACIN ATENDIDA