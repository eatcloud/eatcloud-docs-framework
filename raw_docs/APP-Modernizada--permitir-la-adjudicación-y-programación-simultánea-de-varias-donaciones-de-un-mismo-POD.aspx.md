# APP-Modernizada--permitir-la-adjudicación-y-programación-simultánea-de-varias-donaciones-de-un-mismo-POD.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 APP Modernizada: permitir la adjudicación y programación simultánea de varias donaciones de un mismo POD "},"containsDynamicDataSource":false}">

Resumen: 
 En la actualidad, y dada la entrada de la operación de No Negociados,  es posible que en un mismo POD existan varias donaciones de diversos donantes.  Por esta circunstancia y con el ánimo de facilitar la labor de los beneficiarios, se aprobó una mejora para permitir la adjudicación y programación por lote de donaciones simultáneamente.  A continuación se presentan los diseños que soportan esta mejora y que se encuentran en: https://www.figma.com/design/kppPVS7JYiBEWHZL3tIM9r/Prototipo-no-negociados?node-id=0-1&p=f&t=KYwb0ySLfHTn6FM0-0   

Nueva pestaña en la nube de donaciones: por puntos de donación 
Se deberá desplegar una nueva pestaña en la nube, nombrada “por puntos de donación” 

Esta nueva pestaña tendrá dos subsecciones: 
Tiendas destacadas 
Mostrará las dos tiendas que tienen más donaciones disponibles para el beneficiario en cuestión.  Si existen empates, la variable para desempatar será la cercanía a la sede del beneficiario: se mostrarán primero las más cercanas. 

Todas las tiendas 
Deberá mostrar un listado de los puntos de donación en donde existen donaciones disponibles para el beneficiario, pero en este caso el criterio de ordenamiento será solamente la distancia (no el número de donaciones disponibles como en el caso de “Tiendas destacadas”). 

Al hacer clic en una de las “tiendas” de cualquiera de los dos listados, deberá aparecer una sección denominada “selector de donaciones” que presentará un “listado de donaciones por punto de donación” 

Selector de donaciones 
Funciona de manera muy similar a la nube, pero solamente presentará anuncios de un mismo punto de donación, con la novedad que cada card deberá tener una casilla de selección múltiple 

Como se anota en el figma, por defecto deben aparecer todas las donaciones del pod, seleccionadas. El criterio de ordenamiento de este listado, será que se deben presentar primero las que deben gestionarse antes, es decir, aquellas cuya fecha de cancelación sea más próxima.  Se aconseja también tener la funcionalidad de “des-seleccionar” / “seleccionar” Todas, es decir una casilla de selección al inicio de la lista (por defecto selecionada), que al “des-seleccionarla”, haga esa acción bulk sobre todas las donaciones de la vista. 

En la parte baja de la pantalla, siempre visible, debe existir un botón para “continuar” con las seleccionadas (mostrando el número de donaciones seleccionadas en la vista) 

Cuando se oprime este botón, se continúa a la siguiente pantalla: 

Detalle paquete de donación 
En esta vista se muestra información sobre el paquete de donaciones seleccionadas, con las siguientes funcionalidades: 
Cuenta regresiva para la cancelación  (en el diseño dice liberación, pero en este punto aun no se han programado las donaciones) 
Se mostrará el tiempo más próximo para que una de las donaciones seleccionadas se “cancele”.  Se deberá utilizar convenciones de colores, para que ese aviso esté en rojo, cuando la cancelación de la donación está a menos de una hora de ocurrir. 

Contador de pasos en la gestión del paquete 
Se extiende la funcionalidad que generalmente se desarrolló para una sola donación, al paquete seleccionado 

Detalles del punto de donación (en la imagen dice donante, pero en este caso será punto de donación) 
Se presentará el nombre y la dirección del punto de donación, con un vínculo a una funcionalidad de mapas para ver su coordenada en un mapa. 

Resumen del paquete 
Presentará la cantidad de donaciones seleccionadas y su peso combinado 

Donaciones seleccionadas 
Mostrará en una card abreviada los datos de las donaciones seleccionadas en el paquete, a saber: 

Nombre del donante 

KG totales de cada donacion 

Etiquetas (como por ejemplo: alimento preparado) 

Número de referencias 

Número de unidades 

Detalles de recogida 
Extensión de la misma funcionalidad para donaciones particulares, pero en este caso para el paquete 

Botones de acción para el paquete 
En este apartado habrán dos tipos de botones de acción: 

