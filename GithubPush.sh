#!/bin/bash

cp /scan.json ~/Desktop/wifi-scanner/scan.json
cd ~/Desktop/wifi-scanner
git add scan.json
git commit -m "PUSH SCAN FILE"
git push origin master
