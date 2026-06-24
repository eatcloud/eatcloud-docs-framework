# Frontend Standards - EatCloud Modernizado

## 1. Tecnologías Base
- **Aplicaciones Web:** React
- **Aplicaciones Móviles:** React Native

## 2. Lógica de Interfaz y Flujos de Usuario (Business Flows)

### Flujo de Carga Masiva de PODs (Puntos de Donación)
Este flujo aplica exclusivamente al perfil **Administrador Donante** (anteriormente `datagov_cuentas`).

**1. Validación de Licencia:**
Antes de mostrar el formulario de carga masiva de PODs, la interfaz debe consultar el tipo de licencia del usuario:
- **Licencias válidas:** `impactoplus`, `impacto`, `activo` ➔ Permiten acceder a la funcionalidad.
- **Licencias no válidas:** `esencial`, `free` ➔ Se debe bloquear el acceso, registrar el evento de upgrade en backend, y luego redireccionar a `{{URL_entorno_datagov}}/_dgbo/#!/upgradebyflatfiles`.

**2. Mapeo Preliminar (Archivos Planos):**
- La interfaz debe permitir cargar un archivo plano con información **no geográfica** del punto de donación (POD).
- Se debe utilizar la estructura de base de datos `file_data_map` para determinar y validar qué campos son obligatorios.
- Los PODs cargados en esta fase se guardan con estado **"Inactivo"**.

**3. Mapeo Geográfico (UI de Mapas):**
- Debe existir una pestaña/sección llamada *"Puntos de donación pendientes por registro de coordenada"*.
- Al seleccionar un punto pendiente, se desplegará un **Mapa de Geolocalización**.
- El usuario ubicará el pin en el mapa para extraer las coordenadas. 
- *Validación UI:* Si la interfaz pidió datos de provincia/ciudad en la carga preliminar, debe cruzar esos datos con la respuesta de la API geográfica (basada en el pin del mapa). Si hay discrepancia, se debe mostrar una **Alerta de Confirmación** al usuario para minimizar errores.
- Una vez registrada la coordenada y obtenidos los datos geográficos (provincia, ciudad, localidad), el POD pasa a estado **"Activo"** y se mueve a la lista oficial de puntos de donación del donante.

## 3. Experiencia de Usuario (SaaS)
- Al ser una plataforma SaaS, las pantallas de bloqueo o "Upgrade" deben ser claras y ofrecer valor, explicando por qué una funcionalidad requiere una licencia superior.
- Todos los formularios de carga de archivos planos (`flat_file_upload`) deben mostrar indicadores de progreso y validación de campos obligatorios antes de enviar datos al servidor.

### 3. Visualización de Datos y Dashboards
Reglas específicas para la creación de mapas interactivos y dashboards en el Frontend.

**1. Dashboard de Cancelaciones:**
- **Marcadores:** Utilizar marcadores azules para Beneficiarios Activos y marcadores en rojo (semáforo) para Puntos de Riesgo (cancelaciones).
- **Interacción:** Los popups del mapa deben incluir un botón tipo "acordeón" que despliegue la "Causa de Rechazo".
- **Superposición:** Asegurar la correcta superposición y clustering de marcadores cuando existan múltiples puntos en una misma área geográfica.
