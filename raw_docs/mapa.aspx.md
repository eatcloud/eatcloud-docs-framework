# mapa.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 MAPA&#58; Filtro (a quienes se le muestra el informe, incluyendo su ttulo)&#58; 
 A los usuarios tipo&#160; eatc_cua_master 

&#160; 
 Ttulo del informe&#58;&#160; Mapa de anlisis municipal de ecosistema 
 Label&#58; class=&quot; lbl_mapa_analisis_municipal &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_mapa_analisis_municipal )&#160;&#160;&#160; 

&#160; 
 Descripcin&#58;&#160; 
 Label&#58; class=&quot; lbl_mapa_analisis_municipal_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_mapalbl_mapa_analisis_municipal_desc )&#160;&#160; 
&#160; 
 &quot;En este mapa se podrn hacer anlisis a nivel municipal del ecosistema de rescate alimentario adscrito a EatCloud.&quot; 

 Referente de desarrollo 
 En trminos generales el mapa deber funcionar como lo hace el siguiente 
 https&#58;//www.google.com/maps/d/u/0/viewer?ll=6.282464813376913%2C-75.55903717350469&amp;z=14&amp;mid=1NluQJsdhE8BG5yBtaC-Vuc3PLheag44 &#160; 
&#160; 
 Centrado del mapa 
 El mapa se deber centrar en la coordenada que arroje el browser y por lo tanto al ingresar al mapa debe solicitar los permisos para acceder a la coordenada.&#160; Si no se puede obtener la coordenada, se centrar en Medelln. &#160; El sistema permitir que el usuario vare el centro del mapa y al hacerlo el sistema deber consultar que &quot;eatc_municipalities. eatc-city &quot; corresponde al punto del mapa con la informacin que se guarda en nuestro maestro de municipios (para realizar dichas consultas se pueden utilizar los servicios de consulta de informacin georefernciada con que cuenta EatCloud) 

