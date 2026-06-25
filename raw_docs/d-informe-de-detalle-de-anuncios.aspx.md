# d-informe-de-detalle-de-anuncios.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se realiza la documentación de este informe (que ya fue implementado, pero con documentación pendiente) con el ánimo de incorporarle mejoras (que se indicarán respectivamente como novedad) 

 Consulta de anuncios ***NUEVO DINAMIZAR CON CUENTA MAESTRA 
 El sistema debe tomar la cuenta maestra de la cuenta respectiva para realizar la consulta de los anuncios que le corresponden&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;_DOM. cua_user &#125;&#125; =&gt; eatc_cua_master 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/ &#123;&#123;eatc_cua_master&#125;&#125; /eatc_dona?eatc_donor=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 Ejemplo Éxito en ambiente de pruebas&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito eatc_cua_master=abaco 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona_headers?eatc-donor=exito &#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/ abaco /eatc_dona?eatc_donor=exito &#160; 
&#160; 
 Selector múltiple de estado del anuncio&#58; 
 El informe deberá mostrar un selector para seleccionar todos los estados posibles para traer información (la idea es que pueda funcionar como selección múltiple)&#58;&#160; 
&#160; 
 Anunciados ( annouced ) 
 Adjudicados ( awarded ) 
 Programados ( scheduled ) 
 Despachados ( delivered ) 
 Recibidos ( received ) 
 Pre-certificados ( pre-certified ) 
 Cancelados ( cancelled ) 
 No entregados ( not_delivered ) 
 Certificados ( certified ) 

 Selector de cuenta&#58; 
 Se selecciona la cuenta de la cual se quieren extraer los anuncios 

 Información a mostrar en el listado de detalle 
 Se debe mostrar la información del detalle de cada donación acompañada de cierta información de encabezado 
&#160; 
 Acción 
 Label &#58; class=&quot;lbl_accion&quot; 
&#160; 
 Código del anuncio 
 Label &#58; class=&quot;lbl_codigo_anuncio&quot; 
 Orden&#58; 1ra columna 

 La información se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Fecha 
 Label &#58; class=&quot; lbl_fecha &quot; 
 Orden&#58; 2da columna 

 La información se toma de&#58; eatc_dona_headers .eatc-publication_date 
&#160; 
 Fecha y hora 
 Label &#58; class=&quot; lbl_fecha_hora &quot; 
 Orden&#58; 3ra columna 

 La información se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
&#160; 
 Mes 
 Label &#58; class=&quot; lbl_mes &quot; 
 Orden&#58; 4ta columna 

 La información se toma de&#58; eatc_dona_headers .eatc-publication_date (trayendo el mes) 
&#160; 
 Estado 
 Label &#58; class=&quot; lbl_estado &quot; 
 Orden&#58; 5 ta columna 

 La información se toma de&#58; eatc_dona_headers .eatc-state 
&#160; 
 ***NUEVO&#58; Razón social donante *** 
 Label &#58; class=&quot; lbl_razon_social &quot; 
 Orden&#58; entre la 5ta y la 6ta columna 

 La información se toma de&#58; eatc_dona_headers .eatc_donor_fiscal_name 
&#160; 
 Tipo creación 
 Label &#58; class=&quot;lbl_tipo_creacion&quot; 
 Orden&#58; 5.5&#160; columna 
 La información se toma de&#58; eatc_dona_headers .eatc-code con las siguientes pruebas lógicas&#58; 
 Si el código del anuncio ( eatc_dona_headers .eatc-code ) es propio del cliente (no empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lógica &quot;y&quot;) el código del producto ( eatc_dona .eatc-odd_id ) no es alfanumérico (es decir no fue creado manualmente dado que cuando esto ocurre los códigos del producto son alfanuméricos)&#160; se debe colocar &quot; automatica &quot; (es decir los anuncios que vienen de interfaz o integración).&#160; De otra manera (Els)e se debe colocar &quot; manual &quot; 
 Si el código del anuncio ( eatc_dona_headers .eatc-code ) es del sistema (empieza por la palabra &quot;exito&quot; por ejemplo) y (prueba lógica &quot;y&quot;) el código del producto ( eatc_dona .eatc-odd_id ) es alfanumérico (es decir fue creado manualmente dado que cuando esto ocurre los códigos del producto son alfanuméricos)&#160; se debe colocar &quot; manual &quot; (es decir los anuncios que vienen de interfaz o integración).&#160; De otra manera (Els)e se debe colocar &quot; automatica &quot; 
&#160; 
 Se debe evaluar si solo haciendo la prueba lógica sobre&#160; eatc_dona_headers .eatc-code se logrará atender la necesidad planteada con las pruebas lógicas arriba propuestas 

