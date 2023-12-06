#!/bin/bash

# Pull van project

./home/franco/Desktop/wifi-scanner/GithubPull.sh

# Opstart Script

/home/franco/Desktop/wifi-scanner/newvenv/bin/python3 /home/franco/Desktop/wifi-scanner/main.py
sudo cp /scan.json /home/franco/Desktop/wifi-scanner/scan.json
