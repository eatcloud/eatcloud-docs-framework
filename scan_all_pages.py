import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Buscar el ID de la lista "Páginas del sitio" o "Site Pages"
url_lists = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists"
req = urllib.request.Request(url_lists, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})

site_pages_list_id = None
try:
    with urllib.request.urlopen(req) as response:
        lists_data = json.loads(response.read().decode())
        for l in lists_data.get('value', []):
            if l.get('name') == 'Site Pages' or l.get('displayName') == 'Páginas del sitio' or l.get('name') == 'Páginas del sitio':
                site_pages_list_id = l['id']
                break
except Exception as e:
    print(f"Error getting lists: {e}")

if not site_pages_list_id:
    # Usar el ID conocido que vimos en las descargas anteriores
    site_pages_list_id = "56a5c987-04d3-4784-9c93-dc690568fcc3"

print(f"Usando List ID: {site_pages_list_id}")

url_items = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{site_pages_list_id}/items?$expand=fields"

all_pages = []

try:
    while url_items:
        req_items = urllib.request.Request(url_items, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req_items) as response:
            items_data = json.loads(response.read().decode())
            for item in items_data.get('value', []):
                fields = item.get('fields', {})
                file_name = fields.get('FileLeafRef', '')
                title = fields.get('Title', '')
                if file_name.endswith('.aspx'):
                    all_pages.append(file_name)
            
            url_items = items_data.get('@odata.nextLink')
except Exception as e:
    print(f"Error paginando: {e}")

with open('/Users/usuario2/Documents/eatcloud-docs-framework/all_sharepoint_pages.json', 'w', encoding='utf-8') as f:
    json.dump(all_pages, f, indent=2, ensure_ascii=False)

print(f"Total páginas encontradas: {len(all_pages)}")

# Verificamos cuáles ya tenemos en raw_docs
raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

missing_pages = [p for p in all_pages if p not in existing_files]

with open('/Users/usuario2/Documents/eatcloud-docs-framework/missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(missing_pages, f, indent=2, ensure_ascii=False)

print(f"Páginas faltantes por extraer: {len(missing_pages)}")
