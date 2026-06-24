# Data Model & Business Entities - EatCloud Modernizado

## 1. Entidades Principales (Contexto de Donantes y PODs)

### 1.1 `eatc_cua` (Gestión de Licencias y Cuentas)
Estructura que maneja los datos de la cuenta de usuario (Donante).
- **Campos detectados:** `name`, `type`, `eatc_country`, `eatc_cua_master`.
- **Tipos de Licencia (`type`):** `impactoplus`, `impacto`, `activo`, `esencial`, `free`.

### 1.2 `bo_usuarios` (Backoffice Usuarios)
Usuarios administradores de las cuentas.
- **Campos detectados:** `nombre_usuario`, `email`.

### 1.4 Dashboard de Cancelaciones (v1.3)
Estructuras y campos asociados a la generación del mapa interactivo de donaciones canceladas.
- **Campos detectados:** `eatc_destination_lat`, `lon`, `consolidation_destination` (Nombre de la fundación/beneficiario).
- **Interpolación Espacial:** Dado que algunos registros cancelados no guardan el nombre del beneficiario, se aplica interpolación espacial cruzando coordenadas de donaciones exitosas hacia su respectivo `consolidation_destination`.
- `eatc_platform`: Plataforma de origen (ej. `datagov_cuentas`)
- `eatc_upgrade_event`: Evento desencadenante (ej. `upgrade_by_flat_file_upload`)
- `eatc_user`: Email del usuario (`bo_usuarios.email`)
- `eatc_actual_rescue_plan`: Licencia actual del usuario al momento del evento (`eatc_cua.type`)

### 1.4 `file_data_map` (Diccionario de Mapeo)
Tabla unificada para dictar reglas de mapeo de archivos planos (utilizada tanto para productos como para PODs).
- **Campos obligatorios:** Nombre, Descripción, "Mapeo requerido (Booleano)".

### 1.5 PODs (Puntos de Donación)
Representación de sedes o puntos físicos.
- **Estados Lógicos:** 
  - `Inactivo`: Cuando fue cargado vía archivo plano sin coordenadas.
  - `Activo`: Cuando ya cuenta con información geográfica completa (coordenadas, ciudad, provincia, localidad).

### 1.6 `eatc_odds` (Datos de Productos)
Estructura homóloga al mapeo de PODs, pero utilizada para productos.

## 2. Endpoints Estructurales (CRUD API)
Ejemplo de sintaxis del API heredado para la manipulación e inserción de datos transversales:
`{{URL_entorno_datagov}}/crd/eatcloud/?_tabla={NOMBRE_TABLA}&_operacion={insert|update}&campo1=valor1&campo2=valor2`
### 1.3 `eatc_upgrade_events` (Registro de Upgrades)
Auditoría y tracking de usuarios que intentan acceder a funciones premium sin licencia.
- `eatc_datetime`: Timestamp (ej. 2021-09-11 14:43:00)
- `eatc_date`: Fecha (ej. 2021-09-11)
- `eatc_country`: País de la cuenta (`eatc_cua.eatc_country`)
- `eatc_cua_master`: Cuenta maestra (`eatc_cua.eatc_cua_master`)
- `eatc_cua`: Nombre de la cuenta (CUA)
