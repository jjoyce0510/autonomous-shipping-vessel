from src.main.python.wrappers.lidar.Lidar import Lidar
from src.main.python.exceptions.HardwareException import HardwareException

class TestLidar:
    lidar = Lidar()

    def __init__(self):
        dist = self.lidar.getDistance()
        print "Distance: " + str(dist)
        if dist <= 0.0:
            raise HardwareException
