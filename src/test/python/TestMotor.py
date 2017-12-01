from src.main.python.wrappers.motor.MotorController import MotorController
from src.main.python.exceptions.HardwareException import HardwareException
import time

class TestMotor:
    motorController = MotorController()

    def __init__(self):
        self.testVelocity()

    def testVelocity(self):
        self.motorController.start()
        self.motorController.setVelocity(0.0)
        print self.motorController.getVelocity()
        time.sleep(4.0)
        self.motorController.setVelocity(15.0)
        print self.motorController.getVelocity()
        time.sleep(15.0)
        self.motorController.stop()


