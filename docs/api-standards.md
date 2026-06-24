# API Standards - EatCloud Modernizado

Para todas las consultas debemos tener en cuenta los entornos de despliegue (`{{ENTORNO}}`):
- Desarrollo: `https://devservice.eatcloud.info`
- Producción: `https://service.eatcloud.info`

Las consultas API se dividen en 2: **Consultas privadas** y **Consultas públicas**.

## 1. Consultas privadas (`/api/`)
Requieren un token (JWT) que se genera al iniciar sesión enviando un POST a `{{ENTORNO}}/auth/login`. El token se envía en `Authorization: Bearer <token>`.

- **Formato:** `{{ENTORNO}}/api/{{table_name}}`
- **Ejemplo con parámetros:** `{{ENTORNO}}/api/{{table_name}}?name=eatcloud&_limit=5&_offset=8&_cmp=code,name,cua_user`

## 2. Consultas públicas (`/apipub/`)
No necesitan el uso del token, solo basta con hacer el llamado tipo GET.
- **Formato:** `{{ENTORNO}}/apipub/{{table_name}}`
- Tienen acceso a los mismos parámetros de búsqueda (`_limit`, `_offset`, etc.).

## 3. Parámetros de búsqueda personalizados
El backend cuenta con parámetros personalizados para optimizar consultas:
- `_limit`, `_offset`, `_cmp`, `_count`, `_null`, `_cache`, etc.

## 4. Consultas CRD (Crud)
Las consultas CRD se dividen en 4 operaciones principales. **Todas deben ser POST** y requieren acceso privado (token).

1. **Crear registros (Create)**
   - **Ruta:** `{{ENTORNO}}/crd/create/{{table_name}}`
   - **Body:** Los datos se envían dentro de un arreglo `data`. Permite la creación masiva.
   - **Encriptación:** Para encriptar campos, especificar `"encrypt":"nombre_campo"`.
   ```json
   {
       "encrypt":"name",
       "data": [ { "name": "donante", "password": "***" } ]
   }
   ```

2. **Actualizar registros (Update)**
   - **Ruta:** `{{ENTORNO}}/crd/update/{{table_name}}/{{query.params}}`
   - Los `{{query.params}}` (ej. `?limit=...&name=...`) dicen qué registros editar (función WHERE). El body contiene el dato a actualizar.
   - **Update con Encriptación:** `{{ENTORNO}}/crd/encrypt/update/{{table_name}}/{{query.params}}`

3. **Delete:** Utilizada para cambiar el estado de algunos registros a `false`.
4. **Remove:** Utilizada para eliminar completamente un registro de una tabla.
