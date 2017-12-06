# Singleton holding the controls of the vessel
class VesselControls:
    servo = None
    motor = None

    def __init__(self, motor, servo):
        self.motor = motor
        self.servo = servo

    def getCurrentVelocity(self):
        return self.motor.getVelocity()

    def getCurrentAngle(self):
        return self.servo.getAngle()

    def setVelocity(self, velocity):
        if self.motor.getVelocity() is not velocity:
            self.motor.setVelocity(velocity)

    def setAngle(self, angle):
        self.servo.setAngle(angle)

    def setAngleAndVelocity(self, angle, velocity):
        self.setAngle(angle)
        self.setVelocity(velocity)

    def startMotor(self):
        self.motor.start()

    def stopMotor(self):
        self.motor.stop()
