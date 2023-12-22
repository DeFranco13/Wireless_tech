import requests as r
import time
from random import randint
wpa = ["WPA1", "WPA2", "WPA3", "OPEN", "WEP"]
while True:
    data = {
            "SSID": "Fransen",
            "MODE": "Infra",
            "CHAN": randint(0,30), #16
            "RATE": randint(50, 200),
            "SIGNAL": randint(50,200),
            "SECURITY": wpa[randint(0,len(wpa)-1)] # "WPA1"
        }

    res = r.post("http://localhost:8080/", json=data)
    # res = r.get("http://172.16.153.181:8080/")
    print(res.content, res.status_code)
    time.sleep(0.5)


