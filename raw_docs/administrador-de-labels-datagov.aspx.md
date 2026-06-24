# administrador-de-labels-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 INTRODUCCIN GENERAL 
 Esta ser una herramienta que servir para configurar los " copies" de los labels o etiquetas que maneja la plataforma en varios idiomas, lo cual es necesario para nuestro proceso comercial (microcopy) y de internacionalizacin. 

 Esta funcionalidad se debe incorporar en la plataforma datagov de eatcloud:  https://datagov.eatcloud.info/bo/eatcloud 

 La implementacin debe apoyarse en los aprendizajes e implementaciones realizadas para configurar el administrador de funcionalidades y en principio el trabajo debe ser de una naturaleza muy similar, dado que constar de un CRUD para la creacin de etiquetas, un CRUD para la configuracin de la etiqueta por idioma, la incorporacin de identificadores para dinamizar las etiquetas, y la creacin de un script que lea la configuracin regional del equipo y de acuerdo a ella le despliegue al usuario las etiquetas o labels en su idioma (siendo el idioma por defecto el Ingls) 

 CRUD DE LABELS (ETIQUETAS)  
 Es una funcionalidad para registrar las etiquetas o labels de las diversas plataformas, para que a partir de este maestro, se le puedan asignar traducciones a cada etiqueta.  

 La estructura de datos de los labels debe ser muy similar a  de funcionalidades: https://datagov.eatcloud.info/api/eatcloud/eatc_funcionalidades?_campos y por lo tanto su crud muy similar 

 https://datagov.eatcloud.info/api/eatcloud/eatc_labels?_campos   

 Insert 
 {{parmetros de creacin de eatc_labels }} 

 idlabel : ( eatc_labels. idlabel ): obligatorio 
 label :  ( eatc_labels. label ), cuando se llene esta informacin en este punto se debe colocar cmo est el "label" actualmente en la plataforma, es decir, cmo est en el cdigo html descrita la etiqueta establecida (para tener una clara referencia del label sobre el cul se est trabajando): Obligatorio 
 plataforma :  ( eatc_labels. plataforma ): funciona el mismo listado de plataformas utilizado para el crud de funcionalidades 
 tipo :  ( eatc_labels. tipo ): es ideal que concuerden de alguna manera con los elementos de diseo definidos en el boilerplate: http://repograf.eatcloud.info/boilerplate.html : Obligatorio. 
 descripcion : descripcin del label o etiqueta, que debe idealmente contener la utilidad de la misma ( eatc_labels. descripcion ): opcional. 
 estado : "activo" / "inactivo" ( eatc_labels. estado ) 
 lastupdate : timestamp (en formato: AAAA-MM-DD HH:MM:SS )de la fecha y hora de creacin/actualizacin ( eatc_labels. lastupdate ): obligatorio. 

 [***] Se guarda la informacin en el object store eatc_labels de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_labels&_operacion=insert& {{Parmetros creacin en eatc_labels }} 

 Update 
 {{parmetros para el update de eatc_labels }} 

 label :  ( eatc_labels. label ), cuando se llene esta informacin en este punto se debe colocar cmo est el "label" actualmente en la plataforma, es decir, cmo est en el cdigo html descrita la etiqueta establecida (para tener una clara referencia del label sobre el cul se est trabajando). Obligatorio. 
 plataforma :  ( eatc_labels. plataforma ): funciona el mismo listado de plataformas utilizado para el crud de funcionalidades. Obligatorio 
 tipo :  ( eatc_labels. tipo ): es ideal que concuerden de alguna manera con los elementos de diseo definidos en el boilerplate: http://repograf.eatcloud.info/boilerplate.html . Obligatorio 
 descripcion : descripcin del label o etiqueta, que debe idealmente contener la utilidad de la misma ( eatc_labels.descripcion ). Opcional. 
 estado : "activo" / "inactivo" ( eatc_labels. estado ) 
 lastupdate : timestamp de la fecha y hora de actualizacin ( eatc_labels. lastupdate ). Obligatorio 

 [***] Se guarda la informacin en el object store eatc_labels de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_labels&_operacion=insert& {{Parmetros el uptdate de eatc_labels }}&WHEREidlabel={{ eatc_labels.idlabel }} 

 CRUD DE CONFIGURACIN DE LABEL (IDIOMA, CUENTA) 
 Es una funcionalidad para registrar, a partir de los labels incorporados a la persistencia ( https://datagov.eatcloud.info/api/eatcloud/eatc_labels?_campos ), el copy en espaol y en los diferentes idiomas de la plataforma ( https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* ) de los labels. 

 Selector - Buscador del "label" 
 El sistema consultando los datos creados en el maestro de labels, ( https://datagov.eatcloud.info/api/eatcloud/eatc_labels?_id=_* ), le debe permitir al usuario una manera sencilla de encontrar un label especfico (seleccionar, buscar) para efectuar el ingreso de su  copy en los diferentes idiomas disponibles (mostrando toda su informacin: idlabel , label , plataforma , tipo , descripcion , estado , lastupdate ).  En esta vista, tambin el usuario debe poder establecer (de manera visual) si el label ya tiene copy en los idiomas establecidos, y en caso de tenerlo, poderlo editar. 

 Selector - buscador de idiomas 
 Una vez seleccionado el label al cual se le debe incorporar el copy, el sistema debe permitir seleccionar el idioma en el cual se incorporar ( https://datagov.eatcloud.info/api/eatcloud/eatc_languages?_id=_* ; mostrar en el selector: native_name , llevar al registro el parmetro iso2 ).  El dato obtenido del selector-buscador de idiomas se llevar como registro a eatc_config_label. language (obligatorio) .  

 ***NUEVO*** Selector - buscador de pases 
 Una vez seleccionado el label al cual se le debe incorporar el copy, el sistema debe permitir de manera opcional, seleccionar un pas al cual le aplicar la internacionalizacin particular  ( https://datagov.eatcloud.info/api/eatcloud/eatc_countries?_id=_* ; mostrar en el selector: name , llevar al registro el parmetro iso2 ).  El dato obtenido del selector-buscador de pais se llevar como registro a eatc_config_label. country (opcional) .  

 Selector - buscador de cuentas 
 De manera opcional, para algunas cuentas se deber poder permitir seleccionar un label especfico para ellas (como por ejemplo, para llamar a las clasificaciones dentro de la plataforma y tambin a los mismos puntos de donacin: algunas cuentas los llamarn "Almacenes" y otras "Restaurantes" por ejemplo, y para ello el sistema deber permitir seleccionar (de manera opcional), una cuenta a la cual especficamente se le desea configurar una etiqueta.  Este valor puede ir al registro vaco y el selector - buscador del dato de este registro obtiene sus informacin de: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?_id=_ * name y se lleva al parmetro eatc_config_label. cua (opcional) .  

 La combinacin " idlabel " + " language " (iso2: cdigo de dos dgitos del idioma) + country " (iso2: cdigo de dos dgitos del pas) + " cua " (si existe)  debe ser nica, de tal manera que no existan traducciones duplicadas en el sistema. 

 Introduccin del copy del label 
 El sistema debe proporcionar un campo de captura de texto para incorporar el " copy " en el lenguaje establecido al " label " seleccionado. En espaol ( iso3= es ), se debe sugerir el dato " label " del maestro de labels ( eatc_label. label ) como el " copy " a introducir.  

 Mejora a futuro: sugerencia de traduccin 
 Utilizando un API de traduccin, se le debe enviar el label  ( eatc_label. label ) en espaol para obtener una sugerencia de la traduccin en el idioma seleccionado (diferente al espaol). 
 La informacin digitada se deber llevar al parmetro eatc_config_label. copy   

 Insert 
 {{parmetros de creacin de eatc_config_labels }} 

 idlabel: se obtiene de eatc_labels. idlabel , obligatorio. Hace parte de clave compuesta. 
 label: se obtiene de eatc_labels. label , obligatorio. 
 plataforma: se obtiene de eatc_labels. plataforma , obligatorio. 
 tipo: se obtiene de eatc_labels. tipo , obligatorio. 
 descripcion : se obtiene de eatc_labels. descripcion , opcional. 
 estado: se obtiene de eatc_labels. estado , obligatorio. 
 language : se obtiene del input de la funcionalidad ( eatc_languages. iso2 ) , obligatorio. Hace parte de clave compuesta. 
 country : se obtiene del input de la funcionalidad ( eatc_countries. iso2 ) , opcional. Hace parte de clave compuesta. 
 cua : se obtiene del input de la funcionalidad ( eatc_cua. name ) , opcional. Hace parte de clave compuesta. 
 copy : se obtiene del input de la funcionalidad. Obligatorio. 
 lastupdate: se obtiene del input de la funcionalidad. Obligatorio. 

 [***] Se guarda la informacin en el object store eatc_config_label de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_config_label&_operacion=insert& {{Parmetros creacin en eatc_vistas }} 

 Update 
 {{parmetros para el update de eatc_config_label }} 

 language : se obtiene de eatc_labels. estado , obligatorio. Hace parte de clave compuesta. 
 cua : se obtiene de eatc_cua. name , opcional. Hace parte de clave compuesta. 
 copy : se obtiene del input de la funcionalidad. Obligatorio. 
 lastupdate: se obtiene del input de la funcionalidad. Obligatorio. 

 [***] Se guarda la informacin en el object store eatc_config_label de la cuenta eatcloud: 

 Mtodo POST  
 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_config_label&_operacion=insert& {{Parmetros el uptdate de eatc_config_label }}&WHEREidlabel={{ idlabel }} 

 Script para dinamizacin de labels 
 El script deber en primera medida evaluar la cuenta ( cua ), para establecer si el label tiene un copy especfico para la misma ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&cua={{cua}} ); en caso de no tenerla, como segundo paso,  el sistema debe obtener el idioma del browser o del sistema (cdigo de dos dgitos), para traer el idioma correspondiente a dicha configuracin ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&language={{codigo_2_digitos}} ).  El idioma por defecto ser ingls, de tal manera que si el idioma de la configuracin del browser o sistema operativo es diferente (inicialmente) al espaol y el ingls, entonces el idioma que se despliega es el Ingls ( https://datagov.eatcloud.info/ api/eatcloud/eatc_config_label?idlabel={{idlabel}}&language=en ). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ADMINISTRADOR DE "LABELS" - DATAGOV