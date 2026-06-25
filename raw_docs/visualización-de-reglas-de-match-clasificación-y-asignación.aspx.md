# visualización-de-reglas-de-match-clasificación-y-asignación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 E NVIROMENTS 
 Pruebas 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-c18041c8-e224-4485-94e5-5b462b66436f &#160; 
&#160; 
 Produccin 
 https&#58;//crimson-station-695599.postman.co/workspace/My-Workspace~8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/environment/11174160-866b076d-41f4-4102-aade-7f4da0d32617 &#160; 

&#160; 
 C ONSULTA DE REGLAS DE MATCH POR CUENTA MAESTRA cuenta maestra 
 Coleccin Postman&#58; 
 https&#58;//api.postman.com/collections/11174160-31f6adeb-0d3b-4524-8710-1f96e62ad22c?access_key=REDACTED &#160; 
&#160; 
 Sirve para importar la coleccin con la cual se realizan los llamados para esta configuracin 
&#160; 
 Informacin inicial para realizar el procedimiento&#58; 
 Se configura en el respectivo enviroment 
&#160; 
 Cuenta maestra&#58; 
 cua_master &#160; 

&#160; 
 Consulta de los querys de clasificacin aplicables 
 Se realiza el llamado Query de clasificacin&#58; consulta , con los siguientes parmetros&#58;&#160; 

&#160; 
 &#123;&#123;URL_datagov&#125;&#125;api/eatcloud/dona_match_classification_querys?eatc_cua_master=&#123;&#123;cua_master&#125;&#125;&#160; 
&#160; 
 Ejemplo&#58; ambiente de produccin, cua_master&#58; abaco&#58; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/dona_match_classification_querys?eatc_cua_master=abaco &#160; 
&#160; 
 Con la informacin recibida el sistema arma una tabla de la siguiente manera&#58; 

&#160; 
 Reglas de clasificacin 
 label&#58; class=lbl_reglas_clasificacion 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_reglas_clasificacion &#160; 
&#160; 
 Descripcin 
 label&#58; class=lbl_reglas_clasificacion_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_reglas_clasificacion_desc &#160; 
&#160; 
 &quot;En la siguiente tabla se presentan las reglas aplicables para clasificar un anuncio de acuerdo a sus caractersticas.&#160; A partir de estas clasificaciones, se establecen reglas de asignacin particulares.&quot; 
&#160; 
 El sistema construye una tabla con los siguientes valores&#58; 
&#160; 
 Cuenta maestra 
 label&#58; class=lbl_cua_master 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_cua_master &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc_cua_master 

&#160; 
 Clasificacin de la donacin 
 label&#58; class=lbl_dona_typology_a 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_dona_typology_a &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc_dona_typology_a 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_dona_typology_a_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_dona_typology_a_desc &#160; 
&#160; 
 &quot;(Opcional) Clasificacin de la donacin que puede dar como resultado un tratamiento especial de la misma (por ejemplo, en Mxico las donaciones se clasifican como aquellas que tienen fecha corta y las que tienen fecha larga y de acuerdo a esto se clasifican y tienen un manejo en cuanto a asignacin diferente).&quot; 

&#160; 
 Donante 
 label&#58; class=lbl_donor 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_donor &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc-donor 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_donor_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_donor_desc &#160; 
&#160; 
 &quot;La donacin se podr clasificar si pertenece a un donante, a un conjunto de donantes (valores separados por comas) o si no pertenece a un subconjunto de donantes (valores separados por comas, despus del prefijo &quot;_nin_&quot; que indica que no pertenece a dichos donantes)&quot; 

&#160; 
 Ciudad 
 label&#58; class=lbl_city 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_city &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc-city 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_city_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_city_desc &#160; 
&#160; 
 &quot;(Opcional) Las donaciones se podrn clasificar de acuerdo a si fueron realizadas en una ciudad en particular.&quot; 

&#160; 
 Peso 1 en KG 
 label&#58; class=lbl_peso1_kg 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_peso1_kg &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc-original_weight_kg 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_peso1_kg_desc 
