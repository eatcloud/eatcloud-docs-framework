# enriquecimiento-de-información-de-anuncio-de-donación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 A partir de los datos del anuncio de donacin se genera informacin adicional que servir para el clculo de los KPIs, su clasificacin y su posterior gestin. La estructura enriquecida del anuncio de donacin se puede consultar aqu y los campos mandatorios u obligatorios se pueden consultar aqu .&#160; 

 ANLISIS PARA LA INTEGRACIN 
 Se compone de las siguientes tareas&#58; 

&#160; 
 Solicitud de insumos 
 Para analizar una integracin, se le debe solicitar al cliente que nos enve una estructura de detalle estndar (extrada de sus sistemas) con la informacin de los productos a donar.&#160; Dicha escructura debe contener siempre en la primera fila la declaracin de los campos, y es preferible que se entrege con codificacin UTF-5 y en formato .CSV separado por punto y comas.&#160; Si se entrega en Excel se podrn hacer transformaciones para lograr un insumo con condiciones ptimas.&#160; Dicha estructura debe contener como mnimo los siguientes campos.&#160; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_dona&amp;eatc_madatory=y,if &#160; 
&#160; 
 Si el cliente nos pasa un maestro de productos, entonces los siguientes campos seran opcionales, de acuerdo a la informacin que contenga dicho maestro 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_dona&amp;eatc_alternative_source=eatc_odds &#160; 
&#160; 
 La siguiente informacin es opcional, es decir, si el cliente la enva se podr enriquecer de mejor manera el archivo 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_mandatory_info?eatc_objectstore=eatc_dona&amp;eatc_madatory=n &#160; 

&#160; 
 Anlisis y mapeo de informacin suministrada 
 Con la informacin entregada por el cliente, se debe proceder primero a establecer si la informacin suministrada contiene la mnima necesaria.&#160; Una vez comprobado esto se debe proceder a realizar el mapeo de los datos, que implica establecer cul es la traduccin de la declaracin de los campos enviados por el cliente en trminos de la declaracin estndar de campos EatCloud (parmetro de eatc_dona ).&#160; Para ello se puede utilizar como plantilla la ltima documentacin realizada para el mapeo de integracin . 
&#160; 
 Este proceso se debe realizar previo a la carga de la informacin en la plataforma y con posterioridad se generar un proceso de mapeo para poder almacenar y editar el respectivo mapeo o correspondencia entre los datos entregados y los datos que maneja la plataforma. 

 Se debe procurar en la medida de las posibilidades (y de los datos que pase el donante), incorporar toda la informacin que sugiere la estructura de eatc_dona en su definicin, ya que se considera informacin relevante para las acciones que pretende realizar el sistema. 
&#160; 
 _enriquecer_dona.php 
&#160; 
 En trminos generales existen 4 tipo de acciones que se realizan sobre la informacin y con la informacin entregada para enriquecer el anuncio de donacin a saber&#58; 

 Querys&#58; 

 Teniendo como base los maestros entregados por el cliente, se realizan bsquedas en dichos maestros para traer la informacin del eatc_dona . 

 Constantes&#58; 

 Son valores que se pueden establecer de manera uniforme para toda una fuente de informacin (informacin o archivo entregado por el cliente). 

 Clasificaciones&#58; 

 Corresponde a la clasificacin de los artculos donados segn las clasificaciones que manejan los bancos de alimentos ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_odds_typologies?_id=_* ).&#160; Dado que este proceso requiere realizar un mapeo de categoras, se trata de manera detallada en la seccin &quot; Clasificacin de productos &quot;. 

 Funciones 

 A partir de los datos entregados se realizan operaciones matemticas para consolidar, totalizar o transformar la informacin. 

 EatCloud 

 Corresponde a informacin que es incorporada por la plataforma a partir de sus funcionalidades y que permite enriquecer la informacin del anuncio de donacin. 

 Dado lo anterior, cada vez que ingrese una nueva cuenta, se deber realizar un anlisis para efectuar el mapeo y a partir del mismo programar o parametrizar las funciones que enriquecen el anuncio de donacin especfico. A continuacin se tienen dos ejemplos desarrollados para el xito a fin de enriquecer la informacin de los anuncios propios y los de mercanca de terceros . 

 Configuracin tcnica del mapeo 
 Con la documentacin del mapeo se realiza la programacin de la misma para generar los procesos necesarios de enriquecimiento de informacin y posterior generacin del encabezado. 

 Configuracin de mtodo de intercambio de informacin 
 Se debe establecer el mtodo de intercambio de informacin, para programar funciones que realicen el translado de informacin de un lugar a otro.&#160; Por ejemplo con el xito se realizaron estas funciones. 

 Copia de archivos del FTP exito a estructura exito/eatc_dona&#58; 
 _baja_uploads.php 
&#160; 
 _loadfile.php 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ENRIQUECIMIENTO DE INFORMACIN DE ANUNCIO DE INFORMACIN