# seleccionar-donaciones-para-distribuir.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo&#58;&#160; esta funcionalidad permitirá seleccionar donaciones (eatc_dona_header_code) o porciones de donaciones (es decir productos específicos de una donación eatc_dona. eatc-odd_id ), para invocar el servicio &quot; donatokardex &quot; a través de su respectiva API Pública , con el ánimo de transformar dichas donaciones (recibidas por el beneficiario que está autenticado en la plataforma),&#160; en registros de inventario (Kardex) a partir de los cuales se realizarán distribuciones de donaciones a otras organizaciones sociales. &#160; Por lo tanto esta funcionalidad, presentará principalmente una tabla de datos de los encabezados de donaciones, dando la opción (por defecto) de seleccionar toda una donación para distribuir, o a demanda del usuario, definir de dicha donación qué detalles seleccionar (con la opción de establecer cantidades específicas de dichos detalles) y así tener los datos para invocar el servicio para la generación de registro de inventario 

 Validaciones previas antes de desplegar la funcionalidad 
&#160; 
 Validación del estado y la condición del gestor de donaciones como hub de distribución. 
 El sistema realiza la siguiente consulta, utilizando el &quot; identificador_unico_registro &quot; del beneificario que está logueado en la plataforma &#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123;eatc_donation_managers. identificador_unico_registro &#125;&#125;&amp;eatc-state= activo &amp;eatc_dist_hub= y&amp;_cmp= eatc-state,eatc_dist_hub 
&#160; 
 Si la consulta no arroja un resultado, el servicio deberá entregar la siguiente respuesta&#58; 
 class= lbl_doma_no_valido&#160; &quot;El gestor de donaciones, no está configurado para operar un hub de distribución. ( error_code&#58; doma_config)&quot; 
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
 class= lbl_doma_no_configurado&#160; &quot;El gestor de donaciones, no está configurado para entregar donaciones como hub de distribución. ( error_code&#58; doma_cua_config)&quot; 
&#160; 
 Si la consulta arroja respuesta una respuesta válida el sistema despliega la funcionalidad que se define a continuación. 

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

 Filtro de fechas 
 Nota para el desarrollo&#58; este filtro solo debe permitir traer las donaciones de la última semana (como parametrización inicial, es posible que con posterioridad se pueda modular este parámetro para que permita traer donaciones de más días atrás 
&#160; 
 Filtro&#58; &quot;Última semana&quot; = &gt; Valor por defecto 
 class=&quot; lbl_ultima_semana &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_ultima_semana )&#160; 
&#160; 
 El filtro permitirá por defecto solamente seleccionar los datos de la última semana, así que&#160; 
 &#123;&#123; fecha_inicial_periodo &#125;&#125;= &#123;&#123;día actual - 8 días&#125;&#125; ***En formato AAAA-MM-DD*** 
 &#123;&#123; fecha_final_periodo &#125;&#125; = &#123;&#123;día actual&#125;&#125; ***En formato AAAA-MM-DD*** 
&#160; 
 Filtro&#58; &quot;Personalizar&quot; 
 class=&quot; lbl_personalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_personalizar )&#160; 
&#160; 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_inicial ) Solo permitirá seleccionar hasta 15 días atrás en el calendario 
&#160; 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_fecha_final ) valor por defecto, fecha actual. 
&#160; 
 class=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel= lbl_consultar ) 
 Selector de ciudad&#58; 
 El sistema debe realizar el siguiente llamado,&#160; teniendo en cuenta el identificador único de registro del gestor de donaciones cuyo usuario está logueado en la plataforma BO Beneficiarios ( &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; )&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc_state2= ! distributed &amp;_distinct=eatc-city 
&#160; 
El usuario selecciona la ciudad &#123;&#123; ciudad_seleccionada &#125;&#125; y con ella se construye el siguiente selector 
 Selector de cuenta&#58; 
 El sistema debe realizar el siguiente llamado,&#160; teniendo en cuenta el identificador único de registro del gestor de donaciones cuyo usuario está logueado en la plataforma BO Beneficiarios ( &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; )&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-city= &#123;&#123; ciudad_seleccionada &#125;&#125; &amp; eatc_state2= ! distributed &amp;_distinct=eatc-donor 
