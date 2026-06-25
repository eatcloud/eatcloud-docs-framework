# Error-handler-clasificación--eatc_odds-=--eatc_dona.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Lineamientos principales&#58; 
Este servicio se ajustará a los lineamientos definidos para la clasificación de productos . 
&#160; 
Se debe desarrollar este servicio en modernización (utilizando node.js y sus frameworks o un procedimiento almacenado de BDD), y procurando mucha eficiencia y performance en el desarrollo 

 Objetivo&#58; 
Desarrollar un servicio que corra de manera periódica en horario nocturno y que sirva para llevar las clasificaciones presentes en los maestros de producto (eatc_odds) a saber&#58; 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 

eatc-odd_typology_a 

eatc-odd_typology_b 

eatc-odd_typology_c 
&#160; 
&#160; 
a las clasificaciones presentes en los detalles de donaciones (eatc_dona) de manera respectiva. 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 

eatc-odd_typology_a 

eatc-odd_typology_b 

eatc-odd_typology 
&#160; 
Dada la primera necesidad, simplemente se actualizará uno de los datos, y para la cuenta maestra mexico, pero este desarrollo debe sentar las bases para uno futuro que actualice toda la información. 
&#160; 
 Datos que debe recibir el servicio 
 cua_master 
 cua_user 
 eatc-odd_id 
 eatc-odd_name 
&#160; 
 Consultas para correr el servicio y actualizar los datos&#58; 
Con la información de invocación del servicio, se realizan las siguientes operaciones 
Consulta de información del producto para actualizar en la donación 
El sistema realiza esta consulta&#58; 
 &#123;&#123;url_donantes&#125;&#125; /api/ &#123;&#123;cua_user&#125;&#125; / eatc_odds ?eatc-id= &#123;&#123;eatc-odd_id&#125;&#125; &amp;_cmp= eatc-odd_typology_a,eatc-odd_typology_b 
Si no se reciben datos, o la respuesta es incorrecta, entonces, el servicio para y no sigue adelante con la actualización. Con los datos recibidos en eatc_odds . eatc-odd_typology_a y &#160; eatc_odds . eatc-odd_typology_b el sistema realizará la siguiente actualización de información. 
&#160; 
Actualización de información del producto en los detalles de donación 
Utilizando el servicio updateplus para actualización por consulta de dos parámetros, el sistema realiza la siguiente operación para invocar el respectivo servicio&#58; 
&#160; 
 Endpoint &#58;&#160; &#123;&#123;url_donantes&#125;&#125; /crd/ &#123;&#123; cua_master &#125;&#125; 

 Parámetros en el body&#58; 
 &#160;&#123; 
 &#160;&#160;&#160;&#160;&quot;_tabla&quot;&#58;&quot;eatc_dona&quot;, 
 &#160;&#160;&#160;&#160;&quot;_operacion&quot;&#58;&quot;updateplus&quot;, 
 &#160;&#160;&#160;&#160;&quot;WHERE&quot;&#58;&quot;eatc-odd_id,eatc_donor&quot;, 
 &#160;&#160;&#160;&#160;&quot;_data&quot;&#58;[ 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;odd_typology_a&quot;&#58;&quot; &#123;&#123; eatc_odds. eatc-odd_typology_a &#125;&#125; &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;eatc-odd_id&quot;&#58;&quot;&#123;&#123; eatc-odd_id &#125;&#125;&quot;,&#160;&#160;&#160;&#160;&#160;&#160; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;eatc_donor&quot;&#58;&quot;&#123;&#123; cua_user &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160; &#160; &#160; &#160;&#123; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;odd_typology_b&quot;&#58;&quot; &#123;&#123; eatc_odds. eatc-odd_typology_b &#125;&#125; &quot;, 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;eatc-odd_id&quot;&#58;&quot;&#123;&#123; eatc-odd_id &#125;&#125;&quot;,&#160;&#160;&#160;&#160;&#160;&#160; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&quot;eatc_donor&quot;&#58;&quot;&#123;&#123; cua_user &#125;&#125;&quot; 
 &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#125; 
 &#160;&#160;&#160;&#160;] 
 &#125; 
