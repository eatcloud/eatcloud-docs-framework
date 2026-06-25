# nueva-creación-de-anuncios-de-donación-archivo-plano.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 La presente implementación se puede vasar en la implementación de carga de maestros mediante archivos planos que se desarrolló para la App genérica de Fuerza de Ventas Movilizza, en la cual se puede realizar el mapeo de datos a partir de la carga de un archivo plano y también se basa en la implementación de la Nueva Creación de Anuncio de donación (en lo concerniente al listado de productos para confirmar la donación), desarrollada para esta plataforma. Se establece que en esta funcionalidad, dado que está habilitada para operarios, no se efectuará el proceso del mapeo (el cual se realizará en la interfaz administrativa del Nuevo BO&#58; Datagov Cuentas ) y en esta interfaz solamente se realizará la carga del archivo plano como tal. 

 Despliegue de la funcionalidad 
 Esta funcionalidad solamente se le desplegará a las cuentas cuyo &quot; eatc_cua. type &quot; sea &quot; esencial &quot;, &quot; activo &quot; o &quot; impacto &quot; (en principio incorporar a esta regla las &quot; hero &quot; y &quot; hero_business &quot; aunque estos dos últimos tipos de licencias se deprecarán prontamente) 

 Crear anuncio de donación mediante archivo plano 
 Label del título 
 class=&quot; lbl_crear_anuncio_archivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_crear_anuncio_archivo )&#160; 
&#160; 
 Descripción 
 class=&quot; lbl_crear_anuncio_archivo_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_crear_anuncio_archivo_desc ) 
&#160; 
 Con esta funcionalidad podrás cargar anuncios de donación utilizando un archivo plano, cuya estructura ha sido previamente configurada en la plataforma y será estándar para toda tu organización. 

 VALIDACIÓN PREVIA AL DESPLIEGUE DEL FORMULARIO DE SUBIDA DE ARCHIVO 
 El sistema validará (a manera de error handler, porque el respectivo botón de acceso a la funcionalidad en el menú lateral , en teoría previene el entrar a la funcionalidad sin un mapa realizado) si existe un mapa válido para la cuenta en cuestión, realizando la siguiente consulta&#58; 

&#160; 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_objectstore =eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent 

&#160; 
 Si la consulta no trae resultados o trae resultados vacíos 
 El sistema no permitirá desplegar el formulario de carga del archivo plano y desplegará el siguiente label 
 class=&quot; lbl_sin_mapeo_datos &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_sin_mapeo_datos )&#160; 
&#160; 
 &quot; Actualmente no se cuenta con un mapa creado para realizar la carga del anuncio a partir de archivo plano.&#160; Por favor ponte en contacto con el administrador del sistema EatCloud en tu organización, para que realice la configuración correspondiente &quot;. 

&#160; 
 Ejemplo 1&#58; consulta sin resultados&#58; cuenta &quot;alqueria&quot; ambiente de pruebas. 
 Dado los anteriores datos, el sistema debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= alqueria &amp;eatc_platform= wapp &amp;eatc_objectstore =eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent &#160;&#160;&#160; 
&#160; 
 Como el sistema trae una respuesta de este tipo&#58; 
 &#123; 
 &#160;&#160;&#160;&#160;&quot;ts&quot;&#58; &quot;210802155321&quot;, 
 &#160;&#160;&#160;&#160;&quot;op&quot;&#58; true, 
 &#160;&#160;&#160;&#160;&quot;cont&quot;&#58; 0, 
 &#160;&#160;&#160;&#160;&quot;err_msg&quot;&#58; &quot;No se produjeron resultados&quot;, 
 &#160;&#160;&#160;&#160;&quot;err_num&quot;&#58; &quot;&quot;, 
 &#160;&#160;&#160;&#160;&quot;mem&quot;&#58; 0.419999999999999984456877655247808434069156646728515625, 
 &#160;&#160;&#160;&#160;&quot;time&quot;&#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 Entonces el sistema despliega el label class=&quot; lbl_sin_mapeo_datos &quot; y no despliega el formulario de subida de datos 

&#160; 
 Ejemplo 2&#58; consulta con resultados vacíos&#58; cuenta &quot;ara&quot; ambiente de pruebas (antes de implementar mapeo) 
 Dado los anteriores datos, el sistema debe realizar la siguiente consulta&#58; 
