# Guía de Desarrollo - EatCloud Docs Framework & AI Agents

Este repositorio funciona como la fuente de verdad y el cerebro estructurado para los Agentes de Inteligencia Artificial (Framework OpenSpec/Specboot) y el equipo de desarrollo de EatCloud.

Toda la documentación está escrita estrictamente en **Markdown (.md)** y en **ESPAÑOL**.

## 1. Estructura del Repositorio

El repositorio está dividido en tres capas principales:

*   `/raw_docs/`: Contiene volcados directos (scraping) de las páginas de SharePoint de EatCloud. Es la fuente de consulta cruda e inalterada.
*   `/docs/`: Contiene los **Standards**. Aquí la información de los `raw_docs` ha sido refinada, curada y estructurada en reglas de negocio estrictas (Ej. `wapp-standards.md`, `kpi-standards.md`, `multinube-standards.md`).
*   `/ai-specs/`: Contiene el framework de los Agentes de IA.
    *   `/ai-specs/agents/`: Los *System Prompts* (cerebros) de los agentes (Ej. `bo-developer.md`, `data-analyst.md`).
    *   `/ai-specs/skills/`: Herramientas o *Tools* atómicas que los agentes pueden utilizar.

## 2. Flujo de Trabajo (Actualización de Conocimiento)

Cuando EatCloud introduce una nueva regla de negocio o cambia un proceso en SharePoint, se debe seguir este flujo para mantener a los agentes actualizados:

1.  **Extracción (Raw):** Descargar la página actualizada de SharePoint y colocarla en `/raw_docs/`.
2.  **Consolidación (Docs):** Modificar el archivo correspondiente en `/docs/` (Ej. Si cambió el login, actualizar `bo-login-standards.md`) reflejando la nueva regla técnica.
3.  **Inyección en Agentes:** Revisar si el cambio afecta las *Líneas Rojas* de los System Prompts en `/ai-specs/agents/` y actualizar los prompts para que la IA adopte el nuevo comportamiento.

## 3. Integración con el Flujo de Asana (Discovery)

Cualquier mejora estructural en el código, descubrimiento de bugs o nueva funcionalidad debe someterse al flujo oficial detallado en `process-standards.md`:
*   Levantar tarea en el proyecto **EATC2 - BL Mejoras**.
*   Aprobación -> Discovery -> Sprint Product.
*   **Ningún agente de IA** debe pushear cambios destructivos a producción o saltarse este flujo de validación.

## 4. Estándares de Codificación para los Agentes

*   **Identidad:** Los agentes deben respetar su rol (Frontend, Backend, BO, Data Analyst, QA).
*   **Aislamiento Multinube:** Al manipular bases de datos, los agentes deben recordar aislar transacciones (DONA/ODDS) mediante el `rv_vertical_code` y la cuenta maestra (`cua_master`).
*   **Seguridad Zero Trust:** No generar scripts que expongan endpoints sin autenticación centralizada.
