# EatCloud Arquitectura Multi-Nube (Multi-Cloud)

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