&#160; 
 https&#58;//dev.datagov.eatcloud.info/api/eatcloud/ eatc_data_map ?eatc_cua= ara &amp;eatc_platform= wapp &amp;eatc_objectstore =eatc_dona &amp;eatc_madatory_map= y &amp;_distinct= eatc_equivalent &#160;&#160;&#160;&#160; 
&#160; 
 Como el sistema trae una respuesta de este tipo&#58; 
&#160; 
 &#160;&#160;&quot;ts&quot;&#58; &quot;210802155554&quot;, 
 &#160;&#160;&quot;op&quot;&#58; true, 
 &#160;&#160;&quot;cont&quot;&#58; 1, 
 &#160;&#160;&quot;res&quot;&#58; [ 
 &#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&quot;eatc_equivalent&quot;&#58; &quot;&quot; 
 &#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;], 
 &#160;&#160;&quot;mem&quot;&#58; 0.419999999999999984456877655247808434069156646728515625, 
 &#160;&#160;&quot;time&quot;&#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 Entonces el sistema despliega el label class=&quot; lbl_sin_mapeo_datos &quot; y no despliega el formulario de subida de datos 

&#160; 
 Si la consulta trae resultados (es decir hay un mapa configurado) 
 Entonces se despliega un formulario para subir archivos de con las siguientes características&#58; 

 PASO 1&#58; SUBIR EL ARCHIVO CON LA INFORMACIÓN DE LA DONACIÓN 

&#160; 
 Título&#58; Agrega productos mediante archivo plano 
 class=&quot; lbl_agrega_productos_con_archivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_agrega_productos_con_archivo )&#160; 

&#160; 
 Descripción 
 class=&quot; lbl_agrega_productos_con_archivo_desc &quot; (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_agrega_productos_con_archivo_desc ) 
&#160; 
 &quot; Sube un archivo en formato .CSV (separado por puntos y comas, pipes o tabs) o .XLXS, de no más de 3 MB, que contenga en la primera fila el nombre de las columnas (tal como se definió en el mapeo de datos respectivo realizado por el administrador del sistema) y que contenga datos fidedignos y completos de la donación que vas a realizar. Si no conoces el mapeo realizado y deseas construir el archivo, descarga la muestra del archivo a cargar utilizando el botón &quot;Descarga muestra del archivo&quot;, llénalo y súbelo &quot; 

&#160; 
 Botón&#58; &quot;Descarga muestra del archivo&quot; 
 class=&quot; lbl_descarga_muestra_archivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_descarga_muestra_archivo )&#160; 
&#160; 
 Este botón crea un archivo plano a partir de la información que se encuentra en el mapa con la siguiente información en la primera fila (solo se pondrá en la primera fila información que tenga un equivalente) 
 &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_madatory_map= y,n &amp;_distinct= eatc_equivalent 

&#160; 
 Campo de captura para subida de un archivo 
 Título&#58; Subir archivo class=&quot; lbl_subir_archivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_subir_archivo )&#160; 
&#160; 
 &quot;File Picker&quot;&#58; le permitirá al usuario seleccionar un archivo de su PC para subirlo 
&#160; 
 Botón &quot;File Picker&quot; &#58; Seleccionar archivo class=&quot; lbl_seleccionar_archivo &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_seleccionar_archivo )&#160; 
&#160; 
 &quot;Botón Cargar&quot;&#58; Disparará las validaciones necesarias para la carga del archivo y si las mismas pasan, realizará la carga de los datos y el enriquecimiento de los mismos 
&#160; 
 Botón&#58; Cargar donación class=&quot; lbl_cargar_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_cargar_donacion )&#160; 

&#160; 
 Validaciones para la subida del archivo 
 El sistema realizará las siguientes validaciones para garantizar el correcto funcionamiento del sistema&#58; 
&#160; 
 Validación del tamaño del archivo. 
 El sistema validará que el archivo no pese más de 3 MB .&#160; Si el mismo sobrepasa dicho peso, entonces el sistema desplegará el siguiente label&#58; 
 class=&quot; lbl_archivo_pesado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_archivo_pesado ) 
&#160; 
 &quot; El archivo seleccionado pesa más de 3 MB , por lo tanto no es posible subirlo.&#160; Por favor revísalo e intenta de nuevo &quot; 

