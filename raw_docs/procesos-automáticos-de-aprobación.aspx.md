# procesos-automáticos-de-aprobación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 EVALUACIN DE PROCESOS AUTOMTICOS DE APROBACIN&#58; 
&#160; 
 El sistema debe evaluar por cuenta maestra, los datos cuales aprobaciones son automticas&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_cua_master=_DOM. cua_master &amp;eatc_approval_method= automatica 
&#160; 
 para disparar de manera&#160; automtica y peridica (puede ser a dos o tres cortes diarios) los procesos de evaluacin de prerequisitos correspondientes (los prerrequisitos se evalan realizando consultas al registro de aprobaciones eatc_certification_approval_registry ) para los certificados que no tengan una fecha de certificacin vlida (es decir, que aun estn pendientes de aprobacin). 
&#160; 
 Ejemplo _DOM. cua_master = abaco 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_cua_master=abaco&amp;eatc_approval_method= automatica &#160; 
&#160; 
 Con los datos obtenidos en los parmetros 
&#160; 
 eatc_certification_approval_flow. eatc_precedent_query 
 eatc_certification_approval_flow. eatc_precedent_query_response 
 eatc_certification_approval_flow. eatc_querys_operator 
 eatc_certification_approval_flow. eatc_precedent_query_b 
 eatc_certification_approval_flow. eatc_precedent_query_b_response 
&#160; 
 El sistema debe evaluar si se cumplen los prerrequisitos registrados para la aprobacin, y de ser as se deber disparar el proceso que se indica en el parmetro&#58; 
&#160; 
 eatc_certification_approval_flow. eatc_approval_trigger 

&#160; 
 Evaluacin para determinar los certificados sobre los cuales se deben realizar las evaluaciones 
 El sistema debe determinar los certificados cuya fecha y hora de certificacin sea 0000-00-00 00&#58;00&#58;00 con la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona_certifications ?eatc_certification_datetime= 0000-00-00%2000&#58;00&#58;00 
&#160; 
 Con los datos obtenidos del parmetro eatc_dona_certifications .eatc_code se realizarn las posteriores evaluaciones en el registro de aprobaciones ( eatc_certification_approval_registry ) para determinar si los certificados cumplen o no las condiciones para ser certificados. 

&#160; 
 Evaluacin del primer prerrequisito para mostrar la aprobacin 
 Con el (los) dato(s) que se recuperan de la consulta anterior, en los parmetros&#58; eatc_certification_approval_flow. eatc_precedent_query y el tipo de respuesta que se est esperando segn lo registrado en el parmetro eatc_certification_approval_flow. eatc_precedent_query_response se realiza la siguiente consulta y se evala su respuesta. 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_certification_approval_registry&#123;&#123; eatc_certification_approval_flow. eatc_precedent_query&#125;&#125; 
&#160; 
 Si la respuesta es como se espera (segn lo establecido en eatc_certification_approval_flow. eatc_precedent_query_response ) se debe revisar el dato que se obtiene en eatc_certification_approval_flow. eatc_querys_operator si no se obtiene dato, o se cumplen las siguientes condiciones, quiere decir que solamente con el primer Query, y su respuesta esperada, se cumple el prerrequisito para la aprobacin. 
&#160; 
 Las condiciones que se deben cumplir, as se tenga un dato en el operador y que indica que solo con la primera evaluacin vasta son las siguientes&#58; 
