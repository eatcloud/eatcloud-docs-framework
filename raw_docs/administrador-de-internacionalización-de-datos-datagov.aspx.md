# administrador-de-internacionalización-de-datos-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 INTRODUCCIN GENERAL 
 Esta ser una herramienta que servir para internacionalizar datos de diversos maestros que requieren configuracin en diferentes idiomas. 

 Esta funcionalidad se debe incorporar en la plataforma datagov de eatcloud:  https://datagov.eatcloud.info/bo/eatcloud 

 La implementacin debe apoyarse en los aprendizajes e implementaciones realizadas para configurar el administrador de funcionalidades y el administrador de etiquetas en principio el trabajo debe ser de una naturaleza muy similar, dado que constar de una tabla de maestros a internacionalizar ( eatc_internationalize_mt que inicialmente se carga manualmente pero que se asemeja al maestro que se crea con CRUD para la creacin de etiquetas),  y un CRUD para internacionalizacin de los datos (que se asemeja al CRUD para la configuracin de la etiquetas por idioma).  Este desarrollo en particular no necesitar (en principio) de un script para cambiar cambiar el dato segn el idioma, ya que se documenta en cada funcionalidad que requiera datos internacionalizados, de una nueva manera de obtenerlos haciendo consultas a las nuevas tablas creadas. 

 CRUD DE INTERNACIONALIZACIN DEL DATO (IDIOMA, PAS, CUENTA) - EATC_INTERNATIONALIZE_DT 

 Es una funcionalidad para registrar, a partir de los maestros y campos a internacionalizar incorporados a la persistencia ( https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_mt?_id=_* ), la equivalencia de sus respectivos datos en los idiomas habilitados para la plataforma. 

 Selector - Buscador del "maestro y campo" 
 El sistema construye un selector nico con los datos que obtiene de la consulta: https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_mt?_id=_* (en el selector se debe mostrar los datos eatc_internationalize_mt. eatc_enviroment eatc_internationalize_mt. eatc_mt eatc_internationalize_mt. eatc_int_field ) permitindole de manera sencilla al usuario realizar una seleccin nica del registro en maestro que se consulta ( https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_mt?_id=_* ).  Todos los datos consultados se llevarn al registro del dato internacionalizado ( eatc_internationalize_dt ) de la siguiente manera: 