&#160; 
El usuario selecciona el donante &#123;&#123; donante_seleccionado &#125;&#125; y con ella se construye el siguiente selector 
 Selector de punto de donación&#58; 
 El sistema debe realizar el siguiente llamado,&#160; teniendo en cuenta el identificador único de registro del gestor de donaciones cuyo usuario está logueado en la plataforma BO Beneficiarios ( &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; )&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-city= &#123;&#123; ciudad_seleccionada &#125;&#125; &amp; eatc-donor= &#123;&#123; donante_seleccionado &#125;&#125; &amp; eatc_state2= ! distributed &amp;_distinct= eatc-pod_name 
&#160; 
El usuario selecciona punto de donación &#123;&#123; pod_seleccionado &#125;&#125; y con ella se construye el siguiente selector 
&#160; 
 Selector de donación&#58; 
 El sistema debe realizar el siguiente llamado,&#160; teniendo en cuenta el identificador único de registro del gestor de donaciones cuyo usuario está logueado en la plataforma BO Beneficiarios ( &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; )&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp; eatc-donation_manager_code= &#123;&#123; eatc_donation_managers . identificador_unico_registro &#125;&#125; &amp;eatc-receipt_datetime= ! 0000-00-00 %20 00&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp; eatc-city= &#123;&#123; ciudad_seleccionada &#125;&#125; &amp; eatc-donor= &#123;&#123; donante_seleccionado &#125;&#125;&amp; eatc-pod_name =&#123;&#123; pod_seleccionado &#125;&#125; &amp; eatc_state2= ! distributed &amp;_cmp= eatc-code,eatc-total_weight_kg,eatc_dona_references 