&#160; 
 &quot;La donacin se podr clasificar de acuerdo a su peso utilizando esta informacin. Para realizar dicha clasificacin se utilizan operadores lgicos&#58; _&lt;&#58; Menor que. _&lt;_&#58; Menor o igual que. _&gt;&#58; Mayor que. _&gt;_&#58; Mayor o igual que.&quot; 

&#160; 
 Peso 2 en KG 
 label&#58; class=lbl_peso2_kg 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_peso2_kg &#160;&#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc-original_weight_kg_2 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_peso2_kg_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_peso2_kg_desc &#160; 
&#160; 
 &quot;Cuando hay valores en este campo, se entiende que hay un rango de pesos que define la clasificacin de la donacin. El valor inferior y superior del rango estarn separados por un &quot;|&quot; &quot;pipe&quot; y tambin se utilizarn en su descripcin los operadores lgicos&#58; _&lt;&#58; Menor que. _&lt;_&#58; Menor o igual que. _&gt;&#58; Mayor que. _&gt;_&#58; Mayor o igual que.&quot; 

&#160; 
 Clasificacin para el match 
 label&#58; class=lbl_match_result 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_match_result &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 dona_match_classification_querys. eatc_result 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_match_result_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_match_result_desc &#160; 
&#160; 
 &quot;La clasificacin del anuncio para el match, es el resultado que el sistema le asigna si cumple con los parmetros establecidos y que sirve para establecer reglas de asignacin de las donaciones segn sus caractersticas&quot; 

&#160; 
 Reglas de asignacin 
 label&#58; class=lbl_match_asignation_rule 
&#160; 
 En esta columna, para cada regla de clasificacin, el sistema presentar un botn&#160; 
 &quot;Ver reglas de asignacin&quot; (class= lbl_ver_reglas_asignacion ) 
&#160; 
 Y que al accionarlo el sistema realizar la siguiente consulta, con el nimo de desplegar una tabla secundaria, debajo del registro de la regla respectiva, cuyo comportamiento se detalla ms adelante&#58; 
 &#123;&#123;URL_datagov&#125;&#125;api/eatcloud/eatc_match_asignation_rules?eatc_match_asignation_rule= &#123;&#123; dona_match_classification_querys. eatc_result &#125;&#125; 
&#160; 
 Subtabla&#58; Reglas de asignacin del match 
 Debajo del registro de la regla de clasificacin, al accionar el botn &quot;Ver reglas de asignacin&quot;, se desplegar una subtabla (especie de acorden), que contar con la siguiente informacin, tomada de la consulta arriba descrita, que deber presentarse ordenada por el campo eatc_match_asignation_rule. eatc_asignation_order &#58; 
&#160; 
 Orden de asignacin 
 label&#58; class=lbl_orden_asignacion 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_orden_asignacion &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_asignation_order 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_orden_asignacion_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_orden_asignacion_desc &#160; 
&#160; 
 &quot;Es el orden que se aplica para asignar las donaciones de esta clasificacin a los beneficiarios que cumplen caractersticas definidas en de acuerdo a los datos registrados en el sistema&quot; 
&#160; 
 Parmetro a evaluar del beneficiario 
 label&#58; class=lbl_doma_param 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_doma_param 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_doma_param_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_desc &#160; 
&#160; 
 &quot;La caracterstica o dato que se evala de los gestores de donaciones, para establecer si la donacin se le mostrar en el orden establecido. Por ejemplo un parmetro comn a evaluar es la tipologa b de los gestores de donacin, que determina si son bancos de alimentos, organizaciones adscritas a bancos u otras organizaciones&quot; 

&#160; 
 Valor a evaluar del beneficiario 
 label&#58; class=lbl_doma_param_value 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_value &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_doma_param_value 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_doma_param_value_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_value_desc &#160; 
&#160; 
 &quot;Es el valor que debe tener el parmetro a evaluar, para determinar si la donacin se le asigna a una organizacin que cumple con esa caracterstica.&#160; Por ejemplo es comn que se priorice para cierto tipo de donacin, que se muestre primero a aquellos gestores de donaciones cuya tipologa b es igual a &quot;1&quot; (siendo 1 el valor de esta columna), y que corresponden a bancos de alimentos.&quot; 

