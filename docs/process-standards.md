# EatCloud Process Standards (Asana & Discovery)

Este documento rige el ciclo de vida de desarrollo de producto, incidencias y mejoras. Todos los agentes que deban interactuar con Asana, reportar bugs o crear tareas, deben acoplarse a este flujo.

## 1. Flujo de Discovery y Desarrollo
El sistema central de gestión es **Asana**. Toda "Mejora" o requerimiento debe fluir de la siguiente manera:

1. **Paso 1 (Levantamiento):**
   La persona o agente que solicite la mejora llena el formulario de Asana correspondiente.

2. **Paso 2 (Aprobación):**
   - **Proyecto Asana:** `EATC2 - BL Mejoras`
   - **Sección:** `Pendiente por Aprobación`
   - **Responsable:** Isis Espitia (Aprueba las mejoras a implementar).

3. **Paso 3 (Discovery):**
   - **Proyecto Asana:** `EATC2 - BL Mejoras`
   - **Sección:** `Discovery`
   - **Responsable:** Luis Carlos Correa.
   - **Acción:** Se genera una subtarea obligatoria llamada "Aprobación del flujo de Discovery" que actúa como compuerta (gate) para pasar a desarrollo.

4. **Paso 4 (Paso a Desarrollo):**
   Tras la fase de Discovery, el líder técnico clasifica la tarea y se traslada a los proyectos de ejecución:
   - `Sprint Product` (Nuevas funcionalidades)
   - `Reporte de incidencias` (Bugs, hotfixes).

## 2. Instrucción para Agentes IA
* Si un agente encuentra un bug crítico durante su análisis/ejecución, debe solicitar al usuario (Concejal/Tech Lead) si desea levantar un ticket en `Reporte de incidencias`.
* Si un agente propone una refactorización mayor o nueva feature, debe formularla para que entre a `EATC2 - BL Mejoras` en `Pendiente por Aprobación`.
