# Vista-de-inventario-para-hubs-de-distribución.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo&#58;&#160; esta funcionalidad permitirá visualizar las unidades disponibles según el Kardex que se crea mediante el servicio “ donatokardex ”. &#160;El principal control que debe tener la funcionalidad es que en el listado de unidades disponibles deberá visualizar el último registro de “kardex” para un producto en particular. &#160;Si en dicho registro las cantidades disponibles son iguales a cero, no se mostrará en el listado. &#160;Esta funcionalidad se puede basar en la implementación previa ya realizada de la tabla de información de productos para agregar cantidades de la funcionalidad de creación de distribución y cuya visual se adjunta a continuación&#58; &#160;( https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/btcredona ) &#160; 

 VALIDACIONES PREVIAS ANTES DE DESPLEGAR LA FUNCIONALIDAD 
 Nota &#58; similar a las validaciones para visualizar las funcionalidades de hub de donaciones&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/btcredona y https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/btseldona &#160; 
 Validación del estado y la condición del gestor de donaciones como hub de distribución. 
 El sistema realiza la siguiente consulta, utilizando el &quot; identificador_unico_registro &quot; del beneificario que está logueado en la plataforma &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-state= activo &amp;eatc_dist_hub= y&amp;_cmp= eatc-state,eatc_dist_hub 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
&#160; 
 class= lbl_doma_no_valido ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_doma_no_valido )&#160; &#160; &quot;El gestor de donaciones, no está configurado para operar un hub de distribución. ( error_code&#58; doma_config)&quot; 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema permite seguir adelante con la siguiente validación. 

&#160; 
 Ejemplo 1&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_distributor &#58; &quot; 811018073 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811018073&amp;eatc-state=activo&amp;eatc_dist_hub=y&amp;_cmp=identificador_unico_registro &#160; &#160; 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema permite seguir adelante. 

&#160; 
 Ejemplo 2&#58; entorno de pruebas, cua_master &quot; abaco &quot;, eatc_dona_distributor &#58; &quot; 811000384 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=811000384&amp;eatc-state=activo&amp;eatc_dist_hub=y&amp;_cmp=identificador_unico_registro &#160;&#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 &quot;El gestor de donaciones, no está configurado para operar un hub de distribución. ( error_code&#58; doma_config)&quot; 

&#160; 
 Validación de la configuración del gestor de donaciones como donante para gestionar las distribuciones. 
 El sistema realiza la siguiente consulta, utilizando el &quot; identificador_unico_registro &quot; del beneificario que está logueado en la plataforma &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;fielddecrypt=eatc_cua &#160; 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
