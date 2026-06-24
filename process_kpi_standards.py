import os

docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
kpi_standards_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/kpi-standards.md"

kpi_md = """# EatCloud KPI Standards & Data Types

Este documento centraliza las reglas sobre cómo interactuar con el modelo de datos estadístico y las reglas de KPIs almacenadas en la base de datos de EatCloud.

## 1. Maestro de Reglas: `eatc_kpi_rules`
La plataforma EatCloud utiliza una tabla central (maestro) llamada `eatc_kpi_rules` para almacenar los diferentes KPIs utilizados en los Dashboards, Informes y analítica en tiempo real. 

### 1.1 Accesos al Maestro (Referencia Técnica)
* **Vista de Tabla / Dashboard de configuración (Edición):** 
  `https://config.nzzn.co/ws/v1/vw/externa/editar_llenar_obj_url.php?maestro=eatc_kpi_rules&lista=si&atrib_filtro_tb=kpi&val_filtro_tb=_todos`
* **API de Consulta Externa (JSON):** 
  `https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_kpi_rules&kpi=_todos`
* **Consulta de Definición de Campos:**
  `https://config.nzzn.co/ws/v1/bo/ws_xxx_cons.php?_tabla=eatc_kpi_rules&_campos`

*(Nota: Estas URLs se consideran endpoints legacy/heredados del sistema `config.nzzn.co`, pero son la fuente de verdad de la arquitectura actual).*

## 2. Aplicación de las reglas en la Analítica
Todo Data Analyst o Backend Developer que calcule estadísticas sobre el modelo `eatc_dona` (Donaciones) y `eatc_dona_headers` (Encabezados) debe consultar `eatc_kpi_rules` para determinar qué estados (`eatc_state`) aplican para sumar peso o contar donaciones exitosas.

**Ejemplo de estados válidos típicos para peso rescatado:**
* `delivered` (Entregado en físico)
* `received` (Recibido por beneficiario)
* `pre-certificate` (En proceso de certificación)
* `certificate` (Certificado emitido)
* (Estados como `cancelled`, `rejected` o `not_delivered` NUNCA suman a los KPIs positivos de rescate).

---
> **Nota:** Todos los agentes (Especialmente Data Analyst y Backend Developer) deben basar la construcción de Queries de Informes usando `eatc_kpi_rules`.
"""

with open(kpi_standards_path, "w", encoding="utf-8") as f:
    f.write(kpi_md)

print("kpi-standards.md creado y actualizado.")
