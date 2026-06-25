# updatedomalic-servicio-para-hacerle-upgrade-a-los-datos-de-licenciamiento.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 CONTEXTO GENERAL DEL SERVICIO 
&#160; 
 El presente servicio se especifica para cambiar los datos de licenciamiento de un gestor de donaciones ( &#123;&#123;eatc_donation_managers. eatc_license &#125;&#125;, &#123;&#123;eatc_donation_managers. eatc_license_valid_until &#125;&#125; ). 
&#160; 
 Los llamados al servicio se documentan aqu&#58;&#160; Servicio privado para actualizacin de informacin de licenciamiento de un gestor de donaciones 
&#160; 
 A continuacin se documenta el proceso que debe llevarse a partir del llamado que se hace al servicio en cuestin. 

 LOG DEL SERVICIO 
&#160; 
 El sistema deber guardar en un log, los llamados exitosos y no exitosos del servicio incorporando en dicho log el porqu de un llamado no exitoso (datos incompletos, fallo de ejecucin, fallos validacin entre otros) 

 RESPUESTA ANTE UN FALLO DE EJECUCIN DEL SERVICIO 
&#160; 
 Si existe un fallo de ejecucin en el proceso el servicio debe contestar con la siguiente respuesta&#58; 
 &#160;op&#58;false 

 1. VALIDACIN DE DATOS COMPLETOS 
&#160; 
 El servicio debe validar que los datos de invocacin sean completos, segn la definicin de . Parmetros del body de la peticin &#160; de la especificacin del servicio privado . Si lo son, seguir adelante con el prximo paso.&#160; Si no lo son deber entregar una respuesta de error&#58; 
 incomplete_data 

 2. VALIDACIN DEL ESTADO DEL GESTOR DE DONACIONES 
&#160; 
 Con los datos que llega en los parmetros&#58; 
 cua_master 
 eatc_donation_manager_code 
&#160; 
 El sistema deber realizar la siguiente validacin del punto de donacin, antes de desplegarle la funcionalidad de captura de anuncios de donacin&#58; 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/api/&#123;&#123; cua_master &#125;&#125;/eatc_donation_managers? identificador_unico_registro =&#123;&#123; eatc_donation_manager_code &#125;&#125;&amp; eatc_state = activo &amp;_cmp=_id 
&#160; 
 Si la consulta no arroja un resultado, el servicio deber entregar la siguiente respuesta&#58; 
 fail_not_active_doma 
&#160; 
 Si la consulta arroja respuesta una respuesta vlida el sistema sigue con la siguiente validacin&#58; 

 3. VALIDACIN PAGO 
&#160; 
 En este punto se deber aplicar la experiencia previa (implementada con el cambio de estado ante transaccin de eatc_cua).&#160; En la medida de las posibilidades , el sistema, deber validar el pago 
&#160; 
 Si el pago no se valida, el servicio deber retornar&#58; 
 fail_not_valid_payment 
&#160; 
 Si el borrado es exitoso el sistema sigue adelante con el siguiente paso. 

 4. ACTUALIZACIN DE DATOS DE LICENCIAMIENTO DEL BENEFICIARIO 
&#160; 
 Con los datos que llega en los parmetros&#58; 
&#160; 
 cua_master 
 eatc_donation_manager_code 
 eatc_license 
 eatc_license_valid_until 
&#160; 
 El sistema deber realizar una operacin homloga a la siguiente (dado que se deber bannear precisamente este llamado o cualquier llamado similar que vare los datos de licenciamiento del gestor de donaciones a partir del CRD) 
&#160; 
 &#123;&#123; URL_entorno_beneficiarios &#125;&#125;/crd/&#123;&#123; cua_master &#125;&#125;/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_license 
 = &#123;&#123; eatc_license &#125;&#125;&amp; eatc_license_valid_until = &#123;&#123; eatc_license_valid_until &#125;&#125;&amp;WHERE identificador_unico_registro =&#123;&#123; eatc_donation_manager_code &#125;&#125; 

 5. RESPUESTA EXITOSA DEL SERVICIO ANTE UN PROCESAMIENTO COMPLETO 
&#160; 
 Si la actualizacin de datos fue exitosa, entonces entregar la respuesta&#58; 
 success 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 UPDATEDOMALIC: SERVICIO PARA ACTUALIZAR LOS DATOS DE LICENCIAMIENTO DE UN GESTRO DE DONACIONES