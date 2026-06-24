---
description: Audita el código de la API en busca de vulnerabilidades de exposición de datos en rutas públicas y valida la correcta implementación de seguridad con JWT.
---

# Skill: Auditar Endpoints y Seguridad API (EatCloud)

## Contexto
Este flujo de trabajo se utiliza para realizar una revisión de seguridad y arquitectura sobre cualquier código nuevo o modificado relacionado con los endpoints de la API de EatCloud. Su objetivo es evitar fugas de información.

## Instrucciones de Ejecución

Cuando el usuario invoque esta skill (ej. `/auditar-endpoints`), debes seguir estrictamente los siguientes pasos:

1. **Escaneo de Rutas Públicas (`/apipub/`):**
   - Identifica todos los endpoints definidos bajo el prefijo `/apipub/`.
   - Analiza los datos que se retornan al cliente. 
   - **Regla Crítica:** Si el endpoint expone información sensible (contraseñas, tokens, correos privados o ubicaciones exactas no autorizadas), márcalo como **FALLO DE SEGURIDAD CRÍTICO**.

2. **Validación de Rutas Privadas (`/api/` y `/crd/`):**
   - Identifica las rutas de lectura (`/api/`) y las rutas de mutación (`/crd/create`, `/update`, etc.).
   - Verifica que la lógica requiera un token JWT válido.
   - Si un endpoint bajo estas rutas omite la validación de autenticación (`Bearer Token`), documéntalo como un riesgo alto.

3. **Manejo de Errores Centralizado:**
   - Revisa los controladores (handlers) para asegurar que no se estén respondiendo errores directamente con `res.status(500).send(...)`.
   - El código debe usar `next(error)` para enviar el error al middleware global de *Error Handler*.

4. **Entrega de Resultados:**
   - Genera un reporte en markdown.
   - Categoriza los hallazgos en: 🔴 **Críticos**, 🟡 **Advertencias**, y 🟢 **Buenas Prácticas Cumplidas**.
   - Proporciona un snippet de código con la corrección recomendada para cada fallo encontrado.
