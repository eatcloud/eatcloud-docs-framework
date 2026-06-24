# dashboard-de-anuncio-de-donacion-eatc_dona_dsh_r.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 
 En esta vista se mostrarn los detalles del beneficiario al cual fue asignada la donacin (con su scoring) y los accesos necesarios para registrar la llegada, la salida y la calificacin del gestor de donaciones o beneficiario que recoge.  Adems presenta el detalle de lo que es donado y un mapa para realizarle seguimiento al proceso de recogida y custodia. 

 Detalle de anuncio de donacin: encabezado 
 Este apartado solo se habilita para anuncios de donacin cuyo estado eatc_dona_states ) sea "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado), "received" (recibido), "pre-certified" (pre-certificado) y "certified" (certificado) . Los anuncios con estado " announced" (anunciado) , NO muestran esta informacin. 

 Consulta de anuncios 
 El sistema toma el parmetro " eatc-id " del encabezado de anuncio de donacin ( eatc_dona_headers ) seleccionado desde el listado donde se invoca esta vista ( seguimiento de anuncios de donacin: botn + ) y con l se invoca el respectivo API 

 Ejemplo: 
 El para el anuncio cuyo " eatc-id " = 8687012  

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012   

 Trama comprimida:  https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&_compress   

 Con la respuesta del API se toma la siguiente informacin del gestor de donaciones al que se le adjudic el anuncio: 
 Foto (PENDIENTE POR DEFINIR) 
 Nombre: eatc-donation_manager_name 
 Direccin : eatc-donation_manager_address 
 Telfono : eatc-donation_manager_phone 

 Score : eatc-donation_manager_score 

 Mapa del anuncio de donacin: seguimiento 
 El mapa muestra la coordenada del anuncio pintada en el mapa (eatc_lat, eatc_lon). 

 En trminos generales deber funcionar as: 
 publicado y adjudicado, muestra las coordenadas del almacn;  
 en el estado adjudicado, tambin el seguimiento (geobeneficiario) que hace la App del beneficiario u Operador logstico,  
 en estado entregado la coordenada del almacn y el seguimiento de la App del beneficiario (geobeneficiario) y el operador logstico, 

 en recibido, verificado y certificado la coordenada del beneficiario. 

 Contenido del anuncio 
 Este apartado muestra el detalle de anuncio de donacin (eatc_dona) mediante una consulta al API se debe traer informacin de los productos donados que componen el anuncio y listarlos dentro de un colapsible de la siguiente manera: 

 Consulta de detalles de anuncio de donacin (eatc_dona) 
 El sistema toma el parmetro " eatc-code " del encabezado de anuncio de donacin ( eatc_dona_headers ) y con l se invoca el API de detalles de anuncio de donacin ( eatc_dona ) , enviando ese valor en el parmetro eatc-dona_header_code 
 Ejemplo: 
 El para el anuncio cuyo " eatc-code " = 40716 ( anuncio cuyo " eatc-id " = 7608059 ) (Carulla Palmas: user : 339; password : (4) 6050294) 

 Ambiente productivo: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716      
 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona? eatc-dona_header_code = 40716&_compress   

 Con la respuesta del API se toma la siguiente informacin del gestor de donaciones al que se le adjudic el anuncio: 
 Item: eatc-odd_name 
 Fecha y hora : eatc-date_time 
 Texto secundario : eatc-odd_typology_a 

 Peso en KG : eatc-odd_total_weight_kg 

 Botones de accin 
 Este apartado solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea "awarded" (adjudicado) , "scheduled" (programado), "delivered" (entregado), "received" (recibido), "pre-certified" (pre-certificado) y "certified" (certificado) . Los anuncios con estado " announced" (anunciado) , NO muestran estos botones. 

 Botn: registro de llegada de beneficiario: 
 Solo se solo se habilita para anuncios de donacin cuyo estado ( eatc_dona_states ) sea "awarded" (adjudicado) , "scheduled" (programado) . 
 El botn da acceso a la funcionalidad " entrega de donacin: hora de llegada ". 

 Botn: registro de salida de beneficiario: 
 Solo se solo se habilita para anuncios de donacin ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkin_datetime" . 
 El botn da acceso a la funcionalidad " entrega de donacin: hora de salida ". 

 Botn: califica al beneficiario (OJO QUE DIFIERE A LO PROPUESTO EN EL MOCKUP): 
 Solo se solo se habilita para anuncios de donacin ( eatc_dona_headers ) que tengan registrado un dato en el campo "eatc-picking_checkout_datetime" .  Una vez se acciona y se genera la calificacin el botn debe desaparecer . 
 El botn da acceso a la funcionalidad " entrega de donacin: calificacin beneficiario ". 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-anuncio-de-donacion-eatc_dona_dsh_r%2F2930296227-6.1-detalle-anuncio--eatc_dona_dsh_r-.png&ow=1280&oh=1179, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-de-anuncio-de-donacion-eatc_dona_dsh_r%2F2930296227-6.1-detalle-anuncio--eatc_dona_dsh_r-.png&ow=1280&oh=1179 
 EATCLOUD DONANTES DESKTOP 

 92.0000000000000 

 DASHBOARD DE ANUNCIO DE DONACIN (EATC_DONA_DSH)