import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Intentar endpoint global de paginas para el sitio
url_pages = f"https://graph.microsoft.com/v1.0/sites/{site_id}/pages"
req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})

all_pages = []
try:
    with urllib.request.urlopen(req) as response:
        pages_data = json.loads(response.read().decode())
        for p in pages_data.get('value', []):
            name = p.get('name', '')
            if name.endswith('.aspx'):
                all_pages.append(name)
except Exception as e:
    print(f"Error con /pages: {e}")

# Si falla, vamos a buscar por query la lista "Páginas del sitio" exacta
if not all_pages:
    url_lists = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists"
    req_lists = urllib.request.Request(url_lists, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req_lists) as response:
            lists_data = json.loads(response.read().decode())
            list_id = None
            for l in lists_data.get('value', []):
                name = l.get('name', '').lower()
                disp = l.get('displayName', '').lower()
                if 'page' in name or 'page' in disp or 'página' in disp or 'pagina' in disp:
                    list_id = l['id']
                    
            if list_id:
                url_items = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items?$expand=fields"
                req_items = urllib.request.Request(url_items, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
                with urllib.request.urlopen(req_items) as r2:
                    items_data = json.loads(r2.read().decode())
                    for i in items_data.get('value', []):
                        fn = i.get('fields', {}).get('FileLeafRef', '')
                        if fn.endswith('.aspx'):
                            all_pages.append(fn)
    except Exception as e:
        print(f"Error con list items fallback: {e}")

# Segundo fallback con Search API para listar todo
if not all_pages:
    print("Usando Search API fallback...")
    search_url = "https://graph.microsoft.com/v1.0/search/query"
    payload = {
      "requests": [{
          "entityTypes": ["listItem"],
          "query": {"queryString": f'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/" fileType:aspx'},
          "size": 500
      }]
    }
    req_s = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req_s) as response:
            data = json.loads(response.read().decode())
            hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
            for h in hits:
                resource = h.get('resource', {})
                name = resource.get('name', '')
                if name.endswith('.aspx'):
                    all_pages.append(name)
    except Exception as e:
        print(f"Error Search: {e}")

print(f"Total found: {len(all_pages)}")

raw_docs_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
existing_files = [f.replace('.md', '') for f in os.listdir(raw_docs_dir) if f.endswith('.md')]

missing_pages = list(set([p for p in all_pages if p not in existing_files]))

with open('/Users/usuario2/Documents/eatcloud-docs-framework/missing_pages.json', 'w', encoding='utf-8') as f:
    json.dump(missing_pages, f, indent=2, ensure_ascii=False)

print(f"Faltantes: {len(missing_pages)}")
