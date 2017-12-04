# This class serves as the ships 'bootloader', it ensures our devices are working and manages stuff
import sys
import time
from exceptions.HardwareException import HardwareException
from exceptions.BluetoothException import BluetoothException
from factories.VesselDriverFactory import VesselDriverFactory
from control.Trip import Trip
from wrappers.gps.Coordinates import Coordinates
from BluetoothManagerMock import BluetoothManagerMock
from wrappers.gps.GPS import GPS

from src.test.python.TestGPS import TestGPS
from src.test.python.TestServo import TestServo
from src.test.python.TestMotor import TestMotor
from src.test.python.TestLidar import TestLidar
from src.test.python.TestCamera import TestCamera

class Bootloader():
    driver = VesselDriverFactory().createInstance()

    def __init__(self):
        try:
            self.validate()
            time.sleep(4)
            pass
        except HardwareException, e:
            print str(e) + " Failed to validate hardware."
            sys.exit(0)

        self.launchDriver()

    def validate(self):
        print "Validating..."
        self.validateGPS()
        self.validateLidar()
        #self.validateCamera()
        self.validateMotor()
        self.validateServo()

    def validateGPS(self):
        TestGPS()

    def validateLidar(self):
        TestLidar()

    def validateCamera(self):
        TestCamera()

    def validateMotor(self):
        TestMotor()

    def validateServo(self):
        TestServo()

    def launchDriver(self):
        print "Launching driver"
        btManager = BluetoothManagerMock()
        data = ""
        try:
            btManager.connect()
            data = btManager.getData()
        except BluetoothException, e: #TODO: Implement this exception
            sys.stderr.write("Failed to establish bluetooth connection" + str(e))
	
        coordinates = self.parseCoordinates(data)
 
        if coordinates:
            trip = Trip(GPS())
            trip.setDestinationCoordinates(coordinates)
            self.driver.setTrip(trip)
            self.driver.drive()
            print "We bouta drive bitch."

    def parseCoordinates(self, data):
        if not data:
            return None
        else:
            return Coordinates(data.split()[0], data.split()[1])
