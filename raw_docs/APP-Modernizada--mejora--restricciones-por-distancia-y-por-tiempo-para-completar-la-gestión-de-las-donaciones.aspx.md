# APP-Modernizada--mejora--restricciones-por-distancia-y-por-tiempo-para-completar-la-gestión-de-las-donaciones.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 APP Modernizada: mejora: restricciones por distancia y por tiempo en "Recogida de donación" "},"containsDynamicDataSource":false}">

Resumen: 
 En la actualidad, el botón “recoger donación” se despliega sin ningún tipo de restricción, y esta circunstancia abre la puerta a que se pueda generar una gestión inadecuada de las donaciones, haciéndolas de manera inadecuada a distancia, sin asistir al punto de donación y generando con esto problemas operativos. 

 También se han podido establecer que hay malas prácticas con respecto a la fecha y hora de recogida programadas, que hacen que dicha fecha y hora no se respete. 

 Por lo tanto se ha propuesto una mejora que restrinja por distancia y por tiempo la activación del anterior botón.  A continuación se proponen acciones para dar de alta esta mejora, que contribuirá a una adecuada gestión de las donaciones. 

 Parámetros de configuración de la funcionalidad 
Se deberá dar de alta una estructura de datos mediante la cual se puedan configurar los parámetros de restricción de la siguiente funcionalidad.  Dicha estructura deberá tener los siguientes parámetros 

 cua_master :  debe permitir una configuración _default para generar una configuración (inicial) para todos los casos, pero posteriormente se podrán generar configuraciones por cuenta maestra específica. 

 cua_user :  debe permitir una configuración _default para generar una configuración (inicial) para todos los casos, pero posteriormente se podrán generar configuraciones por cuenta maestra específica. 

 pod_id :  debe permitir una configuración _default para generar una configuración (inicial) para todos los casos, pero posteriormente se podrán generar configuraciones por cuenta maestra específica. => Se puede pensar para más adelante. 

 minutes_from_programed_picking_datetime : Este parámetro contendrá un número, que corresponderá el número de minutos, antes y después, para activar el botón. 

 km_from_pod_coordinates :  Este parámetro contendrá un número, que corresponde al número de KM al rededor de la coordenada del pod, en los cuales se permitirá la activación del mismo. 

Datos iniciales sugeridos 
Se sugieren los siguientes datos iniciales de configuración: 

 cua_master = _default   

 cua_user= _default 

 pod_id = _default 

 minutes_from_programed_picking_datetime =40 

 km_from_pod_coordinates =1 

Lista blanca de usuarios que no se les requerirá operar esta funcionalidad 
El sistema deberá tener una lista blanca en la cuál se agreguen usuarios de la APP, que podrán operar sin estas restricciones, por ser usuarios conocidos y de reconocida correcta operación del sistema.  Para los usuarios no ingresados en esta lista blanca, el sistema operará con las restricciones definidas. 
Al ingresar a la funcionalidad solicitar de manera obligatoria la detección de la ubicación del dispositivo 
Dado que será necesario evaluar la ubicación del dispositivo, se le debe obligar al usuario con restricciones (es decir que no está en lista blanca), que prenda su GPS.  Si no lo prende, el sistema deberá informar que no podrá operar esta funcionalidad necesaria para la gestión de donaciones.  El sistema deberá tomar la coordenada (decimal) al ingresar a la funcionalidad y guardarla en variables que se operarán más adelante 

lat 

lon  

