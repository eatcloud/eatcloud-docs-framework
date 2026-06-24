import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

targets = [
    "login-url-única.aspx",
    "Multi-nube--caracterización.aspx",
    "login-url-unica.aspx",
    "Multi-nube.aspx"
]

search_url = "https://graph.microsoft.com/v1.0/search/query"
payload = {
  "requests": [{
      "entityTypes": ["listItem"],
      "query": {"queryString": f'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/"'},
      "size": 500
  }]
}
req_s = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
with urllib.request.urlopen(req_s) as response:
    data = json.loads(response.read().decode())
    hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
    names = []
    for h in hits:
        resource = h.get('resource', {})
        name = resource.get('name', '')
        if name.endswith('.aspx'):
            names.append(name)
            if "login" in name.lower() or "nube" in name.lower():
                print(f"Match parcial encontrado: {name}")

print("\n¿Están los targets directos en la lista extraída de search?")
for t in targets:
    if t in names:
        print(f"SÍ -> {t}")
    else:
        print(f"NO -> {t}")