&#160; 
El sistema arma un selector de donaciones, en donde aparezca su código, los KG y las referencias de la donación. 
&#160; 
Con la selección de la donación el sistema trae la información para generar la tabla de productos para adicionar al kardex. 

 DEPRECADO&#58; Opción de para seleccionar varias cuentas, o todas (SELECTOR MÚLTIPLE) 
 Con los datos traídos por llamado anterior, el sistema construye un selector múltiple (con la opción de seleccionar todas las cuentas ( class=&quot;lbl_todas&quot; ).&#160; Cuando el usuario realiza su selección entonces el sistema construye con los donantes seleccionados un array de respuestas que servirán para las posteriores consultas&#58; 
&#160; 
 &#123;&#123;array_eatc_donor&#125;&#125; 
 DEPRECADO&#58; Llamado para traer la información para construir la vista de tabla con selección múltiple. 
 El sistema debe realizar el siguiente llamado&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-publication_date[0]=&#123;&#123; fecha_inicial_periodo &#125;&#125;&amp;eatc-publication_date[1]=&#123;&#123; fecha_final_periodo &#125;&#125;&amp;eatc-donation_manager_code=&#123;&#123;eatc_donation_managers . identificador_unico_registro &#125;&#125;&amp;eatc-receipt_datetime=!0000-00-00%2000&#58;00&#58;00&amp;eatc-state=delivered,received,pre-certified,certified&amp;eatc_state2= ! distributed&amp;eatc-donor=&#123;&#123;array_eatc_donor&#125;&#125;&amp;_cmp= eatc-code,eatc-publication_date,eatc-publication_datetime,eatc-state,eatc_state2,eatc-total_weight_kg,eatc-total_cost 
 Informe que permita ordenar por columnas, y que su disposición siempre deje visible el botón &quot;Disponibilizar donaciones para distribuir&quot; 
 El informe deberá permitir ordenar la información por columnas, y el botón de acción &quot; Disponibilizar para distribución &quot;, deberá siempre estar presente en la visual del usuario (bien sea que se ubique abajo o al principio de la tabla.&#160; Esta documentación lo relaciona abajo de la tabla para denotar el orden de las acciones de la funcionalidad, pero la ubicación del botón la podrá definir el desarrollador), de tal manera que cuando el usuario termine de realizar las selecciones que hace la tabla, pueda oprimir fácilmente el botón que invocará el servicio &quot; donatokardex &quot; a través de su respectiva API pública . 
 INFORMACIÓN A MOSTRAR EN LA TABLA PARA SELECCIONAR DONACIONES A DISTRIBUIR. 
 El objetivo principal de esta tabla es el de seleccionar las donaciones, o las porciones de donaciones, que estarán disponibles para distribuir, y a nivel técnico esto quiere decir, obtener la información de los parámetros necesarios para invocar el servicio &quot; donatokardex &quot; a través de su respectiva API pública . Por ese motivo, la tabla deberá tener un comportamiento de tabla para la selección múltiple de registros, y también a partir de una selección en uno de sus selectores, permitir el despliegue de una subtabla, tipo acordeón, para permitir realizar selecciones a nivel de detalle de la donación. 
 Título de la tabla&#58; Donaciones a disponibilizar para distribuir 
 Label&#58; class=&quot;lbl_donaciones_a_distribuir&quot; 
 Descripción (de cara al usuario)&#58; 
 Label&#58; class=&quot;lbl_donaciones_a_distribuir_desc&quot; 
 &quot;En la presente tabla podrás encontrar las donaciones que podrán ser distribuidas a otras organizaciones sociales.&#160; Selecciona las donaciones o las porciones de donaciones que deseas estén disponibles (a través de un sistema de control de inventarios) para crear anuncios de distribución de donaciones que podrán ser gestionados a través de nuestras diversas plataformas&quot; 
&#160; 
 La tabla contendrá las siguientes columnas de información&#58; 
 Seleccionar 
 Label&#58; class=&quot;lbl_seleccionar&quot; 
&#160; 
 En esta columna se ubicará un cuadro de selección múltiple, con la opción de &quot;seleccionar todo&#160; ( class=lbl_seleccionar_todo )&quot;, y que permitirá definir cuál o cuáles donaciones del listado se podrán &quot;distribuír&quot;. Por cada donación &quot;seleccionable&quot;, el usuario verá (en las siguientes columnas) la siguiente información. 
 Código del anuncio 
 Label&#58; class=&quot;lbl_codigo_anuncio&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-code 
 Fecha Publicación 
 Label&#58; class=&quot;lbl_fecha_publicacion&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_date 
 Fecha y hora 
 Label&#58; class=&quot;lbl_fecha_hora&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-publication_datetime 
 Estado 
 Label&#58; class=&quot;lbl_estado&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-state 
 Estado 2 
 Label&#58; class=&quot;lbl_estado2&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-state2 
 Kg recibidos 
 Label&#58; class=&quot;lbl_kg_recibidos&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-total_weight_kg &#160; 
 Costo 
 Label&#58; class=&quot;lbl_costo&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-total_cost &#160;&#160; 
 Tipo de distribución&#58; 
 Label&#58; class=&quot;lbl_tipo_distribucion&quot; 
&#160; 
 Selector único, con dos posiciones (y con un valor por defecto) 
 Distribución total&#58; class= lbl_distribucion_total =&gt; Valor por defecto 
&#160; 
 Si el selector no se cambia, es decir, se deja selecionada la opción &quot; Distribucion total &quot; el sistema, no despliega la subtabla 
&#160; 
 Distribución parcial&#58; class= lbl_distribucion_parcial 
&#160; 
 Si el usuario cambia el valor por defecto y selecciona esta opción &quot; Distribucion parcial &quot;&#160; el sistema abre una subtabla con los detalles de la donación en cuestión (tipo acordeon), que más adelante se detalla y que contendrá información de los detalles de la donación, para realizar una donación parcial. 
 Donante 
 Label&#58; class=&quot;lbl_donante&quot; 
 La información se toma de&#58; eatc_dona_headers . eatc_donor 
 ID Donante 
 Label&#58; class=&quot;lbl_id_donante&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc_donor_code 
 Razón Social 
 Label&#58; class=&quot;lbl_razon_social&quot; 
 Orden&#58; después de ID Donante 
 La información se toma de&#58; eatc_dona_headers .eatc_donor_fiscal_name &#160; 
 Cuenta Origen 
 Label&#58; class=&quot;lbl_cuenta_origen&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc_cua_origin 
 Fecha recepción 
 Label&#58; class=&quot;lbl_fecha_recepcion&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-receipt_datetime 
 Warning 
 Label&#58; class=&quot;lbl_alerta&quot; 
 La información se toma de&#58; eatc_dona_headers .eatc-warning 

 &#160; 
 Tabla&#58; Detalle de donaciones 
 Si el usuario, en el selector de de tipo de distribución, selecciona la opción &quot; lbl_distribucion_parcial &quot;, imnediatamente después de los datos del encabezado, se desplegará una subtabla (tipo acordeón) con la siguiente información y funcionalidad asociada a los detalles de la donación&#58; 
&#160; 
 Llamado para construir la tabla 
 Con el código de la donación ( &#123;&#123;eatc_dona_headers .eatc-code &#125;&#125; ), a la cual se le indicó realizar una disttribución parcial, el sistema realiza la siguiente consulta, para construir, la tabla que permtirá definir los parámetros con los cual se invoca el servicio &quot; donatokardex &quot; a través de su respectiva API pública 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_dona? eatc-dona_header_code = &#123;&#123;eatc_dona_headers .eatc-code &#125;&#125; &amp; eatc_state2 = ! distributed &amp;_cmp= eatc-dona_header_code,eatc-doc,eatc-odd_id,eatc-odd_code,eatc-odd_name, eatc-odd_quantity,eatc_odd_available_quantity ,eatc-odd_unit_weight_kg,eatc-odd_unit_cost,eatc-VAT_percentage,origin_odds_typology_a,origin_odds_typology_b,origin_odds_typology_c,eatc-odd_typology_a,eatc-odd_typology_b,eatc-odd_typology_c,eatc-odd_external_code,eatc-pod_id,eatc_donor,eatc-provider_id,eatc-return_cause_code,eatc-return_cause,eatc-contains_alergens,eatc-closer_expiration_date,eatc_lote, eatc_state2 &#160; 
&#160; 
 Con los datos traídos se construye la sub-tabla, que deberá desplegar la siguiente información y funcionalidad 
&#160; 
 Seleccionar 
 Label&#58; class=&quot;lbl_seleccionar&quot; 
&#160; 
 En esta columna se ubicará un cuadro de selección múltiple, que por defecto seleccionará el primer item de detalle de la donación.&#160; Además de esto,&#160; el selector permitirá tener la opción de &quot;Seleccionar todo&quot; ( class= lbl_seleccionar_todo ) .&#160; Si por algún motivo se deseleccionan todos los items de una donación que ha sido marcada como selección parcial, entonces automáticamente el sistema cambia el selector &quot; Tipo de distribución &quot; a la opción &quot; Distribución total &quot;, y cierra (colapsa) la subtabla. 
&#160; 
 Código del producto 
 Label&#58; class=&quot;lbl_codigo_producto&quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_id 
&#160; 
 Nombre del producto 
 Label&#58; class=&quot;lbl_nombre_producto&quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_name 
&#160; 
 Peso unitario en KG 
 Label&#58; class=&quot; lbl_peso_unitario_kg &quot; 
 La información se toma de&#58; eatc_dona .eatc-odd_unit_weight_kg 
&#160; 
 Unidades recibidas 
 Label&#58; class=&quot; lbl_unidades_recibidas &quot; 
 Tipo de dato&#58; entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
 La información se toma de&#58; eatc_dona .eatc-odd_quantity 
&#160; 
 Unidades disponibles ***NUEVO&#58; solamente los vacíos o nulos son los que permiten igualar la las cantidades disponibles a las cantidades &quot; *** 
 Label&#58; class=&quot;lbl_unidades_recibidas&quot; 
 Tipo de dato&#58; entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
 La información se toma de&#58; eatc_dona .eatc-odd_available_quantity &#160; *** Si este valor lleva vacío o nulo entonces la información se toma de eatc_dona .eatc-odd_quantity ***&#160; 
&#160; 
 ANTES&#58; *** Si este valor lleva vacío o nulo, o en cero (se quitó) , entonces la información se toma de eatc_dona .eatc-odd_quantity ***&#160; 
&#160; 
 Unidades a distribuir 
 Label&#58; class=&quot; lbl_unidades_distribuir &quot; 
 Tipo de dato&#58; entero (si el dato es entero) y float de dos decimales (si el dato es una fracción) 
&#160; 
 Input numérico, que se habilita solo para detalles &quot;seleccionados (primera columna)&quot; de la tabla , cuyo valor por defecto será el se muestre en el campo &quot; Unidades disponibles &quot; (aplicando la lógica que se estableción en el comentario anterior).&#160; No permitirá el ingreso de números mayores a las &quot;Unidades disponibles&quot; (si el usuario ingresa un número mayor a las &quot;unidades disponibles&quot; el sistema automáticamente lo corrige, colocando el valor por defecto) y tampoco valores en cero o vacíos (si se ingresa un valor en cero o vacío, automáticamente el item de detalle queda &quot;des-seleccionado (primera columna)&quot; . Permitirá el ingreso de valores decimales con dos dígitos decimales. 
&#160; 
 Fecha de vencimiento 
 Label&#58; class=&quot; lbl_fecha_vencimiento &quot; 
 La información se toma de&#58;&#160; eatc_dona .eatc-closer_expiration_date &#160; 
&#160; 
 Causal de Baja 
 Label&#58; class=&quot;lbl_causal_baja&quot; 
 La información se toma de&#58;&#160; eatc_dona .eatc-return_cause 

&#160; 
 BOTÓN&#58; DISPONIBILIZAR PARA DISTRIBUCIÓN 
 Label&#58; class=&quot;lbl_disp_distribucion&quot; 
&#160; 
 Este botón tendrá la labor, de tomar los datos necesarios, a partir de las selecciones realizadas en la tabla de donaciones, o en las subtablas de detalle, en las cuales el usuario realizó selecciones y (en algunos casos) edición de cantidades a distribuir.&#160; Este botón se activará solamente cuando haya por lo menos una selección de donación a distribuir en la tabla &quot; Donaciones a disponibilizar para distribuir &quot; 
&#160; 
 El proceso que genera el botón deberá tener una serie de controles para prevenir algunos casos, en donde selecciones o elecciones inconclusas por parte del usuario, tengan el potencial de hacer llamados incorrectos al servicio &quot; donatokardex &quot; a través de su respectiva API pública . 
&#160; 
 Los posibles casos que se pueden presentar son los siguientes&#58; 
&#160; 
 Invocación del servicio sin enviar eatc_odd_id y eatc_odd_quantity 
 Dado que para la invocación del API pública, los datos eatc_odd_id y eatc_odd_quantity son opcionales, se puede dar este caso, principalmente en dos circunstancia (una corresponde a un flujo normal y otra a un flujo incorrecto). 
&#160; 
 El usuario seleccionó una o varias donaciones en la tabla &quot; Donaciones a disponibilizar para distribuir &quot; y dejó en todos los casos, el valor por defecto &quot; Distribucion total &quot; en el selector de &quot; tipo de distribución &quot;&#58;&#160; este comportamiento corresponde a un flujo normal. 
 El usuario, habiendo en algunos casos, en la tabla &quot; Donaciones a disponibilizar para distribuir &quot;, seleccionado el valor&#160; &quot; Distribución parcial &quot; en el selector de &quot; tipo de distribución &quot;, en la subtabla &quot; Detalle de donaciones &quot;, seleccionó &quot; todos los items &quot; y no varió el dato por defecto del input numérico &quot; Unidades a distribuir &quot;&#58;&#160; este es un caso de un flujo de trabajo realizado por un usuario de manera inconclusa (marcó una distribución parcial , pero al operar la subtabla de detalles de la donación, lo hizo como si fuera una distribución total. 
&#160; 
 En ambos casos, por cada donación (encabezado) marcada, el sistema recopilará estos datos&#58; 
 cua_master = &#123;&#123; _DOM. cua_master &#125;&#125; ***Cuenta maestra a la cual pertenece&#160; el gestor de donaciones que está autenticado en BO de beneficiarios*** 
 eatc_user= &#123;&#123; usuario &#125;&#125; ***Nombre de usuario que está autenticado en la plataforma (generalmente una dirección de correo electrónico)*** 
 eatc_dona_header_code = &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; ***De la donación marcada en la columna &quot; Seleccionar &quot; de la tabla&quot; Donaciones a disponibilizar para distribuir &quot;*** 
&#160; 
 Por cada una de las donaciones marcadas, se realiza la invocación del API Pública para la creación de registro de Kardex . 

&#160; 
 Invocación del servicio sin enviar eatc_odd_quantity 
 Dado que para la invocación del API pública, los datos eatc_odd_id y eatc_odd_quantity son opcionales, se puede dar este caso, principalmente en que el usuario no envíe el dato eatc_odd_quantity&#58; 
&#160; 
 El usuario, habiendo en algunos casos, en la tabla &quot; Donaciones a disponibilizar para distribuir &quot;, seleccionado el valor&#160; &quot; Distribución parcial &quot; en el selector de &quot; tipo de distribución &quot;, en la subtabla &quot; Detalle de donaciones &quot;, seleccionó &quot; algunos de los items &quot; y no varió el dato por defecto del input numérico &quot; Unidades a distribuir &quot; (dejando el valor por defecto, correspondiente a todas las cantidades disponibles) 
&#160; 
 En este caso, por cada dupla&#58; donación (encabezado) - item (detelle) seleccionada, el sistema recopilará estos datos&#58; 
 cua_master = &#123;&#123; _DOM. cua_master &#125;&#125; ***Cuenta maestra a la cual pertenece&#160; el gestor de donaciones que está autenticado en BO de beneficiarios*** 
 eatc_user= &#123;&#123; usuario &#125;&#125; ***Nombre de usuario que está autenticado en la plataforma (generalmente una dirección de correo electrónico)*** 
 eatc_dona_header_code = &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; ***De la donación marcada en la columna &quot; Seleccionar &quot; de la tabla&quot; Donaciones a disponibilizar para distribuir &quot;*** 
 eatc_odd_id = &#123;&#123; eatc_dona .eatc-odd_id &#125;&#125; **De la donación marcada en la columna &quot; Seleccionar &quot; de la sub-tabla&quot; Detalle de donaciones &quot;*** 
&#160; 
 Por cada una de las duplas&#58; encabezado - item marcadas, se realiza la invocación del API Pública para la creación de registro de Kardex . 

&#160; 
 Invocación del servicio enviando todos los parámetros 
 En este caso el usuario seleccionó una&#160; (o varias) &quot; Distribución parcial &quot; en el selector de &quot; tipo de distribución &quot;, en la subtabla &quot; Detalle de donaciones &quot;, seleccionó &quot; algunos de los items &quot; y varió el dato por defecto del input numérico &quot; Unidades a distribuir &quot;. 
 En este caso, por cada dupla&#58; donación (encabezado) - item (detelle) seleccionada (y en la cual hayan sido variadas las cantidades a distribuir), el sistema recopilará estos datos&#58; 
&#160; 
 cua_master = &#123;&#123; _DOM. cua_master &#125;&#125; ***Cuenta maestra a la cual pertenece&#160; el gestor de donaciones que está autenticado en BO de beneficiarios*** 
 eatc_user= &#123;&#123; usuario &#125;&#125; ***Nombre de usuario que está autenticado en la plataforma (generalmente una dirección de correo electrónico)*** 
 eatc_dona_header_code = &#123;&#123; eatc_dona_headers . eatc-code &#125;&#125; ***De la donación marcada en la columna &quot; Seleccionar &quot; de la tabla&quot; Donaciones a disponibilizar para distribuir &quot;*** 
 eatc_odd_id = &#123;&#123; eatc_dona .eatc-odd_id &#125;&#125; ***De la donación marcada en la columna &quot; Seleccionar &quot; de la sub-tabla&quot; Detalle de donaciones &quot;*** 
 eatc_odd_quantity = &#123;&#123; input_numerico &#125;&#125; ***De la donación marcada en la columna &quot; Unidades a distribuir &quot; de la sub-tabla &quot; Detalle de donaciones &quot;*** 
&#160; 
 Por cada una de las duplas&#58; encabezado - item marcadas, se realiza la invocación del API Pública para la creación de registro de Kardex . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 BO Beneficiarios 

 SELECCIONA DONACIONES PARA DISTRIBUIR