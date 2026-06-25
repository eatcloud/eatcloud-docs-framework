# excepciones-asignación-directa-creación-de-encabezados.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 ***NUEVO*** proceso dinámico que opera sobre múltiples cuentas maestras 
 El proceso de creación de encabezados de donación debe correr para todas las cuentas maestras registradas en el respectivo maestro&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 
&#160; 
 Este ajuste aplica tanto para los procesos de creación de encabezados activados por tareas programadas como los que son activados mediante servicios web. 
&#160; 
 Dado un anuncio de donación ( eatc_dona )&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. eatc_cua_master &#125;&#125;/eatc_dona?eatc-dona_header_code=&#123;&#123;eatc-dona_header_code&#125;&#125; 
&#160; 
 la plataforma debe crear un encabezado en donde se deberán realizar algunas operaciones de totalización de información, y se adicionará información para facilitar las búsquedas en la plataforma.&#160; Esta información se consolida en eatc_dona_headers 
 _DOM.base + &quot;headersApp/&quot; + _DOM.cua_master + _DOM.cua_user + code, 

&#160; 
 _crear_dona_headers.php 

 Proceso que opera en días NO hábiles (inicialmente para _DOM.cua_master = abaco) 
&#160; 
 Inicialmente a nivel de cronjob se debe programar para que solo opere en días NO&#160; hábiles (después de la generación de encabezados que corre a primera hora de la mañana).&#160; Este proceso deberá a su vez generar un proceso de match no exclusivo para quien generalmente es el adjudicatario directo (inicialmente para el Banco de Alimentos de Cali) y por lo tanto los encabezados de los anuncios que se generen de esta manera deben estar disponibles para todo el ecosistema y no solamente para quienes tienen asignación directa. 
&#160; 
 NOTA PARA POSIBLE MEJORAMIENTO FUTURO&#58; Se deberá evaluar si hay alguna manera de incorporar las condiciones de temporalidad en una persistencia para poderlas hacer dinámicas.&#160; En una primera instancia se establecen como condiciones estáticas que se programan a través de cronjobs. 
&#160; 
 Opera sobre anuncios cuyos puntos de donación poseen asignación directa 
 El sistema deberá realizar la siguiente consulta&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_direct_dona ?_id=_*&amp;_distinct=eatc-pod_id 
&#160; 
 Si se requieren procesos diferentes por cuentas maestras, la consulta sería&#58; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_direct_dona ?eatc_cua_master=&#123;&#123;_DOM. cua_master &#125;&#125;&amp;_distinct= eatc-pod_id 
&#160; 
 Para establecer un array de códigos&#160; de puntos de donación &#123;&#123;array_codigos&#125;&#125; , sobre los cuales este proceso especial de generación de encabezados operará . Esto aplica también para anuncios cuyo origen es a través de la Nueva WAPP (anuncios manuales) que se crean a través del servicio de creación de encabezados. _crear_dona_headers.php . 

 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona ?eatc-pod_id=&#123;&#123; array_codigos &#125;&#125; 

 Proceso similar al de creación tradicional pero con algunas diferencias 
&#160; 
 Las principales diferencias con el proceso de creación tradicional se basan en que estos anuncios deben tener una fecha límite de programación, dado que se deben recoger a más tardar dentro de la franja de días no hábiles, y también generarán un registro que permitirá desistir de su asignación mediante un botón que aparecerá en la App.&#160; El resto del proceso de generación de encabezado es igual al tradicional. Por otro lado este anuncio debe generar un proceso de match que lo haga disponible para todas las fundaciones que cumplan las reglas tradicionales de match (y no solo para las organizaciones que tienen asignación directa). 

 Funciones ***NUEVO CAMPO A AGREGAR A eatc_dona_headers**** 

 eatc_last_p_day (date en formato AAAA-MM-DD) 
&#160; 
 El sistema deberá calcular el último hábil del periodo no hábil.&#160; Por ejemplo si la fecha actual corresponde a un sábado de un fin de semana normal, la fecha que se registra será la del día siguiente.&#160; Si la fecha actual es un&#160; domingo&#160; de un fin de semana normal, la fecha será la del mismo domingo.&#160; (posteriormente cuando se implemente el tema de días festivos, esta fecha se deberá extender hasta el lunes correspondiente).&#160; Esta fecha se llevará a un nuevo campo (que deberá crearse en eatc_dona_headers con las diferentes precauciones y ajustes en otros procesos para que el sistema siga funcionando de manera adecuada). 
&#160; 
 eatc_dona_headers. eatc_last_p_day = &#123;&#123; date en formato AAAA-MM-DD &#125;&#125; 

 Constantes ***NUEVOS CAMPOS A AGREGAR A eatc_dona_headers**** 

 eatc_not_interested_btn (boleano) 
&#160; 
 Cuando se crea un anuncio con este proceso se debe ingresar un campo boleano afirmativo, para este nuevo campo (que deberá crearse en eatc_dona_headers con las diferentes precauciones y ajustes en otros procesos para que el sistema siga funcionando de manera adecuada) 
&#160; 
 eatc_dona_headers. eatc_not_interested_btn = y 

 eatc_with_last_p_day (boleano) 
&#160; 
 Cuando se crea un anuncio con este proceso se debe ingresar un campo boleano afirmativo, para este nuevo campo (que deberá crearse en eatc_dona_headers con las diferentes precauciones y ajustes en otros procesos para que el sistema siga funcionando de manera adecuada) 
&#160; 
 eatc_dona_headers. eatc_with_last_p_day = y 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 20b78fa6-4d06-4143-9512-1d0289835e39 
 3!1!2 
 https://eastus0-1.pushfp.svc.ms/fluid 
 507f3654-55aa-4526-b08c-4c7e0a8e2bac 
 2026-01-20T06:04:16.3903143Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"8be8c9a2-01fe-44e2-b630-073001a5a960","SequenceId":17,"FluidContainerCustomId":"54fdcb78-df3d-4f52-afb3-851b642acf04","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 EXCEPCIONES A DONACIONES CON ASIGNACIÓN DIRECTA: CREACIÓN DE ENCABEZADOS DE ANUNCIO DE DONACIÓN