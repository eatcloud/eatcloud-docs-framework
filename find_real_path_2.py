import urllib.request
import json
import os
import re
import html

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

url_pages = f"https://graph.microsoft.com/beta/sites/{site_id}/pages?$top=500"
req = urllib.request.Request(url_pages, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})

found_pages = []
try:
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        for p in data.get('value', []):
            found_pages.append(p)
            if "data-analytics" in p.get('name', '').lower() or "frameworks-de-desarrollo" in p.get('name', '').lower():
                print(f"Name: {p.get('name')} | WebUrl: {p.get('webUrl')} | ID: {p.get('id')}")
except Exception as e:
    print(f"Error: {e}")

print(f"Total en este lote de beta/pages: {len(found_pages)}")
if len(found_pages) > 0:
    print("Example 1:", found_pages[0].get('name'), " -> ", found_pages[0].get('webUrl'))

