from src.main.python.control.driver.VesselDriver import VesselDriver
from src.main.python.control.Trip import Trip
from ObjectDetectorFactory import ObjectDetectorFactory
from VesselControlsFactory import VesselControlsFactory
from SingletonFactory import SingletonFactory


class VesselDriverFactory(SingletonFactory):
    def createInstance(self):
        return VesselDriver(Trip(), ObjectDetectorFactory().getInstance(), VesselControlsFactory().getInstance())
