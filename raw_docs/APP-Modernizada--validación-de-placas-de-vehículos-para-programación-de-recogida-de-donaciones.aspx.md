# APP-Modernizada--validación-de-placas-de-vehículos-para-programación-de-recogida-de-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen: 
Se deberá establecer una persistencia que permita validar las placas de diversos países de los vehículos que recogen las donaciones.  Además se deberá conectar el proceso con el servicio conrec , que ya está intregado en la APP legacy . 

Además se deberá procurar guardar una base de datos de conductores que estén validados correctamente en la APP (es decir que no estén catalogados en lista negra por el conrec), para facilitarle al usuario la elección de “recolectores válidos” y así hacerle el proceso más ágil. 

Persistencia de expresiones para validar placas 
Dado que es posible encontrar expresiones regulares para la validación de placas de vehículos, como estas: 
1. Colombia: 
- Placas de vehículos: ^[A-Z]{3}-\d{3}$ (3 letras mayúsculas seguidas de un guión y 3 números) 
2. España: 
- Placas de vehículos: ^[A-Z]{1,2}\d{4}[A-Z]{2}$ (1 o 2 letras mayúsculas seguidas de 4 números y 2 letras mayúsculas) 
3. Estados Unidos: 
- Placas de vehículos: ^[A-Z]{3}\d{3}$ o ^[A-Z]{3}-\d{3}$ (3 letras mayúsculas seguidas de 3 números, con o sin guión) 
- Nota: La composición de las placas varía según el estado. 
4. México: 
- Placas de vehículos: ^[A-Z]{3}-\d{3,4}$ (3 letras mayúsculas seguidas de un guión y 3 o 4 números) 
5. Argentina: 
- Placas de vehículos: ^[A-Z]{3}\d{3}$ (3 letras mayúsculas seguidas de 3 números) 

Europa 

1. Alemania: ^[A-Z]{1,3}-\d{1,4}$ (1 a 3 letras mayúsculas seguidas de un guión y 1 a 4 números) 
2. Francia: ^[A-Z]{2}\d{3}[A-Z]{2}$ (2 letras mayúsculas seguidas de 3 números y 2 letras mayúsculas) 
3. Italia: ^[A-Z]{2}\d{3}[A-Z]{2}$ (2 letras mayúsculas seguidas de 3 números y 2 letras mayúsculas) 
4. Reino Unido: ^[A-Z]{2}\d{2}[A-Z]{3}$ (2 letras mayúsculas seguidas de 2 números y 3 letras mayúsculas) 
5. Portugal: ^[A-Z]{2}-\d{2}-[A-Z]{2}$ (2 letras mayúsculas seguidas de un guión, 2 números, otro guión y 2 letras mayúsculas) 

África 

1. Sudáfrica: ^[A-Z]{3}\d{3}$ (3 letras mayúsculas seguidas de 3 números) 
2. Egipto: ^[A-Z]{1,3}\d{1,4}$ (1 a 3 letras mayúsculas seguidas de 1 a 4 números) 
3. Marruecos: ^[A-Z]{1,2}-\d{1,5}$ (1 o 2 letras mayúsculas seguidas de un guión y 1 a 5 números) 
4. Nigeria: ^[A-Z]{3}\d{4}$ (3 letras mayúsculas seguidas de 4 números) 

El sistema deberá contar con una persistencia, que de acuerdo al país de la cua_master, entienda cual es la expresión que permite validar la placa respectiva. 

Persistencia de datos de recolectores: 
En la medida de que las placas pasen el proceso de validación propio del " servicio conrec ”, el sistema debe guardar datos de recolectores válidos en una base de datos encriptada, que luego puede ser accedida por ejemplo a partir de la digitación de las cédulas o las placas, de tal manera que “autocomplete” los datos que el usuario está “programando” en la donación. 

Esta persistencia debe tomar en cuenta, que un mismo identificador personal y nombre (datos que si pueden estar pareados), puede manejar varias placas, y también puede atender a varios beneficiarios. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 f7231dca-55cb-4d19-9ddc-d5aac076b765 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 89de44f0-6be7-4c6b-9e10-9d589ac909ab 
 2025-06-25T04:31:09.0717155Z 

 {"SessionId":"e274c647-b9e6-456d-909e-5be82a71b5fd","SequenceId":3928,"FluidContainerCustomId":"45354ed6-4e2a-49d7-8955-f0bc74c8a8c7","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 APP: validación de placas de vehículos para programación de recogida de donaciones y mejora en el proceso