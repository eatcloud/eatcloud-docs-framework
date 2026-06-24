import urllib.request
import urllib.parse
import json
import os
import re

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"
list_id = "bf37b155-9ccc-4164-a4c3-89d260ec530b"

critical_pages = [
    "eatcloud-nueva-wapp-donantes.aspx",
    "WAPP-Modernizada--restricción-de-edición-de-donaciones.aspx",
    "WAPP-Modernizada--restricción-de-eliminación-de-donaciones.aspx",
    "WAPP-Modernizada--asignación-de-donación-desde-el-POD-(punto-de-donación).aspx",
    "WAPP-Modernizada--captura-del-campo--lote--obligatoria-por--cua_master-.aspx",
    "WAPP-Modernizada--restricción-para-marcar-como-no-entregadas-las-donaciones-de-un-POD-donaciones.aspx",
    "eatc_kpi_rules-reglas-de-calculo-kpis.aspx",
    "WAPP--Creación-de-Donaciones-por-archivo-plano--integración-de-clasificadores.aspx",
    "onboarding-de-beneficiarios.aspx",
    "onboarding-de-cuentas.aspx",
    "d-generación-de-certificado-de-donación.aspx"
]

out_dir = "/Users/usuario2/Documents/eatcloud-docs-framework/raw_docs"
os.makedirs(out_dir, exist_ok=True)

def strip_html(html_str):
    # Remueve tags HTML pero preserva algo de estructura (saltos de línea en p, div, br)
    text = re.sub(r'<(p|div|br|li)[^>]*>', '\n', html_str, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    # Limpiar espacios y saltos múltiples
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

for page_name in critical_pages:
    print(f"Buscando el ID de la página: {page_name}...")
    filter_query = urllib.parse.quote(f"fields/FileLeafRef eq '{page_name}'")
    url_items = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items?$expand=fields&$filter={filter_query}"
    
    req_items = urllib.request.Request(url_items, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req_items) as response:
            data = json.loads(response.read().decode())
            if not data.get('value'):
                print(f"  -> No encontrada en la lista de items.")
                continue
            
            item = data['value'][0]
            item_id = item['id']
            title = item.get('fields', {}).get('Title', page_name)
            
            print(f"  -> ID encontrado: {item_id}. Extrayendo contenido profundo vía Graph Beta...")
            
            # Usar endpoint de Graph Beta para sacar el texto extraído de la página (Client-Side Pages)
            # A veces pages API requiere el ID de la página, que es distinto al listItemId. 
            # Pero en Graph v1 /beta/sites/../pages/ permite usar el listItemId si se provee adecuadamente, o podemos buscar el page ID.
            
            # Un atajo muy confiable en SharePoint Online es leer el campo CanvasContent1 que a veces sí viene o 
            # usar el endpoint de DriveItem contents
            
            drive_item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/driveItem"
            req_drive = urllib.request.Request(drive_item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
            with urllib.request.urlopen(req_drive) as drive_res:
                drive_data = json.loads(drive_res.read().decode())
                download_url = drive_data.get('@microsoft.graph.downloadUrl')
                
                if download_url:
                    req_dl = urllib.request.Request(download_url)
                    with urllib.request.urlopen(req_dl) as dl_res:
                        html_content = dl_res.read().decode('utf-8', errors='ignore')
                        
                        # Extraer solo el contenido de los Canvas/WebParts (donde se guarda el texto)
                        # Buscamos JSON incrustados en data-sp-canvascontrol
                        blocks = []
                        matches = re.finditer(r'data-sp-canvascontrol[^>]+>([\s\S]*?)</div>', html_content)
                        for m in matches:
                            block_html = m.group(1)
                            clean_text = strip_html(block_html)
                            if len(clean_text) > 10:
                                blocks.append(clean_text)
                        
                        # Fallback por si la estructura cambia
                        if not blocks:
                            # Buscar bloques RTE (Rich Text Editor)
                            rte_matches = re.finditer(r'<div[^>]*data-sp-rte[^>]*>([\s\S]*?)</div>', html_content)
                            for m in rte_matches:
                                clean_text = strip_html(m.group(1))
                                if len(clean_text) > 10:
                                    blocks.append(clean_text)
                                    
                        if not blocks:
                            # Otro fallback: Extraer todo el JSON del estado de la página
                            json_matches = re.findall(r'CanvasContent1"\s*:\s*"((?:\\"|[^"])*)"', html_content)
                            for j in json_matches:
                                try:
                                    decoded = j.replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r')
                                    clean_text = strip_html(decoded)
                                    if len(clean_text) > 10:
                                        blocks.append(clean_text)
                                except:
                                    pass

                        final_text = "\n\n".join(blocks)
                        
                        if final_text.strip():
                            filepath = os.path.join(out_dir, f"{page_name}.md")
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(f"# {title}\n\n{final_text}")
                            print(f"  -> ¡Éxito! Contenido guardado. Longitud: {len(final_text)} caracteres.")
                        else:
                            print("  -> Contenido vacío o no pudo ser parseado.")
                else:
                    print("  -> No se encontró Download URL.")

    except Exception as ex:
        print(f"  -> Error: {ex}")

print("\nProceso finalizado.")
