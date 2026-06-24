# dashboard-datagov-bo.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 En este dashboard, cuando se ingrese a la cuenta general es decir a la cuenta EatCloud: 

 https://datagov.eatcloud.info/bo 

 Se debe mostrar un dashboard que presente la jerarqua de Mtricas propias de EatCloud.  Esta jerarqua, que se muestra en el siguiente grfico, debe quedar de alguna manera expresada en el dashboard: 

 FILTRO PRINCIPAL PARA LA VISUALIZACIN DE KPIS 
 Para consultar los KPIs se debe definir el periodo de tiempo de consulta de manera similar a esto, adicionando la opcin de definir fecha inicial y final: 

 VISUALIZACIN DE KPIS 
 En el BO raiz, se debe permitir visualizar todos los KPIs que se definen a continuacin, es decir en https://datagov.eatcloud.info/bo/ .  Pero los mismos debern poderse perfilar o asociar (en la funcionalidad de administrador de funcionalidades que es similar a esta: https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/configuracin-web-app-donantes.aspx pero funcionando con los criterios abajo descritos), a uno de los siguientes criterios de perfilacin: 

 eatc_country: inicialmente ser Colombia pero luego podrn ir creciendo: https://beneficiarios.eatcloud.info/api/data/eatc_countries?_id=_ *  (esta informacin debera estar en  https://datagov.eatcoud.info/api/data/eatc_countries?_id=_*) 
 eatc_cua.vertical: informacin asociada a la CUA: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&vertical=_todos   y cuyo maestro es este: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&nombre=_todos   
 eatc_cua.type: informacin asociada a la CUA: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&type=_todos (free,hero) 

 En etapas posteriores se podrn incorporar criterios adicionales de perfilamiento como: 
 eatc_province (en una segunda etapa) 
 eatc_city (en una segunda etapa) 
 eatc_cua 

 NOTA de mejoramiento futuro: 

 En algn punto se debera poder migrar toda la informacin de cuentas al entorno https://datagov.eatcloud.info/api/eatc_cua y a travs de esta plataforma tener un administrador para poder crear los clientes y las cuentas) 

 CONSULTA DE DATOS PARA LA OBTENCIN DE KPIS 
 En principio los datos, segn sus caractersticas, se estn tomando de entornos de donante y beneficiario y de cuentas maestras: 

 https://donantes.eatcloud.info/api/abaco/ ... 
 https://beneficiarios.eatcloud.info/api/abaco /... 

 Pero en un futuro las cuentas maestras podrn cambiar segn el pas, y la idea primordial de esta plataforma es que centralizar todos los datos de eatcloud, por lo tanto las consultas deberan considerar las dems cuentas maestras que se vallan registrando aqu: https://beneficiarios.eatcloud.info/api/data/eatc_cua_master? eatc_cua =_* (de hecho cuando se monte el entorno esta informacin debera estar aqu: https://datagov.eatcoud.info/api/data/eatc_cua_master? eatc_cua =_* )  

