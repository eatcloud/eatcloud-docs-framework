# bienvenida-puntos-de-venta-cercanos-alimentatón.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Consulta de puntos de venta cercanos 

 Hay un punto de venta cerca de ti: 
 Se deben consultar los puntos de donacin utilizando el API respectiva:  
 https://donantes.eatcloud.info/api/abaco/eatc_pods?eatc-id=_ * 

 OPCION 1: 
 Teniendo en cuenta los datos eatc-lat y eatc-lon, se debe establecer que puntos de donacin estn en un radio de 9 kilmetros. 

 Eso se puede lograr calculando la distancia entre la ubicacin del dispositivo y cada uno de los puntos.  Solo se deben mostrar y listar los que estn a menos de 9 KM. 

 Ejemplo de funcin en javascript para establecer la distancia entre dos puntos: https://codeday.me/es/qa/20190107/67042.html . 

 OPCIN 2: 
 Tomando la coordenada y utilizando un API de geolocalizacin se establece la ciudad en la que se encuentra el usuario.  Utilizando dicha informacin se realiza una consulta al API respectiva calculando la distancia entre el punto ms lejano que trae el API y el usuario para colocar el dato que se muestra en la leyenda "a Xkm de ti" 

 Ejemplo: 
 Un usuario se determina que se encuentra en Medelln, por lo tanto la consulta al API sera (enviando este dato en el parmetro: eatc-city): 

 https://donantes.eatcloud.info/api/abaco/eatc_pods?eatc-city=medellin 

 Se calcula la distancia a todos los puntos que trae el API y se coloca la mayor en la leyenda "a Xkm de ti" 

 MAPA: 
 El punto rojo que se muestra en el mapa es el que corresponde a las coordenadas del dispositivo.  Los puntos que se encuentran a menos de 9KM se muestran en azul 

 Botn: Estoy listo para ayudar a salvar alimentos 
 Debe llevar a la funcionalidad " Dashboard principal -Eleccin de punto de donacin " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbienvenida-puntos-de-venta-cercanos-alimentat%C3%B3n%2F3271067908-4.3-bienvenida-4--eatc_alim_bienv4-.png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fbienvenida-puntos-de-venta-cercanos-alimentat%C3%B3n%2F3271067908-4.3-bienvenida-4--eatc_alim_bienv4-.png&ow=750&oh=1334 
 App usuario final - Alimentatn 

 746.000000000000 

 BIENVENIDA: PUNTOS DE VENTA (EATC_SALE_BIENV4 (EATC_ALIM_BIENV4))