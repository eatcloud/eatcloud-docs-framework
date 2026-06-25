import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"
list_id = "56a5c987-04d3-4784-9c93-dc690568fcc3"

all_files = []
url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items?$expand=fields&$top=1000"

try:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for item in data.get('value', []):
            fields = item.get('fields', {})
            filename = fields.get('FileLeafRef', '')
            if filename.endswith('.aspx'):
                all_files.append(filename)
                
except Exception as e:
    print(f"Error fetching from list: {e}")

print(f"Total de páginas reales en la base de datos de SharePoint: {len(all_files)}")

# Comparar con lo que ya tenemos
raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

faltantes = [f for f in all_files if f not in existing_files]

print(f"Páginas que NO teníamos: {len(faltantes)}")

with open('/Users/usuario2/Documents/eatcloud-docs-framework/absolute_missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(faltantes, f, indent=2, ensure_ascii=False)

if len(faltantes) > 0:
    print("Primeras 10 faltantes descubiertas:")
    for m in faltantes[:10]:
        print(" - " + m)
