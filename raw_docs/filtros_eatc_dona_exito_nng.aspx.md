# filtros_eatc_dona_exito_nng.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Para generar el proceso de Enriquecimiento del anuncio de donacin ( eatc_dona ) solo se debe trabajar con la informacin autorizada para el piloto, por este motivo se debe obviar informacin que no aplica.&#160; A continuacin algunas reglas al respecto 

 Archivo de trabajo&#58; DEP_map_eatc_dona_exito.cfg 

 #nombre del archivo externo 
 nombre = devolucionesnutresa_ddmmaaaa 
 extension = csv&#160; 
 separadores = comas 
 ruta = Z&#58;\Produccion\BancoDonaciones\CRMOVISINE 
&#160; 
 #vector de encabezados 
 headers_vector = Dia DiaID,Dependencia Despacha Dependencia Despacha ID,Sublinea ID,Plu PluCD,Plu DESC, EAN,Proveedor Nit,Proveedor NombreProveedor,Orden Despacho/Devolucion ID,Causa de Devolucion Causa Devolucion ID,Causa de Devolucion Causa Devolucion DESC,# Unidades Despachadas,$ CtoCantDespachada,Plu PluID,Tarifa IVA 
&#160; 
 headers_action = validate //insert&#58; se debe insertar el vector de encabezados al archivo que se carga (porque no lo tiene); validate&#58; se debe validar que el vector de encabezados siempre sea uniforme aunque no debe importar el orden de los campos, solo su declaracin 

 Filtro Proveedor 
 Solo se podrn generarse donaciones de los proveedores que posean cuenta en EatCloud&#58; 
&#160; 
 Planteamiento inicial (si se puede hacer la relacin de un nit a una cuenta) 
&#160; 
 Se debe buscar que el parmetro &quot; customer__eatc_clientes__partyidentification &quot; del maestro de cuentas ( https&#58;//config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_cua&amp;name=_todos ),&#160; corresponda al parmetro &quot; Proveedor Nit &quot; 

 Filtro Sublnea 
 Solo se podrn entregar a partir de este archivo productos de la sublnea&#58; 
&#160; 
 93 (Galletas) 

 Filtro PLU 
 Cmo solo se autoriza para donar los siguientes productos&#58; 
&#160; 
 https&#58;//donantes.eatcloud.info/api/nutresa/eatc_odds?_id=_* 
&#160; 
 Si una&#160; Orden Despacho/Devolucion ID ( eatc-doc) posee un PLU por fuera de los autorizados (verificar que el campo Plu PluCD corresponda al campo &quot; eatc-odd_external_code1 &quot; de la anterior consulta.), el sistema debe retirar de eatc_dona todos los artculos correspondientes a esa&#160; Orden Despacho/Devolucion ID ( eatc-doc) , guardar los artculos retirados en un esquema de almacenamiento similar en estructura a eatc_dona pero destinado a los errores ( eatc_dona_errors )&#160; y colocar en el campo&#160; eatc-warning de dicho esquema de almacenamiento de errores la siguiente leyenda&#58;&#160; 
&#160; 
 Orden de despacho retirada del anuncio de donacin por tener el (los) PLU(s) $&#123;array de PLUs que no corresponden&#125; que no esta(n) autorizado(s)&quot;.&#160; Por favor no recogerla dentro de la donacin 
&#160; 
 En el campo eatc-warning de los artculos que no fueron retirados del respectivo anuncio, se deben guardar la Ordeno Despacho/Devolucion ID ( eatc-doc) o las rdenes retiradas para posteriormente llevar dicha informacin al campo eatc-warning de eatc_dona_headers de la siguiente manera 
&#160; 
 La(s) Orden(es) de despacho $&#123;array de eatc-doc&#125; ha(n) sido retirada(s) del anuncio de donacin del da de hoy por tener el (los) PLU(s) $&#123;array de PLUs que no corresponden correspondientes a la consulta eatc_dona_errors.eatc-odd_id https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_errors?eatc-doc=$&#123;array de eatc-doc&#125;&#125; que no esta(n) autorizado(s) a ser donados. POR FAVOR NO RECIBA ESTA MERCANCA COMO DONACIN.&#160; 

&#160; 
 Notificacin por correo electrnico a encargado de despacho 
 Posteriormente se deber enviar un correo electrnico al encargado de despacho del almacn respectivo un mensaje que contenga lo siguiente. 
&#160; 
 La(s) Orden(es) de despacho $&#123;array de eatc-doc&#125; ha(n) sido retirada(s) del anuncio de donacin del da de hoy por tener el (los) PLU(s) $&#123;array de PLUs que no corresponden correspondientes a la consulta eatc_dona_errors.eatc-odd_id https&#58;//devdonantes.eatcloud.info/api/abaco/eatc_dona_errors?eatc-doc=$&#123;array de eatc-doc&#125;&#125; que no esta(n) autorizado(s) a ser devueltos.&#160; Le solicitamos el favor anule la(s) respectiva(s) orden(es) de despacho, y las vuelva a generar solo con los PLUs autorizados, para que puedan ser incorporadas a partir del da de maana en el anuncio de donacin.&#160; 
&#160; 
 Le pedimos el favor no entregue el contenido de la(s) orden(es) retiradas como donacin. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 FILTROS_EATC_DONA_EXITO_NNG