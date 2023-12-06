#!/bin/bash

# Pull van project

if ping -c 3 1.1.1.1 &> /dev/null; then
	./home/franco/Desktop/wifi-scanner/GithubScripts/GithubPull.sh

# Opstart script enkel als er geen wifi is

else /home/franco/Desktop/wifi-scanner/newvenv/bin/python3 /home/franco/Desktop/wifi-scanner/main.py

fi

# Output files van PI exporteren naar git folder

if [ -f /scan.json ] ; then
	sudo cp /scan.json /home/franco/Desktop/wifi-scanner/Output/scan.json

if [ -f /devices.txt ] ; then
	sudo cp /devices.txt /home/franco/Desktop/wifi-scanner/Output/devices.txt
