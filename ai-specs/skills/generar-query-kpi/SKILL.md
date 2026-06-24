---
description: Genera una consulta optimizada para calcular KPIs (Impacto Ambiental, Económico, etc.) utilizando la tabla dinámica eatc_kpi_rules.
---

# Skill: Generar Query KPI (EatCloud)

## Contexto
En lugar de "quemar" las fórmulas matemáticas en el código, EatCloud utiliza una tabla diccionario (`eatc_kpi_rules`) para calcular su impacto. Este skill ayuda a los analistas a generar el query o script necesario para cruzar kilos de comida con los coeficientes correctos.

## Instrucciones de Ejecución
Cuando el usuario invoque esta skill (ej. `/generar-query-kpi calcular impacto de CO2`), sigue estos pasos:

1. **Reconocimiento del KPI:** Identifica el tipo de KPI solicitado (ej. Gases de efecto invernadero - GHG, Kilos, Económico).
2. **Generación del Script de Búsqueda:** Proporciona un ejemplo de código (JavaScript, Python o SQL conceptual) que primero consulte `{{ENTORNO}}/api/eatc_kpi_rules` para obtener el coeficiente asociado al KPI y a la región.
3. **Cálculo:** Muestra cómo multiplicar el campo `eatc_total_weight_kg` de las donaciones por el coeficiente obtenido.
4. **Respuesta final:** Explica que esta metodología asegura que si las regulaciones internacionales cambian, el código no requiere despliegue nuevo.
