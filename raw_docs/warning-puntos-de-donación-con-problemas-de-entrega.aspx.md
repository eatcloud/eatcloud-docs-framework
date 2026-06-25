# warning-puntos-de-donación-con-problemas-de-entrega.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema generar una alerta para avisar sobre los puntos de donacin que estn presentando problemas con la entrega de producto 
&#160; 
 El sistema debe evaluar si durante la ltima semana ha habido para el punto de donacin del anuncio, algn anuncio cuyo eatc-state=not_delivered o que tenga un registro de Issue relacionado con el tema, consulta que se hace de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_checkin_and_deliver_issues?eatc-issue_cause_code= wrongly_delivered,donation_unknow,eatcloud_unkonw,responsible_not_found &amp;eatc-donor_code=&#123;&#123;eatc_dona_headers. eatc-donor &#125;&#125;&amp;eatc-pod_id=&#123;&#123;eatc_dona_headers. eatc-pod_id &#125;&#125; 
&#160; 
 en ese caso deber escribir en el parmetro eatc-warning del eatc_dona un mensaje de advertencia que alerte al eatc-donation_manager para que tenga cuidado y siga ciertas instrucciones para garantizar que se le entregue el anuncio. 
&#160; 
 Este mensaje tendr&#58; 
 &#160; Un encabezado o introduccin general (que se le desplegar a todos los los puntos de donacin)&#160; 
 Un mensaje especfico&#58; que se desplegar solo cuando exista una definicin especfica de instrucciones para el donante (eatc-donor) al cual pertenece el anuncio 
 Un mensaje final&#58; que se le desplegar en todos los casos. 
&#160; 
 Encabezado&#58; 
 Hemos detectado que el punto de donacin ha tenido problemas en la entrega de los anuncios durante los ltimos das. 
&#160; 
 Mensaje especfico&#58; 
 Si evaluando la informacin de la cuenta correspondiente al eatc-donor del anuncio en cuestin https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name= eatc-donor), se establece que tiene el parmetro not_delivery_instructions (es decir el parmetro existe) y la informacin que contiene es una URL vlida , entonces se despliega el mensaje especfico que debe contener un hipervnculo a la URL que se obtiene de la consulta 
&#160; 
 Ejemplo &#58; 
 Para la cuenta &quot;exito&quot; se evala su respectiva configuracin con el siguiente llamado&#58;&#160; 
&#160; 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito &#160;&#160; 
&#160; 
 Dado que el parmetro &quot; not_delivery_instructions &quot; tiene registrada una URL vlida entonces se en el Warning se registra la porcin correspondiente &quot;Mensaje Especfico&quot;. 
&#160; 
 Si por ejemplo el usuario es de la cuenta &quot;colombia&quot;&#160; 
&#160; 
 https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=colombia &#160; 
&#160; 
 dado que la misma no tiene el parmetro &quot; not_delivery_instructions &quot; se pasa directamente a la seccin &quot;Registro de la no entrega&quot; 
&#160; 
 El mensaje especfico ser el siguiente. 
&#160; 
 Para evitar que tu donacin no te sea entregada, te pedimos el favor que leas con detenimiento y apliques las indicaciones que te entregamos en &quot; este vnculo &quot; 
&#160; 
 Nota&#58; se presenta el hipervnculo que funcionara para la cuenta (eatc-donor) &quot; exito &quot;, que corresponde a la informacion que se obtiene del parmetro &quot; not_delivery_instructions&quot; ( https&#58;//eatcloud.zendesk.com/hc/es-419/articles/360044685832 ) a partir de la consulta&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=exito &#160; 
&#160; 
 Nota&#58; es necesario realizar pruebas para determinar si los hipervnculos enviados aqu son bien interpretados por la App al mostrar ese mensaje.&#160; Si no es as (es decir, desde el warning que se despliega en la App no se puede acceder a un hipervnculo) de deber colocar como mensaje. 
 Para evitar que tu donacin no te sea entregada, te pedimos el favor que te dirijas a la seccin de preguntas frecuentes a travs del men principal de la App y leas el artculo &quot; Qu debo tener en cuenta para que me entreguen exitosamente una donacin en un punto del Grupo xito (xito, Carulla, Surtimax, Surti Mayorista, Super Inter)? &quot; 
&#160; 
 Mensaje final&#58; 
&#160; 
 Si permite hipervnculos&#58; 
&#160; 
 Comuncate con nuestra mesa de ayuda y/o con nuestros agentes de soporte , que haremos lo que est a nuestro alcance para que no tengas inconvenientes recogiendo tu donacin. 
&#160; 
 Nota &#58; las dos URLs estn programadas en este CMS.&#160; La URL a WhatsApp&#160; (agentes de soporte que apunta a https&#58;//api.whatsapp.com/send?phone=573125333638&amp;text=Voy%20para%20%24eatc_dona_headers.eatc-pod_name%20por%20el%20anuncio%20con%20eatc-code%20%24eatc_dona_headers.eatc-code%20y%20ese%20punto%20ultimamente%20ha%20presentado%20problemas%20entregando%20anuncios ) debe incorporar informacin del Punto de donacin ($eatc_dona_headers. eatc-pod_name o %24eatc_dona_headers.eatc-pod_name) y el cdigo de la donacin ($eatc_dona_headers. eatc-code o %24eatc_dona_headers.eatc-code ), Como se indica en el vnculo, pero que se genere de manera dinmica con los datos del anuncio. 
&#160; 
 Si NO permite hipervnculos&#58; 
&#160; 
 Comuncate con nuestra mesa de ayuda (a travs del vnculo del men principal de la App), que haremos lo que est a nuestro alcance para que no tengas inconvenientes recogiendo tu donacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 WARNING: PUNTOS DE DONACIN CON PROBLEMAS DE ENTREGA