&#160; 
 Descripcin regla 
 label&#58; class=lbl_param_value_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_param_value_desc &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_param_value_desc 

&#160; 
 Desde cundo se cuenta el tiempo 
 label&#58; class=lbl_timeout_from 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_from &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_timeout_from 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_timeout_from_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_from_desc &#160; 
&#160; 
 &quot;A partir de una fecha y hora marcada para cada donacin es que se establecen tiempos que determinan la prioridad de despliegue de una donacin a un tipo de gestor de donaciones especfico.&#160; Comunmente este tiempo se cuenta a partir de la fecha y hora de publicacin del anuncio o eatc-publication_datetime .&quot; 

&#160; 
 A partir de cuntos minutos se realiza el match 
 label&#58; class=lbl_timeout_in_minutes 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_in_minutes &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_timeout_in_minutes 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_timeout_in_minutes_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_in_minutes_desc &#160; 
&#160; 
 &quot;Esta columna presenta los minutos a partir de los cuales, se muestra una donacin a las organizaciones que cumplen con los criterios de clasificacin definidos en cada registro.&#160; Si por ejemplo el dato es &quot;0&quot;, significa que a partir de la fecha y hora definida en el campo anterior, se le mostrar a los donantes caracterizados, el anuncio (es decir, de inmediato).&quot; 

&#160; 
 Radio para el match 
 label&#58; class=lbl_min_radius 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_min_radius &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_min_radius 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_min_radius_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_min_radius_desc &#160; 
&#160; 
 &quot;El valor de esta columna determina el radio en Kilmetros, contado a partir de la coordenada del punto de donacin, con el cul se establece la cobertura geogrfica de gestores de donaciones a los cuales se les mostrar el anuncio que ha sido clasificado.&quot; 

&#160; 
 Match exclusivo? 
 label&#58; class=lbl_exclusive 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_exclusive &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_exclusive 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_exclusive_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_exclusive_desc &#160; 
&#160; 
 &quot;En esta columna se marca con una &quot;y&quot;, si la regla es exclusiva, es decir, que solamente se le asigna la donacin clasificada a un solo tipo de gestor de donaciones, que cumple con las caractersticas establecidas&quot; 

&#160; 
 Reglas de ampliacin 
 label&#58; class=lbl_match_expansion_rules 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_match_expansion_rules &#160; 
&#160; 
 En esta columna, para cada regla de clasificacin, el sistema presentar un botn&#160; 
 &quot;Ver reglas de ampliacin&quot; (class= lbl_ver_reglas_ampliacion ) 
&#160; 
 Y que al accionarlo el sistema realizar la siguiente consulta, con el nimo de desplegar una tabla secundaria, debajo del registro de la regla respectiva, cuyo comportamiento se detalla ms adelante&#58; 
&#123;&#123;URL_datagov&#125;&#125;api/eatcloud/eatc_match_expansion_rules?eatc_match_expansion_rule= &#123;&#123; dona_match_classification_querys. eatc_result &#125;&#125; 
&#160; 
 Subtabla&#58; Reglas de ampliacin del match 
 Debajo del registro de la regla de clasificacin, al accionar el botn &quot;Ver reglas de ampliacin&quot;, se desplegar una subtabla (especie de acorden), que contar con la siguiente informacin, tomada de la consulta arriba descrita.&#160; Si la consulta arriba descrita no trae datos, el sistema deber presentar la siguiente informacin&#58; 
&#160; 
 class=lbl_no_aplica_ampliacion 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_no_aplica_ampliacion &#160; 
&#160; 
 &quot;Para la presente clasificacin de anuncio no aplica regla de ampliacin&quot; 
&#160; 
 Parmetro a evaluar del beneficiario 
 label&#58; class=lbl_doma_param 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_doma_param 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_doma_param_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_desc &#160; 
&#160; 
 &quot;La caracterstica o dato que se evala de los gestores de donaciones, para establecer si la donacin se le mostrar en el orden establecido. Por ejemplo un parmetro comn a evaluar es la tipologa b de los gestores de donacin, que determina si son bancos de alimentos, organizaciones adscritas a bancos u otras organizaciones&quot; 

