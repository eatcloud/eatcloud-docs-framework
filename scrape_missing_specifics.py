import urllib.request
import json
import os
import re
import html

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

targets = [
    "frameworks-de-desarrollo.aspx",
    "mapa-público.aspx"
]

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"

def deep_decode(text):
    prev = ""
    while text != prev:
        prev = text
        text = html.unescape(text)
    return text

def extract_text_from_html(html_str):
    decoded = deep_decode(html_str)
    decoded = decoded.replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r')
    decoded = decoded.replace('\\u003c', '<').replace('\\u003e', '>')
    clean = re.sub(r'<(p|div|br|li|h[1-6])[^>]*>', '\n', decoded, flags=re.IGNORECASE)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n', '\n\n', clean)
    return clean.strip()

for page_name in targets:
    print(f"\nBuscando explícitamente: {page_name}...")
    search_url = "https://graph.microsoft.com/v1.0/search/query"
    payload = {
      "requests": [{
          "entityTypes": ["listItem"],
          "query": {"queryString": f'"{page_name}" OR path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/{page_name}"'},
          "size": 5
      }]
    }

    req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req_search) as response:
            data = json.loads(response.read().decode())
            hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
            
            if not hits:
                print(f"  [X] No encontrada vía Search API.")
                continue
                
            hit = hits[0]
            res = hit.get('resource', {})
            list_id = res.get('sharepointIds', {}).get('listId')
            item_id = res.get('sharepointIds', {}).get('listItemId')
            title = hit.get('summary', page_name)
            
            print(f"  [!] ID resuelto: {item_id}. Descargando...")
            
            drive_item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/driveItem"
            req_drive = urllib.request.Request(drive_item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
            
            with urllib.request.urlopen(req_drive) as drive_res:
                drive_data = json.loads(drive_res.read().decode())
                download_url = drive_data.get('@microsoft.graph.downloadUrl')
                
                if download_url:
                    req_dl = urllib.request.Request(download_url)
                    with urllib.request.urlopen(req_dl) as dl_res:
                        raw_file_content = dl_res.read().decode('utf-8', errors='ignore')
                        
                        blocks = []
                        canvas_matches = re.findall(r'CanvasContent1"[^>]*>([\s\S]*?)<', raw_file_content)
                        if not canvas_matches:
                            canvas_matches = re.findall(r'CanvasContent1"\s*:\s*"((?:\\"|[^"])*)"', raw_file_content)
                        
                        if canvas_matches:
                            for match in canvas_matches:
                                extracted = extract_text_from_html(match)
                                if len(extracted) > 10:
                                    blocks.append(extracted)
                        else:
                            extracted = extract_text_from_html(raw_file_content)
                            blocks.append(extracted)

                        final_text = "\n\n".join(blocks)
                        
                        filepath = os.path.join(out_dir, f"{page_name}.md")
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(f"# {page_name}\n\n{final_text}")
                            
                        print(f"  [V] Éxito: Guardado con {len(final_text)} caracteres.")
                else:
                    print(f"  [X] Fallo: El archivo no tiene URL de descarga directa.")
                    
    except Exception as ex:
        print(f"  [X] Error al procesar: {ex}")

print("\nFinalizado script de casos especiales.")
