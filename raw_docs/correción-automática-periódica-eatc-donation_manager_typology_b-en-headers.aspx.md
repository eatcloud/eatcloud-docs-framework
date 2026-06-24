# correción-automática-periódica-eatc-donation_manager_typology_b-en-headers.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Aunque ya se gener el ajuste para que al momento de adjudicarse la donacin se realice el registro correcto , es una mejora que se debe difundir mediante actualizacin de la App y puede darse el caso que usuarios no actualicen y sigan enviando informacin errada, se debe crear un proceso que corra todas las noches para revisar los datos de "" y si en los mismos no hay [a julio 19 de 2020] un entero de un dgito realizar el siguiente query: 

 Tipologa A 
 eatc-donation_manager_typology_a= {{eatc_donation_managers( identificador_unico_registro= eatc_dona_headers .eatc-donation_manager_code ). organizacion_vinculada}} 

 Es decir se debe ir a la tabla " eatc_donation_managers "  para traer a partir del dato del encabezado " eatc_dona_headers .eatc-donation_manager_code ", el punto de donacin y reemplazar el valor ( eatc_dona_headers .eatc-donation_manager_typology_b ) por lo que trae el campo " eatc_donation_managers. organizacion_vinculada " 

 Tipologa B 
 eatc-donation_manager_typology_b= {{eatc_donation_managers( identificador_unico_registro= eatc_dona_headers .eatc-donation_manager_code ). eatc_doma_typology_b}} 

 Es decir se debe ir a la tabla " eatc_donation_managers "  para traer a partir del dato del encabezado " eatc_dona_headers .eatc-donation_manager_code ", el punto de donacin y reemplazar el valor ( eatc_dona_headers .eatc-donation_manager_typology_b ) por lo que trae el campo " eatc_donation_managers. eatc_doma_typology_b " 

 Tipologa C 
 eatc-donation_manager_typology_b= {{eatc_donation_managers( identificador_unico_registro= eatc_dona_headers .eatc-donation_manager_code ). tipo_organizacion}} 

 Es decir se debe ir a la tabla " eatc_donation_managers "  para traer a partir del dato del encabezado " eatc_dona_headers .eatc-donation_manager_code ", el punto de donacin y reemplazar el valor ( eatc_dona_headers .eatc-donation_manager_typology_b ) por lo que trae el campo " eatc_donation_managers. tipo_organizacion " 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 CORRECIN AUTOMTICA PERIDICA TIPOLOGAS DE GESTORESDE DONACIN EN ENCABEZADOS DE ANUNCIOS