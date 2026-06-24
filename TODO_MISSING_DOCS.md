# TODO: Documentación y Tareas del Framework (EatCloud)

*Nota: Esta lista registra los avances y las tareas pendientes para consolidar el Framework `ai-specs`.*

## ✅ Fase 1 Completada (Extracción de Conocimiento)
- [x] Extraer las 11 páginas críticas iniciales.
- [x] Extraer reglas de WAPP, BackOffice (BO) y KPIs.
- [x] Extraer documentos de Login Único y Arquitectura Multinube.
- [x] **Fase 1.6 Bulk Scrape:** Descargadas y procesadas las 195 páginas restantes de SharePoint. Todo el conocimiento institucional (CRM, Blockchain, Flujos de Asana, Cancelaciones, Reglas Contables, etc.) ya reside en `/raw_docs/`.

## 🚧 Fase 2: Creación y Refinamiento de Agentes (System Prompts)
Teniendo toda la base de conocimiento descargada, el siguiente paso es "educar" a nuestros agentes.
- [ ] **wapp-developer.md:** Inyectar las reglas del carrito de compras, validaciones de lote, restricciones de edición/eliminación (Exito) y bloqueos de estado.
- [ ] **bo-developer.md:** Inyectar las reglas de login centralizado, creación de cuentas/beneficiarios y despliegue multinube.
- [ ] **data-analyst.md:** Inyectar el conocimiento sobre la tabla `eatc_kpi_rules`, cálculos de peso por estado y cruces con las verticalidades `rv_vertical_code`.
- [ ] **frontend-developer / backend-developer:** Refinar la arquitectura transversal (Componentes, Endpoints Legacy vs. Modernos).

## 📌 Procesos Específicos y Reglas de Desarrollo
- [ ] **Asana & Discovery Flow:** Se extrajo el documento `Coordinación-flujo-discovery-con-desarrollo`. Se debe crear un `docs/process-standards.md` para enseñar a la IA cómo se mueve una tarea de "Pendiente por Aprobación" a "Discovery" y a "Sprint Product" usando Asana.
- [ ] **Líneas Rojas (Sistemas Legacy):** Definir qué NO debe tocar la IA (Ej. scripts en PHP puro de `config.nzzn.co` que deben ser tratados con cuidado o solo migrados).

## 🛠️ Integraciones Futuras (Conocimiento Extraído)
- [ ] Revisar cómo integrar el conocimiento bajado sobre *Freshworks CRM*, *Blockchain*, y *Datagov* en los flujos de los agentes si se decide modernizar esos módulos.
