from src.main.python.wrappers.servo.ServoController import ServoController
from src.main.python.wrappers.motor.MotorController import MotorController

# Singleton holding the controls of the vessel, always use GETINSTANCE
class VesselControls:
    servo = None
    motor = None

    def getCurrentVelocity(self):
        return self.motor.getVelocity()

    def getCurrentAngle(self):
        return self.servo.getAngle()

    def setVelocity(self, velocity):
        self.motor.setVelocity(velocity)

    def setAngle(self, angle):
        self.servo.setAngle(angle)

    def setAngleAndVelocity(self, angle, velocity):
        self.setAngle(angle)
        self.setVelocity(velocity)