&#160; 
 Código Punto de donación 
 Label &#58; class=&quot; lbl_codigo_punto_donacion &quot; 
 Orden&#58; 6ta columna 

 La información se toma de&#58; eatc_dona .eatc-pod_id 
&#160; 
 Punto de donación 
 Label &#58; class=&quot; lbl_pod &quot; 
 Orden&#58; 7ma columna 

 La información se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Dirección punto de donación 
 Label &#58; class=&quot;lbl_direccion_pod&quot; 
 Orden&#58; 8ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-pod_address 
&#160; 
 Ciudad 
 Label &#58; class=&quot; lbl_ciudad &quot; 
 Orden&#58; 9na columna 

 La información se toma de&#58; eatc_dona_headers .eatc-city 
&#160; 
 Departamento 
 Label &#58; class=&quot; lbl_departamento_provincia_estado &quot; 
 Orden&#58; 9na columna 

 La información se toma de&#58; eatc_dona_headers .eatc-province 
&#160; 
 Anuncio Origen 
 Label &#58; class=&quot;lbl_anuncio_origen&quot; 
 Orden&#58; 9.5 columna 

 La información se toma de&#58; eatc_dona_headers . eatc_consolidation_origin 
&#160; 
 Código del producto 
 Label &#58; class=&quot; lbl_codigo_producto &quot; 
 Orden&#58;&#160; 10ma columna 

 La información se toma de&#58; eatc_dona .eatc-odd_id 
&#160; 
 Nombre del producto 
 Label &#58; class=&quot; lbl_nombre_producto &quot; 
 Orden&#58;&#160; 11ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_name 
&#160; 
 NUEVO&#58;&#160; Clasificación A del producto 
 Label &#58; class=&quot; bl_odd_typology_a &quot;&#160; 
 Orden&#58; 12ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_typology_a 
&#160; 
 NUEVO&#58;&#160; Clasificación B del producto 
 Label &#58; class=&quot; bl_odd_typology_b &quot; 
 Orden&#58; 12ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_typology_b 
&#160; 
 Clasificación Origen A del producto 
 Label &#58; class=&quot; lbl_odd _origin _typology_a &quot; 
 Orden&#58; 12A columna 

 La información se toma de&#58; eatc_dona . origin_odds_typology_a &#160; 
&#160; 
 Clasificación Origen B del producto 
 Label &#58; class=&quot; lbl_odd _origin _typology_b &quot; 
 Orden&#58; 12B columna 

 La información se toma de&#58;&#160; eatc_dona . origin_odds_typology_b 
&#160; 
 Clasificación Origen C del producto 
 Label &#58; class=&quot; lbl_odd _origin _typology_c &quot; 
 Orden&#58; 12C columna 

 La información se toma de&#58;&#160; eatc_dona . origin_odds_typology_c 
&#160; 
 KG Originales 
 Label &#58; class=&quot; kg_originales &quot; 
 Orden&#58; 13ava columna 

 La información se toma de&#58; la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg) 
&#160; 
 KG aprovechados 
 Label &#58; class=&quot; lbl_kg_aprovechados &quot; 
 Orden&#58;&#160; 14ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_total_weight_kg 
&#160; 
 KG&#160; no aprovechados 
 Label &#58; class=&quot; lbl_kg_no_aprovechados &quot; 
 Orden&#58; 15ava columna 
 Tipo de dato&#58; float con dos posiciones decimales 

 La información se toma de&#58;&#160; ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity) * eatc_dona .eatc-odd_unit_weight_kg 
&#160; 
 Unidades aprovechadas 
 Label &#58; class=&quot; lbl_unidades_aprovechadas &quot; 
 Orden&#58; 16ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_quantity 
&#160; 
 Unidades&#160; no aprovechadas 
 Label &#58; class=&quot; lbl_unidades_no_aprovechadas &quot; 
 Orden&#58;&#160; 17ava columna 
 Tipo de dato&#58; float con dos posiciones decimales 

 La información se toma de&#58;&#160; eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity 
&#160; 
 Causal de Baja 
 Label &#58; class=&quot; lbl_causal_baja &quot; 
 Orden&#58;&#160; 18ava columna 

 La información se toma de&#58;&#160; eatc_dona .eatc-return_cause 
