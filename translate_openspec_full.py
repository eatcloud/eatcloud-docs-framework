import re

file_path = "/Users/usuario2/Documents/eatcloud-docs-framework/docs/openspec-tasks-mandatory-steps.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

translations = [
    ("Agent Responsibility", "Responsabilidad del Agente"),
    ("The coding agent MUST execute", "El agente de codificación DEBE ejecutar"),
    ("This is NOT optional and cannot be delegated to the user.", "Esto NO es opcional y no puede ser delegado al usuario."),
    ("Implementation Steps", "Pasos de Implementación"),
    ("Agent must perform", "El agente debe realizarlos"),
    ("Prepare Test Environment", "Preparar el Entorno de Pruebas"),
    ("Run Targeted Unit Tests First", "Ejecutar Pruebas Unitarias Específicas Primero"),
    ("Run Broader Unit Test Suite", "Ejecutar Suite de Pruebas Unitarias Amplia"),
    ("Verify Post-Test Database State", "Verificar Estado de la Base de Datos Post-Prueba"),
    ("Create Unit Test Verification Report in Spec Folder", "Crear Reporte de Verificación de Pruebas Unitarias en la Carpeta de Specs"),
    ("Mark Task as Completed", "Marcar Tarea como Completada"),
    ("Report Template", "Plantilla de Reporte"),
    ("Commands Executed", "Comandos Ejecutados"),
    ("Unit Test Results", "Resultados de Pruebas Unitarias"),
    ("Database State Verification", "Verificación del Estado de la Base de Datos"),
    ("Outcome", "Resultado"),
    ("Dependencies", "Dependencias"),
    ("Notes", "Notas"),
    ("When This Applies", "Cuándo Aplica Esto"),
    ("Example Structure", "Estructura de Ejemplo"),
    ("Agent Execution Requirements", "Requisitos de Ejecución del Agente"),
    ("Never Delegate Testing", "Nunca Delegar Pruebas"),
    ("Document Test Execution", "Documentar la Ejecución de Pruebas"),
    ("Failure to Follow", "Consecuencias de Incumplimiento")
]

for eng, esp in translations:
    content = content.replace(eng, esp)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

