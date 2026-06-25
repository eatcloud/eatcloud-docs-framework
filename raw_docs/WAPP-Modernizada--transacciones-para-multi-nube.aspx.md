# WAPP-Modernizada--transacciones-para-multi-nube.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 En la actualidad eatcloud maneja un solo tipo de transacción, el registro de “anuncios de donación”. &#160;Esta transacción general ha sido utilizada para crear detalles y encabezados de donaciones en lo que era una única cuenta maestra por territorio. 
&#160; 
 A partir de la fecha y con el ánimo de promover nuevas líneas de negocios para contribuir con nuestro propósito #CeroDesperdicio, se deberá implementar en la WAPP la captura de nuevas transacciones, que alimentarán nuevas nubes, bajo el concepto “multi-nube”. &#160; 
&#160; 
 Este registro por tanto se basará en la actual implementación de registro para “anuncios de donaciones”, implementando toda su funcionalidad, pero con dos componentes distintivos&#58; 
&#160; 

Se registrarán en nubes diferentes a las tradicionalmente utilizadas (p.e. abaco, mexico, ecuador…) 

Tendrán una terminología particular, para llamar, por ejemplo, las transacciones de manera diferente. 
&#160; 
Por lo tanto, las estructuras de datos, las estructuras de datos de configuración, (que por ejemplo dictan cuando una cuenta usuario tiene maestros que soporten sus capturas), deberán ser las mismas que las utilizadas en los “anuncios de donación”, pero existirán diferencias en cuanto a&#58; 

&#160;Los “labels” o “etiquetas” que acompañan a los campos de captura 

&#160;Las validaciones de obligatoriedad de algunos de los campos. 

&#160;La escritura en “nubes” diferentes a las utilizadas para las donaciones (pero dichas estructuras de encabezado y detalle conservarán su estructura. 

Algunas funcionalidades que operarán solo para esta captura, como es el caso de la posibilidad de “registrar” lo que en donaciones es “beneficiarios” y que en este nuevo esquema serán “gestores de residuos”. 
&#160; 
Es por eso que se han creado nuevas estructuras de configuración, que darán cuenta de los elementos característicos de estas nuevas “nubes” y de estas nuevas “transacciones” que en adelante se detallan. 
&#160; 
 Caracterización de la multi-nube&#58; 
En esta estructura de datos se caracterizan las diferentes entidades y actores del proceso de las diferentes nubes. &#160; Vale la pena que si bien hay muchas nubes en este momento para la “donación humanitaria de alimentos”, es decir, múltiples cuentas maestras que se comportan de manera similar, en esta estructura de datos solamente se registra la cuenta maestra original, que para el caso de los “anuncios de donación” es abaco, y también una cuenta original para el registro de excedentes, que será col_excedentes. 
&#160; 
A continuación se pueden consultar la caracterización de las multi-nubes&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/multi_cloud_characterization?original_cua_master=col_excedentes &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/multi_cloud_characterization?original_cua_master=abaco &#160; 
Vale la pena resaltar que en esta caracterización, se hace referencia a entidades abstractas que sirven para entender mejor el “ecosistema” que rodea a cada “transacción” y deben ser estudiadas a manera comparativa con lo implementado actualmente, para entender bien los conceptos de transfondo, en donde por ejemplo ya no hablaremos de “beneficiarios” o de “donantes”, sino de otros conceptos, dada la naturaleza de la nueva transacción. &#160;Si se requiere mayor información al respecto, se puede compartir una presentación que profundiza en cada uno de los conceptos que contiene la estructura de datos arriba compartida. 
 Cuentas y/o Puntos a los cuales se le despliega la funcionalidad (nueva transacción) 
Se deberá generar una estructura de datos, en donde se pueda consultar la siguiente información&#58; 
&#160; 

 cua_user &#58; cuenta usuario de la WAPP. &#160;Será un dato obligatorio y hará parte de la clave primaria de la estructura de datos 

 cua_master &#58; cuenta maestra secundaria. &#160;Si bien en cada registro de cua_user hay una cuenta maestra principal, en esta tabla se podrán registrar cuentas maestras secundarias, para indicar nuevas transacciones que se le desplieguen en la WAPP a las cua_user. &#160; Será información obligatoria y hará parte de la clave primaria. 
