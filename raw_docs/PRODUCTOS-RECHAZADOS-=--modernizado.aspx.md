# PRODUCTOS-RECHAZADOS-=--modernizado.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Label Título de la Vista&#58; Informe de productos rechazados 
 id=&quot;lbl_informe_productos_rechazados&quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_productos_rechazados )&#160; 
&#160; 
 Label Descripción de la Vista&#58; 
 class=&quot;lbl_informe_productos_rechazados_desc&quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_productos_rechazados_desc )&#160; 
&#160; 
 &quot;En este informe se podrán consultar rechazos de productos realizados por los beneficiarios en el proceso de verificación detallada de la donación.&quot; 

 Filtro por fechas&#58; 

 Subtítulo&#58; 
 class=&quot; lbl_filtro_fechas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_filtro_fechas )&#160; 
&#160; 
 Filtro&#58; &quot;Hoy&quot; 
 class=&quot; lbl_hoy &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_hoy ) 
&#160; 
 Filtro&#58; &quot;El mes actual&quot; 
 class=&quot; lbl_mes_actual &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_mes_actual ) 

 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_personalizar ) 

&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_inicial ) 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_fecha_final ) 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_consultar ) 

&#160; 
Filtro por ciudades (selector múltiple, con opción &quot;Todas&quot;) 
 Seleccionar ciudad&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel=lbl_selector_ciudad &#160; 
&#160; 
 Con la selección anterior de fechas, el sistema deberá realizar la siguiente consulta&#58; 
&#160; 
 Consulta de las ciudades en donde se realizaron rechazos en las fechas establecidas (para armar el selector múltiple de ciudades solo con las que tienen registros) 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ?eatc_donor=&#123;&#123;_DOM. cua_user &#125;&#125;&amp; eatc-date_time_2[0]= &#123;&#123;fecha_inicial&#125;&#125;&amp; eatc-date_time_2[1]= &#123;&#123;fecha_final&#125;&#125;&amp;eatc-odd_rejection_cause= _novacio &amp;_cmp=eatc-dona_header_code 
&#160; 
 Con esta consulta se obtienen un &#123;&#123; array_codigos_encabezados &#125;&#125; (eatc-dona_header_code) con los cuales se hace la siguiente consulta para obtener el array de ciudades con las que se arma el selector 
&#160; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?eatc-code= &#123;&#123; array_codigos_encabezados &#125;&#125; &amp;_distinct= eatc-city 
&#160; 
 Si no se obtienen resultados en la consulta , se muestra el toast &quot;No se obtubieron resultados &quot;&#160; class=&quot; lbl_toast_sin_resultados &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentasficiarios&amp;idlabel=lbl_toast_sin_resultados &#160; 
&#160; 
 Con las respuestas, el sistema arma un selector múltiple que permitirá seleccionar una, varias o todas las ciudades presentes en el selector.&#160; Una vez el usuario realice su selección, con ella el sistema arma un &#123;&#123; array_de_ciudades &#125;&#125; que utiliza para la siguiente consulta&#58; 
&#160; 
 Consulta de productos rechazados (para las fechas en las ciudades seleccionadas) 
 Con las fechas seleccionadas en el primer selector y las ciudades seleccionadas en el segundo, el sistema realiza la siguiente consulta para traer los datos&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?eatc-code= &#123;&#123; array_codigos_encabezados &#125;&#125; &amp; eatc-city= &#123;&#123; array_de_ciudades &#125;&#125; &amp;_cmp= eatc-code 
&#160; 
&#160; 
&#160; 
 Con esta consulta se obtiene un nuevo &#123;&#123; array_codigos_encabezados &#125;&#125; con el cual se efectúan las siguientes consultas para obtener la información para amar el informe 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_headers ?eatc-code= &#123;&#123; array_codigos_encabezados &#125;&#125; &amp;_cmp= eatc-code,eatc-publication_datetime,eatc-donor,e atc_cua_origin ,eatc-state,eatc-pod_id,eatc-pod_name,eatc-city,eatc-province,eatc-donation_manager_name,eatc-doc, eatc-receipt_datetime , eatc-picker_name , eatc-picker_doc_id 
