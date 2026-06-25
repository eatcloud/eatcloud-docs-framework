import urllib.request
import json
import os
import re
import html
import time
from urllib.parse import quote

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

print(f"Total a procesar: {len(filtered)}")

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

success = 0
errors = 0

for idx, page_name in enumerate(filtered[:200]):
    print(f"[{idx+1}/200] Procesando: {page_name}")
    url = f"https://graph.microsoft.com/beta/sites/{site_id}/pages/{quote(page_name)}?$expand=webparts"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            webparts = data.get('webparts', [])
            
            blocks = []
            for wp in webparts:
                wp_inner = wp.get('innerHtml', '')
                if wp_inner:
                    ext = strip_html(wp_inner)
                    if len(ext) > 10: blocks.append(ext)
            
            final_text = "\n\n".join(blocks)
            if len(final_text.strip()) > 10:
                filepath = os.path.join(out_dir, f"{page_name}.md")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# {page_name}\n\n{final_text}")
                print(f"  -> OK ({len(final_text)} chars)")
                success += 1
            else:
                title = data.get('title', '')
                desc = data.get('description', '')
                final_text = strip_html(f"{title}\n{desc}")
                if len(final_text) > 10:
                    filepath = os.path.join(out_dir, f"{page_name}.md")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(f"# {page_name}\n\n{final_text}")
                    print(f"  -> OK Solo Title/Desc ({len(final_text)} chars)")
                    success += 1
                else:
                    print(f"  -> Vacio")
                    errors += 1
    except Exception as e:
        print(f"  -> Error API: {e}")
        errors += 1
        
    time.sleep(0.1)

print(f"\nFinalizado. Exitos: {success}, Errores: {errors}")
