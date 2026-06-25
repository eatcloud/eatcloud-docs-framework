import urllib.request
import json
import os
import re
import html
from urllib.parse import quote
import time

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Leer el JSON original donde mapeamos las 430 páginas ocultas
with open('/Users/usuario2/Documents/eatcloud-docs-framework/target_missing_pages.json', 'r', encoding='utf-8') as f:
    target_pages = json.load(f)

# Si el JSON se vació accidentalmente, restauramos la lista desde la API Beta
if not target_pages:
    print("Recuperando lista de páginas de Beta API...")
    url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages"
    target_pages = []
    try:
        while url_pages:
            req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                for page in data.get('value', []):
                    name = page.get('name', '')
                    if name.endswith('.aspx'):
                        target_pages.append({'name': name, 'id': page.get('id')})
                url_pages = data.get('@odata.nextLink')
    except Exception as e:
        print(f"Error fetching pages: {e}")
        
    print(f"Recuperadas {len(target_pages)} páginas.")
    
    # Filtrar basura y ya procesadas
    blacklist_keywords = ["bcp", "recursos-humanos", "marketing", "procesos-de-soporte", "vacaciones", "plan-de-continuidad", "rrhh", "comunicado", "directorio", "cumpleaños", "bienestar", "nomina", "plantilla", "entrevista", "navidad", "fiesta", "evento", "boletin"]
    existing_files = [f.replace('.md', '') for f in os.listdir("/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs") if f.endswith('.md')]
    
    filtered_pages = []
    for p in target_pages:
        name = p['name']
        if name in existing_files: continue
        if any(b in name.lower() for b in blacklist_keywords): continue
        filtered_pages.append(p)
        
    target_pages = filtered_pages
    print(f"Páginas a procesar tras el filtro: {len(target_pages)}")
else:
    # Si tenemos los nombres como strings, necesitamos buscar sus IDs en la Graph API
    pass

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

print(f"Iniciando extracción quirúrgica de {len(target_pages)} páginas ocultas...")
success = 0
errors = 0

for idx, page_obj in enumerate(target_pages[:100]): # Limitamos a las primeras 100 para no agotar el tiempo
    page_name = page_obj['name']
    page_id = page_obj['id']
    print(f"[{idx+1}/100] Procesando: {page_name}")
    
    # Extraemos el contenido de los WebParts directamente con la API Beta
    url = f"https://graph.microsoft.com/beta/sites/{site_id}/pages/{page_id}?$expand=webparts"
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
                # Fallback: intentar extraer título y descripción si los webparts están vacíos
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
                    print(f"  -> Vacío o sin WebParts legibles")
                    errors += 1
    except Exception as e:
        print(f"  -> Error API: {e}")
        errors += 1
        
    time.sleep(0.2)

print(f"\nLote Finalizado. Exitos: {success}, Errores: {errors}")