Una vez se realice la actualización, el servicio deberá contestar con un mensaje de éxito. 
&#160; 
Automatización del servicio&#58; 
Prototipo de datos de entrada&#58;&#160; 
eatc_odds=&gt;eatc_dona&#58; &#160; https&#58;//app.nocodb.com/p/aut_cls_eatc_odds_to_eatc_dona (contraseña&#58; eatc_odds=&gt;eatc_dona ) 
&#160; 
Prototipo de proceso de automatización&#58; 
Full&#58; sin servicio de clasificación por cua_user 
&#160; https&#58;//cloud.activepieces.com/templates/ZHaXX3AApfYjn6j3lFQVI * este prototipo funciona sin el servicio anterior descrito, y sirve para entender (en el loop de productos) cómo debería funcionar el servicio de clasificación. &#160;Es importante prestar cuidado a la mensajería diseñada, dado que la respuesta del actual servicio es deficiente para entender si hubo problemas o no en su corrida. &#160;Se replicó el proceso que debería hacer el servicio buscando dar también una idea de su funcionamiento. 
Error_handler&#58; con servicio de clasificación por cua_user 
 https&#58;//cloud.activepieces.com/templates/NI5V9ClGmRypl3rLAYkDs *Este servicio incluye la ejecución del error handler propuesto por cua_user. La misma sirve para evaluar que las respuesta del servicio error_handler, ante una corrida son imprecisas (dado que por ejemplo el servicio genera un mensaje como este “ body&#58; &quot;Datos Actualizados Tipologia a&quot; ”, y al verificarse la corrida, como lo propone el flujo, se puede observar que no hay ningún ítem clasificado) 
&#160; 
El sistema deberá correr un proceso periódico en horario nocturno, que dado unos datos específicos, establezca los detalles de anuncios de donación que no tienen datos, inicialmente en el parámetro &#123;&#123; eatc-odd_typology_b &#125;&#125; &#160; 
&#160; 
 Datos que debe recibir el servicio (para automatizar)&#58; 
Se propone que el servicio reciba como datos de entrada&#58; 

 cua_master 

 cua_user (no debería necesitarlo&#58; a partir del cua_master se deben consultar los cua_user respectivos) 

 fecha_inicial 

 fecha_final 
&#160; 
 Consultas para correr el servicio de automatización&#58; 
Con los datos entregados al invocar el servicio, se deberá realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123;URL_donantes&#125;&#125; /api/ &#123;&#123;cua_master&#125;&#125; /eatc_dona?eatc_donor= &#123;&#123;cua_user&#125;&#125; &amp;eatc-date_time_2[0]= &#123;&#123;fecha_inicial&#125;&#125; &amp;eatc-date_time_2[1]= &#123;&#123;fecha_final&#125;&#125; &amp;eatc-odd_typology_b=_vacio&amp;_distinct= eatc-odd_id 
&#160; 
El servicio traerá un array de eatc_dona . eatc-odd_id , que debe colocarse en una cola de procesamiento, para con ese dato y los recibidos en 

 cua_master 

 cua_user 
&#160; 
Realizar el llamado del servicio y paulatinamente ir realizando, de manera asincrónica, la actualización de la información (o mirar si se pueden realizar llamados en paralelo del servicio para actualizar varios eatc_dona . eatc-odd_id al tiempo y obtener mejor performance. 
&#160; 
Inicialmente se deberá automatizar el servicio para que corra con la cua_master &#58; mexico y todas sus cuentas usuario (https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?eatc_cua_master=mexico&amp;_cmp=name)&#160; 
&#160; 
 Servicios implementados&#58; 
 Clasificación eatc_odds to eatc_dona 
Servicios para clasificar los registros en las donaciones (eatc_dona) a partir de la información que se encuentra en el maestro de productos (eatc_odds) de cada cuenta. 
﻿ 
 GET&#58; Tipología a =&gt; por cua_user 
 &#123;&#123;URL_donantes&#125;&#125; /error_handlers/ &#123;&#123;cua_master&#125;&#125; / &#123;&#123;cua_user&#125;&#125; /tipologia_a&#160; 
 POST&#58; Tipología a =&gt; por producto 
 &#123;&#123;URL_donantes&#125;&#125; /error_handlers/ &#123;&#123;cua_master&#125;&#125; / &#123;&#123;cua_user&#125;&#125; /tipologia_a&#160;&#160; 
 Body&#58; json 
 &#123;
 &quot;_data&quot;&#58;[
 &#123;

 &quot;eatc-odd_id&quot;&#58;&quot; &#123;&#123;eatc-odd_id&#125;&#125; &quot;, 
 &quot;eatc-odd_name&quot;&#58;&quot; &#123;&#123;eatc-odd_name&#125;&#125; &quot;
 &#125;
 ]
&#125; 
&#160; 
 GET&#58; Tipología b =&gt; por cua_user 
 &#123;&#123;URL_donantes&#125;&#125; /error_handlers/ &#123;&#123;cua_master&#125;&#125; / &#123;&#123;cua_user&#125;&#125; /tipologia_b&#160; 
 POST&#58; Tipología b =&gt; por producto 
 &#123;&#123;URL_donantes&#125;&#125; /error_handlers/ &#123;&#123;cua_master&#125;&#125; / &#123;&#123;cua_user&#125;&#125; /tipologia_b&#160; 
 Body&#58; json 
 &#123;
 &quot;_data&quot;&#58;[
 &#123;

 &quot;eatc-odd_id&quot;&#58;&quot; &#123;&#123;eatc-odd_id&#125;&#125; &quot;, 
 &quot;eatc-odd_name&quot;&#58;&quot; &#123;&#123;eatc-odd_name&#125;&#125; &quot;
 &#125;
 ]
