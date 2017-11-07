import smbus
import time

# Created by John Joyce on November 7
# Returns distance to closest object in cm
class Lidar:
    DEFAULT_BUS = 1

    def __init__(self):
        self.address = 0x62
        self.distWriteReg = 0x00
        self.distWriteVal = 0x04
        self.distReadReg1 = 0x8f # This may not be correct, needs testing.
        self.distReadReg2 = 0x10
        self.velWriteReg = 0x04
        self.velWriteVal = 0x08
        self.velReadReg = 0x09
        self.bus = None

        if self.connect(self.DEFAULT_BUS) == 0:
            print "Connected to LiDAR successfully."
        else:
            print "Unable to connect to LiDAR on bus " + self.DEFAULT_BUS

    def connect(self, bus):
        try:
            self.bus = smbus.SMBus(bus)
            time.sleep(0.5)
            return 0
        except:
            return -1

    def writeAndWait(self, register, value):
        self.bus.write_byte_data(self.address, register, value);
        time.sleep(0.02)

    def readAndWait(self, register):
        res = self.bus.read_byte_data(self.address, register)
        time.sleep(0.02)
        return res

    def getDistance(self):
        self.writeAndWait(self.distWriteReg, self.distWriteVal)
        dist1 = self.readAndWait(self.distReadReg1)
        dist2 = self.readAndWait(self.distReadReg2)
        return (dist1 << 8) + dist2

    def getVelocity(self):
        self.writeAndWait(self.distWriteReg, self.distWriteVal)
        self.writeAndWait(self.velWriteReg, self.velWriteVal)
        vel = self.readAndWait(self.velReadReg)
        return self.signedInt(vel)

    def signedInt(self, value):
        if value > 127:
            return (256-value) * (-1)
        else:
            return value
