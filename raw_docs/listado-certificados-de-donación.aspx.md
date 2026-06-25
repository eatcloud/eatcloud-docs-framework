# listado-certificados-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Filtro de fechas (tal como se manejaron en Analytics) 
&#160; 
 Fecha inicial (valor por defecto&#58; primer da del mes) 
 id=&quot; lbl_fecha_inicial &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_fecha_inicial )&#160; 
&#160; 
 Fecha final (valor por defecto&#58; da actual) 
 id=&quot; lbl_fecha_final &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_fecha_final ) 

&#160; 
 Selector de cuentas 
 A partir de la anterior seleccin, se realiza la siguiente consulta para establecer los valores del selector 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_certifications ?eatc_certification_datetime[0]=&#123;&#123; fecha_inicial &#125;&#125; &amp; eatc_certification_datetime[1]=&#123;&#123; fecha_final &#125;&#125;&amp;_distinct= eatc_cua 
&#160; 
 Con los valores que se trae la anterior consulta se arma el siguiente selector mltiple 
&#160; 
 Selecciona la cuenta 
 clase=&quot; lbl_seleccionar_cuenta &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_seleccionar_cuenta )&#160; 
&#160; 
 Se debe presentar una opcin de &quot;Todas&quot; ( clase=&quot; lbl_todas &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_todas ) que al acionarlo seleccione todas las cuentas presentes en el selector 
&#160; 
 Consultar 
 clase=&quot; lbl_consultar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&amp;idlabel=lbl_consultar ) 