&#160; 
 Validación del formato del archivo. 
 El sistema validará que el archivo sea un .CSV separado por punto y coma, pipes o tabs o un Excel.&#160; Si el archivo no posee los formatos permitidos entonces se desplegará un label con la siguiente información&#58; 
 class=&quot; lbl_archivo_formato_incorrecto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_archivo_formato_incorrecto )&#160; 
&#160; 
 &quot; El archivo seleccionado no tiene el formato permitido (.CSV separado por puntos y comas, pipes o tabs, o .XLXS).&#160; Por favor revísalo e intenta de nuevo. &quot; 

&#160; 
 Validación de la estructura de los datos establecida. 
 El sistema validará que en la primera columna el archivo contenga la misma información que se establece en el respectivo mapa ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_objectstore =eatc_dona &amp;eatc_madatory_map= y,n &amp;_distinct= eatc_equivalent ). &#160; Si existe alguna diferencia, o la primera fila no corresponde a la declaración de campos que establece el mapa, entonces el sistema desplegará el siguiente label&#58; 
 class=&quot; lbl_archivo_estructura_datos_incorrecta &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_archivo_estructura_datos_incorrecta )&#160; 
&#160; 
 &quot; El archivo seleccionado no tiene la estructura de datos definida en el mapa de datos configurado. Por favor consulta la estructura definida oprimiendo el botón&#58; &quot;Descarga muestra del archivo&quot; e inténtalo de nuevo&quot;. 

&#160; 
 Enriquecimiento de datos para confirmación de la información subida 
 Nota&#58; posteriormente se desarrolló una documentación más simplificada que la que sigue a continuación y te expresa lo mismo con otras palabras.&#160; La misma puede consultarse aquí 
&#160; 
 Si el archivo pasa las anteriores validaciones, entonces el sistema tomará los datos contenidos en él y realizará las transformaciones respectivas y los cálculos necesarios para completar la información requerida.&#160; Dichas transformaciones se realizan aplicando las validaciones, fórmulas o datos que define el archivo de mapa específico para la información que es requerida ( &#123;&#123;URL_entorno_datagov&#125;&#125;/api/eatcloud/eatc_data_map?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_objectstore= eatc_dona &amp;eatc_requiered= y ) utilizando la información contenida en los campos&#58; 
eatc_data_map. eatc_parameter &#58;&#160; es el campo cómo quedará en la estructura de datos &quot; eatc_dona &quot; de EatCloud (y que servirá posteriormente para la creación del encabezado del anuncio de donación mediante el proceso estándar de procesamiento de detalles. 

&#160; 
eatc_data_map. eatc_equivalent&#58; es la declaración del campo, como proviene de la fuente de datos (archivo cargado) y por lo tanto la información contenida en ese campo se transformará en cuanto a su declaración, en la estructura estándar definida en el mapa&#160; ( eatc_data_map. eatc_parameter ). 

&#160; 
eatc_data_map. eatc_constant_validation &#58; con la información contenida en este campo se realiza una validación para establecer el valor del respectivo registro ( eatc_data_map. eatc_parameter ) y que será una constante para el punto de donación particular y el anuncio en particular (desde el cual se está cargando la donación mediante archivo plano). 

&#160; 
eatc_data_map. eatc_constant_formula &#58; con la información contenida en este campo se ejecuta una fórmula para establecer el valor del respectivo registro ( eatc_data_map. eatc_parameter ) y que será una constante para el punto de donación particular y el anuncio en particular (desde el cual se está cargando la donación mediante archivo plano). En otras palabras, todos los registros que se suban mediante el mismo archivo tendrán en el correspondiente registro ( eatc_data_map. eatc_parameter ) el mismo valor que se calcula para el punto de donación y la donación en particular. 
 NOTA PARA EL PROGRAMADOR&#58; se deberá evaluar si las notaciones utilizadas para las fórmulas requeridas para generar las constantes (eatc_data_map. eatc_constant_formula ), son las más adecuadas para generarlas de manera automática (leyendo de la persistencia). De no serlo se sugiere cambiar los datos almacenados en la respectiva persistencia (eatc_data_map. eatc_constant_formula ) para tener una notación más adecuada para esta automatización. 

&#160; 
eatc_data_map. eatc_constant_value&#58; con la información contenida en este campo se obtiene el valor del respectivo registro ( eatc_data_map. eatc_parameter ) y que será una constante para el punto de donación particular y el anuncio en particular (desde el cual se está cargando la donación mediante archivo plano). En otras palabras, todos los registros que se suban mediante el mismo archivo tendrán en el correspondiente registro ( eatc_data_map. eatc_parameter ) el mismo valor para el punto de donación y la donación en particular. 

