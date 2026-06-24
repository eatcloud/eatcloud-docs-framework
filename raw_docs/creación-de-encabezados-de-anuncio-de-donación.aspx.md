# creación-de-encabezados-de-anuncio-de-donación.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CREACIÓN DE ENCABEZADOS DE ANUNCIO DE DONACIÓN ","encodedImage":"BBR:HGxufQ~qj[fQ"},"containsDynamicDataSource":false}">

 Proceso dinámico que opera sobre múltiples cuentas maestras 
 El proceso de creación de encabezados de donación debe correr para todas las cuentas maestras registradas en el respectivo maestro: 
 https://datagov.eatcloud.info/api/eatcloud/eatc_cua_master?_id=_ * 

 Este ajuste aplica tanto para los procesos de creación de encabezados activados por tareas programadas como los que son activados mediante servicios web. 

 Dado un anuncio de donación ( eatc_dona )  
 {{URL_entorno_donantes}}/api/{{eatc_cua. eatc_cua_master }}/eatc_dona?eatc-dona_header_code={{eatc-dona_header_code}} 

 la plataforma debe crear un encabezado en donde se deberán realizar algunas operaciones de totalización de información, y se adicionará información para facilitar las búsquedas en la plataforma.  Esta información se consolida en eatc_dona_headers 
 _DOM.base + "headersApp/" + _DOM.cua_master + _DOM.cua_user + code, 

 _crear_dona_headers.php 

 Exclusión de la generación de encabezados tradicional, a anuncios con asignación directa 
 El sistema deberá realizar la siguiente consulta: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_direct_dona?_id=_*&_distinct=eatc-pod_id 

 Si se requieren procesos diferentes por cuentas maestras, la consulta sería: 
 {{URL_entorno_datagov}}/api/eatcloud/eatc_direct_dona?eatc_cua_master={{_DOM.cua_master}}&_distinct=eatc-pod_id 

 Para establecer un array de códigos  de punto de donación obtenidos de la anterior consulta {{array_codigos}} , sobre los cuales este primer proceso de generación de encabezados no operará, dado que operará un proceso especial para generar un anuncio que será directamente adjudicado o programado. Esto aplica también para anuncios cuyo origen es a través de la Nueva WAPP (anuncios manuales) que se crean a través del servicio de creación de encabezados. 

 {{URL_entorno_donantes}}/api/{{_DOM.cua_master}}/eatc_dona?eatc-pod_id={{array_codigos}} 

 Al resto de anuncios le operará el proceso de creación tradicional de encabezado de anuncios de donación: 

 CREACIÓN TRADICIONAL DE ENCABEZADOS DE ANUNCIO DE DONACIÓN 

 Transformaciones internas 

 eatc-code   

 Código de la cabecera del anuncio de donación. Generalmente es entregado por el cliente y puede ser similar al identificador único.  Cada vez que llega un anuncio de donación ( eatc_dona ), este código corresponde al parámetro eatc-dona_header_code .  Se debe tener en cuenta que en el anuncio de donación esta información se repite, pero en el encabezado de anuncio de donación, no se puede repetir (es un identificador único). 

 eatc_dona.eatc-dona_header_code (https://donantes.eatcloud.info/api/devexito/eatc_dona?eatc-dona_header_code) 

 eatc-date   

 Fecha del anuncio de donación.  Cada vez que llega un anuncio de donación ( eatc_dona ), esta fecha que corresponde al parámetro eatc-date_time .  Se debe tener en cuenta que en el anuncio de donación esta información se puede repetir, pero en el encabezado de anuncio de donación, no se puede repetir (solo puede haber una fecha por anuncio de donación 

 eatc_dona.eatc-date_time ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_date_time) 

 eatc-pod_id   
 Identificador único del punto de donación.  Cada vez que llega un anuncio de donación ( eatc_dona ), este identificador que corresponde al parámetro eatc-pod_id .  Se debe tener en cuenta que en el anuncio de donación esta información se puede repetir, pero en el encabezado de anuncio de donación, no se puede repetir (solo puede haber una fecha por anuncio de donación 

 eatc_dona.eatc-pod_id ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-pod_id) 

 eatc-donor_code   
 Código del donante (dada la característica que existen anuncios de donaciones que provienen de un donante pero que tienen mercancía de otro, se requiere esta información para identificarlos en el sistema).  Cada vez que llega un anuncio de donación ( eatc_dona ), este identificador que corresponde al parámetro eatc-donor_code .  Se debe tener en cuenta que en el anuncio de donación esta información se puede repetir, pero en el encabezado de anuncio de donación, no se puede repetir (solo puede haber un donante por anuncio) 

 eatc_dona.eatc-donor_code ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-donor_code) 

 eatc-donor   
 Nombre del donante (por como se extrae corresponde al mismo nombre de cuenta de EatCloud).  Cada vez que llega un anuncio de donación ( eatc_dona ), este identificador que corresponde al parámetro eatc-donor .  Se debe tener en cuenta que en el anuncio de donación esta información se puede repetir, pero en el encabezado de anuncio de donación, no se puede repetir (solo puede haber un donante por anuncio) 

 eatc_dona. eatc-donor ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-donor_code) 

 eatc_cua_origin   
 Cuenta desde la cual se crea el anuncio.  Cada vez que llega un anuncio de donación ( eatc_dona ), este identificador que corresponde al parámetro eatc_cua_origin .  

 eatc_dona. eatc_cua_origin ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona? eatc_cua_origin ) 

 eatc-provider_id   
 Corresponde a la identificación o array de identificaciones que poseen los productos del anuncio correspondiente 
 eatc_dona. eatc-provider_id ({{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}}) 

 Querys 

 eatc_cua_size 
 Tamaño de la cuenta que dona el anuncio.  Para obtenerla se debe tomar el eatc-donor e ir al API de consulta de cuentas  (eatc_cua), para traer el parámetro. 

 eatc_cua. eatc_cua_size ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua? name = {{ eatc-donor }}) 

 eatc_pod_name   
 Corresponde al nombre del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación ( eatc_pods ), para traer el parámetro. 

 eatc_pods.eatc-name ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 
 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39", entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   y por lo tanto la "eatc_pod_name" es igual a " EXITO SAN ANTONIO " y este es el dato que debe llevarse al eatc_dona_headers . 

 eatc-pod_address   
 Corresponde a la dirección del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación ( eatc_pods ), para traer el parámetro. 

 eatc_pods.eatc-adress ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la "eatc-pod_address" es igual a " Cl. 48 #46-115, Medellín, Antioquia " y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-pod_phone   
 Corresponde a la dirección del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación ( eatc_pods ), para traer el parámetro. 

 eatc_pods.eatc-adress ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39   y por lo tanto la "eatc-pod_phone" es igual a "(4) 6050372 " y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-pod_typology_a   
 Corresponde a la primera tipología del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación ( eatc_pods ), para traer el parámetro. 

 eatc_pods.eatc-pod_typology_a ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la "eatc-pod_typology_a" es igual a "Exito" y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-pod_typology_b   
 Corresponde a la segunda tipología del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-pod_typology_b ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la "eatc-pod_typology_b" es igual a "DISTRITO MEDELLIN B" y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-pod_typology_c   
 Corresponde a la segunda tipología del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-pod_typology_c ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la "eatc-pod_typology_c" es igual a "MEDELLIN" y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-pod_size 
 Corresponde a la segunda tipología del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-size ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "alimentoscarnicos" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "nutresa_bog", entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/ alimentoscarnicos /eatc_pods?eatc-id= nutresa_bog   y por lo tanto la " eatc-size " es igual a " canal_moderno " y este es el dato que debe llevarse al eatc_dona_headers . eatc-pod_size 

 eatc-lat   
 Cuando se crea el encabezado, corresponde la la latitud del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-lat ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la " eatc-lat " es igual a " 6.24678 " y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-lon   
 Cuando se crea el encabezado, corresponde la la longitud del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-lon ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la " eatc-lat " es igual a " 6.24678 " y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-city   
 Cuando se crea el encabezado, corresponde la ciudad del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-city ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la " eatc-city " es igual a " Medellín " y este es el dato que debe llevarse al eatc_dona_headers 

 eatc-province   
 Cuando se crea el encabezado, corresponde al departamento/provincia/estado del punto de donación. Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 

 eatc_pods.eatc-province ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}}) 

 Ejemplo: Ambiente de pruebas, cuenta "exito" 

 En llega información de un anuncio de donación cuyo "eatc-pod_id" es "39" (Éxito de San Antonio), entonces la consulta a realizar es: https://devdonantes.eatcloud.info/api/exito/eatc_pods?eatc-id=39 y por lo tanto la " eatc-province " es (SERÁ cuando se implemente: https://app.asana.com/0/698639369029630/1185863324863385 ) igual a " ANTIOQUIA " y este es el dato que debe llevarse al eatc_dona_headers 

 ***NUEVO: eatc_comuna_localidad *** (campo a crear en eatc_dona_headers y eatc_deleted_dona_header) 
 Cuando se crea el encabezado, corresponde a la localidad o comumna del punto de donación (en caso de que exista). Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 
 eatc_pods. eatc_comuna_localidad {{URL_entorno_donantes}}/api/ allpods /eatc_pods?eatc-id={{eatc-pod_id}}&eatc-cua= {{eatc_cua}} &_cmp= eatc_comuna_localidad 

 ***NUEVO: eatc_special_project *** 
 Cuando se crea el encabezado, se deberá llevar al mismo si es producido por un punto de donación que fue creado gracias a un proyecto especial  (en caso de que así sea, en caso contrario no se realiza ningún registro). 
 eatc_pods. eatc_special_project {{URL_entorno_donantes}}/api/ allpods /eatc_pods?eatc-id={{eatc-pod_id}}&eatc-cua= {{eatc_cua}} &_cmp= eatc_special_project 

 eatc_region 
 Cuando se crea el encabezado, corresponde a la región del punto de donación (en caso de que exista). Para obtenerla se debe tomar el eatc-pod_id e ir al API de consulta de puntos de donación (eatc_pods), para traer el parámetro. 
 eatc_pods. eatc_region ({{URL_entorno_donantes}}/api/ {{eatc_cua}} /eatc_pods?eatc-id={{eatc-pod_id}})&_cmp=eatc_region 

 eatc_rec_doc   
 Al valor del parámetro eatc_rec_doc, de la cuenta respectiva (eatc_donor) 
 eatc_cua.eatc_rec_doc (https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{eatc-donor}}) 

 eatc_rec_doc_signature   
 Este dato corresponde al valor del parámetro eatc_rec_doc_signature , de la cuenta respectiva ( eatc_donor ) 
 eatc_cua.eatc_rec_doc_signature (https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{eatc-donor}}) 

 Ejemplo: cuenta "nutresa" 

 Para un anuncio cuyo eatc-donor es "nutresa" este parámetro debe guardar "y" dado que en la consulta respectiva ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=nutresa ) este es el dato guardado en el parámetro de la cuenta (CUA) eatc_rec_doc_signature  

 eatc_rec_odds_pre_verification   
 Este dato corresponde al valor del parámetro eatc_rec_odds_pre_verification , de la cuenta respectiva ( eatc_donor ) 
 eatc_cua.eatc_rec_odds_pre_verification (https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{eatc-donor}}) 

 Ejemplo: cuenta "nutresa" 
 Para un anuncio cuyo eatc-donor es "nutresa" este parámetro debe guardar "y" dado que en la consulta respectiva ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name=nutresa ) este es el dato guardado en el parámetro de la cuenta (CUA) eatc_rec_odds_pre_verification  

 eatc_vertical   
 Este dato corresponde al valor del parámetro vertical , de la cuenta respectiva ( eatc_cua_origin ) 
 eatc_cua. vertical (https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name={{ eatc_cua_origin }}) 

 Ejemplo: cuenta "starbucks" 
 Para un anuncio cuyo eatc_cua_origin es " starbucks " este parámetro debe guardar " horeca " dado que en la consulta respectiva ( https://datagov.eatcloud.info/api/eatcloud/eatc_cua?name= starbucks ) este es el dato guardado en el parámetro de la cuenta (CUA) vertical   

 ***NUEVO: eatc_donor_certified_by_doma *** (campo a crear en eatc_dona_headers y eatc_deleted_dona_header) 
 Cuando se crea el encabezado el sistema deberá utilizar los datos consignados en:  
 _DOM. cua_master  
 eatc_dona_headers. eatc-donor 
 eatc_dona_headers. eatc-pod_id 
para realizar la siguiente consulta: 
 {{URL_datagov}} /api/eatcloud/ eatc_doma_certification ?eatc_cua_master={{ _DOM. cua_master  }}&eatc_cua_user={{ eatc_dona_headers. eatc-donor }}&eatc_pod_id={{ eatc_dona_headers. eatc-pod_id }}&_cmp= eatc_certifying_doma_id 
Si obtiene respuesta, guarda el dato obtenido en la variable {{ eatc_certifying_doma_id }}.  Si no obtiene respuesta, procede a realizar la siguiente consulta: 
 {{URL_datagov}} /api/eatcloud/ eatc_doma_certification ?eatc_cua_master={{ _DOM. cua_master  }}&eatc_cua_user={{ eatc_dona_headers. eatc-donor }}&eatc_pod_id= _all &_cmp= eatc_certifying_doma_id 
Si obtiene respuesta, guarda el dato obtenido en la variable {{ eatc_certifying_doma_id }}.  Si no obtiene respuesta, procede a realizar la siguiente consulta: 
{{URL_beneficiarios}}/api/ {{ _DOM. cua_master  }} / eatc_donation_managers ?beneficiary_ecosystem_leader= y &_cmp= identificador_unico_registro 
La respuesta obtenida la guarda en la variable {{ eatc_certifying_doma_id }}.  Con el dato obtenido, realiza la siguiente escritura: 
{{URL_donantes}}/crd/ {{ _DOM. cua_master  }}/?_tabla=eatc_dona_headers&_operacion=update& eatc_donor_certified_by_doma = {{ eatc_certifying_doma_id }}&WHEREeatc-code= {{ eatc_dona_headers. eatc-code }} 

 Funciones 

 eatc-original_cost   
 Costo original  total del anuncio de donación, es decir la sumatoria de " eatc-odd_unit_weight_kg * eatc-odd_original_quantity " del anuncio de donación (eatc_dona) cuyo "eatc-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo). 
 suma(eatc_dona.( eatc-odd_unit_weight_kg * eatc-odd_original_quantity )) 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes " eatc-odd_unit_weight_kg * eatc-odd_original_quantity " y por lo tanto "eatc-original_cost" es: + + + + += 

 eatc-total_cost   
 Costo total del anuncio de donación, es decir la sumatoria de "eact-total_cost" del anuncio de donación (eatc_dona) cuyo "eatc-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo). Cuando se genera el anuncio este valor es igual a eatc-original_cost 
 suma(eatc_dona.eact-total_cost)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eact-total_cost" y por lo tanto "eatc-total_cost" es: + + + + += 

 eatc-original_VAT ***NUEVO: solamente se calcula para los productos clasificados como “alimentos”: eatc-odds_typology_a=food *** 
 Valor original total del impuesto a las ventas de los alimentos, que corresponde al valor del impuesto a las ventas de los alimentos cuya eatc-odds_typology_a=!other 

 {{URL_entorno_donantes}} /api/ {{ eatc_cua_master .eatc_cua}}/eatc_dona? eatc-dona_header_code ={{eatc-code}}& eatc-odd_typology_a = !other& _sum= eatc-original_VAT 
 ***NOTA IMPORTANTE: se deberá realizar esta implementación cuando se termine el proceso de clasificación de artículos y de donaciones: https://app.asana.com/0/1209271596729752/1209252487083670  

 Ejemplo: ambiente de pruebas, cuenta maestra "abaco" 

 En llega información de un anuncio de donación (en ambiente de pruebas) cuyo "eatc-dona_header_code" es "abacoabaco_bog20200414151341645", la consulta sería: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=abacoabaco_bog20200414151341645 & eatc-odd_typology_a = !other& _sum= eatc-original_VAT 

  y por lo tanto "eatc-original_VAT" es = 1265.4 

 Anteriormente:  
 Valor original total del impuesto a las ventas (sumatoria de todos los impuestos a las ventas aplicables a los detalles del anuncio) 
 suma(eatc_dona.eatc-original_VAT)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: ambiente de pruebas, cuenta maestra "abaco" 

 En llega información de un anuncio de donación (en ambiente de pruebas) cuyo "eatc-dona_header_code" es "abacoabaco_bog20200414151341645", entonces el sistema consulta los diferentes "eatc-original_VAT" del eatc_dona respectivo ( https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=abacoabaco_bog20200414151341645 ) y por lo tanto "eatc-original_VAT" es: 231.99+ 1033.41 = 1265.4 

 eatc-total_VAT ***NUEVO: solamente se calcula para los productos clasificados como “alimentos”: eatc-odds_typology_a=food *** 
 Valor original total del impuesto a las ventas de los alimentos, que corresponde al valor del impuesto a las ventas de los alimentos cuya eatc-odds_typology_a=!other 

 {{URL_entorno_donantes}} /api/ {{ eatc_cua_master .eatc_cua}}/eatc_dona? eatc-dona_header_code ={{eatc-code}}& eatc-odd_typology_a = !other& _sum= eatc-total_VAT 
 ***NOTA IMPORTANTE: se deberá realizar esta implementación cuando se termine el proceso de clasificación de artículos y de donaciones: https://app.asana.com/0/1209271596729752/1209252487083670  

 Ejemplo: ambiente de pruebas, cuenta maestra "abaco" 

 En llega información de un anuncio de donación (en ambiente de pruebas) cuyo "eatc-dona_header_code" es "abacoabaco_bog20200414151341645", la consulta sería: 

 https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=abacoabaco_bog20200414151341645 & eatc-odd_typology_a = !other& _sum= eatc-total_VAT   

  y por lo tanto "eatc-total_VAT" es = 1265.4 = eatc-original_VAT (cuando se está creando la donación. Cuando se recalcula el header después de una verificación de donación, el valor puede diferir) 

 ANTERIORMENTE 

 Valor definitivo total del impuesto a las ventas (sumatoria de todos los impuestos a las ventas aplicables a los detalles del anuncio), después del proceso de verificación. Cuando se genera el anuncio este valor es igual a eatc-original_VAT 
 suma(eatc_dona.eact-total_VAT)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: ambiente de pruebas cuenta maestra "abaco" 

 En llega información de un anuncio de donación (en ambiente de pruebas) cuyo "eatc-dona_header_code" es "abacoabaco_bog20200414151341645", entonces el sistema consulta los diferentes "eatc-total_VAT" del eatc_dona respectivo ( https://devdonantes.eatcloud.info/api/abaco/eatc_dona?eatc-dona_header_code=abacoabaco_bog20200414151341645 ) y por lo tanto "eatc-total_VAT" es: 231.99+ 1033.41 = 1265.4 = eatc-original_VAT 

 eatc-original_weight_kg   
 Peso Original total del anuncio de donación, es decir la sumatoria de " eatc-odd_original_quantity * eatc-odd_unit_weight_kg " del "eatc_dona" cuyo "eact-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo) 
 suma(eatc_dona.( eatc-odd_original_quantity * eatc-odd_unit_weight_kg ))  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes " eatc-odd_original_quantity * eatc-odd_unit_weight_kg " y por lo tanto "eatc-total_weight_kg" es: + + + + += 

 eatc-total_weight_kg   
 Peso total del anuncio de donación, es decir la sumatoria de "eatc-odd_total_weight_kg" del "eatc_dona" cuyo "eact-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo). Cuando se genera el anuncio este valor es igual a eatc-original_weight_kg 
 suma(eatc_dona.eatc-odd_total_weight_kg)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eatc-odd_total_weight_kg" y por lo tanto "eatc-total_weight_kg" es: + + + + += 

 eatc-total_volume_cm3   
 Volumen total del anuncio de donación, es decir la sumatoria de "eatc-odd_total_volume_cm3" del "eatc_dona" cuyo "eact-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo) 
 suma(eatc_dona.eatc-odd_total_volume_cm3)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eatc-odd_total_volume_cm3" y por lo tanto "eatc-total_volume_cm3" es: + + + + += 

 eatc_closer_expiration_date ***NUEVO : valor por defecto cuándo no hay fechas en eatc_dona *** 
 El sistema debe evaluar las fechas consignadas en el parámeto  eatc_dona. eatc-closer_expiration_date respectivo 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}}&_cmp= eatc-closer_expiration_date 

 ,y guardar la más próxima (es decir la fecha de expiración del producto que se vence antes) en este campo del encabezado ( eatc_dona_headers. eatc_closer_expiration_date ). 
 Valor por defecto cuando no hay registros en eatc_dona. eatc-closer_expiration_date 
