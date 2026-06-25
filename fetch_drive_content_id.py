import urllib.request
import json
import os
import re
import html
from urllib.parse import quote

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"
drive_id = "b!AwIMMxcGnke5tQngVkgHjl1P49PTupRGjjDbYcbD8Ln4BmhcnsFPRZLjDqj85Pkr"

# Listar todos los hijos de la carpeta raíz de este Drive para ver sus IDs verdaderos
url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root/children?$top=10"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read().decode())
    print("Muestra de archivos reales dentro de SitePages:")
    for item in data.get('value', []):
        print(f"Name: {item.get('name')}")
