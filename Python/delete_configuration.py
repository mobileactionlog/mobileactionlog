import requests;
r = requests.delete('http://localhost:8080/configuration', auth=('admin', 'admin'))
print(r.status_code)
print(r.content)
