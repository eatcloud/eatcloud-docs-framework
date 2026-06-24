---
description: Genera automáticamente el payload JSON y el snippet HTTP (Fetch/Axios) compatible con la arquitectura de mutación CRD de EatCloud a partir de un modelo o entidad de datos.
---

# Skill: Generar Schema CRD (EatCloud)

## Contexto
El backend de EatCloud modernizado utiliza un sistema de mutación de datos centralizado a través de los endpoints de la familia `/crd/`. Este skill asiste a los desarrolladores (Frontend y QA) en la generación rápida de payloads para crear o actualizar registros.

## Instrucciones de Ejecución

Cuando el usuario invoque esta skill (ej. `/generar-crd-schema [NombreTabla]`), sigue estos pasos:

1. **Identificación de la Entidad:**
   - Si el usuario provee un modelo de datos o una lista de campos, asúmelo como la estructura base.
   - Identifica el nombre de la tabla (ej. `eatc_upgrade_events`).

2. **Generación del Payload (Create):**
   - Construye el objeto JSON para creación masiva. Recuerda que la arquitectura CRD exige envolver los registros dentro de un array `"data"`.
   - Si el usuario menciona que algún campo es sensible (ej. contraseñas), añade obligatoriamente la propiedad `"encrypt": "nombre_campo"` en la raíz del JSON.
   
   *Plantilla base a utilizar:*
   ```json
   {
       "encrypt": "opcional_campo_sensible",
       "data": [
           { "campo1": "valor1", "status": true }
       ]
   }
   ```

3. **Generación de la Ruta (Endpoint):**
   - Para creación: `POST {{ENTORNO}}/crd/create/{{table_name}}`
   - Para actualización: `POST {{ENTORNO}}/crd/update/{{table_name}}/?parametro=valor`

4. **Entrega de Resultados:**
   - Entrega el JSON final formateado.
   - Entrega un ejemplo en `curl` o en `fetch` de Javascript indicando que se debe inyectar la cabecera `Authorization: Bearer <token>`.
