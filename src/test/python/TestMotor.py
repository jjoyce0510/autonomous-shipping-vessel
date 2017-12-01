from src.main.python.wrappers.motor.MotorController import MotorController
from src.main.python.exceptions.HardwareException import HardwareException
import time

class TestMotor:
    motorController = MotorController()

    def __init__(self):
	self.testVelocity()
        if self.motorController.getVelocity() is 0.0:
            self.testVelocity()
        #else:
            #raise HardwareException()

    def testVelocity(self):
        self.motorController.setVelocity(0.0)
        print self.motorController.getVelocity()
	time.sleep(4.0)
        self.motorController.setVelocity(10.0)
        print self.motorController.getVelocity()
        time.sleep(2.0)
        self.motorController.setVelocity(10.0)
        print self.motorController.getVelocity()
        time.sleep(2.0)
        self.motorController.setVelocity(10.0)
        print self.motorController.getVelocity()
        time.sleep(2.0)
        self.motorController.setVelocity(10.0)
        print self.motorController.getVelocity()
        time.sleep(2.0)
        self.motorController.setVelocity(0.0)
        print self.motorController.getVelocity()

