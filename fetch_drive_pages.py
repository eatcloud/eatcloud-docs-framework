import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# Encontrar el drive correcto que contiene las aspx
url_drives = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
req = urllib.request.Request(url_drives, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read().decode())
    for d in data.get('value', []):
        print(f"Drive: {d.get('name')} | ID: {d.get('id')}")