&#160; 
A partir de los encabezados se consultan los detalles&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ? eatc-dona_header_code = &#123;&#123; array_codigos_encabezados &#125;&#125; &amp;eatc-odd_rejection_cause= _novacio &amp;_cmp=eatc-dona_header_code, eatc-odd_name,eatc-odd_code,origin_odds_typology_a,origin_odds_typology_b,eatc-odd_original_quantity,eatc-odd_quantity,eatc-odd_state, eatc-odd_rejection_cause&#160; 
&#160; 
 y con cada producto rechazado se realiza la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_odd_rejection_registry?eatc-dona_header_code=&#123;&#123; eatc_dona. eatc-dona_header_code &#125;&#125; &amp;eatc-odd_id=&#123;&#123; eatc_dona. eatc-odd_code&#125;&#125; &amp;_cmp= evidence 
&#160; 

&#160; 
 Tabla de productos rechazados 
 Se debe mostrar en una datatable que permita ordenar por columnas, realizar búsquedas y descargar información (en formato .csv), la siguiente información 
 Código del anuncio 
 La información se toma de&#58; eatc_dona_headers .eatc-code 
 Fecha y hora 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
 Donante 

 La información se toma de&#58; eatc_dona_headers .eatc-donor 
 Origen 

 La información se toma de&#58; eatc_dona_headers .eatc_cua_origin 
 Estado donación 

 La información se toma de&#58; eatc_dona_headers .eatc-state 
 Código Punto de donación 
 La información se toma de&#58; eatc_dona .eatc-pod_id 
 Punto de donación 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_name 
 Ciudad 
 La información se toma de&#58; eatc_dona_headers .eatc-city 
 Departamento 
 La información se toma de&#58; eatc_dona_headers .eatc-province 
 Beneficiario 
 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_name 
 Doc 

 La información se toma de&#58; eatc_dona_headers .eatc-doc 
 Fecha y hora de recepción 

 La información se toma de&#58; eatc_dona_headers . eatc-receipt_datetime 
 Recolector 

 La información se toma de&#58; eatc_dona_headers . eatc-picker_name 
 Doc ID Recolector 

 La información se toma de&#58; eatc_dona_headers . eatc-picker_doc_id 
&#160; 
 Producto 

 La información se toma de&#58; eatc_dona . eatc-odd_name 
 Código producto 

 La información se toma de&#58; eatc_dona . eatc-odd_code 
 Primera tipología del producto 

 La información se toma de&#58; eatc_dona . origin_odds_typology_a 
 Segunda tipología del producto 

 La información se toma de&#58; eatc_dona . origin_odds_typology_b 
 Cantidad original 

 La información se toma de&#58; eatc_dona . eatc-odd_original_quantity 
 Cantidad verificada 

 La información se toma de&#58; eatc_dona . eatc-odd_quantity 
 Estado producto 

 La información se toma de&#58; eatc_dona . , eatc-odd_state 
 Causal de rechazo 

 La información se toma de&#58; eatc_dona .e atc-odd_rejection_cause 
 Evidencia 

 La información se toma de&#58; eatc_odd_rejection_registry . evidence 

 Se debe poder ver la fotografía, ampliarla y descargarla 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 Cuentas datagov 
 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-de-donaciones-eliminadas%2F389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnew-informe-de-donaciones-eliminadas%2F389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"PageThumbnailGettyMetadataEnabled","Version":"On"},{"Name":"AIGeneratedDescription","Version":"On"}] 
 1e6a6651-f6fa-4f88-b63f-75f8bbe74202 
 4!1!3 
 https://centralus0-0.pushfp.svc.ms/fluid 
 eee5cbb8-fe45-4e81-baa3-14c6957712b7 
 2026-06-05T03:25:26.0903374Z 
 [{"id":"608055c5-adb7-4816-afe5-b85129b80f66","t":"2026-06-04T19:32:46.216432Z"}] 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"88e5fcae-6516-4fc6-8d6a-8e03769e65a6","SequenceId":936,"FluidContainerCustomId":"0318035a-cb9f-4201-9398-c92f26fe77aa","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 PRODUCTOS RECHAZADOS => modernizado