&#160; 
 El operador es &quot; y &quot; y la evaluacin del primer query no fue exitosa (la prueba lgica de ambos querys&#160; se puede descartar solo con el resultado de la evaluacin del primer query) 
 El operador es &quot; o &quot; y la evaluacin del primer query&#160; fue exitosa (la prueba lgica de ambos querys puede darse como exitosa solo con el resultado de la evaluacin del primero) 
&#160; 
 Ejemplo (ambiente de pruebas), _DOM .cua_master= abaco eatc_dona_certifications. eatc_code EC-00001-2021 (cdigo que no existe, pero para efectos de esta prueba sirve como ejemplo)&#58; 
&#160; 
 Prosiguiendo con el ejemplo anterior y dada la consulta 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_certification_approval_flow ?eatc_cua_master=abaco&amp;eatc_approval_method= automatica 
&#160; 
 se obtienen los siguientes datos&#58; 
&#160; 
 eatc_certification_approval_flow. eatc_precedent_query= ?eatc_code=&#123;&#123;eatc_dona_certifications.eatc_code&#125;&#125;&amp;eatc_approval_code=revisoria_fiscal 
&#160; 
 eatc_certification_approval_flow. eatc_precedent_query_response=valid 
&#160; 
 Como el dato eatc_certification_approval_flow .eatc_querys_operator = y 
&#160; 
&#160; 
 Entonces el sistema debe evaluar la siguiente consulta&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_certification_approval_registry ?eatc_code=&#123;&#123;eatc_dona_certifications.eatc_code&#125;&#125;&amp;eatc_approval_code=revisoria_fiscal 
&#160; 
 Y dado que eatc_dona_certifications.eatc_code= EC-00001-2021&#160; entonces la consulta debe ser&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_certification_approval_registry ?eatc_code= EC-00001-2021 &amp;eatc_approval_code=revisoria_fiscal &#160; 
&#160; 
 Como la respuesta es&#58;&#160; 
&#160; 
 &#123; 
 ts &#58; &quot;210222093736&quot;, 
 op &#58; true, 
 cont &#58; 0, 
 err_msg &#58; &quot;No se produjeron resultados&quot;, 
 err_num &#58; &quot;&quot;, 
 mem &#58; 0.39, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 Es decir una respuesta invlida, y el valor de&#160; 
 eatc_certification_approval_flow. eatc_precedent_query_response= valid , quiere decir que la condicin para aprobar no se cumple. 
&#160; 
 Como el parmetro eatc_certification_approval_flow .eatc_querys_operator es &quot; y &quot; y la evaluacin del primer query no fue exitosa (la prueba lgica de ambos querys&#160; se puede descartar solo con el resultado de la evaluacin del primer query) 

&#160; 
 Evaluacin del segundo prerrequisito para mostrar el botn de la accin &quot;aprobar&quot; 
&#160; 
 Si se obtiene en eatc_certification_approval_flow. eatc_querys_operator un dato, quiere decir que es necesario, en algunos casos) evaluar el eatc_certification_approval_flow. eatc_precedent_query_b &#160; para establecer si se cumplen las condiciones para la aparicin del botn de accin.&#160; Los casos son los siguientes&#58; 
&#160; 
 El operador es &quot; y &quot; y la evaluacin del primer query fue exitosa 
 El operador es &quot; o &quot; y la evaluacin del primer query no fue exitosa 
&#160; 
 En estos dos casos se procede a realizar&#160; la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_certification_approval_registry&#123;&#123; eatc_certification_approval_flow. eatc_precedent_query_b&#125;&#125; 
&#160; 
 y de acuerdo al dato eatc_certification_approval_flow. eatc_precedent_query_b_response se evalua la respuesta (para establecer si la prueba es exitosa o no exitosa). Con el resultado del segundo trmino y el operador lgico se establece si el botn de accin &quot;aprobar&quot; se muestra o no, de la siguiente manera. 
&#160; 
 El operador es &quot; y &quot; la evaluacin del primer query fue exitosa y la evaluacin del segundo query tambin&#58; se muestra el botn de accin &quot;aprobar&quot;. 
 El operador es &quot; o &quot;, la evaluacin del primer query no fue exitosa y y la evaluacin del segundo query fue exitosa&#58; se muestra el botn de accin &quot;aprobar&quot; 

&#160; 
 Disparador de aprobacin 
 Con el dato que se obtiene en el parmetro&#58; eatc_certification_approval_flow. eatc_approval_trigger se dispara el proceso indicado para terminar el proceso automtico de aprobacin. 
&#160; 
 Para el caso del ejemplo que hemos venido tratando y suponiendo que las precondiciones de aprobacin han sido cumplidas ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_certification_approval_flow?eatc_cua_master=abaco&amp;eatc_approval_method=automatica )&#160; el llamado que debe hacerse cuando se realice la aprobacin automtica es&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/aprv_cert/&#123;&#123;_DOM.cua_master&#125;&#125;/eatc_dona_certification_code=&#123;&#123;eatc_dona_certification_code&#125;&#125; 
&#160; 
 Que para el ejemplo sera 
&#160; 
 https&#58;//devdonantes/aprv_cert/abaco/eatc_dona_certification_code= EC-00001-2021 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESOS AUTOMTICOS DE APROBACIN