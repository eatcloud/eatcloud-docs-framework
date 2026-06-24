# Backend Standards - EatCloud Modernizado

## 1. Introducción y Arquitectura Base
Este backend está desarrollado en **Node.js** y forma parte del proyecto de modernización de EatCloud. Está diseñado para manejar grandes volúmenes de datos mediante consultas optimizadas y un robusto conjunto de endpoints.

### Entornos de Despliegue (`{{ENTORNO}}`)
- **Desarrollo (Pruebas e implementación):** `https://devservice.eatcloud.info`
- **Producción (Operaciones en vivo):** `https://service.eatcloud.info`

## 2. Tecnologías y Dependencias Principales
- **Framework Core:** Node.js con Express (Manejo de peticiones HTTP).
- **ORM:** Sequelize (Interacción con base de datos SQL).
- **Autenticación:** JWT (JSON Web Tokens).
- **Otras dependencias:** Dotenv (Variables de entorno), Cors (Políticas de acceso).

## 3. Estructura del Proyecto (Carpetas)
El proyecto debe adherirse estrictamente a esta organización arquitectónica:
- `config/`: Configuración de la base de datos y variables de entorno.
- `handlers/`: Lógica para manejar las peticiones HTTP (Controladores).
- `middlewares/`: Validaciones, seguridad y manejo centralizado de errores.
- `models/`: Definición de los modelos de base de datos usando Sequelize.
- `routers/`: Definición de las rutas y endpoints (conexión con handlers).
- `utils/`: Funciones reutilizables y helpers genéricos.

## 4. Endpoints y Colecciones (Estructura Lógica)
Las funcionalidades están agrupadas por dominio lógico:
- **auth:** Manejo de login, registro, cambios de contraseña y emisión de tokens con JWT.
- **users:** CRUD de usuarios.
- **crd (Operaciones CRUD generales):** Funciones principales y transversales (Crear, actualizar, encriptar, eliminar y desactivar).
- **api / apipub:** Funciones de consulta para tablas públicas, privadas y encriptadas.

## 5. Reglas Generales de Consultas API
Las peticiones a la API se dividen en categorías principales. Soportan los parámetros personalizados de EatCloud para optimización de consultas:
- `_limit` y `_offset`: Paginación.
- `_cmp`: Operaciones de comparación / selección de campos.
- `_count`: Conteo total de registros.
- `_null`: Filtros de valores nulos.
- `_cache`: Manejo de caché en la consulta.

### 5.1 Consultas Privadas (Requieren Token JWT)
- **Ruta de Autenticación:** Se debe enviar un `POST` a `{{ENTORNO}}/auth/login` para obtener el JWT.
- **Uso del Token:** El token obtenido se debe enviar en la cabecera `Authorization: Bearer <token>`.
- **Sintaxis de la ruta base:** `{{ENTORNO}}/api/{{table_name}}`
- **Ejemplo de consulta con parámetros:**
  `{{ENTORNO}}/api/{{table_name}}?name=eatcloud&_limit=5&_offset=8&code=_lktest_lk&_cmp=code,name,cua_user`

### 5.2 Consultas Públicas (No requieren Token)
- **Sintaxis de la ruta base:** `{{ENTORNO}}/apipub/{{table_name}}`
- **Uso:** Soportan exactamente los mismos parámetros de búsqueda (`_limit`, `_offset`, etc.) pero están abiertas y no exigen cabecera de autenticación.

### 5.3 Consultas CRD (Manipulación de Datos)
Las operaciones de mutación deben ejecutarse a través del endpoint dinámico de CRD. **Todas son peticiones POST** y requieren token privado.

1. **Crear Registros (Create):**
   - **Ruta:** `POST {{ENTORNO}}/crd/create/{{table_name}}`
   - **Payload:** Soporta creación masiva. Debe incluir el objeto o array dentro de la propiedad `"data"`.
   - **Encriptación en creación:** Si se requiere encriptar un campo antes de guardar, incluir la propiedad `"encrypt": "nombre_del_campo"` en el body.
2. **Actualizar Registros (Update):**
   - **Ruta normal:** `POST {{ENTORNO}}/crd/update/{{table_name}}/{{query.params}}`
   - **Ruta con encriptación:** `POST {{ENTORNO}}/crd/encrypt/update/{{table_name}}/{{query.params}}`
   - **Manejo del WHERE:** Los `{{query.params}}` (ej. `?name=eatcloud`) actúan como la cláusula WHERE para filtrar qué registros se actualizarán. El body contendrá la data nueva.
3. **Delete (Lógico):** Cambia el estado de un registro a `false` (Desactivar).
4. **Remove (Físico):** Elimina completamente el registro de la tabla.

## 6. Bases de Datos y Migraciones
La base de datos está diseñada para manejar millones de registros y emplea índices estrictos.

### Reglas de Migración y Sequelize CLI
Cuando la IA o el desarrollador necesiten crear nuevos modelos, deben usar `sequelize-cli`.
**Regla de oro para creación de tablas:** Toda tabla nueva debe contener un campo `status` por defecto.

**Comando de ejemplo:**
```bash
npx sequelize-cli model:generate --name NombreModelo --attributes status:boolean
```

## 7. Buenas Prácticas y Reglas para el Agente (IA)
1. **Seguridad:** Implementar validaciones en TODOS los endpoints y utilizar tokens JWT para rutas privadas.
2. **Manejo de Errores:** La lógica de errores debe estar siempre centralizada en un middleware.
3. **Versionado:** Todo cambio debe mantener retrocompatibilidad.
4. **Optimización:** Toda consulta a la BD debe considerar índices y evitar N+1 queries.
