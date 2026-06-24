# b-informe-de-detalle-de-anuncios.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se realiza la documentación de este informe (que ya fue implementado, pero con documentación pendiente) con el ánimo de incorporarle mejoras (que se indicarán respectivamente como novedad) 

 [NUEVO] Selector múltiple de estado del anuncio: 
 El informe deberá mostrar un selector para seleccionar todos los estados posibles para traer información (la idea es que pueda funcionar como selección múltiple):  

 Anunciados ( annouced ) 
 Adjudicados ( awarded ) 
 Programados ( scheduled ) 
 Despachados ( delivered ) 
 Recibidos ( received ) 
 Pre-certificados ( pre-certified ) 
 Cancelados ( cancelled ) 
 No entregados ( not_delivered ) 
 Certificados ( certified ) 

 Selector de cuenta: 
 Se selecciona la cuenta de la cual se quieren extraer los anuncios 

 OPCIÓN DE SELECCIONAR TODAS LAS CUENTAS O ALGUNAS DE ELLAS (SELECTOR MÚLTIPLE) 
 Selector múltiple, con la opción "Todas" ( class="lbl_todas" ), que permita seleccionar todas las cuentas y sacar la información de todas ellas. 

 *** Selector de ciudad: *** 
 Permite seleccionar la ciudad de la cuál se quiere traer los detalles del anuncio 

 OPCIÓN DE SELECCIONAR TODAS LAS CIUDADES O ALGUNAS DE ELLAS (SELECTOR MÚLTIPLE) 
 El selector debe traer la opción "Todas" ( class="lbl_todas" ), que permita seleccionar todas las ciudades y sacar la información de todas ellas. 

 Informe paginado para consultas que traigan mucha información 
 Como se abrirá la posibilidad de seleccionar todas las cuentas para generar el informe, el mismo se debe paginar para traer lotes de información y no colapsar el servidor, ante grandes volúmenes de registros.  Se debe permitir descargar en .csv todos los registros del informe según el filtro aplicado, de una manera que no colapse el servidor. 

 Información a mostrar en el listado de detalle 
 Se debe mostrar la información del detalle de cada donación acompañada de cierta información de encabezado 

 Código del anuncio 
 Label: class="lbl_codigo_anuncio" 
 La información se toma de: eatc_dona_headers .eatc-code 

 Cambio de label: Fecha Publicación (anteriormente: Fecha) 
 Label: class="lbl_fecha_publicacion" 
 La información se toma de: eatc_dona_headers .eatc-publication_date 

 Fecha y hora 
 Label: class="lbl_fecha_hora" 
 La información se toma de: eatc_dona_headers .eatc-publication_datetime 

 Mes 
 Label: class="lbl_mes" 
 La información se toma de: eatc_dona_headers .eatc-publication_date (trayendo el mes) 

 Estado 
 Label: class="lbl_estado" 
 La información se toma de: eatc_dona_headers .eatc-state 

 Tipo creación 
 Label: class="lbl_tipo_creacion" 
 La información a partir de: eatc_dona_headers .eatc-code : si el código es propio del cliente se debe colocar " automatica " (es decir los anuncios que vienen de interfaz o integración).  Si el código es propio de la plataforma eatcloud (tiene como prefijo el nombre de la cuenta) se debe colocar " manual " 

 ***(Revisar que esté en el informe):  ID Donante 
 Label: class="lbl_id_donante" 
 La información se toma de: eatc_dona_headers . eatc_donor_code 

 ***(Revisar que esté en el informe): Razón Social 
 Label: class="lbl_razon_social" 
 Orden: después de ID Donante 
 La información se toma de: eatc_dona_headers . eatc_donor_fiscal_name   

 Donante 
 Label: class="lbl_donante" 
 La información se toma de: eatc_dona_headers . eatc_donor 

 *** Documento soporte 
 Label: class="lbl_documento_soporte" 
 Orden: después de Donante 
 La información se toma de: eatc_dona_headers .eatc-doc 

 *** 

 Código Punto de donación 
 Label: class="lbl_codigo_punto_donacion" 
 La información se toma de: eatc_dona .eatc-pod_id 

 Punto de donación 
 Label: class="lbl_pod" 
 La información se toma de: eatc_dona_headers .eatc-pod_name 

 Dirección punto de donación 
 Label: class="lbl_direccion_pod" Orden: 12ava columna 
 La información se toma de: eatc_dona_headers .eatc-pod_address 

 Teléfono Punto de Donación  
 Label: class="lbl_telefono_punto_donacion" 
 La información se toma de: eatc_dona_headers . eatc-pod_phone 

 Encargado Punto de Donación  
 Label: class="lbl_encargado_pod" 
 La información se toma de: con el dato de la cua_user y del código del punto de donación  {{eatc_dona_headers. eatc-pod_id }} el sistema realiza la siguiente consulta para obtener ese dato 
 {{URL_entorno_donantes }} /api/{{ cua_user }} /eatc_pods?eatc-id={{eatc_dona_headers. eatc-pod_id }} &_cmp= eatc-responsable 

 Cuenta Origen 
 Label: class="lbl_cuenta_origen" 
 La información se toma de: eatc_dona_headers . eatc_cua_origin 

 Ciudad 
 Label: class="lbl_ciudad" 
 La información se toma de: eatc_dona_headers .eatc-city 

 Departamento  
 Label: class="lbl_departamento_provincia_estado" 
 La información se toma de: eatc_dona_headers . eatc-province 

 Anuncio Origen 
 Label: class="lbl_anuncio_origen" 
 La información se toma de: eatc_dona_headers . eatc_consolidation_origin 

 Fecha detalle 
 Label: class="lbl_fecha_detalle" 
 La información se toma de: eatc_dona . eatc-date_time_2 

 ID Detalle 
 Label: class="lbl_id_detalle" 
 La información se toma de: eatc_dona . _id (se entiende que es el mismo dato que en el informe por la URL corresponde a: _id_det ) 

 Código del producto 
 Label: class="lbl_codigo_producto" 
 La información se toma de: eatc_dona .eatc-odd_id 

 Nombre del producto 
 Label: class="lbl_nombre_producto" 
 La información se toma de: eatc_dona .eatc-odd_name 

 Clasificación del producto 
 Label: class="lbl_clasificacion_producto" 
 La información se toma de: eatc_dona .eatc-odd_typology_a 

 *** Fecha de vencimiento 
 Label: class="lbl_fecha_vencimiento" 
 La información se toma de:  eatc_dona . eatc_closer_expiration_date 

 Unidades originales 
 Label: class="lbl_unidades_originales" 
 Tipo de dato: entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
 La información se toma de: eatc_dona . eatc-odd_original_quantity 

 Unidades aprovechadas 
 Label: class="lbl_unidades_aprovechadas" 
 Tipo de dato: entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
 La información se toma de: eatc_dona .eatc-odd_quantity 

 Unidades  no aprovechados 
 Label: class="lbl_unidades_no_aprovechadas" 
 Tipo de dato: entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
 La información se toma de:  eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity 

 KG Originales 
 Label: class="kg_originales" 
 La información se toma de: la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg ) 

 KG aprovechados 
 Label: class="lbl_kg_aprovechados" 
 La información se toma de: eatc_dona .eatc-odd_total_weight_kg 

 KG  no aprovechados 
 Label: class="lbl_kg_no_aprovechados" 
 Tipo de dato: float con dos posiciones decimales 
 La información se toma de:  ( eatc_dona .eatc-odd_original_quantity - eatc_dona .eatc-odd_quantity ) * eatc_dona .eatc-odd_unit_weight_kg 

 (***REVISAR SU INCORPORACIÓN EN EL INFORME***) Código causal de baja 
 Label: class="lbl_codigo_causal_baja" 
 La información se toma de:  eatc_dona . eatc-return_cause_code 

 (***REVISAR SU INCORPORACIÓN EN EL INFORME***) Causal de Baja 
 Label: class="lbl_causal_baja" 
 La información se toma de:  eatc_dona .eatc-return_cause 

 Costo total definitivo (antes  "Total cost odds") 
 Label: class="kg_costo_total_definitivo" 
 La información se toma de: eatc_dona .eatc-odd_total_cost 

 Sublínea 
 Orden:   28ava columna 
 La información se toma de:  donde se toma actualmente 

 Porcentaje IVA 
 Label: class="lbl_porcentaje_iva" 
 La información se toma de:  eatc_dona .eatc-VAT_percentage 

 Tarifa IVA 
 Label: class=" lbl_iva_total " 
 La información se toma de:  eatc_dona .eatc-total_VAT 

 Beneficiario 
 Label: class=" lbl_beneficiario " 
 La información se toma de:  eatc_dona_headers .eatc-donation_manager_name 

 (***REVISAR SU INCORPORACIÓN EN EL INFORME***) Código Beneficiario 
 Label: class=" lbl_beneficiario " 
 La información se toma de:  eatc_dona_headers . eatc-donation_manager_code 

 (***REVISAR SU INCORPORACIÓN EN EL INFORME***) Tipo Beneficiario 
 Label: class=" lbl_tipo_beneficiario " 
 La información se toma de:  eatc_dona_headers . eatc-donation_manager_typology_b 

 Beneficiario dirección 
 Label: class="lbl_direccion_beneficiario" 
 La información se toma de:  eatc_dona_headers .eatc-donation_manager_adress 

 Beneficiario teléfono 
 Label: class="lbl_telefono_beneficiario" 
 La información se toma de:  eatc_dona_headers .eatc-donation_manager_phone 

 Fecha de adjudicación 
 Label: class="lbl_hora_adjudicacion" 
 La información se toma de: eatc_dona_headers .eatc-adjudication_datetime 

 Fecha programada recogida 
 Label: class="lbl_fecha_programada_de_recogida " 
 La información se toma de: eatc_dona_headers .eatc-programed_picking_datetime 

 Recolector 
 Label: class=" lbl_recolector "=> 
 La información se toma de:  eatc_dona_headers . eatc-picker_name 

 ID Recolector 
 Label: class=" lbl_doc_id_recolector " 
 La información se toma de:  eatc_dona_headers . eatc-picker_doc_id 

 Placa Recolector 
 Label: class=" lbl_placa_recolector " 
 Orden: 39ava  columna 
 La información se toma de:  eatc_dona_headers . eatc-picker_license_plate 

 Fecha y hora salida recolector 
 Label: class=" lbl_fecha_hora_salida_recolector " 
 La información se toma de:  eatc_dona_headers . eatc-picker_start_datetime 

 Fecha entrada 
 Label: class=" lbl_fecha_hora_llegada " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkin_datetime 

 Fecha verificación de código de recogida 
 Label: class=" lbl_fecha_verificacion_codigo " 
 La información se toma de: eatc_dona_headers . eatc_code_verification_datetime 

 Fecha salida 
 Label: class=" lbl_fecha_hora_salida " 
 La información se toma de: eatc_dona_headers .eatc-picking_checkout_datetime 

 Fecha recepción 
 Label: class=" lbl_fecha_recepcion " 
 La información se toma de: eatc_dona_headers .eatc-receipt_datetime 

 Fecha constancia 
 Label: class=" lbl_fecha_constancia " 
 La información se toma de: eatc_dona_headers . eatc_constancy_datetime 

 Fecha pre-certificación 
 Label: class=" lbl_fecha_pre_certificacion " 
 La información se toma de: eatc_dona_headers .eatc-pre_certification_datetime 

 Fecha Certificación 
 Label: class=" lbl_fecha_certificacion " 
 La información se toma de: eatc_dona_headers .eatc-certification_datetime 

 Warning 
 Label: class=" lbl_alerta " 
 La información se toma de: eatc_dona_headers .eatc-warning 

 Horarios de atención  
 Label: class=" lbl_horarios_atencion " 
 La información se toma de: con el dato de la cua_user y del código del punto de donación  {{eatc_dona_headers. eatc-pod_id }} el sistema realiza la siguiente consulta para obtener ese dato 
 {{URL_entorno_donantes }} /api/{{ cua_user }} /eatc_attention_schedule? eatc-pod_id ={{eatc_dona_headers. eatc-pod_id }} &_cmp=eatc-day,eatc-start_hour,eatc-final_hour 

 La información que arroja la consulta se debe mostrar como un array, con salto de línea en la casilla de resultados de la siguiente manera 
 {{eatc-day (sub_1) }}: {{eatc-start_hour (sub_1) }} - {{eatc-final_hour (sub_1) }}, 
 {{eatc-day (sub_2) }}: {{eatc-start_hour (sub_2) }} - {{eatc-final_hour (sub_2) }}, 
 ..... 
 {{eatc-day (sub_n) }}: {{eatc-start_hour (sub_n) }} - {{eatc-final_hour (sub_n) }}, 

 *** 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 
 BO Beneficiarios 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 61a5b389-3c71-427e-aafe-117d30575efd 
 3!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 4806c8b4-950c-4758-9abd-6059e5c8f0dc 
 2025-09-13T05:35:39.1968160Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"4cd6c9e2-ad64-4038-a818-6b6a4bdbc6c8","SequenceId":321,"FluidContainerCustomId":"cefb0d75-c146-4375-ad09-0bb4aecc193d","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 INFORME DE DETALLE DE ANUNCIOS