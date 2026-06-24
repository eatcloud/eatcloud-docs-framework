# WAPP Standards - Aplicación de Donantes Modernizada

## 1. Introducción
La nueva WAPP (Web/WhatsApp App) de Donantes de EatCloud es la interfaz transaccional primaria para la gestión de donaciones en sitio. Debido a la sensibilidad de la data y las implicaciones de auditoría, la WAPP se rige por un estricto conjunto de restricciones operativas.

## 2. Restricciones Operativas (Reglas Duras)
Estas reglas DEBEN ser aplicadas y validadas tanto en el Frontend de la WAPP como en la capa de controladores del Backend.

### 2.1 Edición y Eliminación de Donaciones
- **Prohibición de Eliminación:** Está estrictamente RESTRINGIDA la eliminación física de donaciones desde la WAPP. No debe existir ningún botón u operación que apunte a la eliminación de registros de donaciones.
- **Restricción de Edición:** La edición de donaciones una vez creadas se encuentra altamente restringida. Solo se pueden modificar estados siguiendo el flujo de vida natural de la donación, pero no alterar cantidades, pesos o productos una vez la donación ha sido anunciada.

### 2.2 Captura de Datos Obligatorios
- **Campo Lote:** La captura del campo "Lote" es OBLIGATORIA para todos los productos cuando la regla de negocio lo exige por el nivel de cuenta máster (`cua_master`). 
- **Creación por Archivo Plano:** Se soporta la creación masiva de donaciones por archivo plano, lo cual incluye la integración obligatoria de los clasificadores (ej. tipo de producto, subcategoría) para asegurar que el inventario mantenga coherencia.

### 2.3 Operaciones desde el Punto de Donación (POD)
- **Asignación directa:** La WAPP soporta la asignación de la donación directamente desde el POD al gestor o beneficiario en sitio.
- **Restricción de entrega:** Existe una restricción estricta para marcar donaciones como "no entregadas" cuando se gestionan directamente desde un POD. El flujo requiere justificación estructurada o el paso por el Error Handler si el inventario no coincide.

## 3. Integraciones Adicionales
- La arquitectura permite transacciones multi-nube y debe soportar la captura de archivos XML como adjuntos, los cuales son necesarios para efectos de certificación tributaria de la donación.
