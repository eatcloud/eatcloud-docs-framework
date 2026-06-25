# donación-de-tiempo.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Si el usuario no est registrado se le debe desplegar el formulario de registro de usuario , y posteriormente un formulario (que guarda en la estructura eatc_volunteers ) que permita la captura de la siguiente informacin (toda de manera obligatoria)&#58; 
&#160; 
 Datos necesarios para la donacin de tiempo 
 lugar_voluntariado&#58;&#160; 
 Los lugares de voluntariado se pueden consultar con el API respectiva (parmetro&#58; eatc_name)&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods?eatc-name=_* (se puede por ejemplo realizar primero un selector por &quot;cuidad ( select distinct a los datos del parmetro eatc-city ) y posteriormente desplegar un selector de los puntos disponibles en la ciudad. 
&#160; 
 Ejemplo&#58; 
 El usuario selecciona la ciudad de &quot;Medelln&quot;, entonces le aparecen las siguientes opciones para seleccionar ( eatc-name ) 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods?eatc-city=medellin 
&#160; 
Jumbo Premium Plaza 
XITO ROBLEDO 
EXITO ITAGUI 
MAKRO SAN JUAN 
MAKRO ESTACIN POBLADO 
&#160; 
 (Con datos subidos el 17 de septiembre) 
&#160; 
 La informacin capturada se almacena en el campo &quot; lugar_voluntariado &quot; de &quot; eatc_volunteers &quot; 

&#160; 
 dias&#58;&#160; 
 Selector mltiple de los das de la semana, segn&#160; los das el punto de voluntariado (eatc_pods) seleccionado. Tipo de dato&#58; string. 
&#160; 
 Ejemplo&#58; 
 El usuario seleccion el punto de donacin &quot; Jumbo Premium Plaza &quot; (cuyo eatc-id = 301 ) las nicas opciones de das disponibles sern&#58; los das viernes , sbado ( dias &#58; &quot;vi,sa&quot;) ya que en el campo das de dicho punto de donacin, solo estn estas dos posibilidades. 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods?eatc-id=301 &#160; 
&#160; 
 La informacin capturada se almacena en el campo &quot; dias &quot; de &quot; eatc_volunteers &quot; 

&#160; 
 horario_inicio&#58;&#160; 
 Debe ser consistente con el horario inicio del punto de donacin seleccionado, es decir, el selector no puede colocar horas de inicio por fuera del rango que representan los datos horario_inicio y horario_final 
&#160; 
 Ejemplo&#58; 
 Si el usuario seleccion el punto de donacin &quot;Jumbo Premium Plaza&quot; (cuyo eatc-id =301) la hora de inicio debe estar entre las 09&#58;00&#58;00 y las 21&#58;00&#58;00 horas 

 horario_fin (OJO QUE NO EST EN EL DISEO y hay que colocarlo)&#58;&#160; 
&#160; 
 Debe ser una hora superior a la del anterior selector y debe ser consistente con el horario inicio del punto de donacin seleccionado, es decir, el selector no puede colocar horas de inicio por fuera del rango que representan los datos horario_inicio y horario_final. 
&#160; 
 Ejemplo&#58; 
 Si el usuario seleccion el punto de donacin &quot;EXITO IBAGUE&quot; (cuyo eatc-id =39) la hora de inicio debe ser mayor al horario de_inicio anteriormente fijado estar entre las 09&#58;00&#58;00 y las 21&#58;00&#58;00 horas 
&#160; 
 La informacin capturada ( hora_inicio y hora_fin ) se almacena en el campo &quot; horario &quot; de &quot; eatc_volunteers &quot; 
&#160; 
 Registro de los datos en la estructura de voluntarios (eatc_volunteers)&#160; 
 Escritura con la API&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_volunteers &amp;_operacion=update&amp; lugar_voluntariado= [VALOR] &amp;dias= [VALOR] &amp;horario_inicio= [VALOR] &amp;horario_fin= [VALOR]&amp;WHEREnumero_documento=[VALOR] 
&#160; 
 Ejemplo&#58; 
&#160; 
 El voluntario Jorge Correa (numero_documento=71773955) utilizando el formulario escribi la siguiente informacin 
&#160; 
 lugar_voluntariado&#58; Jumbo Premium Plaza 
 das&#58; viernes,sbado 
 horario_inicio&#58; 10&#58;00&#58;00&#160; 
 horario_fin&#58; 15&#58;00&#58;00 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla= eatc_volunteers &amp;_operacion=update&amp; lugar_voluntariado= Jumbo%20Premium%20Plaza &amp;dias= viernes,sbado &amp;horario_inicio=10&#58; 00&#58;00 &amp;horario_fin= 15&#58;00&#58;00&amp; WHEREnumero_documento =71773955 &#160;&#160; 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924172837&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.73, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 Los datos registrados se pueden consultar en&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_volunteers?numero_documento=71773955 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonaci%C3%B3n-de-tiempo%2F2318810%20voluntarios%20%20%28eatc_alim_vol%29%20%281%29.png&ow=750&oh=3018, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdonaci%C3%B3n-de-tiempo%2F2318810%20voluntarios%20%20%28eatc_alim_vol%29%20%281%29.png&ow=750&oh=3018 
 App usuario final - Alimentatn 

 764.000000000000 

 DONACIN DE TIEMPO (EATC_ALIM_VOL)