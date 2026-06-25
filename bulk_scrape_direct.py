import urllib.request
import json
import os
import re
import html
from urllib.parse import quote

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
drive_id = "b!AwIMMxcGnke5tQngVkgHjl1P49PTupRGjjDbYcbD8Ln4BmhcnsFPRZLjDqj85Pkr"

with open('/Users/usuario2/Documents/eatcloud-docs-framework/target_missing_pages.json', 'r', encoding='utf-8') as f:
    missing_pages = json.load(f)

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
os.makedirs(out_dir, exist_ok=True)

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

print(f"Iniciando descarga DIRECTA (Drive API) de {len(missing_pages)} páginas...")
success = 0
errors = 0

for idx, page_name in enumerate(missing_pages):
    print(f"[{idx+1}/{len(missing_pages)}] {page_name}")
    encoded_name = quote(page_name)
    url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{encoded_name}"
    
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            download_url = data.get('@microsoft.graph.downloadUrl')
            
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
                            ext = extract_text_from_html(match)
                            if len(ext) > 10: blocks.append(ext)
                    else:
                        ext = extract_text_from_html(raw_html)
                        blocks.append(ext)
                        
                    final_text = "\n\n".join(blocks)
                    
                    if len(final_text.strip()) > 0:
                        filepath = os.path.join(out_dir, f"{page_name}.md")
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(f"# {page_name}\n\n{final_text}")
                        print(f"  -> OK ({len(final_text)} chars)")
                        success += 1
                    else:
                        print(f"  -> Vacio")
                        errors += 1
            else:
                print(f"  -> Sin downloadUrl")
                errors += 1
    except Exception as e:
        print(f"  -> Error API: {e}")
        errors += 1

print(f"\nFinalizado. Exitos: {success}, Errores: {errors}")
