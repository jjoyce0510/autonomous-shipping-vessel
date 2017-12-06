#!/bin/bash
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo pigpiod
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
cd /home/pi/autonomous-shipping-vessel

touch boot.log
echo "Start 1 try" >> boot.log
python -m src.main.python.Main >> boot.log
echo "Completed 1 try" >> boot.log
exit 1
#until python -m src.main.python.Main >> boot.log
#do
#    sleep 0.1
#    echo "=========================================" >> boot.log
#done
