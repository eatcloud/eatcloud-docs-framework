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
    pass

blacklist_keywords = [
    "bcp", "recursos-humanos", "marketing", "procesos-de-soporte", "vacaciones",
    "plan-de-continuidad", "rrhh", "comunicado", "directorio", "cumpleaños", "bienestar",
    "nomina", "plantilla", "entrevista", "navidad", "fiesta", "evento", "boletin"
]

raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

filtered_pages = []
for p in pages_list:
    p_lower = p.lower()
    if p in existing_files:
        continue
    if any(b in p_lower for b in blacklist_keywords):
        continue
    filtered_pages.append(p)

with open('/Users/usuario2/Documents/eatcloud-docs-framework/target_missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_pages, f, indent=2, ensure_ascii=False)

print(f"Total encontrado: {len(pages_list)}")
print(f"Ya procesadas: {len(existing_files)}")
print(f"Filtradas (basura): {len(pages_list) - len(existing_files) - len(filtered_pages)}")
print(f"NUEVAS por procesar: {len(filtered_pages)}")

print("\nMuestra 10 nuevas:")
for p in filtered_pages[:10]:
    print(" -", p)