&#160; 
A futuro se podrá complementar con una estructura de datos, que incluya o excluya PODs particulares, de tal manera que se puedan habilitar las transacciones secundarias a un subconjunto de PODs de la respectiva cua_user (pero este tema puede dejarse para una segunda etapa de implementación). 
Cuando se defina la estructura de datos para realizar este registro, se deberá documentar aquí. 

 Diseño de la UI de la nueva transacción 
Existe el siguiente figma en donde se propone el diseño de la nueva transacción&#58; 
 https&#58;//www.figma.com/design/fz65QCafGLQOjca5ShRzTc/Nubola-Design-System?node-id=4775-10395&amp;t=KzJ0yP1on0ZrwYj7-4 &#160; 
Vale la pena resaltar varios aspectos de esta propuesta&#58; 

Las nuevas transacciones generarán dos tipos de transacciones&#58; captura manual y captura por archivo plano 

Las nuevas transacciones tendrán un color de fondo característico que las ayudará a diferenciar del registro de “anuncios de donaciones” 

El diseño presentado en el figma, tiene algunos inconvenientes, como por ejemplo&#58; hay capturas que son a nivel de encabezado, que se están proponiendo en su versión inicial como capturas de detalle. &#160;En esta documentación se aclararán todos estos aspectos para tener claridad en la implementación. 

Caracterización de la transacción. 
Tomando como base la actual implementación de registro de anuncio de donación y el diseño propuesto, se hace una documentación en JSON que permite establecer aquellos puntos en donde se diferencian las dos transacciones. &#160; Se utilizará esta documentación para definir las diferencias fundamentales entre las dos transacciones, y se recomienda que esta estructura, o una similar, sirva de herramienta de configuración para futuras transacciones, de tal manera que al incorporar datos a esta estructura, se puedan dar de alta nuevas transacciones con las características deseadas 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes &#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=abaco &#160; 