&#160; 
 Zoom del mapa 
 El zoom del mapa debe permitir visualizar a pantalla completa el territorio de una ciudad como BOGOT. El usuario podr acercar o alejar el zoom segn sus necesidades de consulta 

 C APAS A MOSTRAR 
 El mapa deber mostrar, tal cual se muestra en el referente ( https&#58;//www.google.com/maps/d/u/0/viewer?ll=6.282464813376901%2C-75.55903717350469&amp;z=14&amp;mid=1NluQJsdhE8BG5yBtaC-Vuc3PLheag44 ), las siguientes capas, cuyo valor por defecto ser &quot;seleccionada&quot; (selector mltiple chuliado).&#160; Cuando el usuario, quite un cluyo de seleccin, la respectiva capa deber quitarse del mapa, dejando las restantes. 
&#160; 
 Las consultas a realizar para mostrar las diferentes capas (principalmente conjunto de puntos representados por coordenadas decimales), son las siguientes&#58; 
&#160; 
 Gestores de donacin con actividad (en el mapa de muestra&#58; &quot; Activas &quot;) 
 class=&quot; lbl_doma_con_actividad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_con_actividad &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_con_actividad_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_con_actividad_desc &#160; &#160; &#160; 
&#160; 
 &quot; Gestores de donaciones que han gestionado satisfactoriamente por lo menos una donacin en los ltimos tres meses &quot; 
&#160; 
 Llamados para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_actual_menos_tres_meses &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_actual &#125;&#125;&amp;eatc-state= received ,pre-certified,certified&amp;eatc-city=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_distinct= eatc-donation_manager_code 
&#160; 
 Las respuestas de la anterior consulta se lleva a un &#123;&#123; array_donation_managers_code &#125;&#125; y con este array se realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123; array_donation_managers_code &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b&#160; 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones con actividad&#58; solicitar estos diseos a LuisK) 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master&#58; abaco, eatc-city=MEDELLIN, fecha actual 2023-10-15 
 El sistema realiza el siguiente llamado 
 https&#58;//dev donantes .eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2023-07-15&amp;eatc-publication_date[1]=2023-10-15&amp;eatc-state= received ,pre-certified,certified&amp;eatc-city=MEDELLIN&amp;_distinct= eatc-donation_manager_code &#160; 
&#160; 
 Dadas las respuestas&#58; &#123;&#123; array_donation_managers_code &#125;&#125; = 811018073,900639899,9008588185,900194548-0 , por lo tanto la consulta siguiente es&#58;&#160; 
 https&#58;//dev beneficiarios .eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= 811018073,900639899,9008588185,900194548-0 &amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &#160; 

&#160; 
 Gestores de donacin sin actividad (en el mapa de muestra &quot; Pasivas &quot;) 
 class=&quot; lbl_doma_sin_actividad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_sin_actividad 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_sin_actividad_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_sin_actividad_desc &#160; &#160; 
&#160; 
 &quot; Gestores de donaciones que NO han gestionado satisfactoriamente por lo menos una donacin en los ltimos tres meses &quot; 
&#160; 
 Llamados para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 Con el &#123;&#123; array_donation_managers_code &#125;&#125; se realiza la siguiente consulta (es prcticamente la misma consulta anterior, pero al array se le incorpora el prefijo _nin_ y con ello el sistema traer los gestores de donacin que no tienen actividad, es decir, excluir de la consulta a los gestores de donacin con actividad, que fueron los que se determinaron en la consulta anterior. Tambin se excluyen de este listado quienes estn marcados con estados persona_natural,expulsado ) y por ltimo, se realiza una consulta municipal (municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;)&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro= _nin_ &#123;&#123; array_donation_managers_code &#125;&#125;&amp;eatc_state= _nin_ persona_natural,expulsado &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b&#160; 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones sin actividad&#58; solicitar estos diseos a LuisK) 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master&#58; abaco, fecha actual 2023-10-15, eatc-city=MEDELLIN 
 Dadas las consultas de la capa anterior en donde&#58; &#123;&#123; array_donation_managers_code &#125;&#125; = 811018073,890980023,900639899,901110283,9008588185,901238380,900194548-0,900693836,901229228 , por lo tanto la consulta siguiente es&#58;&#160; 
 https&#58;//dev beneficiarios .eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= _nin_ 811018073,900639899,9008588185,900194548-0 &amp;eatc_state= _nin_ persona_natural,expulsado &amp;municipio=medellin&amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &#160;&#160;&#160;&#160;&#160; 

&#160; 
 Puntos de donacin con actividad (est incluido en el mapa de muestra en &quot; Donantes &quot;, pero en esta propuesta se mostrarn los puntos con actividad) 
 class=&quot; lbl_pods_con_actividad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_con_actividad &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_pods_con_actividad_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_pods_con_actividad_desc &#160; &#160; &#160; 
&#160; 
 &quot; Puntos de donacin que por lo menos han entregado una donacin en los ltimos tres meses &quot; 
&#160; 
 Capa seleccionada por defecto 
 Esta capa estar seleccionada por defecto, pero ser excluyente con la seleccin de la siguiente capa, es decir, si se selecciona la capa &quot;Todos los puntos&quot;, esta capa se debe des-seleccionar automticamente. 
&#160; 
 Llamados para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_actual_menos_tres_meses &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_actual &#125;&#125;&amp;eatc-state=delivered, received ,pre-certified,certified&amp;eatc-city=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp= eatc-donor,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_phone,eatc-lat,eatc-lon 
&#160; 
 Con los datos que se obtienen en eatc_dona_headers. eatc-lat y eatc_dona_headers. eatc-lon se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son puntod de donacin con actividad&#58; solicitar estos diseos a LuisK).&#160; Si hay puntos de donacin repetidos, solamente se muestra un pin por punto. 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master&#58; abaco, eatc-city=MEDELLIN, fecha actual 2023-10-15 
 El sistema debe realizar el siguiente llamado&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-publication_date[0]=2023-07-15&amp;eatc-publication_date[1]=2023-10-15&amp;eatc-state=delivered, received ,pre-certified,certified&amp;eatc-city=MEDELLIN&amp;_cmp= eatc-donor,eatc-pod_id,eatc-pod_name,eatc-pod_address,eatc-pod_phone,eatc-lat,eatc-lon &#160;&#160; &#160; 

&#160; 
 Todos los puntos de donacin (en el mapa de muestra en &quot; Donantes &quot;) 
 class=&quot; lbl_todos_los_pods &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_todos_los_pods &#160;&#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_todos_los_pods_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_todos_los_pods_desc &#160; &#160; 
&#160; 
 &quot; Puntos de donacin registrados en la plataforma &quot; 
&#160; 
 Capa NO seleccionada por defecto 
 Esta capa no estar seleccionada por defecto, si se selecciona, se debe des-seleccionar la capa &quot;Puntos de donacin con actividad&quot; (la capa anterior). 
&#160; 
 Llamados para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema debe realizar el siguiente llamado&#58; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/allpods/eatc_pods?eatc-city=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=eatc-cua,eatc-id,eatc-name,eatc-adress,eatc-phone,eatc-email,eatc-responsable,eatc_active,eatc-lat,eatc-lon 
&#160; 
 Con los datos que se obtienen en eatc_dona_headers. eatc-lat y eatc_dona_headers. eatc-lon se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son puntod de donacin&#58; solicitar estos diseos a LuisK) 
&#160; 
 Ejemplo&#58; entorno de pruebas, cua_master&#58; abaco, eatc-city=MEDELLIN 
 El sistema debe realizar el siguiente llamado&#58; 
 https&#58;//devdonantes.eatcloud.info/api/allpods/eatc_pods?eatc-city=MEDELLIN&amp;_cmp=eatc-cua,eatc-id,eatc-name,eatc-adress,eatc-phone,eatc-email,eatc-responsable,eatc_active,eatc-lat,eatc-lon &#160; 

&#160; 
 TITULO&#58; Gestores de donacin por estado (Agrupacin de filtros&#58; No est en la muestra) 
 class=&quot; lbl_doma_por_estados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_por_estados &#160; 
&#160; 
 Este ttulo agrupa las siguientes capas&#58; 
&#160; 
 Gestores de donacin activados (No est en el mapa de muestra) 
 class=&quot; lbl_doma_activados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activados &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_activados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_activados_desc &#160; 
&#160; 
 &quot; Gestores de donaciones que tienen estado &quot;activo&quot; en la plataforma, es decir, que pueden gestionar donaciones &quot; 
&#160; 
 Llamado para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_state = activo &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b&#160; 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones con estado &quot;activo&quot;&#58; solicitar estos diseos a LuisK) 

&#160; 
 Gestores de donacin inactivados (No est en el mapa de muestra) 
 class=&quot; lbl_doma_inactivados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivados &#160; &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_inactivados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_inactivados_desc &#160; 
&#160; 
 &quot; Gestores de donaciones que tienen estado &quot;inactivo&quot; en la plataforma, es decir, que no han sido aun aprobados para gestionar donaciones &quot; 
&#160; 
 Llamado para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_state = inactivo &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b&#160; 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones con estado &quot;inactivo&quot;&#58; solicitar estos diseos a LuisK) 

&#160; 
 Gestores de donacin suspendidos (No est en el mapa de muestra) 
 class=&quot; lbl_doma_suspendidos &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_suspendidos &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_suspendidos_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_suspendidos_desc &#160; 
&#160; 
 &quot; Gestores de donaciones que tienen estado &quot;suspendido&quot; en la plataforma, es decir, que no han sido inhabilitados y por lo tanto no pueden gestionar donaciones &quot; 
&#160; 
 Llamado para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_state = suspendido &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state, causal_inactivo ,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones con estado &quot;suspendido&quot;&#58; solicitar estos diseos a LuisK) 

&#160; 
 Gestores de donacin expulsados (No est en el mapa de muestra) 
 class=&quot; lbl_doma_expulsados &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_expulsados &#160; 
&#160; 
 Tooltip&#58; 
 class=&quot; lbl_doma_expulsados_desc &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_expulsados_desc &#160; 
&#160; 
 &quot; Gestores de donaciones que han sido expulsados de la plataforma &quot; 
&#160; 
 Llamado para obtener las coordenadas y la informacin de los puntos a mostrar en la respectiva capa 
 El sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_state = expulsado &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state, causal_inactivo ,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b 
&#160; 
 Con los datos que se obtienen en eatc_donation_managers. coordenadas se pintan los respectivos puntos en el mapa (con un pin distintivo, que denote que son organizaciones con estado &quot;expulsado&quot;&#58; solicitar estos diseos a LuisK) 

&#160; 
 TITULO&#58; Adscritos a (Agrupacin de filtros&#58; No est en la muestra como un ttulo) 
 class=&quot; lbl_doma_adscritos_a &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_doma_adscritos_a &#160; 
 Llamado para obtener la informacin para construir estas capas&#58; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers? eatc_state= _* &amp;municipio=&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;&amp;_distinct=organizacion_vinculada 
 Las respuestas de la anterior consulta se lleva a un &#123;&#123; array_donation_managers_code &#125;&#125; y con este array se realiza la siguiente consulta&#58; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123; array_donation_managers_code &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro 
 Con el dato que se obtiene en eatc_donation_managers. organizacin se crea el nombre de la capa y con el dato que se obtiene en eatc_donation_managers. identificador_unico_registro se realiza la consulta que trae los datos de la respectiva capa 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?organizacion_vinculada = &#123;&#123; eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;_cmp=organizacin,identificador_unico_registro,eatc_state, causal_inactivo ,departamento,municipio,unidad_territorial,coordenadas,latitud,longitud,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b 

&#160; 
 TITULO&#58; Comunas / localidades (Agrupacin de filtros&#58; En la muestra aparece como &quot;Medelln&quot;) 
 class=&quot; lbl_comunas_localidades &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_comunas_localidades &#160; 
&#160; 
 Segn el municipio en dnde se centre el mapa (&#123;&#123;eatc_municipalities. eatc-city &#125;&#125;), se deben consultar sus respectivas localidades o comunas y mostrar una geocelda que las colore.&#160; Se podrn seleccionar o no capas de estas geoceldas. &#160; Se debe iniciar por Medelln ( https&#58;//www.medellin.gov.co/geomedellin/datosAbiertos/243 ) y luego incorporarlas a Bogot, Cali, Barranquilla, Armenia, Manizales, Pereira y luego dems ciudades capitales del pas. 

&#160; 
 I NFORMACIN A MOSTRAR AL HACER CLIC EN UN PIN ESPECFICO&#58; GESTORES DE DONACIN 
 Cuando se hace clic en un pin especfico (coordenada de gestor de donaciones), el sistema muestra la siguiente informacin del gestor de donacin especfico&#58; 
&#160; 
 Nombre 
 class=&quot; lbl_nombre &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_nombre &#160; &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. organizacin 
&#160; 
 Identificacin tributaria 
 class=&quot; lbl_fiscal_id &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_fiscal_id &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. identificador_unico_registro 
&#160; 
 Estado 
 class=&quot; lbl_estado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_estado &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. eatc_state 
&#160; 
 Causal inactivo 
 class=&quot; lbl_causal_inactivo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_causal_inactivo &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. causal_inactivo 
&#160; 
 Departamento 
 class=&quot; lbl_departamento_provincia_estado &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_departamento_provincia_estado &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. departamento 
&#160; 
 Ciudad 
 class=&quot; lbl_ciudad &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_ciudad &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. municipio 
&#160; 
 Direccin 
 class=&quot; lbl_direccion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_direccion &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. unidad_territorial 
 Coordenadas 
 class=&quot; lbl_coordenadas &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_coordenadas &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. coordenadas 
&#160; 
 Latitud 
 class=&quot; lbl_lat &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lat &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. latitud 
 Longitud 
 class=&quot; lbl_lon &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lon &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. longitud 
&#160; 
 Correo electrnico 
 class=&quot; lbl_correo_electronico &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_correo_electronico &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. correo_electronico 
&#160; 
 Representante legal 
 class=&quot; lbl_representante_legal &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_representante_legal &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. representante_legal 
&#160; 
 Telfono 1 
 class=&quot; lbl_tel1 &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_tel1 &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. telefono1 
&#160; 
 Telfono 2 
 class=&quot; lbl_tel2 &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_tel2 &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. telefono2 
&#160; 
 Capacidad de recogida 
 class=&quot; lbl_capacidad_recogida &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_capacidad_recogida &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. capacidad_recogida 
&#160; 
 Capacidad de gestin 
 class=&quot; lbl_capacidad_gestion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_capacidad_gestion &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. capacidad_gestion 
&#160; 
 Tipo de organizacin 
 class=&quot; lbl_tipo_organizacion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_tipo_organizacion &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_donation_managers. eatc_doma_typology_b 
&#160; 
 Organizacin vinculada 
 class=&quot; lbl_organizacion_vinculada &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_organizacion_vinculada &#160; 
&#160; 
 Con la informacin que llega en&#160; eatc_donation_managers. organizacion_vinculada 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?identificador_unico_registro=&#123;&#123; eatc_donation_managers. organizacion_vinculada &#125;&#125;&amp;_cmp=organizacin 
&#160; 
 Muestra la informacin que se encuentra en (segn la anterior consulta)&#58; 
 eatc_donation_managers. organizacin 

&#160; 
 I NFORMACIN A MOSTRAR AL HACER CLIC EN UN PIN ESPECFICO&#58; PUNTOS DE DONACIN CON ACTIVIDAD 
&#160; 
 Cuando se hace clic en un pin especfico (coordenada de un punto de donacin con actividad), el sistema muestra la siguiente informacin del gestor de donacin especfico&#58; 
&#160; 
 Nombre 
 class=&quot; lbl_nombre &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_nombre &#160; &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-pod_name 
&#160; 
 Cdigo 
 class=&quot; lbl_codigo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_codigo &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-pod_id 
&#160; 
 Donante 
 class=&quot; lbl_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donante &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-donor 
&#160; 
 Direccin 
 class=&quot; lbl_direccion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_direccion &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-pod_address 
&#160; 
 Latitud 
 class=&quot; lbl_lat &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lat &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-lat 
&#160; 
 Longitud 
 class=&quot; lbl_lon &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lon &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-lon 
&#160; 
 Telfono 
 class=&quot; lbl_telefono &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_telefono &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-pod_phone 
&#160; 

 I NFORMACIN A MOSTRAR AL HACER CLIC EN UN PIN ESPECFICO&#58; TODOS LOS PUNTOS DE DONACIN 
&#160; 
 Cuando se hace clic en un pin especfico (coordenada de punto de donacin&#58; filtro&#58; todos los puntos), el sistema muestra la siguiente informacin del gestor de donacin especfico&#58; 
&#160; 
 Nombre 
 class=&quot; lbl_nombre &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_nombre &#160; &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-name 
&#160; 
 Cdigo 
 class=&quot; lbl_codigo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_codigo &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-id 
&#160; 
 Donante 
 class=&quot; lbl_donante &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_donante &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-cua 
&#160; 
 Direccin 
 class=&quot; lbl_direccion &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_direccion &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-adress 
&#160; 
 Latitud 
 class=&quot; lbl_lat &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lat &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-lat 
&#160; 
 Longitud 
 class=&quot; lbl_lon &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_lon &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_dona_headers. eatc-lon 
&#160; 
 Telfono 
 class=&quot; lbl_telefono &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_telefono &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-phone 
&#160; 
 Activo 
 class=&quot; lbl_activo &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_activo &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc_active 
&#160; 
 Responsable 
 class=&quot; lbl_responsable &quot;&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_responsable &#160; 
&#160; 
 Muestra la informacin que se encuentra en&#58; 
 eatc_pods. eatc-responsable 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 MAPA