# This class serves as the ships 'bootloader', it ensures our devices are working and manages stuff
import sys
from exceptions.HardwareException import HardwareException
from exceptions.BluetoothException import BluetoothException
from factories.VesselDriverFactory import VesselDriverFactory
from control.Trip import Trip
from wrappers.gps.Coordinates import Coordinates
from BluetoothManager import BluetoothManager

class Bootloader:
    driver = VesselDriverFactory.createInstance()

    def __init__(self):
        try:
            self.validate()
        except HardwareException, e:
            sys.stderr.write('Failed to validate on-board hardware '+ str(e))
            sys.exit(0)

        self.launchDriver()


    def validate(self):
        self.validateGPS()
        self.validateLidar()
        self.validateCamera()
        self.validateMotor()
        self.validateServo()

    #TODO: Validate hardware
    def validateGPS(self):
        pass

    def validateLidar(self):
        pass

    def validateCamera(self):
        pass

    def validateMotor(self):
        pass

    def validateServo(self):
        pass

    def launchDriver(self):
        btManager = BluetoothManager()
        try:
            btManager.connect()
            data = btManager.getData()
        except BluetoothException, e: #TODO: Implement this exception
            sys.stderr.write("Failed to establish bluetooth connection" + str(e))

        coordinates = self.parseCoordinates(data)

        if coordinates:
            trip = Trip()
            trip.setDestinationCoordinates(coordinates)
            self.driver.setTrip(trip)
            self.driver.drive()


    def parseCoordinates(self, data):
        if not data:
            return None
        else:
            return Coordinates(data.getKey("lat"), data.getKey("long"))