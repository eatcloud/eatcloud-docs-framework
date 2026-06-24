import urllib.request
import json
import os
import re

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Lista de las páginas más críticas para la Fase 1
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

search_url = "https://graph.microsoft.com/v1.0/search/query"
payload = {
  "requests": [{
      "entityTypes": ["listItem"],
      "query": {"queryString": 'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages" AND (WAPP OR BO OR Informes OR "nueva wapp" OR kpi OR onboarding)'},
      "size": 100
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
            web_url = res.get('webUrl', '')
            name = web_url.split('/')[-1]
            
            # Filtramos solo las que marcamos como críticas
            if name in critical_pages:
                list_id = res.get('sharepointIds', {}).get('listId')
                item_id = res.get('sharepointIds', {}).get('listItemId')
                
                # Obtener el contenido del item
                item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}?$expand=fields"
                req_item = urllib.request.Request(item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
                try:
                    with urllib.request.urlopen(req_item) as item_res:
                        item_data = json.loads(item_res.read().decode())
                        fields = item_data.get('fields', {})
                        
                        title = fields.get('Title', 'Untitled').replace('/', '-')
                        content = fields.get('CanvasContent1', '') or fields.get('WikiField', '')
                        
                        # Limpieza básica de HTML a Texto
                        text = re.sub('<[^<]+?>', '\n', content)
                        text = re.sub('\n+', '\n', text).strip()
                        
                        filepath = os.path.join(out_dir, name + ".md")
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(f"# {title}\nURL original: {web_url}\n\n{text}")
                        extracted_files.append(name)
                except Exception as ex:
                    print(f"Error extrayendo {name}: {ex}")
                    
        print(f"\nExtracción de Páginas Críticas completada. {len(extracted_files)} archivos guardados en {out_dir}")
        for f in extracted_files:
            print(f"- {f}")
except Exception as e:
    print(f"Error general: {e}")
