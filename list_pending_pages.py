import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

search_url = "https://graph.microsoft.com/v1.0/search/query"
payload = {
  "requests": [{
      "entityTypes": ["listItem"],
      "query": {"queryString": 'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages" AND (WAPP OR BO OR Informes OR "nueva wapp")'},
      "size": 50
  }]
}

req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
try:
    with urllib.request.urlopen(req_search) as response:
        data = json.loads(response.read().decode())
        hits = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])
        
        pages = []
        for hit in hits:
            res = hit.get('resource', {})
            web_url = res.get('webUrl', '')
            name = web_url.split('/')[-1]
            pages.append(name)
            
        print("Páginas encontradas:")
        for p in pages:
            print(f"- {p}")
except Exception as e:
    print(f"Error: {e}")
