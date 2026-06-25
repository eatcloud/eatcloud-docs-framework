# registro-simple-de-beneficiario-final.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Mecanismo para habilitar desde la App beneficiarios un registro de usuarios finales que le permita a la plataforma tener informacin sobre la poblacin atendida por las diversas organizaciones.&#160; Esto se debe implementar en una pgina web responsiva que pueda ser invocada desde la App Beneficiarios. 
&#160; 
 Registro a cuenta usuario especfica ***Revisar dinamismo a partir de _DOM.cua_master*** 
 El registro de punto de donacin se debe generar para una cuenta usuario especfica la cual se debe generar a partir de la URL respectiva 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/&#123;&#123;_DOM. cua_master &#125;&#125;/registro_fibe . 

&#160; 
 Ejemplo _DOM. cua_master=abaco 
&#160; 
 Si se van a registrar puntos de donacin para la cuenta &quot; abaco &quot;, se debera realizar mediante el vnculo https&#58;//beneficiarios.eatcloud.info/abaco/registro_fibe &#160; (en pruebas&#58; https&#58;//devbeneficiarios.eatcloud.info/abaco/registro_fibe ). En una etapa posterior la app deber validar que la cuenta, en este caso &quot;abaco&quot; est registrada en config, es decir, que la siguiente consulta&#58; ***NUEVO*** https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua?name=abaco (anteriormente&#58; https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=abaco) traiga un resultado vlido.&#160; 
&#160; 
 Los datos se deben guardar en la estructura eatc_final_beneficiaries_lt de la cuenta respectiva, que deber ser consultada mediante la API&#58; https&#58;//beneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?_id=_* (en pruebas https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?_id=_* ) 
&#160; 
 Validacin de nmero de usuarios mximo a registrar por organizacin&#58; 
 Antes de realizar el registro, se debe validar si la organizacin en especfico, o el tipo de organizacin en general no ha superado el nmero mximo de usuarios que puede registrar.&#160; Esto se hace con el fin que las instituciones no se sobre demanden y as puedan atender de manera ptima a la poblacin que los requiere. 
&#160; 
 Consulta de nmero de usuarios registrado por organizacin ***Revisar dinamismo a partir de _DOM.cua_marter***&#58; 
&#160; 
 De los datos del usuario particular (eatc_user) se toma el parmetro &quot; organizacion &quot; y con el se consulta el nmero de usuarios que tiene la organizacin registrada de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /api/ &#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende=&#123;&#123; eatc_users.organizacion &#125;&#125; &amp;_compress 
&#160; 
 Del resultado se toma el dato &quot;cont&quot; para establecer el nmero de usuarios registrados a la fecha para la organizacin en particular (a continuacin un ejemplo) 
&#160; 
 Ejemplo _DOM. cua_master=abaco, ambiente de pruebas 
 Para el usuario cuya organizacin es 900326456-1 se realiza la siguiente consulta 
 https&#58;//devbeneficiarios.eatcloud.info/api/abaco/eatc_final_beneficiaries_lt?nit_organizacion_que_lo_atiende=900326456-1&amp;_compress obteniendo como respuesta lo siguiente (a 2020-04-01) 
 &#123; 
 ts &#58; &quot;200401175427&quot;, 
 op &#58; true, cont &#58; 1, 
 res &#58; &quot;bVFdS8ODMBTDvSvCoU8KKyTDq8OccG9jKMOuw4Exw7bCqhLCrsOJbXfCoU1qw5rCgEzDvMOvJm3Ct25qwp7CksKcwo/DnHPDssOywpVIw5LDiTIRw4kkw4lRHUAewqwDw6nCsMKgwqZ1NiBTPsOlKcOPw5JMMDFfCsK+w6TDvMOMw73Cn8OGI8KnwqcZasKldQUYOsKCImvDpMKHR1laCS3CocORGHTDt8KcZ8OTw7nDrG7CnsOGEVrCqsKtw5RWw7kKTRttw5fCr8Kec8K8w5fCvgTCpsKRKcOyGjTCmMOuVsODH8KFVFZTEcKFIsKLw4/Ch1t3bcK4w6hXAElLb0jDmcOLFCJLFyPCo3YUw7TDksOYw6rDncOFWXdYUzDCmSQNFsOeaDsiIxlqLEvDksORbMOXw4/DrsOweCHCucOAw481wprDkE1Fw4PCgMKnIsO5VcKRwoXDsyEnwrbDoMKowrPDnm/Cnh/DtivCtsOZPsKuwrbDq8ONworDnWwpwr7ClgvDiywzw4PCvsKrwowzYDMGA8OaMCFYwoUNNsK3wr9cw4fDqsO6JCDDicOkYBRBN8O9Z0TCnsO6wrzCoXUsMcK3ZkjCocOJwqHCisOfw5sfwqtYK8OVdELCsQbDl8OCw6kDYlVATcOcfcK/w70A&quot;, 
 _compress &#58; true, 
 mem &#58; 0.31, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 En el ejemplo anterior, se tiene como nmero de usuarios registrados &quot;1&quot; ( cont &#58; 1 ) 
