# perfil-de-usuario-nuevo-bo-cua-master-beneficiarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 TTULO DEL FORMULARIO&#58; AJUSTES PERFIL DE USUARIO 
&#160; 
 clase = lbl_ajustes_perfil_usuario (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_ajustes_perfil_usuario ) 

 E-mail (en el mockup est de segundo, pero debe mostrarse de primero)&#58; 
&#160; 
 Label&#58; 
 clase = lbl_correo_electronico ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_correo_electronico )&#160; 
&#160; 
 Caracterizacin del campo&#58; 
 Valor&#58; muestra el email del usuario ( &#123;&#123; email_usuario &#125;&#125; ) el cual no puede ser editado &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/bo_usuarios?email=&#123;&#123;email_usuario&#125;&#125;&amp;_cmp=email &#160; 
&#160; 
&#160; 
 Nombre (en el mockup est de primero, pero debe mostrarse de segundo)&#58; 
&#160; 
 Label&#58; 
 clase = lbl_nombre ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_nombre )&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Nombre de quin est utilizando la presente plataforma&quot; 
 clase = lbl_nombre_usuario_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_nombre_usuario_desc )&#160;&#160;&#160; 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/bo_usuarios?email=&#123;&#123; email_usuario &#125;&#125;&amp;_cmp=nombre_usuario &#160; 
 Tipo de dato&#58; string 
 Tipo de input&#58; text input 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
&#160; 
 Llamado al CRD para creacin del registro 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=bo_usuarios&amp;_operacion=update&amp; nombre_usuario =&#123;&#123; input &#125;&#125;&amp; WHERE email=&#123;&#123; email_usuario &#125;&#125; 
&#160; 
 * Por la naturaleza del campo, se entiende que no se debe realizar edicin de registro en&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_users?_id=_* (por favor verificar si el planteamiento es correcto) 
&#160; 
&#160; 
 Cargo&#58; 
&#160; 
 Label&#58; 
 clase = lbl_cargo ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_cargo )&#160;&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Cargo del usuario dentro de la organizacin&quot; 
 clase = lbl_cargo_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_cargo_desc ) 
&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58; &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM.cua_master&#125;&#125;/bo_usuarios?email=&#123;&#123;email_usuario&#125;&#125;&amp;_cmp=eatc_position &#160; 
 Tipo de dato&#58; string 
 Tipo de input&#58; text input 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
&#160; 
 Llamado al CRD para creacin del registro 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=bo_usuarios&amp;_operacion=update&amp; eatc_position =&#123;&#123; input &#125;&#125;&amp; WHERE email=&#123;&#123; email_usuario &#125;&#125; 
&#160; 
 * Por la naturaleza del campo, se entiende que no se debe realizar edicin de registro en&#58; &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_users?_id=_* (por favor verificar si el planteamiento es correcto) 
&#160; 
&#160; 
 Nueva contrasea&#58; 
&#160; 
 Label&#58; 
 clase = lbl_new_pass ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_new_pass )&#160;&#160;&#160; 
&#160; 
 Tooltip&#58; &quot;Digite una nueva contrasea&quot; 
 clase = lbl_new_pass_desc ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_new_pass_desc )&#160;&#160;&#160; 
&#160; 
 Place holders 
 clase = lbl_password ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_password )&#160; 
&#160; 
 Confirmar contrasea 
 clase = lbl_confirm_pass ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_confirm_pass )&#160; 

&#160; 
 Caracterizacin del Input&#58; 
 Valor por defecto&#58;&#160; Contrasea guardada en Firebase&#160; 
 Tipo de dato&#58; string 
 Tipo de input&#58; text input 
 Obligatoriedad &#58; si 
 Validacin &#58; Que las dos contraseas sean idnticas 
&#160; 
 Llamado al CRD para creacin del registro 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=bo_usuarios&amp;_operacion=update&amp; clave =&#123;&#123; input &#125;&#125;&amp; WHERE email=&#123;&#123; email_usuario &#125;&#125; =&gt; Se debe hashear? 
&#160; 
 Se debe llamar al servicio de Firebase para actualizar la contrasea 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fperfil-de-usuario-nuevo-bo-cua-master-beneficiarios%2F1090119620-Ajustes_perfil_usuario.jpg&ow=683&oh=500, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fperfil-de-usuario-nuevo-bo-cua-master-beneficiarios%2F1090119620-Ajustes_perfil_usuario.jpg&ow=683&oh=500 
 Nuevo BO CUA MASTER Beneficiarios 

 723.000000000000 

 PERFIL DE USUARIO