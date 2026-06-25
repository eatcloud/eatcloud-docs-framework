# transformación-de-ofertas-en-anuncios.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema con un proceso que corra peridicamente (puede ser cada 5 o 10 minutos), debe estar evaluando la fecha y hora actual, versus la fecha y hora registrada en eatc_sale. eatc-offer_lifetime_until , si la fecha y hora actual es posterior a la registrada en eatc_sale. eatc-offer_lifetime_until , entonces deber proceder a realizar la transformacin de la oferta en anuncio, realizando algunos registros en la estructura de la oferta ( eatc_sale ) y copiando los datos de la oferta a eatc_dona , para posteriormente correr el servicio para la generacin del encabezado de anuncio de donacin eatc_dona_headers y as disponibilizar el alimento para la App de Beneficiarios. 
&#160; 
 Consulta de las ofertas a ser transformadas 
 El sistema debe consultar aquellas ofertas que son susceptibles de ser transformadas, para de ellas extractar el dato eatc_sale. eatc-offer_lifetime_until y as poder realizar la comparacin con la fecha y hora actual y determinar si se transforman o no (si la fecha y hora de vida ltil de la oferta es anterior al fecha y hora acutal) 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale?eatc-odd_state=sale,partially_ordered&amp;blocked=no&#160; 
&#160; 
 Ejemplo ambiente de pruebas&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale?eatc-odd_state=sale,partially_ordered&amp;blocked=no &#160; 
&#160; 
 Edicin de datos de la oferta al ser transformada 
 Los siguientes datos deben editarse para registrar que la misma fue transformada&#58; 
&#160; 
 &#123;&#123;parmetros_edicion&#125;&#125; 
&#160; 
 eatc_odd_sale_transformed_quantity 
 Se transforman las unidades que estaban disponibles, es decir eatc_odd_sale_transformed_quantity= &#123;&#123;eatc_sale. eatc-odd_quantity &#125;&#125; 
 eatc-odd_quantity 
 Despus de transformar las unidades disponibles, ests no lo sern ms as que&#58; eatc-odd_quantity= 0 
 eatc-odd_state&#58; 
 Si el eatc-odd_state original es igual a &quot; sale &quot;&#160; entonces eatc-odd_state= transformed 
 Si el eatc-odd_state original es igual a &quot; partially_ordered &quot;&#160; entonces eatc-odd_state= partially_transformed 
 eatc-warning= Anuncio transformado el &#123;&#123;current_datetime&#125;&#125; 
 blocked= si 
 eatc-user_blocked= eatcloud 
&#160; 
 Llamado para editar informacin&#58; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/?_tabla=eatc_sale&amp;_operacion=update&amp;&#123;&#123;parametros_edicion&#125;&#125;&amp;WHERE_id=&#123;&#123;eatc_sale._id&#125;&#125; 
&#160; 
 Transformacin de datos de la oferta 
&#160; 
 Establecimiento de cuenta maestra en la cual se escribe el anuncio de donacin 
 Como primera medida el sistema debe establecer, a partir de los datos de la oferta en qu cuenta maestra se registra la donacin de la siguiente manera&#58; 
&#160; 
 Se toma el dato del la oferta eatc_sale. eatc_cua_origin &#160; y con ese dato se realiza la siguiente consulta para traer el dato eatc_cua. eatc_cua_master que corresponder a la cuenta maestra en la cual se deber hacer el registro del anuncio. 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=&#123;&#123;eatc_sale. eatc_cua_origin&#125;&#125; 
&#160; 
 &#123;&#123;parmetros_insercion&#125;&#125; 
 Los parmetros que se insertan se establecen en el respectivo mapeo de datos . 
&#160; 
 Llamado para insertar la informacin 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/&#123;&#123;eatc_cua. eatc_cua_master &#125;&#125;/?_tabla=eatc_dona&amp;_operacion=insert&amp;&#123;&#123;parmetros_insercion&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 TRANSFORMACIN DE OFERTAS EN ANUNCIOS DE DONACIN