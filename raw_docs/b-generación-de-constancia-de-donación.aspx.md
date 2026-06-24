# b-generación-de-constancia-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Introducción: 
 Esta funcionalidad constará de un informe de anuncios de donación "recibidos" (es decir, aquellos que ya han pasado por el proceso de verificación por parte del "gestor de donaciones" para un donante en particular (cua_user) y le permitirá al usuario seleccionar a demanda que anuncio o conjunto de anuncios desea "pre-cerficicar" para cada donante en particular, para que el sistema genere un informe o constancia de donación donde incluya la información general de dichos anuncios y sus respectivos detalles. 

 Información que trae la lista de anuncios que pueden ser seleccionados para "pre-certificarse" 
 La funcionalidad presenta una lista de anuncios de donación cuyo ( eatc_dona_states ), es "received" o “entregado” , es decir, en la lista se deben mostrar los anuncios que ya han sido verificados por parte del gestor de donaciones. 

 Consulta de anuncios: Filtro principal [PRINCIPAL DIFERENCIA CON LA IMPLEMENTACIÓN EN DEL BO DONANTES] 
 Debe presentar un selector con los  "CUA_user" disponibles ({{URL_entorno}}/cuachk] .  El usuario podrá seleccionar una de las cuentas o donantes habilitados y dicha selección y este será enviada como el parámetro " eatc-donor" , junto con el estado " eatc-state= received". 

 Ejemplo: 
 En el BO ( https://devbeneficiarios.eatcloud.info/bo/abaco y https://beneficiarios.eatcloud.info/bo/abaco ) se realiza la siguiente consulta para determinar las cuentas disponbiles: 

 Ambiente de pruebas: 
 https://devdonantes.eatcloud.info/cuachk   

 Ambiente productivo: 
 https://donantes.eatcloud.info/cuachk   

 El sistema dispone un selector con la información de la respuesta.  Si el usuario por ejemplo oprime el selector "exito", entonces el sistema envía "exito"  al parámetro eatc-donor (teniendo en cuenta los estados (eatc-state=received) de la siguiente manera: 

 Ambiente de pruebas: 
 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=exito&eatc-state=received     
 Trama comprimida: https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=exito&eatc-state=received&_compress     

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=exito&eatc-state=received     
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-donor=exito&eatc-state=received&_compress     

 NOTA IMPORTANTE:  
 de este punto en adelante la implementación es totalmente similar a la que se hizo en el BO donantes 

 Card del anuncio de donación 
 Es un informe muy similar al " informe operativo de donaciones " (se debe procurar reutilizar la mayor cantidad de código posible). El informe debe ser construido en tiempo real para mostrar la fotografía (o estado actual) de los anuncios en el momento que se carga el informe. Se debe pensar en refrescar de manera automática esta carga cada cierto tiempo.  
 Cada anuncio de donación ( eatc_dona_headers ) se presenta en una tarjeta que contiene la siguiente información: 

 ENCABEZADO: 
 Código del anuncio: 
   eatc_dona_headers .eatc-code 

 Fecha y hora del anuncio: 
   eatc_dona_headers .eatc-publication_datetime 

 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudicó el anuncio 

 Nombre: eatc_dona_headers .eatc-donation_manager_name 
 Dirección: eatc_dona_headers .eatc-donation_manager_address 
 Teléfono: eatc_dona_headers .eatc-donation_manager_address 
 Ver mapa: consulta de las coordenadas del anuncio eatc_dona_headers .eatc-lat, eatc_dona_headers .eatc-long 

 En caso que aun no halla sido adjudicado el anuncio, se debe mostrar un letrero vistoso que diga "PENDIENTE DE ADJUDICACIÓN" 

 DETALLE ANUNCIO: 
 Peso total (del anuncio) 
 eatc_dona_headers .eatc-total_weight_kg 

 Valor total (del anuncio) 
 eatc_dona_headers .eatc-total_cost 

 TRACKING: 
 Hora publicación 
 eatc_dona_headers .eatc-publication_datetime 

 Hora adjudicación 
 eatc_dona_headers .eatc-adjudication_datetime 

 Hora de entrega programada 
 eatc_dona_headers .eatc-programed_picking_datetime 

 Hora de entrega real llegada 
 eatc_dona_headers .eatc-picking_checkin_datetime 

 Hora de entrega real salida 
 eatc_dona_headers .eatc-picking_checkout_datetime 

 Hora de recepción 
 eatc_dona_headers .eatc-receipt_datetime 

 Hora de pre-certificación 
 eatc_dona_headers .eatc-pre_certification_datetime 

 Hora de certificación 
 eatc_dona_headers .eatc-certification_datetime 

 ESTADO ( eatc_dona_states ) 
 Solo se muestran anuncios con estado "delivered" o "entregados"  

 Botón + 
 Este botón dará la entrada a la funcionalidad " dashboard de anuncio de donación (eatc_dona_dsh) ", pasando el identificador del encabezado ( eatc-id ). 

 Botón: consulta de novedades de anuncio de donación 
 Con este botón se debe generar una consulta al registro de novedades ( eatc_odd_rejection_registry ) para el anuncio particular, como una especie de detalle adicional, en el cual se debe presentar toda la información que trae la consulta. 

 Ejemplo: 
 Para el anuncio cuyo código de encabezado ( eatc-dona_header_code) es 40716, el sistema debe realizar la siguiente consulta para mostrar los detalles o novedades registradas 

 https://donantes.eatcloud.info/api/abaco/eatc_odd_rejection_registry?eatc-dona_header_code=40716 

 CHECKBOX PARA SELECCIONAR ANUNCIOS A SER PRE-CERTIFICADOS 
 Cada anuncio debe tener un botón que permita seleccionarlo para ser "pre-certificado".  El usuario puede seleccionar uno, varios o todos los anuncios presentes en la lista (debe haber una funcionalidad rápida para seleccionarlos todos" 

 BOTON: "Generar constancia de donación" 
 Una vez que se halla seleccionado por lo menos un anuncio de donación a "pre-certificar", se debe mostrar el botón "generar constancia de donación".  Al oprimirlo, el sistema debe cambiar el estado de todos los anuncios seleccionados a "pre-certified" o "pre-certificado" y generar un informe, que debe ser susceptible de ser impreso o enviado a una dirección de correo electrónico con la siguiente información, construida a partir de la información de los anuncios seleccionados: 

 Municipio:   Siempre será " Bogotá " (obligatorio) 
 Fecha de expedición de la constancia:  {Día} del {Mes} de {Año} que corresponde a la fecha actual, es decir la fecha en la que se oprimió el botón para generar la constancia Ej: 01 de Enero de 2019 (obligatorio) 
 Consecutivo : Todos las constancias de donación debe emitirse con un número de consecutivo, con prefijo EC-Cons, iniciando desde el Número 1 (obligatorio) 
 Año :  en formato (yyyy), corresponde al año en curso (obligatorio) 
 Mes de entrega de la donación: Mes de la entrega de la donación  Ej: "Enero".  Debe corresponder al mes o los meses que se encuentran registrados en la fecha eatc_dona_headers .eatc-receipt_datetime   (obligatorio) 
 Año de entrega donación: en formato (yyyy). Debe corresponder al año o los años que se encuentran registrados en la fecha eatc_dona_headers .eatc-receipt_datetime (obligatorio). 
 Donante: razón social del donante, corresponde al dato eatc_dona_headers .eatc-donor (obligatorio) 
 Número de identificación del donante: Identificador único del donante (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, sin el dígito de verificación (obligatorio) 
 DV: Dígito de verificación del (NIT), corresponde al dato eatc_dona_headers .eatc-donor_code, después del "-", o dígito de verificación (obligatorio) 
 Kilos: Cantidad de kilos reportados como recibidos acorde a la donación anunciada y entregada .  Corresponde a la sumatoria del campo eatc_dona_headers .eatc-total_weight_kg de todos los anuncios de donación seleccionados (obligatorio) 
 Categoría: Categoría del producto entregado en donación anunciada y entregada.  Corresponde a un array del distinct de categorías presentes en los detalles de todos los anuncios de donación seleccionados para certificar eatc_dona. eatc-odd_typology_a (obligatorio) 
 Documento soporte de entrega de donación: número de documento asociado a la entrega del producto, puede ser 1 documento o varios documentos. Corresponde al array de eatc_dona_headers .eatc-code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio) 
 Organizaciones beneficiada(s): Nombre del gestor de donación o los gestores de donaciones a los cuales se les adjudicaron los anuncios, puede ser 1 o varias organizaciones.  Corresponde al array de datos de eatc- eatc_dona_headers . donation_manager_name de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIÓN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.  DE SER NECESARIO EL BANCO HABRÍA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIÓN EN https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA y con ese dato obtener con la misma API el nombre de dicho banco) 
 NIT Beneficiarios :  Identificador de los gestores de donaciones (NIT), puede ser 1 o varios (obligatorio). Corresponde al array de datos de eatc_dona_headers . donation_manager_code de los anuncios que fueron seleccionados para ser pre-certificados (obligatorio). OJO QUE LA ESPECIFICACIÓN HABLA DE BANCOS DE ALIMENTOS NO DE BENEFICIARIOS.  DE SER NECESARIO EL BANCO HABRÍA QUE HACER UN QUERY PARA ESTABLECER EL BdeA PADRE DE CADA INSTITUCIÓN EN https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro= eatc_dona_headers .eatc-donor_code trayendo el campo eatc_donation_managers. organizacion_vinculada (solo para aquellos cuya eatc_donation_managers. tipo_organizacion es diferente a BdeA) 
 Representante legal ABACO: siempre será el de ABACO. Corresponde al dato "representante_legal" de la siguiente consulta: https://beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador=ABACO (obligatorio) 
 Cargo:   Siempre se escribe: Director Ejecutivo (obligatorio) 
 Elaboró certificado: Debe parametrizarse por ahora las siguientes iniciales: N.J.H.H. Si N.J.H.H. (obligatorio) 
 Aprobo certificado: Debe parametrizarse por ahora las siguientes iniciales: I.V.B.P. Si I.V.B.P. (obligatorio) 
 Reviso certificado: Debe parametrizarse por ahora las siguientes iniciales: M.M.P. Si M.M.P. (obligatorio) 

 ***NUEVO***Datos que se llevan al encabezado del anuncio de donación 
 Cuando se genera la constancia se deben llevar los siguientes datos al registro de los encabezados que: 
eatc_dona_headers . eatc_constancy_datetime : corresponde al timestamp de cuando se realizó la constancia en formato AAAA-MM-DD HH:MM:SS 
eatc_dona_headers . eatc_constancy_consecutive : corresponde al consecutivo de la constancia que se generó 

 NOTA IMPORTANTE: 
 Anteriormente el proceso de generación de constancia llevaba el dato " pre-certified " a eatc_dona_headers . eatc_state . Esta especificación implica precisamente reemplazar dicho registro, por lo tanto al crearse la constancia se debe garantizar que el eatc-state sea " pre-certified ". 

 Descarga de detalles de anuncios de donación pre-certificados 
 Se debe permitir descargar un archivo en Excel o .csv que contenga los detalles de los anuncios certificados y que tenga la siguiente estructura: 

 Fecha y hora : eatc_dona. eatc-date_time 
 Mes: mes(eatc_dona. eatc-date_time ) 
 Código : eatc_dona. eatc-dona_header_code 
 Nombre del punto de donación : eatc_pods. eatc-name (WHERE eatc_id=eatc_dona. eatc-pod_id) 
 Código producto : eatc_dona. eatc-odd_id 
 Descripcion del PLU : eatc_dona. eatc-odd_name 
 KG aprovechados : eatc_dona. eatc-odd_total_weight_kg 
 KG No aprovechados : (eatc_dona. eatc-odd_original_quantity * eatc_dona. eatc-odd_unit_weight_kg) - eatc_dona. eatc-odd_total_weight_kg 
 Sublinea ABACO : Pendiente. 
 Banco / Institución que recoge : eatc_dona_headers. donation_manager_name (WHERE eatc-code=eatc_dona. eatc-dona_header_code 
 Tarifa de Iva : eatc_dona. eatc-total_VAT 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO BENEFICIARIOS 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 6fa8e8cd-91ca-4e9f-937d-e92aa6906890 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 05e9b4b1-8b4d-4f64-99d0-363633fb8081 
 2025-05-30T23:14:42.3361881Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"c6a6ac15-d569-4c87-8250-ba491cff9d02","SequenceId":134,"FluidContainerCustomId":"89d88b46-5d4d-4069-9c4e-c9011b4c6aec","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 GENERACIÓN DE CONSTANCIA DE DONACIÓN