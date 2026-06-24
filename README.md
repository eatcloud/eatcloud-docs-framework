# EatCloud AI Specboot Framework 🚀

Este repositorio contiene el "Cerebro" de Inteligencia Artificial para la plataforma modernizada de **EatCloud**. Utilizando el enfoque de desarrollo impulsado por especificaciones (Spec-Driven Development), este framework dota de superpoderes y reglas de negocio estrictas a los agentes de IA (Claude, Cursor, GitHub Copilot, Gemini).

## 📁 Estructura del Proyecto

```text
.
├── docs/                        # La Fuente de la Verdad de EatCloud
│   ├── api-standards.md         # Reglas de peticiones (api, apipub, crd)
│   ├── backend-standards.md     # Reglas de NodeJS, Sequelize y Error Handling
│   ├── data-model.md            # Esquemas de Base de Datos y Mapeos
│   ├── frontend-standards.md    # Lógica React, validación de licencias y flujos
│   ├── development_guide.md     # Guía para despliegue local e integración
│   └── ...
├── ai-specs/                    # Comportamiento y personalidades de la IA
│   ├── agents/                  # Roles (Backend, Frontend, QA Tester, Data Analyst)
│   └── skills/                  # Comandos automatizados (auditorías, generadores)
├── GEMINI.md                    # Instrucciones de inicialización
└── TODO_MISSING_DOCS.md         # Registro de deuda técnica en la documentación
```

## 🧠 ¿Cómo funciona?

En lugar de que la Inteligencia Artificial adivine cómo programar en EatCloud, este framework **fuerza** al Agente a leer las reglas locales antes de escribir código.
Por ejemplo, si le pides al agente hacer un endpoint para guardar datos, el agente consultará `docs/api-standards.md` y sabrá que en EatCloud no se programan endpoints POST independientes, sino que se utiliza la ruta centralizada `/crd/create/`.

## 🛠️ Instalación e Integración (Para el Equipo)

Para que tu IA local o tu entorno de desarrollo aprenda a programar como EatCloud, debes integrar este repositorio en tu proyecto actual:

### Opción A: Copia Directa (Recomendada para proyectos aislados)
Simplemente copia las carpetas `docs/` y `ai-specs/` junto con el archivo `GEMINI.md` en la raíz de tu proyecto (ej. Frontend o Backend de EatCloud).
```bash
cp -r /ruta/a/eatcloud-docs-framework/docs /tu/proyecto/
cp -r /ruta/a/eatcloud-docs-framework/ai-specs /tu/proyecto/
```

### Opción B: Integración con Cursor / Claude
1. Ubícate en tu proyecto (no en el framework).
2. Crea los enlaces simbólicos o incluye referencias directas en tus archivos `.cursorrules` o `CLAUDE.md` apuntando a `docs/backend-standards.md` o al Agente que corresponda.

## 🪄 Skills Disponibles
Los desarrolladores pueden utilizar los siguientes comandos invocándolos a través de su Chat de IA:

- `/auditar-endpoints`: Escanea el código en busca de datos sensibles expuestos en `apipub/` y verifica el uso de JWT.
- `/generar-crd-schema [NombreTabla]`: Genera el payload JSON y el snippet HTTP listo para inyectar en la ruta `/crd/create/` o `/crd/update/`.

---
*Mantenido por el equipo de EatCloud Modernización.*