eatc_id => eatc_internationalize_dt. eatc_mt_id 
eatc_enviroment => eatc_internationalize_dt. eatc_enviroment 
eatc_cua => eatc_internationalize_dt. eatc_cua_mt 
eatc_mt => eatc_internationalize_dt. eatc_mt 
eatc_int_field => eatc_internationalize_dt. eatc_int_field 

 para posteriormente  con ellos armar el selector que se indica a continuacin. 

 Selector - Buscador del "dato" - eatc_data 
 A partir de la seleccin nica anterior, el sistema debe realizar la siguiente consulta para mostrar los datos (eatc_data ) a internacionalizar a travs de un selector. 

 https://{{eatc_internationalize_mt. eatc_enviroment }}.eatcloud.info/api/{{eatc_internationalize_mt. eatc_cua }}/{{eatc_internationalize_mt. eatc_mt }}?_id=_* mostrando en el selector la informacin que trae la consulta en el campo eatc_internationalize_mt. eatc_int_field 

 El usuario podr seleccionar un dato especfico del maestro consultado, para llevarlo al registro eatc_internationalize_dt. eatc_data 

 De igual manera el identificador particular del registro (_id) se lleva al registro eatc_internationalize_dt. eatc_data_id 

 Selector - buscador de idiomas 
 Una vez seleccionado el dato a internacionalizar, el sistema debe permitir seleccionar el idioma en el cual se incorporar ( https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* ; mostrar en el selector: name , llevar al registro el parmetro iso2 ).  El dato obtenido del selector-buscador de idiomas se llevar como registro a eatc_internationalize_dt . eatc_language (obligatorio) .  

 Selector - buscador de pases 
 Una vez seleccionado el label al cual se le debe incorporar el copy, el sistema debe permitir de manera opcional, seleccionar un pas al cual le aplicar la internacionalizacin particular  ( https://datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_* ; mostrar en el selector: name , llevar al registro el parmetro iso2 ).  El dato obtenido del selector-buscador de pais se llevar como registro a eatc_internationalize_dt . eatc_country ( opcional) .  

 Selector - buscador de cuentas 
 De manera opcional, para algunas cuentas se deber poder permitir seleccionar un label especfico para ellas (como por ejemplo, para llamar a las clasificaciones dentro de la plataforma y tambin a los mismos puntos de donacin: algunas cuentas los llamarn "Almacenes" y otras "Restaurantes" por ejemplo, y para ello el sistema deber permitir seleccionar (de manera opcional), una cuenta a la cual especficamente se le desea configurar una etiqueta.  Este valor puede ir al registro vaco y el selector - buscador del dato de este registro obtiene sus informacin de: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?_id=_ * name y se lleva al parmetro eatc_internationalize_dt . eatc_cua (opcional) .  

 La combinacin  " eatc_mt_id " + " eatc_int_field " + " eatc_data_id " + " eatc_language " (iso2: cdigo de dos dgitos del idioma) + " eatc_country " (iso2: cdigo de dos dgitos del pas) + " eatc_cua " (si existe)  debe ser nica, de tal manera que no existan traducciones duplicadas en el sistema (el sistema debe controlar duplicidad). 

 Introduccin del dato internacionalizado 
 El sistema debe proporcionar un campo de captura de texto para incorporar el " dato internacionalizado (eatc_int_data) " en el lenguaje establecido al " eatc_data " seleccionado. En espaol ( iso3= es ), se debe sugerir el dato " eatc_data " seleccionado en la  funcionalidad respectiva como el " eatc_internationalize_dt. eatc_int_data " a introducir.  

 Mejora a futuro: sugerencia de traduccin 
 Utilizando un API de traduccin, se le debe enviar el dato  ( eatc_internationalize_dt. eatc_data ) en espaol para obtener una sugerencia de la traduccin en el idioma seleccionado (diferente al espaol). 

 La informacin digitada se deber llevar al parmetro eatc_internationalize_dt . eatc_int_data   

 Insert 
 {{parmetros de creacin de eatc_internationalize_dt }} 

 eatc_mt_id = eatc_internationalize_mt. eatc_id , obligatorio. Hace parte de la clave compuesta  
 eatc_enviroment = eatc_internationalize_mt. eatc_enviroment , obligatorio. 
 eatc_cua_mt = eatc_internationalize_mt. eatc_cua , obligatorio. 
 eatc_mt = eatc_internationalize_mt. eatc_mt , obligatorio. 
 eatc_int_field = eatc_internationalize_mt. eatc_int_field , obligatorio. Hace parte de la clave compuesta  
 eatc_data_id : se obtiene del input de la funcionalidad, obligatorio. Hace parte de la clave compuesta  
 eatc_data : se obtiene del input de la funcionalidad, obligatorio. 
 eatc_language : se obtiene del input de la funcionalidad ( eatc_languages. iso2 ) , obligatorio. Hace parte de clave compuesta. 
 eatc_country : se obtiene del input de la funcionalidad ( eatc_countries. iso2 ) , opcional. Hace parte de clave compuesta. 
 eatc_cua : se obtiene del input de la funcionalidad ( eatc_cua. name ) , opcional. Hace parte de clave compuesta. 
 eatc_int_data : se obtiene del input de la funcionalidad. Obligatorio. 
 lastupdate : se obtiene del input de la funcionalidad. Obligatorio. 

 [***] Se guarda la informacin en el object store eatc_internationalize_dt de la cuenta eatcloud: 

 Mtodo POST  
 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla= eatc_internationalize_dt &_operacion=insert& {{Parmetros creacin en eatc_internationalize_dt }} 

 Listado de datos internacionalizados 
 A medida que se van incorporando datos a la tabla de internacionalizacin de datos, se debe presentar un listado en donde se relacione cada dato internacionalizado y se indique los idiomas que faltan por incorporar en el registro.  Al seleccionar uno de esos items a editar, se deben abrir los datos que previamente fueron incorporados a saber: 

 eatc_mt_id = eatc_internationalize_mt. eatc_id 
 eatc_enviroment = eatc_internationalize_mt. eatc_enviroment 
 eatc_cua = eatc_internationalize_mt. eatc_cua 
 eatc_mt = eatc_internationalize_mt. eatc_mt 
 eatc_int_field = eatc_internationalize_mt. eatc_int_field 
 eatc_data : se obtiene del input de la funcionalidad, obligatorio. hace parte de la clave compuesta  

 Y se debe permitir editar los dems datos para realizar el update. 

 Update 
 {{parmetros para el update de eatc_internationalize_dt }} 

 eatc_language : se obtiene del input de la funcionalidad ( eatc_languages. iso2 ) , obligatorio. Hace parte de clave compuesta. 
 eatc_country : se obtiene del input de la funcionalidad ( eatc_countries. iso2 ) , opcional. Hace parte de clave compuesta. 
 eatc_cua : se obtiene del input de la funcionalidad ( eatc_cua. name ) , opcional. Hace parte de clave compuesta. 
 eatc_int_data : se obtiene del input de la funcionalidad. Obligatorio. 
 lastupdate : se obtiene del input de la funcionalidad. Obligatorio. 

 [***] Se guarda la informacin en el object store eatc_internationalize_dt de la cuenta eatcloud: 

 Mtodo POST  
 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla= eatc_internationalize_dt &_operacion=insert& {{Parmetros el uptdate de eatc_internationalize_dt }}&WHEREidlabel={{ idlabel }} 

 CRUD DE LABELS (ETIQUETAS) ***ETAPAS POSTERIORES, YA QUE INICIALMENTE SE CARGA MANUALMENTE*** 
 Es una funcionalidad para registrar maestros que requieran internacionalizacin (se debe abordar en etapas posteriores ya que el maestro que ya se carg contiene los maestros que en principio debern ser internacionalizados y en el futuro prximo no se requerirn de muchos nuevos registros en esta estructura).  

 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_mt?_campo 

 Insert 
 {{parmetros de creacin de eatc_internationalize_mt }} 

 eatc_id : ( eatc_internationalize_mt . eatc_id ): obligatorio: lo puede manejar el sistema con un autoincremental 
 eatc_enviroment :  ( eatc_internationalize_mt . eatc_enviroment ), en principio solo tomar los valores "datagov", "beneficiarios" y "devbeneficiarios", pero tambin podr tomar los valores "donantes" y "devdonantes": Selector nico. Obligatorio 
 eatc_cua: ( eatc_internationalize_mt . eatc_cua ), en principio solo tomar el valor "eatcloud": obligatorio 
 eatc_mt: ( eatc_internationalize_mt . eatc_mt ); campo abierto de captura obligatorio en donde se coloca el nombre del maestro 

 [***] Se guarda la informacin en el object store eatc_internationalize_mt de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_internationalize_mt&_operacion=insert& {{Parmetros creacin en eatc_internationalize_mt }} 

 SCRIPT  PARA DINAMIZACIN DE LABELS 
 El script deber en primera medida evaluar la cuenta ( cua ), para establecer si el label tiene un copy especfico para la misma ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&cua={{cua}} ); en caso de no tenerla, como segundo paso,  el sistema debe obtener el idioma del browser o del sistema (cdigo de dos dgitos), para traer el idioma correspondiente a dicha configuracin ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&language={{codigo_2_digitos}} ).  El idioma por defecto ser ingls, de tal manera que si el idioma de la configuracin del browser o sistema operativo es diferente (inicialmente) al espaol y el ingls, entonces el idioma que se despliega es el Ingls ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&language=en ). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ADMINISTRADOR DE INTERNACIONALIZACIN DE DATOS - DATAGOV