&#160; 
 class= lbl_doma_no_configurado ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_doma_no_configurado ) &quot;El gestor de donaciones, no está configurado para entregar donaciones como hub de distribución. ( error_code&#58; doma_cua_config)&quot; 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema, guarda el dato &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &#160;(que corresponde al nombre de la cua_user que ha sido asignado al gestor de donaciones que administra un hub de distribución) y despliega la funcionalidad que se define a continuación . 

&#160; 
 Ejemplo 1&#58; entorno productivo, eatc_dona_distributor &#58; &quot; 900082682 &quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=900082682&amp;fielddecrypt=eatc_cua &#160; &#160; 
&#160; 
 El sistema guarda el valor &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125;= fubam para utilizarlo más adelante en el proceso 
&#160; 
 Dada la respuesta válida que trae el servicio entonces el sistema despliega la funcionalidad .&#160; 

&#160; 
 Ejemplo 2&#58; entorno productivo, eatc_dona_distributor &#58; &quot; 811000387 &quot; 
&#160; 
 EEl sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=811000387&amp;fielddecrypt=eatc_cua &#160;&#160; &#160; 
 &#160; &#160; 
 Dado que no se obtiene una respuesta válida por parte del sistema entonces el sistema despliega la respuesta&#58; 
 &#160; 
 &quot;El gestor de donaciones, no está configurado para entregar donaciones como hub de distribución. ( error_code&#58; doma_cua_config)&quot; 

&#160; 
 Días para el último movimiento&#58; ***NUEVO&#58; &#160;se separan kardex por cua_user correspondiente al gestor de hubs *** 
 Nota&#58; evaluar si esto aplica, y sería similar a la implementación realizada en&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/btcredona &#160; 
&#160; 
 Label (place holder)&#58; class= lbl_dias_ult_mov ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_dias_ult_mov ) 
 Tipo de dato&#58; integer 
 Obligatoriedad &#58; si 
 Validación &#58; obligatoriedad, valor numérico, valor máximo&#58; 30 días. 
 Tipo de campo de captura&#58; campo de numérico 
 Valor por defecto&#58; 7 
&#160; 
 El usuario podrá variar el valor de los días del último movimiento de inventario y lo llevará a la variable &#123;&#123; dias &#125;&#125; , con este valor,&#160; calculará la fecha inicial de la consulta 
 &#123;&#123; fecha_inicial &#125;&#125; = &#123;&#123;fecha_actual&#125;&#125; - &#123;&#123; dias &#125;&#125; 
&#160; 
 Con estos datos y el dato &#160; &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &#160;(obtenido en el proceso de&#160; validación del gestor de donaciones como donante ), &#160;&#123;&#123;eatc_dona .eatc_donor &#125;&#125; el sistema realiza la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/ &#123;&#123; eatc_customers_cua .eatc_cua&#125;&#125; / eatc_kardex ? eatc_cua_origen= &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; &amp; eatc_date[0]=&#123;&#123; fecha_inicial &#125;&#125;&amp;eatc_date[1]=&#123;&#123; fecha_actual &#125;&#125; &amp; eatc_actual_stock=_&gt;0 &amp;_cmp= _id,eatc_odd_id,eatc_odd_name, eatc_donor,eatc_odd_unit_weight_kg.eatc_closer_expiration_date,eatc_return_cause,eatc_date_time,eatc_actual_stock 
&#160; 
 En vez de tener un kardex por cuenta maestra (como estaba anteriormente y se muestra a continuación), se tienen kardex por cua_user correspondiente al gestor de donaciones que administra el hub ( &#123;&#123;eatc_customers_cua. eatc_cua &#125;&#125; ), esto con el objetivo de poder controlar el inventario para cada administrador del hub y no tener un kardex global que pueda mezclar inventarios de varios gestores de donaciones administradores de hubs. 
&#160; 
 El sistema agrupará por eatc_odd_id y determinará para cada arreglo de datos, si el registro más reciente (según&#160; eatc_date_time ), posee stock ( eatc_act_stock mayor que cero) con esos registros&#160; más recientes con existencias, armará una tabla de datos que tendrá un campo para agregar cantidades y que presentará la siguiente información&#58; 

&#160; 
 Tabla de información de productos, para consultar cantidades disponibles&#58; 
 Nota&#58; muy similar a la implementación realizada en&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/btcredona 
 Esta tabla paginada, deberá tener la oporunidad de filtrar por columnas, buscar registros y ordenar por columnas, y presentará la siguiente información&#58; 
 ID 
 label&#58; class= lbl_id ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_id ) 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. eatc_odd_id &#125;&#125; &#160;&#160; 

&#160; 
 Nombre 
 label&#58; class= lbl_nombre ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_nombre ) &#58; 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. eatc_odd_name &#125;&#125; &#160;&#160;&#160; 

&#160; 
 Donante 
 label&#58; class= lbl_donante ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_donante ) 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. eatc_donor &#125;&#125; &#160;&#160;&#160; 

&#160; 
 Peso unitario en KG 
 label&#58; class= lbl_peso_unitario_kg ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_peso_unitario_kg ) 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. eatc_odd_unit_weight_kg &#125;&#125; &#160;&#160;&#160; 

&#160; 
 Fecha de vencimiento 
 label&#58; class= lbl_fecha_vencimiento ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_fecha_vencimiento ) 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. act &#125;&#125; &#160; 
 &#160;&#160; 
 Cantidades en inventario 
 label&#58; class= lbl_cant_inv ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=beneficiarios&amp;idlabel= lbl_cant_inv ) 
 Presenta la información contenida en&#58; &#123;&#123;eatc_kardex. eatc_act_stock &#125;&#125; &#160;&#160;&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FVista-de-inventario-para-hubs-de-distribuci%C3%B3n%2F3620476566-Listado-productos.jpg&ow=800&oh=410, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FVista-de-inventario-para-hubs-de-distribuci%C3%B3n%2F3620476566-Listado-productos.jpg&ow=800&oh=410 

 f5abd853-0207-4533-9fb2-b7e23d2c999f 
 1!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 391e014d-c1cd-4390-9e33-669a2f04c6f9 
 2025-04-15T04:08:39.0652898Z 

 {"SessionId":"85c1c3d9-1d63-45a5-918c-5181cdfc94af","SequenceId":2385,"FluidContainerCustomId":"3408d4c6-5287-44ae-a150-7827d061eee8","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 991.000000000000 

 Vista de inventario para hubs de distribución