&#160; 
eatc_data_map. eatc_variable_validation &#58; con la información contenida en este campo se realiza una validación para establecer el valor del respectivo registro ( eatc_data_map. eatc_parameter ) y que será variable para cada registro en particular, por ejemplo según otros datos contenidos en otros parámetros (como por ejemplo la cantidad, el peso, el costo, etc...). 

&#160; 
eatc_data_map. eatc_variable_formula&#58; con la información contenida en este campo se ejecuta una fórmula para establecer el valor del respectivo registro ( eatc_data_map. eatc_parameter ) y que será variable, para cada registro en particular, por ejemplo según otros datos contenidos en otros parámetros (como por ejemplo la cantidad, el peso, el costo, etc...). 
 NOTA PARA EL PROGRAMADOR&#58; se deberá evaluar si las notaciones utilizadas para las fórmulas requeridas para generar las variables (eatc_data_map. eatc_ variable _formula ), son las más adecuadas para generarlas de manera automática (leyendo de la persistencia). De no serlo se sugiere cambiar los datos almacenados en la respectiva persistencia (eatc_data_map. eatc_ variable _formula ) para tener una notación más adecuada para esta automatización. 

&#160; 
 Una vez se carga la donación y se realizan todos los cálculos para completarla e enriquecerla, se procede a mostrar la misma en una tabla editable, para que el usuario proceda a confirmarla, como se establece a continuación. 

 PASO 2&#58; Confirma la donación 
 Título &#58; class=&quot; lbl_confirma_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirma_donacion )&#160;&#160; 
 Descripción &#58; class=&quot; lbl_confirma_upl_donacion_desc &quot; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirma_donacion_desc )&#160; 
&#160; 
 Revisa los datos cargados y completa aquellos que sean requeridos para realizar el anuncio de donación 
&#160; 
 Se presentará la información cargada en una tabla de las siguientes características y que mostrará la siguiente información (la tabla difiere un poco de la que se muestra en el siguiente gráfico, dado que no incorpora alguna información que es necesaria, la cual es necesaria) y que permitirá editar información agregada desde el archivo, la cual pudo estar incompleta o que no se pudo calcular, por ejemplo por la ausencia de un dato en el maestro de artículos ( eatc_odds ) 

 ***NUEVO&#58; No se deberán permitir cargar productos cuyas cantidades están por fuera del peso máximo permitido *** 
Al cargar productos por archivo plano, el sistema deberá realizar la misma validación de productos con peso máximo permitido (peso bloqueante), que se realiza en l a funcionalidad de creación manual de anuncios de donación . 
&#160; 
 Código del producto (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_codigo_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_codigo_producto )&#160; 
 Toma la información de &#58; eatc_dona. eatc-odd_id 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar.&#160; En un inicio, si no hay código del producto no se debe recibir el registro. Se debe avisar al usuario el número de registros del archivo que no se reciben por esta causa y darle la oportunidad de cargar de nuevo el archivo. 
&#160; 
 Producto (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_producto &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_producto )&#160; 
 Toma la información de &#58; eatc_dona .eatc-odd_name 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar.&#160; Si no hay nombre del producto (que se puede dar por dos razones&#58; 1. porque el archivo no tiene dicho nombre en caso de ser mandatorio 2. porque en el maestro de productos eatc_odds no hay registro para el código informado), se debe permitir agregarlo.&#160; Si el caso es que el registro no existe en el maestro de productos, el nuevo nombre del producto se debe llevar a dicho maestro ( eatc_odds ). 

&#160; 
 Cantidad (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_cantidad &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_cantidad )&#160; 
 Toma la información de &#58; eatc_dona .eatc-odd_original_quantity 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar.&#160; En un inicio, si no hay cantidad se debe permitir que el usuario ingrese una cantidad para el registro en cuestión. 

&#160; 
 Peso unitario (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_peso_unitario &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_peso_unitario )&#160;&#160; 
 Toma la información de &#58; eatc_dona .eatc-odd_unit_weight_kg 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar.&#160; Si no hay peso unitario del producto (que se puede dar por dos razones&#58; 1. porque el archivo no tiene dicho peso en caso de ser mandatorio. 2. porque en el maestro de productos eatc_odds no hay registro para el código informado), se debe permitir agregarlo.&#160; Si el caso es que el registro no existe en el maestro de productos, el nuevo peso unitario del producto se debe llevar a dicho maestro ( eatc_odds ). 

