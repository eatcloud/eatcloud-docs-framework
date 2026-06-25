import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# 1. Inspect Lists
print("--- LISTS ---")
url_lists = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists"
req = urllib.request.Request(url_lists, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as response:
    lists_data = json.loads(response.read().decode())
    for l in lists_data.get('value', []):
        print(f"List: {l.get('name')} | Display: {l.get('displayName')} | ID: {l.get('id')}")

# 2. Inspect Drives
print("\n--- DRIVES ---")
url_drives = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
req_drives = urllib.request.Request(url_drives, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req_drives) as response:
    drives_data = json.loads(response.read().decode())
    for d in drives_data.get('value', []):
        print(f"Drive: {d.get('name')} | Type: {d.get('driveType')} | ID: {d.get('id')}")
