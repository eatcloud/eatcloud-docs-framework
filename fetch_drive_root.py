import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_lists = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists"
req = urllib.request.Request(url_lists, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as res:
    data = json.loads(res.read().decode())
    for l in data.get('value', []):
        print(f"List: {l.get('name')} | Display: {l.get('displayName')} | ID: {l.get('id')}")