&#125; 
&#160; 

Colección Postman 

106 

&#160; 

1 
 &#123; 

2 
 &quot;info&quot; &#58; &#123; 

3 
 &quot;_postman_id&quot; &#58; &quot;e16dc8f5-2d9f-42c3-aa95-e30b335bac64&quot; , 

4 
 &quot;name&quot; &#58; &quot;Clasificación eatc_odds to eatc_dona&quot; , 

5 
 &quot;description&quot; &#58; &quot;Servicios para clasificar los registros en las donaciones (eatc_dona) a partir de la información que se encuentra en el maestro de productos (eatc_odds) de cada cuenta.&quot; , 

6 
 &quot;schema&quot; &#58; &quot;https&#58;//schema.getpostman.com/json/collection/v2.1.0/collection.json&quot; , 

7 
 &quot;_exporter_id&quot; &#58; &quot;11174160&quot; , 

8 
 &quot;_collection_link&quot; &#58; &quot;https&#58;//crimson-station-695599.postman.co/workspace/8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/collection/11174160-e16dc8f5-2d9f-42c3-aa95-e30b335bac64?action=share&amp;source=collection_link&amp;creator=11174160&quot; 

9 
 &#125;, 

10 
 &quot;item&quot; &#58; %5B; 

11 
 &#123; 

12 
 &quot;name&quot; &#58; &quot;Tipología a =&gt; por cua_user&quot; , 

13 
 &quot;request&quot; &#58; &#123; 

14 
 &quot;method&quot; &#58; &quot;GET&quot; , 

15 
 &quot;header&quot; &#58; %5B;%5D;, 

16 
 &quot;url&quot; &#58; &#123; 

17 
 &quot;raw&quot; &#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_a&quot; , 

18 
 &quot;host&quot; &#58; %5B; 

19 
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot; 

20 
 %5D;, 

21 
 &quot;path&quot; &#58; %5B; 

22 
 &quot;&#123;&#123;cua_master&#125;&#125;&quot; , 

23 
 &quot;&#123;&#123;cua_user&#125;&#125;&quot; , 

24 
 &quot;tipologia_a&quot; 

25 
 %5D; 

26 
 &#125; 

27 
 &#125;, 

28 
 &quot;response&quot; &#58; %5B;%5D; 

