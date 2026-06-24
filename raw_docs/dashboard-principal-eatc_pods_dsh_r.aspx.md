# dashboard-principal-eatc_pods_dsh_r.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripcin general 

 Anuncio flotante: Anuncio de donacin adjudicado (OJO QUE NO EST EN EL DISEO) 
 Alerta flotante (Puede ser similar a la card de anuncio de donacin que se implementa en la funcionalidad " seguimiento de anuncio de donacin ")   cada vez que una de las donaciones cambie su estado anunciado a adjudicado. 
 el sistema toma el parmetro " eatc-id " del punto de donacin ( eatc_pods ) respectivo: 
 Ejemplo: 
 El usuario "EXITO COLOMBIA", cuyo " eatc-id " = 31 

 Ambiente de pruebas: https://donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31 

 Trama comprimida: https://donantes.eatcloud.info/api/devexito/eatc_pods?eatc-id=31&_compress   

 Ambiente productivo: https://donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31   

 Trama comprimida: https://donantes.eatcloud.info/api/exito/eatc_pods?eatc-id=31&_compress    
 Con este parmetro se va al API de encabezados de anuncio de donacin ( eatc_dona_headers ) y en el parmetro " eatc-pod_id ", se enva el dato obtenido previamente (organizacion). 
 Ejemplo: 
 El usuario "EXITO COLOMBIA", cuyo " eatc-id ""= 31 , se realiza la siguiente consulta enviando dicho dato al parmetro eatc-pod_id (teniendo en cuenta solamente el estado "awarded" (eatc-state=awarded) a fin de no sobrecargar la consulta: 

 Ambiente productivo: 
 https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&eatc-state=awarded   

 Trama comprimida: https://donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-pod_id=31&eatc-state=awarded   

 La informacin obtenida se presenta en cards de la siguiente manera: 

 Fecha y hora del anuncio: 
   eatc_dona_headers .eatc-publication_datetime 

 Datos del gestor de donaciones ( eatc_donation_manager ) al cual se le adjudic el anuncio 
 Nombre: eatc_dona_headers .eatc-donation_manager_name 
 Direccin: eatc_dona_headers .eatc-donation_manager_address 
 Telfono: eatc_dona_headers .eatc-donation_manager_address 
 Total de kilos que contiene el anuncio 
 eatc_dona_headers .eatc-total_weight_kg 
 Botn + 
 Este botn dar la entrada a la funcionalidad " dashboard de anuncio de donacin (eatc_dona_dsh) " 
 Card Tus mtricas: 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el mes en curso 
 Muestra los kilogramos donados por el punto de donacin ( eatc_pods ) en el ao en curso 
 #KPI de impacto social 
 kg = eatc_dona_headers .eatc-total_weight_kg 
 Indicadores Clave: 
 Mediante tres pestaas presenta los principales indicadores por tipo de indicador, y el botn (+) que da acceso a la funcionalidad: detalle de KPI . Las pestaas son las siguientes: 
 Impacto Social 
 Muestra el total de kilogramos donados por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
 #KPI KG: Regla de clculo 
 kg = eatc_dona_headers .eatc-total_weight_kg. 

 Para realizar el clculo se debe invocar el API: https://donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=kg&eatc-pod_id=[id ] 

 Ejemplo: 
 Para el punto de donacin "", cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 https://donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=kg&eatc-pod_id= [valor] . Luego se realiza una sumatoria del campo "Value" y esta ser el resultado 

 Otros indicadores de impacto social: 
 Impacto social: total de donaciones en KG 
 [PENDIENTE ESTIMAR] Impacto social: total de raciones 
 Impacto social: total poblacin beneficiaria 
 Impacto social: Subtotal poblacin beneficiaria por segmento ( PRIMERA INFANCIA, INFANCIA, ADOLESCENTES, ADULTO, ADULTO MAYOR, MUJERES GESTANTES, FAMILIAS) 
 Impacto econmico: 
 muestra el total de dinero ahorrado por cuenta de las donaciones por parte del punto de donacin ( eatc_pods ), es decir la sumatoria de todos los ahorros y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ) 
 #KPI de impacto econmico: Reglas de clculo 

 Para realizar el clculo se debe invocar el API: https://donantes.eatcloud.info/api/exito/eatc_dona_kpi?eatc-kpi_type=Economic impact&eatc-pod_id=[id] 

 Ejemplo: 
 Para el punto de donacin "", cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 ?eatc-kpi_type=Economic impact&eatc-pod_id = [valor] . Luego se realiza una sumatoria del campo "Value" y esta ser el resultado 

 Otros indicadores de impacto econmico: 
 Impacto econmico: Total ahorro de costos logsticos 
 Impacto econmico: subtotal ahorro de costos de almacenamiento 
 Impacto econmico: subtotal ahorro de costos de trasporte 
 Impacto econmico: subtotal ahorro de costos de gestin de residuos 
 [PENDIENTE ESTIMAR] Impacto econmico: valor en $ de certificados de donacin adjudicados y beneficios tributarios 
 Impacto ambiental:  
 Muestra el total de las emisiones de C02 en toneladas ahorradas por el punto de donacin ( eatc_pods ) y un vnculo a la funcionalidad de detalle de KPI ( eatc_pods_kpi ). 
 #KPI C02_tons: regla de clculo 
 CO2_tons = eatc_dona_headers .eatc-total_weight_kg*(0,023/1000) 

 Para realizar el clculo se debe invocar el API: https://donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=CO2_tons&eatc-pod_id=[id] 

 Ejemplo: 
 Para el punto de donacin "", cuyo eatc-id = [valor] , la consulta para traer los datos del KPI sera 
 https://donantes.eatcloud.info/api/exito/eatc_dona_kpi?kpi=CO2_tons&eatc-pod_id= [valor] . Luego se realiza una sumatoria del campo "Value" y esta ser el resultado 

 Otros indicadores de impacto medioambiental: 
 Impacto medioambiental: toneladas de CO2 
 [STANDBY] Impacto medioambiental: huella de carbono 
 [STANDBY] Impacto medioambiental: huella hdrica 

 Leader Board 
 El dashboard presentar un "Leader Board" o "Tablero de Liderazgo" en donde se presentarn, mediante pestaas, los tres primeros Almacenes ( eatc_pods ) por kilos donados del 1 de enero a la fecha del ao en curso y por $ donados de del 1 de enero a la fecha del ao en curso 

 Botones de accin 
 Desde el dashboard se podr ingresar a los siguientes botones: 
 Seguimiento de anuncios: el globo de notificacin presenta los anuncios de donacin ( eatc_dona_headers ) cuyo estado es "anunciado", es decir, que estn pendientes de ser adjudicados y presenta un vnculo a la funcionalidad " seguimiento de anuncios " 
 Entrega de donacin : presenta los anuncios de donacin ( eatc_dona_headers ) cuyo estado es "programado". Este listado es similar a " seguimiento de anuncios de donaciones ", pero debe presentar un acceso directo para cada anuncio a la funcionalidad " entrega de donacin " (en vez que el "+" dirija al dashboard del anuncio de donacin debe dirigir directamente a la " entrega de donacin " ). 
 Anuncio de donacin : para el piloto del xito este botn puede estar deshabilitado. Debe presentar un acceso a la funcionalidad " Creacin de anuncio de donacin ". 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal-eatc_pods_dsh_r%2F913033.1%2520dashboard%2520de%2520donante%2520%28eatc_pods_dsh_r%29.png, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-principal-eatc_pods_dsh_r%2F913033.1%2520dashboard%2520de%2520donante%2520%28eatc_pods_dsh_r%29.png 
 EatCloud Donantes Desktop 

 73.0000000000000 

 DASHBOARD PRINCIPAL: EATC_PODS_DSH_R