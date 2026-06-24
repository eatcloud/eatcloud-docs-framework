# cronjobs.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C4118 
 Article 

Cada vez que se crea una cuenta maestra legacy, se deben crear ciertos cronjobs para su buen funcionamiento, cabe aclarar que el horario con el que se ejecutan estos crones es con el horario del servidor, para este caso está configurado en la zona horario de Colombia. (America/Bogota) UTC-5 

 Pasos para configurar los crones: 

Revisar la plantilla de crones que luce así:

 Entrar al FTP de donantes en la  ruta: /public_html/jobs 

Aquí se encuentran los archivos necesarios para realizar la configuración.  

- gcron.sh //este archivo contiene el script para generar los cron dentro del servidor 
- crons.txt //este archivo contiene los crones que se van a crear 
- cuamaster.txt //este archivo contiene las cuentas NUEVAS que se van a crear 
- cuamaster_creadas.txt //este archivo es para llevar un control de las cuentas que se han creado

 Abrir el archivo cuamaster.txt si hay algún contenido en este archivo se debe cortar y añadir el contenido al archivo cuamaster_creadas.txt dado que se supone ya fueron creadas (si hay dudas se puede validar si ya fueron creados a través del cPanel buscando por el nombre de la cua_master). Una vez el archivo está limpio, se agregan las nuevas cuentas, por ejemplo para este caso, se van añadir la siguientes cuentas maestras: 
- prt (Portugal) 
- cri (Costa Rica)

Una vez fueron añadidas, guardar los cambios.

Las que ya se crearon: 

 Abrir SSH  
- Pedir las credenciales a quién corresponda dentro del equipo técnico.  

Una vez se inicia sesión, se accede a la ruta donde están los archivos:

Dentro de la ruta se ejecuta el comando ls para listar los archivos disponibles y ahí se visualizan los mismos archivos que anteriormente se habían editado por FTP. Para revisar si los cambios realizados tuvieron efecto se puede ejecutar el siguiente comando para visualizar el contenido del archivo: cat nombre_archivo
Para este caso se ve que tomó el cambio completo como se había editado: 

  Ejecutar script bash  

6. Revisar Cpanel (donantes) . Si es necesario cambiar el horario por cada país , esto se debe hacer manual. 
Luce así:

 Otras configuraciones: 

- Configurar correo donde va a llegar la notificación de nuevo beneficiario inscrito. Datagov.Cua_master.eatc_pod_creation_notification_emails //este correo se debe pedir a la persona encargada.  

 - Revisar que los campos de la tabla de encabezados y detalles, tenga el mismo número de campos que la de ABACO. (Esto no debería pasar normalmente . Recordar que para crear un nuevo campo se debe usar el api de creación de campos para que afecte a todas las cuentas maestras. Y cuando se crea una nueva está toma la estructura de Abaco)  

- Revisar que las tablas comunes por cuentas maestras estén creadas correctamente . (Esto no debería pasar dado que al crear una nueva cuenta usa el mismo script para todas , si por algún motivo se crea de maneral manual y muy particular entonces se debe reportar para hacer los ajustes respectivos)  

 [{"UserId":14,"DisplayName":"Jesús David Ramírez González","LoginName":"jesus.ramirez@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 
 62c1cbf7-62da-4409-b6ba-c701993b740c 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 a10aed5c-fe7a-4a56-95ce-1730f3fe6f3f 
 2025-06-28T22:30:59.4996511Z 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 {"SessionId":"1a5987c5-8dae-4f25-a042-f9a80ea9e9eb","SequenceId":6984,"FluidContainerCustomId":"7ead41e6-fd57-4042-ace4-f2655595b9a7","IsSingleUserSession":true,"ClientOperation":3,"RestoreTo":"","RestoredFrom":""} 
 14;#i:0#.f|membership|jesus.ramirez@eatcloud.com 
 Jesús David Ramírez González 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 1011.00000000000 

 Configurar cron jobs para cuentas maestras