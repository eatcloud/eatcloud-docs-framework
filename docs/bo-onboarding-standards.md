# EatCloud BackOffice - Onboarding Standards

Este documento consolida las reglas de Onboarding y flujo de BackOffice extraídas de la documentación original.

## 1. Onboarding de Cuentas (Donantes)
El BackOffice es el encargado de dar de alta nuevas cuentas donantes en el sistema.

### 1.1 Proceso Principal
* Configuración del NIT o RUT.
* Configuración de la Razón Social y nombre de fantasía.
* Asignación del modelo de `fast_track` o vitrina regular según acuerdo comercial.
* Configuración de parámetros estrictos como `edit_dona_access`, `delete_dona_access`, y `lote_mandatory` en la tabla `cua_master`.

## 2. Onboarding de Beneficiarios
Flujo crítico donde una fundación o banco de alimentos se registra para poder recibir asignaciones.

### 2.1 Puntos de Control y Estados
* **Registro Inicial:** El beneficiario llena el formulario en el portal público (Ej: `https://portal.eatcloud.info/es/onboarding/beneficiarios`).
* **Verificación Legal:** Subida de RUT, Certificación Bancaria y Representación Legal.
* **Aprobación:** BackOffice aprueba el `eatc_state` pasándolo de `pending` a `active`.
* Una vez `active`, la fundación puede empezar a visualizar anuncios en la App/Vitrina de Beneficiarios o ser target en una "Asignación de donación desde el POD".

## 3. Generación de Certificado de Donación
Proceso contable y tributario vital.

### 3.1 Reglas del BackOffice / Sistema
* Solo las donaciones en estado `received` o `pre-certificate` pueden ser certificadas.
* El Banco de Alimentos consolida las donaciones recibidas de una cuenta en un mes fiscal.
* Se genera un documento avalado por la DIAN con los montos/peso.
* El estado del encabezado de la donación cambia a `certificate`.

---
> **Nota:** Todos los agentes (Especialmente BackOffice Developer) deben revisar este flujo para las migraciones y modernizaciones.
