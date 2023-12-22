#!/bin/bash

cp /scan.json /home/franco/Desktop/wifi-scanner/scan.json
cd /home/franco/Desktop/wifi-scanner
git add scan.json
git commit -m "PUSH SCAN FILE"
git push -f origin master
