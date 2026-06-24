---
description: Valida el código de un Pull Request o un bloque de código para asegurar que no incumple ninguna de las restricciones duras de la WAPP.
---

# Skill: Validar Restricciones WAPP (EatCloud)

## Contexto
La WAPP de EatCloud maneja operaciones altamente restringidas por seguridad e inventario. Este skill se utiliza como un paso de Quality Assurance o Code Review automatizado.

## Instrucciones de Ejecución
Cuando el usuario invoque esta skill (ej. `/validar-restricciones-wapp [ruta_del_archivo]`), debes analizar el código proporcionado siguiendo estas reglas críticas:

1. **Escaneo de "Eliminación":** Busca botones, funciones o llamadas a la API que tengan palabras como `delete`, `remove`, `eliminar`. Si encuentras algo que apunte a borrar una donación, márcalo con 🔴 **Fallo Crítico: Eliminación de Donaciones Prohibida**.
2. **Escaneo de "Edición Post-Anuncio":** Revisa que los formularios de edición de donaciones solo expongan estados, y no permitan sobrescribir variables de peso (`weight`) o cantidad (`quantity`) si la donación ya ha sido anunciada.
3. **Escaneo de Campo "Lote":** Verifica que si existe un formulario de creación de productos, este incluya las validaciones condicionales que hacen obligatorio el campo `lote` si la configuración de la cuenta así lo requiere.

Provee un reporte estructurado y, de ser necesario, resalta las líneas problemáticas que deben ser corregidas.