29 
 &#125;, 

30 
 &#123; 

31 
 &quot;name&quot; &#58; &quot;Tipología a =&gt; por producto&quot; , 

32 
 &quot;request&quot; &#58; &#123; 

33 
 &quot;method&quot; &#58; &quot;POST&quot; , 

34 
 &quot;header&quot; &#58; %5B;%5D;, 

35 
 &quot;body&quot; &#58; &#123; 

36 
 &quot;mode&quot; &#58; &quot;raw&quot; , 

37 
 &quot;raw&quot; &#58; &quot;&#123;
 &#160; &#160; \&quot;_data\&quot;&#58;%5B;
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#123;
 &#160; &#160; &#160; &#160; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; \&quot;eatc-odd_id\&quot;&#58;\&quot;&#123;&#123;eatc-odd_id&#125;&#125;\&quot;, &#160; &#160; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; \&quot;eatc-odd_name\&quot;&#58;\&quot;&#123;&#123;eatc-odd_name&#125;&#125;\&quot;
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#125;
 &#160; &#160; &#160; &#160; &#160; &#160; %5D;
&#125;&quot; , 

38 
 &quot;options&quot; &#58; &#123; 

39 
 &quot;raw&quot; &#58; &#123; 

40 
 &quot;language&quot; &#58; &quot;json&quot; 

41 
 &#125; 

42 
 &#125; 

43 
 &#125;, 

44 
 &quot;url&quot; &#58; &#123; 

45 
 &quot;raw&quot; &#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_a&quot; , 

46 
 &quot;host&quot; &#58; %5B; 

47 
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot; 

48 
 %5D;, 

49 
 &quot;path&quot; &#58; %5B; 

50 
 &quot;&#123;&#123;cua_master&#125;&#125;&quot; , 

51 
 &quot;&#123;&#123;cua_user&#125;&#125;&quot; , 

52 
 &quot;tipologia_a&quot; 

53 
 %5D; 

54 
 &#125; 

55 
 &#125;, 

56 
 &quot;response&quot; &#58; %5B;%5D; 

57 
 &#125;, 

58 
 &#123; 

59 
 &quot;name&quot; &#58; &quot;Tipología b =&gt; por cua_user&quot; , 

60 
 &quot;request&quot; &#58; &#123; 

61 
 &quot;method&quot; &#58; &quot;GET&quot; , 

62 
 &quot;header&quot; &#58; %5B;%5D;, 

63 
 &quot;url&quot; &#58; &#123; 

64 
 &quot;raw&quot; &#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_b&quot; , 

65 
 &quot;host&quot; &#58; %5B; 

66 
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot; 

67 
 %5D;, 

68 
 &quot;path&quot; &#58; %5B; 

69 
 &quot;&#123;&#123;cua_master&#125;&#125;&quot; , 

70 
 &quot;&#123;&#123;cua_user&#125;&#125;&quot; , 

71 
 &quot;tipologia_b&quot; 

72 
 %5D; 

73 
 &#125; 

74 
 &#125;, 

75 
 &quot;response&quot; &#58; %5B;%5D; 

76 
 &#125;, 

77 
 &#123; 

78 
 &quot;name&quot; &#58; &quot;Tipología b =&gt; por producto&quot; , 

79 
 &quot;request&quot; &#58; &#123; 

80 
 &quot;method&quot; &#58; &quot;POST&quot; , 

81 
 &quot;header&quot; &#58; %5B;%5D;, 

82 
 &quot;body&quot; &#58; &#123; 

83 
 &quot;mode&quot; &#58; &quot;raw&quot; , 

84 
 &quot;raw&quot; &#58; &quot;&#123;
 &#160; &#160; \&quot;_data\&quot;&#58;%5B;
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#123;
 &#160; &#160; &#160; &#160; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; \&quot;eatc-odd_id\&quot;&#58;\&quot;&#123;&#123;eatc-odd_id&#125;&#125;\&quot;, &#160; &#160; 
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; \&quot;eatc-odd_name\&quot;&#58;\&quot;&#123;&#123;eatc-odd_name&#125;&#125;\&quot;
 &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#125;
 &#160; &#160; &#160; &#160; &#160; &#160; %5D;
