# This class serves as the ships 'bootloader', it ensures our devices are working and manages stuff
import sys
from exceptions.HardwareException import HardwareException
from factories.VesselDriverFactory import VesselDriverFactory
from control.Trip import Trip
from wrappers.gps.Coordinates import Coordinates
class Bootloader:
    vesselFactory = VesselDriverFactory()
    driver = vesselFactory.createInstance()

    def __init__(self):
        try:
            self.validate()
        except HardwareException, e:
            sys.stderr.write('Failed to validate on-board hardware '+ str(e))
            sys.exit(0)
        self.launch()


    def validate(self):
        self.validateGPS()
        self.validateLidar()
        self.validateCamera()
        self.validateMotor()
        self.validateServo()

    def validateGPS(self):

    def validateLidar(self):

    def validateCamera(self):

    def validateMotor(self):

    def validateServo(self):

    def launch(self):
        btManager = BluetoothManager()
        try:
            btManager.connect()
        except BluetoothException, e:
            sys.stderr.write("Failed to establish bluetooth connection" + str(e))
        data = btManager.getData()
        coord = self.parseCoordinates(data)

        if coord:
            trip = Trip()
            trip.setDestinationCoordinates(coord)
            self.driver.setTrip(trip)
            self.driver.drive()


    def parseCoordinates(self, data):
        if not data:
            return None
        else:
            return Coordinates(data.getKey("lat"), data.getKey("long"))