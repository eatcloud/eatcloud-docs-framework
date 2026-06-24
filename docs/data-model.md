# Data Model & Business Entities - EatCloud Modernizado

## 1. Mapeo y Carga de Datos (Puntos de Donación - PODs)

### `eatc_upgrade_events`
Estructura reservada para registrar eventos de upgrade cuando un usuario intenta acceder a funcionalidades premium (como carga masiva de PODs) sin tener una licencia válida.
La estructura de este registro debe ser:
- `eatc_datetime`: Timestamp en formato `AAAA-MM-DD HH:MM:SS`
- `eatc_date`: Datestamp en formato `AAAA-MM-DD`
- `eatc_country`: País, obtenido de `eatc_cua.eatc_country`
- `eatc_cua_master`: Cuenta máster, obtenida de `eatc_cua.eatc_cua_master`
- `eatc_cua`: Nombre de la cuenta
- `eatc_platform`: Ejemplo `datagov_cuentas`
- `eatc_upgrade_event`: Ejemplo `upgrade_by_flat_file_upload`
- `eatc_user`: Email del usuario, obtenido de `bo_usuarios.email`
- `eatc_actual_rescue_plan`: Licencia actual del usuario (obtenida de `eatc_cua.type`)

### Carga Preliminar de PODs (file_data_map)
- La carga masiva inicial de puntos de donación genera PODs en estado **"Inactivo"**.
- La estructura de unión entre la carga de datos y el mapeo es `file_data_map`. Esta tabla de mapeo debe incorporar: nombre, descripción y la indicación de si es necesario mapearlo o no para cada campo.
- Posteriormente se requiere un proceso para geolocalizar estos puntos (asignar coordenadas, provincia, ciudad) antes de pasarlos a estado Activo.
