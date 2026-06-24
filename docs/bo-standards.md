# Back Office (BO) Standards - EatCloud

## 1. Introducción
El Back Office de EatCloud es la plataforma administrativa donde los actores de la cadena (Donantes, Beneficiarios, Bancos de Alimentos - ABACO, Gobiernos y Entes Territoriales) gestionan sus operaciones globales, auditan donaciones y emiten certificaciones.

## 2. Flujos de Onboarding
Los procesos de alta o registro en la plataforma deben seguir flujos estructurados que garanticen la recolección completa de datos formales.
- **Onboarding de Cuentas (Donantes):** Define la creación de la jerarquía de cuentas, asignación al `cua_master` correspondiente, y definición del tipo de licencia de uso (`free`, `impacto`, etc.).
- **Onboarding de Beneficiarios:** Requiere validación estricta de documentos legales y perfilamiento antes de permitirles la recepción de donaciones. 

## 3. Generación de Certificados de Donación
- La emisión de certificados tributarios de donación es una de las salidas de valor más importantes del sistema.
- **Validación de Cierre:** Los certificados solo se pueden generar para donaciones que han completado el ciclo completo (estado `certificado` o equivalente) y cuentan con sus evidencias de entrega, incluyendo archivos XML cuando el país o donante lo requiera.
- **Reportes:** Los actores con perfil de "Líder de Ecosistema" (ej. ABACO) tienen acceso a reportes consolidados de generación de certificados de toda su red.

## 4. Informes y Analítica
- El BO cuenta con informes de data analítica en tiempo real.
- **Nuevos Filtros:** Los informes de donantes incluyen filtros avanzados, como la búsqueda específica por número de documento u orden (`eatc_do`).
- **Control de Mermas:** El BO aloja el "Informe de pesos excesivos" para auditar discrepancias entre las cantidades anunciadas y recibidas en la operación.
