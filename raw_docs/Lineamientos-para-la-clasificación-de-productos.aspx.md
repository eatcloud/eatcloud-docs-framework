# Lineamientos-para-la-clasificación-de-productos.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

Lineamientos principales&#58; 
A continuación se expresan lineamientos principales para poder estructurar procesos de clasificación de alimentos de manera homogénea a lo largo de la plataforma 

 Implicaciones principales&#58; 
Se anotan una serie de implicaciones en diversos aspectos de la plataforma, que deberán ser revisadas, siempre bajo la óptica de aplicarlas tanto en modernización como en legacy, mientras sea necesario&#58; 
&#160; 
Implicación para las estructuras de datos&#58; 
 Se debe revisar que en todas las estructuras eatc_dona (diferentes cuentas maestras) y eatc_odds (diferentes cuentas usuario), existan los campos&#58; 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 

eatc-odd_typology_a 

eatc-odd_typology_b´ 

eatc-odd_typology_b_code 

eatc-odd_typology_c 

eatc-odd_typology_c_code 
&#160; 
Se debe revisar para que en los maestros de artículos actuales, las clasificaciones entregadas por el donante para sus productos, se guarden en&#58; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 
&#160; 
Y las clasificaciones que realiza eatcloud en sus procesos de enriquecimiento de datos se guarden en&#58; 

eatc-odd_typology_a 

eatc-odd_typology_b 

eatc-odd_typology_b_code 

eatc-odd_typology_c 

eatc-odd_typology_c_code 
&#160; 
Implicación para los procesos de creación de maestros de artículos&#58; 
 Se debe revisar que en las funcionalidades que crean maestros de artículos (desde datagov_cuentas y desde la wapp en la creación de anuncios), cuando se captura una, dos o tres tipologías de producto, estas se deben guardar (en los respectivos maestros de artículos eatc_odds ) en&#58; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 
&#160; 
 Implicación para los procesos de creación de anuncios de donaciones&#58; 
 Se debe revisar que cuando se crean donaciones (de manera manual, mediante archivo plano, interfaz o API), siempre se lleve la información registrada en los maestros de artículos (eatc_odds) en 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 

eatc-odd_typology_a 

eatc-odd_typology_b 

eatc-odd_typology_b_code 

eatc-odd_typology_c 

eatc-odd_typology_c_code 
&#160; 
A la información del detalle de la donación (eatc_dona) de manera respectiva a&#58; 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 

eatc-odd_typology_a 

eatc-odd_typology_b 

eatc-odd_typology_b_code 

eatc-odd_typology_c 

eatc-odd_typology_c_code 
&#160; 
 Implicación para los procesos de información sobre donaciones (en especial downlodaddona)&#58; 
 Se debe revisar en el mapeo de los datos que se realiza para la descarga de donaciones, que la categoría solicitada por BAMX, se obtenga desde 
&#160; 
 eatc-odd_typology_b&#160; 
&#160; 
 Implicación para los procesos de clasificación de productos&#58; 
 De ahora en adelante los procesos de clasificación internos de EatCloud, deberán apuntar los datos obtenidos a partir de la información que se tiene en&#58; 
&#160; 
&#160; 
O en el nombre del producto&#58; 
&#160; 

origin_odds_typology_a 

origin_odds_typology_b 

origin_odds_typology_c 
&#160; 
De la siguiente manera&#58; 
&#160; 
Clasificación alimentos / no alimentos 
eatc-odd_typology_a 
&#160; 
Clasificación en categorías de líderes de ecosistema (ABACO / BAMX) 
eatc-odd_typology_b 
eatc-odd_typology_b_code 
&#160; 
Clasificación para cálculo de aporte nutricional 
eatc-odd_typology_c 
eatc-odd_typology_c_code 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FLineamientos-para-la-clasificaci%C3%B3n-de-productos%2F4098732840-Diapositiva1.PNG&ow=1280&oh=720, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2FLineamientos-para-la-clasificaci%C3%B3n-de-productos%2F4098732840-Diapositiva1.PNG&ow=1280&oh=720 

 974.000000000000 

 Lineamientos para la clasificación de productos