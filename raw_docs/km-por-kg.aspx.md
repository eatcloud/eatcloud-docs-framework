# km-por-kg.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Con el nimo de dinamizar el match con respecto a los KM ms adecuados para su realizacin (y empezar a incorporar algunos procesos estadsticos para la optimizacin de la plataforma), se va a empezar a calcular los KM recorridos para cada donacin en comparacin con sus KG, para intentar encontrar alguna distribucin estadstica que nos permita saber, dados los KG de una donacin, cual es su radio optimo en KM para obtener un match lo ms preciso posible. 
&#160; 
 Clculo y persistencia de datos necesarios para el clculo 
 Distancia entre el punto de donacin y el gestor de donaciones 
 Para realizar los clculos se debe programar un proceso de base de datos que calcule el dato de los KM entre el punto de donacin (eatc_pod.(eatc-lat,eatc-lon)) y las coordenadas del donante (eatc_donation_manager.(eatc-lat,eatc-lon). Este dato debe llevarse al eatc_dona_headers como eatc_dona_distance. 
&#160; 
 Puede ser un proceso que corra peridicamente por las noches, o tambin puede hacerse un ajuste en la generacin del eatc_dona_headers para incorporar ese dato de una vez (se deja a criterio del desarrollador la seleccin de la opcin, buscando eficiencia en el proceso). 
&#160; 
 Clculo de KM por KG 
 Se toma el dato calculado en el punto anterior eatc_dona_headers.eatc_dona_distance y se divide por eatc_dona_headers. eatc-original_weight_kg &#160; para establecer, para el anuncio en cuestin, cuantos Kilmetros estuvo dispuesto a recorrer el gestor de donaciones por KG anunciado (originalmente). Por ejemplo, si para un anuncio de 20 que se encontraba a 10 KM del gestor de donaciones, se puede establecer que el gestor estuvo dispuesto a recorrer 0,5 KM por cada KG donado (10KM/20KG). 

&#160; 
 Establecimiento de la distribucin estadstica del dato de KM por KG 
&#160; 
 Se debe establecer un proceso para evaluar la distribucin estadstica ms adecuada de esta informacin, que puede darse por varios factores&#58; 
&#160; 
 Da de la semana 
 Hora del da 
 Da del mes 
 Ciudad 
 Punto de donacin (ubicacin) 
 Distribucin directa (por ejemplo establecer si se puede encontrar una campana o distribucin normal solamente relacionada con el dato obtenido como tal) 
 .... 
&#160; 
 Esto con el nimo de establecer segn que tipo de dato asociado se puede encontrar una distribucin estadstica ms nutrida (con desviacin estndar menor), y as poder guardar en un repositorio (que se debe ir ajustando con el tiempo), el dato de los KM por KG&#160; ms adecuados, segn algn criterio, y a partir del mismo, tener ese dato para calcular un radio optimo (eatc_dona_header.eatc_dona_optimal_radius) para establecer el match por KM, para garantizar de alguna manera que el anuncio sea estadsticamente atractivo para las organizaciones que estn a su alrededor ms prximo. 
&#160; 
 Este dato se deber utilizar, si es mayor al valor por defecto de radio en KM para el match (que a 14 de mayo de 2020 es de 20 KM) y se debe mostrar en el informe del BO de beneficiarios ( Informe de donaciones ) para sugerirlo como radio optimo para hacer un match. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CLCULO DE KM POR KG