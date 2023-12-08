import requests as r

data = "Output/scan_json"

res = r.get("http://172.16.153.181:8080/")
print(res.content, res.status_code)

