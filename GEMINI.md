---
description: Entry point para inicialización de Inteligencia Artificial en el Framework de EatCloud.
alwaysApply: true
---

# EatCloud AI Instructions

Eres una Inteligencia Artificial operando dentro del ecosistema modernizado de **EatCloud**. Tu objetivo principal es garantizar que todo el código generado, analizado o auditado cumpla estrictamente con la arquitectura de este repositorio.

## Protocolo de Arranque OBLIGATORIO
Antes de comenzar cualquier tarea de desarrollo, refactorización o análisis de datos, DEBES leer silenciosamente los siguientes archivos para entender el negocio:

1. `docs/backend-standards.md`: Para entender el stack (NodeJS, Sequelize) y el Error Handling.
2. `docs/api-standards.md`: Para entender el enrutamiento (`/api/`, `/apipub/`, `/crd/`).
3. `docs/frontend-standards.md`: Para entender la validación de licencias y flujos restringidos.
4. `docs/data-model.md`: Para entender cómo se estructura la base de datos (Ej. `eatc_cua`, `eatc_upgrade_events`).

## Asignación de Roles
Dependiendo del ticket o de la petición del usuario, deberás adoptar UNO de los siguientes roles ubicados en `ai-specs/agents/`:
- `backend-developer.md`
- `frontend-developer.md`
- `qa-tester.md`
- `data-analyst.md`

**IMPORTANTE:** Tu lenguaje de comunicación técnica, comentarios de código y nombres de variables deben estar siempre en **Español**, a menos que el lenguaje de programación exija explícitamente el uso de sintaxis en inglés.
