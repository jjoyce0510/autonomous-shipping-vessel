import os
controller = ServoController.ServoController()

while True:
    inp = float(raw_input())
    controller.setAngle(inp)