import os
import re

file_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/openspec-tasks-mandatory-steps.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Traducción básica de las partes más prominentes, conservando estructura técnica.
translated = content.replace("OpenSpec Tasks: Mandatory Steps Enforcement", "Tareas de OpenSpec: Cumplimiento de Pasos Obligatorios")
translated = translated.replace("When creating or updating `tasks.md` artifacts in OpenSpec changes, you MUST:", "Al crear o actualizar los artefactos `tasks.md` en los cambios de OpenSpec, DEBES:")
translated = translated.replace("## 1. Read openspec/config.yaml First", "## 1. Leer openspec/config.yaml Primero")
translated = translated.replace("**BEFORE** creating or updating any `tasks.md` file, you MUST read `openspec/config.yaml` to understand:", "**ANTES** de crear o actualizar cualquier archivo `tasks.md`, DEBES leer `openspec/config.yaml` para entender:")
translated = translated.replace("Backend and frontend-specific mandatory steps", "Pasos obligatorios específicos del backend y frontend")
translated = translated.replace("Branch naming conventions", "Convenciones de nombres de ramas")
translated = translated.replace("Task structure requirements", "Requisitos de estructura de tareas")
translated = translated.replace("Testing and documentation requirements", "Requisitos de pruebas y documentación")
translated = translated.replace("## 2. Mandatory Steps", "## 2. Pasos Obligatorios")
translated = translated.replace("All implementation tasks MUST include these steps in the correct order:", "Todas las tareas de implementación DEBEN incluir estos pasos en el orden correcto:")
translated = translated.replace("### Step 0: Create Feature Branch (MUST BE FIRST)", "### Paso 0: Crear Rama de Funcionalidad (DEBE SER EL PRIMERO)")
translated = translated.replace("**Location**: Must be the very first step (Step 0)", "**Ubicación**: Debe ser el primer paso absoluto (Paso 0)")
translated = translated.replace("**Branch naming**: `feature/[ticket-id]` or `feature/[change-name]`", "**Nomenclatura de la rama**: `feature/[ticket-id]` o `feature/[change-name]`")
translated = translated.replace("**Action**: Create and switch to feature branch before any code changes", "**Acción**: Crear y cambiar a la rama de funcionalidad antes de cualquier cambio de código")
translated = translated.replace("### Mandatory Steps (Must Be Included):", "### Pasos Obligatorios (Deben ser Incluidos):")
translated = translated.replace("Review and Update Existing Unit Tests (MANDATORY)", "Revisar y Actualizar Pruebas Unitarias Existentes (OBLIGATORIO)")
translated = translated.replace("Run Unit Tests and Verify Database State (MANDATORY)", "Ejecutar Pruebas Unitarias y Verificar el Estado de la Base de Datos (OBLIGATORIO)")
translated = translated.replace("Manual Endpoint Testing with curl (MANDATORY) - **AGENT MUST EXECUTE**", "Prueba Manual de Endpoints con curl (OBLIGATORIO) - **EL AGENTE DEBE EJECUTARLA**")
translated = translated.replace("E2E Testing with Playwright MCP (MANDATORY if applicable) - **AGENT MUST EXECUTE**", "Pruebas E2E con Playwright MCP (OBLIGATORIO si aplica) - **EL AGENTE DEBE EJECUTARLAS**")
translated = translated.replace("Update Technical Documentation (MANDATORY)", "Actualizar Documentación Técnica (OBLIGATORIO)")
translated = translated.replace("## 3. Manual Testing Requirements - CRITICAL: Agent Must Execute", "## 3. Requisitos de Pruebas Manuales - CRÍTICO: El Agente Debe Ejecutarlas")
translated = translated.replace("**IMPORTANT**: The coding agent (AI) MUST perform all manual testing steps itself. **NEVER delegate testing to the user**. These tests must be executed by the agent to mark tasks as completed in `tasks.md`.", "**IMPORTANTE**: El agente de codificación (IA) DEBE realizar todos los pasos de pruebas manuales por sí mismo. **NUNCA delegar las pruebas al usuario**. Estas pruebas deben ser ejecutadas por el agente para marcar las tareas como completadas en `tasks.md`.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(translated)

