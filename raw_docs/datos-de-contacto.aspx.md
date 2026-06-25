# datos-de-contacto.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Ttulo&#58; Datos de contacto gestores de donaciones 
 label&#58; class=&quot;lbl_datos_contacto_doma&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_datos_contacto_doma &#160; 
&#160; 
 Descripcin&#58; &quot;En esta seccin encontrars los datos de contacto que los gestores de donaciones registraron en EatCloud&quot; 
 label&#58; class=&quot;lbl_datos_contacto_doma_desc&quot;&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_datos_contacto_doma_desc &#160; 

 Listado paginado, ordenado y descargable 
 Se deben utilizar las funciones de paginado y ordenamiento definidas para las consultas (si las mismas no funcionan como estn en la documentacin se deber contactar a Jess Ramrez para la revisin de las funciones y su despliegue en los ambientes &quot;beneficiario&quot;&#58; dev y produccin), con el nimo de construir un listado paginado (con 20 resultados mximo por pgina) y ordenado alfabticamente por el Nombre de la organizacin.&#160; El reporte se podr descargar en formato .csv y excel. 
&#160; 
 Filtro de estados 
 Para obtener los estados que se desplegarn en un selector nico como criterios de filtro, se debe realizar la siguiente consulta&#58; 
&#123;&#123; URL_entorno_datagov &#125;&#125; /api/eatcloud/eatc_doma_states?active_status=y&amp;eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct=eatc_state_lbl 
&#160; 
 Ejemplo &#58; cua_master&#58; abaco , ambiente de pruebas 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_doma_states?active_status=y&amp;eatc_cua_master= abaco&amp;_distinct=eatc_state_lbl &#160;&#160; 
&#160; 
 A los filtros que se obtienen en la consulta, se les deber adicionar la opcin &quot; Todos &quot;, como se indica ms adelante 
&#160; 
 Segn sea el tipo de organizacin determinada en el proceso de login , se aplicar un filtro diferenciado para traer los datos (a los usuarios tipo cua_master no les aplican los nuevos filtros de informacin y por lo tanto para ellos el BO funciona tal como funciona en su primera implementacin) 
&#160; 
 Filtro&#58; &quot;Todos&quot; =&gt; Filtro por defecto 
 class=&quot; lbl_todos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_todos ) 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista (todos los gestores de donaciones)&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_beneficiarios_adscritos &#125;&#125; &amp;_cmp=organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b&#160; 

&#160; 
 Ejemplo&#58; ambiente de pruebas, cuenta maestra&#58; abaco 
Por defecto el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco /eatc_donation_managers? identificador_unico_registro = _*&amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &#160; 

&#160; 
 Filtro&#58; &quot;Inactivo&quot; 
 class=&quot; lbl_inactivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_inactivo )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_beneficiarios_adscritos &#125;&#125; &amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &amp;eatc_state =inactivo 

&#160; 
 Ejemplo&#58; ambiente de pruebas, cuenta maestra&#58; abaco 
Por defecto el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco /eatc_donation_managers? identificador_unico_registro = _*&amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &amp;eatc_state =inactivo &#160; 
&#160; 
Con los registros obtenidos, se debe construir el listado que ms abajo se especifica. 
&#160; 
 Filtro&#58; &quot;Activo&quot; 
 class=&quot; lbl_activo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_activo )&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_beneficiarios_adscritos &#125;&#125; &amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &amp;eatc_state =activo 
&#160; 
 Filtro&#58; &quot;Suspendido&quot; 
 class=&quot; lbl_suspendido &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_suspendido )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_beneficiarios_adscritos &#125;&#125; &amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &amp;eatc_state =suspendido 
&#160; 
 Filtro&#58; &quot;Expulsado&quot; 
 class=&quot; lbl_expulsado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_expulsado )&#160;&#160; 
&#160; 
 Al seleccionar este filtro el sistema debe realizar la siguiente consulta para desplegar los resultados de la lista&#58; 
