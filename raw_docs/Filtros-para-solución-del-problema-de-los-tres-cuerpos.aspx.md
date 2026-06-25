# Filtros-para-solución-del-problema-de-los-tres-cuerpos.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Nota para el desarrollo&#58; 
 La problemática de los tres cuerpos fue una que se derivó de la utilización del campo eatc_donation_managers . organizacion_vinculada &#160; para en algún momento llevar organizaciones en el territorio del banco, pero que no están vinculadas como tal a ellos. &#160; Es por esto que se están haciendo una serie de ajustes para desambiguar esta información, de tal manera que eatc_donation_managers . organizacion_vinculada &#160; queden solamente datos de los NITs de los bancos a los cuales las organizaciones tipo 2 están efectivamente vinculadas, y por otro lado, las organizaciones tipo 3 ya no tendrán información en ese campo. &#160;Para consultarlas el Banco realizará una búsqueda por territorio que en adelante se detalla. &#160;Por eso es que se debe entender en adelante que los tres cuerpos son&#58; 

 El banco de alimentos 

 Sus organizaciones vinculadas (tipologia b&#58; 2) 

 Las organizaciones en su territorio de incidencia (tipo 3) 
&#160; 
 Figma&#58; https&#58;//www.figma.com/design/fz65QCafGLQOjca5ShRzTc/Nubola-Design-System?node-id=3144-4649 &#160; 

Secciones del BO en donde se deberán aplicar estos filtros (seguir el siguiente orden para la implementación) 

Informe de detalle de anuncios&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/bdtlanun &#160; 

Resultados de donaciones&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/bresdonadona &#160; 

Donantes y beneficiarios&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/bresdona &#160; 

Informe de encabezados de anuncios&#58; https&#58;//devbeneficiarios.eatcloud.info/_nbob/#!/bheadanun &#160; 
&#160; 
 Datos de entrada para construir el filtro 
El dato básico que se requiere para la construcción del filtro es el &#123;&#123;identificador_unico_registro&#125;&#125; del banco en cuestión y con este dato se proceden a realizar las consultas necesarias para construir la información 
&#160; 
 Toogle&#58; información Banco de Alimentos 

Posición por defecto&#58;&#160; 
Activada. &#160;No debe dejar desactivarse si no están activados algunos de los dos otros toogles. 
&#160; 
Información para realizar los filtros&#58;&#160; 
Al estar activado quiere decir que está consultando información solamente del banco de alimentos. 

Encabezados de anuncios de donaciones (eatc_dona_headers) 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donation_manager_code= &#123;&#123;identificador_unico_registro&#125;&#125;&amp;_cmp=eatc-code =&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Detalles de anuncios de donaciones (eatc_dona) 
Tomando el &#123;&#123;array_eatc-code&#125;&#125; obtenido en la consulta anterior, se procede a realizar la consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona ?eatc-dona_header_code= &#123;&#123;array_eatc-code&#125;&#125; 
&#160; 
 Toogle&#58; información Adscritas al Banco de Alimentos 

Posición por defecto&#58;&#160; 
Desactivada. &#160;Debe dejar en cualquier momento al usuario cambiar la posición para activarlo. 
&#160; 
Información para realizar los filtros&#58;&#160; 
Al estar activado quiere decir que está consultando información de las organizaciones adscritas al banco de alimentos, por este motivo debe realizar las siguientes consultas. 

Encabezados de anuncios de donaciones (eatc_dona_headers) 
Para poder establecer que encabezados debe consultar, el sistema debe realizar esta consulta a la estructura eatc_donation_managers 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_donation_managers ? organizacion_vinculada = &#123;&#123;identificador_unico_registro&#125;&#125;&amp;_cmp=identificador_unico_registro =&gt; &#123;&#123;array_identificador_unico_registro&#125;&#125; 
Con el &#123;&#123;array_identificador_unico_registro&#125;&#125; obtenido, procede a realizar la siguiente consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donation_manager_code= &#123;&#123;array_identificador_unico_registro&#125;&#125;&amp;_cmp=eatc-code &#160;=&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Construcción del “Filtro por organización” 

Cuando se activa este toogle, el sistema debe construir un filtro de selección múltiple, con opción “seleccionar todo” (que estaría puesto por defecto) y también “des-seleccionar todo”. &#160;Para construir las opciones de este filtro, se deberá obtener el nombre de la organización ( organizacin ) y asociado al código respectivo generar el selector 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_donation_managers ? organizacion_vinculada = &#123;&#123;identificador_unico_registro&#125;&#125;&amp;_cmp=identificador_unico_registro,organizacin 
Al seleccionar una o varias organizaciones ( organizacin ) se construye un &#123;&#123;array_identificador_unico_registro_especifico&#125;&#125; obtenido, procede a realizar la siguiente consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donation_manager_code= &#123;&#123;array_identificador_unico_registro_espeficico&#125;&#125;&amp;_cmp=eatc-code &#160;=&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Detalles de anuncios de donaciones (eatc_dona) 
Tomando el&#160; &#123;&#123;array_eatc-code&#125;&#125; obtenido en la consulta anterior, se procede a realizar la consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona ?eatc-dona_header_code= &#123;&#123;array_eatc-code&#125;&#125; 
&#160; 
 Toogle&#58; información por departamento 

Posición por defecto&#58;&#160; 
Desactivada. &#160;Debe dejar en cualquier momento al usuario cambiar la posición para activarlo. 
&#160; 
Información para realizar los filtros&#58;&#160; 
Al estar activado quiere decir que está consultando información de las organizaciones en el territorio del banco y para construir esta información deberá realizar lo siguiente. 

Encabezados de anuncios de donaciones (eatc_dona_headers) 
Primero se debe establecer en qué territorios (departamentos) tiene cobertura el banco en cuestión, para lo cual el sistema debe realizar esta consulta a la estructura eatc_dona_headers 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donation_manager_code= &#123;&#123;identificador_unico_registro&#125;&#125;&amp;_distinct=eatc-province &#160;=&gt; &#123;&#123;array_eatc-province&#125;&#125; 
Con el array obtenido &#123;&#123;array_eatc-province&#125;&#125;, excluyendo datos vacíos, debe realizar la siguiente consulta&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-province= &#123;&#123;array_eatc-province&#125;&#125;&amp;_cmp=eatc-code &#160;=&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Construcción del “Filtro por departamento” 

Cuando se activa este toogle, el sistema debe construir un filtro de selección múltiple, con opción “seleccionar todo” (que estaría puesto por defecto) y también “des-seleccionar todo”. &#160;Para construir las opciones de este filtro se utilizan las opciones “no vacías” de &#123;&#123;array_eatc-province&#125;&#125; , al seleccionar una o varias opciones se obtiene un &#123;&#123;array_eatc-province_especifico&#125;&#125; que se utiliza para traer la información&#58; 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-province= &#123;&#123;array_eatc-province_especifico&#125;&#125;&amp;_cmp=eatc-code &#160;=&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Re- Construcción del “Filtro por organizaciones” al activar el filtro por departamento 
Si hay una selección en el filtro por departamento, esta selección debe afectar el filtro por organizaciones, para que solamente aparezcan en ese filtro las organizaciones del departamento o los departamentos seleccionados, para eso se determina las organizaciones que tienen donaciones en ese territorio &#58; 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-province= &#123;&#123;array_eatc-province_especifico&#125;&#125;&amp;_distinct= eatc-donation_manager_code =&gt; &#123;&#123;array_eatc-donation_manager_code&#125;&#125; *** Puede incorporar datos vacíos para donaciones del territorio que aun no han sido asignadas*** 
Cuando el sistema para amar el selector se deben consultar los nombres de las organizaciones en el territorio para generar el selector 
&#160; 
 &#123;&#123;URL_beneficiarios&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_donation_managers ? identificador_unico_registro = &#123;&#123;array_eatc-donation_manager_code&#125;&#125;&amp;_cmp=identificador_unico_registro,organizacin 
Al seleccionar una o varias organizaciones ( organizacin ) se construye un &#123;&#123;array_identificador_unico_registro_especifico&#125;&#125; obtenido, procede a realizar la siguiente consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona_headers ?eatc-donation_manager_code= &#123;&#123;array_identificador_unico_registro_espeficico&#125;&#125;&amp;_cmp=eatc-code &#160;=&gt; &#123;&#123;array_eatc-code&#125;&#125; 

Detalles de anuncios de donaciones (eatc_dona) 
Tomando el&#160; &#123;&#123;array_eatc-code&#125;&#125; obtenido en la consulta anterior, se procede a realizar la consulta 
 &#123;&#123;URL_donantes&#125;&#125;/api/&#123;&#123;cua_master&#125;&#125;/ eatc_dona ?eatc-dona_header_code= &#123;&#123;array_eatc-code&#125;&#125; 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-informe-operativo-bo-de-anuncios-de-donaci%C3%B3n-eatc_dona_lst2-nb%281%29%2F1764191628996image.png&ow=1022&oh=279, https://eatcloudcorp.sharepoint.com/_layouts/15/getpreview.ashx?path=%2Fsites%2FEatCloud2%2FSiteAssets%2FSitePages%2Fb-informe-operativo-bo-de-anuncios-de-donaci%C3%B3n-eatc_dona_lst2-nb%281%29%2F1764191628996image.png&ow=1022&oh=279 

 1116.00000000000 
 4c26c60e-2b63-4a55-a94c-f25be2849afe 
 3!1!2 
 https://eastus0-0.pushfp.svc.ms/fluid 
 b72dde2e-c4fb-4654-a164-1fdedd93b6b4 
 2025-11-27T21:00:09.5794704Z 
 EATCLOUD Nuevo BO CUA MASTER 
 {"SessionId":"134204cd-cc98-43cb-85ec-628a9e12c0b5","SequenceId":203,"FluidContainerCustomId":"2a196832-afd1-4fed-8604-dbc5df01345c","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"On"},{"Name":"ZoneThemeIndex","Version":"On"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"HideOn","Version":"On"}] 

 Filtros para solución del problema de los tres cuerpos