&#160; 
 Costo total definitivo (antes&#160; &quot;Total cost odds&quot;) 
 Label &#58; class=&quot; kg_costo_total_definitivo &quot; 
 Orden&#58;&#160; 19ava columna 

 La información se toma de&#58; eatc_dona .eatc-odd_total_cost 
&#160; 
 Costo no aprovechados 
 Label &#58; class=&quot; kg_costo_no_aprovechados &quot; 
 Orden&#58;&#160; 19.5 

 La información se toma de multiplicar las &quot;Unidades no aprovechadas&quot; (17ava columna) por el costo unitario (eatc_dona .eatc-unit_cost) 
&#160; 
 &#160;Sublínea 
 Label &#58; class=&quot; lbl_tipologia_a_producto &quot; 
 Orden&#58;&#160; &#160;20ava columna 

 La información se toma de&#58;&#160; donde se toma actualmente 
&#160; 
 Porcentaje IVA 
 Label &#58; class=&quot; lbl_porcentaje_iva &quot; 
 Orden&#58;&#160; 21ava columna 

 La información se toma de&#58;&#160; eatc_dona .eatc-VAT_percentage 
&#160; 
 Tarifa IVA 
 Label &#58; class=&quot; lbl_valor_iva &quot; 
 Orden&#58; 22ava columna 

 La información se toma de&#58;&#160; eatc_dona .eatc-total_VAT 
&#160; 
 Beneficiario 
 Label &#58; class=&quot; lbl_beneficiario &quot; 
 Orden&#58; 23ava&#160; columna 

 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_name 
&#160; 
 Beneficiario dirección 
 Label &#58; class=&quot; lbl_direccion_beneficiario &quot; 
 Orden&#58; 24ava&#160; columna 

 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_adress 
&#160; 
 Beneficiario teléfono 
 Label &#58; class=&quot;lbl_telefono_beneficiario&quot; 
 Orden&#58; 25ava&#160; columna 

 La información se toma de&#58;&#160; eatc_dona_headers .eatc-donation_manager_phone 
&#160; 
 Fecha de adjudicación 
 Label &#58; class=&quot; lbl_hora_adjudicacion &quot; 
 Orden&#58; 26ava&#160; columna 

 La información se toma de&#58; eatc_dona_headers .eatc-adjudication_datetime 
&#160; 
 Fecha programada 
 Label &#58; class=&quot; lbl_hora_entrega_programada &quot; 
 Orden&#58; 27ava&#160; columna 

 La información se toma de&#58; eatc_dona_headers .eatc-programed_picking_datetime 
&#160; 
 Fecha entrada 
 Label &#58; class=&quot; lbl_hora_entrega_real_llegada &quot; 
 Orden&#58; 28ava&#160; columna 

 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkin_datetime 
&#160; 
 Fecha verificación de código de recogida 
 Label &#58; class=&quot;lbl_fecha_verificacion_codigo&quot; 
 Orden&#58; 28.5&#160; columna 

 La información se toma de&#58; eatc_dona_headers . eatc_code_verification_datetime 
&#160; 
 Fecha salida 
 Label &#58; class=&quot; lbl_hora_entrega_real_salida &quot; 
 Orden&#58; 29ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-picking_checkout_datetime 
&#160; 
 Fecha recepción 
 Label &#58; class=&quot; lbl_hora_recepcion &quot; 
 Orden&#58; 30ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime 
&#160; 
 Fecha constancia 
 Label &#58; class=&quot;lbl_fecha_constancia&quot; 
 Orden&#58; 31ava columna 

 La información se toma de&#58; eatc_dona_headers . eatc_constancy_datetime 
&#160; 
 Fecha pre-certificación 
 Label &#58; class=&quot; lbl_hora_precertificacion &quot; 
 Orden&#58; 32ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-pre_certification_datetime 
&#160; 
 Fecha Certificación 
 Label &#58; class=&quot;lbl_fecha_certificacion&quot; 
 Orden&#58; 33ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-certification_datetime 
&#160; 
 Doc ID donante 
 Label &#58; class=&quot;lbl_doc_id_donante&quot; 
 Orden&#58; 34ava columna 

 La información se toma de&#58; eatc_dona_headers . eatc-donor_code 
&#160; 
 Doc 
 Label &#58; class=&quot; lbl_documento_soporte &quot; 
 Orden&#58; 35ava columna 

 La información se toma de&#58; eatc_dona_headers .eatc-doc 
&#160; 
 Warning 
 Label &#58; class=&quot; lbl_alerta &quot; 
 Orden&#58; 36ava columna 
 La información se toma de&#58; eatc_dona_headers .eatc-warning 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 262.000000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 e5bb8e55-80d1-4d6e-a60a-cdf1f0978f23 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 f96d5b09-9f2a-42e7-af1f-9ccac8e05b80 
 2025-05-17T07:38:08.6233307Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"2437a081-7f65-4811-a2a9-435ea348afd6","SequenceId":144,"FluidContainerCustomId":"721876a5-f223-4aa6-b39b-0fe3393f360f","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 INFORME DE DETALLE DE ANUNCIOS (ANTES INFORME DE RECIBIDOS, PRE-CERTIFICADOS)