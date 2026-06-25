# éxito-sp_after_insert_dona.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Procedimiento almacenado que se dispara cuando el archivo de exito que alimenta a exito.eatc_dona termina su proceso de carga. 

 after_insert_dona() 
 begin 
 &#160;delete from eatc_dona wehre destino &lt;&gt; trim('04'); 
 &#160;delete from eatc_dona wehre signo &lt;&gt; trim('-'); 
 &#160;delete from eatc_dona wehre sublinea in trim('021','042','051','052','053','65','501','505'); 
 &#160;update eatc_dona set cantidad=round(cantidad/100, 2) where date(fechadocumento) =&#160; DATE_ADD(CURDATE(),INTERVAL -1 DAY); 
 end 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 XITO: SP_AFTER_INSERT_DONA