&#160; 
 Peso total (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_peso_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_peso_total )&#160; 
 Toma la información de &#58; eatc_dona .eatc-odd_total_weight_kg 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar. Si algunos de los valores base para su cálculo (eatc_dona .eatc-odd_original_quantity y eatc_dona .eatc-odd_unit_weight_kg ) fueron agregados en el proceso de verificación de los datos, se debe recalcular con dichos datos agregados. 

&#160; 
 Costo unitario (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_costo_unitario &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_costo_unitario )&#160; 
 Toma la información de &#58; eatc_dona .eatc-unit_cost 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar.&#160; Si no hay costo unitario del producto (que se puede dar por dos razones&#58; 1. porque el archivo no tiene dicho costo en caso de ser mandatorio. 2. porque en el maestro de productos eatc_odds no hay registro para el código informado), se debe permitir agregarlo.&#160; Si el caso es que el registro no existe en el maestro de productos, el nuevo costo unitario del producto se debe llevar a dicho maestro ( eatc_odds ). 

&#160; 
 Costo total (debe tener un asterisco por ser dato obligatorio) 
 class=&quot; lbl_costo_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_costo_total )&#160; 
 Toma la información de &#58; eatc_dona .eatc-odd_total_weight_kg 
 Validaciones&#58; obligatoriedad, diferente de vacío, cero o null. 
 Observaciones&#58; No se podrá editar. Si algunos de los valores base para su cálculo (eatc_dona .eatc-odd_original_quantity y eatc_dona .eatc-unit_cost ) fueron agregados en el proceso de verificación de los datos, se debe recalcular con dichos datos agregados. 

&#160; 
 Totalizaciones 
 Total 
 class=&quot; lbl_total &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_total )&#160; 
&#160; 
 Se deberán totalizar las columnas de Peso total y Costo total al final de la tabla 

 Botón &quot;Confirmar donación&quot; 
 class=&quot; lbl_confirmar_donacion &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_confirmar_donacion )&#160; 
&#160; 
 Al oprimir el botón, el sistema deberá confirmar que todos los datos requeridos ( &#123;&#123; URL_entorno_datagov &#125;&#125;/api/eatcloud/ eatc_data_map ?eatc_cua=&#123;&#123;_DOM. cua_user &#125;&#125;&amp;eatc_platform= wapp &amp;eatc_objectstore= eatc_dona &amp;eatc_requiered= y ) tengan valores válidos y bien formateados. Una vez se compruebe esto, se deben crear los registros en la respectiva tabla de detalles de donaciones 

&#160; 
 &#123;&#123; URL_entorno_donantes &#125;&#125;/api/&#123;&#123;_DOM. cua_master &#125;&#125;/ eatc_dona 
&#160; 
 Una vez todos los registros hallan sido creados en dicha estructura se invoca el servicio para crear el encabezado de la donación.&#160; Si se obtiene una respuesta satisfactoria de dicho servicio, entonces se debe mostrar una pantalla de confirmación que se describe a continuación. 

 Tu anuncio de donación ha sido creado 

 Tu anuncio de donación ha sido creado 
 class=&quot; lbl_anuncio_creado &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_anuncio_creado )&#160; 
&#160; 
 Muchísimas gracias. En breve encontraremos un beneficiario 
 class=&quot; lbl_anuncio_creado_desc &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_anuncio_creado_desc )&#160; 
&#160; 
 Botón finalizar 
 class=&quot; lbl_finalizar &quot; ( https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=webapp&amp;pais=_*&amp;idlabel= lbl_finalizar )&#160; 
&#160; 
 Este botón retorna al dashboard principal . 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnueva-creaci%C3%B3n-de-anuncios-de-donaci%C3%B3n-archivo-plano%2F4026583159-confirmaciondonacion.png&ow=1146&oh=578, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fnueva-creaci%C3%B3n-de-anuncios-de-donaci%C3%B3n-archivo-plano%2F4026583159-confirmaciondonacion.png&ow=1146&oh=578 

 236.000000000000 

 CREACIÓN DE ANUNCIO DE DONACIÓN MEDIANTE ARCHIVO PLANO