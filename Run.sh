#!/bin/bash

# Pull van project
if ping -c 3 1.1.1.1 &> /dev/null; then
                echo "wifi"
                #cd /home/franco/Desktop/wifi-scanner
                #./home/franco/Desktop/wifi-scanner/GithubScripts/GithubPull.sh

# Als er geen wifi is start het script
else
                echo "geen wifi"
                #/home/franco/Desktop/wifi-scanner/newvenv/bin/python3 /home/franco/Desktop/wifi-scanner/main.py

fi




# Output files van PI exporteren naar git
if [ -f /scan.json ]; then
	sudo cp /scan.json /home/franco/Desktop/wifi-scanner/Output/scan.json
fi

if [ -f /devices.txt ]; then
	sudo cp /devices.txt /home/franco/Desktop/wifi-scanner/Output/devices.txt
fi