&#160; 
 Consulta para comparacin contra el mximo especfico ***Revisar dinamismo a partir de _DOM.cua_marter***&#58; 
&#160; 
 De los datos del usuario particular (eatc_user) se toma el parmetro &quot; organizacion &quot; y con el se consulta el nmero mximo de beneficiarios finales para la organizacin en especfico de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /api/ &#123;&#123;_DOM. cua_master &#125;&#125; /eatc_max_fibe_x_doma?identificador_unico_registro=&#123;&#123; eatc_users.organizacion &#125;&#125; 
&#160; 
 Del resultado se toma el dato &quot;cantidad_maxima_ben_final&quot; para comparar con el nmero registrado a la fecha.&#160; Al realizar esta comparacin hay tres opciones&#58; 
&#160; 
 La consulta no trae datos&#58;&#160; si al realizar la consulta, esta no trae datos (ver respuesta de ejemplo abajo), se debe pasar a la siguiente comparacin &quot; Consulta para comparacin contra el mximo general por tipologa B &quot;. 
 &#123; 
 &#160;&#160;&#160;&#160;&quot;ts&quot;&#58; &quot;200401183555&quot;, 
 &#160;&#160;&#160;&#160;&quot;op&quot;&#58; true, 
 &#160;&#160;&#160;&#160;&quot;cont&quot;&#58; 0, 
 &#160;&#160;&#160;&#160;&quot;err_msg&quot;&#58; &quot;No se produjeron resultados&quot;, 
 &#160;&#160;&#160;&#160;&quot;err_num&quot;&#58; &quot;&quot;, 
 &#160;&#160;&#160;&#160;&quot;mem&quot;&#58; 0.29, 
 &#160;&#160;&#160;&#160;&quot;time&quot;&#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
 El dato &quot;cantidad_maxima_ben_final&quot; es mayor a los usuarios actualmente registrados&#58; en este caso se le permite al usuario realizar un nuevo registro de beneficiario final, pasando al formulario respectivo que se describe en &quot; Campos para el registro &quot;. 
 El dato &quot;cantidad_maxima_ben_final&quot; es menor o igual a los usuarios actualmente registrados&#58; en este caso no se le puede permitir al usuario registrar ms beneficiarios finales, por lo tanto se debe presentar el siguiente mensaje&#58; 
&#160; 
 Has registrado el nmero mximo de beneficiarios finales permitido. Si requieres ampliar este nmero por favor comuncate con la Asociacin Colombiana de Bancos de Alimentos. 
&#160; 
 Consulta para comparacin contra el mximo general por tipologa B ***Revisar dinamismo a partir de _DOM.cua_master***&#58; 
&#160; 
 De los datos de la organizacin (eatc_donation_managers) a la cual pertenece el usuario particular (eatc_user) se toma el parmetro &quot; eatc_doma_typology_b &quot; y con el se consulta el nmero mximo de beneficiarios finales para dicha tipologa de la siguiente manera&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /api/ &#123;&#123;_DOM. cua_master &#125;&#125; /eatc_max_fibe_x_doma_typology_b?eatc_doma_typology_b=&#123;&#123; eatc_donation_managers. eatc_doma_typology_b &#125;&#125; 
