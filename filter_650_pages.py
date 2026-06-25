import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages"

pages_list = []
try:
    while url_pages:
        req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for page in data.get('value', []):
                name = page.get('name', '')
                if name.endswith('.aspx'):
                    pages_list.append(name)
            url_pages = data.get('@odata.nextLink')
except Exception as e:
    print(f"Error fetching pages: {e}")

# Filtro Exclusivo
# Palabras clave que identifican páginas "basura corporativa" (no desarrollo / no técnicas)
blacklist_keywords = [
    "bcp", "recursos-humanos", "marketing", "procesos-de-soporte", "vacaciones",
    "plan-de-continuidad", "rrhh", "comunicado", "directorio", "cumpleaños", "bienestar",
    "nomina", "plantilla", "entrevista", "navidad", "fiesta", "evento", "boletin"
]

# Ya tenemos unas ~200 en raw_docs, vamos a cruzarlas
raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

filtered_pages = []
for p in pages_list:
    p_lower = p.lower()
    
    # 1. Ya la tenemos?
    if p in existing_files:
        continue
        
    # 2. Es basura corporativa?
    if any(b in p_lower for b in blacklist_keywords):
        continue
        
    filtered_pages.append(p)

with open('/Users/usuario2/Documents/eatcloud-docs-framework/target_missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_pages, f, indent=2, ensure_ascii=False)

print(f"Total de páginas encontradas en servidor: {len(pages_list)}")
print(f"Páginas ya procesadas: {len(existing_files)}")
print(f"Páginas nuevas por procesar (Limpias de basura HR/BCP): {len(filtered_pages)}")

print("\nMuestra de las nuevas páginas descubiertas:")
for p in filtered_pages[:20]:
    print(" -", p)
