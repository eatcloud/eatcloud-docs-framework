# ganchos-desde-la-configuración.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El flujo de onboarding, hace referencia a un flujo de recoleccin de informacin, regido por un diseo de experiencia de usuario que busca que esta solicitud de informacin sea realizada de una manera que evite la friccin con el usuario y promueva la solicitud efectiva de toda la informacin evitando la desercin.&#160; Las funcionalidades del oboarding tambin podrn estar disponibles en el BO EatCloud de datagov (para ser utilizadas por personal de EatCloud) y en el BO de Cuentas de datagov (que se constituir en el panel de administracin de la cuenta para los usuarios superdaministradores y ser la plataforma a la cual desembocar el proceso de onboarding) 

 SITUACIN ACTUAL 
 Es un proceso manual realizado por funcionarios de EatCloud, fuertemente ligado a estructuras que residen en la plataforma CONFIG y cuya justificacin para estar en dicha plataforma es ahora cuestionable por no presentar ventajas prcticas y ms bien muchas desventajas (Por la dificultad de intervenir desde el exterior y de manera ms flexible dichas estructuras). 
&#160; 
 https&#58;//lucid.app/invitations/accept/38a61007-eb74-4125-b997-975d186b0f64 &#160; 

 COMPONENTES DEL PROCESO DE ONBOARDING E IDEAS PARA SU ATOMATIZACIN 

 CREACIN DE USUARIO (SUPERADMIN) 
&#160; 
 Panorama actual&#58; 
 Los datos del usuario superadministrador asociado a cada cuenta, los estamos creando de manera manual y dicha creaci no est siendo parte de ningn proceso de onboarding.&#160;&#160; 
&#160; 
 Panorama deseado&#58; 
 Se debe generar un formulario de creacin de usuarios mediante social login, que cree un superdaministrador que podr acceder a funciones para crear y&#160; administrar la cuenta, inicialmente desde un flujo de onboarding (el presente), pero posteriormente tambin desde funcionalidades disponibles en un BO que estar en datagov &#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/bo/&#123;&#123;eatc_cua_master&#125;&#125;/&#123;&#123;eatc_cua_user&#125;&#125; 
&#160; 
 Naturaleza del usuario que se crear y principales funciones 
 El usuario que se crea en primera instancia, debe asimilarse al usuario SuperAdmin, que podr realizar en primera instancia las siguientes funciones (a travs de un BO en datagov y tambin algunas en el BO tradicional) 
