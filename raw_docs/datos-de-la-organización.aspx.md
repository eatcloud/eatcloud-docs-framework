# datos-de-la-organización.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 TTULO DEL FORMULARIO&#58; INFORMACIN DE LA ORGANIZACIN 
 clase = lbl_info_org ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_info_org )&#160; 
&#160; 
 Consulta para mostrar la informacin&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Si la consulta no arroja resultados, muestra el siguiente label&#58;&#160; 
&#160; 
 La informacin de la organizacin adscrita a la cuenta maestra no existe.&#160; Si desea configurarla puedes utilizar el siguiente formulario&#58; 
 clase = lbl_info_org_no_config ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_info_org_no_config )&#160;&#160; 
&#160; 
 Y adems el formulario&#160; de informacin de la organizacin deber presentar el siguiente campo&#58; prellenado (no se debe poder cambiar) 
&#160; 
 Identificador (en el mockup no est)&#58; 
 Label&#58; 
 clase = lbl_identificador ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_identificador )&#160;&#160; 
&#160; 
 Caracterizacin del campo&#58; 
 Valor&#58; muestra el dato&#160; ( &#123;&#123; _DOM.cua_master &#125;&#125; ) el cual no puede ser editado y debe llevarse a la variable 
 &#123;&#123; identificador&#125;&#125; 
&#160; 
 Si la consulta arroja resultados, se procede a realizar a desplegar el siguiente formulario&#58; 
&#160; 
 FORMULARIO&#58; INFORMACIN DE LA ORGANIZACIN 
&#160; 
 Identificacin tributaria (en el mockup est de segundo, pero debe mostrarse de primero)&#58; 
 Label&#58; 
 clase = lbl_identificacion_tributaria ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_identificacion_tributaria )&#160; 
&#160; 
 Caracterizacin del campo&#58; Primera etapa 
 Valor&#58; muestra el Identificador nico de registro ( &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; ) el cual no puede ser editado &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123; identificador_unico_registro &#125;&#125;&amp;_cmp= identificador_unico_registro &#160; 

&#160; 
 Caracterizacin del campo&#58; Segunda etapa (deber permitir editar el campo pero solo a usuarios de EatCloud) 
 Tooltip&#58; &quot;Ingrese el identificador nico de la organizacin - identificacin tributaria&quot; 
 clase = lbl_ingrese_identificador_unico_org (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ingrese_identificador_unico_org )&#160;&#160;&#160; 
&#160; 
 Concatenado con&#160; 
&#160; 
 clase = lbl_identificacion_tributaria ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_identificacion_tributaria )&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= identificador_unico_registro &#160; 
 Tipo de dato&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp=eatc_doma_id_datatype &#160; 
 Tipo de input&#58; Segn el tipo de dato&#58; Input numrico (integer), Text input (string) 
 Obligatoriedad &#58; si 
 Validaciones &#58;&#160; 
 Obligatoriedad 
 Tipo de dato 
 Tamao mnimo de caracteres&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp=eatc_doma_id_min_digit_val &#160; 

 Tamao mximo de caracteres&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp=eatc_doma_id_max_digit_val &#160; 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; identificador_unico_registro &#125;&#125; 

&#160; 
&#160; 
 Razn social (en el mockup est de primera, pero debe mostrarse de segunda)&#58; 
 Label&#58; 
 clase = lbl_razon_social ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_razon_social )&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Digita el nombre de la organizacin&quot; 
 clase = lbl_razon_social_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_razon_social_desc )&#160;&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= organizacin 
 Tipo de dato&#58; string 
 Tipo de input&#58; text input 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; organizacin &#125;&#125; 

&#160; 
&#160; 
 Departamento / Provincia / Estado (en el mockup no est)&#58; 
 Label&#58; 
 clase = lbl_departamento_provincia_estado ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_departamento_provincia_estado )&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Utiliza el texto predictivo para ingresar el (la) departamento / provincia / estado &quot; 
 clase = lbl_utiliza_texto_predictivo_para_ingresar (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_utiliza_texto_predictivo_para_ingresar )&#160;&#160;&#160;&#160; 
&#160; 
 Concatenado 
&#160; 
 clase = lbl_departamento_provincia_estado ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_departamento_provincia_estado ) 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= departamento 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto predictivo 
 Para determinar de donde se toma el texto predictivo se debe&#58; 
 Consultar el pas de la respectiva cuenta maestra 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM.cua_master&#125;&#125;&amp;_cmp= eatc_country &#160; 
 Con el pas consultar los respectivos departamentos disponibles de la siguiente manera 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_country &#125;&#125;/eatc_municipalities?_id=_*&amp;_distinct=eatc-province &#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; departamento &#125;&#125; 