Menú lateral&#58; registrar excedentes 
Para acceder a la funcionalidad existirá un nuevo vínculo de menú. &#160;En la “caracterización de la transacción” se puede consultar el nombramiento de este menú en&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= menu_button&#160; &#160; 
Se puede entender que “Registrar excedentes con archivo plano” es un segundo elemento que se puede construir con esta información de configuración (y el sufijo&#58; “con archivo plano”) 

Encabezado de la transacción 

Título&#58; Registra tus excedentes 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=title 

Subtítulo&#58; No aptos para el consumo humano ***No está en el diseño*** 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= subtitle &#160; 
Es importante que este subtítulo sea vistoso porque contiene una información importante que sirve para diferenciar un registro de donación (que contiene productos aptos para el consumo humano) y un registro de excedentes (que no los contiene) 

Llamado a la acción **Diferencia con la implementación de anuncios de donación** 
Este punto del diseño, no se encuentra presente en la implementación inicial de registro de anuncios de donación. &#160;Constará entonces de un título, una descripción y dos botones que se detallan a continuación 
Título llamado a la acción&#58; Crea un registro de excedentes mediante archivo plano 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= call_to_action&#160; 
Descripción de llamado a la acción&#58; S ubiendo un archivo en formato…&#160; 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= call_to_action_desc &#160; 
Botones de llamado a la acción&#58; Registra tus excedentes con archivo plano 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= call_to_action_button 
Se deberá implementar una funcionalidad de subida de los excedentes por archivo plano, homóloga con la actualmente implementada en la WAPP pero con las consideraciones de escritura en una cua_master diferente, y denominación de “labels” que se detallan en esta documentación. &#160;Puede ser considerada para una segunda etapa de implementación. 

Primeras capturas de datos de encabezado de la nueva transacción 
Al inicio de la transacción se podrán capturar los datos que corresponden a datos de encabezado y que se definen a continuación. 
&#160; 
1. Información sobre el donante ***No está en el diseño*** 
Este componente de la creación de la nueva transacción, que será homólogo con lo que originalmente se denominó “ multiples_nit ”, deberá estar también presente en esta nueva transacción, operando sobre él los mismos parámetros de configuración y el mismo maestro de “diferentes compañías”, pero los labels serán diferentes. &#160;Partiendo del actual diseño, se detallarán estos nuevos “labels”&#58; 

Título&#58; Información de la empresa (en la implementación anterior de donaciones (imagen arriba)&#58; “Información sobre donantes”) 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=company_info 
Primer campo de captura&#58; Nombre de la empresa (en la implementación anterior de donaciones (imagen arriba)&#58; “Nombre del donante”) 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=company_name &#160; 
Segundo campo&#58; Doc ID de la empresa (en la implementación anterior de donaciones (imagen arriba)&#58; “Doc ID donante”) 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=company_id&#160; 

2. Quién recibe (mal ubicada en el figma, dado que allí podría entenderse como una captura a nivel de detalle) 

Aunque en el Figma esta captura pareciera a ser una a nivel de detalle, debe ser en la práctica una captura más parecida a la funcionalidad actualmente implementada de&#58;&#160; 

Esta funcionalidad estárá definida por dos parámetros de configuración&#58; 
Label o etiqueta&#58; Quién recibe 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=doma_selector &#160; 
&#160; 
Creación de receptores (DOMA)&#58; Nueva funcionalidad 
Según el siguiente parámetro de la caracterización de la transacción, para este caso se obtiene un valor de “TRUE”, lo que quiere decir que no solamente se podrán seleccionar los receptores, sinó que también se pueden crear. &#160;Se debe entender estos receptores (DOMA&#58; Dinamic Operators of Material Alocation) una entidad homóloga a los “Beneficiarios” de la transacción de Anuncios de donaciones. &#160;Por este motivo sus estructuras de maestros, deben corresponder a las mismas que se manejan en el caso de la transacción donación (eatc_donation_managers por ejemplo) y en su registro en la transacción como tal (eatc_dona_headers) deben ocupar también los mismos campos que ocupan los “beneficiarios” en las donaciones. 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=doma_creator &#160; 
Por lo tanto se podrán, no solo seleccionar “receptores”, sino también dar de alta y por lo tanto el desarrollador debe establecer los mecanismos para escribir tanto en el maestro como en los detalles y encabezados de la transacción, pero en la nube respectiva (la cua_master de la nueva transacción). 

3. Categoría del excedente (doma_typology_a) (mal ubicada en el figma, dado que allí podría entenderse como una captura a nivel de detalle) 

Por definición se establece que para esta transacción en particular, su “categoría” o como se lee en el diseño “categoría del excedente” será la tipología a de la donación , tal como se lee en la caracterización de la transacción 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=dona_typology_a &#160; 
Dada dicha definición sus estructuras de maestros, estarán definidas por cua_master (con esta consulta se arma el selector) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_typology_a?eatc_cua_master=col_excedentes &#160; 
&#160;y se debe llevar a nivel de la transacción al mismo campo en donde se registra dicha tipología (eatc_dona_headers. eatc_dona_typology_a). &#160; En este punto se debe procurar llevar el eatc_cause_label al registro, en vez del nombre (para que funcione mejor como un código) y explorar la posibilidad de incorporar un nuevo campo en el encabezado que de cuenta del nombre de la tipología a de la donación (algo como eatc_dona_headers. eatc_dona_typology_a_name) 

4. Tipo de disposición (doma_typology_b) (mal ubicada en el figma, dado que allí podría entenderse como una captura a nivel de detalle) 

De manera muy similar a la anterior definición de captura, &#160;se establece que para esta transacción en particular, su “ tipo de disposición ” será l a tipología b de la donación , tal como se lee en la caracterización de la transacción 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=dona_typology_b &#160; 
Dada dicha definición sus estructuras de maestros, estarán definidas por cua_master (con esta consulta se arma el selector) 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_dona_typology_b?eatc_cua_master=col_excedentes &#160; 
y se debe llevar a nivel de la transacción a un campo nuevo que deberá crearse en la estructura de encabezados de la cua_master col_excedentes (eatc_dona_headers. eatc_dona_typology_b) =&gt; Se debe reflexionar si se debe llevar ese mismo campo a todas las demás estructuras de encabezados en las diversas cuentas maestras. &#160; En este punto se debe procurar llevar el eatc_cause_label al registro, en vez del nombre (para que funcione mejor como un código) y explorar la posibilidad de incorporar un nuevo campo en el encabezado que de cuenta del nombre de la tipología a de la donación (algo como eatc_dona_headers. eatc_dona_typology_b_name) 

&#160; 
&#160; 
Captura de información de detalle de la nueva transacción 
&#160; 
Este componente de la creación de los detalles de la nueva transacción, será homólogo a la captura original de donaciones, operando sobre ella los mismos parámetros de configuración (por ejemplo, aquellos que dictan por cua_user, cuál es el nivel de captura de información de los productos por ejemplo si el precio y el peso se sacan del maestro o se deben digitar) y el mismo maestro de productos , pero los labels serán diferentes. 
También tendrá una consideración importante&#58; en la caracterización de la transacción, se establece la obligatoriedad de estas capturas, habiendo una condicionada a la selección de una tipología de la donación. &#160;Estas definiciones de qué es obligatorio y qué no lo es, se pueden establecer mediante la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_quantity,odds_unit_weight,odds_unit_cost,odds_vat,odds_lot,odds_expiration_date &#160; 

Título&#58; Agrega productos al registro del excedente (en el diseño existe un título adicional “Información del excedente” que se considera que no debe ir) 
Esta definición se encuentra en el JSON de caracterización en este punto&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=add_odds_title&#160; 

Cómo se hace referencia a los odds en las diferentes etiquetas&#58; Productos 
 En todas las etiquetas que hagan referencia a los componentes individuales de la transacción, se deberá hacer referencia a productos, tal como se define en la caracterización de la transacción&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds&#160; 

 Selector del Producto 
 Debe funcionar de manera similar a como funciona la transacción de registro de anuncios de donaciones 

 Cantidad 
 Es una captura mandatoria 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_quantity &#160; 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

 Peso unitario 
 Es una captura mandatoria 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_unit_weight &#160; 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

 Costo unitario 
 Es una captura mandatoria, si al seleccionar la tipologia_a de la transacción se seleccionó la opción “venta” 
https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_unit_cost,odds_vat,odds_lot 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

 IVA 
 Es una captura opcional 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_vat &#160; 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

 Lote 
 Es una captura opcional 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=odds_lot &#160; 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

 Fecha de caducidad más próxima 
 Es una captura opcional 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp= odds_expiration_date &#160; 
 &#160;y debe funcionar tal cual lo hace en la captura de anuncios de donación. 

Otras capturas a nivel de detalle no operan 
En particular no se deberá capturar lo que en este momento se captura como&#58; 

Motivo de la donación 

Contiene alergenos 

Comida preparada (que puede ser homóloga a la captura de la tipología a, pero en este caso operará con un selector no con un checkbox) 

Otras capturas de información a nivel de encabezado 
Se deberán conservar las capturas de documentos soporte, observaciones y demás capturas a nivel de encabezado que enriquecen la información de la donación 

Resumen 
Se deberá conservar el estilo del resumen, pero cambiando las palabras “ anuncio ” &#160;y “ anuncio de donación ” por “ Registro de excedentes ”&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/transaction_characterization?original_cua_master=col_excedentes&amp;_cmp=transaction_name &#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FWAPP-Modernizada--transacciones-para-multi-nube%2F1754689754642image.png&ow=316&oh=219, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FWAPP-Modernizada--transacciones-para-multi-nube%2F1754689754642image.png&ow=316&oh=219 

 3762ee88-809e-4720-8326-387cf3ec71e3 
 1!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 ef82e97b-58a5-4174-b625-10c8d7178326 
 2025-08-12T23:28:54.0608201Z 

 {"SessionId":"07ecfb3c-c2e2-4d36-9366-328c3a9f26a1","SequenceId":12866,"FluidContainerCustomId":"7e4917ec-4c1e-4461-b857-42f30049a404","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1070.00000000000 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"On"}] 

 WAPP Modernizada: transacciones para multi-nube