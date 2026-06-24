import urllib.request
import urllib.parse
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"
list_id = "bf37b155-9ccc-4164-a4c3-89d260ec530b"

filter_query = urllib.parse.quote("fields/FileLeafRef eq 'eatcloud-nueva-wapp-donantes.aspx'")
url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items?$expand=fields&$filter={filter_query}"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    fields = data['value'][0]['fields']
    with open("fields.json", "w") as f:
        json.dump(fields, f, indent=2)
print("Done")
