# clasificación-de-productos_1.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Funcionalidad para creacin del mapeo de las categoras xito, a las categoras baco. 
 Debe existir una funcionalidad asociada al BO de baco en donantes ( https://donantes.eatcloud.info/bo/abaco/ ) que inicialmente permita asociar las diversas tipologas de productos susceptibles a ser donados del xito (eatc_odds_typolgy_a, eatc_odds_typolgy_b, eatc_odds_typolgy_c) a las tipologas baco (eatc_odds_typologies). Luego se debe pensar la funcionalidad para dada una cuenta cualquiera, se pueda mapear las diversas tipologas de esa cuenta (eatc_odds_typolgy_a, eatc_odds_typolgy_b, eatc_odds_typolgy_c) a las categoras baco (eatc_odds_typologies).  

 Dado que se est pensando en una funcionalidad estndar, siempre se hablar dentro de los esquemas de persistencia de la plataforma, de eatc_odds_typolgy_a, eatc_odds_typolgy_b, eatc_odds_typolgy_c, pero se cuenta con una herramienta para nombrar cada tipologa  (typology) como la nombra cada cuenta (equivalent): 

 Nombramiento de tipologas de producto para Almacenes xito :  https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=exito&object=eatc_odds   

 Nombramiento de tipologas de producto para baco : https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=abaco&object=eatc_odds   

 La funcionalidad de Mapeo debe permitir en primera instancia asociar la eatc_odds_typolgy_a (sublneas) del xito a un registro de tipologa de baco . Si se puede hacer esta asociacin se debe guardar un registro  as (en la estructura map_odds_exito  que debe guardarse en la cuenta del xito): 

 _id: identificador del registro (lo genera la plataforma) 
 origin_odds_typology_a: tipologa a del xito (Sublnea) que se asocia 
 origin_odds_typology_b: (vaco) 
 origin_odds_typology_c: (vaco) 
 typology_name: Nombre de la "tipologa a" (sublnea) seleccionada 
 eatc_odds_typology_a: Tipologa A (categora) de baco. 
 eatc_odds_typology_b: Tipologa B (subcategora) de baco. 
 eatc_odds_typology_c: Tipologa C (alimentos_y_otros) de baco. 

 Ejemplo: 
 En el selector se seleccion la sublnea del xito " TEXTIL FIDELIZACION " (cdigo 811 ) y se la asoci al siguiente registro de tipologas de baco ( https://donantes.eatcloud.info/api/abaco/eatc_odds_typologies?_id=315 ): 

 _id : "315", 
 codigo : "315", 
 eatc_odds_typolgy_a : "Otros No Alimentos", 
 eatc_odds_typolgy_b : "Textiles", 
 eatc_odds_typolgy_c : "Textiles" 

 Por lo tanto el registro de mapeo debe quedar de la siguiente manera: 

 _id: ####### 
 origin_odds_typology_a: 811 
 origin_odds_typology_b: (vaco) 
 origin_odds_typology_c: (vaco) 
 typology_name: TEXTIL FIDELIZACION 
 eatc_odds_typology_a : "Otros No Alimentos", 
 eatc_odds_typology_b : "Textiles", 
 eatc_odds_typology_c : "Textiles" 

 Para efectos de pruebas se realiz el montaje de la respectiva estructura en el ambiente de pruebas del xito y se puede consultar aqu el registro https://donantes.eatcloud.info/api/devexito/map_odds?origin_odds_typology_a=811   

 Si la tipologa anterior ( eatc_odds_typolgy_a : sublneas xito) no puede asociarse a una  tipologa de baco , el usuario podr profundizar en dicha tipologa a del xito (sublineas) para consultar sus tipologas b asociadas (categoras)  para seleccionar una o varias que si se puedan asociar a una  tipologa de baco . Al hacerlo se debe debe guardar un registro  as: 

 _id: identificador del registro (lo genera la plataforma) 
 origin_odds_typology_a: (vaco) 
 origin_odds_typology_b: tipologa a del xito (categora) que se asocia 
 origin_odds_typology_c: (vaco) 
 typology_name: nombre de la "tipologa b" (categora) xito seleccionada 
 eatc_odds_typology_a: Tipologa A (categora) de baco. 
 eatc_odds_typology_b: Tipologa B (subcategora) de baco. 
 eatc_odds_typology_c: Tipologa C (alimentos_y_otros) de baco. 

 Ejemplo: 
 En el selector se seleccion la categora del xito " HELADOS " (cdigo 00420 ) y se la asoci al siguiente registro de tipologas de baco ( https://donantes.eatcloud.info/api/abaco/eatc_odds_typologies?_id=253 ): 

 _id : "253", 
 codigo : "253", 
 eatc_odds_typolgy_a : "Azcares", 
 eatc_odds_typolgy_b : "Dulces y postres", 
 eatc_odds_typolgy_c : "Helados" 

 Por lo tanto el registro de mapeo debe quedar de la siguiente manera: 

 _id: ####### 
 origin_odds_typology_a: (vaco) 
 origin_odds_typology_b: 00420 
 origin_odds_typology_c: (vaco) 
 typology_name: HELADOS 
 eatc_odds_typology_a : "Azcares", 
 eatc_odds_typology_b : "Dulces y postres", 
 eatc_odds_typology_c : "Helados" 

 Para efectos de pruebas se realiz el montaje de la respectiva estructura en el ambiente de pruebas del xito y se puede consultar aqu el registro https://donantes.eatcloud.info/api/devexito/map_odds?origin_odds_typology_b= 00420   

 Si la tipologa anterior ( eatc_odds_typolgy_b : categoras xito) no puede asociarse a una  tipologa de baco , el usuario podr profundizar un nivel ms para consultar sus tipologas c asociadas (subcategoras)  para seleccionar una o varias que si se puedan asociar a una  tipologa de baco . Al hacerlo se debe debe guardar un registro  as: 

 _id: identificador del registro (lo genera la plataforma) 
 origin_odds_typolgy_a: (vaco) 
 origin_odds_typolgy_b: (vaco) 
 origin_odds_typolgy_c: tipologa a del xito (subcategora) que se asocia 
 typolgy_name: nombre de la "tipologa c" (subcategora) xito seleccionada 
 eatc_odds_typology_a: Tipologa A (categora) de baco. 
 eatc_odds_typology_b: Tipologa B (subcategora) de baco. 
 eatc_odds_typology_c: Tipologa C (alimentos_y_otros) de baco. 

 Ejemplo: 
 En el selector se seleccion la subcategora del xito " MIEL DE ABEJAS " (cdigo 1630 ) y se la asoci al siguiente registro de tipologas de baco ( https://donantes.eatcloud.info/api/abaco/eatc_odds_typologies?_id=232 ): 

 _id : "232", 
 codigo : "232", 
 eatc_odds_typolgy_a : "Azcares", 
 eatc_odds_typolgy_b : "Azcares simples", 
 eatc_odds_typolgy_c : "Miel de abejas" 

 Por lo tanto el registro de mapeo debe quedar de la siguiente manera: 

 _id: ####### 
 origin_odds_typolgy_a: (vaco) 
 origin_odds_typolgy_b: (vaco) 
 origin_odds_typolgy_c: 1630 
 typology_name: MIEL DE ABEJAS 
 eatc_odds_typolgy_a : "Azcares", 
 eatc_odds_typolgy_b : "Azcares simples", 
 eatc_odds_typolgy_c : "Miel de abejas" 

 Para efectos de pruebas se realiz el montaje de la respectiva estructura en el ambiente de pruebas del xito y se puede consultar aqu el registro https://donantes.eatcloud.info/api/devexito/map_odds?origin_odds_typology_c= 1630 

 El object store creado debe servir para, dado un registro de producto "eatc_dona" en el xito, este se pueda categorizar en las categoras baco en el proceso de " Enriquecimiento de la informacin de anuncio de donacin " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CLASIFICACIN DE PRODUCTOS