Al ingresar a la funcionalidad el sistema deberá consultar la fecha y hora actual 
En formato AAAA-MM-DD HH:MM:SS y teniendo en cuenta los respectivos husos horarios, para hacer comparable esta fecha y hora con la fecha y hora de recogida programada (eatc-programed_picking_datetime) 
Consultas para definir los parámetros de restricción 
Para todos los usuarios con restricciones (es decir que no está en lista blanca) el sistema deberá consultar la cua_master , la cua_origin y el pod-id, de la respectiva donación a gestionar, adicional a los parámetros que permitirán evaluar las restricciones (eatc-programed_picking_datetime, eatc-lat, eatc-lon) 
{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-code= {{eatc-code}} &_cmp=eatc-pod_id,eatc_cua_origin,eatc-programed_picking_datetime,eatc-lat,eatc-lon 

Ejemplo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=_lk77&_cmp=eatc-pod_id,eatc_cua_origin,eatc-programed_picking_datetime,eatc-lat,eatc-lon   

Con estos datos deberá consultar los parámetros de configuración de la presente funcionalidad (el parámetro cua_user corresponderá a eatc_cua_origin , y establecer si se tienen registros válidos.  En caso de que no, se deberán consultar los parámetros por _default , que para el caso inicial sugerido serán:  

 minutes_from_programed_picking_datetime =40 

 km_from_pod_coordinates =1 

Validación de ubicación 
Con los datos de las anteriores consultas ( lat , lon del dispositivo; parámetros de restricción y datos de la donación), el sistema deberá realizar la siguiente validación: 
 {{URL_entorno_donantes}} /get/ {{cua_master}} /getpuntos? table = eatc_dona_headers & fieldname = eatc-lat,eatc-lon & fieldvalue = {{ lat }} , {{ lon }} & showfield = {{eatc-code}} & km = {{ km_from_pod_coordinates }} &filterfield_1=eatc-code&filtervalue_1= {{eatc-code}} 
Si la consulta arroja una respuesta válida, se pasa a la segunda validación (validación por tiempo). 
Si no arroja una respuesta válida, se debe ampliar la consulta a 1000 KM para obtener la distancia a la cual está el punto de donación (la donación) de la coordenada. 
 {{URL_entorno_donantes}} /get/ {{cua_master}} /getpuntos? table = eatc_dona_headers & fieldname = eatc-lat,eatc-lon & fieldvalue = {{ lat }} , {{ lon }} & showfield = eatc-code,eatc-programed_picking_datetime & km = 1000 &filterfield_1=eatc-code&filtervalue_1= {{eatc-code}} 
 Y mostrar el botón desactivado, mostrandole al usuario que se encuentra a X KM de la donación, y por lo tanto no se activa el botón. 

 Ejemplo 1: 

 Ambiente:  pruebas  https://devdonantes.eatcloud.info 
 cua_master: abaco 
 coordenadas del dispositivo:  6.243966, -75.595080 
 km: valor por defecto ( km_from_pod_coordinates ) =1 
 código de la donación:   00002003120729 

El sistema realiza esta consulta: 

 https://devdonantes.eatcloud.info/get/abaco/getpuntos?table=eatc_dona_headers&fieldname=eatc-lat,eatc-lon&fieldvalue=6.2443369,-75.5961205& showfield=eatc-code,eatc-programed_picking_datetime &km=1&filterfield_1=eatc-code&filtervalue_1= 00002003120729 

 Dado que el sistema arroja una respuesta válida se pasa a la validación del tiempo  

 Ejemplo 2: 
 Ambiente:  pruebas  https://devdonantes.eatcloud.info 
 cua_master: abaco 
 coordenadas del dispositivo:  6.236543, -75.611441  
 km: valor por defecto ( km_from_pod_coordinates ) =1 
 código de la donación:   00002003120729 

El sistema realiza esta consulta: 
 https://devdonantes.eatcloud.info/get/abaco/getpuntos?table=eatc_dona_headers&fieldname=eatc-lat,eatc-lon&fieldvalue= 6.236543,-75.611441 & showfield=eatc-code,eatc-programed_picking_datetime &km=1&filterfield_1=eatc-code&filtervalue_1= 00002003120729   

Como la consulta no arroja un resultado válido, entonces el sistema realiza la siguiente consulta (ampliando el rango de búsqueda a 1000 KM) 
 https://devdonantes.eatcloud.info/get/abaco/getpuntos?table=eatc_dona_headers&fieldname=eatc-lat,eatc-lon&fieldvalue=6.236543,-75.611441&showfield=eatc-code,eatc-programed_picking_datetime&km=1000&filterfield_1=eatc-code&filtervalue_1=00002003120729   

 Y con los datos recibidos, coloca el botón inactivo y le informa al usuario que aun no puede recoger la donación porque está a 2,09 KM del punto de donación 

Validación por tiempo 
El sistema deberá tomar la fecha y hora actual (capturada por el dispositivo) y a esa fecha y hora restarle (para obtener el rango inferior) y sumarle (para obtener el rango superior) el dato de la restricción minutes_from_programed_picking_datetime . Con estas fechas, procederá a consultar la fecha y hora programada de recogida, para establecer si la misma está en el rango definido, de la siguiente manera 
{{URL_donantes}}/api/{{cua_master}}/eatc_dona_headers?eatc-code= {{eatc-code}} &eatc-programed_picking_datetime[0]={{fecha_hora_actual_ menos _ minutes_from_programed_picking_datetime }}&eatc-programed_picking_datetime[1]={{fecha_hora_actual_ mas _ minutes_from_programed_picking_datetime }}&_cmp=eatc-code 
Si la consulta se obtiene una respuesta válida, entonces se despliega el botón. 

En caso de que no se obtenga una respuesta válida, se debe informar que aun no puede gestionar la donación porque no se ha cumplido la fecha y hora programada de recogida. 

 Ejemplo 1: 
 Ambiente:  pruebas  https://devdonantes.eatcloud.info 
 cua_master: abaco 
 código de la donación:   00002003120729 
 Fecha y hora actual capturada por el dispositivo : 2020-03-13 13:10:00 
 minutes_from_programed_picking_datetime =40 (valor por defecto) 

 El sistema determina el rango inferior y superior para la consulta 

Rango inferior = 2020-03-13 13:10:00 - 40 minutos = 2020-03-13 12:30:00 

Rango superior = 2020-03-13 13:10:00 + 40 minutos = 2020-03-13 13:50:00 
Por lo tanto el sistema realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00002003120729&eatc-programed_picking_datetime[0]=2020-03-13%2012:30:00&eatc-programed_picking_datetime[1]=2020-03-13%2013:50:00&_cmp=eatc-code   

Como obtiene una respuesta válida, entonces muestra el respectivo botón. 

 Ejemplo 1: 
 Ambiente:  pruebas  https://devdonantes.eatcloud.info 
 cua_master: abaco 
 código de la donación:   00002003120729 
 Fecha y hora actual capturada por el dispositivo : 2020-03-13 13:55:00 
 minutes_from_programed_picking_datetime =40 (valor por defecto) 

 El sistema determina el rango inferior y superior para la consulta 

Rango inferior = 2020-03-13 13:55:00 - 40 minutos = 2020-03-13 13:15:00 

Rango superior = 2020-03-13 13:10:00 + 40 minutos = 2020-03-13 14:35:00 
Por lo tanto el sistema realiza la siguiente consulta: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-code=00002003120729&eatc-programed_picking_datetime[0]=2020-03-13%2013:15:00&eatc-programed_picking_datetime[1]=2020-03-13%2014:35:00&_cmp=eatc-code   

Como la misma no arroja resultados, entonces el botón se muestra desactivado 

Otra información a mostrar cuando no se despliega el botón 
Cuando no se despliegue el botón, el sistema deberá mostrar un botón con más información, en donde se expliquen estas restricciones.  Y se le diga al usuario que si tiene alguna condición operativa recurrente que no le permite estar en el punto de donación para recogerla a la hora programada, se comunique con el área de soporte (puede ser a través de un mensaje de whatsapp predeterminado, en donde se le pida a la organización que explique su “condición recurrente de operación que le impide ir al punto a la hora programada” (con el ánimo de evaluar la inclusión del usuario en la lista blanca).  El mensaje debería incluir el código del usuario para facilitar la edición de la lista blanca. 
También se debe darle la opción al usuario (cuando no se muestra por temas de tiempo) que reprograme la recogida, de tal manera que (en caso de que se pueda) quede una fecha y hora de recogida que esté dentro del rango de evaluación. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%2810%29%2F1761777911089image.png&ow=380&oh=446, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FPage%2810%29%2F1761777911089image.png&ow=380&oh=446 

 3f279341-0ac6-401b-b338-bfeaca76526e 
 4!1!3 
 https://eastus0-0.pushfp.svc.ms/fluid 
 bad4a538-0328-4545-9780-7789db8d53ff 
 2025-10-30T06:41:45.6507396Z 

 {"SessionId":"c7be084b-50f2-4927-81b5-b86675b91577","SequenceId":19501,"FluidContainerCustomId":"c22ef4a8-1636-4dc8-aa31-3f0af3b941f7","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1111.00000000000 

 APP Modernizada: mejora: restricciones por distancia y por tiempo en "Recogida de donación"