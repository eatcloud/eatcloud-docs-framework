# Frontend Standards - EatCloud Modernizado

## 1. Módulos Funcionales - Front Office & Back Office
*Basado en la funcionalidad de Perfil "administrador donante".*

### Flujo: Mapeo y carga masiva de PODs
Esta funcionalidad es exclusiva para el administrador donante que desea cargar PODs masivamente.

**Validación del tipo de licencia:**
Antes de desplegar el formulario, el sistema Frontend debe validar el tipo de licencia del usuario:
- Consultar a la API: `{{URL_entorno_datagov}}/api/eatcloud/eatc_cua?name={{_DOM.cua_user}}&_distinct=type`
- **Licencias Permitidas:** `impactoplus`, `impacto` o `activo`. Si el usuario tiene una de estas licencias, se le permite el paso a la funcionalidad.
- **Licencias Denegadas:** `esencial` o `free`. Si el usuario tiene estas licencias:
  1. El sistema debe realizar una petición POST de tipo "Create" hacia la tabla `eatc_upgrade_events` para registrar el intento.
  2. Una vez hecho el registro, debe redireccionar al usuario a la página de upgrade respectiva: `{{URL_entorno_datagov}}/_dgbo/#!/upgradebyflatfiles`.

### Puntos de donación pendientes por registro de coordenada
- Los puntos cargados preliminarmente no tienen información geográfica y están "Inactivos".
- El Frontend debe mostrar una pestaña o sección "Puntos de donación pendientes por registro de coordenada".
- Al acceder, se debe desplegar el mapa de geolocalización.
- Si el usuario sube ciudad/provincia en la carga plana, el sistema debe ayudar a validar que la coordenada marcada corresponda a los datos precargados para minimizar errores. Una vez validada, el POD se activa y se mueve al listado definitivo.