Cuando la donación no posee registros en eatc_dona. eatc-closer_expiration_date, el sistema deberá colocar como eatc_dona_headers. eatc_closer_expiration_date el valor contenido en eatc_dona_headers .eatc-cancellation_datetime es decir, la fecha más próxima de expiración, será igual a la fecha (la porción correspondiente) de cancelación.   

 NOTA: se documenta este ajuste, dado que después de una revisión para realizar un ajuste necesario, se encontró que esta fecha por defecto se colocaba sumando dos horas a otra fecha de la donación y este comportamiento no permite implementar la mejora propuesta de manera adecuada (que trata sobre la limitación del date picker de programación y que debe contener información sobre la fecha más próxima de vencimiento para limitar dicho selector). 

 Ejemplo: 

 En el detalle del anuncio hay un producto con eatc-closer_expiration_date   = 2020-03-10, otro con eatc-closer_expiration_date   = 2020-03-11 y otro con eatc-closer_expiration_date   = 2020-03-14, por lo tanto el sistema debe guardar en el parámetro eatc_closer_expiration_date del encabezado la fecha "2020-03-10", que es la más próxima de las tres. 

 eatc-contains_alergens   
 Si cualquiera  de los detalles del anuncio de donación  eatc_dona. eatc-contains_alergens respectivo, tiene como valor "si" en este parámetro ( eatc_dona. eatc-contains_alergens. Con solo uno que lo tenga se cumple la regla), el encabezado respectivo debe tener  en el valor eatc-contains_alergens =si . 

   eatc-warning   
 Si en el eatc_dona, el parámetro eatc-warning   con información, se debe consolidar un mensaje para escribir en el campo eatc-warning del encabezado de anuncio de donación  lo siguiente: 

 La(s) Orden(es) de despacho ${array de eatc-doc} ha(n) sido retirada(s) del anuncio de donación del día de hoy por tener el (los) PLU(s) ${array de PLUs que no corresponden correspondientes a la consulta eatc_dona_errors.eatc-odd_id https://devdonantes.eatcloud.info/api/abaco/eatc_dona_errors?eatc-doc=${array de eatc-doc}} que no esta(n) autorizado(s) a ser donados. POR FAVOR NO RECIBA/ENTREGUE ESTA MERCANCÍA COMO DONACIÓN.  

 ****NUEVO***** 
 Si existe información en el parámetro : eatc-closer_expiration_date del encabezado se debe generar una escritura en el warning (sin borrar otras escrituras previas) 

 Precaución: el presente anuncio contiene productos cuya fecha de expiración más próxima es [eatc_dona_header. eatc-closer_expiration_date] . 

 ****NUEVO***** 
 Si en el parámetro eatc_dona. eatc-contains_alergens tiene como valor "SI", se debe generar un regirstro en  eatc-warning   (sin borrar otras escrituras previas) de la siguiente forma: 

 Precaución: el presente anuncio de donación contiene alérgenos. 

 eatc_dona_references  
 Se deberá guardar el número de referencias del anuncio; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona?eatc-dona_header_code={{eatc_dona_headers. eatc-code }}&_distinct=eatc-odd_id&_cont 

 Se toma el resultado obtenido en " count " y se lleva al parámetro en cuestión. 

 NOTA IMPORTANTE: la escritura de este dato se deberá realizar en los  procesos bulk y los bajo demanda y también cuando se recalculen los datos de los encabezados (por ejemplo cuando se edita una donación). 

 eatc_dona_units 
 Se deberá guardar el número de unidades del anuncio; para ello deberá consultar para cada anuncio (partiendo de su código de cabecera eatc_dona_headers. eatc-code los detalles del mismo de la siguiente manera: 

 {{ URL_entorno_donantes }}/api/{{_DOM. cua_master }}/eatc_dona?eatc-dona_header_code={{eatc_dona_headers. eatc-code }} &_sum = eatc-odd_quantity 

 NOTA IMPORTANTE: la escritura de este dato se deberá realizar en los  procesos bulk y los bajo demanda y también cuando se recalculen los datos de los encabezados (por ejemplo cuando se edita una donación). 

 Calificaciones 
 El manejo de las calificaciones de los puntos de donación y de los gestores de donación se desarrolla aquí . 

 eatc-donation_manager_score = //Score del gestor de donaciones al cual se le adjudica el anuncio, al momento de la adjudicación 
 eatc-pod_score = //Score del punto de donación que realiza el anuncio, al momento de la creación del encabezado 

 Publicación del anuncio 
 Una vez se terminan los anteriores pasos, el anuncio puede ser publicado.  Al hacerlo el sistema debe guardar la siguiente información: 

 #publicación 

 eatc-publication_date 
 fecha de la publicación (fecha sin la hora, para poder hacer consultas por fecha de anuncios generados) en formato AAAA-MM-DD 

 eatc-publication_datetime 
 Fecha y hora de publicación del anuncio de donación en formato AAAA-MM-DD HH:MM:SS 

 eatc_dona_headers. eatc-cancellation_datetime 

 El cálculo tradicional se debe realizar tal como se venía haciendo, pero el dato obtenido se debe guardar en una variable  eatc-cancellation_datetime1 

 IF eatc_cua_origin= eatc-donor (eatc-cancellation_datetime = eatc-publication_datetime + eatc_timeout_rules .eatc-timeout_in_hours    
 {{URL_entorno_donantes}} /api/{{eatc_cua_master .eatc_cua }}/ eatc_timeout_rules ?eatc-timeout_name =dona_cancellation_timeout )   

 ELSE  
 (eatc-cancellation_datetime = eatc-publication_datetime + eatc_timeout_rules .eatc-timeout_in_hours    
 {{URL_entorno_donantes}} /api/{{eatc_cua_master. eatc_cua }}/ eatc_timeout_rules ?eatc-timeout_name =dona_nng_cancellation_timeout ) 

 Si no existe dato en " eatc_dona_headers. eatc_closer_expiration_date " (es vacío, nulo o cero) entonces eatc- cancellation_datetime = " eatc-cancellation_datetime1 " 

 ***NUEVO: si el anuncio tiene registrado el dato “ eatc_closer_expiration_date ” y (prueba lógica “y”, debe cumplir ambas condiciones) dicha fecha es posterior a “ eatc-cancellation_datetime1 ” (calculada en el algoritmo original ) colocar como fecha de cancelación el dato consignado en eatc_closer_expiration_date   MENOS UN DÍA *** en los casos en donde no haya fecha de expiración más próxima, el proceso coloca la fecha de cancelación según los timeouts” 
 NOTA EXPLICATIVA: cuando se solicitó la mejora  que dio como resultado esta documentación, la misma fue fruto de donaciones cuya fecha de vencimiento era larga y superaba la fecha de cancelación del anuncio.  Como quedó documentado en un principio, en donde en todo caso en donde había una “ eatc_closer_expiration_date ” en el anuncio, se generaba una fecha de cancelación a partir de ella, primero se generaron problemas por fechas próximas, que quedaban inclusive con fecha de cancelación anterior a la de publicación (error que ya fue corregido) pero ahora se reportan inconvenientes, cuando la cancelación de los anuncios no corresponden a las políticas definidas por las empresas en los timeouts , en especial cuando las cancelaciones son más próximas de lo que proponen los timeouts. Por esa razón se limita el uso de la fecha consignada en “ eatc_closer_expiration_date ”, a los casos en donde dicha fecha, supera la fecha de cancelación calculada a partir de los timeout como se hacía originalmente . 

 Si existe dato válido en  " eatc_dona_headers .eatc_closer_expiration_date " y  eatc_dona_headers. eatc_closer_expiration_date > eatc-cancellation_datetime1 , entonces   eatc-cancellation_datetime = {{eatc_dona_headers. eatc_closer_expiration_date }} - 1 día 

 DEPRECADO: si el anuncio tiene registrado el dato “eatc_closer_expiration_date” colocar como fecha de cancelación el dato consignado en eatc_closer_expiration_date   MENOS UN DÍA en los casos en donde no haya fecha de expiración más próxima, el proceso coloca la fecha de cancelación según los timeouts” 
 NOTA EXPLICATIVA: esta definición busca que un anuncio de donación, no se cancele hasta que sus todos sus productos tengan aun una vida útil y se aun se puedan gestionar el anuncio (por eso la condición de un día antes de la fecha más próxima de expiración), es por eso que haciendo el cálculo tradicional de la fecha de cancelación (según los respectivos timeouts), y cuando el anuncio tenga dato válido (no en cero, vacío o nulo) en el campo “ eatc_closer_expiration_date ”, la fecha de cancelación del anuncio será entonces la fecha guardada en “ eatc_closer_expiration_date ”, menos un día, siempre y cuando esta fecha no sea inferior a la fecha de creación del anuncio.  En caso que la eatc_closer_expiration_date corresponda al día en curso, y así al restarle un día la fecha y hora de cancelación quede anterior a la fecha de publicación, el sistema colocará como fecha y hora de cancelación las 11:55 PM del día en curso (si el anuncio se hace en la mañana) y el medio día del día siguiente (si el anuncio se hace en horas de la noche. 

 Si existe dato válido en  " eatc_dona_headers. eatc_closer_expiration_date ", entonces   eatc-cancellation_datetime = {{ eatc_dona_headers. eatc_closer_expiration_date}} - 1 día 

 Deprecado: 
 Se debe comparar con el dato " eatc_dona_headers. eatc_closer_expiration_date ", en cuanto a fecha se refiere.   
 Si la fecha es igual en ambos datos, el dato que se debe llevar al campo ( eatc_dona_headers. eatc-cancellation_datetime ) será cancellation_datetime1 . 
 Si eatc-cancellation_datetime1 es más próximo que (en cuanto a fecha se refiere) que    eatc_closer_expiration_date , se llevará al dato eatc-cancellation_datetime1 
 Si eatc_closer_expiration_date es más próximo que (en cuanto a fecha se refiere) que  eatc-cancellation_datetime1 , se llevará al dato eatc_closer_expiration_date con la hora última de dicho día (es decir 23:59:59 ) 

 A continuación se presentan ejemplos de los tres casos descritos anteriormente: 

 Si la fecha es igual en ambos datos, el dato que se debe llevar al campo ( eatc_dona_headers. eatc-cancellation_datetime ) será cancellation_datetime1 .   

 Ejemplo 1: 
 Después de correr el algoritmo de cálculo de eatc-cancellation_datetime1 , el mismo dió como resultado eatc-cancellation_datetime1 =2023-03-08 20:20:20 y para la misma donación el dato eatc_closer_expiration_date= 2023-03-08.  Como en fecha es más próximo el dato registrados en eatc_closer_expiration_date, entonces al campo "eatc_dona_headers. eatc-cancellation_datetime " se llevará el dato registrado en  eatc-cancellation_datetime1 =2023-03-08 20:20:20 

 Si eatc-cancellation_datetime1 es más próximo que (en cuanto a fecha se refiere) que    eatc_closer_expiration_date , se llevará al dato eatc-cancellation_datetime1 

 Ejemplo 2: 
 Después de correr el algoritmo de cálculo de eatc-cancellation_datetime1 , el mismo dió como resultado eatc-cancellation_datetime1 =2023-03-09 20:20:20 y para la misma donación el dato eatc_closer_expiration_date= 2023-03-10.  Como en fecha es más próximo el dato registrados en eatc_closer_expiration_date, entonces al campo "eatc_dona_headers. eatc-cancellation_datetime " se llevará el dato registrado en  eatc-cancellation_datetime1 =2023-03-08 20:20:20 

 Si eatc_closer_expiration_date es más próximo que (en cuanto a fecha se refiere) que  eatc-cancellation_datetime1 , se llevará al dato eatc_closer_expiration_date con la hora última de dicho día (es decir 23:59:59 ) 

 Ejemplo 3: 
 Después de correr el algoritmo de cálculo de eatc-cancellation_datetime1 , el mismo dió como resultado eatc-cancellation_datetime1 =2023-03-09 20:20:20 y para la misma donación el dato eatc_closer_expiration_date= 2023-03-08.  Como en fecha es más próximo el dato registrados en eatc_closer_expiration_date, entonces al campo "eatc_dona_headers. eatc-cancellation_datetime " se llevará el dato: 2023-03-08 23:59:59 *** 

 eatc-id  
 identificador único del anuncio de donación, que lo genera el sistema 

 eatc-state 
 El estado al publicarse debe ser " announced " 

 eatc-verification_code 
 Código de verificación (que se utilizará en las funcionalidades " Entrega de donación: hora de llegada (eatc_doma_checkin) " y " Código para recogida de donación (eatc_dona_code) ".  Es un código único de 6 dígitos (puede corresponder a un hash de alguna información del anuncio) que se genera para cada encabezado y que servirá para validar la identidad de quien recoge. 

 EatCloud 
 Corresponde a información que se agrega a partir de la interacción con la plataforma.  Por este motivo, cuando se crea un anuncio de donación se deben crear estos campos pero dejarlos vacíos. 

 eatc-adjudication_datetime = //Fecha y hora de la adjudicación del anuncio de donación 
 eatc-donation_manager_user_doc_id = //Documento de identidad del usuario que acepta la donación 
 eatc-donation_manager_code = //Código del gestor de donaciones al cual se le adjudica el anuncio (eatc_donation_managers.identificador_unico_registro) 
 eatc-donation_manager_name = //Nombre del gestor de donaciones al cual se le adjudica el anuncio (eatc_donation_managers.organizacin) 
 eatc-donation_manager_address = //Dirección del gestor de donaciones al cual se le adjudica el anuncio (eatc_donation_managers.unidad_territorial) 
 eatc-donation_manager_phone = //Teléfono del gestor de donaciones al cual se le adjudica el anuncio (eatc_donation_managers.telefono1) 
 eatc-donation_manager_typology_a = //Primera tipología del gestor de donaciones al cual se le adjudica el anuncio (eatc_donation_managers.organizacion_vinculada) 
 eatc-donation_manager_typology_b = //Segunda tipología del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-donation_manager_typology_c = //Tercera tipología del gestor de donaciones al cual se le adjudica el anuncio 
 eatc-scheduling_datetime = //Fecha y hora en la cual se efectuó la programación de la recogida del anuncio de donación 
 eatc-programed_picking_datetime = //Fecha y hora programada de la recogida del anuncio de donación 
 eatc-picker_name = //Nombre de la persona quien recoge la donación 
 eatc-picker_doc_id = //Documento de identidad de la persona quien recoge la donación 
 eatc-picker_license_plate = //Nombre de la persona quien recoge la donación 
 eatc-picker_start_datetime = // Fecha y hora en que se activa la funcionalidad de "recoger anuncio de donación" 
 eatc-picker_lat = // Latitud de quien recoge 
 eatc-picker_lon = // Longitud de quien recoge 
 eatc-picking_checkin_datetime = //Fecha y hora real del ingreso a la recogida del anuncio de donación 
 eatc-check_datetime = //Fecha y hora cuando se termina el chequeo de la donación en el punto de donación 
 eatc-picking_checkout_datetime = //Fecha y hora real de la salida de la recogida del anuncio de donación 
 eatc-receipt_datetime = //Fecha y hora de la recepción del anuncio de donación en las instalaciones del gestor de las donaciones 
 eatc-pre_certification_datetime = //Fecha y hora de la certificación preliminar del anuncio de donación 
 eatc-certification_datetime = //Fecha y hora de la certificación del anuncio de donación 
 eatc_doc_datetime = //Fecha y hora de subida de documentos al sistema 
 eatc_doc_url = //URL de los documentos guardados 
 eatc_rec_doc_signature_datetime = //Fecha y hora de la verificación de la firma del documento soporte 
 eatc_rec_odds_pre_verification_datetime = //Fecha y hora de la pre-verificación de los artículos 

 Verificación del anuncio (PENDIENTE) 
 Una vez se realiza la verificación del anuncio los anteriores pasos ( eatc-state= recieved ). El sistema ajusta (desde el dispositivo) la siguiente información: 

 _DOM.base + "headersApp/" + _DOM.cua_master + _DOM.cua_user + code, 

 eatc-total_cost   
 Costo total del anuncio de donación, es decir la sumatoria de "eact-total_cost" del anuncio de donación (eatc_dona) cuyo "eatc-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo). 
 suma(eatc_dona.eact-total_cost)  
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eact-total_cost" y por lo tanto "eatc-total_cost" es: + + + + += 

 eatc-total_VAT   
 Valor definitivo total del impuesto a las ventas (sumatoria de todos los impuestos a las ventas aplicables a los detalles del anuncio), después del proceso de verificación. 

 suma(eatc_dona.eact-total_VAT) 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eact-total_VAT" y por lo tanto "eatc-total_VAT" es: + + + + += 

 eatc-total_weight_kg   
 Peso total del anuncio de donación, es decir la sumatoria de "eatc-odd_total_weight_kg" del "eatc_dona" cuyo "eact-dona_header_code" corresponde a "eatc-code" del "eatc_dona_header" respectivo) 

 suma(eatc_dona.eatc-odd_total_weight_kg) 
 {{URL_entorno_donantes}}/api/{{eatc_cua_master. eatc_cua }}/eatc_dona?eatc-dona_header_code={{eatc-code}} 

 Ejemplo: 

 En llega información de un anuncio de donación cuyo "eatc-dona_header_code" es "________", entonces el sistema consulta los diferentes "eatc-odd_total_weight_kg" y por lo tanto "eatc-total_weight_kg" es: + + + + += 

 LLAMADO AL SERVICIO PARA LA EVALUACIÓN EXCESIVO - EXW 
 Nota importante: este llamado debe funcionar tanto para los procesos que se llaman por cronjobs, como para los que se llaman bajo demanda. 

 Endpoint (según documentación : sujeto a revisión) 
 {{URL_entorno_datagov}}/exw 

 Parámetros para el llamado al servicio: 
 eatc_dona_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio 

 eatc_telgram_msg: 
 "y" 

 ***NUEVO : LLAMADO AL SERVICIO PARA CLASIFICACIÓN CON RESPECTO A FECHAS CORTAS " SHORT_DATES_CLASSIFICATION " *** 
 Nota importante: inicialmente esto solamente operará para los anuncios de Mexico (piloto Nestlé). Luego se evaluará extender la aplicación a otros procesos de otras cuentas maestras. 

 Endpoint (según documentación : sujeto a revisión) 
 {{ URL_entorno_donantes }}/ short_dates_classification /{{ _DOM. cua_master }}/   

 por lo dicho anteriormente el EndPoint inicial será: 

 {{ URL_entorno_donantes }}/ short_dates_classification /mexico/   

 Parámetros para el llamado al servicio: 
 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio (para la URL del endpoint) 

 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_headers. eatc-code => parámetro de carácter obligatorio 

 eatc_donor: 
 Código donante: eatc_dona_headers. eatc-donor => parámetro de carácter obligatorio 

 eatc_closer_expiration_date: 
 Fecha más próxima de expiración para el anuncio: eatc_dona_headers. eatc_closer_expiration_date => parámetro de carácter obligatorio 

 Así se construirá entonces el llamado: 

 {{ URL_entorno_donantes }}/ short_dates_classification /{{ _DOM. cua_master }}/?eatc_dona_header_code={{ eatc_dona_headers. eatc-code }}& eatc_donor = {{ eatc_dona_headers. eatc-donor } }& eatc_closer_expiration_date={{ eatc_dona_headers .eatc_closer_expiration_date } } 

 EJEMPLO (ambiente de pruebas):  
 https://devdonantes.eatcloud.info/ short_dates_classification /mexico/? eatc_dona_header_code = 00002108194223 & eatc_donor = {{ eatc_dona_headers. eatc-donor } }& eatc_closer_expiration_date=2021-09-01 

 Nota importante : el presente servicio de clasificación se deberá llamar antes de que se invoque el servicio para realizar el match (donamatchclass: cuya documentación se puede consultar aquí ) , ya que su resultado infiere en el proceso de match (inicialmente para el caso específico de Mexico)   

 DEPRECADO: LLAMADO A SERVICIOS DE INTEGRACIÓN CON BLOCKCHAIN 
 Nota importante: estos llamados deben funcionar tanto para los procesos que se llaman por cronjobs, como para los que se llaman bajo demanda. 

 Endpoint: Creación de encabezados (según documentación : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmDonacionExcedente 

 Endpoint: Creación de detalles (según documentación : sujeto a revisión) 
 {{ URL_entorno_datagov }}/int/eatcloud/int_blockchain?eatc_cua_master={{_DOM. cua_master }}&eatc_dona_header_code={{eatc_dona_headers. eatc-code }}&_servicio=frmBulkProductoDonacion 

 Parámetros para el llamado al servicio: 
 eatc_dona_header_code: 
 Código del anuncio de donación recientemente creado: eatc_dona_heaaders. eatc-code => parámetro de carácter obligatorio 

 eatc_cua_master: 
 Cuenta maestra a la cual pertenece el anuncio ( _DOM. cua_master ) => parámetro de carácter obligatorio 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 
 e3149ff7-8f72-4812-aaf7-715175743d04 
 4!1!3 
 https://eastus0-3.pushfp.svc.ms/fluid 
 132ea5e1-5638-45da-8e21-4fecbd989d45 
 2025-11-26T05:48:21.3503038Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"8b395908-8ebe-4fea-bafa-0cb910cc2063","SequenceId":1706,"FluidContainerCustomId":"3ac74fbf-2ae8-4d2c-8dcf-08a381be5816","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 CREACIÓN DE ENCABEZADOS DE ANUNCIO DE DONACIÓN