&#125;&quot; , 

85 
 &quot;options&quot; &#58; &#123; 

86 
 &quot;raw&quot; &#58; &#123; 

87 
 &quot;language&quot; &#58; &quot;json&quot; 

88 
 &#125; 

89 
 &#125; 

90 
 &#125;, 

91 
 &quot;url&quot; &#58; &#123; 

92 
 &quot;raw&quot; &#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_b&quot; , 

93 
 &quot;host&quot; &#58; %5B; 

94 
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot; 

95 
 %5D;, 

96 
 &quot;path&quot; &#58; %5B; 

97 
 &quot;&#123;&#123;cua_master&#125;&#125;&quot; , 

98 
 &quot;&#123;&#123;cua_user&#125;&#125;&quot; , 

99 
 &quot;tipologia_b&quot; 

100 
 %5D; 

101 
 &#125; 

102 
 &#125;, 

103 
 &quot;response&quot; &#58; %5B;%5D; 

104 
 &#125; 

105 
 %5D; 

106 
 &#125; 

&#123;
 &quot;info&quot;&#58; &#123;
 &quot;_postman_id&quot;&#58; &quot;e16dc8f5-2d9f-42c3-aa95-e30b335bac64&quot;,
 &quot;name&quot;&#58; &quot;Clasificación eatc_odds to eatc_dona&quot;,
 &quot;description&quot;&#58; &quot;Servicios para clasificar los registros en las donaciones (eatc_dona) a partir de la información que se encuentra en el maestro de productos (eatc_odds) de cada cuenta.&quot;,
 &quot;schema&quot;&#58; &quot;https&#58;//schema.getpostman.com/json/collection/v2.1.0/collection.json&quot;,
 &quot;_exporter_id&quot;&#58; &quot;11174160&quot;,
 &quot;_collection_link&quot;&#58; &quot;https&#58;//crimson-station-695599.postman.co/workspace/8de4455f-d7f8-4e18-87d8-f58fb4a0d87c/collection/11174160-e16dc8f5-2d9f-42c3-aa95-e30b335bac64?action=share&amp;source=collection_link&amp;creator=11174160&quot;
 &#125;,
 &quot;item&quot;&#58; %5B;
 &#123;
 &quot;name&quot;&#58; &quot;Tipología a =&gt; por cua_user&quot;,
 &quot;request&quot;&#58; &#123;
 &quot;method&quot;&#58; &quot;GET&quot;,
 &quot;header&quot;&#58; %5B;%5D;,
 &quot;url&quot;&#58; &#123;
 &quot;raw&quot;&#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_a&quot;,
 &quot;host&quot;&#58; %5B;
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot;
 %5D;,
 &quot;path&quot;&#58; %5B;
 &quot;&#123;&#123;cua_master&#125;&#125;&quot;,
 &quot;&#123;&#123;cua_user&#125;&#125;&quot;,
 &quot;tipologia_a&quot;
 %5D;
 &#125;
 &#125;,
 &quot;response&quot;&#58; %5B;%5D;
 &#125;,
 &#123;
 &quot;name&quot;&#58; &quot;Tipología a =&gt; por producto&quot;,
 &quot;request&quot;&#58; &#123;
 &quot;method&quot;&#58; &quot;POST&quot;,
 &quot;header&quot;&#58; %5B;%5D;,
 &quot;body&quot;&#58; &#123;
 &quot;mode&quot;&#58; &quot;raw&quot;,
 &quot;raw&quot;&#58; &quot;&#123;
 \&quot;_data\&quot;&#58;%5B;
 &#123;

 \&quot;eatc-odd_id\&quot;&#58;\&quot;&#123;&#123;eatc-odd_id&#125;&#125;\&quot;, 
 \&quot;eatc-odd_name\&quot;&#58;\&quot;&#123;&#123;eatc-odd_name&#125;&#125;\&quot;
 &#125;
 %5D;
