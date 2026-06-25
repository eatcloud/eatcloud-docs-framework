# new-wapp-informe-de-revisión-de-cancelados.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 NOTA PARA EL DESARROLLO &#58;&#160; Este informe se puede basar en el informe de pesos excesivos, dado que su documentacin es muy similar y sirvi como modelo para esta. 

 Etiquetas encabezado del informe&#58; 
 Informe de revisin de cancelados 
 Label &#58; class=&quot;lbl_info_revision_cancelados&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_info_revision_cancelados )&#160;&#160;&#160; 
&#160; 
 Informe de revisin de cancelados&#58; descripcin 
 Label &#58; class=&quot;lbl_info_revision_cancelados_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_info_revision_cancelados_desc )&#160;&#160;&#160; 
&#160; 
 En este informe podrs revisar las donaciones canceladas, con pesos altos, para analizar si las puedes liberar de nuevo para que las tomen nuestros beneficiarios. 
&#160; 
 Filtrar 
 Label &#58; class=&quot;lbl_filtrar&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_filtrar )&#160; 

 FILTRO DE PESO 
 Donaciones canceladas con peso mayor o igual a&#58; 
 Label &#58; class=&quot;lbl_canceladas_mayores_a&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_canceladas_mayores_a )&#160;&#160;&#160; 
&#160; 
 Campo de Captura (integer input)&#58; 
 Se deber implementar un tipo campo de captura de nmeros enteros, que permita establecer el peso con el cual se evala si las donaciones canceladas que son mayores al dicho campo de captura , cuyo valor por defecto sea 50, y que permita filtrar (junto con el selector de fechas que se describe ms abajo), los anuncios cancelados que se van a revisar&#58; 
 Tipo de dato&#58; integer 
 Tipo de input&#58; integer input 
 Valor por defecto&#58; 50 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
en la variable&#58; &#123;&#123;KG&#125;&#125; que se utiliza ms adelante. 
&#160; 
 Leyenda despus del campo de captura&#58; KG 
 Se coloca inmediatamente despus del campo de captura anterior, para denotar que en el mismo se ingresan KG (Kilogramos). 
 Label &#58; class=&quot;lbl_kg&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_kg )&#160;&#160;&#160;&#160; 
&#160; 
 FILTRO DE FECHAS 
 Se deber implementar un filtro de fechas, cuyo valor por defecto sea el mes actual, y que permita filtrar al seleccionar una fecha inicial y una fecha final, los anuncios de ese periodo.&#160; Los dems filtros del informe (Filtro por estados abreviados) operarn para donaciones de las fechas seleccionadas&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ /eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125; &amp; eatc_cua_origin =&#123;&#123;_DOM .cua_user &#125;&#125; &amp; eatc-original_weight_kg = _&gt;_ &#123;&#123;KG&#125;&#125; &amp; eatc-pod_id =&#123;&#123; eatc-pod_id &#125;&#125;&amp; eatc-state = cancelled &amp;_cmp=eatc-code,eatc-publication_datetime,eatc-state,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-pod_id,eatc-original_weight_kg, eatc_excessive_weight_kg_ref, eatc-state,eatc-donation_manager_name,eatc-donation_manager_phone 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; = &gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_mes_actual )&#160;&#160;&#160;&#160; 
 &#123;&#123; fecha_inicial_periodo &#125;&#125; = Primer da del mes actual 
 &#123;&#123; fecha_final_periodo &#125;&#125; &#160; = Da actual 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_personalizar )&#160; 
&#160; 
 Este filtro debe aparecer, pero si la licencia rescate es &quot;free&quot;, al accionarlo solo podr consultar hasta 7 das atrs del da actual) 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= type 
&#160; 
 La respuesta corresponde a eatc_cua. type = free caso en el cual en vez de presentarle las opciones de seleccionar las fechas inIcial y final a libre eleccin, solo le permitir seleccionar fechas entre el rango de fechas del da actual y siete das antes. 
&#160; 
 Si la respuesta a la anterior consulta da como resultado 
