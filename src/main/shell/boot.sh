#!/bin/bash
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo pigpiod
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
cd /home/pi/autonomous-shipping-vessel

#touch boot.log
#echo "==== Starting ====" >> boot.log
#until python -m src.main.python.Main >> boot.log
#do
#    sleep 30
#    echo "=========================================" >> boot.log
#done