&#160; 
&#123;&#123; URL_entorno_beneficarios &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125; /eatc_donation_managers? identificador_unico_registro = &#123;&#123; array_beneficiarios_adscritos &#125;&#125; &amp;_cmp= organizacin,identificador_unico_registro,eatc_state,departamento,municipio,unidad_territorial,coordenadas,correo_electronico,representante_legal,telefono1,telefono2,telefono3,capacidad_recogida,capacidad_gestion,organizacion_vinculada,eatc_doma_typology_b &amp;eatc_state =expulsado 

&#160; 
 Botn&#58; &quot;Descargar&quot; 
 class=&quot; lbl_descargar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_descargar )&#160; 
&#160; 
 Al presionar este botn se descargarn los datos de la siguiente lista segn el criterio de filtro aplicado. 

 Listado de contactos de Gestores de Donaciones 
 El listado estar compuesto por las siguientes columnas&#58; 
&#160; 
 Nombre de la organizacin =&gt; Ordenar alfabticamente por este campo la lista&#58; 
 class=&quot; lbl_nombre_organizacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_nombre_organizacion )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . organizacin 

&#160; 
 NIT&#58; 
 class=&quot; lbl_identificacion_tributaria &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_identificacion_tributaria )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . identificador_unico_registro 

&#160; 
 Estado&#58; 
 class=&quot; lbl_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_estado )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . eatc_state 

&#160; 
 Ciudad&#58; 
 class=&quot; lbl_ciudad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ciudad )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers . municipio 

&#160; 
 Direccin&#58; 
 class=&quot; lbl_direccion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_direccion ) 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .unidad_territorial 

&#160; 
 Correo electrnico&#58; 
 class=&quot; lbl_doma_email &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_doma_email )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .correo_electronico 

&#160; 
 Representante legal&#58; 
 class=&quot; lbl_rep_legal &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_rep_legal ) 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .representante_legal 

&#160; 
 Telfono 1&#58; 
 class=&quot; lbl_tel1 &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_tel1 )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .telefono1 

&#160; 
 Telfono 2&#58; 
 class=&quot; lbl_tel2 &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_tel2)&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .telefono2 

&#160; 
 Telfono 3&#58; 
 class=&quot; lbl_tel2 &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_tel3)&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .telefono3 

&#160; 
 Capacidad de recogida&#58; 
 class=&quot; lbl_capacidad_recogida &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_capacidad_recogida )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers. capacidad_recogida 

&#160; 
 Capacidad de gestin&#58; 
 class=&quot; lbl_capacidad_gestion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_capacidad_gestion ) 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers. capacidad_gestion 

&#160; 
 Organizacin vinculada&#58; 
 class=&quot; lbl_organizacion_vinculada &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_organizacion_vinculada &#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers. organizacion_vinculada 

&#160; 
 Tipo organizacin&#58; 
 class=&quot; lbl_tipo_organizacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_tipo_organizacion )&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_donation_managers .eatc_doma_typology_b 

&#160; 
 NOTA PARA EL DESARROLLO&#58; en estos dos ltimos casos (nombre y correo de quien usa la APP), se debe evaluar si al hacer una consulta cruzada, esto recarga al informe, caso en el cual se deben traer primer los datos que hasta este punto se han establecido y luego ir trayendo los dos datos que a continuacin se definen, colocando un &quot;loader&quot; mientras estos datos cargan (en cada fila) 
&#160; 
 El sistema con el dato contenido en eatc_donation_managers . identificador_unico_registro realiza la siguiente consulta&#58;&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;api/&#123;&#123;cua_master&#125;&#125;/eatc_users?organizacion=&#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;_cmp= contratista,correo_electronico &amp;_token=eb20a489e56e3294e66b2ffe4809ec40&#160; 
&#160; 
 Usa la App&#58; Nombre 
 class=&quot; lbl_usa_la_app_nombre &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_usa_la_app_nombre)&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_users . contratista 
&#160; 
 Usa la App&#58; e-mail 
 class=&quot; lbl_usa_la_app_nombre &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_usa_la_app_nombre)&#160; 
&#160; 
 Mostrar la informacin contenida en el parmetro&#58; eatc_users . correo_electronico 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 DATOS DE CONTACTO (BENEFICIARIOS)