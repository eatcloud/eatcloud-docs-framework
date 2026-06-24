# BO-Donantes-Modernizado--Mensaje-donantes-en-mora.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 BO Donantes Modernizado: Mensaje donantes en mora ","showTimeToRead":false},"containsDynamicDataSource":false}">

Resumen: 
 Se ha creado una automatización, que apunta a una estructura de datos del API legacy, en donde se muestra si una cuenta posee pagos en mora, con tres niveles de criticidad: verde, amarillo y rojo (siendo esta última la más alta).  Por lo tanto, leyendo esa estructura de datos, el sistema debe identificar si la cua_user que está ingresada en el BO, posee este tipo de condición y a partir de la misma, colocar un mensaje visible en el encabezado de la página, en donde se alerte de ello al usuario.  El diseño de dicho mensaje se encuentra en el siguiente figma: https://www.figma.com/design/fz65QCafGLQOjca5ShRzTc/Nubola-Design-System?node-id=2513-477&p=f&t=1jRQP9b7uL0Z64uX-0   

 Consulta para determinar el tipo de mensaje a desplegar 
Con el código de la cua_user ( code_cua_user ) del usuario que se encuentra loggeado en la plataforma, el sistema debe realizar la siguiente consulta: 
{{URL_datagov}}api/eatcloud/ customer_warning_cua ?cua={{ code_cua_user }}&estado=vigente&_cmp=categoria 

Si la consulta no arroja resultados, entonces no se muestra ningún mensaje. 

Si la consulta arroja como resultado: categoria= bajo 
Entonces el sistema despliega el mensaje cuyo fondo está en verde 

Para determinar el mensaje que se despliega, se debe realizar esta consulta (no se coloca el vínculo “ver estado” solamente el mensaje como se obtiene de la siguiente consulta: 
{{URL_datagov}}api/eatcloud/ customer_warning_messages? categoria= bajo & _cmp= mensaje 

Que para este efecto es: 
 Su empresa se encuentra atrazada en el pago de sus productos y licencia.  Por favor ponganse al día 

Si la consulta arroja como resultado: categoria= medio 
Entonces el sistema despliega el mensaje cuyo fondo está en naranja 

Para determinar el mensaje que se despliega, se debe realizar esta consulta (no se coloca el vínculo “ver estado” solamente el mensaje como se obtiene de la siguiente consulta: 
{{URL_datagov}}api/eatcloud/ customer_warning_messages? categoria= medio & _cmp= mensaje 
Que para este efecto es: 
     Su empresa se encuentra atrazada en varios pagos de sus productos y licencias. Evite el corte de sus servicios. Ponganse al dia y comuníquese con cobranzas EatCloud al 3043140103    

Si la consulta arroja como resultado: categoria= critico 
Entonces el sistema despliega el mensaje cuyo fondo está en rojo 

Para determinar el mensaje que se despliega, se debe realizar esta consulta (no se coloca el vínculo “ver estado” solamente el mensaje como se obtiene de la siguiente consulta: 
{{URL_datagov}}api/eatcloud/ customer_warning_messages? categoria= critico & _cmp= mensaje 
Que para este efecto es: 
     No hemos recibido pagos de sus productos y licencias. Evite el corte de sus servicios. Ponganse al día y comuníquese de manera inmediata a el área de cobranzas EatCloud al 3043140103"    

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Donantes-Modernizado--Mensaje-donantes-en-mora%2F1769704024612image.png&ow=778&oh=746, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FBO-Donantes-Modernizado--Mensaje-donantes-en-mora%2F1769704024612image.png&ow=778&oh=746 

 076efeda-c948-4f6d-8b1a-0d4e956813b2 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 03fb6e04-bcc7-48d0-9b8a-024911b3c018 
 2026-01-30T00:21:28.4705949Z 

 {"SessionId":"7ba5ebcb-e278-4bec-9779-10bf18874416","SequenceId":3899,"FluidContainerCustomId":"36cda58c-2956-4a7a-a6dc-261b608055bb","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1185.00000000000 

 BO Donantes Modernizado: Mensaje donantes en mora