Programar recogida (junto con tiempo de programación de la donación) 
En este recuadro se presentará la información de la donación cuya programación deberá hacerse de manera más próxima, de acuerdo a los timeouts y restricciones que operan también para las donaciones singulares.  El botón de programar recogida, hará una función secuencial de la siguiente manera 

 Invocación múltiple del proceso “awarddona” : Se deberá invocar el proceso tantas veces como donaciones existan en el paquete, con el ánimo que todas queden asignadas al mismo beneficiario. 

 Paso directo a la pantalla de programación de las donaciones (programación del paquete): una vez las donaciones hayan quedado asignadas al beneficiario que opera la funcionalidad, se dará entrada directa a la funcionalidad de programación de las donaciones que más adelante se detalla ( Programación del paquete ). 
Elegir paquete 
Al elegir paquete se realizarán las siguientes funciones: 

 Invocación múltiple del proceso “awarddona” : Se deberá invocar el proceso tantas veces como donaciones existan en el paquete, con el ánimo que todas queden asignadas al mismo beneficiario. 

 Paso a modal en donde se pregunta si desea programar las donaciones (en este caso el paquete): Se mostrará un modal en donde se le pregunta al usuario si desea programar las donaciones todas de una vez.  En caso de que acepte, se le dirigirá a la funcionalidad de Programación del paquete .  En caso de que no, se le deberá indicar que deberá programar una a una las donaciones (y se redireccionan al flujo normal). 
No me interesa 
Si el usuario oprime este botón, se le deberá mostrar una advertencia que al hacerlo todas las donaciones del paquete seleccionado dejarán de aparecer en su nube de donaciones.  Si el usuario confirma, se deberá realizar la accion de “no me interesa” para todas las donaciones del paquete. 

Programación del paquete 
Esta funcionalidad será similar a la programación de una sola donación y mostrará lo siguiente 

Pasos restante para obtener las donaciones 
Funciona de manera similar a la implementación para donaciones particulares 

Horarios de atención 
Desplegará información de los horarios de atención del punto 

Formulario de datos de recolección 
Funcionará de manera similar a como funciona para una donación particular.  Se deberán tener en cuenta las anotaciones de diseño, por si es necesario aplicarlas no solamente en este punto, sino también en el proceso de programación singular de donaciones. 

Las restricciones del calendario deberán obrar dirigidas por los datos de la donación, con fecha máxima de programación más próxima, es decir, se revisan todas las donaciones del paquete de acuerdo a su timeout de programación ( global_scheduling_timeout ) y se escoge el más próximo 

Cuadro informativo de fecha máxima de recolección 
En este cuadro se debe mostrar (ojo que puede sonar algo contradictorio): la fecha máxima de recogida más próxima del paquete, es decir: se toman todas las fechas máximas de recogida (según el timeout respectivo:   global_scheduling_timeout ) de las donaciones del paquete y de todas ellas se muestra la más próxima.   

Cuadro informativo de fecha máxima para realizar la programación 
En este cuadro se debe mostrar (ojo que puede sonar algo contradictorio): la fecha máxima límite para programar el paquete, es decir: se toman todas las fechas máximas de programación de recogida (según el timeout respectivo:   particular_scheduling_timeout ) de las donaciones del paquete y de todas ellas se muestra la más próxima.   

Botón “Programar recolección del paquete” 
Al accionar este botón se deberán realizar invocaciones a los servicios: 

 conrec : con los datos de recolección y el dato de una sola donación, se debe validar si el recolector no está en lista negra. 

 programdona : se deberá invocar tantas veces como donaciones hayan en el paquete (con los mismos datos de recolección en cada una de esas invocaciones) 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=7ccb4a66b98c43f7a08449f32a0f47bb&ext=png&ow=857&oh=830, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=7ccb4a66b98c43f7a08449f32a0f47bb&ext=png&ow=857&oh=830 

 a1c087ce-6a3d-4ce0-9e8a-61c47d75b410 
 4!1!3 
 https://centralus0-0.pushfp.svc.ms/fluid 
 8a912e21-11ad-44fc-b4c4-8019c9829566 
 2026-02-06T03:40:29.8065724Z 

 {"SessionId":"892a68f3-427a-41fb-bc31-00f779062e70","SequenceId":18844,"FluidContainerCustomId":"64646a5b-487f-4842-9b0a-bc3151d3cefc","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1190.00000000000 

 APP Modernizada: permitir la adjudicación y programación simultánea de varias donaciones de un mismo POD