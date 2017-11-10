from SingletonFactory import SingletonFactory
from src.main.python.control.VesselControls import VesselControls
from src.main.python.wrappers.servo.ServoController import ServoController
from src.main.python.wrappers.motor.MotorController import MotorController

class VesselControlsFactory(SingletonFactory):
    def createInstance(self):
        return VesselControls(MotorController(), ServoController())