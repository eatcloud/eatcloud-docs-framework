import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

# We know the page id for "Modernización.aspx" is "82f87138-5d0d-47ff-9817-d5ad68e64980" (from our previous search)
page_id = "82f87138-5d0d-47ff-9817-d5ad68e64980"
url = f"https://graph.microsoft.com/beta/sites/{site_id}/pages/{page_id}?$expand=canvasLayout"

req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    with open("page_test.json", "w") as f:
        json.dump(data, f, indent=2)
print("Done")
