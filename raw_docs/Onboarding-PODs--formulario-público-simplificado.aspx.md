# Onboarding-PODs--formulario-público-simplificado.aspx

﻿ 

 0x0101009D1CB255DA76424F860D91F20E6C411800C12E4AF3524183439921C4A8ABBCA98F 
 Article 

 Descripción general 
En la actualidad, el formulario de creación de PODs se despliega al interior del BO Donantes Modernizado. &#160;Para la activación de plataformas en emergencias es necesario desplegar un formulario online que pueda ser consultado por el público en general y con ello poder dar de alta puntos de donación por fuera del BO de donaciones. 
&#160; 
 Configuración del formulario público&#58; 
El formulario público deberá tener los siguientes parámetros de configuración. &#160;Esta configuración la debe realizar personal de EatCloud, y una vez realizada, el sistema deberá arrojar una URL pública única que contenga esta información y despliegue el mismo formulario de ONB de Pods (con algunas simplificaciones), para ser operado por el público&#58; 
Llamado a la acción (título del formulario)&#58; =&gt; Obligatorio 
Permitirá incluirle al formulario un título que sea llamativo e invite a la acción 
Descripción del llamado a la acción&#58; =&gt; Obligatorio 
Permitirá la redacción de un párrafo que se desplegará al inicio del formulario que explicará a los usuarios el propósito del mismo. 
&#160; 
Mensaje de agradecimiento&#58; =&gt; Obligatorio 
Permitirá la redacción de un párrafo que se desplegará cuando el usuario complete el registro. &#160;Idealmente este apartado deberá permitir la incorporación de código HTML, permitiendo el enlace a línks externos la incorporación por ejemplo de videos. 
&#160; 
 cua_master &#58; =&gt; Obligatorio 
Cuenta maestra mediante la cual se gestionan las donaciones de los puntos que se crean mediante el formulario desplegado. &#160;Todo POD creado por este formulario en particular, tendrá registrada dicha cuenta maestra. 
&#160; 
 cua_user &#58; =&gt; Obligatorio 
Cuenta usuario mediante la cual se gestionan las donaciones de los puntos que se crean mediante el formulario desplegado. &#160;Todo POD creado por este formulario en particular, tendrá registrada dicha cuenta usuario. 
&#160; 
 Proyecto especial &#58; =&gt; Opcional 
Se podrá elegir un proyecto especial al cual pertenezca el POD y estará registrado en el campo respectivo del maestro (en legacy era&#58; eatc_pods. eatc_special_project &#58; &#160; https&#58;//donantes.eatcloud.info/api/allpods/eatc_pods?_id=_*&amp;_distinct=eatc_special_project) .&#160; 
&#160; 
 Donaciones certificables (SI / NO) =&gt; Obligatorio 
Se debe desplegar un selector único, para establecer si las donaciones creadas desde los puntos de donación, si el usuario selecciona si, durante el proceso de registro del pod, no se realizará ninguna acción adicional. &#160;Si el usuario escoge la opción “no”, entonces, &#160;se deberá permitir la captura de dos datos adicionales (que serán opcionales)&#58; 

 Identificador de la entidad certificadora&#58; 

 Nombre de la entidad certificadora&#58; 
Si no se registra información en estos dos campos, entonces no se llevará información al siguiente registro. 
A la hora de crear el punto, el sistema deberá realizar la siguiente escritura, de acuerdo a los datos de configuración del formulario anteriormente descritos y el código del punto de donación que se genera para su creación&#58; 
 &#123;&#123;URL_datagov&#125;&#125;/crd/eatcloud/?_tabla= eatc_doma_certification ?&amp;_operacion=insert&amp;eatc_cua_master=&#123;&#123; cua_master &#125;&#125; &amp;eatc_cua_user=&#123;&#123; cua_user &#125;&#125;&amp; eatc_pod_id =&#123;&#123; pod_id &#125;&#125; &amp; eatc_certifying_doma_id =&#123;&#123; Identificador de la entidad certificadora &#125;&#125; &amp; eatc_certifying_doma_name =&#123;&#123; Nombre de la entidad certificadora &#125;&#125; 
&#160; 
&#160; Formulario simplificado&#58; 
El formulario se debe basar en la implementación del formulario oficial de creación de PODs, pero deberá simplificarse al máximo según instrucciones entregadas por Isis Espitia. &#160;En general, campos como clasificación de PODs y temas muy puntuales utilizados para la operación de EatCloud deberán suprimirse, mientras que la identificación básica del punto y su responsable, los datos de login, y los datos geográficos del Punto de donación solamente. 

 [{"UserId":12,"DisplayName":"Juan David Correa","LoginName":"juan.correa@eatcloud.com"}] 
 b6917cb1-93a0-4b97-a84d-7cf49975d4ec 

 https://eatcloudcorp.sharepoint.com/_layouts/15/images/sitepagethumbnail.png, /_layouts/15/images/sitepagethumbnail.png 

 a977ef1f-6998-4512-94d2-4399fab11bb2 
 1!1!2 
 https://eastus0-2.pushfp.svc.ms/fluid 
 7529b90e-e17d-40fa-ac05-432ffe0afb69 
 2025-05-01T00:17:18.5901421Z 

 {"SessionId":"e3e927ad-95e2-49c7-be10-d42c655ee151","SequenceId":1075,"FluidContainerCustomId":"918d401f-9f26-44c1-bbd6-4ee75defc72c","IsSingleUserSession":true,"ClientOperation":4,"RestoreTo":"","RestoredFrom":""} 
 [{"Name":"PagesFluidVersion","Version":"2.12"},{"Name":"AppType","Version":"Pages"},{"Name":"ZoneReflowStrategy","Version":"Off"},{"Name":"OptionalTitleRegion","Version":"On"},{"Name":"SharedTreeV2","Version":"On"},{"Name":"ZoneThemeIndex","Version":"Off"},{"Name":"DynamicContent","Version":"Off"},{"Name":"AIContextStore","Version":"Off"},{"Name":"CanvasPlaceholderSchema","Version":"Off"}] 

 Onboarding PODs: formulario público simplificado