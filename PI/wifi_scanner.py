import platform
import subprocess
import json
import os
import nmcli
import time


class WifiScanner:
    def __init__(self):
        self.os_computer = platform.system()
        self.wifi_networks = {}
        self.deauth = False

    def start(self):
        while True:
            self.read_json()
            self.get_networks()
            self.log_results()
            #self.pushFile()

    def get_networks(self):
        if self.os_computer == 'Windows':
            command = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True).stdout
            self.parse_networks_windows(command)
        if self.os_computer == 'Linux':
            self.parse_networks_linux()

    def parse_networks_windows(self, command):
        current_ssid = None

        for line in command.splitlines():
            if "SSID" in line:
                current_ssid = line.split(":")[1].strip()
                self.wifi_networks[current_ssid] = {}
            elif current_ssid:
                parts = line.split(" : ")
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip()
                    self.wifi_networks[current_ssid][key] = value

    def checkMode(self, connectionSecurity):
        if connectionSecurity == "":
            return "OPEN"
        elif connectionSecurity == "WEP":
            return "WEP"
        elif connectionSecurity == "WPA1":
            return "WPA1"
        elif connectionSecurity == "WPA2":
            return "WPA2"
        elif connectionSecurity == "WPA3":
            return "WPA3"

    def parse_networks_linux(self):
        global connections
        connections = nmcli.device.wifi()

        for connection in connections:
            self.wifi_networks = {
                "SSID": connection.ssid,
                "MODE": connection.mode,
                "CHAN": connection.chan,
                "RATE": connection.rate,
                "SIGNAL": connection.signal,
                "SECURITY": self.checkMode(connection.security),
                "BSSID": connection.bssid,
                "TIMESTAMP": time.time(),
                "COORDS": "TODO"
            }

    ### MOETEN NOG TESTEN
    def pushFile(self):
        if os.popen("ping -c 3 1.1.1.1 &> /dev/null").read():
            os.system('./home/franco/Desktop/wifi-scanner/GithubScripts/GithubPush.sh')

    def read_json(self):
        if not os.path.exists('scan.json'):
            with open('scan.json', 'w') as file:
                json.dump({}, file)

        with open('scan.json', 'r') as file:
            self.wifi_networks = json.load(file)

    def log_results(self):
        with open('scan.json', 'w') as file:
            json.dump(self.wifi_networks, file, indent=4)
