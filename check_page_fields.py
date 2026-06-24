import urllib.request
import json
import os

token = os.popen("~/.openclaw/workspace/skills/custom-microsoft-graph/venv/bin/python ~/.openclaw/workspace/skills/custom-microsoft-graph/get_token.py").read().strip()
site_id = "eatcloudcorp.sharepoint.com,330c0203-0617-479e-b9b5-09e05648078e,d3e34f5d-bad3-4694-8e30-db61c6c3f0b9"

search_url = "https://graph.microsoft.com/v1.0/search/query"
payload = {
  "requests": [{
      "entityTypes": ["listItem"],
      "query": {"queryString": 'path:"https://eatcloudcorp.sharepoint.com/sites/EatCloud2/SitePages/eatcloud-nueva-wapp-donantes.aspx"'},
      "size": 1
  }]
}

req_search = urllib.request.Request(search_url, data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
with urllib.request.urlopen(req_search) as response:
    data = json.loads(response.read().decode())
    hit = data.get('value', [])[0].get('hitsContainers', [])[0].get('hits', [])[0]
    res = hit.get('resource', {})
    
    list_id = res.get('sharepointIds', {}).get('listId')
    item_id = res.get('sharepointIds', {}).get('listItemId')
    
    item_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}?$expand=fields"
    req_item = urllib.request.Request(item_url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
    with urllib.request.urlopen(req_item) as item_res:
        item_data = json.loads(item_res.read().decode())
        with open("page_dump.json", "w") as f:
            json.dump(item_data['fields'], f, indent=2)
print("Done")
