# integración-infraestructura-elástica.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 DOCUMENTACIN DE REFERENCA&#58; 
 Instalacin de AWS PHP SDK manualmente&#58; https&#58;//docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_installation.html (As a ZIP file of the SDK) 
 Crear una clase que importe el SDK y genere los consumos para el CRUD va DynamoDB ( https&#58;//docs.aws.amazon.com/es_es/amazondynamodb/latest/developerguide/GettingStarted.PHP.html ) 

 TABLAS PARA INTEGRACIN INICIAL 
 Se van a empezar el proceso de integracin, con las siguientes tablas&#160; 

&#160; 
 eatc_dona_headers&#58; entorno donantes 
 Estos son los ndices y claves propuestos para esta tabla&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_dona_headers &#160; 
&#160; 
 Esta tabla se encuentra en el entorno &quot;donantes&quot; y tiene las siguientes instancias actualmente&#58; 
&#160; 
 Entorno de pruebas&#58; abaco &#58; devdonantes-abaco-eatc_dona_headers 
 Campos &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?_campos &#160;&#160; 
 Registros &#58; https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_headers?_id=_* &#160; 
&#160; 
 Entorno produccin&#58; abaco &#58; donantes-abaco-eatc_dona_headers 
 Campos &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?_campos &#160; 
 Registros &#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?_id=_* &#160; 

&#160; 
 Entorno de pruebas&#58; argentina &#58; devdonantes-argentina-eatc_dona_headers 
 Campos &#58; https&#58;//devdonantes.eatcloud.info/api/argentina/eatc_dona_headers?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//devdonantes.eatcloud.info/api/argentina/eatc_dona_headers?_id=_* &#160;&#160; 
&#160; 
 Entorno produccin&#58; argentina &#58; donantes-argentina-eatc_dona_headers ( PENDIENTE ) 
 Campos &#58; https&#58;//donantes.eatcloud.info/api/argentina/eatc_dona_headers?_campos &#160;&#160; 
 Registros &#58; https&#58;//donantes.eatcloud.info/api/argentina/eatc_dona_headers?_id=_* &#160;&#160; 

&#160; 
 Entorno de pruebas&#58; mexico &#58; devdonantes-mexico-eatc_dona_headers 
 Campos &#58; https&#58;//devdonantes.eatcloud.info/api/mexico/eatc_dona_headers?_campos &#160;&#160;&#160;&#160; 
 Registros &#58; https&#58;//devdonantes.eatcloud.info/api/argentina/eatc_dona_headers?_id=_* &#160; 
&#160; 
 Entorno produccin&#58; mexico &#58; donantes-mexico-eatc_dona_headers ( PENDIENTE ) 
 Campos &#58; https&#58;//donantes.eatcloud.info/api/mexico/eatc_dona_headers?_campos &#160; 
 Registros &#58; https&#58;//donantes.eatcloud.info/api/mexico/eatc_dona_headers?_id=_* &#160; 

&#160; 
 eatc_match_registry&#58; entorno beneficiarios 
 Estos son los ndices y claves propuestos para esta tabla&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_indexes?eatc_objst=eatc_match_registry &#160; &#160; 
&#160; 
 Esta tabla se encuentra en el entorno &quot;beneficiarios&quot; y tiene las siguientes instancias actualmente 
&#160; 
 Entorno de pruebas&#58; abaco &#58; devbeneficiarios-abaco-eatc_match_registry 
 Campos &#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_match_registry?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_match_registry?_id=_*&#160; 
&#160; 
 Entorno produccin&#58; abaco &#58; beneficiarios-abaco-eatc_match_registry 
 Campos &#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?_id=_*&#160; 

&#160; 
 Entorno de pruebas&#58; argentina &#58; devbeneficiarios-argentina-eatc_match_registry 
 Campos &#58; https&#58;//devbeneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//devbeneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_id=_*&#160; 
&#160; 
 Entorno produccin&#58; argentina &#58; beneficiarios-argentina-eatc_match_registry ( PENDIENTE ) 
 Campos &#58; https&#58;//beneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//beneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_id=_*&#160; 

&#160; 
 Entorno de pruebas&#58; mexico &#58; devbeneficiarios-mexico-eatc_match_registry 
 Campos &#58; https&#58;//devbeneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_campos &#160;&#160;&#160; 
 Registros &#58; https&#58;//devbeneficiarios.eatcloud.info/api/argentina/eatc_match_registry?_id=_*&#160; 
&#160; 
 Entorno produccin&#58; mexico &#58; beneficiarios-mexico-eatc_match_registry ( PENDIENTE ) 
 Campos &#58; https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_match_registry?_campos &#160;&#160;&#160;&#160; 
 Registros &#58; https&#58;//beneficiarios.eatcloud.info/api/ mexico /eatc_match_registry?_id=_* 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 INTEGRACIN INFRAESTRUCTURA ELSTICA