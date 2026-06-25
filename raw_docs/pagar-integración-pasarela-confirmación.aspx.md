# pagar-integración-pasarela-confirmación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Diseo&#58; 

 INTEGRACIN CON LA PASARELA DE PAGOS 
 Con los datos obtenidos del Carro de Compra s, y del proceso de check-out , se realiza en envo de datos a la pasarela de pagos aplicando las guas y la documentacin respectiva&#58; https&#58;//docs.wompi.co/docs/en/inicio-rapido#haz-una-integraci%C3%B3n-totalmente-a-la-medida .&#160; La pasarela entregar una confirmacin de un pago exitoso o declinar el pago y de acuerdo a esta respuesta el sistema deber actuar como se indica adelante 

 CONFIRMACIN DE PAGO EXITOSO 
 Si la pasarela de pagos entrega una respuesta confirmando un pago exitoso, el sistema deber realizar los siguientes registros de datos, para los datos del detalle de la orden respectiva (eatc_sale_order) y posteriormente deber crear el encabezado de la orden. 
&#160; 
 Actualizacin de datos de detalle 
 &#123;&#123;parmetros de actualizacin de datos de eatc_sale_order &#125;&#125; para los detalles de la presente orden 
&#160; 
 eatc-sale_order_header_code &#58; corresponder al cdigo nico de transaccin ( eatc_sale_order_header.eatc-code ), que se genera en el proceso de pago .&#160; 

 eatc-odd_state&#58; corresponder a la constante paid_out 
&#160; 
 [***] Se guarda la informacin en el object store eatc_sale_order de la cuenta eatcloud&#58; 
&#160; 
 Mtodo POST&#160; 
&#160; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order&amp;_operacion=update&amp; &#123;&#123;Parmetros actualizacin en eatc_sale_order &#125;&#125;&amp;WHERE_id=&#123;&#123;id_registro_sale_order&#125;&#125; 
&#160; 
 Una vez se realicen los respectivos registros, el sistema deber confirmar que los mismos hallan sido realizados de manera exitosa (respespuesta de exito del API) para proceder con el siguiente proceso 
&#160; 
 Ejemplo&#58; 
 En ambiente de pruebas se recibe un pago exitoso de un pedido compuesto por el _id=55 . El proceso de pago haba generado para esta transaccin el cdigo 7777 , por lo tanto el llamado al servicio debe ser&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crd/eatcloud/?_tabla=eatc_sale_order&amp;_operacion=update&amp; eatc-sale_order_header_code= 7777 &amp;eatc-odd_state= paid_out &amp;WHERE_id= 55 &#160; 

&#160; 
 Registro de encabezado de pedido 
 El sistema realiza el proceso de creacin de encabezado de orden , haciendo el siguiente llamado al servicio dispuesto para este fin&#58; 
&#160; 
 &#123;&#123;URL_entorno_beneficiario&#125;&#125;/saleheaders/eatcloud/&#123;&#123;eatc_sale_order_header. eatc-code &#125;&#125;/&#123;&#123;eatc_sale_order_header. eatc-delivery_method &#125;&#125; 
&#160; 
 Dnde&#58; 
 eatc_sale_order_header. eatc-code // que se obtiene al invocar proceso de check-out 
 eatc_sale_order_header. eatc-delivery_method // que se obtiene en el proceso de check-out 
&#160; 
 Ejemplo&#58; 
 Se desea generar un encabezado, en ambiente de pruebas, con los siguientes datos&#58; 
&#160; 
 eatc_sale_order_header. eatc-code = 7777 
 eatc_sale_order_header. eatc-delivery_method = Recogida por parte del usuario 
&#160; 
 Por lo tanto el llamado al servicio debe ser&#58; 
 https&#58;//devbeneficiarios.eatcloud.info/saleheaders/eatcloud/7777/Recogida%20por%20parte%20del%20usuario &#160; 
&#160; 
 El sistema entrega la siguiente respuesta&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;200903093819&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 mem &#58; 0.4, 
 time &#58; &quot;00&#58;00&#58;00&quot; 
 &#125; 
