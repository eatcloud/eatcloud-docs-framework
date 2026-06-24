import urllib.request
import json
import os
import re

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

critical_pages = [
    "eatcloud-nueva-wapp-donantes.aspx"
]

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
os.makedirs(out_dir, exist_ok=True)

def strip_html(html_str):
    text = re.sub(r'<(p|div|br|li)[^>]*>', '\n', html_str, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

for page_name in critical_pages:
    print(f"Buscando vía Search: {page_name}...")
    search_url = "https://graph.microsoft.com/v1.0/search/query"
    payload = {
      "requests": [{
          "entityTypes": ["listItem"],
          "query": {"queryString": f'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/{page_name}"'},
          "size": 1
      }]
    }

    req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req_search) as response:
        data = json.loads(response.read().decode())
        hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
        hit = hits[0]
        res = hit.get('resource', {})
        list_id = res.get('sharepointIds', {}).get('listId')
        item_id = res.get('sharepointIds', {}).get('listItemId')
        
        drive_item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/driveItem"
        req_drive = urllib.request.Request(drive_item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req_drive) as drive_res:
            drive_data = json.loads(drive_res.read().decode())
            download_url = drive_data.get('@microsoft.graph.downloadUrl')
            
            req_dl = urllib.request.Request(download_url)
            with urllib.request.urlopen(req_dl) as dl_res:
                html_content = dl_res.read().decode('utf-8', errors='ignore')
                with open("test_page_html.txt", "w", encoding="utf-8") as f:
                    f.write(html_content)
                print("Guardado en test_page_html.txt")

