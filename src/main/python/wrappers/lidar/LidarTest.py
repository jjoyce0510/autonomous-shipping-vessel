from Lidar import Lidar
import time
lidar = Lidar()

while True:
    print lidar.getDistance()
    time.sleep(0.5)