&#160; 
 El encabezado queda creado y se puede consultar aqu&#58;&#160; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/api/eatcloud/eatc_sale_order_headers?eatc-code=7777 &#160; 
&#160; 
 Si se desean consultar los datos desencriptados del usuario que se guardan en el encabezado se utiliza el siguiente llamado (teniendo en cuenta los procesos de autenticacin )&#58; 
&#160; 
 https&#58;//devbeneficiarios.eatcloud.info/crypt/eatcloud/decrypt?table=eatc_sale_order_headers&amp;fieldname= eatc-user_doc_id , eatc-user_name , eatc-user_address , eatc-user_phone , eatc-user_city &amp;filterfield_1=eatc-code&amp;filtervalue_1=7777 &#160; 

 Gracias por tu pedido 
 ......&#58; 
&#160; 
 Nombre de quien recoge 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Una variable&#58; eatc_sale_order_headers. eatc-picker_name , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 
&#160; 
 Nmero de documento 
 Tipo de dato &#58; string 
 Tipo de input de datos&#58; text field 
 Obligatoriedad &#58; si 
 Validacin &#58; obligatoriedad 
 Se guarda en &#58;&#160; 
Una variable&#58; eatc_sale_order_headers. eatc-picker_doc_id , que posteriormente se llevar al registro del encabezado de la orden ( eatc_sale_order_headers ) 

 TRANSACCIN DECLINADA 
 Si la transaccin es declinada por la pasarela de pagos, el sistema debe mostrar el siguiente mensaje&#58; 
&#160; 
 Tu transaccin ha sido declinada por la pasarela de pago. Deseas intentar de nuevo con otro medio de pago? 
&#160; 
 Si&#160; No 
&#160; 
 Opcin Si 
 Se retorna a la vista para ingresar un medio de pago y volver a intentar la transaccin 

&#160; 
 Opcin No 
 El sistema despliega otro mensaje de advertencia 
&#160; 
 Ests seguro de declinar la transaccin? Esto retornar los productos a inventario, para que puedan ser adquiridos por otros miembros de nuestra comunidad de rescate de alimentos. 
&#160; 
 Si, quiero declinar&#160; &#160; &#160; No, quiero intentar de nuevo 
&#160; 
 Opcin&#58; No, quiero intentar de nuevo 
 Se retorna a la vista para ingresar un medio de pago y volver a intentar la transaccin 
&#160; 
 Opcin&#58; Si, quiero declinar&#58; 
 Si el usuario&#160; declina la transaccin el sistema deber actualizar los registros para reversar la transaccin como se estipula a continuacin 
&#160; 
 Actualizacin de registros tras declinar una transaccin&#58; 
 Actualizacin de estado (declinado) de los registros eatc_sale_order&#58; 
 El sistema deber registrar el nuevo estado &quot; declined &quot; para cada uno de los registros de detalle (cada uno de los _id que componen la orden) de orden ( eatc_sale_order ) y tambin debern devolverse los datos definitivos de dicha orden a&#160; 0 de la siguiente manera&#58; 
&#160; 
 &#123;&#123;parmetros de actualizacin de eatc_sale_order &#125;&#125; 
&#160; 
 eatc-odd_quantity= 0 
 eatc-odd_total_weight_kg= 0 
 eatc-odd_total_price= 0 
 eatc-vat_base= 0 
 eatc-total_vat= 0 
 eatc-other_taxes_base= 0 
 eatc-total_other_taxes= 0 
 eatc-state =declined 
&#160; 
 Teniendo los _ids de la eatc_sale_order declinada, se realiza el siguiente llamado para actualizar la informacin. 
&#160; 
 &#123;URL_entorno_beneficiarios&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale_order&amp;_operacion=update&amp; &#123;&#123;parmetros de actualizacin de eatc_sale_order &#125;&#125;&amp;WHERE_id=&#123;&#123;ids_sale_order&#125;&#125; 
