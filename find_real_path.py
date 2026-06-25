import urllib.request
import json
import os
import re
import html
from urllib.parse import quote

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages?$top=50"
req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read().decode())
    for p in data.get('value', []):
        if "data-analytics" in p.get('name', '').lower() or "mapa" in p.get('name', '').lower():
            print(f"Name: {p.get('name')} | WebUrl: {p.get('webUrl')} | ID: {p.get('id')}")

