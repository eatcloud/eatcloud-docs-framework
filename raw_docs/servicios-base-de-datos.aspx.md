# servicios-base-de-datos.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Se han disponibilizado servicios web, que permiten realizar trabajos sobre la base de datos, como incorporar, renombrar o borrar campos, eliminar tablas, etc. 
&#160; 
 Estos servicios requieren de autenticacin para poder ser consumidos&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;CUA&#125;&#125;/&#123;&#123;nombre_servicio&#125;&#125;?_tabla=&#123;&#123;tabla&#125;&#125; 
&#160; 
 A continuacin los casos implementados hasta el momento&#58; 
&#160; 
 Para acceder se requieren las siguientes credenciales&#58; 
&#160; 
 US&#58; eatcloud 
&#160; 
 PS&#58; nzzn;4118869;eatc 

 Creacin de Object Store ( casedb ) 
 Este servicio que tiene la misma naturaleza de los dems servicios aqu creados, se cre como un casedb por eso se debe consultar aqu 

 Renombrar campos 
 Para qu sirve&#58; 
 Para renombrar un campo de una tabla especfica 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/renamecampo?_tabla=&#123;&#123;tabla_a_la_que_pertenece_el_campo&#125;&#125;&amp;new_field=&#123;&#123;nuevo_mombre_del_campo&#125;&#125;&amp;old_field=&#123;&#123;campo_que_se_renombra&#125;&#125; 

 Adicionar campos 
 Para qu sirve&#58; 
 Para adicionar un campo de una tabla especfica 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/newcampo?_tabla=&#123;&#123;tabla_a_la_que_se_adiciona_el_campo&#125;&#125;&amp;new_field=&#123;&#123;mombre_del_campo_nuevo&#125;&#125; 
&#160; 
 Nueva documentacin&#58; 
 https&#58;//documenter.getpostman.com/view/5936058/2s93z9c3Hs 

 Adicionar campos a mltiples tablas 
 Para qu sirve&#58; 
 Para adicionar un campo a mltiples tablas (por ejemplo de cuentas maestras diferentes) 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/newfield 
&#160; 
 Nueva documentacin&#58; 
 https&#58;//documenter.getpostman.com/view/5936058/2s946eADqF &#160; 

 Quitar campos 
 Para qu sirve&#58; 
 Para adicionar un campo a mltiples tablas (por ejemplo de cuentas maestras diferentes) 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/dropfield 
&#160; 
 Nueva documentacin&#58; 
 https&#58;//documenter.getpostman.com/view/5936058/2s946eADqF &#160; 

 Quitar campos 
 Para qu sirve&#58; 
 Para renombrar un campo de una tabla especfica 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/dropcampo?_tabla=&#123;&#123;tabla_a_la_que_pertenece_el_campo&#125;&#125;&amp;field=&#123;&#123;mombre_del_campo_a_quitar&#125;&#125; 

 Borrado de tablas 
 Para qu sirve&#58; 
 Para borrar por completo una tabla que se ha creado en la base de datos 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123;cua_user&#125;&#125;/droptable?_tabla=&#123;&#123;tabla_a_borrar&#125;&#125; 

 [NUEVO] Borrado de base de datos (object store) 
 Para qu sirve&#58; 
 Para borrar por completo una base de datos, diferentes a eatcloud y las cuentas maestras 

&#160; 
 URL del servicio&#58; 
 &#123;&#123;URL_entorno&#125;&#125;/optb/&#123;&#123; cua_user &#125;&#125;/dropbdd&amp;_token=&#123;&#123;token_autorizacion&#125;&#125; 

&#160; 
 IMPORTANTE &#58; prohibicin de borrado de bases de datos de cuentas maestras e eatcloud. 
 Este servicio no debe poderse efectuar en las tablas propias de las cuentas maestras ( abaco, mexico, argentina, esp ) y en las tablas propias de eatcloud (como medida de precaucin ), es decir, si en &#123;&#123; cua_user &#125;&#125; se recibe cualquiera de los nombres de las cuentas maestras (ejemplo entorno productivo&#58; https&#58;//datagov.eatcloud.info/api/eatcloud/eatc_cua_master?eatc_country=_*&amp;_cmp=eatc_cua ) o &quot; eatcloud &quot;, se debe responder con un &quot;forbbiden&quot; y no realizar ningn borrado 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 SERVICIOS DE CASOS SOBRE LA BASE DE DATOS - OPTB