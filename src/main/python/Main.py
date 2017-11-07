import os
from wrappers.servo.ServoController import ServoController
from wrappers.motor.MotorController import MotorController

# Tests the servo controller
servo = ServoController()
motor = MotorController()

while True:
    inp = float(raw_input())
    servo.setAngle(inp)
    motor.setVelocity(0.0)