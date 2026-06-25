import urllib.request
import json
import os
import re
import html
from urllib.parse import quote
import time

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages"
all_pages = []
try:
    while url_pages:
        req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            for page in data.get('value', []):
                name = page.get('name', '')
                if name.endswith('.aspx'):
                    all_pages.append(name)
            url_pages = data.get('@odata.nextLink')
except Exception as e:
    pass

blacklist = ["bcp", "recursos-humanos", "marketing", "procesos-de-soporte", "vacaciones", "plan-de-continuidad", "rrhh", "comunicado", "directorio", "cumpleaños", "bienestar", "nomina", "plantilla", "entrevista", "navidad", "fiesta", "evento", "boletin"]
existing = [f.replace('.md', '') for f in os.listdir("/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs") if f.endswith('.md')]

filtered = [p for p in all_pages if p not in existing and not any(b in p.lower() for b in blacklist)]

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"

def strip_html(html_str):
    decoded = html.unescape(html_str)
    decoded = decoded.replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r')
    decoded = decoded.replace('\\u003c', '<').replace('\\u003e', '>')
    clean = re.sub(r'<(p|div|br|li|h[1-6])[^>]*>', '\n', decoded, flags=re.IGNORECASE)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n', '\n\n', clean)
    return clean.strip()

print(f"Iniciando Extracción Total por Búsqueda Exacta (Lote de {len(filtered)})...")
success = 0
errors = 0

for idx, page_name in enumerate(filtered):
    print(f"[{idx+1}/{len(filtered)}] {page_name}")
    
    search_url = "https://graph.microsoft.com/v1.0/search/query"
    payload = {
      "requests": [{
          "entityTypes": ["listItem"],
          "query": {"queryString": f'"{page_name}"'},
          "size": 5
      }]
    }

    req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req_search) as response:
            data = json.loads(response.read().decode())
            hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
            
            if not hits:
                print(f"  -> No encontrada.")
                errors += 1
                continue
                
            hit = hits[0]
            res = hit.get('resource', {})
            list_id = res.get('sharepointIds', {}).get('listId')
            item_id = res.get('sharepointIds', {}).get('listItemId')
            
            drive_item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/driveItem"
            req_drive = urllib.request.Request(drive_item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
            
            with urllib.request.urlopen(req_drive) as drive_res:
                drive_data = json.loads(drive_res.read().decode())
                download_url = drive_data.get('@microsoft.graph.downloadUrl')
                
                if download_url:
                    req_dl = urllib.request.Request(download_url)
                    with urllib.request.urlopen(req_dl) as dl_res:
                        raw_html = dl_res.read().decode('utf-8', errors='ignore')
                        
                        blocks = []
                        canvas_matches = re.findall(r'CanvasContent1"[^>]*>([\s\S]*?)<', raw_html)
                        if not canvas_matches:
                            canvas_matches = re.findall(r'CanvasContent1"\s*:\s*"((?:\\"|[^"])*)"', raw_html)
                            
                        if canvas_matches:
                            for match in canvas_matches:
                                ext = strip_html(match)
                                if len(ext) > 10: blocks.append(ext)
                        else:
                            ext = strip_html(raw_html)
                            blocks.append(ext)
                            
                        final_text = "\n\n".join(blocks)
                        
                        if len(final_text.strip()) > 10:
                            filepath = os.path.join(out_dir, f"{page_name}.md")
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(f"# {page_name}\n\n{final_text}")
                            print(f"  -> OK ({len(final_text)} chars)")
                            success += 1
                        else:
                            print(f"  -> Vacio")
                            errors += 1
                else:
                    print(f"  -> Sin URL.")
                    errors += 1
    except Exception as ex:
        print(f"  -> Error API")
        errors += 1
        
    time.sleep(0.1)

print(f"\nFinalizado absoluto. Exitos: {success}, Errores: {errors}")
