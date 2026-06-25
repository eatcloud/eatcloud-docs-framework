# pacadi-escritura-de-turnos-en-eatc_donation_managers.aspx

0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Contexto general 
 BAMX nos entregar diariamente una extraccin de los turnos PACADI en un SFTP que EatCloud habilitar para ello. A partir de esta informacin el presente proceso escribir un ordinal que empezar en 1, en cuatro campos diferentes, para todos los Bancos de Alimentos adscritos a BAMX, segn las indicaciones que se brindan a continuacin (para ello se mont una muestra del archivo al entorno beneficiario con el objetivo de mostrar con las APIs las consultas que se debern realizar para escribir el ordinal respectivo) 
&#160; 
 Bancos auditados por Nestl 
 Para la realizacin del piloto con Nestl, se debe tener en cuenta que dicha compaa solamente dona a Bancos de Alimentos de la red BAMX que han pasado un proceso de auditora conducido por ellos.&#160; Para identificar los bancos que han pasado dicha auditora, se crear un nuevo campo boleano en la tabla eatc_donation_managers que indicar eso, a saber&#58;&#160; eatc_donation_managers. eatc_audited_by_nestle =y .&#160; A continuacin se presenta la lista que entreg en primera instancia BAMX de bancos auditados por Nestl. 
&#160; 
 Listado de Bancos auditados por Nestl 
 Nombre &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; idBanco&#160; 
 BAMX GUADALAJARA &#160; &#160;34&#160; 
 BAMX HERMOSILLO &#160; &#160; &#160; 25&#160; 
 BAMX LEN &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;35&#160; 
 BAMX NUEVO LEN &#160; &#160; &#160; 39&#160; 
 BAMX PUEBLA &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;63&#160; 
 BAMX QUERTARO &#160; &#160; &#160; &#160; 8&#160; 
 BAMX SAN CRISTBAL &#160; 47&#160; 
 BAMX TAPACHULA &#160; &#160; &#160; &#160; 2&#160; 
 BAMX TIJUANA &#160; &#160; &#160; &#160; &#160; &#160; &#160; 24&#160; 
 BAMX TUXTLA &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;40&#160; 
 BAMX VERACRUZ &#160; &#160; &#160; &#160; &#160; 64 
 BAMX XALAPA &#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160;30&#160; 
 BAMX ZAPOTLANEJO &#160; &#160; 50&#160; 
&#160; 
 Turnos PACADI para Nestl 
