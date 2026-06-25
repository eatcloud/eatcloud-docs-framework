# no-me-validaron-el-código-de-recogida.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Dado que cuando se realiza un registro de check-out y no est presente la fecha y hora de verificacin del cdigo de recogida (bien sea si se hizo de a tiempo o de manera extempornea ), se realiza un registro automtico en &quot;eatc_checkin_and_deliver_issues&quot;, al ingresar a esta funcionalidad se deben mostrar los issues respectivos con su informacin bsica, de la siguiente manera. 
&#160; 
 Consulta para traer informacin 
 Para traer la informacin de los Issues por no validacin del cdigo de recogida, para el anuncio en cuestin, se utiliza la siguiente consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code =&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; resolved =no 
&#160; 
 Con el resultado de la consulta de presenta la informacin de la siguiente manera 
&#160; 
 Presentacin de informacin&#58; 
 Con los datos que trae la consulta, en particular estos&#58; 
&#160; 
 Se hace el registro de un issue, por la no realizacin de la validacin a tiempo. de la siguiente manera&#58; 
 eatc-datetime &#58; fecha actual en formato AAAA-MM-DD HH&#58;MM&#58;SS 
 eatc-pod_name &#58; corresponde a eatc_dona_headers. eatc-pod_name 
 eatc-dona_header_code &#58; corresponde a eatc_dona_headers. eatc-code 
 eatc-verification_code&#58; corresponde a eatc_dona_headers. eatc-verification_code 
 eatc-dona_final_state &#58; corresponde a eatc_dona_headers. eatc-state 
 eatc-issue_cause_code &#58; extemporaneous_code_verification . 
 eatc-issue_cause &#58; El punto de donacin no valid el cdigo de recogida antes de la salida del gestor de sus instalaciones. 
&#160; 
 Se debe disponer el siguiente mensaje&#58; 
&#160; 
 El &#123;&#123;eatc_checkin_and_deliver_issues. eatc-datetime &#125;&#125; el sistema detect que &#123;&#123;eatc_checkin_and_deliver_issues. eatc-issue_cause &#125;&#125; y por lo tanto el anuncio sigue estando en estado &#123;&#123;eatc_checkin_and_deliver_issues. eatc-dona_final_state &#125;&#125;. Hemos notificado automticamente al &#123;&#123;eatc_checkin_and_deliver_issues. eatc-pod_name &#125;&#125; enviando el cdigo de verificacin para que pueda realizar el proceso de manera remota. 
&#160; 
 Te recordamos para futuras ocasiones, que antes de salir del punto de donacin te cerciores que te validen el cdigo de recogida. 
&#160; 
 Si requieres ms ayuda comuncate con nuestro helpdesk y/o con nuestros agentes de soporte , que haremos lo que est a nuestro alcance para realizar la verificacin del cdigo. 
&#160; 
 Consulta de datos de telfonos de soporte ***Implementacin de dinamismo a partir de _DOM.cua_master*** 
 Para&#160; incorporar el telfono del agente de soporte ( telefono_soporte ), se debe realizar el siguiente llamado al API&#58; 
&#160; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_cua=&#123;&#123;_DOM. cua_master &#125;&#125; 
&#160; 
 El valor que retorna el parmetro &quot; eatc_doma_wa &quot; corresponde al telefono_soporte 
&#160; 
 Nota &#58; las dos URLs estn programadas en este CMS. La URL a WhatsApp (agentes de soporte que apunta a&#160; 
&#160; 
 https&#58;//api.whatsapp.com/send?phone=&#123;&#123;telefono_soporte&#125;&#125;&amp;text=&#123;&#123;eatc_dona_headers.eatc-pod_name&#125;&#125;%20no%20valid%20a%20tiempo%20el%20cdigo%20de%20recogida%20del%20anuncio%20con%20eatc-code%20&#123;&#123;eatc_dona_headers.eatc-code&#125;&#125;%20Por%20favor%20me%20pueden%20ayudar)&#160; 
&#160; 
 debe incorporar informacin del Punto de donacin (&#123;&#123;eatc_dona_headers. eatc-pod_name&#125;&#125; o anteriormente %24eatc_dona_headers.eatc-pod_name) y el cdigo de la donacin (&#123;&#123;eatc_dona_headers. eatc-code&#125;&#125; o o anteriormente eatc_dona_headers.eatc-code ), Como se indica en el vnculo, pero que se genere de manera dinmica con los datos del anuncio. 

&#160; 
 No trae informacin (se recuperan &quot;issues&quot; resueltos)&#58; 
 Si la&#160; consulta 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125;&amp; resolved =no 
&#160; 
 No trae informacin, entonces se debe realizar la siguiente consulta&#58; 
&#160; 
 &#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 Si trae informacin quiere decir que el Issue fue resuelto y por lo tanto el anuncio ya debe tener el estado de &quot;delivered&quot;, por lo tanto se debe mostrar el siguiente mensaje&#58; 
&#160; 
 El punto de donacin ya valid el cdigo de recogida a las &#123;&#123;eatc_dona_headers. eatc-code_verification_datetime &#125;&#125; y tu anuncio tiene estado &#123;&#123;eatc_dona_headers. eatc-state en espaol &#125;&#125;. Por lo tanto ya podrs seguir con el proceso de verificacin del anuncio para darlo por recibido. 
&#160; 
 Te recordamos para futuras ocasiones, que antes de salir del punto de donacin te cerciores que te validen el cdigo de recogida. 
&#160; 
 Botn&#58; Verificar Anuncio de donacin. 
&#160; 
 El botn debe cumplir las mismas reglas de despliegue que se definen para el mismo en el dashboard de donacin, y dar acceso a la funcionalidad &quot; Verificacin detallada de anuncio de donacin &quot; 
&#160; 
 No trae informacin (no se encuentran issues)&#58; 
 Si con la consulta&#58; 
&#160; 
 &#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/ eatc_checkin_and_deliver_issues ? eatc-dona_header_code=&#123;&#123;eatc_dona_headers. eatc-code &#125;&#125; 
&#160; 
 No se recupera ninguna informacin, se debe mostrar el siguiente mensaje&#58; 
&#160; 
 Te recomendamos descargar aqu la ltima versin de la App, que tiene herramientas para gestionar de manera automtica este tipo de incidencias. 
&#160; 
 Te recordamos para futuras ocasiones, que antes de salir del punto de donacin te cerciores que te validen el cdigo de recogida. 
&#160; 
 Comuncate con nuestro helpdesk y/o con nuestros agentes de soporte , que haremos lo que est a nuestro alcance para realizar la verificacin del cdigo. 
&#160; 
 Nota &#58; las dos URLs estn programadas en este CMS. La URL a WhatsApp (agentes de soporte que apunta a https&#58;//api.whatsapp.com/send?phone=573125333638&amp;text=%24eatc_dona_headers.eatc-pod_name%20no%20valid%20a%20tiempo%20el%20cdigo%20de%20recogida%20del%20anuncio%20con%20eatc-code%20%24eatc_dona_headers.eatc-code.%20Por%20favor%20me%20pueden%20ayudar) debe incorporar informacin del Punto de donacin ($eatc_dona_headers. eatc-pod_name o %24eatc_dona_headers.eatc-pod_name) y el cdigo de la donacin ($eatc_dona_headers. eatc-code o %24eatc_dona_headers.eatc-code ), Como se indica en el vnculo, pero que se genere de manera dinmica con los datos del anuncio. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 
 EatCloud Beneficiarios 

 NO ME VALIDARON EL CDIGO DE RECOGIDA