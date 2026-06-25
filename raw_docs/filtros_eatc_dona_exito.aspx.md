# filtros_eatc_dona_exito.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Para generar el proceso de Enriquecimiento del anuncio de donacin ( eatc_dona ) solo se debe trabajar con la informacin autorizada para el piloto, por este motivo se debe obviar informacin que no aplica.&#160; A continuacin algunas reglas al respecto 

Archivo de trabajo&#58; DEP_map_eatc_dona_exito.cfg 

 #nombre del archivo externo 
 name = 
 extension = txt 
&#160; 
 #vector de encabezados 
 headers_vector = Accion,Dependencia,Numdoc,CodMov3,FechaDocumento,Plu,Cantidad,Signo,TipoMarca,FechaHora,FechaIng,FechaUlAct,Causa,Destino,Costo,PreVta,Cedula,IdeConf,Sublinea,TipoNegociacion 

 Filtro Destino 
 Solo se deben traer informacin del destino 04 

 Filtro Sublnea 
 Dado que no se pueden entregar en donacin productos de &quot;electro digital&quot; se deben retirar aquellos productos que en el dato Sublinea tengan los siguientes registros&#58; 
&#160; 
 21 
 42 
 43 
 51 
 52 
 53 
 65 
 501 
 505 

 Consolidacin por codmov 
 Se evidencian 2 cdigos diferentes en la columna codmov3, el mov 14 representa la grabacin de averas y el movimiento 13 son ajustes a las averas, para obtener el dato real de las unidades a donar de un PLU en una fecha dada tendran que restarle a las unidades del movimiento 14 con destino 04 los ajustes del movimiento 13 con destino 04.&#160; Esto solo aplicara para el caso en que el almacn por error grabe una donacin y ese mismo da realice el ajuste, si este ltimo lo hiciera un da diferente no lograramos identificarlo sino hasta el momento en que la institucin llegue a recoger la mercanca, para este caso propondra pensar en una opcin de edicin manual del anuncio para el momento en que suceda que no cuadran las cifras del sistema con la donacin real. 
&#160; 
 [***NUEVO***] Incorporacin de los codmov3 200 y 201 
 Se incorporan 2 cdigos nuevos que viajan en la columna codmov3 y que traen los movimientos de los Centros de Distribucin, el mov 200 representa la grabacin de averas en los CEDIS y el movimiento 201 son ajustes a las averas, para obtener el dato real de las unidades a donar de un PLU en una fecha dada tendran que restarle a las unidades del movimiento 200 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 FILTROS_EATC_DONA_EXITO