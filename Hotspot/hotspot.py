import subprocess
import time
from flask import Flask, render_template
import json

#
#
# sudo apt-get update
# sudo apt-get install createap
#
#

app = Flask(__name__)

json_data = "Output/scan_json"

def index():
    return render_template('index.html', data=json_data)

def Start_Hotspot():
    subprocess.run(['sudo', 'create_ap', 'wlan0', 'wlan0', 'YourHotspotName', 'YourPassword'])

def Stop_Hotspot():
    subprocess.run(['sudo', 'killall', 'create_ap'])



if __name__ == '__main__': 
    try:
        Start_Hotspot()
        app.run(host='192.168.0.1', port=80, debug=True)
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        Stop_Hotspot()
