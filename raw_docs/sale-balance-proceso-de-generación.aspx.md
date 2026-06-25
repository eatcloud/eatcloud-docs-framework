# sale-balance-proceso-de-generación.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 El sistema con un proceso que corra segn lo establecen los datos incorporados aqu&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_sale_balance_timeout ?_id=_* 
&#160; 
 Y cuyos registros debern seguir la misma notacin utilizados por los cronjobs&#58; 
&#160; 
 Minute The minute of each hour at which to run the cron job. For example, enter 15 to run the cron job at 15 minutes past the hour. 
 Hour The hour of each day (in 24-hour format ) at which to run the cron job. For example, enter 2100 to run the cron job at 9&#58;00 PM local time. 
 Day The day of the month on which to run the cron job. For example, enter 15 to run the cron job on the 15th of the month. 
 Month The month of the year in which to run the cron job. For example, enter 7 to run the cron job in July. 
 Weekday The day(s) of the week on which to run the cron job. For example, a value of 0 indicates Sunday, or a value of 6 indicates Saturday. 
&#160; 
 Ejemplo&#58; cuenta maestra &quot;abaco&quot; 
&#160; 
 Dado que la siguiente consulta&#58; 
 https&#58;//datagov.eatcloud.info/api/eatcloud/ eatc_sale_balance_timeout ?_id=_* 
&#160; 
 Arroja este resultado&#58; 
&#160; 
 &#123; 
 _id &#58; &quot;1&quot;, 
 eatc_cua_master &#58; &quot;abaco&quot;, 
 eatc_cua &#58; &quot;&quot;, 
 minute &#58; &quot;&quot;, 
 hour &#58; &quot;23&#58;59&#58;00&quot;, 
 day &#58; &quot;*&quot;, 
 month &#58; &quot;*&quot;, 
 weekday &#58; &quot;5&quot; 
 &#125; 
&#160; 
 Para todas las cuentas cuya cuenta maestra sea &quot;abaco&quot;, el proceso de generacin de balance deber correr a las 11&#58;59 PM los viernes (da 5). 
 En el momento que corra el proceso, el mismo debe&#160; evaluar, para las ofertas cuyo estado ( eatc_sale. eatc-odd_state ) es diferente a &quot; balance &quot; y que no estn bloqueadas&#58; 
&#160; 
 &#123;&#123;URL_entorno_donantes&#125;&#125;/eatcloud/eatc_sale?eatc-odd_state=sale,partially_ordered,ordered,transformed,partially_transformed&amp;blocked=no 
&#160; 
 la fecha y hora actual (para el ejemplo anterior que ser la primera versin de operacin, la fecha de cada viernes a las 23&#58;59&#58;00) , versus la fecha y hora registrada en eatc_sale. eatc-offer _lifetime_ until , si la fecha y hora de ejecucin del proceso de &quot;balance&quot; es posterior a la registrada en eatc_sale. eatc-offer_lifetime_until , y el estado del los detalles&#160; entonces deber proceder a realizar, para conjunto de ofertas realizadas por un mismo eatc_sale. eatc_donor_code el proceso de&#58; 
&#160; 
 Enriquecimiento de informacin de eatc_sale para proceso de balance 
 Este proceso que se detalla aqu , generar una liquidacin (es decir, que generar un cdigo de balance o eatc-sale_balance_header_code ) por cada conjunto de rdenes cuyo eatc_sale. eatc-offer_lifetime_until se haya cumplido ha la hora de hacer el proceso.&#160; Una vez se terminen de enriquecer los datos de eatc_sale con la informacin requerida para el balance se debe generar el siguiente proceso. 
&#160; 
 Creacin de encabezados de balance (eatc_sale_balance_headers)&#160; 
 Este proceso que se detalla aqu , generar las totalizaciones de los detalles eatc_sale con el nimo de establecer los valores a pagar a los diferentes proveedores. 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PROCESO DE GENRACIN DEL BALANCE