# deprecado-edición-de-coordenadas.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 (DEPRECADA&#58; porque este campo junto con el anterior se tomarn de un nuevo maestro) NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc_donor_fiscal_name) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods. eatc-donor_code y eatc_dona_headers. eatc-donor_code 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
&#160; 
 CASO 1&#58; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la donacin (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
 CASO 2&#58; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_dona_headers . 
&#160; 
 [***NUEVO****]&#58; Revisar que para cuentas con multiple_donors=si el dato del nit se est llevando a eatc_dona_headers.eatc-donor_code 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin. Cuando se deja la informacin cmo estaba no se realiza la _operacin update 

 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor_code=&#123;&#123;input&#125;&#125; 
&#160; 
 ***REVISAR***[+++] Parmetros para editar informacin del punto de donacin (y guardarla en la persistencia eatc_pods), cuando se edita el nombre del donante y su identificacin para cuentas que manejen mltiples donantes 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
 [***] Cuando se termina de editar esta informacin 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

&#160; 
 Edicin de coordenadas del punto de donacin&#58; 
 Despliegue de la funcionalidad 
 Si evaluando la informacin de la cuenta respectiva ( &#123;&#123;cua_user&#125;&#125; ) permite edicin de coordinadas.&#160; Para ello el sistema realiza la siguiente consulta&#58; 
 &#123;&#123;URL_datagov&#125;&#125; /api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; &amp; edit_coordinates=si&amp;_cmp=name 
&#160; 
 Si el sistema entrega no entrega un resultado vlido, entonces no es posible editar coordenadas.&#160; Si entrega un resultado vlido entonces el sistema presenta un botn que permite editar/seleccionar una direccin (coordenadas) para efectuar la donacin. 
&#160; 
 Ejemplo &#58; cuenta &quot;colombia&quot; ambiente de pruebas&#58; 
 El sistema realiza el siguiente llamado&#58;&#160; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia&amp; edit_coordinates=si&amp;_cmp=name &#160; &#160;&#160; 
&#160; 
 Como se recibe una respuesta vlida el sistema debe habilitar la funcionalidad para la cuenta en cuestin. 
&#160; 
 Edicin de coordenadas&#58; 
 Al darle clic al botn, la plataforma debe evaluar si en la persistencia &quot; eatc_pods_coordinates (NOTA PARA JDC&#58; falta documentacin mtodo, parmetros) &quot; para el &quot;eatc_pod&quot; respectivo existe informacin ( eatc_pods.eatc-id ), para mostrar las diversas direcciones guardadas en un selector (se muestra en el selector la direccin y su nombre, permitiendo traer las coordenadas respectivas, informacin que se terminar llevando a la informacin del respectivo eatc_pod).&#160;&#160; 
&#160; 
 Ejemplo &#58; 
 Para el punto de donacin &quot;nzzn1&quot; de la cuenta &quot;colombia&quot; se tiene la siguiente informacin&#58; 
&#160; 
 Ambiente de prueba&#58; https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id=nzzn1 &#160; 
&#160; 
 Por lo tanto se debe poder seleccionar una de las direcciones registradas (en etapas posteriores se debe poder operar este selector como un buscador) para desplegar la latitud y longitud determinada. 
&#160; 
 Tambin debe presentar la opcin de adicionar una nueva direccin, y para hacerlo se debe desplegar un mapa que coloque por defecto a eatc_lat y eatc_lon del eatc_pod respectivo (se debe reciclar lo implementado aqu&#58; https&#58;//devdonantes.eatcloud.info/registro/colombia &#160; para mayor informacin comunicarse con Ivn Daro Restrepo). La nica diferencia con las imgenes abajo dispuestas, es que debe existir un campo de captura adicional con la etiqueta &quot; Nombre del punto de donacin &quot; inmediatamente abajo de la direccin y que corresponde a la informacin que se encuentra en eatc_pods.eatc-name (en caso de que no halla un registro en eatc_pods_coordinates ) o eatc_pods_coordinates .eatc-name cuando se ha realizado una seleccin de las coordenadas registradas o en (ser un campo editable tipo text_field que reciba informacin tipo string) 

 Al mover el PIN en el mapa se podr ir variando las coordenadas y la direccin (tal como lo hace la actual implementacin ejemplo https&#58;//devdonantes.eatcloud.info/regpdona/ )&#160; 

 Siempre se permitir editar la direccin que aparece a partir del la seleccin del PIN. Ciudad y Pas no permitirn ser editados, solo sern editables a partir de la seleccin el pin en el mapa. 

 ***REVISAR***Edicin de coordenadas del punto de donacin&#58; se selecciona un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
&#160; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
&#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se toma de eatc_pods_coordinates y se lleva a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Selector (nico)&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-name 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Es decir, el selector debe tener los valores&#58; oficina y casa. El valor que sea seleccionado se llevar al &#123;&#123;input&#125;&#125; respectivo y se guardar su _id para las posteriores consultas 
&#160; 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 
&#160; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lat y se lleva a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lat 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; 6.252699799631093 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates.eatc-lon y se lleva a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon &#160; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lon 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; -75.59463315188623 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates.eatc-adress y se lleva a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-adress 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates.eatc-city y se lleva a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-city 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Medelln 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 

&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 
&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates.eatc-country y se lleva a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-country 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; CO 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc_donor_fiscal_name) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc_pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods. eatc-donor y eatc_dona_headers. eatc_donor_fiscal_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
&#160; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro&#160; del anuncio de donacin (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
&#160; 
 [***NUEVO***&#58; Cuentas con multiple_donors=si&#58; El nombre del donante que se digita se guarda en eatc_dona_headers.eatc_donor_fiscal_name] 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin. Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers? eatc_donor_fiscal_name =&#123;&#123;input&#125;&#125; 
 NOTA IMPORTANTE&#58; ANTERIORMENTE SE LLEVABA A &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor=&#123;&#123;input&#125;&#125; SE DEBE GARANTIZAR QUE A ESTE REGISTRO SE LLEVE SIEMPRE _DOM. cua_user 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
&#160; 
 [***NUEVO****]&#58; Revisar que para cuentas con multiple_donors=si el dato del nit se est llevando a eatc_dona_headers.eatc-donor_code 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin. Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor_code=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates.eatc-warning y se lleva a eatc_sale)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-warning 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Primera observacin de prueba 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para editar informacin de coordenadas (y guardarla en la persistencia eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125;&amp; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
 [***] Cuando se termina de editar los datos de las coordenadas (seleccionando una opcin diferente a la almacenada en eatc_pods) 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 
&#160; 
 ***REVISAR***Edicin de coordenadas del punto de donacin&#58; se editan los datos un punto ya creado en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-name luego a eatc_pods.eatc-name y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Selector (nico)&#58; formado con la siguiente consulta de valores&#58; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; eatc-name 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , esta ser la informacin que se despliega en el selector&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Es decir, el selector debe tener los valores&#58; oficina y casa. El valor que sea seleccionado se llevar al &#123;&#123;input&#125;&#125; respectivo y se guardar su _id para las posteriores consultas 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado en el anterior selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 

&#160; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lat 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; 6.252699799631093 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-lon 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; -75.59463315188623 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo en el punto anterior ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-adress 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion en el punto anterior la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Calle 45D, Florida Nueva, Comuna 11 - Laureles-Estadio, Zona Urbana Medelln 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-city 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Medelln 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-city=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 

&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-country 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; CO 
&#160; 
 El usuario podr cambiar la informacin del dato seleccionado (moviendo el pin en el mapa. En una primera etapa solo se aceptarn ventas de Colombia, pero a futuro se debern incorporar nuevos pases) y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo para luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-country=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc_donor_fiscal_name) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods. eatc-donor y eatc_dona_headers. eatc_donor_fiscal_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al anuncio de donacion (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_dona_headers . 
&#160; 
 [***NUEVO***&#58; Cuentas con multiple_donors=si&#58; El nombre del donante que se digita se guarda en eatc_dona_headers.eatc_donor_fiscal_name] 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin. Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers? eatc_donor_fiscal_name =&#123;&#123;input&#125;&#125; 
 NOTA IMPORTANTE&#58; ANTERIORMENTE SE LLEVABA A &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor=&#123;&#123;input&#125;&#125; SE DEBE GARANTIZAR QUE A ESTE REGISTRO SE LLEVE SIEMPRE _DOM. cua_user 
 &#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor=&#123;&#123;_DOM. cua_user &#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods. eatc-donor_code y eatc_dona_headers .eatc-donor_code 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user &#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
&#160; 
 [***NUEVO****]&#58; Revisar que para cuentas con multiple_donors=si el dato del nit se est llevando a eatc_dona_headers.eatc-donor_code 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin. Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor_code=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_dona_headers?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-warning luego a eatc_sale.eatc-warning)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 eatc_pods_coordinates partiendo de la seleccin que se hizo anteriormente ( selector nombre punto de venta )&#58; &#160; 
&#160; 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125;&amp;_id=&#123;&#123;_id tomado de la seleccin anterior&#125;&#125; eatc-warning 
&#160; 
 Ejemplo&#58; 
 Para el punto en la cuenta colombia (ambiente de pruebas) cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH , y se seleccion anteriormente la opcin &quot; oficina &quot; (_id= 17 )&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods_coordinates?eatc-id= fRfpi7G2m2SYWdRHH4oJH &amp;_id =17 &#160;&#160; 
&#160; 
 Por lo tanto el valor que se llevar al &#123;&#123;input&#125;&#125; respectivo es&#58; Primera observacin de prueba 
&#160; 
 El usuario podr cambiar la informacin del dato que se despliega a partir del selector y si esto se hace, se debe hacer un update al object store de eatc_pods_coordinates para guardar el cambio respectivo y luego llevarlo a eatc_pods y eatc_sale 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-warning=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para editar informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
 &#123;&#123;Parametros edicin en eatc_pods_coordinates &#125;&#125; &#58; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods_coordinates&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods_coordinates&#125;&#125; &amp;WHER_id=&#123;&#123; eatc_pods_coordinates._id&#125;&#125; 

&#160; 
 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 
&#160; 
 ***REVISAR***Creacin de coordenadas del punto de donacin&#58; se crea un nuevo punto en eatc_pods_coordinates 
 Identificador del punto de venta (se toma de eatc_pods.eatc-id)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-id y eatc_sale.eatc-pod_id 
 La informacin se toma de&#58; 
 El proceso de login . 
 &#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-id=&#123;&#123;current&#58;eatc_pods.eatc-id&#125;&#125; 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 [***] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_id=&#123;&#123;input&#125;&#125; 

&#160; 
 Nombre del punto de venta (se despliega un campo de captura y luego se lleva eatc_pods_coordinates.eatc-name, a eatc_pods.eatc-name y a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-name [pendiente documentacin], eatc_pods.eatc-name y eatc_sale.eatc-pod_name 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-name=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_name=&#123;&#123;input&#125;&#125; 
&#160; 
 Latitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lat luego a eatc_pods.eatc-lat y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lat [pendiente documentacin], eatc_pods.eatc-lat y eatc_sale.eatc-pod_lat 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lat=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lat=&#123;&#123;input&#125;&#125; 

&#160; 
 Longitud del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-lon luego a eatc_pods.eatc-lon y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-lon [pendiente documentacin], eatc_pods.eatc-lon y eatc_sale.eatc-pod_lon 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-lon=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_lon=&#123;&#123;input&#125;&#125; 

&#160; 
 Direccin del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-adress luego a eatc_pods.eatc-adress y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque ahora se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-adress [pendiente documentacin], eatc_pods.eatc-adress y eatc_sale.eatc-pod_address 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN), con posibilidad de editar la direccin que sugiere el mapa 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-adress=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_adress=&#123;&#123;input&#125;&#125; 

&#160; 
 Ciudad del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-city luego a eatc_pods.eatc-city y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-city [pendiente documentacin], eatc_pods.eatc-city y eatc_sale.eatc-pod_city 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-city=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-city=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_city=&#123;&#123;input&#125;&#125; 

&#160; 
 Pas del punto de venta (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc-country luego a eatc_pods.eatc-country y luego a eatc_sale)&#58; 
 [+++] Este tem es nuevo en cuanto a su manejo porque en el proceso de creacin de donaciones no se no se tomaba en cuenta, pero ahora si se consultar y se llevar al object store de las ventas (eatc_sale) 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-country [pendiente documentacin], eatc_pods.eatc-country y eatc_sale.eatc-pod_country 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Mapa (ubicacin de PIN) 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-country=&#123;&#123;input&#125;&#125; &#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-country=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-pod_country=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] Nombre del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor &#58; &quot; Juan David Correa Toro &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 [+++] NIT o Identificacin del donante (para cuentas con mltiples donantes)&#58; 
 [+++] Este tem es nuevo y se implementa porque para cuentas que manejen mltiples donantes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?multiple_donors=si ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;multiple_donors=si )) se debe preguntar el nombre (eatc-donor) y el NIT (eatc-donor_code) de quien est vendiendo para llevarlo a la persistencia de los puntos de donacin (eatc-pods) y no tomar esta informacin desde los datos de configuracin de la cuenta (como se hace hasta el momento).&#160; Este manejo se deber extender en su momento a la creacin de anuncios de donacin. 
 Informacin tcnica del parmetro&#58; eatc_pods.eatc-donor_code y eatc_sale.eatc-donor 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; si (si la cuenta maneja mltiples donantes) 
 Validacin &#58; obligatoriedad (si la cuenta maneja mltiples donantes) 
 La informacin se toma de&#58; 
 CASO 1&#58; 
&#160; 
 S i la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) no tiene dato registrado en el parmetro multiple_donors o el parmetro no existe o el valor de ese parmetro es &quot; no &quot; 
&#160; 
 No se despliega ningn campo de captura ni se lleva ninguna informacin con respecto a este dato al registro de la oferta de ltimo minuto eatc_sale (ya que el dato se tomar ms adelante desde la informacin de cofiguracin de la cuenta ) 
&#160; 
 Ejemplo 1&#58; 
 Para cualquier punto de la cuenta exito se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito &#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; no &quot;, entonces no se debe mostrar ningn campo de captura. 
&#160; 
 Ejemplo 2&#58; 
 Para cualquier punto de la cuenta makro se debe hacer la siguiente consulta&#58; 
&#160; 
 ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) 
&#160; 
 Como el parmetro multiple_donors no existe para este registro de configuracin de cuenta, no se debe mostrar ningn campo de captura. 
&#160; 
&#160; 
 CASO 2&#58; 
&#160; 
 Si la cuenta respectiva en datagov ( ***NUEVO*** &#160; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;cua_user&#125;&#125; 
 ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=&#123;&#123;cua_user&#125;&#125;) ) tiene registrado en el parmetro multiple_donors el valor &quot; si &quot;, el sistema debe traer los datos guardados en eatc_pods.eatc-donor_code a un cuadro de captura de texto, y los mismos podrn ser editados o dejados de igual manera y estos datos, segn sea el caso se enviarn a los repositorios de eatc_pods (cuando se editen) y eatc_sale segn sea el caso 
&#160; 
&#160; 
 Ejemplo 1&#58; 
 Para el punto en la cuenta colombia cuyo eatc-id es fRfpi7G2m2SYWdRHH4oJH se debe realizar la siguiente consulta&#58; 
&#160; 
 **NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=colombia &#160;&#160;&#160; 
 (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia) 
&#160; 
 Como el resultado del parmetro multiple_donors es &quot; si &quot;, se debe proceder a realizar la siguiente consulta (ambiente de pruebas)&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=fRfpi7G2m2SYWdRHH4oJH &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor_code &#58; &quot; 71745712 &quot;, esta informacin se trae a un campo de texto que podr ser editado o no y que es de carcter obligatorio. 
&#160; 
&#160; 
 Ejemplo 2&#58; 
 Para otro punto de donacin de la cuenta colombia (que ya sabemos que tiene en el parmetro multiple_donors el registro &quot; si &quot;) cuyo eatc-id es AlzZOAxyXNW3aV9mxDRUW , se debe proceder a realizar la siguiente consulta (ambiente de pruebas) 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/colombia/eatc_pods?eatc-id=AlzZOAxyXNW3aV9mxDRUW &#160; 
&#160; 
 Como la consulta para este punto de donacin aparece el dato en el parmetro eatc-donor no tiene un dato registrado, la web app debe desplegar un campo de texto con la etiqueta &quot;nombre del donante&quot; de carcter obligatorio para incorporar esta informacin a los object store eatc_pods y eatc_sale . 
 [+++] Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods?eatc-donor=&#123;&#123;input&#125;&#125; =&gt; cuando se edita o se crea esta informacin.&#160; Cuando se deja la informacin cmo estaba no se realiza la _operacin update 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-donor=&#123;&#123;input&#125;&#125; 

&#160; 
 Observaciones para la recogida (se toma de eatc_pods_coordinates y si se edita el dato se lleva eatc_pods_coordinates.eatc- luego a eatc_sale)&#58; 
 Informacin tcnica del parmetro&#58; eatc_pods_coordinates.eatc-warning [pendiente documentacin], eatc_pods.eatc-warning y eatc_sale.eatc-warning 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Validacin &#58; ninguna 
 La informacin se toma de&#58; 
 Campo de captura Tipo &#58; Pregunta abierta ( Textarea ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Se guarda en [+++] &#58;&#160; 
&#123;&#123;URL_entorno&#125;&#125;/api/&#123;&#123;cua_user&#125;&#125;/eatc_pods_coordinates?eatc-warning=&#123;&#123;input&#125;&#125; 
&#123;&#123;URL_entorno&#125;&#125;/api/eatcloud/eatc_sale?eatc-warning=&#123;&#123;input&#125;&#125; 

&#160; 
 Parmetros para crear informacin de coordenadas (y guardarla en las persistencias eatc_pods_coordinates y eatc_pods) 
 Una vez se termina de hacer la edicin del punto de donacin, se toma la siguiente informacin o parmetros para realizar los registros respectivos&#58; 
 &#123;&#123;Parametros creacin en eatc_pods_coordinates &#125;&#125; &#58; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;CO&#125;&#125;&amp; eatc-warning= &#123;&#123; OBSERVACIONES_PARA_LA_RECOGIDA &#125;&#125; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods_coordinates&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods_coordinates&amp;_operacion= insert &amp;&#123;&#123; Parametros edicin en eatc_pods_coordinates&#125;&#125; 
 &#123;&#123;Parametros edicin en eatc_pods &#125;&#125;&#58; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-city =&#123;&#123;Ciudad&#125;&#125;&amp; eatc-adress =&#123;&#123;Direccion&#125;&#125;&amp; eatc-lat =&#123;&#123;eatc-lat&#125;&#125;&amp; eatc-lon =&#123;&#123;eatc-lon&#125;&#125;&amp; eatc-name =&#123;&#123;eatc-name&#125;&#125;&amp; eatc-country =&#123;&#123;pas&#125;&#125;&amp; eatc-donor =&#123;&#123;Nombre del donate&#125;&#125;&amp; eatc-donor_code =&#123;&#123;Nit o identificacin del donate&#125;&#125; 
 [***] Cuando se&#160; terminan de editar los datos de las coordenadas se realiza la actualizacin en eatc_pods&#58; 
 Mtodo POST https&#58;//devdonantes.eatcloud.info/crd/&#123;&#123;cua_user&#125;&#125;/?_tabla=eatc_pods&amp;_operacion=update&amp;&#123;&#123; Parametros edicin en eatc_pods&#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods.eatc-id&#125;&#125; 

&#160; 
 ***REVISAR***Datos que se digitan en el encabezado (una sola vez por anuncio) 
 Documento soporte&#58;&#160; 
 Campo de texto abierto que se despliega si se cumple la siguiente condicin&#58; que en parmetro eatc_dona_upl tenga como valor &quot;yes&quot; ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ). En caso que el parmetro tenga como valor &quot;no&quot; no se debe desplegar campo de captura y se toma este dato como vaco (para posteriormente llevarlo al registro . 
 **NUEVO**&#58;&#160; ID Para identificar el div de la funcionalidad&#58; id=&quot; btn_document_soporte &quot; 
 Informacin tcnica del parmetro&#58;&#160; eatc_sale.eatc-doc 
 Descripcin ( tooltip ) &#58; Ingrese por favor un documento de soporte 
 Tipo &#58; Pregunta abierta ( cuadro de texto ) ( informacin tcnica sobre el tipo de pregunta &#58; PAT ) 
 Tipo de dato&#58; string 
 Obligatoriedad &#58; no 
 Regla obligatoriedad &#58; no aplica 
 Validacin &#58; ninguna 
 Se guarda en &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/eatc_dona_headers?eatc-doc=&#123;&#123;input&#125;&#125; 
 Mtodo para guardar especfico (para efectos indicativos, no prcticos, dado que los parmetros se envan todos en una sola llamada al CRD) &#58;&#160; 
&#123;&#123;URL_entorno_donantes&#125;&#125;/crd/&#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla=eatc_dona_headers&amp;_operacin=insert&amp;eatc-doc=&#123;&#123;input&#125;&#125; 
&#160; 
 Detalle de anuncio de donacin 
 Los datos de detalle se pueden adicionar varias veces a la transaccin (un anuncio de donacin, puede tener &quot;n&quot; detalles, tantos como sea necesarios para registrar una donacin de un conjunto de productos) a partir de la seleccin de un producto utilizando un buscador de productos y se hace de la siguiente manera&#58; 
&#160; 
 Productos (eatc-name)&#58; 
 El sistema deber evaluar el parmentro eatc_odds_app de la cuenta (cua) respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), para establecer el tipo de captura que utiliza para este dato&#58;&#160; hay tres opciones, tradicionales y una nueva opcin segn la escogencia realizada en la funcionalidad de Multiples Donantes (validacin de punto de donacin de no negociados) &#58; 
&#160; 
 0. ***NUEVO&#58; Cuentas con multiple_donors=si&#58; y el punto de donacin tiene registros en &quot; eatc_pods_cua_donor_nng &quot; y no se selecciona el valor por defecto &#58; 
 Esto quiere decir que el nombre del producto se debe tomar del maestro de productos de la cuenta donante de no negociados, por lo tanto a partir de la seleccin realizada , se realiza la siguiente consulta. 
 &#123;&#123;URL_donantes&#125;&#125;/api/ &#123;&#123; eatc_multiple_donors_info. eatc_cua_user&#125;&#125; /eatc_odds?_id=_* 
 [predictive text] Buscador de productos 
 La App despliega un buscador de producto, que se debe nutrir para su bsqueda, de la tabla eatc_odds de la cuenta [cua] respectiva y tener capacidades de teclado predictivo para encontrar rpidamente el producto por todas sus caractersticas ( nombre, cdigos, tipologas, etc ) y lectura de cdigo de barras (esta lectura de cdigo de barras opera sobre&#58; eatc_odds,eatc-odd_code ) . 
 Ejemplo &#58; cua_user&#58; exito, ambiente de pruebas, el usuario seleccion mediante la funcionalidad &quot;multiple_donors&quot; la opcin cuya &quot; eatc_multiple_donors_info. eatc_cua_user &quot; es &quot; alimentoscarnicos &quot; 
&#160; 
 Como el usuario no realiz la seleccin de la cuenta por defecto, el sistema deber realizar la siguiente consulta para traer la informacin de los productos&#58;&#160; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/alimentoscarnicos/eatc_odds?_id=_* &#160; 

&#160; 
 En el buscador de productos, tambin se podr digitar el eatc-odd_code, para traer el producto respectivo. 
 En el campo de captura del nombre del producto, tambin se podr digitar el cdigo del producto (eatc-odd_code) y que a travs de dicha digitacin se traiga el nombre del artculo. Esto se solicita, porque en maestros de productos con muchos productos (como es el caso por ejemplo de Makro), la bsqueda por nombre puede requerir una digitacin casi que completa para lograr tener resultados en el buscador (para productos que manejan muchas referencias), y si se digita un cdigo puede ser ms fcil encontrar el producto. 
&#160; 
&#160; 
 ***LAS dems opciones funcionan tal como lo venan haciendo antes, cuando se selecciona el valor por defecto o un donante que es propio de la cuenta, es decir, que no es un donante de no negociados*** 
 1. eatc_cua.eatc_odds_app = eatc_dona_app&#58;&#160; 
 Esto quiere decir que el nombre del producto se debe tomar de la digitacin de un nombre de producto.&#160; Por lo tanto la App debe desplegar un campo de texto [input type=textfield data type=string] para que el usuario digite el nombre del producto a donar. 
 Ejemplo&#58; 
 Para la cuenta &quot;prueba&quot; el valor de eatc_odds_app &#160; ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=prueba &#160; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=prueba )) es eatc_dona_app por lo tanto la App deber proveer un campo de captura tipo texto para que el usuario digite el nombre del producto (en etapas posteriores del desarrollo con esta informacin digitada se debe empezar a llenar un repositorio que sirva para activar funciones de texto predictivo para futuras digitaciones de producto) 
&#160; 
&#160; 
 ***IDEA*** capturar las categoras baco **** 
 2. eatc_cua.eatc_odds_app = no trae datos o es indefinido 
 Se aplica lo mismo que en el punto anterior.&#160; 
&#160; 
 3. eatc_cua.eatc_odds_app = eatc_odds&#58;&#160; 
 Esto quiere decir que el nombre del producto se debe tomar del maestro de productos respectivo (eatc_odds) y se aplica el siguiente tipo de input. 
 [predictive text] Buscador de productos 
 La App despliega un buscador de producto, que se debe nutrir para su bsqueda, de la tabla eatc_odds de la cuenta [cua] respectiva y tener capacidades de teclado predictivo para encontrar rpidamente el producto por todas sus caractersticas ( nombre, cdigos, tipologas, etc ) y lectura de cdigo de barras (esta lectura de cdigo de barras opera sobre&#58; eatc_odds,eatc-odd_code ) . 
 Ejemplo &#58; 
&#160; 
 Suponiendo que el xito ( cua=exito ) tuviera configurada la opcin de generar anuncios de donacin&#160; desde la app ( eatc_dona_upl &#58; &quot; yes &quot;, cosa que no ocurre), el buscador debera utilizar el maestro de la cuenta respectiva para alimentar el buscador&#58; ( https&#58;//devdonantes.eatcloud.info/api/ [cua] /eatc_odds?_id=_ *) 
 As&#58;&#160; 
(dada la cantidad de datos que tiene el xito, para efectos demostrativos se utiliza la consulta de un solo artculo)&#58; 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_odds?_id=00001 
&#160; 
 Nota importante &#58;&#160; los atributos estndar del objeto de donacin se pueden consultar aqu&#58;&#160; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=eatc_odds Los atributos obligatorios deben ser estos&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_parametros&amp;metodo=eatc_odds&amp;obligatorio=si (para el caso del xito por el tamao del maestro el dato de la equivalencia a KG fue entregado en otro maestro.&#160; Se evaluar si esta es una circunstancia normal, caso en el cual se configurar un maestro adicional para generar ese dato). 
&#160; 
 En el buscador de productos, tambin se podr digitar el eatc-odd_code, para traer el producto respectivo. 
 En el campo de captura del nombre del producto, tambin se podr digitar el cdigo del producto (eatc-odd_code) y que a travs de dicha digitacin se traiga el nombre del artculo. Esto se solicita, porque en maestros de productos con muchos productos (como es el caso por ejemplo de Makro), la bsqueda por nombre puede requerir una digitacin casi que completa para lograr tener resultados en el buscador (para productos que manejan muchas referencias), y si se digita un cdigo puede ser ms fcil encontrar el producto. 
&#160; 
 [Input] Digitacin de cantidades&#58; 
 El sistema despliega un formulario para digitar las cantidades del artculo ( unidades&#58; debe ser el label del input ). El input debe ser de tipo numrico float.&#160; Con este Input ( eatc-odd_quantity) , el sistema debe calcular los siguientes datos&#58; 
 Peso total de la mercanca donada&#58; eatc-odd_total_weight_kg&#58; corresponde a la multiplicacin de las unidades digitadas por eatc-odd_unit_weight_kg ( eatc-odd_quantity* eatc-odd_unit_weight_kg). En Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_weight_kg . 
 Costo total de la mercanca donada&#58; eatc-odd_total_cost&#58; corresponde a la multiplicacin de las unidades digitadas por eatc-odd_unit_cost ( eatc-odd_quantity*eatc-odd_unit_cost ). En Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos se establece como se obtiene eatc-odd_unit_cost . 
&#160; 
 [NUEVO] Validacin de peso total (eatc-odd_total_weight_kg) cuando el resultado es cero (no se deben permitir que los pesos estn en cero)&#58; 
 Si el sistema detecta que el peso total de la mercanca donada (eatc-odd_total_weight) es igual a cero, se debe mostrar en una ventana modal el siguiente mensaje&#58; 
 Contar con un peso aproximado unitario por producto, nos es de gran ayuda para medir el impacto social y ambiental de cada donacin y para asignar la donacin al beneficiario ms idneo. 
&#160; 
 Ingresa el peso unitario 
 Si se acciona la opcin Ingresa el peso unitario , el sistema se debe posar en el dato de Peso unitario en KG ( eatc-odd_unit_weight_kg ), para permitir su edicin de la manera ms ptima posible (por ejemplo seleccionando el cero). 
 En trminos generales la validacin no dejar pasar al usuario, si no digita un peso unitario. 

 [***NUEVO***CONSULTA A PERSISTENCIA PARA OBTENER PESO EXCESIVO***] Validacin de peso total (eatc-odd_total_weight_kg) cuando el resultado es un peso muy elevado =&gt; MENSAJE CON NMEROS VIVOS PARA PROMOVER UNA EFECTIVA VERIFICACION&#58; 
 Con el nimo de promover una verificacin de peso ms efectiva (dado que siguen habiendo errores de digitacin que traen como resultado anuncios con pesos errneos exagerados), se hace la siguiente propuesta de mensaje en ventana modal, con un nmero vivo (equivalencia del peso en estibas llenas), que deber presentarse cuando el peso excede un valor determinado&#58; 

 Obtencin del dato de peso excesivo ( eatc_excessive_weight_kg )&#58; 
 Para obtener el dato del peso excesivo, a partir del cual se desplegar el modal, ser el siguiente&#58; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_cua= &#123;&#123;_DOM. cua_user &#125;&#125; &amp;eatc_pod_id= &#123;&#123;eatc_pod. eatc-id &#125;&#125; &amp;_distinct= eatc_excessive_weight_kg 
&#160; 
 Si la anterior consulta no trae resultados se debe realizar esta&#58;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_cua= &#123;&#123;_DOM. cua_user &#125;&#125; &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg 
&#160; 
 Si la anterior consulta no trae resultados se debe realizar esta&#58;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= &#123;&#123;_DOM. cua_master &#125;&#125; &amp;eatc_cua= _default &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg 
&#160; 
 Y por ltimo, si la anterior consulta no trae resultados se debe realizar esta&#58;&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125; /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &amp;eatc_cua= _default &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg 
&#160; 
 Si no se obtiene respuesta (por un problema de conectividad o de respuesta del servidor, dado que la ltima consulta tiene datos disponibles) la wapp debe tener el valor &quot;quemado&quot; de 500, a manera de error handler. 
&#160; 
 T an pronto el sistema tenga los datos para calcular el peso total del producto donado (unidades por peso unitario) si el sistema detecta que dicho peso total de la mercanca donada ( eatc-odd_total_weight ) es mayor al parmetro que se obtiene de las anteriores consultas eatc_excessive_weight_kg se debe mostrar en una ventana modal diseada con los siguientes labels (para que quede de una vez correctamente internacionalizado), dispuestos de la siguiente manera (ms abajo se presenta un listado de los labels y las variables a utilizar)&#58; 

 DEPRECADO&#58; (el valor de este parmetro inicialmente se quema en la APP y ser igual a 500 KG , posteriormente se podr consultar con un API que se estar ajustando diariamente) ,&#160; 
&#160; 
 Ejemplo 1 (ambiente de pruebas)&#58; de peso excesivo para el eatc_pod. eatc-id=20, de _DOM. cua_user=exito, _DOM. cua_master=abaco 
 Se debe realizar la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= abaco &amp;eatc_cua= exito &amp;eatc_pod_id= 20 &amp;_distinct= eatc_excessive_weight_kg 
&#160; 
 Dado que el sistema responde&#58; 
 &#123; 
 ts &#58; &quot;210623113311&quot; , 
 op &#58; true , 
 cont &#58; 1 , 
 res &#58;&#160; 
 [ 
 &#123; 
 eatc_excessive_weight_kg &#58; &quot;1000&quot; 
 &#125; 
 ], 
 mem &#58; 0.41 , 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 A los anuncios con peso mayor a 1000 KG desplegarn el pop-up de peso excesivo 

&#160; 
 Ejemplo 2 (ambiente de pruebas)&#58; de peso excesivo para el eatc_pod.eatc-id=9JcLv7lAdqqJ4siphIBIE, de _DOM.cua_user=argentina2, _DOM.cua_master=argentina 
 Se debe realizar la siguiente consulta&#58; 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &amp;eatc_cua= argentina2 &amp;eatc_pod_id=9JcLv7lAdqqJ4siphIBIE&amp;_distinct= eatc_excessive_weight_kg &#160; 
&#160; 
 Como no se obtiene una respuesta vlida, se procede a realizar la siguiente consulta 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &amp;eatc_cua= argentina2 &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg &#160;&#160; 
&#160; 
 Como no se obtiene una respuesta vlida, se procede a realizar la siguiente consulta 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= argentina &amp;eatc_cua= _default &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg &#160;&#160; 
&#160; 
 Como no se obtiene una respuesta vlida, se procede a realizar la siguiente consulta 
 https&#58;//dev.datagov.eatcloud.info /api/eatcloud/eatc_excessive_dona_weight?eatc_cua_master= _default &amp;eatc_cua= _default &amp;eatc_pod_id= _default &amp;_distinct= eatc_excessive_weight_kg &#160;&#160; 
&#160; 
 Dado que el sistema responde&#58; 
 &#123; 
 ts &#58; &quot;210623113311&quot; , 
 op &#58; true , 
 cont &#58; 1 , 
 res &#58;&#160; 
 [ 
 &#123; 
 eatc_excessive_weight_kg &#58; &quot;500&quot; 
 &#125; 
 ], 
 mem &#58; 0.41 , 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 A los anuncios con peso mayor a 500 KG desplegarn el pop-up de peso excesivo 

&#160; 
 Diseo&#58; https&#58;//materializecss.com/modals.html &#160; 
 Recordar colocar adentro de la etiqueta ( &lt;... class=&quot;...&quot;&gt; aqu &lt;...&gt; ) el texto de la misma, para que sirva como valor por defecto (por si las funciones de internacionalizacin fallan). 

 class=&quot; lbl_atencion &quot; 
 Texto etiqueta&#58; Atencin!&quot; 
 ( ttulo ) 

&#160; 
 class=&quot; lbl_acabas_de_registrar_donacion &quot; 
 Texto etiqueta&#58; Acabas de registrar una donacin de 
 ( texto normal ) 

&#160; 
 &#123;&#123;eatc-odd_quantity&#125;&#125; 
 Cantidad del producto digitada por el usuario&#160; 
 (variable resaltada en rojo y negrilla ). 

&#160; 
 class=&quot; lbl_unidades_producto &quot; 
 Texto etiqueta&#58; unidad(es) del producto 
 &#160;( texto normal ) 

&#160; 
 &#123;&#123;eatc-name&#125;&#125; 
 Nombre del producto&#160; 
 (digitado o ingresado a partir de maestro por el usuario&#58; resaltado en negrilla ). 

&#160; 
 class=&quot; lbl_tienen_peso_total &quot; 
 Texto etiqueta&#58; que tiene(n) un peso total de 
 ( texto normal ) 

&#160; 
 &#123;&#123;eatc-odd_total_weight_kg&#125;&#125; 
 Peso total del producto que corresponde a la cantidad del producto por su peso unitario&#160; 
 (Cmputo a partir de las cantidades digitadas&#160; y los pesos digitados o ingresados a partir de maestro respectivo por el usuario&#58; resaltado en rojo y negrilla ). 

&#160; 
 class=&quot; lbl_equivalente_a &quot; 
 Texto etiqueta&#58; lo cual equivale aproximadamente a&#58; 
 ( texto normal ) 

&#160; 
 &#123;&#123;n&#125;&#125; 
 Clculo de la cifra viva de equivalencia a estibas del producto ( nmero muy grande, en rojo, muy resaltado ). En principio una estiba corresponde a 1000 KG, por lo tanto este nmero se obtiene de dividir &#123;&#123;eatc-odd_total_weight_kg&#125;&#125; entre 1000 .&#160; Este valor debe tener el siguiente comportamiento, segn el valor que de&#58; 
 Si el valor se sita entre 0,5 y 0,6666....( o 2/3 )&#58; se debe colocar&#58; ms de 1/2 
 Si el valor se sita entre (2/3) y 0,999999&#58; se debe colocar&#58; ms de 2/3 
 Si el valor es mayor o igual a 1&#58; se debe colocar el resultado de la divisin ( &#123;&#123;eatc-odd_total_weight_kg&#125;&#125; entre 1000) con dos cifras decimales cuando el resultado no sea un entero.&#160; Si el resultado es un entero o muy cercano a un entero, NO se deben colocar cifras decimales. 

&#160; 
 x (imagen estiba) 
 La imagen definitiva se encuentra aqu&#58; http&#58;//repograf.eatcloud.info/img/x_cajas_en_estiba.png &#160; 

 class=&quot; lbl_estibas_maxima_capacidad &quot; 
&#160; 
 Texto etiqueta&#58; Estiba(s) llena(s) a su MXIMA capacidad 
 ( resaltado en negrilla y cursiva.&#160; Se coloca abajo de la imagen) 

&#160; 
 class=&quot; lbl_estas_seguro &quot; 
&#160; 
 Texto etiqueta&#58; Ests seguro, que este es la cantidad / peso de producto donado es correcta? 
 ( texto resaltado ) 

&#160; 
 Botn &#58; class=&quot; lbl_corregir_peso_cantidad &quot; 
&#160; 
 Texto etiqueta&#58; NO, debo CORREGIR el peso y / o cantidad 
 ( Botn )&#58; Si el usuario presiona este botn&#58; el sistema se debe posar en el dato de Cantidad para permitir su edicin y posteriormente la de peso (se debe posar en el primer de estos datos pedido por el formulario) de la manera ms ptima posible (por ejemplo seleccionando todo el nmero de la cantidad digitada). 

&#160; 
 Botn &#58; class=&quot; lbl_confirmar_peso_cantidad &quot; 
&#160; 
 Texto etiqueta&#58; Si, deseo donar esa cantidad / peso 
 ( Botn )&#58; Si el usuario presiona este botn&#58; el sistema se debe permitir seguir adelante. 

 Unidad de medida (informacin al lado del campo de digitacin de cantidades) 
 Al lado del campo de digitacin de cantidades debe mostrarse la unidad de medida o unidad en la que se dona ( eatc_odds.eatc_dona_unit ).&#160;&#160; 
 Nota importante&#58; esta implementacin informativa no est en los maestros del xito, por lo tanto si no se encuentra dicho valor en el maestro respectivo (eatc_odds) el valor por defecto de dicha unidad debe ser &quot; unidades &quot; 

&#160; 
 [Dropdown] Selector de causal de la baja del producto&#58; 
 Para cada registro se debe entregar una causal de la baja (este debe ser el label del dropdown) o retiro del producto del inventario.&#160; Para hacerlo se debe realizar la siguiente consulta (teniendo en cuenta la respectiva Cuenta [CUA]&#58;&#160; 
 https&#58;//devdonantes.eatcloud.info/api/[CUA]/eatc_dona_return_causes?_id=_ * 
&#160; 
 Ejemplo &#58; 
 Para consultar las causales de devolucin / donacin de la cuenta &quot; exito &quot; (en ambiente de pruebas) se debe realizar la siguiente consulta 
 https&#58;//devdonantes.eatcloud.info/api/exito/eatc_dona_return_causes?_id=_* &#160; 
&#160; 
 En el selector se debe mostrar lo correspondiente al parmetro&#58; eatc-return_cause.&#160; En el objeto se debern almacenar eatc-return_cause y eatc-return_cause_code. 

&#160; 
 [Dropdown (si / no)] Selector &quot;Contiene alrgenos?&#58; 
 Para cada registro se debe determinar si la donacin contiene alrgenos. Para ello la App dispondr de un selector, cuyo valor por defecto es &quot;no&quot;.&#160; La informacin se lleva al eatc-dona en el parmetro&#58; &quot;eatc-contains_alergens&quot;. 

&#160; 
 ***NUEVO*** [Date picker] Fecha ms prxima de vencimiento&#58; 
 Para cada registro se debe de manera opcional , seleccionar la fecha ms prxima de vencimiento.&#160; Si el usuario no selecciona ninguna fecha (utilizando el selector de fechas), el dato que debe viajar y quedar registrado en el respectivo parmetro ( eatc_dona. eatc-closer_expiration_date ) ser&#58; 0000-00-00 . Si el usuario desea registrar una fecha, deber ingresar a un &quot; date picker &quot; o &quot; selector de fechas &quot; que presenta por defecto, como sugerencia de &quot;fecha ms prxima de vencimiento&quot; la sumatoria de la fecha actual ms el nmero que se encuentra en el parmetro&#160; eatc_cua. days_before_expiration ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ) .&#160; Si no existe el dato eatc_cua. days_before_expiration, o el mismo llega vaco o nulo, el valor por defecto que debe tomarse es &quot;5&quot;, para realizar la sumatoria y asi sugerir la fecha .&#160; El usuario podr modificar esa fecha sugerida, y el sistema no le permitir ingresar fechas anteriores al da actual ms 1 da. (solo se podrn ingresar fechas posteriores). El dato resultante (tipo fecha con formato AAAA-MM-DD) se deber guardar en el parmetro eatc_dona. eatc-closer_expiration_date 
&#160; 
 Ejemplo &#58; 
 El da 2020-02-27 se realiza un anuncio de donacin para la cuenta Makro (en ambiente de pruebas).&#160; Como en esta cuenta el parmetro eatc_cua. days_before_expiration es igual a 5 ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro)) 
 , el usuario al ingresar al selector de fechas, el mismo le debe sugerir la fecha &quot;2020-02-27 + 5 das&quot; es decir &quot;2020-03-03&quot;.&#160; Si el usuario no vara esta seleccin (puede hacerlo siempre y cuando la fecha del selector de fechas no sea anterior a 2020-02-28 (2020-02-27 + 1 da)), el sistema debe registrar en el eatc_dona. eatc-closer_expiration_date el dato 2020-03-03 
&#160; 
 Detalle&#58; Inputs paramtricos&#58; 
 Los siguientes inputs no estarn presentes por defecto en todas las APPs, y para desplegarse (mostrarse en el formulario de captura) la App deber consultar parmetros registrados en DATAGOV para la cuenta en cuestin [CUA]&#160; ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ) 

&#160; 
 [Input&#58; float] Digitacin de KG&#58; 
 Si el parmetro odds_weight &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua ] ) )&#160; tiene como valor&#58; &quot; eatc_dona &quot; el sistema debe desplegar un campo de captura de KG (float) (peso unitario en KG&#58; es el label del input) y guardarlo en&#58;&#160; eatc-odd_unit_weight_kg 
 Ejemplo&#58;&#160; 
 Teniendo en cuenta que para la cuenta &quot; exito &quot; el parmetro odds_weight tiene como valor eatc_dona ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) ).&#160; Entonces el sistema debe deplegar un input de datos que permita el ingreso de nmeros flotantes (con dos cifras decimales) para que el usuario digite los KG (peso unitario en KG&#58; es el label del input) que se donan. 

&#160; 
 [Input&#58; float] Digitacin del costo unitario de la mercanca donada&#58; 
 Si el parmetro costs &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_dona &quot; el sistema debe desplegar un campo de captura para el costo unitario (este es el label del input) del producto donado (float) y guardarlo en&#58; eatc-unit_cost&#160; 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta exito el parmetro costs tiene como valor eatc_dona ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) ).&#160; Entonces el sistema debe desplegar un input de datos que permita el ingreso de nmeros flotantes (con dos cifras decimales) para que el usuario digite el costo unitario de lo que se dona que se donan. 

&#160; 
 [Input&#58; float] Digitacin del porcentaje del impuesto al valor agregado (IVA) aplicable&#58; 
 Si el parmetro taxes &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_dona &quot; el sistema debe desplegar un campo de captura para el porcentaje de IVA aplicable (este es el label del input) del producto donado (float solo con dos cifras enteras), y guardarlo en&#58;&#160; [CORREGIR] eatc-VAT_percentage.&#160; Este campo debe presentar como valor por defecto &quot;19&quot; (que corresponde al 19% de IVA que se le aplica a la mayora de los productos susceptibles de donacin. 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta exito el parmetro taxes tiene como valor eatc_dona ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) ).&#160; Entonces el sistema debe desplegar un input de datos que permita el ingreso de nmeros flotantes (con dos cifras decimales) para que el usuario digite el el porcentaje del IVA. El sistema sugiere la cifra &quot;19&quot; en el respectivo campo de captura. El usuario podr modificarla o dejarla tal como se sugiere. 

&#160; 
 Agregar productos&#58; 
 El botn de agregar productos guarda la informacin del mismo (para su registro ) y la muestra en el listado de &quot; Contenido del anuncio&quot; . 

&#160; 
 Contenido del anuncio&#58; 
 Listado de los productos que han sido agregados al anuncio, en donde se muestra el nombre del producto (eatc_odds. eatc-name ) , la cantidad digitada ( eatc-quantity ) la causal de baja del producto ( eatc-return_cause ) y el peso total en KG ( eatc-odd_total_weight_kg ). Este listado deber ser accionable, de tal manera que al hacer click en una de sus lneas el producto en cuestin pueda ser editado&#160; o borrado. 

&#160; 
 Editar productos&#58; 
 Haciendo clic en la lnea del listado de productos ( Contenido del anuncio ), el usuario podr editar cantidades , causales de baja del producto . y dems inputs paramtricos (segn sea el caso) o eliminar la lnea de producto. 
 &#123;&#123;URL_entorno_donante&#125;&#125;/crd/ &#123;&#123; _DOM.cua_master&#125;&#125; /?_tabla= eatc_dona &amp;_operacion=update&amp;&#123;&#123;parametros_editados&#125;&#125;&amp;WHERE _id=&#123;&#123;_id_producto_a_editar&#125;&#125; 

&#160; 
 Borrar productos&#58; 
 Haciendo clic en el botn de borrar de un producto en particular de la lista de productos agregados, el sistema debe realizar el siguiente llamado al CRD para borarro de eatc_dona . 
 &#123;&#123;URL_entorno_donante&#125;&#125;/crd/ &#123;&#123; _DOM.cua_master&#125;&#125; /?_tabla= eatc_dona &amp;_operacion=delete&amp;WHERE _id=&#123;&#123;_id producto_a_borrar&#125;&#125; 

&#160; 
 Registro del anuncio de donacin&#58; 
 Con la informacin de encabezado ( generada por el sistema , tomada de la informacin de la cuenta ,&#160; tomada del maestro de puntos de donacin y digitada ) y cuyo carcter ser repetitivo a lo largo de los registros de un mismo anuncio; y&#160; con la informacin de detalle que se toma del maestro de productos susceptibles a ser donados ,&#160; las cantidades digitadas , los clculos a partir de las cantidades, los selectores de causales de baja y otros inputs paramtricos (segn sea el caso),&#160; se procede a realizar el registro de detalle del anuncio de donacin (eatc_dona) de la siguiente manera&#58; 
&#160; 
 Informacin de encabezado genera el sistema 
 eatc-dona_header_code = Cdigo de la cabecera del anuncio de donacin (lo genera la App para que sea nico) 
 eatc-date_time = $current_date Fecha y hora del anuncio de donacin en formato&#58; AAAAMMDDHHMMSS 
 eatc-date_time_2 = $current_date Fecha del anuncio de donacin en formato&#58; AAAA-MM-DD 
 ***NUEVO*** 
 eatc_cua_origin = $DOM.cua_user //Cuenta desde la cual se genera el anuncio de donacin que corresponde a la cua_user de la App. 
&#160; 
 [A TENER EN CUENTA POR EL AJUSTE DE EDICIN DE COORDENADAS] Informacin de encabezado que se toma del maestro de puntos de donacin (eatc_pods) 
 eatc-pod_id = Identificador nico del punto de donacin ( eatc_pods.eatc-id ) =&gt; Sigue tal cual como estaba antes.&#160; Al colocar este cdigo el sistema lo toma para que en la creacin del eatc_dona_headers (que se activa con el botn&#58; Anunciar Donacin) tome los datos de ubicacin que se debieron editar en el eatc_pods al agregar el primer producto. 
&#160; 
 Informacin de encabezado que se toma del maestro de la informacin de la cuenta (eatc_cua) ***SE DEJA ESTA CONSULTA HASTA IMPLEMENTAR REGISTRO DEL CLIENTE EN EL ERP*** 
 eatc_donor_code = Proveedor Nit. eatc_cua . customer__eatc_clientes__partyidentification ( https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= [cua] )=&gt; la informacin de la CUA se toma del DOM 
 eatc_donor = eatc_cua.name https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;customer__eatc_clientes__partyidentification=eatc_donor_code //Con el eatc_donor_code, se realiza una consulta al WS de Cuentas (eatc_cua) y se coloca el &quot; name &quot; 
 Nota&#58; Si evaluando la informacin de la cuenta respectiva (cua_user) ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua]), se establece que la cuenta est habilitada para editar coordenadas edit_coordinates=si ), este valor ser igual al parmetro eatc-name de eatc_pods ( eatc_donor =eatc_pods.eatc_name) 
&#160; 
 Informacin de encabezado que se digita 
 [INPUT] eatc-doc = Documento soporte de la transaccin (se utiliza cuando se tiene un documento soporte que no puede utilizarse como cdigo del encabezado) o a peticin del cliente. 
&#160; 
 Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds)&#58; buscador de productos (o de otros maestros asociados) 
 eatc-odd_id = Identificador nico del producto o artculo donado ( eatc_odds.eatc-id ). Si eatc_cua. eatc_odds_app = eatc_dona_app , el dato que se lleva a este campo es el mismo nombre del artculo, sin espacios ni caracteres especiales.&#160; 
 [CORREGIR] eatc-odd_name = Nombre o descripcin del producto a susceptible de donacin ( eatc_odds.eatc-odd_name ) Si eatc_cua. eatc_odds_app = eatc_dona_app , el dato que se lleva a este campo es lo que digita el usuario en el campo de texto respectivo 
 [CORREGIR] eatc-odd_code = Cdigo internacional del artculo o producto susceptible a ser donado ( eatc_odds.eatc-odd_code ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco (eatc-code = &quot;&quot;) . 
 [CORREGIR] eatc-odd_code_type = Tipo del cdigo internacional del artculo o producto susceptible a ser donado (ejemplo&#58; EAN8, EAN13, UPC...&#58; ( eatc_odds.eatc-odd_code_type )). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
 origin_odds_typology_a = Primera tipologa consignada en el origen del producto susceptible a ser donado ( atc_odds.eatc-odd_typology_a ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
 origin_odds_typology_b = Segunda tipologa consignada en el origen del producto susceptible a ser donado ( atc_odds.eatc-odd_typology_b ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
 origin_odds_typology_c = Tercera tipologa consignada en el origen del producto susceptible a ser donado ( atc_odds.eatc-odd_typology_c ). Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
&#160; 
 [CORREGIR] [ESTOS TRES NO SE ENVAN EN EL JSON] 
 eatc-height_cm = Altura unitaria en centmetros del artculo o producto susceptible a ser donado ( eatc_odds.eatc-height_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
 eatc-width_cm = Ancho unitario en centmetros del artculo o producto susceptible a ser donado (eatc_odds.eatc-width_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
 eatc-length_cm = Longitud unitaria en centmetros del artculo o producto susceptible a ser donado (eatc_odds.eatc-length_cm) . Si eatc_cua. eatc_odds_app = eatc_dona_app este dato se deja vaco. 
&#160; 
 [LOS ANTERIORES TRES NO SE ENVAN EN EL JSON] 
&#160; 
 Informacin de detalle que se toma del maestro de productos susceptibles a ser donados (eatc_odds) o de otros maestros asociados) a partir de los resultados del buscador de productos y parmetros del sistema 
 Peso unitario en kilogramos del artculo o producto donado&#58; eatc-odd_unit_weight_kg.&#160; 
 Para tomar este dato tenemos las siguientes opciones&#58; 
 El dato se encuentra en el maestro de productos ( eact_odds. eatc-odd_unit_weight_kg )&#58; esta circunstancia se da si el parmetro odds_weight de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ,&#160; tiene como valor&#58; eatc_odds 
 El dato se encuentra en un maestro de conversin a kg (se enva el eatc-odd_id al mismo parmetro de del maestro eatc_odds_weight para traer eatc-odd_unit_weight_kg) &#58;&#160; esta circunstancia se da si el parmetro odds_weight &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; eatc_odds_weight 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta &quot;exito&quot; el parmetro odds_weight tiene como valor eatc_odds_weight ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) cosa que no es cierta (el valor de ese parmetro es eatc_dona ), as que se debe suponer inyectndola en el cdigo).&#160; Entonces el sistema debe realizar la siguiente bsqueda, tomando el eatc-odd_id que se tom en el selector (suponiendo que eatc-odd_id sea 243448 )&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_odds_weight?eatc-odd_id=243448 para tomar lo que retorna el parmetro eatc-odd_unit_weight_kg que en este ejemplo es &quot;2&quot; 
&#160; 
 El dato se toma en la donacin&#58; se toma del input respectivo realizado en la APP &#58;&#160; esta circunstancia se da si el parmetro odds_weight &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_dona &quot; 

&#160; 
 Costo unitario del artculo o producto donado&#58; eatc-unit_cost. 
 Para tomar este dato tenemos las siguientes opciones&#58; 
 El dato se encuentra en el maestro de productos ( eatc_odds. eatc-unit_cost )&#58; esta circunstancia se da si el parmetro costs de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_odds &quot; 
 Ejemplo&#58;&#160; 
 Para la cuenta makro el parmetro costs tiene como valor eatc_odds ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=makro &#160; (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=makro) ).&#160; Entonces el sistema debe realizar la siguiente bsqueda, tomando el eatc-odd_id que se tom en el selector (suponiendo que eatc-odd_id sea 2704 )&#58; https&#58;//devdonantes.eatcloud.info/api/makro/eatc_odds? eatc-id = 2704 &#160;&#160; &#160;para tomar lo que retorna el parmetro eatc-unit_cost que en este ejemplo es &quot; 2829 &quot; 
 El dato se encuentra en un maestro de costos (se enva el eatc-odd_id al mismo parmetro de del maestro eatc_odds_cost&#160; para traer eatc-odd_unit_cost) &#58;&#160; esta circunstancia se da si el parmetro costs &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_odds_costs &quot; 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta exito el parmetro costs tiene como valor eatc_odds_costs ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) cosa que no es cierta (el valor de ese parmetro es eatc_dona ), as que se debe suponer inyectndola en el cdigo).&#160; Entonces el sistema debe realizar la siguiente bsqueda, tomando el eatc-odd_id que se tom en el selector (suponiendo que eatc-odd_id sea 243448 )&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_odds_costs?eatc-odd_id=243448 &#160; para tomar lo que retorna el parmetro eatc-odd_unit_cost que en este ejemplo es &quot;10000&quot; 
&#160; 
 El dato se toma en la donacin&#58; se toma del input respectivo realizado en la APP &#58;&#160; esta circunstancia se da si el parmetro costs &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_dona &quot; 

&#160; 
 Porcentaje del impuesto al valor agregado aplicable al artculo&#58; eatc-VAT_percentage.&#160;&#160; 
 Para tomar este dato tenemos las siguientes opciones&#58; 
 El dato se encuentra en el maestro de productos ( eatc_odds. eatc-vat_percentage )&#58; esta circunstancia se da si el parmetro taxes de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_odds &quot; 
 El dato se encuentra en un maestro de costos (se enva el eatc-odd_id al mismo parmetro de del maestro eatc_odds_cost&#160; para traer eatc-odd_unit_cost) &#58;&#160; esta circunstancia se da si el parmetro taxes &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_odds_costs &quot; 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta exito el parmetro taxes tiene como valor eatc_odds_costs ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) cosa que no es cierta (el valor de ese parmetro es eatc_dona ), as que se debe suponer inyectndola en el cdigo).&#160; Entonces el sistema debe realizar la siguiente bsqueda, tomando el eatc-odd_id que se tom en el selector (suponiendo que eatc-odd_id sea 243448 )&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_odds_costs?eatc-odd_id=243448 &#160; para tomar lo que retorna el parmetro eatc-vat_percentage que en este ejemplo es &quot;19&quot; 
&#160; 
 El dato se encuentra en un maestro de impuestos&#160; (se enva el eatc-odd_id al mismo parmetro de del maestro eatc_odds_taxes&#160; para traer eatc-vat_percentage) &#58;&#160; esta circunstancia se da si el parmetro taxes &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) , tiene como valor&#58; &quot; eatc_odds_taxess &quot; 
 Ejemplo&#58;&#160; 
 Se supone que para la cuenta exito el parmetro taxes tiene como valor eatc_odds_taxes ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito) cosa que no es cierta (el valor de ese parmetro es eatc_dona ), as que se debe suponer inyectndola en el cdigo).&#160; Entonces el sistema debe realizar la siguiente bsqueda, tomando el eatc-odd_id que se tom en el selector (suponiendo que eatc-odd_id sea 243448 )&#58; https&#58;//devdonantes.eatcloud.info/api/exito/eatc_odds_taxes?eatc-odd_id=243448 &#160; para tomar lo que retorna el parmetro eatc-vat_percentage que en este ejemplo es &quot;19&quot; 
 El dato se toma en la donacin&#58; se toma del input respectivo realizado en la APP &#58;&#160; esta circunstancia se da si el parmetro taxes &#160; de la cuenta respectiva ( ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name= &#123;&#123;cua_user&#125;&#125; ( anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=[cua] ) ), tiene como valor&#58; &quot; eatc_dona &quot; 

&#160; 
 Informacin que se toma a partir de inputs y selectores de la APP 
 [INPUT] eatc-odd_quantity = Cantidad del producto o artculo donado (cantidad digitada por el usuario para generar el anuncio) 
 [INPUT] eatc-odd_original_quantity = Cantidad del producto o artculo donado&#58; Se toma del input anterior 
 [DROPDOWN] eatc-return_cause = Causa de Devolucion Causa Devolucion DESC // Descripcin del causal de devolucin 
 eatc-return_cause_code = Causa de Devolucion Causa Devolucion ID //Cdigo del causal de devolucin se toma a partir del anterior dropdown 
 [DROPDOWN] eatc-contains_alergens = definicin si la donacin contiene alrgenos. 
 ***NUEVO*** [DATE DATEPICKER] eatc-closer_expiration_date = fecha ms prxima de expiracin del producto (o los productos) anunciado(s). 
&#160; 
 Informacin que se toma a partir de clculos a partir de los inputs y selectores de la APP 
 eatc-odd_total_weight_kg = Peso total en kilogramos del artculo o producto donado, es decir, peso unitario por cantidad donada (eatc_odds_kg.valor_kg*eatc-odd_quantity) 
 eatc-total_cost = Costo total del o de los productos o artculos donados ( eatc-quantity * eatc-unit_cost ) 
 eatc-original_VAT = Valor original total del impuesto a las ventas (eatc-odd_original_quantity*eatc-odd_unit_cost*eatc-VAT_percentage) 
 eatc-total_VAT = Valor definitivo total del impuesto a las ventas&#160; (eatc-odd_quantity*eatc-odd_unit_cost*eatc-VAT_percentage), despus del proceso de verificacin.&#160; Como aun no se ha efectuado la verificacin es similar a eatc-original_VAT 
&#160; 
 [CORREGIR] Datos que se pasan con cero (se deben enviar as porque la tabla tiene que recibir nmeros) 
 eatc-odd_total_height_cm = 0 // No aplica por no tener datos 
 eatc-odd_total_width_cm = 0 // No aplica por no tener datos 
 eatc-odd_total_length_cm = 0 // No aplica por no tener datos 
 eatc-odd_total_volume_cm3 = 0 // No aplica por no tener datos 
&#160; 
 Datos que se pasan vacos 
 [CORREGIR] eatc -odd_ typology_a = Primera tipologa EatCloud (equivalente) del artculo o producto donado 
 [CORREGIR] eatc- odd_ typology_b = Segunda tipologa EatCloud (equivalente) del artculo o producto donado 
 [CORREGIR] eatc- odd_ typology_c = Tercera tipologa EatCloud (equivalente) del artculo o producto donado 
 eatc-odd_state = //Estado producto&#58; certificable, rechazado. Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin 
 eatc-odd_rejection_cause = //Causal del rechazo de un producto donado.&#160; Lo incorpora la App en el proceso de chequeo o verificacin del anuncio de donacin 
&#160; 
 [NUEVO&#58; observaciones para la recogida]&#58;&#160; 
 eatc-warning = OBSERVACIONES PARA LA RECOGIDA //A tener en cuenta&#58; tambin se coloca informacin segn lo planteado aqu 
&#160; 
 PENDIENTE DE DEFINICIONES (Por el momento dejarlos vacos)&#58;&#160; 
 eatc-odd_external_code = Cdigo del artculo entregado por el proveedor del mismo&#58; se utiliza cuando un donante informa mercanca que pertenece a un tercero identificado en el sistema (que debera ser una nueva cuenta&#160; (CUA) en el sistema) 
&#160; 
 BOTN &quot;AGREGAR PRODUCTO&quot; ***REVISAR DINAMIZACIN A PARTIR DE CUENTA MAESTRA*** 
&#160; 
 Si la cuenta no permite editar las coordenadas ( edit_coordinates ) o si la permite pero no se editaron 
 Al presionar este botn la app se debe asegurar que todos los registros de detalle (eatc_dona) hallan sido realizados mediante el API respectiva&#160;&#160; 
 Mtodo POST&#58; 
 &#123;&#123;URL_entorno_donante&#125;&#125;/crd/ &#123;&#123; _DOM.cua_master&#125;&#125; /?_tabla= eatc_dona &amp;_operacion=insert 
&#160; 
 Si la cuenta permite editar las coordenadas ( edit_coordinates ) y las mismas se editaron 
 Se realiza el anterior registro&#160; y cuando se registra el primer producto se realizan las siguientes operaciones&#58; 
&#160; 
 Edicin registro en eatc_pods&#58; 
 Mtodo POST 
 https&#58;//devdonantes.eatcloud.info/crd/ &#123;&#123; _DOM.cua_user&#125;&#125; /?_tabla=eatc_pods_coordinates&amp;_operacion=update&amp; &#123;&#123; Parametros edicin en eatc_pods &#125;&#125; &amp;WHEREeatc-id=&#123;&#123; eatc_pods. eatc-id &#125;&#125; 
&#160; 
 Se debe validar que la edicin halla sido realizada correctamente porque ser muy importante a la hora de generar los anuncios de donacin (anunciar donacin). 
&#160; 
 Creacin del registro en eatc_pods_coordinates&#58; 
 Mtodo POST 
 https&#58;//devdonantes.eatcloud.info/crd/ &#123;&#123; _DOM.cua_user&#125;&#125; /?_tabla=eatc_pods_coordinates&amp;_operacion=insert&amp; &#123;&#123; Parametros edicin en eatc_pods &#125;&#125; 
&#160; 
 BOTN ANUNCIAR DONACIN ***REVISAR DINAMISMO A PARTIR DE _DOM.CUA_USER 
 Se debe llamar al proceso en el servidor que genera los encabezados del anuncio de donacin , para que corra, y una vez corra, debe llamar al proceso que genera el match para el presente anuncio de donacin. 
 Se debe verificar que los procesos que se llaman, reciben como parmetro _DOM.cua_user para la creacin de los mismos y su match en mltiples cuentas maestras. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdeprecado-edici%C3%B3n-de-coordenadas%2F4034218213-unnamed.png&ow=1840&oh=882, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fdeprecado-edici%C3%B3n-de-coordenadas%2F4034218213-unnamed.png&ow=1840&oh=882 

 122.000000000000 

 DEPRECADO: CREACIN DE ANUNCIO DE DONACIN (EATC_DONA_UPL) LEGACY