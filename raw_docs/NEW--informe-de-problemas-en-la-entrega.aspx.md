# NEW--informe-de-problemas-en-la-entrega.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Label Título de la Vista&#58; Informe de problemas en la entrega 
 id=&quot;lbl_informe_novedades_entrega&quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_novedades_entrega )&#160; 
&#160; 
 Label Descripción de la Vista&#58; 
 class=&quot;lbl_informe_novedades_entrega_desc&quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?idlabel= lbl_informe_novedades_entrega_desc )&#160; 
&#160; 
 &quot;En este informe se podrán consultar inconvenientes reportados en las entregas de donaciones.&quot; 

Informe con filtros para la perspectiva de los tres cuerpos 
Para este informe le aplicará la perspectiva de los tres cuerpos, por lo tanto después de aplicar&#160; los respectivo filtros , se obtendrá un “array de códigos de beneficiario” ( &#123;&#123;array_doma_codes&#125;&#125; ) que serán los que se apliquen a las consultas&#160;que traen la información para construir el informe y que más adelante se detallan. 
&#160; 

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

 Consulta de las novedades en las entregas 
El sistema, con el &#123;&#123;array_doma_codes&#125;&#125; que se obtiene de los filtros de la perspectiva de los tres cuerpos, y con las fechas establecidas, realiza la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_checkin_and_deliver_issues?eatc-eatc-date[0]=&#123;&#123;fecha_inicial&#125;&#125;&amp;eatc-eatc-date[1]=&#123;&#123;fecha_final&#125;&#125;&amp;eatc-donation_manager_code= &#123;&#123;array_doma_codes&#125;&#125; 
&#160; 
 Tabla de novedades en las entregas 
 Se debe mostrar en una datatable que permita ordenar por columnas, realizar búsquedas y descargar información (en formato .csv), la siguiente información 
 Código del anuncio 
 Label &#58; class=&quot;lbl_codigo_anuncio&quot;&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&amp;idlabel=lbl_codigo_anuncio 
 Orden&#58; 1ra columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-dona_header_code 
 Fecha 
 Label &#58; class=&quot; lbl_fecha &quot; 
 Orden&#58; 2da columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-date 
 Estado inicial 
 Label &#58; class=&quot; lbl_estado_inicial &quot; 
 Orden&#58; 3r a columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-dona_initial_state 
 Estado final 
 Label &#58; class=&quot; lbl_estado_final &quot; 
 Orden&#58; 4r a columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-dona_final_state 
 Donante 
 Label &#58; class=&quot; lbl_donante &quot; 
 Orden&#58; 5t a columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-donor 
 Código Punto de donación 
 Label &#58; class=&quot; lbl_codigo_punto_donacion &quot; 
 Orden&#58; 6ta columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-pod_id 
 Punto de donación 
 Label &#58; class=&quot; lbl_pod &quot; 
 Orden&#58; 7ma columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-pod_name 
 Ciudad 
 Label &#58; class=&quot; lbl_ciudad &quot; 
 Orden&#58; 8va columna 
 La información se toma de&#58; eatc_checkin_and_deliver_issues . eatc-city 
 Beneficiario 
 Label &#58; class=&quot; lbl_beneficiario &quot; 
 Orden&#58; 9na&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . eatc-donation_manager_name 
 Código beneficiario 
 Label &#58; class=&quot; lbl_codigo_beneficiario &quot; 
 Orden&#58; 10ma&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . eatc-donation_manager_code 
 Novedad 
 Label &#58; class=&quot; lbl_novedad &quot; 
 Orden&#58; 11ava&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . eatc-issue_cause 
&#160; 
 Código novedad 
 Label &#58; class=&quot; lbl_codigo_novedad &quot; 
 Orden&#58; 12ava&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . eatc-issue_cause_code 
&#160; 
 Notas 
 Label &#58; class=&quot; lbl_notas &quot; 
 Orden&#58; 13ava&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . eatc-log 
&#160; 
 ¿Resuelto? 
 Label &#58; class=&quot; lbl_resuelto &quot; 
 Orden&#58; 14ava&#160; columna 
 La información se toma de&#58;&#160; eatc_checkin_and_deliver_issues . resolved 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb269ff7d-7d85-4ddc-bae1-c7698e235fb3%2Fcopy-%281%29-389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb269ff7d-7d85-4ddc-bae1-c7698e235fb3%2Fcopy-%281%29-389328572-filtro_mis_resultados--2-.jpg&ow=1273&oh=181 
 12;#i:0#.f|membership|juan.correa@eatcloud.com 
 1183.00000000000 
 73efc9f4-7b7c-4014-8a7d-36b7a290701d 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 8d58c10c-90b0-42d1-94e4-e884ab73b7b3 
 2025-12-30T00:06:57.4315119Z 

 {"SessionId":"d0bf2d0e-90f2-4269-84dd-708c945b48cd","SequenceId":2587,"FluidContainerCustomId":"2a6b8881-21c8-41a8-b05f-771d90856927","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 Juan David Correa 

 NEW: informe de novedades en la entrega (BO Beneficiarios)