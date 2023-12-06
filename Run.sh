#!/bin/bash

# Pull van project

if ping -c 3 1.1.1.1 &> /dev/null; then
	./home/franco/Desktop/wifi-scanner/GithubScripts/GithubPull.sh
fi

# Opstart Script

/home/franco/Desktop/wifi-scanner/newvenv/bin/python3 /home/franco/Desktop/wifi-scanner/main.py
sudo cp /scan.json /home/franco/Desktop/wifi-scanner/Output/scan.json