&#160; 
 Reversa de inventario en la oferta eatc_sale&#58; 
 Las unidades que estaban &quot;separadas&quot; para el pedido que fue declinado ( eatc_sale_order. eatc-odd_original_quantity ) se debern reversar para adicionarlas en el&#160; registro previo de cantidad disponible&#160; ( eatc-odd_quantity_anterior) en eatc_sale &#160; 
&#160; 
 Para establecer cul es el registro previo de cantidad disponible se debe hacer la siguiente consulta. para obtener el valor eatc-odd_quantity antes de realizar la operacin, para la orden que se est revesando (eatc_sale_order), mandando el parmetro eatc_sale_order .eatc-sale_code de los diferentes detalles de orden que se estn reversando al parmetro eatc_code de la oferta ( eatc_sale ). 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/api/eatcloud/eatc_sale? eatc-code=&#123;&#123; eatc_sale_order .eatc-sale_code&#125;&#125; eatc-odd_quantity 

&#160; 
 Ejemplo ambiente de pruebas&#58; 
 Se desea saber cual es la cantidad anterior ( eatc-odd_quantity_anterior ) teniendo como base el eatc_sale_order cuyo eatc-code es 5 
&#160; 
 Por tal motivo la consulta sera la siguiente&#58; 
&#160; 
 https&#58;//devdonantes.eatcloud.info/api/eatcloud/eatc_sale? eatc-code= 5 
&#160; 
 Como la consulta trae esta informacin (a 24 de septiembre de 2020 siendo las 4&#58;11 PM)&#58; 
&#160; 
 &#123; 
 ts &#58; &quot;200924161028&quot;, 
 op &#58; true, 
 cont &#58; 1, 
 res &#58;&#160; 
 [ 
 &#123; 
 _id &#58; &quot;5&quot;, 
 eatc-dona_header_code &#58; &quot;5&quot;, 
 ...... , 
 eatc-odd_original_quantity &#58; &quot;50&quot;, 
 eatc-odd_quantity &#58; &quot;28&quot;, 
 eatc-pod_id &#58; &quot;u4bdtz0ie85xBZPKp1 
 .... 
&#160; 
 eatc-odd_quantity_anterior=28 
&#160; 
 y tambin cambiar el estado del respectivo item ( eatc-odd_state ) de la siguiente manera&#58; 
&#160; 
 Si eatc-odd_quantity_anterior + eatc_sale_order. eatc-odd_original_quantity&#160; es menor&#160; eatc_sale. eatc-odd_original_quantity entonces new_state =partially_ordered &quot; 
 Si eatc-odd_quantity_anterior + eatc_sale_order. eatc-odd_original_quantity&#160; es igual a&#160; eatc_sale. eatc-odd_original_quantity entonces new_state = sale 
 Si eatc-odd_quantity_anterior + eatc_sale_order. eatc-odd_original_quantity&#160; es mayor&#160; eatc_sale. eatc-odd_original_quantity entonces se&#160; produjo un error, y por lo tanto se debe colocar&#160; eatc-odd_quantity=eatc-odd_original_quantity y new_state = sale 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/crd/eatcloud/?_tabla=eatc_sale&amp;_operacion=update&amp; eatc-odd_quantity=&#123;&#123; eatc_sale_order. eatc-odd_original_quantity + eatc_sale_order. eatc-odd_original_quantity &#125;&#125; &amp;eatc-odd_state=&#123;&#123;new_state&#125;&#125;&amp;WHEREeatc-code=&#123;&#123;eatc-code&#125;&#125; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fpagar-integraci%C3%B3n-pasarela-confirmaci%C3%B3n%2F874097839-EmbeddedImage---2024-07-30T010627.363.jpg&ow=448&oh=860, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fpagar-integraci%C3%B3n-pasarela-confirmaci%C3%B3n%2F874097839-EmbeddedImage---2024-07-30T010627.363.jpg&ow=448&oh=860 
 App usuario final - Sale 

 836.000000000000 

 PAGAR: INTEGRACIN PASARELA, CONFIRMACIN PASARELA, GENERACIN DE INFORMACIN DE ENCABEZADO DE PEDIDO