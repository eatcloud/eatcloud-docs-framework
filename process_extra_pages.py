import os

docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
bo_login_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/bo-login-standards.md"
multinube_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/multinube-standards.md"

# 1. Procesar Login URL Única
bo_login_md = """# EatCloud BO Login - URL Única

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
"""

with open(bo_login_path, "w", encoding="utf-8") as f:
    f.write(bo_login_md)

# 2. Procesar Multi-Nube
multinube_md = """# EatCloud Arquitectura Multi-Nube (Multi-Cloud)

Este documento define la nueva abstracción del modelo de negocio de EatCloud, expandiéndose desde "Alimentos" a múltiples verticales de revalorización de materiales.

## 1. Conceptos Fundamentales
La plataforma evoluciona de "Donación de Alimentos" a un modelo abstracto de "Revalorización y Valorización" aplicable a cualquier industria.

### 1.1 Entidades Clave
* **Revalorizar - Valorizar:** La dinámica operativa central. Tomar un "material" físico con riesgo de ser pérdida y reinsertarlo en una cadena de valor.
* **Vertical de Revalorización (`revalorizer_valorizer_vertical`):** Una cadena de valor específica (Ej. *Gestión humanitaria de excedentes alimentarios*). Agrupa entidades homogéneas.
* **Código de la Vertical (`rv_vertical_code`):** Identificador único. Una cuenta maestra (`cua_master`) ahora está vinculada a una Vertical.
* **Cuenta Maestra Original (`original_cua_master`):** Registro de la primera cuenta que operó dentro de una vertical.

### 1.2 El Nuevo Modelo de Transacción
Los términos de Donación clásica evolucionan:
* **ODDS (Objects for Donation, Distribution and Stewardship):** Reemplaza el concepto puramente de "Alimentos". Son los objetos físicos transables dentro de la plataforma (ej. Alimentos, No Alimentos, Textiles, etc).
* **DONA (Distributed Objects for Non-Wasteful Actions):** Un conjunto de *ODDS* conforman una *DONA*. Esta es la evolución técnica del término "Donación", convirtiéndolo en un acrónimo global de acción anti-desperdicio.
* **Entidad Generadora (`material_odds_generator_entity`):** Entidad (Ej: Industria Alimentaria, Textilera) que genera los ODDS. Conceptualmente agrupa a las cuentas usuario (`cua_user`).

## 2. Impacto Técnico en Base de Datos
Cualquier desarrollo de nuevos modelos o esquemas de base de datos debe soportar el parámetro de **Vertical de Valorización**, permitiendo que un mismo BackOffice y WAPP puedan gestionar Múltiples Nubes (Ej. Una nube para Alimentos y otra para Textil/Material de Construcción) simplemente aislando por el código de la vertical y la cuenta maestra.

---
> **Nota:** Todos los agentes (Especialmente Data Analyst y Backend Developer) deben considerar este glosario abstracto (ODDS, DONA, Verticales) al interpretar esquemas de datos o crear nuevos modelos, ya que la base de datos no está atada exclusivamente a "Comida".
"""

with open(multinube_path, "w", encoding="utf-8") as f:
    f.write(multinube_md)

print("Documentos extras de BO y Multinube procesados.")
