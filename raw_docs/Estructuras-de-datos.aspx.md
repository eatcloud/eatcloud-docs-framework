# Estructuras-de-datos.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

 eatc_cua&#58; configuración de cuentas maestras 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?_campos &#160; 
&#160; 
name 
Nombre de la cuenta usuario. &#160;Se utiliza como un identificador único de la cuenta a lo largo de la plataforma 
&#160; 
eatc_country 
País en donde se ubica la cuenta&#58; 
Los posibles valores del país se pueden consultar en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_*&amp;_cmp=iso2 &#160; 
eatc_cua_master 
Cuenta maestra a la cual pertenece la cuenta&#58; 
Los posibles valores las cuentas maestras se pueden consultar en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_*&amp;_cmp=eatc_cua &#160; 
vertical 
Vertical a la cual pertenece la cuenta. 
Los posibles valores de la vertical se pueden consultar en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id=_*&amp;_cmp=eatc_name &#160; 
&#160; 
type 
Tipo de licencia rescate que posee la cuenta. 
Los posibles valores de tipos de licencias rescate se pueden consultar en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_types_of_licenses?eatc_code=_*&amp;_cmp=eatc_code &#160; 
creation_datetime 
Fecha y hora en la cual se crea la cuenta 
creation_date 
Fecha en la cual se crea la cuenta 
last_modification_datetime 
Fecha y hora de la última modificación de la información de la cuenta 
last_modification_date 
Fecha de la última modificación de la información de la cuenta 
eatc_dona_upl 
Parámetro de configuración para establecer si la cuenta puede crear donaciones a través de la webapp ( yes &#58; las puede crear. no &#58; no las puede crear) 
edit_coordinates 
Parámetro de configuración para establecer si la cuenta puede crear donaciones desde múltiples puntos de donación, que serán seleccionados antes de crear la donación en la webapp ( si &#58; las puede crear donaciones desde múltiples puntos. no &#58; solo puede crear donaciones desde el propio punto de donación) 
multiple_donors 
Parámetro de configuración que establecerá si se podrán realizar donaciones asociados a múltiples razones sociales e identificadores fiscales ( si &#58; se pueden crear donaciones de múltiples razones sociales. no &#58; solo puede crear donaciones de una razón social) 
eatc_odds_app 
Parámetro de configuración que establecerá de donde se obtiene o captura la información de los productos (código y nombre) para crear anuncios de donación ( eatc_dona_app &#58; indicará que la información del producto se captura por la webapp. eatc_odds &#58; indica que la información se toma de un maestro de productos) 
odds_weight 
Parámetro de configuración que establecerá de donde se obtiene o captura la información del peso (en kg) de los productos &#160;para crear anuncios de donación ( eatc_dona &#58; indicará que la información de peso del producto se captura por la webapp. eatc_odds &#58; indica que la información se toma de un maestro de productos) 
costs 
Parámetro de configuración que establecerá de donde se obtiene o captura la información del costo de los productos &#160;para crear anuncios de donación ( eatc_dona &#58; indicará que la información del costo del producto se captura por la webapp. eatc_odds &#58; indica que la información se toma de un maestro de productos. eatc_odds_costs &#58; indica que se tomará de un maestro de costos) 
taxes 
Parámetro de configuración que establecerá de donde se obtiene o captura la información de los impuestos de los productos para crear anuncios de donación ( eatc_dona &#58; indicará que la información impositiva del producto se captura por la webapp. eatc_odds &#58; indica que la información se toma de un maestro de productos. eatc_odds_costs &#58; indica que se tomará de un maestro de costos) 
days_before_expiration 
Parámetro de configuración que permitirá configurar la fecha de vencimiento por defecto que presenta la plataforma para registrar en la donación la respectiva fecha de caducidad de los productos. Para más información consultar aquí . 
 eatc_rec_doc&#160; 
 En eatc_dona_headers se utiliza el campo para dejar una traza de auditoría cuando se reestablece una donación, indicando el proceso que la reestableció, y originalmente quién y cuándo la borró. 
 En eatc_deleted_dona_header, si tiene un “y” como dato, indica que la donación fue reestablecida. 
 (en desuso) Parámetro de configuración que permite llevar información de documento de recolección a la donación. &#160;Para mayor información consultar aquí . 
 eatc_rec_doc_signature (en desuso) 
 Parámetro de configuración que permite llevar información de la firma del documento de recolección a la donación. &#160;Para mayor información consultar aquí . 
 eatc_rec_odds_pre_verification (en desuso) 
 Parámetro de configuración que permite llevar información al encabezado de las donaciones. &#160;Para mayor información consultar aquí . 
faqs_url 
Parámetro de configuración que permite establecer una URL para preguntas frecuentes, personalizada por donante https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/preguntas-frecuentes.aspx &#160; 
not_delivery_instructions 
Parámetro de configuración que permitirá establecer instrucciones particulares ante una no entrega para desplegarlas a los beneficiarios&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/tengo-problemas-para-que-me-entreguen.aspx &#160; 
eatc_user_manual 
Parámetro de configuración que permitirá entregar manuales de usuario diferenciales por cuenta en la webapp donantes&#58;&#160; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/manual-de-usuario.aspx &#160; 
eatc_cua_size 
Tamaño de la cuenta. &#160;Cada vertical posee diferentes tamaños los cuales se pueden consultar aquí&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_size_mt?_id=_*&amp;_cmp=eatc_vertical_code,eatc_code &#160; 
eatc_default_certification_support 
Parámetro de configuración que permite establecer cuál es el método de soporte para la elaboración de certificados de donación (por el momento las posibles opciones son&#58; carta_colombia y factura_electronica_colombia ) 
eatc_days_back_pending_code_vrf 
Parámetro de configuración que sirve para establecer un número de días particular por cuenta, para mostrar anuncios pendientes de gestión en el dashboard de la webapp. &#160;Para mayor información consultar aquí . 
type_period 
Parámetro de configuración para establecer el periodo por el cual se contratan las licencias ( lbl_mensual &#58; mensual. lbl_anual_ahoras_15pc &#58; anual). 
 sale_pwa (en desuso) 
 Parámetro para definir si la cuenta contaría con una Progresive WebApp para la venta de ofertas de último minuto (modelo de negocio que nunca se concretó) 
 sale_wapp (en desuso) 
 Parámetro para definir si la cuenta contaría con una funcionalidad en la webapp para generar ofertas de último minuto (modelo de negocio que nunca se concretó) 
eatc_postal_code 
Código postal de la cuenta 
eatc_doc_madatory 
Parámetro de configuración que indica si la captura de documento soporte en la donación es obligatorio ( y ) o no. Para mayor información consultar https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/creaci%C3%B3n-de-anuncio-de-donaci%C3%B3n-eatc_dona_upl.aspx#obligatoriedad-***nuevo-obligatoriedad-seg%C3%BAn-par%C3%A1metro-de-configuraci%C3%B3n*** y https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/donantes-verificaci%C3%B3n-del-codigo-de-recogida.aspx#captura-de-documento-soporte &#160; 
logo_proof_of_delivery 
Parámetro de configuración que permite configurarle un logo personalizado a un documento de constancia de entrega. &#160;Para mayor información consultar aquí . 
contract_supervisor 
Parámetro de configuración que permite configurarle información personalizada a un documento de constancia de entrega. &#160;Para mayor información consultar aquí . 
eatc_days_to_short_date 
Parámetro de configuración que se utiliza para clasificar según el donante cuando una donación se puede calificar como de fecha corta o no. &#160;Para más información consultar&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/short_dates_classification.aspx &#160; 
eatc_mandatory_closer_exp_date 
Parámetro de configuración que permite establecer la captura obligatoria de la fecha de vencimiento ( y ) de los productos para realizar una donación. 
eatc_program_dona_email 
Parámetro de configuración que permite establecer si se envía un correo electrónico a un encargado en el donante ante una programación de una donación. &#160;Para mayor información consultar aquí . 
eatc_special_project 
Permite asociar la cuenta a un proyecto especial. &#160;Los proyectos especiales se pueden consultar en&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_special_projects?_id=_* &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 12;#i:0#.f|membership|juan.correa@eatcloud.com 
 Juan David Correa 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 1925d49c-cf85-4695-a70d-fd9a3e3e42ce 
 4!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 ca55abee-503c-4ff2-a089-21709d67b2fe 
 2025-12-11T06:34:13.9046510Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"b1a2d390-b66f-45a9-9570-6da3ecf706d1","SequenceId":692,"FluidContainerCustomId":"3abfbeab-2156-45e3-8cb5-32f2c26e2c12","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Estructuras de datos