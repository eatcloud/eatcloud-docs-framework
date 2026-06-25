import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages"
req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})

pages_list = []
try:
    while url_pages:
        req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for page in data.get('value', []):
                name = page.get('name', '')
                if name.endswith('.aspx'):
                    pages_list.append(name)
            url_pages = data.get('@odata.nextLink')
except Exception as e:
    print(f"Error Beta API Pages: {e}")

print(f"Pages found via Beta API: {len(pages_list)}")
for p in pages_list[:5]:
    print(" -", p)
