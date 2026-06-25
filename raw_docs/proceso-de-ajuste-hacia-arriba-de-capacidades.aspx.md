# proceso-de-ajuste-hacia-arriba-de-capacidades.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El propsito de este proceso es generar un ajuste automtico de las capacidades de los beneficiarios, una vez que se habilite una funcionalidad desde la APP para ajustar las capacidades de las instituciones (hacia abajo) y que las organizaciones lo puedan hacer fcilmente bajo demanda 

 Revisin de capacidades mximas&#58; 
 En la actualidad se tiene la siguiente informacin registrada&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_max_kg_x_doma_typology_b?_id=_ *&#160; 
&#160; 
 &#123; 
 _id &#58; &quot;1&quot;, 
 eatc_doma_typology_b &#58; &quot;1&quot;, 
 limite_superior_kg &#58; &quot;1000000&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;2&quot;, 
 eatc_doma_typology_b &#58; &quot;2&quot;, 
 limite_superior_kg &#58; &quot;500&quot; 
 &#125;, 
 &#123; 
 _id &#58; &quot;3&quot;, 
 eatc_doma_typology_b &#58; &quot;3&quot;, 
 limite_superior_kg &#58; &quot;100&quot; 
 &#125; 
&#160; 
 Se debe revisar si estos datos se pueden ajustar para colocar mayores capacidades 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_max_kg_x_doma_typology_b&amp;_operacion=update&amp; limite_superior_kg= 1000&amp;WHERE eatc_doma_typology_b= 2 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_max_kg_x_doma_typology_b&amp;_operacion=update&amp; limite_superior_kg= 200&amp;WHERE eatc_doma_typology_b= 3 
&#160; 
 Se incorporaron los registros para tipologas 4 y 5 ( https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_doma_typology_b?_id=_* )&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_max_kg_x_doma_typology_b?_id=_* 
&#160; 
 Si se ajustan capacidades a la alza esta sera la actualizacin&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_max_kg_x_doma_typology_b&amp;_operacion=update&amp; limite_superior_kg= 200&amp;WHERE eatc_doma_typology_b=4&#160; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_max_kg_x_doma_typology_b&amp;_operacion=update&amp; limite_superior_kg= 1000&amp;WHERE eatc_doma_typology_b=5 

 Ajuste de capacidades mximas&#58; 
 Una vez revisadas las capacidades (y si se aceptan los cambios), se debe proceder a realizar los siguientes llamados 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; capacidad_recogida= 1000000&amp; capacidad_gestion= 1000000&amp;WHERE eatc_doma_typology_b= 1 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; capacidad_recogida= 1000&amp; capacidad_gestion= 1000&amp;WHERE eatc_doma_typology_b= 2 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; capacidad_recogida= 200&amp; capacidad_gestion= 200&amp;WHERE eatc_doma_typology_b=3 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; capacidad_recogida= 200&amp; capacidad_gestion= 200&amp;WHERE eatc_doma_typology_b=4 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; capacidad_recogida= 1000&amp; capacidad_gestion= 1000&amp;WHERE eatc_doma_typology_b= 5 

 Mensaje en la App para el Opt-out de capacidades&#58; 
 Cuando se haga el ajuste, se colocar el siguiente anuncio en la APP 
 Nueva funcionalidad de ajuste de capacidades 
&#160; 
 A partir de la fecha, desde el men superior derecho de la App (tres puntos en la parte superior izquierda de la pantalla), podrn ingresar a la funcionalidad de ajuste de capacidades.&#160; Como desde la fecha lo podrn hacer a su antojo y necesidad (permitiendo visualizar anuncios que se ajusten a esta capacidad), hemos configurado dichos datos a la mxima capacidad permitida, y as pretendemos entregar a todos mayores posibilidades de visualizacin de donaciones 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESO DE AJUSTE HACIA ARRIBA DE CAPACIDADES