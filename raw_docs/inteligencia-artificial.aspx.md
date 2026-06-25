# inteligencia-artificial.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En la presente sección se establecen los lineamientos generales y las áreas en que se plantean para el desarrollo de proyectos que incorporen tecnologías de inteligencia artificial en EatCloud. 

 Proyectos principales&#58; 
&#160; 
 1. Automatización de interfaces de ingreso de información a la plataforma EatCloud 
 Mediante diferentes técnicas y arquitecturas, que potencien al máximo una interacción fluída y natural con los usuarios finales (como por ejemplo&#58; interacción en lenguaje natural, captura de información de productos y pesos a partir de fotografías, entre otras), permitir la carga de información al sistema EatCloud, con la siguiente proyección&#58; 
&#160; 

&#160;Creación de donaciones (transacciones en general) 
Utilizando las APIs que tenemos desarrolladas para ingresar “Donaciones (o transacciones en general)” a nuestro sistema, permitir la captura mediante diversos métodos de fácil utilización y adopción y con técnicas que permitan una interacción en lenguaje natural o a través del reconocimiento de imágenes, para aportar los componentes de una donación (productos con sus respectivas cantidades, pesos unitarios y pesos totales). &#160; Para un proyecto anterior que proponía una interfaz a través de un chat de WhatsApp, se levantó la siguiente especificación&#58; 
&#160; 
&#160; 

Bot_creacion_donacion_spec 

 En estas aplicaciones se podrán implementar técnicas de &quot; computer visión &quot; o &quot; reconocimiento de imágenes &quot; para la publicación de los anuncios y la identificación de productos (producto, cantidad, pesos unitarios y pesos totales).&#160; También se podrán incorporar estas técnicas para la determinación y registro de las fechas de vencimiento.&#160; También se podrán incorporar tecnologías de reconocimiento de voz para la captura de anuncios (dictado directo a la máquina o dispositivo). 
&#160; 
2. Onboarding de cuentas usuario 
Mediante un agente o asistente automatizado, permitir el ingreso de todos los datos necesarios para dar de alta en el sistema una “cua_user” o “donante”, de tal manera que la captura que se realiza actualmente en las URLs de Onboarding ( Registro de donantes y puntos de donación ), se pueda hacer de manera conversacional y asistida por inteligencia artificial, facilitando al máximo la labor para los nuevos clientes. 
&#160; 
3. Onboarding de ✅ DOMA – Dynamic Operators for Material Allocation 
Mediante un agente o asistente automatizado, permitir el ingreso de todos los datos necesarios para dar de alta en el sistema una “DOMA” o “Beneficiario”, de tal manera que la captura que se realiza actualmente en las URLs de Onboarding ( Registro de beneficiarios ), se pueda hacer de manera conversacional y asistida por inteligencia artificial, facilitando al máximo la labor para los nuevos miembros del ecosistema de rescate o revalorización. 

 2. Entrenamiento de un modelo de IA para revisión de errores en los datos 
Nuestro sistema, al permitir capturas manuales de productos que se donan, o al permitir carga de archivos planos manuales con la información de las donaciones, es propenso a que se le introduzcan errores, como por ejemplo, cantidades y pesos excesivos. &#160; Aunque el sistema cuenta con implementaciones para minimizar este tipo de problemas no ha sido posible zanjarlos por completo, y por eso se requiere de un sistema que permita identificar de manera temprana este tipo de errores, y corregirlos o informar para que se corrijan rápidamente. &#160;A continuación se presenta un primer análisis que se realizó con respecto a esta necesidad 

Alarmas-y-Control-de-la-Data-en-EatCloud 

 3. Proyecciones de nuevos indicadores y de desperdicio de alimentos 
A partir de la información histórica recolectada en nuestra plataforma, contar con un sistema que permita realizar proyecciones y cálculos estadísticos, para generar informes y cifras que generen valor para nuestros clientes y la comunidad en general. 

&#160; 
 Otros proyectos&#58; 
&#160; 
 Aprovechando la IA Generativa y la Clasificación de Texto para Medir el Impacto Real de las Donaciones 
&#160; 
La capacidad de categorizar eficientemente las donaciones en alimentos y no alimentos es un aspecto estratégico clave para la operación exitosa de la plataforma eatcloud. Actualmente, estamos categorizando los productos de nuestros clientes, como insumo para identificar KPIs de alimentos y de no alimentos (caso MAKRO), e igualmente para asignar categorías que permitan la integración a los sistemas de información de bancos de alimentos (caso BAMX). 
Al contar con esta funcionalidad, eatcloud puede ofrecer a los bancos de alimentos una visibilidad clara y detallada sobre el tipo de productos que están recibiendo. Esto permite a los bancos de alimentos planificar mejor la distribución y uso de estos recursos, asegurando que los alimentos lleguen rápidamente a quienes los necesitan. 
Asimismo, el uso de etiquetas representativas del tipo de producto donado brinda valiosa información adicional. Estas etiquetas permiten desglosar las donaciones en categorías significativas, como frutas y verduras, productos enlatados, productos secos, etc. Esto facilita el análisis del impacto económico, social y ambiental de las donaciones, permitiendo a eatcloud generar KPIs más precisos para sus clientes. 
Por ejemplo, al poder distinguir entre donaciones de alimentos y donaciones de suministros no comestibles, eatcloud puede cuantificar con mayor exactitud la cantidad de alimentos que lograron llegar a las comunidades necesitadas. Esto a su vez permite calcular el valor nutricional y el ahorro económico generado por estas donaciones de alimentos. Adicionalmente, al desglosar las donaciones por tipo de producto, eatcloud puede identificar tendencias y oportunidades para mejorar la sostenibilidad ambiental, como promover mayores donaciones de productos frescos y locales. 
En resumen, la capacidad de categorizar y etiquetar las donaciones es crucial para que eatcloud pueda brindar a sus clientes una visión completa del impacto de sus contribuciones. Esto fortalece la posición estratégica de eatcloud como proveedor de una plataforma tecnológica de vanguardia que maximiza el valor de las donaciones para las comunidades a las que sirven. 

 Automatización de tareas para promover la recogida de las donaciones 
 Se podrán utilizar técnicas de machine learning , y analítica de datos , para establecer las probabilidades de recogida de un anuncio de donación , teniendo en cuenta aspectos como, contenido del anuncio, comportamiento del punto de donación, cercanía de los beneficiarios, la horas de publicación, y el comportamiento y las necesidades de los beneficiarios, y de esta manera controlar parámetros dinámicos incorporables al anuncio, como es el caso del tiempo de cancelación del anuncio, la mensajería asociada a su publicación y el establecimiento de incentivos mediante técnicas de gamificación, para promover la recogida del anuncio. 

 Análisis de territorios EatCloud 
 Se podrán utilizar técnicas de machine learning , y análítica de datos , para establecer las configuraciones ideales, según el territorio y sus necesidades, de los tipos y volúmenes de donantes y de beneficiarios que deberán entrar a jugar parte del ecosistema, para que este sea lo más eficiente posible. 

 Automatización de la internacionalización de la plataforma 
 Se podrán utilizar técnicas de traducción automática combinadas con técnicas de data goverment para internacionalizar la plataforma de manera automática y poder acceder de manera muy rápida a nuevos territorios. 

 Automatización de procesos de soporte 
 Mediante técnicas de Machine Learning y Bots conversacionales , se podrán implementar mecanismo de soporte técnico automáticos para la atención de necesidades en este sentido. 

 Cálculo de KPIs 
 Mediante técnicas de Machine Learning y análisis de big data se podrán ajustar de manera dinámica el cálculo de KPIs e incorporar nuevos KPIs, importantes para la medición del impacto (como por ejemplo&#58; huella hídrica). 

 Análisis y atención de necesidades nutricionales 
 Mediante técnicas de Machine Learning y análisis de big data se podrán determinar las necesidades nutricionales de las diversas fundaciones o personas que se atiendan mediante la plataforma y con ello permitirles acceder a una dieta más balanceada a partir de los alimentos que se gestionan. 

 Recursos 
 https&#58;//fairlac.iadb.org/es 
 Sesión aceleración Google sobre productos con alto riesgo tecnológico 
 Productos Google 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finteligencia-artificial%2FBot_creacion_donacion_spec.pdf, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Finteligencia-artificial%2FBot_creacion_donacion_spec.pdf 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 d13899a2-6ec6-4475-93f4-68f6ee61854f 
 3!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 0454e277-2cf6-48d1-bd7c-aa09a3e4f286 
 2025-09-23T00:08:46.9385756Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"b56962c3-6fea-48b7-bc87-a0d43d1e3f15","SequenceId":7368,"FluidContainerCustomId":"caa645bd-6672-4807-92d2-816d786926f6","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 1103.00000000000 

 INTELIGENCIA ARTIFICIAL