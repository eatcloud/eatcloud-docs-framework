import urllib.request
import json
import os
import re
import html
from urllib.parse import quote

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

with open('/Users/usuario2/Documents/eatcloud-docs-framework/target_missing_pages.json', 'r', encoding='utf-8') as f:
    missing_pages = json.load(f)

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
os.makedirs(out_dir, exist_ok=True)

def strip_html(html_str):
    decoded = html.unescape(html_str)
    decoded = decoded.replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r')
    decoded = decoded.replace('\\u003c', '<').replace('\\u003e', '>')
    clean = re.sub(r'<(p|div|br|li|h[1-6])[^>]*>', '\n', decoded, flags=re.IGNORECASE)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'[ \t]+', ' ', clean)
    clean = re.sub(r'\n\s*\n', '\n\n', clean)
    return clean.strip()

print("Usando Beta API para leer webParts...")
success = 0
errors = 0

# Limitaremos la muestra para verificar que funciona
for page_name in missing_pages[:15]:
    print(f"\nProcesando: {page_name}")
    
    # Obtener la pagina via beta api para leer su webparts
    url = f"https://graph.microsoft.com/beta/sites/{site_id}/pages/{quote(page_name)}?$expand=webparts"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            webparts = data.get('webparts', [])
            
            blocks = []
            for wp in webparts:
                wp_type = wp.get('innerHtml', '')
                if wp_type:
                    ext = strip_html(wp_type)
                    if len(ext) > 10: blocks.append(ext)
            
            final_text = "\n\n".join(blocks)
            if len(final_text.strip()) > 0:
                filepath = os.path.join(out_dir, f"{page_name}.md")
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# {page_name}\n\n{final_text}")
                print(f"  -> OK ({len(final_text)} chars)")
                success += 1
            else:
                # Si no tiene innerHtml, tal vez es el title u otras props
                title = data.get('title', '')
                desc = data.get('description', '')
                final_text = strip_html(f"{title}\n{desc}")
                
                if len(final_text) > 1:
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

print(f"\nFinalizado test. Exitos: {success}, Errores: {errors}")
