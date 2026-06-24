# centro-de-ayuda-para-pedidos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Esta vista mostrar un listado de los pedidos ( eatc_sale_order_headers ) en curso (en primera prioridad: pedidos cuyo estado eatc_state , es paid_out ), empezando por el ms antiguo (es decir, aquel cuya eatc-datetime sea ms antigua y por lo tanto, el que tiene mayor prioridad de recogida), y tambin los pedidos ya entregados (cuyo estado eatc_state , es delivered,partially_refund,refund ), mostrando en este segundo caso primero los ms actuales. 

 Consulta para traer la informacin para el centro de ayuda 
 Con los datos del usuario de la App  ( eatc_user_code ) se realiza la siguiente consulta para traer los datos de sus pedidos: 
 {{URL_entorno_beneficiarios}}/api/eatcloud/eatc_sale_order_headers?eatc-user_code={{eatc_sale_users. eatc-code}} 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 App usuario final - Sale 

 CENTRO DE AYUDA PARA PEDIDOS