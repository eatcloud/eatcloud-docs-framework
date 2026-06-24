# cancelación-anuncio-de-donación-eatc_dona_cancel.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Botn "no estoy interesado" 
 Al presionar este botn, el sistema debe tomar los datos de la donacin seleccionada , del gestor de donaciones , de la cuenta maestra y del usuario de la App , y del match del anuncio respectivo para realizar el siguiente llamado: 

 ***ANTERIORMENTE: estaba documentado el llamado a {{ URL_entorno_datagov }}, pero lo que funciona est en entrono beneficiarios y el servicio era im_not_interested y ahora notinterested *** 

 {{ URL_entorno_beneficiarios }} / notinterested /{{ _DOM. cua_master }}? eatc_country = {{ eatc_cua_master . eatc_country }}& eatc_city = {{{ eatc_dona_headers. eatc-city }}& eatc_doma = {{ eatc_donation_managers. organizacin }}& eatc_doma_code= {{ eatc_donation_managers. identificador_unico_registro }}& eatc_user= {{ eatc_users . correo_electronico }}& eatc_platform = app_beneficiarios & eatc_dona_header_code ={{ eatc_dona_headers. eatc-code }}& eatc_cua = {{ eatc_dona_headers. eatc_cua_origin }}& eatc_state ={{ eatc_dona_headers. eatc-state }}& eatc_match_registry_id= {{ eatc_match_registry. _id }} 

 Para obtener el _id del match se debe realizar la siguiente consulta: 

 ({{URL_entorno_beneficiario}}/api/ {{ _DOM. cua_master }} / eatc_match_registry ? organizacin = {{ eatc_donation_managers. organizacin }} &eatc-dona_header_code= {{ eatc_dona_headers. eatc-code }} &_distinct= _id ) 

 Vnculo "cancelar" 
 Retorna a la vista anterior sin ninguna accin adicional. 

 DEPRECADO:  

 Botn "no estoy interesado" 
 Al presionar este botn, el anuncio se debe retirar del listado de la funcionalidad " Nube de donaciones " (no volverlo a mostrar en el listado) y se debe retornar a dicha vista. 

 Borrado de match (cuando estn implementadas las funcionalidades de Match ) ***REVISAR dinamismo a partir de _DOM.cua_master*** 

 El sistema debe borrar el registro de match, que se utiliza para definir los anuncios que se muestran en la nube de donaciones con el siguiente llamado: 

 {{URL_entorno_beneficiarios}}/crd/{{_DOM. cua_master }}/?_tabla= eatc_match_registry &_operacion=DELETE&WHERE_id={{_id}} 

 Ejemplo _DOM. cua_master=abaco: 
 El usuario defini (perteneciente a la organizacin (cuyo cdigo es 900082682-9 y organizacin : "ASOCIACION DE BANCOS DE ALIMENTOS DE COLOMBIA") que no le interesa el anuncio (eatc_dona) de donacin cuyo eatc-dona_header_code (eatc-code) es " 2019209714"  por lo tanto debe realizar una llamada al API para la tabla de Match para determinar el _id del registro: 

 https://beneficiarios.eatcloud.info/api/abaco/ eatc_match_registry ? organizacin =ASOCIACION%20DE%20BANCOS%20DE%20ALIMENTOS%20DE%20COLOMBIA&eatc-dona_header_code=2019209714    

 DEPRECADO: https://beneficiarios.eatcloud.info/api/abaco/eatc_match_registry?eatc-donation_manager_code=900082682-9&eatc-dona_header_code=2019209714    

 Determinando que su _id : "2", Por lo tanto realiza el siguiente llamado al API para borrar el registro de match 

 Ambiente productivo: https://beneficiarios.eatcloud.info/crd/abaco/?_tabla=eatc_match_registry&_operacion=DELETE&WHERE_id=2   

 Nota : para deshacer este ejemplo (es decir para volver a generar el registro de match) ir a aqu   

 Vnculo "cancelar" 
 Retorna a la vista anterior sin ninguna accin adicional. 

 ***NUEVO: Registro en eatc_match_rejection_registry*** 

 Con los datos de la donacin seleccionada, del gestor de donaciones y del usuario de la App, se realiza el siguiente registro: 

 {{parametros_registro}} 
 eatc_datetime = {{timestamp_en_formato AAAA-MM-DD HH:MM:SS }} 
 eatc_date = {{datestamp_en_formato AAAA-MM-DD }} 
 eatc_country ={{ URL_entorno_datagov }}/api/eatcloud/ eatc_cua_master ?eatc_cua={{_DOM. cua_master }}&_distinct =eatc_country 
 eatc_city ={{eatc_dona_headers. eatc-city }} 
 eatc_cua_master ={{_DOM. cua_master }} 
 eatc_doma ={{eatc_donation_managers. organizacin }} 
 eatc_doma_code ={{eatc_donation_managers. identificador_unico_registro }} 
 eatc_dona_header_code ={{eatc_dona_headers. eatc-code }} 
 eatc_cua ={{eatc_dona_headers. eatc_cua_origin }} 
 eatc_platform =app_beneficiarios 
 eatc_reject_cause =no_me_interesa 
 eatc_user ={{eatc_users. correo_electronico }} 

 Llamado al api con los {{parametros_registro}} (en el llamado los parmetros se separan por " & ") 
 {{ URL_entorno_datagov }}/crd/eatcloud/?_tabla=eatc_match_rejection_registry&_operacion=insert& {{parametros_registro}} 

 Ejemplo: Ambiente de pruebas, Gestor de donaciones: Banco Arquidiocesano de Alimentos de Cali , Usuario: astridgiraldo@bancalimentos.org , Anuncio de donacin " 00002108194223 (no est en productivo, est en ambiente de pruebas ) " el " 2021-09-11 14:43:00 ". 

 El sistema toma los siguientes datos 
 eatc_datetime =2021-09-11 14:43:00 
 eatc_date =2021-09-11 
 eatc_country = https://dev.donantes.eatcloud.info/api/eatcloud/ eatc_cua_master ?eatc_cua=abaco&_distinct =eatc_country =co 
 eatc_city ={{ eatc_dona_headers. eatc-city }}=CALI 
 eatc_cua_master =abaco 
 eatc_doma ={{ eatc_donation_managers. organizacin }}=FUNDACION ARQUIDIOCESANA BANCO DE ALIMENTOS DE CALI 
 eatc_doma_code ={{ eatc_donation_managers. identificador_unico_registro }}=805025018 
 eatc_dona_header_code ={{ eatc_dona_headers. eatc-code }}=00002108194223 
 eatc_cua ={{ eatc_dona_headers. eatc_cua_origin }}=exito 
 eatc_platform =app_beneficiarios 
 eatc_reject_cause =no_me_interesa 
 eatc_user ={{ eatc_users. correo_electronico }}=astridgiraldo@bancalimentos.org 

 Entonces se realiza el siguiente llamado al API de creacin de registro 
 https://dev.datagov.eatcloud.info/crd/eatcloud/?_tabla=eatc_match_rejection_registry&_operacion=insert& eatc_datetime =2021-09-11%2014:43:00& eatc_date =2021-09-11& eatc_country= co& eatc_cua_master =abaco& eatc_cua =abaco& eatc_doma =FUNDACION%20ARQUIDIOCESANA%20BANCO%20DE%20ALIMENTOS%20DE%20CALI& eatc_doma_code =805025018& eatc_dona_header_code =00002108194223& eatc_cua =exito& eatc_platform =app_beneficiarios& eatc_reject_cause =no_me_interesa& eatc_user =astridgiraldo@bancalimentos.org 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaci%C3%B3n-anuncio-de-donaci%C3%B3n-eatc_dona_cancel%2F3452108644-10.1-no-interesado-cancela--eatc_dona_cancel-.png&ow=750&oh=1334, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fcancelaci%C3%B3n-anuncio-de-donaci%C3%B3n-eatc_dona_cancel%2F3452108644-10.1-no-interesado-cancela--eatc_dona_cancel-.png&ow=750&oh=1334 
 EatCloud Beneficiarios 

 542.000000000000 

 CANCELACIN ANUNCIO DE DONACIN (EATC_DONA_CANCEL)