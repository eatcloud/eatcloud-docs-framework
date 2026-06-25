# Onboarding-beneficiarios--nuevo-campo--capacidad-mínima-de-gestión(1).aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
Ante la solicitud de la creación de un campo adicional solicitado por ABACO para el Onboarding de organizaciones sociales, en vez de generar una mejora particular (Creación del campo casilla 53 del RUT), se va a establecer una funcionalidad más general, que a futuro permita crear campos “custom” por cua_master, para incorporarlos (inicialmente) en el formulario de ONB de Beneficiarios. &#160;Con posterioridad, y de acuerdo a solicitud de mejoras, se deberá pensar inclusive en una implementación más general, que permita incorporar nuevos campos de captura en diversos formularios por cuenta maestra, a lo largo de la plataforma (como por ejemplo el caso de ONB de cua_user, ONB de PODs, y Creación de donaciones), pero eso será objeto de mejoras futuras. 
Descripción general 
En el BO Beneficiarios, perfil “Líder de Ecosistema”, se deberá habilitar un formulario para la creación de “Campos personalizados” para el ONBOARDING de Beneficiarios. 
&#160; 
Dicho formulario deberá permitir la creación de campos “custom” que solamente se le desplegarán a dicha cuenta maestra en el proceso de ONB de de Beneficiarios y dicha configuración deberá contener información como la siguiente (se propone información básica para caracterizar el campo de captura, que el desarrollador podrá modificar para acercarse a estándares de programación que faciliten la implementación, por lo tanto la siguiente descripción es meramente indicativa, y podrá variarse según la conveniencia dictada por el desarrollador)&#58; 
Agregar un nuevo campo al formulario de Onboarding de organizaciones sociales (antes de los datos de capacidades máximas de gestión y recogida), en donde se solicite la “ Capacidad mínima de gestión en KG ” ( tooltip &#58; por debajo de este peso para un anuncio, no estás dispuesto a ir a recogerlo ). &#160;El dato deberá tener la siguientes características 
&#160; 

 Nombre del campo de captura&#58;&#160; Etiqueta que se desplegará en el formulario de ONB de beneficiarios =&gt; Obligatorio 

 Descripción o texto de ayuda&#58; que se deberá desplegar en el respectivo tooltip =&gt; Obligatorio 

 Tipo de dato a capturar&#58; deberá desplegar opciones como “Alfanumérico o string”, “numérico entero o integer”, “numérico decimal o float” =&gt; Obligatorio, valor por defecto&#58; sting =&gt; NOTA&#58; lo que se lleve a la persistencia debe ser un dato técnico que permita el fácil despliegue de tipo de dato en la base de datos en donde se persistirá lo que se registre en el campo custom del formulario, pero al usuario se le deben presentar términos no tan técnicos, que le permitan identificar el campo de captura que está caracterizando. 

 Tipo de campo de captura&#58; se le deben presentar opciones básicas al usuario como por ejemplo&#58; texto corto, texto largo, numérico, selección única, selección múltiple (y los demás que considere relevante el desarrollador) &#160;=&gt; Obligatorio 

Si determinó campos tipo selector, el sistema le deberá permitir establecer las posibles opciones de selección &#160; =&gt; Obligatorio si el campo de captura es de tipo selector. 

 Valor por defecto&#58; el usuario podrá establecer un valor por defecto (si el campo es de tipo selector podrá ser una de las opciones anteriormente establecidas) =&gt; No obligatorio&#58; si se deja vacío el sistema deberá entender que no existe valor por defecto 

 Obligatoriedad&#58; SI / NO&#58; el usuario deberá establecer si el registro en el campo es obligatorio o no 

Mensaje ante el no registro obligatorio&#58; si el campo se define como obligatorio, se deberá permitir la captura de un mensaje que aparezca ante la no validación del campo. 

 Otras validaciones&#58; &#160;Aunque no es necesario en una primera etapa, se podrán establecer otras validaciones, como despliegue condicionado del campo, valores mínimos y máximos para campos numéricos y otras a consideración del desarrollador. 

 Visualización de datos en informes&#58; &#160;El sistema deberá establecer un selector múltiple, que permita establecer en donde se podrán visualizar los datos capturados mediante este campo custom. &#160;Para el caso particular, serán (se aporta la respectiva documentación de estas vistas, con el ánimo de entender, cuando se implemente el BO Beneficiario modernizado, en dónde se visualizarán los datos capturados por campos “custom”)&#58; 

Activaciones&#58; Listado de beneficiarios inscritos&#58; &#160; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/activaci%C3%B3n-beneficiarios.aspx#listado-de-gestores-de-donaciones &#160; 

Activaciones&#58; Listado de beneficiarios inscritos&#58; &#160;Descarga&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/activaci%C3%B3n-beneficiarios.aspx#bot%C3%B3n-descargar &#160; 

Activaciones&#58; información particular del beneficiario&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/activaci%C3%B3n-beneficiarios.aspx#detalles-del-gestor-de-donaciones &#160; 

Listado de beneficiarios finales&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/listado-beneficiarios.aspx &#160; 

Descarga en archivo plano de beneficiarios inscritos&#58; https&#58;//eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/listado-beneficiarios.aspx#bot%C3%B3n-descargar &#160; 
&#160; 
 Nota &#58; el desarrollador a su juicio podrá simplificar a un solo campo de configuración la visualización de la información y su respectiva descarga, si así lo estima conveniente. 
&#160; 
Despliegue del campo configurado en el formulario de ONBOARDING de beneficiarios 
Con la información recolectada, el formulario de ONB de Beneficiarios, deberá desplegar, al final de sus campos de captura actuales, el nuevo campo de captura, por cuenta maestra (estos campos están restringidos por cuenta maestra, así que no se deben mostrar en cuentas maestras que no los han solicitado / configurado). 
&#160; 
Despliegue de los datos capturados en los informes indicados por el usuario&#160; 
Con la información recolectada, el sistema desplegará los datos que se capturan por los campos custom, en los lugares establecidos en su configuración. 

 [] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 b5515f1f-5cba-448a-b7bd-3c54ca601b94 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 8ce99431-915d-4298-b618-1509654b6588 
 2025-04-28T23:47:28.6779762Z 

 {"SessionId":"26ff105f-b074-40a9-bf4d-2eb9b13dae4c","SequenceId":12252,"FluidContainerCustomId":"90e41273-0538-401c-87e0-2ee6947151d6","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"}] 

 Onboarding beneficiarios: posibilidad de crear campos "customizados" por cua_master