import requests
import json

payload = { "gridType": "STATIC_GRID" }
headers = { "Content-Type": "application/json" }
r = requests.post('http://localhost:8080/configuration', headers=headers, data=json.dumps(payload), auth=('admin', 'admin'))
print(r.status_code)
print(r.content)
