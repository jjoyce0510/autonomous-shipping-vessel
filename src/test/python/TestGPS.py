from src.main.python.wrappers.gps.GPS import GPS
from src.main.python.exceptions.HardwareException import HardwareException

class TestGPS:

    def __init__(self):
        self.gps = GPS()
        self.testCoordinates()
        self.testHeading()

    def testCoordinates(self):
        coord = self.gps.getCoord()
        print coord.getLat()
        print coord.getLon()
        if coord.getLon() is "" or coord.getLat() is  "":
            raise HardwareException("Invalid GPS coordinates.")

    def testHeading(self):
        print self.gps.getHeading()
        if self.gps.getHeading() is "":
            raise HardwareException("Invalid GPS heading.")
