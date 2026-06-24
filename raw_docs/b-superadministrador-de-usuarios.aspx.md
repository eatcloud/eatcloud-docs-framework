# b-superadministrador-de-usuarios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Ver comunicacin activa: ✓ Ajuste de funcionalidad de creacin de usuarios back office para incorporar criterios de filtro {codigo_tarea} [HHE]  

 Cuando se crea un usuario, cada a cada usuario se le puede asociar una tipologa propia de los puntos de donacin ( https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=exito&object=eatc_pods ) 

 Se deben incorporar los siguientes filtros que deben ser "armados" a partir del maestro de puntos de donacin de la respectiva cuenta (eatc_pods para la cuenta devexito ( https://donantes.eatcloud.info/api/devexito/eatc_pods?_id=_* ): 

 eatc_typology_a = marca ( https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=exito&object=eatc_pods&typology=a ) 

 eatc_typology_b = subzona ( https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=exito&object=eatc_pods&typology=b ) 

 eatc_typology_c = distrito ( https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_typologies&cua=exito&object=eatc_pods&typology=c ) 

 Ideal que siempre se pueda escoger uno o varios y tambin tener la posibilidad de escoger "todos". La "cascada de seleccin" debe operar en el orden arriba descrito, es decir: si selecciona una o varias marcas (eatc_typology_a)  se deben desplegar las subzonas (eatc_typology_b) pertenecientes a dicha o dichas marcas, si se selecciona una o varias subzonas, se deben desplegar los distritos (eatc_typology_c)  correspondentes a dicha o dichas subzonas y posteriormente los almacenes (eatc_pods) correspondidentes a dichos distritos.  El objetivo final del filtro es saber que puntos de donacin puede consultar el usuario en particular (eatc_pods. eatc-id: con estos identificadores de puntos de donacin, el usuario deber filtrar la informacin que se le presenta en el BO y el mismo solo le deber mostrar informacin asociada a los puntos de donacin correspondientes) 

 Tambin la seleccin puede darse seleccionando valores de un solo criterio (ejemplo: solo marca (eatc_typology_a)   y se entiende que de ah en adelante podr ver toda la informacin de las subzonas, distritos y puntos de donacin), de dos (por ejemplo: marca y subzona y se entiende que de ah en adelante podr ver todos los distritos, y los puntos de donacin correspondientes); de tres (por ejemplo: marca, subzona, distrito, y se entiende que de ah en adelante podr ver toda la informacin de los puntos de donacin correspondientes) 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 [PENDIENTE] SUPERADMINISTRADOR DE USUARIOS (BO BENEFICIARIOS)