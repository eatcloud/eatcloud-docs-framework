# login-url-única.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

URL 
{{URL_beneficiarios}}/signin 

Pruebas: https://devbeneficiarios.eatcloud.info/signin   

Producción: https://beneficiarios.eatcloud.info/signin   
({{URL_beneficiarios}}/_nbob/#!/login)  

Pruebas: https://devbeneficiarios.eatcloud.info/_nbob/#!/login 

Producción: https://beneficiarios.eatcloud.info/_nbob/#!/login 

Datos genéricos de ingreso: 
{{nombre_cua_master}}@ eatcloud.com 
Master.2000* 

 El ingreso tradicional a este entorno se ha venido dando por el registro que se genera en la estructura 
 {{ URL_entorno_beneficiarios }}/api/{{_DOM. cua_master }}/ bo_usuarios ?id=_* 

 Tal como se implementó en para el caso de los puntos de donación y del nuevo BO, se deberán llevar estos usuarios a una estructura centralizada ( guardando el password hasheado ), que permita que en el proceso de login se pueda consultar a qué cuenta maestra pertenece el usuario y por lo tanto, direccionarlo a su propio entorno. 

 De igual manera en el proceso de creación de datos de cuentas maestras ( CREACIÓN DE TABLAS NECESARIAS PARA ALTA DE LA CUENTA MAESTRA ), se deberá incorporar el registro de estos usuarios en una estructura de datos centralizada. 

 ***NUEVO: FUNCIONAMIENTO DEL LOGIN PARA PERMITIR EL INGRESO A LA PLATAFORMA DE BANCOS DE ALIMENTOS Y FUNDACIONES *** 
 El actual BO de la cuenta maestra de Beneficiarios, deberá en el cercano futuro, permitir el ingreso a Bancos de Alimentos y Fundaciones, para consultar algunas de sus funcionalidades, que deberán involucrar filtros para la consulta de la información de los Bancos de Alimentos y sus organizaciones adscritas y también de la información de las organizaciones sociales de manera individual. 

 Para ello nos valdremos de los datos de acceso configurados para la APP Móvil, y una vez se valide que quien intente entrar a este BO, es un usuario de EatCloud Beneficiarios, se le permita crear un usuario y una contraseña asociada a su respectivo eatc_donation_manager y con ella podrá ingresar en adelante al presente BO.  A continuación se propone la ruta funcional de este login ampliado. 

 ***NUEVO: B OTÓN: INGRESO POR PRIMERA VEZ *** 
 class=" lbl_ingreso_primera_vez " (https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_ingreso_primera_vez) 

 P resentar un selector de países 
 Si el loggin tradicional, cómo ha venido funcionando hasta el momento, el sistema deberá presentar un selector de países construído con la siguiente consulta, que permita establecer la cuenta maestra a la cuál pertenece el usuario y así poder consultar los datos de acceso que se presentan más adelante (esto se puede basar en la funcionalidad de seleccionar país en el onboarding de cua_users , implementado en https://datagov.eatcloud.info/_dgbo/#!/onb1 ) 

 Información técnica del parámetro: eatc_cua. eatc_country , eatc_cua. eatc-cua_master 
 Tipo de dato: string 
 Tipo de input: selector único 
 La información del selector se toma de: 

 Data maestra y registro de datos 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_cua_master?eatc_country=_*&_cmp=eatc_country,eatc_cua 

 Se muestra en el selector:  
 {{URL_entorno_datagov}}/api/eatcloud/eatc_countries?iso2={{eatc_cua_master. eatc_country }}&_cmp=nombre 

 Ejemplo, ambiente productivo , eatc_cua_master. eatc_country =co 
 https://datagov.eatcloud.info/api/eatcloud/eatc_countries?iso2=co&_cmp=nombre   

 Obligatoriedad : si 

 Validación: ubicación del browser 
 Validación : obligatoriedad, Ubicación del browser.  Se debe solicitar habilitar los datos de ubicación del browser y cotejarla con el país seleccionado, si no corresponde se debe avisar al usuario de esta circunstancia y si se tiene o no cobertura en el país desde donde se está haciendo el registros y si desea seguir adelante con el registro pero con los datos del país seleccionado. 
 A partir de la selección realizada por el usuario :  Se lleva el dato  eatc_cua_master . eatc_cua a la variable {{_DOM. cua_master }} para la siguiente validación 

 ***NUEVO: Una vez obtenido el valor de la cuenta maestra ( {{_DOM. cua_master }} ) se despliega un nuevo formulario de validación de usuario y contraseña contra el maestro eatc_users *** 
 El sistema despliega un formulario de validación de usuario y contraseña, pero que esta vez permite  realizar una validación contra el maestro eatc_users de la respectiva cuenta maestra de beneficiarios (y que funciona de manera muy similar al login que se realiza a través de la App Beneficiarios de EatCloud. 

 Nombre de usuario 
 Place holder: 
 class=" lbl_usuario " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_usuario )  

 Valor por defecto para el cuadro de texto: 
 Ninguno (es decir, debe mostrar el place holder) 

 Validación para el cuadro de texto: 
 El formulario deberá validar que se agregue un nombre de usuario. 

 El texto digitado se lleva: 
 Se debe guardar en a variable {{ usuario }} para posteriormente realizar la validación del usuario. 

 Contraseña (cuadro de captura de texto) 
 Place holder: 
 class=" lbl_password " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_password )   

 Valor por defecto para el cuadro de texto: 
 Ninguno (es decir, debe mostrar el place holder) 

 Validación para el cuadro de texto: 
 El formulario deberá validar que se agregue una contraseña. 

 El texto digitado se lleva: 
 Se debe guardar en a variable {{ password }} para posteriormente realizar la validación de la contraseña. 

 V ALIDACIÓN DEL NOMBRE DE USUARIO Y LA CONTRASEÑA 
 El sistema deberá realizar la siguiente consulta: 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_users ?correo_electronico= {{ usuario }} &numero_cedula= {{ password }}&_cmp= organizacion &_token={{token}} 

 Validación fallida: 
 Si el sistema no entrega una respuesta válida, entonces se desplegará el siguiente mensaje 

 No fue posible autenticar los datos de acceso del usuario. Por favor intenta de nuevo: 
 class=" lbl_sin_autenticacion " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_sin_autenticacion ) 

 Validación exitosa: 
 Si el sistema entrega una respuesta válida, con la información obtenida en el parámetro " eatc_users. organización ", de la consulta de validación, el sistema deberá proceder a realizar la siguiente consulta 

 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers ? identificador_unico_registro = {{ eatc_users . organizacion }}&_cmp= identificador_unico_registro,identificador,eatc_cua_master,eatc_doma_typology_b 

 Y con ello realizar la siguiente clasificación del usuario que se creará posteriormente, con el ánimo de aplicar filtros a lo largo de los informes del BO, de la siguiente manera: 

 La organización es la cuenta maestra: 
 beneficiary_ecosystem_leader=y 

 En este caso, el BO funcionará de la misma manera como se desarrolló inicialmente, trayendo todos los datos de la cuenta maestra en cuestión. 

 La organización es un banco de alimentos: 
 eatc_doma_typology_b = 1  

 En este caso, el BO funcionará  aplicando el nuevo  tipo_BdeA que se definirá para cada informe en particular, de los que aplican para este tipo de organización (no todos los informes y funcionalidades se les desplegarán a los bancos de alimentos). 

 El sistema guardará el identificador único de registro del banco de alimento 

 El sistema realizará la siguiente consulta, para obtener el un array de beneficiarios adscritos al banco de alimentos ( array_beneficiarios_adscritos ) 
 {{URL_entorno_beneficiarios}}/api/{{_DOM. cua_master }}/eatc_donation_managers ? organizacion_vinculada = {{ eatc_users . organizacion }}&_cmp= identificador_unico_registro 

 En los diferentes informes e indicadores de la plataforma, se aplicarán diferentes clases de filtros (teniendo como base las consultas desarrolladas en el BO Beneficiarios CUA_MASTER) y que constarán básicamente de agregar a las consultas ya construidas, las siguieentes consultas, que filtrarán información para traer la que corresponde al respectivo banco, de la siguiente manera: 

 {{filtro_eatc_dona_headers (tipo_BdeA) }} 
 eatc-donation_manager_code= {{ array_beneficiarios_adscritos }} 
 {{filtro_eatc_dona (tipo_BdeA) }} 
 {{filtro_eatc_dona_kpi (tipo_BdeA) }} 
 eatc-donation_manager_code= {{ array_beneficiarios_adscritos }} 

 La organización no es un banco de alimentos: 
 eatc_doma_typology_b = ! 1  

 En este caso, el BO funcionará  aplicando el nuevo  tipo_no_BdeA que se definirá para cada informe en particular, de los que aplican para este tipo de organización (no todos los informes y funcionalidades se les desplegarán a las demás organizaciones sociales) 

 Para esta organización, se deberá guardar el dato de eatc_donation_managers. identificador_unico_registro para aplicar a diversos filtros de información 

 En los diferentes informes e indicadores de la plataforma, se aplicarán diferentes clases de filtros (teniendo como base las consultas desarrolladas en el BO Beneficiarios CUA_MASTER) y que constarán básicamente de agregar a las consultas ya construidas, las siguientes consultas (o porciones de consulta), que filtrarán información para traer la que corresponde al respectivo beneficiario, de la siguiente manera: 

 {{filtro_eatc_dona_headers (tipo_no_BdeA) }} 
 eatc-donation_manager_code= {{eatc_donation_managers. identificador_unico_registro }} 
 {{filtro_eatc_dona (tipo_no_BdeA) }} 
 eatc-donation_manager_code= {{eatc_donation_managers. identificador_unico_registro }} 
 {{filtro_eatc_dona_kpi (tipo_no_BdeA) }} 
 eatc-donation_manager_code= {{eatc_donation_managers. identificador_unico_registro }} 

 Posteriormente el sistema procederá a desplegar un formulario de creación de usuario y password (de Back Office), que guardará en la misma o las mismas estructuras de datos dispuestas para la autenticación original del BO beneficiarios (incluyendo firebase), desplegando un formulario de la siguiente manera: 

 Nombre de usuario 
 Place holder: 
 class=" lbl_usuario " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_usuario )  

 Valor por defecto para el cuadro de texto: 
 El guardado en la variable {{ usuario }} 

 Validación para el cuadro de texto: 
 El formulario deberá validar que se agregue un nombre de usuario. 

 El texto digitado se lleva: 
 Al repositorio o los repositorios en donde reposan los datos de acceso del actual bo_beneficiarios (incluyendo firebase) 

 Contraseña (cuadro de captura de texto doble para confirmar contraseña) 
 Place holder primer campo de captura: 
 class=" lbl_password " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_password )   

 Place holder segundocampo de captura: 
 class=" lbl_digita_de_nuevo_el_password " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_password )   

 Valor por defecto para los cuadros de texto: 
 Ninguno (es decir, debe mostrar el place holder) 

 Validaciones para el ingreso de la contraseña: 
 Fortaleza de la contraseña: mientras se va digitando la contraseña, debe aparecer el siguiente label de indicación, hasta que se ingrese una contraseña fuerte, caso en el cual se podrá continuar con el registro 
 class=" lbl_doma_psw_desc " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel=lbl_doma_psw_desc ) 
 Te recomendamos utilizar una contraseña fuerte que involucre signos, números y letras  
 Correspondencia entre las dos contraseñas digitadas: El formulario deberá validar que se agregue una contraseña, similar en ambos campos de captura, en caso de que esto no ocurra deberá desplegar el siguiente mensaje 
 class=" lbl_passwords_diferentes " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_passwords_diferentes ) 

 Las contraseñas ingresadas no son iguales.  

 El texto digitado se lleva: 
 Se debe guardar en a variable {{ password }} para posteriormente realizar la validación de la contraseña. 

 ***NUEVO: B OTÓN: INGRESO DIFERENTE A LA PRIMERA VEZ *** 
 class=" lbl_ingreso_diferente_primera_vez " ( https://datagov.eatcloud.info/api/eatcloud/eatc_config_labels? plataforma =beneficiarios&idlabel= lbl_ingreso_diferente_primera_vez ) 

 Flujo tradicional de login, como viene funcionando en este momento.  Lo único que hay que ajustar es que para las organizaciones tipo_BdeA, se debe actualizar 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"On"}] 
 3d5df893-77b7-409a-9f45-a3f25ed16f14 
 1!1!3 
 https://eastus0-2.pushfp.svc.ms/fluid 
 2f052cfa-512a-4b5a-bfa0-6f643c10ef25 
 2025-05-22T03:41:19.7893464Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"eaa1a2cd-ce42-40d7-9151-732d90172c74","SequenceId":430,"FluidContainerCustomId":"a882b9ed-8f91-415c-a809-a8382a795f85","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 LOGIN (URL ÚNICA)