&#160; 
&#160; 
 Ciudad&#58; 
 Label&#58; 
 clase = lbl_ciudad ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ciudad )&#160; 
&#160; 
 Tooltip&#58; &quot;Utiliza el texto predictivo para ingresar la ciudad &quot; 
 clase = lbl_utiliza_texto_predictivo_para_ingresar_la (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_utiliza_texto_predictivo_para_ingresar_la )&#160;&#160;&#160;&#160; 
&#160; 
 Concatenado 
&#160; 
 clase = lbl_ciudad ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ciudad )&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= municipio 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto predictivo 
 Para determinar de donde se toma el texto predictivo se debe&#58; 
 Con los datos de la consulta anterior se debe realizar la siguiente consulta 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/&#123;&#123;eatc_cua_master. eatc_country &#125;&#125;/eatc_municipalities?eatc-province=&#123;&#123; departamento &#125;&#125;&amp;_distinct= eatc-city &#160; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; municipio &#125;&#125; 
&#160; 
&#160; 
 Direccin domicilio principal&#58; 
 Label&#58; 
 clase = lbl_direccion_domicilio_ppal ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_direccion_domicilio_ppal )&#160; 
&#160; 
 Tooltip&#58; &quot;Digita la direccin principal de la organizacin&quot; 
 clase = lbl_direccion_domicilio_ppal_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_direccion_domicilio_ppal_desc )&#160;&#160;&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= unidad_territorial 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; unidad_territorial &#125;&#125; 
&#160; 
&#160; 
 Telfono&#58; 
 Label&#58; 
 clase = lbl_telefono ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_telefono )&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Digita el telfono principal de la organizacin&quot; 
 clase = lbl_telefono_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_telefono_desc )&#160;&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= telefono1 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; telefono1 &#125;&#125; 

&#160; 
 Correo electrnico (no est en el diseo)&#58; 
 Label&#58; 
 clase = lbl_correo_electronico ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_correo_electronico )&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Digita el correo electrnico principal de la organizacin&quot; 
 clase = lbl_correo_electronico_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_correo_electronico_desc )&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= correo_electronico 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; correo_electronico &#125;&#125; 
&#160; 
&#160; 
 Representante legal&#58; 
 Label&#58; 
 clase = lbl_representante_legal ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_representante_legal )&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Digita el nombre completo del representante legal de la organizacin&quot; 
 clase = lbl_telefono_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_representante_legal_desc )&#160;&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_donation_managers?identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_cmp= representante_legal 
 Tipo de dato&#58; string 
 Tipo de input&#58; Texto 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 El input se lleva a la variable (para su posterior registro) 
 &#123;&#123; representante_legal &#125;&#125; 
&#160; 
&#160; 
 LLAMADO AL CRD PARA ACTUALIZACIN / CREACIN DEL REGISTRO 
 Actualizacin / Edicin&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; identificador_unico_registro =&#123;&#123; identificador_unico_registro &#125;&#125;&amp; organizacin =&#123;&#123;organizacin&#125;&#125; &amp; departamento =&#123;&#123;departamento&#125;&#125; &amp; municipio =&#123;&#123;municipio&#125;&#125; &amp; unidad_territorial =&#123;&#123;unidad_territorial&#125;&#125; &amp; telefono1 =&#123;&#123;telefono1&#125;&#125; &amp; correo_electronico =&#123;&#123;correo_electronico&#125;&#125; &amp; representante_legal =&#123;&#123;representante_legal&#125;&#125; &amp; WHERE identificador=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 Creacin&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_donation_managers&amp;_operacion=insert&amp;identificador=&#123;&#123;_DOM. cua_master &#125;&#125;&amp; identificador_unico_registro =&#123;&#123; identificador_unico_registro &#125;&#125;&amp; organizacin =&#123;&#123;organizacin&#125;&#125; &amp; departamento =&#123;&#123;departamento&#125;&#125; &amp; municipio =&#123;&#123;municipio&#125;&#125; &amp; unidad_territorial =&#123;&#123;unidad_territorial&#125;&#125; &amp; telefono1 =&#123;&#123;telefono1&#125;&#125; &amp; correo_electronico =&#123;&#123;correo_electronico&#125;&#125; &amp; representante_legal =&#123;&#123;representante_legal&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdatos-de-la-organizaci%C3%B3n%2F3863974135-Informacion_empresa.jpg&ow=709&oh=593, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdatos-de-la-organizaci%C3%B3n%2F3863974135-Informacion_empresa.jpg&ow=709&oh=593 
 Nuevo BO CUA MASTER Beneficiarios 

 728.000000000000 

 DATOS DE LA ORGANIZACIN