&#160; 
 Del resultado se toma el dato &quot;cantidad_maxima_ben_final&quot; para comparar con el nmero registrado a la fecha.&#160; Al realizar esta comparacin hay dos opciones&#58; 
&#160; 
 El dato &quot;cantidad_maxima_ben_final&quot; es mayor a los usuarios actualmente registrados&#58; en este caso se le permite al usuario realizar un nuevo registro de beneficiario final, pasando al formulario respectivo que se describe en &quot; Campos para el registro &quot;. 
 El dato &quot;cantidad_maxima_ben_final&quot; es menor o igual a los usuarios actualmente registrados&#58; en este caso no se le puede permitir al usuario registrar ms beneficiarios finales, por lo tanto se debe presentar el siguiente mensaje&#58; 
&#160; 
 Has registrado el nmero mximo de beneficiarios finales permitido. Si requieres ampliar este nmero por favor comuncate con la Asociacin Colombiana de Bancos de Alimentos. 
&#160; 
 Campos para el registro ***REVISAR dinamismo a partir de _DOM.cua_master*** 
 Los campos para el registro debern ser los siguientes&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /api/ &#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt?_campos&#160; 
&#160; 
 Nota importante&#58; la &quot;Informacin opcional para datos de contacto&quot; no fue solicitada, pero se considera importante (y muy seguramente se pedir en algn momento), razn por la cual debe ser tenida en cuenta en esta implementacin aunque no se haga inicialmente (o puede ser una especie de colapsible opcional que lo llenen si lo consideran oportuno) 

Formulario_registro_simple_usuarios 

 Botn &quot;Registrar beneficiario final&quot; ***Revisar dinamismo a partir de _DOM.cua_master*** 
 Al presionar este botn el formulario debe asegurar que todos los campos requeridos estn y sean vlidos, y luego se hace el respectivo llamado para la incorporacin de la informacin 
&#160; 
 Mtodo POST 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /crd/ &#123;&#123;_DOM. cua_master &#125;&#125;/?_tabla= eatc_final_beneficiaries_lt &amp;_operacion=insert&amp;&#123;&#123;parametros&#125;&#125; 
&#160; 
 Confirmacin de registro realizado 
 El formulario se debe confirmar la creacin correcta del punto de donacin y desplegar el siguiente mensaje&#58; 
 &quot;Beneficiario final correctamente registrado. Te invitamos a que sigas registrando tus beneficiarios en la plataforma&quot; 

&#160; 
 Carga de usuarios en lote ***Revisar dinamismo a partir de _DOM.cua_master&#58; 
 Se debe presentar una opcin en donde el usuario pueda descargar un archivo plano de muestra, para que diligencien la informacin en bloque y posteriormente sea cargada a la plataforma (carga bulk). 
&#160; 
 La plataforma deber validar que el vector de encabezados sea el correcto, y que las validaciones como &quot;unicidad del identificador nico&quot; sean llevadas a cabo por el sistema, bien sea en la misma carga, o como un proceso posterior que no permita dichos duplicados. 
&#160; 
 Tambin debe evaluarse como desde el archivo de muestra se pueden obtener los datos de los cdigos que se necesitan (como por ejemplo&#58; el cdigo del tipo de documento de identidad) bien sea como una tabla interconectada con una tabla maestra adicional o con otro mtodo que sea plausible. O tambin contemplar como en este tipo de carga simplemente se llevan a los datos solo la informacin originalmente requerida, y lo dems se deja en blanco. 
&#160; 
 Se dan indicaciones generales, porque se apela a la experiencia y los recursos del desarrollador para encontrar una implementacin de este requisito de la manera ms eficiente posible (si se estima necesario se puede utilizar el respectivo cargador&#58; 
 &#160; &#123;&#123;URL_entorno_beneficiarios&#125;&#125; /mstr/ &#123;&#123;_DOM. cua_master &#125;&#125; /eatc_final_beneficiaries_lt&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FFormulario_registro_simple_usuarios.xlsx, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FDocumentos%2520compartidos%2FFormulario_registro_simple_usuarios.xlsx 

 REGISTRO SIMPLE DE BENEFICIARIO FINAL (PERSONA NATURAL)