&#160; 
 Crear datos de la cuenta ( ya implementado , pero requerir revisin de UX/UI en lo que se considerara una versin alternativa, la actual se puede conservar para uso interno de EatCloud). 
 Crear y editar datos de usuarios administradores de BO (BO datagov&#58; habra que trasladarlo ya que en este momento est en BO donantes). 
 Editar datos de la cuenta (BO datagov&#58; pendiente de implementacin). 
 Crear datos de puntos de donacin (BO datagov reutilizando la implementacin de registro simple de punto de donacin ). 
 Editar datos de puntos de donacin (BO datagov pendiente de implementacin, la idea es reutilizar la implementacin de registro simple de punto de donacin para esto). 
 Crear y editar datos de facturacin&#58; datos del cliente, adquisicin de licencias (BO Datagov&#58; pendiente de implementar). 
 Configurar funcionalidades (BO datagov&#58; habra que trasladarlo ya que en este momento est en BO donantes). 
&#160; 
 Formulario de creacin de usuario (cuando se ingresa por primera vez.&#160; En los ingresos posteriores este debe ser el formulario de login a cuentas datagov ) 
&#160; 
 Este formulario debe ser pblico, para poderlo incorporar en pginas web externas, como por ejemplo WordPress.&#160; El diseo debe utilizar los elementos del boilerplate de materialized y su wireframe es como se presenta a continuacin&#58; 
&#160; 
 Nota importante de implementacin&#58; en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Se crear mediante mecanismos de social login de firebase para facilitar este registro y manejar estndares de seguridad (cosa que ya es una prctica comn de la industria), con los siguientes mtodos&#58; 
&#160; 
 Usuario y contrasea&#58; 
 Se plantea hacerlo a travs de social login utilizando frameworks como Firebase 
&#160; 
 Otros mtodos proporcionados por Firebase&#58; 
 Telfono 
 Google 
 Facebook =&gt; Requiere de implementacin de esta tarea para su implementacin 
 Twitter =&gt; Requiere de implementacin de esta tarea para su implementacin 
&#160; 
 Aceptacin de los trminos de uso&#58; 
 Checkbox cuyo valor por defecto es chequeado ; si si no se chequea no permite finalizar el registro.&#160; Para establecer el vnculo en el cual se consultan estos trminos y condiciones, se tiene como insumo esta tarea&#58; https&#58;//app.asana.com/0/search/1199340210733943/1199183624112451 &#160; 
&#160; 
 Acepto recibir noticias y actualizaciones de EatCloud&#58; 
 Checkbox cuyo valor por defecto es no chequeado ; esta aceptacin se deber guardar en algn repositorio (se entendera que en el CRM, pero no se tiene aun claridad al respecto y habra que estudiar las capacidades de integracin de la herramienta ( https&#58;//api.datacrm.la/#89d2801a-15c5-4260-a418-d4a1f643f34e ), para establecer si lo permite). 
&#160; 
 Este dato se guardar una vez se realice el registro del usuario en el campo (boleano)&#58; 
&#160; 
 bo_usuarios. notificaciones 
&#160; 
 Una vez terminada esta primera pantalla de registro, se pasar la la segunda pantalla, que sirve para incorporar un nombre de pila al usuario que se est registrando. 

&#160; 
 Registro del nombre de pila del usuario (formulario paso A) 
 Nota importante de implementacin&#58; en esta implementacin se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Con este formulario se crea el Nombre y Apellido del Usuario SuperAdmin (que se debe guardar para los registros posteriores). 
&#160; 
 Cmo te enteraste de nosotros (PENDIENTE&#58; por el momento no se implementa)&#58; 
 Se debe hacer&#160; una conexin con estrategias de CRM para poder medir de que embudo o por medio de qu estrategia lleg el usuario.&#160; Igual se debera poder recolectar informacin de un referidor si el usuario lleg por como referido. 
&#160; 
 Relacin usuario - cuenta 
 Cuando el usuario se cree, sus datos deben quedar almacenados en algn repositorio (que por lo analizado hasta el momento debera ser el propio de Firebase) y esta relacin se crea vaca.&#160; Luego cuando se realiza la creacin de cuenta , se deber crear el usuario en el repositorio de la cuenta en particular (se entiende que este repositorio es bo_usuarios ) asociar el usuario a la cuenta maestra ( eatc_cua_master ) y a la cuenta respectiva que se genera. ( eatc_cua_user ). 
&#160; 
 Tomados los datos de esta pantalla se pasa al siguiente formulario de creacin de cuenta (para esta implementacin se tomar como base la implementacin inicial de Onboarding&#58; https&#58;//datagov.eatcloud.info/eatc/new_account ) de cuentas con algunos ajustes que ms adelante se especifican. 

 CREACIN DE CUENTAS 
&#160; 
 Panorama desde el que se parti&#58; 
 La cuenta se creaba en nuestra plataforma CONFIG, y esto trae algunos problemas de integracin para un sistema de onboarding como el que se plantea.&#160; Adems es un registro monoltico (que se hace de una sola vez) y que requiere de un registro previo de cliente (que en verdad no es una exigencia real del sistema) y esto trae complicaciones para generar un proceso fluido. 
&#160; 
 Panorama deseado implementado (y que ser utilizado en BO EatCloud Datagov en su versin inicial y se ajustar nueva versin de onboarding con UX/UI diferente para el precesnte flujo) 
&#160; 
 Se generar una estructura eatc_cua en datagov.eatcloud.info/api/eatcloud/ . De esta manera se podr abordar la creacin de la cuenta con una filosofa minimalista y luego a medida que avance el proceso de onboarding, se podr ir incorporando ms informacin a la cuenta para terminar de configurarla.&#160; Es importante realizar un formulario de captura de datos que sea fcilmente integrable con otros entornos web, para poderlo incorporar en pginas web externas, como por ejemplo WordPress (con la filosofa que se emple alguna vez en config, que permita integrar el formulario mediante una URL en otro entorno como se puede ver aqu&#58; https&#58;//config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?atrib_filtro_tb=name&amp;formulario=si&amp;maestro=eatc_cua&amp;val_filtro_tb=_todos . No se pretende que la implementacin sea similar, pero si debe cumplir el objetivo de poder llevar fcilmente el formulario creado a otras pginas web). 
&#160; 
 FORMULARIO PBLICO PARA CREACIN DE CUENTAS 
 Formulario paso B 
 Nota importante de implementacin&#58; en la implementacin del siguiente formulario se deben utilizar de raz (es decir, desde su implementacin inicial) en vez de los textos que se presentan a continuacin, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementacin de base sea internacionalizada. 

 Subttulo&#58; &#123;&#123;Nombre_de_pila&#125;&#125; estamos a punto de terminar 
 Se toma el nombre de pila registrado en el formulario anterior , y se acompaa del ID respectivo para incorporar el label subsiguiente &quot; estamos a punto de terminar... &quot; 
&#160; 
 Nombre de la cuenta ***NUEVO&#58; evaluar unicidad por nombre (antes se haba definido que por nombre o por pas)**** 
&#160; 
 Nota sobre el diseo arriba expuesto&#58; 
&#160; 
 En el diseo propuesto, se est solicitando el nombre de la empresa mediante la pregunta Cul es el nombre de tu empresa ?, lo cual es redundante con una pregunta posterior del mismo flujo de onboarding.&#160; En este punto debemos pregunta&#58; Cul es el nombre corto o abreviado que identificar tu empresa de manera nica en el sistema? (sin espacios, ni caracteres especiales). 
&#160; 
 tooltip &#58; ingrese un nombre corto que lo identificar en la plataforma.&#160; El mismo no debe tener espacios ni caracteres especiales 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_cua. name 
 Tipo de dato&#58; string 
 Tipo de input&#58; text input 
 Valor por defecto&#58; vaco 
 Obligatoriedad &#58; si 
 Validacin ***NUEVO*** &#58; obligatoriedad , unicidad&#58; no deben existir dos registros con el mismo nombre. Si alguien quiere registrar un nombre que ya est registrado, se le debe informar que el nombre no est disponible y sugerirle que registre ese mismo nombre, seguido por un _&#123;&#123;eatc_cua.eatc_country&#125;&#125; , simpre y cuando en el pas de origen no exista una cuenta con ese mismo nombre.&#160; Si en el pas existe una cuenta con ese mismo nombre, el sistema informar que el nombre ya est siendo utilizado y que por favor cambie su nombre de cuenta. 
&#160; 
 Ejemplo 1 (hipottico)&#58; 
&#160; 
 Alguien en Brasil (iso2=br) desea registrar la cuenta &quot; exito &quot;, el sistema valida y ya encuentra una cuenta con ese nombre ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.&#160; El sistema valida si en el pas en el cual se est registrando existe una cuenta con ese mismo nombre&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;eatc_country=br y como no existe le sugiere registrar&quot; exito_br&quot; como nombre de cuenta alternativo para seguir adelante. 
&#160; 
 Ejemplo 2&#58; 
&#160; 
 Alguien en Colombia (iso2=co) desea registrar la cuenta &quot; exito &quot;, el sistema valida y ya encuentra una cuenta con ese nombre ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.&#160; El sistema valida si en el pas en el cual se est registrando existe una cuenta con ese mismo nombre&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&amp;eatc_country=co &#160; y como si existe simplemente le dice que el nombre de cuenta ya est siendo utilizado y que debe registrar otro diferente. 
&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123; input &#125;&#125; 
&#160; 
 Vertical de negocio *** NUEVO&#58; maestro migra a datagov y se internacionaliza***&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. vertical &#160; 
 Tipo de dato&#58; string 
 Tipo de input&#58; selector nico 
 La informacin del selector se toma de&#58; 
&#160; 
 *** NUEVO&#58; Paso 1&#58; consulta del idioma 
 El sistema debe consultar el idioma (cdigo de dos dgitos) del dispositivo para con l realizar la nueva consulta de las verticales 
&#160; 
 ***NUEVO&#58; Paso 3&#58; consulta de verticales disponibles para este onboarding&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?eatc_onboarding=1 &#160; 
&#160; 
 El sistema toma el array de valores del parmetro eatc_verticals_mt. _id para realizar la siguiente consulta 
&#160; 
 Ejemplo&#58; a 11 de noviembre de 2020&#58; 
 el array de _id sera 4,5,6,7 
&#160; 
 ***NUEVO&#58; Paso 3&#58; consulta de las verticales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&amp;eatc_language=&#123;&#123;codigo_dos_digitos_idioma&#125;&#125;&amp; eatc_data_id=&#123;&#123;array( eatc_verticals_mt. _id)&#125;&#125; 
&#160; 
 (Anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&amp;onboarding=1 ) 
&#160; 
 Ejemplo&#58; idioma espaol a 11 de noviembre de 2020&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&amp;eatc_language=es&amp; eatc_data_id=4,5,6,7 &#160; 
&#160; 
 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&amp;eatc_language=en&amp; eatc_data_id=&#123;&#123;array( eatc_verticals_mt. eatc_code)&#125;&#125; 
&#160; 
 El sistema toma los datos consignados en el campo &quot; eatc_internationalize_dt. eatc_int_data &quot; para mostrarlos en el selector &#160; 
&#160; 
 Ejemplo&#58; idioma espaol a 11 de noviembre de 2020&#58; 
 Se mostraran en el selector los valores 
&#160; 
Hoteles, restaurantes y casinos 
Industria 
Retail 
Sector agrcola 
&#160; 
 cundo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id =&#123;&#123; eatc_internationalize_dt. eatc_int_data_id &#125;&#125; para llevar al registro el valor eatc_verticales_mt. eatc_code 
&#160; 
 Ejemplo, continuando con el anterior 
 Si el usuario selecciona &quot;retail&quot; entonces eatc_internationalize_dt. eatc_data_id=6 por lo tanto al hacer la siguiente consulta&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id=6 al registro se llevara el valor &quot;eatc_verticales_mt. eatc_code &quot; = &quot;retail&quot; 
&#160; 
 Valor por defecto&#58; ninguno 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua?vertical=&#123;&#123; eatc_verticales_mt. eatc_code &#125;&#125; 

&#160; 
 Pas&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. eatc_country , eatc_cua.eatc-cua_master &#160; 
 Tipo de dato&#58; string 
 Tipo de input&#58; selector nico 
 La informacin del selector se toma de&#58; 
&#160; 
 ***REVISIN data maestra y registro de datos*** 
 ***REVISAR PORQUE ESTABA APUNTANDO A UN MAESTRO EN BENEFICIARIOS Y AHORA DEBE APUNTAR A DATAGOV*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country=_* eatc_country , eatc_cua (se muestra en el selector&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2=&#123;&#123;eatc_country&#125;&#125; nombre) 
&#160; 
 Obligatoriedad &#58; si 
&#160; 
 ***NUEVA validacin&#58; ubicacin del browser*** 
 Validacin &#58; obligatoriedad, Ubicacin del browser.&#160; Se debe solicitar habilitar los datos de ubicacin del browser y cotejarla con el pas seleccionado, si no corresponde se debe avisar al usuario de esta circunstancia y si se tiene o no cobertura en el pas desde donde se est haciendo el registros y si desea seguir adelante con el registro pero con los datos del pas seleccionado. 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_country=&#123;&#123; eatc_master_cua. eatc_country &#125;&#125; 
https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc-cua_master=&#123;&#123; eatc_master_cua. eatc_cua &#125;&#125; 

&#160; 
 Tipo de licencia *** NUEVO&#58; en flujo de onboarding pasa a creacin automtica de dato , es decir&#58; sale del formulario.&#160; En onboarding primera versin que se operar desde datagov BO EatCloud , se mantiene como dato de captura***&#58; 
 Hasta aqu queda la primera parte del onboarding de cuentas (Formulario Paso B),&#160; y se debe proceder con los datos automticos para la creacin de la cuenta y&#160; 
&#160; 
 Datos automticos para la creacin de cuenta 
 Los siguientes datos los generar automticamente el sistema, sin que tenga que mediar intervencin humana.&#160; Algunos de los mismos son datos por defecto que deben quedar as configurados sobre todo para una operacin inicial de la funcionalidad de creacin manual de anuncios de donacin. 
&#160; 
 Fecha y hora de creacin&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. creation_datetime 
 Tipo de dato&#58; datetime 
 Tipo de input&#58; timestamp 
 Valor por defecto&#58; fecha y hora actual 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_datetime =&#123;&#123; current_datetime &#125;&#125; 
&#160; 
 Fecha de creacin&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. creation_date 
 Tipo de dato&#58; date 
 Tipo de input&#58; datestamp 
 Valor por defecto&#58; fecha actual 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_date =&#123;&#123; current_date &#125;&#125; 
&#160; 
 Fecha y hora de ltima modificacin&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. last_modification_datetime 
 Tipo de dato&#58; datetime 
 Tipo de input&#58; timestamp 
 Valor por defecto&#58; fecha y hora actual 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_datetime =&#123;&#123; current_datetime &#125;&#125; 
&#160; 
 Fecha de ltima modificacin&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. last_modification_date 
 Tipo de dato&#58; date 
 Tipo de input&#58; datestamp 
 Valor por defecto&#58; fecha actual 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_date =&#123;&#123; current_date &#125;&#125; 
&#160; 
 Tipo de licencia *** NUEVO&#58; en flujo de onboarding se crear siempre licencia free_trial***&#58; 
 Informacin tcnica del parmetro&#58; eatc_cua. type 
 Tipo de dato&#58; string 
 &#160;Input&#58; free_trial 
 Valor por defecto&#58; free_trial 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua?type=&#123;&#123; eatc_customer_type. type &#125;&#125; 
&#160; 
 eatc_dona_upl 
 Informacin tcnica del parmetro&#58; eatc_cua. eatc_dona_upl 
 Tipo de dato&#58; string 
 Input&#58; &quot;yes&quot; 
 Valor por defecto&#58; &quot;yes&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_dona_upl =yes 
&#160; 
 multiple_donors 
 Informacin tcnica del parmetro&#58; eatc_cua. multiple_donors 
 Tipo de dato&#58; string 
 Input&#58; &quot;no&quot; 
 Valor por defecto&#58; &quot;no&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? multiple_donors =no 
&#160; 
 edit_coordinates 
 Informacin tcnica del parmetro&#58; eatc_cua. edit_coordinates 
 Tipo de dato&#58; string 
 Input&#58; &quot;no&quot; 
 Valor por defecto&#58; &quot;no&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? edit_coordinates =no 
&#160; 
 eatc_odds_app 
 Informacin tcnica del parmetro&#58; eatc_cua. eatc_odds_app 
 Tipo de dato&#58; string 
 Input&#58; &quot;eatc_dona_app&quot; 
 Valor por defecto&#58; &quot;eatc_dona_app&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_odds_app =eatc_dona_app 
&#160; 
 odds_weight 
 Informacin tcnica del parmetro&#58; eatc_cua. odds_weight 
 Tipo de dato&#58; string 
 Input&#58; &quot;eatc_dona&quot; 
 Valor por defecto&#58; &quot;eatc_dona&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? odds_weight =eatc_dona 
&#160; 
 costs 
 Informacin tcnica del parmetro&#58; eatc_cua. costs 
 Tipo de dato&#58; string 
 Input&#58; &quot;eatc_dona&quot; 
 Valor por defecto&#58; &quot;eatc_dona&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? costs =eatc_dona 
&#160; 
 taxes 
 Informacin tcnica del parmetro&#58; eatc_cua. taxes 
 Tipo de dato&#58; string 
 Input&#58; &quot;eatc_dona&quot; 
 Valor por defecto&#58; &quot;eatc_dona&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? taxes =eatc_dona 
&#160; 
 days_before_expiration 
 Informacin tcnica del parmetro&#58; eatc_cua. days_before_expiration 
 Tipo de dato&#58; integer 
 Input&#58; &quot;3&quot; 
 Valor por defecto&#58; &quot;3&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? days_before_expiration =3 

&#160; 
 Non award alert 
 Con el dato guardado en eatc_cua. name , se activa el servicio para la creacin de un &quot;non_award_alert&quot; realizando el siguiente llamado&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/casebd/&#123;&#123;eatc_cua. name &#125;&#125;/non_award_alert 

 CREACIN DE TABLAS NECESARIAS PARA ALTA DE CUENTA 
 Panorama actual&#58; 
 Se realiza una creacin manual de las tablas. 
&#160; 
 Panorama deseado&#58; 
 Cuando se cree la cuenta se debera realizar un proceso automtico de creacin de tablas (puede ser una serie de casedb que se activen una vez se termina de completar los datos mnimos para la creacin de la cuenta).&#160; El proceso debera recibir un parmetro adicional ambiente_de_pruebas=&#123;&#123;si/no&#125;&#125; (por defecto debe estar en &quot;no&quot;), que defina si las tablas se crean solo en ambiente productivo ( ambiente_de_pruebas=no ) o en ambos ambientes ( ambiente_de_pruebas=si )&#160; 
&#160; 
 Tablas que se deben crear 
&#160; 
 eatc_pods_login_history 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc-pod_id;eatc-login_datetime 
&#160; 
 eatc_attention_schedule 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 
&#160; 
 eatc_sale_schedule 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 
&#160; 
 eatc_sale_prd_mstr 
 Cmo se crea &#58; se crea con datos 
 Datos (las URLs de imagen cambiarn)&#58; 
&#160; 
 eatc-odd_id;eatc-odd_code;eatc-odd_code_type;eatc-odd_name;eatc_odd_description;eatc_odd_image;eatc-odd_unit_weight_kg;eatc_VAT_percentage;eatc-other_taxes_percentage;eatc-contains_alergens;eatc-odd_typology_a 
 1;box_1;;Caja sorpesa de 1 KG;Caja con productos sorpresa con un peso de 1 KG; http&#58;//repograf.eatcloud.info/img/box-prd-1kg.png ;1;;;;box 
 2;box_2;;Caja sorpesa de 2 KG;Caja con productos sorpresa con un peso de 2 KG; http&#58;//repograf.eatcloud.info/img/box-prd-2kg.png ;2;;;;box 
 5;box_5;;Caja sorpesa de 5 KG;Caja con productos sorpresa con un peso de 2 KG; http&#58;//repograf.eatcloud.info/img/box-prd-5kg.png ;5;;;;box 
 10;box_10;;Caja sorpesa de 10 KG;Caja con productos sorpresa con un peso de 10 KG; http&#58;//repograf.eatcloud.info/img/box-prd-10kg.png ;10;;;;box 
&#160; 
 eatc_dona_return_causes 
 Cmo se crea &#58; se crea con datos 
 Datos&#58; 
&#160; 
 eatc-return_cause_code;eatc-return_cause 
 1;Avera 
 2;Prximo a vencerse 
 3;Dao en el empaque 
 4;Temporada 
 5;Donacin humanitaria 
&#160; 
 eatc_pods 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58;&#160; eatc-province;eatc-city;eatc-email;eatc-adress;eatc-dona_packing;eatc-lat;eatc-lon;eatc-name;eatc-country;eatc-responsable;eatc-phone;eatc-typology_a;eatc-typology_b;eatc-typology_c;password;eatc-production_date;eatc_coordinate_id;eatc-donor;eatc-donor_code;eatc-size;eatc-creation_datetime;eatc-last_modification_datetime 
&#160; 
 [***NUEVO***] eatc_pods_coordinates 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc-city;eatc-adress;eatc-id;eatc-lat;eatc-lon;eatc-name;eatc-country;eatc-warning;eatc-province 
&#160; 
 eatc_pods_typolgy_a 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc_code;eatc_name 
&#160; 
 eatc_pods_typolgy_b 
 Cmo se crea &#58; Se crea sin datos 
 Vector de encabezados &#58; eatc_code;eatc_name 
&#160; 
 Cuando se terminan de crear las tablas necesarias (y ya se crearon los datos automticos )&#58; 
 El sistema da ingreso a la plataforma de la cuenta en datagov (se debe realizar el login automtico a la plataforma con los datos del superadmin capturados por social login), para lanzar la funcionalidad de &quot; Configuracin bsica &quot; (que siempre debe ser lanzada cuando se ingresa por primera vez). 

 *****POSIBLES GANCHOS DESDE LA CONFIGURACIN DE CREACIN DE ANUNCIO DE DONACIN***** 
 Panorama actual&#58; 
 Originalmente se realiz la configuracin manualmente por parte de EatCloud y actuando sobre config. Con el presente trabajo de automatizacin de creacin de cuentas se estableci que gran parte de la configuracin se har por defecto. 
&#160; 
 Panorama deseado&#58; 
 Muchas de las posibilidades de configuracin pueden servir para generar ganchos comerciales, por eso si un usuario la requiere, se podr utilizar para llevarlos a la landing de compra del producto. 
&#160; 
 Gancho #&#58; Creacin de ambiente de pruebas 
 Justificacin&#58; 
 Por defecto las cuentas se deberan crear en productivo, pero si una empresa desea crear un ambiente de pruebas debera solicitar la compra de la licencia &quot;hero&quot;. 
&#160; 
 Desea crear un ambiente de pruebas?&#160; 
 Esto le permitir realizar procesos de capacitacin y entrenamiento con su personal sin tener que comprometer datos que afecten la operacin real de la plataforma 

&#160; 
 Gancho #&#58; Manejo de mltiples puntos de donacin desde una sola&#160; 
 Justificacin&#58; 
 Algunas empresas, por su modelo operativo, en el sitio de entrega no tienen a disposicin personal para entregar y registrar las donaciones, por lo tante.&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. edit_coordinates cmo &quot; si &quot;. 
&#160; 
 Desea manejar mltiples puntos de donacin desde una misma app?&#160; 
 Esto le permitir generar donaciones de mltiples localidades con un mismo usuario de la plataforma 
 Informacin tcnica del parmetro&#58; eatc_cua. edit_coordinates 
 Tipo de dato&#58; string 
 Input&#58; &quot;si&quot; (despus de un proceso comercial de compra de licencia) 
 Valor por defecto&#58; &quot;no&quot; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? edit_coordinates =si 
&#160; 
 Gancho #&#58; subir los productos desde un maestro de productos 
 Justificacin&#58; 
 El tener un maestro de productos para generar donaciones / ventas facilita el proceso de digitacin de las mismas .&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. eatc_odds_app cmo &quot; eatc_odds &quot;. 
&#160; 
 Deseas subir tus donaciones a partir de un maestro de productos?&#160; 
 Esto te permitir buscar tus productos en vez de digitarlos en la plataforma lo cual facilitar el proceso de generacin de anuncios u ofertas de ltimo minuto 
&#160; 
 eatc_odds_app 
 Informacin tcnica del parmetro&#58; eatc_cua. eatc_odds_app 
 Tipo de dato&#58; string 
 Input&#58; (si / no)&#58; el si generara un registro con el valor&#58; eatc_odds despus de completado un proceso comercial. 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_odds_app = eatc_odds 
&#160; 
 Gancho #&#58; obtener el peso de los artculos desde un maestro 
 Justificacin&#58; 
 ______________________________________ .&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. odds_weight cmo &quot; eatc_odds &quot; o &quot; eatc_odds_weight &quot;. 
&#160; 
 Deseas obtener el peso de los productos desde un maestro?&#160; 
 Si en el maestro de productos tienes los pesos de tus artculos, o nos puedes proporcionar un maestro de conversin a KG, puedes facilitar el ingreso de tus donaciones / ventas de ltimo minuto, utilizando esta configuracin. 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_cua. odds_weight 
 Tipo de dato&#58; string 
 Input&#58; Cmo nos deseas informar los pesos de tus productos? 
 Desde el maestro de productos ( eatc_odds )&#160; 
 Desde un maestro de KG por producto ( eatc_odds_weight ) 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? odds_weight =&#123;&#123;input&#125;&#125; 
&#160; 
 Gancho #&#58; obtener el valor de las donaciones / ventas, dede un maestro 
 Justificacin&#58; 
 ______________________________________ .&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. costs cmo &quot; eatc_odds &quot; o &quot; eatc_odds_costs &quot;. 
&#160; 
 Deseas informar los costos de las donaciones? 
 Si en el maestro de productos tienes los costos de tus artculos, o nos puedes proporcionar un maestro de costos, puedes facilitar el ingreso de tus donaciones / ventas de ltimo minuto, utilizando esta configuracin. 
 Informacin tcnica del parmetro&#58; eatc_cua. costs 
 Tipo de dato&#58; string 
 Input&#58; Cmo nos deseas informar los valores/costos de tus productos? 
 Desde el maestro de productos ( eatc_odds )&#160; 
 Desde un maestro de costos por producto ( eatc_odds_costs ) 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? costs =&#123;&#123;input&#125;&#125; 
&#160; 
 Gancho #&#58; Manejo de mltiples donantes 
 Justificacin&#58; 
 Algunas empresas, sobre todo grandes, requieren que desde la plataforma se puedan hacer donaciones de mltiples NITs.&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. multiple_donors cmo &quot; si &quot;. 
&#160; 
 Desea manejar mltiples donantes?&#160; 
 Esto le permitir generar donaciones de mltiples personeras jurdicas a travs de una nica plataforma 
 Informacin tcnica del parmetro&#58; eatc_cua. multiple_donors 
 Tipo de dato&#58; string 
 Input&#58; &quot;no&quot; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? multiple_donors =no 
&#160; 
 Gancho #&#58; ingreso de los impuestos desde un maestro 
 Justificacin&#58; 
 ______________________________________ .&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. taxes cmo &quot; eatc_odds &quot; o &quot; eatc_odds_costs &quot; o &quot; eatc_odds_taxes &quot; 
&#160; 
 Deseas informar los impuestos aplicables a tus productos? 
 Si en el maestro de productos tienes los costos de tus artculos, o nos puedes proporcionar un maestro de costos, puedes facilitar el ingreso de tus donaciones / ventas de ltimo minuto, utilizando esta configuracin. 
 Informacin tcnica del parmetro&#58; eatc_cua. taxes 
 Tipo de dato&#58; string 
 Input&#58; Cmo nos deseas informar los valores/costos de tus productos? 
 Desde el maestro de productos ( eatc_odds )&#160; 
 Desde un maestro de costos por producto ( eatc_odds_costs ) 
 Desde un maestro de impuestos ( eatc_odds_taxes ) 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? taxes =&#123;&#123;input&#125;&#125; 
&#160; 
 Gancho #&#58; no est claro an este gancho. 
 Justificacin&#58; 
 ______________________________________ .&#160; Esto puede ser considerado como una funcionalidad &quot; hero &quot; por lo tanto si se da esta posibilidad de configurar el parmetro eatc_cua. __________ cmo &quot; __________________ &quot;. 
 __________________?&#160; 
&#160; 
 days_before_expiration 
&#160; 
 Informacin tcnica del parmetro&#58; eatc_cua. days_before_expiration 
 Tipo de dato&#58; integer 
 Input&#58; &quot;3&quot; 
 Valor por defecto&#58; &quot;3&quot; 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad&#160; 
 Se guarda en (para efectos indicativos, no prcticos) &#58;&#160; 
datagov.eatcloud.info/api/eatcloud/eatc_cua? days_before_expiration =3 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=52cc10c0dd07443484b8313f83cc4b9e&ext=jpg&ow=1280&oh=815, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=52cc10c0dd07443484b8313f83cc4b9e&ext=jpg&ow=1280&oh=815 

 889.000000000000 

 ONBOARDING DE CUENTAS