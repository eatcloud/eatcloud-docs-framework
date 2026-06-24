# consulta-de-certificados-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 C ONSULTA DE CERTIFICADOS DE DONACIN 
 ID funcionalidad: consulta_certificados_donacion (falta crearse) 

 Label botn de men izquierdo : class=" lbl_menu_consulta_certificados " 

 Label ttulo de la funcionalidad: class=" lbl_consulta_certificados " 

 Label descripcin de la funcionalidad: class=" lbl_consulta_certificados_desc " 

 Listado de de certificados pendientes de aprobacin 
 A este listado, que contendr una lista de los certificados que responden a esta consulta: 
 {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_dona_certifications ?eatc_cua ={{ _DOM .cua_user}} 

 La lista deber contener dos filtros 

 Filtro por fecha (label:  class="lbl_filtro_fecha) 
 Aplica sobre los valores contenidos en eatc_dona_certifications . eatc_datetime . Debe tener un selector de fecha inicial y fecha final, cuyos valores por defecto deben ser: 

 Fecha inicial (label: id=" lbl_fecha_inicial " ) : tres meses antes de la fecha actual 
 Fecha final (label: id=" lbl_fecha_final " ) : fecha actual 

 Filtro por estado de aprobacin (label:  class="lbl_filtro_aprobacion) 
 Aplica sobre los valores contenidos en eatc_dona_certifications . eatc_certification_datetime . Los selectores para el filtro sern : 

 Pendientes de aprobacin (label: class=" lbl_pendientes_aprobacion " ) : al presionarlo, traer los certificados que no contengan una fecha vlida en  eatc_dona_certifications . eatc_certification_datetime (para el periodo de tiempo seleccionado en el filtro por fecha) 
 Aprobados (label: class=" lbl_aprobados " ) : al presionarlo, traer los certificados que tienen una fecha vlida en  eatc_dona_certifications . eatc_certification_datetime (para el periodo de tiempo seleccionado en el fltro por fecha) 
 Todos (label: class=" lbl_todos " ) : Ser el valor por defecto y trae todos los certificados, mostrando primero los pendientes de aprobacin con fecha ms antigua. 

 A partir de la seleccin que el usuario haga en los filtros, se deber mostrar un listado de certificados que contiene las siguientes columnas: 

 Cdigo:  
 Label : class=" lbl_codigo " ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_code 

 Fecha y hora:  
 Label : class=" lbl_fecha_hora " ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_datetime   

 Identificacin tributaria donante:  
 Label : class=" lbl_id_donante " 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_donor_code 

 Razn Social:  
 Label : class=" lbl_razon_social " ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_donor_fiscal_name 

 Valor total:  
 Label : class=" lbl_valor_total " ) 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_value 

 Documento(s) soporte: 
 Label : class=" lbl_docs_soporte " 
 Con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certifications_supports ?eatc_certification_code={{eatc_dona_certifications . eatc_code }} se deben obtener los cdigos de los soportes ( eatc_certifications_supports .eatc_certification_support_code ), y con ellos se realiza una lista de soportes (con sus cdigos) y con la siguiente consulta: {{URL_entorno_donantes}}/api/{{_DOM. cua_master }}/ eatc_certification_supports_headers ? eatc_certification_support_code ={{eatc_certifications_supports .eatc_certification_support_code }} , para traer la informacin que permite descargar el soporte ( eatc_certification_support_code.eatc_support_file ) se deben activar vnculos en cada uno de esos cdigos para descargar el respectivo soporte. 

 Descargar archivo 
 Label : class=" lbl_descargar_archivo " 
 Como no existe un registro vlido en eatc_dona_certifications . eatc_certification_datetime se debe presentar el botn " Descargar borrador " ( class=" lbl_descargar_borrador " ) (en el listado de consultar certificados podr existir uno con una fecha vlida en eatc_dona_certifications . eatc_certification_datetime s e deber presentar entonces el boton "Descargar soporte" ( class=" lbl_descargar_certificado " ) El botn servir para descargar el borrador del certificado a partir de la informacin consignada en: eatc_dona_certifications . eatc_certificate_file 

 Fecha y hora de aprobacin: 
 Label : class=" lbl_fecha_hora_aprobacion " ). 
 Muestra la informacin contenida en eatc_dona_certifications . eatc_certification_datetime . Cuando no existe una fecha y hora vlida registrada, en vez de mostrarla, se deber mostrar lo siguiente: 
 Uno o varios tags con vnculo mostrando las aprobaciones: indicando que el certificado ha sido aprobado por una o diferentes reas del ente certificador; 

 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Si la consulta no trae informacin deber mostrar el tag con la etiqueta class=" lbl_pendiente_aprobaciones " 

 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente: 

 Con los datos obtenidos en el parmetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parmetro eatc_certification_approval_flow. eatc_approval_by_label . Cada etiqueta debe tener un vnculo que muestre la siguiente informacin del registro de aprobacin ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} )  
 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la informacin contenida en el parmetro eatc_certification_approval_registry. eatc_approval_datetime 

 Usuario ( class=" lbl_usuario_solo " ): que muestra la informacin contenida en el parmetro eatc_certification_approval_registry. eatc_bo_user 

 Un botn para la accin " Aprobar ", segn las indicaciones que se entregan en la siguiente funcionalidad. o en su defecto un mensaje "Pendiente de aprobacin" ( class=" lbl_pendiente_aprobacion " ) 

 Uno o varios tags con vnculo mostrando las desaprobaciones: indicando que el certificado ha sido desaprobado por una o varias reas del ente certificador; 

 Para ello el sistema debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} 

 Si la consulta no trae informacin no mostrar nada 

 Si la consulta trae resultados, con dichos resultados se debe realizar lo siguiente: 

 Con los datos obtenidos en el parmetro eatc_certification_approval_registry . eatc_approval_code se debe realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_approval_code={{eatc_certification_approval_registry . eatc_approval_code }} 

 La etiqueta se construye con los datos obtenidos del parmetro eatc_certification_approval_flow. eatc_disapproval_by_label . Cada etiqueta debe tener un vnculo que muestre la siguiente informacin del registro de desaprobacin ( https://datagov.eatcloud.info/api/eatcloud/eatc_certification_disapproval_registry? eatc_certification_code ={{eatc_dona_certifications . eatc_code }} )  

 Fecha y hora ( class=" lbl_fecha_hora " ): que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_approval_datetime 
 Usuario ( class=" lbl_usuario_solo " ): que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_bo_user 

 Explicacin: ( class=" lbl_explicacion " ): que muestra la informacin contenida en el parmetro eatc_certification_disapproval_registry. eatc_disapproval_note 

 Un botn para la accin " Aprobar ", segn las indicaciones que se entregan en la siguiente funcionalidad. o en su defecto un mensaje "Pendiente de aprobacin" ( class=" lbl_pendiente_aprobacion " ) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CONSULTA DE CERTIFICADOS DE DONACIN