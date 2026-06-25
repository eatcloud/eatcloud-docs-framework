# dashboard-principal-elección-de-punto-de-donación-alimentatón.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mapa&#58; 
 Muestra la ubicacin del dispositivo 

&#160; 
 Card&#58; Raciones donandas en el pas 
 Realizando una consulta al API respectiva ( https&#58;//donantes.eatcloud.info/api/abaco/raciones_acumuladas_alimentaton?dia=_* ), se trae el nmero de raciones acumuladas a la fecha para el da actual (enviado al API en formato AAAA-MM-DD) 

&#160; 
 Ejemplo&#58; 
 Un usuario ingresa a la App el da 15 de octubre (2019-10-15), la consulta a la API sera&#58; 
 &#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/raciones_acumuladas_alimentaton?dia=2019-10-15 &#160; 
&#160; 
 por lo tanto el dato a mostrar en la card sera &quot;1000&quot; (correspondiente al parmetro&#58; &quot;raciones_acumuladas_alimentaton&quot; ) 
&#160; 
 Carrusel de puntos de donacin cercanos 
 Tomando los datos de los puntos de donacin cercanos que se establecieron en la funcionalidad &quot; Bienvenida&#58; puntos de donacin cercanos &quot;. se muestran en un carrusel los diferentes puntos disponibles en las cercanas del dispositivo. 
 Ejemplo&#58; 
 Se determin que los puntos a menos de 9 KM del dispositivo son MAKRO ESTACIN POBLADO (eatc-id=217) y MAKRO SAN JUAN (eatc-id=205) , por lo tanto en el carrusel se debe mostrar informacin correspondiente a la siguiente consulta&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/abaco/eatc_pods?eatc-id=207,215 
&#160; 
 La informacin que se muestra por almacn es la siguiente&#58; 
 Fotografa &#58; PENDIENTE DE DEFINIR 
 Direccin &#58; corresponde al parmetro &quot;eatc-adress&quot; 
 Horario &#58; corresponde a los parmetros &quot;dias&quot;, &quot;horario_inicio&quot;, &quot;horario_final&quot; . 
&#160; 
 Botn&#58; Qu alimentos puedes donar? 
 Da ingreso a la funcionalidad &quot; Consulta de productos para donacin en especie &quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=1e937bad48584aa3ae14dbcbe8711080&ext=png&ow=750&oh=2156, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=1e937bad48584aa3ae14dbcbe8711080&ext=png&ow=750&oh=2156 
 App usuario final - Alimentatn 

 748.000000000000 

 DASHBOARD PRINCIPAL - ELECCIN DE PUNTO DE DONACIN - ALIMENTATN (EATC_ALIM_DASH)