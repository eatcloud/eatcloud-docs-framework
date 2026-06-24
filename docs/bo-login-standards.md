# EatCloud BO Login - URL Única

Este documento define la arquitectura y requerimientos para el sistema unificado de Login de Beneficiarios y BackOffice.

## 1. Arquitectura Centralizada de Acceso
Históricamente, el acceso se realizaba a través de endpoints fragmentados por cuenta maestra (Ej: `/api/{{_DOM.cua_master}}/bo_usuarios`).
En la modernización de la plataforma, el acceso se migra a una **URL Única y Centralizada**.

### 1.1 Entornos y URLs Oficiales
* **Producción:** `https://beneficiarios.eatcloud.info/signin` (y su contraparte legada `https://beneficiarios.eatcloud.info/_nbob/#!/login`).
* **Pruebas:** `https://devbeneficiarios.eatcloud.info/signin` (y `https://devbeneficiarios.eatcloud.info/_nbob/#!/login`).

### 1.2 Reglas de Base de Datos y Ruteo
* **Almacenamiento Central:** Los usuarios se llevan a una estructura centralizada.
* **Seguridad:** El sistema exige **guardar el password hasheado** en esta base de datos global.
* **Direccionamiento Dinámico:** Durante el proceso de autenticación, el sistema central consulta a qué Cuenta Maestra (`cua_master`) pertenece el usuario autenticado y lo direcciona ("enruta") dinámicamente a su propio entorno.
* **Alta de Nuevas Cuentas:** Cuando se crea una nueva cuenta maestra, el proceso automatizado de "Creación de Tablas Necesarias" también debe insertar los usuarios raíz de esa cuenta en esta estructura centralizada.

---
> **Nota:** Todos los agentes (BackOffice Developer, API Developer) deben asegurar que cualquier modificación a tablas de usuarios o creación de cuentas maestras pase por la estructura central de login.