&#160; 
 Valor a evaluar del beneficiario 
 label&#58; class=lbl_doma_param_value 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_value &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_doma_param_value 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_doma_param_value_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_doma_param_value_desc &#160; 
&#160; 
 &quot;Es el valor que debe tener el parmetro a evaluar, para determinar si la donacin se le asigna a una organizacin que cumple con esa caracterstica.&#160; Por ejemplo es comn que se priorice para cierto tipo de donacin, que se muestre primero a aquellos gestores de donaciones cuya tipologa b es igual a &quot;1&quot; (siendo 1 el valor de esta columna), y que corresponden a bancos de alimentos.&quot; 

&#160; 
 Descripcin regla 
 label&#58; class=lbl_param_value_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_param_value_desc &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_param_value_desc 

&#160; 
 Desde cundo se cuenta el tiempo 
 label&#58; class=lbl_timeout_from 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_from &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_timeout_from 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_timeout_from_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_from_desc &#160; 
&#160; 
 &quot;A partir de una fecha y hora marcada para cada donacin es que se establecen tiempos que determinan la prioridad de despliegue de una donacin a un tipo de gestor de donaciones especfico.&#160; Comunmente este tiempo se cuenta a partir de la fecha y hora de publicacin del anuncio o eatc-publication_datetime .&quot; 

&#160; 
 A partir de cuntos minutos se realiza la ampliacin 
 label&#58; class=lbl_timeout_in_minutes_amp 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_in_minutes_amp &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_timeout_in_minutes 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_timeout_in_minutes_amp_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_timeout_in_minutes_amp_desc &#160; 
&#160; 
 &quot;Esta columna presenta los minutos a partir de los cuales, se realiza una ampliacin.&#160; Si por ejemplo el dato es &quot;120&quot;, significa que a partir de la fecha y hora definida en el campo anterior, corrern 2 horas antes de realizar una ampliacin del match (esto solo aplica para donaciones que no han sido asignadas).&quot; 

&#160; 
 Lapso de expansin en minutos 
 label&#58; class=lbl_expansion_lapse_in_minutes 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_expansion_lapse_in_minutes &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_ expansion_lapse_in_minutes 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_expansion_lapse_in_minutes_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_expansion_lapse_in_minutes_desc &#160; 
&#160; 
 &quot;A partir de los minutos definidos en el campo anterior, en un lapso definido en el valor de este campo, se realizar una ampliacin del radio en el cual la donacin har match&quot; 

&#160; 
 Radio de expansin 
 label&#58; class=lbl_expansion_radius 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_expansion_radius &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_expansion_radius 
&#160; 
 Tooltip&#58; 
&#160; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_expansion_radius_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_expansion_radius_desc &#160; 
&#160; 
 &quot;Las expansiones, suman un radio igual al establecido en este campo, al radio de influencia de la donacin para determinar a que organizaciones les hace match.&quot; 

&#160; 
 Radio mximo de expansin 
 label&#58; class=lbl_max_expansion_radius 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_max_expansion_radius &#160; 
&#160; 
 Presenta los datos que llegan en el parmetro&#58; 
 eatc_match_asignation_rule. eatc_max_expansion_radius 
&#160; 
 Tooltip&#58; 
 Al lado de la descripcin del campo en la tabla se debe colocar un signo de interrogacin encerrado en un crculo,&#160; al hacer clic en esta &quot;ayuda&quot; o &quot;tooltip&quot; se deber desplegar la siguiente informacin&#58; 
&#160; 
 label&#58; class=lbl_max_expansion_radius_desc 
 datagov.eatcloud.info/api/eatcloud/eatc_config_labels?plataforma=_*&amp;cua=_*&amp;idlabel=lbl_max_expansion_radius_desc &#160; 
&#160; 
 &quot;El dato mostrado en este campo representa el mximo radio que alcanzar la ampliacin, contado desde la coordenada del punto de donacin respectivo.&quot; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 Nuevo BO CUA MASTER Beneficiarios 

 VISUALIZACIN DE REGLAS DE MATCH (CLASIFICACIN Y ASIGNACIN)