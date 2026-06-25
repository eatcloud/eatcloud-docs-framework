# peticiones-quejas-y-reclamos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Funcionalidad para registrar peticiones, quejas y reclamos con respecto a un anuncio de donacin, permitiendo incorporar texto y fotografa.&#160; Para la implementacin se puede reutilizar parte del cdigo utilizado para el registro de rechazos en la funcionalidad de Verificacin detallada de auncios de Donacin 

 Encabezado 
 Se coloca el siguiente texto introductorio a la funcionalidad 
&#160; 
 Peticiones, quejas y reclamos 
 Si tienes una peticin, queja o reclamo con respecto al anuncio de donacin entregado, por favor djanos tus comentarios y si lo deseas fotografas para sustentar su comunicacin. Estaremos revisando la informacin para darte una pronta respuesta. 
&#160; 
 Formulario de peticin, queja o reclamo 
&#160; 
 Selector tipo&#58; 
&#160; 
 Se muestra un selector para definir si se est registrando una 
&#160; 
Peticin 
Queja 
Reclamo 
&#160; 
 Es informacin obligatoria 
&#160; 
 Text Area&#58; 
 Se presenta un rea de texto para que el usuario digite el cuerpo de la peticin queja o reclamo.&#160; Es informacin obligatoria 
&#160; 
 Fotografas 
 La App permitir tomar hasta tres fotografas (de manera opcional) para sustentar la peticin, queja o reclamo 
&#160; 
 Registro de la PQR 
 La App realizar un registro en la estructura definida para tal fin (Ambiente de pruebas&#58; eatc_dona_pqrs_registry ) y el encabezado de anuncio de donacin (eatc_dona_headers). 

&#160; 
 Escritura en eatc_dona_pqrs_registry con la API&#58;&#160; 
 AMBIENTE DE PRUEBAS 
 https&#58;//devdonantes.eatcloud.info/crd/exito/?_tabla=eatc_dona_pqrs_registry&amp;_operacion=insert&amp;date_time= [DATETIME]&amp; eatc-donation_manager_code=[VALOR]&amp;eatc-donation_manager_user_doc_id=[VALOR]&amp;eatc_donor_code=[VALOR]&amp;eatc-dona_header_code=[VALOR]&amp;eatc-pod_id=[VALOR]&amp;eatc-pqr_type=[VALOR]&amp;eatc-pqr_description=[DESC]&amp;eatc-pqr_evidence1=[FOTO]&amp;eatc-pqr_evidence2=[FOTO]&amp;eatc-pqr_evidence3=[FOTO] 
&#160; 
 Ejemplo (de la vida real)&#58; 
&#160; 
 Para el anuncio de donacin cuyo eatc-code = 00001912070729 , El usuario El usuario Karla Gutierrez (numero_cedula = 1037608308) ; que tiene como organizacin a la Fundacin San Nicols&#58; 901096189-3 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_donation_managers?identificador_unico_registro=901096189-3 ) Nos entreg la siguiente queja&#58; 
&#160; 
 &quot;La experiencia que tuvimos hoy en la entrega de donacin en Carulla Laureles no fue tan agradable. Inicialmente nos manifestaron que la entrega deba ser despus de las 11&#58;00 am. Solucionado ese inconveniente, las personas encargadas del despacho a nuestro sentir no fueron los ms cordiales a la hora del despacho, se tornaron un poco dspotas con la persona encargada de recoger la donacin. 
 Por otro lado de los alimentos ofertados, no haban ni la mitad y los que llegaron, evidentemente se encontraron en mal estado&#58; olan muy maluco y toda, toda la parva se encontraba en descomposicin con hongos visibles. Adicional a eso, en el lugar de entrega no se suministro hoja de verificacin de productos como siempre lo hacen los colaboradores del xito. 
 Adjunto registro fotogrfico&quot; (en adelante DESC) 
&#160; 
&#160; 
&#160; 
 A las 12&#58;11&#58;00 del da 2019-12-10. 

 Hipotticamente el usuario debi llenar estos datos en el formulario, seleccionando una queja y adjuntando tres archivos fotogrficos 
&#160; 
 Dado que se tienen los siguientes datos (nota se simulan URLs utilizando G-Drive, pero la idea es que esto se guarde en una carpeta en el servidor de donantes cuenta xito )&#58; 
&#160; 
 date_time&#58; 2019-12-10 12&#58;11&#58;00&#160; 
 eatc-donation_manager_code= 901096189-3 (que corresponde a eatc_donation_managers. identificador_unico_registro ) 
 eatc-donation_manager_user_doc_id= 1037608308 (que corresponde a numero_cedula ) 
 eatc_donor_code= 890.900.608-9 (que corresponde a eatc_dona. eatc_donor_code) 
 eatc-dona_header_code= 00001912070729 (que corresponde a eatc_dona. eatc-dona_header_code) 
 eatc-pod_id= 729 (que corresponde a eatc_dona. eatc-pod_id) 
 eatc-pqr_type= queja 
 eatc-pqr_description =[DESC] 
 eatc-pqr_evidence1 = https&#58;//drive.google.com/open?id=1aJP_9_Hm_i-9KcBWhGdNS5rbpfd4MxGE corresponde a la URL del recurso (fotografa) de evidencia que se guarda en el servidor 
 eatc-pqr_evidence2 =corresponde a la URL del recurso (fotografa) de evidencia que se guarda en el servidor 
 eatc-pqr_evidence3 = corresponde a la URL del recurso (fotografa) de evidencia que se guarda en el servidor 
&#160; 
 Utilizando el API (Mtodo POST) se debe realizar el registro (para efectos ilustrativos se utiliz el cargador para guardar el registro) 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtengan respuestas de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924182418&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 last &#58; 4, 
 mem &#58; 0.75, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logran obtener estas respuestas, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 
&#160; 
 El registro se puede consultar aqu&#58; https&#58;//donantes.eatcloud.info/api/exito/eatc_dona_pqrs_registry?eatc-dona_header_code=1912070729 &#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 PETICIONES, QUEJAS Y RECLAMOS (EATC_DONA_PQRS)