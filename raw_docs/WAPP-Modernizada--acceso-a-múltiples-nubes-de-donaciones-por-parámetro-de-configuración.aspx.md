# WAPP-Modernizada--acceso-a-múltiples-nubes-de-donaciones-por-parámetro-de-configuración.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Resumen&#58; 
 Dadas las proyecciones de nuevas funcionalidades para EatCloud, que implicarán la creación de nuevas “nubes” o “cuentas maestras” para un mismo territorio, se deberá habilitar para los diferentes Puntos de Donación el poder crear “donaciones” o nuevos conceptos como “ventas”, “distribuciones”, “revalorizaciones” (que a nivel de datos serán muy similares al ente “donación” del sistema actual). &#160;Esto implicará que un mismo POD o una CUA_USER, podrá tener parámetros de configuración para asociarle una, dos, tres, … (por el momento se tiene en mente hasta tres, pero esto puede ampliarse a futuro), que le permita hacer&#58; donaciones, ventas, revalorizaciones, distribuciones, afectando diferentes “nubes” (que para efectos técnicos serían eatc_dona_headers y eatc_dona de diversas cuentas maestras. 
&#160; 
 Aproximación inicial&#58; una tabla con cuentas maestras secundarias 
 Dado que en la estructura actual de datos, un POD y una CUA_USER, están asociadas a una sola CUA_MASTER, se propone, crear una estructura de datos adicional, en donde se relacione a cada cua_user o cada POD, con cuentas maestras secundarias, a las cuales podrá acceder a través de la misma funcionalidad de “Crear donación” habilitando selectores para identificar la nube respectiva, y en las funcionalidades de gestión también a nivel de selectores, pero privilegiando una vista integrada de las diferentes nubes (el selector de “nube” deberá servir más como un filtro que como una habilitador de consulta). 
&#160; 
En la estructura de configuración se deberá también habilitar parámetros o campos que permitan nombrar la “transacción respectiva”, los objetos transables (que para el caso de las donaciones son productos) y de acuerdo a estas configuraciones, al seleccionar una nube u otra, la UI deberá nombrar las transacciones y los objetos transables, tal cómo se configuran en la tabla de cuentas maestras adicionales asociadas. 
&#160; 
Como práctica común se ha establecido que este tipo de configuraciones se puedan operar por CUA_USER, pero también a nivel más granular por POD, por lo tanto la arquitectura de la tabla deberá contemplar estas dos opciones. 
&#160; 
 Ajuste en funcionalidad de “Creación de donaciones” 
Se deberá ajustar la funcionalidad de creación de donaciones, para permitir el acceso a varias “nubes” o “cuentas maestras” y al seleccionarlas, cambiar la UI para nombrar las “transacciones” y también los objetos transables según la configuración específica. 
&#160; 
 Ajustes en las funcionalidades de “Gestión de donaciones” 
Se deberá ajustar las funcionalidades asociadas con la “gestión de donaciones”, como por ejemplo&#58; los listados de “donaciones”, para incorporar las transacciones de otras nubes o cuentas maestras en la misma interfaz. &#160;Deberán existir filtros para visualizar transacciones propias de una nube específica. &#160;Se deberán contemplar por ejemplo, tarjetas de colores diferentes para diferenciar las diferentes transacciones correspondientes a las diversas nubes. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 752e75db-b080-4e3b-a61b-1551000cbf86 
 1!1!2 
 https://eastus0-3.pushfp.svc.ms/fluid 
 d5d0f8ec-9942-4ace-a772-cc6b1280302d 
 2025-06-06T05:36:57.6526233Z 

 {"SessionId":"09d0dc12-837f-4e89-91e0-2369c059f046","SequenceId":6624,"FluidContainerCustomId":"5446e8f9-dc47-4d42-b562-7e68324e4c5b","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 WAPP Modernizada: acceso a múltiples nubes de donaciones por parámetro de configuración