&#160; 
eatc_cua. type = esencial eatc_cua. type = activo &#160; eatc_cua. type = impacto se permitir configurar las fechas a libre eleccin, del informe que se presenta ms adelante . 
&#160; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_personalizar )&#160;&#160;&#160;&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_fecha_inicial ) &#160; =&gt; &#123;&#123; fecha_inicial_periodo &#125;&#125;&#160; 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_fecha_final )&#160; =&gt; &#123;&#123; fecha_final_periodo &#125;&#125; 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_consultar ) 
 &#160; 
 Label para cuando la consulta no trae resultados&#58; &quot;No existen anuncios de donacin cancelados con peso mayor o igual al indicado&quot; 
 Label &#58; class=&quot;lbl_sin_cancelados&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel=lbl_sin_cancelados )&#160; &#160;&#160; 

 INFORME PARA REVISIN DE CANCELADOS 
 El sistema deber construir una Datatable , con ordenamiento por columnas y buscador , que contenga la siguiente informacin. 
&#160; 
 Cdigo&#58; 
 Label&#58; class=&quot; lbl_codigo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-code 

&#160; 
 Fecha publicacin&#58; 
 Label&#58; class=&quot; lbl_fecha_publicacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_fecha_publicacion )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-publication_datetime 

&#160; 
 Estado&#58; 
 Label&#58; class=&quot; lbl_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_estado )&#160;&#160;&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-state =&gt; Debe ser siempre &quot;Cancelled&quot; 

&#160; 
 Peso (KG)&#58; 
 Label&#58; class=&quot; lbl_peso_kg &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_peso_kg )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-original_weight_kg 

&#160; 
 Editar donacin&#58; 
 Label 
 class=&quot; lbl_editar_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_editar_donacion )&#160;&#160;&#160;&#160; 
 Este botn deber dar acceso a la funcionalidad de &quot; Edicin de donacin &quot; (tal cual se maneja en la ACTUAL WAPP). 
&#160; 
 Liberar donacin 
 class=&quot; lbl_libdona &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =webapp&amp;idlabel= lbl_libdona )&#160; 
&#160; 
 Debe presentar un botn con el mismo label, por cada anuncio de donacin en el informe.&#160; Si el usuario oprime un botn para un anuncio en cuestin, se debe realizar lo siguiente ( Funcionalidad ya implementada en la WAPP ) 

 DONACIONES CANCELADAS&#58; SELECCIONA UN CAUSAL DE LIBERACIN 
 Label del ttulo 
 class=&quot; lbl_selecciona_causal_liberacin &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;idlabel= lbl_selecciona_causal_liberacin )&#160;&#160;&#160;&#160; 
&#160; 
 Selector nico 
 Valor por defecto 
 Vaco (ninguno seleccionado) 
&#160; 
 Valores del selector 
 El sistema, tomando el estado de la donacin ( eatc_dona_headers. eatc-state ), realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_release_causes?eatc_cua_master= _default &amp;eatc_cua_user= _default &amp;eatc_dona_state= cancelled &amp;_cmp=eatc_name,eatc_cause_label 
&#160; 
 En principio se realiza el llamado con para cua_master y eatc_cua_user = _default (se deja la puerta para que posteriormente se pueda dinamizar por eatc_cua_master y eatc_cua_user ). 
&#160; 
 Se coloca como &quot; class &quot; (para la internacionalizacin de las etiquetas de las opciones) el valor contenido en eatc_dona_ralease_causes. eatc_cause_label y el valor entre los tags eatc_dona_ralease_causes. eatc_name 
&#160; 
 Ejemplo&#58; ambiente de produccin, cua_master&#58; abaco , eatc-state= cancelled 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_release_causes?eatc_cua_master=_default&amp;eatc_cua_user=_default&amp;eatc_dona_state=cancelled&amp;_cmp=eatc_name,eatc_cause_label &#160; 
&#160; 
 Por lo tanto las opciones que se desplegarn son&#58; 
 Toda la mercanca apta para el consumo humano ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_toda_dona_ok )&#160;&#160; 
 La mayor parte de la mercanca apta para el consumo humano ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel=lbl_casi_toda_dona_ok )&#160; 
&#160; 
 Valores a guardar a partir de la seleccin para posterior llamado al servicio 
 A partir de la seleccin del usuario el sistema guardar el valor contenido en eatc_dona_release_causes. eatc_cause_label como valor para hacer el posterior llamado al servicio de liberacin. 

&#160; 
 Botn &quot;Confirmar liberacin&quot; 
 class=&quot; lbl_confirmar_liberacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirmar_liberacion )&#160;&#160; 
&#160; 
 Al oprimir el botn, y con la informacin del Punto de donacin, la donacin y la causal de liberacin el sistema deber llamar al servicio de liberacin de anuncios tal cual se especifica en la documentacin del servicio pblico (se incorporan parmetros de autenticacin en la cabecera del llamado). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nueva WAPP 

 NUEVO: INFORME DE REVISIN DE CANCELADOS