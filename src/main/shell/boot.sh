#!/bin/bash
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo pigpiod
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
cd /home/pi/autonomous-shipping-vessel
python -m src.main.python.Bootloader
