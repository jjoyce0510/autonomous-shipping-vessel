from src.main.python.wrappers.servo.ServoController import ServoController
from src.main.python.exceptions.HardwareException import HardwareException
import time

class TestServo:
    servoController = ServoController()

    def __init__(self):
	print "running"
        if self.servoController.getAngle() == 0.0:
            self.testAngle()
        else:
            raise HardwareException()


    def testAngle(self):
        self.servoController.setAngle(-30.0)
        print self.servoController.getAngle()
        time.sleep(1.0)
        self.servoController.setAngle(-15.0)
        print self.servoController.getAngle()
        time.sleep(1.0)
        self.servoController.setAngle(0.0)
        print self.servoController.getAngle()
        time.sleep(1.0)
        self.servoController.setAngle(15.0)
        print self.servoController.getAngle()
        time.sleep(1.0)
        self.servoController.setAngle(30.0)
        print self.servoController.getAngle()
        time.sleep(1.0)
        self.servoController.setAngle(0.0)
        print self.servoController.getAngle()