https://donantes.eatcloud.info/api/{{eatc_cua_master. eatc_cua }}/... 
https://beneficiarios.eatcloud.info/api/{{eatc_cua_master. eatc_cua }}/.., 

 CARD DE KPI 
 Para presentar cada uno de los KPIs, se utilizar una card que debe contener informacin: 

 {{Nombre del KPI o mtrica}} 
 Se constituye en el distintivo principal del KPI 

 (?) Tooltip 
 Al presionar el signo de interrogacin se debe mostrar la descripcin detallada del KPI, que se constituye en una descripcin en lenguaje no tcnico de la ficha tcnica del indicador (ver segunda imagen del carrusel) 

 {{Valor del indicador}} (para el periodo seleccionado. En el ejemplo 146) 
 Es el valor del indicador o KPI para el periodo de tiempo seleccionado en el selector de punto anterior 

 {{Porcentaje de variacin}} en comparacin con el periodo anterior (-5.19 % en el ejemplo) 
 Corresponde a la diferencia entre el valor del KPI del periodo actual menos el valor del periodo anterior anterior, sobre el valor del periodo anterior (por cien) 

 {{Grfico de tendencia}} 
 Muestra los valores da a da del indicador o KPI, y su promedio en el periodo seleccionado. En este link se puede consultar una hoja de datos.  Cundo se hace clic en un dato de una fecha especfica, sale un cuadro en dnde se ve la fecha, el valor del KPI y su promedio (ver tercera imagen del carrusel) 

 A futuro {{Presupuesto y ejecucin presupuestal}} 
 En un futuro se deber poder incorporar el dato del presupuesto para la mtrica en particular (presupuesto diario) y poderlo ver graficado en el grfico de tendencia  (como se ve por ejemplo el grfico del promedio) y en el despliegue de datos se debe colocar el porcentaje de ejecucin presupuestal que se debe calcular como Valor del KPI / Presupuesto del KPI (para cada da) 

 NSM (MTRICA DE ESTRELLA DEL NORTE) 
 Esta mtrica debe destacarse en el Dashboard mostrando su importancia y se debe visualizar en primera instancia (aunque en el diseo que se muestra a continuacin la card destacada no tiene el diseo de card de KPI arriba descrito, cuando se pinte el KPI el mismo debe construirse de acuerdo a la Card de KPI , por lo tanto el siguiente ejemplo solo sirve para mostrar los rasgos que permiten visualizar el KPI como el ms importante y prominente. 

 Nombre del KPI o mtrica: Kilogramos entregados acumulados 
 Se diferencia de la que se presenta en el diseo del wireframe en primera instancia 

 Tooltip o descripcin detallada: 
 Sumatoria de los Kilogramos de los anuncios de donacin efectivamente entregados a beneficiarios y de ofertas de ltimo minuto distribuidas en el pblico en general. 

 Valor del inidicador: cmo se calcula 
 Sumatoria de los Kilogramos de los anuncios ( eatc_dona_headers. eatc-total_weight_kg ), cuyo estado es "entregado (delivered)", "recibido (received)", "pre-certificado (pre-certified)" y "certificado (certified)" y de las ofertas ( eatc_sale_order. eatc-odd_total_weight_kg ) cuyo estado es  "pagado (paid_out)" , "entregado (delivered)", "parcialmente reembolsado (partially_refund), que se encuentran en todas las cuentas maestras ( eatc_dona_headers en el entorno de donantes y eatc_sale_order en el entorno beneficiarios).   

 Las cuentas maestras se pueden consultar aqu: https://beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_country=_* . Inicialmente solo tenemos como cuenta maestra a baco, pero en un futuro se deber consolidar en este dashboard datos de otras cuentas maestras. 

 Prximamente: grfico de torta 
 Este grfico deber mostrar la distribucin de dicho indicador por diversos criterios como seran: 

 eatc_country 
 eatc_province 
 eatc_city 
 eatc_donor 
 vertical (nuevo, pendiente de implementar: es informacin que est presente en la informacin de la cuenta) 

 KPIS DE ALTO NIVEL 
 Es un conjunto de cuatro KPIs de alto nivel que deben visualizarse en segundo orden de importancia.  En la siguiente hoja se muestra el detalle de estos KPIs, 

KPIs EatCloud 

 IMPULSORES CLAVE 
 Cada KPI de alto nivel se decompone en impulsores clave.  Por lo tanto estos se deben mostrar en tercera jerarqua, pero se debe entender que estos subconjuntos de KPIs tienen que ver con  un KPI de alto nivel (KPI de alto nivel relacionado).  
 Se debe evaluar si se colocan en bloques sucesivos despus de los KPIs de alto Nivel, o si en un bloque que se colapse y descolapse debajo de cada KPI de alto nivel correspondiente.  En primera instancia en este dashboard se debern mostrar los impulsores relacionados co los KPIs de Alto Nivel:  
 # de puntos de donacin / despacho (eatc_pods) activos 
 # de anuncios / ofertas generados acumulados 
 Los impulsores clave relacionados con "# de beneficiarios (gestores de donaciones) activos" se sacarn de la Google Play Console (inicialmente de manera manual y luego se evaluar algn mecanismo tcnico), y los relacionados con "# de usuarios finales activos" aun est pendiente de definir los mecanismos tcnicos para obtenerlos (por lo tanto aun no se traen aqu) 

KPIs EatCloud 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-datagov-bo%2F33939P9DTGh25uIVRdxoyWIBUPN5sQUWJc427gSEZt0V56JuCCLDPNfMVJntgSYQgvqIh-djPpA%3Dw16383.jpg, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdashboard-datagov-bo%2F33939P9DTGh25uIVRdxoyWIBUPN5sQUWJc427gSEZt0V56JuCCLDPNfMVJntgSYQgvqIh-djPpA%3Dw16383.jpg 

 856.000000000000 

 DASHBOARD - DATAGOV