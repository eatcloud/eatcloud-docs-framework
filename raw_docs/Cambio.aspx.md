# Cambio.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
 Se documentan los diferentes estados de las donaciones, con el ánimo de que a partir de esta información general, se establezcan los puntos en la APP y en la WAPP en dónde deben llevarse a persistencia, sobretodo estados secundarios. 
 Estados base ( https://datagov.eatcloud.info/api/eatcloud/eatc_dona_headers_states?_id=_* ) 

Anunciada = Announced 

Adjudicada = Awarded 

Programada = Scheduled 

Entregada = Delivered 

Recibida = Received 

Pre-certificada= pre-certified 

 Certificada = certified 

 No entregada= not_delivered 

 Cancelada = cancelled 

 Subestados 
Estos subestados deberán llevarse a eatc_state3 para poder ser consultadas las donaciones a partir de los mismos: 

Por entregar 
Cuando la donación está en estado “awarded” o “scheduled”. 
Se podría manejar desde el servicio “ awarddona ”, para su incorporación. 

Por validar 
Se configura cuándo NO hay fecha y hora de verificación, osea ["eatc_code_verification_datetime"] == "0000-00-00 00:00:00", pero que hay fecha y hora de recibido, o sea [" eatc-receipt_datetime "] != "0000-00-00 00:00:00"

Se podría manejar desde la funcionalidad de la APP: verificación detallada de donación por unidades (en sus diferentes casos), y verificación detallada por peso (en sus diferentes casos). 

Despachado 
Se registra ese estado cuando eatc-state sea “ delivered ”

No se encuentran casos funcionales en donde esto ocurra, dado que en la APP se marca despachado pero al hacerlo se genera un eatc-pickin_checkout_datetime y con o sin eatc_code_verification_datetime, lo que hace que caiga siempre en los dos casos posteriores.  Cuando se marca “delivered” desde la WAPP mediante el proceso de “verificación de código de recogida”, se cumple la condición para marcar como “Verificado”.  Se debe revisar si lo que se está proponiendo es un estado compuesto, como “despachado por verificar” y “despachado verificado”, en cuyo caso también se manejaría directamente en los casos posteriores. 

Por verificar 
Se registra ese estado cuando eatc-state sea “ delivered ”, y  existe hora de checkout, es decir ["eatc-picking_checkout_datetime"] != "0000-00-00 00:00:00" y que NO hay fecha y hora de verificación, es decir ["eatc_code_verification_datetime"] == "0000-00-00 00:00:00"

Se podría manejar desde la funcionalidad de la APP: entrega de donación: hora de salida (en sus diferentes casos). 

Verificado 
Se registra ese estado cuando eatc-state sea “ delivered ”, y  existe hora de checkout, osea ["eatc-picking_checkout_datetime"] != "0000-00-00 00:00:00" y que hay fecha y hora de verificación, es decir ["eatc_code_verification_datetime"] != "0000-00-00 00:00:00"

Se puede manejar desde la funcionalidad de la WAPP: verificación del código de recogida y también desde la funcionalidad de la APP: entrega de donación: hora de salida (en sus diferentes casos). 

Recibido 
Se registra ese estado cuando eatc-state sea “ received ”.

Se puede manejar desde la funcionalidad de la WAPP: verificación del código de recogida (en sus diferentes casos) y también desde la funcionalidad de la APP: verificación detallada de donación por unidades (en sus diferentes casos), y verificación detallada por peso (en sus diferentes casos). 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 4f0a3b25-e8cc-4b43-9116-02481894a396 
 1!1!3 
 https://eastus0-1.pushfp.svc.ms/fluid 
 ff449cc2-2406-476c-a899-ada373420e3d 
 2025-06-13T04:45:19.4466061Z 

 {"SessionId":"d0ca2c5e-71cd-4b5d-8787-dcb03bb70ef6","SequenceId":4633,"FluidContainerCustomId":"1537efc5-b10b-4e67-b332-0d2ac29246c4","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 

 Estados de las donaciones