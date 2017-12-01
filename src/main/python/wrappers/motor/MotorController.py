import time
time.sleep(1)
import pigpio
from threading import Thread

# Created by John Joyce November 7, 2017
class MotorController:
    MOTOR_PIN = 4
    MIN_PULSE_VALUE = 800
    MAX_PULSE_VALUE = 1800
    MIN_VELOCITY = 0.0
    MAX_VELOCITY = 100.0

    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_servo_pulsewidth(self.MOTOR_PIN, 0)
        self.currentVelocity = self.MIN_VELOCITY
        self.currentPWM = self.MIN_PULSE_VALUE
        self.isActive = True
        self.updateThread = Thread(target=self.sendPWM).start()

    def setVelocity(self, velocity):
        pulseWidth = self.translateVelocityToPulseWidth(velocity) + self.MIN_PULSE_VALUE
        if self.isInPWMRange(pulseWidth):
            self.currentVelocity = velocity
            self.currentPWM = pulseWidth
            self.pi.set_servo_pulsewidth(self.MOTOR_PIN, pulseWidth)

    def getVelocity(self):
        return self.currentVelocity

    def increaseVelocity(self, increment):
        incPulseWidth = self.translateVelocityToPulseWidth(increment)
        pulseWidth = self.currentPWM + incPulseWidth
        if self.isInPWMRange(pulseWidth):
            self.currentVelocity = self.currentVelocity + increment
            self.currentPWM = pulseWidth
            self.pi.set_servo_pulsewidth(self.MOTOR_PIN, pulseWidth)

    def decreaseVelocity(self, decrement):
        decPulseWidth = self.translateVelocityToPulseWidth(decrement)
        pulseWidth = self.currentPWM - decPulseWidth
        if self.isInPWMRange(pulseWidth):
            self.currentVelocity = self.currentVelocity - decrement
            self.currentPWM = pulseWidth
            self.pi.set_servo_pulsewidth(self.MOTOR_PIN, pulseWidth)

    def stop(self):
        self.currentPWM = self.MIN_PULSE_VALUE
        self.currentVelocity = self.MIN_VELOCITY
        self.isActive = False

    def translateVelocityToPulseWidth(self, velocity):
        pwmRange = self.MAX_PULSE_VALUE - self.MIN_PULSE_VALUE
        velocityRange = self.MAX_VELOCITY - self.MIN_VELOCITY
        distanceFromBase = velocity - self.MIN_VELOCITY
        percentageUsed = distanceFromBase/velocityRange
        pwmEquivalent = pwmRange*percentageUsed
        return pwmEquivalent

    def sendPWM(self):
        while self.isActive:
            self.pi.set_servo_pulsewidth(self.MOTOR_PIN, self.currentPWM)
            time.sleep(2)

    def isInPWMRange(self, pulseWidth):
        return pulseWidth >= self.MIN_PULSE_VALUE and pulseWidth <= self.MAX_PULSE_VALUE
