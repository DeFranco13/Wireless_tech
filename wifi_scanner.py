import platform
import subprocess
import json
import os
import nmcli
import nmap

class WifiScanner:
   def __init__(self):
      self.os_computer = platform.system()
      self.wifi_networks = {}
      self.deauth = False

   def start(self):
      while True:
         self.read_json()
         self.get_networks()
         self.sniff_wifi()
         self.get_handshake()
         self.deauth_wifi()
         self.log_results()
         self.pushFile()

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

   def parse_networks_linux(self):
       global connections
       connections = nmcli.device.wifi()

       for connection in connections:
           ssid = connection.ssid
           self.wifi_networks[ssid] = {
              "MODE": connection.mode,
              "CHAN": connection.chan,
              "RATE": connection.rate,
              "SIGNAL": connection.signal,
              "SECURITY": connection.security,
           }

   def get_handshake(self):
       for connection in connections:
           if connection.security == "WPA2" | connection.security == "WPA3" | connection.security == "WPA1":
              os.system(f'airodump-ng -c {connection.chan} --bssid {connection.ssid} -w HandshakeOf{connection.ssid} wlan0')

   def deauth_wifi(self):
       if self.deauth == True:
          for connection in connections:
              os.system(f'aireplay-ng -0 1 -a')

   def sniff_wifi(self):
       for connection in connections:
           if connection.security == "":
              os.system(f'nmcli -a d wifi connect {connection.bssid}')
              device_scan = nmap.PortScanner()
              device = device_scan.scan("192.168.2.1/24", arguments='-sn', sudo=True)
              os.system(f'nmcli c delete {connection.bssid}')

   def pushFile():
       if ping -c 3 1.1.1.1 &> /dev/null ; then
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
