# administrador-de-funcionalidades-datagov.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 INTRODUCCIN GENERAL 
 Esta ser una herramienta que servir para configurar las funcionalidades que se visualizan en los diferentes BO y en este entorno para los diferentes perfiles de clientes.  Por esta razn ser una funcionalidad que solo estar disponible para ser operada desde aqu : https://datagov.eatcloud.info/bo 

 La definicin de esta funcionalidad se apoyar en las definiciones y extructuras de datos que se definieron para implementar el administrador de visualizacin de funcionalidades en las diferentes webapps donantes., por lo tanto deber incorporar estructuras de datos similares a estas: 

 https://donantes.eatcloud.info/api/allpods/eatc_vistas?id=_* 
 https://devdonantes.eatcloud.info/api/allpods/eatc_visible_wapp?idvista=_* https://devdonantes.eatcloud.info/api/allpods/eatc_visible_wapp?id_pod=31 https://devdonantes.eatcloud.info/api/allpods/eatc_visible_wapp?id_pod=4159 (con la variacin que esto ya no deber funcionar por punto de donacin sino por perfil de cuenta o pas) 

 Por esta razn esta funcionalidad deber tener dos componentes: un CRUD de vistas y un CRUD de visualizacin de vistas, basados en las anteriores estructuras pero con diferencias en algunos datos y tambin dichas estructuras deberan estar alojadas en el entorno datagov. 

 El abordaje de esta implementacin debe tener en cuenta lo siguiente: en adelante se presenta una definicin ideal.  Se debe procurar que para el 1 de octubre del presente ao se implemente una funcionalidad operativa, as no sea la ideal y que permita la visualizacin selectiva de funcionalidades principalmente en el BO de donantes 

 CRUD DE VISTAS 
 Es una funcionalidad para registrar vistas objeto de la visualizacin selectiva por perfil, y por lo tanto deber funcionar para incorporar los siguientes datos: 

 Insert 
 {{parmetros de creacin de eatc_vistas }} 

 ambiente (quitar) : por practicidad se recomenda tener esta informacin en  el object_store de visualizacin de vistas y no en este 
 vista : nombre de la vista ( eatc_vistas.vista ) (debera crearse un maestro para esto) 
 idvista : se debe evaluar si esto se utiliza o no ( eatc_vistas.idvista ) (debera crearse un maestro para esto) 
 funcionalidad : nombre de la funcionalidad, ( eatc_vistas.funcionalidad ) 
 idfuncionalidad : identificador de la funcionalidad que se lleva al cdigo, ( eatc_vistas.idfuncionalidad ) 
 descripcion : descripcin de la funcionalidad que se lleva a un tooltip, ( eatc_vistas.descripcion ) 
 lastupdate : timestamp de la fecha y hora de creacin ( eatc_vistas.lastupdate ) 

 [***] Se guarda la informacin en el object store eatc_vistas de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/?_tabla=eatc_vistas&_operacion=insert& {{Parmetros creacin en eatc_vistas }} 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_vistas&_operacion=insert& {{Parmetros creacin en eatc_vistas }} 

 Update 
 {{parmetros para el update de eatc_vistas }} 

 vista : "dashboard" ( eatc_vistas.vista ) 
 idvista : se debe evaluar si esto se utiliza o no ( eatc_vistas.idvista ) 
 funcionalidad : nombre de la funcionalidad, ( eatc_vistas.funcionalidad ) 
 descripcion : descripcin de la funcionalidad que se lleva a un tooltip, ( eatc_vistas.descripcion ) 
 lastupdate : timestamp de la fecha y hora de creacin ( eatc_vistas.lastupdate ) 

 [***] Se guarda la informacin en el object store eatc_vistas de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/?_tabla=eatc_vistas&_operacion=update& {{Parmetros el uptdate de eatc_vistas }}&WHEREidfuncionalidad={{ eatc_vistas.idfuncionalidad }} 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_vistas&_operacion=insert& {{Parmetros el uptdate de eatc_vistas }}&WHEREidfuncionalidad={{ eatc_vistas.idfuncionalidad }} 

 CRUD DE VISUALIZACIN DE VISTAS 
 Es una funcionalidad para registrar, a partir de las vistas registradas, su visualizacin en los : 

 Insert 
 {{parmetros de creacin de eatc_visualizacion_vistas }} 

 vista : se toma de un selector nico del maestro de vistas: eatc_vistas.vista ( eatc_visualizacion_vistas.ambiente ) 
 idfuncionalidad : a partir de la anterior seleccin se toma  del maestro de vistas: eatc_vistas.idfuncionalidad   ( eatc_visualizacion_vistas.idfuncionalidad ) 
 funcionalidad : a partir de la seleccin se toma  del maestro de vistas: eatc_vistas.funcionalidad ( eatc_visualizacion_vistas.funcionalidad ) 
 descripcion : a partir de la seleccin se toma  del maestro de vistas: eatc_vistas.funcionalidad ( eatc_visualizacion_vistas.descripcion ) 
 ambiente (***nuevo***) : para este caso el ambiente podr ser "BO" o "DataGov" ( eatc_visualizacion_vistas.ambiente ) 
 tipo_ambiente (***nuevo***) : pruebas, productivo, ambos ( eatc_visualizacion_vistas.tipo_ambiente ) 
 visible : no se entiende muy bien la utilidad de este campo ( eatc_visualizacion_vistas.visible ) 
 eatc_country (***nuevo***) :  no obligatorio se toma de un selector nico  cuyos valores se obtienen de:  https://beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_country=_* ( eatc_visualizacion_vistas.visible ) 
 cua : ser en principio no obligatorio y se tomar como selector del  maestro eatc_cua que reposa en config. https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=_todos   ( eatc_visualizacion_vistas.cua ) 
 cua_vertical : opcional, se toma de la informacin del maestro respectivo en config:  https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&nombre=_todos ( eatc_visualizacion_vistas.cua_vertical ) 
 cua_type: obligatorio, puede en principio tomar dos valores: "free" y "hero". 
 experimental_desde : campo de fecha opcional en formato AAAA-MM-DD , cuando contenga informacin el campo experimental hasta deber tambin contenerla y estas fechas dictarn un periodo de visualizacin experimental de la funcionalidad, en donde la misma se desplegar acompaada de un mtodo para capturar opiniones de dicha funcionalidad y un vnculo a una landing page de enganche comercial 
 experimental_hasta : campo de fecha opcional en formato AAAA-MM-DD (obligatorio si experimental_desde tiene un dato vlido). 
 lastupdate :  en formato AAAA-MM-DD HH:MM:SS, timestamp de la fecha y hora de creacin ( eatc_visualizacion_vistas.lastupdate ) 
 name_pod (quitar) : no se recomienda utilizar en esta estructura 
 login_pod : (quitar) : no se recomienda utilizar en esta estructura 

 [***] Se guarda la informacin en el object store eatc_sale_order de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/?_tabla=eatc_visualizacion_vistas&_operacion=insert& {{Parmetros creacin en eatc_vistas }} 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_visualizacion_vistas&_operacion=insert& {{Parmetros creacin en eatc_vistas }} 

 Update 
 {{parmetros para el update de eatc_visualizacion_vistas }} 

 ambiente (***nuevo***) : para este caso el ambiente podr ser "BO" o "DataGov" ( eatc_visualizacion_vistas.ambiente ) 
 tipo_ambiente (***nuevo***) : pruebas, productivo, ambos ( eatc_visualizacion_vistas.tipo_ambiente ) 
 visible : no se entiende muy bien la utilidad de este campo ( eatc_visualizacion_vistas.visible ) 
 eatc_country (***nuevo***) :  no obligatorio se toma de un selector nico  cuyos valores se obtienen de:  https://beneficiarios.eatcloud.info/api/data/eatc_cua_master?eatc_country=_* ( eatc_visualizacion_vistas.visible ) 
 cua : ser en principio no obligatorio y se tomar como selector del  maestro eatc_cua que reposa en config. https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&name=_todos   ( eatc_visualizacion_vistas.cua ) 
 cua_vertical : opcional, se toma de la informacin del maestro respectivo en config:  https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&nombre=_todos ( eatc_visualizacion_vistas.cua_vertical ) 
 cua_type: obligatorio, puede en principio tomar dos valores: "free" y "hero". 
 experimental_desde : campo de fecha opcional en formato AAAA-MM-DD , cuando contenga informacin el campo experimental hasta deber tambin contenerla y estas fechas dictarn un periodo de visualizacin experimental de la funcionalidad, en donde la misma se desplegar acompaada de un mtodo para capturar opiniones de dicha funcionalidad y un vnculo a una landing page de enganche comercial 
 experimental_hasta : campo de fecha opcional en formato AAAA-MM-DD (obligatorio si experimental_desde tiene un dato vlido). 
 lastupdate :  en formato AAAA-MM-DD HH:MM:SS, timestamp de la fecha y hora de creacin ( eatc_visualizacion_vistas.lastupdate ) 

 [***] Se guarda la informacin en el object store eatc_visualizacion_vistas de la cuenta eatcloud: 

 Mtodo POST  

 Se debe evaluar si es fcil llevar este object store a la raz (primera opcin) o si se debe llevar a una "cuenta" dentro de datagov caso en el cual debe ser la cuenta "eatcloud" 

 https://datagov.eatcloud.info/ crd/?_tabla=eatc_visualizacion_vistas&_operacion=update& {{Parmetros el uptdate de eatc_vistas }}&WHEREidfuncionalidad={{ eatc_vistas.idfuncionalidad }} 

 https://datagov.eatcloud.info/ crd/eatcloud/?_tabla=eatc_visualizacion_vistas&_operacion=insert& {{Parmetros el uptdate de eatc_vistas }}&WHEREidfuncionalidad={{ eatc_vistas.idfuncionalidad }} 

 VISUALIZACIN DE KPIS 
 En el BO raz , se debe permitir visualizar todos los KPIs que se definen a continuacin, es decir en https://datagov.eatcloud.info/bo/ .  Pero los mismos debern poderse perfilar o asociar (en una funcionalidad que posteriormente se definir y que ser similar a esta: https://sites.google.com/nodrizza.com/eatcloud/m%C3%B3dulos-funcionales/eatcloud-bo-donantes/configuraci%C3%B3n-web-app-donantes?authuser=0 pero funcionando con los criterios abajo descritos), a uno de los siguientes criterios de perfilacin: 

 eatc_country: inicialmente ser Colombia pero luego podrn ir creciendo: https://beneficiarios.eatcloud.info/api/data/eatc_countries?_id=_ *  (esta informacin debera estar en  https://datagov.eatcoud.info/api/data/eatc_countries?_id=_*) 
 eatc_cua.vertical: informacin asociada a la CUA: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&vertical=_todos   y cuyo maestro es este: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&nombre=_todos   
 eatc_cua.type: informacin asociada a la CUA: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&type=_todos (free,hero) 

 En etapas posteriores se podrn incorporar criterios adicionales de perfilamiento como: 
 eatc_province (en una segunda etapa) 
 eatc_city (en una segunda etapa) 
 eatc_cua 

 NOTA de mejoramiento futuro: 

 En algn punto se debera poder migrar toda la informacin de cuentas al entorno https://datagov.eatcloud.info/api/eatc_cua y a travs de esta plataforma tener un administrador para poder crear los clientes y las cuentas) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 ADMINISTRADOR DE FUNCIONALIDADES - DATAGOV