&#160; 
 La consulta para construir los ordinales aplicables a Nestl (dos en total&#58; para anuncios menores a 1 tonelada y para anuncios mayores a una tonelada), como primer paso, se saca un array de los &quot;identificadores&quot; de los bancos que estn auditados por Nestl de la siguiente manera. 
&#160; 
 &#123;&#123; array_idBancos_auditados_nestle &#125;&#125;=&#123;&#123;url_entorno_beneficiarios&#125;&#125;/api/mexico/eatc_donation_managers? eatc_audited_by_nestle =y&amp;_cmp= identificador 
&#160; 
 Cuando se suba la informacin que nos entreg en primera instancia BAMX ( listado de bancos auditados por Nestl ), se entiende que la respuesta ser la siguiente&#58; 
&#160; 
 &#123;&#123; array_idBancos_auditados_nestle &#125;&#125;= 34,25,35,39,63,8,47,2,24,40,64,30,50 

&#160; 
 eatc_donation_managers .eatc_pacadi_nestle_turn_under_1_ton 
&#160; 
 En este campo se escribir el orden de los bancos que estn auditados por Nestl y que vienen ordenados en extraccin respectiva, sin hacer ninguna excepcin adicional.&#160;&#160; 
&#160; 
 Con el array de bancos auditados por Nestl se filtra la informacin de la tabla de turnos, de la siguiente manera (tomando como ejemplo la informacin subida en productivo)&#58; 
 https&#58;//donantes.eatcloud.info/api/mexico/turnos_pacadi?idbanco=34,25,35,39,63,8,47,2,24,40,64,30,50&amp;_cmp= turno,idbanco&amp; _orderby= turno&amp; _ordertype=asc &#160; 
&#160; 
 La lista obtenida (para el ejemplo anterior)&#160; se le agrega un ordinal que empiece en 1 y termine en 13 (para el ejemplo particular), ordenando con el nmero 1 al nmero de menor valor que aparece en el parmetro turno, colocndole el ordinal 2 al nmero de valor inmediatamente mayor y continuando as hasta el ordinal 13 que se le colocara al nmero con mayor valor de la lista.&#160; Con estos ordinales, el sistema realiza el siguiente update de informacin en la tabla eatc_donation_managers &#58; 
&#160; 
 &#123;&#123;url_entorno_beneficiarios&#125;&#125;/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp;eatc_pacadi_nestle_turn_under_1_ton =&#123;&#123; ordinal &#125;&#125;&amp;WHERE identificador=&#123;&#123; turnos_pacadi .turnos&#125;&#125; 
&#160; 
 eatc_donation_managers .eatc_pacadi_nestle_turn_over_1_ton 
&#160; 
 En este campo se escribir el orden de los bancos que estn auditados por Nestl y que vienen ordenados en extraccin respectiva,&#160; quitando aquellos bancos que estn bloqueados, es decir que tienen en el campo &quot; snbloqueado &quot; como valor &quot;1&quot;.&#160;&#160; 
&#160; 
 Con el array de bancos auditados por Nestl se filtra la informacin de la tabla de turnos, de la siguiente manera (tomando como ejemplo la informacin subida en productivo)&#58; 
 https&#58;//donantes.eatcloud.info/api/mexico/turnos_pacadi?idbanco=34,25,35,39,63,8,47,2,24,40,64,30,50&amp; snbloqueado = ! 1&amp;_cmp= turno,idbanco&amp; _orderby= turno&amp; _ordertype=asc &#160; 
&#160; 
 La lista obtenida (para el ejemplo anterior) se le agrega un ordinal que empiece en 1 y termine en 11 (para el ejemplo particular), ordenando con el nmero 1 al nmero de menor valor que aparece en el parmetro turno, colocndole el ordinal 2 al nmero de valor inmediatamente mayor y continuando as hasta el ordinal 13 que se le colocara al nmero con mayor valor de la lista.&#160; Con estos ordinales, el sistema realiza el siguiente update de informacin en la tabla eatc_donation_managers &#58; 
&#160; 
 &#123;&#123;url_entorno_beneficiarios&#125;&#125;/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp;eatc_pacadi_nestle_turn_over_1_ton =&#123;&#123; ordinal &#125;&#125;&amp;WHERE identificador=&#123;&#123; turnos_pacadi .turnos&#125;&#125; 

 *** NUEVO&#58; TURNOS POR REGIONES *** 
&#160; 
 Se deber clasificar al interior de cada una de las regiones de los bancos registrados en la plataforma, el ordenamiento pacadi, al interior de la misma, esto con el fin de tener turnos cercanos por regiones, independientemente que los turnos generales sean muy altos. 
&#160; 
 Establecimiento de las regiones&#58; 
&#160; 
 Para establecer las regiones, para las cuales debe haber una clasificacin especfica de turnos, se podr realizar la siguiente consulta&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?_id=_*&amp;_distinct=eatc_region 
&#160; 
 Ejemplo&#58; ambiente productivo cuenta maestra mexico 
 https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_donation_managers?_id=_*&amp;_distinct=eatc_region &#160; 
&#160; 
 El sistema responde de la siguiente manera&#58; 
 &#123; 
 eatc_region &#58; &quot;&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;noreste&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;occidente&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;bajio&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;centrosur&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;noroeste&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;suristmo&quot; 
 &#125;, 
 &#123; 
 eatc_region &#58; &quot;pacifico&quot; 
 &#125; 
&#160; 
 Por lo tanto se tendr que realizar una clasificacin individual de turnos pacadi para cada una de estas regiones (incluyendo la &quot;vaca&quot;) como se detalla a continuacin (teniendo como base si ya el proceso de clasificacin de turnos pacadi original ya corri y tenemos clasificaciones en las primeras cuatro clasificaciones de PACADI 
&#160; 
 eatc_pacadi_region_turn_under_1_ton 
&#160; 
 Para cada regin con la cual responde el anterior llamado el sistema deber realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?eatc_region=&#123;&#123;eatc_donation_managers. eatc_region &#125;&#125;&amp;_cmp= identificador_unico_registro,eatc_pacadi_turn_under_1_ton 
&#160; 
 De acuerdo a la respuesta, el sistema ordena y registra en el parmetro&#160; eatc_donation_managers. eatc_pacadi_region_turn_under_1_ton un ordinal nuevo, siendo el &quot;1&quot;, el primer turno que aparece en la consulta, 2 el segundo, 3 el tercero, y as sucesivamente (lo que se procura aqu es que los&#160; 
&#160; 
 Ejemplo&#58; ambiente de produccin, regin &quot;occidente&quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_donation_managers?eatc_region=occidente&amp;_cmp= identificador_unico_registro,eatc_pacadi_turn_under_1_ton &#160; 
&#160; 
 Dado que el sistema responde as&#58; 
 &#123; 
 identificador_unico_registro &#58; &quot; BAZ091005GZ7 &quot;, 
 eatc_pacadi_turn_under_1_ton &#58; &quot;12&quot; 
 &#125;, 
 &#123; 
 identificador_unico_registro &#58; &quot; BDA9205064S1 &quot;, 
 eatc_pacadi_turn_under_1_ton &#58; &quot;32&quot; 
 &#125; 
&#160; 
 Entonces el sistema realizar estos registros&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_region_turn_under_1_ton= 1 &amp;WHERE identificador_unico_registro= BAZ091005GZ7 &#160; 
&#160; 
 y 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_region_turn_under_1_ton= 2 &amp;WHERE identificador_unico_registro= BDA9205064S1 &#160; 
&#160; 
 NOTA para revisin de datos &#58; Revisar bien la clasificacin original, que se intuye que puede tener algn tipo de error (dado que en todas las otras clasificaciones ( eatc_pacadi_turn_over_1_ton , eatc_pacadi_nestle_turn_under_1_ton , eatc_pacadi_nestle_turn_over_1_ton ) siempre el banco con cdigo BAZ091005GZ7 est en un turno por encima del del banco BDA9205064S1 cosa que no ocurre en este caso ( BAZ091005GZ7 tiene un turno inferior que BDA9205064S1 ).&#160; Se entiende que si la fuente original para realizar el ordenamiento es una, en todos los ordenamientos el banco que aparezca con un orden inferior en el archivo de PACADI, deber aparecer en todos los ordenamientos con el mismo &quot;turno&quot; y no se entendera porqu en uno aparece antes y en los otros despus).&#160; Para efectos del ejemplo, es til que salga como sali, porque ayuda a entender la naturaleza del ordenamiento al interior de cada regin (como si fueran ejemplos separados). 

&#160; 
 eatc_pacadi_region_turn_over_1_ton 
&#160; 
 Para cada regin con la cual responde el anterior llamado el sistema deber realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?eatc_region=&#123;&#123;eatc_donation_managers. eatc_region &#125;&#125;&amp;_cmp= identificador_unico_registro,eatc_pacadi_turn_over_1_ton 
&#160; 
 De acuerdo a la respuesta, el sistema ordena y registra en el parmetro&#160; eatc_donation_managers. eatc_pacadi_region_turn_over_1_ton un ordinal nuevo, siendo el &quot;1&quot;, el primer turno que aparece en la consulta, 2 el segundo, 3 el tercero, y as sucesivamente (lo que se procura aqu es que los&#160; 
&#160; 
 Ejemplo&#58; ambiente de produccin, regin &quot;occidente&quot; 
&#160; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_donation_managers?eatc_region=occidente&amp;_cmp= identificador_unico_registro,eatc_pacadi_turn_over_1_ton &#160;&#160; 
&#160; 
 Dado que el sistema responde as&#58; 
&#160; 
 &#123; 
 identificador_unico_registro &#58; &quot; BAZ091005GZ7 &quot;, 
 eatc_pacadi_turn_over_1_ton &#58; &quot;49&quot; 
 &#125;, 
 &#123; 
 identificador_unico_registro &#58; &quot; BDA9205064S1 &quot;, 
 eatc_pacadi_turn_over_1_ton &#58; &quot;29&quot; 
 &#125; 
&#160; 
 Entonces el sistema realizar estos registros&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_region_turn_over_1_ton= 2 &amp;WHERE identificador_unico_registro= BAZ091005GZ7 &#160; 
&#160; 
 y 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_region_turn_over_1_ton= 1 &amp;WHERE identificador_unico_registro= BDA9205064S1&#160; 

&#160; 
 eatc_pacadi_nestle_region_turn_under_1_ton 
&#160; 
 Para cada regin con la cual responde el anterior llamado el sistema deber realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?eatc_region=&#123;&#123;eatc_donation_managers. eatc_region &#125;&#125;&amp;_cmp= identificador_unico_registro,eatc_pacadi_nestle_turn_under_1_ton 
&#160; 
 De acuerdo a la respuesta, el sistema ordena y registra en el parmetro&#160; eatc_donation_managers. eatc_pacadi_nestle_region_turn_under_1_ton un ordinal nuevo, siendo el &quot;1&quot;, el primer turno que aparece en la consulta, 2 el segundo, 3 el tercero, y as sucesivamente (lo que se procura aqu es que los&#160; 
&#160; 
 Ejemplo&#58; ambiente de produccin, regin &quot;occidente&quot; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_donation_managers?eatc_region=occidente&amp;_cmp= identificador_unico_registro,eatc_pacadi_nestle_turn_under_1_ton &#160;&#160; 
&#160; 
 Dado que el sistema responde as&#58; 
 &#123; 
 identificador_unico_registro &#58; &quot; BAZ091005GZ7 &quot;, 
 eatc_pacadi_nestle_turn_under_1_ton &#58; &quot;12&quot; 
 &#125;, 
 &#123; 
 identificador_unico_registro &#58; &quot; BDA9205064S1 &quot;, 
 eatc_pacadi_nestle_turn_under_1_ton &#58; &quot;8&quot; 
 &#125; 
&#160; 
 Entonces el sistema realizar estos registros&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_nestle_region_turn_under_1_ton= 2 &amp;WHERE identificador_unico_registro= BAZ091005GZ7&#160; 
&#160; 
 y 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_nestle_region_turn_under_1_ton= 1 &amp;WHERE identificador_unico_registro= BDA9205064S1 

&#160; 
 eatc_pacadi_nestle_region_turn_over_1_ton 
&#160; 
 Para cada regin con la cual responde el anterior llamado el sistema deber realizar el siguiente llamado&#58; 
 &#123;&#123;URL_entorno_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/eatc_donation_managers?eatc_region=&#123;&#123;eatc_donation_managers. eatc_region &#125;&#125;&amp;_cmp= identificador_unico_registro,eatc_pacadi_nestle_turn_over_1_ton 
&#160; 
 De acuerdo a la respuesta, el sistema ordena y registra en el parmetro&#160; eatc_donation_managers. eatc_pacadi_nestle_region_turn_over_1_ton un ordinal nuevo, siendo el &quot;1&quot;, el primer turno que aparece en la consulta, 2 el segundo, 3 el tercero, y as sucesivamente (lo que se procura aqu es que los&#160; 
&#160; 
 Ejemplo&#58; ambiente de produccin, regin &quot;occidente&quot; 
 El sistema realiza la siguiente consulta&#58; 
 https&#58;//beneficiarios.eatcloud.info/api/mexico/eatc_donation_managers?eatc_region=occidente&amp;_cmp= identificador_unico_registro,eatc_pacadi_nestle_turn_over_1_ton &#160;&#160;&#160; 
&#160; 
 Dado que el sistema responde as&#58; 
 &#123; 
 identificador_unico_registro &#58; &quot; BAZ091005GZ7 &quot;, 
 eatc_pacadi_nestle_turn_over_1_ton &#58; &quot;13&quot; 
 &#125;, 
 &#123; 
 identificador_unico_registro &#58; &quot; BDA9205064S1 &quot;, 
 eatc_pacadi_nestle_turn_over_1_ton &#58; &quot;8&quot; 
 &#125; 
&#160; 
 Entonces el sistema realizar estos registros&#58; 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_nestle_region_turn_over_1_ton= 2 &amp;WHERE identificador_unico_registro= BAZ091005GZ7&#160; 
&#160; 
 y 
&#160; 
 https&#58;//beneficiarios.eatcloud.info/crd/mexico/?_tabla=eatc_donation_managers&amp;_operacion=update&amp; eatc_pacadi_nestle_region_turn_over_1_ton= 1 &amp;WHERE identificador_unico_registro= BDA9205064S1&#160; 

 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 PACADI: ESCRITURA DE TURNOS EN EATC_DONATION_MANAGERS