&#160; 
 A partir de las selecciones del usuario en el anterior selector, el sistema arma un array de cuentas (&#123;&#123;array_cua&#125;&#125;) que servir para realizar la consulta que arma el listado de certificados. 

&#160; 
 Listado de de certificados de donacin 
 A este listado, que contendr los botones de accin para descargar los certificados&#160; que responden a esta consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_certifications ?eatc_certification_datetime[0]=&#123;&#123; fecha_inicial &#125;&#125; &amp; eatc_certification_datetime[1]=&#123;&#123; fecha_final &#125;&#125;&amp; eatc_cua= &#123;&#123;array_cua&#125;&#125; 
 mostrando primero los ms antiguos, y luego los ms nuevos, en una tabla que contiene las siguientes columnas 
&#160; 
 Cdigo&#58;&#160; 
 Label &#58; class=&quot; lbl_codigo &quot; 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_code 
&#160; 
 Fecha y hora&#58;&#160; 
 Label &#58; class=&quot; lbl_fecha_hora &quot; ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_datetime &#160; 
&#160; 
 Identificacin tributaria donante&#58;&#160; 
 Label &#58; class=&quot; lbl_id_donante &quot; 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_donor_code 
&#160; 
 Razn Social&#58;&#160; 
 Label &#58; class=&quot; lbl_razon_social &quot; ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_donor_fiscal_name 
&#160; 
 Valor total&#58;&#160; 
 Label &#58; class=&quot; lbl_valor_total &quot; ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_value 
&#160; 
 Documento(s) soporte&#160; 
 Label (columna) &#58; class=&quot; lbl_documentos_soporte_tabla &quot; ) &#160; 
 Con la siguiente consulta&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_certifications_supports ?eatc_certification_code=&#123;&#123;eatc_dona_certifications . eatc_code &#125;&#125;&amp;_distinct= eatc_certification_support_code se deben obtener los cdigos de los soportes ( eatc_certifications_supports .eatc_certification_support_code ), y con ellos se realiza una lista de soportes (con sus cdigos) y con la siguiente consulta&#58; &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_certification_supports_headers ? eatc_certification_support_code =&#123;&#123;eatc_certifications_supports .eatc_certification_support_code &#125;&#125; , para traer la informacin que permite descargar el soporte ( eatc_certification_supports_headers .eatc_support_file ) se deben activar vnculos en cada uno de esos cdigos para descargar el respectivo soporte. 
&#160; 
 Nota importante&#58; para el soporte tipo carta_colombia, solo hay una carta soporte por certificado, en ese caso se puede colocar el label &quot; lbl_descargar_archivo &quot; para que funcione igual a como se implement en&#58; Listado de soportes ***NUEVO&#58; Selector de documentos firmados y no firmados***** &#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/d-generacin-de-certificado-de-donacin.aspx (Hablar con Ivn sobre esta implementacin). Cuando el mtodo de soporte es factura_electrnica_colombia pueden haber varios soportes.&#160; La idea es que en ese caso se vincule en diferentes botones que presenten el cdigo de la factura ( eatc_certification_supports_headers. eatc_certification_support_code ) la URL de descarga de la factura que provee la DIAN y que ser informada en el campo eatc_certification_supports_headers .eatc_support_file y ser implementado prximamente. 

&#160; 
 Ejemplo&#58; entorno de pruebas, _DOM.cua_master=abaco, eatc_certification_code= EC-000035-2021 
&#160; 
 El sistema realiza la siguiente consulta&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/ eatc_certifications_supports ?eatc_certification_code=EC-000035-2021&amp;_distinct= eatc_certification_support_code &#160; 
&#160; 
 Dado que el sistema entrega como respuesta&#58; 
&#160; 
 eatc_certification_support_code &#58; &quot;3d628f183c24f24ec65835630319aee0&quot; 
&#160; 
 Entonces se realiza la siguiente consulta&#58; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/ eatc_certification_supports_headers ? eatc_certification_support_code =3d628f183c24f24ec65835630319aee0 &#160; 
&#160; 
 Y para el mismo implementar la URL de descarga, tal como se implement en el Listado de documentos soporte del Nuevo BO Datagov Cuentas. 
&#160; 
 Descargar archivo 
 La idea de esta funcionalidad es la de permitir descargar el precertificado (cuando no se ha terminado el proceso de aprobacin del mismo) o el certificado (cuando ya se tienen todas las aprobaciones).&#160; Es por eso que segn ciertos registros en las estructuras de datos que se indican abajo, se estar 
&#160; 
 Label &#58; class=&quot; lbl_descargar_archivo &quot; ) &#160; 
 Como no&#160; existe un registro vlido en&#160; eatc_dona_certifications . eatc_certification_datetime se debe presentar el botn &quot; Descargar borrador &quot; ( class=&quot; lbl_descargar_borrador &quot; ) (en el listado de consultar certificados podr existir uno con una fecha vlida en eatc_dona_certifications . eatc_certification_datetime s e deber presentar entonces el boton &quot;Descargar soporte&quot; ( class=&quot; lbl_descargar_certificado &quot; ) El botn servir para descargar el borrador del certificado a partir de la informacin consignada en&#58; eatc_dona_certifications . eatc_certificate_file 

&#160; 
 Fecha y hora de aprobacin&#58; 
 Label &#58; class=&quot; lbl_fecha_hora_aprobacion &quot; ). 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_certification_datetime . Como no existe una fecha y hora vlida registrada, en vez de mostrarla, se deber mostrar dos cosas, segn sea el caso y el rol del usuario&#58; 

 Uno o varios label indicando que el certificado ha sido aprobado por una o diferentes reas de la empresa; 
&#160; 
 Para ello el sistema debe realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code =&#123;&#123;eatc_dona_certifications . eatc_code &#125;&#125; 
&#160; 
 Con los datos obtenidos en el parmetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code=&#123;&#123;eatc_certification_approval_registry . eatc_approval_code &#125;&#125; 
&#160; 
 La etiqueta se construye con los datos obtenidos del parmetro eatc_certification_approval_flow. eatc_approval_by_label . Cada etiqueta debe tener un vnculo que muestre la siguiente informacin del registro de aprobacin ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code =&#123;&#123;eatc_dona_certifications . eatc_code &#125;&#125; )&#160; 
&#160; 
 Fecha y hora ( class=&quot; lbl_fecha_hora &quot; )&#58; que muestra la informacin contenida en el parmetro eatc_certification_approval_registry. eatc_approval_datetime 

 Usuario ( class=&quot; lbl_usuario_solo &quot; )&#58; que muestra la informacin contenida en el parmetro eatc_certification_approval_registry. eatc_bo_user 
&#160; 

 Uno o varios tags con vnculo mostrando las desaprobaciones&#58; indicando que el certificado ha sido desaprobado por una o varias reas del ente certificador; 
&#160; 
 Para ello el sistema debe realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code =&#123;&#123;eatc_dona_certifications . eatc_code &#125;&#125; 
&#160; 
 Si la consulta no trae informacin no mostrar nada 
&#160; 
 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente&#58; 
&#160; 
 Con los datos obtenidos en el parmetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code=&#123;&#123;eatc_certification_approval_registry . eatc_approval_code &#125;&#125; 
&#160; 
 La etiqueta se construye con los datos obtenidos del parmetro eatc_certification_approval_flow. eatc_disapproval_by_label . Cada etiqueta debe tener un vnculo que muestre la siguiente informacin del registro de desaprobacin ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code =&#123;&#123;eatc_dona_certifications . eatc_code &#125;&#125; )&#160; 
&#160; 
 Fecha y hora ( class=&quot; lbl_fecha_hora &quot; )&#58; que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_approval_datetime 
 Usuario ( class=&quot; lbl_usuario_solo &quot; )&#58; que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_bo_user 

 Explicacin&#58; ( class=&quot; lbl_explicacion &quot; )&#58; que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_disapproval_note 
&#160; 
 Un botn para la accin &quot; Aprobar &quot;, segn las indicaciones que se entregan en&#160; la siguiente funcionalidad. o en su defecto un mensaje &quot;Pendiente de aprobacin&quot; ( class=&quot; lbl_pendiente_aprobacion &quot; ) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 LISTADO (CERTIFICADOS DE DONACIN)