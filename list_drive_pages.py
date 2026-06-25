import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Obtener todos los drives (librerías de documentos) del sitio
url_drives = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
req = urllib.request.Request(url_drives, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})

pages_drive_id = None
try:
    with urllib.request.urlopen(req) as response:
        drives_data = json.loads(response.read().decode())
        for d in drives_data.get('value', []):
            if d.get('name') == 'Páginas del sitio' or d.get('name') == 'Site Pages':
                pages_drive_id = d['id']
                break
except Exception as e:
    print(f"Error drives: {e}")

if not pages_drive_id:
    print("No se encontró el Drive de Páginas del sitio.")
    exit(1)

print(f"Drive ID encontrado: {pages_drive_id}")

# Iterar sobre el contenido del Drive
all_files = []
url_children = f"https://graph.microsoft.com/v1.0/drives/{pages_drive_id}/root/children?$top=500"

try:
    while url_children:
        req_ch = urllib.request.Request(url_children, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req_ch) as response:
            data = json.loads(response.read().decode())
            for item in data.get('value', []):
                name = item.get('name', '')
                if name.endswith('.aspx'):
                    all_files.append(name)
            
            url_children = data.get('@odata.nextLink')
except Exception as e:
    print(f"Error children: {e}")

print(f"Total REAL de páginas en la carpeta: {len(all_files)}")

raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

faltantes = [f for f in all_files if f not in existing_files]

print(f"Páginas que NO teníamos: {len(faltantes)}")

with open('/Users/usuario2/Documents/eatcloud-docs-framework/absolute_missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(faltantes, f, indent=2, ensure_ascii=False)

