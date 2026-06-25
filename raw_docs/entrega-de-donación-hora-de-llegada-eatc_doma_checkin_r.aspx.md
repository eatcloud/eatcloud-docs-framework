# entrega-de-donación-hora-de-llegada-eatc_doma_checkin_r.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Registro de llegada de beneficiario 
&#160; 
 Cuando el anuncio tiene un estado (eatc-state) &quot;scheduled&quot; (programado) debe aparecer el botn &quot; registro de llegada beneficiario &quot; quien da la entrada a la funcionalidad &quot; Entrega de donacin&#58; hora de llegada &quot;.&#160; 
&#160; 
 Validacin del cdigo de verificacin de donacin 
 Al accionar el botn &quot; registro de llegada beneficiario&quot; debe salir un formulario para ingresar el Cdigo de verificacin del beneficiario que recoge. Este cdigo corresponde al parmetro &quot; eatc-verification_code &quot;, del respectivo encabezado de donacin ( eatc_dona_headers ). 
&#160; 
 Ejemplo&#58; 
 El para el anuncio cuyo &quot; eatc-id &quot; = 8687012&#160; 
&#160; 
 Ambiente productivo&#58; https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012 &#160; 

 El cdigo de verificacin (eatc-verification_code) es&#58; 715518 &#160;&#160; 
&#160; 
 Por lo tanto si el usuario digita dicho nmero y se oprime el botn &quot; valida el cdigo &quot; ( https&#58;//donantes.eatcloud.info/api/abaco/eatc_dona_headers?eatc-id=8687012&amp;eatc-verification_code=715518 ) el sistema lo debe dejar pasar. y debe traer a pantalla la siguiente informacin&#58; 
&#160; 
 eatc-donation_manager_name = Nombre del gestor de donaciones al cual se le adjudica el anuncio&#160; 
 eatc-picker_name = Nombre de la persona quien recoge la donacin 
 eatc-picker_doc_id = Documento de identidad de la persona quien recoge la donacin 
 eatc-picker_license_plate = Nombre de la persona quien recoge la donacin 
&#160; 
 Si se digita un cdigo diferente, se debe anunciar que el cdigo no es vlido y no dejar continuar. 

 Registro de la fecha y hora de llegada (eatc-picking_checkin_datetime)&#160; 
 Una vez validado el usuario, mediante el API (CRUD), el sistema debe registrar la fecha y hora de llegada ( eatc-picking_checkin_datetime ) en el respectivo encabezado ( eatc_dona_headers ) 
&#160; 
 Escritura con la API&#58;&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime=[fecha_hora]&amp;WHEREeatc-code=[valor] 
&#160; 
 Ejemplo&#58; 
 Para el anuncio de donacin cuyo eatc-code = 40717 , y que mediante la App se accion el botn de registro de llegada de beneficiario a las 2019-11-01 10&#58;10&#58;00&#160; mediante la API se debe hacer la siguiente escritura 
&#160; 
 https&#58;//donantes.eatcloud.info/crd/abaco/?_tabla=eatc_dona_headers&amp;_operacion=update&amp;eatc-picking_checkin_datetime=2019-11-01%2010&#58;10&#58;00&amp;WHEREeatc-code=40717 
&#160; 
 La App debe validar que el registro se realice, es decir que se obtenga una respuesta de este tipo&#58; 
 &#123; 
 ts &#58; &quot;190924114127&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.74, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 SI no se logra obtener esta respuesta, el sistema debe reintentar el llamado al API, hasta obtener una respuesta satisfactoria. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fentrega-de-donaci%C3%B3n-hora-de-llegada-eatc_doma_checkin_r%2F15891320-7-entrega-de-donaciones--eatc_dona_checkin_r-.png&ow=1280&oh=910, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fentrega-de-donaci%C3%B3n-hora-de-llegada-eatc_doma_checkin_r%2F15891320-7-entrega-de-donaciones--eatc_dona_checkin_r-.png&ow=1280&oh=910 
 EATCLOUD DESKTOP 

 98.0000000000000 

 ENTREGA DE DONACIN: HORA DE LLEGADA (EATC_DOMA_CHECKIN_R