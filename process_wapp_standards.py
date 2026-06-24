import os
import glob

docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
wapp_standards_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/wapp-standards.md"

def get_markdown_content(filename):
    filepath = os.path.join(docs_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Leemos las reglas de negocio de los RAWs
edicion = get_markdown_content("WAPP-Modernizada--restricción-de-edición-de-donaciones.aspx.md")
eliminacion = get_markdown_content("WAPP-Modernizada--restricción-de-eliminación-de-donaciones.aspx.md")
asignacion = get_markdown_content("WAPP-Modernizada--asignación-de-donación-desde-el-POD-(punto-de-donación).aspx.md")
lote = get_markdown_content("WAPP-Modernizada--captura-del-campo--lote--obligatoria-por--cua_master-.aspx.md")
no_entregadas = get_markdown_content("WAPP-Modernizada--restricción-para-marcar-como-no-entregadas-las-donaciones-de-un-POD-donaciones.aspx.md")
archivos_planos = get_markdown_content("WAPP--Creación-de-Donaciones-por-archivo-plano--integración-de-clasificadores.aspx.md")

# Actualizamos wapp-standards.md
wapp_md = f"""# EatCloud WAPP Standards

Este documento centraliza todas las reglas de negocio, validaciones y restricciones exclusivas del Frontend de la aplicación web (WAPP) modernizada.

## 1. Arquitectura Base
* La WAPP Donantes fue re-diseñada buscando simplificar la experiencia operativa.
* **Componentes Principales:**
    * **Login:** Rediseñado con nuevos labels.
    * **Menú Lateral:** Simplificado.
    * **Crear anuncio de donación:** Experiencia estilo "carrito de compras" con visibilidad dividida.
    * **Dashboard Principal:** Simplificado, enfocado a la gestión diaria inmediata sin estadísticas complejas.
    * **Listado de donaciones:** Unificación de las antiguas vistas "Seguimiento de anuncios" y "Entrega de donaciones", utilizando un modelo de estados simplificado.
    * **Resultados:** Indicadores de gestión movidos a vista interior.

## 2. Restricciones de Manipulación de Donaciones

### 2.1 Restricción de Edición
La WAPP valida si una cuenta tiene permitido editar donaciones mediante el parámetro de configuración `edit_dona_access`.
* **Si `edit_dona_access` == 'n' / 'FALSE':** La WAPP **ocultará** el botón de editar donación.
* **Si `edit_dona_access` == 'y' / 'TRUE':** La WAPP permitirá el despliegue del botón.
*(Regla nacida de la solicitud del cliente Exito)*

### 2.2 Restricción de Eliminación
La WAPP valida si una cuenta tiene permitido eliminar donaciones mediante el parámetro de configuración `delete_dona_access`.
* **Si `delete_dona_access` == 'n' / 'FALSE':** La WAPP **ocultará** el botón para borrar donaciones.
* **Si `delete_dona_access` == 'y' / 'TRUE':** La WAPP permitirá el despliegue del botón.
*(Regla nacida de la solicitud del cliente Exito)*

### 2.3 Restricción para marcar como "No Entregadas"
La WAPP valida si un punto de donación (POD) tiene habilitado marcar donaciones como no entregadas mediante el parámetro de configuración `del_dona_access`.
* **Si `del_dona_access` == 'n' / 'FALSE':** La WAPP **ocultará** el botón que permite marcar una donación como no entregada.
* **Si `del_dona_access` == 's' / 'TRUE':** La WAPP permitirá desplegar la funcionalidad de marcado.

## 3. Asignación Directa desde el POD
La WAPP modernizada permite crear anuncios "fast-track" (Asignación Directa).
* El sistema valida la configuración `fast_track` en la tabla maestra de cuenta de usuario.
* El operador selecciona la bodega del Banco de Alimentos destino de la lista habilitada (`beneficiary_assignment`).
* Se crea el encabezado (`eatc_dona_header`) en estado `scheduled` y la donación (`eatc_dona`) en estado `scheduled`.
* Se salta la etapa de publicación ("vitrina") y no se requiere programar recolección ni firmar pre-certificados para ese paso.
* Posteriormente se cambia directamente de `scheduled` a `delivered` cuando se entrega.

## 4. Validación de Lote
El campo "Lote" es administrado dinámicamente según la regla de la cuenta (`cua_master`).
* La WAPP valida el parámetro `lote_mandatory`.
* **Si `lote_mandatory` == 'y' / 'TRUE':** El campo "lote" se pinta con asterisco (*) rojo y no permite avanzar ni guardar (botón "Agregar al carrito" inactivo) hasta que no se diligencie, mostrando una alerta estilo: "El campo LOTE es obligatorio y debe ser llenado."
* **Si `lote_mandatory` == 'n' / 'FALSE':** El campo es completamente opcional.

## 5. Creación por Archivo Plano e Integración de Clasificadores
La WAPP permite cargas masivas a través de archivos planos.
* El sistema valida la columna `bar_code` (EAN) u `odd_code` y cruza contra `cua_products` y el maestro global de EatCloud.
* Asigna automáticamente las taxonomías (`typology_a`, `typology_b`) a los productos que ingresan por carga masiva, asegurando que las reglas de KPI de peso y mix de alimentos cuadren en la consolidación.

---
> **Nota:** Todos los agentes (Especialmente WAPP Developer) deben consultar este archivo en cada modificación de la interfaz gráfica y validación de botones.
"""

with open(wapp_standards_path, "w", encoding="utf-8") as f:
    f.write(wapp_md)

print("wapp-standards.md actualizado con la extracción profunda.")