&#125;&quot;,
 &quot;options&quot;&#58; &#123;
 &quot;raw&quot;&#58; &#123;
 &quot;language&quot;&#58; &quot;json&quot;
 &#125;
 &#125;
 &#125;,
 &quot;url&quot;&#58; &#123;
 &quot;raw&quot;&#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_a&quot;,
 &quot;host&quot;&#58; %5B;
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot;
 %5D;,
 &quot;path&quot;&#58; %5B;
 &quot;&#123;&#123;cua_master&#125;&#125;&quot;,
 &quot;&#123;&#123;cua_user&#125;&#125;&quot;,
 &quot;tipologia_a&quot;
 %5D;
 &#125;
 &#125;,
 &quot;response&quot;&#58; %5B;%5D;
 &#125;,
 &#123;
 &quot;name&quot;&#58; &quot;Tipología b =&gt; por cua_user&quot;,
 &quot;request&quot;&#58; &#123;
 &quot;method&quot;&#58; &quot;GET&quot;,
 &quot;header&quot;&#58; %5B;%5D;,
 &quot;url&quot;&#58; &#123;
 &quot;raw&quot;&#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_b&quot;,
 &quot;host&quot;&#58; %5B;
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot;
 %5D;,
 &quot;path&quot;&#58; %5B;
 &quot;&#123;&#123;cua_master&#125;&#125;&quot;,
 &quot;&#123;&#123;cua_user&#125;&#125;&quot;,
 &quot;tipologia_b&quot;
 %5D;
 &#125;
 &#125;,
 &quot;response&quot;&#58; %5B;%5D;
 &#125;,
 &#123;
 &quot;name&quot;&#58; &quot;Tipología b =&gt; por producto&quot;,
 &quot;request&quot;&#58; &#123;
 &quot;method&quot;&#58; &quot;POST&quot;,
 &quot;header&quot;&#58; %5B;%5D;,
 &quot;body&quot;&#58; &#123;
 &quot;mode&quot;&#58; &quot;raw&quot;,
 &quot;raw&quot;&#58; &quot;&#123;
 \&quot;_data\&quot;&#58;%5B;
 &#123;

 \&quot;eatc-odd_id\&quot;&#58;\&quot;&#123;&#123;eatc-odd_id&#125;&#125;\&quot;, 
 \&quot;eatc-odd_name\&quot;&#58;\&quot;&#123;&#123;eatc-odd_name&#125;&#125;\&quot;
 &#125;
 %5D;
&#125;&quot;,
 &quot;options&quot;&#58; &#123;
 &quot;raw&quot;&#58; &#123;
 &quot;language&quot;&#58; &quot;json&quot;
 &#125;
 &#125;
 &#125;,
 &quot;url&quot;&#58; &#123;
 &quot;raw&quot;&#58; &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers/&#123;&#123;cua_master&#125;&#125;/&#123;&#123;cua_user&#125;&#125;/tipologia_b&quot;,
 &quot;host&quot;&#58; %5B;
 &quot;&#123;&#123;URL_donantes&#125;&#125;error_handlers&quot;
 %5D;,
 &quot;path&quot;&#58; %5B;
 &quot;&#123;&#123;cua_master&#125;&#125;&quot;,
 &quot;&#123;&#123;cua_user&#125;&#125;&quot;,
 &quot;tipologia_b&quot;
 %5D;
 &#125;
 &#125;,
 &quot;response&quot;&#58; %5B;%5D;
 &#125;
 %5D;
&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"Off"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"}] 
 ffb434a9-0529-4cfe-9ec9-4f8128975512 
 1!1!3 
 https://eastus1-1.pushfp.svc.ms/fluid 
 d5d478b9-f827-4697-a40d-19123b458200 
 2025-03-27T04:30:44.4471496Z 
 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 {"SessionId":"d16cab61-ff49-461d-a06f-5c1e1a71dd16","SequenceId":1559,"FluidContainerCustomId":"240d49d5-abbd-475b-a6c1-e9d99b33d230","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 

 Error handler clasificación: eatc_odds => eatc_dona