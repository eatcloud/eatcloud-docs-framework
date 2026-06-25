# visualización-nps-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 FILTRO PRINCIPAL PARA LA VISUALIZACIN DE LAS ESTADSTICAS DE NPS 
 Para consultar el NPS se debe definir el periodo de tiempo de consulta de manera similar a esto, adicionando la opcin de definir fecha inicial y final (el valor por defecto ser &quot;ltimos 30 das&quot;. 

 VISUALIZACIN DE NPS 
 En principio se deber visualizar el promedio del dato NPS (&#123; &#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_nps_registry?nps=_ *) para el periodo seleccionado. 
&#160; 
 Entorno de pruebas&#58; https&#58;//dev.datagov.eatcloud.info//api/eatcloud/eatc_nps_registry?nps=_* &#160; 
&#160; 
 Entorno productivo&#58; https&#58;//datagov.eatcloud.info//api/eatcloud/eatc_nps_registry?nps=_* &#160;&#160; 

 CARD DE NPS 
 Para presentar el NPS, se utilizar una card que debe contener informacin&#58; 

 NPS 
 Se constituye en el distintivo principal del KPI&#160; 
&#160; 
 (?) Tooltip 
 Net Promoter Score 
&#160; 
 &#123;&#123;Valor del indicador&#125;&#125; (para el periodo seleccionado. En el ejemplo 146&#58; el NPS debe estar entre 0 y 10) 
 Es el valor del indicador NPS, promedio para el periodo seleccionado 

 &#123;&#123;Porcentaje de variacin&#125;&#125; en comparacin con el periodo anterior (-5.19 % en el ejemplo) 
 Corresponde a la diferencia entre el valor del NPS del periodo actual menos el valor del periodo anterior, sobre el valor del periodo anterior (por cien) 
&#160; 
 &#123;&#123;Grfico de tendencia&#125;&#125; 
 Muestra los valores da a da del indicador NPS (sus promedios da a da), y su promedio (en este&#160; caso ser un promedio de los promedios) en el periodo seleccionado. En este link se puede consultar una hoja de datos.&#160; Cundo se hace clic en un dato de una fecha especfica, sale un cuadro en dnde se ve la fecha, el valor del NPS (que en este caso ser el promedio para los datos del periodo) y su promedio (el promedio de los promedios da a da&#58; ver tercera imagen del carrusel) 

&#160; 
 &#123;&#123;Lneas de valor del KPI (no estn en la card de muestra)&#125;&#125; 
 Se debe mostrar en el grfico de tendencia una lnea en el valor &quot;6&quot; y otra en el valor &quot;9&quot; que muestren en el grfico las franjas de &quot;Detractor&quot;, &quot;Pasivo&quot;, &quot;Promotor&quot; 
&#160; 
 A futuro &#123;&#123;Presupuesto y ejecucin presupuestal&#125;&#125; 
 En un futuro se deber poder incorporar el dato del presupuesto para la mtrica en particular (presupuesto diario) y poderlo ver graficado en el grfico de tendencia&#160; (como se ve por ejemplo el grfico del promedio) y en el despliegue de datos se debe colocar el porcentaje de ejecucin presupuestal que se debe calcular como Valor del NPS / Presupuesto del NPS (para cada da) 

 GRFICO TORTA DE NPS_QUALIFICATION 
 Se debe mostrar en una torta el conteo de los valores &quot; detractor &quot;, &quot; pasivo &quot; y &quot; promotor &quot; ( eatc_nps_registry. nps_qualification ) para el periodo en cuestin con sus respectivos porcentajes de participacin 

 GRFICO BARRAS DE NPS POR PLATAFORMA (eatc_nps_registry. eatc_plataform ) 
 Se debe mostrar un grfico de barras, con los promedios del NPS ( eatc_nps_registry. nps ) para cada una de las plataformas (que se registran en eatc_nps_registry. eatc_plataform ) en el periodo en cuestin. 

 GRFICOS TORTAS DE NPS_QUALIFICATION POR PLATAFORMA (eatc_nps_registry. eatc_plataform ) 
 Se debe mostrar en una torta por plataforma (que se registran en eatc_nps_registry. eatc_plataform ) para el conteo de lo valores &quot; detractor &quot;, &quot; pasivo &quot; y &quot; promotor &quot; ( eatc_nps_registry. nps_qualification ) para el periodo en cuestin con sus respectivos porcentajes de participacin 

 FILTRO POR PLATAFORMA (eatc_nps_registry. eatc_plataform ) 
 Se debe mostrar (puede ser en una pgina aparte)&#160; un selector que permita seleccionar la plataforma (select distinct sobre&#58; eatc_nps_registry. eatc_plataform ) &#160; y al hacer dicha seleccin, mostrar la Card de NPS , para la plataforma seleccionada en el periodo seleccionado 

 FILTRO POR VERTICAL (eatc_nps_registry. eatc_vertical ) 
 Se debe mostrar (puede ser en una pgina aparte)&#160; un selector que permita seleccionar la vertical (select distinct sobre&#58; eatc_nps_registry. eatc_vertical ) &#160; y al hacer dicha seleccin, mostrar la Card de NPS , para la vertical seleccionada en el periodo seleccionado y tambin Grfico torta de nps_qualification respectivo 

 FILTRO POR TIPO DE LICENCIA (eatc_nps_registry. eatc_licence_type ) 
 Se debe mostrar (puede ser en una pgina aparte)&#160; un selector que permita seleccionar el tipo de licencia (select distinct sobre&#58; eatc_nps_registry. eatc_licence_type ) &#160; y al hacer dicha seleccin, mostrar la Card de NPS , para el tipo de licencia seleccionado en el periodo seleccionado y tambin Grfico torta de nps_qualification respectivo 

 FILTRO POR TAMAO (eatc_nps_registry. eatc_cua_size ) 
 Se debe mostrar (puede ser en una pgina aparte)&#160; un selector que permita seleccionar el tamao de la cuenta (select distinct sobre&#58; eatc_nps_registry. eatc_cua_size ) &#160; y al hacer dicha seleccin, mostrar la Card de NPS , para el tamao seleccionado en el periodo seleccionado y tambin Grfico torta de nps_qualification respectivo. 

 FILTRO POR CUENTA (eatc_nps_registry. eatc_cua ) 
 Se debe mostrar (puede ser en una pgina aparte)&#160; un selector que permita seleccionar la cuenta (select distinct sobre&#58; eatc_nps_registry. eatc_cua ) &#160; y al hacer dicha seleccin, mostrar la Card de NPS , para la cuenta seleccionada en el periodo seleccionado y tambin Grfico torta de nps_qualification respectivo. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fvisualizaci%C3%B3n-nps-datagov%2F109266760-EmbeddedImage---2024-07-30T130852.000.jpg&ow=361&oh=546, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fvisualizaci%C3%B3n-nps-datagov%2F109266760-EmbeddedImage---2024-07-30T130852.000.jpg&ow=361&oh=546 

 863.000000000000 

 VISUALIZACIN DE ESTADSTICAS DE NPS - DATAGOV