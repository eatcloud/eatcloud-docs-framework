# new-informe-de-pesos-excesivos-bo.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Etiquetas encabezado del informe&#58; 

 Informe de peso excesivo 
 Label &#58; class=&quot;lbl_info_peso_excesivo&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_peso_excesivo )&#160;&#160;&#160; 
&#160; 
 Listado de donaciones&#58; descripcin 
 Label &#58; class=&quot;lbl_info_peso_excesivo_desc&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_info_peso_excesivo_desc )&#160; 
&#160; 
 En este informe podrs ver donaciones con pesos excesivos, para corregirlos de ser el caso. 
&#160; 
 Filtrar 
 Label &#58; class=&quot;lbl_filtrar&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_filtrar )&#160; 

 FILTRO DE FECHAS 
 Se deber implementar un filtro de fechas, cuyo valor por defecto sea el mes actual, y que permita filtrar al seleccionar una fecha inicial y una fecha final, los anuncios de ese periodo.&#160; Los dems filtros del informe (Filtro por estados abreviados) operarn para donaciones de las fechas seleccionadas&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-pod_id=&#123;&#123; eatc-pod_id &#125;&#125; &amp; eatc_cua_origin =&#123;&#123; _DOM .cua_user &#125;&#125; &amp; eatc_excessive_weight= y &amp;_cmp=eatc-code,eatc-publication_datetime,eatc-state,eatc-donor,eatc_cua_origin,eatc-pod_name,eatc-pod_id,eatc-original_weight_kg, eatc_excessive_weight_kg_ref, eatc-state,eatc-donation_manager_name,eatc-donation_manager_phone 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; = &gt; Valor por defecto 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual )&#160;&#160;&#160; 
 &#123;&#123; fecha_inicial_periodo &#125;&#125; = Primer da del mes actual 
 &#123;&#123; fecha_final_periodo &#125;&#125; &#160; = Da actual 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_personalizar ) 
&#160; 
 Este filtro debe aparecer, pero si la licencia rescate es &quot;free&quot;, al accionarlo no debe abrir el selector de fecha inicial y final, sino que debe redireccionar a pgina de upgrade 
 Actualmente la opcin de filtro &quot;personalizar&quot; se ocult, permitiendo solamente la opcin &quot;mes actual&quot;.&#160; La idea es reactivar la opcin, pero el sistema debe evaluar mediante la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;_distinct= type 
&#160; 
 La respuesta corresponde a eatc_cua. type = free caso en el cual en vez de presentarle las opciones de seleccionar las fechas inicial o final, se debe redireccionar a la pgina de upgrade por configuracin de fechas . 
&#160; 
 Si la respuesta a la anterior consulta da como resultado 
eatc_cua. type = esencial eatc_cua. type = activo &#160; eatc_cua. type = impacto se permitir configurar las fechas del informe mediante la funcionalidad que se define adelante . 

&#160; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_personalizar )&#160;&#160;&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial )&#160; =&gt; &#123;&#123; fecha_inicial_periodo &#125;&#125;&#160; 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) =&gt; &#123;&#123; fecha_final_periodo &#125;&#125; 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 
&#160; 
 Label para cuando la consulta no trae resultados&#58; &quot;No existen anuncios de donacin con peso excesivo para las fechas seleccionadas&quot; 
 Label &#58; class=&quot;lbl_sin_anuncios_con_peso_excesivo&quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_sin_anuncios_con_peso_excesivo )&#160;&#160; 

 I NFORME DE PESO EXCESIVO 
 El sistema deber construir una Datatatable , con ordenamiento por columnas y buscador , que contenga la siguiente informacin. 
&#160; 
 Cdigo&#58; 
 Label&#58; class=&quot; lbl_codigo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_codigo )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-code 

&#160; 
 Fecha publicacin&#58; 
 Label&#58; class=&quot; lbl_fecha_publicacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_publicacion )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-publication_datetime 

&#160; 
 Punto de donacin&#58; 
 Label&#58; class=&quot; lbl_pod &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pod )&#160;&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-pod_name 

&#160; 
 Cdigo punto de donacin&#58; 
 Label&#58; class=&quot; lbl_pod_id &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_pod_id ) 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-pod_id 

&#160; 
 Estado&#58; 
 Label&#58; class=&quot; lbl_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_estado )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-state 

&#160; 
 Peso (excesivo)&#58; 
 Label&#58; class=&quot; lbl_peso_excesivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_peso_excesivo )&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-original_weight_kg 

&#160; 
 Observacin&#58; 
 Label&#58; class=&quot; lbl_observacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? 
 plataforma =datagov_cuentas&amp;idlabel= lbl_observacion )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc_excessive_weight_kg_ref 

&#160; 
 Beneficiario&#58; 
 Label&#58; class=&quot; lbl_beneficiario &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_beneficiario )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-donation_manager_name 

&#160; 
 Telfono Beneficiario&#58; 
 Label&#58; class=&quot; lbl_telefono_beneficiario &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_telefono_beneficiario )&#160;&#160; 
&#160; 
 Presenta informacin del campo&#58; 
 eatc_dona_headers. eatc-donation_manager_phone 

&#160; 
 Corregir peso&#58; 
 Label&#58; class=&quot; lbl_corregir_peso &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_corregir_peso )&#160; 
&#160; 
 Debe presentar un botn con el mismo label, por cada anuncio de donacin en el informe.&#160; Si el usuario oprime un botn para un anuncio en cuestin, se le debe dar ingreso al dashboard de donacin, contenido del anuncio (habra que migrar esto de la WAPP a datagov_cuentas), en donde se despliegan las funcionalidades para editar el anuncio de donacin. 

&#160; 
 Est OK&#58; 
 Label&#58; class=&quot; lbl_esta_ok &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_esta_ok )&#160;&#160; 
&#160; 
 Debe presentar un botn con el mismo label, por cada anuncio de donacin en el informe. Al presionar el botn, se deber ocultar este anuncio del informe y no mostrarlo de nuevo en el mismo.&#160; Se debe dar una opcin para mostrar aquellos anuncios que se marcaron como OK, en este informe. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Datagov Cuentas 

 NUEVO: INFORME DE PESOS EXCESIVOS