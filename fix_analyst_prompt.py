import os

file_path = "/Users/usuario2/Documents/eatcloud-docs-framework/ai-specs/agents/data-analyst.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Reemplazar la mención personal por un rol corporativo
content = content.replace(
    "a menos que el Concejal pida un balance unificado.",
    "a menos que el usuario, Tech Lead o Product Owner solicite expresamente un balance unificado."
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Corregido!")
