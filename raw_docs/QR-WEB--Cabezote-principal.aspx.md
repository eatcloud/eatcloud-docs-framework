# QR-WEB--Cabezote-principal.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Persistencia&#58; 
 Se deberá crear una persistencia a la cuál se pueda acceder mediante una consulta API, y que albergue la siguiente información&#58; 
&#160; 

 cua_master &#58; corresponde a la información de las cuentas maestras albergadas en el respectivo maestro de EatCloud. Será un campo obligatorio y parte de la clave compuesta del repositorio 

 cua_user &#58; corresponde a la información de las cuentas usuario albergadas en el respectivo maestro de EatCloud. Será un campo obligatorio y parte de la clave compuesta del repositorio 

 pod_typology_a &#58; tiplogía a de pods, y corresponderá a los datos albergados en el respectivo maestro. &#160;Será un campo “opcional” y hará parte de la clave compuesta del repositorio. &#160;Aunque no está en el diseño, la pod_typology_a , se deberá mostrar (su nombre, no su código) para que sea visible en el cabezote. 

 title &#58; Título del cabezote; para el ejemplo en el diseño de muestra corresponde a “ Dunkin Donuts ”. &#160;Será un campo obligatorio. 

 subtitle &#58; Subtítulo del cabezote; para el ejemplo en el diseño de muestra corresponde a “ Alimentando Esperanzas ”. &#160;Será un campo obligatorio. 

 call_to_action &#58; llamado a la acción del cabezote; para el ejemplo en el diseño de muestra corresponde a “ Descubre el impacto positivo de nuestras donaciones de alimentos en comunidades necesitadas ”. &#160;Será un campo obligatorio. 

 call_to_action_button &#58; etiqueta del botón de llamado a la acción; para el ejemplo en el diseño de muestra corresponde a “ Conoce nuestro impacto ”. &#160;Será un campo obligatorio. 

 header_image &#58; contendrá el recurso de la imagen que es el fondo del cabezote; para el ejemplo del diseño corresponde a la imagen del miembro del equipo de DD sonriente. Será un campo obligatorio. 

 creation_datetime &#58; fecha y hora de creación del registro&#58; campo obligatorio automático. 

 creation_user &#58; usuario que crea el registro (a futuro esta creación se deberá enlazar con los BO de donantes y de EatCloud, para “dar de alta” a quienes desean utilizar la funcionaldiad 

 modification_datetime &#58; fecha y hora de modificación del registro (para efectos de habilitación y deshabilitación). 

 modification_user &#58; usuario que modifica el registro 

 modification_notes &#58; para guardar notas de auditoría sobre la modificación del registro 

 active (true, false)&#58; estado del registro, en TRUE, es registro es activo, es decir generará el QR_WEB. Si está en FALSE el WEB_QR quedará inactivo&#160; 
&#160; 
Con los parámetros que se reciban por la URL , el sistema deberá proceder a realizar la consulta a esta persistencia, para traer la información que permita construir el cabezote de manera dinámica. 
&#160; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=b55eb27c82f2412e9adc99952ea6f222&ext=png&ow=6784&oh=2345, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=b55eb27c82f2412e9adc99952ea6f222&ext=png&ow=6784&oh=2345 

 1034.00000000000 
 27570daf-91af-49a9-bed0-b2ff8de3d5e5 
 1!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 006bfa67-a36a-40c8-8920-e491f2f68963 
 2025-08-01T23:08:56.4598394Z 

 {"SessionId":"fc316cf9-b17f-4408-b539-db19278224c9","SequenceId":1749,"FluidContainerCustomId":"0670262e-9f07-4a86-aff4-a1c9dda82b9f","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"},{"Name":"ZonePlaceholderData","Version":"Off"}] 

 QR WEB: Cabezote principal