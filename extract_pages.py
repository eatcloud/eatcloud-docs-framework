import urllib.request
import json
import os
import re

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

search_url = "https://graph.microsoft.com/v1.0/search/query"
payload = {
  "requests": [{
      "entityTypes": ["listItem"],
      "query": {"queryString": 'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages" AND filetype:aspx'},
      "size": 50
  }]
}

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
os.makedirs(out_dir, exist_ok=True)

extracted_files = []

req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
try:
    with urllib.request.urlopen(req_search) as response:
        data = json.loads(response.read().decode())
        hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
        
        for hit in hits:
            res = hit.get('resource', {})
            list_id = res.get('sharepointIds', {}).get('listId')
            item_id = res.get('sharepointIds', {}).get('listItemId')
            web_url = res.get('webUrl', '')
            
            # Filtramos por las palabras clave de nuestras bases
            targets = ['modernizaci', 'backend', 'api', 'crd', 'error', 'logica-super', 'mapeo-y-carga']
            if any(t.lower() in web_url.lower() for t in targets):
                # Obtener el contenido del item
                item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}?$expand=fields"
                req_item = urllib.request.Request(item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
                with urllib.request.urlopen(req_item) as item_res:
                    item_data = json.loads(item_res.read().decode())
                    fields = item_data.get('fields', {})
                    
                    title = fields.get('Title', 'Untitled').replace('/', '-')
                    file_leaf_ref = fields.get('FileLeafRef', '')
                    content = fields.get('CanvasContent1', '') or fields.get('WikiField', '')
                    
                    # Limpieza básica de HTML a Texto
                    text = re.sub('<[^<]+?>', '\n', content)
                    text = re.sub('\n+', '\n', text).strip()
                    
                    filepath = os.path.join(out_dir, f"{file_leaf_ref}.md")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(f"# {title}\nURL original: {web_url}\n\n{text}")
                    extracted_files.append(file_leaf_ref)
                    
        print(f"\nExtracción completada. {len(extracted_files)} archivos guardados en {out_dir}")
        for f in extracted_files:
            print(f"- {f}")
except Exception as e:
    print(f"Error: {e}")
