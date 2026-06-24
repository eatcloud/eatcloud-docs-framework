# Bots-inteligentes-para-automatización-de-procesos.aspx

0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

Caso de uso: Creacin de donaciones 

Actores: 
Usuario, Bot inteligente, Sistema EatCloud (API y API pblica) 

Objetivo: 
Facilitar el proceso de creacin de donaciones en la plataforma EatCloud, mediante un bot conversacional en WhatsApp 

Descripcin: 
Un bot conversacional ira preguntando al usuario de EatCloud por la informacin necesaria para realizar una donacin en la plataforma. 

Precondicin: 
Cuenta de Usuario (empresa) del usuario dada de alta en el sistema EatCloud.  API pblica de creacin de donaciones, dada de alta. 

Secuencia normal 
El usuario entra al bot 
El bot saluda y pregunta sobre el nombre de usuario en EatCloud (eatc_user) para un punto de donacin en especfico y la contrasea (eatc_password) de dicho punto de donacin 
El usuario entrega la informacin del nombre de usuario y de la contrasea almacenada en el sistema de EatCloud. 
El Bot enva esta informacin a travs de un API privada a EatCloud, para la validacin de las credenciales de acceso 
Si la validacin es incorrecta, el sistema responde con un mensaje de error.  El Bot le informa al usuario que sus datos no son vlidos y no lo deja entrar. 
Si la validacin es correcta, el sistema retorna la cuenta maestra (eatc_cua_master), la cuenta usuario (eatc_cua) y el cdigo del punto de donacin ( eatc-pod_id ) 
El bot pregunta sobre el primer producto que desea donar (nombre: eatc-odd_name ). 
El Usuario le da el nombre del producto a donar 
El bot enva el nombre a la API privada de productos para ver si existe la informacin del mismo para traerla 
Si le informacin del producto no existe, el API EatCloud entregar una respuesta no vlida y ante esta respuesta el bot deber preguntar la siguiente informacin con respecto al producto especfico 
Cdigo del producto ( eatc-odd_id ): String. 
Peso unitario del producto en KG  ( eatc-odd_unit_weight_kg ): Float (separador de decimales punto). 
Costo del producto  ( eatc-unit_cost ); Integer 
El porcentaje de IVA del producto ( eatc-VAT_percentage ): Integer (de cero a 19 por lo general) 
Si la informacin del producto existe, el sistema retornar cdigo del producto  ( eatc-odd_id ), el peso unitario en KG ( eatc-odd_unit_weight_kg ), el costo unitario ( eatc-unit_cost ), y el porcentaje de iva del producto ( eatc-VAT_percentage ) 
El Bot pregunta por la cantidad a donar del producto 
El usuario entrega el dato del nmero de unidades del producto definido para donar ( eatc-odd_original_quantity ) 
El Bot multiplicando el peso unitario en KG ( eatc-odd_unit_weight_kg ) por las cantidades ( eatc-odd_original_quantity ), valida en un API privada el peso a donar , es excesivo o es no permitido 
Si el peso es excesivo, le pregunta al usuario si est seguro que esa es la cantidad a donar dado que representa un peso total de {{ eatc-odd_original_quantity*eatc-odd_unit_weight_kg }} KG 
Si el usuario confirma la cantidad, el Bot sigue adelante 
Si el usuario cambia la cantidad esta ser el nuevo dato de cantidad a donar ( eatc-odd_original_quantity ) 
Si el peso es prohibitivo, el sistema informa que no le est permitido donar  {{ eatc-odd_original_quantity*eatc-odd_unit_weight_kg }} KG del producto y solicita que ingrese una nueva cantidad. 
El usuario ingresa una nueva cantidad 
El Bot efecta de nuevo la validacin a partir del paso 7.d.i- 
El Bot guarda la informacin para construir el llamado al API pblica de creacin de donaciones. 
El Bot pregunta si desea donar otro producto 
Si el usuario dice que si, repite el proceso a partir del punto 5 
Si el usuario dice que no, el bot prepara la informacin para realizar el llamado al API pblica 
Con la informacin recolectada, el Bot arma la informacin para realizar el llamado al API pblica de la siguiente manera 
 Endpoint : 
Pruebas: https://devdonantes.eatcloud.info/pbapi/ {{eatc_cua_master}} / {{eatc_cua}} 
Produccin: https://donantes.eatcloud.info/pbapi/ {{eatc_cua_master}} / {{eatc_cua}} 
 Mtodo: POST 
 Datos de autenticacin del servicio:  
 Usuario: {{eatc_user}} 
 Password: {{eatc_password}} 
 Mtodo de autenticacin: Basic Auth 
 Objeto en el body de la peticin: 1 

 { 
      "_operation": "create_donation" , 
      "_data":[ 
         { 
         "eatc-pod_id": "{{ eatc-pod_id }} 1 " , 
         "eatc-odd_id" : "{{ eatc-odd_id }} 1 " , 
         "eatc-odd_name": "{{ eatc-odd_name }} 1 " , 
          "eatc-odd_original_quantity": "{{ eatc-odd_original_quantity }} 1 " , 
          "eatc-odd_unit_weight_kg": "{{ eatc-odd_unit_weight_kg }} 1 " , 
          "eatc-unit_cost": "{{ eatc-unit_cost }} 1 " , 
          "eatc-VAT_percentage": "{{ eatc-VAT_percentage }} 1 " 
         }, 
         { 

         } 
        { 
         "eatc-pod_id": "{{ eatc-pod_id }} n " , 
         "eatc-odd_id" : "{{ eatc-odd_id }} n " , 
         "eatc-odd_name": "{{ eatc-odd_name }} n " , 
          "eatc-odd_original_quantity": "{{ eatc-odd_original_quantity }} n " , 
          "eatc-odd_unit_weight_kg": "{{ eatc-odd_unit_weight_kg }} n " , 
          "eatc-unit_cost": "{{ eatc-unit_cost }} n " , 
          "eatc-VAT_percentage": "{{ eatc-VAT_percentage }} n " 
         }, 
     ] 
 } 

El sistema responde a partir de la ejecucin del servicio 
Si la respuesta no es exitosa, el Bot deber informarle al usuario que la donacin no fue creada y el motivo de la misma, y preguntarle si desea intentar de nuevo 
Si la respuesta es exitosa, el Bot informa al usuario que su donacin se cre exitosamente y que podr seguir su gestin por la WAPP del punto de donacin especfico 

Postcondicin: 
Anuncio de donacin creado en el sistema EatCloud 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=b81d3e09efaf4ec59d77ad4e715c267e&ext=jpeg, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=b81d3e09efaf4ec59d77ad4e715c267e&ext=jpeg 

 12;#i:0#.f|membership|juan.correa@eatcloud.com 
 Juan David Correa 
 965.000000000000 

 Bots inteligentes para automatizacin de procesos