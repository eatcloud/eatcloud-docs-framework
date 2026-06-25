import urllib.request
import json
import os
import re
import html
from urllib.parse import quote

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"
drive_id = "b!AwIMMxcGnke5tQngVkgHjl1P49PTupRGjjDbYcbD8Ln4BmhcnsFPRZLjDqj85Pkr"

page_name = "data-analytics.aspx"

url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{quote(page_name)}"
print(f"URL: {url}")
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
try:
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode())
        print(f"ID del archivo: {data.get('id')}")
        download_url = data.get('@microsoft.graph.downloadUrl')
        if download_url:
            print("Download URL encontrado.")
            req_dl = urllib.request.Request(download_url)
            with urllib.request.urlopen(req_dl) as dl_res:
                raw_html = dl_res.read().decode('utf-8', errors='ignore')
                print(f"HTML descargado, len: {len(raw_html)}")
        else:
            print("Sin Download URL")
except Exception as e:
    print(f"Error: {e}")
