import requests as r

data = {
        "SSID": "Fransen",
        "MODE": "Infra",
        "CHAN": 6,
        "RATE": 130,
        "SIGNAL": 39,
        "SECURITY": "WPA2"
    }

# res = r.post("http://localhost:8080/", json=data)
res = r.get("http://172.16.153.181:8080/")
print(res.content, res.status_code)

