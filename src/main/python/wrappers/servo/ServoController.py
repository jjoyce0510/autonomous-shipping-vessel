import time
time.sleep(1)
import pigpio

# Created by John Joyce November 7, 2017
class ServoController:
    SERVO_PIN = 17
    MIN_PULSE_VALUE = 600
    MAX_PULSE_VALUE = 2100
    MIN_ANGLE_VALUE = -30.0
    MAX_ANGLE_VALUE = 30.0

    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.SERVO_PIN, 0)
        self.currentAngle = 0.0
        self.currentPWM = 0.0

    def setAngle(self, angle):
        pulseWidth = self.translateAngleToPulseWidth(angle) + self.MIN_PULSE_VALUE
        if self.isInPWMRange(pulseWidth):
            self.currentAngle = angle
            self.currentPWM = pulseWidth
            self.pi.set_servo_pulsewidth(self.SERVO_PIN, pulseWidth)

    def getAngle(self):
        return self.currentAngle

    def moveRightByAngle(self, angle):
        # Decrement angle
        decPulseWidth = self.translateAngleToPulseWidth(angle)
        newPulseWidth = self.currentPWM - decPulseWidth
        if self.isInPWMRange(newPulseWidth):
            self.currentPWM = newPulseWidth
            self.currentAngle = self.currentAngle - angle
            self.pi.set_servo_pulsewidth(self.SERVO_PIN, newPulseWidth)

    def moveLeftByAngle(self, angle):
        # Inc angle
        incPulseWidth = self.translateAngleToPulseWidth(angle)
        newPulseWidth = self.currentPWM + incPulseWidth
        if self.isInPWMRange(newPulseWidth):
            self.currentPWM = newPulseWidth
            self.currentAngle = self.currentAngle + angle
            self.pi.set_servo_pulsewidth(self.SERVO_PIN, newPulseWidth)

    def translateAngleToPulseWidth(self, angle):
        pwmRange = self.MAX_PULSE_VALUE - self.MIN_PULSE_VALUE
        angleRange = self.MAX_ANGLE_VALUE - self.MIN_ANGLE_VALUE
        distanceFromBase = angle - self.MIN_ANGLE_VALUE
        percentageUsed = distanceFromBase/angleRange
        pwmEquivalent = pwmRange*percentageUsed
        return pwmEquivalent

    def isInPWMRange(self, pulseWidth):
        return pulseWidth >= self.MIN_PULSE_VALUE and pulseWidth <= self.MAX_PULSE_VALUE

