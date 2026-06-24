# Backend Standards - EatCloud Modernizado

## 1. Introducción
Este backend desarrollado en NodeJS es parte del proyecto de modernización de EatCloud, diseñado para manejar grandes volúmenes de datos mediante consultas optimizadas y robusto conjunto de endpoints.

## 2. Entornos de Despliegue (`{{ENTORNO}}`)
- **Entorno de desarrollo:** `https://devservice.eatcloud.info`
- **Entorno de producción:** `https://service.eatcloud.info`

## 3. Estructura del proyecto
El proyecto está organizado de acuerdo a las mejores prácticas de desarrollo de NodeJS:
- `Config`: Configuración de la base de datos y variables de entorno.
- `Handlers`: Lógica para manejar peticiones HTTP.
- `Middlewares`: Validaciones y manejo de errores.
- `Models`: Definición de modelos Sequelize.
- `Routers`: Definición de las rutas y endpoints.
- `Utils`: Funciones reutilizables.

## 4. Principales dependencias
- **Express**: Framework para el manejo de peticiones HTTP.
- **Sequelize**: ORM para interactuar con la base de datos.
- **Dotenv**: Manejo de variables de entorno.
- **Cors**: Configuración de políticas de acceso.

## 5. Colecciones de Endpoints
A continuación se describen las principales funcionalidades de cada encarpetado:
- **Autenticación (auth)**: Manejo de login, registro, cambios de contraseña y tokens con JWT.
- **Users**: Crud de usuarios.
- **Operaciones crud (crd)**: Funciones principales generales (Crear registro, actualizar, encriptar, eliminar y desactivar).
- **Api**: Funciones de consulta para tablas públicas, privadas y encriptadas.

## 6. Bases de datos y Migraciones
La base de datos está diseñada para manejar millones de registros, con índices para optimizar las consultas.

### Migraciones en NodeJs para el manejo de bases de datos
📌 **Crear una tabla nueva con un campo status por defecto**
Generar el modelo y la migración con solo el campo status. 
*Nota: Cambiar el "NombreModelo" antes de ejecutar.*
```bash
npx sequelize-cli model:generate --name NombreModelo --attributes status:boolean
```

## 7. Buenas prácticas
- **Seguridad**: Implementar validaciones en los endpoints y utilizar tokens JWT para autenticación.
- **Manejo de errores**: Centralizar la lógica de errores en un middleware.
- **Versionado de la API**: Mantener retrocompatibilidad con versiones previas.
