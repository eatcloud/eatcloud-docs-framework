# informes-de-anuncios-informe-liviano-de-detalles.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota importante de implementación&#58;&#160; 
 Se implementa este informe como una version abreviada de uno ya implementado, que estará disponible para todo tipo de licencias (es decir que no requerirá verificacion del tipo de licencia para poder ingresar a él), por lo tanto su estrategia de desarrollo puede ser la de duplicar el informe anteriormente implementado, quitarle la restricción de acceso por licencia, y luego &quot;peluquiar campos&quot; para dejar los que se establecieron. 

&#160; 
 Nota importante de implementación&#58; se basa enteramente en funcionalidad ya implementada 
 Esta implementación debe constar en el traspaso (o copia exacta) de la funcionalidad &quot; Informe de detalle de anuncios &quot; 

 Validación del tipo de licencia para el despliegue de la funcionalidad 
 Este informe se le desplegará a todas las licencias, por lo tanto no requiere de validación del tipo de licencias 

&#160; 
 Titulo de la vista&#58; Informe liviano de detalle de anuncios 
 class=&quot; lbl_informe_liviano_detalle_anuncios &quot; ( htt p s&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_detalle_anuncios ) 
&#160; 
 Descripción del informe 
 class=&quot; lbl_informe_detalle_anuncios_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_informe_detalle_anuncios_desc ) 

&#160; 
 Filtro de fechas 
 Fecha inicial 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_inicial ) 
&#160; 
 Fecha final 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_fecha_final ) 

&#160; 
 Selector de estados 
 Selecciona el estado 
 clase=&quot; lbl_seleccionar_estado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_seleccionar_estado ) 
&#160; 
 Labels de estados 
 Se toman del campo &quot; eatc_plural_label &quot; del maestro de estados. 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_dona_headers_states?_id=_* 
 ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?_id=_* ) 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel=lbl_consultar ) 

&#160; 
 Sumatoria totales 
 class=&quot; lbl_sumatoria_totales &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cu 
 entas&amp;idlabel=lbl_sumatoria_totales ) 
&#160; 
 KG aprovechados 
 clase=&quot; lbl_kg_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_aprovechados ) 
&#160; 
 KG&#160; no aprovechados 
 clase=&quot; lbl_kg_no_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_kg_no_aprovechados ) 
&#160; 
 Unidades aprovechados 
 clase=&quot; lbl_unidades_aprovechadas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_unidades_aprovechadas ) 
&#160; 
 Unidades&#160; no aprovechados 
 clase=&quot; lbl_unidades_no_aprovechados &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_unidades_no_aprovechados ) 
&#160; 
 Costo total 
 clase=&quot; lbl_costo_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =datagov_cuentas&amp;idlabel= lbl_costo_total ) 
&#160; 
 Tabla de información de detalle de anuncios 
 Información a mostrar en el listado de detalle 
 Se debe mostrar la información del detalle de cada donación acompañada de cierta información de encabezado 

&#160; 
 Código del anuncio 
 Label &#58; class=&quot;lbl_codigo_anuncio&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-code 
&#160; 
 Mes 
 Label &#58; class=&quot; lbl_mes &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date (trayendo el mes) 
&#160; 
 Estado 
 Label &#58; class=&quot; lbl_estado &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-state 

&#160; ***NUEVO&#58; Causal no entrega *** 
 Label &#58; class=&quot; lbl_causal_not_delivered &quot; 
 La información se toma de&#58; eatc_dona_headers . eatc_not_delivery_cause 
&#160; 
 Punto de donación 
 Label &#58; class=&quot; lbl_pod &quot; 

 La información se toma de&#58; eatc_dona_headers .eatc-pod_name 
&#160; 
 Código punto de donación 
 Label &#58; class=&quot; lbl_pod_id &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-pod_id 

&#160; 
 Código del producto 
 Label &#58; class=&quot; lbl_codigo_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_id 

&#160; 
 Nombre del producto 
 Label &#58; class=&quot; lbl_nombre_producto &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_name 

&#160; 
 KG Originales 
 Label &#58; class=&quot; kg_originales &quot; 
 La información se toma de&#58; la multiplicación de las unidades originales por el pseo unitario ( eatc_dona .eatc-odd_quantity * eatc_dona .eatc-odd_unit_weight_kg) 

&#160; 
 KG aprovechados 
 Label &#58; class=&quot; lbl_kg_aprovechados &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_weight_kg 

&#160; 
 Costo total definitivo (antes &quot;Total cost odds&quot;) 
 Label &#58; class=&quot; kg_costo_total_definitivo &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_total_cost 

&#160; 
 Porcentaje IVA 
 Label &#58; class=&quot; lbl_porcentaje_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-VAT_percentage 

&#160; 
 Tarifa IVA 
 Label &#58; class=&quot; lbl_valor_iva &quot; 
 La información se toma de&#58; eatc_dona .eatc-total_VAT 

&#160; 
 Doc ID donante 
 Label &#58; class=&quot;lbl_doc_id_donante&quot; 
 La información se toma de&#58; eatc_dona_headers . eatc-donor_code 
&#160; 
 Doc 
 Label &#58; class=&quot; lbl_documento_soporte &quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-doc 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 
 Cuentas datagov 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 9f75a0a8-982f-4447-8c12-988798975029 
 4!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 6c1942d0-2464-46b3-a281-bb24b49e5050 
 2025-12-24T03:00:39.3554592Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"5d4d795c-bc03-4304-a5b6-066aab62cae8","SequenceId":152,"FluidContainerCustomId":"7a63f937-8678-4eac-bfbb-6b75a920f64e","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 DATA ANALYTICS: INFORMES DE ANUNCIOS > INFORME LIVIANO DE DETALLES