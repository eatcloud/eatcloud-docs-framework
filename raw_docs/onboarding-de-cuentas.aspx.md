# onboarding-de-cuentas.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El flujo de onboarding, hace referencia a un flujo de recolección de información, regido por un diseño de experiencia de usuario que busca que esta solicitud de información sea realizada de una manera que evite la fricción con el usuario y promueva la solicitud efectiva de toda la información evitando la deserción.  Las funcionalidades del oboarding también podrán estar disponibles en el BO EatCloud de datagov (para ser utilizadas por personal de EatCloud) y en el BO de Cuentas de datagov (que se constituirá en el panel de administración de la cuenta para los usuarios superdaministradores y será la plataforma a la cual desembocará el proceso de onboarding) 

 DEPRECADO: Situación actual 
 Es un proceso manual realizado por funcionarios de EatCloud, fuertemente ligado a estructuras que residen en la plataforma CONFIG y cuya justificación para estar en dicha plataforma es ahora cuestionable por no presentar ventajas prácticas y más bien muchas desventajas (Por la dificultad de intervenir desde el exterior y de manera más flexible dichas estructuras). 

 https://lucid.app/invitations/accept/38a61007-eb74-4125-b997-975d186b0f64   

 CREACIÓN DE USUARIO (SUPERADMIN) 
 Panorama actual: 
 Los datos del usuario superadministrador asociado a cada cuenta, los estamos creando de manera manual y dicha creación no está siendo parte de ningún proceso de onboarding.   

 Panorama deseado: 
 Se debe generar un formulario de creación de usuarios mediante social login, que cree un superdaministrador que podrá acceder a funciones para crear y  administrar la cuenta, inicialmente desde un flujo de onboarding (el presente), pero posteriormente también desde funcionalidades disponibles en un BO que estará en datagov : 
 https://datagov.eatcloud.info/bo/{{eatc_cua_master}}/{{eatc_cua_user}} 

 Naturaleza del usuario que se creará y principales funciones 
 El usuario que se crea en primera instancia, debe asimilarse al usuario SuperAdmin, que podrá realizar en primera instancia las siguientes funciones (a través de un BO en datagov y también algunas en el BO tradicional) 

 Crear datos de la cuenta ( ya implementado , pero requerirá revisión de UX/UI en lo que se consideraría una versión alternativa, la actual se puede conservar para uso interno de EatCloud). 
 Crear y editar datos de usuarios administradores de BO (BO datagov: habría que trasladarlo ya que en este momento está en BO donantes). 
 Editar datos de la cuenta (BO datagov: pendiente de implementación). 
 Crear datos de puntos de donación (BO datagov reutilizando la implementación de registro simple de punto de donación ). 
 Editar datos de puntos de donación (BO datagov pendiente de implementación, la idea es reutilizar la implementación de registro simple de punto de donación para esto). 
 Crear y editar datos de facturación: datos del cliente, adquisición de licencias (BO Datagov: pendiente de implementar). 

 ***NUEVO: Validación para prevención de creación de cuentas duplicadas *** 

 Dada la problemática detectada de creación de cuentas duplicadas y creación de cuentas basura, se propone hacerle una reingeniería al formulario de onboarding, con el ánimo de poder mitigar el riesgo de la incorporación de información duplicada, y tratar de mitigar el riesgo de creación de cuentas "basura" que llenan nuestras bases de datos de información que no es conveniente.  Por esta razón se propone un mecanismo de validación de NIT inicial, para evitar que los mismos ya estén utilizados dentro de la plataforma, y también un mecanismo de validación de correo electrónico, para seguir adelante con el proceso, después de un registro básico (que si se realiza de manera inadecuada, se pueda borrar fácilmente, sin generar mucho contratiempo. 

 La idea es que cuando se oprima el botón "Registrarse" (https://dev.datagov.eatcloud.info/_dgbo/#!/start), no se direccione al actual flujo de onboarding (https://dev.datagov.eatcloud.info/_dgbo/#!/onb1), sino que se direccione al siguiente formulario: 

 Formulario de validación de datos antes de la creación del usuario 

 Formulario de creación de usuario  
 Este formulario debe ser público, para poderlo incorporar en páginas web externas, como por ejemplo WordPress.  El diseño debe utilizar los elementos del boilerplate de materialized y su wireframe es como se presenta a continuación: 

 Nota importante de implementación: en esta implementación se deben utilizar de raíz (es decir, desde su implementación inicial) en vez de los textos que se presentan a continuación, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementación de base sea internacionalizada. 

 Se creará mediante mecanismos de social login de firebase para facilitar este registro y manejar estándares de seguridad (cosa que ya es una práctica común de la industria), con los siguientes métodos: 

 Usuario y contraseña: 
 Se plantea hacerlo a través de social login utilizando frameworks como Firebase 

 Estos datos se guardan en variables globales o en el repositorio de firebase para posteriormente realizar los siguientes registros (cuando se cree la cuenta) 
 bo_usuarios. usuario 
 bo_usuarios. email 
 bo_usuarios. clave 

 Otros métodos proporcionados por Firebase: 
 Teléfono 
 Google 
 Facebook => Requiere de implementación de esta tarea para su implementación 
 Twitter => Requiere de implementación de esta tarea para su implementación 

 Generalmente el social login provee un token que se guarda para para posteriormente realizar el siguiente registro (cuando se cree la cuenta) 
 bo_usuarios. token 

 Aceptación de los términos de uso: 
 Checkbox cuyo valor por defecto es chequeado ; si si no se chequea no permite finalizar el registro.  Para establecer el vínculo en el cual se consultan estos términos y condiciones, se tiene como insumo esta tarea: https://app.asana.com/0/search/1199340210733943/1199183624112451   

 Acepto recibir noticias y actualizaciones de EatCloud: 
 Checkbox cuyo valor por defecto es no chequeado ; esta aceptación se deberá guardar en algún repositorio (se entendería que en el CRM, pero no se tiene aun claridad al respecto y habría que estudiar las capacidades de integración de la herramienta ( https://api.datacrm.la/#89d2801a-15c5-4260-a418-d4a1f643f34e ), para establecer si lo permite). 

 Este dato se guardará una vez se realice el registro del usuario en el campo (boleano), para posteriormente realizar el siguiente registro (cuando se cree la cuenta). 
 bo_usuarios. notificaciones 

 Una vez terminada esta primera pantalla de registro, se pasará la la segunda pantalla, que sirve para incorporar un nombre de pila al usuario que se está registrando. 

 Registro del nombre de pila del usuario (formulario paso A) 
 Nota importante de implementación: en esta implementación se deben utilizar de raíz (es decir, desde su implementación inicial) en vez de los textos que se presentan a continuación, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementación de base sea internacionalizada. 

 Con este formulario se crea el Nombre y Apellido del Usuario SuperAdmin (que se debe guardar para los registros posteriores). Se guarda para para posteriormente realizar el siguiente registro (cuando se cree la cuenta) 
 bo_usuarios. nombre_usuario 

 Cómo te enteraste de nosotros (PENDIENTE: por el momento no se implementa): 
 Se debe hacer  una conexión con estrategias de CRM para poder medir de que embudo o por medio de qué estrategia llegó el usuario.  Igual se debería poder recolectar información de un referidor si el usuario llegó por como referido. 

 CREACIÓN DE CUENTAS 
 Panorama desde el que se partió: 
 La cuenta se creaba en nuestra plataforma CONFIG, y esto trae algunos problemas de integración para un sistema de onboarding como el que se plantea.  Además es un registro monolítico (que se hace de una sola vez) y que requiere de un registro previo de cliente (que en verdad no es una exigencia real del sistema) y esto trae complicaciones para generar un proceso fluido. 

 Panorama deseado implementado (y que será utilizado en BO EatCloud Datagov en su versión inicial y se ajustará nueva versión de onboarding con UX/UI diferente para el precesnte flujo) 
 Se generará una estructura eatc_cua en datagov.eatcloud.info/api/eatcloud/ . De esta manera se podrá abordar la creación de la cuenta con una filosofía minimalista y luego a medida que avance el proceso de onboarding, se podrá ir incorporando más información a la cuenta para terminar de configurarla.  Es importante realizar un formulario de captura de datos que sea fácilmente integrable con otros entornos web, para poderlo incorporar en páginas web externas, como por ejemplo WordPress (con la filosofía que se empleó alguna vez en config, que permitía integrar el formulario mediante una URL en otro entorno como se puede ver aquí: https://config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?atrib_filtro_tb=name&formulario=si&maestro=eatc_cua&val_filtro_tb=_todos . No se pretende que la implementación sea similar, pero si debe cumplir el objetivo de poder llevar fácilmente el formulario creado a otras páginas web). 

 Formulario público para creación de cuentas 
 Formulario paso B 
 Nota importante de implementación: en la implementación del siguiente formulario se deben utilizar de raíz (es decir, desde su implementación inicial) en vez de los textos que se presentan a continuación, ids , clases y registros en el administrador de labels (guiados inicialmente por lo abajo expuesto), para que su implementación de base sea internacionalizada. 

 Subtítulo: {{Nombre_de_pila}} estamos a punto de terminar 

 Se toma el nombre de pila registrado en el formulario anterior , y se acompaña del ID respectivo para incorporar el label subsiguiente " estamos a punto de terminar... " 

 Nombre de la cuenta ***NUEVO: evaluar unicidad por nombre (antes se había definido que por nombre o por país)**** 

 Nota sobre el diseño arriba expuesto: 
 En el diseño propuesto, se está solicitando el nombre de la empresa mediante la pregunta ¿ Cuál es el nombre de tu empresa ?, lo cual es redundante con una pregunta posterior del mismo flujo de onboarding.  En este punto debemos pregunta: ¿Cuál es el nombre corto o abreviado que identificará tu empresa de manera única en el sistema? (sin espacios, ni caracteres especiales). 

 tooltip : ingrese un nombre corto que lo identificará en la plataforma.  El mismo no debe tener espacios ni caracteres especiales 
 Información técnica del parámetro: eatc_cua. name 
 Tipo de dato: string 
 Tipo de input: text input 
 Valor por defecto: vacío 
 Obligatoriedad : si 
 Validación ***NUEVO*** : obligatoriedad , unicidad: no deben existir dos registros con el mismo nombre. Si alguien quiere registrar un nombre que ya está registrado, se le debe informar que el nombre no está disponible y sugerirle que registre ese mismo nombre, seguido por un _{{eatc_cua.eatc_country}} , simpre y cuando en el país de origen no exista una cuenta con ese mismo nombre.  Si en el país existe una cuenta con ese mismo nombre, el sistema informará que el nombre ya está siendo utilizado y que por favor cambie su nombre de cuenta. 

 Ejemplo 1 (hipotético): 
 Alguien en Brasil (iso2=br) desea registrar la cuenta " exito ", el sistema valida y ya encuentra una cuenta con ese nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.  El sistema valida si en el país en el cual se está registrando existe una cuenta con ese mismo nombre: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&eatc_country=br y como no existe le sugiere registrar" exito_br" como nombre de cuenta alternativo para seguir adelante. 

 Ejemplo 2: 
 Alguien en Colombia (iso2=co) desea registrar la cuenta " exito ", el sistema valida y ya encuentra una cuenta con ese nombre ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito ), por lo tanto el sistema le informa al usuario que la cuenta ya existe.  El sistema valida si en el país en el cual se está registrando existe una cuenta con ese mismo nombre: https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=exito&eatc_country=co   y como si existe simplemente le dice que el nombre de cuenta ya está siendo utilizado y que debe registrar otro diferente. 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{ input }} 

 Vertical de negocio *** NUEVO : el label para internacionalización se toma del dato: eatc_verticals_mt .eatc_name ***: 
 Información técnica del parámetro: eatc_cua. vertical 
 Tipo de dato: string 
 Tipo de input: selector único 
 La información del selector se toma de: class={{ eatc_verticals_mt .eatc_name }} (se deberá configurar para que los valores que se obtienen de la siguiente consulta, sean tratados como labels) 

 Consulta de verticales disponibles para este onboarding: 
 {{ URL_entorno_datagov }} /api/eatcloud/eatc_verticals_mt?eatc_onboarding=1 &_distinct= eatc_name 

 Ejemplo en ambiente productivo: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?eatc_onboarding=1&_distinct= eatc_name   

 Como el sistema responde: 
 res :  
 [ 
 { 
 eatc_name : "horeca" 
 }, 
 { 
 eatc_name : "industria" 
 }, 
 { 
 eatc_name : "retail" 
 }, 
 { 
 eatc_name : "agro" 
 } 
 ], 

 Entonces los selectores se deben popular con los siguientes labels: 
 class=" horeca ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=horeca 
 class=" industria ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=industria 
 class=" retail ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=retail 
 class=" agro ": https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=datagov_cuentas&idlabel=agro   

 DEPRECADO: 
 *** NUEVO: Paso 1: consulta del idioma 
 El sistema debe consultar el idioma (código de dos dígitos) del dispositivo para con él realizar la nueva consulta de las verticales 

 ***NUEVO: Paso 3: consulta de verticales disponibles para este onboarding: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?eatc_onboarding=1   

 El sistema toma el array de valores del parámetro eatc_verticals_mt. _id para realizar la siguiente consulta 
 Ejemplo: a 11 de noviembre de 2020: 
 el array de _id sería 4,5,6,7 

 ***NUEVO: Paso 3: consulta de las verticales 
 Para realizar esta consulta, el sistema debe realizar el siguiente llamado 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language={{codigo_dos_digitos_idioma}}& eatc_data_id={{array( eatc_verticals_mt. _id)}} 
 (Anteriormente: https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_verticales_mt&onboarding=1 ) 

 Ejemplo: idioma español a 11 de noviembre de 2020: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language=es& eatc_data_id=4,5,6,7   

 Si el anterior llamado no trae datos se utiliza el siguiente llamado para obtener valores por defecto: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_internationalize_dt?eatc_mt=eatc_verticals_mt&eatc_language=en& eatc_data_id={{array( eatc_verticals_mt. eatc_code)}} 

 El sistema toma los datos consignados en el campo " eatc_internationalize_dt. eatc_int_data " para mostrarlos en el selector   

 Ejemplo: idioma español a 11 de noviembre de 2020: 
 Se mostrarían en el selector los valores 
 Hoteles, restaurantes y casinos 
 Industria 
 Retail 
 Sector agrícola 

 cuándo se selecciona un dato en particular se procede a tomar el eatc_internationalize_dt. eatc_data_id para realizar la siguiente consulta: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id ={{ eatc_internationalize_dt. eatc_int_data_id }} para llevar al registro el valor eatc_verticales_mt. eatc_code 

 Ejemplo, continuando con el anterior Si el usuario selecciona "retail" entonces eatc_internationalize_dt. eatc_data_id=6 por lo tanto al hacer la siguiente consulta: https://datagov.eatcloud.info/api/eatcloud/eatc_verticals_mt?_id=6 al registro se llevaría el valor "eatc_verticales_mt. eatc_code " = "retail" 
 Valor por defecto: ninguno 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua?vertical={{ eatc_verticales_mt. eatc_code }} 

 País: 
 Información técnica del parámetro: eatc_cua. eatc_country , eatc_cua.eatc-cua_master 
 Tipo de dato: string 
 Tipo de input: selector único 
 La información del selector se toma de: 

 ***REVISIÓN data maestra y registro de datos*** 
 ***REVISAR PORQUE ESTABA APUNTANDO A UN MAESTRO EN BENEFICIARIOS Y AHORA DEBE APUNTAR A DATAGOV*** https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country=_* eatc_country , eatc_cua (se muestra en el selector: https://datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2={{eatc_country}} nombre) 
 Obligatoriedad : si 

 ***NUEVA validación: ubicación del browser*** 
 Validación : obligatoriedad, Ubicación del browser.  Se debe solicitar habilitar los datos de ubicación del browser y cotejarla con el país seleccionado, si no corresponde se debe avisar al usuario de esta circunstancia y si se tiene o no cobertura en el país desde donde se está haciendo el registros y si desea seguir adelante con el registro pero con los datos del país seleccionado. 
 Se guarda en (para efectos indicativos, no prácticos) : 
https://datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_country={{ eatc_master_cua. eatc_country }} 
https://datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc-cua_master={{ eatc_master_cua. eatc_cua }} 

 Tipo de licencia *** NUEVO: en flujo de onboarding pasa a creación automática de dato , es decir: sale del formulario.  En onboarding primera versión que se operará desde datagov BO EatCloud , se mantiene como dato de captura***: 
 Hasta aquí queda la primera parte del onboarding de cuentas (Formulario Paso B),  y se debe proceder con los datos automáticos para la creación de la cuenta y  

 Datos automáticos para la creación de cuenta 
 Los siguientes datos los generará automáticamente el sistema, sin que tenga que mediar intervención humana.  Algunos de los mismos son datos por defecto que deben quedar así configurados sobre todo para una operación inicial de la funcionalidad de creación manual de anuncios de donación. 

 Fecha y hora de creación: 
 Información técnica del parámetro: eatc_cua. creation_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_datetime ={{ current_datetime }} 

 Fecha de creación: 
 Información técnica del parámetro: eatc_cua. creation_date 
 Tipo de dato: date 
 Tipo de input: datestamp 
 Valor por defecto: fecha actual 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? creation_date ={{ current_date }} 

 Fecha y hora de última modificación: 
 Información técnica del parámetro: eatc_cua. last_modification_datetime 
 Tipo de dato: datetime 
 Tipo de input: timestamp 
 Valor por defecto: fecha y hora actual 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_datetime ={{ current_datetime }} 

 Fecha de última modificación: 
 Información técnica del parámetro: eatc_cua. last_modification_date 
 Tipo de dato: date 
 Tipo de input: datestamp 
 Valor por defecto: fecha actual 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? last_modification_date ={{ current_date }} 

 Tipo de licencia *** NUEVO: en flujo de onboarding se creará siempre licencia " free " (antes era  "free_trial") ***: 
 Información técnica del parámetro: eatc_cua. type 
 Tipo de dato: string 
 Input: free ( antes era "free_trial" ) 
 Valor por defecto: free ( antes era "free_trial" ) 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua?type={{ eatc_customer_type. type }} 

 eatc_dona_upl 
 Información técnica del parámetro: eatc_cua. eatc_dona_upl 
 Tipo de dato: string 
 Input: "yes" 
 Valor por defecto: "yes" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_dona_upl =yes 

 multiple_donors 
 Información técnica del parámetro: eatc_cua. multiple_donors 
 Tipo de dato: string 
 Input: "no" 
 Valor por defecto: "no" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? multiple_donors =no 

 edit_coordinates 
 Información técnica del parámetro: eatc_cua. edit_coordinates 
 Tipo de dato: string 
 Input: "no" 
 Valor por defecto: "no" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? edit_coordinates =no 

 eatc_odds_app 
 Información técnica del parámetro: eatc_cua. eatc_odds_app 
 Tipo de dato: string 
 Input: "eatc_dona_app" 
 Valor por defecto: "eatc_dona_app" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? eatc_odds_app =eatc_dona_app 

 odds_weight 
 Información técnica del parámetro: eatc_cua. odds_weight 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? odds_weight =eatc_dona 

 costs 
 Información técnica del parámetro: eatc_cua. costs 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? costs =eatc_dona 

 taxes 
 Información técnica del parámetro: eatc_cua. taxes 
 Tipo de dato: string 
 Input: "eatc_dona" 
 Valor por defecto: "eatc_dona" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? taxes =eatc_dona 

 days_before_expiration 
 Información técnica del parámetro: eatc_cua. days_before_expiration 
 Tipo de dato: integer 
 Input: "3" 
 Valor por defecto: "3" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? days_before_expiration =3 

 days_before_expiration 
 Información técnica del parámetro: eatc_cua. days_before_expiration 
 Tipo de dato: integer 
 Input: "3" 
 Valor por defecto: "3" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua? days_before_expiration =3 

 manual de usuario 
 Información técnica del parámetro: eatc_cua. user_manual 
 Tipo de dato: string 
 Input: "" 
 Valor por defecto: "" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua?= 

 manual de usuario bo 
 Información técnica del parámetro: eatc_cua. user_manual 
 Tipo de dato: string 
 Input: "" 
 Valor por defecto: "" 
 Obligatoriedad : si 
 Validación : obligatoriedad 
 Se guarda en (para efectos indicativos, no prácticos) : 
datagov.eatcloud.info/api/eatcloud/eatc_cua?= 

 Non award alert 
 Con el dato guardado en eatc_cua. name , se activa el servicio para la creación de un "non_award_alert" realizando el siguiente llamado: 
 {{URL_entorno_donantes}}/casebd/{{eatc_cua. name }}/non_award_alert 

 CREACIÓN DE TABLAS NECESARIAS PARA ALTA DE CUENTA 

 Panorama actual: 
 Se realiza una creación manual de las tablas. 

 Panorama deseado: 
 Cuando se cree la cuenta se debería realizar un proceso automático de creación de tablas (puede ser una serie de casedb que se activen una vez se termina de completar los datos mínimos para la creación de la cuenta).  El proceso debería recibir un parámetro adicional ambiente_de_pruebas={{si/no}} (por defecto debe estar en "no"), que defina si las tablas se crean solo en ambiente productivo ( ambiente_de_pruebas=no ) o en ambos ambientes ( ambiente_de_pruebas=si )  

 Tablas que se deben crear 

 eatc_pods_login_history 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc-pod_id;eatc-login_datetime 

 eatc_attention_schedule 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 
 Índices: eatc_indexes .eatc_key : https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_attention_schedule 

 eatc_sale_schedule 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc-day;eatc-final_hour;eatc-start_hour;eatc-pod_id 

 eatc_sale_prd_mstr 
 Cómo se crea : se crea con datos 
 Datos: 
 eatc-odd_id;eatc-odd_code;eatc-odd_code_type;eatc-odd_name;eatc_odd_description;eatc_odd_image;eatc-odd_unit_weight_kg;eatc_VAT_percentage;eatc-other_taxes_percentage;eatc-contains_alergens;eatc-odd_typology_a 
 1;box_1;;Caja sorpesa de 1 KG;Caja con productos sorpresa con un peso de 1 KG; http://repograf.eatcloud.info/img/box-prd-1kg.png ;1;;;;box 
 2;box_2;;Caja sorpesa de 2 KG;Caja con productos sorpresa con un peso de 2 KG; http://repograf.eatcloud.info/img/box-prd-2kg.png ;2;;;;box 
 5;box_5;;Caja sorpesa de 5 KG;Caja con productos sorpresa con un peso de 2 KG; http://repograf.eatcloud.info/img/box-prd-5kg.png ;5;;;;box 
 10;box_10;;Caja sorpesa de 10 KG;Caja con productos sorpresa con un peso de 10 KG; http://repograf.eatcloud.info/img/box-prd-10kg.png ;10;;;;box 
 Índices: eatc_indexes .eatc_key : https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_sale_prd_mstr 

 eatc_dona_return_causes 
 Cómo se crea : se crea con datos 
 Datos: 
 eatc-return_cause_code;eatc-return_cause 
 1;Avería 
 2;Próximo a vencerse 
 3;Daño en el empaque 
 4;Temporada 
 5;Donación humanitaria 

 eatc_pods 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : REVISAR: https://donantes.eatcloud.info/api/colombia/eatc_pods?_campos 
 Índices: eatc_indexes .eatc_key : https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_pods 

 eatc_pods_coordinates 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc-city;eatc-adress;eatc-id;eatc-lat;eatc-lon;eatc-name;eatc-country;eatc-warning;eatc-province 

 eatc_pods_typolgy_a 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc_code;eatc_name 

 eatc_pods_typolgy_b 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : eatc_code;eatc_name 

 bo_usuarios (se propone crear con varios campos nuevos) 
 Cómo se crea : Se crea con los datos del usuario superadmin que se creó mediante el social login 
 Vector de encabezados : (se colocan los nuevos campos a crear resaltados ) 
 usuario;clave;nombre_usuario;tipousuario;email; telefono ;ingresos;ultimo_ingreso; eatc_user_profile;notificaciones;token 
 Datos : con los datos del social login se crea el registro del usuario superadministrador 
 usuario;clave;nombre_usuario;tipousuario;email;telefono;ingresos;ultimo_ingreso;eatc_user_profile;notificaciones;token 
 {{bo_usuarios. usuario }};{{bo_usuarios. clave }};{{bo_usuarios. nombre_usuario }};A;{{bo_usuarios. email }};;;;;{{bo_usuarios. notificaciones }} ; {{bo_usuarios. token }} 

 ***NUEVO: eatc_odds *** 
 Cómo se crea : Se crea sin datos 
 Vector de encabezados : REVISAR (definir cual es el modelo idóneo para los campos de esta tabla): https://donantes.eatcloud.info/api/ara/eatc_odds?_campos 
 Índices: eatc_indexes .eatc_key : https://datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_odds 

 ***NUEVO:  Envío de correo electrónico al gestor del ecosistema social ante la creación de una nueva cuenta de usuario *** 
 Determinación del correo electrónico al cuál se envía: 

 El sistema realiza la siguiente consulta: 
 {{ URL_datagov }}/api/eatcloud/eatc_cua_master?eatc_cua={{_DOM. cua_master }}&_cmp= eatc_pod_creation_notification_emails 

 Con la respuesta, el sistema construye un {{ array_destinatarios }} a los cuales enviará el siguiente correo electrónico.  Si la consulta no arroja resultados el correo no se envía. 
 Envío de correo, ante cua_user creada 
 Nota para el desarrollo: en la presente documentación se presenta en dónde reposa la información en la tabla eatc_customers y eatc_cua (anotando las variables correspondientes con la siguiente notación: {{ tabla .campo}}) , con el ánimo de indicar donde reposa esa información en la plataforma legacy.  El desarrollo deberá tomar la información donde reposa la mima en la plataforma modernizada   

 from :  noreply@eatcloud.com 

 to : {{ array_destinatarios }}  

 Asunto : Nueva cuenta donante creada 

 Cuerpo : 

Estimado equipo de ABACO: 

Por medio de la presente, se les informa de la creación de una nueva cuenta donante en nuestro sistema. 

Detalles de la cuenta: 

Nombre completo: {{eatc_customers. eatc_fiscal_name }} 
NIT: {{eatc_customers. eatc_fiscal_id }} 
Sector al que pertenece: {{eatc_cua. vertical }} 
Correo electrónico: {{eatc_customers. eatc_email }} 
Fecha de creación: {{eatc_cua. creation_date }} 

Agradecemos que tomen las acciones correspondientes para dar la bienvenida a nuestro nuevo donante y activar los procesos de reglas de match ( https://bit.ly/eatc_configmatch : informando el nombre de la cuenta {{eatc_cua. name }} ) y cobertura. 

Atentamente, 

EatCloud 

 ENVÍO DE CORREOS PARA CONFIGURACIÓN DE CRONJOBS PARA CONSOLIDACIÓN DE DATOS Y KPIS 
 Panorama actual: 
 Este proceso se realiza de manera manual. 
 Panorama deseado: 
 Cada vez que se cree una cuenta debería generarse un correo electrónico (que incluya correo electrónico a Tablero de Asana: ) para crear los conjobs necesarios para la correcta operación del sistema.  Lo que es ideal a futuro es ingeniarse una manera para crear estos cronjobs de manera automática utilizando inicialmente el API de CPanel https://documentation.cpanel.net/display/DD/cPanel+API+2+Functions+-+Cron%3A%3Aadd_line . 

 Cuando se terminan de crear las tablas necesarias (y ya se crearon los datos automáticos ): 
 El sistema da ingreso a la plataforma de la cuenta en datagov (se debe realizar el login automático a la plataforma con los datos del superadmin capturados por social login: https://datagov.eatcloud.info/bo/{{eatc_cua. name }} ), para lanzar la funcionalidad de " Configuración básica " (que siempre debe ser lanzada cuando se ingresa por primera vez). 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 281.000000000000 

 ONBOARDING DE CUENTAS