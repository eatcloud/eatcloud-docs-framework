# mejoras-api-púbica-creación-de-donaciones.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CREACIN DE DONACIONES 
&#160; 
 eatc_dona_distributor (parmetro opcional) 
 Incorporar el parmetro&#58; eatc_dona_distributor en el API pblica de creacin de donaciones, con este dato el sistema deber realizar la siguiente consulta&#58; 
&#160; 
 &#123;&#123; URL_entorno_datagov &#125;&#125;/crypt/eatcloud/getcrypt?table=eatc_customers_cua&amp;fieldname=eatc_customer_fiscal_id&amp;fieldvalue=&#123;&#123; eatc_dona_distributor &#125;&#125;&amp;fielddecrypt=eatc_cua 
&#160; 
 Para posteriormente llevar el valor obtenido en &quot; eatc_customers_cua. eatc_cua &quot; al campo&#58; eatc_cua_origin de la respectiva donacin ( eatc_dona_headers ) y se deber crear un nuevo campo boleano en eatc_dona_headers (y tablas relacionadas, como eatc_deleted_dona_header ) donde se coloque&#58; eatc_distribution = y 

&#160; 
 eatc_donation_manager_code (parmetro opcional) 
&#160; 
 Incorporar el parmetro&#58; eatc_donation_manager_code en el API pblica de creacin de donaciones.&#160; Cuando este dato llegue se debe operar el proceso &quot; Awardona &quot;, para dejar esa donacin como &quot;asignada&quot; (awarded). El id de usuario utilizado en dicho llamado puede ser pbapi_dona_creation 

&#160; 
 eatc_donor&#58; ajustar el proceso para que pueda recibir un array 
&#160; 
 Dada la circunstancias que las donaciones de &quot;distribucin&quot; o &quot;distribuciones&quot;, pueden contenier artculos de diversos donantes, se deber ajustar el proceso para que en estos casos, en el parmetro &quot;eatc_donor&quot; se pueda recibir un &quot;array&quot; de donantes y no solamente un dato singular como vena ocurriendo hasta el momento.&#125; 

&#160; 
 eatc_closer_expiration_date&#58; validacin condicionada de obligatoriedad 
&#160; 
 Dado que ABACO ha mostrado inters de solicitar a futuro la obligatoriedad del campo de &quot;fecha de vencimiento ms prxima&quot; a travs de la API, se establece que para validar dicha obligatoriedad se utilizar el parmetro &quot;eatc_cua.&quot;, para establecer si el API valida o no la obligatoriedad de la misma, de la siguiente manera&#58; 
&#160; 
 Obligatoriedad del campo 
 El sistema realizar la validacin de obligatoriedad de este dato si al hacer la siguiente consulta obtiene una respuesta vlida&#58; 
 &#123;&#123; URL_datagov &#125;&#125;/api/eatcloud/eatc_cua?name=&#123;&#123; eatc_cua &#125;&#125;&amp; eatc_mandatory_closer_exp_date = y &amp;cmp=name 
&#160; 
 Campo opcional 
 Si la anterior consulta no entrega una respuesta vlida, el campo ser opcional. 

&#160; 
&#160; 
 CONSULTA DE DONACIONES CON GESTIN EXITOSA O NO EXITOSA 
&#160; 
 Traer en la respuesta un array de objetos dentro de cada donacin con informacin de los items de las mismas y sus cantidades 
&#160; 
 Para cada respuesta de la consulta de donaciones, que en la actualidad se ve de esta manera&#58; 

 Agregar un array de objetos con los detalles de cada donaccin, que muestre la siguiente informacin a saber&#58; 

&#160; 
 eatc-odd_id = &#123;&#123;eatc_dona. eatc-odd_id &#125;&#125; 
 eatc-odd_name = &#123;&#123;eatc_dona. eatc-odd_name &#125;&#125; 
 eatc-odd_quantity = &#123;&#123;eatc_dona. eatc-odd_quantity &#125;&#125; 
 eatc-unit_cost = &#123;&#123;eatc_dona. eatc-unit_cost &#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=d1517e4818fa4e10a63687f44ff31ee3&ext=png&ow=644&oh=434, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?guidSite=330c02030617479eb9b509e05648078e&guidWeb=d3e34f5dbad346948e30db61c6c3f0b9&guidFile=d1517e4818fa4e10a63687f44ff31ee3&ext=png&ow=644&oh=434 

 946.000000000000 

 MEJORAS: API PBLICA CREACIN DE DONACIONES